import sys; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
head=make_head('Madhya Raṅga · Śivanasamudra · Triraṅga · srini.presents',
 'Madhya Raṅga, the Raṅganātha temple at Śivanasamudra on the Kāverī: the youthful Jaganmohana Raṅga between the Gaganacukki and Bharacukki falls. Indra’s penance, the split rock, the temple, its festivals and the island around it. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
island=lambda cx,cy,rx,ry: f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#dfeccf" stroke="#111" stroke-width="2"/>'
GOP=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'+''.join(f'<path d="M{-22+k*3} {-k*10} h{44-k*6} l-2 -10 h{-(40-k*6)}z" fill="#e2cfa8"/>' for k in range(7))+'<path d="M-6 -70 q6 -10 12 0z" fill="#e0a800"/><rect x="-6" y="-12" width="12" height="12" fill="#7a5a2a"/></g>'
FALLS=lambda x,y,h=80,w=40: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#e8f6ff"/>'+''.join(f'<path d="M{x+6+k*8} {y} v{h}" stroke="#9fd3f0" stroke-width="3" stroke-dasharray="8 5"/>' for k in range(int(w/8)))
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="An island temple with a seven-tiered gopuram between two great white waterfalls, the youthful Ranganatha resting above">'
 '<rect width="380" height="268" fill="#14315a" rx="8"/>'+FALLS(20,120,148,60)+FALLS(300,120,148,60)
 +'<path d="M0 200 q190 -30 380 0 V268 H0z" fill="#4aa3df"/>'+island(190,206,110,30)+GOP(150,204,1.0)+'<rect x="176" y="176" width="70" height="28" fill="#f6f1e2" stroke="#111" stroke-width="2"/>'
 +RANGA(190,96,1.35,youth=True)+T(50,112,'BHARACUKKI',11,'#fff')+T(330,112,'GAGANACUKKI',11,'#fff')+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','Viṣṇu as Raṅganātha, called <b>Jaganmohana Raṅga</b> or <b>Mohana Raṅga</b>, “enchanter of the world”: the Lord in his <b>youthful</b> form'),
 ('Image','Carved from a single black <b>śālagrāma</b> stone, about <b>8–9 feet</b> long, reclining on Ādiśeṣa; Lakṣmī near his feet, a small Garuḍa near his head'),
 ('Place','An island of the Kāverī at <b>Śivanasamudra</b>, Kollegāl taluk, Chamarajanagar district, Karnataka'),
 ('Setting','Between the twin waterfalls <b>Bharacukki</b> and <b>Gaganacukki</b>'),
 ('Triraṅga','The <b>middle</b> of the three island Raṅgas'),
 ('Other names','<b>Takṣaka Kṣetra</b>; <b>Śilābhedana Kṣetra</b>, “where the rock was split”'),
 ('Legend','<b>Indra</b> freed from the sin of slaying Vṛtra'),
 ('Style','Drāviḍa, with a <b>seven-tiered</b> rājagopuram'),
 ('Festivals','Vaikuṇṭha Ekādaśī (a butter alaṅkāra), Dhanurmāsa worship, Ratha Saptamī, Brahmotsava')])
 +talk("A young Raṅganātha? How do you tell?","The devotees see it in his face: Jaganmohana, the charming one. Same Lord, same serpent bed, but here they see him as a youth.")))
mapfig=fig(560,260,'Schematic map: the Kaveri divides around the island of Shivanasamudra, falling as Bharachukki on the west and Gaganachukki on the east, with the Ranganatha temple and the Someshwara temple on the island. Not to scale.',
 '<rect width="560" height="260" fill="#4aa3df"/><path d="M80 130 C 120 40, 440 40, 480 130 C 440 220, 120 220, 80 130z" fill="#dfeccf" stroke="#111" stroke-width="2"/>'
 +FALLS(10,40,180,50)+FALLS(500,40,180,50)+T(35,32,'BHARACUKKI',11,'#fff')+T(525,32,'GAGANACUKKI',11,'#fff')
 +GOP(230,140,.7)+'<rect x="244" y="116" width="50" height="22" fill="#f6f1e2" stroke="#111" stroke-width="2"/>'+T(260,160,'RAṄGANĀTHA',11,'#0d3f73')
 +'<rect x="350" y="110" width="40" height="26" fill="#e2cfa8" stroke="#111" stroke-width="2"/>'+T(370,154,'SOMEŚVARA',11,'#0d3f73')
 +T(280,214,'ŚIVANASAMUDRA ISLAND',12,'#2a5a3a')+T(280,252,'simplified, not to scale',9,'#fff'))
pages.append(page('where','WHERE IT IS','An island between two waterfalls',mapfig+'''<div class="panel reading">
<p>Below Śrīraṅgapaṭṭaṇa, the Kāverī runs east until, at <b>Śivanasamudra</b>, she divides around a rocky island and plunges down the Deccan edge in two great falls: <b>Bharacukki</b> on the west branch, <b>Gaganacukki</b> on the east.</p>
<p>On the island stands the temple of <b>Madhya Raṅga</b>, the middle Raṅga, between the first at Śrīraṅgapaṭṭaṇa and the last at Śrīraṅgam.</p>
</div>'''))
deity=fig(560,240,'The youthful Ranganatha, carved from black saligrama stone, reclining on the seven-hooded serpent, Lakshmi near his feet and a small kneeling Garuda near his head',
 '<rect width="560" height="240" fill="#dcecff"/>'+RANGA(290,150,2.5,skin='#2a3a5a',youth=True)+'<circle cx="465" cy="150" r="10" fill="#f2c79b" stroke="#111"/><path d="M455 180 q10 -26 20 0z" fill="#c0392b" stroke="#111"/>'
 +'<g transform="translate(70 170)" stroke="#111" stroke-width="2"><circle r="8" fill="#c0392b"/><path d="M-12 26 q12 -30 24 0z" fill="#ffd60a"/><path d="M-14 10 q-10 -8 -6 -18 M14 10 q10 -8 6 -18" fill="none"/></g>'
 +T(70,212,'GARUḌA',11)+T(465,206,'LAKṢMĪ',11,'#c0392b')+T(290,30,'JAGANMOHANA RAṄGA',15,'#0d3f73'))
pages.append(page('deity','THE YOUTHFUL LORD','Jaganmohana, the enchanter of the world',deity+'''<div class="g2">
<div class="card bg-blue"><h4>🪨 One black stone</h4><p>The image is carved from a single black <b>śālagrāma</b> stone, about 8 feet long by one account and 9 by another, resting on Ādiśeṣa.</p></div>
<div class="card bg-yellow"><h4>✨ The youthful form</h4><p>Of the three Raṅgas, devotees see the Lord here in his <b>youth</b>: <b>Mohana Raṅga</b>, “the charming Raṅga”.</p></div>
</div>
<div class="panel reading"><p><b>Seven hoods or five?</b> Some sources say the serpent here has <b>seven</b> hoods, unlike five at the other two Raṅgas. Others describe seven hoods at Ādi Raṅga too. We give both rather than pick one. The goddess near the feet is described as Lakṣmī, and by one source as Lakṣmī in the form of the river Kāverī.</p></div>'''))
leg1=fig(560,200,'Indra on his white elephant striking the demon Vritra with the thunderbolt; then Indra in penance on a river island before Ranganatha',
 '<rect width="560" height="200" fill="#ffe3c4"/><rect x="0" y="0" width="270" height="200" fill="#2b2140"/>'+'<rect x="40" y="110" width="80" height="40" rx="16" fill="#eee" stroke="#111" stroke-width="2"/>'+person(80,108,'#ffd60a','#c98b5a',.8)+'<path d="M110 60 l10 20 h-8 l10 20" stroke="#ffd60a" stroke-width="4" fill="none"/>'+person(200,160,'#333','#5a7a4a',1.4)
 +'<path d="M270 170 q145 -20 290 0 V200 H270z" fill="#4aa3df"/>'+person(340,160,'#ffd60a','#c98b5a',1)+RANGA(460,110,.9,youth=True)+T(135,190,'VṚTRA SLAIN',12,'#fff')+T(415,30,'INDRA’S PENANCE',13,'#0d3f73'))
pages.append(page('legends1','THE LEGENDS · I','Indra and the sin of slaying Vṛtra',leg1+'''<div class="steps">
<div><b>The demon.</b> The Bhāgavata Purāṇa tells of <b>Vṛtra</b>, a mighty demon born from the sage Tvaṣṭṛ’s sacrifice, who terrified sages and gods alike.</div>
<div><b>The weapon.</b> The sage <b>Dadhīci</b> gave up his body, and from his bones Viśvakarmā made the <b>vajra</b>, the thunderbolt. Riding Airāvata, Indra slew Vṛtra.</div>
<div><b>The stain.</b> But the slaying left Indra with <b>brahmahatyā</b>, the grave sin of killing one born of a sage’s line.</div>
<div><b>The island.</b> Temple tradition says Viṣṇu sent Indra to an island in the Kāverī, <b>Takṣaka Kṣetra</b>, to do penance; Viśvakarmā carved a Raṅganātha from a single stone for him to worship.</div>
<div><b>Release.</b> After long penance and bathing in the Kāverī, Raṅganātha appeared and freed him. So the place became <b>Madhya Raṅga</b>, where worship is believed to wash away sin.</div>
</div>'''))
leg2=fig(560,200,'A great rock split by a thunderbolt, the river pouring through the gap on both sides as two waterfalls, with Shiva and Parvati watching from the sky',
 '<rect width="560" height="200" fill="#dcecff"/><path d="M180 200 L220 70 L340 70 L380 200z" fill="#8a7a6a" stroke="#111" stroke-width="2"/><path d="M280 70 l-10 40 l14 10 l-10 40" stroke="#ffd60a" stroke-width="5" fill="none"/>'+FALLS(120,80,120,40)+FALLS(400,80,120,40)
 +'<g transform="translate(470 40)">'+person(0,30,'#9fd3f0','#c98b5a',.6)+person(24,30,'#e05a8a','#c98b5a',.6)+'</g>'+T(140,70,'BHARACUKKI',10)+T(420,70,'GAGANACUKKI',10)+T(280,30,'THE SPLIT ROCK',13,'#0d3f73'))
pages.append(page('legends2','THE LEGENDS · II','The split rock, the falls and the name',leg2+'''<div class="steps">
<div><b>The rock split.</b> One telling continues Indra’s story: when the Kāverī rose and threatened his worship, Indra cleft the rock to turn the river aside. The two streams became <b>Bharacukki</b> and <b>Gaganacukki</b>, and the island is called <b>Śilābhedana Kṣetra</b>, “where the rock was split”.</div>
<div><b>The name.</b> Another tells that Śiva and Pārvatī, passing through the sky, saw the Kāverī spread out around a great rock like an ocean. Śiva praised it, and Pārvatī named the place <b>Śivanasamudra</b>, “Śiva’s ocean”.</div>
<div><b>Seven sages.</b> A third remembers the island as <b>Saptarṣi Kṣetra</b>, where the river split into seven streams, one before each of seven sages.</div>
<div><b>Tellings differ.</b> These are temple and local traditions, and sources tell them differently.</div>
</div>'''+talk("So who made the waterfalls, Indra or geology?","Geology made the Deccan edge! The legends make it holy. Both can sit on the same rock.")))
pages.append(page('history','HISTORY','What is known, and what is not',tl([
 ('Origins','Sources disagree. Deccan Herald dates the temple to the <b>Cōḻa</b> period; temple tradition links it to the early <b>Western Gaṅgas</b>. No founding inscription is cited by either.'),
 ('Patrons','Later work is credited to the <b>Hoysaḷas</b>, the <b>Vijayanagara</b> kings and the <b>Woḍeyars</b> of Mysore.'),
 ('A carved history','Deccan Herald notes a claim that the temple’s whole history is carved on a pillar in the Someśvara temple at Halasūru (Ulsoor), Bengaluru.'),
 ('Quiet years','A small, little-visited temple for long periods; Deccan Herald found some outer maṇḍapas neglected.'),
 ('2021','Renovation of the temple was reported to begin in February 2021.')])
 +'<div class="panel reading"><p><b>Small, but not lesser.</b> Beside Śrīraṅgapaṭṭaṇa’s royal history and Śrīraṅgam’s vast walls, Madhya Raṅga’s story is quiet and partly unrecorded. In the Triraṅga, it is still the indispensable middle.</p></div>'
 +talk("We don't know who built it?","Not for certain. Some temples come with inscriptions; some come only with devotion. Here, the honest answer is 'Cōḻa or Gaṅga, and patrons since'.")))
plan=fig(560,220,'Simplified layout: a seven-tiered rajagopuram, flagstaff and lamp pillar, a four-pillared mandapa, two Garuda pillars with lamps, a Garuda shrine, then the sanctum with the reclining Lord; a separate Ranganayaki shrine and an utsava mandapa in the courtyard',
 '<rect width="560" height="220" fill="#f6f1e2"/><rect x="30" y="20" width="500" height="180" fill="none" stroke="#7a5a2a" stroke-width="3"/>'
 +GOP(490,140,.6)+T(490,160,'RĀJAGOPURAM',9)+'<path d="M430 80 v60 M415 80 v60" stroke="#e0a800" stroke-width="5"/>'+T(422,160,'FLAG · LAMP',9)
 +'<rect x="350" y="96" width="40" height="36" fill="none" stroke="#111" stroke-width="2"/>'+T(370,160,'4-PILLAR',9)
 +'<path d="M310 90 v40 M300 90 v40" stroke="#c0392b" stroke-width="4"/>'+T(305,160,'GARUḌA PILLARS',9)
 +'<circle cx="262" cy="112" r="10" fill="#c0392b" stroke="#111"/>'+T(262,160,'GARUḌA',9)
 +'<rect x="80" y="80" width="150" height="66" fill="#dcecff" stroke="#111" stroke-width="2"/>'+RANGA(155,118,.5,skin='#2a3a5a',youth=True)+T(155,160,'SANCTUM',9)
 +'<rect x="60" y="30" width="60" height="34" fill="#ffe0e0" stroke="#111" stroke-width="2"/>'+T(90,76,'RAṄGANĀYAKĪ',9)
 +'<rect x="340" y="30" width="60" height="30" fill="#fff3b0" stroke="#111" stroke-width="2"/>'+T(370,74,'UTSAVA MAṆḌAPA',9)
 +T(280,214,'east → west · simplified, not to scale',9,'#555'))
pages.append(page('temple','THE TEMPLE','From gopuram to the Lord',plan+'''<div class="g2">
<div class="card bg-yellow"><h4>🏯 The approach</h4><p>A <b>seven-tiered rājagopuram</b>, a flagstaff and a lamp pillar, a four-pillared maṇḍapa, then <b>two Garuḍa pillars</b>, each crowned with a lamp, leading to a shrine of Garuḍa kneeling with folded hands.</p></div>
<div class="card bg-blue"><h4>🙏 Within</h4><p>The sanctum of the reclining Lord; a separate shrine of the Goddess <b>Raṅganāyakī</b>; and a small <b>utsava maṇḍapa</b> for festival images.</p></div>
</div>
<div class="panel reading"><p><b>Outside the walls.</b> A tall four-pillared stone structure and a five-pillared maṇḍapa stand further along the same line; Deccan Herald reported them neglected and in need of care.</p></div>'''))
pages.append(page('festivals','FESTIVALS','The Lord’s calendar','''<div class="g2">
<div class="card bg-green"><h4>🧈 Vaikuṇṭha Ekādaśī</h4><p>The greatest day: darśan through the <b>Vaikuṇṭha door</b>, and a rare <b>alaṅkāra of fresh butter</b> on the Lord.</p></div>
<div class="card bg-blue"><h4>🌅 Dhanurmāsa</h4><p>Special early-morning worship through the month, the season of the <b>Triraṅga</b> vow.</p></div>
<div class="card bg-yellow"><h4>☀️ Ratha Saptamī</h4><p>The sun’s birthday (Sūrya Jayantī), kept as a major day of worship.</p></div>
<div class="card bg-red"><h4>🎉 Brahmotsava</h4><p>The annual festival: several days of rituals and processions on vāhanas.</p></div>
</div>
<div class="panel reading"><p><b>Through the year.</b> Śrī Rāma Navamī, Narasiṃha Jayantī, Kṛṣṇa Janmāṣṭamī, Dīpāvalī and Kārtika Dīpotsava are also kept. Dates follow the temple’s own calendar each year.</p></div>'''
 +talk("A butter costume? Seriously?","Seriously! Butter alaṅkāra is a loving old custom. For the youthful Lord, think of little Kṛṣṇa the butter thief, now wearing it.")))
pages.append(page('island','AROUND THE ISLAND','Śiva, the Goddess and the falls',facts([
 ('Someśvara','A Śiva temple a short walk away, with a large black-stone liṅga; dated by Deccan Herald to the Cōḻa period, restored in 2011. A fish carved on its maṇḍapa ceiling is believed to grant wishes made beneath it'),
 ('Prasanna Mīnākṣī','The Goddess’s shrine at Someśvara; Ādi Śaṅkara is believed to have consecrated the <b>Śrī Cakra</b> here, toward which her eyes are turned; a sacred <b>śamī</b> tree stands outside'),
 ('Vanadurgā','A temple of the Goddess of the forest nearby'),
 ('Śiṃśā Māramma','The village goddess (grāmadevate) of the area, a form of Durgā'),
 ('The falls','Bharacukki and Gaganacukki, the Kāverī’s twin falls on either side of the island'),
 ('1902','One of Asia’s earliest hydroelectric stations was built at Śivanasamudra, sending power to the Kolar Gold Fields')])
 +talk("Raṅganātha, Śiva, the Goddess and a power station?","That's Śivanasamudra: Hari, Hara, the Mother, and the river's power, all on one rock.")))
pages.append(page('triranga','THE MIDDLE OF THREE','Madhya Raṅga in the Triraṅga',fig(560,120,'Three islands in a row along the river, the middle one highlighted','<rect width="560" height="120" fill="#4aa3df"/>'+''.join(island(x,60,70,24)+RANGA(x,54,.36,youth=(i==1)) for i,x in enumerate([100,280,460]))+'<rect x="200" y="24" width="160" height="72" fill="none" stroke="#ffd60a" stroke-width="4" rx="8"/>'+T(100,112,'ĀDI',11,'#fff')+T(280,112,'MADHYA · YOU ARE HERE',11,'#fff')+T(460,112,'ANTYA',11,'#fff'))+'''<div class="panel reading">
<p><b>The middle.</b> In the Triraṅga vow, Madhya Raṅga comes <b>second</b>, after <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga</a> at Śrīraṅgapaṭṭaṇa and before Antya Raṅga at Śrīraṅgam.</p>
<p><b>First, middle, last.</b> Some read the three as a life: beginning, middle and end. If so, the middle Raṅga is the youthful one, the Lord in the prime of life.</p>
<p>See the <a href="/bhakti/temples-of-india/triranga/">Triraṅga overview</a> for all three together.</p>
</div>'''))
glossary=[('Madhya Raṅga','“the middle Raṅga”: the Raṅganātha of Śivanasamudra'),('Jaganmohana','“enchanter of the world”'),('Śālagrāma','a sacred black stone worshipped as Viṣṇu'),('Śivanasamudra','“Śiva’s ocean”, the name of the island'),('Śilābhedana Kṣetra','“the place where the rock was split”'),('Takṣaka Kṣetra','an old name of the island in the Indra legend'),('Brahmahatyā','the grave sin of killing one of a sage’s line'),('Vajra','Indra’s thunderbolt, made from Dadhīci’s bones'),('Garuḍa stambha','a pillar facing the shrine, for Viṣṇu’s eagle'),('Alaṅkāra','the dressing and adorning of the deity'),('Ratha Saptamī','the sun’s festival, on the seventh day of Māgha'),('Śrī Cakra','a sacred diagram of the Goddess'),('Grāmadevate','a village’s guardian goddess')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','MADHYA RAṄGA ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The place.</b> An island in the Kāverī at Śivanasamudra, Karnataka, between the Bharacukki and Gaganacukki falls; the middle of the three Raṅgas.</div>
<div><b>The Lord.</b> Jaganmohana Raṅga, the youthful form, carved from one black śālagrāma, about 8–9 feet long.</div>
<div><b>The legends.</b> Indra’s penance for slaying Vṛtra; the split rock and the falls; Śiva’s ocean; the seven sages.</div>
<div><b>The history.</b> Cōḻa or Gaṅga origins, later Hoysaḷa, Vijayanagara and Woḍeyar patrons; renovation from 2021.</div>
<div><b>The festivals.</b> Vaikuṇṭha Ekādaśī with the butter alaṅkāra, Dhanurmāsa, Ratha Saptamī, Brahmotsava.</div>
</div>'''+talk("And next?","Downstream to the last and greatest: Antya Raṅga at Śrīraṅgam, seven walls around the Lord.")+'<div class="key">The middle Raṅga: <b>the Lord in his youth, between two waterfalls</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Ranganathaswamy Temple, Shivanasamudra” (location; Drāviḍa style; Jaganmohana and Mohana Raṅga; youthful form; renovation from February 2021; Someśvara and Vanadurgā). Tirthayatra.org (Indra and Vṛtra legend; Takṣaka Kṣetra; single śālagrāma about 8 ft; Lakṣmī and Garuḍa; two Garuḍa pillars; festivals including the butter alaṅkāra and Ratha Saptamī; Śiṃśā Māramma). Deccan Herald, “Of temples and legends” (Cōḻa period; śālagrāma; Raṅganāyakī shrine; utsava maṇḍapa; outer maṇḍapas; the Ulsoor pillar; Someśvara and Prasanna Mīnākṣī, the fish carving and the Śrī Cakra). Hindu Blog (seven-tiered rājagopuram; about 9 ft; the split rock and the falls; the name; Saptarṣi Kṣetra; festival list).</p>
<p><b>Not settled:</b> the temple’s origin (Cōḻa or Gaṅga); the length of the image (8 or 9 ft); the number of hoods (seven here, and at Ādi Raṅga, by different sources); the legends, which differ by source. The 1902 hydroelectric station is from general historical record.</p>
<p>Maps and plans are simplified illustrations, not to scale. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('deity','The Youthful Lord'),('legends1','Legends · Indra'),('legends2','Legends · The Split Rock'),('history','History'),('temple','The Temple'),('festivals','Festivals'),('island','Around the Island'),('triranga','The Middle of Three'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TRIRAṄGA · 2 OF 3</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">MADHYA RAṄGA</h1>
  <div class="series">JAGANMOHANA RAṄGANĀTHA · ŚIVANASAMUDRA · A REFERENCE GUIDE</div>
  <div class="tag">The middle Raṅga, between two waterfalls</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Downstream of Śrīraṅgapaṭṭaṇa, the Kāverī reaches the edge of the plateau, splits around a rock, and roars down in two great falls. On that rock, between the thunder of the water, a small temple keeps a quiet Lord: <b>Madhya Raṅga</b>.</p>
    <p>Here Raṅganātha is the <b>youthful</b> one, Jaganmohana, “enchanter of the world”, carved from a single black stone. Here, legend says, Indra came to wash away a terrible sin.</p>
    <p>Smaller and less visited than the other two Raṅgas, it is still the heart of the Triraṅga: the middle that joins the first and the last.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why is the middle one so small?","Not every great thing is big, Zappy. The Triraṅga needs all three, and the quiet middle holds the other two together.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/triranga/Madhya_Ranga.html','w').write(head+b+tail())
print('ok')
