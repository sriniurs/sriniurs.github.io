import sys,asyncio,re,glob
from playwright.async_api import async_playwright
import pypdf
from PIL import Image
async def one(b,slug,root="festivals/navaratri"):
    url=f'http://localhost:8765/{root}/{slug}/'
    pg=await b.new_page(viewport={'width':390,'height':844}); await pg.goto(url); await pg.wait_for_timeout(600)
    sw=await pg.evaluate("document.documentElement.scrollWidth"); await pg.close()
    pg2=await b.new_page(); await pg2.goto(url); await pg2.wait_for_timeout(400)
    pdf=f'/tmp/{slug}.pdf'; await pg2.pdf(path=pdf,format='A4',print_background=True,prefer_css_page_size=True); await pg2.close()
    n=len(pypdf.PdfReader(pdf).pages)
    html=open(glob.glob(f'/home/claude/srv/{root}/{slug}/index.html')[0]).read()
    secs=html.count('<section class="page')
    return slug,sw,n,secs
async def main(slugs,root):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        for s in slugs:
            r=await one(b,s,root); print(*r, 'OK' if r[1]==390 and r[2]==r[3] else '<<< FIX')
        await b.close()
root=sys.argv[1]; slugs=sys.argv[2:]
asyncio.run(main(slugs,root))
