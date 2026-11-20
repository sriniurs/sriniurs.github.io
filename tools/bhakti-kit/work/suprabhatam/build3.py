import re,sys
sys.path.insert(0,'.')
from sdata1 import talk,person,F,SUN,HILL,TEMPLE
from sdata3 import V
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śrī Veṅkaṭeśa Suprabhātam · Part 3 · Stotram · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="The Śrī Veṅkaṭeśa Suprabhātam, Part 3, the Śrī Veṅkaṭeśa Stotram (11 verses), explained verse by verse in plain English with illustrations: the dawn hymn of Tirumala.">',head)
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
  <div class="burst yel">PART 3 OF 5</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.6vw,72px)">ŚRĪ VEṄKAṬEŚA<br>SUPRABHĀTAM</h1>
  <div class="series">PART 3 · THE STOTRAM · 11 VERSES OF PRAISE</div>
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
  <h2 class="page-title">NOW THAT HE IS AWAKE</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Parts 1 and 2</b>, the 29 verses of the Suprabhātam woke the Lord: Lakṣmī first, then the sages, the birds, the bees, the gods, the planets, the whole court at the golden door, until the sun was up.</p>
    <p><b>Part 3</b> is the second section of the hymn, the <b>Stotram</b>: eleven verses of praise. The poet now speaks to the Lord directly. He asks for protection, confesses his faults, sees the Lord as Kṛṣṇa and Rāma, and ends by asking forgiveness.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Govindā Govindā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is the Stotram part of the Suprabhātam?","It's the second of the four sections, always recited right after. Shorter verses, a quicker beat, and much more personal.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">THE STOTRAM IN ONE GO</h2>
  <div class="sub">Verses 1–6, for chanting</div>
  <div class="full">{''.join(full(v) for v in V[:6])}</div>
</section>
<section class="page" id="full2">
  <h2 class="page-title">THE STOTRAM IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 7–11</div>
  <div class="full">{''.join(full(v) for v in V[6:])}</div>
  <div class="note">Each line is split at its natural pause. Text checked against shlokam.org and sanskritdocuments.org; variant spellings are noted on the verse pages.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE SHAPE OF THE STOTRAM</h2>
  <div class="sub">One Lord, seen three ways</div>
  <table class="ct">
    <tr><th>Verses</th><th>Whom he sees</th><th>What he says</th></tr>
    <tr><td><b>1–3</b></td><td>Veṅkaṭeśa, with Lakṣmī</td><td>Victory to You; protect me; save me despite my faults</td></tr>
    <tr><td><b>4</b></td><td>Veṅkaṭeśa, the generous</td><td>None higher than Lakṣmī's beloved</td></tr>
    <tr><td><b>5</b></td><td>Kṛṣṇa with the gopīs</td><td>None higher than Vasudeva's son</td></tr>
    <tr><td><b>6–8</b></td><td>Rāma, Sītā's husband</td><td>Grant blessings; I worship no other</td></tr>
    <tr><td><b>9–10</b></td><td>Veṅkaṭeśa again</td><td>No lord but You; grant eternal service</td></tr>
    <tr><td><b>11</b></td><td>Hari of Śeṣa hill</td><td>Forgive all my faults</td></tr>
  </table>
  <div class="g2" style="margin-top:10px">
    <div class="card bg-yellow"><h4>🎵 Three rhythms</h4><p>Verses 1–8 in <b>toṭaka</b> (da-da-DUM ×4); 9–10 in <b>bhujaṅga-prayāta</b> (da-DUM-DUM ×4); 11 in <b>anuṣṭubh</b>.</p></div>
    <div class="card bg-blue"><h4>🙏 From praise to plea</h4><p>The Suprabhātam asked nothing; the Stotram asks: protect, save, bless, forgive.</p></div>
  </div>
  {talk("Why Kṛṣṇa and Rāma in a hymn to Veṅkaṭeśa?","Because they're one Lord. The poet sees the flute-player and the archer standing on the Seven Hills.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Now That He Is Awake</a></li>
    <li><span class="num">🔤</span><a href="#full">The Stotram in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Shape of the Stotram</a></li>
        <li><span class="num">∑</span><a href="#end">Part 3 on One Page</a></li>
    <li class="part">THE 11 VERSES</li>
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
  <h2 class="page-title">PART 3 ON ONE PAGE</h2>
  <div class="sub">The Stotram in five lines</div>
  <div class="steps">
    <div><b>Verses 1–3.</b> Victory to the Lord reddened by Lakṣmī's kuṅkuma; protect me; save me despite my faults.</div>
    <div><b>Verse 4.</b> He gives more than we ask: none higher than Lakṣmī's beloved.</div>
    <div><b>Verse 5.</b> Kṛṣṇa with His flute among the gopīs: none higher than Him.</div>
    <div><b>Verses 6–8.</b> Rāma: archer, Sītā's husband, sun to Rāvaṇa's darkness, easy to reach. I worship no other.</div>
    <div><b>Verses 9–11.</b> No lord but Veṅkaṭeśa; one visit, eternal service; forgive all my faults.</div>
  </div>
  {talk("What comes next?","Part 4: the Prapatti, sixteen verses of formal surrender at the Lord's feet. The heart of the Śrīvaiṣṇava way.")}
  <div class="key">The Stotram: <b>from praise to a personal plea</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Veṅkaṭeśa Stotram (section 2 of the Suprabhātam). Text checked word by word against shlokam.org and sanskritdocuments.org; variant spellings are noted. Background: Tirumala Tirupati Devasthanams (four sections of 29, 11, 16 and 14 verses by Prativādi Bhayaṅkara Aṇṇan, disciple of Maṇavāḷa Māmuni); Wikipedia (composed c. 1420–1432; the Rāmāyaṇa opening verse; vasantatilakā metre; M. S. Subbulakshmi). Meanings are our own plain-English renderings. Metre names are from standard prosody. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Venkatesa_Suprabhatam_Part3.html','w').write(head+''.join(b)+tail)
