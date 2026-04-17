# blog.centresource.com

Restored archive of the CentreSource company blog (2005-2017), scraped from the Wayback Machine and served as a Jekyll site with the original 2005-era theme.

## Architecture

- **Jekyll 4.4** static site with `jekyll-commonmark` (not the ghpages variant - it crashes on edge-case header slugs)
- **Dockerized**: `docker-compose.yml` has a `jekyll` service and a `scraper` service (profile: `scrape`)
- **Scraper**: Python script (`scripts/scrape.py`) that pulls posts from the Wayback Machine CDX API, handles three WordPress theme eras (early/mid/late), and outputs Jekyll-compatible markdown with frontmatter
- Posts live in `_posts/` as `YYYY-MM-DD-slug.md`

## Running

- `./dev.sh` or `docker compose up --build` — Jekyll dev server on :4000
- `docker compose --profile scrape run --rm scraper` — run the scraper (skips already-downloaded posts)
- `docker compose --profile scrape run --rm scraper --dry-run` — list posts without downloading

## Known issues / Smart typography

The `commonmarker` gem crashes on certain Unicode characters (en-dashes, smart quotes). The scraper cleans these in content but older downloads may need a fix-up pass. Titles with literal `"` inside `"` delimiters also break YAML frontmatter — the scraper escapes these, but check for YAML errors after bulk imports.

## TODOs

- [ ] **Rewrite dead hyperlinks to Wayback Machine URLs**: Most outbound links in posts (especially 2005-2010 era) point to long-dead URLs. After scraping is complete, write a script to:
  1. Parse each post for outbound links
  2. Query the Wayback Machine CDX API for the closest snapshot to the post's publication date
  3. Rewrite `href` values to `https://web.archive.org/web/{timestamp}/{original_url}`
  4. Leave links that still resolve (200) untouched, or flag them for review
- [ ] **Run smart-typography fix-up** on all posts after scraping completes (the scraper was updated mid-run, so earlier downloads may still have raw Unicode smart quotes/dashes)
- [ ] **Rebuild scraper image** with latest `scrape.py` before any future scrape runs
- [ ] **Review empty-content posts** — some posts may have scraped with no body content due to theme detection mismatches; grep for posts with very small file sizes
- [ ] **Audit mid-era (2009-2013) extraction** — this theme era had the most varied HTML structure; spot-check a sample of posts for missing content or metadata
