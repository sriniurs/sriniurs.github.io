import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
import common_t
def head_navy(title,desc):
    h=open(common_t.SRC).read(); hd=h[:h.find('<div class="book">')]
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
head=head_navy('Mudukutore · Mallikārjuna · Temples around Mysuru · srini.presents',
 'Mudukutore Mallikārjuna on Somagiri hill by the Kāverī: Abhinava Śrīśaila, the fifth of Talakāḍu’s Pañcaliṅgas. Arjuna’s jasmine, the cow’s footprint, Bhramarāmbā and the bee, and the great cattle fair. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def HILL(x,y,w,h,c='#8a9a6a'):
    return f'<path d="M{x-w/2} {y} Q{x-w/4} {y-h*0.6} {x-w/10} {y-h} Q{x} {y-h*1.06} {x+w/10} {y-h} Q{x+w/4} {y-h*0.6} {x+w/2} {y}z" fill="{c}" stroke="#111" stroke-width="2"/>'
def TEMPLE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="#f2e6c8"/><path d="M-14 -16 h28 l-4 -10 h-20z M-10 -26 h20 l-4 -10 h-12z" fill="#e2cfa8"/><circle cy="-40" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def LINGA(x,y,s=1,hoof=False):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 0 h60 l-6 -10 h-48z" fill="#8a8a8a"/><path d="M20 -6 h18 l-3 5 h-15z" fill="#8a8a8a"/><path d="M-12 -10 v-26 a12 12 0 0 1 24 0 v26z" fill="#3a3a3a"/>'
    g+= '<path d="M-5 -40 q-3 6 0 10 q3 -2 3 -5z M5 -40 q3 6 0 10 q-3 -2 -3 -5z" fill="#c9a26b"/>' if hoof else '<path d="M-8 -30 h16 M-8 -26 h16 M-8 -22 h16" stroke="#fff" stroke-width="2"/>'
    return g+'</g>'
def COW(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cy="-20" rx="26" ry="14" fill="#fff"/><circle cx="-26" cy="-28" r="9" fill="#fff"/><path d="M-30 -36 l-4 -6 M-22 -36 l4 -6"/><rect x="-18" y="-8" width="5" height="10" fill="#fff"/><rect x="12" y="-8" width="5" height="10" fill="#fff"/><circle cx="6" cy="-24" r="5" fill="#8a5a3a" stroke="none"/><path d="M-4 -8 q4 6 8 0" fill="#f4b8c8"/></g>'
def JASMINE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+''.join(f'<circle cx="{a}" cy="{b}" r="5" fill="#fff" stroke="#999"/>' for a,b in ((0,0),(8,4),(-8,4),(4,-7),(-4,-7)))+'<circle r="2.4" fill="#ffd60a"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A small hill on a bend of the Kaveri with a temple on top; jasmine flowers and a linga in front">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/><circle cx="300" cy="60" r="30" fill="#ffd166" opacity=".35"/>'
 '<path d="M0 220 C 120 200, 160 268, 260 240 S 360 210, 380 220 V268 H0z" fill="#4aa3df"/>'+HILL(170,236,240,130)+TEMPLE(170,110,1.3)
 +''.join(f'<path d="M{150+i*6} {236-i*18} h14" stroke="#e2cfa8" stroke-width="3"/>' for i in range(6))+LINGA(310,170,1.2)+JASMINE(290,120,1.3)+JASMINE(330,110,1.1)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','Śiva as <b>Mallikārjuna</b> (Mallikārjuneśvara), a <b>liṅga</b> facing east, said to bear a <b>cow’s footprint</b>'),
 ('Goddess','<b>Bhramarāmbā</b> (Bhramarāmbikā), in her own shrine beside him'),
 ('Place','Somagiri hill above the <b>Kāverī</b> at <b>Mudukutore</b> (T. Beṭṭahaḷḷi), T. Narasipura taluk, Mysuru district'),
 ('Title','<b>Abhinava Śrīśaila</b>, “the new Śrīśaila”'),
 ('Pañcaliṅga','The <b>fifth</b> of the five liṅgas of the Talakāḍu Pañcaliṅga Darśana'),
 ('Legends','Arjuna’s jasmine worship; the cow and the hidden liṅga; Bhramarāmbā the bee'),
 ('Builders','Begun by the <b>Gaṅgas</b>, over 800 years ago by tradition; enlarged under Vijayanagara and the Woḍeyars'),
 ('Fair','A week-long <b>fair</b> in January–February, with a big trade in cattle and farm produce')])
 +talk("Another Mallikārjuna? Isn't that at Śrīśaila?","Same Lord, same Goddess! That's why this hill is called the new Śrīśaila.")))
mapfig=fig(560,220,'Schematic map: the Kaveri making a sharp turn at Mudukutore, with Somagiri hill and the temple on top, and Talakadu with its sand dunes a little downstream. Not to scale.',
 '<rect width="560" height="220" fill="#eef6e4"/><path d="M0 60 C 160 50, 230 70, 260 120 C 290 170, 380 180, 560 150" fill="none" stroke="#4aa3df" stroke-width="20"/>'
 +HILL(200,170,140,90)+TEMPLE(200,86,.7)+T(200,190,'SOMAGIRI · MUDUKUTORE',11,'#0b2a4a')
 +'<path d="M380 110 Q440 80 500 100 Q520 120 480 130 Q420 140 380 110z" fill="#e8d29a" stroke="#b89a5a"/>'+T(450,74,'TALAKĀḌU',11,'#7a5a2a')
 +'<path d="M250 120 a16 16 0 1 1 10 20" stroke="#111" stroke-width="2" fill="none"/><path d="M262 140 l-2 -10 l8 4z" fill="#111"/>'+T(310,214,'the river turns',10,'#1d6fb8')+T(80,214,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','Where the river turns',mapfig+'''<div class="panel reading">
<p><b>The hill.</b> The temple crowns <b>Somagiri</b>, a small hill about 200 ft high on the bank of the Kāverī, near Talakāḍu. Steps and a road lead up to it.</p>
<p><b>The name.</b> Here the river makes a turn and flows on: <i>muduku</i>, a turning aside, and <i>tore</i>, flowing on. <b>Mudukutore</b> is the river’s own signature.</p>
<p><b>The village.</b> In government records the village is <b>T. Beṭṭahaḷḷi</b> (Tirumalakūḍu Beṭṭahaḷḷi); Mudukutore is the older, sacred name.</p>
</div>'''))
leg1=fig(560,180,'Arjuna with his bow, seated before a linga on the hilltop, offering heaps of white jasmine flowers',
 '<rect width="560" height="180" fill="#fff4dc"/>'+HILL(280,180,520,80)+LINGA(320,124,1.4)+''.join(JASMINE(x,y,1) for x,y in ((290,124),(352,124),(320,80),(300,96),(340,96)))
 +person(200,140,'#3b6fd0','#c98b5a',1)+'<path d="M176 60 q-20 40 0 80" stroke="#7a5a2a" stroke-width="4" fill="none"/><path d="M176 60 v80" stroke="#555"/>'+T(200,172,'ARJUNA',11,'#0b2a4a'))
pages.append(page('legends1','THE LEGENDS · I','Arjuna’s jasmine',leg1+'''<div class="steps">
<div><b>An exile’s halt.</b> During the Pāṇḍavas’ exile in the Mahābhārata, tradition says <b>Arjuna</b> stayed for a time on this hill.</div>
<div><b>Jasmine for Śiva.</b> He installed (some tellings say carved) a liṅga of Śiva on the summit and worshipped it with <b>mallikā</b>, jasmine flowers.</div>
<div><b>The name.</b> <i>Mallikā</i> plus <i>Arjuna</i>: the Lord became <b>Mallikārjuna</b>, “Arjuna’s jasmine Lord”.</div>
</div>'''+talk("Is that also why Śrīśaila's Lord is Mallikārjuna?","Śrīśaila has its own stories of the name. Here, the jasmine and Arjuna make it local!")))
leg2=fig(560,180,'A cow standing on a mound on the hilltop letting her milk flow onto it; the angry cowherd with a stick; then the linga revealed with a hoof mark on top',
 '<rect width="560" height="180" fill="#e8f5e2"/><path d="M120 150 q40 -30 80 0z" fill="#b89a5a" stroke="#111"/>'+COW(160,130,1)+''.join(f'<circle cx="{160+i*4}" cy="{132+i*4}" r="2" fill="#fff"/>' for i in range(3))
 +person(260,160,'#ffd60a','#8a5a3a',.9)+'<path d="M278 100 l30 -30" stroke="#7a5a2a" stroke-width="3"/>'
 +'<path d="M330 90 h40" stroke="#111" stroke-width="2"/><path d="M370 84 l10 6 l-10 6z" fill="#111"/>'+LINGA(450,150,1.8,hoof=True)+T(450,172,'THE COW’S HOOF MARK',10,'#0b2a4a'))
pages.append(page('legends2','THE LEGENDS · II','The cow and the hidden liṅga',leg2+'''<div class="steps">
<div><b>A dry cow.</b> A cowherd of Mudukutore found his cow gave no milk at home. He followed her up Somagiri, and saw her emptying her udder every day onto a mound on the hilltop.</div>
<div><b>The whip.</b> Angry, he struck her. The cow leapt, and one hoof landed on the mound, breaking it open.</div>
<div><b>The liṅga.</b> Beneath lay a <b>liṅga</b>, self-born. The mark of the cow’s hoof, devotees say, can still be seen on it.</div>
</div>'''+talk("Cows keep finding liṅgas in these stories!","Many temples tell it! A cow pours her milk on the hidden Lord and shows the people where He is.")))
leg3=fig(560,180,'Sage Kapila travelling south with a linga; the Goddess as a great golden bee confronting a many-eyed demon',
 '<rect width="560" height="180" fill="#fdf3e8"/>'+person(110,170,'#ff8c1a','#c98b5a',1)+LINGA(110,96,.6)+T(110,176,'KAPILA',10,'#0b2a4a')
 +'<g transform="translate(330 90)" stroke="#111" stroke-width="2"><ellipse rx="30" ry="18" fill="#e0a800"/><path d="M-20 -6 v12 M-6 -10 v20 M8 -10 v20" stroke="#111" stroke-width="4"/><ellipse cx="-6" cy="-28" rx="18" ry="10" fill="#dff" opacity=".8"/><ellipse cx="10" cy="-28" rx="18" ry="10" fill="#dff" opacity=".8"/><circle cx="34" cy="-4" r="9" fill="#2b2b2b"/></g>'
 +'<g transform="translate(480 160)" stroke="#111" stroke-width="2"><circle cy="-50" r="20" fill="#3a5a2a"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="3" fill="#ffd60a"/>' for a,b in ((-8,-56),(8,-56),(0,-46),(-12,-44),(12,-44),(0,-60)))+'<path d="M-26 20 q26 -70 52 0z" fill="#2b2b2b"/></g>'+T(480,176,'SAHASRĀKṢA',10,'#2b2b2b'))
pages.append(page('legends3','THE LEGENDS · III','Kapila, and Bhramarāmbā the bee',leg3+'''<div class="steps">
<div><b>Kapila’s liṅga.</b> The temple priests tell another story: that the sage <b>Kapila</b>, travelling south in ancient times, installed the liṅga here.</div>
<div><b>The Goddess.</b> Beside Mallikārjuna stands the shrine of his consort, <b>Bhramarāmbā</b>.</div>
<div><b>The bee.</b> She is believed to have taken the form of a <b>bhramara</b>, a great bee, to destroy a demon named <b>Sahasrākṣa</b>, “the thousand-eyed”. So she is Bhramarāmbā, the Bee-Mother.</div>
<div><b>Abhinava Śrīśaila.</b> Mallikārjuna and Bhramarāmbā are the same divine pair worshipped at <a href="/bhakti/temples-of-india/12-jyotirlingas/mallikarjuna/">Śrīśaila</a>, the jyotirliṅga. So this hill is called the new Śrīśaila.</div>
</div>'''))
plan=fig(560,200,'Simplified plan: steps rising up the hill to a three-tiered gateway, then flag-pillar, Nandi and altar, the sanctum with its halls, and the Goddess shrine behind',
 '<rect width="560" height="200" fill="#f6f1e2"/>'+''.join(f'<rect x="{40+i*14}" y="{170-i*12}" width="14" height="{30+i*12}" fill="#e2cfa8" stroke="#7a5a2a"/>' for i in range(8))+T(90,196,'STEPS',9)
 +'<rect x="170" y="70" width="40" height="80" fill="#e2cfa8" stroke="#111" stroke-width="2"/><path d="M174 70 h32 l-4 -14 h-24z M178 56 h24 l-3 -12 h-18z M182 44 h16 l-3 -10 h-10z" fill="#d9c9a0" stroke="#111"/>'+T(190,164,'GOPURA',9)
 +'<rect x="234" y="100" width="8" height="40" fill="#e0a800" stroke="#111"/><ellipse cx="270" cy="128" rx="14" ry="8" fill="#bbb" stroke="#111"/>'+T(256,164,'FLAG · NANDI',9)
 +'<rect x="300" y="80" width="140" height="70" fill="#fff" stroke="#111"/><rect x="400" y="94" width="36" height="42" fill="#0b2a4a" stroke="#111"/>'+T(350,120,'MAHĀ · ARDHA MAṆḌAPA',8)+T(418,164,'SANCTUM',9,'#0b2a4a')
 +'<rect x="460" y="94" width="60" height="42" fill="#fdecea" stroke="#111"/>'+T(490,120,'BHRAMARĀMBĀ',8,'#c0392b')+T(500,24,'simplified, not to scale',9,'#555','end'))
pages.append(page('temple','THE TEMPLE','Up the steps of Somagiri',plan+'''<div class="g2">
<div class="card bg-blue"><h4>🛕 The shrine</h4><p>East-facing, with a <b>three-tiered rājagopura</b>, then the flag-pillar, Nandi and altar facing the sanctum, which has an ardha- and mahā-maṇḍapa.</p></div>
<div class="card bg-yellow"><h4>🪜 The climb</h4><p>An arch at the foot of the hill shows Śiva on Nandi between Gaṇeśa and Subrahmaṇya. Accounts count from about 40 to 100 steps to the top.</p></div>
</div>
<div class="panel reading"><p><b>Other shrines:</b> the festival images, Gaṇeśa, Subrahmaṇya and Bhairava; and, down a small path, the village Goddess <b>Beṭṭaḷi Māramma</b>.</p></div>'''))
pages.append(page('pancalinga','THE FIFTH LIṄGA','Mudukutore and the Pañcaliṅga Darśana',fig(560,110,'Five lingas in a row, the last one highlighted on its hill',
 '<rect width="560" height="110" fill="#eef3fa"/>'+''.join(LINGA(70+i*105,92,1)+T(70+i*105,108,n,9,'#0b2a4a') for i,n in enumerate(('VAIDYEŚVARA','PĀTĀLEŚVARA','MARAḶEŚVARA','ARKEŚVARA','MALLIKĀRJUNA')))+'<rect x="440" y="20" width="110" height="88" fill="none" stroke="#e0a800" stroke-width="4" rx="8"/>')+'''<div class="panel reading">
<p><b>One of five.</b> Mudukutore’s Mallikārjuna is the fifth of the <b>Pañcaliṅgas</b> of Talakāḍu, held to be the five faces of Śiva. One account names him as the <b>Vāmadeva</b> face.</p>
<p><b>The Darśana.</b> On the rare day of the <b>Pañcaliṅga Darśana</b> in Kārtika, pilgrims visit all five in one auspicious window: the three in the Talakāḍu dunes, Arkeśvara at Vijayapura, and finally this hill.</p>
<p>Full story: <a href="/bhakti/temples-of-india/around-mysuru/talakadu/">Talakāḍu ➜</a></p>
</div>'''+talk("So you can't finish the Pañcaliṅga without climbing this hill?","Exactly. Four in the sand, one on the hill. The last climb is the sweetest.")))
pages.append(page('history','HISTORY','From the Gaṅgas to a rebuilding',tl([
 ('Legend','Arjuna’s jasmine; Kapila’s liṅga; the cow on the hill.'),
 ('Gaṅga period','The temple is said to have been built by the <b>Gaṅgas</b> of Talakāḍu, over 800 years ago.'),
 ('Vijayanagara','The temple is developed further by the Vijayanagara kings.'),
 ('Woḍeyars','<b>Mummaḍi Kṛṣṇarāja Woḍeyar</b> is credited with the main entrance and the mukha-maṇḍapa.'),
 ('2020','Called dilapidated, the temple and its Goddess shrine are taken up for rebuilding: the Chief Minister lays the foundation stone in November, with ₹16 crore for a first phase.')])
 +'<div class="panel reading small"><p><b>Note.</b> The history comes mainly from tradition and from remarks at the 2020 ceremony; we found no dated inscription. Excavations nearby are reported to have found remains about 800 years old.</p></div>'))
fair=fig(560,170,'A busy village fair at the foot of the hill: decorated bullocks with painted horns, stalls of grain and vegetables, and a temple chariot',
 '<rect width="560" height="170" fill="#ffe9c4"/>'+HILL(460,170,200,110)+TEMPLE(460,64,.6)
 +''.join(f'<g transform="translate({x} 150)" stroke="#111" stroke-width="2"><ellipse cy="-20" rx="26" ry="14" fill="#e8e0d0"/><circle cx="-26" cy="-28" r="9" fill="#e8e0d0"/><path d="M-32 -36 q-4 -10 2 -12 M-20 -36 q4 -10 -2 -12" stroke="{c}" stroke-width="4" fill="none"/></g>' for x,c in ((70,'#c0392b'),(150,'#3b6fd0'),(230,'#2e9a5a')))
 +''.join(f'<rect x="{x}" y="120" width="40" height="30" fill="#f2e6c8" stroke="#111"/><path d="M{x-4} 120 l24 -14 l24 14z" fill="{c}" stroke="#111"/>' for x,c in ((280,'#e05a8a'),(330,'#ffd60a'))))
pages.append(page('fair','THE GREAT FAIR','Bullocks, grain and the Lord',fair+'''<div class="panel reading">
<p><b>When.</b> Every year in <b>January–February</b>, a big fair is held at Mudukutore for about a week.</p>
<p><b>What.</b> Farmers bring <b>cattle</b> and <b>farm produce</b> to trade, and thousands of visitors come for the Lord, the fair and the river.</p>
<p><b>Old Karnataka.</b> Temple fairs like this have long been the great markets of the Kāverī villages: a festival for the god, and the year’s biggest bazaar for the farmer.</p>
<p><b>Sources differ.</b> Most describe it as annual; one source calls the great Mudukutore jātre a 12-yearly event.</p>
</div>'''))
pages.append(page('around','AROUND MUDUKUTORE','The Kāverī temple trail',facts([
 ('Talakāḍu','The buried city of the other four Pañcaliṅgas, Vaidyeśvara and Kīrtinārāyaṇa'),
 ('Somanāthapura','The Hoysaḷa Keśava temple of 1268'),
 ('T. Narasipura','The saṅgama of the Kāverī and Kapilā, Tirumakūḍalu')])
 +'''<div class="panel reading"><p>More temples around Mysuru: <a href="/bhakti/temples-of-india/around-mysuru/talakadu/">Talakāḍu</a> · <a href="/bhakti/temples-of-india/around-mysuru/nanjangud/">Nañjanagūḍu</a> · <a href="/bhakti/temples-of-india/around-mysuru/">the full series</a>.</p></div>'''))
glossary=[('Mudukutore','“where the river turns and flows on”'),('Somagiri','the hill of the temple'),('Mallikā','jasmine'),('Mallikārjuna','“Arjuna’s jasmine Lord”'),('Bhramara','a large bee'),('Bhramarāmbā','the Bee-Mother, Śiva’s consort here'),('Sahasrākṣa','“thousand-eyed”, the demon'),('Abhinava Śrīśaila','“the new Śrīśaila”'),('Svayambhū','self-born'),('Pañcaliṅga','the five liṅgas of Talakāḍu'),('Rājagopura','main gateway tower'),('Jātre','temple fair')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','MUDUKUTORE ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Lord.</b> Mallikārjuna, with Bhramarāmbā: Abhinava Śrīśaila on Somagiri hill.</div>
<div><b>The place.</b> Where the Kāverī turns and flows on, near Talakāḍu.</div>
<div><b>The legends.</b> Arjuna’s jasmine; the cow’s hoof on the hidden liṅga; Kapila; the bee and the thousand-eyed demon.</div>
<div><b>The Pañcaliṅga.</b> The fifth and last liṅga of the Talakāḍu Darśana.</div>
<div><b>The fair.</b> A week of cattle, grain and devotion every January–February.</div>
</div>'''+talk("One line to remember?","Climb the steps where the river turns, and meet Śrīśaila's Lord, wearing Arjuna's jasmine.")+'<div class="key">The new Śrīśaila: <b>jasmine, a cow’s hoof, and a river’s turn</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Place and legend:</b> Wikipedia, “Mudukuthore”: T. Beṭṭahaḷḷi; Somagiri; the meaning of the name; Arjuna and the mallikā flowers; the January–February fair; one of the five Pañcaliṅgas. Hindu Temples of India (blog): the cow and the hoof-marked liṅga; the temple layout, 200-ft hill, about 100 steps, three-tiered gopura, shrines, Bhramarāmbikā. Deccan Herald, “Destinations along Cauvery”: 35–40 steps; Kapila; Bhramarāmbā, the bee and Sahasrākṣa; “a stream with a twist”.</p>
<p><b>History:</b> The Hans India, November 2020: Gaṅga builders, over 800 years; Vijayanagara; Mummaḍi Kṛṣṇarāja Woḍeyar’s entrance and mukha-maṇḍapa; Abhinava Śrīśaila; the rebuilding (₹16 crore first phase); finds about 800 years old. The Hans India, December 2020: Vāmadeva face.</p>
<p><b>Sources differ:</b> the number of steps; annual or 12-yearly great fair; who installed the liṅga (Arjuna, Kapila, or self-born). <b>Not verified:</b> no dated inscription found; the status of the 2020 rebuilding today. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('legends1','Legends · Arjuna’s Jasmine'),('legends2','Legends · The Cow'),('legends3','Legends · Kapila and the Bee'),('temple','The Temple'),('pancalinga','The Fifth Liṅga'),('history','History'),('fair','The Great Fair'),('around','Around Mudukutore'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.2vw,78px)">MUDUKUTORE</h1>
  <div class="series">MALLIKĀRJUNA · ABHINAVA ŚRĪŚAILA · A REFERENCE GUIDE</div>
  <div class="tag">Where the river turns, and Arjuna brought jasmine</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Just upstream of Talakāḍu, the Kāverī makes a sharp turn around a small hill. On top sits a temple of Śiva as <b>Mallikārjuna</b>, with his Goddess <b>Bhramarāmbā</b>: the same pair as at the great Śrīśaila.</p>
    <p>Devotees call it <b>Abhinava Śrīśaila</b>, and it is the last of the five liṅgas of the Pañcaliṅga Darśana.</p>
    <p>This guide tells its legends, its temple and its fair.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Oṃ Namaḥ Śivāya,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A small hill with a big name?","Small hill, three legends, one famous fair, and a starring role in the Pañcaliṅga. Not bad!")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Mudukutore.html','w').write(head+b+tail())
print('ok')
