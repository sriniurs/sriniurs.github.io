import re,sys
sys.path.insert(0,'.')
from sdata1 import talk,person,F,SUN,HILL,TEMPLE
from sdata4 import V
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śrī Veṅkaṭeśa Suprabhātam · Part 4 · Prapatti · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="The Śrī Veṅkaṭeśa Suprabhātam, Part 4, the Śrī Veṅkaṭeśa Prapatti (16 verses of surrender), explained verse by verse in plain English with illustrations: the dawn hymn of Tirumala.">',head)
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
  <div class="burst yel">PART 4 OF 5</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.6vw,72px)">ŚRĪ VEṄKAṬEŚA<br>SUPRABHĀTAM</h1>
  <div class="series">PART 4 · THE PRAPATTI · 16 VERSES OF SURRENDER</div>
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
  <h2 class="page-title">FROM PRAISE TO SURRENDER</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>So far</b>, the Suprabhātam woke the Lord and the Stotram praised Him and pleaded with Him.</p>
    <p><b>Part 4</b> is the third section, the <b>Prapatti</b>: sixteen verses of surrender. It begins with Lakṣmī, the Mother who brings us to Him; then twelve verses gaze only at His feet: their fragrance, colour, marks, softness, their place in the Veda and the Gītā. It ends with the poet's own teacher, and a prayer to serve the Lord forever, never for oneself.</p>
    <p>Every verse from 2 to 15 ends with the same words: <b>"śrī-veṅkaṭeśa-caraṇau śaraṇaṃ prapadye"</b>, "I take the feet of Śrī Veṅkaṭeśa as my refuge."</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Govindā Govindā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Twelve verses just about His feet?","When you bow, the feet are what you see! The poet looks at them from every side, and each verse ends with the same surrender.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">THE PRAPATTI IN ONE GO</h2>
  <div class="sub">Verses 1–8, for chanting</div>
  <div class="full">{''.join(full(v) for v in V[:8])}</div>
</section>
<section class="page" id="full2">
  <h2 class="page-title">THE PRAPATTI IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 9–16</div>
  <div class="full">{''.join(full(v) for v in V[8:])}</div>
  <div class="note">Each line is split at its natural pause. Text checked against shlokam.org; variant readings are noted on the verse pages.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE SHAPE OF THE PRAPATTI</h2>
  <div class="sub">Surrender in four steps</div>
  <div class="steps">
    <div><b>Verse 1: to the Mother.</b> Surrender begins with Śrī, who lives on His chest and makes Him forgiving.</div>
    <div><b>Verse 2: His qualities.</b> All-knowing, all-powerful, loving, master, gracious, easy to reach: every doubt answered.</div>
    <div><b>Verses 3–14: His feet.</b> Fragrance (3), beyond lotuses (4), holy marks (5), colour (6), tenderness (7–8), the gods' crowns (9), the Veda (10), the Gītā (11), where they have stood (12), the hill's jewel (13), a mother's nectar (14).</div>
    <div><b>Verses 15–16: teacher and service.</b> My ācārya showed me these feet; may I serve You with Śrī, never for myself.</div>
  </div>
  <div class="g2" style="margin-top:10px">
    <div class="card bg-yellow"><h4>🔑 The Dvaya mantra</h4><p>The refrain echoes the Śrīvaiṣṇava mantra of surrender: "śrīman nārāyaṇa caraṇau śaraṇaṃ prapadye · śrīmate nārāyaṇāya namaḥ".</p></div>
    <div class="card bg-blue"><h4>🎵 The sound</h4><p>Verse 1 in stately <b>śārdūla-vikrīḍita</b>; verses 2–16 in flowing <b>vasantatilakā</b>, like the Suprabhātam.</p></div>
  </div>
  {talk("What does prapatti actually mean?","Falling at His feet: giving up the idea that we save ourselves, and taking the Lord alone as our way. The Śrīvaiṣṇava tradition calls it surrender.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">From Praise to Surrender</a></li>
    <li><span class="num">🔤</span><a href="#full">The Prapatti in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Shape of the Prapatti</a></li>
        <li><span class="num">∑</span><a href="#end">Part 4 on One Page</a></li>
    <li class="part">THE 16 VERSES</li>
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
  <h2 class="page-title">PART 4 ON ONE PAGE</h2>
  <div class="sub">The Prapatti in five lines</div>
  <div class="steps">
    <div><b>Verse 1.</b> To Śrī, Mother of the world, who makes the Lord forgiving.</div>
    <div><b>Verse 2.</b> To the Lord of every good quality: "I take His feet as my refuge."</div>
    <div><b>Verses 3–9.</b> His feet: sweeter than flowers, beyond lotuses, marked with holy signs, brighter than jewels, tender, honoured by the gods.</div>
    <div><b>Verses 10–14.</b> Praised in the Veda, shown to Arjuna, resting everywhere, the hill's jewel, nectar to the surrendered.</div>
    <div><b>Verses 15–16.</b> My teacher showed me these feet; let me serve You, never for myself.</div>
  </div>
  {talk("What's left after surrender?","Part 5: the Maṅgalāśāsanam. Having surrendered, the devotee now blesses the Lord: maṅgalam, may all be well with You!")}
  <div class="key">The Prapatti: <b>"I take His feet as my refuge"</b>. 🙏</div>
  
<div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Veṅkaṭeśa Prapatti (section 3 of the Suprabhātam). Key words checked against shlokam.org; Vedic and Gītā references: Ṛg Veda 1.154.5, Bhagavad Gītā 18.66; variant spellings are noted. Background: Tirumala Tirupati Devasthanams (four sections of 29, 11, 16 and 14 verses by Prativādi Bhayaṅkara Aṇṇan, disciple of Maṇavāḷa Māmuni); Wikipedia (composed c. 1420–1432; the Rāmāyaṇa opening verse; vasantatilakā metre; M. S. Subbulakshmi). Meanings are our own plain-English renderings. Metre names are from standard prosody; readings of the Lord’s hand gestures are traditional interpretations. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Venkatesa_Suprabhatam_Part4.html','w').write(head+''.join(b)+tail)
