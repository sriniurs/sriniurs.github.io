"""Site-wide uniformity pass for bhakti.srinipresents.com.
1. Old covers (bhakti-article-cover / legacy) -> masthead cover2 with the logo.
2. Logo only on the cover: remove per-page pglogo images.
Idempotent. Usage: python3 cover_fix.py <repo> [paths...]"""
import re, sys, glob, os, html
REPO = sys.argv[1]
MAST = {'maroon': '#8e1f17', 'light-blue': '#1d4f8a', 'navy': '#15365a', None: '#15365a'}
CSS = '''<style id="cover2-uniform">
section.page.cover.cover2{background:#f2f2ef!important;background-image:none!important;padding:0!important;border:6px solid #2a1d16;border-radius:14px;overflow:hidden;text-align:center;box-shadow:8px 8px 0 #2a1d16;color:#111}
section.page.cover.cover2 .mast{background:var(--mastc,#15365a);padding:22px 18px 26px;color:#fff}
section.page.cover.cover2 .brandtile{display:block;width:150px;max-width:44vw;height:auto;margin:0 auto 10px;background:#ebeae0;border:2px solid #111;border-radius:10px;padding:4px 8px}
section.page.cover.cover2 .byline{font-family:"Noto Sans",sans-serif;font-weight:700;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#fff;margin:0 0 10px;text-shadow:none;background:none;border:0;transform:none;box-shadow:none;padding:0;display:block;position:static}
section.page.cover.cover2 .kicker{display:inline-block;background:#fbf3df;color:var(--mastc,#15365a);font-family:"Noto Sans",sans-serif;font-weight:700;font-size:12px;letter-spacing:1.2px;text-transform:uppercase;border-radius:999px;padding:4px 12px;margin:0 0 12px;max-width:100%}
section.page.cover.cover2 h1{font-family:Georgia,"Times New Roman",serif;font-weight:700;color:#fbf3df;-webkit-text-stroke:0;text-shadow:none;line-height:1.02;text-transform:uppercase;margin:4px 0 12px;letter-spacing:.5px;background:none;border:0;transform:none;padding:0;overflow-wrap:anywhere}
section.page.cover.cover2 .tag{font-family:Georgia,serif;font-size:clamp(16px,2.6vw,20px);color:#fff;text-shadow:none;margin:0 auto;max-width:560px;line-height:1.35;text-transform:none;background:none}
section.page.cover.cover2 .coverbody{padding:18px 16px 22px}
section.page.cover.cover2 .coverart{display:block;margin:0 auto;max-width:min(100%,620px);width:100%;height:auto;max-height:340px;border-radius:10px;border:0;box-shadow:none}
section.page.cover.cover2 .cvcap{font-family:Georgia,serif;font-style:italic;text-transform:uppercase;font-size:13px;letter-spacing:.5px;color:#333;margin:8px 0 6px;text-shadow:none}
section.page.cover.cover2 .cast figure{color:#111;text-shadow:none}
section.page.cover.cover2 .bubble{background:#fff;border:1.5px solid #9aa3ad;border-radius:8px;text-align:left;max-width:600px;margin:12px auto 6px;font-size:14.5px;color:#111;box-shadow:none}
section.page.cover.cover2 .bubble b.lead{font-family:Bangers,Impact,sans-serif;font-style:italic;letter-spacing:.6px;font-size:17px}
@media screen and (max-width:720px){section.page.cover.cover2{width:100%;max-width:100%;min-width:0;margin-inline:0;box-shadow:none}section.page.cover.cover2 .mast{padding-inline:10px;min-width:0}section.page.cover.cover2 h1{font-size:clamp(18px,5.5vw,38px)!important;letter-spacing:0!important;line-height:1.12;white-space:normal;max-width:100%}section.page.cover.cover2 .coverbody{padding-inline:10px}}
</style>'''
LOGO = '<img class="brandtile" src="/assets/brand/logo-clear.png" alt="srini.presents" width="420" height="192">'

def txt(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s or '')).strip()
def grab(c, cls, tag=r'\w+'):
    m = re.search(r'<(' + tag + r')[^>]*class="' + cls + r'"[^>]*>(.*?)</\1>', c, re.S)
    return m.group(2).strip() if m else ''

def new_cover(h, c):
    th = re.search(r'data-cover-theme="([^"]*)"', c)
    th = th.group(1) if th else None
    if th is None and re.search(r'data-bhakti-article="maroon"', h): th = 'maroon'
    if th is None and re.search(r'data-bhakti-article="light-blue"', h): th = 'light-blue'
    mc = MAST.get(th, '#15365a')
    chap = grab(c, 'cover-chapter') or grab(c, 'series')
    inv = grab(c, 'cover-invocation')
    h1m = re.search(r'<h1[^>]*>(.*?)</h1>', c, re.S); title = h1m.group(1).strip()
    sub = grab(c, 'cover-subtitle') or grab(c, 'tag')
    if sub and 'explained' not in sub.lower() and 'illustrated' not in sub.lower(): sub += ' · explained and illustrated'
    art = re.search(r'<figure class="(?:cover-art|article-legacy-art)">\s*(<svg.*?</svg>)\s*</figure>', c, re.S)
    art = art.group(1) if art else ''
    if art: art = re.sub(r'^<svg', '<svg class="coverart"', re.sub(r'^<svg([^>]*?) class="[^"]*"', r'<svg\1', art))
    cast = re.search(r'<div class="cast">.*?</figure>\s*<figure>.*?</figure>\s*</div>', c, re.S)
    cast = cast.group(0) if cast else ''
    bubs = re.findall(r'<div class="bubble[^"]*"[^>]*>(.*?)</div>', c, re.S)
    how = ''
    for b in bubs:
        if re.search(r'HOW THIS', b):
            how = re.sub(r'<span class="who">[^<]*</span>', '', b).strip()
    if not how:
        d = re.search(r'<meta name="description" content="([^"]*)"', h)
        how = d.group(1) if d else ''
        how = re.sub(r'\s*An illustrated reference guide\.?\s*$', '', how)
    extra = ''.join(f'<div class="bubble">{b.strip()}</div>' for b in bubs if 'MEET THE CAST' in b)
    if chap: kicker, cap = chap, inv
    else: kicker, cap = inv, ''
    n = len(txt(title))
    fs = 'clamp(40px,8.5vw,80px)' if n <= 14 else 'clamp(32px,6.6vw,62px)' if n <= 24 else 'clamp(26px,5.2vw,48px)'
    return f'''<section class="page cover cover2" style="--mastc:{mc}">
  <div class="mast">
    {LOGO}
    <p class="byline">Srini presents</p>
    {f'<div class="kicker">{kicker}</div>' if kicker else ''}
    <h1 style="font-size:{fs}">{title}</h1>
    <p class="tag">{sub}</p>
  </div>
  <div class="coverbody">
    {art}
    {f'<p class="cvcap">{cap}</p>' if cap else ''}
    {cast}
    {extra}
    <div class="bubble"><b class="lead">HOW THIS WORKS:</b> {how}</div>
  </div>
</section>'''

def fix(path):
    h = open(path, encoding='utf-8').read()
    if 'class="book"' not in h: return None
    o = h
    m = re.search(r'<section[^>]*class="page cover(?! cover2)[^"]*"[^>]*>.*?</section>', h, re.S)
    if m and 'cover2' not in m.group(0):
        h = h[:m.start()] + new_cover(h, m.group(0)) + h[m.end():]
        if 'id="cover2-uniform"' not in h: h = h.replace('</head>', CSS + '\n</head>', 1)
    h = re.sub(r'<img class="pglogo"[^>]*>', '', h)
    if h != o:
        open(path, 'w', encoding='utf-8').write(h); return True
    return False

if __name__ == '__main__':
    files = sys.argv[2:] or glob.glob(os.path.join(REPO, '**/index.html'), recursive=True)
    n = 0
    for f in files:
        if '/tools/' in f: continue
        if fix(f): n += 1
    print('changed', n)
