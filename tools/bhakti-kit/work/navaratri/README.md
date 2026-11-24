# Navarātri series builders
Red Devī theme; head/CSS read from the published Guruvāyūr page in srini-bhakti. `python3 p01.py` … writes out/<slug>/; `nd.py` is the shared Navadurgā template (data in nd1–nd3). `iast.py` builds /how-to-read-iast/ (navy). `hub.py` builds the series index. Check with `python3 chk.py festivals/navaratri <slug>` against a local http.server on port 8765.

Festival series (Nov 2026): ek.py (+ek_data.py) Ekādaśī, kartika.py (+dam.txt), pitru.py, misc.py (Guru Pūrṇimā, Akṣaya Tṛtīyā, Śrāvaṇa Pūrṇimā, Dhanurmāsa), hubx.py hubs. pages.configure() sets base/parts/theme (red|navy|blue); output to outx/.

Pradoṣa (pradosha.py, pradosha2.py, prad.txt). Depth add-on pages: extras1.py / extras2.py fill pages.EXTRA[url] (inserted before On One Page) then re-run the series builder.

- ek2.py + ek_more.py: Ekādaśī 28-part build (one article per Ekādaśī) → outx/ekadashi/. Supersedes ek.py.
- sank.py + sank_data.py + fig3.py (Gaṇeśa figures) + sank_hub.py: Saṅkaṣṭī Caturthī 17-part build → outs/sankashti-chaturthi/ (published at /ganesha/festivals/sankashti-chaturthi/).
- puja.py, samskara.py: single-article practice guides → outp/ (published at /home-puja/, /sixteen-samskaras/). pages.py: CFG backurl/backname for single articles.
