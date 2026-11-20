import json,re,sys
sys.path.insert(0,'.')
from data import V,talk,svg,T,LINGA
S=json.load(open('split.json'))
src=open('../stotram.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śiva Mahimna Stotram · Part 1 · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Mahimnaḥ pāraṃ te: Puṣpadanta\'s Śiva Mahimna Stotram, Part 1 (verses 1–11), explained verse by verse in plain English with illustrations, with the story of the gandharva who lost his powers.">',head)
head=head.replace('</style>','  .iast .cl2{padding-left:2.2em}\n  .full .ln2{padding-left:2.2em}\n  @media(max-width:720px){.iast .cl2{padding-left:1.6em}.full .ln2{padding-left:1.6em}}\n</style>',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
def iast(i):
    out=''
    for a,b in S[i]:
        out+=f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>'
    return f'<div class="iast">{out}</div>'
def full(i):
    o=f'<p><span class="vn">VERSE {i+1}</span>'
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
  <div class="burst yel">PART 1 OF 4</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(28px,8vw,76px)">ŚIVA MAHIMNA<br>STOTRAM</h1>
  <div class="series">PART 1 · VERSES 1–11 · PRAISE BEYOND WORDS</div>
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
    <p>"Mahimnaḥ pāraṃ te…" For many families, the Śiva Mahimna Stotram is the great hymn of the evening: long, flowing, and sung in a melody that rises and falls like a river. It is said to be the song of a heavenly musician who lost his powers, and found his way back by singing.</p>
    <p>It is also one of the most thoughtful hymns in Sanskrit. It opens by admitting that no words can reach Śiva, argues with the doubters, and then says something the whole world later heard in Chicago: that all paths, straight or winding, lead to the same ocean.</p>
    <p>Because it is long, we take it in four parts. This first part covers verses 1–11: praise beyond words, the questions of the doubters, the many rivers, Śiva the owner of nothing, and the pillar of fire.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Har Har Mahādev,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
</section>

<section class="page" id="full">
  <h2 class="page-title">PART 1 IN ONE GO</h2>
  <div class="sub">Verses 1–11, for chanting</div>
  <div class="full">{''.join(full(i) for i in range(6))}</div>
</section>
<section class="page" id="full2">
  <h2 class="page-title">PART 1 IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 7–11</div>
  <div class="full">{''.join(full(i) for i in range(6,11))}</div>
  <div class="note">Text as on sanskritdocuments.org; each line is split at its natural pause (the <i>yati</i> after the sixth syllable).</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · THE GANDHARVA WHO STOLE FLOWERS</h2>
  <div class="sub">Tradition's account of how the hymn was born</div>
  {story_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>A garden for Śiva.</b> King <b>Citraratha</b>, a great devotee of Śiva, grows a beautiful garden and offers its flowers in worship every day.</div>
      <div><b>An invisible thief.</b> <b>Puṣpadanta</b>, a gandharva, a musician of the gods, is enchanted by the flowers and begins stealing them. Gandharvas can make themselves invisible, so the king cannot catch him.</div>
      <div><b>The king's trap.</b> The king scatters <b>Śiva nirmālya</b>, the bilva leaves and flowers already offered to Śiva, along the garden paths.</div>
      <div><b>Caught.</b> Not knowing, Puṣpadanta steps on the sacred offerings. He loses his divine powers, becomes visible, and is caught.</div>
      <div><b>The hymn.</b> Ashamed, he sings a hymn to Śiva's greatness. Pleased, Śiva restores his powers. That hymn is the Mahimna.</div>
    </div>
  </div>
  <div class="g3">
    <div class="card bg-yellow"><h4>The singer</h4><p><b>Puṣpadanta</b>, "flower-toothed", a gandharva.</p></div>
    <div class="card bg-red"><h4>The fault</h4><p>Stepping on <b>Śiva's offerings</b>.</p></div>
    <div class="card bg-green"><h4>The way back</h4><p>A <b>hymn of praise</b>.</p></div>
  </div>
  {talk("He lost his powers for stepping on old flowers?","Flowers already offered to Śiva are sacred. The story's real point is the comeback: a fall, and a way back through praise.")}
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
    <tr><td><b>1</b> (this one)</td><td>1–11</td><td>Praise beyond words; the doubters; many rivers, one ocean; the pillar of fire</td></tr>
    <tr><td><b>2</b></td><td>12–22</td><td>Rāvaṇa and Bāṇa; the poison; Kāma; Tripura; Dakṣa's sacrifice</td></tr>
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
    <li><span class="num">🔤</span><a href="#full">Part 1 in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story: The Gandharva Who Stole Flowers</a></li>
    <li><span class="num">ℹ</span><a href="#about">About the Mahimna</a></li>
    <li><span class="num">∑</span><a href="#end">Part 1 on One Page</a></li>
    <li class="part">VERSES 1–11</li>
    {''.join(f'<li><span class="num">{i+1}</span><a href="#v{i+1}">Verse {i+1}: {v["theme"].title().replace("’S","’s").replace("\'S","\'s")}</a></li>' for i,v in enumerate(V))}
  </ul>
</section>
''')
for i,v in enumerate(V):
    n=i+1
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
  <h2 class="page-title">PART 1 ON ONE PAGE</h2>
  <div class="sub">Verses 1–11 in five lines</div>
  <div class="steps">
    <div><b>Verses 1–3.</b> No one can praise Śiva fully, not even Brahmā; so each praises as far as they can, to purify their own speech.</div>
    <div><b>Verses 4–6.</b> One power in three forms; the doubter's questions answered: a world made of parts points to a Maker.</div>
    <div><b>Verse 7.</b> Many paths, straight or winding; one goal, as all rivers reach the sea.</div>
    <div><b>Verses 8–9.</b> Śiva owns a bull, a skull and ash, and gives the gods their wealth; the poet leaves the philosophers arguing and simply praises.</div>
    <div><b>Verses 10–11.</b> Brahmā and Viṣṇu fail to measure the pillar of fire, but devotion brings Śiva near; Rāvaṇa's power was the fruit of his devotion.</div>
  </div>
  {talk("What happens in Part 2?","Rāvaṇa tries to lift Kailāsa, Śiva drinks the poison, burns Kāma and destroys the three cities with a chariot made of the earth.")}
  <div class="key">Śiva Mahimna, Part 1: <b>praise beyond words, and every river reaching the sea</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śiva Mahimna Stotram, verses 1–11. Sanskrit text from sanskritdocuments.org (Puṣpadanta's Śivamahimna Stotram, with translation by Devendraray V. Bhatt and S. V. Ganesan), shown in IAST; meanings are our own plain-English renderings, checked against that translation. The story of Puṣpadanta is traditional; versions differ. Not independently verified: the traditional story, the Rāmakṛṣṇa anecdote, and the split of verses between editions. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
html=head+''.join(b)+tail
open('Shiva_Mahimna_Stotram_Part1.html','w').write(html)
print(len(html))
