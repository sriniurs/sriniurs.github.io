exec(open('/home/claude/work/shakti/common_s.py').read())
head=make_head('Ahobilam · The Nine Narasiṃhas · srini.presents',
 'Ahobilam in the Nallamala hills: where Narasiṃha burst from the pillar for Prahlāda. The Ugra Stambha, the nine Narasiṃha shrines, Garuḍa’s penance, Cheñcu Lakṣmī and the forest wedding, the Prahlādavarada temple, the Ahobila Maṭha and the history from the Kākatīyas to Vijayanagara. An illustrated reference guide.')
def ah(lat,lon): return 40+(lon-77.9)*400, 20+(16.3-lat)*180
def AHMAP(marks,w=560,h=280):
    g=''
    for la,lo,t,side,col in marks:
        x,y=ah(la,lo); r=8 if col=='#1d4f9a' else 6
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',t,12,'#111','start' if side=='r' else 'end')
    hills=''.join(f'<path d="M{x} {y} l18 -26 l18 26z" fill="#4a8a4a" stroke="#111" stroke-width="1"/>' for x,y in ((300,250),(330,236),(360,262),(400,240),(420,200),(390,170),(430,140),(450,110),(470,90)))
    return (f'<rect width="{w}" height="{h}" fill="#e7f0d8"/>'+hills+f'<path d="M0 {ah(16.0,0)[1]:.0f} Q200 {ah(16.15,0)[1]:.0f} {ah(16.07,78.6)[0]:.0f} {ah(16.07,78.6)[1]:.0f} T{w} {ah(16.25,0)[1]:.0f}" stroke="#4aa3df" stroke-width="7" fill="none"/>'
     +T(60,ah(16.05,0)[1]-10,'KṚṢṆĀ',11,'#1d4f9a','start')+T(500,250,'NALLAMALA',12,'#2e5a2e','end')+g+T(w-10,h-8,'simplified, not to scale',10,'#555','end'))
def NARA(x,y,s=1,c='#ffb84d'): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 60 q-4 -60 30 -70 q34 10 30 70z" fill="#ffd60a"/>'
 f'<circle cy="-24" r="22" fill="#e08a2a"/><circle cy="-20" r="15" fill="{c}"/><circle cx="-6" cy="-24" r="2.6" fill="#111"/><circle cx="6" cy="-24" r="2.6" fill="#111"/><path d="M-8 -12 q8 6 16 0" fill="#c0392b"/><path d="M-4 -8 l-2 6 M4 -8 l2 6" stroke="#fff" stroke-width="2"/>'
 '<path d="M-14 -46 h28 l-4 -14 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/><path d="M-26 0 l-26 -14 M26 0 l26 -14" stroke="#ffb84d" stroke-width="7"/><circle cx="-54" cy="-18" r="7" fill="#fff" stroke="#111"/><path d="M50 -24 a8 8 0 1 1 0 .1z" fill="#ffd60a"/></g>')
def PILLAR(x,y,s=1,broken=False): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-14" y="-120" width="28" height="120" fill="#d8d0c0"/>'+''.join(f'<path d="M-14 {-20-k*20} h28" />' for k in range(5))+('<path d="M-14 -70 l10 8 l-6 10 l12 6 l12 -12" fill="none" stroke-width="3"/>' if broken else '')+'</g>'
def KING(x,y,s=1,c='#5a2a6a'): return f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,c,'#5a8a3a',1)+'<path d="M-12 -40 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800" stroke="#111" stroke-width="1.5"/></g>'
def ROCKCLEFT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-80 0 L-60 -140 L-12 -170 L-8 0z" fill="#8a7a6a"/><path d="M8 0 L12 -176 L60 -150 L80 0z" fill="#7a6a5a"/></g>'
CHENCHU=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,'#2a9d6f','#8a5a3a',1)+'<path d="M-10 -44 q10 -14 20 0" fill="#2b1a0e" stroke="#111"/><path d="M8 -46 l6 -12" stroke="#ff8c1a" stroke-width="3"/><path d="M-20 -6 l-12 -20" stroke="#7a5a2a" stroke-width="3"/><path d="M-34 -30 q10 4 4 14" fill="none" stroke="#7a5a2a" stroke-width="2"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The man-lion Narasimha bursting from a stone pillar in a forest gorge, a split rock peak behind him, the boy Prahlada with folded hands">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/>'+ROCKCLEFT(190,268,1.2)+'<circle cx="190" cy="120" r="70" fill="#ffd166" opacity=".45"/>'+PILLAR(110,250,1.1,True)+NARA(200,150,1.6)+person(320,240,'#ffd60a','#f2c79b',1)+'<path d="M312 196 l8 -8 l8 8" stroke="#f2c79b" stroke-width="4" fill="none"/></svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','<b>Narasiṃha</b>, Viṣṇu as man-lion, in <b>nine</b> forms: the Nava Narasiṃha'),
 ('Where','<b>Ahobilam</b>, Nandyal district, Andhra Pradesh, in the <b>Nallamala</b> forest of the Eastern Ghats'),
 ('Two levels','<b>Lower Ahobilam</b> (Prahlādavarada temple) and <b>Upper Ahobilam</b>, about 8 km up a forest ravine'),
 ('The legend','Here, tradition says, Narasiṃha burst from a pillar to kill <b>Hiraṇyakaśipu</b> and save <b>Prahlāda</b>'),
 ('The pillar','<b>Ugra Stambha</b>, a split rock peak high above the shrines'),
 ('Consorts','<b>Lakṣmī</b> (Amṛtavallī) and <b>Cheñcu Lakṣmī</b>, the forest girl he married'),
 ('Divya Deśam','Sung by <b>Tirumaṅgai Āḻvār</b> in the 9th century: one of the 108 Viṣṇu shrines'),
 ('Maṭha','Home of the <b>Ahobila Maṭha</b>, a great Śrī Vaiṣṇava institution'),
 ('Festival','The <b>Phālguna Brahmotsavam</b>, and the <b>Paruveṭa</b>, the Lord’s forest wedding tour')])
 +talk("Nine Narasiṃhas in one forest?","Nine shrines, nine moods: fierce, calm, in yoga, with Lakṣmī, under a tree. Ahobilam is all of him.")))
pages.append(page('where','WHERE IT IS','In the Nallamala hills',fig(560,280,'Simplified map of the Nallamala region: Ahobilam in blue in the hills south of Nandyal, Mahanandi nearby, Kurnool to the west and Srisailam to the north on the Krishna',
 AHMAP([(15.13,78.72,'AHOBILAM','r','#1d4f9a'),(15.48,78.48,'Nandyal','l','#bbb'),(15.47,78.62,'Mahānandi','r','#bbb'),(15.83,78.04,'Kurnool','r','#bbb'),(16.07,78.87,'Śrīśailam','r','#ffd166')]))+'''<div class="panel reading">
<p><b>The forest.</b> Ahobilam lies in the <b>Nallamala</b> hills, a wild stretch of the Eastern Ghats full of gorges, streams and caves, home of the forest-dwelling <b>Cheñcu</b> people.</p>
<p><b>Two Ahobilams.</b> <b>Lower Ahobilam</b> (Diguva, “below”) is the village with the great Prahlādavarada temple. <b>Upper Ahobilam</b> (Eguva, “above”) is about 8 km up the ravine, with the oldest shrine and the trails to the others.</p>
<p><b>Neighbours.</b> <a href="/bhakti/temples-of-india/12-jyotirlingas/mallikarjuna/">Śrīśailam</a> lies north in the same hills; an old record measures Ahobilam’s distance from it.</p>
</div>'''))
pages.append(page('names','THE NAMES','Strength, and a cave',facts([
 ('Aho balam!','“Oh, what strength!”: what the gods cried when they saw Narasiṃha kill Hiraṇyakaśipu'),
 ('Aho bilam!','“Oh, what a cave!”: the great cave where <b>Garuḍa</b> saw the Lord'),
 ('Garuḍādri','“Garuḍa’s hill”, for his penance, and because the peaks look like Garuḍa'),
 ('Vedādri','“Hill of the Vedas”, another name of the range'),
 ('Siṅgavēḷ Kuṉṟam','The Tamil name: “the hill of the lion”'),
 ('Diguva / Eguva','Telugu for Lower and Upper Ahobilam')])
 +'<div class="panel reading small"><p>A verse sung by pilgrims: <i>aho vīryam aho śauryam aho bāhuparākramaḥ | nārasiṃhaṃ paraṃ daivam ahobilam aho balam</i>: “Oh his valour, his courage, the might of his arms! Narasiṃha is the highest God: Ahobilam, oh what strength!”</p></div>'
 +talk("Strength or cave: which is right?","Both, in one cry. Aho-bala, aho-bila. The place is a pun the gods made.")))
pages.append(page('legend','THE LEGEND','Prahlāda and the pillar',fig(560,200,'A demon king striking a pillar with his mace in a palace hall at dusk; the man-lion bursting out; the boy Prahlada with folded hands',
 '<rect width="560" height="200" fill="#2a1a3a"/><rect y="170" width="560" height="30" fill="#5a4a3a"/>'+KING(110,170,1.3)+'<path d="M140 110 L200 80" stroke="#7a5a2a" stroke-width="6"/><circle cx="202" cy="78" r="9" fill="#bbb" stroke="#111"/>'
 +PILLAR(260,170,1.2,True)+'<circle cx="300" cy="90" r="60" fill="#ffd166" opacity=".4"/>'+NARA(310,110,1.1)+person(470,170,'#ffd60a','#f2c79b',1)+'<path d="M462 128 l8 -8 l8 8" stroke="#f2c79b" stroke-width="4" fill="none"/>'+T(470,186,'PRAHLĀDA',11,'#ffd166'))+'''<div class="steps">
<div><b>The boon.</b> The demon king <b>Hiraṇyakaśipu</b> won a boon: no man or beast could kill him, not by day or night, not inside or outside, not on earth or in the sky, by no weapon.</div>
<div><b>The son.</b> His little son <b>Prahlāda</b> worshipped Viṣṇu anyway. Torture could not stop him. “Is your Viṣṇu in this pillar too?” the king roared, and struck it.</div>
<div><b>The man-lion.</b> From the pillar burst <b>Narasiṃha</b>, neither man nor beast. At dusk, on the threshold, holding the demon on his lap, he tore him apart with his claws: every condition of the boon kept, and broken.</div>
<div><b>Here.</b> The Bhāgavata tells the story; Ahobilam’s tradition says it happened in these hills.</div>
</div>'''))
pages.append(page('stambha','THE UGRA STAMBHA','The split rock',fig(560,220,'A tall rock peak split down the middle by a narrow cleft, high above forest, with a small saffron flag at the top',
 '<rect width="560" height="220" fill="#cfe3f5"/>'+HILL(120,220,240,120,'#3a7a3a')+HILL(460,220,240,110,'#4a8a4a')+ROCKCLEFT(280,214,1.15)+'<path d="M290 14 v-10"/><path d="M290 6 l14 5 l-14 5z" fill="#ff8c1a" stroke="#111"/>'+T(430,40,'UGRA STAMBHA',13,'#0d3f73'))+'''<div class="panel reading">
<p><b>The pillar.</b> High above Upper Ahobilam, a great rock peak is split into two by a narrow cleft. Pilgrims call it the <b>Ugra Stambha</b>, “the fierce pillar”: the pillar from which Narasiṃha emerged.</p>
<p><b>The climb.</b> It is a steep, rough climb beyond the Jvālā Narasiṃha shrine, done by the hardy few.</p>
<p><b>Prahlāda Meṭṭu.</b> Between the stambha and Upper Ahobilam, a small cave shrine on the hillside is dedicated to <b>Prahlāda</b>, the boy whose faith brought the Lord out of stone.</p>
</div>'''+talk("A mountain is the pillar?","When God steps out of a pillar, the pillar has to be the size of a mountain.")))
nine=[('Ahobila (Ugra)','Upper Ahobilam','The main and oldest shrine: fierce, seated, self-manifest, in a cave; Cheñcu Lakṣmī has a shrine here'),
 ('Kroḍa (Varāha)','Near Upper Ahobilam','A boar-faced Narasiṃha with Lakṣmī'),
 ('Mālola','About 2 km from Upper','Gentle, with Lakṣmī: “dear to Mā”; its festival image travels with the Ahobila Maṭha’s Jīyar'),
 ('Jvālā','Higher up, on Acalachāya Meru','The fiery moment of the killing; a pool nearby is where he washed his bloodied hands'),
 ('Kārañja','About 1 km from Upper','Under a karañja tree; also called Śāraṅga'),
 ('Bhārgava','About 2 km from Lower','By the Bhārgava tīrtha, where Paraśurāma did penance; up long steps'),
 ('Yogānanda','About 2 km from Lower','In yogic posture: here he taught Prahlāda yoga'),
 ('Chatravaṭa','About 3–4 km from Lower','Under a peepal tree that shades him like an umbrella'),
 ('Pāvana','About 6–7 km from Upper','On the Pāvana stream: gracious, purifying, and the hardest to reach')]
pages.append(page('nava','THE NINE NARASIṂHAS','Jvālā, Ahobila, Mālola…','<table class="ct"><tr><th>Narasiṃha</th><th>Where</th><th>What to know</th></tr>'+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a,b,c in nine)+'</table>'
 +'<div class="panel reading small"><p>A verse lists them: <i>jvālāhobila-mālola-kroḍa-kārañja-bhārgavāḥ | yogānanda-kṣatravaṭa-pāvanā nava mūrtayaḥ</i>. Distances are rough, along forest paths.</p></div>'))
def mini(lbl,inner): return f'<div class="card bg-blue" style="text-align:center"><svg width="150" height="110" viewBox="0 0 150 110" role="img" aria-label="{lbl}"><rect width="150" height="110" fill="#eef3fa"/>{inner}</svg><h4>{lbl}</h4></div>'
pages.append(page('moods','NINE MOODS','How the nine differ','<div class="g2">'
 +mini('Ugra: fierce','<g transform="translate(75 70) scale(.6)">'+NARA(0,0,1)+'</g>')
 +mini('Jvālā: blazing','<path d="M30 100 q-10 -50 20 -80 q4 30 16 34 q6 -40 30 -50 q-10 40 6 56 q10 -14 6 -30 q20 30 -6 70z" fill="#ff8c1a" stroke="#111"/><g transform="translate(75 74) scale(.5)">'+NARA(0,0,1)+'</g>')
 +mini('Mālola: with Lakṣmī','<g transform="translate(55 74) scale(.5)">'+NARA(0,0,1)+'</g>'+GENTLE(105,64,.45).replace('#e05a8a','#c0392b'))
 +mini('Yogānanda: in yoga','<g transform="translate(75 72) scale(.55)">'+NARA(0,0,1)+'</g><path d="M40 100 q35 -16 70 0" stroke="#ffd60a" stroke-width="8" fill="none"/>')
 +'</div>'+'<div class="panel reading"><p><b>Ugra and Saumya.</b> The nine run from <b>fierce</b> (Ahobila, Jvālā) to <b>gentle</b> (Mālola, Pāvana) and <b>meditative</b> (Yogānanda). The Prahlādavarada temple below, built last, shows him <b>calm</b>, granting boons to the boy: the story’s whole arc, laid out across a forest.</p></div>'))
pages.append(page('garuda','THE LEGEND · GARUḌA','The eagle’s penance',fig(560,170,'The eagle Garuda meditating on a rock in the hills; the man-lion appearing in a blaze inside a cave',
 '<rect width="560" height="170" fill="#e6eef8"/>'+HILL(160,170,280,120,'#3a7a3a')+'<g transform="translate(160 70)" stroke="#111" stroke-width="2"><path d="M-40 0 q40 -30 80 0 q-40 -10 -80 0z" fill="#c0392b"/><circle cy="-14" r="12" fill="#e0a800"/><path d="M-6 -14 l-8 4 l8 2z" fill="#ffd60a"/><path d="M-10 0 v30 h20 v-30" fill="#3b6fd0"/></g>'
 +'<ellipse cx="420" cy="110" rx="90" ry="56" fill="#2a1a0a"/><circle cx="420" cy="100" r="44" fill="#ffd166" opacity=".6"/>'+NARA(420,110,.6))+'''<div class="steps">
<div><b>A wish.</b> <b>Garuḍa</b>, Viṣṇu’s eagle, longed to see the Lord in his Narasiṃha form. His father, the sage Kaśyapa, sent him to these hills to do penance.</div>
<div><b>The vision.</b> After long austerity, Narasiṃha appeared to him in a great cave, the <b>aho-bila</b>. The hills became <b>Garuḍādri</b>.</div>
<div><b>Nine forms.</b> The local account says that the Lord then took his nine forms in these hills, for Garuḍa and for the sages who followed, Paraśurāma among them.</div>
</div>'''))
pages.append(page('chenchu','CHEÑCU LAKṢMĪ','The forest wedding',fig(560,180,'Narasimha meeting a forest girl with a bow in the jungle; later the pair seated together as bride and groom',
 '<rect width="560" height="180" fill="#e7f0d8"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="26" fill="#3a8a3a"/>' for x,y in ((40,40),(100,26),(500,30),(540,60)))+NARA(170,110,1.0)+CHENCHU(290,170,1.1)
 +'<path d="M340 90 h40" stroke="#111" stroke-width="3"/><path d="M380 90 l-10 -6 v12z" fill="#111"/>'+NARA(430,110,.7)+CHENCHU(490,170,.8)+'<path d="M420 160 q35 -20 70 0" stroke="#e0a800" stroke-width="4" fill="none"/>')+'''<div class="steps">
<div><b>Still blazing.</b> After the killing, the story goes, Narasiṃha wandered the Nallamala forest, still in his terrible form. The gods asked Lakṣmī to calm him.</div>
<div><b>The forest girl.</b> She was born among the <b>Cheñcus</b>, the forest people, as <b>Cheñcu Lakṣmī</b>. The Lord saw her, fell in love, and asked to marry her; some say he refused ever to leave.</div>
<div><b>In-laws.</b> The Cheñcus still treat Narasiṃha as their <b>son-in-law</b> and Cheñcu Lakṣmī as their daughter. Pillars in both temples show the pair.</div>
<div><b>In a play.</b> The seventh Jīyar of the Ahobila Maṭha wrote a Sanskrit drama of the wedding, the <b>Vāsantikā Pariṇayam</b>, in the 16th century.</div>
</div>'''))
pages.append(page('lower','THE PRAHLĀDAVARADA TEMPLE','Lower Ahobilam',fig(560,180,'A large Vijayanagara temple with a seven-tiered gateway tower, three enclosing walls, carved pillared halls and a tall victory pillar in front',
 '<rect width="560" height="180" fill="#fdf1e8"/><rect x="60" y="80" width="440" height="90" fill="#efe4cc" stroke="#111" stroke-width="2"/><rect x="110" y="96" width="340" height="70" fill="#e8dcc0" stroke="#111" stroke-width="2"/>'
 +f'<g transform="translate(150 170) scale(.9)" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-34+k*3} {-k*12} h{68-k*6} l-1 -12 h{-(66-k*6)}z" fill="{"#f2e6c8" if k%2 else "#e2cfa8"}"/>' for k in range(7))+'</g>'
 +TEMPLE(360,150,1.6,'#dfe8f5')+'<rect x="36" y="40" width="10" height="130" fill="#d8d0c0" stroke="#111"/>'+T(40,32,'JAYA',9,'#555')+T(40,22,'STAMBHA',9,'#555'))+facts([
 ('Deity','<b>Prahlādavarada</b> Lakṣmī-Narasiṃha: “the boon-giver to Prahlāda”, the calm form; Goddess <b>Amṛtavallī</b>'),
 ('Built','Mostly <b>16th century</b>, possibly begun under Sāḷuva Narasiṃha (15th c.); Reḍḍi beginnings are also claimed'),
 ('Plan','Three enclosures, an east-facing seven-tiered gopura, a victory pillar (<b>jayastambha</b>) in front'),
 ('Carving','Pillared halls full of Vijayanagara sculpture: musicians, dancers, Rāma, Narasiṃha with Cheñcu Lakṣmī, and a figure of Narasa Nāyaka'),
 ('Not one of the nine','Built after the Āḻvār’s time, it is counted apart from the Nava Narasiṃhas')])))
pages.append(page('history','HISTORY','Kings of the man-lion',tl([
 ('9th c.','<b>Tirumaṅgai Āḻvār</b> sings of Ahobilam in the Periya Tirumoḻi: it becomes a Divya Deśam.'),
 ('12th–16th c.','Sanskrit and Telugu works mention the shrines.'),
 ('13th–14th c.','<b>Kākatīya</b> and <b>Reḍḍi</b> kings patronise the hills.'),
 ('15th c.','The <b>Sāḷuvas</b>; Prahlādavarada may be begun under Sāḷuva Narasiṃha Rāya.'),
 ('16th c.','The <b>Tuluvas</b>: most inscriptions date from now; <b>Kṛṣṇadevarāya</b> visits and gives gifts.'),
 ('1579','A Golconda commander, <b>Murahari Rao</b>, raids Ahobilam; the jewelled image is carried off.'),
 ('After','With Vijayanagara gone, royal patronage fades; the Ahobila Maṭha keeps worship alive.')])
 +'<div class="panel reading small"><p>Old copper-plate records once kept near the Cheñcu Lakṣmī shrine are said to have been destroyed for their metal: a loss for history.</p></div>'))
pages.append(page('matha','THE AHOBILA MAṬHA','Carrying Mālola across India',fig(560,150,'A saffron-robed ascetic carrying a small golden image of Narasimha with Lakshmi in a palanquin, walking along a road',
 '<rect width="560" height="150" fill="#fff4cd"/><path d="M0 130 Q280 110 560 130" stroke="#c9a26b" stroke-width="10" fill="none"/>'+person(200,124,'#ff8c1a','#c98b5a',1.1)+'<path d="M260 70 h120" stroke="#7a5a2a" stroke-width="5"/><rect x="300" y="44" width="40" height="26" fill="#c0392b" stroke="#111"/><path d="M296 44 h48 l-24 -16z" fill="#e0a800" stroke="#111"/>'+person(420,124,'#fff','#c98b5a',.9))+'''<div class="steps">
<div><b>The founder.</b> The maṭha traces itself to <b>Ādivaṇ Śaṭhakopa Jīyar</b>, a Vaḍakalai Śrī Vaiṣṇava teacher of the <b>early 1400s</b>. Tradition says Narasiṃha himself called him to Ahobilam and gave him sannyāsa; some scholars date the maṭha a century later.</div>
<div><b>The image.</b> Legend says the festival image of <b>Mālola Narasiṃha</b> leapt into his hands and told him to travel. Ever since, each <b>Jīyar</b> carries Mālola with him wherever he goes.</div>
<div><b>Today.</b> The maṭha, with its line of more than forty-five Jīyars, looks after the shrines and is one of the great institutions of Śrī Vaiṣṇavism.</div>
</div>'''+talk("The god travels with the monk?","For six hundred years. Wherever the Jīyar camps, Mālola is worshipped.")))
pages.append(page('voices','IN SONG AND STORY','Saints who came to the hills',facts([
 ('Tirumaṅgai Āḻvār','Tamil hymns (9th c.) on the lion of Siṅgavēḷ Kuṉṟam'),
 ('Vāsantikā Pariṇayam','Sanskrit play of the forest wedding, by the seventh Jīyar (16th c.)'),
 ('Annamācārya','The Tirupati poet-composer, by tradition initiated by the maṭha’s founder, sang of Ahobila Narasiṃha'),
 ('Caitanya','The Bengali saint’s visit is remembered at Upper Ahobilam')])
 +talk("Even Tirupati's poet came here?","Tradition says he took his vows here. The hills of Tirumala and Ahobilam are on the same pilgrim road.")))
pages.append(page('festivals','THROUGH THE YEAR','The Lord’s calendar',facts([
 ('Brahmotsavam','The great festival in <b>Phālguna</b> (Feb–Mar), in both Upper and Lower Ahobilam'),
 ('Paruveṭa','Before it, Jvālā and Prahlādavarada Narasiṃha tour some <b>48 villages</b> in a mock hunt, inviting the Cheñcus and everyone else to his wedding'),
 ('Kalyāṇa','The wedding with Cheñcu Lakṣmī, played out with full ceremony'),
 ('Narasiṃha Jayantī','The day of his appearance from the pillar'),
 ('Svātī','His birth-star, honoured each month')])
 +'<div class="key">A god who goes village to village <b>inviting everyone to his wedding</b>.</div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Narasiṃha','Man-lion: Viṣṇu’s fourth avatāra'),('Ugra · Saumya','Fierce · gentle'),('Stambha','Pillar'),('Nava','Nine'),('Bila','Cave'),
 ('Divya Deśam','One of 108 Viṣṇu shrines sung by the Āḻvārs'),('Jīyar','Head of a Śrī Vaiṣṇava maṭha'),('Paruveṭa','The Lord’s ritual hunt'),('Cheñcu','Forest people of the Nallamala'),('Jayastambha','Victory pillar')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The place.</b> Ahobilam in the Nallamala hills: Lower and Upper, nine Narasiṃhas, a Divya Deśam.</div>
<div><b>The legend.</b> Narasiṃha burst from the pillar for Prahlāda; the Ugra Stambha is that pillar.</div>
<div><b>The nine.</b> Jvālā, Ahobila, Mālola, Kroḍa, Kārañja, Bhārgava, Yogānanda, Chatravaṭa, Pāvana: fierce to gentle.</div>
<div><b>The wedding.</b> Cheñcu Lakṣmī calmed him; the forest people are his in-laws, and he tours their villages every year.</div>
<div><b>The history.</b> Kākatīyas to Vijayanagara; the 1579 raid; the Ahobila Maṭha and Mālola’s travels.</div>
</div>'''+talk("One line to remember?","God came out of a pillar for one small boy, then married a forest girl and stayed.")+'<div class="key">Aho balam! <b>Ahobilam</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Place and history:</b> Wikipedia, “Ahobilam”: Nandyal district; Nallamala; Lower and Upper (8 km); nine shrines and Prahlādavarada as the saumya, last-built shrine; Tirumaṅgai Āḻvār and the Divya Deśam; Kākatīyas, Reḍḍis, Sāḷuvas, Tuluvas, Kṛṣṇadevarāya; the 1579 raid by Murahari Rao; maṭha origin dated by scholars to the late 15th or early 16th c. Wikipedia, “Ahobila Matha”: Ādivaṇ Śaṭhakopa Jīyar, early 1400s; Mālola leaping into his hands; 46th Jīyar.</p>
<p><b>Shrines and legends:</b> ahobilamutt.org (the nine; Kārañja tree; Mālola as the maṭha’s deity; Yogānanda and Prahlāda; Kroḍa with Lakṣmī; Garuḍa’s penance in an old record). ramanuja.org and ibiblio.org archives (Ugra Stambha cleft; Prahlāda Meṭṭu; Bhārgava tīrtha; Chatravaṭa under a peepal). tirthayatra.org (Ahobila svayambhū, fierce; Akṣaya tīrtha). Outlook Traveller (Jvālā and the blood-washing pool; Pāvana hardest to reach; Cheñcu Lakṣmī shrine). harekrsna.com (Acalachāya Meru). greenmesg.org and others (aho balam / aho bilam; Garuḍādri). indiancolumbus.blogspot.com (Siṅgavēḷ Kuṉṟam; Vāsantikā Pariṇayam; lost copper plates). holydham.com and hindutemples-india.blogspot.com (Cheñcu Lakṣmī legend; Paruveṭa in 48 villages). veludharan.blogspot.com, trawell.in, touritvirtually.com (Prahlādavarada: jayastambha, three prakāras, sculptures, Narasa Nāyaka; not counted among the nine). temples-site (Phālguna Brahmotsavam; Paruveṭa).</p>
<p><b>Sources differ:</b> the maṭha’s founding date; the Prahlādavarada temple’s beginning; distances. <b>Not verified:</b> Annamācārya’s initiation here and Caitanya’s visit (tradition). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('legend','The Legend'),('stambha','The Ugra Stambha'),('nava','The Nine Narasiṃhas'),('moods','Nine Moods'),('garuda','Legend · Garuḍa'),('chenchu','Cheñcu Lakṣmī'),
 ('lower','The Prahlādavarada Temple'),('history','History'),('matha','The Ahobila Maṭha'),('voices','In Song and Story'),('festivals','Through the Year'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">THE NINE NARASIṂHAS</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">AHOBILAM</h1>
  <div class="series">NALLAMALA HILLS · A REFERENCE GUIDE</div>
  <div class="tag">Where the man-lion burst from the pillar</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>A demon king struck a pillar and dared his son’s God to come out. He did: <b>Narasiṃha</b>, the man-lion. Tradition says it happened here, in the gorges of the Nallamala hills, and points to a split rock peak as the pillar.</p>
    <p>In these hills the Lord is worshipped in <b>nine</b> forms, from blazing to blissful. Here, too, a forest girl calmed him, and her people still call him their son-in-law.</p>
    <p>This guide walks the nine shrines, tells the legends, and follows the kings and the Jīyars who kept them.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Jai Narasiṃha,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Do people really walk to all nine?","Many do, some barefoot. Two are by the road; the rest are forest climbs. Pāvana is the hardest.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Ahobilam.html','w').write(head+b+tail())
print('ok',len(pages))
