import sys,asyncio
from playwright.async_api import async_playwright
async def main(names):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        for n in names:
            pg=await b.new_page(viewport={'width':794,'height':1123}); await pg.emulate_media(media='print')
            await pg.goto(f'http://localhost:8765/test/{n}/'); await pg.wait_for_timeout(500)
            r=await pg.evaluate("[...document.querySelectorAll('section.page')].map(s=>[s.id,s.scrollHeight])")
            print(n,sorted(r,key=lambda x:-x[1])[:3]); await pg.close()
        await b.close()
asyncio.run(main(sys.argv[1:]))
