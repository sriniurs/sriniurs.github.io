exec(open('/home/claude/work/shakti/saptapuri.py').read().split("\nhead=head_navy(")[0])
head=head_navy('Char Dham · The Four Abodes · srini.presents',
 'Char Dham, the four abodes: the all-India circuit of Badrīnāth, Purī, Rāmeśvaram and Dvārakā linked to Ādi Śaṅkara and the four yugas, and the Himalayan Chota Char Dham of Yamunotrī, Gaṅgotrī, Kedārnāth and Badrīnāth. Maps, legends, the four maṭhas and the rivers. An illustrated reference guide.')
JY='/bhakti/temples-of-india/12-jyotirlingas/'
B=[('Badrīnāth','North','Uttarakhand',30.74,79.49,'Viṣṇu as Badrīnārāyaṇa','Satya'),
   ('Rāmeśvaram','South','Tamil Nadu',9.29,79.31,'Śiva as Rāmanāthasvāmī','Tretā'),
   ('Dvārakā','West','Gujarat',22.24,68.97,'Kṛṣṇa as Dvārakādhīś','Dvāpara'),
   ('Purī','East','Odisha',19.80,85.82,'Viṣṇu as Jagannātha','Kali')]
def INDIA(marks,w=560,h=470,note=''):
    g=''
    for i,(nm,la,lo,col,side) in enumerate(marks):
        x,y=xy(la,lo); g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(13 if side=="r" else -13):.0f}',f'{y+5:.0f}',nm,13,'#111','start' if side=='r' else 'end')
    return (f'<rect width="{w}" height="{h}" fill="#eef3fa"/><g transform="translate(-14 4) scale(1.3)">'+LAND().replace('#f4e6d0','#e8eedf')+'</g>'
     +f'<g transform="translate(-14 4) scale(1.3)">{g}</g>'+T(w-10,h-8,'Outline simplified; not an official boundary.',11,'#555','end')+note)
def uk(lat,lon): return 40+(lon-78.0)*300, 30+(31.2-lat)*300
def UKMAP(w=560,h=330):
    pts={'Yamunotrī':(31.01,78.46),'Gaṅgotrī':(30.99,78.94),'Kedārnāth':(30.73,79.07),'Badrīnāth':(30.74,79.49)}
    conf={'Devaprayāg':(30.15,78.6),'Rudraprayāg':(30.29,78.98)}
    def P(a): return uk(*a)
    riv=lambda a,b,c,lab: f'<path d="M{P(a)[0]:.0f} {P(a)[1]:.0f} Q{P(b)[0]:.0f} {P(b)[1]:.0f} {P(c)[0]:.0f} {P(c)[1]:.0f}" stroke="#4aa3df" stroke-width="5" fill="none"/>'
    g=('<rect width="%d" height="%d" fill="#e7f0d8"/>'%(w,h)+''.join(f'<path d="M{x} {y} l22 -30 l22 30z" fill="#fff" stroke="#888" stroke-width="1"/>' for x,y in ((120,40),(260,36),(330,60),(430,44),(500,70)))
     +riv((31.01,78.46),(30.6,78.2),(30.2,78.1),'')+riv((30.99,78.94),(30.6,78.55),(30.15,78.6),'')+riv((30.73,79.07),(30.5,79.05),(30.29,78.98),'')
     +riv((30.74,79.49),(30.45,79.3),(30.29,78.98),'')+riv((30.29,78.98),(30.2,78.8),(30.15,78.6),'')+f'<path d="M{P((30.15,78.6))[0]:.0f} {P((30.15,78.6))[1]:.0f} L{P((29.95,78.16))[0]:.0f} {P((29.95,78.16))[1]:.0f}" stroke="#1d6fd0" stroke-width="8"/>')
    for nm,(la,lo) in conf.items():
        x,y=uk(la,lo); g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="#fff" stroke="#111"/>'+T(f'{x+8:.0f}',f'{y+16:.0f}',nm,11,'#1d4f9a','start')
    for nm,(la,lo) in pts.items():
        x,y=uk(la,lo); g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#ff8c1a" stroke="#111" stroke-width="1.5"/>'+T(f'{x:.0f}',f'{y-14:.0f}',nm,13,'#111')
    x,y=uk(29.95,78.16); g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="#bbb" stroke="#111"/>'+T(f'{x+10:.0f}',f'{y+5:.0f}','Haridvār',11,'#555','start')
    g+=T(90,170,'Yamunā',11,'#1d4f9a','start')+T(250,190,'Bhāgīrathī',11,'#1d4f9a','start')+T(335,240,'Mandākinī',11,'#1d4f9a','start')+T(440,230,'Alakanandā',11,'#1d4f9a','start')+T(140,318,'GAṄGĀ',12,'#1d4f9a','start')
    return g+T(w-10,h-8,'simplified, not to scale',10,'#555','end')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Four temples at the four corners of a stylised India, a snow peak in the north and the sea on the other three sides">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/><circle cx="190" cy="134" r="96" fill="#ffd166" opacity=".25"/><circle cx="190" cy="134" r="60" fill="none" stroke="#ffd166" stroke-width="3" stroke-dasharray="6 6"/>'
 +'<path d="M150 70 l40 -50 l40 50z" fill="#fff" stroke="#111" stroke-width="2"/>'+TEMPLE(190,76,.8,'#dfe8f5')+TEMPLE(190,252,.8,'#ffe1a8')+TEMPLE(60,170,.8,'#ffd0c0')+TEMPLE(320,170,.8,'#d0f0d8')
 +T(190,110,'N',14,'#ffd166')+T(190,200,'S',14,'#ffd166')+T(108,140,'W',14,'#ffd166')+T(272,140,'E',14,'#ffd166')+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Char Dham','“Four abodes”: four places of God, to be visited once in a lifetime'),
 ('Bada Char Dham','<b>Badrīnāth</b> (N), <b>Purī</b> (E), <b>Rāmeśvaram</b> (S), <b>Dvārakā</b> (W): the all-India circuit'),
 ('Credited to','<b>Ādi Śaṅkara</b>, by tradition'),
 ('Deities','Three of Viṣṇu (Badrīnāth, Purī, Dvārakā), one of Śiva (Rāmeśvaram)'),
 ('Four ages','Satya: Badrīnāth · Tretā: Rāmeśvaram · Dvāpara: Dvārakā · Kali: Purī'),
 ('Chota Char Dham','The Himalayan four: <b>Yamunotrī, Gaṅgotrī, Kedārnāth, Badrīnāth</b>, all in Uttarakhand'),
 ('The link','<b>Badrīnāth</b> is in both'),
 ('Today','“Char Dham” in everyday speech often means the Himalayan four')])
 +talk("So which one is the real Char Dham?","Both are real. The big one circles India; the small one circles four Himalayan valleys. Badrīnāth anchors them both.")))
pages.append(page('dham','WHAT IS A DHĀM?','Abode, seat, home',facts([
 ('Dhāma','Sanskrit: an abode, a dwelling, a seat of power; also light and splendour'),
 ('Char','Hindi for “four”; in Sanskrit, <b>catur-dhāma</b>'),
 ('Belief','A pilgrimage to all four is held to help one towards <b>mokṣa</b>, liberation'),
 ('Purī, tīrtha, dhām','A <b>purī</b> is a holy city, a <b>tīrtha</b> a crossing-place, a <b>dhām</b> a place God lives')])
 +'<div class="panel reading"><p><b>Four corners.</b> The big circuit sets one abode near each edge of the land: Himalayan snow in the north, the Bay of Bengal in the east, the strait facing Laṅkā in the south and the Arabian Sea in the west. To complete it is, quite literally, to walk around India.</p></div>'
 +talk("Why four, and why at the edges?","Four directions, one home of God in each. Draw a line through them and you've drawn the country.")))
pages.append(page('map','THE FOUR ON ONE MAP','North, East, South, West',fig(560,470,'Simplified map of India marking Badrinath in the north, Puri in the east, Rameswaram in the south and Dwarka in the west',
 INDIA([('Badrīnāth',30.74,79.49,'#1d4f9a','r'),('Purī',19.80,85.82,'#1d4f9a','r'),('Rāmeśvaram',9.29,79.31,'#c0392b','r'),('Dvārakā',22.24,68.97,'#1d4f9a','r')]))
 +'<div class="key"><b>Blue</b>: Viṣṇu. <b>Red</b>: Śiva. Three of the four abodes are Viṣṇu’s.</div>'))
pages.append(page('yugas','FOUR AGES, FOUR ABODES','Satya to Kali','<table class="ct"><tr><th>Yuga</th><th>Dhām</th><th>Why</th></tr>'
 '<tr><td><b>Satya</b></td><td>Badrīnāth</td><td>Nara-Nārāyaṇa’s penance among the badrī (jujube) trees</td></tr>'
 '<tr><td><b>Tretā</b></td><td>Rāmeśvaram</td><td>Rāma installs a Śiva-liṅga here after the war with Rāvaṇa</td></tr>'
 '<tr><td><b>Dvāpara</b></td><td>Dvārakā</td><td>Kṛṣṇa leaves Mathurā and makes Dvārakā his capital</td></tr>'
 '<tr><td><b>Kali</b></td><td>Purī</td><td>Viṣṇu as <b>Jagannātha</b>, Lord of the World, for this age</td></tr></table>'
 +'<div class="panel reading"><p>Tradition links this scheme to Ādi Śaṅkara: each abode stands for one age of the world, so the circuit is a walk through time as well as space. Pilgrims often go in the order of the ages, ending at Purī in our own age.</p></div>'
 +talk("We live in the Kali age, so Purī is ours?","That's the idea: Jagannātha is the Lord for now. The other three are the ages behind us.")))
def dham(k,title,sub,art,rows,q,a,extra=''):
    pages.append(page(k,title,sub,fig(560,170,art[0],art[1])+facts(rows)+extra+talk(q,a)))
dham('badri','BADRĪNĀTH','Abode of the North · Satya Yuga',('A small brightly painted Himalayan temple below snow peaks beside a rushing river',
 '<rect width="560" height="170" fill="#cfe3f5"/>'+''.join(f'<path d="M{x} 130 l60 -100 l60 100z" fill="#fff" stroke="#888"/>' for x in (20,140,300,420))+'<rect y="130" width="560" height="40" fill="#8aa37a"/><path d="M0 160 Q280 140 560 162" stroke="#4aa3df" stroke-width="8" fill="none"/>'+TEMPLE(280,140,1.3,'#ff8c8c')),[
 ('Where','Uttarakhand, high in the Garhwal Himalaya, on the <b>Alakanandā</b> river'),
 ('Deity','<b>Badrīnārāyaṇa</b>: Viṣṇu seated in meditation, in black stone'),
 ('Legend','Viṣṇu did penance here as <b>Nara-Nārāyaṇa</b>; Lakṣmī became a <b>badrī</b> tree to shade him'),
 ('Śaṅkara','Tradition says he recovered the image from the <b>Nārada Kuṇḍa</b> and re-established worship'),
 ('Priest','The chief priest, the <b>Rāval</b>, is by custom a Nambūdiri brāhmaṇa from Kerala'),
 ('Season','Open in summer; in winter the worship moves down to <b>Jyotirmaṭh</b> (Joshimath)'),
 ('In both lists','The northern Dhām of the Bada Char Dham and the last stop of the Chota Char Dham')],
 "A priest from Kerala at the top of the Himalayas?","Śaṅkara's legacy: India's south looking after its north for over a thousand years.")
dham('rames','RĀMEŚVARAM','Abode of the South · Tretā Yuga',('A temple on an island with long pillared corridors, waves on both sides',
 '<rect width="560" height="170" fill="#bfe3f0"/><path d="M0 120 Q280 100 560 120 V170 H0z" fill="#f4e6c0"/>'+TEMPLE(280,130,1.4,'#ffe1a8')+''.join(f'<rect x="{60+i*28}" y="110" width="6" height="40" fill="#c9a26b" stroke="#111"/>' for i in range(4))+''.join(f'<rect x="{410+i*28}" y="110" width="6" height="40" fill="#c9a26b" stroke="#111"/>' for i in range(4))),[
 ('Where','Pamban island, Tamil Nadu, facing Laṅkā across the sea'),
 ('Deity','<b>Rāmanāthasvāmī</b>: Śiva as “Rāma’s Lord”, a Jyotirliṅga'),
 ('Legend','Rāma worshipped Śiva here after the war, to cleanse the sin of killing Rāvaṇa'),
 ('Famous for','Its very long pillared corridors and the many <b>tīrthas</b> (wells) bathed in before darśan'),
 ('The one Śiva Dhām','The only Śaiva abode of the four')],
 "Why is a Viṣṇu circuit holding a Śiva temple?","Because Viṣṇu, as Rāma, worshipped Śiva here. The four are a conversation, not a contest.",
 f'<div class="key">Full guide: <a href="{JY}rameswaram/">Rāmeśvaram, in the 12 Jyotirliṅgas series</a></div>')
dham('dwarka','DVĀRAKĀ','Abode of the West · Dvāpara Yuga',('A tall multi-storeyed temple spire on the shore where a river meets the sea, flags flying',
 '<rect width="560" height="170" fill="#cfe3f5"/><rect y="120" width="560" height="50" fill="#4aa3df"/><path d="M0 120 Q200 110 320 124 L560 124" fill="#f4e6c0"/>'
 +'<g transform="translate(300 124)" stroke="#111" stroke-width="1.6">'+''.join(f'<rect x="{-30+k*3}" y="{-18-k*16}" width="{60-k*6}" height="16" fill="{"#f2e6c8" if k%2 else "#e2cfa8"}"/>' for k in range(6))+'<path d="M0 -114 v-24"/><path d="M0 -138 l24 6 l-24 6z" fill="#ff8c1a"/></g>'),[
 ('Where','Gujarat, on the Arabian Sea where the <b>Gomatī</b> meets the ocean'),
 ('Deity','<b>Dvārakādhīś</b>: Kṛṣṇa as “King of Dvārakā”'),
 ('Legend','Kṛṣṇa built his capital here after leaving Mathurā; after his time the sea swallowed the city'),
 ('Temple','The <b>Jagat Mandir</b>, a tall five-storeyed spire with a great flag'),
 ('Maṭha','Seat of the western Śaṅkara maṭha, the <b>Śāradā Pīṭha</b>'),
 ('Also','One of the seven sacred cities, the <b>Saptapurī</b>')],
 "Is the old city really under the sea?","Tradition says so, and divers have searched offshore. What they found is still debated.",
 '<div class="key">See also: <a href="/bhakti/temples-of-india/sapta-puri/">The Saptapurī</a></div>')
dham('puri','PURĪ','Abode of the East · Kali Yuga',('Three wooden deities with large round eyes, dark, white and yellow, and a great chariot on wheels',
 '<rect width="560" height="170" fill="#fff4cd"/>'+''.join(f'<g transform="translate({x} 100)" stroke="#111" stroke-width="2"><rect x="-22" y="-40" width="44" height="70" rx="10" fill="{c}"/><circle cx="-9" cy="-18" r="8" fill="#fff"/><circle cx="9" cy="-18" r="8" fill="#fff"/><circle cx="-9" cy="-18" r="3"/><circle cx="9" cy="-18" r="3"/><path d="M-10 4 q10 8 20 0" fill="#c0392b"/></g>' for x,c in ((90,'#fff'),(160,'#ffd60a'),(230,'#222')))
 +'<g transform="translate(420 150)" stroke="#111" stroke-width="2"><rect x="-60" y="-50" width="120" height="40" fill="#c0392b"/><path d="M-60 -50 l60 -70 l60 70z" fill="#ffd60a"/><circle cx="-40" r="16" fill="#7a5a2a"/><circle cx="40" r="16" fill="#7a5a2a"/></g>'),[
 ('Where','Odisha, on the Bay of Bengal'),
 ('Deities','<b>Jagannātha</b> with his brother <b>Balabhadra</b> and sister <b>Subhadrā</b>, carved in <b>wood</b>'),
 ('Navakalevara','“New body”: the wooden images are replaced in a secret rite, in certain years'),
 ('Ratha Yātrā','The chariot festival: the three ride huge chariots through the streets'),
 ('Temple','Begun in the 12th century by <b>Anantavarman Coḍagaṅga</b> of the Eastern Gaṅga dynasty'),
 ('Maṭha','Seat of the eastern Śaṅkara maṭha, the <b>Govardhana Maṭha</b>')],
 "God made of wood, renewed every few years?","A God who takes a new body, just as we do. That's the Kali-age lesson Purī teaches.")
pages.append(page('mathas','ŚAṄKARA’S FOUR MAṬHAS','Four seats, four directions','<table class="ct"><tr><th>Direction</th><th>Maṭha</th><th>Veda</th><th>Great saying</th><th>First head</th></tr>'
 '<tr><td>North</td><td><b>Jyotirmaṭh</b> (near Badrīnāth)</td><td>Atharva</td><td><i>ayam ātmā brahma</i></td><td>Toṭaka</td></tr>'
 '<tr><td>East</td><td><b>Govardhana</b>, Purī</td><td>Ṛg</td><td><i>prajñānaṃ brahma</i></td><td>Padmapāda</td></tr>'
 '<tr><td>South</td><td><b>Śṛṅgeri</b>, Karnataka</td><td>Yajur</td><td><i>ahaṃ brahmāsmi</i></td><td>Sureśvara</td></tr>'
 '<tr><td>West</td><td><b>Śāradā</b>, Dvārakā</td><td>Sāma</td><td><i>tat tvam asi</i></td><td>Hastāmalaka</td></tr></table>'
 +'<div class="panel reading"><p><b>Matching the Dhāms.</b> Three maṭhas sit at or beside a Dhām. The southern one is at <b>Śṛṅgeri</b> in Karnataka, not at Rāmeśvaram.</p><p><b>Dates.</b> Tradition credits Śaṅkara with founding all four; historians debate how many go back to him, and when.</p></div>'
 +talk("Four Vedas, four sayings, four corners?","Śaṅkara's map of India was also a map of the Vedas. Each corner guards one.")))
pages.append(page('pairs','PAIRED SHRINES','A partner for each abode',facts([
 ('Badrīnāth','paired with <b>Kedārnāth</b>'),('Rāmeśvaram','paired with <b>Raṅganātha</b> (Śrīraṅgam)'),
 ('Dvārakā','paired with <b>Somanātha</b>'),('Purī','paired with <b>Liṅgarāja</b>, Bhubaneswar')])
 +'<div class="panel reading"><p>Some traditions pair each abode with a partner of the other god, so every Viṣṇu Dhām has a Śiva shrine nearby and Śiva’s Rāmeśvaram has Viṣṇu’s Śrīraṅgam. One version even lists the four Dhāms as all Viṣṇu (with Raṅganātha in place of Rāmeśvaram) and the partners as all Śiva.</p></div>'
 +f'<div class="key">Kedārnāth and Somanātha are Jyotirliṅgas: <a href="{JY}kedarnath/">Kedārnāth</a> · <a href="{JY}somnath/">Somanātha</a></div>'))
pages.append(page('chota','THE CHOTA CHAR DHAM','Four in the Himalaya',fig(560,330,'Simplified map of Garhwal: Yamunotri, Gangotri, Kedarnath and Badrinath at the heads of the Yamuna, Bhagirathi, Mandakini and Alakananda rivers, which join to form the Ganga at Devaprayag',UKMAP())
 +'''<div class="panel reading"><p><b>Four river sources.</b> Each of the four stands near the head of a sacred river: <b>Yamunā</b> at Yamunotrī, <b>Bhāgīrathī</b> at Gaṅgotrī, <b>Mandākinī</b> at Kedārnāth and <b>Alakanandā</b> at Badrīnāth. The last three meet and at <b>Devaprayāg</b> become the <b>Gaṅgā</b>.</p>
<p><b>West to east.</b> Pilgrims usually go in that order: Yamunotrī, Gaṅgotrī, Kedārnāth, then Badrīnāth.</p></div>'''))
pages.append(page('chota2','HOW THE SMALL ONE GOT ITS NAME','From “Chota” to just “Char Dham”',facts([
 ('Chota','Hindi “small”: the Himalayan four were called the <b>Chota</b> Char Dham to set them apart from the all-India circuit'),
 ('Since mid-20th c.','As roads reached the hills, the Himalayan four became known simply as “the Char Dham”'),
 ('Mix of traditions','Two goddess shrines (<b>Yamunā, Gaṅgā</b>), one Śiva (<b>Kedārnāth</b>), one Viṣṇu (<b>Badrīnāth</b>)'),
 ('Season','All four close in winter under snow; the deities’ worship moves to villages lower down, and returns in summer')])
 +talk("So when someone says 'I did the Char Dham'...","Ask which one. Nine times in ten, they mean the Himalayan four.")))
dham('yamunotri','YAMUNOTRĪ','Source of the Yamunā',('A small temple in a narrow valley with steam rising from a hot spring beside it, a waterfall behind',
 '<rect width="560" height="170" fill="#cfe3f5"/>'+HILL(100,170,240,150,'#3a7a3a')+HILL(460,170,240,150,'#3a7a3a')+'<path d="M280 0 v130" stroke="#bfe3f0" stroke-width="10"/>'+TEMPLE(240,150,1.1,'#ffe1a8')+'<ellipse cx="350" cy="150" rx="30" ry="10" fill="#bfe3f0" stroke="#111"/>'+''.join(f'<path d="M{340+i*10} 140 q-6 -14 0 -26" stroke="#bbb" stroke-width="3" fill="none"/>' for i in range(3))),[
 ('River','The <b>Yamunā</b>, rising on the glacier above'),
 ('Goddess','<b>Yamunā</b>, daughter of Sūrya the Sun and sister of <b>Yama</b>, god of death'),
 ('Belief','A bath in her waters is said to spare one an untimely death'),
 ('Sūrya Kuṇḍa','A hot spring beside the temple: pilgrims cook rice and potatoes in it as prasāda'),
 ('Winter seat','Her image goes down to the village of <b>Kharsālī</b>')],
 "Cooking rice in a holy spring?","Boiled by the Sun's daughter herself. It's the only temple where the stove is the river.")
dham('gangotri','GAṄGOTRĪ','Where Gaṅgā came down',('A white stone temple on a riverbank, a king meditating on a rock nearby, a glacier in the distance',
 '<rect width="560" height="170" fill="#cfe3f5"/><path d="M380 60 l60 -40 l80 40z" fill="#fff" stroke="#888"/><path d="M0 150 Q280 130 560 150" stroke="#4aa3df" stroke-width="12" fill="none"/>'+TEMPLE(200,140,1.2,'#fff')+'<rect x="330" y="120" width="60" height="20" fill="#8a7a6a" stroke="#111"/>'+KING(360,118,.8)),[
 ('River','The <b>Bhāgīrathī</b>, which becomes the Gaṅgā; its glacier source is <b>Gaumukha</b>, “cow’s mouth”, higher up'),
 ('Legend','King <b>Bhagīratha</b> did penance here to bring Gaṅgā down from heaven to free his ancestors; Śiva caught her in his hair'),
 ('Bhagīratha Śilā','The rock where he is said to have meditated'),
 ('Temple','Built by the Gorkha general <b>Amar Singh Thapa</b>, during Nepal’s rule of Garhwal in the early 19th century'),
 ('Winter seat','Gaṅgā’s image goes down to <b>Mukhbā</b>')],
 "Why is the river called Bhāgīrathī here?","After Bhagīratha. We still say 'Bhagīratha effort' for a near-impossible task.")
dham('kedar','KEDĀRNĀTH','Śiva in the snows',('A massive grey stone temple below a wall of snow peaks',
 '<rect width="560" height="170" fill="#cfe3f5"/>'+''.join(f'<path d="M{x} 120 l70 -110 l70 110z" fill="#fff" stroke="#888"/>' for x in (40,180,320))+'<rect y="120" width="560" height="50" fill="#9aa"/>'+TEMPLE(280,150,1.5,'#b8b8b8')),[
 ('River','The <b>Mandākinī</b>'),
 ('Deity','Śiva as <b>Kedāreśvara</b>, a Jyotirliṅga: the hump of the bull-form he took to hide from the Pāṇḍavas'),
 ('Paired with','Badrīnāth, in the Bada Char Dham pairs'),
 ('Winter seat','Worship moves to <b>Ukhīmaṭh</b>')],
 "The Pāṇḍavas are here too?","Seeking Śiva's forgiveness after the war. He dived into the earth; his hump stayed here.",
 f'<div class="key">Full guide: <a href="{JY}kedarnath/">Kedārnāth, in the 12 Jyotirliṅgas series</a></div>')
pages.append(page('compare','THE TWO SIDE BY SIDE','Big circle, small circle','<table class="ct"><tr><th></th><th>Bada Char Dham</th><th>Chota Char Dham</th></tr>'
 '<tr><td><b>Sites</b></td><td>Badrīnāth, Purī, Rāmeśvaram, Dvārakā</td><td>Yamunotrī, Gaṅgotrī, Kedārnāth, Badrīnāth</td></tr>'
 '<tr><td><b>Spread</b></td><td>Four corners of India</td><td>Four valleys of Garhwal, Uttarakhand</td></tr>'
 '<tr><td><b>Deities</b></td><td>3 Viṣṇu, 1 Śiva</td><td>2 river goddesses, 1 Śiva, 1 Viṣṇu</td></tr>'
 '<tr><td><b>Idea</b></td><td>Four directions, four yugas, four maṭhas</td><td>Four river sources of the Gaṅgā system</td></tr>'
 '<tr><td><b>Open</b></td><td>All year, except Badrīnāth</td><td>Summer only</td></tr>'
 '<tr><td><b>Credited to</b></td><td>Ādi Śaṅkara, by tradition</td><td>Old pilgrim route; name popular since the mid-20th c.</td></tr></table>'
 +'<div class="key">The two circles touch at one point: <b>Badrīnāth</b>.</div>'))
pages.append(page('links','HOW IT CONNECTS','Other sacred sets on this site',facts([
 ('12 Jyotirliṅgas',f'<a href="{JY}rameswaram/">Rāmeśvaram</a> and <a href="{JY}kedarnath/">Kedārnāth</a> are both Jyotirliṅgas; so is <a href="{JY}somnath/">Somanātha</a>, Dvārakā’s partner'),
 ('Saptapurī','<a href="/bhakti/temples-of-india/sapta-puri/">Dvārakā</a> is one of the seven sacred cities; some lists slip Purī in too'),
 ('Śakti Pīṭhas','Purī’s goddess <b>Vimalā</b>, inside the Jagannātha temple, is counted among the wider Śakti Pīṭhas')])
 +talk("Is there any place in all the lists?","Not one. But Dvārakā and Rāmeśvaram come closest, with two lists each.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Dhāma','Abode, seat'),('Char · Catur','Four'),('Bada · Chota','Big · small'),('Yuga','An age of the world: Satya, Tretā, Dvāpara, Kali'),
 ('Maṭha','Monastery, seat of a lineage'),('Mahāvākya','A “great saying” of the Upaniṣads'),('Badrī','The jujube tree'),('Navakalevara','“New body”: Purī’s renewal of the wooden images'),
 ('Ratha','Chariot'),('Kuṇḍa','Pool, spring'),('Prayāga','A river confluence')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Two sets.</b> “Char Dham” means two different circuits of four.</div>
<div><b>The big one.</b> Badrīnāth, Purī, Rāmeśvaram, Dvārakā: four corners of India, four yugas, credited to Śaṅkara.</div>
<div><b>The maṭhas.</b> Four Śaṅkara seats at Jyotirmaṭh, Purī, Śṛṅgeri and Dvārakā guard four Vedas.</div>
<div><b>The small one.</b> Yamunotrī, Gaṅgotrī, Kedārnāth, Badrīnāth: four river sources in Garhwal, open only in summer.</div>
<div><b>The hinge.</b> Badrīnāth belongs to both.</div>
</div>'''+talk("One line to remember?","Walk the big circle and you've walked India; walk the small one and you've walked to where the Gaṅgā begins.")+'<div class="key">Jai Badrī Viśāl! 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Char Dham:</b> Wikipedia, “Char Dham”: Badrīnāth, Dvārakā, Purī, Rāmeśvaram; three Viṣṇu and one Śiva; Ādi Śaṅkara and the four yugas; Jagannātha as the Kali-yuga form; the four Āmnāya maṭhas (direction, Veda, mahāvākya, first disciple); Purī temple begun by Anantavarman Coḍagaṅga; Govardhana Maṭha at Purī; Badrīnāth closed in winter; alternative Vaiṣṇava list and paired shrines (Kedārnāth, Rāmeśvaram/Raṅganātha, Somanātha, Liṅgarāja). New World Encyclopedia, “Char Dham”.</p>
<p><b>Chota Char Dham:</b> Wikipedia, “Chota Char Dham”: the Uttarakhand four; name to distinguish from the larger circuit; called simply Char Dham since the mid-20th c.; two goddess sites, one Śaiva, one Vaiṣṇava; closed in winter.</p>
<p><b>Individual shrines:</b> Wikipedia articles on Badrinath Temple (Nara-Nārāyaṇa; Nārada Kuṇḍa; Rāval from Kerala; Joshimath), Yamunotri (Sūrya Kuṇḍa; Kharsālī), Gangotri (Bhagīratha; Gaumukha; Amar Singh Thapa; Mukhbā), Kedarnath (Pāṇḍavas; Ukhīmaṭh), Dwarkadhish Temple (Jagat Mandir; Gomatī), Jagannath Temple (Navakalevara; Ratha Yātrā; Vimalā). Rāmeśvaram and Kedārnāth details also in this site’s Jyotirliṅga guides.</p>
<p><b>Sources differ:</b> how many maṭhas Śaṅkara himself founded, and when; who first defined the Char Dham; which shrine pairs with which. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('dham','What Is a Dhām?'),('map','The Four on One Map'),('yugas','Four Ages, Four Abodes'),('badri','Badrīnāth'),('rames','Rāmeśvaram'),('dwarka','Dvārakā'),('puri','Purī'),
 ('mathas','Śaṅkara’s Four Maṭhas'),('pairs','Paired Shrines'),('chota','The Chota Char Dham'),('chota2','How the Small One Got Its Name'),('yamunotri','Yamunotrī'),('gangotri','Gaṅgotrī'),('kedar','Kedārnāth'),
 ('compare','The Two Side by Side'),('links','How It Connects'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">THE FOUR ABODES</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">CHAR DHAM</h1>
  <div class="series">TEMPLES OF INDIA · A REFERENCE GUIDE</div>
  <div class="tag">Four corners of India, and four Himalayan valleys</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Say “Char Dham” to ten pilgrims and you may get two different answers. For some it is the great circle around India: <b>Badrīnāth</b> in the snows, <b>Purī</b> on the eastern sea, <b>Rāmeśvaram</b> at the southern tip and <b>Dvārakā</b> on the western shore.</p>
    <p>For others it is four shrines in the Himalaya, at the heads of the rivers that become the Gaṅgā: <b>Yamunotrī</b>, <b>Gaṅgotrī</b>, <b>Kedārnāth</b> and Badrīnāth again.</p>
    <p>This guide explains both: the abodes, the legends, the four ages and Śaṅkara’s four maṭhas, and where the two circles meet.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Jai Badrī Viśāl,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Two Char Dhams? Which one did my grandparents mean?","Depends where they lived. In the south, the big circle. In the north, often the Himalayan four.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Char_Dham.html','w').write(head+b+tail())
print('ok',len(pages))
