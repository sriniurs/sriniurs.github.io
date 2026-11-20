import re,sys
sys.path.insert(0,'.')
from sdata1 import talk,person,F,SUN,HILL,TEMPLE
from sdata2 import V
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śrī Veṅkaṭeśa Suprabhātam · Part 2 · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="The Śrī Veṅkaṭeśa Suprabhātam, Part 2 (verses 16–29), explained verse by verse in plain English with illustrations: the dawn hymn of Tirumala.">',head)
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
  <div class="burst yel">PART 2 OF 5</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.6vw,72px)">ŚRĪ VEṄKAṬEŚA<br>SUPRABHĀTAM</h1>
  <div class="series">PART 2 · VERSES 16–29 · THE COURT AT THE DOOR</div>
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
  <h2 class="page-title">PREVIOUSLY · AND NOW</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Part 1</b> (verses 1–15), Viśvāmitra's call to Rāma opened the hymn. Lakṣmī was greeted first; then the whole world woke: the seven sages with lotuses, the gods singing, the parrots, Nārada's vīṇā, the bees, the churning in the cowherd homes, and the gods queuing at the golden door.</p>
    <p><b>In Part 2</b> (verses 16–29), the court of the universe gathers. The guardians of the eight directions, the royal vehicles, the nine planets and the great devotees arrive. The poet calls the Lord by His names and His ten avatāras, the priests bring water for His bath, the sun rises, and the Suprabhātam ends with its blessing.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Govindā Govindā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Who's at the door this time?","Everyone! Gods, planets, sacred animals, sages, yogis, devotees. By verse 27 the whole universe is waiting for Him to wake.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">PART 2 IN ONE GO</h2>
  <div class="sub">Verses 16–22, for chanting</div>
  <div class="full">{''.join(full(v) for v in V[:7])}</div>
</section>
<section class="page" id="full2">
  <h2 class="page-title">PART 2 IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 23–29</div>
  <div class="full">{''.join(full(v) for v in V[7:])}</div>
  <div class="note">Each line is split at its natural pause. Text checked against shlokam.org; variant spellings are noted on the verse pages.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE COURT AT THE DOOR</h2>
  <div class="sub">Who gathers to greet the Lord in verses 16–29</div>
  <table class="ct">
    <tr><th>Verse</th><th>Who comes</th><th>What they bring</th></tr>
    <tr><td><b>16</b></td><td>The eight guardians of the directions</td><td>Folded hands, ready to serve</td></tr>
    <tr><td><b>17</b></td><td>Garuḍa, lion, Śeṣa, elephant, horse</td><td>Eagerness to carry Him</td></tr>
    <tr><td><b>18</b></td><td>The nine planets</td><td>Service as servants' servants</td></tr>
    <tr><td><b>19–20</b></td><td>Devotees; ordinary people</td><td>Love that wants nothing else</td></tr>
    <tr><td><b>21–24</b></td><td>The poet himself</td><td>His names and ten avatāras</td></tr>
    <tr><td><b>25</b></td><td>Vedic scholars</td><td>Scented water in golden pots</td></tr>
    <tr><td><b>26</b></td><td>Sun, lotuses, birds, Śrīvaiṣṇavas</td><td>Full sunrise</td></tr>
    <tr><td><b>27</b></td><td>Brahmā, sages, yogis</td><td>Auspicious objects</td></tr>
    <tr><td><b>28–29</b></td><td>The poet, and us</td><td>Final praise; the blessing</td></tr>
  </table>
  <div class="panel reading" style="margin-top:10px">
    <p><b>A royal court.</b> A suprabhāta treats the Lord as a king waking in his palace. Ministers, vassal kings and priests wait outside his chamber; here they are gods, planets and sages.</p>
    <p><b>The refrains change.</b> Verses 16–24, 27 and 28 end "śrī-veṅkaṭācala-pate tava suprabhātam". Verses 25 and 26 vary the ending, and verse 29, the blessing, has no refrain at all.</p>
  </div>
  {talk("Why make God's waking so grand?","Because the whole universe depends on Him. If He is the King of kings, His morning court is the whole creation.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Previously, and Now</a></li>
    <li><span class="num">🔤</span><a href="#full">Part 2 in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Court at the Door</a></li>
        <li><span class="num">∑</span><a href="#end">Part 2 on One Page</a></li>
    <li class="part">VERSES 16–29</li>
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
  <h2 class="page-title">PART 2 ON ONE PAGE</h2>
  <div class="sub">Verses 16–29 in five lines</div>
  <div class="steps">
    <div><b>Verses 16–18.</b> The guardians of the directions, the royal vehicles and the nine planets wait as His servants.</div>
    <div><b>Verses 19–20.</b> Devotees want only His feet; one look at His tower makes earth better than heaven.</div>
    <div><b>Verses 21–24.</b> A garland of names: Lord of Śrī and Bhū, Padmanābha, Mādhava, and all ten avatāras.</div>
    <div><b>Verses 25–27.</b> Scented water for His bath, full sunrise, and the whole court with auspicious gifts.</div>
    <div><b>Verses 28–29.</b> The bridge across saṃsāra, and the blessing: wisdom for all who recite it at dawn.</div>
  </div>
  {talk("What comes after the Suprabhātam?","Part 3: the Stotram, eleven verses praising the Lord's beauty and qualities, now that He is awake.")}
  <div class="key">Suprabhātam, Part 2: <b>the whole universe gathers at His door</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Veṅkaṭeśa Suprabhātam, verses 16–29. Text checked word by word against shlokam.org; variant spellings are noted. Background: Tirumala Tirupati Devasthanams (four sections of 29, 11, 16 and 14 verses by Prativādi Bhayaṅkara Aṇṇan, disciple of Maṇavāḷa Māmuni); Wikipedia (composed c. 1420–1432; the Rāmāyaṇa opening verse; vasantatilakā metre; M. S. Subbulakshmi). Meanings are our own plain-English renderings. Lists of the ten avatāras and of the eight directional guardians vary between traditions. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Venkatesa_Suprabhatam_Part2.html','w').write(head+''.join(b)+tail)
