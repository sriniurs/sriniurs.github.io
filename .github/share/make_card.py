"""Make the vintage WhatsApp share card (2400x1600 PNG) for a Srini Presents comic.

Usage: python3 make_card.py spec.json out.png
spec.json keys:
  title   - comic title (plain text)
  note    - 3-6 words for the pinned note (sits on the right, above the art); wrap ONE key phrase in *stars* to highlight it
  weekday - e.g. "THURSDAY"
  theme   - day theme, e.g. "FUTURE IS HERE"
  art     - inner SVG markup for ONE big topic illustration (bottom-right) drawn in viewBox 0 0 430 400;
            keep the top ~80 units fairly empty or light, the pinned note sits just above it
            (flat muted vintage colours, 4px #2a2420 outlines; see phone_example.svg)
Fonts and the template live next to this script, so it works from a fresh clone.
"""
import html, json, re, sys, pathlib
from playwright.sync_api import sync_playwright

here = pathlib.Path(__file__).resolve().parent
spec = json.load(open(sys.argv[1], encoding="utf-8"))
out = pathlib.Path(sys.argv[2]).resolve()

def esc(t):
    return html.escape(t, quote=False)

note = esc(spec["note"])
note = re.sub(r"\*(.+?)\*", r'<u style="white-space:nowrap">\1</u>', note)
page = (here / "card_template.html").read_text(encoding="utf-8")
page = (page.replace("{{TITLE}}", esc(spec["title"]))
            .replace("{{NOTE}}", note)
            .replace("{{WEEKDAY}}", esc(spec["weekday"].upper()))
            .replace("{{THEME}}", esc(spec["theme"].upper()))
            .replace("{{ART}}", spec["art"]))
tmp = here / "_card_render.html"
tmp.write_text(page, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 800}, device_scale_factor=2)
    pg.goto(tmp.as_uri())
    pg.evaluate("window.cardReady")
    pg.wait_for_timeout(600)
    pg.screenshot(path=str(out))
    b.close()
tmp.unlink()
print("wrote", out)
