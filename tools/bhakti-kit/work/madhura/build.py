import re,sys
sys.path.insert(0,'.'); sys.path.insert(0,'/home/claude/work/suprabhatam')
from sdata1 import talk,person,F,SUN,HILL,TEMPLE
from mdata import V
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Madhurāṣṭakam · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Adharaṃ madhuram: Vallabhācārya’s Madhurāṣṭakam, the hymn to Kṛṣṇa’s sweetness, explained verse by verse in plain English with illustrations.">',head)
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
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Young Krishna playing the flute by the Yamuna river under a full moon, with a cow and lotuses">'
 '<circle cx="300" cy="60" r="34" fill="#fff8c0" stroke="#111" stroke-width="3"/>'
 '<path d="M0 220 q95 -20 190 0 t190 0 V268 H0z" fill="#4aa3df" stroke="#111" stroke-width="2"/>'
 +''.join(f'<path d="M{x} 236 q-12 -18 0 -26 q12 8 0 26z" fill="#f08aa6" stroke="#111"/>' for x in (40,330))
 +'<g transform="translate(190 30) scale(1.3)" stroke="#111" stroke-width="2.5"><circle cy="56" r="15" fill="#3b6fd0"/><path d="M-10 40 q10 -14 20 0" fill="#111"/><path d="M4 36 q10 -20 6 -30" stroke="#2a9d6f" stroke-width="3" fill="none"/><circle cx="10" cy="8" r="4" fill="#1d6fb8" stroke="#2a9d6f"/><path d="M-22 150 q-4 -66 22 -78 q26 12 22 78z" fill="#ffd60a"/><path d="M-14 82 q14 30 28 0" fill="none" stroke="#e05a8a" stroke-width="4"/></g>'
 '<path d="M200 106 l70 -18" stroke="#7a5a3a" stroke-width="6" stroke-linecap="round"/>'
 '<g transform="translate(90 196)" stroke="#111" stroke-width="2"><ellipse rx="30" ry="16" fill="#fff"/><circle cx="-32" cy="-8" r="10" fill="#fff"/><circle cx="6" cy="-2" r="6" fill="#8a6a4a"/></g>'
 +''.join(f'<text x="{x}" y="{y}" font-family="Bangers" font-size="22" fill="#fff">♪</text>' for x,y in [(280,120),(310,150),(250,150)])+'</svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: Vishvamitra waking young Rama at dawn; the poet Annan composing at Kanchipuram; priests singing before the golden door at Tirumala">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#ffe3c4','RĀMĀYAṆA'),('#e7f4ea','AṆṆAN, c. 1430'),('#dfe9f6','TIRUMALA TODAY')]))
 +'<circle cx="120" cy="40" r="14" fill="#ffd60a"/>'+person(50,150,'#ff8c1a')+person(100,160,'#4a7fd0','#4a7fd0',.8)
 +person(230,150,'#fff')+'<rect x="246" y="140" width="40" height="26" fill="#fff3b0" stroke="#111" stroke-width="2"/>'
 +'<rect x="370" y="40" width="70" height="120" fill="#ffd60a" stroke="#111" stroke-width="3"/><path d="M405 40 v120" stroke="#111"/>'+person(340,160,'#fff','#f2c79b',.8)+'</svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">8 VERSES</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,80px)">MADHURĀṢṬAKAM</h1>
  <div class="series">ŚRĪ VALLABHĀCĀRYA · THE SWEETNESS OF KṚṢṆA</div>
  <div class="tag">“Adharaṃ madhuram” · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First the whole hymn for chanting in one go. Then the story of how the hymn came to be and its background, and <b>two pages for each verse</b>: the chant, a picture, what it says and the key words; then a deeper look, background facts, the inner teaching and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>"Adharaṃ madhuraṃ, vadanaṃ madhuraṃ…" Few Sanskrit hymns are as easy to love. Even a child can sing it, and many do: one word, <i>madhuram</i>, "sweet", sung again and again.</p>
    <p>The Madhurāṣṭakam was composed by <b>Śrī Vallabhācārya</b>, founder of the Puṣṭimārga, the "Path of Grace". In eight short verses, he looks at Kṛṣṇa from head to foot, from His smile to His flute, His river, His cows and the whole creation, and finds only one word for all of it.</p>
    <p>This is not a hymn that argues or asks. It simply gazes, and is overwhelmed.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Jai Śrī Kṛṣṇa,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is it really just one word?","Almost! Six sweet things in each verse, and every verse ends: 'everything about the Lord of Sweetness is sweet'.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">THE MADHURĀṢṬAKAM IN ONE GO</h2>
  <div class="sub">All 8 verses, for chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Each line is split at its natural pause. Text checked against shlokam.org and Wikipedia; variant readings are noted on the verse pages.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · A MIDNIGHT VISION</h2>
  <div class="sub">Vallabhācārya and the Path of Grace</div>
  <div class="panel" style="margin-top:6px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>A Telugu boy.</b> Vallabhācārya (1479–1531, by most accounts) was born into a Telugu brāhmaṇa family and became a great scholar of the Vedānta and the Bhāgavatam.</div>
      <div><b>A teacher who walked.</b> He travelled across India on foot, debating and teaching, and visited Vraja, Kṛṣṇa's land, many times.</div>
      <div><b>A vision at midnight.</b> According to tradition, Kṛṣṇa appeared to him at midnight on the eleventh day of the bright half of Śrāvaṇa, and Vallabha composed the Madhurāṣṭakam in His praise.</div>
      <div><b>The Path of Grace.</b> He founded the <b>Puṣṭimārga</b>, where the Lord is loved and served (<i>sevā</i>) as a beloved child, by singing, remembering, seeing and serving Him.</div>
      <div><b>Every Janmāṣṭamī.</b> The hymn is sung wherever Kṛṣṇa is loved, especially on His birthday; M. S. Subbulakshmi's rendition is widely loved.</div>
    </div>
  </div>
  {talk("Why 'Path of Grace'?","Puṣṭi means nourishment, grace. Vallabha taught that we are held by the Lord's grace, not by our own efforts. And grace tastes sweet!")}
</section>

<section class="page" id="about">
  <h2 class="page-title">ABOUT THE MADHURĀṢṬAKAM</h2>
  <div class="sub">Eight verses, forty-eight sweet things</div>
  <div class="g2">
    <div class="card bg-blue"><h4>✍️ The author</h4><p><b>Śrī Vallabhācārya</b>, founder of the Puṣṭimārga and the philosophy of Śuddhādvaita, "pure non-dualism".</p></div>
    <div class="card bg-yellow"><h4>🍯 The word</h4><p><b>Madhura</b> means sweet, lovely, charming. <b>Mādhurya</b>, the Lord's sweetness, is set against His <b>aiśvarya</b>, majesty.</p></div>
  </div>
  <table class="ct">
    <tr><th>Verse</th><th>What is sweet</th></tr>
    <tr><td><b>1</b></td><td>Lips, face, eyes, smile, heart, walk</td></tr>
    <tr><td><b>2</b></td><td>Words, deeds, clothes, posture, movement, wandering</td></tr>
    <tr><td><b>3</b></td><td>Flute, dust of His feet, hands, feet, dance, friendship</td></tr>
    <tr><td><b>4</b></td><td>Singing, drinking, eating, sleeping, form, tilaka</td></tr>
    <tr><td><b>5</b></td><td>Deeds, saving, stealing, play, giving, calm</td></tr>
    <tr><td><b>6</b></td><td>Berry necklace, garland, Yamunā, waves, water, lotuses</td></tr>
    <tr><td><b>7</b></td><td>Gopīs, play, union, parting, glance, courtesy</td></tr>
    <tr><td><b>8</b></td><td>Cowherds, cows, staff, creation, crushing evil, fruit</td></tr>
  </table>
  <div class="panel reading"><p><b>The movement.</b> From His face (1) to His life (2–5), to what is near Him (6–7), to the whole creation (8): sweetness spreading outward like ripples.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">The Madhurāṣṭakam in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story: A Midnight Vision</a></li>
    <li><span class="num">ℹ</span><a href="#about">About the Madhurāṣṭakam</a></li>
    <li><span class="num">∑</span><a href="#end">The Madhurāṣṭakam on One Page</a></li>
    <li class="part">THE 8 VERSES</li>
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
  <h2 class="page-title">THE MADHURĀṢṬAKAM ON ONE PAGE</h2>
  <div class="sub">Eight verses in four lines</div>
  <div class="steps">
    <div><b>Verses 1–2.</b> His face, smile, heart, words, deeds, clothes and wanderings: all sweet.</div>
    <div><b>Verses 3–5.</b> His flute, dance, friendship, eating, sleeping, stealing and saving: all sweet.</div>
    <div><b>Verses 6–7.</b> His garland, the Yamunā, the gopīs, His play, union and parting: all sweet.</div>
    <div><b>Verse 8.</b> His cows, His staff, His whole creation: <i>akhilaṃ madhuram</i>, everything is sweet.</div>
  </div>
  {talk("What's the one thing to remember?","When you love the Lord, everything about Him, and everything He touches, becomes sweet. Madhuram!")}
  <div class="key">"Madhurādhipater akhilaṃ madhuram": <b>everything about Him is sweet</b>. 🙏</div>
  
<div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Madhurāṣṭakam of Śrī Vallabhācārya. Text checked word by word against shlokam.org and the Wikipedia article “Madhurāṣṭakam”; variant readings (smaraṇam, bhuktam) are noted. Background: Wikipedia (author, legend of composition, Puṣṭimārga); shlokam.org. Vallabha’s dates differ slightly between sources (1478 or 1479–1531). Meanings of vamitam and śamitam vary between commentators. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Madhurashtakam.html','w').write(head+''.join(b)+tail)
