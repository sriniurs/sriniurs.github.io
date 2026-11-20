import sys; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
head=make_head('Ādi Raṅga · Śrīraṅgapaṭṭaṇa · Triraṅga · srini.presents',
 'Ādi Raṅga, the Ranganāthasvāmi temple at Śrīraṅgapaṭṭaṇa on the Kāverī: the first of the three Raṅgas. Legends of Gautama and the Kāverī, the Gaṅga, Hoysaḷa, Vijayanagara and Mysore history, the temple, its festivals and the island around it. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
island=lambda cx,cy,rx,ry: f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#dfeccf" stroke="#111" stroke-width="2"/>'
GOP=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-22 0 h44 l-6 -22 h-32z" fill="#e2cfa8"/><path d="M-16 -22 h32 l-5 -18 h-22z" fill="#e2cfa8"/><path d="M-11 -40 h22 l-4 -14 h-14z" fill="#e2cfa8"/><path d="M-12 -54 q12 -12 24 0z" fill="#e0a800"/><rect x="-7" y="-14" width="14" height="14" fill="#7a5a2a"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The Srirangapatna temple gopuram on its island in the Kaveri at dawn, with the great reclining Ranganatha shown large in the sky above">'
 '<rect width="380" height="268" fill="#14315a" rx="8"/><circle cx="300" cy="70" r="26" fill="#ffd166"/>'
 +'<path d="M0 196 q190 -30 380 0 V268 H0z" fill="#4aa3df"/>'+island(190,206,150,30)+GOP(150,200,1.4)+'<rect x="186" y="170" width="90" height="30" fill="#f6f1e2" stroke="#111" stroke-width="2"/>'
 +RANGA(190,110,1.5)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','Viṣṇu as <b>Raṅganātha</b>, reclining on the <b>seven-hooded</b> Ādiśeṣa; also called <b>Ādi Raṅga</b>, the first Raṅga'),
 ('Place','<b>Śrīraṅgapaṭṭaṇa</b>, an island town in the Kāverī, Mandya district, Karnataka; the town is named after the temple'),
 ('Triraṅga','The <b>first</b> of the three island Raṅgas (with Śivanasamudra and Śrīraṅgam)'),
 ('Pañcaraṅga','The first of the five Raṅganātha temples on the Kāverī'),
 ('Founded','Inscription of <b>894 CE</b>: built by <b>Tirumalaiah</b>, a chief under the Western Gaṅgas'),
 ('Builders','Western Gaṅgas; <b>Hoysaḷas</b>; <b>Vijayanagara</b>; the <b>Woḍeyars</b> of Mysore'),
 ('Sacred link','Granted by Hoysaḷa King Viṣṇuvardhana to <b>Rāmānuja</b> as a seat of learning'),
 ('Legend','<b>Gautama Kṣetra</b>: where sage Gautama saw the Lord in his reclining form'),
 ('Big festivals','The Makara Saṅkrānti <b>Brahmotsava</b>, with the Vaikuṇṭha door opened; Vaikuṇṭha Ekādaśī'),
 ('Status','Protected by the <b>Archaeological Survey of India</b>')])
 +talk("A whole town named after a temple?","Śrī-Raṅga-paṭṭaṇa: 'the town of Śrī Raṅga'. The Lord came first; the kings, the forts and the capitals came later.")))
mapfig=fig(560,260,'Schematic map of the island of Srirangapatna: the Kaveri divides around it, the main stream on the east and the Paschimavahini on the west; the Ranganatha temple stands in the town, with the Sangama at the eastern tip. Not to scale.',
 '<rect width="560" height="260" fill="#4aa3df"/><path d="M60 130 C 120 40, 380 30, 500 120 C 400 220, 140 220, 60 130z" fill="#dfeccf" stroke="#111" stroke-width="2"/>'
 +GOP(260,130,.9)+'<rect x="272" y="104" width="60" height="26" fill="#f6f1e2" stroke="#111" stroke-width="2"/>'+T(290,152,'RAṄGANĀTHA TEMPLE',11,'#0d3f73')
 +T(110,40,'PAŚCIMAVĀHINĪ (west branch)',11,'#fff')+T(430,240,'KĀVERĪ (main stream)',11,'#fff')
 +'<circle cx="500" cy="122" r="6" fill="#ffd60a" stroke="#111"/>'+T(510,104,'SAṄGAMA',11,'#fff','start')
 +T(200,200,'ŚRĪRAṄGAPAṬṬAṆA ISLAND',12,'#2a5a3a')+T(280,252,'simplified, not to scale',9,'#fff'))
pages.append(page('where','WHERE IT IS','An island in the Kāverī',mapfig+'''<div class="panel reading">
<p>Śrīraṅgapaṭṭaṇa is a <b>river island</b>: the Kāverī divides and flows around the whole town. The main stream runs on its eastern side; the branch on the west flows westward, and is called <b>Paścimavāhinī</b>, “the west-flowing”.</p>
<p>It is the <b>first</b> of the three islands of the Triraṅga, upstream of Śivanasamudra and Śrīraṅgam, in the old Mysore country of southern Karnataka.</p>
</div>'''))
deity=fig(560,240,'The great reclining Ranganatha on the coils of seven-hooded Adisesha, his head resting on his right hand, his left arm along his body, with a goddess and the sage Gautama at his feet',
 '<rect width="560" height="240" fill="#dcecff"/>'+RANGA(280,150,2.6)+'<circle cx="455" cy="148" r="10" fill="#f2c79b" stroke="#111"/><path d="M445 180 q10 -26 20 0z" fill="#c0392b" stroke="#111"/><circle cx="490" cy="150" r="9" fill="#c98b5a" stroke="#111"/><path d="M480 180 q10 -26 20 0z" fill="#ff8c1a" stroke="#111"/>'
 +T(120,30,'SEVEN HOODS',12,'#2a7a4a')+T(470,206,'GODDESS · GAUTAMA',11,'#c0392b')+T(280,226,'RAṄGANĀTHA, ABOUT 4.5 M LONG',12,'#0d3f73'))
pages.append(page('deity','THE LORD OF ĀDI RAṄGA','A giant at rest',deity+'''<div class="g2">
<div class="card bg-blue"><h4>🐍 On seven hoods</h4><p>The Lord lies on the coils of <b>Ādiśeṣa</b>, whose <b>seven</b> hoods spread over his head like a canopy. The image is described as about <b>4.5 m</b> long.</p></div>
<div class="card bg-yellow"><h4>👑 The pose</h4><p>He rests his head on his right hand, with his left arm along his body; a tall crown, rich ornaments, and eyes half open in yogic sleep.</p></div>
</div>
<div class="panel reading"><p><b>Who is at his feet?</b> Sources differ: Wikipedia names <b>Lakṣmī</b> at his feet, with Śrīdevī, Bhūdevī and Brahmā beside him; temple tradition identifies the figure as the river goddess <b>Kāverī</b>, with the sage <b>Gautama</b>. Both readings fit the legends on the next pages.</p></div>'''))
leg1=fig(560,200,'The sage Gautama in deep penance on the bank of the Kaveri, and Vishnu appearing before him in his reclining form',
 '<rect width="560" height="200" fill="#ddf5ea"/><path d="M0 170 q140 -20 280 0 t280 0 V200 H0z" fill="#4aa3df"/>'+person(140,150,'#ff8c1a','#c98b5a',1.3)+'<circle cx="140" cy="70" r="30" fill="#ffd60a" opacity=".3"/>'+'<circle cx="380" cy="90" r="80" fill="#ffd60a" opacity=".3"/>'+RANGA(380,110,1.4)+T(140,190,'GAUTAMA',12)+T(380,30,'THE LORD APPEARS',13,'#0d3f73'))
pages.append(page('legends1','THE LEGENDS · I','Gautama Kṣetra',leg1+'''<div class="steps">
<div><b>The sage on the bank.</b> Temple tradition says the sage <b>Gautama</b> lived and did penance here on the Kāverī, longing to see Viṣṇu in his reclining form.</div>
<div><b>The vision.</b> Pleased, the Lord appeared as <b>Raṅganātha</b>, resting on Ādiśeṣa, in the yogic sleep the sage had prayed to see.</div>
<div><b>A name for the place.</b> So the island is also called <b>Gautama Kṣetra</b>, the sacred field of Gautama, and the sage is shown at the Lord’s feet.</div>
<div><b>Who built it?</b> One telling says that at Gautama’s request <b>Brahmā</b> himself built the first temple. History, on the next pages, has its own answer.</div>
</div>'''+talk("Gautama? The one from the Rāmāyaṇa?","The same famous name: Gautama, husband of Ahalyā. Many Kāverī shrines are linked to him. Whether it's one sage or a family of sages, tradition doesn't fuss.")))
leg2=fig(560,200,'The river goddess Kaveri doing penance, and Ranganatha granting her three boons shown as three glowing lamps',
 '<rect width="560" height="200" fill="#dcecff"/><path d="M0 150 q140 -20 280 0 t280 0 V200 H0z" fill="#4aa3df"/>'+person(140,140,'#4aa3df','#c98b5a',1.3)+RANGA(390,110,1.2)+''.join(f'<path d="M{250+k*40} 60 h16 l-3 8 h-10z" fill="#e0a800" stroke="#111"/><path d="M{258+k*40} 58 q-6 -10 0 -18 q6 8 0 18z" fill="#ffd60a" stroke="#111"/>' for k in range(3))+T(140,186,'KĀVERĪ',12)+T(290,30,'THREE BOONS',13,'#0d3f73'))
pages.append(page('legends2','THE LEGENDS · II','The river’s three boons',leg2+'''<div class="steps">
<div><b>The river’s penance.</b> Another temple tradition tells of the river goddess <b>Kāverī</b> herself doing penance here to win the Lord’s grace.</div>
<div><b>Three boons.</b> Pleased, Raṅganātha granted her three boons, one telling says: that her waters would be counted holier even than the Gaṅgā; that this place would become a great pilgrimage; and that he would stay here.</div>
<div><b>At his feet.</b> So devotees see the goddess at the Lord’s feet as Kāverī, the river who holds him on her island.</div>
<div><b>One river, three Raṅgas.</b> The same longing is told of all three islands: the Kāverī wraps her arms around the Lord three times on her way to the sea.</div>
</div>'''+talk("Holier than the Gaṅgā?","That's the river's boon, as Kāverī devotees tell it! Every great river has its own pride; the Gaṅgā's devotees have their own stories too.")))
pages.append(page('history1','HISTORY · I','From the Gaṅgas to Vijayanagara',tl([
 ('894 CE','An inscription records the temple built by <b>Tirumalaiah</b>, a local chief under the <b>Western Gaṅga</b> kings, whose capital was at Talakāḍu. An earlier shrine may have stood here. (Some sources print the date as 984.)'),
 ('1108–52','The <b>Hoysaḷa</b> king <b>Viṣṇuvardhana</b> grants the village to <b>Rāmānuja</b> as an <i>agrahāra</i>, a seat of learning.'),
 ('1210','An inscription of <b>Vīra Ballāḷa II</b> records additions and renovations; the temple’s lathe-turned pillars are Hoysaḷa work.'),
 ('1300s–1500s','Under <b>Vijayanagara</b>, Śrīraṅgapaṭṭaṇa becomes the seat of a great viceroyalty, overseeing vassals such as Mysore and Talakāḍu. The entrance gopuram is in the Vijayanagara style.')])
 +'<div class="panel reading"><p><b>Three styles in one temple.</b> Gaṅga foundations, Hoysaḷa pillars and a Vijayanagara gateway: the temple grew with each dynasty that ruled the island, and was never replaced by any of them.</p></div>'
 +talk("Rāmānuja got a whole village?","As a seat of learning, yes. The Hoysaḷa king who gave it, Viṣṇuvardhana, is remembered in tradition as Rāmānuja's great royal follower.")))
pages.append(page('history2','HISTORY · II','A royal capital, a famous siege',tl([
 ('1610','<b>Rāja Woḍeyar I</b> of Mysore takes the island from the Vijayanagara viceroy, makes it his capital, and celebrates <b>Navarātri</b> there that year: the beginning of the royal Mysore <b>Dasara</b>.'),
 ('1610–1799','Śrīraṅgapaṭṭaṇa is the capital of the Mysore kingdom; the Woḍeyars add to the temple.'),
 ('1761–1799','Real power passes to <b>Hyder Ali</b> and his son <b>Tipu Sultan</b>, who rule from the island fortress. Karnataka Tourism notes that both held the temple in regard.'),
 ('4 May 1799','British forces storm the fort; Tipu Sultan is killed. The Woḍeyars are restored, and the capital returns to Mysuru.'),
 ('Today','The temple is protected by the <b>Archaeological Survey of India</b> as a monument of national importance.')])
 +'<div class="panel reading"><p><b>Through it all.</b> Capitals moved and armies came and went across this island. The temple at its heart kept its worship through every change of ruler.</p></div>'
 +talk("Dasara started here, not in Mysuru?","Yes! The Woḍeyar Dasara began on this island in 1610 and moved to Mysuru after 1799. The Lord of Ādi Raṅga watched the first one.")))
plan=fig(560,230,'Simplified plan of the temple: an east-facing gopuram, two concentric enclosures, a series of halls (mukhamandapa, navaranga, sukhanasi) leading to the sanctum with the reclining Ranganatha',
 '<rect width="560" height="230" fill="#f6f1e2"/><rect x="40" y="20" width="480" height="190" fill="none" stroke="#7a5a2a" stroke-width="3"/><rect x="80" y="45" width="400" height="140" fill="none" stroke="#7a5a2a" stroke-width="3"/>'
 +'<rect x="490" y="95" width="40" height="40" fill="#e2cfa8" stroke="#111" stroke-width="2"/>'+T(510,155,'GOPURAM',9)
 +''.join(f'<rect x="{x}" y="90" width="{w}" height="50" fill="{c}" stroke="#111" stroke-width="2"/>'+T(x+w/2,160,t,9) for x,w,c,t in [(360,90,'#fff3b0','MUKHA-MAṆḌAPA'),(280,70,'#ffe3c4','NAVARAṄGA'),(220,50,'#ffe0e0','SUKHANĀSI'),(110,100,'#dcecff','SANCTUM')])
 +RANGA(160,120,.45)+T(280,214,'east → west · simplified, not to scale',9,'#555'))
pages.append(page('temple','THE TEMPLE TODAY','From gateway to sanctum',plan+'''<div class="g2">
<div class="card bg-yellow"><h4>🏯 The approach</h4><p>A Vijayanagara-style <b>gopuram</b> leads through <b>two concentric enclosures</b> (prākāras) and a line of halls: the <b>mukhamaṇḍapa</b>, the <b>navaraṅga</b> and the <b>sukhanāsi</b>, to the sanctum.</p></div>
<div class="card bg-blue"><h4>🪨 Hoysaḷa touch</h4><p>In the inner hall stand <b>lathe-turned pillars</b>, a Hoysaḷa signature; the hall roof carries small stucco shrines with images of Viṣṇu.</p></div>
</div>
<div class="panel reading"><p><b>Shrines within.</b> Around the main sanctum are shrines to <b>Narasiṃha</b>, <b>Gopālakṛṣṇa</b>, <b>Śrīnivāsa</b>, <b>Hanumān</b>, <b>Garuḍa</b> and the <b>Āḻvārs</b>, the Tamil poet-saints of Viṣṇu.</p></div>'''))
pages.append(page('festivals','FESTIVALS','The Lord’s calendar','''<div class="g2">
<div class="card bg-yellow"><h4>☀️ Saṅkrānti Brahmotsava</h4><p>The temple’s great festival falls in the month of <b>Puṣya</b>, around <b>Makara Saṅkrānti</b>. On its sixth day, as the sun turns north (Uttarāyaṇa), the <b>Vaikuṇṭha door</b> is opened for devotees.</p></div>
<div class="card bg-blue"><h4>🪔 Lakṣa Dīpotsava</h4><p>With the Brahmotsava comes the festival of a <b>hundred thousand lamps</b>, when the temple glows with oil lamps.</p></div>
<div class="card bg-green"><h4>🚪 Vaikuṇṭha Ekādaśī</h4><p>As at every Raṅganātha temple, the Ekādaśī of Dhanurmāsa is a high day, and the season of the <b>Triraṅga</b> vow.</p></div>
<div class="card bg-red"><h4>🦅 Garuḍa Utsava</h4><p>Temple tradition keeps a Garuḍa festival in memory of the Lord’s appearance to Gautama.</p></div>
</div>
<div class="panel reading"><p><b>A different door day.</b> At Śrīraṅgam the gate of Vaikuṇṭha opens on Vaikuṇṭha Ekādaśī; here, sources describe it opening during the Saṅkrānti Brahmotsava. Dates follow the temple’s own calendar each year.</p></div>'''
 +talk("Why a door to heaven in a temple?","It's a picture of the soul's last journey: through the door, to the Lord. Walking through it on the holy day is a way of saying 'take me there'.")))
pages.append(page('ramanuja','RĀMĀNUJA AND ĀDI RAṄGA','One teacher, two Raṅgas','''<div class="panel reading">
<p><b>The teacher.</b> <b>Rāmānuja</b> (traditionally 1017–1137) is the great teacher of <b>Viśiṣṭādvaita</b> and of the Śrīvaiṣṇava tradition, the worship of Viṣṇu with Lakṣmī.</p>
<p><b>In Karnataka.</b> Tradition holds that Rāmānuja spent many years in the Hoysaḷa country, centred on <b>Melukote</b>, where a great Śrīvaiṣṇava centre grew around him.</p>
<p><b>The grant.</b> Inscriptions show King <b>Viṣṇuvardhana</b> granting the village of Śrīraṅgapaṭṭaṇa to Rāmānuja as a seat of learning.</p>
<p><b>Two Raṅgas.</b> Rāmānuja’s life ended at <b>Śrīraṅgam</b>, the Antya Raṅga, where his preserved body is still enshrined. So the great teacher links the first and the last of the three Raṅgas.</p>
</div>'''+talk("So Ādi Raṅga and Antya Raṅga share a teacher?","Exactly. The Triraṅga isn't only a river path; it's also a teacher's path, from the Hoysaḷa country to Śrīraṅgam.")))
pages.append(page('island','AROUND THE ISLAND','A sacred island, and a historic one',facts([
 ('Paścimavāhinī','The west-flowing branch of the Kāverī, where families traditionally perform rites for their ancestors'),
 ('Saṅgama','The point where the two branches of the Kāverī meet again at the island’s eastern end'),
 ('Nimiṣāmbā','A temple of the Goddess (Pārvatī) on the bank of the Lokapāvanī, who devotees believe clears troubles “in a <i>nimiṣa</i>”, an instant'),
 ('Gaṅgādhareśvara','A Śiva temple among the town’s old shrines'),
 ('Lakṣmī-Narasiṃha','A temple of Narasiṃha with Lakṣmī, among the town’s old shrines'),
 ('Karighaṭṭa','A Śrīnivāsa temple on a black hill nearby, reached by about 450 stone steps'),
 ('The fort era','The fort walls, Tipu Sultan’s summer palace (Dariyā Daulat) and the Gumbaz, the tomb of Hyder Ali and Tipu, recall the island’s years as a capital')])
 +talk("A Śiva temple, a Devī temple and Viṣṇu all on one island?","That's typical of the old Mysore country: Śaiva, Śākta and Vaiṣṇava shrines side by side, and the river shared by all.")))
pages.append(page('triranga','THE FIRST OF THREE','Ādi Raṅga in the Triraṅga',fig(560,120,'Three islands in a row along the river, the first one highlighted','<rect width="560" height="120" fill="#4aa3df"/>'+''.join(island(x,60,70,24)+RANGA(x,54,.36,youth=(i==1)) for i,x in enumerate([100,280,460]))+'<rect x="20" y="24" width="160" height="72" fill="none" stroke="#ffd60a" stroke-width="4" rx="8"/>'+T(100,112,'ĀDI · YOU ARE HERE',11,'#fff')+T(280,112,'MADHYA',11,'#fff')+T(460,112,'ANTYA',11,'#fff'))+'''<div class="panel reading">
<p><b>The beginning.</b> In the Triraṅga, the vow to see all three Raṅganāthas in one day, Ādi Raṅga comes <b>first</b>: the first island the Kāverī makes on her way east.</p>
<p><b>Next.</b> Downstream lies <b>Madhya Raṅga</b> at Śivanasamudra, the youthful Lord between the waterfalls; and at the end, <b>Antya Raṅga</b> at Śrīraṅgam, the greatest of the three.</p>
<p>See the <a href="/bhakti/temples-of-india/triranga/">Triraṅga overview</a> for all three together.</p>
</div>'''))
glossary=[('Ādi Raṅga','“the first Raṅga”: the Raṅganātha of Śrīraṅgapaṭṭaṇa'),('Śrīraṅgapaṭṭaṇa','“the town of Śrī Raṅga”'),('Gautama Kṣetra','“Gautama’s sacred field”, a name of the island'),('Paścimavāhinī','“west-flowing”, the western branch of the Kāverī'),('Saṅgama','a confluence, where streams meet'),('Agrahāra','a village granted for Vedic learning'),('Prākāra','an enclosing wall and courtyard'),('Gopuram','a temple gateway tower'),('Mukhamaṇḍapa · Navaraṅga','the front hall · the inner pillared hall'),('Sukhanāsi','the vestibule before the sanctum'),('Brahmotsava','a temple’s great annual festival'),('Uttarāyaṇa','the sun’s northward course, beginning at Makara Saṅkrānti'),('Vaikuṇṭha dvāra','the “door of Vaikuṇṭha”, opened on a holy day'),('Viśiṣṭādvaita','Rāmānuja’s philosophy, “qualified non-dualism”')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','ĀDI RAṄGA ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The place.</b> Śrīraṅgapaṭṭaṇa, an island in the Kāverī in Karnataka, named after the Lord; the first of the three Raṅgas.</div>
<div><b>The Lord.</b> Raṅganātha, about 4.5 m long, on the seven-hooded Ādiśeṣa, with the goddess and the sage Gautama at his feet.</div>
<div><b>The legends.</b> Gautama’s penance and vision; the Kāverī’s penance and her three boons.</div>
<div><b>The history.</b> Founded 894 CE under the Gaṅgas; Hoysaḷa grant to Rāmānuja; Vijayanagara viceroys; Woḍeyar capital and the first Dasara (1610); Hyder Ali and Tipu Sultan; the siege of 1799.</div>
<div><b>The festivals.</b> The Saṅkrānti Brahmotsava with the Vaikuṇṭha door, the festival of lamps, Vaikuṇṭha Ekādaśī.</div>
</div>'''+talk("What's next?","Downstream to Madhya Raṅga: the youthful Lord on an island between two great waterfalls.")+'<div class="key">The first Raṅga: <b>where the river first holds the Lord</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Ranganathaswamy Temple, Srirangapatna”, and the sources it cites (894 CE inscription of Tirumalaiah; Viṣṇuvardhana’s grant to Rāmānuja; Vīra Ballāḷa II, 1210; George Michell on Woḍeyar contributions; two prākāras; mukhamaṇḍapa, navaraṅga, sukhanāsi; lathe-turned pillars; subsidiary shrines; ASI protection). Tirthayatra.org and TalkativeMan for the image (about 4.5 m; posture; Gautama and the goddess at the feet).</p>
<p><b>Legends:</b> Wikipedia (Gautama’s penance); Pilgrim Aide (the Kāverī’s three boons; the Saṅkrānti Brahmotsava and the Vaikuṇṭha door on its sixth day); Tirthayatra.org (Gautama Kṣetra; Garuḍa Utsava); Bhakti Bharat (Brahmā building the temple).</p>
<p><b>Town and history:</b> Wikipedia, “Srirangapatna” (river branches; Vijayanagara viceroyalty; 1610 and the first Navarātri; Nimiṣāmbā; Karighaṭṭa); Wikipedia, “Wadiyar dynasty”; Karnataka Tourism (4 May 1799; Hyder Ali and Tipu Sultan’s regard for the temple); Ministry of Tourism Utsav portal via CultureandHeritage.org (Dasara from 1610); Hindu Blog (Lakṣa Dīpotsava).</p>
<p><b>Not verified:</b> the founding year (894 in the temple article, 984 in the town article); the identity of the figure at the Lord’s feet (Lakṣmī or Kāverī); festival details, which follow the temple’s yearly calendar; Rāmānuja’s dates and years in Karnataka are traditional; the ancestral rites at Paścimavāhinī are widely described but not checked against a primary source.</p>
<p>Maps and plans are simplified illustrations, not to scale. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('deity','The Lord of Ādi Raṅga'),('legends1','Legends · Gautama'),('legends2','Legends · Kāverī'),('history1','History · I'),('history2','History · II'),('temple','The Temple Today'),('festivals','Festivals'),('ramanuja','Rāmānuja'),('island','Around the Island'),('triranga','The First of Three'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TRIRAṄGA · 1 OF 3</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">ĀDI RAṄGA</h1>
  <div class="series">ŚRĪ RAṄGANĀTHASVĀMI · ŚRĪRAṄGAPAṬṬAṆA · A REFERENCE GUIDE</div>
  <div class="tag">The first Raṅga on the Kāverī</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>The Kāverī has barely left the hills when she parts around an island and holds, in its heart, a giant at rest: <b>Raṅganātha</b>, Viṣṇu reclining on the seven-hooded serpent. This is <b>Ādi Raṅga</b>, the first of the three Raṅgas.</p>
    <p>The island took its name from him: <b>Śrīraṅgapaṭṭaṇa</b>, the town of Śrī Raṅga. Kings of four dynasties built here; the Mysore Dasara began here; a famous siege ended here. Through all of it, the Lord kept resting.</p>
    <p>This guide tells the temple’s legends, history, festivals, and the island around it.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("If he's resting, who's running the world?","He is, Zappy. That's the point of yoganidrā: the Lord at rest still holds everything. Calm is not the same as idle.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/triranga/Adi_Ranga.html','w').write(head+b+tail())
print('ok')
