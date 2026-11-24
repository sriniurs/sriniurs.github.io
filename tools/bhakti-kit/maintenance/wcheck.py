import sys,glob,random,os
from playwright.sync_api import sync_playwright
os.chdir('/home/claude/srini-bhakti')
fs=[f[:-11] for f in glob.glob('**/index.html',recursive=True) if 'class="book' in open(f).read() and not f.startswith('tools')]
random.seed(1); s=fs
bad=[]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':800})
    pg.route('**/*', lambda r: r.abort() if 'fonts.g' in r.request.url or 'google' in r.request.url else r.continue_())
    for f in s:
        try:
            pg.goto(f'http://localhost:8765/site/{f}/',wait_until='domcontentloaded',timeout=15000)
            r=pg.evaluate('''()=>{const c=document.querySelector("section.page.cover.cover2");const r=c?c.getBoundingClientRect():null;return [document.documentElement.scrollWidth, c?Math.round(r.width):0, document.querySelectorAll("img.brandtile").length, document.querySelectorAll("img.pglogo").length, !!document.querySelector("#sources")]}''')
            if r[0]>392 or r[1]==0 or r[2]!=1 or r[3]!=0 or not r[4]: bad.append((f,r))
        except Exception as e: bad.append((f,str(e)[:80]))
    b.close()
print(len(s),'checked; bad:',bad)
