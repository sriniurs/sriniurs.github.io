#!/usr/bin/env python3
"""Render the srini.presents share images for one article.

usage: python3 tools/article-kit/make_share.py spec.json

spec.json:
{
  "slug": "drishti-face",                 # output goes to <repo>/<slug>/ unless "out" is given
  "word": "DRISHTI",                       # one big topic word
  "word_color": "#e63946",                 # one strong colour
  "title": "Who is the shocked woman staring from every half-built house?",
  "badge_big": "3.2 MILLION",              # sourced number, worded exactly as measured
  "badge_small": "views for one question",
  "art": "<g>…</g>",                       # original simple SVG on a 300x300 viewBox
  "out": "optional/output/folder"
}

Writes og.png (1200x630), card.jpg (same, JPEG), insta.png and insta.jpg (1080x1920).
Look at both images afterwards: nothing off the edge, badge clear of art and title.
"""
import json, sys, os, base64, asyncio, html
from playwright.async_api import async_playwright

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..'))
CHROME = next((p for p in ['/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser'] if os.path.exists(p)), None)

def logo_uri():
    p = os.path.join(REPO, 'assets/brand/logo-clear.png')
    return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:W;height:H;overflow:hidden;background:#fbf3e2;
 background-image:radial-gradient(#e7d6b4 2.2px,transparent 2.4px);background-size:22px 22px;
 font-family:'DejaVu Sans',Arial,sans-serif;color:#151515;position:relative}
.word{font-family:Impact,'Arial Black','DejaVu Sans',sans-serif;font-weight:900;letter-spacing:1px;line-height:1}
.title{font-weight:900;line-height:1.16}
.badge{position:absolute;background:#ffd23f;border:4px solid #151515;box-shadow:8px 8px 0 #151515;
 text-align:center;font-weight:900;padding:12px 22px;line-height:1.1}
.badge b{display:block}.badge span{display:block;font-weight:700}
.art{position:absolute}
.strip{position:absolute;left:0;right:0;bottom:0;background:#14254a;color:#fff;font-weight:900;
 display:flex;align-items:center;justify-content:space-between}
.strip em{font-style:normal;color:#ffd23f}
"""

def page_og(s):
    css = BASE_CSS.replace('W', '1200px').replace('H', '630px')
    return f"""<html><head><style>{css}
.logo{{position:absolute;left:36px;top:24px;height:104px}}
.word{{position:absolute;left:286px;top:34px;font-size:96px;color:{s['word_color']};max-width:520px;white-space:nowrap}}
.title{{position:absolute;left:40px;top:178px;width:700px;font-size:46px}}
.badge{{left:40px;top:392px;transform:rotate(-4deg)}}.badge b{{font-size:34px}}.badge span{{font-size:21px}}
.art{{right:40px;top:40px;width:340px;height:340px}}
.strip{{height:90px;padding:0 40px;font-size:28px}}.strip .h{{font-size:24px}}
</style></head><body>
<img class="logo" src="{logo_uri()}"><div class="word">{html.escape(s['word'])}</div>
<div class="title">{html.escape(s['title'])}</div>
<div class="badge"><b>{html.escape(s['badge_big'])}</b><span>{html.escape(s['badge_small'])}</span></div>
<svg class="art" viewBox="0 0 300 300">{s['art']}</svg>
<div class="strip"><div>READ THE FULL STORY · <em>srinipresents.com</em></div><div class="h">srini.present@gmail.com</div></div>
</body></html>"""

def page_insta(s):
    css = BASE_CSS.replace('W', '1080px').replace('H', '1920px')
    return f"""<html><head><style>{css}
.logo{{position:absolute;left:60px;top:70px;height:170px}}
.word{{position:absolute;left:60px;top:300px;font-size:150px;color:{s['word_color']};max-width:960px;overflow-wrap:anywhere}}
.title{{position:absolute;left:60px;top:500px;width:960px;font-size:72px}}
.art{{left:210px;top:1010px;width:660px;height:660px}}
.badge{{right:60px;top:880px;transform:rotate(4deg)}}.badge b{{font-size:52px}}.badge span{{font-size:30px}}
.strip{{height:190px;padding:0 60px;font-size:40px;flex-direction:column;justify-content:center;align-items:flex-start;gap:16px}}.strip .h{{font-size:34px;color:#cfd8ea}}
</style></head><body>
<img class="logo" src="{logo_uri()}"><div class="word">{html.escape(s['word'])}</div>
<div class="title">{html.escape(s['title'])}</div>
<svg class="art" viewBox="0 0 300 300">{s['art']}</svg>
<div class="badge"><b>{html.escape(s['badge_big'])}</b><span>{html.escape(s['badge_small'])}</span></div>
<div class="strip"><div>READ THE FULL STORY · <em>srinipresents.com</em></div><div class="h">srini.present@gmail.com</div></div>
</body></html>"""

async def render(spec):
    out = spec.get('out') or os.path.join(REPO, spec['slug'])
    os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(**({'executable_path': CHROME} if CHROME else {}))
        for name, w, h, fn in [('og', 1200, 630, page_og), ('insta', 1080, 1920, page_insta)]:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.set_content(fn(spec)); await pg.wait_for_timeout(400)
            # shrink the title if it runs into the badge / strip
            await pg.evaluate("""()=>{const t=document.querySelector('.title');const lim=%d;let f=parseFloat(getComputedStyle(t).fontSize);
              while(t.getBoundingClientRect().bottom>lim && f>24){f-=2;t.style.fontSize=f+'px'}
              const w=document.querySelector('.word');let g=parseFloat(getComputedStyle(w).fontSize);
              while(w.scrollWidth>w.clientWidth+2 && g>40){g-=4;w.style.fontSize=g+'px'}}""" % (380 if name == 'og' else 900))
            png = os.path.join(out, f'{name}.png')
            await pg.screenshot(path=png)
            await pg.screenshot(path=os.path.join(out, 'card.jpg' if name == 'og' else 'insta.jpg'), type='jpeg', quality=85)
            print('wrote', png)
        await b.close()

if __name__ == '__main__':
    asyncio.run(render(json.load(open(sys.argv[1]))))
