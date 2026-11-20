import re,sys
sys.path.insert(0,'.')
from data2 import V
from data1 import talk,person,F
src=open('/home/claude/work/stotram.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Bhaja Govindam · Part 2 · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Bhaja govindaṃ bhaja govindaṃ: Ādi Śaṅkara\'s Bhaja Govindam (Moha Mudgara), Part 2 (verses 11–20), explained verse by verse in plain English with illustrations: time, desire, the robe and the belly, and a little Gītā.">',head)
theme='''  /* Viṣṇu theme: light blue */
  .cover{background:radial-gradient(circle at 50% 38%,#8fd0f5,#1d6fb8 55%,#0b3d6e)}
  .sloka-head{background:#1d6fb8}
  .sloka{background:#e3f2fd;box-shadow:7px 7px 0 #1d6fb8}
  .sub{color:#1d6fb8}
  .num{background:#1d6fb8}
  .steps div:before{background:#1d6fb8}
  .full .vn,.full .end{color:#1d6fb8}
  .iast:before{color:#1d6fb8}
  .contlink{color:#1d6fb8}
</style>'''
head=head.replace('</style>',theme,1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
def iast(v): return '<div class="iast">'+''.join(f'<span class="cl">{l}</span>' for l in v['lines'])+'</div>'
def full(i,v):
    ls=[l for l in v['lines'] if l!='· · ·']; ls[-1]=re.sub(r'\s*‖(\d+)‖$',r'<span class="end">‖ \1 ‖</span>',ls[-1])
    return f'<p><span class="vn">VERSE {v["n"]}</span>'+''.join(f'<span class="ln">{l}</span>' for l in ls)+'</p>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Govinda as a young cowherd playing the flute beside a cow, under a pillar of light, with the words bhaja govindam">'
 '<rect x="174" y="0" width="32" height="268" fill="#fff" opacity=".18"/><path d="M0 220 Q190 196 380 220 V268 H0Z" fill="#2a7a4a" stroke="#111" stroke-width="2"/>'
 '<g transform="translate(190 170)" stroke="#111" stroke-width="3"><path d="M-34 60 q-6 -80 34 -96 q40 16 34 96z" fill="#ffd60a"/><path d="M-22 -10 q22 14 44 0" fill="none" stroke="#e63946" stroke-width="4"/><circle cy="-56" r="20" fill="#4a7fd0"/><path d="M-30 -30 q-10 20 6 30 M30 -30 q12 8 8 22" fill="none" stroke="#4a7fd0" stroke-width="8"/><path d="M-6 -76 q10 -30 22 -20 q-6 10 -14 22z" fill="#2a9d6f"/><circle cx="8" cy="-90" r="4" fill="#1d6fb8"/><path d="M-28 -36 L44 -50" stroke="#7a5a3a" stroke-width="5"/></g>'
 '<g transform="translate(80 210)" stroke="#111" stroke-width="2.5"><ellipse rx="44" ry="22" fill="#fff"/><circle cx="44" cy="-14" r="14" fill="#fff"/><path d="M40 -26 l-6 -10 M52 -26 l6 -10"/><path d="M-30 20 v16 M30 20 v16" /></g>'
 '<text x="300" y="80" text-anchor="middle" font-family="Bangers" font-size="22" fill="#fff">♪ bhaja</text><text x="310" y="108" text-anchor="middle" font-family="Bangers" font-size="22" fill="#ffd60a">govindaṃ…</text></svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Shankara and his disciples on a lane in Kashi meeting an old man reciting grammar rules from a book">'
 '<rect width="460" height="210" fill="#fff8ec"/><path d="M0 170 h460" stroke="#c9a26b" stroke-width="4"/><path d="M380 30 h70 v140 h-70z M390 50 h16 v20 h-16z M420 50 h16 v20 h-16z" fill="#e8c27a" stroke="#111" stroke-width="2"/>'
 +person(110,150,'#ff8c1a','#f2c79b',1.4).replace('stroke-width="2.5"','stroke-width="2.5"')+'<path d="M140 60 v110" stroke="#7a5a3a" stroke-width="5"/>'
 +person(60,156,'#ff8c1a','#f2c79b',1.0)+person(30,158,'#ff8c1a','#f2c79b',.9)
 +person(300,150,'#999','#e0c09b',1.3)+'<rect x="262" y="140" width="70" height="30" fill="#fff3b0" stroke="#111" stroke-width="2"/><text x="297" y="160" text-anchor="middle" font-family="Noto Sans" font-style="italic" font-size="11">ḍukṛñ karaṇe…</text>'
 '<text x="110" y="40" text-anchor="middle" font-family="Bangers" font-size="16" fill="#1d6fb8">ŚAṄKARA</text><text x="300" y="50" text-anchor="middle" font-family="Bangers" font-size="14">THE OLD GRAMMARIAN</text><text x="415" y="196" text-anchor="middle" font-family="Bangers" font-size="12">KĀŚĪ</text></svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 2 OF 3</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(30px,9vw,76px)">BHAJA GOVINDAM</h1>
  <div class="series">PART 2 · VERSES 11–20 · THE NOOSE OF DESIRE</div>
  <div class="tag">Ādi Śaṅkara's "hammer for delusion" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First Part 2 for chanting in one go. Then the story of the fourteen disciples and the hymn's background, and <b>two pages for each verse</b>: the chant, a picture, what it says and the key words; then a deeper look, background facts, the inner teaching and the one thing to remember. Part 1 covered verses 1–10; Part 3 covers 21–33.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>In Part 1, Śaṅkara shook the old grammarian awake: wealth, the body, family and life itself are fleeting; turn to Govinda.</p>
    <p>Part 2 (verses 11–20) goes further. Time plays and life runs out; desire never ages; robes and austerities can be costumes; even pilgrimages are not enough without knowledge. Here Śaṅkara's own "garland of twelve" ends, and his disciples begin to speak.</p>
    <p>And then the tone turns gentle: whoever delights in the highest rejoices anywhere, and a little Gītā, a drop of Gaṅgā water and one sincere prayer are enough to lose the fear of death.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
</section>

<section class="page" id="full">
  <h2 class="page-title">PART 2 IN ONE GO</h2>
  <div class="sub">Verses 11–20, for chanting</div>
  <div class="full">{''.join(full(i,v) for i,v in enumerate(V))}</div>
  <div class="note">In singing, the refrain "bhaja govindaṃ bhaja govindaṃ, govindaṃ bhaja mūḍhamate" is usually repeated after every verse. Text as on sanskritdocuments.org.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · THE FOURTEEN DISCIPLES</h2>
  <div class="sub">How the "garland of twelve" grew into a hymn</div>
  {story_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>The master's twelve.</b> On the lane in Kāśī, Śaṅkara sings to the old grammarian. His verses, with the refrain, make the <b>Dvādaśa-mañjarikā</b>, "the garland of twelve".</div>
      <div><b>The signature.</b> A verse closes it: "thus this whole teaching was given to the grammarian by Śrī Śaṅkara Bhagavatpāda".</div>
      <div><b>The disciples are moved.</b> Tradition says fourteen of his disciples, hearing the master, each added a verse of their own.</div>
      <div><b>The garland of fourteen.</b> Their verses form the <b>Caturdaśa-mañjarikā</b>. Some lists name the disciple for each verse, including Padmapāda, Toṭaka, Hastāmalaka and Sureśvara; the lists differ.</div>
      <div><b>One hymn.</b> Together with a few closing verses, the two garlands became the Bhaja Govindam we sing today.</div>
    </div>
  </div>
  <div class="g3">
    <div class="card bg-yellow"><h4>The master</h4><p><b>Śaṅkara</b>: twelve verses and the refrain.</p></div>
    <div class="card bg-red"><h4>The pupils</h4><p><b>Fourteen</b> disciples, a verse each.</p></div>
    <div class="card bg-green"><h4>The result</h4><p>A hymn sung by <b>everyone</b>.</p></div>
  </div>
  {talk("The disciples wrote part of it?","So tradition says. That's why some verses sound like monks warning monks: they were students taking the master's words to heart.")}
</section>

<section class="page" id="about">
  <h2 class="page-title">ABOUT BHAJA GOVINDAM</h2>
  <div class="sub">A Vedānta primer in song</div>
  <div class="g2">
    <div class="card bg-blue"><h4>✍️ The author</h4><p>Ascribed to <b>Ādi Śaṅkara</b>, the 8th-century teacher of Advaita Vedānta, with verses traditionally credited to his disciples.</p></div>
    <div class="card bg-yellow"><h4>🎵 The sound</h4><p>Short rhyming lines of sixteen beats (<i>mātrās</i>), in a metre called <b>pādākulaka</b>: easy to sing and remember.</p></div>
  </div>
  <div class="panel reading">
    <p><b>Two garlands.</b> Tradition groups the verses into the <b>Dvādaśa-mañjarikā</b>, "the garland of twelve" that Śaṅkara sang, and the <b>Caturdaśa-mañjarikā</b>, "the garland of fourteen" by his disciples. Versions differ in how they number and divide them.</p>
    <p><b>For everyone.</b> Its refrain names Govinda, Kṛṣṇa, so it is loved by Advaitins, Smārtas and Vaiṣṇavas alike. M. S. Subbulakshmi's recording made it famous across India.</p>
    <p><b>Knowledge and devotion.</b> Coming from the great teacher of knowledge (<i>jñāna</i>), its message is striking: knowledge must ripen into devotion (<i>bhakti</i>).</p>
  </div>
  <table class="ct">
    <tr><th>Part</th><th>Verses</th><th>Theme</th></tr>
    <tr><td><b>1</b></td><td>1–10</td><td>Wake up: wealth, the body, the drop on the lotus leaf, family, "who are you?", good company</td></tr>
    <tr><td><b>2</b> (this one)</td><td>11–20</td><td>Time steals everything; the ascetic who is still attached; scripture, Gaṅgā and Govinda</td></tr>
    <tr><td><b>3</b></td><td>21–33</td><td>Birth and death again and again; one Viṣṇu in all; the guru's feet; the closing verses</td></tr>
  </table>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">Part 2 in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story: The Fourteen Disciples</a></li>
    <li><span class="num">ℹ</span><a href="#about">About Bhaja Govindam</a></li>
    <li><span class="num">∑</span><a href="#end">Part 2 on One Page</a></li>
    <li class="part">VERSES 11–20</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">Verse {v["n"]}{"–13a" if v["n"]=="13" else ""}: {v["theme"].title().replace("’S","’s")}</a></li>' for i,v in enumerate(V))}
  </ul>
</section>
''']
for i,v in enumerate(V):
    n=v['n']
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    c=v['cards']
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    b.append(f'''<section class="page" id="v{n}">
  <h2 class="page-title">VERSE {n}{" & 13A" if n=="13" else ""}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(v)}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>
    <div class="plain">{v['plain']}</div>
    <table class="ct"><tr><th>Word</th><th>Means</th></tr>{words}</table>
  </div>
  <p class="center" style="margin:0"><a href="#v{n}b" class="contlink">Continue: going deeper ➜</a></p>
</section>
<section class="page" id="v{n}b">
  <h2 class="page-title">VERSE {n}{" & 13A" if n=="13" else ""} · GOING DEEPER</h2>
  <div class="sub">{v['theme']}</div>
  <div class="panel reading">{v['deep']}</div>
  <div class="g2"><div class="card bg-yellow"><h4>{c[0]}</h4><p>{c[1]}</p></div><div class="card bg-blue"><h4>{c[2]}</h4><p>{c[3]}</p></div></div>
  <div class="inner">{v['inner']}</div>
  {talk(*v['talk'])}
  <div class="key">{v['key']}</div>{note}
</section>
''')
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 2 ON ONE PAGE</h2>
  <div class="sub">Verses 11–20 in five lines</div>
  <div class="steps">
    <div><b>Verses 11–12.</b> Time takes wealth, followers and youth in a blink; seasons return, life runs out, desire never tires.</div>
    <div><b>Verse 13.</b> Stop worrying as if no one were in charge; good company is the only boat. Śaṅkara's "garland of twelve" ends.</div>
    <div><b>Verses 14–16.</b> The disciples speak: a robe is not renunciation; desire outlasts the body; it can bind a hermit too.</div>
    <div><b>Verses 17–18.</b> Pilgrimages without knowledge don't free us; true dispassion is happiness.</div>
    <div><b>Verses 19–20.</b> A mind resting in Brahman rejoices anywhere; a little Gītā, a drop of Gaṅgā and one prayer are enough.</div>
  </div>
  {talk("What happens in Part 3?","Birth and death again and again, the patched robe, the beggar who is a king, the four rules of life, and the closing prayer to the guru's feet.")}
  <div class="key">Bhaja Govindam, Part 2: <b>desire never ages; a little true devotion is enough</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on Bhaja Govindam, verses 11–20. Sanskrit text checked word by word against sanskritdocuments.org (bhajagovindam.itx, transliterated by M. Giridhar), shown in IAST; meanings are our own plain-English renderings. Verse 11 has a recorded variant (budhvā for hitvā). The story of the fourteen disciples is traditional; lists of names differ. Not independently verified: the division of verses between Śaṅkara and his disciples, which varies between editions. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Bhaja_Govindam_Part2.html','w').write(head+''.join(b)+tail)
