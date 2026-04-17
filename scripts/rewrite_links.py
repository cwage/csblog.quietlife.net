#!/usr/bin/env python3
"""
Rewrite dead outbound links in blog posts to their closest Wayback Machine snapshot.

For each post:
1. Parse all outbound http/https links from the markdown
2. Query the Wayback Machine CDX API for the closest snapshot to the post date
3. Rewrite links that have snapshots; leave the rest alone

Usage:
  docker compose --profile scrape run --rm scraper python /app/rewrite_links.py
  docker compose --profile scrape run --rm scraper python /app/rewrite_links.py --dry-run
  docker compose --profile scrape run --rm scraper python /app/rewrite_links.py --limit 10
"""

import argparse
import glob
import os
import re
import sys
import time
from urllib.parse import quote, urlparse

import requests

POSTS_DIR = os.environ.get("OUTPUT_DIR", "/output")
CDX_API = "https://web.archive.org/cdx/search/cdx"
WEB_BASE = "https://web.archive.org/web"

REQUEST_DELAY = 0.5  # delay per CDX lookup (lightweight API)
MAX_RETRIES = 3
BACKOFF_BASE = 5

# Skip links that are already archive.org links or are internal/anchor links
SKIP_PATTERNS = [
    r"^https?://web\.archive\.org/",
    r"^#",
    r"^mailto:",
    r"^/",
]


def extract_post_date(content):
    """Extract the date from frontmatter."""
    m = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", content, re.MULTILINE)
    if m:
        return m.group(1).replace("-", "")
    return None


def find_links(content):
    """Find all markdown links in the post body (after frontmatter)."""
    # Split off frontmatter
    parts = content.split("---", 2)
    if len(parts) < 3:
        return []
    body = parts[2]

    # Match markdown links: [text](url)
    links = set()
    for m in re.finditer(r'\[([^\]]*)\]\(<?(https?://[^>)\s]+)>?\)', body):
        links.add(m.group(2))
    for m in re.finditer(r'\[([^\]]*)\]\((https?://[^)\s]+)\)', body):
        links.add(m.group(2))

    # Match bare autolinks: <http://...>
    for m in re.finditer(r'(?<!\()(?<!\[)<(https?://[^>]+)>', body):
        links.add(m.group(1))

    return list(links)


def should_skip(url):
    """Check if a URL should be skipped."""
    for pattern in SKIP_PATTERNS:
        if re.match(pattern, url):
            return True
    return False


def find_snapshot(url, post_date):
    """Query CDX API for the closest snapshot to the post date.

    Returns the timestamp if found, None otherwise.
    """
    params = {
        "url": url,
        "output": "json",
        "fl": "timestamp",
        "limit": 1,
        "closest": post_date,
        "sort": "closest",
        "filter": "statuscode:200",
    }

    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(CDX_API, params=params, timeout=15)
            if resp.status_code == 429:
                wait = BACKOFF_BASE * (2 ** attempt)
                time.sleep(wait)
                continue
            resp.raise_for_status()

            data = resp.json()
            if len(data) > 1:
                return data[1][0]  # first result's timestamp
            return None
        except (requests.ConnectionError, requests.Timeout):
            wait = BACKOFF_BASE * (2 ** attempt)
            if attempt < MAX_RETRIES - 1:
                time.sleep(wait)
            else:
                return None
        except (requests.RequestException, ValueError):
            return None

    return None


def rewrite_link(content, old_url, new_url):
    """Replace a URL in the post content, handling markdown link syntax."""
    # Replace in order: markdown links first, then bare autolinks
    content = content.replace(f"(<{old_url}>)", f"(<{new_url}>)")
    content = content.replace(f"({old_url})", f"({new_url})")
    content = content.replace(f"<{old_url}>", f"<{new_url}>")
    return content


def process_post(filepath, dry_run=False):
    """Process a single post file. Returns (links_found, links_rewritten)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    post_date = extract_post_date(content)
    if not post_date:
        return 0, 0

    links = find_links(content)
    if not links:
        return 0, 0

    found = len(links)
    rewritten = 0
    new_content = content

    for url in links:
        if should_skip(url):
            continue

        timestamp = find_snapshot(url, post_date)
        time.sleep(REQUEST_DELAY)

        if timestamp:
            archive_url = f"{WEB_BASE}/{timestamp}/{url}"
            if not dry_run:
                new_content = rewrite_link(new_content, url, archive_url)
            rewritten += 1
            print(f"    OK: {url[:80]}")
        # If no snapshot, leave the link as-is silently

    if not dry_run and new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return found, rewritten


def main():
    parser = argparse.ArgumentParser(description="Rewrite dead links to Wayback Machine URLs")
    parser.add_argument("--dry-run", action="store_true", help="Report without modifying files")
    parser.add_argument("--limit", type=int, help="Limit number of posts to process")
    parser.add_argument("--file", type=str, help="Process a single file")
    args = parser.parse_args()

    if args.file:
        files = [args.file]
    else:
        files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))

    if args.limit:
        files = files[:args.limit]

    print(f"Processing {len(files)} posts {'(dry run)' if args.dry_run else ''}...")

    total_links = 0
    total_rewritten = 0
    posts_modified = 0

    for i, filepath in enumerate(files):
        basename = os.path.basename(filepath)
        links = find_links(open(filepath, encoding="utf-8").read())
        outbound = [l for l in links if not should_skip(l)]

        if not outbound:
            continue

        print(f"  [{i+1}/{len(files)}] {basename} ({len(outbound)} links)")
        found, rewritten = process_post(filepath, dry_run=args.dry_run)
        total_links += found
        total_rewritten += rewritten
        if rewritten > 0:
            posts_modified += 1

    print(f"\nDone! {total_links} links found, {total_rewritten} rewritten across {posts_modified} posts")


if __name__ == "__main__":
    main()
