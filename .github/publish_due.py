"""Feature at most one due story per IST day. Standard library only."""
import argparse
import copy
import datetime as dt
import json
import os
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())


class Structure(HTMLParser):
    """Locate the source list and cards without reserialising the HTML."""
    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text = text
        self.lines = [0]
        self.lines += [m.end() for m in re.finditer('\n', text)]
        self.stack = []
        self.lists = []
        self.cards = []
        self.active = None
        self.feed(text)
        self.close()

    def pos(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        at = self.pos()
        parent = self.stack[-1] if self.stack else None
        entry = {'tag': tag, 'attrs': attrs, 'start': at}
        if tag == 'ul' and parent and 'page' in parent['attrs'].get('class', '').split():
            entry['source'] = True
            entry['inner_start'] = at + len(self.get_starttag_text())
        if tag == 'li' and parent and parent.get('source'):
            if self.active is not None:
                raise ValueError('Unclosed story card')
            self.active = {'start': at, 'href': None}
        if tag == 'a' and self.active is not None and self.active['href'] is None:
            self.active['href'] = attrs.get('href')
        if tag not in VOID:
            self.stack.append(entry)

    def handle_startendtag(self, tag, attrs):
        if tag not in VOID:
            self.handle_starttag(tag, attrs)
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1]['tag'] != tag:
            raise ValueError('Unexpected HTML closing tag: ' + tag)
        entry = self.stack.pop()
        if tag == 'li' and self.active is not None and self.stack and self.stack[-1].get('source'):
            self.active['end'] = self.pos() + len('</li>')
            self.cards.append(self.active)
            self.active = None
        if entry.get('source'):
            entry['inner_end'] = self.pos()
            self.lists.append(entry)


SITE_HOSTS = {'srinipresents.com', 'www.srinipresents.com', 'sriniurs.github.io'}


def canonical(href):
    parsed = urlsplit(href or '')
    if parsed.netloc and parsed.netloc not in SITE_HOSTS:
        return None
    path = parsed.path
    if path.endswith('index.html'):
        path = path[:-10]
    return '/' + path.strip('/') + '/'


def feature(text, card, href):
    doc = Structure(text)
    if len(doc.lists) != 1:
        raise ValueError('Expected one direct .page > ul source list')
    source = doc.lists[0]
    script = text.find('id="theme-groups-js"')
    if script < source['inner_end']:
        raise ValueError('Source list must precede the theme grouping script')
    target = canonical(href)
    remove = [c for c in doc.cards if canonical(c['href']) == target]
    inner = text[source['inner_start']:source['inner_end']]
    for c in reversed(remove):
        a, b = c['start'] - source['inner_start'], c['end'] - source['inner_start']
        inner = inner[:a] + inner[b:]
    return text[:source['inner_start']] + '\n' + card + '\n' + inner + text[source['inner_end']:]


def validate(root, queue):
    if queue.get('time_zone') != 'Asia/Kolkata' or queue.get('publish_time') != '05:00':
        raise ValueError('Unexpected queue timezone or release time')
    numbers = [e['number'] for e in queue['entries']]
    if any(type(n) is not int or n <= 0 for n in numbers) or len(set(numbers)) != len(numbers):
        raise ValueError('Queue numbers must be unique positive integers')
    paths = []
    for e in queue['entries']:
        path = e['path']
        if not re.fullmatch(r'/[a-z0-9-]+/', path) or canonical(e['url']) != path:
            raise ValueError('Invalid story path or URL')
        if path in paths:
            raise ValueError('Duplicate queued story path')
        paths.append(path)
        if e['status'] not in ('pending', 'published'):
            raise ValueError('Invalid story status')
        when = dt.datetime.fromisoformat(e['not_before'])
        if when.tzinfo is None:
            raise ValueError('not_before must include timezone')
        page = root / path.strip('/') / 'index.html'
        if not page.is_file() or '<html' not in page.read_text(encoding='utf-8').lower():
            raise ValueError('Missing or invalid article: ' + str(page))
        card = e['card_html']
        if len(re.findall(r'<li\b', card)) != 1 or not card.rstrip().endswith('</li>'):
            raise ValueError('Expected one complete story card')
        links = re.findall(r'<a\b[^>]*href=[\"\x27]([^\"\x27]+)', card)
        if not links or canonical(links[0]) != path:
            raise ValueError('Card link does not match story')
        if len(re.findall(r'<span\b[^>]*class=[\"\x27]story-date[\"\x27][^>]*>.*?</span>', card)) != 1:
            raise ValueError('Expected one story-date')
    for name in ('index.html', 'archive/index.html'):
        text = (root / name).read_text(encoding='utf-8')
        doc = Structure(text)
        if len(doc.lists) != 1:
            raise ValueError('Missing source article list: ' + name)
        if 'id="theme-groups-js"' not in text:
            raise ValueError('Missing theme grouping script: ' + name)


def plan(root, queue, now):
    """Return changes in memory; validate everything before touching any files."""
    validate(root, queue)
    now = now.astimezone(IST)
    today = now.date()
    last = queue.get('last_published_on')
    if last and dt.date.fromisoformat(last) > today:
        raise ValueError('last_published_on is in the future')
    # Check publication records as well as the guard field to prevent duplicate releases.
    published_today = any(e.get('published_at') and
                          dt.datetime.fromisoformat(e['published_at']).astimezone(IST).date() == today
                          for e in queue['entries'])
    if last == today.isoformat() or published_today:
        return {}, 'Today’s story is already published.'
    if today < dt.date.fromisoformat(queue['start_date']) or now.time() < dt.time(5):
        return {}, 'Before the daily 05:00 IST release time.'
    pending = sorted((e for e in queue['entries'] if e['status'] == 'pending'), key=lambda e: e['number'])
    if not pending:
        return {}, 'Queue is empty.'
    chosen = pending[0]
    if dt.datetime.fromisoformat(chosen['not_before']) > now:
        return {}, 'Next story is not due yet: ' + chosen['title']
    changed_queue = copy.deepcopy(queue)
    entry = next(e for e in changed_queue['entries'] if e['number'] == chosen['number'])
    date = f'{today.day} {today.strftime("%b")} {today.year}'
    card = re.sub(r'(<span\b[^>]*class=[\"\x27]story-date[\"\x27][^>]*>).*?(</span>)',
                  lambda m: m[1] + date + m[2], entry['card_html'])
    changes = {name: feature((root / name).read_text(encoding='utf-8'), card, entry['path'])
               for name in ('index.html', 'archive/index.html')}
    entry.update(status='published', published_at=now.isoformat(timespec='seconds'), card_html=card)
    changed_queue['last_published_on'] = today.isoformat()
    changes['publishing-queue.json'] = json.dumps(changed_queue, ensure_ascii=False, indent=2) + '\n'
    return changes, 'Published #' + str(entry['number']) + ': ' + entry['title']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--now', help='Timezone-aware time; allowed only with --dry-run')
    args = parser.parse_args()
    if args.now and not args.dry_run:
        parser.error('--now requires --dry-run; production always uses the real clock')
    now = dt.datetime.fromisoformat(args.now) if args.now else dt.datetime.now(IST)
    if now.tzinfo is None:
        parser.error('--now requires a timezone offset')
    queue = json.loads((args.root / 'publishing-queue.json').read_text(encoding='utf-8'))
    changes, message = plan(args.root, queue, now)
    if not args.dry_run:
        for name, text in changes.items():
            (args.root / name).write_text(text, encoding='utf-8')
    print(('DRY RUN: ' if args.dry_run else '') + message)
    output = os.environ.get('GITHUB_OUTPUT')
    if output:
        with open(output, 'a', encoding='utf-8') as stream:
            stream.write('changed=' + ('true' if changes and not args.dry_run else 'false') + '\n')
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a', encoding='utf-8') as stream:
            stream.write('### Daily story publisher\n\n' + message + '\n')


if __name__ == '__main__':
    main()
