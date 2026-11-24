# Navarātri series builders
Red Devī theme; head/CSS read from the published Guruvāyūr page in srini-bhakti. `python3 p01.py` … writes out/<slug>/; `nd.py` is the shared Navadurgā template (data in nd1–nd3). `iast.py` builds /how-to-read-iast/ (navy). `hub.py` builds the series index. Check with `python3 chk.py festivals/navaratri <slug>` against a local http.server on port 8765.

Festival series (Nov 2026): ek.py (+ek_data.py) Ekādaśī, kartika.py (+dam.txt), pitru.py, misc.py (Guru Pūrṇimā, Akṣaya Tṛtīyā, Śrāvaṇa Pūrṇimā, Dhanurmāsa), hubx.py hubs. pages.configure() sets base/parts/theme (red|navy|blue); output to outx/.

Pradoṣa (pradosha.py, pradosha2.py, prad.txt). Depth add-on pages: extras1.py / extras2.py fill pages.EXTRA[url] (inserted before On One Page) then re-run the series builder.
