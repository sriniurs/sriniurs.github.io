import sys; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
head=make_head('Himavad Gopālasvāmi Beṭṭa · Veṇugopāla · Temples around Mysuru · srini.presents',
 'Himavad Gopālasvāmi Beṭṭa: Kṛṣṇa as Veṇugopāla on the misty summit of Bandipur. Agastya’s penance, the crow that became a swan, Dakṣiṇa Govardhanagiri, and the car drawn with forest creepers. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def HILL(x,y,w,h,c='#3a6a3a'):
    return f'<path d="M{x-w/2} {y} Q{x-w/4} {y-h*0.6} {x-w/10} {y-h} Q{x} {y-h*1.06} {x+w/10} {y-h} Q{x+w/4} {y-h*0.6} {x+w/2} {y}z" fill="{c}" stroke="#111" stroke-width="2"/>'
def TEMPLE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="#f2e6c8"/><rect x="-8" y="-24" width="16" height="8" fill="#e2cfa8"/><path d="M-8 -24 l8 -14 l8 14z" fill="#e2cfa8"/><circle cy="-40" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def MIST(x,y,w,o=.75): return f'<g fill="#fff" opacity="{o}"><ellipse cx="{x}" cy="{y}" rx="{w}" ry="{w/5}"/><ellipse cx="{x+w*.5}" cy="{y-8}" rx="{w*.6}" ry="{w/6}"/></g>'
def VENU(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-6 70 l-6 -50 h24 l-4 50" fill="#ffd60a"/><path d="M-12 20 l18 52" stroke="#3b6fd0" stroke-width="7"/><path d="M8 20 l-14 52" stroke="#3b6fd0" stroke-width="7"/>'
     '<path d="M-16 22 q16 -12 32 0 v-34 q-16 -8 -32 0z" fill="#3b6fd0"/><path d="M-16 -8 q-14 -6 -20 -20 M16 -8 q14 -6 22 -22" stroke="#3b6fd0" stroke-width="7" fill="none"/>'
     '<path d="M-40 -30 l70 -6" stroke="#7a5a2a" stroke-width="4"/>'
     '<circle cy="-24" r="12" fill="#3b6fd0"/><path d="M-10 -34 h20 l-3 -10 h-14z" fill="#e0a800"/><path d="M4 -48 q10 -16 18 -2" fill="none" stroke="#2e9a5a" stroke-width="3"/><circle cx="20" cy="-50" r="4" fill="#1d6fb8"/>'
     '<path d="M-16 4 q16 10 32 0" fill="none" stroke="#c0392b" stroke-width="3"/></g>')
def COW(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cy="-20" rx="26" ry="14" fill="#fff"/><circle cx="-26" cy="-28" r="9" fill="#fff"/><path d="M-30 -36 l-4 -6 M-22 -36 l4 -6"/><rect x="-18" y="-8" width="5" height="10" fill="#fff"/><rect x="12" y="-8" width="5" height="10" fill="#fff"/><circle cx="6" cy="-24" r="5" fill="#8a5a3a" stroke="none"/></g>'
def BIRD(x,y,s=1,c='#222',swan=False):
    if swan: return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-20 0 q20 14 40 0 q-6 -16 -24 -10 q-4 -14 4 -24 q-10 -4 -12 8 q-2 10 4 20 q-10 -2 -12 6z" fill="#fff"/><path d="M-6 -36 l-6 2" stroke="#e0a800" stroke-width="3"/></g>'
    return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse rx="18" ry="10" fill="{c}"/><circle cx="-16" cy="-8" r="7" fill="{c}"/><path d="M-22 -8 l-8 2 l8 2" fill="#555"/><path d="M14 0 l14 -4 l-2 8z" fill="{c}"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Krishna playing the flute above a forested hill wrapped in mist, with a small temple on the summit">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/><circle cx="300" cy="60" r="44" fill="#ffd166" opacity=".3"/>'
 +HILL(160,268,320,170)+TEMPLE(160,104,1.3)+MIST(90,170,70)+MIST(220,200,80,.6)+VENU(300,150,1.3)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','Kṛṣṇa as <b>Gopālasvāmi</b>, <b>Veṇugopāla</b>: playing the flute beneath a tree, about 6 ft tall'),
 ('With him','<b>Rukmiṇī</b> and <b>Satyabhāmā</b>, companions, cows and cowherds'),
 ('Place','The summit of <b>Gopālasvāmi Beṭṭa</b>, Gundlupet taluk, Chamarajanagar district, Karnataka'),
 ('Height','About <b>1,450 m</b>: the highest peak of <b>Bandipur National Park</b>'),
 ('Name','<b>Himavad</b>, for the mist that covers the hill most of the year; <b>Gopālasvāmi</b>, the Lord; <b>beṭṭa</b>, hill'),
 ('Old names','<b>Dakṣiṇa Govardhanagiri</b>, the southern Govardhana, and <b>Kamalācala</b>'),
 ('Sage','<b>Agastya</b> did penance here; tradition says he installed the Lord'),
 ('Built','<b>1315</b>, attributed to a <b>Ballāḷa</b> king (see History)'),
 ('Waters','<b>Haṃsa Tīrtha</b>, the swan lake, among some <b>77</b> sacred tanks'),
 ('Great festival','The <b>Brahma Rathotsava</b>, the car pulled with <b>forest creepers</b> instead of ropes')])
 +talk("A temple in the middle of a tiger reserve?","Right in the core of Bandipur! The Lord lives with tigers, elephants and mist. The forest gets to keep its peace too.")))
mapfig=fig(560,240,'Schematic map: Gopalaswamy Betta inside Bandipur National Park, with Gundlupet to the north and Mysuru further north-east; the road to the Nilgiris passing nearby. Not to scale.',
 '<rect width="560" height="240" fill="#eef6e4"/><path d="M60 60 C 140 20, 440 30, 520 90 C 540 170, 420 230, 250 228 C 90 226, 30 150, 60 60z" fill="#cfe6bf" stroke="#2e6a2e" stroke-width="3" stroke-dasharray="8 5"/>'
 +T(400,210,'BANDIPUR NATIONAL PARK',11,'#2e6a2e')+HILL(240,160,170,90)+TEMPLE(240,78,.7)+MIST(200,120,40)+T(240,180,'GOPĀLASVĀMI BEṬṬA',11,'#0d3f73')
 +'<circle cx="300" cy="20" r="6" fill="#e0a800" stroke="#111"/>'+T(312,24,'GUNDLUPET',10,'#0d3f73','start')+'<path d="M460 10 l8 -6 l8 6" fill="none" stroke="#111" stroke-width="2"/>'+T(486,14,'to MYSURU',10,'#555','start')
 +'<path d="M300 26 C 330 100, 380 160, 420 240" stroke="#8a7a6a" stroke-width="4" stroke-dasharray="10 6" fill="none"/>'+T(440,236,'to the Nilgiris',9,'#555','start')+T(110,236,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','The highest hill of Bandipur',mapfig+'''<div class="panel reading">
<p><b>The hill.</b> Gopālasvāmi Beṭṭa rises to about <b>1,450 m</b> in the south of Karnataka, near Gundlupet. It is the highest peak in <b>Bandipur National Park</b>, and the temple sits in the park’s core.</p>
<p><b>The mist.</b> Dense fog wraps the hill for much of the year, which is why it is called <b>Himavad</b>, the misty one.</p>
<p><b>The forest.</b> The slopes are thick with forest, home to tigers and leopards; the grassy tops draw elephants, deer and gaur.</p>
</div>'''))
deity=fig(560,240,'Krishna standing under a tree playing the flute, one foot crossed over the other, flanked by Rukmini and Satyabhama, with cows and cowherd boys to the right',
 '<rect width="560" height="240" fill="#dcecff"/><circle cx="250" cy="50" r="60" fill="#5a9a4a" stroke="#111" stroke-width="2"/><rect x="244" y="90" width="12" height="40" fill="#7a5a2a" stroke="#111"/>'
 +VENU(250,150,1.3)+''.join(f'<g transform="translate({x} 170)" stroke="#111" stroke-width="2"><circle cy="-34" r="11" fill="#f2c79b"/><path d="M-9 -45 h18 l-3 -10 h-12z" fill="#ffd60a"/><path d="M-20 46 q20 -76 40 0z" fill="{c}"/></g>' for x,c in ((130,'#e05a8a'),(370,'#2e9a5a')))
 +COW(470,214,.9)+COW(520,190,.7)+person(450,160,'#ffd60a','#c98b5a',.6)
 +T(250,234,'VEṆUGOPĀLA',12,'#0d3f73')+T(130,234,'RUKMIṆĪ',11,'#c0392b')+T(370,234,'SATYABHĀMĀ',11,'#2e9a5a'))
pages.append(page('deity','THE LORD WITH THE FLUTE','Gopālasvāmi, Veṇugopāla',deity+'''<div class="g2">
<div class="card bg-blue"><h4>🎶 The image</h4><p>About <b>6 ft</b> tall, Kṛṣṇa plays the flute beneath a tree, in a dancing pose with his <b>left big toe resting on the right</b>. The temple faces <b>north</b>.</p></div>
<div class="card bg-yellow"><h4>🐄 The panel</h4><p>Around him the back panel shows the tree, his friends, his consorts <b>Rukmiṇī</b> and <b>Satyabhāmā</b>, and <b>cows and cowherds</b> on the right side.</p></div>
</div>
<div class="panel reading"><p><b>Gopāla.</b> <i>Go</i> is cow, <i>pāla</i> protector: the cowherd Kṛṣṇa of Vṛndāvana, and <b>Veṇu</b> is his flute. On this hill he stands as he stood among the cows of Gokula.</p></div>'''))
pages.append(page('names','A HILL OF MANY NAMES','Himavad, Govardhana, Kamalācala',facts([
 ('Himavad','From the mist that covers the hill most of the year'),
 ('Gopālasvāmi','The Lord of the hill: Kṛṣṇa the cowherd'),
 ('Beṭṭa','Kannada for hill'),
 ('Dakṣiṇa Govardhanagiri','“The southern Govardhana”: the hill of the cowherd god'),
 ('Kamalācala','“Lotus hill”, another old name'),
 ('Haṃsa Tīrtha','“The swan lake”, a name for the place and for its sacred tank')])
 +'''<div class="panel reading"><p><b>Why Govardhana?</b> When Indra sent storms to drown Gokula, the boy Kṛṣṇa lifted Mount <b>Govardhana</b> on his finger and sheltered the cowherds and their cows beneath it for seven days. A cowherd’s god on a cloud-wrapped hill: the old name fits.</p></div>'''
 +talk("Did he lift this hill too?","No, that was Govardhana near Mathurā! This one is its southern namesake. But with all this mist, you'd want a hill-umbrella too.")))
leg1=fig(560,190,'Sage Agastya seated in deep meditation on the misty summit; Vishnu appears above in blessing',
 '<rect width="560" height="190" fill="#e8f0fa"/>'+HILL(280,190,520,110,'#5a8a4a')+MIST(120,110,70)+MIST(420,100,80)
 +person(280,128,'#ff8c1a','#c98b5a',1)+'<path d="M260 66 q20 -24 40 0" fill="#fff" stroke="#111"/><circle cx="280" cy="76" r="4" fill="#111"/>'
 +'<g transform="translate(430 60)" stroke="#111" stroke-width="2"><circle r="30" fill="#ffd60a" opacity=".5"/><circle cy="-4" r="11" fill="#3b6fd0"/><path d="M-9 -14 h18 l-3 -10 h-12z" fill="#e0a800"/><path d="M-14 30 q14 -30 28 0z" fill="#ffd60a"/></g>'
 +T(280,184,'AGASTYA',12,'#0d3f73'))
pages.append(page('legends1','THE LEGENDS · I','Agastya’s penance',leg1+'''<div class="steps">
<div><b>The sage of the south.</b> <b>Agastya</b> is the great sage of South India in the Purāṇas: the one who crossed the Vindhyas and brought the Vedic tradition south.</div>
<div><b>His penance.</b> Tradition says Agastya performed intense penance on this hill.</div>
<div><b>The promise.</b> Pleased, Viṣṇu blessed the place and promised to stay here. Temple tradition says Agastya himself installed the Lord as Gopālasvāmi.</div>
<div><b>A place of penance.</b> Because sages worshipped and meditated here, the place came to be called <b>Haṃsa Tīrtha</b>: the swan stands for knowledge, calm and liberation.</div>
</div>'''))
leg2=fig(560,190,'A black crow dipping into a small pond and rising out as a white swan; no crows anywhere on the hill',
 '<rect width="560" height="190" fill="#fffbe8"/><ellipse cx="280" cy="140" rx="160" ry="34" fill="#4aa3df" stroke="#111" stroke-width="2"/>'
 +BIRD(130,70,1.4)+'<path d="M170 80 q40 30 80 50" stroke="#111" stroke-width="2" stroke-dasharray="6 5" fill="none"/>'
 +'<path d="M300 130 q40 -40 90 -60" stroke="#111" stroke-width="2" stroke-dasharray="6 5" fill="none"/>'+BIRD(430,70,1.5,swan=True)
 +T(130,40,'A CROW',12)+T(430,30,'A SWAN',12,'#0d3f73')+T(280,182,'HAṂSA TĪRTHA',12,'#0d3f73'))
pages.append(page('legends2','THE LEGENDS · II','The crow that became a swan',leg2+'''<div class="steps">
<div><b>The bath.</b> The story goes that a crow bathed in one of the hill’s sacred tanks and rose out of it a <b>swan</b>.</div>
<div><b>The name.</b> From then on the tank was called <b>Haṃsa Tīrtha</b>, the swan’s pool.</div>
<div><b>No crows.</b> Devotees say that to this day no crows are seen on the hill.</div>
<div><b>77 tīrthas.</b> Tradition counts about <b>77</b> sacred tanks and springs in and around the hill temple.</div>
</div>'''+talk("A crow turns into a swan just by bathing?","That's the point of a tīrtha: it purifies. The crow is ordinary us; the swan is who we can become.")))
pages.append(page('drip','THE WATER THAT NEVER STOPS','A blessing from above the door',fig(560,160,'Water dripping steadily from above the sanctum door; a priest sprinkling it on devotees',
 '<rect width="560" height="160" fill="#f6f1e2"/><rect x="230" y="20" width="100" height="130" fill="#5a3a1a" stroke="#111" stroke-width="2"/><rect x="220" y="12" width="120" height="14" fill="#c9a26b" stroke="#111"/>'
 +''.join(f'<path d="M{x} {y} q3 6 0 9 q-3 -3 0 -9z" fill="#4aa3df"/>' for x,y in ((250,34),(280,50),(310,40),(266,74),(296,90)))
 +person(400,150,'#fff','#c98b5a',.8)+''.join(person(x,154,c,'#c98b5a',.6) for x,c in ((470,'#e05a8a'),(510,'#3b6fd0'))))+'''<div class="panel reading">
<p><b>A year-round drip.</b> Water drips from above the door of the sanctum through the year, said to be cold and constant even in the dry months.</p>
<p><b>Shared as prasāda.</b> The priest sprinkles this water on devotees while telling the legends of the hill.</p>
<p><b>Mist made visible.</b> On a hill wrapped in fog for most of the year, the Lord’s own doorway seems to gather the mist and give it back as blessing.</p>
</div>'''))
pages.append(page('history','HISTORY','Seven centuries on the hill',tl([
 ('Legend','Agastya’s penance; the Lord promises to stay.'),
 ('1315','The temple is built. Sources disagree on the builder: most name a king <b>Ballāḷa</b>, called a <b>Hoysaḷa</b> (Vīra Ballāḷa) in some accounts and a local <b>Cōḻa Ballāḷa of Terakaṇāmbi</b> in others.'),
 ('14th c. on','The temple stands on the hill through Vijayanagara and later times.'),
 ('Woḍeyars','The Woḍeyars of Mysuru, devotees of Veṇugopāla, take a keen interest in maintaining the hill temple.'),
 ('20th c.','The hill falls within <b>Bandipur</b>, later a tiger reserve: the temple becomes a sanctuary within a sanctuary.')])
 +'''<div class="panel reading"><p><b>Which Ballāḷa?</b> The Hoysaḷa king Vīra Ballāḷa III ruled the region in the early 1300s, so the Hoysaḷa reading fits the date. The “Cōḻa Ballāḷa” of Terakaṇāmbi, a nearby old town, may be a local ruler of the same name. We show both.</p></div>'''))
plan=fig(560,220,'Simplified plan: north-facing temple with a single-tiered gateway on the compound wall, the inner porch with flag-pillar and altar, a parapet carved with the ten avatars, and the sanctum with its tower',
 '<rect width="560" height="220" fill="#f6f1e2"/><rect x="140" y="20" width="280" height="180" fill="none" stroke="#7a5a2a" stroke-width="4"/>'
 +'<rect x="250" y="12" width="60" height="18" fill="#e2cfa8" stroke="#111"/>'+T(280,10,'GOPURAM (north)',9)
 +'<rect x="270" y="46" width="20" height="10" fill="#e0a800" stroke="#111"/>'+T(310,56,'FLAG-PILLAR · ALTAR',9,'#555','start')
 +'<rect x="210" y="70" width="140" height="44" fill="#fff" stroke="#111"/>'+''.join(f'<circle cx="{222+i*13}" cy="78" r="4" fill="#e0a800" stroke="#111"/>' for i in range(10))+T(280,104,'MUKHA MAṆḌAPA · DAŚĀVATĀRA',8)
 +'<rect x="240" y="124" width="80" height="60" fill="#0d3f73" stroke="#111"/>'+T(280,160,'SANCTUM',10,'#fff')
 +T(470,210,'simplified, not to scale',9,'#555'))
pages.append(page('temple','THE TEMPLE','Small, old and north-facing',plan+'''<div class="g2">
<div class="card bg-yellow"><h4>🏯 The gateway</h4><p>A <b>single-tiered gopuram</b> rests on the compound wall. Inside, the porch holds a <b>dhvajastambha</b> (flag-pillar) and a <b>bali-pīṭha</b> (altar).</p></div>
<div class="card bg-blue"><h4>🔟 Ten avatars</h4><p>The parapet of the porch is carved with the <b>Daśāvatāra</b>, Viṣṇu’s ten avatars, with <b>Kṛṣṇa</b> at the centre. A śikhara rises over the sanctum.</p></div>
</div>
<div class="panel reading"><p><b>Style.</b> A compact Dravidian-style shrine, built to stand on an exposed, misty summit.</p></div>'''))
fest=fig(560,170,'A temple chariot pulled by devotees using long green forest creepers instead of ropes',
 '<rect width="560" height="170" fill="#e8f5e2"/><g transform="translate(400 150)" stroke="#111" stroke-width="2"><circle cx="-24" cy="-8" r="10" fill="#7a5a2a"/><circle cx="24" cy="-8" r="10" fill="#7a5a2a"/><rect x="-34" y="-40" width="68" height="24" fill="#a0522d"/><path d="M-40 -40 h80 l-40 -64z" fill="#2e9a5a"/><path d="M-34 -40 q34 12 68 0" fill="none" stroke="#ffd60a" stroke-width="3"/></g>'
 +'<path d="M366 140 C 300 120, 200 160, 40 136" stroke="#3a8a2a" stroke-width="5" fill="none"/>'+''.join(f'<path d="M{x} {128+(x%3)*4} l6 -8 l4 8z" fill="#5aba4a" stroke="#111" stroke-width="1"/>' for x in range(60,350,26))
 +crowd(['#fff','#ffd60a','#ff8c1a','#3b6fd0','#e05a8a'],60,40,160,.5))
pages.append(page('festivals','FESTIVALS','The car drawn with creepers',fest+facts([
 ('Brahma Rathotsava','The annual car festival in <b>Phālguna</b> (around March); the chariot is pulled not with ropes but with <b>creepers gathered from the forest</b>'),
 ('Śrāvaṇa Saturdays','Special pūjās every Saturday in the month of Śrāvaṇa, drawing thousands of devotees'),
 ('Jātre','A fair held with the festival')])
 +talk("Why creepers and not ropes?","Because the forest is part of the family here! Bamboo creepers from Bandipur pull the Lord's chariot. Nice touch, no?")))
pages.append(page('forest','A TEMPLE IN A TIGER RESERVE','Where the Lord shares his hill',facts([
 ('Bandipur','The hill lies in the core of Bandipur National Park, under Project Tiger'),
 ('Wildlife','Tigers, leopards and wild dogs; elephants, gaur, chital and sambar; peacocks and forest birds'),
 ('Trees','Rosewood, teak and other forest trees on the slopes'),
 ('Protection','Under the Wildlife (Protection) Act, the forest beyond the temple is protected: no trekking or wandering')])
 +'''<div class="panel reading"><p><b>A sanctuary within a sanctuary.</b> Few great temples stand inside a tiger reserve. Here devotion and conservation share the same summit: the Lord on the hill, and the forest kept for the animals around him.</p>
<p>Read more about the tigers of this forest in our story <a href="/bandipur-tigers/">Bandipur’s tigers</a>.</p></div>'''
 +talk("So the Lord protects the cows and the forest protects the tigers?","Exactly. Gopāla is the protector. Here he gets to protect everybody!")))
pages.append(page('around','AROUND THE HILL','Gundlupet and the Mysuru temples',facts([
 ('Gundlupet','The taluk town at the edge of the forest, below the hill'),
 ('Bandipur','The national park all around, part of the Nilgiri Biosphere Reserve'),
 ('Nañjanagūḍu','Śiva as Nañjuṇḍeśvara on the Kapilā, on the way back toward Mysuru')])
 +'''<div class="panel reading"><p>More temples around Mysuru: <a href="/bhakti/temples-of-india/around-mysuru/nanjangud/">Nañjanagūḍu</a>, <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga</a> and <a href="/bhakti/temples-of-india/triranga/madhya-ranga/">Madhya Raṅga</a>.</p></div>'''))
glossary=[('Himavad','misty, wrapped in fog'),('Gopālasvāmi','“Lord Gopāla”, Kṛṣṇa the cowherd'),('Veṇugopāla','Kṛṣṇa with the flute'),('Beṭṭa','Kannada for hill'),('Govardhana','the hill Kṛṣṇa lifted to shelter Gokula'),('Kamalācala','“lotus hill”'),('Haṃsa','swan'),('Tīrtha','a sacred pool, tank or river'),('Prabhāvalī','the carved back panel behind an image'),('Dhvajastambha','flag-pillar'),('Bali-pīṭha','altar for offerings'),('Daśāvatāra','the ten avatars of Viṣṇu'),('Śikhara','tower over a sanctum'),('Rathotsava','chariot festival'),('Śrāvaṇa','the monsoon month, July–August')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','GOPĀLASVĀMI BEṬṬA ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Lord.</b> Kṛṣṇa as Veṇugopāla: flute in hand, under a tree, toe over toe, with Rukmiṇī, Satyabhāmā and the cows.</div>
<div><b>The place.</b> The misty summit of Bandipur, about 1,450 m: Himavad, Dakṣiṇa Govardhanagiri, Kamalācala.</div>
<div><b>The legends.</b> Agastya’s penance and the Lord’s promise; the crow that became a swan at Haṃsa Tīrtha; 77 sacred tanks.</div>
<div><b>The history.</b> Built in 1315 under a king Ballāḷa; cared for by the Woḍeyars of Mysuru.</div>
<div><b>The festival.</b> The Brahma Rathotsava, the car drawn with forest creepers; Saturdays of Śrāvaṇa.</div>
</div>'''+talk("One line to remember?","Up in the clouds, inside the tiger forest, the cowherd plays his flute. Mist, music and a crow-free hill.")+'<div class="key">The misty hill of the cowherd: <b>Gopāla in the clouds</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Hill and temple:</b> Wikipedia, “Himavad Gopalaswamy Betta”: name and meaning; Gundlupet taluk, Chamarajanagar; 1,450 m; highest peak of Bandipur, in the core area; 1315 and the Hoysaḷa era; the “Chola” builder; the Woḍeyars; Kṛṣṇa with the flute under a tree, the left toe on the right, Rukmiṇī and Satyabhāmā; the single-tiered gopuram, dhvajastambha, Daśāvatāra parapet and śikhara; Agastya; Haṃsa Tīrtha; the wildlife and the Wildlife Act.</p>
<p><b>Temple site:</b> himavadgopalaswamy.org.in: South Govardhanagiri and Kamalācala; Agastya’s installation; 6 ft image; the prabhāvalī with cows and cowherds; north-facing; the crow-to-swan legend and no crows; the dripping water; the Brahma Rathotsava in Phālguna with creepers; Śrāvaṇa Saturdays.</p>
<p><b>Other:</b> Anudinam (about 77 tīrthas; creepers; Project Tiger; birds and trees); CPREEC Eco-heritage (“Chola Ballala of Terakanambi”); Rural Tourism, Govt of India (14th century, Agastya). Govardhana and Agastya stories, and Vīra Ballāḷa III, are general knowledge.</p>
<p><b>Sources differ:</b> the builder (Hoysaḷa Vīra Ballāḷa or a local Cōḻa Ballāḷa of Terakaṇāmbi); the height (about 1,450 m, with other figures in some sources).</p>
<p><b>Not verified:</b> the count of 77 tīrthas; the “no crows” belief (devotional tradition). Maps and plans are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('deity','The Lord with the Flute'),('names','A Hill of Many Names'),('legends1','Legends · Agastya'),('legends2','Legends · The Crow and the Swan'),('drip','The Water That Never Stops'),('history','History'),('temple','The Temple'),('festivals','Festivals'),('forest','A Temple in a Tiger Reserve'),('around','Around the Hill'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,6.6vw,72px)">GOPĀLASVĀMI BEṬṬA</h1>
  <div class="series">HIMAVAD VEṆUGOPĀLA · BANDIPUR · A REFERENCE GUIDE</div>
  <div class="tag">The cowherd in the clouds</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>In the heart of Bandipur, above the teak and the tigers, one hill wears the clouds like a shawl for most of the year.</p>
    <p>On its summit, in a small old temple, <b>Kṛṣṇa</b> stands under a tree playing his flute, his cows beside him. This is <b>Himavad Gopālasvāmi Beṭṭa</b>, the misty hill of the cowherd Lord.</p>
    <p>This guide tells its names, its legends and its story.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hare Kṛṣṇa,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A temple inside the clouds?","Most of the year, yes! The mist is so constant that it's part of the hill's name.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Gopalaswamy_Betta.html','w').write(head+b+tail())
print('ok')
