import re,sys
sys.path.insert(0,'/home/claude/work/purusha')
from pdata import *
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Puruṣa Sūktam · The Hymn of the Cosmic Person · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Sahasraśīrṣā puruṣaḥ: the Puruṣa Sūktam (Ṛg Veda 10.90), the Vedic hymn of the Cosmic Person, explained verse by verse in plain English with illustrations, with the Taittirīya additions recited in Viṣṇu worship.">',head)
head=head.replace('</style>','  .iast .cl2{padding-left:2.2em}\n  .full .ln2{padding-left:2.2em}\n  .pt{font-size:14.5px;line-height:1.45;margin:8px 0}\n  .toc.tight{gap:5px;grid-template-columns:repeat(3,1fr)}.toc.tight li{padding:3px 8px;font-size:13px}.toc.tight .part{font-size:16px}\n  .vfig svg{max-height:150px;width:auto}\n  @media(max-width:720px){.iast .cl2{padding-left:1.4em}.full .ln2{padding-left:1.4em}}\n</style>',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
def iast(v): return '<div class="iast">'+''.join(f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>' for a,b in v['lines'])+'</div>'
def full(v):
    o=f'<p><span class="vn">{v["lab"]}</span>'
    for a,b in v['lines']:
        b=re.sub(r'\s*‖(\w+)‖$',r'<span class="end">‖ \1 ‖</span>',b)
        o+=f'<span class="ln">{a}</span><span class="ln ln2">{b}</span>'
    return o+'</p>'
def fullpage(id_,title,sub,vs,note=''):
    return f'''<section class="page" id="{id_}">
  <h2 class="page-title">{title}</h2>
  <div class="sub">{sub}</div>
  <div class="full">{''.join(full(v) for v in vs)}</div>{note}
</section>
'''
FOLLOW='<div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A vast star-filled blue Cosmic Person towering over the round earth, with sun and moon at his eyes and a sacred fire at his feet">'
 '<rect width="380" height="268" fill="#0d1b3a" rx="8"/>'+''.join(f'<text x="{(41*k)%370+5}" y="{(67*k+13)%250+12}" font-family="Bangers" font-size="10" fill="#fff">✦</text>' for k in range(30))
 +PU(190,0,1.55)+MOON(150,62,10)+SUN(230,62,10)+'<circle cx="190" cy="262" r="40" fill="#2a9d6f" stroke="#111" stroke-width="3"/>'+FIRE(190,236,.7)+'</svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: the seer Narayana in meditation; the gods performing the first sacrifice with the Cosmic Person; the worlds, sun and moon coming from his body">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#ffe3c4','THE SEER SEES'),('#e7f4ea','THE FIRST SACRIFICE'),('#dfe9f6','THE WORLDS ARE BORN')]))
 +person(78,150,'#ff8c1a','#c98b5a',1.1)+PU(78,10,.35,False)
 +FIRE(230,160,.9)+PU(230,10,.5,False)+person(180,170,'#ffd60a','#f2c79b',.6)+person(280,170,'#fff','#f2c79b',.6)
 +'<rect x="309" y="9" width="139" height="170" fill="#0d1b3a"/>'+PU(380,14,.7)+MOON(345,40,10)+SUN(415,40,10)+'</svg>')
V12=[v for v in V if v['n']=='12'][0]
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ṚG VEDA 10.90</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.6vw,80px)">PURUṢA SŪKTAM</h1>
  <div class="series">THE HYMN OF THE COSMIC PERSON</div>
  <div class="tag">“Sahasraśīrṣā puruṣaḥ” · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First all 16 verses for chanting in one go. Then the story and background, and <b>one page for each verse</b>: the chant, a picture, what it says, the key words, one insight and the one thing to remember. At the end: how verse 12 is read, and the extra verses recited in South Indian worship.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>“Sahasraśīrṣā puruṣaḥ…” If you have stood near a temple during an abhiṣeka, you have heard it: the steady Vedic chant as water, milk and honey pour over the deity.</p>
    <p>The Puruṣa Sūktam is one of the most famous hymns of the Ṛg Veda. In sixteen verses it pictures God as a <b>Cosmic Person</b>, with a thousand heads and a thousand eyes, who is everything that was and will be, and still stands beyond it all. From His sacrifice come the seasons, the creatures, the Vedas, the sun and moon, the sky and the earth.</p>
    <p>For Vaiṣṇavas this Person is Nārāyaṇa, and the hymn is the Vedic foundation of Viṣṇu worship. Its seer is even named Nārāyaṇa.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is it really 3,000 years old?","The Ṛg Veda is usually dated to the second millennium BCE, and scholars place this hymn in its later layer. Either way, it is among the oldest hymns still chanted every day.")}
</section>
''',
fullpage('full','THE PURUṢA SŪKTAM IN ONE GO','Ṛg Veda 10.90 · verses 1–8',V[:8]),
fullpage('full2','IN ONE GO · CONTINUED','Verses 9–16',V[8:],'\n  <div class="note">Lines are split at their natural pause. Text of Ṛg Veda 10.90 checked word by word against wisdomlib.org and greenmesg.org. The Taittirīya recitation differs slightly in order and adds verses: see the page near the end.</div>'),
f'''<section class="page" id="story">
  <h2 class="page-title">THE STORY · THE PERSON WHO BECAME THE WORLD</h2>
  <div class="sub">A seer’s vision of how everything began</div>
  {story_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>The seer.</b> The Ṛg Veda names the seer of this hymn as <b>Nārāyaṇa</b>, and its deity as <b>Puruṣa</b>, the Person.</div>
      <div><b>The vision.</b> He sees one vast Being, with countless heads, eyes and feet, filling the world and rising beyond it.</div>
      <div><b>The sacrifice.</b> The gods perform the first sacrifice, and the offering is the Person Himself. The seasons are its ghee, fuel and oblation.</div>
      <div><b>The world is born.</b> From that offering come animals, the Vedas, society, the moon from His mind, the sun from His eye, sky, air and earth.</div>
      <div><b>The pattern.</b> That first sacrifice becomes the model, the “first dharma”, for all worship after it.</div>
    </div>
  </div>
  {talk("The gods sacrificed God? That sounds strange!","It is a picture, not a crime scene! It means the world exists because the Lord gives Himself. Creation is an act of self-giving.")}
</section>

<section class="page" id="about">
  <h2 class="page-title">ABOUT THE PURUṢA SŪKTAM</h2>
  <div class="sub">One hymn, found in all the Vedas</div>
  <div class="g2">
    <div class="card bg-blue"><h4>📜 Where it comes from</h4><p><b>Ṛg Veda 10.90</b>. Seer: Nārāyaṇa. Deity: Puruṣa. 15 verses in <b>anuṣṭubh</b> (4 × 8 syllables), the last in <b>triṣṭubh</b> (4 × 11).</p></div>
    <div class="card bg-yellow"><h4>🔁 In other Vedas</h4><p>With variations in the Atharva Veda (19.6), the Vājasaneyi Saṃhitā of the Śukla Yajur Veda, and the <b>Taittirīya Āraṇyaka</b> of the Kṛṣṇa Yajur Veda.</p></div>
  </div>
  <table class="ct">
    <tr><th>Link to Viṣṇu</th><th>Where</th></tr>
    <tr><td><b>Seer Nārāyaṇa</b></td><td>The Ṛg Veda names him as the seer; later texts identify the Puruṣa with Nārāyaṇa</td></tr>
    <tr><td><b>Lakṣmī’s Lord</b></td><td>The Taittirīya “uttara” section ends: Hrī and Lakṣmī are Your consorts</td></tr>
    <tr><td><b>Sahasranāma</b></td><td>“sahasramūrdhā viśvātmā sahasrākṣaḥ sahasrapāt” echoes verse 1</td></tr>
    <tr><td><b>Bhagavad Gītā</b></td><td>Kṛṣṇa as Puruṣottama, the Supreme Person (15.18); the universal form (ch. 11)</td></tr>
    <tr><td><b>Worship</b></td><td>Chanted at abhiṣeka; in many traditions the 16 verses go with the 16 offerings (ṣoḍaśopacāra) of pūjā</td></tr>
  </table>
  <div class="panel reading"><p><b>Old and new.</b> Many scholars consider the hymn part of the later layer of the Ṛg Veda, on grounds of its language and ideas. Tradition, for its part, calls it the heart of the Vedas: <i>vedeṣu pauruṣaṃ sūktam</i>, “among Vedic hymns, the Puruṣa Sūktam”.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">In One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story</a></li>
    <li><span class="num">ℹ</span><a href="#about">About the Hymn</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    <li class="part">THE 16 VERSES</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title().replace("’S","’s")}</a></li>' for v in V)}
    <li class="part">MORE</li>
    <li><span class="num">12</span><a href="#v12b">Reading Verse 12</a></li>
    <li><span class="num">TA</span><a href="#taitt">The Taittirīya Verses</a></li>
  </ul>
</section>
''']
for v in V:
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    b.append(f'''<section class="page" id="v{v['n']}">
  <h2 class="page-title">{v['lab']}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(v)}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>
    <div class="plain">{v['plain']}</div>
    <table class="ct"><tr><th>Word</th><th>Means</th></tr>{words}</table>
  </div>
  <div class="panel reading pt">{v['point']}</div>
  <div class="key">{v['key']}</div>{note}
</section>
''')
    if v['n']=='12':
        b.append(f'''<section class="page" id="v12b">
  <h2 class="page-title">READING VERSE 12</h2>
  <div class="sub">The most debated verse in the Vedas: the main views, side by side</div>
  <table class="ct">
    <tr><th>View</th><th>How it reads the verse</th></tr>
    <tr><td><b>The plain sense</b></td><td>Four social orders, pictured as mouth, arms, thighs and feet of one cosmic body. It is the only Ṛg Veda verse that names all four together.</td></tr>
    <tr><td><b>One body</b></td><td>Many traditional readers stress unity: every part belongs to the same Person and the body needs all of them. The same body gives the moon, the sun and the earth (verses 13–14).</td></tr>
    <tr><td><b>Quality and work</b></td><td>The Gītā says the four orders were made “by division of qualities and work” (<i>guṇa-karma-vibhāgaśaḥ</i>, 4.13); many teachers read varṇa as nature and calling rather than birth.</td></tr>
    <tr><td><b>A later addition</b></td><td>Max Müller and many later scholars saw the hymn as late in its language and ideas, and the varṇa verse as inserted later. Some describe it as a “charter myth” for social order.</td></tr>
    <tr><td><b>Original to the hymn</b></td><td>Other scholars hold that the verse belongs to the hymn as composed. The question is still argued.</td></tr>
  </table>
  <div class="panel reading pt"><p><b>What is widely agreed.</b> The later caste system, with fixed birth-groups and rules on marriage and eating together, grew far more elaborate and rigid than anything the Ṛg Veda describes. The Ṛg Veda itself never hints at such rules.</p></div>
  {talk("So which reading is right?","Scholars and teachers still disagree. What everyone can see: the hymn's main message is that all of it, every part, is one Person.")}
  <div class="key">Read in many ways; <b>one body, one Person</b> is the hymn’s own frame.</div>
</section>
''')
b.append(f'''<section class="page" id="taitt">
  <h2 class="page-title">THE TAITTIRĪYA VERSES</h2>
  <div class="sub">The version chanted in South Indian temples and homes</div>
  <p class="pt" style="margin:4px 0">The <b>Taittirīya Āraṇyaka</b> (3.12–13) version changes the order a little (verse 15 follows verse 6) and adds verses. Two of the best-loved come before the final verse:</p>
  <div class="sloka" style="margin-top:4px">
    <div class="iast"><span class="cl">vedāham etaṃ puruṣaṃ mahāntam</span><span class="cl cl2">ādityavarṇaṃ tamasas tu pāre |</span><span class="cl">sarvāṇi rūpāṇi vicitya dhīraḥ</span><span class="cl cl2">nāmāni kṛtvābhivadan yad āste ‖</span></div>
    <div class="mean">I know this great Person, bright as the sun, beyond all darkness: the wise One who shaped every form, gave each its name, and abides, calling them.</div>
    <div class="iast"><span class="cl">dhātā purastād yam udājahāra</span><span class="cl cl2">śakraḥ pravidvān pradiśaś catasraḥ |</span><span class="cl">tam evaṃ vidvān amṛta iha bhavati</span><span class="cl cl2">nānyaḥ panthā ayanāya vidyate ‖</span></div>
    <div class="mean">Him whom the Creator proclaimed of old, and Indra, knowing, in all four directions: whoever knows Him thus becomes immortal here. There is no other path to go.</div>
  </div>
  <table class="ct">
    <tr><th>Also added</th><th>What it says</th></tr>
    <tr><td><b>Uttara-Nārāyaṇa</b></td><td>A second section beginning <i>adbhyaḥ sambhūtaḥ</i>, “born of the waters”, that praises the Person as the sun’s radiance</td></tr>
    <tr><td><b>The closing</b></td><td><i>hrīś ca te lakṣmīś ca patnyau</i>: “Hrī and Lakṣmī are Your consorts; day and night Your two sides”</td></tr>
    <tr><td><b>Śānti · echo</b></td><td>Framed by the peace prayer <i>tac chaṃ yor āvṛṇīmahe</i>; the vedāham verse returns in the Śvetāśvatara Upaniṣad (3.8)</td></tr>
  </table>
</section>

<section class="page" id="end">
  <h2 class="page-title">THE PURUṢA SŪKTAM ON ONE PAGE</h2>
  <div class="sub">Sixteen verses in five lines</div>
  <div class="steps">
    <div><b>Verses 1–5.</b> The Person: countless heads, eyes, feet; all that was and will be; the world only a quarter of Him; from Him Virāj, and He within it.</div>
    <div><b>Verses 6–7.</b> The gods perform the first sacrifice with the Person as offering; the seasons are its ghee, fuel and oblation.</div>
    <div><b>Verses 8–10.</b> From it come the creatures, the Vedas and the animals of the home.</div>
    <div><b>Verses 11–14.</b> His body divided: society, moon and sun, Indra, Agni and wind, sky, air and earth.</div>
    <div><b>Verses 15–16.</b> The cosmos is the altar; the first sacrifice is the first dharma, the pattern of all worship.</div>
  </div>
  {talk("What's the one thing to remember?","Everything you see is one Person, and still He is greater than all of it. Worship is how we join in His self-giving.")}
  <div class="key">“Puruṣa evedaṃ sarvam”: <b>all this is He, and He is more</b>. 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Puruṣa Sūktam, Ṛg Veda 10.90 (seer Nārāyaṇa, deity Puruṣa). Ṛg Veda text checked word by word against wisdomlib.org (with Sāyaṇa’s commentary) and greenmesg.org; Taittirīya additions checked against prapatti.com. Views on verse 12 summarise published scholarship (Max Müller; Jamison and Brereton) and traditional readings; dates of the Ṛg Veda are approximate and debated. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('/home/claude/work/purusha/Purusha_Suktam.html','w').write(head+''.join(b)+tail)
print('ok')
