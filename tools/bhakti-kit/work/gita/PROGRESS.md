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

Done (v2 format): ch 1–5. Next: ch 6 (write cNN.py; long chapters split cNNa.py/cNNb.py).

Draft links (claude.ai artifacts, republish with the same slug):
- ch1 de0966e1-6ae8-4f96-a9f2-a78b3411b961 https://claude.ai/artifact/URFHvJYRPifW7VJ9wbSEKr
- ch2 11457796-5cfe-4ea5-8eff-aad4a401cd75 https://claude.ai/artifact/38hYJHDoUcrZbXgdL3Kasn
- ch3 c42196d5-ecd6-4154-8fbe-8b981d1a1be3 https://claude.ai/artifact/RDi7VWHFwZEcD2SdgBMXJr
- ch4 f8186089-e434-4035-a555-c0236da05398 https://claude.ai/artifact/Xdt26xpSYJKEdw9nqCmTAP
