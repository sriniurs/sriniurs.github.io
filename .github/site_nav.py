#!/usr/bin/env python3
"""Put the same Back / Home bar at the top of every story page.

The bar is inserted right after <body ...> inside a marked block, so re-running
replaces it instead of stacking copies. Back returns to the previous page when
the reader came from this site, otherwise it goes to the archive.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {'archive', 'assets', 'queue', 'preview', 's', 'stats', 'about'}
START, END = '<!-- sitenav:auto -->', '<!-- /sitenav:auto -->'
BLOCK = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)

BAR = START + """<style>
.sp-bar{position:sticky;top:0;z-index:9999;display:flex;gap:8px;align-items:center;
padding:8px 12px;background:rgba(255,253,244,.94);border-bottom:2px solid #09283f;
backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);
font:700 14px/1 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.sp-bar a{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:999px;
border:2px solid #09283f;background:#fff;color:#09283f;text-decoration:none;box-shadow:2px 2px 0 #09283f}
.sp-bar a:hover,.sp-bar a:focus-visible{background:#ffe53a}
.sp-bar a:active{transform:translate(1px,1px);box-shadow:1px 1px 0 #09283f}
.sp-bar .sp-brand{margin-left:auto;border:0;box-shadow:none;background:none;padding:0 2px}
.sp-bar .sp-brand img{display:block;height:36px;width:auto}
.sp-bar .sp-brand:hover{background:none}
@media print{.sp-bar{display:none}}
</style>
<nav class="sp-bar" aria-label="Site">
<a href="/archive/" id="sp-back" aria-label="Go back">&larr; Back</a>
<a href="/" aria-label="Home page">&#8962; Home</a>
<a class="sp-brand" href="/"><img src="/assets/brand/logo.png" alt="srini.presents" width="420" height="192"></a>
</nav>
<script>
(function(){var b=document.getElementById('sp-back');if(!b)return;
b.addEventListener('click',function(e){var r=document.referrer;
if(r&&r.indexOf(location.origin)===0&&history.length>1){e.preventDefault();history.back();}});})();
</script>
""" + END + '\n'


def process(path):
    with open(path, encoding='utf-8', newline='') as fh:
        page = fh.read()
    if re.search(r'(?i)<meta[^>]+http-equiv=["\']?refresh', page):
        return False                       # redirect stub
    clean = BLOCK.sub('', page)
    m = re.search(r'(?is)<body\b[^>]*>', clean)
    if not m:
        return False
    new = clean[:m.end()] + '\n' + BAR + clean[m.end():].lstrip('\n')
    if new == page:
        return False
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(new)
    return True


def main():
    changed = []
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        page = d / 'index.html'
        if d.name.startswith('.') or d.name in SKIP or not page.exists():
            continue
        if process(page):
            changed.append(d.name)
    print(f'site_nav: updated {len(changed)} page(s)')
    import brand_logo
    brand_logo.main()


if __name__ == '__main__':
    main()
