#!/usr/bin/env python3
"""Add search and sharing tags to every story page, filling only what is missing.

For each story folder's index.html this adds, inside one marked block before
</head>: a meta description, a canonical link, Open Graph and Twitter tags,
and schema.org Article data (author, headline, image, publish date).
Tags a page already has are left alone. Re-running replaces only the marked
block, so it is safe to run on every publish.

Description source, in order: the page's own description, its og:description,
its card text in publishing-queue.json, then the first long paragraph after
the headline.
"""
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://sriniurs.github.io'
SKIP = {'archive', 'assets', 'queue', 'preview', 's', 'stats'}
# Faceless by choice: pen name and profession only, no full name or hospital.
AUTHOR = {'@type': 'Person', 'name': 'Dr. Srini', 'honorificPrefix': 'Dr.',
          'jobTitle': 'Orthopaedic surgeon', 'url': BASE + '/about/'}
START, END = '<!-- seo:auto -->', '<!-- /seo:auto -->'
BLOCK = re.compile(re.escape(START) + r'.*?' + re.escape(END), re.S)


class Head(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.meta, self.links, self.title, self._in_title = {}, {}, '', False

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or '') for k, v in attrs}
        if tag == 'meta':
            key = (a.get('name') or a.get('property') or a.get('http-equiv') or '').lower()
            if key:
                self.meta[key] = a.get('content', '')
        elif tag == 'link' and a.get('rel'):
            self.links[a['rel'].lower()] = a.get('href', '')
        elif tag == 'title':
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def text_of(fragment):
    fragment = re.sub(r'(?is)<(script|style|svg)\b.*?</\1>', ' ', fragment)
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', fragment)).split())


def clip(text, limit=160):
    if len(text) <= limit:
        return text
    cut = text[:limit]
    end = max(cut.rfind('. '), cut.rfind('? '), cut.rfind('! '))
    if end >= 80:
        return cut[:end + 1]
    return cut[:cut.rfind(' ')].rstrip(',;:') + '…'


def standfirst(body):
    after = re.split(r'(?is)</h1>', body, maxsplit=1)
    for p in re.findall(r'(?is)<p\b[^>]*>(.*?)</p>', after[-1]):
        t = text_of(p)
        if len(t) >= 60:
            return t
    return ''


def attr(v):
    return html.escape(v, quote=True)


def process(slug, cards, published):
    path = ROOT / slug / 'index.html'
    with open(path, encoding='utf-8', newline='') as fh:   # keep CRLF files as CRLF
        page = fh.read()
    if '</head>' not in page:
        return False
    head, body = page.split('</head>', 1)
    clean_head = BLOCK.sub('', head)
    h = Head()
    h.feed(clean_head)
    if 'refresh' in h.meta:          # redirect stub, not a story
        return False

    url = f'{BASE}/{slug}/'
    raw_title = h.title
    if not raw_title.strip():        # some pages put <title> just after </head>
        m = (re.search(r'(?is)<title[^>]*>(.*?)</title>', page)
             or re.search(r'(?is)<h1\b[^>]*>(.*?)</h1>', body))
        raw_title = text_of(m.group(1)) if m else ''
    title = re.sub(r'\s*[—|-]\s*srini\.presents\s*$', '', ' '.join(html.unescape(raw_title).split()))
    card = re.search(r'(?is)<p>(.*?)</p>', cards.get(slug, ''))
    desc = (h.meta.get('description') or h.meta.get('og:description')
            or (text_of(card.group(1)) if card else '') or standfirst(body))
    desc = clip(' '.join(html.unescape(desc).split()))
    image = f'{BASE}/{slug}/og.png' if (ROOT / slug / 'og.png').exists() else f'{BASE}/og.png'

    tags = []
    def meta(key, value, prop=False):
        if key not in h.meta and value:
            kind = 'property' if prop else 'name'
            tags.append(f'<meta {kind}="{key}" content="{attr(value)}">')

    meta('description', desc)
    if 'canonical' not in h.links:
        tags.append(f'<link rel="canonical" href="{url}">')
    meta('og:title', title, True)
    meta('og:description', desc, True)
    meta('og:url', url, True)
    meta('og:type', 'article', True)
    meta('og:image', image, True)
    meta('og:site_name', 'srini.presents', True)
    meta('twitter:card', 'summary_large_image')
    if 'application/ld+json' not in clean_head:
        data = {'@context': 'https://schema.org', '@type': 'Article',
                'headline': title, 'description': desc, 'url': url,
                'mainEntityOfPage': url,
                'image': h.meta.get('og:image') or image,
                'author': AUTHOR,
                'publisher': {'@type': 'Organization', 'name': 'srini.presents',
                              'url': BASE + '/'},
                'inLanguage': 'en-IN'}
        if slug in published:
            data['datePublished'] = published[slug]
        ld = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
        tags.append(f'<script type="application/ld+json">{ld}</script>')

    block = (START + ''.join(tags) + END) if tags else ''
    new = clean_head + block + '</head>' + body
    if new != page:
        with open(path, 'w', encoding='utf-8', newline='') as fh:
            fh.write(new)
        return True
    return False


def main():
    queue = json.loads((ROOT / 'publishing-queue.json').read_text(encoding='utf-8'))
    cards = {e['path'].strip('/'): e.get('card_html', '') for e in queue['entries']}
    published = {e['path'].strip('/'): e['published_at']
                 for e in queue['entries']
                 if e.get('status') == 'published' and e.get('published_at')}
    changed = []
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        if d.name.startswith('.') or d.name in SKIP or not (d / 'index.html').exists():
            continue
        if process(d.name, cards, published):
            changed.append(d.name)
    print(f'seo_meta: updated {len(changed)} page(s)' + (': ' + ', '.join(changed) if changed else ''))


if __name__ == '__main__':
    sys.exit(main())
