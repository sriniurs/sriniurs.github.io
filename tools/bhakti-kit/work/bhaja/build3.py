import re,sys
sys.path.insert(0,'.')
from data3 import V
from data1 import talk,person,F
LAB={'28':'Verses 28–29','32':'Verses 32–33'}
src=open('/home/claude/work/stotram.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Bhaja Govindam · Part 3 · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Bhaja govindaṃ bhaja govindaṃ: Ādi Śaṅkara\'s Bhaja Govindam (Moha Mudgara), Part 3 (verses 21–33), explained verse by verse in plain English with illustrations: punarapi jananaṃ, one Viṣṇu in all, the feet of the guru, and the grammarian awakened.">',head)
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
  <div class="burst yel">PART 3 OF 3</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(30px,9vw,76px)">BHAJA GOVINDAM</h1>
  <div class="series">PART 3 · VERSES 21–33 · THE WAY ACROSS</div>
  <div class="tag">Ādi Śaṅkara's "hammer for delusion" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First Part 3 for chanting in one go. Then the end of the grammarian's story and the hymn's background, and <b>two pages for each verse</b>: the chant, a picture, what it says and the key words; then a deeper look, background facts, the inner teaching and the one thing to remember. Parts 1–2 covered verses 1–20.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Parts 1 and 2 hammered at delusion: wealth, the body, family, time and desire. Part 3 (verses 21–33) turns from warning to the way across.</p>
    <p>It begins with the most-sung line after the refrain, "punarapi jananaṃ punarapi maraṇaṃ", and a cry for grace. Then come the great teachings of oneness: one Viṣṇu in you, in me, in all; see the Self in friend and foe; ask "who am I?"; sing, meditate, keep good company, give.</p>
    <p>It ends at the guru's feet, with the Lord seen in one's own heart, and with the old grammarian of Kāśī awakened at last.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
</section>

<section class="page" id="full">
  <h2 class="page-title">PART 3 IN ONE GO</h2>
  <div class="sub">Verses 21–33, for chanting</div>
  <div class="full">{''.join(full(i,v) for i,v in enumerate(V))}</div>
  <div class="note">In singing, the refrain "bhaja govindaṃ bhaja govindaṃ, govindaṃ bhaja mūḍhamate" is usually repeated after every verse. Text as on sanskritdocuments.org.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · THE GRAMMARIAN AWAKENED</h2>
  <div class="sub">How the Kāśī story ends, and how the hymn lives on</div>
  {story_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>The song goes on.</b> Śaṅkara's twelve verses and his disciples' fourteen fill the lane in Kāśī.</div>
      <div><b>The old man listens.</b> The grammarian, cramming "ḍukṛñ karaṇe", stops and hears.</div>
      <div><b>Awakened.</b> Verse 32 says he was awakened by Śaṅkara's disciples, his mind purified.</div>
      <div><b>The Name.</b> The last verse repeats the refrain and gives the final answer: remembering the Lord's Name is the way across the ocean.</div>
      <div><b>Still sung.</b> Twelve centuries later it is sung in homes, temples and concert halls, most famously in M. S. Subbulakshmi's recording.</div>
    </div>
  </div>
  <div class="g3">
    <div class="card bg-yellow"><h4>The old man</h4><p>From <b>grammar</b> to the <b>Name</b>.</p></div>
    <div class="card bg-red"><h4>The teachers</h4><p><b>Śaṅkara</b> and his disciples.</p></div>
    <div class="card bg-green"><h4>The answer</h4><p><b>Bhaja govindaṃ</b>.</p></div>
  </div>
  {talk("So the hymn tells its own ending?","Yes: verse 32 says the grammarian was awakened. It's a story inside a song, with a happy ending.")}
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
    <tr><td><b>2</b></td><td>11–20</td><td>Time steals everything; the ascetic who is still attached; scripture, Gaṅgā and Govinda</td></tr>
    <tr><td><b>3</b> (this one)</td><td>21–33</td><td>Birth and death again and again; one Viṣṇu in all; the guru's feet; the closing verses</td></tr>
  </table>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">Part 3 in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story: The Grammarian Awakened</a></li>
    <li><span class="num">ℹ</span><a href="#about">About Bhaja Govindam</a></li>
    <li><span class="num">∑</span><a href="#end">Part 3 on One Page</a></li>
    <li class="part">VERSES 21–33</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{LAB.get(v["n"],"Verse "+v["n"])}: {v["theme"].title().replace("’S","’s")}</a></li>' for i,v in enumerate(V))}
  </ul>
</section>
''']
for i,v in enumerate(V):
    n=v['n']
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    c=v['cards']
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    b.append(f'''<section class="page" id="v{n}">
  <h2 class="page-title">{LAB.get(n,"Verse "+n).upper()}</h2>
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
  <h2 class="page-title">{LAB.get(n,"Verse "+n).upper()} · GOING DEEPER</h2>
  <div class="sub">{v['theme']}</div>
  <div class="panel reading">{v['deep']}</div>
  <div class="g2"><div class="card bg-yellow"><h4>{c[0]}</h4><p>{c[1]}</p></div><div class="card bg-blue"><h4>{c[2]}</h4><p>{c[3]}</p></div></div>
  <div class="inner">{v['inner']}</div>
  {talk(*v['talk'])}
  <div class="key">{v['key']}</div>{note}
</section>
''')
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 3 ON ONE PAGE</h2>
  <div class="sub">Verses 21–33, and the whole hymn</div>
  <div class="steps">
    <div><b>Verses 21–23.</b> Born again, dying again: save me, Murāri; the free yogī plays like a child; "who am I?", and the world as a dream.</div>
    <div><b>Verses 24–26.</b> One Viṣṇu in all, so why be angry; see the Self in friend and foe; drop the four thieves and ask "who am I?".</div>
    <div><b>Verses 27–29.</b> Sing, meditate, keep good company, give; pleasure brings illness, wealth brings fear.</div>
    <div><b>Verses 30–31.</b> Practise with great care; serve the guru, and see the Lord in your own heart.</div>
    <div><b>Verses 32–33.</b> The grammarian awakened; remembering the Name is the way across.</div>
  </div>
  <div class="panel"><span class="caption">The whole Bhaja Govindam</span><p style="margin:0">Part 1: wake up, O mind (1–10) · Part 2: the noose of desire (11–20) · Part 3: the way across (21–33).</p></div>
  {talk("If you remember one line?","Verse 9, the ladder from good company to freedom, or simply the refrain: bhaja govindaṃ, O mind.")}
  <div class="key">Bhaja Govindam: <b>a hammer for delusion, and a hand held out to every mind</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on Bhaja Govindam, verses 21–33. Sanskrit text checked word by word against sanskritdocuments.org (bhajagovindam.itx, transliterated by M. Giridhar), shown in IAST; meanings are our own plain-English renderings. Recorded variants are noted on the verse pages (26, 33). The Kāśī story is traditional. Not independently verified: the division of verses between Śaṅkara and his disciples, which varies between editions. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Bhaja_Govindam_Part3.html','w').write(head+''.join(b)+tail)
