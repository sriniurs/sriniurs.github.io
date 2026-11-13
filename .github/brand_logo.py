#!/usr/bin/env python3
"""Put the srini.presents logo (assets/brand/logo.png) on every page.

- Story covers: the first byline inside <header class="cover..."> becomes the
  logo tile (keeping the "for curious grown-ups" tagline when present).
- Home, Past stories and About: the header wordmark becomes the logo.
Idempotent: pages already carrying data-brand-logo are left alone.
Called from site_nav.py, so every publish/unpack run applies it.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {'assets', 'queue', 'preview', 's', 'stats', 'nifty-chronicles', 'nifty-comics', 'markets', 'funds', 'nifty'}
SRC = '/assets/brand/logo.png'
CSS = ('<style id="brand-logo">'
       '.brand{display:inline-flex;flex-direction:column;align-items:flex-start;gap:6px;margin:0 0 14px}'
       '.brand img{display:block;width:210px;max-width:70vw;height:auto;background:#ebeae0;border:3px solid #151515;'
       'border-radius:14px;padding:6px 10px;box-shadow:4px 4px 0 #151515}'
       '.brand .tagline{margin:0!important}'
       ''
       '.wordmark img.brand-mark{display:block;height:92px;width:auto;margin:-6px 0}@media(max-width:640px){.brand img{width:180px}.wordmark img.brand-mark{height:66px;margin:-4px 0}}'
       '</style>')
IMG = f'<img data-brand-logo src="{SRC}" alt="srini.presents" width="420" height="192">'
BYLINE = re.compile(r'<(p|div)\s+class=["\'](?:byline|by)["\'][^>]*>(.*?)</\1>', re.S)
LOOSE = re.compile(r'<(p)\b[^>]*>(\s*(?:srini\.presents|Srini presents)\s*)</p>')
TAG = re.compile(r'<span\s+class=["\']tagline["\'][^>]*>(.*?)</span>', re.S)
WORDMARK = re.compile(r'(<a\s+class=["\']wordmark["\'][^>]*>)(.*?)(</a>)', re.S)


def brand_cover(page):
    m = re.search(r'<header\s+class=["\']cover[^>]*>', page) or re.search(r'<header>', page)
    if not m:
        return page
    end = page.find('</header>', m.end())
    if end < 0:
        return page
    seg = page[m.end():end]
    b = BYLINE.search(seg) or LOOSE.search(seg)
    if not b:
        return page
    t = TAG.search(b.group(2))
    tag = f'<span class="tagline">{t.group(1)}</span>' if t else ''
    new = f'<div class="brand">{IMG}{tag}</div>'
    seg = seg[:b.start()] + new + seg[b.end():]
    return page[:m.end()] + seg + page[end:]


def brand_wordmark(page):
    img = f'<img data-brand-logo class="brand-mark" src="/assets/brand/logo-clear.png" alt="srini.presents" width="560" height="257">'
    return WORDMARK.sub(lambda m: m.group(1) + img + m.group(3), page, count=1)


DAYS = r'(?:MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY)'
DATEBOX = re.compile(r'<(span|p|div)\s+class=["\'](?:daytag|day|edition|tag|sample)["\'][^>]*>([^<]*)</\1>')


def strip_dates(page):
    """Remove weekday/date boxes and the black .sample label chip from the cover (Srini's rule, 13 Nov 2026)."""
    m = re.search(r'<header\b[^>]*>', page)
    if not m:
        return page
    end = page.find('</header>', m.end())
    if end < 0:
        return page
    seg = page[m.end():end]

    def kill(e):
        txt = e.group(2).strip().upper()
        cls = re.search(r'class=["\']([^"\']+)', e.group(0)).group(1)
        if cls in ('daytag', 'day', 'edition', 'sample'):
            return ''
        if re.match(DAYS, txt):          # sample/tag that starts with a weekday
            return ''
        return e.group(0)
    seg = DATEBOX.sub(kill, seg)
    return page[:m.end()] + seg + page[end:]


def process(path):
    page = path.read_text(encoding='utf-8')
    if re.search(r'(?i)http-equiv=["\']?refresh', page):
        return False
    new = strip_dates(page)
    if 'data-brand-logo' not in new:
        new = brand_wordmark(brand_cover(new))
    if new == page:
        return False
    if 'data-brand-logo' in new and '<style id="brand-logo">' not in new:
        new = new.replace('</head>', CSS + '</head>', 1)
    path.write_text(new, encoding='utf-8')
    return True


def main():
    pages = [ROOT / 'index.html', ROOT / 'archive' / 'index.html']
    pages += sorted((ROOT / 'archive').glob('20*.html'))
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        if d.name.startswith('.') or d.name in SKIP or d.name == 'archive':
            continue
        if (d / 'index.html').exists():
            pages.append(d / 'index.html')
    n = sum(process(p) for p in pages if p.exists())
    print(f'brand_logo: updated {n} page(s)')


if __name__ == '__main__':
    main()
