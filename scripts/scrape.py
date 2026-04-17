#!/usr/bin/env python3
"""
Scrape blog.centresource.com posts from the Wayback Machine
and output them as Jekyll-compatible markdown files.

Usage:
  docker compose --profile scrape run --rm scraper
  docker compose --profile scrape run --rm scraper --limit 10
  docker compose --profile scrape run --rm scraper --year 2005
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import unquote

import html2text
import requests
from bs4 import BeautifulSoup

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))
CDX_API = "https://web.archive.org/cdx/search/cdx"
WEB_BASE = "https://web.archive.org/web"

# Rate limiting - be polite to the Wayback Machine
REQUEST_DELAY = 2.0  # seconds between requests
MAX_RETRIES = 5
BACKOFF_BASE = 10  # seconds; doubles each retry
CONSECUTIVE_FAIL_PAUSE = 60  # long pause after N consecutive failures
CONSECUTIVE_FAIL_THRESHOLD = 3


def get_post_urls(year=None):
    """Fetch all blog post URLs from the CDX API."""
    params = {
        "url": "blog.centresource.com/*",
        "output": "json",
        "fl": "timestamp,original,statuscode,mimetype",
        "filter": ["statuscode:200", "mimetype:text/html"],
        "collapse": "urlkey",
    }

    print("Querying Wayback Machine CDX API...")
    resp = requests.get(CDX_API, params=params, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    rows = data[1:]  # skip header

    # Filter to blog post URLs (date-based paths like /2005/04/20/slug/)
    posts = []
    for row in rows:
        timestamp, url, status, mime = row
        if not re.search(r"/\d{4}/\d{2}/\d{2}/", url):
            continue
        # Skip pagination, comments, feeds, trackbacks
        if any(x in url for x in ["comment-page", "/feed/", "/page/", "/trackback/", "#"]):
            continue
        # Skip multi-page posts (e.g. /slug/2, /slug/3/)
        if re.search(r"/\d{4}/\d{2}/\d{2}/[^/]+/\d+/?$", url):
            continue
        if year and f"/{year}/" not in url:
            continue
        posts.append((timestamp, url))

    # Deduplicate by URL (keep first/earliest timestamp)
    seen = set()
    unique = []
    for ts, url in posts:
        # Normalize URL
        normalized = re.sub(r":80/", "/", url)
        normalized = normalized.rstrip("/").rstrip("?")
        if normalized not in seen:
            seen.add(normalized)
            unique.append((ts, url))

    print(f"Found {len(unique)} unique blog posts")
    return unique


def extract_post_early_era(soup):
    """Extract content from the early WordPress theme (2005-2009ish).

    Structure: div.storycontent, h3.storytitle, div.meta, h2.date
    """
    content_div = soup.find("div", class_="storycontent")
    title_tag = soup.find("h3", class_="storytitle")
    date_tag = soup.find("h2", class_="date")
    meta_tag = soup.find("div", class_="meta")

    title = title_tag.get_text(strip=True) if title_tag else None
    date_str = date_tag.get_text(strip=True) if date_tag else None

    # Extract categories from meta
    categories = []
    author = None
    if meta_tag:
        cat_links = meta_tag.find_all("a", rel="category tag")
        categories = [a.get_text(strip=True) for a in cat_links]
        meta_text = meta_tag.get_text()
        author_match = re.search(r"—\s*(\w+)\s*@", meta_text)
        if author_match:
            author = author_match.group(1)

    return title, date_str, author, categories, content_div


def extract_post_mid_era(soup):
    """Extract content from the mid-era theme (2009-2013ish).

    Structure: div.body, h2 with post title link, div.author-name
    """
    # Title is in an h2 inside the content area
    title = None
    title_tag = soup.find("h2")
    content_area = soup.find("div", id="single-post")
    if content_area:
        h2 = content_area.find("h2")
        if h2:
            link = h2.find("a")
            title = link.get_text(strip=True) if link else h2.get_text(strip=True)

    content_div = soup.find("div", class_="body")

    # Author
    author = None
    author_div = soup.find("div", class_="author-name")
    if author_div:
        author = author_div.get_text(strip=True)

    # Categories from meta-info
    categories = []
    meta_div = soup.find("div", class_="meta-info")
    if meta_div:
        cat_links = meta_div.find_all("a", rel="category tag")
        categories = [a.get_text(strip=True) for a in cat_links]

    # Date from cal-date
    date_str = None
    cal_div = soup.find("div", class_=re.compile(r"cal-date"))
    if cal_div:
        date_str = cal_div.get_text(strip=True)

    return title, date_str, author, categories, content_div


def extract_post_late_era(soup):
    """Extract content from the late-era theme (2013-2017).

    Structure: article tag, div.entry-content, h1.post-title or h1
    """
    content_div = soup.find("div", class_="entry-content")

    # Title - try multiple locations
    title = None
    for selector in [
        lambda: soup.find("h1", class_="post-title"),
        lambda: soup.find("div", class_="post-hero-copy-wrap") and soup.find("div", class_="post-hero-copy-wrap").find("h1"),
        lambda: soup.find("header", class_="entry-header") and soup.find("header", class_="entry-header").find("h1"),
    ]:
        tag = selector()
        if tag:
            title = tag.get_text(strip=True)
            break

    # Author
    author = None
    for cls in ["byline", "post-subtitle"]:
        byline = soup.find("div", class_=cls)
        if byline:
            link = byline.find("a", rel="author")
            if link:
                author = link.get_text(strip=True)
                break

    # Categories
    categories = []
    entry_meta = soup.find("div", class_="entry-meta")
    if entry_meta:
        cat_links = entry_meta.find_all("a", rel="category tag")
        categories = [a.get_text(strip=True) for a in cat_links]

    # Date
    date_str = None
    if entry_meta:
        meta_text = entry_meta.get_text(strip=True)
        date_match = re.search(r"(\w+ \d{1,2}, \d{4})", meta_text)
        if date_match:
            date_str = date_match.group(1)

    return title, date_str, author, categories, content_div


def extract_post(html, url):
    """Detect which theme era and extract content accordingly."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove Wayback Machine toolbar/injection
    for tag in soup.find_all("div", id="wm-ipp-base"):
        tag.decompose()
    for tag in soup.find_all("div", id="wm-ipp"):
        tag.decompose()
    for tag in soup.find_all(id="donato"):
        tag.decompose()
    for tag in soup.find_all(id="playback"):
        tag.decompose()

    # Detect era by HTML structure
    if soup.find("div", class_="storycontent"):
        title, date_str, author, categories, content_div = extract_post_early_era(soup)
        era = "early"
    elif soup.find("div", class_="entry-content"):
        title, date_str, author, categories, content_div = extract_post_late_era(soup)
        era = "late"
    elif soup.find("div", class_="body") and soup.find("div", id="single-post"):
        title, date_str, author, categories, content_div = extract_post_mid_era(soup)
        era = "mid"
    else:
        # Fallback - try to get whatever we can
        title = None
        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.get_text(strip=True)
            # Clean up title suffixes
            for sep in [" - ", " | ", " &raquo; "]:
                if sep in title:
                    title = title.split(sep)[0].strip()
                    # For early titles like "CentreSource: Blog » Title"
                    if ":" in title:
                        parts = title.split(":")
                        if len(parts) > 1:
                            title = parts[-1].strip()

        content_div = soup.find("div", id="content")
        date_str = None
        author = None
        categories = []
        era = "unknown"

    # Fallback: extract title from <title> tag if we didn't get one
    if not title:
        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.get_text(strip=True)
            for sep in [" - ", " | ", " &raquo; "]:
                if sep in title:
                    title = title.split(sep)[-1].strip()
                    break

    # Fallback: extract title from URL
    if not title:
        slug = url.rstrip("/").split("/")[-1]
        title = slug.replace("-", " ").title()

    return title, date_str, author, categories, content_div, era


def html_to_markdown(content_div):
    """Convert an HTML content div to clean markdown."""
    if not content_div:
        return ""

    # Clean up Wayback Machine URLs in links
    for tag in content_div.find_all(["a", "img"]):
        for attr in ["href", "src"]:
            val = tag.get(attr)
            if val and "web.archive.org" in val:
                # Extract original URL from wayback URL
                match = re.search(r"https?://web\.archive\.org/web/\d+(?:im_|cs_|js_|fw_|if_)?/(.+)", val)
                if match:
                    tag[attr] = match.group(1)

    h = html2text.HTML2Text()
    h.body_width = 0  # Don't wrap lines
    h.protect_links = True
    h.wrap_links = False
    h.unicode_snob = True

    md = h.handle(str(content_div)).strip()

    # Replace smart typography that breaks commonmarker
    md = md.replace("\u2013", "-")   # en-dash
    md = md.replace("\u2014", "--")  # em-dash
    md = md.replace("\u2018", "'")   # left single quote
    md = md.replace("\u2019", "'")   # right single quote
    md = md.replace("\u201C", '"')   # left double quote
    md = md.replace("\u201D", '"')   # right double quote
    md = md.replace("\u2033", '"')   # double prime
    md = md.replace("\u2032", "'")   # prime
    md = md.replace("\u2026", "...")  # ellipsis
    md = md.replace("\u00a0", " ")   # non-breaking space

    return md


def parse_date_from_url(url):
    """Extract date from the URL path like /2005/04/20/slug/."""
    match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None


def slug_from_url(url):
    """Extract the slug from the URL."""
    # Remove trailing slash and query params
    clean = url.rstrip("/").split("?")[0]
    slug = clean.split("/")[-1]
    # Clean up the slug
    slug = re.sub(r"[^a-z0-9-]", "", slug.lower())
    return slug


def write_post(date, slug, title, author, categories, content_md):
    """Write a Jekyll-compatible markdown file."""
    filename = f"{date}-{slug}.md"
    filepath = OUTPUT_DIR / filename

    # Build frontmatter
    fm = ["---"]
    fm.append("layout: post")
    # Clean smart typography in title and escape quotes
    safe_title = title
    for old, new in [
        ("\u2013", "-"), ("\u2014", "--"),
        ("\u2018", "'"), ("\u2019", "'"),
        ("\u201C", '"'), ("\u201D", '"'),
        ("\u2033", '"'), ("\u2032", "'"),
        ("\u2026", "..."), ("\u00a0", " "),
    ]:
        safe_title = safe_title.replace(old, new)
    safe_title = safe_title.replace('"', '\\"')
    fm.append(f'title: "{safe_title}"')
    fm.append(f"date: {date}")
    if author:
        fm.append(f"author: {author}")
    if categories:
        fm.append(f"categories: [{', '.join(categories)}]")
    fm.append("---")
    fm.append("")

    frontmatter = "\n".join(fm)

    filepath.write_text(frontmatter + content_md + "\n", encoding="utf-8")
    return filepath


def fetch_post(timestamp, url):
    """Fetch a single post from the Wayback Machine with retry + backoff."""
    wayback_url = f"{WEB_BASE}/{timestamp}/{url}"

    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(wayback_url, timeout=30)
            if resp.status_code == 429:
                wait = BACKOFF_BASE * (2 ** attempt)
                print(f"RATE LIMITED, waiting {wait}s ...", end=" ", flush=True)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.text
        except (requests.ConnectionError, requests.Timeout) as e:
            wait = BACKOFF_BASE * (2 ** attempt)
            if attempt < MAX_RETRIES - 1:
                print(f"RETRY {attempt+1} in {wait}s ...", end=" ", flush=True)
                time.sleep(wait)
            else:
                print(f"FAILED after {MAX_RETRIES} retries", end=" ", flush=True)
                return None
        except requests.RequestException as e:
            print(f"ERROR: {e}", end=" ", flush=True)
            return None
    return None


def main():
    parser = argparse.ArgumentParser(description="Scrape blog.centresource.com from Wayback Machine")
    parser.add_argument("--limit", type=int, help="Limit number of posts to scrape")
    parser.add_argument("--year", type=str, help="Only scrape posts from this year")
    parser.add_argument("--dry-run", action="store_true", help="List posts without downloading")
    parser.add_argument("--skip-existing", action="store_true", default=True, help="Skip posts already downloaded (default)")
    parser.add_argument("--delay", type=float, default=REQUEST_DELAY, help=f"Delay between requests in seconds (default: {REQUEST_DELAY})")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    posts = get_post_urls(year=args.year)

    if args.limit:
        posts = posts[:args.limit]

    if args.dry_run:
        for ts, url in posts:
            date = parse_date_from_url(url)
            slug = slug_from_url(url)
            print(f"  {date} {slug}: {url}")
        print(f"\nTotal: {len(posts)} posts")
        return

    success = 0
    skipped = 0
    failed = 0
    consecutive_fails = 0

    for i, (timestamp, url) in enumerate(posts):
        date = parse_date_from_url(url)
        slug = slug_from_url(url)

        if not date or not slug:
            print(f"  [{i+1}/{len(posts)}] SKIP (bad URL): {url}")
            failed += 1
            continue

        filename = f"{date}-{slug}.md"

        if args.skip_existing and (OUTPUT_DIR / filename).exists():
            skipped += 1
            continue

        print(f"  [{i+1}/{len(posts)}] {filename} ...", end=" ", flush=True)

        html = fetch_post(timestamp, url)
        if not html:
            failed += 1
            consecutive_fails += 1
            print()
            # If we're getting hammered, take a long break
            if consecutive_fails >= CONSECUTIVE_FAIL_THRESHOLD:
                pause = CONSECUTIVE_FAIL_PAUSE * (consecutive_fails // CONSECUTIVE_FAIL_THRESHOLD)
                pause = min(pause, 300)  # cap at 5 min
                print(f"  ** {consecutive_fails} consecutive failures, pausing {pause}s **", flush=True)
                time.sleep(pause)
            continue

        consecutive_fails = 0  # reset on success

        title, date_str, author, categories, content_div, era = extract_post(html, url)
        content_md = html_to_markdown(content_div)

        if not content_md.strip():
            print(f"WARN: empty content ({era} era)")
        else:
            print(f"OK ({era}, {len(content_md)} chars)")

        write_post(date, slug, title, author, categories, content_md)
        success += 1

        # Be polite to the Wayback Machine
        if i < len(posts) - 1:
            time.sleep(args.delay)

    print(f"\nDone! {success} scraped, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
