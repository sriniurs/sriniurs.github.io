# Bhakti builder kit

The Python builders behind the illustrated articles in `/bhakti/`. Not served as pages:
templates are stored as `*.html.tmpl` and only become `.html` after setup.

## Install (fresh chat or machine)

```bash
bash tools/bhakti-kit/setup.sh            # installs to /home/claude/work (default)
bash tools/bhakti-kit/setup.sh ~/work     # or anywhere; hard-coded paths are rewritten
```

Needs python3, playwright + Chrome (`/usr/bin/google-chrome`), pypdf, poppler (`pdftoppm`), Pillow.

## Check an article

```bash
cd <WORK>/devim && bash ../dchk.sh p07.py Devi_Mahatmya_Part07.html          # Devī Māhātmya style
cd <WORK>/shakti && bash ../chk.sh dv1_matsya.py DV1_Matsya.html             # temple / deity style
```

Both print `scrollWidth` (must be 390), the PDF page count and the section count
(must match), and write a contact sheet to `<WORK>/sheet.png`. `dchk.sh` also prints
`OVERFLOW?` for any page that spilled onto a second A4 sheet.

## Which library to start from

| Kind of article | Library | Example builders |
|---|---|---|
| Scripture in parts, verse by verse (red Devī theme) | `devim/dmc.py` (uses `devim/common.py`, `build5.py`, `build6.py`) | `devim/p07.py`–`p19.py` |
| Hymn verse by verse (blue Viṣṇu theme) | `vsn/`, `bhaja/`, `suprabhatam/`, `madhura/`, `acyuta/` | `vsn/*.py`, `bhaja/*.py` |
| Śiva hymn (navy) | `mahimna/` | `mahimna/*.py` |
| Temple article (Śakti Pīṭha, Char Dham, Saptapurī) | `shakti/common_s.py` | `shakti/kamakshi.py`, `badrinath.py`, `saptapuri.py` |
| Temple circuit (navy, south-India map) | `shakti/ps_common.py` | `shakti/ps_overview.py`, `ps_kanchi.py` … |
| Deity series, Viṣṇu (light blue) | `shakti/dv_common.py` | `shakti/dv_overview.py`, `dv1_matsya.py` … |
| Deity series, Devī (red) | `shakti/mv_common.py` | `shakti/mv_overview.py`, `mv_kali.py` … |
| Around Mysuru / Triraṅga temples | `mysuru/`, `triranga/common_t.py` | `mysuru/nanjangud.py`, `triranga/*.py` |

Copy the closest example, change the data, run the check, look at the sheet.

## Upload helpers

`up_lib.py` gives `cp()`, `tile()` and `index()` for copying pages into the repo and
building series index pages. Upload scripts (`dv_upload.py`, `ps_upload.py`,
`mv_upload.py`) show how a series is copied, indexed and added to
`bhakti/catalog.json`. Copy only the new files: never re-copy older drafts over live pages.

After copying: `python3 .github/bhakti_hubs.py --strict && python3 .github/site_nav.py && python3 .github/build_sitemap.py`,
run a link check, commit, push. The full workflow is in the `srinipresents-bhakti` skill
and the "Bhakti section" of `PUBLISHING.md`.

Several builders read the published version of an earlier page for its head and
CSS, so pull the repo before building.
