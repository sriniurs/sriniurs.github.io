import re,sys
sys.path.insert(0,'.'); sys.path.insert(0,'/home/claude/work/suprabhatam')
from sdata1 import talk,person,F,SUN,HILL,TEMPLE
from adata import V
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Acyutāṣṭakam · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Acyutaṃ keśavaṃ: the Acyutāṣṭakam attributed to Ādi Śaṅkarācārya, a garland of the names of Viṣṇu, Rāma and Kṛṣṇa, explained verse by verse in plain English with illustrations.">',head)
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
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Rama with his bow and Krishna with his flute standing side by side, framed by a garland of flowers">'
 '<circle cx="190" cy="130" r="110" fill="none" stroke="#f08aa6" stroke-width="10" stroke-dasharray="2 14" stroke-linecap="round"/>'
 '<g transform="translate(130 40) scale(1.1)" stroke="#111" stroke-width="2.5"><circle cy="50" r="13" fill="#2a9d6f"/><path d="M-12 36 h24 v-12 h-24z" fill="#ffd60a"/><path d="M-20 140 q-4 -60 20 -76 q24 16 20 76z" fill="#ffd60a"/><path d="M-34 40 q-24 44 0 90" fill="none" stroke="#7a5a3a" stroke-width="5"/></g>'
 '<g transform="translate(250 40) scale(1.1)" stroke="#111" stroke-width="2.5"><circle cy="56" r="15" fill="#3b6fd0"/><path d="M-10 40 q10 -14 20 0" fill="#111"/><path d="M4 36 q10 -20 6 -30" stroke="#2a9d6f" stroke-width="3" fill="none"/><circle cx="10" cy="8" r="4" fill="#1d6fb8" stroke="#2a9d6f"/><path d="M-22 150 q-4 -66 22 -78 q26 12 22 78z" fill="#ffd60a"/><path d="M-14 82 q14 30 28 0" fill="none" stroke="#e05a8a" stroke-width="4"/></g>'
 '<path d="M260 106 l50 -14" stroke="#7a5a3a" stroke-width="6" stroke-linecap="round"/>'
 '<text x="190" y="258" text-anchor="middle" font-family="Bangers" font-size="22" fill="#fff" stroke="#111" stroke-width="1">RĀMA · KṚṢṆA</text></svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: Vishvamitra waking young Rama at dawn; the poet Annan composing at Kanchipuram; priests singing before the golden door at Tirumala">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#ffe3c4','RĀMĀYAṆA'),('#e7f4ea','AṆṆAN, c. 1430'),('#dfe9f6','TIRUMALA TODAY')]))
 +'<circle cx="120" cy="40" r="14" fill="#ffd60a"/>'+person(50,150,'#ff8c1a')+person(100,160,'#4a7fd0','#4a7fd0',.8)
 +person(230,150,'#fff')+'<rect x="246" y="140" width="40" height="26" fill="#fff3b0" stroke="#111" stroke-width="2"/>'
 +'<rect x="370" y="40" width="70" height="120" fill="#ffd60a" stroke="#111" stroke-width="3"/><path d="M405 40 v120" stroke="#111"/>'+person(340,160,'#fff','#f2c79b',.8)+'</svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">8 + 1 VERSES</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7.4vw,80px)">ACYUTĀṢṬAKAM</h1>
  <div class="series">ĀDI ŚAṄKARĀCĀRYA · A GARLAND OF THE LORD’S NAMES</div>
  <div class="tag">“Acyutaṃ keśavaṃ” · explained and illustrated</div>
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
    <p>"Acyutaṃ keśavaṃ rāma-nārāyaṇaṃ…" It opens like a bell ringing: name after name of the Lord, in a lilting, swinging rhythm that children learn before they know what it means.</p>
    <p>The Acyutāṣṭakam is traditionally attributed to <b>Ādi Śaṅkarācārya</b>. In eight verses it worships the Lord by His names, then turns to Rāma in the forest and to little Kṛṣṇa among the cows, and ends with a meditation on His form, from rain-cloud body to jingling waist-bells.</p>
    <p>It is a hymn for singing aloud: <i>nāma-saṅkīrtana</i>, the joy of the holy names.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is this the bhajan 'Acyutam Keśavam Kṛṣṇa Dāmodaram'?","That popular Hindi bhajan borrows this hymn's opening, then goes its own way. This is the original Sanskrit hymn.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">THE ACYUTĀṢṬAKAM IN ONE GO</h2>
  <div class="sub">All 9 verses, for chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Each line is split at its natural pause. Text checked against shlokam.org; variant readings are noted on the verse pages.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · A TEACHER WHO SANG</h2>
  <div class="sub">Śaṅkara, the philosopher of oneness, singing the names</div>
  <div class="panel" style="margin-top:6px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>The philosopher.</b> Ādi Śaṅkarācārya, from Kālaḍi in Kerala, taught Advaita Vedānta: the Self and Brahman are one.</div>
      <div><b>The poet.</b> Tradition credits him with many devotional hymns too: Bhaja Govindam, Śiva Pañcākṣara, Kanakadhārā and others.</div>
      <div><b>Knowledge and love.</b> For Śaṅkara, devotion purifies the mind and prepares it for knowledge; singing the names is open to everyone.</div>
      <div><b>A garland of names.</b> The Acyutāṣṭakam is pure <i>nāma-saṅkīrtana</i>: the Lord's names, strung together in a singing metre.</div>
      <div><b>A note on authorship.</b> Scholars debate which hymns Śaṅkara himself wrote; this one is traditionally attributed to him.</div>
    </div>
  </div>
  {talk("A philosopher of oneness singing to Kṛṣṇa?","Why not? The Lord we sing to is our own deepest Self, says verse 3. Love and knowledge meet.")}
</section>

<section class="page" id="about">
  <h2 class="page-title">ABOUT THE ACYUTĀṢṬAKAM</h2>
  <div class="sub">Eight verses and a blessing</div>
  <div class="g2">
    <div class="card bg-blue"><h4>🔔 The rhythm</h4><p><b>Sragviṇī</b>, "garland-wearer": four DUM-da-DUM beats a line. ACyu-TAM KEśa-VAM.</p></div>
    <div class="card bg-yellow"><h4>📛 The name</h4><p>"Acyuta" means unfailing: the One who never falls, and never lets His devotee fall.</p></div>
  </div>
  <table class="ct">
    <tr><th>Verse</th><th>What it does</th></tr>
    <tr><td><b>1</b></td><td>I worship: a garland of His names</td></tr>
    <tr><td><b>2</b></td><td>I hold in mind: Devakī's joy, Nanda's son</td></tr>
    <tr><td><b>3</b></td><td>Salutations to You: conch, discus, flute</td></tr>
    <tr><td><b>4</b></td><td>Calling out: "O Kṛṣṇa! O Govinda!"</td></tr>
    <tr><td><b>5</b></td><td>May Rāma of the forest protect me</td></tr>
    <tr><td><b>6</b></td><td>May little Gopāla always protect me</td></tr>
    <tr><td><b>7–8</b></td><td>Meditation on His form, head to foot</td></tr>
    <tr><td><b>9</b></td><td>The fruit: Hari is won by love</td></tr>
  </table>
  <div class="panel reading"><p><b>Not to be confused</b> with another hymn of the same name, "acyutācyuta hare paramātman…", also attributed to Śaṅkara.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">The Acyutāṣṭakam in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story: A Teacher Who Sang</a></li>
    <li><span class="num">ℹ</span><a href="#about">About the Acyutāṣṭakam</a></li>
    <li><span class="num">∑</span><a href="#end">The Acyutāṣṭakam on One Page</a></li>
    <li class="part">THE 9 VERSES</li>
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
  <h2 class="page-title">THE ACYUTĀṢṬAKAM ON ONE PAGE</h2>
  <div class="sub">Nine verses in five lines</div>
  <div class="steps">
    <div><b>Verses 1–3.</b> I worship, I hold in mind, I bow: Acyuta, Keśava, Rāma, Nārāyaṇa, Kṛṣṇa, the Self of all.</div>
    <div><b>Verse 4.</b> Pure calling: "Kṛṣṇa! Govinda! Protector of Draupadī!"</div>
    <div><b>Verses 5–6.</b> Rāma of the forest and little Gopāla among the cows: may they protect me.</div>
    <div><b>Verses 7–8.</b> Meditation: rain-cloud body, lightning silk, curls, crown and tinkling bells.</div>
    <div><b>Verse 9.</b> Sung with love each day, the hymn wins Hari's heart.</div>
  </div>
  {talk("What's the one thing to remember?","The names of God are enough. Sing them with love, and the Unfailing One comes close.")}
  <div class="key">"Acyutaṃ keśavaṃ": <b>sing the names, and He comes</b>. 🙏</div>
  
<div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Acyutāṣṭakam (acyutaṃ keśavaṃ), traditionally attributed to Ādi Śaṅkarācārya. Text checked word by word against shlokam.org; variant readings (nandanaṃ, rukmiṇi-, dhenukāriṣṭako’niṣṭakṛd dveṣiṇāṃ) are noted. Authorship of many hymns attributed to Śaṅkara is debated by scholars. The metre (sragviṇī) is from standard prosody. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Acyutashtakam.html','w').write(head+''.join(b)+tail)
