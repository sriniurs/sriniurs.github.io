"""Make og-share.jpg (1200x630) from each article's cover and add share meta tags.
Usage: python3 og.py <repo> [--all] [paths...]"""
import re, sys, os, glob, html, io
from playwright.sync_api import sync_playwright
from PIL import Image
REPO = sys.argv[1]; ALL = '--all' in sys.argv
only = [a for a in sys.argv[2:] if not a.startswith('--')]
SITE = 'https://bhakti.srinipresents.com'
LOGO = os.path.join(REPO, 'assets/brand/logo-clear.png')
if not os.path.exists(LOGO): LOGO = os.path.join(REPO, 'assets/brand/logo.png')

def parts(h):
    m = re.search(r'<section[^>]*class="page cover cover2"[^>]*>.*?</section>', h, re.S)
    c = m.group(0)
    mc = re.search(r'--mastc:\s*(#[0-9a-fA-F]{3,6})', c) or re.search(r'class="mast"[^>]*style="[^"]*background:\s*(#[0-9a-fA-F]{3,6})', c)
    if not mc:
        mc = re.search(r'\.cover2 \.mast\{[^}]*background:\s*(#[0-9a-fA-F]{6})', h)
    mast = mc.group(1) if mc else '#15365a'
    g = lambda pat: (re.search(pat, c, re.S).group(1).strip() if re.search(pat, c, re.S) else '')
    kicker = g(r'<div class="kicker">(.*?)</div>')
    title = g(r'<h1[^>]*>(.*?)</h1>')
    tag = g(r'<p class="tag">(.*?)</p>')
    body = c[c.find('coverbody'):] if 'coverbody' in c else c
    art = re.search(r'<svg(?=[^>]*(?:class="coverart"|viewBox))[^>]*>.*?</svg>', body, re.S)
    art = art.group(0) if art else ''
    return mast, kicker, title, tag, art

def card(mast, kicker, title, tag, art):
    t = re.sub(r'<br\s*/?>', ' ', title); tl = len(re.sub('<[^>]+>', '', t))
    fs = 76 if tl <= 14 else 62 if tl <= 22 else 50 if tl <= 34 else 40
    art = re.sub(r'^<svg', '<svg preserveAspectRatio="xMidYMid meet"', re.sub(r'\s(width|height)="[^"]*"', '', art[:art.find('>')]) + art[art.find('>'):]) if art else ''
    return f'''<html><head><meta charset="utf-8"><style>
body{{margin:0;width:1200px;height:630px;background:#2a1d16;font-family:"Noto Sans",Arial,sans-serif}}
.w{{position:absolute;inset:14px;border-radius:18px;overflow:hidden;display:flex;background:#f2f2ef}}
.l{{width:610px;overflow:hidden;background:{mast};color:#fff;padding:40px 44px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:center}}
.logo{{width:190px;background:#ebeae0;border-radius:12px;padding:6px 10px;border:2px solid #111;margin-bottom:14px}}
.by{{font-weight:700;letter-spacing:3px;font-size:16px;text-transform:uppercase;margin-bottom:16px}}
.k{{align-self:flex-start;background:#fbf3df;color:{mast};font-weight:700;font-size:16px;letter-spacing:1.2px;text-transform:uppercase;border-radius:999px;padding:6px 16px;margin-bottom:18px;max-width:100%;line-height:1.3}}
h1{{overflow-wrap:normal;word-break:keep-all;font-family:Georgia,"Times New Roman",serif;color:#fbf3df;text-transform:uppercase;font-size:{fs}px;line-height:1.02;margin:0 0 16px}}
.t{{font-family:Georgia,serif;font-size:22px;line-height:1.3}}
.r{{flex:1;display:flex;align-items:center;justify-content:center;padding:26px}}
.r svg{{width:100%;height:auto;max-height:560px;border-radius:12px}}
</style></head><body><div class="w"><div class="l"><img class="logo" src="file://{LOGO}"><div class="by">Srini presents</div>
{f'<div class="k">{kicker}</div>' if kicker else ''}<h1>{t}</h1><div class="t">{tag}</div></div><div class="r">{art}</div></div><script>const h=document.querySelector('h1');let f=parseFloat(getComputedStyle(h).fontSize);const L=document.querySelector('.l');while((h.scrollWidth>h.clientWidth+1||L.scrollHeight>L.clientHeight+1)&&f>26){{f-=2;h.style.fontSize=f+'px';}}</script></body></html>'''

import json
PAINT = json.load(open('/tmp/painted.json'))
def pcard(img, mast, kicker, title):
    t = re.sub(r'<br\s*/?>', ' ', title)
    return f'''<html><head><meta charset="utf-8"><style>
body{{margin:0;width:1200px;height:630px;background:#000;font-family:"Noto Sans",Arial,sans-serif;overflow:hidden}}
.bg{{position:absolute;inset:0;background:url("file://{img}") center 22%/cover no-repeat;image-rendering:auto;filter:saturate(1.05) contrast(1.03)}}
.band{{position:absolute;left:0;right:0;bottom:0;padding:22px 36px 24px 36px;background:linear-gradient(to top,rgba(0,0,0,.82),rgba(0,0,0,.55) 70%,rgba(0,0,0,0));display:flex;align-items:flex-end;gap:22px}}
.logo{{width:170px;background:#ebeae0;border-radius:12px;padding:6px 10px;border:2px solid #111;flex:none}}
.tx{{color:#fff;min-width:0}}
.k{{display:inline-block;background:#fbf3df;color:{mast};font-weight:700;font-size:15px;letter-spacing:1.2px;text-transform:uppercase;border-radius:999px;padding:5px 14px;margin-bottom:8px}}
h1{{font-family:Georgia,serif;color:#fbf3df;text-transform:uppercase;font-size:54px;line-height:1.02;margin:0;text-shadow:0 2px 6px rgba(0,0,0,.6);overflow-wrap:normal}}
</style></head><body><div class="bg"></div><div class="band"><img class="logo" src="file://{LOGO}"><div class="tx">{f'<div class="k">{kicker}</div>' if kicker else ''}<h1>{t}</h1></div></div>
<script>const h=document.querySelector('h1');let f=54;while((h.scrollWidth>h.clientWidth+1||h.offsetHeight>130)&&f>28){{f-=2;h.style.fontSize=f+'px';}}</script></body></html>'''

def meta(h, rel):
    t = re.search(r'<title>(.*?)</title>', h, re.S); t = html.unescape(t.group(1).strip()) if t else rel
    t = re.sub(r'\s*\|\s*srini\.presents.*$', '', t)
    d = re.search(r'<meta name="description" content="([^"]*)"', h); d = d.group(1) if d else ''
    e = lambda s: html.escape(s, quote=True)
    url = f'{SITE}/{rel}/'; img = f'{url}og-share.jpg'
    tags = [f'<meta property="og:title" content="{e(t)}">', f'<meta property="og:description" content="{d}">',
            '<meta property="og:type" content="article">', f'<meta property="og:url" content="{url}">',
            '<meta property="og:site_name" content="srini.presents">', f'<meta property="og:image" content="{img}">',
            '<meta property="og:image:type" content="image/jpeg">', '<meta property="og:image:width" content="1200">',
            '<meta property="og:image:height" content="630">', f'<meta property="og:image:alt" content="Srini Presents cover for {e(t)}">',
            '<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:title" content="{e(t)}">',
            f'<meta name="twitter:description" content="{d}">', f'<meta name="twitter:image" content="{img}">']
    h = re.sub(r'\s*<meta (?:property="og:[^"]*"|name="twitter:[^"]*")[^>]*>', '', h)
    anchor = re.search(r'<meta name="description"[^>]*>', h)
    i = anchor.end() if anchor else h.find('</title>') + 8
    return h[:i] + '\n' + '\n'.join(tags) + h[i:]

files = [os.path.join(REPO, p, 'index.html') for p in only] if only else glob.glob(os.path.join(REPO, '**/index.html'), recursive=True)
todo = []
for f in files:
    if '/tools/' in f: continue
    h = open(f, encoding='utf-8').read()
    if 'class="book' not in h or 'cover2' not in h: continue
    if not ALL and 'og:image' in h and os.path.exists(os.path.join(os.path.dirname(f), 'og-share.jpg')): continue
    todo.append(f)
print('to do', len(todo))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 630})
    for f in todo:
        h = open(f, encoding='utf-8').read(); rel = os.path.relpath(os.path.dirname(f), REPO)
        tmp = '/tmp/ogcard.html'; pt = parts(h); key = '/' + rel + '/'
        if key in PAINT and os.path.exists(os.path.join(REPO, PAINT[key].lstrip('/'))) and 'collection' not in PAINT[key]:
            open(tmp, 'w').write(pcard(os.path.join(REPO, PAINT[key].lstrip('/')), pt[0], pt[1], pt[2]))
        else:
            open(tmp, 'w').write(card(*pt))
        pg.goto('file://' + tmp); pg.wait_for_timeout(60)
        png = pg.screenshot(clip={'x': 0, 'y': 0, 'width': 1200, 'height': 630})
        Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(os.path.dirname(f), 'og-share.jpg'), quality=86, optimize=True)
        open(f, 'w', encoding='utf-8').write(meta(h, rel))
    b.close()
print('done')
