"""Make the 3 minimalist video slides (VERTICAL 1080x1920 JPEG, 9:16) for Srini's daily ~18 s video.

Approved by Srini, 5 Nov 2026: minimalist, BRIGHT day colour (same as the share card), vertical, no vintage
paper; big slab headline with one red accent word, "Srini presents" top-left, "n / 3" top-right.
  Slide 1 = quiz title, Slide 2 = 3 questions with one-word answers, Slide 3 = "N more ... inside" + link.

Usage:  python3 make_slides.py spec.json OUTPREFIX     -> OUTPREFIX-1.jpg, -2.jpg, -3.jpg
spec.json keys:
  weekday    e.g. "THURSDAY" (picks the pastel; optional "paper" overrides)
  icon       1-2 characters/emoji in the yellow circle on slide 1 (e.g. "₹", "📞")
  title      slide-1 headline; "\n" = line break, *word* = red accent  e.g. "Caller ID\n*quiz.*"
  sub        slide-1 sub line, e.g. "3 questions.\n3 traps."
  questions  list of 3 {q, a, note?}: question, short answer ("NO", "NOPE", "YES"), optional small note
  more       slide-3 headline, e.g. "4 more\n*traps*\ninside."
  url        e.g. "sriniurs.github.io/caller-id"
  tap        optional, default "Tap the link to read ↓"
  art1, art3 inner SVG (viewBox 0 0 100 100, flat cartoon, 3px #151515 outlines) for slides 1 and 3
  questions[].art  optional small icon per question (same format; reuse assets/ill/library.json)
  zappy1     Zappy's bubble on slide 1 (3-6 words, e.g. "Think you know gold?")
  bolt2      Prof. Bolt's bubble on slide 2 (2-5 words, e.g. "Surprised? Most are.")
  zappy3, bolt3  bubbles on slide 3 (e.g. "Wait, there's more?!" / "Tap. The rest is inside.")
Characters (#kiran = Zappy, #guru = Prof. Bolt) are built into slides_template.html.
"""
import json, sys, os, pathlib
from playwright.sync_api import sync_playwright
PAPER = {"MONDAY": "#c2410c", "TUESDAY": "#b45309", "WEDNESDAY": "#15803d", "THURSDAY": "#1d4ed8", "FRIDAY": "#be185d", "SATURDAY": "#6d28d9", "SUNDAY": "#0f766e"}  # rich day colours on warm off-white (Srini, 5 Nov 2026: bright lime looked cheap)
spec = json.load(open(sys.argv[1])); out = sys.argv[2]
here = pathlib.Path(__file__).resolve().parent
paper = spec.get("paper") or PAPER.get(spec["weekday"].strip().upper(), "#d3e3c2")
page = (here / "slides_template.html").read_text().replace("{{C}}", paper)\
    .replace("{{SPEC}}", json.dumps(spec, ensure_ascii=False).replace("</", "<\\/"))
tmp = here / "_slides_tmp.html"; tmp.write_text(page)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    for n in (1, 2, 3):
        pg.goto(tmp.as_uri() + f"?s={n}"); pg.wait_for_timeout(300)
        pg.screenshot(path=f"{out}-{n}.jpg", type="jpeg", quality=90)
    b.close()
tmp.unlink()
print("wrote", *(f"{out}-{n}.jpg" for n in (1, 2, 3)))
