exec(open('/home/claude/work/shakti/common_s.py').read())
import math
head=head_red('Mahālakṣmī · Kolhapur · The 18 Śakti Pīṭhas · srini.presents',
 'Mahālakṣmī (Ambābāī) of Kolhapur, the seventh of the 18 Śakti Pīṭhas: the west-facing Goddess with citron, mace, shield and cup, the Kolhāsura legend, the Tirupati story, the Kiraṇotsav when the setting sun touches her feet, Śilāhāra history and the image hidden and restored in the 18th century. An illustrated reference guide.')
def mh(lat,lon): return 40+(lon-72.5)*90, 20+(21-lat)*55
COASTM=[(21.0,72.6),(19.9,72.75),(19.0,72.85),(18.0,73.0),(17.0,73.3),(16.0,73.5),(15.6,73.75)]
def MHMAP(marks,w=560,h=290):
    sea='M0 0 '+' '.join(f'L{mh(a,b)[0]:.0f} {mh(a,b)[1]:.0f}' for a,b in COASTM)+f' L{mh(15.6,73.75)[0]:.0f} {h} L0 {h}z'
    g=''
    for la,lo,t,side,col in marks:
        x,y=mh(la,lo); r=8 if col=='#c0392b' else 6
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',t,12,'#111','start' if side=='r' else 'end')
    return (f'<rect width="{w}" height="{h}" fill="#f1e6cf"/><path d="{sea}" fill="#9ad1f5" stroke="#111" stroke-width="2"/>'+T(30,h-20,'ARABIAN SEA',11,'#1d4f9a','start')
     +T(w-20,30,'MAHARASHTRA',13,'#7a5a2a','end')+g+T(w-10,h-8,'simplified, not to scale',10,'#555','end'))
def AMBA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-30 60 q-4 -60 30 -70 q34 10 30 70z" fill="#2b2b2b"/><path d="M-30 60 q30 -10 60 0" fill="#c0392b"/><path d="M-26 40 q26 12 52 0" fill="none" stroke="#e0a800" stroke-width="4"/>'
 '<circle cy="-22" r="12" fill="#2b2b2b"/><circle cx="-4" cy="-24" r="2" fill="#fff"/><circle cx="4" cy="-24" r="2" fill="#fff"/>'
 '<path d="M-14 -32 h28 l-4 -18 h-20z" fill="#e0a800"/>'+''.join(f'<circle cx="{-10+k*5}" cy="-56" r="4" fill="#3a6a3a"/>' for k in range(5))+'<path d="M-12 -52 q12 -10 24 0" fill="#3a6a3a"/><path d="M-3 -40 v-6 a3 3 0 0 1 6 0 v6z" fill="#3a3a3a"/>'
 '<path d="M-22 -2 l-24 -12 M22 -2 l24 -12 M-20 14 l-24 4 M20 14 l24 4" stroke="#2b2b2b" stroke-width="6"/>'
 '<circle cx="-50" cy="-16" r="7" fill="#e0c03a"/><path d="M48 -24 l6 -14" stroke="#bbb" stroke-width="5"/><circle cx="54" cy="-40" r="5" fill="#bbb"/>'
 '<ellipse cx="-48" cy="20" rx="9" ry="11" fill="#7a5a2a"/><path d="M42 20 h14 l-2 8 h-10z" fill="#e0a800"/></g>')
def LIONB(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cy="-20" rx="40" ry="18" fill="#9a8a7a"/><circle cx="-38" cy="-30" r="18" fill="#8a7a6a"/><circle cx="-42" cy="-30" r="10" fill="#9a8a7a"/><rect x="-30" y="-6" width="8" height="12" fill="#9a8a7a"/><rect x="22" y="-6" width="8" height="12" fill="#9a8a7a"/></g>'
def HEMAD(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-60" y="-30" width="120" height="30" fill="#5a5a5a"/>'
 +''.join(f'<path d="M{-60+k*12} -30 v30" stroke="#888"/>' for k in range(11))+'<path d="M-40 -30 h80 l-10 -16 h-60z" fill="#6a6a6a"/><path d="M-26 -46 Q-24 -100 0 -114 Q24 -100 26 -46z" fill="#d8d0c0"/>'
 +''.join(f'<path d="M-24 {-54-k*10} H24" stroke-width="1"/>' for k in range(5))+'<path d="M0 -114 v-14"/><path d="M0 -128 l14 5 l-14 5z" fill="#ff8c1a"/><rect x="-8" y="-20" width="16" height="20" fill="#2a1a0a"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The dark stone Goddess Mahalakshmi with a cobra hood over her crown and a lion behind, golden rays of the setting sun falling on her through a doorway">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/><path d="M0 40 L240 150 L240 200 L0 120z" fill="#ffd166" opacity=".45"/><circle cx="30" cy="70" r="26" fill="#ffd166"/>'
 +LIONB(270,190,1.2)+AMBA(250,150,1.7)+HEMAD(90,262,.8)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Mahālakṣmī</b>, called <b>Ambābāī</b> in Kolhapur: Pīṭha no. 7 of the eighteen'),
 ('Hymn line','<i>kolhāpure mahālakṣmī</i>: “Mahālakṣmī in Kolhāpura”'),
 ('Where','<b>Kolhapur</b>, south-west Maharashtra, on the Pañcagaṅgā; old name <b>Karavīra</b>'),
 ('Body part','Satī’s <b>eyes</b>, in the usual list'),
 ('The image','Dark stone, about <b>3 ft</b>: holding a <b>citron</b>, <b>mace</b>, <b>shield</b> and <b>cup</b>; a five-hooded serpent and a liṅga on her crown; a lion behind'),
 ('Faces','<b>West</b>, unusual for a main image'),
 ('Kiraṇotsav','Twice a year the <b>setting sun</b> reaches her through the west door: feet, then chest, then her whole form'),
 ('History','Chalukya beginnings; Śilāhāra temple (11th c.); image hidden for centuries, reinstalled about <b>1715</b>'),
 ('In Maharashtra','One of the state’s <b>three and a half</b> Śakti Pīṭhas')])
 +talk("Lakṣmī is a Śakti Pīṭha? I thought those were Pārvatī.","At Kolhapur she's both. Wait till you see the liṅga on her crown.")))
pages.append(page('where','WHERE IT IS','Kolhapur and Maharashtra’s Goddesses',fig(560,290,'Simplified map of Maharashtra marking Kolhapur in red in the south-west, with Tuljapur, Mahur and Saptashringi, and Mumbai and Pune for reference',
 MHMAP([(16.70,74.24,'KOLHAPUR','r','#c0392b'),(18.01,76.07,'Tuljāpur','r','#ffd166'),(19.83,77.92,'Māhur','l','#ffd166'),(20.39,73.91,'Saptaśṛṅgī','r','#ffd166'),(19.08,72.88,'Mumbai','r','#bbb'),(18.52,73.86,'Pune','r','#bbb'),(17.68,75.33,'Paṇḍharpur','r','#bbb')]))+'''<div class="panel reading">
<p><b>The city.</b> Kolhapur lies on the <b>Pañcagaṅgā</b>, “five Gaṅgās”, below the Sahyādri hills. Its old name, <b>Karavīra</b>, is still used for the temple’s Goddess: <i>Karavīra-nivāsinī</i>, “she who dwells in Karavīra”.</p>
<p><b>Dakṣiṇa Kāśī.</b> Like several holy towns of the South, Kolhapur calls itself the “Kāśī of the South”, mainly because of this temple.</p>
<p><b>The yellow dots</b> are Maharashtra’s other great Goddess seats, including <b>Māhur</b>, the next pīṭha in the hymn.</p>
</div>'''))
pages.append(page('names','HER NAMES','Ambā, Lakṣmī, Karavīravāsinī',facts([
 ('Ambābāī','“Mother”: the name Kolhapur uses for her, as the city’s guardian'),
 ('Mahālakṣmī','“The great Lakṣmī”: the hymn’s name, and the temple’s formal one'),
 ('Karavīra-nivāsinī','“She who dwells in Karavīra”: a name in the Lakṣmī Sahasranāma'),
 ('Siṃhavāhinī','“Who rides the lion”: so an inscription of 1049 calls her'),
 ('Kolhāpura','The city named after the demon she defeated, Kolhāsura')])
 +talk("Another city named after a demon? Like Mysuru!","Same pattern: the Goddess wins, the demon asks to be remembered, the city keeps his name.")))
pages.append(page('pitha','THE PĪṬHA','Where Satī’s eyes fell',fig(560,150,'Shiva carrying Sati across a night sky, two glowing points falling onto a city by a river',
 '<rect width="560" height="150" fill="#2a0805"/>'+STAR+SHIVA(140,60,.7)+SATI(162,64,.55,-10)+'<path d="M190 80 q80 10 190 40" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><circle cx="378" cy="118" r="5" fill="#ffd166"/><circle cx="392" cy="122" r="5" fill="#ffd166"/>'+HEMAD(460,148,.45)+T(440,24,'KOLHĀPURA',14,'#ffd166'))+'''<div class="panel reading">
<p><b>The verse.</b> <i>kolhāpure mahālakṣmī, māhuryām ekavīrikā</i>: Kolhapur and Māhur, the two Maharashtra seats, named together.</p>
<p><b>What fell here.</b> Satī’s <b>eyes</b>, by the usual list. Some temple accounts add that the Goddess’s gaze watches over the city.</p>
<p><b>Older than the list.</b> Kolhapur’s own text, the <b>Karavīra Māhātmya</b>, tells a different story of why she is here: the slaying of Kolhāsura.</p>
</div>'''))
pages.append(page('goddess','THE GODDESS','Citron, mace, shield and cup',fig(560,230,'The dark stone Goddess with four arms holding a citron, a mace, a shield and a cup, a five-hooded serpent and lingam on her crown, a stone lion behind',
 '<rect width="560" height="230" fill="#fde4e4"/><rect x="160" y="10" width="240" height="200" fill="#f3e3c3" stroke="#111" stroke-width="2"/>'+LIONB(330,190,1.0)+AMBA(270,120,1.8)
 +T(90,50,'CITRON',12,'#7a1d12')+T(90,70,'MACE',12,'#7a1d12')+T(90,90,'SHIELD',12,'#7a1d12')+T(90,110,'CUP',12,'#7a1d12')+T(470,40,'SERPENT',12,'#7a1d12')+T(470,60,'+ LIṄGA',12,'#7a1d12')+T(470,190,'LION',12,'#7a1d12'))+'''<div class="g2">
<div class="card bg-red"><h4>🖐 Four hands</h4><p>A <b>mātuliṅga</b> (citron), a <b>gadā</b> (mace), a <b>kheṭa</b> (shield) and a <b>pānapātra</b> (drinking cup). The image is of dark stone, about three feet high, on a stone platform.</p></div>
<div class="card bg-yellow"><h4>🐍 On her head</h4><p>A <b>five-hooded serpent</b> shades her crown, and a small <b>liṅga</b> sits in it. Behind her stands her mount, a stone <b>lion</b>. A Śrī Yantra is carved on the wall.</p></div>
</div>'''+talk("A citron? Not a lotus?","Not a lotus in sight. This is not the Lakṣmī of the calendars. Turn the page.")))
pages.append(page('which','LAKṢMĪ OR AMBĀ?','The supreme Mahālakṣmī',fig(560,130,'An open book with a verse, next to the Goddess holding citron, mace, shield and cup, matching the text',
 '<rect width="560" height="130" fill="#fff4cd"/><rect x="60" y="20" width="220" height="90" rx="8" fill="#f3e3c3" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M80 {40+k*14} H260" stroke="#7a5a2a"/>' for k in range(5))+'<path d="M300 66 h60" stroke="#111" stroke-width="3"/><path d="M360 66 l-10 -6 v12z" fill="#111"/>'+AMBA(450,70,.8))+'''<div class="panel reading">
<p><b>The puzzle.</b> Mahālakṣmī with a mace and shield, a serpent and a liṅga on her head, riding a lion? That is not Viṣṇu’s gentle consort.</p>
<p><b>The answer.</b> An appendix to the <b>Devī Māhātmya</b>, the <i>Prādhānika Rahasya</i>, describes the <b>supreme Mahālakṣmī</b>, the first Goddess, from whom Mahākālī and Mahāsarasvatī come: she holds a <b>citron, mace, shield and cup</b>, and bears a <b>serpent, a liṅga and a yoni</b> on her head. Kolhapur’s image matches it closely.</p>
<p><b>Both at once.</b> So Ambābāī is the great Goddess of the Devī Māhātmya, honoured by Śaivas, Śāktas and Vaiṣṇavas alike. An inscription of 1049 calls her both lion-rider and Śiva’s consort; the Tirupati story makes her Viṣṇu’s.</p>
</div><div class="panel reading small"><p>Read the trinity of Mahākālī, Mahālakṣmī and Mahāsarasvatī in our <a href="/bhakti/devi/devi-mahatmya/">Devī Māhātmya</a> series.</p></div>'''))
pages.append(page('kolhasura','THE LEGEND · KOLHĀSURA','How the city got its name',fig(560,180,'The Goddess on her lion striking down a demon; afterwards, the demon kneeling and asking a favour',
 '<rect width="560" height="180" fill="#ffe9c4"/>'+LIONB(160,170,1.3)+AMBA(170,96,.9)+'<g transform="translate(330 170)">'+DEMON(0,0,1.5,'#4a3a2a')+'</g>'+'<path d="M220 90 L300 120" stroke="#bbb" stroke-width="5"/>'+'<g transform="translate(480 170)">'+DEMON(0,0,1.0,'#4a3a2a')+'</g>'+T(480,60,'“NAME IT',11,'#7a1d12')+T(480,76,'AFTER ME”',11,'#7a1d12'))+'''<div class="steps">
<div><b>The demon.</b> The <b>Karavīra Māhātmya</b> tells of <b>Kolhāsura</b>, who tormented gods and people in the land of Karavīra.</div>
<div><b>The Goddess.</b> Mahālakṣmī came to protect the people and killed him in battle.</div>
<div><b>The boon.</b> Dying, the demon asked that the place bear his name. She agreed: <b>Kolhāpura</b>. The spot where he fell became a tīrtha, and she stayed to guard the city.</div>
</div><div class="panel reading small"><p>The Karavīra Māhātmya is a local sacred text, said to belong to the Skanda Purāṇa; one study dates the Kolhāpur Māhātmya to about 1730.</p></div>'''))
pages.append(page('tirupati','THE LEGEND · TIRUPATI','Why Lakṣmī left Vaikuṇṭha',fig(560,170,'A sage kicking the sleeping Vishnu’s chest; Lakshmi walking away angry towards Kolhapur; Vishnu later on the Tirumala hill',
 '<rect width="560" height="170" fill="#e6eef8"/><path d="M40 120 q80 -20 160 0" fill="#7aa86a" stroke="#111"/>'+person(80,108,'#ffd60a','#3b6fd0',.8)+person(150,110,'#fff','#c98b5a',.8)+'<path d="M146 104 l-40 -6" stroke="#c98b5a" stroke-width="5"/>'
 +GENTLE(300,100,.7).replace('#e05a8a','#c0392b')+'<path d="M330 120 q60 -20 100 0" stroke="#c9a26b" stroke-width="3" stroke-dasharray="6 5" fill="none"/>'+HEMAD(470,160,.5)+T(470,166,'KOLHAPUR',10,'#7a1d12')+T(120,30,'BHṚGU KICKS VIṢṆU',11,'#1d4f9a'))+'''<div class="steps">
<div><b>The kick.</b> The sage <b>Bhṛgu</b>, testing the gods, came to Viṣṇu and, ignored, kicked him on the chest, where Lakṣmī lives. Viṣṇu only asked if the sage’s foot was hurt.</div>
<div><b>Lakṣmī leaves.</b> Angry that her husband had not defended her place, Lakṣmī left Vaikuṇṭha and came to Kolhapur.</div>
<div><b>Viṣṇu follows.</b> Viṣṇu came down to earth searching for her and settled on the Tirumala hill as <b>Śrīnivāsa</b>, Lord Veṅkaṭeśvara.</div>
</div>'''+talk("So Tirupati and Kolhapur are a married couple who quarrelled?","In the story, yes. Many pilgrims visit both, to see them both.")))
pages.append(page('kiran','THE KIRAṆOTSAV','When the sun bows to her',fig(560,200,'The setting sun’s rays passing through the long west door and halls of the temple, lighting the Goddess first at the feet, then the chest, then the whole image',
 '<rect width="560" height="200" fill="#2a0805"/><circle cx="40" cy="60" r="28" fill="#ffd166"/><path d="M60 70 L440 120 L440 170 L60 90z" fill="#ffd166" opacity=".55"/>'
 +''.join(f'<rect x="{110+k*80}" y="40" width="16" height="150" fill="#5a5a5a" stroke="#111"/>' for k in range(4))+AMBA(480,120,1.1)+T(480,196,'FEET · CHEST · ALL',11,'#ffd166'))+facts([
 ('When','Twice a year, around <b>31 January – 2 February</b> and <b>9 – 11 November</b>, about three days each'),
 ('How','The <b>setting sun</b>, low in the west, shines straight through the great west gate and the halls into the sanctum'),
 ('The order','Day one, her <b>feet</b>; day two, her <b>chest</b>; day three, her <b>whole form</b>'),
 ('Meaning','Devotees say the Sun god comes to pay homage to the Goddess'),
 ('Today','New buildings and changes along the line have shifted or shortened it in some years')])
 +talk("The temple was built to catch the sunset?","She faces west for a reason. Twice a year, the light walks up to her.")))
pages.append(page('history1','HISTORY · I','Chalukyas and Śilāhāras',tl([
 ('Legend','A Konkan king, <b>Karṇadeva</b>, is said to have cleared the forest and found the shrine (one tradition says 109 CE).'),
 ('7th c.','The first temple, often credited to the <b>Chalukyas</b>; one account gives 634 CE.'),
 ('940–1212','Kolhapur is the seat of the <b>Śilāhāra</b> kings; their age gives the temple much of its present core.'),
 ('1049','An inscription of a devotee of “Mahālakṣmī of Kolhapur” calls her <b>lion-rider</b> and <b>Śiva’s consort</b>.'),
 ('11th c.','<b>Gaṇḍarāditya</b> of the Śilāhāras completes the temple and builds the path around the sanctum.'),
 ('Later','The <b>Yādavas</b> of Devagiri and others patronise the shrine.')])
 +'<div class="panel reading small"><p>Dates for the earliest stages are traditions, not inscriptions. Jain Tīrthaṅkara figures carved on the sanctum walls reflect the Śilāhāra age, when Jainism flourished in Kolhapur.</p></div>'))
pages.append(page('history2','HISTORY · II','Hidden, then home',fig(560,150,'Priests secretly carrying the Goddess image into a house at night; later a royal procession bringing her back to the temple at Vijayadashami',
 '<rect width="560" height="150" fill="#1a1a2a"/>'+STAR+'<rect x="40" y="70" width="110" height="70" fill="#8a7a6a" stroke="#111" stroke-width="2"/><path d="M30 70 l65 -34 l65 34z" fill="#6a5a4a" stroke="#111" stroke-width="2"/>'+person(190,130,'#fff','#c98b5a',.7)+AMBA(210,104,.25)
 +'<rect x="300" y="0" width="260" height="150" fill="#ffe9c4"/>'+HEMAD(480,148,.8)+''.join(person(x,140,'#ff8c1a','#c98b5a',.6) for x in (330,360,390))+'<path d="M330 92 l-6 -30 l12 0z" fill="#ff8c1a" stroke="#111"/>')+tl([
 ('14th–17th c.','In the Sultanate and Ādilshāhī years the image is <b>hidden</b> in a priest’s house for safety.'),
 ('Early 1700s','Tārābāī makes Kolhapur a Maratha capital. A priest dreams of where the Goddess is hidden; <b>Sambhājī</b> of Kolhapur has her found.'),
 ('c. 1715','<b>Sidhojī Hindurāv Ghorpaḍe</b> reinstalls the image on <b>Vijayādaśamī</b>. (Sources give 1712, 1715 or 1722.)'),
 ('1838–43','The <b>Garuḍa Maṇḍapa</b> is added under Dājī Paṇḍit.')])))
pages.append(page('temple','THE TEMPLE','Black stone, west door',fig(560,180,'The temple of dark stone with a white later spire, side shrines and a tank',
 '<rect width="560" height="180" fill="#fdf1e8"/>'+HEMAD(280,170,1.3)+TEMPLE(110,170,1.2,'#d8d0c0')+TEMPLE(450,170,1.2,'#d8d0c0')+T(110,128,'MAHĀKĀLĪ',10,'#555')+T(450,128,'MAHĀSARASVATĪ',10,'#555'))+facts([
 ('Style','<b>Hemāḍpanti</b>-style dark stone, richly carved below, with a plainer later <b>spire</b>, which suggests rebuilding after the image returned'),
 ('Facing','<b>West</b>, toward the setting sun'),
 ('Shrines','<b>Mahākālī</b> and <b>Mahāsarasvatī</b>, the other two of the Devī Māhātmya trinity; Gaṇapati in an upper shrine; and many more'),
 ('Garuḍa Maṇḍapa','A 19th-century hall facing the sanctum'),
 ('Maṇikarṇikā Kuṇḍ','The old temple tank, recently restored')])
 +talk("Why does the bottom look older than the top?","Because it is. The carved base is Śilāhāra; the spire came later, after the troubles.")))
pages.append(page('saving','SAVING THE IMAGE','A thousand years of abhiṣeka',fig(560,140,'Conservators in a sanctum gently treating a worn stone image, with tools and a protective covering',
 '<rect width="560" height="140" fill="#eef3fa"/>'+AMBA(280,80,.9)+person(170,130,'#fff','#f2c79b',.9)+person(390,130,'#fff','#c98b5a',.9)+'<path d="M190 80 l50 0" stroke="#7a5a2a" stroke-width="4"/>')+'''<div class="steps">
<div><b>The problem.</b> Centuries of bathing the image with milk, water and other offerings had worn and cracked the stone.</div>
<div><b>The treatments.</b> Conservation was done in <b>1955</b>; the Archaeological Survey treated it again in <b>2015</b> with a coating called <i>vajralepa</i> (darśan stopped for two weeks), and again in <b>April 2024</b>.</div>
<div><b>The debate.</b> Devotees and experts have argued over methods: some praise the care taken; others say chemical work did harm, and there has even been talk of replacing the image. It remains a sensitive subject in Kolhapur.</div>
</div>'''))
pages.append(page('festivals','THROUGH THE YEAR','Her festivals',facts([
 ('Navarātri','The great festival; the Goddess is dressed in a different form each night and goes out in her palanquin'),
 ('Kiraṇotsav','The sun festival, January–February and November'),
 ('Rathotsav','The chariot festival'),
 ('Dīpāvalī','Lakṣmī’s own night of lamps'),
 ('Mārgaśīrṣa Thursdays','Weekly Lakṣmī worship in the winter month'),
 ('Lalitā Pañcamī','In Navarātri, the Goddess’s visit to her “friend” outside the city')])
 +'<div class="key">Ambābāī, <b>the city’s mother</b>, and the family Goddess of countless Maharashtrian homes.</div>'))
pages.append(page('threehalf','THREE AND A HALF PĪṬHAS','Maharashtra’s Goddess circuit',facts([
 ('Kolhapur','<b>Mahālakṣmī</b>: a full pīṭha'),('Tuljāpur','<b>Tulajā Bhavānī</b>, the Bhosales’ family Goddess: a full pīṭha'),
 ('Māhur','<b>Reṇukā</b> (Ekavīrā): a full pīṭha, and the next in our hymn'),('Vaṇī','<b>Saptaśṛṅgī</b> on her seven peaks: the “half” pīṭha')])
 +'''<div class="panel reading"><p><b>A Marathi tradition.</b> The “three and a half Śakti Pīṭhas” (<i>sāḍe tīn śaktipīṭhe</i>) are a much-loved pilgrimage of Maharashtra, separate from the 51 or 18 lists. Two of them, Kolhapur and Māhur, are also in the eighteen.</p></div>'''
 +talk("Why only half for Saptaśṛṅgī?","One explanation: the three and a half stand for the syllable Om, A-U-M and the half-syllable after. Saptaśṛṅgī is the half.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Ambābāī','Mother (Marathi, affectionate)'),('Karavīra','Old name of Kolhapur'),('Mātuliṅga','Citron fruit'),('Gadā · kheṭa','Mace · shield'),('Pānapātra','Drinking cup'),
 ('Kiraṇotsav','The festival of the sun’s rays'),('Hemāḍpanti','A Deccan style of dark-stone temple'),('Vajralepa','A protective coating for stone images'),('Māhātmya','A text in praise of a holy place'),('Śilāhāra','The dynasty of medieval Kolhapur')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Goddess.</b> Mahālakṣmī, Ambābāī: the supreme Goddess of the Devī Māhātmya, with citron, mace, shield, cup, serpent and liṅga; Satī’s eyes fell here.</div>
<div><b>The legends.</b> Kolhāsura gave the city its name; Lakṣmī left Vaikuṇṭha for Kolhapur, and Viṣṇu followed to Tirumala.</div>
<div><b>The light.</b> She faces west; twice a year the setting sun climbs from her feet to her face.</div>
<div><b>The history.</b> Chalukya and Śilāhāra temple; image hidden for centuries, home again about 1715.</div>
<div><b>The care.</b> Conservation in 1955, 2015 and 2024, and an ongoing debate.</div>
</div>'''+talk("One line to remember?","The Goddess who faces the sunset, and the sun comes to her.")+'<div class="key">The seventh seat of the Mother: <b>Mahālakṣmī of Kolhapur</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Mahalakshmi Temple, Kolhapur”: the black stone image about 3 ft; citron, mace, shield, cup; five-headed serpent; lion; Śrī Yantra; Karavīra-nivāsinī; Chalukya Karṇadeva 634; Hemāḍpanti; Jain figures; festivals; three and a half pīṭhas. cultureandheritage.org: west-facing; Rahasya of the Devī Māhātmya; Sambhājī’s letter (1712). Wikipedia mirror and adiveda.substack: Kiraṇotsav dates and order (setting sun). Lokmat Times, 2025 (changes to the alignment). ambabai.com and esamskriti.com (hidden in a priest’s house; Vijayādaśamī 1715). apalakolhapur.blogspot (Gazetteer: Sidhojī Ghorpaḍe; about 1722). hindu-blog.com (plain later spire). bhaktikalpa.com and templesinindiainfo.com (Karṇadeva 109; Gaṇḍarāditya; 1049 inscription; Garuḍa Maṇḍapa 1838–43). Wikipedia, “Kolhapur” (Śilāhāras 940–1212; Dakṣiṇa Kāśī). livehistoryindia.com (Kolhāpur Māhātmya c. 1730; Tirupati link). DNA India (1955, 2015, 2016 treatments); mypunepulse (April 2024); Free Press Journal (replacement talk). rkmm.org and dharma-renaissance (Kolhāsura and the name).</p>
<p><b>Sources differ:</b> date of reinstallation (1712, 1715 or 1722); the earliest temple date; Kiraṇotsav by sunrise or sunset (we follow the west door). <b>Not verified:</b> the Karṇadeva story; the Om explanation of the “half” pīṭha (popular). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('goddess','The Goddess'),('which','Lakṣmī or Ambā?'),('kolhasura','Legend · Kolhāsura'),('tirupati','Legend · Tirupati'),('kiran','The Kiraṇotsav'),
 ('history1','History · Chalukyas and Śilāhāras'),('history2','History · Hidden, then Home'),('temple','The Temple'),('saving','Saving the Image'),('festivals','Through the Year'),('threehalf','Three and a Half Pīṭhas'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 7 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7.4vw,74px)">MAHĀLAKṢMĪ</h1>
  <div class="series">AMBĀBĀĪ OF KOLHAPUR · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess who faces the sunset</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Kolhapur calls her <b>Ambābāī</b>, Mother. The hymn calls her <b>Mahālakṣmī</b>. Her dark stone image holds a citron and a mace, wears a serpent and a liṅga on her crown, and faces west, so that twice a year the setting sun walks up to her.</p>
    <p>She killed the demon who gave the city its name. In another story, she left Viṣṇu’s heaven in a temper and Viṣṇu followed her to Tirumala.</p>
    <p>This guide follows her legends, her temple, her centuries in hiding, and her return.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Ambābāī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why does the sun only reach her twice a year?","The sun sets in a different place every day. Only twice a year does it line up with her west door.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Mahalakshmi_Kolhapur.html','w').write(head+b+tail())
print('ok',len(pages))
