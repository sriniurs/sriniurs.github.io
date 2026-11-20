exec(open('/home/claude/work/shakti/common_s.py').read())
head=make_head('Purī Jagannātha · Abode of the East · srini.presents',
 'Jagannātha of Purī: the Nīla Mādhava legend and the wooden images, Jagannātha, Balabhadra, Subhadrā and Sudarśana, the great temple and its Nīla Cakra, the kitchen and mahāprasāda, Snāna Yātrā, Ratha Yātrā and Navakalevara, Vimalā, the saints, and Purī as the Kali-yuga Dhām. An illustrated reference guide.')
def o(lat,lon): return 60+(lon-85.0)*250, 30+(20.6-lat)*250
def OMAP(w=560,h=300):
    coast=' '.join(f'{o(la,lo)[0]:.0f},{o(la,lo)[1]:.0f}' for la,lo in ((20.6,86.75),(20.25,86.55),(19.95,86.25),(19.80,85.85),(19.62,85.45),(19.40,85.10),(19.2,84.9)))
    g=f'<rect width="{w}" height="{h}" fill="#bfe3f0"/><polygon points="0,0 {o(20.6,86.75)[0]:.0f},0 {coast} 0,{h}" fill="#e7f0d8" stroke="#111" stroke-width="2"/>'
    cx,cy=o(19.7,85.33); g+=f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="44" ry="22" fill="#9fd0ea" stroke="#111"/>'+T(f'{cx:.0f}',f'{cy+5:.0f}','Chilikā',11,'#1d4f9a')
    for nm,la,lo,col,side in (('PURĪ',19.80,85.82,'#1d4f9a','l'),('Koṇārka',19.89,86.09,'#bbb','r'),('Bhubaneswar',20.27,85.84,'#bbb','r'),('Sākṣīgopāla',19.98,85.79,'#bbb','l')):
        x,y=o(la,lo); r=8 if col=='#1d4f9a' else 6
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',nm,12,'#111','start' if side=='r' else 'end')
    return g+T(470,250,'BAY OF BENGAL',13,'#1d4f9a')+T(w-10,h-8,'simplified, not to scale',10,'#555','end')
def DEITY(x,y,c,face='#fff',s=1,arms=True):
    eye='#111'
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 40 v-80 q30 -24 60 0 v80z" fill="{c}"/>'
     f'<circle cx="-13" cy="-18" r="11" fill="#fff"/><circle cx="13" cy="-18" r="11" fill="#fff"/><circle cx="-13" cy="-18" r="5" fill="{eye}"/><circle cx="13" cy="-18" r="5" fill="{eye}"/><path d="M-14 6 q14 10 28 0" fill="#c0392b"/>'
     +(f'<path d="M-30 -2 h-18 M30 -2 h18" stroke="{c}" stroke-width="10"/>' if arms else '')+'<path d="M-24 -46 l24 -16 l24 16" fill="#e0a800"/></g>')
def DEUL(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-80" y="-30" width="160" height="30" fill="#e8dcc0"/>'
 '<path d="M-36 -30 q-6 -80 10 -130 q26 -24 52 0 q16 50 10 130z" fill="#f2e6c8"/>'+''.join(f'<path d="M{-34+k} {-40-k*10} h{68-2*k}" stroke-width="1"/>' for k in range(10))
 +'<path d="M-20 -160 q20 -16 40 0" fill="#e2cfa8"/><circle cy="-170" r="12" fill="#3b6fd0"/><path d="M0 -182 v-26"/><path d="M0 -208 l22 6 l-22 6z" fill="#ff8c1a"/>'
 '<path d="M-80 -30 l-26 -40 h40z M80 -30 l26 -40 h-40z" fill="#e2cfa8"/></g>')
def CHARIOT(x,y,s=1,c='#c0392b',c2='#ffd60a'): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-50" y="-40" width="100" height="30" fill="#7a5a2a"/>'
 f'<path d="M-46 -40 q46 -110 92 0z" fill="{c}"/><path d="M-30 -40 q30 -70 60 0" fill="{c2}"/><path d="M0 -118 v-20"/><path d="M0 -138 l18 5 l-18 5z" fill="{c2}"/>'
 +''.join(f'<circle cx="{dx}" cy="-8" r="13" fill="#5a3a1a"/>' for dx in (-36,-12,12,36))+'</g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Three wooden deities with large round eyes, dark, white and yellow, in front of a tall curved temple tower by the sea">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/><rect y="220" width="380" height="48" fill="#4aa3df" rx="8"/>'+DEUL(190,214,.9)
 +DEITY(90,210,'#f2f2f2',s=.9)+DEITY(190,226,'#ffd60a',s=.7,arms=False)+DEITY(290,210,'#1a1a1a',s=.9)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deities','<b>Jagannātha</b>, his elder brother <b>Balabhadra</b>, his sister <b>Subhadrā</b>, and <b>Sudarśana</b>'),
 ('Made of','<b>Wood</b>: neem logs called <b>dāru brahma</b>, replaced from time to time'),
 ('Where','Purī, on the Bay of Bengal, Odisha'),
 ('Temple','The <b>Baḍa Deuḷa</b>, 12th century, Eastern Gaṅga kings, about 65 m tall'),
 ('Char Dham','The eastern abode, for <b>Kali Yuga</b>'),
 ('Famous for','<b>Ratha Yātrā</b>, the chariot festival; <b>mahāprasāda</b> from one of India’s biggest kitchens'),
 ('Goddess','<b>Vimalā</b>, inside the complex; Lakṣmī has her own shrine'),
 ('Śaṅkara maṭha','<b>Govardhana Maṭha</b>, the eastern seat')])
 +talk("Why does God have such huge round eyes here?","So he never blinks. Jagannātha keeps watching the world, and the world can always meet his gaze.")))
pages.append(page('where','WHERE IT IS','On the Bay of Bengal',fig(560,300,'Simplified map of the Odisha coast: Puri on the Bay of Bengal, Konark to the north-east, Bhubaneswar inland and Chilika lake to the south-west',OMAP())
 +'''<div class="panel reading"><p><b>The holy field.</b> Purī stands on the sand by the sea. Its old names are <b>Śrī Kṣetra</b>, <b>Puruṣottama Kṣetra</b> and <b>Nīlācala</b>, “the blue hill”, for the low sandy rise the temple stands on.</p>
<p><b>The triangle.</b> With the Sun temple of <b>Koṇārka</b> and Śiva’s <b>Liṅgarāja</b> at Bhubaneswar, Purī forms Odisha’s great temple triangle. Liṅgarāja is counted as Purī’s Śiva partner in the Char Dham pairs.</p></div>'''))
pages.append(page('names','THE NAMES','Lord of the world',facts([
 ('Jagannātha','<i>jagat</i> “world” + <i>nātha</i> “lord”: Lord of the Universe'),
 ('Jagā, Jagabandhu','Odia pet names: “Jaga”, “Friend of the world”'),
 ('Kālia, Cakā Ākhi','“The dark one”; “Round-eyes”'),
 ('Puruṣottama','“The Supreme Person”: an old name of the god and of Purī'),
 ('Baḍa Deuḷa','“The Great Temple”, as Odias call it'),
 ('Baḍa Ṭhākura','“Elder Lord”: Balabhadra')])
 +talk("English got the word 'juggernaut' from here?","Yes: from the giant chariots that nothing could stop. The word travelled; the god stayed home.")))
pages.append(page('legend','THE LEGEND · NĪLA MĀDHAVA','The blue god in the forest',fig(560,170,'A forest chief worshipping a shining blue image in a cave, a priest with a blindfold following him, mustard seeds dropping from his hand',
 '<rect width="560" height="170" fill="#e7f0d8"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="28" fill="#3a8a3a"/>' for x,y in ((40,40),(110,30),(470,30),(530,50)))+'<ellipse cx="420" cy="120" rx="100" ry="50" fill="#3a2a1a"/><circle cx="420" cy="110" r="26" fill="#3b6fd0" stroke="#111" stroke-width="2"/><circle cx="420" cy="110" r="38" fill="#9fd0ea" opacity=".4"/>'
 +person(300,150,'#2a9d6f','#8a5a3a',1)+person(200,150,'#ffd60a','#e8b48a',1)+'<path d="M188 116 h24" stroke="#111" stroke-width="5"/>'+''.join(f'<circle cx="{160+i*12}" cy="{162+(i%2)*4}" r="2.5" fill="#e0a800"/>' for i in range(5)))+'''<div class="steps">
<div><b>The secret god.</b> In the forests lived the <b>Śabara</b> people. Their chief, <b>Viśvāvasu</b>, secretly worshipped a shining blue image of Viṣṇu, <b>Nīla Mādhava</b>, in a hidden cave.</div>
<div><b>The king’s search.</b> King <b>Indradyumna</b> of Avanti heard of it and sent priests to find it. Only one, <b>Vidyāpati</b>, came close: he lived with the Śabaras and married Viśvāvasu’s daughter, <b>Lalitā</b>.</div>
<div><b>Blindfolded.</b> At last the chief led his son-in-law to the god, blindfolded. A popular telling adds that Vidyāpati dropped mustard seeds along the way, so the path could be found again when they sprouted.</div>
<div><b>Gone.</b> When the king came, Nīla Mādhava had vanished. A voice told him the Lord would come again, as a log of wood.</div>
</div>'''))
pages.append(page('log','THE LOG AND THE CARPENTER','How the images were made',fig(560,170,'A great log floating to the shore; an old carpenter working alone behind closed doors; a king opening the door early',
 '<rect width="560" height="170" fill="#bfe3f0"/><rect y="110" width="200" height="60" fill="#f4e6c0"/><rect x="40" y="110" width="140" height="22" rx="11" fill="#9a6a3a" stroke="#111" stroke-width="2"/>'
 +'<rect x="240" y="40" width="300" height="130" fill="#e8dcc0" stroke="#111" stroke-width="2"/><rect x="300" y="70" width="80" height="100" fill="#7a3a2a" stroke="#111"/><path d="M380 70 l40 10 v90 l-40 0z" fill="#9a5a3a" stroke="#111"/>'+person(470,160,'#5a2a6a','#c98b5a',.9)+DEITY(340,150,'#c9a26b',s=.5,arms=False))+'''<div class="steps">
<div><b>The dāru.</b> A great log, the <b>dāru brahma</b>, washed up on the shore, as the voice had promised.</div>
<div><b>The old carpenter.</b> No one could carve it, until an old craftsman (in many tellings <b>Viśvakarmā</b>, or Viṣṇu himself) offered to, on one condition: he must work behind closed doors for 21 days, undisturbed.</div>
<div><b>The door.</b> When the sounds stopped, the queen grew anxious and the king opened the door early. The carpenter had vanished, leaving the images with stumps for arms and no feet.</div>
<div><b>As they are.</b> A voice said: worship them just so. That is why Jagannātha looks as he does.</div>
</div>'''+talk("So God is unfinished?","Or finished in a way we didn't expect. He needs no hands to hold you, no feet to come to you.")))
pages.append(page('deities','THE FOUR ON THE JEWEL THRONE','Ratnavedī',fig(560,190,'Four wooden deities on a raised throne: white Balabhadra, yellow Subhadra, black Jagannatha and a tall pillar-like Sudarshana',
 '<rect width="560" height="190" fill="#2a1a3a"/><rect x="40" y="160" width="480" height="20" fill="#e0a800" stroke="#111" stroke-width="2"/>'+DEITY(130,120,'#f2f2f2',s=1)+DEITY(260,130,'#ffd60a',s=.75,arms=False)+DEITY(390,120,'#1a1a1a',s=1)+'<rect x="486" y="60" width="16" height="100" fill="#c0392b" stroke="#111" stroke-width="2"/>'
 +T(130,186,'BALABHADRA',11,'#ffd166')+T(260,186,'SUBHADRĀ',11,'#ffd166')+T(390,186,'JAGANNĀTHA',11,'#ffd166')+T(494,50,'SUDARŚANA',10,'#ffd166'))+facts([
 ('Balabhadra','The elder brother, white, the tallest; Balarāma'),
 ('Subhadrā','The sister, yellow, in the middle, smaller and without arms'),
 ('Jagannātha','Dark, with round eyes and a wide smile; Kṛṣṇa, Viṣṇu'),
 ('Sudarśana','Viṣṇu’s discus, as a tall wooden pillar'),
 ('Also','Small metal images of Mādhava, Śrīdevī and Bhūdevī')])
 +'<div class="key">A god with his <b>family</b>, brother and sister, rather than a consort.</div>'))
pages.append(page('temple','THE BAḌA DEUḶA','The great temple',fig(560,230,'The tall curved tower of the Jagannatha temple with a wheel and flag on top, a front hall, and a pillar before the lion gate',
 '<rect width="560" height="230" fill="#cfe3f5"/><rect y="200" width="560" height="30" fill="#d8c8a8"/>'+DEUL(300,200,1)+'<rect x="80" y="110" width="12" height="90" fill="#bbb" stroke="#111" stroke-width="1.5"/><circle cx="86" cy="104" r="8" fill="#ffd60a" stroke="#111"/>'+T(86,92,'ARUṆA STAMBHA',9,'#555')
 +''.join(f'<g transform="translate({x} 196)" stroke="#111"><rect x="-10" y="-20" width="20" height="20" fill="#e8b84a"/><circle cy="-26" r="8" fill="#e8b84a"/></g>' for x in (140,190)))+facts([
 ('Style','Kaliṅga <b>rekha deuḷa</b>: a curved tower on a five-fold (pañcaratha) plan, about 65 m tall'),
 ('Built','Begun under <b>Anantavarman Coḍagaṅga</b> (12th c.), completed or renewed under <b>Anaṅgabhīma III</b>'),
 ('Gates','Four: the main <b>Siṃha Dvāra</b> (Lion Gate) faces east'),
 ('Aruṇa Stambha','A pillar before the Lion Gate, brought from the Sun temple at Koṇārka in the 18th century'),
 ('Patita Pāvana','An image of Jagannātha in the gate passage, visible from the road to all'),
 ('Within','Over a hundred smaller shrines, among them Lakṣmī, Vimalā and Gaṇeśa')])))
pages.append(page('chakra','THE NĪLA CAKRA','The wheel on top',facts([
 ('What','A great wheel of <b>eight metals</b> (aṣṭadhātu) on the very top of the tower'),
 ('Flag','A fresh flag is tied to its mast every day by a servitor who climbs the tower'),
 ('Ekādaśī','A lamp is lit up beside it on Ekādaśī'),
 ('Darśana','Seeing the wheel from outside is held to be as good as seeing the Lord')])
 +talk("Climbing a 65-metre tower every day, by hand?","Every single day, for centuries. The family that does it says the Lord holds the ladder.")))
pages.append(page('kitchen','THE KITCHEN','Mahāprasāda',fig(560,160,'Clay pots stacked in a tower over a wood fire in a huge kitchen',
 '<rect width="560" height="160" fill="#fdf1e8"/>'+''.join(f'<g transform="translate({x} 150)"><path d="M-30 0 l10 -20 h40 l10 20z" fill="#ff8c1a" stroke="#111"/>'+''.join(f'<ellipse cy="{-30-k*22}" rx="{24-k*2}" ry="12" fill="#c0713a" stroke="#111" stroke-width="1.5"/>' for k in range(5))+'</g>' for x in (90,220,350,480)))+facts([
 ('Kitchen','One of the largest temple kitchens in India, run by hereditary cooks'),
 ('Cooking','In clay pots on wood fires; pots are stacked, and tradition says the top one cooks first'),
 ('Offered','To Jagannātha, then to <b>Vimalā</b>: only then does it become <b>mahāprasāda</b>'),
 ('Ānanda Bāzār','The market inside the temple where mahāprasāda is sold and shared'),
 ('No caste','Mahāprasāda is shared from one plate, whoever you are')])
 +talk("Why must it go to Vimalā first?","Jagannātha's food becomes 'mahā' only after the goddess tastes it. Even here, she has the last word.")))
pages.append(page('snana','SNĀNA YĀTRĀ AND ANASARA','The bath and the fever',facts([
 ('Snāna Pūrṇimā','On the full moon of Jyeṣṭha, the deities are brought out and bathed with 108 pots of water from the <b>Sunā Kuā</b>, the golden well'),
 ('Anasara','After the bath they “fall ill” and are hidden from view for about two weeks, given herbal medicines by their own servitors'),
 ('Paṭṭi Diyaṁ','Painted cloth images are worshipped in their place'),
 ('Nava Yauvana','They reappear “young again”, just before the chariot festival')])
 +talk("God catches a fever?","He lives as a member of the family: bathed, fed, put to bed, nursed when ill. That's the sweetness of Purī.")))
pages.append(page('ratha','RATHA YĀTRĀ','The chariot festival',fig(560,190,'Three huge chariots in a row on a broad road, crowds pulling ropes, a king sweeping with a golden broom',
 '<rect width="560" height="190" fill="#fff4cd"/><rect y="160" width="560" height="30" fill="#d8c8a8"/>'+CHARIOT(110,170,1,'#2a9d6f','#c0392b')+CHARIOT(280,170,.9,'#111','#c0392b')+CHARIOT(450,170,1.1,'#ffd60a','#c0392b')
 +''.join(f'<circle cx="{20+i*20}" cy="186" r="5" fill="#c98b5a"/>' for i in range(27)))+facts([
 ('When','Āṣāḍha, in the monsoon'),
 ('Chariots','<b>Nandighoṣa</b> (Jagannātha), <b>Tāladhvaja</b> (Balabhadra), <b>Darpadalana</b> (Subhadrā): built new every year'),
 ('Where to','Along the Grand Road (Baḍa Daṇḍa) to the <b>Guṇḍicā</b> temple, the “aunt’s house”'),
 ('Chherā Pahanrā','The <b>Gajapati</b> king sweeps the chariots with a golden broom: before God, a king is a sweeper'),
 ('Return','After about a week, the <b>Bahuḍā Yātrā</b> brings them home'),
 ('Suna Beśa','Back on the chariots at the gate, they are dressed in gold')])))
pages.append(page('nava','NAVAKALEVARA','A new body',facts([
 ('What','“New body”: the wooden images are replaced with new ones carved from fresh neem'),
 ('When','In a year with an extra (adhika) Āṣāḍha month: usually every 12 to 19 years'),
 ('Finding the trees','Servitors search for neem trees with special signs: a conch or discus mark, a snake’s hole, no birds’ nests, near water and a Śiva shrine'),
 ('The secret','The mysterious <b>brahma padārtha</b>, “divine substance”, is moved from old body to new by blindfolded servitors at night'),
 ('The old','The old images are buried in the <b>Koili Vaikuṇṭha</b> garden within the temple')])
 +talk("God dies and is reborn?","The wood is laid to rest; the life inside moves on. Purī acts out the Gītā's line about changing clothes.")))
pages.append(page('vimala','VIMALĀ','The goddess within',facts([
 ('Who','<b>Vimalā</b>, a form of Durgā, in her own shrine in the inner enclosure'),
 ('Śakti Pīṭha','Counted among the Śakti Pīṭhas: in one tradition the place where Satī’s feet fell'),
 ('Mahāprasāda','Food offered to Jagannātha becomes mahāprasāda only after it is offered to her'),
 ('Durgā Pūjā','Her great festival is in autumn, with special rites'),
 ('Bhairava','Jagannātha himself is called her Bhairava, her guardian')])
 +talk("A Śakti Pīṭha inside a Viṣṇu temple?","Purī keeps every tradition under one roof: Vaiṣṇava, Śākta, Śaiva, even tribal roots.")))
pages.append(page('history','HISTORY','Kings, saints and invasions',tl([
 ('Legend','King <b>Indradyumna</b> builds the first temple.'),
 ('12th c.','<b>Anantavarman Coḍagaṅga</b> of the Eastern Gaṅgas begins the present temple; <b>Jayadeva</b> sings the Gītagovinda.'),
 ('13th c.','<b>Anaṅgabhīma III</b> dedicates his kingdom to Jagannātha, ruling as his deputy.'),
 ('15th c.','<b>Kapilendra Deva</b> declares Jagannātha the true king and himself the first servant.'),
 ('1506','<b>Guru Nānak</b> visits Purī.'),
 ('16th c.','<b>Caitanya</b> lives his last years in Purī, lost in love for Jagannātha.'),
 ('Through history','The temple chronicle, the <b>Mādalā Pāñji</b>, records eighteen invasions; the images were hidden many times.'),
 ('Today','Run by the Shree Jagannath Temple Administration; the Gajapati still performs his rites.')])))
pages.append(page('saints','SAINTS OF PURĪ','Poets and pilgrims',facts([
 ('Jayadeva','12th-c. poet of the <b>Gītagovinda</b>, the love-songs of Rādhā and Kṛṣṇa, still sung in the temple'),
 ('Caitanya','The Bengali saint, founder of Gauḍīya Vaiṣṇavism, lived in Purī for many years'),
 ('Guru Nānak','Visited in 1506; his song of the cosmic āratī is linked to Purī'),
 ('Śaṅkara','Founded the <b>Govardhana Maṭha</b>, the eastern seat, by tradition'),
 ('Rāmānuja','Visited and founded a maṭha here, by tradition')])))
pages.append(page('entry','WHO MAY ENTER','A rule and a debate','''<div class="g2">
<div class="card bg-blue"><h4>📜 The rule</h4><p>Entry is for <b>Hindus</b>; Jains, Sikhs and Buddhists are also admitted, but other non-Hindus and foreigners are not. The temple says the rule is as old as the temple.</p></div>
<div class="card bg-red"><h4>🗣️ The debate</h4><p>Critics point to devout foreign-born Hindus turned away, and to the temple’s past bar on Dalits. Defenders say a living temple sets its own customs. The question returns to the news again and again.</p></div>
</div>
<div class="panel reading"><p><b>For everyone.</b> <b>Patita Pāvana</b>, “saviour of the fallen”, looks out from the gate passage so all can see him; the Nīla Cakra is visible across the town; and on <b>Ratha Yātrā</b> the Lord comes out into the street for all.</p></div>'''
 +talk("So someone who can't go in still gets darśana?","Once a year, Jagannātha goes out to them. That's the whole point of the chariots.")))
pages.append(page('connect','IN THE CHAR DHAM','The abode for our age',facts([
 ('Dhām','The eastern abode of the Bada Char Dham, for <b>Kali Yuga</b>'),
 ('Paired with','<b>Liṅgarāja</b>, Bhubaneswar, Śiva’s temple'),
 ('Maṭha','<b>Govardhana</b>, the eastern Śaṅkara seat, for the Ṛg Veda'),
 ('Śakti Pīṭha','Vimalā, in the wider list of Śakti Pīṭhas'),
 ('Saptapurī','Some lists slip Purī in among the seven sacred cities')])
 +'<div class="key">More: <a href="/bhakti/temples-of-india/char-dham/">Char Dham, the two circuits</a> · <a href="/bhakti/temples-of-india/char-dham/badrinath/">Badrīnāth</a></div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Dāru brahma','God as wood: the sacred neem logs'),('Ratnavedī','The jewelled throne'),('Deuḷa','Odia for temple'),('Ratha','Chariot'),('Yātrā','Procession, journey'),
 ('Mahāprasāda','Food offered to the Lord and Vimalā'),('Anasara','The deities’ sick-room period'),('Navakalevara','New body'),('Gajapati','Title of the kings of Purī'),('Beśa','Dress, adornment')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The god.</b> Jagannātha with Balabhadra, Subhadrā and Sudarśana, in wood, with round unblinking eyes.</div>
<div><b>The legend.</b> Nīla Mādhava of the forest; the log from the sea; the carpenter disturbed too soon.</div>
<div><b>The temple.</b> The Baḍa Deuḷa of the Gaṅga kings, the Nīla Cakra on top, Vimalā within.</div>
<div><b>The year.</b> The bath, the fever, the chariots, and every dozen years or so, a new body.</div>
<div><b>The Dhām.</b> The eastern abode, for Kali Yuga: our own age.</div>
</div>'''+talk("One line to remember?","The Lord of the world is a family man: he bathes, falls ill, visits his aunt, and comes home.")+'<div class="key">Jai Jagannātha! 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple and history:</b> Wikipedia, “Jagannath Temple, Puri” (Indradyumna; Viśvāvasu, Vidyāpati and Lalitā from the Skanda and Brahma Purāṇas; construction after 1112 CE, Anantavarman and Anaṅgabhīma; Kaliṅga style; Mādalā Pāñji and eighteen invasions; images of neem dāru; Sudarśana, Mādhava, Śrīdevī, Bhūdevī; entry rule, exceptions and controversy; Guru Nānak 1506; Caitanya). Wikipedia, “Puri” (Śrī Kṣetra, Baḍa Deuḷa; 65 m / 214 ft; the king sweeping the chariots). Wikipedia, “Jagannath” (etymology; Jagā, Jagabandhu). hindupedia.com (rekha deuḷa, pañcaratha; Kapilendra Deva; kitchen). holydham.com (Aruṇa Stambha from Koṇārka; Patita Pāvana; Rohiṇī Kuṇḍa; Sunā Kuā). adiveda.substack.com, iskcondesiretree.com and thegaudiyatreasuresofbengal.com (Nīla Cakra of eight metals; daily flag; Ekādaśī lamp; Jayadeva; Ānanda Bāzār). anantamias.com and imvoyager.com (chariot names; Guṇḍicā; Chherā Pahanrā; new chariots yearly). bunkarvalley.com (stacked pots).</p>
<p><b>Sources differ:</b> who began and who finished the temple; the exact Navakalevara interval. <b>Not verified, tradition only:</b> the mustard-seed trail; 21 days for the carpenter; the top pot cooking first; the signs on Navakalevara trees and the brahma padārtha; Vimalā’s Pīṭha body part; Rāmānuja’s maṭha; Guru Nānak’s āratī linked to Purī. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('legend','Legend · Nīla Mādhava'),('log','The Log and the Carpenter'),('deities','The Four on the Throne'),('temple','The Baḍa Deuḷa'),('chakra','The Nīla Cakra'),
 ('kitchen','The Kitchen'),('snana','Snāna Yātrā and Anasara'),('ratha','Ratha Yātrā'),('nava','Navakalevara'),('vimala','Vimalā'),('history','History'),('saints','Saints of Purī'),('entry','Who May Enter'),('connect','In the Char Dham'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
bk=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ABODE OF THE EAST</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">PURĪ JAGANNĀTHA</h1>
  <div class="series">CHAR DHAM · A REFERENCE GUIDE</div>
  <div class="tag">The Lord of the World, in wood, by the sea</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>On the sands of Odisha, God is carved in wood, with no hands to speak of and eyes too big to close. He lives with his brother and sister, eats from one of the largest kitchens in India, falls ill after his yearly bath, and once a year rides out on a chariot so huge that English borrowed his name for anything unstoppable.</p>
    <p>This is <b>Jagannātha</b>, Lord of the World, and Purī is his abode: the eastern Dhām, the one for our own age.</p>
    <p>This guide tells his legends, his temple, his festivals and his saints.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Jai Jagannātha,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is Jagannātha Kṛṣṇa or Viṣṇu?","Both, and more. Vaiṣṇavas see Kṛṣṇa; others see Viṣṇu, Śiva-Śakti or the forest god of the Śabaras. He doesn't mind.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Puri_Jagannatha.html','w').write(head+bk+tail())
print('ok',len(pages))
