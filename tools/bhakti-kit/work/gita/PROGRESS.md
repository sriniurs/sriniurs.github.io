# Bhagavad Gītā series (in progress)

Format (Srini, 21 Nov 2026): every one of the 700 ślokas on TWO pages
(page A: chant, picture, meaning, word table; page B: deep dive: in context /
looking deeper / for today). Each chapter = one article at
/bhakti/vishnu/bhagavad-gita/chapter-N/ (+ /overview/). Light-blue Viṣṇu theme.
Upload everything at the end, after all 18 chapters + overview are built.

Text: gita_iast.json, built by translit.py from the bhagavadgita.io (gita/gita)
Devanagari, cross-checked against vedicscriptures/bhagavad-gita-data (IIT Kanpur
Gita Supersite); verse-specific fixes are in translit.py FIX. 13.0 = the extra
verse "prakṛtiṃ puruṣaṃ caiva" (not counted in the 700).

Build: `cd work/gita && bash ../gchk.sh cNN.py Gita_ChapterNN.html` (library gc.py,
builder build2, verse helper X(...)). Draft view links are claude.ai artifacts.

Done (v2 format): ch 1, 2, 3. Next: ch 4 (write cNN.py; long chapters split cNNa.py/cNNb.py).
