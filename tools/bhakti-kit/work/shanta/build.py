import re,sys
sys.path.insert(0,'/home/claude/work/vsn')
from d1 import talk,person,F,VIS,K,svg,SUN,lab
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śāntākāraṃ Bhujagaśayanam · The Viṣṇu Dhyāna Ślokam · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śāntākāraṃ bhujagaśayanam: the best-loved meditation verse on Viṣṇu, explained word by word with illustrations, its picture, its rhythm and how to meditate with it.">',head)
head=head.replace('</style>','''  .big{font-size:21px;line-height:1.9;font-style:italic}
  .big .seg{display:inline-block;margin-right:.5em}
  .big .bar{color:#1d6fb8;font-style:normal;font-weight:700;margin-right:.5em}
  .ep{border:3px solid var(--ink);background:#fff;padding:8px 12px;margin:8px 0}
  .ep h4{margin:0 0 4px;font-family:Bangers;letter-spacing:1px;font-size:20px;color:#1d6fb8}
  .ep .w{font-style:italic;font-weight:700}
  .ep p{margin:2px 0;font-size:15px;line-height:1.45}
  .beat{display:flex;gap:3px;flex-wrap:wrap;margin:6px 0}
  .beat span{border:2px solid var(--ink);padding:3px 6px;font-size:14px;background:#fff}
  .beat .G{background:#1d6fb8;color:#fff;font-weight:700}
  .beat .Y{border:none;background:none;font-weight:700;color:#e63946}
  @media(max-width:720px){.big{font-size:17px}}
</style>''',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
L=[['śāntākāraṃ','bhujagaśayanaṃ','padmanābhaṃ sureśaṃ'],['viśvādhāraṃ','gaganasadṛśaṃ','meghavarṇaṃ śubhāṅgam |'],['lakṣmīkāntaṃ','kamalanayanaṃ','yogibhir dhyānagamyaṃ'],['vande viṣṇuṃ','bhavabhayaharaṃ','sarvalokaikanātham ‖']]
def bigverse(): return '<div class="sloka"><div class="sloka-head"><span class="theme" style="font-size:22px">ŚĀNTĀKĀRAM</span></div><div class="iast big">'+''.join('<div>'+'<span class="bar">·</span>'.join(f'<span class="seg">{s}</span>' for s in l)+'</div>' for l in L)+'</div></div>'
def RECLINE(w=460,h=260):
    return (f'<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="{w}" height="{h}" viewBox="0 0 460 260" role="img" aria-label="Vishnu reclining peacefully on the coiled serpent Adishesha on the cosmic ocean, the serpent\'s hoods sheltering his head, a lotus rising from his navel with Brahma seated on it, and Lakshmi seated at his feet">'
     '<rect width="460" height="260" fill="#0b3d6e"/>'+''.join(f'<circle cx="{(k*67)%460}" cy="{(k*29)%110}" r="1.6" fill="#fff"/>' for k in range(30))
     +'<rect x="0" y="200" width="460" height="60" fill="#4aa3df"/>'+''.join(f'<path d="M{40*k} 204 q20 -10 40 0" fill="none" stroke="#9fd3f0" stroke-width="3"/>' for k in range(12))
     +'<g stroke="#111" stroke-width="2.5"><ellipse cx="230" cy="196" rx="170" ry="26" fill="#e0e0e0"/><ellipse cx="230" cy="184" rx="150" ry="18" fill="#d6d6d6"/></g>'
     +''.join(f'<path d="M{360+12*k} 180 q{-6+3*k} -60 {6+6*k} -80" fill="none" stroke="#2a7a4a" stroke-width="10" stroke-linecap="round"/>' for k in range(5))
     +''.join(f'<ellipse cx="{360+12*k+6+6*k-6}" cy="98" rx="10" ry="7" fill="#2a7a4a" stroke="#111"/>' for k in range(5))
     +'<g stroke="#111" stroke-width="2.5"><path d="M110 168 q120 -36 236 -8" fill="none" stroke="#3b6fd0" stroke-width="26" stroke-linecap="round"/><path d="M120 164 q110 -30 200 -10" fill="none" stroke="#ffd60a" stroke-width="12"/></g>'
     +'<g stroke="#111" stroke-width="2.5"><circle cx="352" cy="146" r="18" fill="#3b6fd0"/><path d="M340 128 h24 l-4 -18 h-16z" fill="#ffd60a"/></g><path d="M346 146 q6 4 12 0" fill="none" stroke="#111" stroke-width="2"/>'
     +'<path d="M240 150 q6 -50 0 -90" fill="none" stroke="#2a9d6f" stroke-width="4"/><g transform="translate(240 60)" stroke="#111" stroke-width="2"><path d="M0 0 q-20 -10 -24 -24 q18 0 24 24z" fill="#f08aa6"/><path d="M0 0 q20 -10 24 -24 q-18 0 -24 24z" fill="#f08aa6"/><path d="M0 0 q-8 -20 0 -32 q8 12 0 32z" fill="#f6b8c8"/><circle cy="-40" r="8" fill="#e0a800"/></g>'
     +'<g transform="translate(96 170)" stroke="#111" stroke-width="2"><circle cy="-34" r="10" fill="#f2c79b"/><path d="M-16 0 q16 -44 32 0z" fill="#e05a8a"/></g>'
     +''.join(f'<text x="{x}" y="{y}" font-family="Bangers" font-size="13" fill="#fff">{t}</text>' for x,y,t in [(250,40,"BRAHMĀ"),(214,140,"PADMANĀBHA"),(60,130,"LAKṢMĪ"),(380,80,"ĀDIŚEṢA"),(20,244,"KṢĪRA-SĀGARA · THE COSMIC OCEAN")])+'</svg>')
cover=('<svg width="380" height="268" viewBox="0 0 460 260" role="img" aria-label="Vishnu reclining on the serpent on the cosmic ocean under a starry sky">'+RECLINE()[RECLINE().index('<rect'):])
EP=lambda t,w,m,p: f'<div class="ep"><h4>{t}</h4><p><span class="w">{w}</span>: {m}</p><p>{p}</p></div>'
def linepage(i,title,sub,eps,tk):
    return f'''<section class="page" id="l{i}">
  <h2 class="page-title">LINE {i} · {title}</h2>
  <div class="sub">{sub}</div>
  <div class="panel" style="padding:8px 12px"><div class="iast big" style="margin:0">{'<span class="bar">·</span>'.join(f'<span class="seg">{s}</span>' for s in L[i-1])}</div></div>
  {''.join(EP(*e) for e in eps)}
  <div class="key">{tk}</div>
</section>
'''
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ONE VERSE</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,70px)">ŚĀNTĀKĀRAṂ<br>BHUJAGAŚAYANAM</h1>
  <div class="series">THE VIṢṆU DHYĀNA ŚLOKAM</div>
  <div class="tag">Peace that holds up the universe · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> The verse to chant, the picture it paints, then <b>one page for each line</b> with every word explained. Then the paradox at its heart, its rhythm, and a short meditation to do with it.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>"Śāntākāraṃ bhujagaśayanaṃ…" If there is one Sanskrit verse that almost every Hindu home knows, it may be this one. It is chanted before prayers, before the Viṣṇu Sahasranāma, before a journey, before an exam, and at the end of a long day.</p>
    <p>It is a <b>dhyāna ślokam</b>, a meditation verse: four lines that paint a picture to hold in the mind. Viṣṇu lies at perfect peace on the great serpent, on the cosmic ocean, while holding up the whole universe.</p>
    <p>Sixteen words, one picture, one prayer: take away the fear of life itself.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why is a verse about a sleeping God so popular?","Because He isn't just resting: He's peaceful while carrying everything. That's exactly what all of us want to learn.")}
</section>

<section class="page" id="chant">
  <h2 class="page-title">THE VERSE</h2>
  <div class="sub">To chant slowly, pausing at each dot</div>
  {bigverse()}
  <div class="panel reading" style="margin-top:12px">
    <p><b>In plain words:</b> I bow to Viṣṇu, the peaceful One, who rests on the serpent, from whose navel a lotus rises, Lord of the gods; the support of the universe, vast as the sky, dark as a rain cloud, with beautiful limbs; the beloved of Lakṣmī, lotus-eyed, reached by yogis in meditation; who takes away the fear of worldly existence, the one Lord of all the worlds.</p>
  </div>
  <div class="note">The dots mark the natural pauses of the metre (after the 4th and 10th syllables). Text as given in the dhyāna of the Viṣṇu Sahasranāma, checked against shlokam.org.</div>
</section>

<section class="page" id="picture">
  <h2 class="page-title">THE PICTURE</h2>
  <div class="sub">What the verse asks you to see</div>
  {RECLINE()}
  <div class="steps" style="margin-top:10px">
    <div><b>The ocean.</b> The cosmic ocean of milk, before and between creations: vast, deep, endless.</div>
    <div><b>The serpent.</b> Ādiśeṣa, "the remainder", who remains when all else dissolves; his coils are the Lord's bed, his hoods His canopy.</div>
    <div><b>The Lord.</b> Dark blue like a rain cloud, in yellow silk, resting at perfect ease, eyes half-closed in <i>yoga-nidrā</i>, the sleep of meditation.</div>
    <div><b>The lotus.</b> From His navel rises a lotus; on it sits Brahmā, about to create the worlds.</div>
    <div><b>Lakṣmī.</b> The Goddess sits at His feet, serving Him with love.</div>
  </div>
</section>
''']
b.append(linepage(1,'THE PEACEFUL ONE','śāntākāraṃ · bhujagaśayanaṃ · padmanābhaṃ sureśaṃ',[
 ('Śāntākāram','śānta-ākāram','"whose form is peace". Not just looking calm: peace is His very shape.','The verse opens with peace before any power. The Lord we meditate on is not angry, rushed or anxious. To look at Him is already to grow calm.'),
 ('Bhujagaśayanam','bhujaga-śayanam','"who lies on the serpent". Bhujaga, "one that moves on its coils", is Ādiśeṣa.','He rests on a serpent, a creature most of us fear. What frightens us is His bed. Śeṣa is also time and the "remainder" left when worlds end: He rests on time itself.'),
 ('Padmanābham','padma-nābham','"lotus-navelled". From His navel springs the lotus from which Brahmā creates.','All creation grows from Him as a lotus grows from its stem. Name 48 and 196 of the Sahasranāma.'),
 ('Sureśam','sura-īśam','"Lord of the gods".','Even the gods, Brahmā included, depend on Him. The peaceful one is the ruler of all.')],
 'He is peace, resting on what we fear, <b>and all creation grows from Him</b>.'))
b.append(linepage(2,'VAST AS THE SKY','viśvādhāraṃ · gaganasadṛśaṃ · meghavarṇaṃ śubhāṅgam',[
 ('Viśvādhāram','viśva-ādhāram','"the support of the universe".','The surprise of the verse: the one lying at rest is the one holding everything up. He carries the universe the way the ground carries us, without strain.'),
 ('Gaganasadṛśam','gagana-sadṛśam','"like the sky": all-pervading, untouched, without limits.','Clouds, storms and smoke pass through the sky and leave it clean. So the Lord is in everything, yet untouched by it.'),
 ('Meghavarṇam','megha-varṇam','"the colour of a rain cloud": dark blue-grey.','In a hot land, the dark monsoon cloud means relief and life. His colour is a promise of grace, like rain on dry fields (compare Parjanya, name 810).'),
 ('Śubhāṅgam','śubha-aṅgam','"with auspicious limbs": beautiful and bringing good.','Every part of His form brings blessing. Name 586 of the Sahasranāma.')],
 'He holds up everything, <b>yet is free and open as the sky</b>.'))
b.append(linepage(3,'BELOVED OF LAKṢMĪ','lakṣmīkāntaṃ · kamalanayanaṃ · yogibhir dhyānagamyaṃ',[
 ('Lakṣmīkāntam','lakṣmī-kāntam','"the beloved of Lakṣmī".','The Lord of the universe is also a loving husband. Grace and abundance (Lakṣmī) are never far from Him.'),
 ('Kamalanayanam','kamala-nayanam','"lotus-eyed".','Long, gentle eyes like lotus petals: eyes of compassion. In the picture, they are half-closed in meditation, yet they see everything (compare animiṣa, name 215).'),
 ('Yogibhir dhyānagamyam','yogibhiḥ dhyāna-gamyam','"reached by yogis through meditation".','The verse tells us how to reach Him: not by argument but by <i>dhyāna</i>, quiet attention. That is exactly what the verse itself invites us to do.')],
 'Loving, compassionate, <b>and found in stillness</b>.'))
b.append(linepage(4,'I BOW TO VIṢṆU','vande viṣṇuṃ · bhavabhayaharaṃ · sarvalokaikanātham',[
 ('Vande Viṣṇum','vande viṣṇum','"I bow to Viṣṇu", the all-pervading.','The only verb in the whole verse comes here at the end: after fourteen words of seeing, one word of doing. First we look; then we bow.'),
 ('Bhavabhayaharam','bhava-bhaya-haram','"who takes away the fear of bhava": the fear that comes with worldly existence, birth and death.','This is the heart of the prayer. Not "give me things" but "take away my fear". The peaceful Lord gives His peace to us.'),
 ('Sarvalokaikanātham','sarva-loka-eka-nātham','"the one Lord of all the worlds".','One Lord for everyone, everywhere. The verse ends wide open, embracing every world and every being.')],
 'After all the seeing, one word: <b>"I bow"</b>, and the fear goes.'))
b.append(f'''<section class="page" id="paradox">
  <h2 class="page-title">THE PARADOX AT ITS HEART</h2>
  <div class="sub">How can He rest and hold everything at once?</div>
  <div class="g2">
    <div class="card bg-blue"><h4>😌 At rest</h4><p>Śāntākāra, the form of peace; lying down; eyes half-closed in meditation; beside Lakṣmī.</p></div>
    <div class="card bg-yellow"><h4>🌌 At work</h4><p>Viśvādhāra, holding up the universe; Brahmā's lotus rising; Lord of gods and of all worlds.</p></div>
  </div>
  <div class="panel reading">
    <p><b>Both, at once.</b> The verse never chooses. The deepest action comes from the deepest calm. A great surgeon, a great musician, a great parent: the best work comes from a steady, peaceful centre, not a frantic one.</p>
    <p><b>Resting on the serpent.</b> Śeṣa can stand for time and for the fears of life. The Lord does not run from them; He lies on them, at ease. The verse invites us to do the same: not to escape our troubles, but to rest in Him on top of them.</p>
    <p><b>The ocean.</b> The milk ocean is the cosmos between creations: vast, deep, unknown. In the middle of all that, peace.</p>
  </div>
  {talk("So I should lie down and do nothing?","Ha! No: be calm inside while you act. That's the Gītā's teaching too: work from peace, not from fear.")}
  <div class="key">Peace and power together: <b>act from a calm centre</b>.</div>
</section>

<section class="page" id="rhythm">
  <h2 class="page-title">THE RHYTHM</h2>
  <div class="sub">Mandākrāntā: "the slow-stepping"</div>
  <div class="panel reading"><p>The verse is in <b>mandākrāntā</b>, a stately metre of 17 syllables per line, made famous by Kālidāsa's <i>Meghadūta</i>, "the cloud messenger". Its slow, rolling beat suits a meditation: you cannot rush it.</p></div>
  <div class="panel" style="padding:10px">
    <span class="caption">One line, beat by beat (dark = long, white = short, red = pause)</span>
    <div class="beat">{''.join(f'<span class="{c}">{s}</span>' for s,c in [('śān','G'),('tā','G'),('kā','G'),('raṃ','G'),('|','Y'),('bhu',''),('ja',''),('ga',''),('śa',''),('ya',''),('naṃ','G'),('|','Y'),('pad','G'),('ma',''),('nā','G'),('bhaṃ','G'),('su',''),('re','G'),('śaṃ','G')])}</div>
  </div>
  <div class="steps">
    <div><b>Four long.</b> śān-tā-kā-raṃ: slow and steady, like four deep breaths.</div>
    <div><b>Then a run of short.</b> bhu-ja-ga-śa-ya: quick, like ripples on water.</div>
    <div><b>Then the rolling close.</b> naṃ pad-ma-nā-bhaṃ su-re-śaṃ: long-short-long, like waves settling.</div>
    <div><b>Pauses.</b> Rest briefly after the 4th and 10th syllables, where the dots are on the chant page.</div>
  </div>
  {talk("Does the rhythm really matter?","Try saying it fast: it feels wrong! The slow metre itself calms the breath. The sound teaches the peace the words describe.")}
</section>

<section class="page" id="meditate">
  <h2 class="page-title">A FIVE-MINUTE MEDITATION</h2>
  <div class="sub">Using the verse as it was meant to be used</div>
  <div class="steps">
    <div><b>Sit and breathe.</b> Sit comfortably. Take four slow breaths, matching the four long syllables "śān-tā-kā-raṃ".</div>
    <div><b>Chant once, slowly.</b> Say the whole verse aloud or silently, pausing at each dot.</div>
    <div><b>See the ocean.</b> Picture a vast, calm ocean, deep blue, stretching in every direction.</div>
    <div><b>See the Lord.</b> On it, the great serpent's coils, and Viṣṇu resting, peaceful, dark as a rain cloud, eyes gently half-closed. Lakṣmī at His feet; a lotus rising from His navel.</div>
    <div><b>Rest with Him.</b> Feel that the One holding up the universe is at peace, and that you too are held. Let go of one worry; place it on the ocean.</div>
    <div><b>Bow.</b> End with "vande viṣṇuṃ": I bow. Sit quietly for a few breaths before getting up.</div>
  </div>
  <div class="note">This is a simple devotional practice, not medical advice. Anyone can do it, any time of day.</div>
</section>

<section class="page" id="where">
  <h2 class="page-title">WHERE THIS PICTURE LIVES</h2>
  <div class="sub">The verse, the names and the sacred image</div>
  <table class="ct">
    <tr><th>In the verse</th><th>In the Sahasranāma</th></tr>
    <tr><td>Padmanābha, lotus-navelled</td><td>Names 48, 196, 346</td></tr>
    <tr><td>Lies on the ocean</td><td>Mahodadhiśaya (519), Kuvaleśaya (590)</td></tr>
    <tr><td>Śubhāṅga, auspicious limbs</td><td>Name 586</td></tr>
    <tr><td>Śānta, peaceful</td><td>Śāntaḥ (582), Śāntiḥ (584)</td></tr>
    <tr><td>Lord of the gods</td><td>Sureśa (85)</td></tr>
  </table>
  <div class="panel reading" style="margin-top:10px">
    <p><b>Anantaśayana.</b> The reclining Lord on the serpent, the <i>Anantaśayana</i> or <i>Śeṣaśāyī</i> form, is one of the great images of Indian art and worship, carved in temples and caves across India. In South India, the Raṅganātha form at Śrīraṅgam and Padmanābhasvāmi at Thiruvananthapuram are the best-known.</p>
    <p><b>Its place in prayer.</b> The verse is recited as one of the dhyāna verses before the Viṣṇu Sahasranāma (see Sahasranāma Part 1), and on its own in daily worship. Its author is not known.</p>
  </div>
  {talk("Who wrote it?","Nobody knows! Like many of the best-loved verses, it belongs to everyone.")}
</section>

<section class="page" id="end">
  <h2 class="page-title">THE VERSE ON ONE PAGE</h2>
  <div class="sub">Four lines, four lessons</div>
  <div class="steps">
    <div><b>Line 1.</b> He is peace itself, resting on what we fear, and all creation grows from Him.</div>
    <div><b>Line 2.</b> He holds up the universe, yet is free and open as the sky, dark as a cloud full of rain.</div>
    <div><b>Line 3.</b> Loving, compassionate, and found in stillness.</div>
    <div><b>Line 4.</b> I bow to Him, who takes away the fear of life, the one Lord of all.</div>
    <div><b>The lesson.</b> Act from a calm centre: peace and power together.</div>
  </div>
  {talk("What's the one thing to remember?","When you're anxious, picture Him: at rest, holding everything. Then say 'vande viṣṇum'.")}
  <div class="key">Śāntākāram: <b>peace that holds up the universe</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Viṣṇu dhyāna ślokam "śāntākāraṃ bhujagaśayanam". Text as recited among the dhyāna verses of the Viṣṇu Sahasranāma, checked against shlokam.org. Author unknown. Metre (mandākrāntā) from standard prosody. Name numbers follow the Sahasranāma list on shlokam.org. The meditation is a simple devotional practice, not medical advice. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
b.insert(1,'''<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#chant">The Verse</a></li>
    <li><span class="num">🖼</span><a href="#picture">The Picture</a></li>
    <li><span class="num">1</span><a href="#l1">Line 1: The Peaceful One</a></li>
    <li><span class="num">2</span><a href="#l2">Line 2: Vast as the Sky</a></li>
    <li><span class="num">3</span><a href="#l3">Line 3: Beloved of Lakṣmī</a></li>
    <li><span class="num">4</span><a href="#l4">Line 4: I Bow to Viṣṇu</a></li>
    <li><span class="num">☯</span><a href="#paradox">The Paradox at Its Heart</a></li>
    <li><span class="num">🎵</span><a href="#rhythm">The Rhythm</a></li>
    <li><span class="num">🧘</span><a href="#meditate">A Five-Minute Meditation</a></li>
    <li><span class="num">🛕</span><a href="#where">Where This Picture Lives</a></li>
    <li><span class="num">∑</span><a href="#end">The Verse on One Page</a></li>
  </ul>
</section>
''')
# contents should come after foreword: reorder
first=b[0]; i=first.index('<section class="page" id="chant">')
b[0]=first[:i]; b.insert(2,first[i:])
open('Shantakaram.html','w').write(head+''.join(b)+tail)
