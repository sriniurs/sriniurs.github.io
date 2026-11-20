import sys; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
head=make_head('Karighaṭṭa · Śrī Śrīnivāsa · Temples around Mysuru · srini.presents',
 'Karighaṭṭa, Chikka Tirupati: Śrī Śrīnivāsa on Nīlācala above the confluence of the Kāverī and Lokapāvanī. The hill from Tirumala, Kari and Kutsa, Bhṛgu’s penance, Vaikhānasa’s chariot. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def SRINI(x,y,s=1,skin='#2b2b3a',arms=True):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-20 70 h40 l-4 -60 h-32z" fill="#ffd60a"/><path d="M-16 10 q16 -14 32 0 v-30 q-16 -10 -32 0z" fill="'+skin+'"/>'
     +('<path d="M-16 -14 l-16 -22 M16 -14 l16 -22" stroke="'+skin+'" stroke-width="7"/><circle cx="-34" cy="-40" r="7" fill="#fff"/><circle cx="34" cy="-40" r="8" fill="#ffd60a"/><circle cx="34" cy="-40" r="3" fill="#c0392b"/>' if arms else '')
     +f'<circle cy="-34" r="12" fill="{skin}"/><path d="M-12 -46 h24 l-4 -22 h-16z" fill="#e0a800"/><path d="M-6 -36 h12" stroke="#fff" stroke-width="3"/><path d="M-1 -42 v8" stroke="#c0392b" stroke-width="2"/>'
     '<path d="M-16 -4 q16 12 32 0" fill="none" stroke="#c0392b" stroke-width="4"/></g>')
def HILL(x,y,w,h,c='#3a4a3a'):
    return f'<path d="M{x-w/2} {y} Q{x-w/4} {y-h*0.6} {x-w/10} {y-h} Q{x} {y-h*1.06} {x+w/10} {y-h} Q{x+w/4} {y-h*0.6} {x+w/2} {y}z" fill="{c}" stroke="#111" stroke-width="2"/>'
def TEMPLE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-22" y="-16" width="44" height="16" fill="#f2e6c8"/><path d="M-12 -16 l12 -18 l12 18z" fill="#e2cfa8"/><circle cy="-36" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def ELE(x,y,s=1,c='#555'):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cy="-40" rx="50" ry="32" fill="{c}"/><circle cx="-46" cy="-54" r="20" fill="{c}"/>'
     f'<path d="M-62 -46 q-12 26 2 46" fill="none" stroke="{c}" stroke-width="10"/><path d="M-56 -40 q-6 8 -14 6" stroke="#fff" stroke-width="3" fill="none"/><circle cx="-52" cy="-60" r="2.4" fill="#fff"/>'
     f'<rect x="-30" y="-12" width="12" height="18" fill="{c}"/><rect x="20" y="-12" width="12" height="18" fill="{c}"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Lord Srinivasa shining above a dark hill with a small temple on top, two rivers meeting at its foot">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/><circle cx="300" cy="60" r="44" fill="#ffd166" opacity=".35"/>'
 '<path d="M0 230 q100 -18 190 0 q90 18 190 0 V268 H0z" fill="#4aa3df"/><path d="M190 230 q-30 20 -60 38" stroke="#7cc4f0" stroke-width="10" fill="none"/>'
 +HILL(150,232,240,130)+TEMPLE(150,104,1.3)+SRINI(300,130,1.25)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','Viṣṇu as <b>Śrī Śrīnivāsa</b>, also called <b>Karigirivāsa</b> and <b>Bairāgi Veṅkaṭaramaṇa</b>: a black-stone image of about 6 ft'),
 ('With him','<b>Yoga Śrīnivāsa</b> and <b>Bhoga Śrīnivāsa</b>; <b>Padmāvatī</b> in her own shrine'),
 ('Place','<b>Karighaṭṭa</b> hill, outside Śrīraṅgapaṭṭaṇa, Mandya district, Karnataka'),
 ('Hill','About <b>2,697 ft</b> above sea level; called <b>Nīlācala</b>, “the blue mountain”, in the Varāha Purāṇa'),
 ('Rivers','The <b>Lokapāvanī</b> flows past the hill and joins the <b>Kāverī</b> at a saṅgama below it'),
 ('Popular name','<b>Chikka Tirupati</b>, “little Tirupati”'),
 ('Installed by','Tradition says the sage <b>Bhṛgu</b>'),
 ('Great festival','The <b>car festival</b> in Kumbha month (February–March), said to have been begun by the sage <b>Vaikhānasa</b>'),
 ('Neighbours','<b>Nimiṣāmbā</b> across the Lokapāvanī; <b>Ādi Raṅga</b> on the island of Śrīraṅgapaṭṭaṇa')])
 +talk("Little Tirupati? Is it really connected to Tirupati?","By legend, the hill itself came from Tirumala's seven hills! Hold on, Zappy, that story is coming up.")))
mapfig=fig(560,250,'Schematic map: Karighatta hill beside the Lokapavani river, which joins the Kaveri at a confluence; the island of Srirangapatna with the Ranganatha temple downstream, and the Nimishamba temple across the river. Not to scale.',
 '<rect width="560" height="250" fill="#eef6e4"/><path d="M0 190 C 160 170, 320 210, 560 180" fill="none" stroke="#4aa3df" stroke-width="22"/>'
 '<path d="M150 0 C 170 60, 200 120, 250 186" fill="none" stroke="#4aa3df" stroke-width="12"/>'
 +HILL(110,140,150,90)+TEMPLE(110,58,.8)+T(110,160,'KARIGHAṬṬA',12,'#0d3f73')
 +'<circle cx="252" cy="188" r="8" fill="#e0a800" stroke="#111"/>'+T(264,166,'SAṄGAMA',10,'#0d3f73','start')
 +'<rect x="300" y="132" width="34" height="22" fill="#fdecea" stroke="#111"/>'+T(318,126,'NIMIṢĀMBĀ',9,'#c0392b')
 +'<ellipse cx="460" cy="214" rx="70" ry="16" fill="#dfeccf" stroke="#111" stroke-width="2"/>'+T(460,240,'ŚRĪRAṄGAPAṬṬAṆA (Ādi Raṅga)',10,'#0d3f73')
 +T(190,40,'LOKAPĀVANĪ',11,'#1d6fb8','start')+T(40,220,'KĀVERĪ',12,'#1d6fb8')+T(520,30,'simplified, not to scale',9,'#555','end'))
pages.append(page('where','WHERE IT IS','A lone hill above a confluence',mapfig+'''<div class="panel reading">
<p><b>The hill.</b> Karighaṭṭa rises alone from the paddy fields just outside the island town of Śrīraṅgapaṭṭaṇa. Its slopes carry dry scrub, with tamarind and gooseberry trees around the temple on top.</p>
<p><b>The rivers.</b> The small <b>Lokapāvanī</b>, “purifier of the world”, flows past the hill and meets the Kāverī at a saṅgama below it.</p>
<p><b>The view.</b> From the top you can see Śrīraṅgapaṭṭaṇa and Mysuru, the confluence, and the Nimiṣāmbā temple across the Lokapāvanī.</p>
</div>'''))
deity=fig(560,230,'Three images of Srinivasa side by side: Vaikuntha Srinivasa in the centre, tall and black, with Yoga Srinivasa on his left and Bhoga Srinivasa on his right; Padmavati in her own shrine',
 '<rect width="560" height="230" fill="#dcecff"/><rect x="40" y="194" width="380" height="16" fill="#c9a26b" stroke="#111"/>'+SRINI(230,140,1.4)+SRINI(110,160,.9)+SRINI(350,160,.9)
 +'<g transform="translate(490 160)" stroke="#111" stroke-width="2"><circle cy="-34" r="12" fill="#f2c79b"/><path d="M-10 -46 h20 l-3 -12 h-14z" fill="#ffd60a"/><path d="M-22 50 q22 -80 44 0z" fill="#e05a8a"/><circle cx="-16" cy="-6" r="7" fill="#ffc2dc"/></g>'
 +T(230,226,'VAIKUṆṬHA ŚRĪNIVĀSA',12,'#0d3f73')+T(110,226,'YOGA',11)+T(350,226,'BHOGA',11)+T(490,226,'PADMĀVATĪ',11,'#c0392b'))
pages.append(page('deity','THE LORD OF THE HILL','Śrīnivāsa, Karigirivāsa, Bairāgi Veṅkaṭaramaṇa',deity+'''<div class="g2">
<div class="card bg-blue"><h4>🙏 Three Śrīnivāsas</h4><p>The main image is <b>Vaikuṇṭha Śrīnivāsa</b>, about 6 ft of black stone. Beside him stand <b>Yoga Śrīnivāsa</b>, shown without his consort, and <b>Bhoga Śrīnivāsa</b>.</p></div>
<div class="card bg-yellow"><h4>🌸 Bairāgi</h4><p>He is called <b>Bairāgi Veṅkaṭaramaṇa</b> because when he is decorated with flowers, he looks like a <i>bairāgi</i>, a wandering ascetic.</p></div>
</div>
<div class="panel reading"><p><b>The Goddess.</b> <b>Padmāvatī</b>, consort of Śrīnivāsa, has her own shrine on the western side. A Garuḍa statue and pillar face the main shrine, and behind the temple are the Lord’s footprints, the <b>Viṣṇu-pāda</b>.</p></div>'''))
leg1=fig(560,200,'A monkey hero flying through the sky carrying a blue hill; below, sages at a river confluence raise their hands asking him to set it down',
 '<rect width="560" height="200" fill="#ffe9c4"/><path d="M0 170 q140 -16 280 0 t280 0 V200 H0z" fill="#4aa3df"/>'
 +'<g transform="translate(300 70)">'+HILL(0,30,150,70,'#3b5a8a')+'</g>'
 +'<g transform="translate(300 110)" stroke="#111" stroke-width="2"><circle cy="-6" r="13" fill="#c98b5a"/><path d="M-14 10 q14 30 28 0z" fill="#c0392b"/><path d="M-14 -2 l-30 -40 M14 -2 l30 -40" stroke="#c98b5a" stroke-width="7"/><path d="M14 20 q30 10 20 -20" fill="none" stroke="#c98b5a" stroke-width="4"/></g>'
 +''.join(person(x,170,'#ff8c1a','#c98b5a',.7) for x in (90,130,170))+'<path d="M80 110 l-6 -20 M120 110 l-6 -20" stroke="#c98b5a" stroke-width="4"/>'
 +T(130,194,'SAGES AT THE SAṄGAMA',11,'#0d3f73')+T(300,24,'NĪLĀCALA',12,'#0d3f73'))
pages.append(page('legends1','THE LEGENDS · I','The hill that came from Tirumala',leg1+'''<div class="steps">
<div><b>Nīlācala.</b> The Varāha Purāṇa calls this hill <b>Nīlācala</b>, “the blue mountain”. Tradition says it was once one of the <b>Seven Hills of Tirumala</b>.</div>
<div><b>Sugrīva’s version.</b> When Rāma’s army was building the bridge to Laṅkā, <b>Sugrīva</b> uprooted Nīlācala and flew south with it. Over the Kāverī confluence, Viṣṇu’s devotees doing penance there begged him to leave it, and he set it down.</div>
<div><b>Hanumān’s version.</b> Another telling says <b>Hanumān</b>, sent for the Sañjīvanī mountain to save Lakṣmaṇa, took Nīlācala by mistake. The sages at the saṅgama told him the healing herbs were in the Himālaya, so he left this hill here.</div>
<div><b>So, Chikka Tirupati.</b> A piece of Tirumala, with Śrīnivāsa on top: <i>chikka</i> is Kannada for “small”.</div>
</div>'''+talk("Sugrīva or Hanumān: which one is right?","Both are told! Different tellings, same point: this hill is a piece of the Lord's own mountain.")))
leg2=fig(560,190,'A wild elephant charging at four girls by the river; a sage in deep meditation; the girls standing alive again before Srinivasa',
 '<rect width="560" height="190" fill="#e8f5e2"/><path d="M0 160 q140 -14 280 0 V190 H0z" fill="#4aa3df"/>'+ELE(110,150,.9)
 +''.join(person(x,160,c,'#c98b5a',.6) for x,c in ((200,'#e05a8a'),(228,'#ffd60a'),(256,'#3b6fd0'),(284,'#2e9a5a')))
 +person(390,166,'#ff8c1a','#c98b5a',.9)+'<path d="M374 120 q16 -20 32 0" fill="#fff" stroke="#111"/>'+SRINI(490,120,.8)
 +T(110,184,'KARI',12,'#c0392b')+T(390,184,'KUTSA',12,'#0d3f73'))
pages.append(page('legends2','THE LEGENDS · II','Kari the elephant, and the sage Kutsa',leg2+'''<div class="steps">
<div><b>The elephant.</b> A wild elephant named <b>Kari</b> attacked four girls bathing by the river, devotees of Śrīnivāsa, and killed them.</div>
<div><b>The sage.</b> The sage <b>Kutsa</b> (Kutsamuni) performed penance and prayed to the Lord to bring them back to life and to protect his devotees.</div>
<div><b>The name.</b> The hill is said to take its name from the elephant: <b>Kari-ghaṭṭa</b>, “elephant hill”. Others read <i>kari</i> as “black”, for the dark rock: “the black hill”.</div>
</div>'''+talk("Elephant hill or black hill?","In Kannada, kari can mean either! The legend says elephant; the rock says black. We'll let the hill keep both.")))
leg3=fig(560,200,'Sage Bhrigu in penance by a river; above, Lakshmi Narasimha appears; on the hill, Vishnu meditates under a pipal tree',
 '<rect width="560" height="200" fill="#fff4dc"/><path d="M0 170 q140 -14 280 0 V200 H0z" fill="#4aa3df"/>'+person(110,166,'#ff8c1a','#c98b5a',1)+'<path d="M90 106 q20 -24 40 0" fill="#fff" stroke="#111"/>'
 +'<g transform="translate(270 90)" stroke="#111" stroke-width="2"><circle r="22" fill="#e0a800"/><path d="M-18 -10 q-8 -20 6 -18 M18 -10 q8 -20 -6 -18" fill="#e0a800"/><circle cx="-7" cy="-4" r="3" fill="#111"/><circle cx="7" cy="-4" r="3" fill="#111"/><path d="M-8 8 q8 6 16 0" fill="none"/><path d="M-24 60 q24 -50 48 0z" fill="#ffd60a"/></g>'
 +'<g transform="translate(440 150)"><circle cy="-80" r="40" fill="#5a9a4a" stroke="#111" stroke-width="2"/><rect x="-6" y="-44" width="12" height="44" fill="#7a5a2a" stroke="#111"/></g>'+SRINI(420,160,.6)
 +T(110,194,'BHṚGU',12,'#0d3f73')+T(270,194,'LAKṢMĪ NARASIṂHA',11,'#c0392b')+T(440,194,'NĪLĀCALA',11,'#0d3f73'))
pages.append(page('legends3','THE LEGENDS · III','Bhṛgu’s curse and Bhṛgu’s prayer',leg3+'''<div class="steps">
<div><b>A war.</b> In a war between gods and demons, the fleeing demons took shelter with <b>Khyāti</b>, wife of the sage <b>Bhṛgu</b>, who would not give them up. Viṣṇu struck her down with his discus.</div>
<div><b>The curse.</b> Bhṛgu cursed Viṣṇu to be born on earth and suffer separation from his wife. Viṣṇu accepted it, and did penance under an aśvattha tree on <b>Nīlācala</b>.</div>
<div><b>Narasiṃha.</b> <b>Lakṣmī Narasiṃha</b> appeared there, and told Bhṛgu that he too must atone, for cursing the Lord.</div>
<div><b>The prayer.</b> Bhṛgu did penance on the banks of the <b>Maṇikarṇikā</b> river. Pleased, the Lord blessed him, and Bhṛgu asked him to stay on this hill for his devotees. So Śrīnivāsa came to Karighaṭṭa, and tradition says it was <b>Bhṛgu</b> who installed the image.</div>
</div>'''))
sages=fig(560,170,'Three sages seated in a row on the hill: Chandra the moon god, Bodhayana, and Vaikhanasa with a small chariot; a clump of sharp grass in front',
 '<rect width="560" height="170" fill="#f2f6ff"/>'+''.join(person(x,150,c,'#c98b5a',.9)+T(x,166,n,10,'#0d3f73') for x,c,n in ((90,'#e8e8f8','CANDRA'),(260,'#ff8c1a','BODHĀYANA'),(430,'#ffd60a','VAIKHĀNASA')))
 +'<path d="M70 70 a18 18 0 1 0 22 -16 a14 14 0 1 1 -22 16z" fill="#ffd166" stroke="#111"/>'+'<g transform="translate(500 140) scale(.5)">'+''.join(f'<circle cx="{c}" cy="0" r="9" fill="#7a5a2a" stroke="#111" stroke-width="2"/>' for c in (-20,20))+'<rect x="-28" y="-30" width="56" height="22" fill="#a0522d" stroke="#111" stroke-width="2"/><path d="M-30 -30 h60 l-30 -40z" fill="#c0392b" stroke="#111" stroke-width="2"/></g>'
 +''.join(f'<path d="M{x} 166 l{d} -40" stroke="#5a8a3a" stroke-width="2"/>' for x,d in ((330,-6),(336,0),(342,6),(348,-4),(354,4))))
pages.append(page('sages','SAGES OF NĪLĀCALA','Tales from the Purāṇas and tradition',sages+facts([
 ('Candra','The Moon, who had wronged his teacher Bṛhaspati by loving his wife Tārā, did penance by the <b>Paścimavāhinī</b> and had darśan of the Lord on Nīlācala every day'),
 ('Bodhāyana','The sage did penance here and became fit to compose the <b>Bodhāyana Dharma-sūtras</b>'),
 ('Vaikhānasa','Held the <b>first chariot festival</b> for Śrīnivāsa, in Kumbha month under the star Uttara Phalgunī: the festival still held today'),
 ('The darbha grass','The sharp grass on the hill, <b>darbhe hullu</b> in Kannada, used in sacred rites: the Varāha Purāṇa says it grew from hairs that fell when Viṣṇu as <b>Varāha</b>, the boar, shook himself')])
 +talk("Even the grass has a legend?","Of course! Priests all over use darbha in rituals. Here they say it came straight from the Lord's own boar-form.")))
plan=fig(560,220,'Simplified plan of the hilltop: steps and road climbing to a wooden gate, a courtyard with Garuda pillar, the main shrine with three images, the Padmavati shrine on the west, the footprints behind, and a wedding hall',
 '<rect width="560" height="220" fill="#f6f1e2"/><rect x="120" y="30" width="320" height="160" fill="none" stroke="#7a5a2a" stroke-width="4"/>'
 +'<rect x="250" y="176" width="60" height="18" fill="#7a5a2a" stroke="#111"/>'+T(280,212,'WOODEN GATE · STEPS AND ROAD BELOW',9)
 +'<rect x="272" y="140" width="16" height="16" fill="#e0a800" stroke="#111"/>'+T(310,152,'GARUḌA',9,'#555','start')
 +'<rect x="220" y="50" width="120" height="60" fill="#0d3f73" stroke="#111"/>'+T(280,84,'3 ŚRĪNIVĀSAS',10,'#fff')
 +'<rect x="140" y="70" width="56" height="40" fill="#fdecea" stroke="#111"/>'+T(168,94,'PADMĀVATĪ',8,'#c0392b')
 +'<ellipse cx="280" cy="40" rx="18" ry="6" fill="#c9a26b" stroke="#111"/>'+T(330,44,'VIṢṆU-PĀDA',9,'#555','start')
 +'<rect x="360" y="120" width="70" height="40" fill="#fff" stroke="#111"/>'+T(395,144,'KALYĀṆA MAṆḌAPA',8)
 +T(60,110,'W',14,'#555')+T(500,110,'E',14,'#555')+T(470,24,'simplified, not to scale',9,'#555'))
pages.append(page('temple','THE TEMPLE','On the summit',plan+'''<div class="g2">
<div class="card bg-yellow"><h4>🪜 The climb</h4><p>A long flight of stone steps, or a winding road, leads to the flat summit. Sources count the steps differently, from about <b>300</b> to <b>450</b>.</p></div>
<div class="card bg-blue"><h4>🚪 Inside</h4><p>Huge wooden doors open into a large quadrangle with the main shrine of the three Śrīnivāsas, Garuḍa facing them, and <b>Padmāvatī</b> to the west.</p></div>
</div>
<div class="panel reading"><p><b>Also on the summit:</b> the Lord’s footprints behind the temple, a shrine of Hanumān, and a <b>Kalyāṇa Maṇḍapa</b> where weddings are held.</p></div>'''))
pages.append(page('history','HISTORY','Legend, tradition and the siege',tl([
 ('Tretā Yuga','By tradition: Nīlācala set down at the saṅgama; Vaikhānasa’s first chariot festival.'),
 ('Purāṇas','The Varāha Purāṇa names the hill Nīlācala and tells of its grass; tradition cites the Padma Purāṇa for the tales of Candra and Bodhāyana.'),
 ('Bhṛgu','Tradition says the sage installed the image.'),
 ('1792','Third Anglo-Mysore War: Tipu Sultan holds a post on the hill, which British records call <b>Carigat</b> or <b>Karigaut Hill</b>. Lord Cornwallis’s army attacks it during the <b>siege of Śrīraṅgapaṭṭaṇa</b>, and later pulls his command back to the hill.'),
 ('1799','The final siege, in which Tipu dies. Local legend says British cannons stood on Karighaṭṭa; the records we found confirm only 1792.'),
 ('Today','A living hill shrine with its yearly car festival and a steady stream of pilgrims.')])
 +'''<div class="panel reading"><p><b>A note on dates.</b> Unlike the great island temples nearby, Karighaṭṭa has no dated inscriptions in the sources we used. Its story is carried by Purāṇa and local tradition, so this guide does not give it a building date.</p></div>'''
 +talk("A battlefield on a temple hill?","It's the highest point around: a perfect view of Tipu's fort. In 1792 the British wrote it into their war records as Carigat Hill.")))
fest=fig(560,170,'A temple chariot being pulled up by crowds at the foot of the hill',
 '<rect width="560" height="170" fill="#ffe9c4"/>'+HILL(420,170,240,120)+TEMPLE(420,54,.7)
 +'<g transform="translate(220 150)" stroke="#111" stroke-width="2"><circle cx="-24" cy="-8" r="10" fill="#7a5a2a"/><circle cx="24" cy="-8" r="10" fill="#7a5a2a"/><rect x="-34" y="-40" width="68" height="24" fill="#a0522d"/><path d="M-40 -40 h80 l-40 -60z" fill="#c0392b"/><path d="M-34 -40 q34 12 68 0" fill="none" stroke="#ffd60a" stroke-width="3"/></g>'
 +'<path d="M180 140 h-110" stroke="#7a5a2a" stroke-width="4"/>'+crowd(['#fff','#ffd60a','#ff8c1a','#3b6fd0','#e05a8a'],40,24,160,.5))
pages.append(page('festivals','THE CAR FESTIVAL','Vaikhānasa’s chariot',fest+'''<div class="panel reading">
<p><b>Since the Tretā Yuga.</b> Tradition says the sage <b>Vaikhānasa</b> held the first chariot festival for Śrīnivāsa, in <b>Kumbha</b> month under the star <b>Uttara Phalgunī</b>, and that it has been held every year since.</p>
<p><b>When.</b> The annual car festival and fair fall in Kumbha and Phālguna, roughly <b>February–March</b>, and draw pilgrims from all around Mysuru and Mandya.</p>
<p><b>Why Vaikhānasa?</b> Vaikhānasa is the sage of the <b>Vaikhānasa Āgama</b>, the tradition of temple worship followed at Tirumala: fitting for a “little Tirupati”.</p>
</div>'''))
pages.append(page('tirupati','CHIKKA TIRUPATI','Why devotees call it little Tirupati',facts([
 ('The hill','By legend, Nīlācala is one of Tirumala’s seven hills, carried here in the Rāmāyaṇa age'),
 ('The Lord','The same <b>Śrīnivāsa</b> (Veṅkaṭeśvara) as on Tirumala, with <b>Padmāvatī</b> as at Tiruchanur'),
 ('The sage','<b>Bhṛgu</b>, whose quarrel with Viṣṇu is also at the heart of Tirumala’s own story'),
 ('The festival','A chariot festival in the tradition of <b>Vaikhānasa</b>, sage of Tirumala’s mode of worship')])
 +'''<div class="panel reading"><p><b>Two Bhṛgu stories.</b> At Tirumala the best-known tale is of Bhṛgu kicking Viṣṇu’s chest, Lakṣmī leaving, and Viṣṇu coming to earth as Śrīnivāsa. At Karighaṭṭa the story is of Bhṛgu’s curse over Khyāti. Both tie the sage to the Lord’s coming to earth.</p></div>'''
 +talk("So I can pray here instead of going to Tirupati?","Devotees around Mysuru have done just that for generations. The Lord is the same; only the queue is shorter!")))
pages.append(page('around','AROUND KARIGHAṬṬA','The confluence and its temples',facts([
 ('The saṅgama','The meeting of the Lokapāvanī and the Kāverī below the hill'),
 ('Nimiṣāmbā','Across the Lokapāvanī: the Goddess as Pārvatī, believed to clear her devotees’ troubles in a moment (<i>nimiṣa</i>)'),
 ('Ādi Raṅga','Raṅganātha on the island of Śrīraṅgapaṭṭaṇa, first of the Triraṅga'),
 ('From the summit','Śrīraṅgapaṭṭaṇa, Mysuru city and the Cāmuṇḍī hills on a clear day')])
 +'''<div class="panel reading"><p><b>Viṣṇu reclining, Viṣṇu standing.</b> In one short stretch of the Kāverī you can see the Lord lying on Ādiśeṣa at Śrīraṅgapaṭṭaṇa and standing on his hill at Karighaṭṭa.</p>
<p>More temples around Mysuru: <a href="/bhakti/temples-of-india/around-mysuru/nanjangud/">Nañjanagūḍu</a>, <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga</a> and <a href="/bhakti/temples-of-india/triranga/madhya-ranga/">Madhya Raṅga</a>.</p></div>'''))
glossary=[('Karighaṭṭa','“elephant hill” or “black hill” (Kannada <i>kari</i>, <i>ghaṭṭa</i>)'),('Karigirivāsa','“the one who dwells on Karigiri”'),('Nīlācala','“the blue mountain”, the Purāṇic name of the hill'),('Chikka Tirupati','“little Tirupati”'),('Bairāgi','a wandering ascetic'),('Yoga · Bhoga','the Lord in meditation · the Lord in enjoyment, with his consorts'),('Viṣṇu-pāda','footprints of Viṣṇu'),('Saṅgama','a confluence of rivers'),('Lokapāvanī','“purifier of the world”'),('Paścimavāhinī','the Kāverī where she flows westward'),('Darbha','sacred grass used in rites'),('Varāha','Viṣṇu’s boar form'),('Vaikhānasa','the sage, and the āgama of temple worship named after him'),('Kalyāṇa Maṇḍapa','wedding hall'),('Ratha','temple chariot')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','KARIGHAṬṬA ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Lord.</b> Śrī Śrīnivāsa, Karigirivāsa, Bairāgi Veṅkaṭaramaṇa, with Yoga and Bhoga Śrīnivāsa and Padmāvatī.</div>
<div><b>The place.</b> A lone hill outside Śrīraṅgapaṭṭaṇa, above the meeting of the Lokapāvanī and the Kāverī: Chikka Tirupati.</div>
<div><b>The hill.</b> Nīlācala, carried from Tirumala by Sugrīva, or Hanumān, and set down at the saṅgama.</div>
<div><b>The legends.</b> Kari the elephant and Kutsa; Bhṛgu’s curse, Narasiṃha and Bhṛgu’s prayer; Candra, Bodhāyana and the darbha grass.</div>
<div><b>The festival.</b> The car festival of Kumbha–Phālguna, begun, they say, by Vaikhānasa himself.</div>
</div>'''+talk("One line to remember?","A piece of Tirumala, set down beside the Kāverī, so the Lord of the Seven Hills could stand near Mysuru too.")+'<div class="key">Chikka Tirupati: <b>the Lord of the Seven Hills, on one hill by the Kāverī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Karighatta”: “elephant hill”; 2,697 ft; scrub, tamarind and gooseberry; the Lokapāvanī; Nīlācala in the Varāha Purāṇa; Karigirivāsa, Śrīnivāsa and Bairāgi Veṅkaṭaramaṇa and the meaning of Bairāgi; the wooden door and quadrangle; Vaikuṇṭha, Yoga and Bhoga Śrīnivāsa; Padmāvatī on the west; Garuḍa and pillar; Kalyāṇa Maṇḍapa; Bhṛgu’s installation; 450 steps and the road; the view; Nimiṣāmbā; Kari and Kutsamuni; Sugrīva and Nīlācala; the darbha grass and Varāha; the cannons legend; Vaikhānasa and the car festival in Kumbha–Phālguna.</p>
<p><b>Legends:</b> Tirtha Yatra, “Karighatta”: Chikka Tirupati; Sugrīva and Hanumān tellings; Khyāti, Bhṛgu’s curse, Viṣṇu’s penance under the aśvattha, Lakṣmī Narasiṃha, Bhṛgu at the Maṇikarṇikā; Candra by the Paścimavāhinī; Bodhāyana; Vaikhānasa in Kumbha, Uttara Phalgunī; about 300 steps.</p>
<p><b>Other:</b> the six-foot image and the Viṣṇu-pāda (Indianetzone and devotee accounts); the Hanumān shrine (devotee accounts). Siege of 1792: Wikipedia, “Siege of Seringapatam (1792)” and FIBIS (the attack on the post at Carigat Hill; Cornwallis withdrawing to Karigaut Hill). The siege of 1799 and the Tirumala Bhṛgu story are general knowledge.</p>
<p><b>Sources differ:</b> the meaning of “Kari” (elephant or black); the number of steps (about 300 or 450); which hero carried the hill (Sugrīva or Hanumān).</p>
<p><b>Not verified:</b> any building date (none found); cannons on the hill in 1799 (legend). Maps and plans are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('deity','The Lord of the Hill'),('legends1','Legends · The Hill from Tirumala'),('legends2','Legends · Kari and Kutsa'),('legends3','Legends · Bhṛgu'),('sages','Sages of Nīlācala'),('temple','The Temple'),('history','History'),('festivals','The Car Festival'),('tirupati','Chikka Tirupati'),('around','Around Karighaṭṭa'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">KARIGHAṬṬA</h1>
  <div class="series">ŚRĪ ŚRĪNIVĀSA · CHIKKA TIRUPATI · A REFERENCE GUIDE</div>
  <div class="tag">A hill from Tirumala, beside the Kāverī</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Just outside Śrīraṅgapaṭṭaṇa, one dark hill rises alone from the green fields, where the little Lokapāvanī meets the Kāverī.</p>
    <p>On its summit stands <b>Śrī Śrīnivāsa</b>, the Lord of the Seven Hills, and devotees call the place <b>Chikka Tirupati</b>. The legends say the hill itself came from Tirumala.</p>
    <p>This guide tells the stories of the hill, its sages and its Lord.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Govinda Govinda,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A hill that flew in from Tirupati?","That's the legend! Monkeys, sages, an elephant and an angry rishi: this little hill has more stories than steps.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Karighatta.html','w').write(head+b+tail())
print('ok')
