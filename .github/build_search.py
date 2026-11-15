#!/usr/bin/env python3
"""Build the search index from published articles, retaining their live URLs."""

import html
import json
import re
import shutil
import subprocess
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = 'https://srinipresents.com'
HUBS = {'/', '/archive/', '/ortho/', '/ortho/fracture/', '/ortho/neck-pain/', '/ortho/shoulder/', '/ortho/knee-replacement/', '/health/'}
BODY = re.compile(r'<body\b[^>]*>', re.I)
REDIRECT = re.compile(r'<meta[^>]+http-equiv\s*=\s*["\']?refresh', re.I)


class ArticleLinks(HTMLParser):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.routes = set()

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        href = dict(attrs).get('href')
        if not href:
            return
        target = urlsplit(urljoin(ORIGIN + self.route, href))
        if target.netloc == 'srinipresents.com' and re.fullmatch(r'/[a-z0-9./-]*', target.path):
            self.routes.add(target.path)


def page_path(route):
    if route.endswith('/'):
        return route.strip('/') + '/index.html' if route != '/' else 'index.html'
    return route.lstrip('/')


def section_for(route):
    if route.startswith('/health/'):
        return 'Common Health Conditions'
    if route.startswith('/ortho/') or route == '/robotic-knee-replacement/':
        return 'Ortho'
    return 'Everyday Curiosity'


def collect_articles():
    queue = json.loads((ROOT / 'publishing-queue.json').read_text(encoding='utf-8'))
    pending = {item['path'] for item in queue['entries'] if item.get('status') != 'published'}
    published = {item['path'] for item in queue['entries'] if item.get('status') == 'published'}
    links = set(published)
    for hub in HUBS:
        parser = ArticleLinks(hub)
        parser.feed((ROOT / page_path(hub)).read_text(encoding='utf-8'))
        links.update(parser.routes)

    for route in sorted(links - pending - HUBS):
        if not re.fullmatch(r'/(?:[a-z0-9-]+/|archive/[a-z0-9-]+\.html|(?:health|ortho)/(?:[a-z0-9-]+/)+)', route):
            continue
        if route in {'/about/', '/search/', '/nifty/', '/nifty-chronicles/'}:
            continue
        source = ROOT / page_path(route)
        if not source.is_file():
            continue
        page = source.read_text(encoding='utf-8')
        if REDIRECT.search(page) or not BODY.search(page):
            continue
        section = html.escape(section_for(route), quote=True)
        marker = f'<span data-pagefind-filter="section:{section}"></span>'
        yield page_path(route), BODY.sub(lambda match: match[0] + marker, page, count=1)


def main():
    with tempfile.TemporaryDirectory() as folder:
        site = Path(folder) / 'site'
        count = 0
        for path, page in collect_articles():
            output = site / path
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(page, encoding='utf-8')
            count += 1
        if not count:
            raise RuntimeError('No published articles found')
        subprocess.run([
            'npx', '--yes', 'pagefind@1.6.0', '--site', str(site),
            '--force-language', 'en',
            '--exclude-selectors', 'nav, footer, svg, .evidence, .patient-note',
        ], check=True, cwd=ROOT)
        target = ROOT / 'pagefind'
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(site / 'pagefind', target)
        print(f'Built the search index from {count} articles')


if __name__ == '__main__':
    main()
