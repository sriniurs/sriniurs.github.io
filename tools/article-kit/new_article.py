#!/usr/bin/env python3
"""Start a new srini.presents article from the master template.

usage: python3 tools/article-kit/new_article.py <slug> "<Title>" "<meta description>" [--day mon..sun] [--template drishti-face]

Writes <workdir>/<slug>/index.html (default workdir: ~/articles) with the template's
<head> and Zappy/Prof. Bolt symbols, a cover scaffold, 8 episode stubs, the deep-dive
banner after episode 4, the evidence file, Follow footer and GoatCounter. Fill the
TODOs; never hand-add Open Graph, canonical, sitenav or the logo div (scripts do that).
"""
import sys, os, re, argparse
KIT = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(KIT, '..', '..'))
DAYS = {  # cover bg, title colour, text colour, byline colour
 'mon': ('#c2410c', '#fff', '#fff', '#fff1a8'), 'tue': ('#ffd23f', '#151515', '#151515', '#9d0208'),
 'wed': ('#17703f', '#fff', '#fff', '#ffd23f'), 'thu': ('#1d4f9a', '#ffd23f', '#fff', '#fff'),
 'fri': ('#ffc6cf', '#151515', '#151515', '#9d174d'), 'sat': ('#ddd0ff', '#151515', '#151515', '#4c1d95'),
 'sun': ('#0e5b57', '#ffd23f', '#fff', '#a7f3d0')}
a = argparse.ArgumentParser(); a.add_argument('slug'); a.add_argument('title'); a.add_argument('desc')
a.add_argument('--day'); a.add_argument('--template', default='drishti-face'); a.add_argument('--workdir', default=os.path.expanduser('~/articles'))
o = a.parse_args()
src = open(os.path.join(REPO, o.template, 'index.html')).read()
head = src[:src.find('</head>')]
head = re.sub(r'<!-- seo:auto -->.*?<!-- /seo:auto -->\n?', '', head, flags=re.S)
head = re.sub(r'<title>.*?</title>', f'<title>{o.title} — srini.presents</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{o.desc}">', head)
if o.day:
    bg, tc, xc, bc = DAYS[o.day]
    head += (f'<style id="day-cover">header.cover{{background:{bg}!important;color:{xc}!important}}header.cover h1{{color:{tc}!important;-webkit-text-stroke:0!important;text-shadow:none!important}}'
             f'header.cover .byline{{color:{bc}!important}}header.cover .sub,header.cover .readtime,header.cover .cast,header.cover .cast small,header.cover .tagline{{color:{xc}!important}}</style>\n')
# Logo on the cover in every new article (Srini's rule, 24 Nov 2026): absolute URL so samples and
# previews outside the site show it too; data-brand-logo keeps .github/brand_logo.py from redoing it.
sys.path.insert(0, os.path.join(REPO, '.github'))
from brand_logo import CSS as BRAND_CSS
BRAND = ('<div class="brand"><img data-brand-logo src="https://srinipresents.com/assets/brand/logo.png" '
         'alt="srini.presents" width="420" height="192"><span class="tagline">for curious grown-ups</span></div>')
if '<style id="brand-logo">' not in head:
    head += BRAND_CSS + '\n'
body = src[src.find('<body>'):src.find('<main')]
body = re.sub(r'<!-- sitenav:auto -->.*?<!-- /sitenav:auto -->\n?', '', body, flags=re.S)
eps = ''
for n in range(1, 9):
    if n == 5:
        eps += '<div class="era p2">THE DEEP DIVE<small>TODO one-line promise of the deep dive.</small></div>\n\n'
    eps += (f'<section class="ep" id="section-{n:02d}"><div class="ep-head"><span class="no">{n:02d}</span><h2>TODO episode {n}</h2></div>'
            '<div class="reading"><p>TODO narration with facts and [n] links <a href="#s1">[1]</a></p></div>'
            + ('<div class="banter"><div class="say"><svg class="av" viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg><p class="bubble"><span class="who">Zappy</span>TODO</p></div>'
               '<div class="say g"><svg class="av" viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg><p class="bubble"><span class="who">Prof. Bolt</span>TODO</p></div></div>' if n % 2 else '')
            + '</section>\n\n')
main = f'''<main class="wrap"><header class="cover">{BRAND}<h1>{o.title}</h1><p class="sub">TODO subtitle</p><div class="fs"><span>TODO</span><span>TODO</span><span>TODO</span></div><div class="cast"><figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>TODO</small></figure><figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>TODO</small></figure></div><p class="readtime">ABOUT N MINUTES</p></header>

{eps}<section class="evidence" id="sources"><h2>The evidence file</h2><p>Checked TODO date. Source types are labelled. Dialogue is fictional; legends are described, not endorsed.</p><ol class="source-list">
<li id="s1"><a href="TODO">TODO title</a> — TODO type, date; what it supports.</li>
</ol></section>

<section class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></section>
<footer class="foot">THE END · srini.presents · for curious grown-ups</footer></main>

<script data-goatcounter="https://sriniurs.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body></html>
'''
out = os.path.join(o.workdir, o.slug); os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'index.html'), 'w').write(head + '</head>\n' + body + main)
print('wrote', os.path.join(out, 'index.html'))
