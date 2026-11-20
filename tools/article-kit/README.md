# Article kit (srini.presents daily articles)

Helpers for the daily explainer articles. Bhakti articles have their own kit in `../bhakti-kit/`.

| Script | What it does |
|---|---|
| `new_article.py <slug> "<Title>" "<description>" [--day mon..sun]` | Starts `~/articles/<slug>/index.html` from the master template (`drishti-face/`): head + style blocks, Zappy/Prof. Bolt symbols, cover scaffold in the day colour, 8 episode stubs, deep-dive banner after episode 4, evidence file, Follow footer, GoatCounter. Fill every TODO. |
| `qa.py <index.html> [outdir]` | Screenshots at 390 light, 390 dark, 340 and 1100 px; prints scrollWidth (must equal the width) and counts TODOs left. |
| `make_share.py spec.json` | Renders the share images: `og.png` + `card.jpg` (1200×630) and `insta.png` + `insta.jpg` (1080×1920) in the approved design (cream halftone, logo, big topic word, bold title, yellow number badge, original art, navy "READ THE FULL STORY · srinipresents.com" strip). See the docstring for the spec fields; `example_spec.json` is a working example. |

Needs python3, playwright + Chrome/Chromium, Pillow. Web fonts don't load offline,
so QA screenshots show fallback fonts; layout and widths are still valid.

Queueing, status links and publishing: see the "Daily article queue" section of
`PUBLISHING.md` and the `srini-presents-article` skill.
