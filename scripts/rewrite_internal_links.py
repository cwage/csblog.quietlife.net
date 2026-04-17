#!/usr/bin/env python3
"""
Rewrite blog.centresource.com references to csblog.quietlife.net.

Three cases handled:
  1. Direct: http(s)://blog.centresource.com/<path>  ->  https://csblog.quietlife.net/<path>
  2. Wayback-wrapped from PR #1:
       https://web.archive.org/web/<ts>/http(s)://blog.centresource.com/<path>
         ->  https://csblog.quietlife.net/<path>
     (the content is canonical here now; no need to route through Wayback)
  3. Relative Wayback paths left by the scraper (host stripped at scrape time):
       /web/<ts>/http(s)://blog.centresource.com/<path>   (or csblog.quietlife.net after pass 1)
         ->  https://csblog.quietlife.net/<path>

Covers both post links and wp-content image/asset references.

Usage:
  python3 scripts/rewrite_internal_links.py
  python3 scripts/rewrite_internal_links.py --dry-run
"""

import argparse
import glob
import os
import re
import sys

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "_posts")

OLD_HOST = r"https?://blog\.centresource\.com"
NEW_BASE = "https://csblog.quietlife.net"

# Match a Wayback-wrapped blog.centresource.com URL. Capture the trailing path (if any).
WAYBACK_WRAPPED = re.compile(
    r"https://web\.archive\.org/web/\d+/" + OLD_HOST + r"(?P<path>[^\s)>\"']*)"
)

# Relative Wayback path (scraper left these with no host): /web/<ts>/http(s)://<host><path>
# The inner host may be blog.centresource.com (pre-rewrite) or csblog.quietlife.net (post-rewrite),
# so handle both so the script remains idempotent.
RELATIVE_WAYBACK = re.compile(
    r"/web/\d+/https?://(?:blog\.centresource\.com|csblog\.quietlife\.net)(?P<path>[^\s)>\"']*)"
)

# Match a direct blog.centresource.com URL. Capture the trailing path (if any).
DIRECT = re.compile(OLD_HOST + r"(?P<path>[^\s)>\"']*)")


def rewrite(content):
    """Return (new_content, wayback_count, direct_count, relative_count)."""
    wb_count = [0]
    dir_count = [0]
    rel_count = [0]

    def wb_sub(m):
        wb_count[0] += 1
        return NEW_BASE + m.group("path")

    def rel_sub(m):
        rel_count[0] += 1
        return NEW_BASE + m.group("path")

    def dir_sub(m):
        dir_count[0] += 1
        return NEW_BASE + m.group("path")

    # Order matters: fully-qualified Wayback wrappers and relative Wayback paths must be
    # collapsed before the plain DIRECT pass, or the inner host would be matched twice.
    new_content = WAYBACK_WRAPPED.sub(wb_sub, content)
    new_content = RELATIVE_WAYBACK.sub(rel_sub, new_content)
    new_content = DIRECT.sub(dir_sub, new_content)

    return new_content, wb_count[0], dir_count[0], rel_count[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))

    total_wb = 0
    total_direct = 0
    total_rel = 0
    files_changed = 0

    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        new_content, wb, direct, rel = rewrite(content)

        if wb == 0 and direct == 0 and rel == 0:
            continue

        total_wb += wb
        total_direct += direct
        total_rel += rel
        files_changed += 1

        basename = os.path.basename(filepath)
        print(f"  {basename}: {direct} direct, {wb} wayback-wrapped, {rel} relative-wayback")

        if not args.dry_run and new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

    print(
        f"\n{'[dry-run] ' if args.dry_run else ''}"
        f"Files changed: {files_changed} | "
        f"direct rewrites: {total_direct} | "
        f"wayback unwraps: {total_wb} | "
        f"relative-wayback collapses: {total_rel}"
    )


if __name__ == "__main__":
    main()
