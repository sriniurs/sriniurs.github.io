# srini.presents · Bhakti: complete handover

Start a new chat with this file. It lists everything needed to build, check and publish new Bhakti articles at bhakti.srinipresents.com without the history of earlier chats. Read it once fully before building anything.

Owner: **Dr. Srinivas Deep Urs ("Srini")**, Mysuru. Brand: **srini.presents**. Replies to Srini: brief, frank, no step-by-step recap. Say what went live, the URL, anything flagged.

---

## 0. What the site is

- A timeless, illustrated reference library on Hindu hymns, scriptures, gods, temples and festivals.
- Each article is one long HTML page. Every `<section class="page">` prints as exactly one A4 sheet, so the page is also a printable booklet.
- Two characters run every article:
  - **Zappy** (curious young learner) asks;
  - **Prof. Bolt** (wise mentor) answers.
- Live site: https://bhakti.srinipresents.com. Old srinipresents.com/bhakti/ URLs redirect there.
- Content repo: **`sriniurs/srini-bhakti`** (GitHub Pages). Paths have no `/bhakti/` prefix, e.g. `/festivals/navaratri/`.
- Builder kit: **`sriniurs/sriniurs.github.io`** → `tools/bhakti-kit/`. It holds every builder script used so far.
- Size: about 690 index pages. The doors (sections) are `gods`, `hymns`, `scriptures`, `temples`, plus festivals, Śrīvidyā, Tuḷunāḍu, Gaṇeśa, Hanumān, Subrahmaṇya, Home Pūjā, the Sixteen Saṃskāras, and How to read IAST.

---

## 1. Non-negotiable rules (all of them)

### Brand, people, contact
1. **Cover byline:** exactly **"Srini presents"**. Foreword signature: "With the blessings of the Devī / Lord, srini.presents 🙏".
2. **Characters:** Zappy asks, Prof. Bolt answers. Their exchange (a `talk` block) appears on most pages. Each exchange must add something new and never repeat the text above it.
3. **Logo:** the srini.presents logo (`/assets/brand/logo.png`, `img.brandtile`) goes **on the cover only**. Inner pages carry **no** logo, so no `img.pglogo`. In the kit `lib.py`, `LOGO=''`; keep it that way.
4. **Contact:** the only contact anywhere is **srini.presents@gmail.com**, shown in the "Share your thoughts" block. Never add YouTube, Instagram, Facebook or any social handle, and never add a FOLLOW block.
5. **Never write "comic"** in reader-facing text. Call it an "article" or "guide". The comic art style itself stays. The font name "Comic Neue" in CSS is fine.
6. **Footer** always ends with: "Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional."

### Language and content
7. **IAST only.** Write no Devanagari, Tamil, Kannada or other script anywhere on a page. Convert ṁ to ṃ. Even the symbol ॐ is written "Oṃ".
8. **Sanskrit text** must come from an authoritative edition **fetched in the session**, never from memory.
   - Good sources: shlokam.org, greenmesg.org, stotranidhi.com, devimahatmyam.aurobharati.in.
   - sanskritdocuments.org often fails to fetch; use the others.
   - Name the edition and its numbering in a note and in the footer.
9. **Never print secret or initiatory mantras** (bīja japa formulas, Mahāvidyā mantras). Describe them, don't give them.
10. **Timeless.** No timings, tickets, routes or visiting tips.
    - **No relative time** anchored to the day of writing: never "today is Puttari", "tomorrow is…", "this year's date", "upcoming", "recently". Describe recurring festivals by month, tithi, nakṣatra or season; a fixed date only if it never changes (Paryāya on 18 January, Bisu 14–15 April).
    - **Dated past events are fine** when true and sourced ("on 10 September 2025 the chariot…", "consecrated 26 March 1820").
    - **No visitor-guide content at all:** no "Visiting" page, no distances ("about 35 km from X" → "near X"), dress codes, best seasons, weather, crowds-planning, lunch timings, nearby treks, "check timings". The site is for knowledge seekers, not tourists; every page is history, legend, ritual, meaning, culture.
11. **Neutral.** On disputes (rival lists, sectarian claims, contested history) write "traditions differ" and give both sides.
12. **Mark interpretation** as interpretation ("Many read this as… (Interpretation.)").
13. **Meanings are our own plain-English renderings.** Never copy a translation.
14. **Verify, don't recall.** Facts come from sources fetched in the session (Wikipedia, temple or shrine board sites, Purāṇa editions). Common knowledge is fine. Anything unchecked goes on the Sources page under "Sources differ / unverified".
15. **Copyright.** Never reproduce song lyrics, poems or long passages from modern sources. Short quotes only, under 15 words.

### Depth standard (Srini is strict about this)
16. **At least 14 pages** per article; typical is 16–24. A 9–11 page article is a failure.
17. **A picture on every page** except Contents and Sources. Each picture is a flat SVG made for that page's subject, with its own `aria-label`. Generic rows of people are a last resort.
18. **Tables only on At a Glance.**
    - Every other page is prose (3–5 paragraphs, each opening with a **bold lead-in**), or a 5-frame story strip, or a 2×n card grid.
    - Hymn verse pages keep their small "Word / Meaning" table; that is the series format.
19. **Each content page** has its own subject, picture, prose, a Zappy/Bolt talk and a one-line `key` takeaway.
20. **Cover every angle:**
    - origin and name;
    - every attached story, each told in full on its own page;
    - scripture, with the verse where one exists;
    - iconography;
    - how it is kept, with Karnataka/Mysuru practice whenever it exists;
    - meaning and the readings of teachers;
    - links to the rest of the site;
    - a Sources page with an honest unverified list.
21. If a batch is too big to do at full depth, build fewer articles at full depth and say what remains. Never ship thin.

### Commits
22. Commit as **`Srinivas Deep Urs <sriniurs@yahoo.com>`** with these trailers (use the new chat's own session URL):
    ```
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>   (use the model name the new chat's attribution reminder gives)
    Claude-Session: <this chat's session URL>
    ```
    Run `git pull --rebase` before every push. If a push is rejected, pull with rebase and push again.

---

## 2. Setup in a fresh chat

```bash
# attach both repos with push access (add_repo tool), then:
git clone https://github.com/sriniurs/srini-bhakti /home/claude/srini-bhakti
git clone https://github.com/sriniurs/sriniurs.github.io /home/claude/sriniurs.github.io
cd /home/claude/sriniurs.github.io && bash tools/bhakti-kit/setup.sh   # installs kit to /home/claude/work
# if setup.sh does not copy everything, copy by hand:
mkdir -p /home/claude/work/navaratri
cp -r tools/bhakti-kit/work/navaratri/* /home/claude/work/navaratri/
cp tools/bhakti-kit/maintenance/* /home/claude/work/
cp tools/bhakti-kit/maintenance/painted.json /tmp/painted.json
```

Tools needed: python3, playwright with Chrome (`/usr/bin/google-chrome`), pypdf, pdftoppm (poppler), PIL. If network installs are blocked, use what is already installed.

Local test server, used by the checks:
```bash
mkdir -p /home/claude/srv/test
(curl -s -o /dev/null localhost:8765/ || (cd /home/claude/srv && nohup python3 -m http.server 8765 >/dev/null 2>&1 &))
```
The server dies between turns. Restart it before every check.

Also read in the kit: `tools/bhakti-kit/README.md`, `HANDOFF_SRIVIDYA.md`, and `PUBLISHING.md` ("Bhakti section") in the site repo.

---

## 3. The builder framework (`/home/claude/work/navaratri/`)

This is the current, preferred framework. Older series libraries (`devim/dmc.py`, `shakti/*_common.py`, `mysuru/`, `triranga/`, `vsn/` and others) also live in `tools/bhakti-kit/work/`. Start from the closest example so the look matches.

### `pages.py` (imported as `PG`): the page assembler
- `PG.configure(base, parts, theme, series, sign, short)`
  - `base` is the URL folder, e.g. `'/temples-of-india/'`.
  - `parts` is `[(slug, title, tagline), …]`. One entry means a standalone article; several mean a series with Part n of N and prev/next links.
  - `theme` is `'red'` (Devī), `'blue'` (Viṣṇu) or `'navy'` (Śiva and mixed temples).
  - `sign` is `'Devī'` or `'Lord'`, used in the foreword signature.
- `PG.CFG['backurl']` and `PG.CFG['backname']` set the "Back to …" link for standalone articles.
- `PG.OUT='outd/<folder>/'` is the output folder; files go to `OUT/<slug>/index.html` and `cover.svg`.
- Page functions, each returning a `<section>`:
  - `foreword(i, paras, talk)`: Where We Are, with signature and series line.
  - `glance(rows, figsvg, talk, key)`: the At a Glance table. The only table allowed.
  - `reading(id, TITLE, sub, figsvg, paras, talk, key)`: picture plus prose panel.
  - `story(id, TITLE, sub, stripsvg, lead, [5 steps], talk, key)`: a 3-panel strip plus 5 numbered frames.
  - `cards(id, TITLE, sub, figsvg, [(emoji, h4, text)…], talk, key, intro)`: picture plus a 2-column card grid.
  - `verse(...)`: a hymn verse page.
  - `end(i, [5 lines], nextText, keyText)`: On One Page.
  - `sources([(label, text)…], unverified, study)`: Sources & Notes.
  - `build(i, kicker, coverSvg, caption, howText, metaDescription, pages)`: assembles the cover (cover2 masthead), foreword, auto Contents, all pages and the Share block, then writes the files.
  - `covart(label, inner)`: the 440×220 cover picture.
- `talk` format: `[('z', 'Zappy line'), ('b', 'Bolt line')]`.

### `fx.py` / `fig.py`: flat SVG figure helpers
- **Layout and canvas:**
  - `svg(w, h, label, inner)`;
  - `g(x, y, scale, inner, flip=False)` places a figure;
  - `lab(x, y, text, size)` adds a label;
  - `strip(label, [panel(...)×3], [3 captions])` makes the 460×210 story strip, with `panel([(figure, scale), …], bg)`.
- **Gods and people:** `devi(skin, sari, items=(…), fierce, hair_open, child_lap, seat)` (items: trident, lotus, sword, bell, rosary, kamandalu, pot, discus, conch, mace, damaru, hook, vajra, book, abhaya, bow, arrow, redpot), `shiva()`, `vishnu()`, `sheshashayi()`, `krishna()`, `krishna_child()`, `lakshmi()`, `ganesha(c, seat, arms)`, `hanuman()`, `narasimha()`, `vamana()`, `god(c)`, `sage(c)`, `person(c, seat)`, `namaste(c)`, `child()`, `baby()`, `mother()`, `demon(c)`.
- **Animals:** `garuda()`, `nandi()`, `lion()`, `cow()`, `elephant(howdah)`, `bird(c)`, `mouse()`, `buffalo()`.
- **Objects:** `linga()`, `palace()` (temple), `shrine()`, `mountain(c, snow)`, `tree(c)`, `river(w, y)`, `moon()`, `sun()`, `lamp()`, `fire()`, `pot()`, `kalasha()`, `plate()`, `coconut()`, `coins()`, `lotus(c, c2)`, `tulasi()`, `vina()`, `book()`, `scroll()`, `rosary()`, `trident()`, `damaru()`, `conch()`, `discus()`, `mace()`, `sword()`, `bow()`, `arrow()`, `flag(c)`, `pillar_fire()`, `swing()`, `cradle()`, `rangoli()`, `modaka()`, `leaf()`, `gooseberry()`, `durva()`, `umbrella()`, `boat_lamp()`.
- Watch the coordinates. Helpers that already take `(x, y)` must not also be wrapped in `g(...)` at a non-zero position, or the figure is double-offset and lands off canvas. Check the contact sheet.

### Example builders to copy
| Kind | Builder | Notes |
|---|---|---|
| Temple guide, standalone (latest, 24 pages) | `navaratri/vd.py` (Vaiṣṇo Devī) | custom map, route, cave scenes |
| Deity guide (Gods door) | `navaratri/godlib.py` + `g_shiva.py`, `g_vishnu.py`, `g_devi.py`, `g_lakshmi.py`, `g_sarasvati.py`, `g_krishna.py`, `g_rama.py` | `deity(base, slug, title, tag, theme, sign, dict)`; the dict holds pages as `('r'\|'s'\|'c', …)` |
| Temple series in many parts | `navaratri/gtlib.py` + `ashta1-3.py`, `gt2.py`, `gt3.py` (17 Gaṇeśa temples) | `temple(i, dict)` |
| Festival series | `navaratri/p01.py…`, `ek.py` (Ekādaśī), `kartika.py`, `pradosha.py`, `pitru.py`, `sankranti.py` and others | |
| Add pages and pictures to an existing live article | `navaratri/pk.py` (Pañca Kedār), `gr.py` (Veda / Gītā), `maintenance/khadga.py` | edits the live HTML in place |
| Scripture in parts (red) | `devim/dmc.py`, `devim/pNN.py` | |
| Hymns | `vsn/`, `bhaja/`, `suprabhatam/`, `madhura/`, `acyuta/`, `mahimna/` | |

---

## 4. Page anatomy (what every article contains)

1. **Cover** `section.page.cover.cover2`, the masthead design. No rays, no yellow burst, no series bar. Two zones inside a page framed in dark brown (#2a1d16):
   - **Masthead**, a band in the theme colour (navy #15365a, deep red #8e1f17, deep blue #1d4f8a), containing:
     - the logo tile (the only logo in the article);
     - "SRINI PRESENTS" in small white caps;
     - a kicker pill of 2–4 items joined by " · ", no more than about 60 characters (series parts start "PART n OF N · ");
     - the huge cream serif title in caps;
     - a white serif subtitle: "<what it covers> · explained and illustrated".
   - **Body** in light grey, containing:
     - the cover SVG on a pale tinted panel;
     - an italic caps caption;
     - the CAST block (Zappy and Prof. Bolt);
     - a bubble that opens "HOW THIS WORKS:".
   - The cover CSS includes `max-height:340px` on the cover art so the cover fits one A4 sheet.
2. **Where We Are** (`#foreword`): 2–3 paragraphs, the signature, a talk, and the series line.
3. **Contents** (`#contents`): built automatically from the page titles.
4. **At a Glance** (`#glance`): a picture plus a table of 8–10 rows.
5. **Content pages** (9–15 of them): reading, story and card pages as above.
6. **Words to Know** (`#glossary`): cards with a picture.
7. **On One Page** (`#end`): five summary lines, a "What's next?" talk and a `key`.
8. **Sources & Notes** (`#sources`):
   - a reading panel of sources;
   - a "Sources differ / unverified:" line;
   - the study-notes footer line with the fixed last sentence.
9. **Share your thoughts** block, after the pages:
   - a cream card with a serif heading and the line "If an article touched your heart, or you have a suggestion, reflection or correction, I would love to hear from you.";
   - a rust button: `mailto:srini.presents@gmail.com`, text "Write to me · srini.presents@gmail.com".

Links inside dark `.key` boxes must be light blue: `.key a{color:#8fd3ff;text-decoration:underline}`.

---

## 5. Checks (before every upload)

Run from `/home/claude/work/navaratri`:

```bash
rm -rf /home/claude/srv/test/NAME && cp -r outd/<folder>/<slug> /home/claude/srv/test/NAME
python3 chk.py test NAME        # prints: NAME 390 <pdfPages> <sections> OK | <<< FIX
python3 tall.py NAME            # tallest sections in print; overflow starts at about 965–1000 px
```

1. **Mobile:** the width must print as **390**, meaning no sideways scroll.
2. **Print:** the PDF page count must equal the number of sections. If a page spills over:
   - shorten its text, or
   - shrink that page's figure with `maintenance/fitfix.py <repo-relative-path>`, which adds `max-height` to the overflowing figure, or
   - split the page in two.
   - Never shrink fonts.
3. **Contact sheet:** look at it every time, for broken or empty figures, overlapping labels and cramped covers. `chk.py` writes `/tmp/NAME.pdf`; make the sheet with:
   ```bash
   pdftoppm -r 26 -png /tmp/NAME.pdf /tmp/cs_NAME
   # then paste the PNGs into a grid with PIL and Read the image
   ```
4. **Links:** every `href="/…"` in the new page must resolve to `./path/index.html` in the repo.
5. **Rules:** no Devanagari (`grep -c '[ऀ-ॿ]'` must be 0); no "comic" outside CSS; 14 or more pages; a picture on every content page.
6. Optional site-wide checks: `maintenance/wcheck.py` (mobile width, all pages) and `maintenance/linkchk.py`.

---

## 6. Upload procedure (careful: generators churn the repo)

```bash
cd /home/claude/srini-bhakti && git pull -q --rebase
mkdir -p <dest> && cp /home/claude/work/navaratri/outd/<folder>/<slug>/* <dest>/      # index.html + cover.svg
```

### 6a. `catalog.json` entry (one per article or series folder)
- Insert the entry with Python and write it back with `json.dumps(c, ensure_ascii=False, indent=1)`. **`indent=1`** keeps the file's existing format; any other indent rewrites the whole file.
- Fields:
  - `path`, e.g. `"/temples-of-india/vaishno-devi/"`;
  - `door`: gods | hymns | scriptures | temples;
  - `deities`: any of shiva, vishnu, devi;
  - `group` (temples only): circuits | places;
  - `tile`: the hub card HTML. The order of entries is the order on the hubs.
- Tile template:
  ```html
  <li><a href="/PATH/"><div class="tile-art" style="background:#f6e3e1"><img src="/PATH/cover.svg" width="380" height="268" alt="" loading="lazy"></div><div class="tile-copy"><strong class="label">Guide · Devī</strong><h2>Title</h2><p>One-line description.</p><span class="read">Read ↗</span></div></a></li>
  ```
  Use background #f6e3e1 for red and #e3eaf3 for navy or blue.

### 6b. Hub pages: **do not commit the generator's mass output**
- `python3 .github/bhakti_hubs.py --strict` regenerates the hubs, but it also rewrites about 630 files (collection counts in every nav) and **strips the painted `<!-- library:card -->` images** from hub tiles.
- The procedure that works:
  1. Run `python3 .github/bhakti_hubs.py --strict`.
  2. Copy out only the hub pages that gained your new tile, e.g. `gods/index.html`, `devi/index.html`, `temples-of-india/index.html`, to `/tmp/new_*`.
  3. Run `git checkout -- .`, which reverts the churn and catalog.json too; save catalog.json to /tmp first and restore it after.
  4. Write the saved hub pages back, **re-inserting the painted card blocks** from the HEAD version:
     ```python
     import re
     cards={m.group(1):m.group(2) for m in re.finditer(r'<a href="([^"]+)"><div class="tile-art"[^>]*>(<!-- library:card -->.*?<!-- /library:card -->)',old,re.S)}
     new=re.sub(r'<a href="([^"]+)"><div class="tile-art"[^>]*>(?!<!-- library:card)',lambda m:m.group(0)+cards.get(m.group(1),''),new)
     ```
  5. Verify: the count of `library:card -->` is unchanged, and the tile count rose by exactly the number of new articles.
- `festivals/index.html` and `hymns/index.html` are hand-made; add tiles to them by hand.
- Delete `.github/__pycache__/` before committing.

### 6c. Share images (link preview)
- `cd /home/claude/work && python3 og.py /home/claude/srini-bhakti --all <repo-relative paths…>`
- This makes `og-share.jpg` (1200×630) from the painted collection card, a logo band and the title, and adds the og meta tags. It needs `/tmp/painted.json`; `og.py` falls back to `painted.json` beside itself.
- Srini specifically wants the painted card pictures in link previews.
- A blank WhatsApp preview is usually WhatsApp's cache, not a bug.

### 6d. Commit and push only the intended files
```bash
git add catalog.json <hub pages> <new dirs>
git -c user.name="Srinivas Deep Urs" -c user.email="sriniurs@yahoo.com" commit -m "…" -m "Co-Authored-By: …" 
git pull -q --rebase && git push
```
`git status --short` must be clean afterwards. CI (`bhakti-seo.yml`) refreshes the sitemap and SEO automatically.

### 6e. Save builders to the kit
Copy every new builder or library to `sriniurs.github.io/tools/bhakti-kit/work/navaratri/` (or `maintenance/`), then commit and push the same way. Save templates as `*.html.tmpl`, never `.html`.

---

## 7. Gotchas learned

- **Hub regeneration** churns about 630 files and strips the painted tile images. Never commit that; use 6b.
- **`catalog.json` must keep `indent=1`.** A different indent rewrites the whole file.
- **Figure double-offset.** A helper with default x/y wrapped in `g()` lands off canvas (the Vaiṣṇo Devī piṇḍīs page once rendered empty).
- **Print overflow.** A section taller than about 965–1000 px in print spills onto two A4 sheets. Use `tall.py` to find it.
- **Pages that print onto a second sheet.** Covers could spill until `max-height:340px` was added to the cover art. Glance or map pictures with many rows can also do it; shrink the picture rather than the font.
- **Contact sheet reveals what the checks miss:** empty or blank figures, overlapping labels, cramped kicker pills.
- **Folder names lie.** Before saying a topic is missing, search the page **titles** and **body text** across all `index.html` files, not just folder names. Srini caught this once: Cāmuṇḍeśvarī, Tirumala and Mēlukōṭe existed under other folders. Use:
  ```bash
  find . -name index.html -not -path "./.git/*" | while read f; do echo "${f#./}|$(grep -o '<title>[^<]*' "$f"|head -1)"; done > /tmp/titles.txt
  ```
- **Link targets that differ from the obvious:**
  - Gaṇeśa festivals live under `/ganesha/festivals/` (ganesha-chaturthi, sankashti-chaturthi), not `/festivals/`.
  - There is **no Gaṅgā Dussehrā page**.
- **Upload scripts must copy only the new files.** Re-copying old drafts overwrites live fixes.
- **Shared fact-table pages, now fixed.** 230 older articles had fact tables on inner pages; all were converted to prose with `maintenance/untable.py`. Don't reintroduce them.
- **Hymn verse "Word / Meaning" tables** (about 2,160) are the series format and were deliberately left. That is a pending decision; see section 9.

---

## 8. Current state of the site

All earlier batches are live and checked. Done in the last sessions:

- **Covers:** every cover is in the cover2 masthead style, with the logo on the cover only; the old per-page logos were removed.
- **Sources pages:** 103 articles were missing one; all now have one.
- **Share images:** all about 545 articles have `og-share.jpg`, using the painted card pictures.
- **Hymns:** 26 hymn texts were checked against editions, and wording errors corrected (Mahiṣāsura Mardinī rebuilt to the standard 21 verses; Kāśī Viśvanātha, Annapūrṇā, Liṅgāṣṭakam and Kanakadhārā fixed).
- **Expanded to 14+ pages:**
  - Khaḍgamālā, 13 parts, with a picture on every page;
  - all 17 Gaṇeśa temples (Aṣṭavināyaka overview plus 8, Gokarṇa, Iḍagunji, Hampi, Doḍḍa Gaṇapati, Ucchi Pillaiyār, Pillaiyārpaṭṭi, Madhūr, Siddhivināyak Mumbai);
  - Pañca Kedār, all 6;
  - Gaṇapati in the Ṛgveda;
  - the Gītā overview.
- **Fact tables:** 1,948 fact tables outside At a Glance were turned into prose, across 230 articles.
- **New Temples guide:** **Vaiṣṇo Devī**, `/temples-of-india/vaishno-devi/` (24 pages).
- **New Gods guides:**
  - `/shiva/who-is-shiva/` (19 pages);
  - `/vishnu/who-is-vishnu/` (20);
  - `/devi/durga-and-parvati/` (18);
  - `/devi/lakshmi/` (17);
  - `/devi/sarasvati/` (17);
  - `/vishnu/krishna/` (17);
  - `/vishnu/rama/` (17).
- **Gods hub:** now 13 guides:
  - Daśa Mahāvidyā, Aṣṭa Lakṣmī, Śrīvidyā, Śiva's Family and Symbols, Subramanya, Daśāvatāra, Hanumān, Gaṇeśa;
  - plus the 7 new guides above.

Every article is at least 14 pages, has a Sources page and a share image, contains no Devanagari, and passes the mobile check.

---

## 9. Pending (needs Srini's decision first)

1. **Pictures on verse deep-dive pages.** About 4,000 inner pages in 354 articles have no picture. These are mostly the "deep dive" second page of a verse, designed as text pages:
   - Gītā deep dives: 700;
   - Garuḍa Purāṇa: 288;
   - Śrīvidyā deities: 223;
   - Lalitā Sahasranāma: 187;
   - Viṣṇu Sahasranāma: 181.

   Srini has not yet said whether to keep them text-only or add a small picture to each. Ask.
2. **Hymn "Word / Meaning" tables** (about 2,160). Keep them as the series format, or convert them to prose? Ask.
3. **Painted tile pictures** for the 8 new cards (Vaiṣṇo Devī plus the 7 Gods guides). Their hub cards show the article's own `cover.svg` instead of a painted picture like the neighbouring cards. The painted images live in `/assets/editorial/bhakti-library/painted-tile-*.webp`, with the map in `painted.json`. Making new painted tiles needs an image pipeline; flag it if asked.

---

## 10. Ideas for new content (checked against the site; none has its own article yet)

### Gods door: still missing
- Brahmā
- Dattātreya (only appears as a Śrīvidyā teacher)
- Ayyappa (only Sabarimala as a temple)
- The Navagrahas
- Sūrya
- Śani
- Kāla Bhairava as a deity guide (only the hymn exists)
- Narasiṃha as a full guide (only an avatāra page plus Ahobilam and Simhācalam)
- Gaṅgā, the river goddess
- The Sapta Mātṛkās
- Garuḍa and Nandi, the divine vehicles
- Jagannātha
- Viṭṭhala of Paṇḍharpur
- The Vedic gods: Indra, Agni, Vāyu, Varuṇa

Builder: `godlib.py`. Śiva, Viṣṇu and Kṛṣṇa use navy or blue; Devī goddesses use red.

### Hymns (quick single articles, in hymn format with fetched text)
- Ādityahṛdayam
- Śrī Sūktam
- Dakṣiṇāmūrti Stotram
- Rāma Rakṣā Stotram
- Navagraha Stotram, one part for each planet

### Scriptures
- **Rāmāyaṇa by kāṇḍa.** Bāla, Ayodhyā and Araṇya kāṇḍas and the Uttara kāṇḍa are missing; Kiṣkindhā, Sundara and Yuddha are covered through the Hanumān stories.
- **Upaniṣads**, one each: Īśa, Kena, Kaṭha, Māṇḍūkya and others.
- **Mahābhārata** in parts.
- **Bhāgavata stories:** Prahlāda, Dhruva, Gajendra.

### Karnataka
- Purandara Dāsa and the Haridāsas
- Basavaṇṇa and the vacanas
- (Hampi, Belūr–Haḷebīḍu, Banaśaṅkarī, Sāvadatti, Gāṇagāpura: DONE 25 Nov 2026, see §13)

### Other India
- Paṇḍharpur and the Vārī
- Śrīraṅgam as a full temple guide

### Practice and festivals
- Ārati
- Rudrākṣa
- Sandhyāvandana for beginners
- Datta Jayantī
- Gītā Jayantī
- Vasant Pañcamī

### Existing collections (do not duplicate)
- **Festivals:** akshaya-tritiya, deepavali, dhanurmasa, ekadashi, guru-purnima, hanuman-jayanti, holi, kartika, krishna-janmashtami, maha-shivaratri, makara-sankranti, naga-panchami, navaratri, panchanga, pitru-paksha, pradosha, rama-navami, ratha-saptami, shravana-purnima, ugadi, vaikuntha-ekadashi, varamahalakshmi.
- **Temples of India:** 12-jyotirlingas, 18-shakti-peethas, ahobilam, andhra-pradesh (annavaram, lepakshi, mantralayam, simhachalam, tirumala, vijayawada-kanaka-durga), around-mysuru (br-hills, chamundeshwari, gopalaswamy-betta, karighatta, melukote, mm-hills, mudukutore, muguru, nanjangud, nimishamba, palace-temples, t-narasipura, talakadu, tipu-and-the-temples, uttanahalli), char-dham, how-to-read-a-hindu-temple, karnataka (gokarna, horanadu-annapurneshwari, murudeshwara), kerala (aranmula, chottanikkara, guruvayur, kodungallur, mannarasala, padmanabhaswamy, parassinikadavu, sabarimala, vadakkunnathan, vaikom), kumbh-mela, muktisthalas, pancha-bhuta-sthalas, pancha-kedar, sapta-puri, tamil-nadu (kanchipuram-varadaraja, kumbakonam, palani, thanjavur, tiruchendur), triranga, vaishno-devi.
- **Other sections:**
  - Tuḷunāḍu: temples (Udupi, Dharmasthala, Kaṭīl and more), daiva, culture, art.
  - Śrīvidyā, about 130 articles: temples including Śṛṅgeri, Kollūr, Madurai, Kāñcī.
  - Gaṇeśa: forms, temples, stories, hymns, festivals.
  - Hanumān.
  - Subrahmaṇya: Ghāṭi, Kukke, Ṣaṣṭhī, Skanda.
  - Śiva hymns.
  - Viṣṇu: Gītā (all chapters), Sahasranāma, Garuḍa Purāṇa, Daśāvatāra.
  - Devī: Devī Māhātmya (19 parts), Aṣṭa Lakṣmī, hymns.

---

## 11. Srini's standing preferences (from memory)

- Wants straight, frank, unpolished answers, without diplomatic hedging or boilerplate disclaimers.
- Bhakti: the logo on the cover only. Everything else on srini.presents carries the logo.
- The only contact is srini.presents@gmail.com, spelled with the "s". No YouTube, Instagram or Facebook.
- Never call anything a "comic" in reader-facing text.
- Zappy asks, Prof. Bolt answers. Their roles stay general, not tech-specific.
- Byline "Srini presents".
- Reply briefly after uploads: what went live, the URLs, anything flagged.
- Workflow words:
  - **"next"**: build the next article in the current series;
  - **"upload"**: publish what was reviewed;
  - **"create and upload"** / **"finish and upload all"**: build, check and publish without waiting.
- When asked what's pending, check the site properly (titles and body text) before listing, and order the list by importance.

---

## 13. Latest session (25 Nov 2026): what was added and how

### Live now
- **Durgā Namaskāra** `/tulunadu/culture/durga-namaskara/` (26 pp). Builders `dnp.py`, `dnp2.py`, figures `dnfig.py`.
- **Tulu Nadu Festivals, 9 parts** `/tulunadu/festivals/{tulu-year, mangaluru-dasara, udupi-festivals, laksha-deepotsava, polali-jatre, katil-festivals, kodi-habba, bappanadu-jatre, siri-jatre}/`. Builders `tn_common.py` (`PG.OUT='outt/tulunadu/festivals/'`), `tn1.py…tn9.py`. The hub `tulunadu/festivals/index.html` is hand-made; tiles point to the 9.
- **Temples of Karnataka, 5 new** `/temples-of-india/karnataka/{hampi-virupaksha, belur-halebidu, savadatti-yellamma, ganagapura-dattatreya, banashankari}/`. Builders `kt_common.py` (`outk/…`), `kt1.py…kt5.py`. Śṛṅgeri, Kollūr, Kukke, Dharmasthaḷa, Melukōṭe already existed and are linked, not rewritten. `.github/bhakti_hubs.py` has `KARNATAKA_ENTRIES` + an "Also in Karnataka" block.
- **Kodagu: Culture and Festivals, 12 parts** `/kodagu/{kodavas, puttari, kailpodh, kaveri-sankramana, igguthappa, mand-and-dances, ainmane, life-rites, village-deities, temples, kodava-year, communities}/` (14–18 pp each). Builders `kd_common.py` (`PG.OUT='outd2/kodagu/'`, theme navy, sign "Kāverī Amma", Kodava figures: `kodava_man`, `kodava_woman`, `gun`, `kutti`, `nere`, `paddy`, `hills`, `coffee`, `kola_dancer`, `dudi`, `ainmane`, `hanging_lamp`), `kd1.py…kd12.py`.
- Shared figure library for these series: `tfig.py` (+ `tfig_base.py`): `flame, lamps_row, tulu_temple, vimana, crowd, float_cart, flagpole, fireworks, tank, raft, map_frame, pin, tl_strip, RATHA, LINGA` etc. `fig.strip`, `fig2.fig_row/panel`, `pages.story(id,T,sub,strip,lead,[3 lines],talk,key)` (3 frames in these series).

### Home-page restructure: "Karnataka Cultures"
- The home collection tile that was "Tulu Nadu" is now **Karnataka Cultures → `/karnataka-cultures/`**, a hand-made hub with two tiles: Tulu Nadu and Kodagu. `/kodagu/` is a hand-made hub with the 12 parts. Both made by `navaratri/mkhub.py` (clones the head of `tulunadu/festivals/index.html`; sets og:image per hub; re-run it if Kodagu tiles change).
- `index.html`: tile `li.library-theme-tulu` → href `/karnataka-cultures/`, label "Karnataka Cultures", `data-library-count="Karnataka Cultures"`; the article-index `<details>` is "Karnataka Cultures · N articles" listing Kodagu hub + 12 parts + Tulu Nadu items.
- `scripts/library_registry.py`: COLLECTIONS maps the 7th group to `/karnataka-cultures/`. `scripts/sync_collection_counts.py`: GROUPS label "Karnataka Cultures" (that script already fails on HEAD with "Gods and Goddesses 1/0" — pre-existing, CI does not run it; ignore).
- Breadcrumbs are now auto: Home › Karnataka Cultures › Tulu Nadu/Kodagu › page.

### Upload procedure that worked this session (simpler than §6b)
```bash
cd /home/claude/srini-bhakti && git pull -q --rebase
cp /home/claude/work/navaratri/<out>/<path>/<slug>/* <path>/<slug>/
cd /home/claude/work && python3 og.py /home/claude/srini-bhakti --all <path>/<slug>   # per article
cd /home/claude/srini-bhakti
python3 scripts/library_registry.py      # paints crumbs, cards, search, registry json
python3 scripts/seo_sync.py              # run until it says "sitemap current"
python3 scripts/library_registry.py --check; python3 scripts/seo_sync.py --check   # what CI runs
rm -rf scripts/__pycache__ .github/__pycache__
# linked-works svgs: keep only those referenced by pages, else delete before pull
git add -A && git commit … && git pull -q --rebase && python3 scripts/seo_sync.py --check && git push
gh api repos/sriniurs/srini-bhakti/actions/runs?per_page=4 --jq '.workflow_runs[]|[.name,.head_sha[0:7],.conclusion]|@tsv'
```
- CI workflow `bhakti-seo.yml` runs only `library_registry.py --check` and `seo_sync.py --check`. If it fails right after a push it is usually a race with CI's own sitemap commit: pull, re-run seo_sync, push.
- For catalog.json / `.github/bhakti_hubs.py` work see §6a/6b (needed for temples hubs, not for hand-made hubs).
- The shell cannot reach bhakti.srinipresents.com (proxy 403); verify locally with `python3 -m http.server` + playwright screenshots.

### Checks
- `navaratri/tchk.sh <outdir> <root> <slug…>` copies to `/home/claude/srv/<root>/` and runs `chk.py` (prints `slug 390 pdfPages sections OK`). Its "spill?" lines are **false positives** when a page title has diacritic caps (Ō, Ē, Ṅ…).
- **tchk.sh hang gotcha:** if the 8765 server is not running, tchk starts it inside a subshell that keeps the output pipe open, and the command never returns. Start the server first: `cd /home/claude/srv && (nohup python3 -m http.server 8765 >/dev/null 2>&1 &)` then run tchk with `timeout 250`.
- `sheet.sh <slug> <cols>` makes a contact sheet but can hang; instead `pdftoppm -r 28 -png /tmp/<slug>.pdf /tmp/pv_<slug>` + `montage … -tile 6x` and Read the PNG.
- Logo in downloaded HTML: `finish()` in the commons swaps the logo src to the absolute `https://bhakti.srinipresents.com/assets/brand/logo-clear.png`.

### Ideas offered but not yet built
- More Karnataka Cultures: Malenāḍu / Havyaka traditions; Nāḍahabba Mysuru Dasarā link-up; Uttara Kannaḍa (Gokarṇa culture, Yakṣagāna Baḍagutiṭṭu); North Karnataka jātres (Sāvadatti done; Mailāra, Yallamma, Siddhārūḍha).
- Gods door, hymns, scriptures, practice lists in §10 are still open.

---

## 12. Fresh-chat checklist (copy this into the first message)

1. Attach `sriniurs/srini-bhakti` and `sriniurs/sriniurs.github.io` with push access, and clone both.
2. Install the kit to `/home/claude/work`, copy `painted.json` to `/tmp/`, and start the 8765 server.
3. Read this handover, the kit README and the closest example builder.
4. Research the subject (WebFetch or WebSearch) and fetch any Sanskrit from an edition.
5. Write `<name>.py` from the closest builder. Aim for 16–24 pages, a picture on every page, prose only, and a Sources page with an unverified list.
6. Run `chk.py` until it prints OK, look at the contact sheet, check links, and grep for Devanagari and "comic".
7. Upload with section 6: catalog `indent=1`, hub tiles with painted cards restored, `og.py`, commit only the intended files, push.
8. Copy the builders to the kit and push.
9. Reply to Srini in 3–6 lines with the URLs and anything flagged.

---

## 14. NEXT JOB (Srini's request, 25 Nov 2026): "Why do we…" series, 10 parts

Build and upload all 10, each a short but **full-depth** article (14+ pages, picture on every page, Zappy/Bolt, Sources page with unverified list, no visitor info, no "today/tomorrow" dates):
1. Why do we do ārati?  2. Why do we wear tilaka?  3. Why do we take prasāda?  4. Why do we break a coconut?  5. Why do we ring the bell?  6. Why do we do pradakṣiṇā?  7. Why do we do namaskāra?  8. Why do we worship tulasī?  9. Why 108?  10. Why do we fast (upavāsa)?
- Checked 25 Nov: no existing article titles on these topics (only `/home-puja/`, which they should link to and from). Re-check titles + body text before building (see §7).
- Suggested base `/why-do-we/<slug>/` with a hand-made hub `/why-do-we/index.html` (clone `mkhub.py` approach), theme navy, sign "Lord". New `wd_common.py` modelled on `kd_common.py`; series of 10 with Part n of 10.
- Each article: origin and name; scriptural basis (fetch verses from an edition, IAST only); how it is done step by step at home and in temple, with Karnataka/Mysuru practice; regional variants (Vaiṣṇava/Śaiva/Śākta, Mādhva/Smārta); symbolism and teachers' readings (marked as interpretation); common myths vs what texts say; related stories; links (Home Pūjā, festivals, relevant deity guides).
- Add to the home page under the Practice/Festivals collection or a new collection only after asking Srini.

- PROGRESS: `wd_common.py` (PG.OUT=outw/why-do-we/) , `wd1.py` (ārati, 19 pp) , `wd2.py` (tilaka, 17 pp), `wd3.py` (prasāda, 16 pp), `wd4.py` (coconut, 15 pp), `wd5.py` (bell, 15 pp), `wd6.py` (pradakṣiṇā, 16 pp), `wd7.py` (namaskāra, 16 pp), `wd8.py` (tulasī, 16 pp), `wd9.py` (108, 15 pp) built and checked 25 Nov, NOT uploaded. Next: wd10 upavāsa … wd10. Then hub /why-do-we/ + upload.
