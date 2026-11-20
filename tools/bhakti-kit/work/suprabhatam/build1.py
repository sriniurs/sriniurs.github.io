import re,sys
sys.path.insert(0,'.')
from sdata1 import V,talk,person,F,SUN,HILL,TEMPLE
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śrī Veṅkaṭeśa Suprabhātam · Part 1 · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Kausalyā suprajā rāma: the Śrī Veṅkaṭeśa Suprabhātam, Part 1 (verses 1–15), explained verse by verse in plain English with illustrations: the dawn hymn of Tirumala.">',head)
head=head.replace('</style>','  .iast .cl2{padding-left:2.2em}\n  .full .ln2{padding-left:2.2em}\n  @media(max-width:720px){.iast .cl2{padding-left:1.4em}.full .ln2{padding-left:1.4em}}\n</style>',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
def iast(v): return '<div class="iast">'+''.join(f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>' for a,b in v['lines'])+'</div>'
def full(v):
    o=f'<p><span class="vn">VERSE {v["n"]}</span>'
    for a,b in v['lines']:
        b=re.sub(r'\s*‖(\d+)‖$',r'<span class="end">‖ \1 ‖</span>',b)
        o+=f'<span class="ln">{a}</span><span class="ln ln2">{b}</span>'
    return o+'</p>'
vid=lambda v: v.get('ids',v['n'])
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Sunrise over seven green hills with a golden temple on the top, and a bell and a lamp in front">'
 '<circle cx="190" cy="150" r="70" fill="#ffd60a" stroke="#ff8c1a" stroke-width="4"/>'
 +''.join(f'<path d="M{-10+56*k} 230 l38 -{60+(k%3)*24} l38 {60+(k%3)*24}z" fill="#2a7a4a" stroke="#111" stroke-width="2"/>' for k in range(7))
 +'<g transform="translate(190 150)" stroke="#111" stroke-width="3"><rect x="-34" y="-30" width="68" height="30" fill="#ffd60a"/><path d="M-24 -30 l24 -40 l24 40z" fill="#e0a800"/><path d="M0 -70 v-12" /><circle cy="-84" r="4" fill="#ffd60a"/></g>'
 '<path d="M0 230 H380 V268 H0Z" fill="#1b5e3a"/><g transform="translate(70 246)" stroke="#111" stroke-width="2"><path d="M-14 0 h28 l-4 8 h-20z" fill="#e0a800"/><path d="M0 0 q-8 -16 0 -24 q8 8 0 24z" fill="#ff8c1a"/></g>'
 '<g transform="translate(310 236)" stroke="#111" stroke-width="2"><path d="M-14 16 q0 -30 14 -30 q14 0 14 30z" fill="#c9a26b"/><circle cy="20" r="4" fill="#c9a26b"/></g></svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: Vishvamitra waking young Rama at dawn; the poet Annan composing at Kanchipuram; priests singing before the golden door at Tirumala">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#ffe3c4','RĀMĀYAṆA'),('#e7f4ea','AṆṆAN, c. 1430'),('#dfe9f6','TIRUMALA TODAY')]))
 +'<circle cx="120" cy="40" r="14" fill="#ffd60a"/>'+person(50,150,'#ff8c1a')+person(100,160,'#4a7fd0','#4a7fd0',.8)
 +person(230,150,'#fff')+'<rect x="246" y="140" width="40" height="26" fill="#fff3b0" stroke="#111" stroke-width="2"/>'
 +'<rect x="370" y="40" width="70" height="120" fill="#ffd60a" stroke="#111" stroke-width="3"/><path d="M405 40 v120" stroke="#111"/>'+person(340,160,'#fff','#f2c79b',.8)+'</svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 1 OF 5</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.6vw,72px)">ŚRĪ VEṄKAṬEŚA<br>SUPRABHĀTAM</h1>
  <div class="series">PART 1 · VERSES 1–15 · THE WORLD WAKES UP</div>
  <div class="tag">The dawn hymn of Tirumala · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First Part 1 for chanting in one go. Then the story of how the hymn came to be and its background, and <b>two pages for each verse</b>: the chant, a picture, what it says and the key words; then a deeper look, background facts, the inner teaching and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>"Kausalyā suprajā rāma…" For millions of Indian homes, this is the sound of dawn. Before the milk boils and the day begins, M. S. Subbulakshmi's voice wakes Lord Veṅkaṭeśvara, and wakes the household with Him.</p>
    <p>The Śrī Veṅkaṭeśa Suprabhātam is sung every morning at Tirumala, before the golden door of the sanctum, as the Lord is woken. It begins with a verse from the Rāmāyaṇa, wakes the Goddess, and then shows the whole world rising to greet the Lord of the Seven Hills: sages with lotuses, gods singing, parrots reciting, bees humming, the cowherd homes churning butter.</p>
    <p>The full hymn has four sections and seventy verses. We take it in five parts. This first part covers verses 1–15 of the Suprabhātam proper.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Govindā Govindā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
</section>

<section class="page" id="full">
  <h2 class="page-title">PART 1 IN ONE GO</h2>
  <div class="sub">Verses 1–8, for chanting</div>
  <div class="full">{''.join(full(v) for v in V[:7])}</div>
</section>
<section class="page" id="full2">
  <h2 class="page-title">PART 1 IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 9–15</div>
  <div class="full">{''.join(full(v) for v in V[7:])}</div>
  <div class="note">Each line is split at its natural pause. Text checked against shlokam.org and Wikipedia; variant spellings are noted on the verse pages.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · A MORNING CALL, 600 YEARS OLD</h2>
  <div class="sub">From Viśvāmitra's call to the golden door of Tirumala</div>
  {story_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>The first morning call.</b> In the Rāmāyaṇa, the sage Viśvāmitra wakes the young Rāma in the forest: "Kausalyā suprajā rāma…" Every suprabhātam begins from this one verse.</div>
      <div><b>A disciple's task.</b> In the early 15th century, the Śrīvaiṣṇava teacher Maṇavāḷa Māmuni asks his disciple <b>Prativādi Bhayaṅkaram Aṇṇan</b> of Kāñcīpuram to compose a dawn hymn for the Lord of Tirumala.</div>
      <div><b>Tamil roots.</b> Aṇṇan draws on the Tamil dawn songs of the Āḻvārs, Toṇḍaraḍippoḍi's <i>Tiruppaḷḷiyeḻucci</i> and Āṇḍāḷ's <i>Tiruppāvai</i>, and writes in Sanskrit.</div>
      <div><b>Four sections.</b> He writes the Suprabhātam (29 verses), the Stotram (11), the Prapatti (16) and the Maṅgalāśāsanam (14): 70 in all.</div>
      <div><b>Every dawn since.</b> It is sung daily at Tirumala before the golden door, and M. S. Subbulakshmi's recording carried it into homes everywhere.</div>
    </div>
  </div>
  {talk("Six hundred years, every single morning?","That's the tradition: sung at the Lord's door each dawn. And for most of us, MS Amma's voice is what we hear.")}
</section>

<section class="page" id="about">
  <h2 class="page-title">ABOUT THE SUPRABHĀTAM</h2>
  <div class="sub">A royal wake-up for the Lord of the Seven Hills</div>
  <div class="g2">
    <div class="card bg-blue"><h4>✍️ The author</h4><p><b>Prativādi Bhayaṅkaram Aṇṇan</b> (also Anantācārya), a Śrīvaiṣṇava scholar of Kāñcīpuram and disciple of Maṇavāḷa Māmuni; composed around 1420–1432.</p></div>
    <div class="card bg-yellow"><h4>🎵 The sound</h4><p>Mostly in <b>vasantatilakā</b>, "ornament of spring": fourteen syllables a line, a flowing metre loved for dawn hymns.</p></div>
  </div>
  <div class="panel reading">
    <p><b>The genre.</b> A <i>suprabhāta</i>, "auspicious dawn", is a hymn sung to wake a deity, treating the Lord as a beloved king whose court gathers at sunrise. The Veṅkaṭeśa Suprabhātam is the most famous of all.</p>
    <p><b>The refrains.</b> Most verses end "śeṣādri-śekhara-vibho tava suprabhātam" or "śrī-veṅkaṭācala-pate tava suprabhātam": "Lord of Śeṣādri / Lord of Veṅkaṭa hill, a good morning to You!"</p>
  </div>
  <table class="ct">
    <tr><th>Part</th><th>Section</th><th>Verses</th></tr>
    <tr><td><b>1</b> (this one)</td><td>Suprabhātam: the world wakes up</td><td>1–15</td></tr>
    <tr><td><b>2</b></td><td>Suprabhātam: the court at the door</td><td>16–29</td></tr>
    <tr><td><b>3</b></td><td>Stotram: praise and refuge</td><td>11 verses</td></tr>
    <tr><td><b>4</b></td><td>Prapatti: surrender at His feet</td><td>16 verses</td></tr>
    <tr><td><b>5</b></td><td>Maṅgalāśāsanam: the blessing</td><td>14 verses</td></tr>
  </table>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">Part 1 in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story: A Morning Call, 600 Years Old</a></li>
    <li><span class="num">ℹ</span><a href="#about">About the Suprabhātam</a></li>
    <li><span class="num">∑</span><a href="#end">Part 1 on One Page</a></li>
    <li class="part">VERSES 1–15</li>
    {''.join(f'<li><span class="num">{vid(v)}</span><a href="#v{vid(v)}">{"Verses" if "–" in v["n"] else "Verse"} {v["n"]}: {v["theme"].title().replace("’S","’s").replace(chr(39)+"S",chr(39)+"s")}</a></li>' for v in V)}
  </ul>
</section>
''']
for v in V:
    n=vid(v); lab=("VERSES " if "–" in v['n'] else "VERSE ")+v['n']
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    c=v['cards']; note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    b.append(f'''<section class="page" id="v{n}">
  <h2 class="page-title">{lab}</h2>
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
  <h2 class="page-title">{lab} · GOING DEEPER</h2>
  <div class="sub">{v['theme']}</div>
  <div class="panel reading">{v['deep']}</div>
  <div class="g2"><div class="card bg-yellow"><h4>{c[0]}</h4><p>{c[1]}</p></div><div class="card bg-blue"><h4>{c[2]}</h4><p>{c[3]}</p></div></div>
  <div class="inner">{v['inner']}</div>
  {talk(*v['talk'])}
  <div class="key">{v['key']}</div>{note}
</section>
''')
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 1 ON ONE PAGE</h2>
  <div class="sub">Verses 1–15 in five lines</div>
  <div class="steps">
    <div><b>Verses 1–2.</b> Viśvāmitra's call to Rāma, then to Govinda: arise, and bless the three worlds.</div>
    <div><b>Verses 3–4.</b> Good morning first to the Mother, Lakṣmī, who lives in His heart and speaks for us.</div>
    <div><b>Verses 5–6.</b> The seven sages bring lotuses; the gods sing; Bṛhaspati reads the day's almanac.</div>
    <div><b>Verses 7–12.</b> The breeze, the parrots, Nārada's vīṇā, the bees, the churning in the cowherd homes: all nature wakes for Him.</div>
    <div><b>Verses 13–15.</b> Śrīnivāsa, friend of all; the gods queue at His golden door; the names of the seven hills.</div>
  </div>
  {talk("What happens in Part 2?","The court gathers: the ten avatāras, the devotees at the door, the great Vaiṣṇava saints, the sunrise itself, and the blessing for all who hear the Suprabhātam.")}
  <div class="key">Suprabhātam, Part 1: <b>the whole world wakes to greet the Lord</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Veṅkaṭeśa Suprabhātam, verses 1–15. Text checked word by word against shlokam.org and the Wikipedia article "Suprabhatam"; variant spellings are noted. Background: Tirumala Tirupati Devasthanams (four sections of 29, 11, 16 and 14 verses by Prativādi Bhayaṅkara Aṇṇan, disciple of Maṇavāḷa Māmuni); Wikipedia (composed c. 1420–1432; the Rāmāyaṇa opening verse; vasantatilakā metre; M. S. Subbulakshmi). Meanings are our own plain-English renderings. Not independently verified: lists of the seven hills vary. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Venkatesa_Suprabhatam_Part1.html','w').write(head+''.join(b)+tail)
