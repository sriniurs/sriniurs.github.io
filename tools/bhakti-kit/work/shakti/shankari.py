exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Śāṅkarī Devī · Laṅkā · The 18 Śakti Pīṭhas · srini.presents',
 'Śāṅkarī Devī of Laṅkā, first of the 18 Śakti Pīṭhas, worshipped at Trincomalee beside Koṇeśvaram on Swami Rock: Rāvaṇa’s legend, the Tēvāram, the Portuguese destruction of 1622–24, the idols recovered in 1950, and the debate over which Laṅkā the hymn meant. An illustrated reference guide.')
def sl(lat,lon): return 230+(lon-79.5)*62, 18+(10.0-lat)*62
SLP=[(9.83,80.2),(9.6,80.6),(9.0,80.95),(8.6,81.2),(8.2,81.4),(7.6,81.75),(7.0,81.88),(6.5,81.7),(6.1,81.2),(5.92,80.6),(6.05,80.1),(6.6,79.88),(7.3,79.8),(8.0,79.78),(8.6,79.92),(9.05,79.95),(9.4,80.05),(9.7,80.0)]
SLPOLY=' '.join(f'{sl(a,b)[0]:.0f},{sl(a,b)[1]:.0f}' for a,b in SLP)
INDIA='<path d="M0 0 H200 L196 30 Q190 60 176 80 L150 100 L120 112 L0 112z" fill="#e8e2d0" stroke="#111" stroke-width="2"/>'
def SLMAP(marks,w=560,h=300):
    g=''
    for la,lo,t,side,col in marks:
        x,y=sl(la,lo); r=8 if col=='#c0392b' else 5
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',t,12,'#111','start' if side=='r' else 'end')
    return (f'<rect width="{w}" height="{h}" fill="#dff0fa"/>'+INDIA+T(80,40,'INDIA',13,'#555')+f'<polygon points="{SLPOLY}" fill="#e7f0d8" stroke="#111" stroke-width="2"/>'
     +'<path d="M168 62 L206 70 L224 78" stroke="#c9a26b" stroke-width="4" stroke-dasharray="5 4"/>'+T(330,170,'SRI LANKA',14,'#2e5a2e')+g+T(w-10,h-8,'simplified, not to scale',10,'#555','end'))
def ROCK(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-160 0 L-160 -60 Q-120 -90 -40 -96 L60 -100 L70 -60 L84 0z" fill="#8a7a6a"/>'
 '<path d="M60 -100 L64 -70 L80 -40 L84 0" fill="#6a5a4a"/><path d="M30 -100 l6 30" stroke="#3a2a1a" stroke-width="3"/></g>')
def GOP(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-30+k*3} {-k*12} h{60-k*6} l-1 -12 h{-(58-k*6)}z" fill="{"#f2e6c8" if k%2 else "#e2cfa8"}"/>' for k in range(5))+''.join(f'<path d="M{-10+j*5} {-60} l2 -10 l2 10z" fill="#e0a800"/>' for j in range(5))+'<rect x="-8" y="-18" width="16" height="18" fill="#5a3a1a"/></g>'
def SEA(y,w=560,h=60): return f'<rect x="0" y="{y}" width="{w}" height="{h}" fill="#4aa3df"/>'+''.join(f'<path d="M{k*40} {y+12+(k%3)*12} q10 -6 20 0" stroke="#fff" stroke-width="2" fill="none"/>' for k in range(w//40))
def RAVANA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-26 70 q-4 -60 26 -70 q30 10 26 70z" fill="#5a2a6a"/>'
 +''.join(f'<circle cx="{dx}" cy="-14" r="9" fill="#c98b5a"/><path d="M{dx-8} -22 h16 l-3 -9 h-10z" fill="#e0a800"/>' for dx in (-36,-18,0,18,36))
 +'<path d="M30 20 l40 -40" stroke="#bbb" stroke-width="6"/><path d="M-30 20 l-26 -10" stroke="#c98b5a" stroke-width="7"/></g>')
SANK=lambda x,y,s=1: GENTLE(x,y,s).replace('#e05a8a','#c0392b')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A temple with a gopura on a sheer cliff above the sea at sunrise, the Goddess Shankari beside it">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/><circle cx="300" cy="80" r="40" fill="#ffd166" opacity=".55"/>'
 +SEA(200,380,68)+ROCK(210,210,1.1)+GOP(170,100,.9)+SANK(320,150,1.1)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Śāṅkarī Devī</b>, “consort of Śaṅkara”: Pīṭha no. 1 of the eighteen'),
 ('Hymn line','<i>laṅkāyāṃ śāṅkarī devī</i>: “Śāṅkarī Devī in Laṅkā”'),
 ('Where','<b>Swami Rock</b> (Koṇamalai), Trincomalee, on Sri Lanka’s north-east coast'),
 ('Body part','Satī’s <b>groin</b>, in the usual South Indian list'),
 ('Her Lord','<b>Koṇeśvara</b> (Koṇanātha) with his consort <b>Mātumai Ammai</b>, at the great Śiva temple of <b>Koṇeśvaram</b>'),
 ('Titles','<b>Dakṣiṇa Kailāsa</b>, the Kailāsa of the South; <b>Tirukoṇamalai</b> of the Tēvāram'),
 ('Destroyed','By the Portuguese, from <b>14 April 1622</b>; stones used in Fort Frederick by <b>1624</b>'),
 ('Revived','Bronze images found in <b>1950</b>; temple reconsecrated on <b>3 March 1963</b>'),
 ('Debated','Whether the hymn’s “Laṅkā” is this site at all')])
 +talk("The very first pīṭha is outside India?","On an island cliff above the sea. The hymn begins where the land ends.")))
pages.append(page('where','WHERE IT IS','A headland on the north-east coast',fig(560,300,'Simplified map of Sri Lanka with the tip of India above it: Trincomalee on the north-east coast marked in red, with Nainativu, the other Ishvaram temples and Rameswaram also marked',
 SLMAP([(8.58,81.23,'TRINCOMALEE · KOṆEŚVARAM','r','#c0392b'),(9.61,79.77,'Nainativu','l','#ffd166'),(8.95,79.95,'Kētīśvaram','r','#bbb'),(7.58,79.80,'Munnēśvaram','l','#bbb'),(9.81,80.02,'Nakulēśvaram','r','#bbb'),(5.92,80.59,'Tēṉāvaram','l','#bbb'),(9.29,79.31,'Rāmeśvaram','l','#bbb')]))
 +'''<div class="panel reading">
<p><b>The rock.</b> Trincomalee stands on a peninsula guarding one of the world’s great natural harbours. At its tip is <b>Swami Rock</b>, a cliff that drops about <b>120 m</b> straight into the Indian Ocean. Koṇeśvaram and the Śāṅkarī shrine stand on top.</p>
<p><b>The fort.</b> Today you reach the rock through the gate of <b>Fort Frederick</b>, the fort the Portuguese built from the temple’s own stones.</p>
<p><b>Kailāsa’s line.</b> Trincomalee lies on almost the same longitude as Mount Kailāsa, which is why it is called the <b>Kailāsa of the South</b>.</p>
</div>'''))
pages.append(page('names','HER NAMES','And the names of the place',facts([
 ('Śāṅkarī','“She of Śaṅkara”: the Goddess as Śiva’s own power'),
 ('Laṅkā','The hymn’s word: Laṅkā, Rāvaṇa’s island, usually taken as Sri Lanka'),
 ('Tirukoṇamalai','“Sacred hill of Koṇam”: the Tamil name; <b>Trincomalee</b> grew from it'),
 ('Koṇeśvaram','The temple of <b>Koṇeśvara</b>, “Lord of the Koṇam”'),
 ('Dakṣiṇa Kailāsa','The Kailāsa of the South'),
 ('Mātumai Ammai','The Goddess as consort of Koṇeśvara in the main temple'),
 ('“Pagoda of Trincomalee”','What Europeans called the old temple, famous for its <b>thousand-pillared hall</b>')])
 +talk("Is Śāṅkarī different from Mātumai Ammai?","Two shrines, one Goddess. Śāṅkarī is her name as the pīṭha; Mātumai Ammai is her name as Koṇeśvara's consort.")))
pages.append(page('pitha','THE PĪṬHA','The first of eighteen',fig(560,150,'Shiva carrying Sati across the night sky, a glowing piece falling onto a cliff in the sea',
 '<rect width="560" height="150" fill="#2a0805"/>'+STAR+SHIVA(140,60,.7)+SATI(162,64,.55,-10)+'<path d="M190 80 q60 20 180 40" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><circle cx="372" cy="120" r="6" fill="#ffd166"/>'+SEA(126,560,24)+ROCK(420,130,.5)+T(420,24,'LAṄKĀ',14,'#ffd166'))+'''<div class="panel reading">
<p><b>The verse.</b> The hymn opens: <i>laṅkāyāṃ śāṅkarī devī</i>, “in Laṅkā, Śāṅkarī Devī”. Of all eighteen, she is named first.</p>
<p><b>What fell here.</b> The usual South Indian list says Satī’s <b>groin</b>. Some lists say her heart. The Bengali 51-list puts Laṅkā’s pīṭha elsewhere and says her <b>anklets</b> fell there (see “Which Laṅkā?”).</p>
<p><b>Why first?</b> No text explains the order. One reading: the hymn starts at the far south of the sacred land and works its way north to Kashmir.</p>
</div>'''))
pages.append(page('goddess','THE GODDESS TODAY','A small shrine on the great rock',fig(560,190,'A small Goddess shrine beside the larger Shiva temple on the cliff, a single old pillar standing at the cliff edge',
 '<rect width="560" height="190" fill="#fde4e4"/>'+SEA(150,560,40)+ROCK(330,160,1.3)+GOP(250,30,.8).replace('translate(250 30)','translate(250 60)')+TEMPLE(380,58,1.0)+SANK(380,22,.3)+'<rect x="420" y="16" width="8" height="42" fill="#d8d0c0" stroke="#111"/>'+T(424,12,'PILLAR',10,'#555')+T(250,110,'KOṆEŚVARAM',10,'#555')+T(380,76,'ŚĀṄKARĪ',10,'#7a1d12'))+'''<div class="g2">
<div class="card bg-red"><h4>🛕 Her shrine</h4><p>Śāṅkarī Devī has her own small shrine inside the Koṇeśvaram complex on Swami Rock, built in the Dravidian style. Pilgrims’ accounts describe a <b>standing, four-armed</b> image.</p></div>
<div class="card bg-yellow"><h4>🪨 The old site</h4><p>Temple tradition says her original shrine stood at the cliff edge and was destroyed with the rest in 1622–24. A lone pillar is said to mark the spot today.</p></div>
</div><div class="panel reading small"><p>Several writers date the present Śāṅkarī shrine to the revival of the 1950s; we could not confirm the exact year.</p></div>'''))
pages.append(page('konesvara','KOṆEŚVARA','The Lord on the hill',fig(560,170,'The Koneswaram temple on the cliff, a lingam in the sanctum, and a tall statue of Shiva on the rock',
 '<rect width="560" height="170" fill="#e6eef8"/>'+SEA(140,560,30)+ROCK(300,140,1.2)+GOP(200,96,.75)+'<path d="M300 80 v-14 a10 10 0 0 1 20 0 v14z" fill="#3a3a3a" stroke="#111"/>'+SHIVA(440,30,.55)+T(440,104,'ŚIVA STATUE',10,'#1d4f9a'))+facts([
 ('Deity','Śiva as <b>Koṇeśvara</b>, also Koṇanātha'),('Consort','<b>Mātumai Ammai</b>'),('Tēvāram','A <b>pāṭal peṟṟa sthalam</b>: sung by <b>Campantar</b> and <b>Cuntarar</b>'),
 ('Pañca Īśvaram','One of the five ancient coastal Śiva temples of Sri Lanka'),('Statue','A tall Śiva statue on the rock, rebuilt in <b>2018</b>')])
 +talk("So the pīṭha is inside a Śiva temple?","Like Śrīśailam and Kāśī. Where the Goddess sits, Śiva stays to guard her.")))
pages.append(page('ravana','THE LEGEND · RĀVAṆA','The cleft in the rock',fig(560,180,'Ten-headed Ravana trying to heave the cliff temple with his sword, the sword wedged in a cleft in the rock',
 '<rect width="560" height="180" fill="#ffe9c4"/>'+SEA(150,560,30)+ROCK(360,152,1.3)+GOP(330,56,.6)+'<path d="M386 30 l8 110" stroke="#3a2a1a" stroke-width="4"/>'+RAVANA(160,80,1.1)+'<path d="M228 60 L380 90" stroke="#bbb" stroke-width="5"/>'+T(400,24,'RĀVAṆAṈ VEṬṬU',11,'#7a1d12','start'))+'''<div class="steps">
<div><b>A devotee king.</b> In local tradition <b>Rāvaṇa</b>, king of Laṅkā and a great devotee of Śiva, came here with his mother to worship Koṇeśvara.</div>
<div><b>The sword.</b> When his mother grew too ill to make the journey, Rāvaṇa tried to prise the whole temple loose and carry it to her. Śiva made him drop his sword; it left a cleft in the rock, still called <b>Rāvaṇaṉ Veṭṭu</b>, “Rāvaṇa’s cut”.</div>
<div><b>The hot wells.</b> His mother died; grieving, Rāvaṇa struck the ground at nearby <b>Kanniya</b>, and hot springs gushed out, where he performed her last rites. Hindus there still perform rites for the dead.</div>
<div><b>An echo.</b> The story mirrors the Kailāsa legend, where Rāvaṇa tries to lift Śiva’s mountain and is pinned by Śiva’s toe.</div>
</div>'''))
pages.append(page('kulakkottan','THE LEGEND · THE BUILDER','Kulakkoṭṭaṉ and the stone chronicle',fig(560,150,'A Chola prince overseeing the building of a temple tower and a reservoir',
 '<rect width="560" height="150" fill="#f3e3c3"/>'+GOP(150,130,1.1)+'<ellipse cx="400" cy="120" rx="120" ry="18" fill="#4aa3df" stroke="#111" stroke-width="2"/>'+KING(280,140,.9,'#c0392b')+T(400,84,'KANTALAI TANK',11,'#1d4f9a'))+'''<div class="steps">
<div><b>The builder.</b> Tamil chronicles tell of <b>Kulakkoṭṭaṉ</b>, “builder of tank and temple”, a Chola prince who restored Koṇeśvaram and the great <b>Kantalai</b> reservoir that fed its lands. The <b>Konesar Kalveṭṭu</b> places his work in <b>432–440 CE</b>; others date him much earlier.</div>
<div><b>The stone chronicle.</b> The <i>Konesar Kalveṭṭu</i> is a 17th-century Tamil verse chronicle. It gives the shrine a founding date of about <b>1580 BCE</b>, a figure of tradition, not of archaeology.</div>
<div><b>A prophecy.</b> It also “foretells” that the <b>Paraṅkis</b> (the Portuguese) would destroy the temple. Since it was composed after 1622, historians read this as history told as prophecy.</div>
</div>'''))
pages.append(page('whichlanka','WHICH LAṄKĀ?','The debate, both sides',fig(560,140,'Two map pins on Sri Lanka, one at Trincomalee on the east coast and one at Nainativu island in the north, with a question mark between',
 '<rect width="560" height="140" fill="#fdf1e8"/><g transform="translate(-30 -4) scale(.48)">'+f'<polygon points="{SLPOLY}" fill="#e7f0d8" stroke="#111" stroke-width="3"/>'+f'<circle cx="{sl(8.58,81.23)[0]:.0f}" cy="{sl(8.58,81.23)[1]:.0f}" r="12" fill="#c0392b" stroke="#111" stroke-width="2"/><circle cx="{sl(9.61,79.77)[0]:.0f}" cy="{sl(9.61,79.77)[1]:.0f}" r="12" fill="#ffd166" stroke="#111" stroke-width="2"/></g>'
 +T(330,46,'TRINCOMALEE · ŚĀṄKARĪ',13,'#7a1d12','start')+T(330,76,'NAINATIVU · NĀKAPŪŚAṆI',13,'#7a5a2a','start')+T(330,108,'?',30,'#111','start'))+'''<div class="g2">
<div class="card bg-red"><h4>📍 Trincomalee</h4><p>The popular identification, especially among Sri Lankan Tamils and South Indian pilgrims: Laṅkā’s Śāṅkarī is the Goddess of Koṇeśvaram, the island’s most famous ancient Śiva temple.</p></div>
<div class="card bg-yellow"><h4>📍 Nainativu</h4><p>The <b>Nākapūśaṇi Ammaṉ</b> temple on Nainativu island, off Jaffna, is counted as Laṅkā’s pīṭha in the 51/64 traditions: there the Goddess is <b>Indrākṣī</b> and her <b>anklets</b> fell.</p></div>
</div><div class="panel reading"><p><b>What historians say.</b> Some reference works call the hymn’s Laṅkā “historically undetermined”, and say that Trincomalee’s claim is a fairly recent popular identification. Others point out that Koṇeśvaram has been a major Śākta-Śaiva centre for over a thousand years. The hymn itself names only “Laṅkā”.</p></div>'''))
pages.append(page('history1','HISTORY · I','From Purāṇa to pilgrim kings',tl([
 ('c. 300 CE','The <b>Vāyu Purāṇa</b> is cited as the earliest mention of the shrine.'),
 ('6th–7th c.','<b>Campantar</b> sings of Tirukoṇamalai in the Tēvāram; <b>Cuntarar</b> follows.'),
 ('537–668','The <b>thousand-pillared hall</b> (Āyiram Kāl Maṇṭapam) is dated to this Pallava period.'),
 ('1131–53','<b>Gajabāhu II</b> of Polonnaruwa is remembered as a devotee and donor.'),
 ('1223','A Kalinga king, <b>Codaganga Deva</b>, makes gifts after worshipping on Tamil New Year’s Day.'),
 ('1262','<b>Jaṭāvarman Vīra Pāṇḍya</b> sets up the Pāṇḍya bull and double-fish emblems here.'),
 ('1380','The <b>Dakṣiṇa Kailāsa Purāṇam</b> is compiled under the Jaffna kings.'),
 ('1468','<b>Aruṇakirinātar</b> praises the temple in his Tiruppukaḻ.')])
 +talk("Sinhala kings AND Tamil kings gave gifts here?","And Pāṇḍyas, Pallavas, a Kalinga king. The rock was holy to everyone who sailed past.")))
pages.append(page('history2','HISTORY · II','The fall: 1622–1624',fig(560,160,'Portuguese ships off the cliff firing cannon; the temple tower crumbling; priests carrying small bronze idols away',
 '<rect width="560" height="160" fill="#2a0805"/>'+SEA(120,560,40)+ROCK(260,124,1.1)+GOP(230,50,.7).replace('fill="#f2e6c8"','fill="#9a8a7a"').replace('fill="#e2cfa8"','fill="#7a6a5a"')
 +''.join(f'<g transform="translate({x} 122)" stroke="#111" stroke-width="2"><path d="M-30 0 h60 l-10 14 h-40z" fill="#6a4a2a"/><path d="M0 0 v-40" /><path d="M0 -38 h20 v20 h-20z" fill="#eee"/></g>' for x in (420,500))
 +'<path d="M400 112 L300 70" stroke="#ff8c1a" stroke-width="3" stroke-dasharray="6 4"/>'+person(60,134,'#e0a800','#c98b5a',.7)+person(96,134,'#e0a800','#c98b5a',.7)+'<circle cx="78" cy="124" r="5" fill="#c98b2a" stroke="#111"/>')+'''<div class="steps">
<div><b>A temple seen from the sea.</b> In <b>1613</b> a Jesuit, Manuel Barradas, described the temple as a massive granite structure on the headland.</div>
<div><b>14 April 1622.</b> On Tamil New Year’s Day, while the images were out in procession, troops of the Portuguese captain-general <b>Constantino de Sá de Noronha</b> attacked. Priests and pilgrims were killed and the shrines torn down; much was thrown into the sea.</div>
<div><b>1624.</b> The last structures fell. Their stones built <b>Fort Frederick</b> across the neck of the headland.</div>
<div><b>Saved.</b> Some images escaped, carried inland. They came to rest in the <b>Ati Koṇanāyakar</b> temple at <b>Tampalakāmam</b>, built in the 17th century to house them.</div>
</div>'''))
pages.append(page('history3','HISTORY · III','Three centuries of waiting, then revival',tl([
 ('1687','The Dutch re-erect a memorial pillar on the rock; a romantic “Lover’s Leap” tale later grows around it.'),
 ('1738','Dutch governor <b>van Imhoff</b> records visiting the ruined site.'),
 ('1870','The first photograph of the temple’s remains.'),
 ('1950','Digging a well near the site, the Trincomalee Urban Council finds <b>bronze images</b> of the old temple.'),
 ('1951','An annual three-day procession after Mahāśivarātri begins.'),
 ('1956–57','<b>Arthur C. Clarke</b> and Mike Wilson dive off the rock and find carved temple stones on the seabed.'),
 ('1963','On <b>3 March</b>, the rebuilt temple is consecrated with the recovered images.'),
 ('2003','The <b>Tēr</b> chariot festival returns after 379 years.'),
 ('2018','The great Śiva statue on the rock is rebuilt.')])
 +talk("The gods were under the sea for three hundred years?","Some of them. A science-fiction writer went diving and found pieces of a temple. Truth is stranger!")))
pages.append(page('sea','THE TEMPLE UNDER THE SEA','What the divers found',fig(560,200,'A diver underwater beside fallen carved temple stones and a stone lingam on the sea floor, fish swimming',
 '<rect width="560" height="200" fill="#1d6fa0"/>'+''.join(f'<path d="M{k*50} {20+(k%4)*8} q12 -6 24 0" stroke="#bfe6ff" stroke-width="2" fill="none"/>' for k in range(12))
 +'<path d="M0 200 Q140 170 280 184 T560 176 V200z" fill="#d9c79a"/>'+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="18" fill="#9a8a7a" stroke="#111" stroke-width="1.5" transform="rotate({r} {x} {y})"/>' for x,y,w,r in ((120,168,60,-8),(200,172,40,10),(380,166,70,4)))
 +'<path d="M300 176 v-22 a12 12 0 0 1 24 0 v22z" fill="#5a5a5a" stroke="#111"/><g transform="translate(220 90) rotate(-20)" stroke="#111" stroke-width="2"><ellipse rx="40" ry="12" fill="#222"/><circle cx="-44" r="12" fill="#ffd166"/><rect x="-10" y="-20" width="26" height="10" fill="#ff8c1a"/><path d="M40 0 l24 -8 l0 16z" fill="#222"/></g>'
 +''.join(f'<path d="M{x} {y} q10 -8 20 0 q-10 8 -20 0z M{x+20} {y} l8 -6 v12z" fill="#ffd166" stroke="#111"/>' for x,y in ((420,70),(470,100),(380,120))))+'''<div class="panel reading">
<p><b>The dive.</b> In 1956 the writer <b>Arthur C. Clarke</b> and photographer <b>Mike Wilson</b> dived beneath Swami Rock and found worked temple stones on the seabed, debris from 1622. Clarke told the story in <i>The Reefs of Taprobane</i> (1957).</p>
<p><b>On land.</b> Six years earlier, workmen digging a well had found bronze images of the old temple. Between the well and the sea, Koṇeśvaram got some of its past back.</p>
</div>'''))
pages.append(page('hymns','IN THE HYMNS','Sung for over a thousand years',fig(560,130,'A Tamil saint singing with cymbals, facing the cliff temple across the sea',
 '<rect width="560" height="130" fill="#fff4cd"/>'+person(110,100,'#ff8c1a','#c98b5a',1)+'<circle cx="86" cy="84" r="7" fill="#e0a800" stroke="#111"/><circle cx="134" cy="84" r="7" fill="#e0a800" stroke="#111"/>'+''.join(f'<text x="{170+k*30}" y="{60-k*6}" font-size="18">♪</text>' for k in range(4))+SEA(100,560,30).replace('x="0"','x="300"')+ROCK(470,104,.8)+GOP(450,36,.5))+facts([
 ('Tēvāram','<b>Campantar</b> (7th c.) and <b>Cuntarar</b> sing of Tirukoṇamalai: one of only two Śiva temples in Sri Lanka in the Tēvāram, with Kētīśvaram'),
 ('Tiruppukaḻ','<b>Aruṇakirinātar</b> (15th c.) praises the Lord of the hill'),
 ('Purāṇas','The <b>Dakṣiṇa Kailāsa Purāṇam</b> and the Dakṣiṇa Kailāsa Māṉmiyam tell the shrine’s legends'),
 ('Chronicles','The <b>Konesar Kalveṭṭu</b> and the <b>Tirukoṇācala Vaipavam</b> (written 1889, published 1952) record its history'),
 ('The hymn','<i>Laṅkāyāṃ śāṅkarī devī</i>: the line that puts the Goddess here among the eighteen')])))
pages.append(page('festivals','THROUGH THE YEAR','The temple’s festivals',facts([
 ('Tēr','A <b>22-day</b> festival with the great chariot, ending at the Tamil New Year in April, the very day of the 1622 attack'),
 ('Tīrttam','The sacred bath at the <b>Pāpanāśam</b> well'),
 ('Navarātri','Nine nights of the Goddess: Śāṅkarī’s own season'),
 ('Mahāśivarātri','Koṇeśvara’s great night, followed by a <b>three-day procession</b> held since 1951'),
 ('Tamil New Year','Remembered both as a feast and as the day of the temple’s fall')])
 +talk("They hold the chariot festival on the day the temple was destroyed?","And with that festival back since 2003, the day that ended it now belongs to it again.")+'<div class="key">The New Year procession, broken in 1622, <b>runs again</b>.</div>'))
pages.append(page('ishvarams','THE FIVE ĪŚVARAMS','Śiva’s ring around the island',fig(560,260,'Map of Sri Lanka marking the five ancient coastal Shiva temples',
 SLMAP([(8.58,81.23,'KOṆEŚVARAM','r','#c0392b'),(8.95,79.95,'KĒTĪŚVARAM','r','#1d4f9a'),(7.58,79.80,'MUNNĒŚVARAM','l','#1d4f9a'),(9.81,80.02,'NAKULĒŚVARAM','r','#1d4f9a'),(5.92,80.59,'TĒṈĀVARAM','l','#1d4f9a')],560,260))
 +facts([('Koṇeśvaram','Trincomalee, east coast: with Śāṅkarī’s pīṭha'),('Kētīśvaram','Mannar, north-west: also in the Tēvāram'),('Munnēśvaram','Chilaw, west coast'),('Nakulēśvaram','Kīrimalai, north tip'),('Tēṉāvaram','Dondra, the island’s southern point')])))
pages.append(page('around','AROUND THE ROCK','Places tied to the shrine',facts([
 ('Kanniya','The <b>seven hot wells</b> of the Rāvaṇa legend; protected as an archaeological site since 2011'),
 ('Tampalakāmam','The <b>Ati Koṇanāyakar</b> temple that sheltered the rescued images'),
 ('Kantalai','The great reservoir credited to Kulakkoṭṭaṉ, which once fed the temple’s lands'),
 ('Bhadrakāḷi','The <b>Bhadrakāḷi Ammaṉ</b> temple in Trincomalee town, another Śakti shrine'),
 ('Fort Frederick','The Portuguese fort built from the temple’s stones'),
 ('Nainativu','Nākapūśaṇi Ammaṉ, the rival claimant for Laṅkā’s pīṭha')])
 +talk("The fort is made of the temple?","Walk through its gate and some of the stones around you once stood in the temple.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Śāṅkarī','Consort of Śaṅkara (Śiva)'),('Koṇam / Koṇeśvara','The headland and its Lord'),('Dakṣiṇa Kailāsa','The Kailāsa of the South'),
 ('Tēvāram','The Tamil Śaiva hymns of the 7th–8th c. saints'),('Pāṭal peṟṟa sthalam','A temple sung in the Tēvāram'),('Kalveṭṭu','Stone inscription; here a verse chronicle'),
 ('Paraṅki','“Frank”: the Portuguese'),('Tēr','Temple chariot'),('Tīrttam','Sacred water; a sacred bath'),('Īśvaram','A Śiva temple, “of the Lord”')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Goddess.</b> Śāṅkarī Devī, first of the eighteen, “in Laṅkā”, where Satī’s groin is said to have fallen.</div>
<div><b>The place.</b> Swami Rock, Trincomalee: Koṇeśvaram, Dakṣiṇa Kailāsa, sung in the Tēvāram.</div>
<div><b>The legends.</b> Rāvaṇa’s sword-cleft, the hot wells of Kanniya, Kulakkoṭṭaṉ the builder.</div>
<div><b>The history.</b> Kings of every coast gave gifts; the Portuguese destroyed it in 1622–24; the images came back in 1950 and the temple in 1963.</div>
<div><b>The question.</b> Trincomalee or Nainativu: the hymn says only “Laṅkā”.</div>
</div>'''+talk("One line to remember?","A Goddess on a cliff above the ocean, torn down, rebuilt, and named first in the hymn.")+'<div class="key">The first seat of the Mother: <b>Śāṅkarī of Laṅkā</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple and history:</b> Wikipedia, “Koneswaram Temple”: Koṇeśvara and Mātumai; Swami Rock (about 120 m); Tirukoṇamalai in the Tēvāram; Rāvaṇaṉ Veṭṭu; Kulakkoṭṭaṉ and 432–440 CE; Konesar Kalveṭṭu and c. 1580 BCE; Kailāsa longitude; thousand-pillared hall (537–668); Vāyu Purāṇa (c. 300); Gajabāhu II; Codaganga 1223; Jaṭāvarman Vīra Pāṇḍya 1262; Dakṣiṇa Kailāsa Purāṇam 1380; Aruṇakirinātar 1468; Barradas 1613; 14 April 1622 and 1624; Ati Koṇanāyakar; Dutch pillar 1687; van Imhoff 1738; 1870 photograph; 1950 bronzes; 1951 procession; Clarke and Wilson 1956–57; 3 March 1963; Tēr revived 2003; statue 2018; Tēr, Tīrttam, Navarātri, Śivarātri. Wikipedia, “Kulakkottan”. Wikipedia, “Kanniya Hot Springs” (legend; protected 2011). Tamil Digital Library, “A Tamil Inscription from Fort Frederick” (the Paraṅki prophecy).</p>
<p><b>The pīṭha:</b> Wikipedia, “Shakta pithas” (groin; Laṅkā “historically undetermined”; Koṇeśvaram as a recent claim). Wikipedia, “Nainativu Nagapooshani Amman Temple” and its talk page (Nainativu claim; not named in the hymn). shubhpanchang.com and trawell.in (shrine within the complex; four-armed standing image).</p>
<p><b>Sources differ:</b> body part (groin or heart); Ati Koṇanāyakar date (1632 or 1639–89). <b>Not verified:</b> the year the present Śāṅkarī shrine was built (1952 is claimed); the lone pillar as her original site; the image’s description. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('goddess','The Goddess Today'),('konesvara','Koṇeśvara'),('ravana','Legend · Rāvaṇa'),('kulakkottan','Legend · The Builder'),('whichlanka','Which Laṅkā?'),
 ('history1','History · To 1468'),('history2','History · The Fall'),('history3','History · The Revival'),('sea','The Temple under the Sea'),('hymns','In the Hymns'),('festivals','Through the Year'),('ishvarams','The Five Īśvarams'),('around','Around the Rock'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 1 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚĀṄKARĪ DEVĪ</h1>
  <div class="series">LAṄKĀ · TRINCOMALEE · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess on the cliff above the sea</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>The hymn of the eighteen Śakti Pīṭhas begins far from India, on an island: <i>laṅkāyāṃ śāṅkarī devī</i>.</p>
    <p>Pilgrims find her on <b>Swami Rock</b> at Trincomalee, beside the ancient Śiva temple of <b>Koṇeśvaram</b>: sung by the Tēvāram saints, torn down by the Portuguese, and rebuilt from images found in a well.</p>
    <p>This guide tells her story, the temple’s, and the open question of which Laṅkā the hymn meant.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā Śāṅkarī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is she the most famous of the eighteen?","Among the least visited! But she comes first in the hymn, so she comes first here.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Shankari.html','w').write(head+b+tail())
print('ok',len(pages))
