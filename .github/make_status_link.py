"""Make the STATUS link page for a story (Srini, 4 Nov 2026).

Usage: python3 .github/make_status_link.py <slug> "<Comic title>" "<og description>"
Writes s/<slug>/index.html: a tiny page that records the visit in GoatCounter
under /s/<slug> and then forwards to /<slug>/. So the dashboard shows
  /s/<slug>  = readers who came from the WhatsApp STATUS
  /<slug>/   = all readers (status + groups)  -> groups = /<slug>/ minus /s/<slug>
"""
import html, os, sys
slug, title, desc = sys.argv[1], sys.argv[2], sys.argv[3]
t, d = html.escape(title), html.escape(desc)
page = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:image" content="https://sriniurs.github.io/{slug}/og.png">
<meta property="og:url" content="https://sriniurs.github.io/s/{slug}/"><meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="noindex"><meta http-equiv="refresh" content="3; url=/{slug}/">
<style>body{{font-family:system-ui,sans-serif;background:#fffbe6;display:flex;align-items:center;justify-content:center;height:90vh;margin:0}}a{{color:#c0262d;font-weight:700;font-size:20px}}</style>
</head><body><a href="/{slug}/">Opening the story…</a>
<script>window.goatcounter={{no_onload:true}};</script>
<script src="//gc.zgo.at/count.js" data-goatcounter="https://sriniurs.goatcounter.com/count" async onload="try{{goatcounter.count({{path:'/s/{slug}'}})}}catch(e){{}}setTimeout(function(){{location.replace('/{slug}/')}},400)" onerror="location.replace('/{slug}/')"></script>
<script>setTimeout(function(){{location.replace('/{slug}/')}},1500);</script>
</body></html>
'''
os.makedirs(f's/{slug}', exist_ok=True)
open(f's/{slug}/index.html', 'w', encoding='utf-8').write(page)
print('wrote', f's/{slug}/index.html')
