"""Make the vintage WhatsApp share card (2400x1600 PNG) for a Srini Presents comic.

Usage: python3 make_card.py spec.json out.jpg [--story]
  --story  tall 1080x1920 version for WhatsApp status / Instagram story
spec.json keys:
  title   - comic title (plain text)
  note    - 3-6 words for the pinned note (sits on the right, above the art); wrap ONE key phrase in *stars* to highlight it
  weekday - e.g. "THURSDAY" (also picks the day's pastel paper colour; optional "paper" overrides it)
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
# Vintage paper tinted to the day's theme colour (Srini, 4 Nov 2026) so each day's
# status looks new: pastel version of the comic's cover colour for that weekday.
PAPER = {"MONDAY": "#f4d3b8", "TUESDAY": "#f3e1a6", "WEDNESDAY": "#d3e3c2",
         "THURSDAY": "#cfdcee", "FRIDAY": "#f3cfd4", "SATURDAY": "#ddd3f0",
         "SUNDAY": "#c6e1dc"}
paper = spec.get("paper") or PAPER.get(spec["weekday"].strip().upper(), "#f1dfba")
story = "--story" in sys.argv  # tall 9:16 version for WhatsApp status / Instagram story
import colorsys
def _band(hexc):
    # same hue as the day's paper, made dark so WhatsApp's white caption reads well (Srini, 4 Nov 2026)
    r, g, b = (int(hexc[i:i+2], 16) / 255 for i in (1, 3, 5))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    r, g, b = colorsys.hls_to_rgb(h, 0.24, min(1.0, s * 0.75 + 0.15))
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))
band = _band(paper)
page = (here / ("card_story_template.html" if story else "card_template.html")).read_text(encoding="utf-8")
page = page.replace("{{PAPER}}", paper).replace("{{BAND0}}", band + "00").replace("{{BAND}}", band)
page = (page.replace("{{TITLE}}", esc(spec["title"]))
            .replace("{{NOTE}}", note)
            .replace("{{WEEKDAY}}", esc(spec["weekday"].upper()))
            .replace("{{THEME}}", esc(spec["theme"].upper()))
            .replace("{{ART}}", spec["art"]))
tmp = here / "_card_render.html"
tmp.write_text(page, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch()
    jpg = out.suffix.lower() in (".jpg", ".jpeg")
    # JPEG for WhatsApp: 1620x1080, quality 80 (~150 KB) so it loads fast on phones
    vw, vh = (720, 1280) if story else (1200, 800)
    pg = b.new_page(viewport={"width": vw, "height": vh}, device_scale_factor=(1.5 if story else 1.35) if jpg else 2)
    pg.goto(tmp.as_uri())
    pg.evaluate("window.cardReady")
    pg.wait_for_timeout(600)
    pg.screenshot(path=str(out), type="jpeg", quality=80) if jpg else pg.screenshot(path=str(out))
    b.close()
tmp.unlink()
print("wrote", out)
