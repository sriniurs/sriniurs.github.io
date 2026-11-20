import re,sys
sys.path.insert(0,'.')
from d1 import V,talk,person,F,BHISMA,VIS,K
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śrī Viṣṇu Sahasranāma · Part 1 · The Opening · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 1: the opening prayers, Bhīṣma\'s teaching to Yudhiṣṭhira (pūrvabhāga) and the dhyāna verses, explained verse by verse in plain English with illustrations.">',head)
head=head.replace('</style>','  .iast .cl2{padding-left:2.2em}\n  .full .ln2{padding-left:2.2em}\n  .pt{font-size:14.5px;line-height:1.45;margin:8px 0}\n  .toc.tight{gap:5px;grid-template-columns:repeat(3,1fr)}.toc.tight li{padding:3px 8px;font-size:13px}.toc.tight .part{font-size:16px}\n  .long .vfig svg{max-height:150px;width:auto}\n  .long .ct td{padding-top:2px;padding-bottom:2px}\n  @media(max-width:720px){.iast .cl2{padding-left:1.4em}.full .ln2{padding-left:1.4em}}\n</style>',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
def iast(v): return '<div class="iast">'+''.join(f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>' for a,b in v['lines'])+'</div>'
def full(v):
    o=f'<p><span class="vn">{v["lab"]}</span>'
    for a,b in v['lines']:
        b=re.sub(r'\s*‖(\d+)‖$',r'<span class="end">‖ \1 ‖</span>',b)
        o+=f'<span class="ln">{a}</span><span class="ln ln2">{b}</span>'
    return o+'</p>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Bhishma lying on a bed of arrows at Kurukshetra at sunset, with Yudhishthira kneeling and Krishna standing, and the four-armed Vishnu shining in the sky">'
 '<circle cx="190" cy="80" r="70" fill="#ffd60a" opacity=".5"/>'+VIS(190,-6,.75)+
 '<path d="M0 230 H380 V268 H0Z" fill="#c9a26b"/>'+BHISMA(190,232,1.4)+person(70,250,'#e63946','#f2c79b',.7)+K(320,120,.6)+'</svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: the war ends at Kurukshetra; Bhishma teaches Yudhishthira from the bed of arrows while Krishna listens; the thousand names are recited">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#ffe3c4','THE WAR ENDS'),('#e7f4ea','BHĪṢMA TEACHES'),('#dfe9f6','1000 NAMES')]))
 +''.join(f'<path d="M{20+16*k} 160 l10 -60" stroke="#7a5a3a" stroke-width="3"/>' for k in range(7))
 +'<g transform="translate(78 0)">'+'</g>'+BHISMA(230,150,.9)+person(186,170,'#e63946','#f2c79b',.45)+K(270,60,.35)
 +''.join(f'<text x="{330+22*(k%5)}" y="{50+24*(k//5)}" font-family="Bangers" font-size="11" fill="#1d6fb8">✿</text>' for k in range(25))+'</svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 1 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 1 · THE OPENING · BHĪṢMA'S ANSWER</div>
  <div class="tag">The thousand names of Viṣṇu · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First all of Part 1 for chanting in one go. Then the story and background, and <b>one page for each verse</b>: the chant, a picture, what it says, the key words, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>"Viśvaṃ viṣṇur vaṣaṭkāraḥ…" In millions of homes and temples, the Viṣṇu Sahasranāma, the "thousand names of Viṣṇu", is chanted every day. Many know it by heart; many more hear it every morning without knowing what the names mean.</p>
    <p>It comes from the Mahābhārata. At the end of the great war, the dying Bhīṣma answers Yudhiṣṭhira's question, "What should one chant to be free?", with a thousand names of the Lord, while Kṛṣṇa Himself stands listening.</p>
    <p>This series takes it one verse at a time, in ten parts. <b>Part 1</b> covers everything before the names: the opening prayers, Bhīṣma's teaching (the <i>pūrvabhāga</i>) and the meditation verses (<i>dhyāna</i>).</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A thousand names! Where do we even start?","With the story: why Bhīṣma gave them. Once you know the question, every name becomes part of the answer.")}
</section>
''']
def fullpage(id_,title,sub,vs,note=''):
    return f'''<section class="page" id="{id_}">
  <h2 class="page-title">{title}</h2>
  <div class="sub">{sub}</div>
  <div class="full">{''.join(full(v) for v in vs)}</div>{note}
</section>
'''
op=[v for v in V if v['sec']=='OPENING']; pu=[v for v in V if v['sec']=='PŪRVA']; ny=[v for v in V if v['sec']=='NYĀSA']; dh=[v for v in V if v['sec']=='DHYĀNA']
b.append(fullpage('full','PART 1 IN ONE GO','Opening prayers and pūrvabhāga 1–9',op+pu[:8]))
b.append(fullpage('full2','PART 1 IN ONE GO · CONTINUED','Pūrvabhāga 10–16',pu[8:]))
b.append(fullpage('full3','PART 1 IN ONE GO · DHYĀNA','The meditation verses',dh,'\n  <div class="note">Lines are split at natural pauses. Text checked word by word against shlokam.org. The prose nyāsa, recited between the pūrvabhāga and the dhyāna, is summarised on its own page.</div>'))
b.append(f'''<section class="page" id="story">
  <h2 class="page-title">THE STORY · ON A BED OF ARROWS</h2>
  <div class="sub">How the thousand names were given</div>
  {story_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>The war is over.</b> The Pāṇḍavas have won at Kurukṣetra, but Yudhiṣṭhira, the new king, is crushed by grief at the cost.</div>
      <div><b>A dying teacher.</b> Bhīṣma, the great-uncle of both sides, lies on a bed of arrows, waiting for the sun to turn north before he dies.</div>
      <div><b>Kṛṣṇa's advice.</b> Kṛṣṇa takes Yudhiṣṭhira to Bhīṣma to learn: kingship, dharma, how to live and how to let go.</div>
      <div><b>The last question.</b> After many days of teaching, Yudhiṣṭhira asks: who is the one God, and what should one chant to be free?</div>
      <div><b>The answer.</b> Bhīṣma recites the thousand names of Viṣṇu, while Kṛṣṇa stands before him. The Mahābhārata places this in the Anuśāsana Parva.</div>
    </div>
  </div>
  {talk("Kṛṣṇa was right there while Bhīṣma praised Him?","Yes! Bhīṣma was praising the very Lord standing in front of him. That's why the hymn names 'Devakī's son' as its deity.")}
</section>

<section class="page" id="about">
  <h2 class="page-title">ABOUT THE SAHASRANĀMA</h2>
  <div class="sub">A thousand names in four sections</div>
  <div class="g2">
    <div class="card bg-blue"><h4>📜 Where it comes from</h4><p>The Mahābhārata, Anuśāsana Parva (chapter 149 in the popular edition; numbered differently in the Critical Edition). Seer: <b>Vyāsa</b>.</p></div>
    <div class="card bg-yellow"><h4>🎵 The sound</h4><p>The names are in <b>anuṣṭubh</b>: four lines of eight syllables. Some dhyāna verses use longer metres.</p></div>
  </div>
  <table class="ct">
    <tr><th>Section</th><th>What it contains</th><th>In this series</th></tr>
    <tr><td><b>Opening prayers</b></td><td>To Viṣvaksena, Vyāsa and Viṣṇu</td><td>Part 1</td></tr>
    <tr><td><b>Pūrvabhāga</b></td><td>Yudhiṣṭhira's questions, Bhīṣma's answer</td><td>Part 1</td></tr>
    <tr><td><b>Nyāsa · Dhyāna</b></td><td>Preparation and meditation verses</td><td>Part 1</td></tr>
    <tr><td><b>The names</b></td><td>1,000 names in about 108 verses</td><td>Parts 2–9</td></tr>
    <tr><td><b>Uttarabhāga</b></td><td>The fruits of chanting; closing verses</td><td>Part 10</td></tr>
  </table>
  <div class="panel reading"><p><b>Two great commentaries.</b> Ādi Śaṅkara wrote a famous commentary on the names from the Advaita view; Parāśara Bhaṭṭar wrote one from the Śrīvaiṣṇava view. They sometimes read the same name differently; where they do, this series will say so.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">Part 1 in One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story: On a Bed of Arrows</a></li>
    <li><span class="num">ℹ</span><a href="#about">About the Sahasranāma</a></li>
    <li><span class="num">∑</span><a href="#end">Part 1 on One Page</a></li>
    <li class="part">OPENING PRAYERS</li>
    {''.join(f'<li><span class="num">{v["n"][1:]}</span><a href="#v{v["n"]}">{v["theme"].title()}</a></li>' for v in op)}
    <li class="part">PŪRVABHĀGA · BHĪṢMA'S TEACHING</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title()}</a></li>' for v in pu)}
    <li class="part">NYĀSA · DHYĀNA</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title()}</a></li>' for v in ny+dh)}
  </ul>
</section>
''')
for v in V:
    lg=len(v['lines'])>=3
    ws=v['words'][:4] if lg else v['words']
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in ws)
    plain='' if lg else f'<div class="plain">{v["plain"]}</div>'
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    b.append(f'''<section class="page{' long' if lg else ''}" id="v{v['n']}">
  <h2 class="page-title">{v['lab']}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(v)}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>
    {plain}
    <table class="ct"><tr><th>Word</th><th>Means</th></tr>{words}</table>
  </div>
  <div class="panel reading pt">{v['point']}</div>
  <div class="key">{v['key']}</div>{note}
</section>
''')
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 1 ON ONE PAGE</h2>
  <div class="sub">The opening in five lines</div>
  <div class="steps">
    <div><b>Opening prayers.</b> To the obstacle-remover, to Viṣvaksena, to Vyāsa who is Viṣṇu, to the changeless Lord whose remembrance frees us.</div>
    <div><b>The questions.</b> After the war, Yudhiṣṭhira asks Bhīṣma six questions: who is God, what is the goal, whom to praise and worship, what is the highest dharma, what frees us?</div>
    <div><b>The answer.</b> Praise the endless Lord, source and end of all beings, with love, through His thousand names: that is the highest dharma.</div>
    <div><b>The mantra.</b> Seer Vyāsa, metre anuṣṭubh, deity Kṛṣṇa; chanted for peace.</div>
    <div><b>The meditation.</b> The Lord by the milk ocean, as the universe, resting on the serpent, rain-cloud dark, under the wish-tree.</div>
  </div>
  {talk("When do the names start?","Part 2! 'Viśvaṃ viṣṇur vaṣaṭkāraḥ…': the first name is Viśvam, 'the universe'.")}
  <div class="key">Part 1: <b>Bhīṣma's answer is a thousand names</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, Part 1: opening prayers, pūrvabhāga and dhyāna. Text checked word by word against shlokam.org. Source: Mahābhārata, Anuśāsana Parva (ch. 149 in the vulgate). Opening prayers vary between traditions; the full prose nyāsa is summarised, not reproduced. Metre names are from standard prosody. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part1.html','w').write(head+''.join(b)+tail)
