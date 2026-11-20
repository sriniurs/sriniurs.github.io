import json,re,sys
sys.path.insert(0,'.')
from data2 import V
from data import talk,svg,T,LINGA
S=json.load(open('split2.json'))
src=open('../stotram.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śiva Mahimna Stotram · Part 2 · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Mahimnaḥ pāraṃ te: Puṣpadanta\'s Śiva Mahimna Stotram, Part 2 (verses 12–22), explained verse by verse in plain English with illustrations: Rāvaṇa and Bāṇa, the blue throat, Kāma, the dance, Tripura and Dakṣa.">',head)
head=head.replace('</style>','  .iast .cl2{padding-left:2.2em}\n  .full .ln2{padding-left:2.2em}\n  @media(max-width:720px){.iast .cl2{padding-left:1.6em}.full .ln2{padding-left:1.6em}}\n</style>',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
def iast(i):
    out=''
    for a,b in S[i]:
        out+=f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>'
    return f'<div class="iast">{out}</div>'
def full(i):
    o=f'<p><span class="vn">VERSE {i+12}</span>'
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
  <div class="burst yel">PART 2 OF 4</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(28px,8vw,76px)">ŚIVA MAHIMNA<br>STOTRAM</h1>
  <div class="series">PART 2 · VERSES 12–22 · THE GREAT DEEDS</div>
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
    <p>In Part 1, Puṣpadanta admitted that no words can reach Śiva, answered the doubters, and saw all paths flowing to one ocean. Now he turns from argument to story.</p>
    <p>Verses 12–22 are the great deeds: Rāvaṇa pressed down by one toe, Bāṇa raised by bowing, the poison held in the throat, Kāma burnt to ash, the dance that shakes the worlds, the Gaṅgā as a drop, the chariot made of the universe, Viṣṇu's eye, Dakṣa's broken sacrifice, and a hunter who still chases a deer across the night sky.</p>
    <p>Each story ends with a line of wisdom: on pride, humility, compassion, self-control and faith. This is the part of the hymn children remember first.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Har Har Mahādev,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
</section>

<section class="page" id="full">
  <h2 class="page-title">PART 2 IN ONE GO</h2>
  <div class="sub">Verses 12–22, for chanting</div>
  <div class="full">{''.join(full(i) for i in range(6))}</div>
</section>
<section class="page" id="full2">
  <h2 class="page-title">PART 2 IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 18–22</div>
  <div class="full">{''.join(full(i) for i in range(6,11))}</div>
  <div class="note">Text as on sanskritdocuments.org; each line is split at its natural pause (the <i>yati</i> after the sixth syllable).</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · THE THREE FLYING CITIES</h2>
  <div class="sub">Why Śiva is called Tripurāntaka, "ender of the three cities"</div>
  {tripura_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>Three cities.</b> Three demon brothers, sons of Tāraka, win a boon: three flying cities, of <b>gold</b> in heaven, <b>silver</b> in the sky and <b>iron</b> on earth, built by the architect Maya.</div>
      <div><b>The catch.</b> The cities can be destroyed only by a single arrow, at the one moment in a thousand years when all three line up.</div>
      <div><b>Terror.</b> From their moving fortresses the brothers trouble gods and people. The gods turn to Śiva.</div>
      <div><b>The chariot.</b> The whole universe is made into His war-chariot: the earth its body, sun and moon its wheels, Brahmā the charioteer, Mount Meru the bow, Viṣṇu the arrow.</div>
      <div><b>One arrow.</b> When the cities align, Śiva destroys all three at once; many tellings say He did it with a smile alone.</div>
    </div>
  </div>
  <div class="g3">
    <div class="card bg-yellow"><h4>The cities</h4><p><b>Gold, silver, iron</b>: heaven, sky, earth.</p></div>
    <div class="card bg-red"><h4>The archer</h4><p><b>Tripurāntaka</b>, Śiva with Meru as His bow.</p></div>
    <div class="card bg-green"><h4>Inner reading</h4><p>Three cities = <b>three bodies</b> or <b>three impurities</b>.</p></div>
  </div>
  {talk("Why does the hymn keep calling Him 'destroyer of the cities'?","Because Tripura is His great victory, and verse 18 tells it. Puramathana and Tripurahara both mean the same: the one who burnt the three cities.")}
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
    <tr><td><b>2</b> (this one)</td><td>12–22</td><td>Rāvaṇa and Bāṇa; the poison; Kāma; Tripura; Dakṣa's sacrifice</td></tr>
    <tr><td><b>3</b></td><td>23–32</td><td>The cremation ground; the yogī's light; Oṃ; the eight names; "if the ocean were ink"</td></tr>
    <tr><td><b>4</b></td><td>33–end</td><td>The fruit of the hymn; Puṣpadanta named; the closing verses</td></tr>
  </table>
  <div class="note">The number of verses differs between editions, from about 31 core verses to over 40 with the closing verses.</div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">Part 2 in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story: The Three Flying Cities</a></li>
    <li><span class="num">ℹ</span><a href="#about">About the Mahimna</a></li>
    <li><span class="num">∑</span><a href="#end">Part 2 on One Page</a></li>
    <li class="part">VERSES 12–22</li>
    {''.join(f'<li><span class="num">{i+12}</span><a href="#v{i+12}">Verse {i+12}: {v["theme"].title().replace("’S","’s").replace("\'S","\'s")}</a></li>' for i,v in enumerate(V))}
  </ul>
</section>
''')
for i,v in enumerate(V):
    n=i+12
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    c=v['cards']
    b.append(f'''<section class="page" id="v{n}">
  <h2 class="page-title">VERSE {n}</h2>
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
  <h2 class="page-title">VERSE {n} · GOING DEEPER</h2>
  <div class="sub">{v['theme']}</div>
  <div class="panel reading">{v['deep']}</div>
  <div class="g2"><div class="card bg-yellow"><h4>{c[0]}</h4><p>{c[1]}</p></div><div class="card bg-blue"><h4>{c[2]}</h4><p>{c[3]}</p></div></div>
  <div class="inner">{v['inner']}</div>
  {talk(*v['talk'])}
  <div class="key">{v['key']}</div>
</section>
''')
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 2 ON ONE PAGE</h2>
  <div class="sub">Verses 12–22 in five lines</div>
  <div class="steps">
    <div><b>Verses 12–13.</b> Rāvaṇa misuses Śiva's gift and is pressed down by one toe; Bāṇa bows and rises: bowing to Śiva lifts anyone.</div>
    <div><b>Verses 14–15.</b> The poison held in the throat: a scar of compassion as an ornament; Kāma, who never missed, burnt to a memory.</div>
    <div><b>Verses 16–17.</b> The dance that shakes the worlds to protect them; the Gaṅgā that rings the earth is a drop in His hair.</div>
    <div><b>Verses 18–19.</b> The universe as a chariot He did not need, against the three cities; Viṣṇu's eye-offering becomes the Sudarśana discus.</div>
    <div><b>Verses 20–22.</b> He stays awake to give the fruit of every rite; Dakṣa's faithless sacrifice falls; even the creator is not above His justice.</div>
  </div>
  {talk("What happens in Part 3?","Śiva in the cremation ground, the yogī's inner light, Oṃ, the eight names, and the most famous verse of all: if the ocean were ink and the earth were paper…")}
  <div class="key">Śiva Mahimna, Part 2: <b>the great deeds, each with a lesson</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śiva Mahimna Stotram, verses 12–22. Sanskrit text from sanskritdocuments.org (Puṣpadanta's Śivamahimna Stotram, with translation by Devendraray V. Bhatt and S. V. Ganesan), shown in IAST; meanings are our own plain-English renderings. The stories are from the Purāṇas, the Brāhmaṇas and temple tradition, retold briefly; versions differ. Not independently verified: the identification of the deer and the hunter with Mṛgaśiras and Sirius follows tradition. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
html=head+''.join(b)+tail
open('Shiva_Mahimna_Stotram_Part2.html','w').write(html)
print(len(html))
