#!/usr/bin/env python3
"""Phone-first QA for a srini.presents article.

usage: python3 tools/article-kit/qa.py path/to/index.html [outdir]

Screenshots at 390px light, 390px dark, 340px and 1100px (full page), prints
scrollWidth at each width (must equal the width: no sideways scroll), and lists
any TODO left in the file. Look at the 390px images like a phone reader.
"""
import sys, os, asyncio
from playwright.async_api import async_playwright
CHROME = next((p for p in ['/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser'] if os.path.exists(p)), None)
async def main(path, out):
    os.makedirs(out, exist_ok=True); ok = True
    async with async_playwright() as p:
        b = await p.chromium.launch(**({'executable_path': CHROME} if CHROME else {}))
        for name, w, scheme in [('390-light', 390, 'light'), ('390-dark', 390, 'dark'), ('340', 340, 'light'), ('1100', 1100, 'light')]:
            pg = await b.new_page(viewport={'width': w, 'height': 900}, color_scheme=scheme)
            await pg.goto('file://' + os.path.abspath(path)); await pg.wait_for_timeout(1200)
            sw = await pg.evaluate('document.documentElement.scrollWidth'); print(f'{name}: scrollWidth {sw}', 'OK' if sw <= w else 'SIDEWAYS SCROLL!')
            ok &= sw <= w
            await pg.screenshot(path=os.path.join(out, f'qa-{name}.png'), full_page=True)
        await b.close()
    todo = open(path).read().count('TODO'); print('TODOs left:', todo)
    print('screenshots in', out); return ok and not todo
if __name__ == '__main__':
    sys.exit(0 if asyncio.run(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '/tmp/qa')) else 1)
