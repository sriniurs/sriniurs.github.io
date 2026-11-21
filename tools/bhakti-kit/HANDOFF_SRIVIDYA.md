# Śrīvidyā series: handoff for a new chat

Paste this whole file into a new chat as the first message, or attach it and say:
**"Read this handoff and start Day 1."**

---

## 1. Who I am and how to work with me

- I am **Dr. Srinivas Deep Urs (Srini)**, an orthopaedic surgeon in Mysuru. I run **srinipresents.com**, a GitHub Pages site in the repo **`sriniurs/sriniurs.github.io`** behind Cloudflare.
- I want **frank, unpolished answers**: no hedging and no boilerplate disclaimers.
- **Goal for this week:** finish the whole **Śrīvidyā section** (about 90 articles) in 7 days, then move on to the next series.
- **Workflow:** build → check → upload. When I say "create and upload", do both without asking again. Use a task list. Send me the live links at the end of each batch.
- **New account?** Connect GitHub (Settings → Connectors) so the chat can push to `sriniurs/sriniurs.github.io`.

## 2. House rules for every Bhakti article (non-negotiable)

1. **Format:**
   - The cover byline is always **"Srini presents"**, and the foreword is signed **"srini.presents"**.
   - The characters are always **Zappy** (a curious young learner who asks) and **Prof. Bolt** (a wise mentor who answers).
   - Use the comic-panel style of the existing kits.
2. **Language:** English only, with Sanskrit in **IAST**. Meanings are our own plain-English renderings.
3. **Footer:** must end with *"Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional."*
4. **Detail rule (standing):** every article is real reference material, never a token page.
   - Hymns and scriptures are done **Gītā-style**: every verse on 2 pages. Page 1 has the chant, a picture, the meaning and the key words. Page 2 is a deep dive.
   - Deity and temple articles: every page has a facts table, a Zappy/Bolt exchange and a **deep-dive panel of new material** (2–3 paragraphs).
   - **The deep dive must never repeat page 1** (no repeating the glosses or the meaning).
   - Pages should be about 70% full or more.
5. **No secret mantras.** Never reproduce, assemble or explain the Pañcadaśī, Ṣoḍaśī, Bālā or any initiatory mantra, nyāsa, dīkṣā or pūjā procedure.
   - Explaining names, stories, philosophy, Śrīcakra geometry, deities, temples and music is fine.
   - For bījas such as hrīṃ, explain the meaning, never the ritual use.
   - In the Triśatī, say that the names follow a mantra given at initiation, but never spell out the order as a mantra.
6. **Neutral on disputes.** Present each school's reading (Śaṅkara, Rāmānuja, Madhva, Śākta schools) side by side without taking sides. Flag later or folk tellings as such.
7. **Sources page at the end of every article,** with a "Sources differ / unverified" note. Never invent attributions such as "X says…". If unsure, write "commentators" or "tradition".
8. **Texts:**
   - Never build a long hymn from memory. Use a text PDF I supply; Vaidika Vignanam PDFs are fine.
   - Modern copyrighted hymns (for example the Aṣṭalakṣmī Stotram) are described, never printed.
9. **Never call Hanumān or the Rāmāyaṇa army "monkey".** Use **vānara** or the name.
10. **Temples of India rules:** timeless, not touristy. No travel, stay or best-season pages, no road or trek distances.
11. **Every tile on every series index page gets a small SVG illustration.** No plain number circles.
12. **Placement:** placement follows `bhakti/catalog.json`.
   - Doors are **gods, hymns, scriptures and temples**.
   - The `deities` field takes `shiva`, `vishnu` or `devi` (the first one decides the hub).
   - Existing URLs never change.

## 3. Setup in a fresh chat

```bash
git clone https://github.com/sriniurs/sriniurs.github.io.git /home/claude/sriniurs.github.io
cd /home/claude/sriniurs.github.io
bash tools/bhakti-kit/setup.sh            # installs builders to /home/claude/work, check.py to /home/claude/check.py
cat tools/bhakti-kit/README.md            # which library to use for which kind of article
```

- **Needs:** python3, Chrome (`/usr/bin/google-chrome`), pypdf, poppler (`pdftoppm`) and Pillow. The `check.py` script uses headless Chrome.
- **Pull before building.** Some builders read live pages for their head and CSS.

## 4. Which kit to use (templates that already work)

| Article type | Copy this | Notes |
|---|---|---|
| **Devī deity series** (red) | `work/shakti/al_common.py` + `al_forms*.py` (Aṣṭa Lakṣmī) | `P(id,title,sub,rows,talk,extra,figure)`, an `EX` dict of deep-dive paragraphs per page id, and `albuild()`. The cover series line is replaced in `albuild`; change it to "ŚRĪVIDYĀ · A REFERENCE GUIDE". |
| Older Devī deity style | `work/shakti/mv_common.py` (Mahāvidyās) | Has the `KAM`, `GAJA` and `LOTUS` drawings. |
| **Hymn verse by verse, Devī red** | `work/lalita/lk.py` + `trishati.py` + `la/lb/lc.py` | `X(n,title,LS(...),meaning,[(name,gloss)...],ctx,read,life,key)`. `hymn(P,TX,label)` builds it; `recolor()` turns the blue kit red. `LAL()` is the Lalitā drawing. Text goes in `ltx.py`, one line per verse as `n|half1|half2`. Set `tocper=30` when there are many sections, or the contents page spills. |
| Hymn, Viṣṇu blue | `work/hanuman/hk.py` + `calisa.py` | Same engine without recolouring. |
| Single festival or deity article | `work/shakti/vk.py` (Vaikuṇṭha Ekādaśī) or `hn1_who.py` | Built with `hn_common.py` / `dv_common.py`. |
| Śiva temple series (navy) | `work/shakti/pk_common.py` + `pk_all.py` (Pañca Kedār) | |
| Upload a series | `work/al_upload.py`, `work/hn_upload.py`, `work/lt_upload.py` | `up_lib.py` provides `cp()`, `tile()` and `index()`. Insert the catalog entry after a related entry. |

**Check every article.** Use `python3 /home/claude/check.py $PWD/FILE.html`, or `bash ../chk.sh build.py FILE.html`. Then:
- `scrollWidth` must be **390**.
- The PDF page count (`/home/claude/work/out.pdf`) must **equal** the number of `<section class="page"` sections.
- Look at a contact sheet (pdftoppm → PIL, as in the README) to see how full the pages are.

**Upload:**
1. Run the upload script.
2. `cd repo && python3 .github/bhakti_hubs.py --strict && python3 .github/site_nav.py && python3 .github/build_sitemap.py`
3. Run a link check over `bhakti/**/index.html`. It must print **broken 0**.
4. Copy the new builder scripts into `tools/bhakti-kit/work/`.
5. Commit as **Srinivas Deep Urs <sriniurs@yahoo.com>**, then `git pull --rebase` and push. CI commits often, so always rebase.
6. Check with `gh run list` that "pages build and deployment" succeeded, then fetch the live URL.

## 5. THE ŚRĪVIDYĀ PLAN (about 90 articles)

Root: **`/bhakti/devi/srividya/`**. It has its own series index with tiles. Add catalog entries:
- the series itself under `door:'gods'`, deity `devi`
- each verse-by-verse hymn under `door:'hymns'`
- the temples under `door:'temples'`

Cross-link these existing pages; don't rebuild them:
- `/bhakti/devi/lalita-trishati/`
- `/bhakti/devi/lalita-pancharatnam/`
- `/bhakti/devi/dasha-mahavidya/` (Ṣoḍaśī, Tārā, Bhairavī, Kamalā)
- `/bhakti/devi/ashta-lakshmi/`
- `/bhakti/devi/devi-mahatmya/`
- `/bhakti/temples-of-india/18-shakti-peethas/` (Kāmākhyā, Kāmākṣī, Kolhāpur)

### A. Foundations (6): `srividya/<slug>/`
1. `what-is-srividya`: the tradition, its goal, and why the mantra is guru-given (stated, never given)
2. `lalita-tripurasundari`: names and forms (Bālā, Lalitā, Rājarājeśvarī); the four weapons (noose, goad, sugarcane bow, five flower arrows); the five-Brahma couch
3. `history`: the Vedic Śrī, Kashmir and South Indian streams, and the Kādi and Hādi schools described without mantras
4. `texts`: a map of the Lalitopākhyāna (Brahmāṇḍa Purāṇa), Tantrarāja, Vāmakeśvara/Nityāṣoḍaśikārṇava, Paraśurāma Kalpasūtra, Tripurā Upaniṣad and Bhāvanopaniṣad
5. `shiva-shakti`: Kāmeśvara and Kāmeśvarī, and Śrīvidyā and Vedānta
6. `shankara-and-srividya`: Śṛṅgeri and Kāñcī; what is history and what is tradition

### B. Lalitopākhyāna story (6): `srividya/lalitopakhyana/part-1..6/`
1. Kāma burned; Bhaṇḍa born from the ash
2. Lalitā rises from the sacrificial fire; her wedding to Kāmeśvara
3. Śrīpura on Meru and the Cintāmaṇi palace
4. The war (Daṇḍinī/Vārāhī, Mantriṇī/Śyāmalā, Aśvārūḍhā, Sampatkarī, Jvālāmālinī's fire-wall)
5. Bālā kills Bhaṇḍa's sons; Gaṇeśa destroys the obstacle yantra; Tiraskariṇī
6. Bhaṇḍa falls; Kāma is revived

### C. Deities of Śrīvidyā (about 35): `srividya/deities/<slug>/`
- **Requested by Srini:** Tithi Nityā Devīs (overview + 15), Vārāhī, Pratyaṅgirā, Vāñchākalpalatā Gaṇapati, Ucchiṣṭa Gaṇapati, Nīla Sarasvatī
- **Added:** Rājaśyāmalā/Mātaṅgī (Mantriṇī; Kālidāsa's Śyāmalā Daṇḍaka described), Bālā Tripurasundarī, Kāmeśvara, Mahāgaṇapati with Siddhilakṣmī, Aśvārūḍhā, Sampatkarī, Tiraskariṇī, Kurukullā, Hayagrīva (teacher of Agastya)
- **Pratyaṅgirā and Ucchiṣṭa Gaṇapati:** cover story, form, temples and meaning only, in a protective and devotional frame. No rites and no abhicāra (sorcery).
- **Tithi Nityās** (overview `nityas/` plus one article each). Each one gets its tithi, form, weapons, colour, place on the Śrīcakra, meaning, and how the moon's phases map onto the Goddess:
  1. Kāmeśvarī
  2. Bhagamālinī
  3. Nityaklinnā
  4. Bheruṇḍā
  5. Vahnivāsinī
  6. Mahāvajreśvarī
  7. Śivadūtī
  8. Tvaritā
  9. Kulasundarī
  10. Nityā
  11. Nīlapatākā
  12. Vijayā
  13. Sarvamaṅgalā
  14. Jvālāmālinī
  15. Citrā
  16. Mahānityā (Lalitā herself)

### D. Śrīcakra (11): `srividya/srichakra/<slug>/`
1. `overview`: 9 interlocking triangles (4 Śiva, 5 Śakti), 43 small triangles, the 8- and 16-petal lotuses, the bhūpura; the flat and Mahāmeru forms; history and the Śaṅkara tradition
2. One article per āvaraṇa. For each: its shape, presiding Tripurā goddess, yoginī class and deities by name (public, as in Dīkṣitar), meaning, and the matching Navāvaraṇa kṛti (described).
   1. Trailokyamohana (bhūpura)
   2. Sarvāśāparipūraka (16 petals)
   3. Sarvasaṅkṣobhaṇa (8 petals)
   4. Sarvasaubhāgyadāyaka (14 triangles)
   5. Sarvārthasādhaka (outer 10)
   6. Sarvarakṣākara (inner 10)
   7. Sarvarogahara (8)
   8. Sarvasiddhiprada (triangle)
   9. Sarvānandamaya (bindu)
3. `bhavanopanishad`: the Śrīcakra as the body, verse by verse. **Needs a text PDF.**

### E. Hymns verse by verse (Gītā format, Hymns door): `/bhakti/devi/<slug>/` (part-N if long)
1. **Lalitā Sahasranāma**: about 183 ślokas in about 8 parts. **Needs a text PDF.**
2. **Saundaryalaharī**: 100 verses in 5 parts; attribution to Śaṅkara noted as traditional. **Needs a text PDF.**
3. **Kamalāmbā Navāvaraṇa kṛtis** (Muttusvāmi Dīkṣitar): 11 songs in 2 parts. **Needs a text PDF.**
4. Link the existing Triśatī and Pañcaratnam.

### F. Teachers and texts (about 8): `srividya/teachers/<slug>/`
Agastya and Lopāmudrā, Dattātreya and Paraśurāma, Bhāskararāya (Saubhāgya Bhāskara, Setubandha), Muttusvāmi Dīkṣitar, and the **Tripurā Rahasya** (Jñāna Khaṇḍa) in about 4 parts.

### G. Temples (7): `srividya/temples/<slug>/` (also `door:'temples'`)
Kāñcī Kāmākṣī (link the Śakti Pīṭha article; this one is the Śrīvidyā angle), Madurai Mīnākṣī, Tiruvānaikkāval Akhilāṇḍeśvarī (Śaṅkara's tāṭaṅka earrings), Tiruvārūr Kamalāmbā, Śṛṅgeri Śāradā, Kollūr Mūkāmbikā, and Lalitā at Naimiṣāraṇya.

### H. Festivals (2)
Navarātri as Lalitā worship; Lalitā Pañcamī and Lalitā Jayantī (dates from almanac sites, with a "check your pañcāṅga" note).

## 6. Seven-day schedule (heavy; drop to fewer per day if pages get thin; quality first)

| Day | Build and upload |
|---|---|
| 1 | Series index + A (6) + B (6) |
| 2 | C core: Vārāhī, Rājaśyāmalā, Bālā, Kāmeśvara, Mahāgaṇapati, Vāñchākalpalatā, Ucchiṣṭa Gaṇapati, Pratyaṅgirā, Nīla Sarasvatī, Aśvārūḍhā, Sampatkarī, Tiraskariṇī, Kurukullā, Hayagrīva |
| 3 | D: Śrīcakra overview + 9 āvaraṇas (+ Bhāvanopaniṣad if the PDF has arrived) |
| 4 | C: Tithi Nityās overview + 15 + Mahānityā |
| 5 | E: Saundaryalaharī (5 parts) |
| 6 | E: Lalitā Sahasranāma (8 parts) |
| 7 | E: Navāvaraṇa kṛtis; F teachers and Tripurā Rahasya; G temples; H festivals; final index, catalog and checks |

**PDFs I will supply** (Vaidika Vignanam or a printed book): Lalitā Sahasranāma, Saundaryalaharī, Bhāvanopaniṣad, Kamalāmbā Navāvaraṇa kṛtis, Tripurā Rahasya (Jñāna Khaṇḍa) if done verse by verse.

## 7. What is already on the site (don't redo)

- **Viṣṇu:**
  - Bhagavad Gītā (all 18 chapters, 700 ślokas, deep dives)
  - Daśāvatāra
  - Viṣṇu Sahasranāma
  - Hanumān (6 parts + Cālīsā, Saṅkaṭmocan Aṣṭak, ślokas)
  - Vaikuṇṭha Ekādaśī 2026 (20 Dec)
  - Bhaja Govindam, Suprabhātam, Acyutāṣṭakam, Madhurāṣṭakam, Govinda Nāmālu and more
- **Devī:**
  - Devī Māhātmya (19 parts)
  - Daśa Mahāvidyā
  - Aṣṭa Lakṣmī (overview + 8)
  - Lalitā Triśatī (59 ślokas)
  - Lalitā Pañcaratnam, Kanakadhārā, Mahālakṣmī Aṣṭakam, Annapūrṇā, Mahiṣāsuramardinī, Yā Devī, Gāyatrī
- **Śiva:** Subrahmaṇya Ṣaṣṭhī, Śiva hymns (Rudram, Mahimna, Tāṇḍava and more)
- **Temples:** 12 Jyotirliṅgas, Pañca Bhūta, 18 Śakti Pīṭhas + 51 round-up, Char Dham, Saptapurī, Triraṅga, Ahobilam, around Mysuru (15), Pañca Kedār

## 8. Backlog after Śrīvidyā

- **Upaniṣads,** done in full Gītā style, about 36 articles. Order: overview, Īśa, Kena, Kaṭha, Muṇḍaka, Māṇḍūkya, Praśna, Taittirīya, Aitareya, Śvetāśvatara, Chāndogya, Bṛhadāraṇyaka. List them under no single god.
- **Dattātreya:** about 5 articles; Datta Jayantī is in late December.
- **Gaṇeśa + Aṣṭavināyaka:** about 9 articles; there is no Gaṇeśa page yet.
- **Pañca Badrī** (6) and **Hanumad Vrata** (Karnataka Hanumān Jayantī, in December).
- **Bajrang Bāṇ:** waiting for a trusted text from Srini.
- **Clean-up:**
  - add tile illustrations to the older series indexes (Daśāvatāra, Mahāvidyā, Jyotirliṅgas, Śakti Pīṭhas and others)
  - fill out the Pañca Kedār pages to the full deep-dive depth
