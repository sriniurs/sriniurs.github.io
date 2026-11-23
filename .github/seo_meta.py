#!/usr/bin/env python3
"""Build static sharing metadata and cover images for published story HTML."""
import html
import json
import re
import struct
from contextlib import ExitStack
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://srinipresents.com'
SKIP = {'about', 'archive', 'assets', 'bhakti', 'devi', 'gods', 'health', 'ortho', 'pagefind', 'preview', 'queue', 's', 'search', 'stats'}
# Discreet by choice: pen name and city only.
AUTHOR = {'@type': 'Person', 'name': 'Dr. Srini',
          'homeLocation': {'@type': 'Place', 'name': 'Mysuru'}, 'url': BASE + '/about/'}
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
                self.meta.setdefault(key, a.get('content', ''))
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


META_TAG = re.compile(r"""<meta\b(?:[^>"']|"[^"]*"|'[^']*')*>""", re.I)
HEAD_END = re.compile(r'</head\s*>', re.I)
SVG = re.compile(r'<svg\b[^>]*>.*?</svg\s*>', re.I | re.S)
ANCHOR = re.compile(r"""<a\b[^>]*\bhref=["']([^"']+)["'][^>]*>(.*?)</a>""", re.I | re.S)
OWN_TAGS = {'og:title', 'og:description', 'og:type', 'og:url', 'og:site_name',
            'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image'}
WIDTH, HEIGHT = 1200, 630


def strip_sharing(head):
    def replace(match):
        tag = Head()
        tag.feed(match[0])
        if any(key in OWN_TAGS or key == 'og:image' or key.startswith('og:image:')
               for key in tag.meta):
            return ''
        return match[0]
    return META_TAG.sub(replace, head)


def route(path):
    relative = path.relative_to(ROOT)
    return '/' + (relative.parent.as_posix() + '/' if path.name == 'index.html'
                  else relative.as_posix())


def file_for_url(url, base):
    parts = urlsplit(urljoin(base, url))
    if parts.netloc != urlsplit(BASE).netloc:
        return None
    path = ROOT / unquote(parts.path).lstrip('/')
    if not path.resolve().is_relative_to(ROOT):
        return None
    return path / 'index.html' if parts.path.endswith('/') else path


def story_pages():
    for path in ROOT.glob('*/index.html'):
        if path.parent.name not in SKIP and not path.parent.name.startswith('.'):
            yield path
    for path in (ROOT / 'archive').glob('*.html'):
        if path.name != 'index.html':
            yield path
    yield from (ROOT / 'health').glob('[0-9][0-9]-*/index.html')
    yield from (ROOT / 'health' / 'ortho').glob('*/*/index.html')
    yield from (ROOT / 'bhakti').glob('*/*/index.html')
    yield from (ROOT / 'bhakti').glob('*/*/*/index.html')


def card_art():
    indexes = [ROOT / 'index.html', ROOT / 'archive/index.html',
               ROOT / 'health/general/index.html']
    indexes.extend((ROOT / 'health/ortho').glob('*/index.html'))
    art = {}
    for index in indexes:
        if not index.is_file():
            continue
        base = BASE + ('/' if index.parent == ROOT else route(index))
        for href, content in ANCHOR.findall(index.read_text(encoding='utf-8')):
            svg = SVG.search(content)
            target = file_for_url(href, base)
            if svg and target and target.is_file() and 'viewBox' in svg[0]:
                art.setdefault(target, svg[0])
    return art


def article_art(body):
    return next((svg[0] for svg in SVG.finditer(body)
                 if re.match(r"""<svg\b[^>]*\bclass=["'](?:ill|spot)\b""", svg[0], re.I)
                 and 'viewBox' in svg[0]), '')


def read_page(path):
    with path.open(encoding='utf-8', newline='') as stream:
        return stream.read()


def save_page(path, old, new):
    if new == old:
        return False
    with path.open('w', encoding='utf-8', newline='') as stream:
        stream.write(new)
    return True


def share_tags(title, desc, url, image, alt):
    image_url = BASE + '/' + image.relative_to(ROOT).as_posix()
    values = [
        ('og:title', title), ('og:description', desc), ('og:type', 'article'),
        ('og:url', url), ('og:site_name', 'srini.presents'), ('og:image', image_url),
        ('og:image:type', 'image/png' if image.suffix == '.png' else 'image/jpeg'),
    ]
    if image.suffix == '.png':
        with image.open('rb') as stream:
            header = stream.read(24)
        if header.startswith(b'\x89PNG\r\n\x1a\n') and len(header) == 24:
            width, height = struct.unpack('>II', header[16:24])
            values.extend([('og:image:width', str(width)), ('og:image:height', str(height))])
    elif image.name == 'og-share.jpg' or image.name.endswith('-og-share.jpg'):
        values.extend([('og:image:width', str(WIDTH)), ('og:image:height', str(HEIGHT))])
    values.append(('og:image:alt', alt))
    tags = [f'<meta property="{key}" content="{attr(value)}">' for key, value in values]
    tags.extend(f'<meta name="twitter:{key}" content="{attr(value)}">' for key, value in [
        ('card', 'summary_large_image'), ('title', title), ('description', desc), ('image', image_url),
    ])
    return tags, image_url


class CoverRenderer:
    def __init__(self, stack):
        self.stack = stack
        self.page = None

    def render(self, path, title, art):
        if self.page is None:
            from playwright.sync_api import sync_playwright
            playwright = self.stack.enter_context(sync_playwright())
            browser = playwright.chromium.launch(channel='chrome')
            self.stack.callback(browser.close)
            self.page = browser.new_page(viewport={'width': WIDTH, 'height': HEIGHT})
            self.page.route('**/*', lambda request: request.abort())

        # Reuse the article's published illustration. CSS keeps the complete
        # artwork inside its panel, including thumbnail-sized social previews.
        figure = f'<div class="art">{art}</div>' if art else ''
        size = 52 if len(title) > 75 else 62
        self.page.set_content(f"""<!doctype html><meta charset="utf-8"><style>
*{{box-sizing:border-box}}body{{margin:0;background:#fff9e7;color:#09283f;font-family:Georgia,serif}}
main{{display:flex;align-items:center;gap:54px;width:1120px;height:550px;margin:40px;
      padding:54px;border:4px solid #09283f;border-radius:24px;background:#fffdf4}}
.copy{{flex:1;min-width:0}}.brand{{color:#962039;font:bold 25px Arial,sans-serif;margin:0 0 26px}}
h1{{margin:0;font-size:{size}px;line-height:1.08;overflow-wrap:anywhere}}
.art{{display:grid;place-items:center;flex:0 0 350px;height:350px;background:#cbdfff;
     border:3px solid #09283f;border-radius:20px}}.art svg{{display:block;width:270px;height:270px}}
</style><main><div class="copy"><p class="brand">srini.presents</p><h1>{attr(title)}</h1></div>{figure}</main>""")
        self.page.screenshot(path=str(path), type='jpeg', quality=88)


def article_cover(path, head, url, title, art, renderer):
    archived = path.name != 'index.html'
    original = path.with_suffix('.png') if archived else path.with_name('og.png')
    generated = (path.with_name(path.stem + '-og-share.jpg') if archived
                 else path.with_name('og-share.jpg'))
    explicit = file_for_url(head.meta.get('og:image', ''), url)
    # Ignore generic and cross-article preview images, even when they exist.
    if (explicit and explicit.is_file() and explicit.suffix in {'.png', '.jpg', '.jpeg'}
            and explicit.parent == path.parent
            and (not archived or explicit.stem in {path.stem, generated.stem})):
        return explicit
    if original.is_file():
        return original
    if not generated.is_file():
        renderer.render(generated, title, art)
    return generated


def process(path, cards, published, thumbnails, renderer):
    page = read_page(path)
    end = HEAD_END.search(page)
    if not end:
        # Redirect stubs (e.g. health pages moved to health.srinipresents.com) may have no
        # <head> tag at all; they are not articles, so leave them alone instead of failing.
        if re.search(r'(?i)http-equiv=["\']?refresh|<link[^>]+rel=["\']?canonical[^>]+https://health\.', page):
            return None, False
        raise ValueError(f'No HTML head in {path.relative_to(ROOT)}')
    head, body = page[:end.start()], page[end.end():]
    clean = BLOCK.sub('', head)
    h = Head()
    h.feed(head)
    if 'refresh' in h.meta:
        return None, False

    url = BASE + route(path)
    slug = route(path).strip('/')
    headline = re.search(r'(?is)<h1\b[^>]*>(.*?)</h1>', body)
    raw_title = h.meta.get('og:title') or h.title or (text_of(headline[1]) if headline else '')
    title = re.sub(r'\s*[·—|–-]\s*srini\.presents\s*$', '', ' '.join(raw_title.split()), flags=re.I)
    card = re.search(r'(?is)<p>(.*?)</p>', cards.get(slug, ''))
    desc = (h.meta.get('description') or h.meta.get('og:description')
            or (text_of(card[1]) if card else '') or standfirst(body))
    desc = clip(' '.join(desc.split())) or title
    if not title:
        raise ValueError(f'No article title in {path.relative_to(ROOT)}')

    image = article_cover(path, h, url, title, thumbnails.get(path) or article_art(body), renderer)
    alt = h.meta.get('og:image:alt') or f'Srini Presents cover for {title}'
    tags, image_url = share_tags(title, desc, url, image, alt)
    authored = Head()
    authored.feed(clean)
    if not authored.meta.get('description'):
        tags.append(f'<meta name="description" content="{attr(desc)}">')
    if 'canonical' not in authored.links:
        tags.append(f'<link rel="canonical" href="{url}">')
    if 'application/ld+json' not in clean:
        data = {'@context': 'https://schema.org', '@type': 'Article',
                'headline': title, 'description': desc, 'url': url,
                'mainEntityOfPage': url, 'image': image_url,
                'author': AUTHOR, 'publisher': {'@type': 'Organization',
                'name': 'srini.presents', 'url': BASE + '/'}, 'inLanguage': 'en-IN'}
        if slug in published:
            data['datePublished'] = published[slug]
        ld = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
        tags.append(f'<script type="application/ld+json">{ld}</script>')

    new = strip_sharing(clean) + START + ''.join(tags) + END + end[0] + body
    return (title, desc, url, image, alt), save_page(path, page, new)


def refresh_share_page(path, article_metadata):
    page = read_page(path)
    end = HEAD_END.search(page)
    if not end:
        return False
    clean = BLOCK.sub('', page[:end.start()])
    h = Head()
    h.feed(page[:end.start()])
    if 'refresh' not in h.meta or not any(key.startswith('og:') for key in h.meta):
        return False
    target_url = re.search(r'(?i)\burl\s*=\s*(.+)$', h.meta['refresh'])
    target = file_for_url(target_url[1].strip(' "\''), BASE + route(path)) if target_url else None
    if target not in article_metadata:
        return False
    title, desc, url, image, alt = article_metadata[target]
    # Short share routes have their own identity for visit tracking.
    if path.relative_to(ROOT).parts[0] == 's':
        url = BASE + route(path)
    tags, _ = share_tags(title, desc, url, image, alt)
    new = strip_sharing(clean) + START + ''.join(tags) + END + page[end.start():]
    return save_page(path, page, new)


def main():
    queue = json.loads((ROOT / 'publishing-queue.json').read_text(encoding='utf-8'))
    cards = {e['path'].strip('/'): e.get('card_html', '') for e in queue['entries']}
    published = {e['path'].strip('/'): e['published_at']
                 for e in queue['entries']
                 if e.get('status') == 'published' and e.get('published_at')}
    thumbnails = card_art()
    metadata = {}
    changed = 0
    with ExitStack() as stack:
        renderer = CoverRenderer(stack)
        for path in sorted(story_pages()):
            article, updated = process(path, cards, published, thumbnails, renderer)
            if article:
                metadata[path] = article
            changed += updated

    aliases = sorted(set(ROOT.glob('*/index.html')) - metadata.keys())
    aliases.extend(sorted((ROOT / 's').glob('*/index.html')))
    changed += sum(refresh_share_page(path, metadata) for path in aliases)
    print(f'seo_meta: verified {len(metadata)} article covers; updated {changed} HTML heads')


if __name__ == '__main__':
    main()
