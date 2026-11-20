import re,sys
sys.path.insert(0,'/home/claude/work/purusha')
from pdata import talk,svg,person,F,SUN,B,lab,crowd,K,MOON,STARS,NIGHT
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Tiruppāvai · Day 1 · Mārgaḻit Tiṅgaḷ · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Tiruppāvai Day 1, Mārgaḻit tiṅgaḷ: the first of Āṇḍāḷ’s 30 Dhanurmāsa songs, explained in plain English with illustrations: the full-moon morning, the girls of Āyppāḍi, and “Nārāyaṇa alone will give us the drum”.">',head)
head=head.replace('</style>','  .iast .cl2{padding-left:2.2em}\n  .pt{font-size:14.5px;line-height:1.45;margin:8px 0}\n  .vfig svg{max-height:160px;width:auto}\n  @media(max-width:720px){.iast .cl2{padding-left:1.4em}}\n</style>',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
FOLLOW='<div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>'

LINES=[('mārgaḻit tiṅgaḷ madi niṟainda nannāḷāl','nīrāḍap pōduvīr pōdumiṉō nēriḻaiyīr'),
 ('śīr malgum āyppāḍic celvac ciṟumīrgāḷ','kūrvēl koḍuntoḻilaṉ nandagōpaṉ kumaraṉ'),
 ('ērārnda kaṇṇi yaśōdai iḷañciṅgam','kārmēṉic ceṅgaṇ kadirmadiyam pōl mugattāṉ'),
 ('nārāyaṇaṉē namakkē paṟai taruvāṉ','pārōr pugaḻap paḍindēlōr empāvāy ‖1‖')]
iast='<div class="iast">'+''.join(f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>' for a,b in LINES)+'</div>'

def GIRL(x,y,c,s=1,pot=True):
    p=f'<ellipse cx="14" cy="-22" rx="8" ry="7" fill="#c9a26b" stroke="#111" stroke-width="2"/>' if pot else ''
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2"><circle cy="-30" r="11" fill="#c98b5a"/>'
            f'<path d="M-8 -40 q8 -8 16 0" fill="#111"/><path d="M-16 22 q16 -52 32 0z" fill="{c}"/>{p}</g>')
RIVER='<path d="M0 128 q55 -10 110 0 t110 0 V160 H0z" fill="#4aa3df" stroke="#111" stroke-width="2"/>'
DAWN='<rect width="220" height="160" fill="#2b3a6b"/><rect y="90" width="220" height="70" fill="#f4b183" opacity=".55"/>'

cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Before dawn under a full moon, young girls carrying pots walk to the river, while Krishna’s dark blue face glows in the sky">'
 '<rect width="380" height="268" fill="#1c2a55" rx="8"/><rect y="160" width="380" height="108" fill="#f4b183" opacity=".5"/>'
 +''.join(f'<text x="{(41*k)%370+5}" y="{(37*k+13)%140+12}" font-family="Bangers" font-size="9" fill="#fff">✦</text>' for k in range(22))
 +'<circle cx="300" cy="60" r="34" fill="#fff8c0" stroke="#ffd60a" stroke-width="4"/>'
 +K(150,10,1.0)
 +'<path d="M0 222 q95 -16 190 0 t190 0 V268 H0z" fill="#4aa3df" stroke="#111" stroke-width="2"/>'
 +GIRL(60,214,'#e05a8a',1.2)+GIRL(110,218,'#ffd60a',1.1)+GIRL(250,214,'#2a9d6f',1.2)+GIRL(300,218,'#ff8c1a',1.1)+GIRL(340,214,'#9b5de5',1.0)
 +'</svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: Periyalvar finds a baby girl under a tulasi plant; young Andal wears the Lord’s garland and looks in a mirror; Andal sings with her friends at dawn in Margazhi">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#e7f4ea','FOUND IN THE TULASĪ'),('#fde4ec','THE GARLAND'),('#dfe9f6','THE MĀRGAḺI SONGS')]))
 +'<path d="M50 160 v-40 M50 130 q-14 -10 -20 -24 M50 124 q14 -10 22 -22 M50 140 q-16 -4 -24 -14" stroke="#2a7a4a" stroke-width="4" fill="none"/><ellipse cx="66" cy="158" rx="12" ry="7" fill="#f2c79b" stroke="#111" stroke-width="2"/>'+person(110,160,'#fff','#c98b5a',.9)
 +GIRL(210,160,'#e05a8a',1.1,False)+'<path d="M196 118 q14 18 28 0" fill="none" stroke="#f08aa6" stroke-width="5" stroke-dasharray="3 3"/><rect x="246" y="96" width="26" height="36" rx="12" fill="#bfe0f5" stroke="#111" stroke-width="2"/>'
 +'<circle cx="420" cy="34" r="14" fill="#fff8c0" stroke="#111" stroke-width="2"/>'+GIRL(340,160,'#e05a8a',.9)+GIRL(380,164,'#ffd60a',.8)+GIRL(420,160,'#2a9d6f',.9)+'</svg>')
vsvg=svg('Under a full moon at dawn, girls walk to the river; Nandagopa with his spear stands guard, Yashoda’s lion cub Krishna sits on her lap, and above them shines Narayana',
 DAWN+'<circle cx="190" cy="26" r="14" fill="#fff8c0" stroke="#111" stroke-width="2"/>'+RIVER
 +GIRL(24,128,'#e05a8a',.7)+GIRL(50,130,'#ffd60a',.7)+GIRL(76,128,'#2a9d6f',.7)
 +person(130,124,'#fff','#c98b5a',.8)+'<path d="M144 132 V70" stroke="#7a5a3a" stroke-width="3"/><path d="M140 72 l4 -12 l4 12z" fill="#ccc" stroke="#111"/>'
 +person(178,128,'#ffd60a','#c98b5a',.8)+'<circle cx="168" cy="118" r="7" fill="#3b6fd0" stroke="#111" stroke-width="2"/>'
 +K(98,-6,.42)+lab(30,22,'MĀRGAḺI',10).replace('font-size','fill="#fff" font-size'),B)

WORDS=[('mārgaḻit tiṅgaḷ','<b>the month of Mārgaḻi</b> (Dhanurmāsa, mid-Dec to mid-Jan)'),
 ('madi niṟainda nannāḷ','<b>the good day when the moon is full</b>'),
 ('nīrāḍap pōduvīr pōdumiṉō','<b>you who wish to bathe, come!</b>'),
 ('nēriḻaiyīr','<b>girls in fine jewels</b>'),
 ('śīr malgum āyppāḍi','<b>the prosperous cowherd village</b> (Gokula)'),
 ('kūrvēl koḍuntoḻilaṉ','<b>fierce, with a sharp spear</b>: Nandagopa on guard'),
 ('ērārnda kaṇṇi yaśōdai','<b>Yaśodā of the beautiful eyes</b>'),
 ('iḷañciṅgam','<b>the young lion</b>: little Kṛṣṇa'),
 ('kārmēṉi · ceṅgaṇ','<b>rain-cloud body</b> · <b>lotus-red eyes</b>'),
 ('kadirmadiyam pōl mugattāṉ','<b>a face like the sun and the moon</b>'),
 ('nārāyaṇaṉē … paṟai taruvāṉ','<b>Nārāyaṇa alone will give us the paṟai</b> (the drum)'),
 ('ēlōr empāvāy','<b>the refrain</b>: “come, our pāvai”, closing every song')]
words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in WORDS)

b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">DAY 1 OF 30</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">TIRUPPĀVAI</h1>
  <div class="series">ĀṆḌĀḶ’S SONGS FOR DHANURMĀSA · PĀSURAM 1</div>
  <div class="tag">“Mārgaḻit tiṅgaḷ” · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> One song a day, for the 30 days of Dhanurmāsa. Each day: the pāsuram to sing, a picture, what it says, the key words, and one insight to carry through the day. Day 1 also tells you who Āṇḍāḷ was.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>“Mārgaḻit tiṅgaḷ…” In the cold dark before dawn, through the month of Mārgaḻi, these words ring out from temples and homes across the South. Girls draw kōlams at the door; families wake to a song written more than a thousand years ago by a young woman.</p>
    <p>She is <b>Āṇḍāḷ</b>, the only woman among the twelve Āḻvārs, the poet-saints of Viṣṇu. Her <b>Tiruppāvai</b> is thirty songs, one for each day of the month. In them she becomes a cowherd girl of Kṛṣṇa’s village, waking her friends to bathe in the river and go to Him together.</p>
    <p>This series takes one song a day, from the first day of Dhanurmāsa to Saṅkrānti.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is this in Sanskrit?","No: Tamil! The Tiruppāvai is part of the Nālāyira Divya Prabandham, the 4,000 Tamil verses of the Āḻvārs. Tradition calls it “the seed of all the Vedas”.")}
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · THE GIRL WHO WORE THE GARLAND</h2>
  <div class="sub">Āṇḍāḷ of Śrīvilliputtūr</div>
  {story_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>Found in the garden.</b> Tradition says Periyāḻvār, a temple gardener-saint of Śrīvilliputtūr, found a baby girl under a tulasī plant and named her Kōdai.</div>
      <div><b>The borrowed garland.</b> Each day she secretly wore the garland made for the Lord, to see if she was fit for Him. When her father found out, the Lord said He wanted only the garlands she had worn.</div>
      <div><b>A new name.</b> So she is called <i>śūḍikkoḍutta śuḍarkkoḍi</i>, “the shining creeper who wore it and then gave it”, and Āṇḍāḷ, “she who rules” the Lord’s heart.</div>
      <div><b>The Mārgaḻi vow.</b> She imagined herself a gopī of Kṛṣṇa’s village keeping the girls’ month-long vow, the <i>pāvai nōṉbu</i>, and sang the 30 songs of the Tiruppāvai.</div>
      <div><b>Union.</b> Tradition holds that she was wedded to Raṅganātha at Śrīraṅgam and merged into Him.</div>
    </div>
  </div>
  {talk("She wore God's garland first? Wasn't that wrong?","Her father thought so! But the Lord wanted it that way. Love that holds nothing back was the point.")}
</section>

<section class="page" id="v1">
  <h2 class="page-title">PĀSURAM 1</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">THE FULL-MOON MORNING</span></div>
    {iast}
    <div class="vfig">{vsvg}<div class="mean">It is the month of Mārgaḻi, on the good day of the full moon. Girls in fine jewels, you who wish to bathe, come! Rich young girls of the prosperous cowherd village: Nārāyaṇa, the son of fierce Nandagopa with his sharp spear, the young lion of lovely-eyed Yaśodā, with a body dark as a rain cloud, eyes red as lotus, and a face like the sun and the moon, He alone will give us the drum. Come, let us bathe, so the whole world praises us.</div></div>
    <div class="plain">It’s the full-moon morning of Mārgaḻi. Come, friends, let’s go bathe! Kṛṣṇa, Nanda’s son and Yaśodā’s lion cub, who is Nārāyaṇa Himself, will give us what we ask.</div>
  </div>
  <p class="center" style="margin:0"><a href="#v1b" class="contlink">Continue: the key words ➜</a></p>
</section>

<section class="page" id="v1b">
  <h2 class="page-title">PĀSURAM 1 · THE KEY WORDS</h2>
  <table class="ct"><tr><th>Word</th><th>Means</th></tr>{words}</table>
  <div class="g2">
    <div class="card bg-yellow"><h4>🥁 The paṟai</h4><p>Literally a drum used in the girls’ vow. The teachers read it as the real boon: to be with the Lord and serve Him.</p></div>
    <div class="card bg-blue"><h4>🎵 How it’s sung</h4><p>In <b>rāga Nāṭṭai</b>, <b>Ādi tāḷa</b>. It is verse 474 of the Nālāyira Divya Prabandham.</p></div>
  </div>
</section>

<section class="page" id="end">
  <h2 class="page-title">GOING DEEPER</h2>
  <div class="sub">Why the first song is about Nārāyaṇa</div>
  <div class="panel reading pt">
    <p><b>The best month.</b> Kṛṣṇa says in the Gītā (10.35), “Among months I am Mārgaśīrṣa.” Āṇḍāḷ begins on its full moon: the right time, the right day.</p>
    <p><b>Who gives the drum?</b> The verse builds up a picture of little Kṛṣṇa, Nanda’s boy and Yaśodā’s lion cub, and then turns: <i>nārāyaṇaṉē</i>, “Nārāyaṇa <b>alone</b>”. The cowherd child is the Supreme. Note the double <i>-ē</i>: Nārāyaṇa alone will give, and to <b>us</b> alone. Only He gives; we need only ask Him.</p>
    <p><b>Five forms in five songs.</b> Śrīvaiṣṇava teachers see the first five songs as the Lord’s five forms: here the Supreme (<i>para</i>); then the Lord on the milk ocean, Trivikrama’s strides, the inner Lord as rain, and Kṛṣṇa of Mathurā.</p>
  </div>
  <div class="inner">Morning, bath, friends, the Lord: Āṇḍāḷ turns an ordinary dawn into worship.</div>
  {talk("What's the one thing to remember today?","Don't go alone! Āṇḍāḷ wakes her friends first. The way to Him is together.")}
  <div class="key">“Nārāyaṇaṉē namakkē paṟai taruvāṉ”: <b>He alone gives; just ask Him</b>. 🙏</div>
  <div class="panel"><span class="caption">Tomorrow · Day 2</span><p style="margin:0"><b>“Vaiyattu vāḻvīrgāḷ”</b>: what the girls will do, and what they will give up, during the vow.</p></div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on Tiruppāvai pāsuram 1 (Mārgaḻit tiṅgaḷ) by Āṇḍāḷ. Text checked against divyaprabandham.koyil.org, sadagopan.org and SriPedia; the transliteration follows the common sung form. The traditional readings (paṟai, the five forms) follow Śrīvaiṣṇava commentary. The story of Āṇḍāḷ is as told in tradition. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''']
open('/home/claude/work/tiruppavai/Tiruppavai_Day01.html','w').write(head+''.join(b)+tail)
print('ok')
