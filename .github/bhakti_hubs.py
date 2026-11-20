#!/usr/bin/env python3
"""Build the Bhakti hubs from bhakti/catalog.json and add a trail to every Bhakti article.

The section has four doors (Gods, Hymns, Scriptures, Temples) and three deity
views (Śiva, Viṣṇu, Devi). Every article or series under /bhakti/ needs one entry
in bhakti/catalog.json; this script then places its card on the right hubs.

  python3 .github/bhakti_hubs.py           rebuild hubs and trails
  python3 .github/bhakti_hubs.py --strict  also fail if any Bhakti page is uncatalogued
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = ROOT / 'bhakti' / 'catalog.json'

DOORS = {
    'gods': ('Gods and Goddesses', 'Who they are'),
    'hymns': ('Hymns and Mantras', 'What to chant'),
    'scriptures': ('Scriptures and Stories', 'What to read'),
    'temples': ('Temples and Tīrthas', 'Where to go'),
}
DOOR_URL = {'gods': '/bhakti/gods/', 'hymns': '/bhakti/hymns/',
            'scriptures': '/bhakti/scriptures/', 'temples': '/bhakti/temples-of-india/'}
DEITIES = {'shiva': ('Śiva', 'he'), 'vishnu': ('Viṣṇu', 'he'), 'devi': ('Devi', 'she')}
UNIT = {'gods': 'guide', 'hymns': 'hymn', 'scriptures': 'text', 'temples': 'temple guide'}


def plural(n, word):
    return f'{n} {word}' + ('' if n == 1 else 's')


GROUPS = {'circuits': 'Pan-India circuits', 'regional': 'Regional guides'}
HUBS = {'/bhakti/', '/bhakti/gods/', '/bhakti/hymns/', '/bhakti/scriptures/',
        '/bhakti/temples-of-india/', '/bhakti/shiva/', '/bhakti/vishnu/', '/bhakti/devi/'}

HUB_S, HUB_E = '<!-- hub:auto -->', '<!-- /hub:auto -->'
TR_S, TR_E = '<!-- bhaktitrail:auto -->', '<!-- /bhaktitrail:auto -->'
SHELF_CSS = ('<style>.shelf{max-width:1180px;margin:34px auto 6px;padding:0 18px;'
             'font:800 clamp(20px,3vw,28px)/1.2 system-ui,-apple-system,"Segoe UI",sans-serif;color:#151515}'
             '.shelf small{display:block;font:500 15px/1.4 system-ui,sans-serif;color:#555;margin-top:4px}</style>')
TRAIL_CSS = ('<style>.bk-trail{max-width:820px;margin:28px auto 18px;padding:12px 16px;border:2px solid #09283f;'
             'border-radius:14px;background:#fffdf4;box-shadow:3px 3px 0 #09283f;'
             'font:600 15px/1.7 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#09283f}'
             '.bk-trail a{color:#09283f;text-decoration:underline;text-underline-offset:3px}'
             '.bk-trail .sep{opacity:.55;margin:0 6px}.bk-trail .also{display:block;font-weight:500}'
             '@media print{.bk-trail{display:none}}</style>')


def load():
    data = json.loads(CAT.read_text(encoding='utf-8'))
    entries = data['entries']
    seen = set()
    for e in entries:
        p = e['path']
        if not (p.startswith('/bhakti/') and p.endswith('/')):
            sys.exit(f'catalog: bad path {p}')
        if p in seen:
            sys.exit(f'catalog: duplicate {p}')
        seen.add(p)
        if e['door'] not in DOORS:
            sys.exit(f'catalog: unknown door {e["door"]} for {p}')
        for d in e['deities']:
            if d not in DEITIES:
                sys.exit(f'catalog: unknown deity {d} for {p}')
        if not (ROOT / p.strip('/') / 'index.html').exists():
            sys.exit(f'catalog: no page at {p}')
    return entries


def pages_under(path):
    base = ROOT / path.strip('/')
    return sum(1 for f in base.rglob('index.html') if not is_redirect(f))


def is_redirect(f):
    return bool(re.search(r'(?i)<meta[^>]+http-equiv=["\']?refresh', f.read_text(encoding='utf-8', errors='ignore')[:3000]))


def shelf(title, sub, tiles, anchor=''):
    if not tiles:
        return ''
    a = f' id="{anchor}"' if anchor else ''
    s = f'<small>{sub}</small>' if sub else ''
    return f'<h2 class="shelf"{a}>{title}{s}</h2>\n  <ol class="tiles">\n    ' + ''.join(tiles) + '\n  </ol>\n'


def write_hub(url, body):
    f = ROOT / url.strip('/') / 'index.html'
    page = f.read_text(encoding='utf-8')
    block = HUB_S + SHELF_CSS + '\n' + body + HUB_E
    if HUB_S in page:
        new = re.sub(re.escape(HUB_S) + r'.*?' + re.escape(HUB_E), lambda m: block, page, flags=re.S)
    else:
        new = re.sub(r'<ol class="tiles">.*?</ol>', lambda m: block, page, count=1, flags=re.S)
        if new == page:
            sys.exit(f'hub {url}: no tiles list to replace')
    if new != page:
        f.write_text(new, encoding='utf-8')


def card(href, bg, art, label, title, text, read='Open ↗'):
    return (f'<li><a href="{href}"><div class="tile-art" style="background:{bg}"><svg class="ill" viewBox="0 0 100 100" '
            f'aria-hidden="true"><g stroke="#151515" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{art}</g>'
            f'</svg></div><div class="tile-copy"><strong class="label">{label}</strong><h2>{title}</h2><p>{text}</p>'
            f'<span class="read">{read}</span></div></a></li>')


ART = {
    'gods': ('#3a1414', '<circle cx="50" cy="40" r="16" fill="#f2c79b"/><path d="M32 26 h36 l-5 -16 l-8 8 l-5 -12 l-5 12 l-8 -8z" fill="#ffd60a"/><path d="M26 94 q-4 -40 24 -46 q28 6 24 46z" fill="#c0392b"/>'),
    'hymns': ('#fff1d6', '<path d="M20 84 h60 l-10 10 h-40z" fill="#c9a26b"/><path d="M50 80 q-18 -22 0 -50 q18 28 0 50z" fill="#ff8c1a"/><path d="M50 74 q-8 -12 0 -26 q8 14 0 26z" fill="#ffd60a"/><path d="M18 30 q4 -8 8 0 M74 24 q4 -8 8 0" fill="none"/>'),
    'scriptures': ('#f3e3c3', '<path d="M12 40 h76 v40 h-76z" fill="#e8c27a"/><path d="M12 48 h76 M12 56 h76 M12 64 h76 M12 72 h76" stroke-width="1.5"/><path d="M30 34 v52 M70 34 v52" stroke="#7a4a1a" stroke-width="4"/>'),
    'temples': ('#f3e3c3', '<path d="M10 92 h80 v-8 h-80z" fill="#c9a26b"/><path d="M22 84 v-26 h56 v26z" fill="#e8c27a"/><path d="M30 58 L50 10 L70 58Z" fill="#d9782f"/><path d="M44 84 v-14 a6 6 0 0 1 12 0 v14z" fill="#2b1a0e"/><path d="M50 10 v-6"/><path d="M50 4 l10 3 l-10 3z" fill="#ff8c1a"/>'),
}
DEITY_ART = {
    'devi': ('#ffe3ec', '<path d="M50 88 C26 76 20 50 30 36 C40 48 46 64 50 88Z M50 88 C74 76 80 50 70 36 C60 48 54 64 50 88Z" fill="#f08aa6"/><path d="M50 88 C38 66 40 40 50 22 C60 40 62 66 50 88Z" fill="#ffc2dc"/>'),
    'shiva': ('#0b2a4a', '<path d="M50 94 V30" stroke="#d9a21b" stroke-width="7"/><path d="M36 44 Q36 26 50 30 Q64 26 64 44" fill="none" stroke="#d9a21b" stroke-width="7"/><path d="M32 46 L36 18 L40 46Z M46 32 L50 4 L54 32Z M60 46 L64 18 L68 46Z" fill="#ffd23f" stroke-width="2"/><path d="M38 58 L62 58 L52 68 L62 78 L38 78 L48 68Z" fill="#e63946" stroke-width="2"/>'),
    'vishnu': ('#dcecff', '<path d="M50 14 C70 14 84 34 80 56 C76 76 58 88 42 82 C28 76 26 58 38 50 C48 44 58 50 56 60" fill="#fff8e7"/><path d="M50 14 C40 22 34 34 36 46" fill="none"/>'),
}


def build(entries):
    count = {e['path']: pages_under(e['path']) for e in entries}
    by = lambda door, deity=None, group=None: [e for e in entries if e['door'] == door
                                                and (deity is None or deity in e['deities'])
                                                and (group is None or e.get('group') == group)]
    tiles = lambda es: [e['tile'] for e in es]
    n_art = lambda es: sum(count[e['path']] for e in es)

    # Bhakti home: four doors, then the deity views
    doors = []
    for k, (t, sub) in DOORS.items():
        es = by(k)
        bg, art = ART[k]
        doors.append(card(DOOR_URL[k], bg, art, f'{plural(len(es), UNIT[k])} · {n_art(es)} articles', t, sub + '.'))
    deities = []
    for d, (name, _) in DEITIES.items():
        es = [e for e in entries if d in e['deities']]
        bg, art = DEITY_ART[d]
        parts = [plural(len(by(k, d)), UNIT[k]) for k in DOORS if by(k, d)]
        deities.append(card(f'/bhakti/{d}/', bg, art, ' · '.join(parts), name,
                            f'Everything for {name} in one place, from all four doors.'))
    write_hub('/bhakti/', shelf('Four doors', 'Pick what you are looking for.', doors)
              + shelf('Or start with a deity', 'Each deity page gathers all four doors.', deities))

    # door pages
    for k in ('gods', 'hymns', 'scriptures'):
        body = ''
        for d, (name, _) in DEITIES.items():
            es = [e for e in by(k) if e['deities'][0] == d]
            body += shelf(name, '', tiles(es), d)
        write_hub(DOOR_URL[k], body)
    write_hub('/bhakti/temples-of-india/', ''.join(shelf(g, '', tiles(by('temples', group=gk)), gk) for gk, g in GROUPS.items()))

    # deity pages
    for d, (name, pron) in DEITIES.items():
        body = (shelf(f'Who {pron} is', 'Forms, stories and symbols.', tiles(by('gods', d)), 'who')
                + shelf('Hymns and mantras', 'What to chant, verse by verse.', tiles(by('hymns', d)), 'hymns')
                + shelf('Scriptures and stories', 'Texts read in parts.', tiles(by('scriptures', d)), 'scriptures')
                + shelf('Temples', 'Where to go.', tiles(by('temples', d)), 'temples'))
        write_hub(f'/bhakti/{d}/', body)


def trail_for(entry, entries):
    door = entry['door']
    t = [f'<a href="/bhakti/">Bhakti</a>', f'<a href="{DOOR_URL[door]}">{DOORS[door][0]}</a>']
    also = ''
    if len(entry['deities']) == 1:
        d = entry['deities'][0]
        name, pron = DEITIES[d]
        t.append(f'<a href="/bhakti/{d}/">{name}</a>')
        links = []
        for k, label in (('gods', f'who {pron} is'), ('hymns', 'hymns'), ('scriptures', 'scriptures'), ('temples', 'temples')):
            if k != door and any(e['door'] == k and d in e['deities'] for e in entries):
                anchor = {'gods': 'who'}.get(k, k)
                links.append(f'<a href="/bhakti/{d}/#{anchor}">{label}</a>')
        if links:
            also = f'<span class="also">More for {name}: ' + ' · '.join(links) + '</span>'
    return (TR_S + TRAIL_CSS + '<nav class="bk-trail" aria-label="Bhakti section">'
            + '<span class="sep">›</span>'.join(t) + also + '</nav>' + TR_E + '\n')


def trails(entries, strict):
    order = sorted(entries, key=lambda e: -len(e['path']))
    missing = []
    for f in sorted((ROOT / 'bhakti').rglob('index.html')):
        url = '/' + str(f.parent.relative_to(ROOT)).replace('\\', '/') + '/'
        if url in HUBS:
            continue
        page = f.read_text(encoding='utf-8')
        if is_redirect(f):
            continue
        entry = next((e for e in order if url.startswith(e['path'])), None)
        clean = re.sub(re.escape(TR_S) + r'.*?' + re.escape(TR_E) + r'\n?', '', page, flags=re.S)
        if entry is None:
            missing.append(url)
            new = clean
        else:
            block = trail_for(entry, entries)
            m = re.search(r'<script[^>]*data-goatcounter', clean) or re.search(r'</body>', clean, re.I)
            if not m:
                continue
            new = clean[:m.start()] + block + clean[m.start():]
        if new != page:
            f.write_text(new, encoding='utf-8')
    if missing:
        print('Uncatalogued Bhakti pages (add them to bhakti/catalog.json):')
        for u in missing:
            print('  ' + u)
        if strict:
            sys.exit(1)


if __name__ == '__main__':
    entries = load()
    build(entries)
    trails(entries, '--strict' in sys.argv)
    print(f'bhakti hubs: {len(entries)} catalog entries')
