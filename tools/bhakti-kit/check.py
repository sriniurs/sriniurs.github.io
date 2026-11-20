import sys,asyncio
from playwright.async_api import async_playwright
async def main(path):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':390,'height':844})
        await pg.goto('file://'+path); await pg.wait_for_timeout(1500)
        await pg.screenshot(path='/home/claude/work/m_cover.png')
        ov=await pg.evaluate("document.documentElement.scrollWidth")
        print('scrollWidth',ov)
        await pg.screenshot(path='/home/claude/work/m_full.png',full_page=True)
        pg2=await b.new_page()
        await pg2.goto('file://'+path); await pg2.wait_for_timeout(1000)
        await pg2.pdf(path='/home/claude/work/out.pdf',format='A4',print_background=True,prefer_css_page_size=True)
        await b.close()
asyncio.run(main(sys.argv[1]))
