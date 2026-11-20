exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Kamalā · Daśa Mahāvidyā 10 · srini.presents',
 'Kamalā or Kamalātmikā, the tenth and last of the Daśa Mahāvidyā: the lotus Goddess bathed by elephants, the Tantric form of Śrī-Lakṣmī, the churning of the ocean, Gaja-Lakṣmī from Sāñcī to today, the Śrī Sūkta, her seat in the Kāmākhyā sanctum, and the ten Great Wisdoms seen together. An illustrated reference guide.')
def LOTUS(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.5">'+''.join(f'<path d="M0 0 q{dx} -26 {dx*2} 0z" fill="#f2a6c0" transform="rotate({r})"/>' for dx,r in ((-10,0),(10,0),(-8,-30),(8,30)))+'<path d="M-10 0 q10 -34 20 0z" fill="#e0115f"/></g>'
def ELE(x,y,s=1,flip=1): return (f'<g transform="translate({x} {y}) scale({s*flip} {s})" stroke="#111" stroke-width="2"><path d="M-30 20 q-4 -40 30 -44 q34 4 30 44z" fill="#d8d8e0"/><path d="M20 -10 q24 -10 30 -40 q2 -10 -4 -12" fill="none" stroke="#d8d8e0" stroke-width="9"/><path d="M20 -10 q24 -10 30 -40 q2 -10 -4 -12" fill="none" stroke="#111" stroke-width="1"/>'
 '<path d="M-20 20 v14 M20 20 v14" stroke="#d8d8e0" stroke-width="10"/><circle cx="10" cy="-12" r="2.4" fill="#111"/><path d="M-6 -20 q-14 0 -14 16 q10 4 16 -4z" fill="#c8c8d0"/>'
 '<path d="M44 -54 l-6 -10 h16z" fill="#e0a800"/></g>')
def KAM(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 +''.join(f'<path d="M0 54 q{dx} -30 {dx*2} 0z" fill="#f2a6c0"/>' for dx in (-34,-20,20,34))+'<ellipse cy="54" rx="56" ry="8" fill="#2a9d6f"/>'
 '<path d="M-30 50 q-4 -54 30 -66 q34 12 30 66z" fill="#e0115f"/><path d="M-26 20 q26 10 52 0" stroke="#e0a800" stroke-width="4" fill="none"/>'
 '<path d="M-22 -8 l-26 -20 M22 -8 l26 -20 M-22 6 l-24 6 M22 6 l24 6" stroke="#f2c070" stroke-width="7"/>'
 +LOTUS(-50,-28,.7)+LOTUS(50,-28,.7)+'<circle cx="46" cy="14" r="4" fill="#e0a800"/><circle cx="52" cy="18" r="4" fill="#e0a800"/>'
 '<circle cy="-36" r="15" fill="#f2c070"/><path d="M-14 -48 h28 l-4 -16 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/>'
 '<circle cx="-5" cy="-38" r="2.4" fill="#111"/><circle cx="5" cy="-38" r="2.4" fill="#111"/><path d="M-3 -46 h6" stroke="#c0392b" stroke-width="2"/><path d="M-6 -29 q6 5 12 0" fill="none"/></g>')
def GAJA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+ELE(-96,-10,.9,1)+ELE(96,-10,.9,-1)+'<path d="M-50 -62 q20 10 34 34 M50 -62 q-20 10 -34 34" stroke="#5ab0f0" stroke-width="4" fill="none" stroke-dasharray="5 4"/>'+KAM(0,0,1)+'</g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The golden lotus goddess Kamala seated on a lotus, two white elephants pouring water over her">'
 '<rect width="380" height="268" fill="#0e3a4a" rx="8"/><rect y="220" width="380" height="48" fill="#1d6f8a"/>'+''.join(LOTUS(30+i*64,236,.6) for i in range(6))+GAJA(190,150,1.15)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Kamalā</b>, “she of the lotus”; also <b>Kamalātmikā</b>, “whose very self is the lotus”'),
 ('Place','<b>Tenth</b> and last of the Mahāvidyās'),
 ('She is','The Tantric form of <b>Śrī-Lakṣmī</b>: prosperity, beauty, fertility and grace'),
 ('Look','Golden; seated on a lotus; holding two lotuses; giving boons and “fear not”'),
 ('Elephants','Two or four elephants pour water over her: the <b>Gaja-Lakṣmī</b> image'),
 ('Vishnu?','Unlike Lakṣmī, she is shown <b>alone</b>; Viṣṇu is mostly absent'),
 ('Popularity','Kinsley: the best known Mahāvidyā, with the oldest worship outside the group'),
 ('Kāmākhyā','She sits in the main sanctum, with Tripurasundarī and Mātaṅgī')])
 +talk("The last Wisdom is just Lakṣmī?","Lakṣmī without Viṣṇu, on her own throne. The series ends in abundance.")))
pages.append(page('names','HER NAMES','The lotus lady',facts([
 ('Kamalā','From <i>kamala</i>, lotus'),
 ('Kamalātmikā','“She whose soul is the lotus”'),
 ('Kamalālayā','“She who dwells in the lotus”'),
 ('Śrī','Glory, splendour: her oldest name, from the Vedic age'),
 ('Gaja-Lakṣmī','Lakṣmī with the elephants')])
 +talk("Why a lotus?","It grows from mud and stays clean. Wealth without stain.")))
pages.append(page('form','HER FORM','The golden Goddess',fig(560,210,'A golden goddess seated on a lotus holding two lotuses, two white elephants pouring water over her',
 '<rect width="560" height="210" fill="#e8f6fb"/><rect y="180" width="560" height="30" fill="#9fd0ea"/>'+GAJA(280,130,1.2))+facts([
 ('Colour','Golden, shining like the sun'),
 ('Hands','Two lotuses; one gives boons, one says “fear not”'),
 ('Seat','A lotus, in a lotus pond'),
 ('Elephants','White elephants with golden pots pour nectar over her'),
 ('Jewels','Crown, silk and gold: a queen’s splendour')])))
pages.append(page('churning','FROM THE OCEAN OF MILK','Her birth',fig(560,170,'Gods and demons churning the ocean with a mountain and serpent, a goddess rising on a lotus',
 '<rect width="560" height="170" fill="#dff2fb"/><rect y="110" width="560" height="60" fill="#9fd0ea"/><path d="M270 120 l10 -90 l10 90z" fill="#8a6a4a" stroke="#111" stroke-width="2"/>'
 +'<path d="M100 80 q180 30 360 0" stroke="#2a7a4a" stroke-width="8" fill="none"/>'+''.join(person(x,70,c,s,.55) for x,c,s in ((80,'#e0a800','#f2c79b'),(130,'#e0a800','#f2c79b'),(430,'#3a3a5a','#5a7a5a'),(480,'#3a3a5a','#5a7a5a')))+KAM(380,120,.45))+'''<div class="steps">
<div><b>Lost glory.</b> When Śrī left the gods, they grew weak and the demons strong.</div>
<div><b>The churning.</b> On Viṣṇu’s advice, gods and demons churned the ocean of milk, with Mount Mandara as the rod and the serpent Vāsuki as the rope.</div>
<div><b>Her rising.</b> Among the treasures rose Lakṣmī on a lotus. She chose Viṣṇu, and the gods’ fortunes returned.</div>
</div>'''+talk("Where did she go when she left?","Into the ocean. Fortune hides when it is not respected.")))
pages.append(page('alone','WHY ALONE?','Kamalā versus Lakṣmī',facts([
 ('Lakṣmī','In Vaiṣṇava art she sits at Viṣṇu’s feet or by his side, with two hands'),
 ('Kamalā','In the Mahāvidyā set she has four arms and her own throne; Viṣṇu is mostly absent'),
 ('Meaning','The Goddess is not wealth belonging to a god: she is the source of it'),
 ('Not the same','Some writers insist Kamalā and Lakṣmī are distinct; most, like Kinsley, treat them as one'),
 ('Tenth wisdom','After nine fierce and strange forms, the Goddess as grace and fullness')])
 +talk("So she is independent here?","In this series every Goddess is Śakti herself. Kamalā too.")))
pages.append(page('gajalakshmi','GAJA-LAKṢMĪ','A very old image',fig(560,150,'A carved stone panel of a goddess on a lotus with two elephants, on a stupa gateway',
 '<rect width="560" height="150" fill="#f2e6c8"/><rect x="140" y="20" width="280" height="120" fill="#d8c8a0" stroke="#111" stroke-width="2"/><rect x="150" y="30" width="260" height="100" fill="#e8d8b0" stroke="#111"/>'+GAJA(280,96,.6).replace('#e0115f','#c8b080').replace('#d8d8e0','#c8b890').replace('#f2c070','#c8b080'))+facts([
 ('Sāñcī and Bharhut','Gaja-Lakṣmī is carved on the early Buddhist stūpa gateways and railings'),
 ('Coins','She appears on ancient Indian coins'),
 ('Shared','Buddhists, Jains and Hindus all used the image'),
 ('Today','Above doorways and shop counters across India')])
 +talk("A Buddhist Lakṣmī?","The image of fortune belonged to everyone. Sāñcī's gates show it.")))
pages.append(page('srisukta','THE ŚRĪ SŪKTA','Her oldest hymn',facts([
 ('What','A hymn to Śrī in the supplement (khila) to the Ṛg Veda'),
 ('Images','Golden, lotus-born, lotus-coloured, standing in a lotus, garlanded with lotuses'),
 ('Elephants','It praises her as awakened by the trumpeting of elephants'),
 ('Alakṣmī','It asks her to drive away Alakṣmī, misfortune: Dhūmāvatī’s sister'),
 ('Use','Still recited in Lakṣmī worship everywhere')])
 +'<div class="key">Read: <a href="/bhakti/devi/kanakadhara-stotram/">Kanakadhārā Stotram</a> · <a href="/bhakti/devi/mahalakshmi-ashtakam/">Mahālakṣmī Aṣṭakam</a></div>'))
pages.append(page('kamakhya','KAMALĀ AT KĀMĀKHYĀ','In the womb of the temple',facts([
 ('The ten','Kāmākhyā’s hill holds shrines of all ten Mahāvidyās'),
 ('Inside','Tripurasundarī, Mātaṅgī and Kamalā reside in the main sanctum'),
 ('Outside','The other seven have their own temples on Nīlācala'),
 ('Meaning','Beauty, speech and fortune at the heart of the Goddess’s own seat')])
 +'<div class="key">See: <a href="/bhakti/temples-of-india/18-shakti-peethas/kamakhya/">Kāmākhyā</a></div>'))
pages.append(page('temples','HER TEMPLES','Lakṣmī’s homes',facts([
 ('Kolhāpur','Mahālakṣmī (Ambābāī), one of the eighteen Śakti Pīṭhas'),
 ('Few as Kamalā','Shrines named for Kamalā the Mahāvidyā are rare; she is worshipped as Lakṣmī everywhere'),
 ('Every home','The household shrine, the shop and the cash box are her temples'),
 ('Mahāvidyā sets','She closes every row of ten, as at Kāmākhyā and Rajrappa')])
 +'<div class="key">See: <a href="/bhakti/temples-of-india/18-shakti-peethas/mahalakshmi-kolhapur/">Mahālakṣmī, Kolhāpur</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','Her days',facts([
 ('Dīpāvalī','Lakṣmī Pūjā on the new moon of Kārttika (or Āśvina, by month-reckoning); some almanacs mark Kamalā Jayantī the same night'),
 ('Śarad Pūrṇimā','Kojāgarī Lakṣmī Pūjā in Bengal and the east'),
 ('Varalakṣmī Vratam','Śrāvaṇa, in Karnataka, Andhra and Tamil Nadu'),
 ('Fridays','Lakṣmī’s weekday')])))
pages.append(page('ten','THE TEN TOGETHER','The whole series on one page','<div class="steps">'+''.join(f'<div><b>{n}. <a href="{MVS}{s}/">{nm}</a></b>: {m}.</div>' for n,nm,s,m in MVN)+'</div>'
 +talk("From Kālī to Kamalā?","From the darkness of time to the lotus of fortune. Ten faces, one Mother.")))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of fullness',facts([
 ('Abundance is sacred','Wealth, beauty and comfort are her gifts, not sins'),
 ('Stay clean','Like the lotus, live in the world without its mud sticking'),
 ('Respect fortune','She leaves where she is disrespected'),
 ('Full circle','The Mother who devours is also the Mother who feeds')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Kamala','Lotus'),('Śrī','Glory, fortune'),('Gaja','Elephant'),('Abhiṣeka','Ritual bathing'),('Kṣīrasāgara','Ocean of milk'),('Khila','Supplement to a Veda'),('Stūpa','Buddhist relic mound'),('Vrata','Vowed observance')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Kamalā, Kamalātmikā, tenth and last Mahāvidyā: the Tantric Śrī-Lakṣmī.</div>
<div><b>Form.</b> Golden, lotus-seated, lotus-holding, bathed by elephants.</div>
<div><b>Story.</b> She rose from the churned ocean of milk; here she reigns alone.</div>
<div><b>Places.</b> Kāmākhyā’s sanctum; Kolhāpur; Sāñcī’s gateways; every home.</div>
<div><b>Lesson.</b> Abundance is sacred; stay clean as the lotus.</div>
</div>'''+talk("One line to end the series?","Ten Wisdoms, one Mother. She is Kālī, and she is Kamalā.")+'<div class="key">The tenth Great Wisdom: <b>Kamalā</b>. The series is complete. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Goddess:</b> D. Kinsley, <i>Tantric Visions of the Divine Feminine</i> (1997), ch. on Kamalā (best known, oldest worship; Śrī-Lakṣmī; churning; Lakṣmī with two hands beside Viṣṇu); <i>Hindu Goddesses</i> (1988). Wikipedia, “Kamalatmika” (tenth; lotus; elephants; Viṣṇu mostly absent; Kamalālayā). Metropolitan Museum (Kamalātmikā as Tantric Lakṣmī; Gaja-Lakṣmī). Śrī Sūkta (Ṛg Veda khila).</p>
<p><b>Kāmākhyā:</b> Wikipedia, “Kamakhya Temple” (ten Mahāvidyā shrines; Tripurasundarī, Mātaṅgī and Kamalā in the main temple).</p>
<p><b>Sources differ / unverified:</b> whether Kamalā and Lakṣmī are one goddess or two; the date of Kamalā Jayantī; Gaja-Lakṣmī on Sāñcī and Bharhut and on coins is standard art history, summarised here. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('form','Her Form'),('churning','From the Ocean of Milk'),('alone','Why Alone?'),('gajalakshmi','Gaja-Lakṣmī'),('srisukta','The Śrī Sūkta'),
 ('kamakhya','Kamalā at Kāmākhyā'),('temples','Her Temples'),('festivals','Through the Year'),('ten','The Ten Together'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 10 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,76px)">KAMALĀ</h1>
  <div class="series">DAŚA MAHĀVIDYĀ · A REFERENCE GUIDE</div>
  <div class="tag">The lotus Goddess of fortune</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>The ten Great Wisdoms began with Kālī in the cremation ground. They end on a lotus. <b>Kamalā</b>, the tenth, is golden and smiling, holding lotuses, while white elephants pour water over her: the Gaja-Lakṣmī image found from the gateways of Sāñcī to the doorways of Indian homes.</p>
    <p>She is Śrī-Lakṣmī, risen from the ocean of milk. But in the Mahāvidyā circle she sits alone, without Viṣṇu: not a god’s consort but the source of fortune herself. At Kāmākhyā she lives in the inner sanctum.</p>
    <p>This guide tells her stories and meaning, and closes the series with all ten together.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Kamalā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is this the last one?","The tenth and last. After the storm of the fierce ones, the lotus.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms. Previous: <a href="{MVS}matangi/">Mātaṅgī</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV10_Kamala.html','w').write(head+b+tail())
print('ok',len(pages))
