#!/usr/bin/env python3
"""Add Back and Home links to public HTML pages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {'assets', 'queue', 'preview', 's', 'stats', 'nifty', 'tools', 'pagefind'}
START, END = '<!-- sitenav:auto -->', '<!-- /sitenav:auto -->'
BLOCK = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)

BAR = START + """<link rel="stylesheet" href="/assets/reader-navigation.css">
<div class="sr-reader-slot"><nav class="sr-reader-bar" aria-label="Reader navigation">
<a class="sr-reader-back" href="__BACK_PATH__"><span aria-hidden="true">&larr;</span> Back</a>
<a href="/"><span aria-hidden="true">&#8962;</span> Home</a>
<a href="/search/"><span aria-hidden="true"><span class="sr-search-icon"></span></span> Search</a>
</nav></div>
<script defer src="/assets/reader-navigation.js"></script>
""" + END + '\n'


def back_path(relative):
    directories = relative.parts[:-1]
    if len(directories) == 2 and directories[0] == 'health' and re.match(r'^\d{2}-', directories[1]):
        return '/health/general/'
    if len(directories) > 1:
        return '/' + '/'.join(directories[:-1]) + '/'
    if directories == ('archive',) and relative.name != 'index.html':
        return '/archive/'
    if not directories or directories[0] in {'about', 'archive', 'bhakti', 'gods', 'health', 'ortho'}:
        return '/'
    return '/archive/'


def process(path):
    with open(path, encoding='utf-8', newline='') as fh:
        page = fh.read()
    if re.search(r'(?i)<meta[^>]+http-equiv=["\']?refresh', page):
        return False                       # redirect stub
    clean = BLOCK.sub('', page)
    if path.relative_to(ROOT).parts[0] == 'health':
        clean = re.sub(r'<a class="series-home"[^>]*>[^<]*</a>', '', clean)
    m = re.search(r'(?is)<body\b[^>]*>', clean)
    if not m:
        return False
    new = clean[:m.end()] + '\n' + BAR.replace('__BACK_PATH__', back_path(path.relative_to(ROOT))) + clean[m.end():].lstrip('\n')
    if new == page:
        return False
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(new)
    return True


def main():
    changed = []
    for page in sorted(ROOT.rglob('*.html')):
        relative = page.relative_to(ROOT)
        if any(part.startswith('.') or part in SKIP for part in relative.parts[:-1]):
            continue
        if process(page):
            changed.append(relative)
    print(f'site_nav: updated {len(changed)} page(s)')
    import brand_logo
    brand_logo.main()


if __name__ == '__main__':
    main()
