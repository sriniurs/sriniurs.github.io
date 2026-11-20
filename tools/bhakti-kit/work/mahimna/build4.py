import json,re,sys
sys.path.insert(0,'.')
from data4 import V
from data import talk,svg,T,LINGA
S=json.load(open('split4.json'))
src=open('../stotram.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śiva Mahimna Stotram · Part 4 · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Mahimnaḥ pāraṃ te: Puṣpadanta\'s Śiva Mahimna Stotram, Part 4 (verses 33–43), the closing verses, explained in plain English with illustrations: Puṣpadanta named, the fruit of chanting, and Whatever You are, to That I bow.">',head)
head=head.replace('</style>','  .iast .cl2{padding-left:2.2em}\n  .full .ln2{padding-left:2.2em}\n  @media(max-width:720px){.iast .cl2{padding-left:1.6em}.full .ln2{padding-left:1.6em}}\n</style>',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
def lab(v):
    a=v['vs'][0]+33; z=v['vs'][-1]+33
    return f'Verse {a}' if a==z else f'Verses {a}–{z}'
def iast(i):
    out=''
    for a,b in [x for k in V[i]['vs'] for x in S[k]]:
        out+=f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>'
    return f'<div class="iast">{out}</div>'
def full(i):
    o=f'<p><span class="vn">VERSE {i+33}</span>'
    for a,b in S[i]:
        b2=re.sub(r'\s*‖(\d+)‖$',r'<span class="end">‖ \1 ‖</span>',b)
        o+=f'<span class="ln">{a}</span><span class="ln ln2">{b2}</span>'
    return o+'</p>'
cover_svg=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A gandharva with folded hands singing before a linga under a pillar of light, with scattered flowers on the ground">'
 '<rect x="174" y="0" width="32" height="268" fill="#ffd60a" opacity=".2"/><path d="M0 220 Q190 196 380 220 V268 H0Z" fill="#2a5a3a" stroke="#111" stroke-width="2"/>'
 '<g transform="translate(190 214) scale(1.6)">'+LINGA+'</g>'
 +''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}" stroke="#111" stroke-width="1.2"/>' for x,y,c in [(60,236,'#f08aa6'),(90,246,'#ffd60a'),(300,238,'#f08aa6'),(330,250,'#4caf50'),(120,240,'#4caf50'),(270,246,'#ffd60a'),(150,252,'#f08aa6'),(240,252,'#4caf50')])
 +'<g transform="translate(80 150)" stroke="#111" stroke-width="2.5"><circle cx="0" cy="-34" r="14" fill="#f2c79b"/><path d="M-12 -46 l12 -14 l12 14" fill="#ffd60a"/><path d="M-20 30 q0 -50 20 -50 q20 0 20 50z" fill="#7a3fa0"/><path d="M-6 -6 l6 -10 l6 10z" fill="#f2c79b"/><path d="M-30 -10 q-20 -10 -24 10 M30 -10 q20 -10 24 10" fill="none" stroke="#bcd4f0" stroke-width="4"/></g>'
 '<text x="80" y="198" text-anchor="middle" font-family="Bangers" font-size="13" fill="#ffd60a">PUṢPADANTA</text>'
 '<text x="300" y="70" text-anchor="middle" font-family="Bangers" font-size="22" fill="#fff">♪ mahimnaḥ</text><text x="320" y="96" text-anchor="middle" font-family="Bangers" font-size="18" fill="#ffd60a">pāraṃ te…</text></svg>')
forgiven_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#16264a" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Puṣpadanta rising back into the sky with his powers restored, a scroll of the hymn left behind on earth for people to sing"><rect width="460" height="210" fill="#16264a"/><path d="M0 170 Q230 150 460 170 V210 H0Z" fill="#2a5a3a"/><g transform="translate(300 70)" stroke="#111" stroke-width="2.5"><circle cy="-20" r="14" fill="#f2c79b"/><path d="M-12 -32 l12 -14 l12 14" fill="#ffd60a"/><path d="M-20 40 q0 -50 20 -50 q20 0 20 50z" fill="#7a3fa0"/><path d="M-30 0 q-24 -10 -30 12 M30 0 q24 -10 30 12" fill="none" stroke="#bcd4f0" stroke-width="4"/></g><path d="M300 130 v30" stroke="#ffd60a" stroke-width="2" stroke-dasharray="4 3"/><rect x="80" y="150" width="90" height="30" rx="4" fill="#fff3b0" stroke="#111" stroke-width="2"/><text x="125" y="170" text-anchor="middle" font-family="Bangers" font-size="12" fill="#c0392b">MAHIMNA</text><text x="300" y="196" text-anchor="middle" font-family="Bangers" font-size="14" fill="#ffd60a">POWERS RESTORED</text></svg>')
ardha_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Ardhanarishvara, half Shiva and half Parvati in one body, with the sage Bhringi as a bee and later standing on three legs"><rect width="460" height="210" fill="#fff8ec"/><g stroke="#111" stroke-width="3"><path d="M230 30 a24 24 0 0 0 0 48z" fill="#bcd4f0"/><path d="M230 30 a24 24 0 0 1 0 48z" fill="#f2c79b"/><path d="M230 78 l-36 120 h36z" fill="#1d4f9a"/><path d="M230 78 l36 120 h-36z" fill="#e05a8a"/></g><path d="M210 30 q-8 -18 8 -20 q4 12 -8 20z" fill="#c9a26b" stroke="#111" stroke-width="2"/><circle cx="246" cy="24" r="6" fill="#ffd60a" stroke="#111" stroke-width="2"/><text x="150" y="60" text-anchor="middle" font-family="Bangers" font-size="16" fill="#1d4f9a">ŚIVA</text><text x="320" y="60" text-anchor="middle" font-family="Bangers" font-size="16" fill="#c0392b">ŚAKTI</text><g transform="translate(100 120)"><ellipse rx="10" ry="7" fill="#ffd60a" stroke="#111" stroke-width="2"/><path d="M-4 -6 q-8 -12 -14 -2 M4 -6 q8 -12 14 -2" fill="none" stroke="#111" stroke-width="2"/></g><g stroke="#111" stroke-width="2.5" transform="translate(380 110)"><circle cy="-20" r="10" fill="#f2c79b"/><path d="M0 -10 v40 M0 30 l-12 30 M0 30 l12 30 M0 30 v30" fill="none"/></g><text x="380" y="196" text-anchor="middle" font-family="Bangers" font-size="12">BHṚṄGI · THREE LEGS</text><text x="100" y="150" text-anchor="middle" font-family="Bangers" font-size="12">BHṚṄGI AS A BEE</text></svg>')
tripura_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#16264a" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three flying cities of gold, silver and iron lining up in the sky as Shiva aims a single arrow from a chariot"><rect width="460" height="210" fill="#16264a"/>'+''.join(f'<g transform="translate({x} {y})"><path d="M-34 0 h68 l-10 14 h-48z" fill="{c}" stroke="#111" stroke-width="2.5"/>'+''.join(f'<rect x="{-28+14*k}" y="-22" width="10" height="22" fill="{c}" stroke="#111" stroke-width="1.5"/>' for k in range(5))+'</g>' for x,y,c in [(300,50,'#ffd60a'),(360,90,'#d9d9d9'),(420,130,'#7a7f8a')])+'<path d="M110 150 L420 50" stroke="#ff8c1a" stroke-width="3" stroke-dasharray="8 5"/><path d="M60 170 h90 l-10 18 h-70z" fill="#2a9d6f" stroke="#111" stroke-width="2.5"/><circle cx="78" cy="190" r="12" fill="#ffd60a" stroke="#111" stroke-width="2"/><circle cx="132" cy="190" r="12" fill="#eee" stroke="#111" stroke-width="2"/><path d="M110 170 q-30 -50 0 -100" fill="none" stroke="#c9a26b" stroke-width="5"/><text x="360" y="190" text-anchor="middle" font-family="Bangers" font-size="16" fill="#ffd60a">ONE ARROW · THREE CITIES</text></svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Four panels: a gandharva stealing flowers invisibly, the king scattering offered flowers on the path, the gandharva stepping on them and becoming visible, and the gandharva singing to Shiva">'
 '<rect width="460" height="210" fill="#fffaf0"/>'
 +''.join(f'<rect x="{6+113*i}" y="6" width="107" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{59+113*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#e7f4ea','1 · INVISIBLE THIEF'),('#ffe3c4','2 · THE KING\'S TRAP'),('#ffe0e0','3 · CAUGHT!'),('#dfe9f6','4 · THE HYMN')]))
 +'<g opacity=".35" stroke="#111" stroke-width="2"><circle cx="59" cy="60" r="12" fill="#f2c79b"/><path d="M43 120 q16 -50 32 0z" fill="#7a3fa0"/></g><path d="M20 150 q10 -20 20 0 q10 -20 20 0 q10 -20 20 0" fill="none" stroke="#2a9d6f" stroke-width="3"/>'
 +''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#f08aa6" stroke="#111"/>' for x,y in [(70,90),(82,96),(30,140),(90,140)])
 +'<g stroke="#111" stroke-width="2"><circle cx="160" cy="58" r="12" fill="#f2c79b"/><path d="M152 46 l8 -10 l8 10" fill="#ffd60a"/><path d="M144 120 q16 -50 32 0z" fill="#c0392b"/></g>'+''.join(f'<circle cx="{x}" cy="160" r="5" fill="#4caf50" stroke="#111"/>' for x in (134,150,166,182,198))
 +'<g stroke="#111" stroke-width="2"><circle cx="285" cy="60" r="12" fill="#f2c79b"/><path d="M269 122 q16 -50 32 0z" fill="#7a3fa0"/></g>'+''.join(f'<circle cx="{x}" cy="160" r="5" fill="#4caf50" stroke="#111"/>' for x in (262,278,294,310))+'<text x="285" y="34" text-anchor="middle" font-family="Bangers" font-size="18" fill="#c0392b">!</text>'
 +'<g transform="translate(398 150)">'+LINGA+'</g><g stroke="#111" stroke-width="2"><circle cx="372" cy="70" r="11" fill="#f2c79b"/><path d="M358 130 q14 -44 28 0z" fill="#7a3fa0"/></g><text x="410" y="70" font-family="Bangers" font-size="16" fill="#1d4f9a">♪</text></svg>')
b=[]
b.append(f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 4 OF 4</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(28px,8vw,76px)">ŚIVA MAHIMNA<br>STOTRAM</h1>
  <div class="series">PART 4 · VERSES 33–43 · THE CLOSING VERSES</div>
  <div class="tag">"Mahimnaḥ pāraṃ te…" · the gandharva's hymn to the greatness of Śiva, explained and illustrated</div>
  {cover_svg}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First Part 1 for chanting in one go. Then the story of Puṣpadanta and the hymn's background, and <b>two pages for each verse</b>: the chant, a picture, what it says and the key words; then a deeper look, background facts, the inner teaching and the one thing to remember. Parts 2–4 cover the rest of the hymn.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>The praise ended with verse 32: if the ocean were ink and the earth paper, the goddess of learning still could not finish. What follows are the closing verses.</p>
    <p>In verses 33–43 the poet signs his name, tells how he fell from his greatness and sang, promises blessings to those who chant the hymn, and offers it at Śiva's feet as a worship made of words.</p>
    <p>And in the middle of them is perhaps the most beautiful line of all: "I do not know what You are, O Lord. Whatever You are, to That I bow, again and again."</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Har Har Mahādev,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
</section>

<section class="page" id="full">
  <h2 class="page-title">PART 4 IN ONE GO</h2>
  <div class="sub">Verses 33–43, for chanting</div>
  <div class="full">{''.join(full(i) for i in range(6))}</div>
</section>
<section class="page" id="full2">
  <h2 class="page-title">PART 4 IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 39–43</div>
  <div class="full">{''.join(full(i) for i in range(6,11))}</div>
  <p class="center" style="font-family:Noto Sans,sans-serif;font-style:italic;margin:8px 0">‖ iti śrī puṣpadanta-viracitaṃ śivamahimnaḥ stotraṃ samāptam ‖</p>
  <div class="note">Text as on sanskritdocuments.org; each line is split at its natural pause (the <i>yati</i> after the sixth syllable).</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · THE GANDHARVA FORGIVEN</h2>
  <div class="sub">How the story ends, and how the hymn lives on</div>
  {forgiven_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>The fall.</b> Puṣpadanta, king of the gandharvas, steps on flowers offered to Śiva and loses his divine powers (Part 1).</div>
      <div><b>The song.</b> Fallen and visible, he sings the greatness of the Lord whose offering he trampled.</div>
      <div><b>Forgiven.</b> Pleased, Śiva restores his powers. The hymn itself, in verse 37, says he fell from his greatness and then composed it.</div>
      <div><b>Handed down.</b> The hymn spreads across India; the scholar Madhusūdana Sarasvatī comments on it, reading every verse for both Śiva and Viṣṇu.</div>
      <div><b>Still sung.</b> Śrī Rāmakṛṣṇa is said to have entered samādhi reciting a few verses; Swami Vivekananda quoted verse 7 in Chicago in 1893; families chant it every evening.</div>
    </div>
  </div>
  <div class="g3">
    <div class="card bg-yellow"><h4>The fault</h4><p>Pride and carelessness.</p></div>
    <div class="card bg-red"><h4>The cure</h4><p>A hymn of <b>humble praise</b>.</p></div>
    <div class="card bg-green"><h4>The gift</h4><p>The <b>Mahimna</b>, for everyone.</p></div>
  </div>
  {talk("So his mistake gave the world this hymn?","That's how tradition sees it. A fall, a song, forgiveness, and a gift that has lasted for centuries.")}
</section>

<section class="page" id="about">
  <h2 class="page-title">ABOUT THE MAHIMNA</h2>
  <div class="sub">A hymn of thought and devotion</div>
  <div class="g2">
    <div class="card bg-blue"><h4>✍️ The author</h4><p>Ascribed to <b>Puṣpadanta</b>; a later verse names him as the composer. Its real date is not known; it is an old and much-copied hymn.</p></div>
    <div class="card bg-yellow"><h4>🎵 The sound</h4><p>Written in <b>śikhariṇī</b>, seventeen syllables a line with a pause after the sixth, and chanted to a much-loved traditional tune.</p></div>
  </div>
  <div class="panel reading">
    <p><b>The shape.</b> Verses 1–3 apologise for praising the unpraisable; 4–9 answer doubters and debaters; 10–24 tell Śiva's great deeds; 25–31 turn to Oṃ, the eight names and salutations; 32 is the famous "if the ocean were ink" verse; the rest are closing verses.</p>
    <p><b>Read two ways.</b> The 16th-century Advaita scholar <b>Madhusūdana Sarasvatī</b> wrote a commentary reading every verse as praise of both Śiva and Viṣṇu.</p>
    <p><b>Beloved by saints.</b> Śrī Rāmakṛṣṇa is said to have gone into samādhi while reciting only a few of its verses.</p>
  </div>
  <table class="ct">
    <tr><th>Part</th><th>Verses</th><th>Theme</th></tr>
    <tr><td><b>1</b></td><td>1–11</td><td>Praise beyond words; the doubters; many rivers, one ocean; the pillar of fire</td></tr>
    <tr><td><b>2</b></td><td>12–22</td><td>Rāvaṇa and Bāṇa; the poison; Kāma; Tripura; Dakṣa's sacrifice</td></tr>
    <tr><td><b>3</b></td><td>23–32</td><td>The cremation ground; the yogī's light; Oṃ; the eight names; "if the ocean were ink"</td></tr>
    <tr><td><b>4</b> (this one)</td><td>33–43</td><td>The fruit of the hymn; Puṣpadanta named; the closing verses</td></tr>
  </table>
  <div class="note">The number of verses differs between editions, from about 31 core verses to over 40 with the closing verses.</div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">Part 4 in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story: The Gandharva Forgiven</a></li>
    <li><span class="num">ℹ</span><a href="#about">About the Mahimna</a></li>
    <li><span class="num">∑</span><a href="#end">Part 4 on One Page</a></li>
    <li class="part">VERSES 33–43</li>
    {''.join(f'<li><span class="num">{v["vs"][0]+33}</span><a href="#v{v["vs"][0]+33}">{lab(v)}: {v["theme"].title().replace("’S","’s").replace("\'S","\'s")}</a></li>' for i,v in enumerate(V))}
  </ul>
</section>
''')
for i,v in enumerate(V):
    n=v['vs'][0]+33
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    c=v['cards']
    b.append(f'''<section class="page" id="v{n}">
  <h2 class="page-title">{lab(v).upper()}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(i)}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>
    <div class="plain">{v['plain']}</div>
    <table class="ct"><tr><th>Word</th><th>Means</th></tr>{words}</table>
  </div>
  <p class="center" style="margin:0"><a href="#v{n}b" class="contlink">Continue: going deeper ➜</a></p>
</section>
<section class="page" id="v{n}b">
  <h2 class="page-title">{lab(v).upper()} · GOING DEEPER</h2>
  <div class="sub">{v['theme']}</div>
  <div class="panel reading">{v['deep']}</div>
  <div class="g2"><div class="card bg-yellow"><h4>{c[0]}</h4><p>{c[1]}</p></div><div class="card bg-blue"><h4>{c[2]}</h4><p>{c[3]}</p></div></div>
  <div class="inner">{v['inner']}</div>
  {talk(*v['talk'])}
  <div class="key">{v['key']}</div>
</section>
''')
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 4 ON ONE PAGE</h2>
  <div class="sub">The closing verses, and the whole hymn</div>
  <div class="steps">
    <div><b>Verses 33–34.</b> Puṣpadanta signs the hymn; chanted daily with devotion, it blesses this life and the next.</div>
    <div><b>Verses 35–36.</b> No god above Maheśa, no hymn above the Mahimna, no mantra above Aghora, no truth above the guru.</div>
    <div><b>Verses 37–40.</b> He fell from his greatness and sang of Śiva's; with folded hands, the hymn is offered as a worship of words.</div>
    <div><b>Verses 41–42.</b> "I do not know what You are; whatever You are, to That I bow."</div>
    <div><b>Verse 43.</b> From the lotus mouth of Puṣpadanta: learnt by heart, recited, reflected on, it pleases the Lord of all beings.</div>
  </div>
  <div class="panel"><span class="caption">The whole Mahimna</span><p style="margin:0">Part 1: praise beyond words (1–11) · Part 2: the great deeds (12–22) · Part 3: all and beyond all (23–32) · Part 4: the closing verses (33–43).</p></div>
  {talk("What did you like most in the whole hymn?","Verse 7, every river reaching the sea, and verse 41: whatever You are, to That I bow. Between them is everything a seeker needs.")}
  <div class="key">Śiva Mahimna: <b>a fallen singer's apology that became a gift for all</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śiva Mahimna Stotram, verses 33–43. Sanskrit text from sanskritdocuments.org (Puṣpadanta's Śivamahimna Stotram, with translation by Devendraray V. Bhatt and S. V. Ganesan), shown in IAST; meanings are our own plain-English renderings. The story of Puṣpadanta is traditional; versions differ. In verse 38 \'suraguru\' is read by some as Bṛhaspati and by others as Śiva; we follow the second. Not independently verified: the Rāmakṛṣṇa anecdote. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
html=head+''.join(b)+tail
open('Shiva_Mahimna_Stotram_Part4.html','w').write(html)
print(len(html))
