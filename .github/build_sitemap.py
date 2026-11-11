#!/usr/bin/env python3
"""Rebuild sitemap.xml from the stories that are actually live.

A page is listed when it is the homepage, the archive, a story linked from
the homepage or archive, or a queue entry marked "published". Queue entries
still "pending" are never listed, even if their folder already exists, so
search engines cannot find a story before its release date.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://srinipresents.com'
# Live sections served from their own repos (e.g. sriniurs/nifty).
OTHER_REPOS = {'/nifty/'}
LINK = re.compile(r'href="(/[a-z0-9-]+/)"')


def main():
    queue = json.loads((ROOT / 'publishing-queue.json').read_text(encoding='utf-8'))
    pending = {e['path'] for e in queue['entries'] if e.get('status') != 'published'}
    lastmod = {e['path']: e['published_at'][:10]
               for e in queue['entries']
               if e.get('status') == 'published' and e.get('published_at')}

    paths = {'/', '/archive/'} | set(lastmod)
    for page in ('index.html', 'archive/index.html'):
        f = ROOT / page
        if f.exists():
            paths |= set(LINK.findall(f.read_text(encoding='utf-8')))

    live = sorted(p for p in paths
                  if p not in pending and (ROOT / p.strip('/') / 'index.html').exists()) + sorted(OTHER_REPOS)

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in live:
        mod = f'<lastmod>{lastmod[p]}</lastmod>' if p in lastmod else ''
        lines.append(f'  <url><loc>{BASE}{p}</loc>{mod}</url>')
    lines.append('</urlset>')
    (ROOT / 'sitemap.xml').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'sitemap.xml: {len(live)} URLs')


if __name__ == '__main__':
    main()
