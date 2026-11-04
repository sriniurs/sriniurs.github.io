"""Make the 3 minimalist video slides (1080x1920 JPEG) for Srini's daily ~18 s video.

Approved by Srini, 5 Nov 2026: minimalist, day pastel colour (same as the share card), no vintage
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
"""
import json, sys, os, pathlib
from playwright.sync_api import sync_playwright
PAPER = {"MONDAY": "#f4d3b8", "TUESDAY": "#f3e1a6", "WEDNESDAY": "#d3e3c2", "THURSDAY": "#cfdcee",
         "FRIDAY": "#f3cfd4", "SATURDAY": "#ddd3f0", "SUNDAY": "#c6e1dc"}
spec = json.load(open(sys.argv[1])); out = sys.argv[2]
here = pathlib.Path(__file__).resolve().parent
paper = spec.get("paper") or PAPER.get(spec["weekday"].strip().upper(), "#d3e3c2")
page = (here / "slides_template.html").read_text().replace("{{PAPER}}", paper)\
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
