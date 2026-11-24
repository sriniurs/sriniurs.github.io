"""Turn the end-of-book 'Study notes' footer into a proper SOURCES & NOTES page,
add it to the contents, and normalise contents labels. Idempotent."""
import re, sys, glob, os
REPO = sys.argv[1]
TEXTW = re.compile(r'\b(text|edition|shlokam|sanskritdocuments|Vaidika|Gītā Press|Gita Press|checked|printed|published|numbering|translation|IIT Kanpur|Supersite|aurobharati|made from)\b', re.I)
DOUBT = re.compile(r'(not independently verified|not verified|unverified|versions differ|traditions differ|interpret|is traditional|are traditional|traditionally ascribed|popular tradition|devotional tradition|disputed|debated|differ\b|attributed)', re.I)
STD = re.compile(r'(Meanings are|fictional|Illustrations drawn|Pictures are)', re.I)
NAMED = re.compile(r'([a-z0-9-]+\.(?:org|com|in|net)\b|Press|shlokam|sanskritdocuments|Vaidika|Gītā Press|Gita Press|IIT Kanpur|aurobharati|Devasthanams|Tirumala|edition of)', re.I)
MANUAL = {
 'devi/mahishasura-mardini': ['Study notes on Ayi Giri Nandini, the Mahiṣāsuramardinī Stotram, in the 21-verse form commonly sung today. The story of the buffalo demon is told in the Devī Māhātmya (Mārkaṇḍeya Purāṇa, chapters 2–4); see our Devī Māhātmya series. The hymn is popularly ascribed to Ādi Śaṅkara, but the attribution is traditional and historians are not sure of it. The inner readings of the verses are interpretation.'],
 'vishnu/bhagavad-gita/overview': ['Study notes on the Bhagavad Gītā (Mahābhārata, Bhīṣma Parva, chapters 23–40 in the critical edition). Ślokas follow the Gītā Press (Gorakhpur) reading and numbering, 700 ślokas in 18 chapters, checked line by line against the IIT Kanpur Gita Supersite, in IAST. Where the great commentators (Śaṅkara, Rāmānuja, Madhva and others) read the Gītā differently, we say so; such readings are interpretation. Dating of the text is debated by scholars.'],
}

def sentences(s):
    s = re.sub(r'\s+', ' ', s).strip()
    out, cur = [], ''
    for part in re.split(r'(?<!Prof\.)(?<!Dr\.)(?<!St\.)(?<=[.!?])\s+(?=[A-ZĀĪŪṚŚṢṆḌṬ“"(])', s):
        out.append(part)
    return [x for x in out if x]

def build_page(notes):
    sents = sentences(re.sub(r'<[^>]+>', '', notes))
    text, doubt, other = [], [], []
    for x in sents:
        if STD.search(x):
            # keep any non-standard tail (e.g. "Meanings are simplified; the stories are traditional ...")
            if DOUBT.search(x) and 'Meanings are our own' not in x: doubt.append(x)
            continue
        if re.match(r'Study notes', x): text.append(x); continue
        if DOUBT.search(x) and not NAMED.search(x): doubt.append(x)
        elif TEXTW.search(x): text.append(x)
        else: other.append(x)
    if not any(NAMED.search(x) for x in text):
        doubt.append('Our verse text has not yet been checked word by word against one named printed edition; editions differ in small readings.')
    ps = []
    if text: ps.append('<p><b>Text and edition:</b> ' + ' '.join(text) + '</p>')
    if other: ps.append('<p><b>Background:</b> ' + ' '.join(other) + '</p>')
    ps.append('<p><b>Sources differ / unverified:</b> ' + (' '.join(doubt) if doubt else 'Nothing further flagged; editions differ only in small spellings.') + '</p>')
    return ('<section class="page" id="sources"><h2 class="page-title">SOURCES &amp; NOTES</h2><div class="sub">Where the text and facts come from</div>\n'
            '<div class="panel reading small">\n' + '\n'.join(ps) + '\n</div>\n'
            '<p class="studynotes" style="font-size:13px;opacity:.8;text-align:center">Interpretations are marked as such. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p>\n</section>')

def add_toc(h):
    if 'href="#sources"' in h: return h
    m = re.search(r'(<ul class="toc[^"]*"[^>]*>)(.*?)(</ul>)', h, re.S)
    if not m: return h
    nums = [int(x) for x in re.findall(r'<span class="num">(\d+)</span>', m.group(2))]
    n = (max(nums) + 1) if nums else 'S'
    li = f'<li><span class="num">{n}</span><a href="#sources">Sources &amp; Notes</a></li>'
    return h[:m.end(2)] + li + h[m.end(2):]

def fix(f, key):
    h = open(f, encoding='utf-8').read(); o = h
    if 'class="book' not in h: return False
    h = h.replace('&Amp;', '&amp;')
    h = re.sub(r'(<a href="#sources">)Sources(</a>)', r'\1Sources &amp; Notes\2', h)
    has = re.search(r'<section[^>]*id="sources"', h) or re.search(r'<h2 class="page-title">\s*SOURCES', h, re.I)
    if not has:
        fm = None
        for m in re.finditer(r'<footer[^>]*>(.*?)</footer>', h, re.S):
            if 'Study notes' in m.group(1): fm = m; break
        if fm:
            page = build_page(fm.group(1))
            h = h[:fm.start()] + page + h[fm.end():]
        elif key in MANUAL:
            page = build_page(MANUAL[key][0])
            # insert after the last page section inside the book
            i = h.rfind('</section>', 0, h.find('<script', h.find('class="book')) if '<script' in h[h.find('class="book'):] else len(h))
            h = h[:i + 10] + '\n' + page + h[i + 10:]
        else:
            print('NO NOTES', key); return False
        h = add_toc(h)
    if h != o:
        open(f, 'w', encoding='utf-8').write(h); return True
    return False

if __name__ == '__main__':
    n = 0
    for f in sorted(glob.glob(os.path.join(REPO, '**/index.html'), recursive=True)):
        if '/tools/' in f: continue
        key = os.path.relpath(os.path.dirname(f), REPO)
        if fix(f, key): n += 1
    print('changed', n)
