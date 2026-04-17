#!/usr/bin/env python3
"""
Recover wp-content/uploads/* image + file assets from the Wayback Machine.

- Collects every unique wp-content/uploads URL referenced by _posts/*.md
- For each one, queries the Wayback CDX API for the closest snapshot
- Downloads the raw bytes via /web/<ts>id_/<url> and saves to ./wp-content/uploads/<path>
- Idempotent: files that already exist locally are skipped
- Thumbnail fallback: if a WordPress-sized variant like foo-300x200.jpg misses,
  retries with the unsized original (foo.jpg)

Usage:
  python3 scripts/recover_assets.py              # download everything
  python3 scripts/recover_assets.py --dry-run    # plan only
  python3 scripts/recover_assets.py --limit 10   # probe a few first
"""

import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
POSTS_DIR = os.path.join(ROOT, "_posts")
ASSETS_DIR = os.path.join(ROOT, "wp-content", "uploads")

# Any URL containing /wp-content/uploads/<path>
URL_RE = re.compile(r"[a-zA-Z]+://[^\s)>\"']+/wp-content/uploads/[^\s)>\"']+")

# WordPress auto-generates sized variants like foo-300x200.jpg, foo-1024x768.png
THUMB_RE = re.compile(r"-\d{2,4}x\d{2,4}(?=\.[A-Za-z0-9]{2,5}$)")

CDX = "http://web.archive.org/cdx/search/cdx"
WB = "https://web.archive.org/web"

UA = "centresource-archive-recovery/1.0 (cwage@quietlife.net)"


def collect_urls():
    urls = set()
    for p in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
        with open(p, encoding="utf-8") as f:
            for m in URL_RE.finditer(f.read()):
                urls.add(m.group(0))
    return sorted(urls)


def to_cdx_target(url):
    """Map the local canonical host back to the original for Wayback lookups."""
    return url.replace("https://csblog.quietlife.net", "http://blog.centresource.com")


def local_path(url):
    """Map a wp-content/uploads URL to its local filesystem path (URL-decoded)."""
    after = url.split("/wp-content/uploads/", 1)[1]
    after = urllib.parse.unquote(after)
    # Strip any query string just in case
    after = after.split("?", 1)[0]
    return os.path.join(ASSETS_DIR, after)


def cdx_lookup(url, retries=1, backoff=2.0, timeout=12):
    """Return ((timestamp, archived_url), None) for the closest snapshot, or (None, reason)."""
    q = urllib.parse.urlencode({"url": url, "output": "json", "limit": 1})
    full = f"{CDX}?{q}"
    last_err = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(full, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = json.loads(r.read().decode())
        except Exception as e:
            last_err = str(e)
            if attempt < retries:
                time.sleep(backoff * (attempt + 1))
                continue
            return None, last_err
        if len(data) < 2:
            return None, "no snapshot"
        row = data[1]
        # CDX columns: urlkey, timestamp, original, mimetype, statuscode, digest, length
        return (row[1], row[2]), None
    return None, last_err or "unknown"


def download(ts, original, dest):
    """Fetch raw bytes via the id_ flag and write to dest."""
    fetch_url = f"{WB}/{ts}id_/{original}"
    req = urllib.request.Request(fetch_url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


def thumb_base(url):
    """If url has a WordPress -NNNxMMM suffix, return the unsized equivalent; else None."""
    new = THUMB_RE.sub("", url)
    return new if new != url else None


def try_recover(url, dry_run):
    """Return ('ok', bytes) | ('exists', 0) | ('miss', reason) | ('err', reason)."""
    dest = local_path(url)
    if os.path.exists(dest):
        return "exists", 0

    target = to_cdx_target(url)
    result, err = cdx_lookup(target)

    if result is None:
        base = thumb_base(target)
        if base:
            result, err2 = cdx_lookup(base)
            if result is None:
                return "miss", f"{err}; thumb-base: {err2}"
            # Save the base snapshot as the thumbnail name (serving the full-size
            # file in place of the resized variant is fine for archival display)
        else:
            return "miss", err

    if dry_run:
        return "ok", 0

    ts, original = result
    try:
        size = download(ts, original, dest)
    except Exception as e:
        return "err", str(e)
    return "ok", size


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="only process first N URLs")
    ap.add_argument("--sleep", type=float, default=0.25, help="seconds between requests")
    args = ap.parse_args()

    urls = collect_urls()
    if args.limit:
        urls = urls[: args.limit]

    print(f"{len(urls)} unique wp-content URLs to process")
    print(f"Output dir: {ASSETS_DIR}")
    if args.dry_run:
        print("[dry-run]")
    print()

    counts = {"ok": 0, "exists": 0, "miss": 0, "err": 0}
    total_bytes = 0
    misses = []
    errors = []

    for i, url in enumerate(urls, 1):
        status, payload = try_recover(url, args.dry_run)
        counts[status] += 1
        if status == "ok":
            total_bytes += payload
            print(f"  [{i}/{len(urls)}] ok ({payload:>7} B) {url[-80:]}")
        elif status == "exists":
            print(f"  [{i}/{len(urls)}] skip (exists)  {url[-80:]}")
        elif status == "miss":
            misses.append((url, payload))
            print(f"  [{i}/{len(urls)}] MISS  {url[-80:]}")
        else:
            errors.append((url, payload))
            print(f"  [{i}/{len(urls)}] ERR   {url[-80:]}: {payload}")
        time.sleep(args.sleep)

    print()
    print(f"Summary: ok={counts['ok']} exists={counts['exists']} miss={counts['miss']} err={counts['err']}")
    print(f"Downloaded: {total_bytes/1024/1024:.2f} MiB")
    if misses:
        print(f"\nMisses ({len(misses)}):")
        for u, r in misses:
            print(f"  {u}  [{r}]")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for u, r in errors:
            print(f"  {u}  [{r}]")


if __name__ == "__main__":
    main()
