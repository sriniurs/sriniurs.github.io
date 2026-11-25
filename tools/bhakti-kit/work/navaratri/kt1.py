from kt_common import *
i=0
def hmap():
    o='<rect width="560" height="230" fill="#eadcc0"/><path d="M0 40 q140 20 280 0 t280 10" fill="none" stroke="#8fb8de" stroke-width="16"/>'+T(80,30,'Tuṅgabhadrā (Pampā)',10,fill='#1d4f8a')
    o+=g(120,190,.8,boulders(160,2))+g(470,200,.7,boulders(140,5))
    o+=pin(230,90,'Virūpākṣa temple')+pin(170,140,'Hemakūṭa hill',icon=mountain('#b08a62'))+'<path d="M260 96 h170" stroke="#8a6a3a" stroke-width="6"/>'+T(350,112,'Hampi Bazaar',10)
    o+=pin(440,80,'Mātaṅga hill',icon=mountain('#b08a62'))+pin(510,40,'Vijaya Viṭṭhala',.3)+pin(320,14,'Āñjanādri · Kiṣkindhā (across river)',.3)+pin(300,180,'Manmatha tank',.3)
    return o+T(480,226,'simplified, not to scale',9)
fw=foreword(i,['Among the boulder hills on the Tuṅgabhadrā stand the ruins of Vijayanagara, once among the largest cities in the world. Its palaces fell in 1565, but one temple never stopped its worship: <b>Virūpākṣa</b>, Śiva as the husband of the river goddess Pampā, whose shrine is older than the empire that made it great.',
 'This guide covers the place and its names, the story of Pampā and the burning of Kāma, Hemakūṭa hill, the temple’s growth from a 7th-century shrine to the great complex of the Vijayanagara kings, its gopuras, Kṛṣṇadevarāya’s hall and painted ceiling, the upside-down tower, the river in the kitchen, and the festivals of the god’s betrothal and wedding.',
 'It opens our '+L('/temples-of-india/karnataka/','Temples of Karnataka')+' series. Hampi’s Gaṇeśas are in '+L('/ganesha/temples/hampi/','Hampi’s Gaṇeśas')+'; the Kiṣkindhā of the Rāmāyaṇa in '+L('/vishnu/hanuman/kishkindha/','Hanumān in Kiṣkindhā')+'.'],
 [('z','A living temple in a ruined city?'),('b','The city died; the god did not. Worship at Virūpākṣa has gone on through every century since.')])
gl=glance([('Deity','Śiva as Virūpākṣa or Pampāpati, “husband of Pampā”'),('Goddess','Pampā Devī, goddess of the Tuṅgabhadrā; also Bhuvaneśvarī'),('Place','Hampi, Vijayanagara district, on the south bank of the Tuṅgabhadrā'),('Old names','Pampā-kṣetra, Kiṣkindhā-kṣetra, Bhāskara-kṣetra'),('Age','Worship from about the 7th century; inscriptions to Śiva in the 9th–10th'),('Builders','Cāḷukya and Hoysaḷa additions; the great complex under Vijayanagara'),('Patrons','Lakkaṇa Daṇḍeśa under Devarāya II; Kṛṣṇadevarāya (hall of 1510)'),('East gopura','Nine tiers, about 50 m'),('Festivals','Betrothal and wedding of Virūpākṣa and Pampā (Dec); chariot festival (Feb)'),('Status','Part of the UNESCO Group of Monuments at Hampi')],
 S('The great nine-tiered gopura of Virūpākṣa among boulders by the river',g(280,200,2,GOP(0,0,1,9))+g(90,200,.9,boulders(160,3))+g(470,200,.9,boulders(160,7))+'<path d="M0 214 h560" stroke="#8fb8de" stroke-width="10"/>','#e3eaf3',220),
 [('z','How tall is that tower?'),('b','About fifty metres: nine storeys of brick and stucco on a stone base.')],'Pampā’s husband <b>outlived his empire</b>.')
where=reading('where','WHERE IT IS','A sacred landscape of boulders',svg(560,230,'Simplified map of Hampi: the river, Hemakūṭa, Virūpākṣa, the bazaar, Mātaṅga hill, Vijaya Viṭṭhala and Āñjanādri across the river',hmap()),
 ['<b>The river.</b> The Tuṅgabhadrā, whose old name is <b>Pampā</b>, flows past the temple’s north side; a narrow channel of it runs through the temple.',
  '<b>Hemakūṭa.</b> The low hill beside the temple, covered with small early shrines, is where Śiva did penance before his marriage.',
  '<b>The bazaar.</b> From the east gopura a long street, Hampi Bazaar, runs east to the foot of Mātaṅga hill; it once held the market and the chariot route.',
  '<b>Kiṣkindhā.</b> Across the river lies Āñjanādri, held to be Hanumān’s birthplace, in the Kiṣkindhā of the Rāmāyaṇa.',
  '<b>The ruins.</b> Beyond lie the royal centre and the great temples of Vijaya Viṭṭhala and others, all ruined in 1565.'],
 [('z','Why build a capital among boulders?'),('b','A river on one side, rock walls all round: a natural fortress. And an old holy place at its heart.')],'A holy place <b>became a capital</b>.')
name=reading('name','THE NAMES','Pampā, Hampi and Virūpākṣa',
 S('A river goddess and a three-eyed Śiva with the words Pampā to Hampe to Hampi',g(120,190,1.4,devi(sari='#2a9d6f',items=('lotus',)))+T(120,206,'Pampā')+g(440,190,1.4,SHIVA(0,0,1))+T(440,206,'Virūpākṣa')+T(280,90,'Pampā → Hampe → Hampi',16,fill='#1d4f8a'),'#e3eaf3',215),
 ['<b>Pampā.</b> The old name of the Tuṅgabhadrā, and of the local goddess of the river, identified with Pārvatī.',
  '<b>Hampi.</b> The town’s name is Pampā worn down by speech: Pampā, Hampe, Hampi. The place was Pampā-kṣetra, “the field of Pampā”.',
  '<b>Pampāpati.</b> Śiva here is “husband of Pampā”: the god married the local river goddess.',
  '<b>Virūpākṣa.</b> “He of the odd eye”: Śiva’s third eye, the eye that burned Kāma.',
  '<b>Kiṣkindhā.</b> The area is also called Kiṣkindhā-kṣetra after the kingdom of Vālī and Sugrīva in the Rāmāyaṇa; the Pampā lake of the epic is placed nearby.'],
 [('z','A god named after his strange eye?'),('b','After the eye that ended desire’s attack. The name tells the whole story of this place in one word.')],'A river’s name <b>became a city’s</b>.')
pampa=story('pampa','STORY · PAMPĀ AND KĀMA','How the ascetic became a husband',
 strip('Three panels: Śiva in meditation on a hill; Kāma shooting a flower arrow and burnt by the third eye; Śiva and Pampā married with gold showering down',
  [('<rect width="144" height="190" fill="#eadcc0"/>'+g(72,160,.8,mountain('#b08a62'))+g(72,120,.6,SHIVA(0,0,1)),'#eadcc0'),
   ('<rect width="144" height="190" fill="#3a2a50"/>'+g(40,170,.8,person('#e05050'))+'<path d="M56 110 l40 -20" stroke="#ffd60a" stroke-width="2"/>'+g(110,130,.5,SHIVA(0,0,1))+g(40,90,1,flame(1,'#ff8c1a')),'#3a2a50'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(50,170,.55,SHIVA(0,0,1))+g(100,170,.75,devi(sari='#2a9d6f',items=()))+''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#e0a800"/>' for x in range(10,144,18) for y in (20,40)),'#fff3cf')],
  ['penance on Hemakūṭa','the third eye','a rain of gold']),'The legend of Pampā-kṣetra, as told at Hampi.',
 ['After the death of Satī, Śiva came south and sat in deep penance on <b>Hemakūṭa</b> hill.',
  '<b>Pampā</b>, the river goddess, a form of Pārvatī (in one telling Brahmā’s daughter), set her heart on him and did penance to win him.',
  'The gods sent <b>Kāma</b>, god of love, to break Śiva’s meditation. Kāma shot a flower arrow; Śiva opened his third eye and burned him to ashes.',
  'Yet the arrow had found its mark. Pleased with Pampā’s devotion, Śiva married her and became <b>Pampāpati</b> and <b>Virūpākṣa</b>.',
  'At the wedding the gods showered gold on the hill: hence <b>Hemakūṭa</b>, “heap of gold”. The great tank near the temple is named for Manmatha (Kāma).'],
 [('z','The love god burned, and the wedding happened anyway?'),('b','That is the point. Desire is burned; love stays. The third eye ends lust, not devotion.')],'Desire burned, <b>love stayed</b>.')
hema=reading('hemakuta','HEMAKŪṬA','The hill of the oldest shrines',
 S('A low rocky hill covered with small stone shrines with stepped roofs',g(280,200,2.4,mountain('#b08a62'))+''.join(g(160+k*60,150-(k%2)*20,.5,'<rect x="-20" y="-24" width="40" height="24" fill="#a7a08c"/>'+''.join(f'<path d="M{-20+j*3} {-24-j*6} h{40-j*6} v-6 h{-(40-j*6)}z" fill="#8f8a7a"/>' for j in range(4))) for k in range(5)),'#eadcc0',210),
 ['<b>Where it began.</b> The worship of Pampā and her Lord is far older than Vijayanagara. Hemakūṭa hill, beside the temple, holds a cluster of early shrines.',
  '<b>Mūla Virūpākṣa.</b> A small early shrine on the hill, by a spring-fed pond, is held to mark the place of Śiva’s penance; it is called the “original” Virūpākṣa.',
  '<b>Stepped roofs.</b> Many Hemakūṭa shrines have pyramidal stepped stone roofs of an early Deccan style.',
  '<b>From local to great.</b> Historians trace how a local Śaiva pilgrimage centre of Pampā and Bhairava grew into the great centre of Virūpākṣa worship.',
  '<b>Views.</b> From the hill you look down on the temple’s great gopura and the bazaar.'],
 [('z','So the big temple is the younger one?'),('b','The big buildings are younger; the worship is older. Hemakūṭa keeps the memory of the small beginning.')],'Small shrines <b>where it began</b>.')
hist=reading('history','THE KINGS’ GOD','From a shrine to an empire’s temple',
 svg(560,150,'Timeline of the Virūpākṣa temple','<rect width="560" height="150" fill="#fff3cf"/>'+tl_strip([('c. 7th c.','worship begins'),('9–10th c.','Śiva inscriptions'),('12th c.','Cāḷukya, Hoysaḷa'),('1336','Vijayanagara'),('15th c.','Lakkaṇa Daṇḍeśa'),('1510','Kṛṣṇadevarāya'),('1565','city falls')],560,150)),
 ['<b>Before the empire.</b> Worship here runs from about the 7th century; inscriptions to Śiva date from the 9th and 10th centuries, with additions in the late Cāḷukya and Hoysaḷa periods.',
  '<b>Vijayanagara.</b> When the empire’s capital rose here in the 14th century, Virūpākṣa became the kings’ own god; tradition says the empire’s founders acted in his name. (Tradition.)',
  '<b>Lakkaṇa Daṇḍeśa.</b> The great complex is credited to <b>Lakkaṇa Daṇḍeśa</b>, a chieftain under Devarāya II, in the 15th century.',
  '<b>Kṛṣṇadevarāya.</b> The greatest emperor built the central pillared hall in 1510 to mark his accession, and is credited with the inner gateway and the eastern gopura works.',
  '<b>1565 and after.</b> The city was destroyed after the battle of Talikota, but worship at Virūpākṣa never stopped; in the early 19th century its broken north and east gopuras were restored.'],
 [('z','Why did Virūpākṣa survive when the city didn’t?'),('b','Because it was a living temple with priests and pilgrims who kept coming back. Stone needs people to keep it alive.')],'An empire rose <b>around an older god</b>.')
def plan():
    o='<rect width="560" height="230" fill="#eadcc0"/><rect x="60" y="40" width="300" height="150" fill="#d9c7a0"/><rect x="380" y="60" width="140" height="110" fill="#e9dcc0"/>'
    o+='<rect x="520" y="95" width="30" height="40" fill="#a0522d"/>'+T(535,150,'east gopura',9)+'<rect x="364" y="100" width="20" height="30" fill="#a0522d"/>'+T(374,146,'1510 gopura',9)
    o+='<rect x="150" y="80" width="150" height="70" fill="#c9a36b"/>'+T(225,118,'raṅga maṇḍapa (1510)',9)+'<rect x="90" y="95" width="60" height="40" fill="#8a6a3a"/>'+T(120,90,'sanctum',9)
    o+='<rect x="200" y="20" width="30" height="24" fill="#a0522d"/>'+T(215,14,'Kanakagiri (north) gopura',9)+'<path d="M20 30 C120 30 140 200 300 210" fill="none" stroke="#4aa3df" stroke-width="5"/>'+T(60,215,'river channel',9,fill='#1d4f8a')
    o+=T(450,186,'outer court',9)+T(260,180,'inner court',9)
    return o+T(470,226,'simplified plan; east to the right',9)
temple=reading('temple','THE TEMPLE','Courts, halls and gateways',svg(560,230,'Simplified plan of the Virūpākṣa temple: outer court, inner court, sanctum, halls and gopuras',plan()),
 ['<b>Facing east.</b> The temple faces east, toward the bazaar and the sunrise; its main axis runs west to the sanctum.',
  '<b>Two courts.</b> The great east gopura leads into an outer court; a smaller gopura of 1510 leads into the inner court with the main shrine.',
  '<b>The main temple.</b> A sanctum, three antechambers, a pillared hall and an open pillared hall, with delicately carved pillars, surrounded by cloisters, gateways and smaller shrines.',
  '<b>The north gate.</b> The <b>Kanakagiri gopura</b> opens north toward the river.',
  '<b>Other shrines.</b> Pampā Devī and Bhuvaneśvarī have their own shrines in the complex.'],
 [('z','Why so many gates?'),('b','Every king added one. A temple this old is a record of everyone who loved it.')],'A temple <b>built in layers by kings</b>.')
gop=reading('gopura','THE GOPURAS','Nine storeys over the bazaar',
 S('The east gopura with its tiers and the smaller inner gopura behind',g(200,210,2.2,GOP(0,0,1,9))+g(420,210,1.4,GOP(0,0,1,5)),'#e3eaf3',220),
 ['<b>The east gopura.</b> The largest gateway has <b>nine tiers</b> and rises about 50 m: a brick superstructure on a stone base, covered in stucco figures.',
  '<b>Its date.</b> The great tower is commonly dated to the 15th century (1442 is often cited) and was restored in the early 19th century.',
  '<b>The inner gopura.</b> A smaller gateway of 1510 leads to the inner court; Kṛṣṇadevarāya is credited with it.',
  '<b>Kanakagiri.</b> The north gopura faces the river.',
  '<b>Repeating patterns.</b> Observers note that the tower’s forms divide and repeat as they rise, like a snowflake; the overall shape is a triangle. (Observation.)'],
 [('z','Why build the gateway taller than the shrine?'),('b','South Indian temples do this from Vijayanagara times on: the gopura announces the god to the whole city. The sanctum stays small and dark, as it should.')],'A tower <b>that announces the god</b>.')
hall=reading('ranga','KṚṢṆADEVARĀYA’S HALL','The raṅga maṇḍapa and its painted ceiling',
 S('A pillared hall with lion-pillars and a painted ceiling of gods and processions',''.join(g(60+k*90,200,1,'<rect x="-10" y="-120" width="20" height="120" fill="#a7a08c"/><path d="M-14 -60 q14 -30 28 0" fill="#8f8a7a"/>') for k in range(6))+'<rect x="40" y="20" width="480" height="60" fill="#c0392b"/>'+''.join(g(80+k*80,70,.4,[SHIVA(0,0,1),devi(items=()),person('#e0a800'),SHIVA(0,0,1),devi(items=()),person('#1d4f8a')][k]) for k in range(6)),'#eadcc0',210),
 ['<b>1510.</b> Kṛṣṇadevarāya built the central pillared hall, the <b>raṅga maṇḍapa</b>, to mark his accession; an inscribed stone plaque beside it records this.',
  '<b>The pillars.</b> Its pillars carry rearing mythical beasts (yāḷis) with riders, a hallmark of Vijayanagara art.',
  '<b>The ceiling.</b> The ceiling is painted, among the few Vijayanagara paintings to survive; the paintings date from the 14th to 16th centuries. Scenes commonly described include the wedding of Śiva and Pampā and episodes from the epics. (Description varies.)',
  '<b>Used for festivals.</b> The halls were used to display the deities during music, dance and drama, and for the deities’ wedding rites.',
  '<b>Read more.</b> On reading temple halls, see '+L('/temples-of-india/how-to-read-a-hindu-temple/','How to Read a Hindu Temple')+'.'],
 [('z','Paintings that survived 1565?'),('b','Inside a living temple, yes. The ruined halls lost theirs; the working temple kept its roof.')],'An emperor’s hall <b>with a painted sky</b>.')
shadow=reading('shadow','THE UPSIDE-DOWN TOWER','An image through a slit',
 S('Light from the gopura passing through a narrow slit and forming an inverted image of the tower on a dark wall',g(110,200,1.4,GOP(0,0,1,7))+'<rect x="300" y="20" width="20" height="180" fill="#5a3a1a"/><rect x="306" y="100" width="8" height="14" fill="#ffd60a"/>'+'<path d="M150 80 L310 106 L470 170 M150 200 L310 108 L470 40" stroke="#ffd60a" stroke-width="1.5" stroke-dasharray="4 4"/>'+'<rect x="440" y="20" width="100" height="180" fill="#3a3a3a"/>'+'<g transform="translate(490 30) scale(.7 -.7)">'+GOP(0,0,1,7).replace('fill="#f2e6c8"','fill="#8a8a6a"').replace('fill="#e2cfa8"','fill="#6a6a5a"')+'</g>','#eadcc0',215),
 ['<b>The effect.</b> In a dark chamber of the temple, an <b>inverted image</b> of the main gopura falls on the wall, upside down.',
  '<b>How.</b> Light from the tower passes through a narrow opening into the dark room and forms an image, the principle of the pinhole camera (camera obscura).',
  '<b>Designed or chance?</b> Many guides call it a deliberate marvel of the builders; others think it may be a happy accident. (Opinions differ.)',
  '<b>Mysticism.</b> For pilgrims it adds a quiet wonder to the visit: the god’s gateway, reversed, inside the temple.',
  '<b>Look for it.</b> Guides point visitors to the chamber; the image is clearest when the sun is bright.'],
 [('z','A camera in a medieval temple?'),('b','A camera is just a dark box with a hole. The builders certainly understood light, whether or not they planned this.')],'Light through a slit <b>turns the tower over</b>.')
sanct=reading('sanctum','THE SANCTUM AND THE RIVER','Mukha-liṅga, Pampā and the kitchen stream',
 S('A liṅga with a brass face in the sanctum; a channel of river water flowing through a temple kitchen',g(150,200,1.6,LINGA(0,0,1))+'<circle cx="150" cy="136" r="16" fill="#e0a800"/>'+'<rect x="300" y="140" width="240" height="20" fill="#4aa3df"/>'+g(420,140,1,'<rect x="-40" y="-40" width="80" height="40" fill="#e9d6c0"/>')+g(480,130,.8,'<ellipse rx="20" ry="10" fill="#5a3a1a"/>'+flame(.6,'#ff8c1a')),'#eadcc0',210),
 ['<b>The god.</b> The sanctum holds a <b>mukha-liṅga</b>: a Śiva liṅga with a face of the Lord in brass.',
  '<b>The goddess.</b> Pampā Devī, the river goddess, has her own shrine nearby, as does Bhuvaneśvarī. Together they are the divine household of the place.',
  '<b>The river inside.</b> A narrow channel of the Tuṅgabhadrā runs along the temple terrace, down through the temple <b>kitchen</b>, and out through the outer court.',
  '<b>Why.</b> Running river water for cooking and worship, brought inside the walls: a practical and sacred plan. (Interpretation.)',
  '<b>Lakṣmī.</b> The temple elephant, Lakṣmī, blesses pilgrims with her trunk.'],
 [('z','A river through the kitchen?'),('b','Pampā cooks for her husband, people like to say. The water of the goddess feeds the god’s household.')],'The river goddess <b>flows through her husband’s house</b>.')
fest=reading('festivals','THE BETROTHAL AND THE WEDDING','Festivals of Pampā and Virūpākṣa',
 S('A wedding procession of Śiva and Pampā images under a canopy, and a chariot on the bazaar street',g(150,200,1,'<rect x="-60" y="-90" width="120" height="8" fill="#e0a800"/><path d="M-56 -82 v82 M56 -82 v82" stroke-width="3"/>'+g(-20,0,.6,SHIVA(0,0,1))+g(24,0,.7,devi(sari='#2a9d6f',items=())))+g(410,205,1.4,RATHA(0,0,1,'#c0392b'))+g(410,210,1,crowd(6,200,0,.45)),'#e3eaf3',215),
 ['<b>Phalapūjā.</b> In December the temple celebrates the <b>betrothal</b> of Virūpākṣa and Pampā, the Phalapūjā, drawing large crowds.',
  '<b>Kalyāṇa.</b> The wedding follows, re-enacting the legend of the place; the temple’s halls were built for such wedding rites.',
  '<b>The chariot.</b> In February (Phālguna) the annual <b>chariot festival</b> draws the deities down the bazaar street.',
  '<b>Śivarātri and Kārtika.</b> As at every Śiva temple, Mahāśivarātri and the Kārtika lamps are great days. See '+L('/festivals/maha-shivaratri/','Mahāśivarātri')+'.',
  '<b>Hampi Utsav.</b> A state cultural festival, the Hampi Utsav, is also held among the monuments. (Not a temple festival.)'],
 [('z','A god who gets married every year?'),('b','Every year the coastal and Deccan temples re-enact their god’s wedding. It renews the bond between the god, the goddess and the place.')],'A wedding <b>renewed every year</b>.')
around=cards('around','AROUND VIRŪPĀKṢA','The sacred centre of Hampi',
 S('Boulders, a stone chariot, a giant Gaṇeśa and a hill across the river',g(100,200,.9,boulders(160,4))+g(240,200,1.1,'<rect x="-30" y="-50" width="60" height="50" fill="#a7a08c"/><circle cx="-24" cy="0" r="12" fill="#8f8a7a"/><circle cx="24" cy="0" r="12" fill="#8f8a7a"/><path d="M-30 -50 l30 -30 l30 30z" fill="#8f8a7a"/>')+T(240,214,'stone chariot',9)+g(380,200,1.2,ganesha())+g(500,200,1,mountain('#b08a62')),'#eadcc0',215),
 [('🐘','Sāsivekāḷu and Kaḍalekāḷu','The giant Gaṇeśas on Hemakūṭa. See '+L('/ganesha/temples/hampi/','Hampi’s Gaṇeśas')+'.'),('🛕','Vijaya Viṭṭhala','The great temple with the stone chariot and musical pillars, in ruins.'),('🐒','Āñjanādri','Across the river, held to be Hanumān’s birthplace. See '+L('/vishnu/hanuman/kishkindha/','Kiṣkindhā')+'.'),('🦁','Ugra Narasiṃha','A huge monolithic Narasiṃha carved in 1528.'),('🌊','Pampā Sarovar','A lake linked with the Rāmāyaṇa’s Śabarī.'),('⛰️','Mātaṅga hill','The hill at the end of the bazaar, with views over the ruins.')],
 None,'A whole sacred landscape <b>around one living temple</b>.')
endp=end(i,['<b>God.</b> Virūpākṣa, Śiva of the third eye, husband of the river goddess Pampā.','<b>Story.</b> Penance on Hemakūṭa, Kāma burned, the wedding and the rain of gold.','<b>History.</b> From a 7th-century shrine to the Vijayanagara kings’ temple; never abandoned.','<b>Temple.</b> Nine-tiered gopura, 1510 hall, painted ceiling, the upside-down tower, the river in the kitchen.','<b>Festivals.</b> The betrothal and wedding in December; the chariot in February.'],
 'Part 2 goes to the Hoysaḷa temples of Belūr and Haḷebīḍu.','Pampā’s husband outlived his empire')
src=sources([('Temple:','Wikipedia, “Virupaksha Temple, Hampi” and “Hampi”; Incredible India (gopura, inverted shadow, legend); Britannica; Google Arts & Culture / Incredible India (1442 gopura); Anantam IAS notes; Hindustan Times (Mūla Virūpākṣa, Manmatha tank); hampi.in (Pampā, Hemakūṭa, gold shower); Hindu Blog (Satī, Kāma, third eye).')],
 'the date of the east gopura (1442 is widely cited but not confirmed by the main encyclopedia source); Lakkaṇa Daṇḍeśa’s role (uncited in the main source); the subjects of the ceiling paintings; whether the inverted image was designed; tradition of the founders acting in Virūpākṣa’s name.','Festival months as reported.')
finish(i,'PART 1 OF 5 · PAMPĀ · THE GOPURA · VIJAYANAGARA',covart('The great gopura of Virūpākṣa among boulders by the river',g(220,190,1.7,GOP(0,0,1,9))+g(70,190,.8,boulders(120,3))+g(370,190,.8,boulders(120,6))),'The living temple of a ruined city',
 'Virūpākṣa of <b>Hampi</b>: the legend of <b>Pampā</b> and the burning of Kāma, the temple of the <b>Vijayanagara</b> kings, its gopuras, painted hall and upside-down tower, and its festivals.',
 'Virūpākṣa temple at Hampi explained and illustrated: Pampā and Pampāpati, the burning of Kāma on Hemakūṭa, the temple’s history from the 7th century through Vijayanagara and Kṛṣṇadevarāya, the nine-tiered gopura, the painted raṅga maṇḍapa, the inverted shadow, and the betrothal, wedding and chariot festivals.',
 [fw,gl,where,name,pampa,hema,hist,temple,gop,hall,shadow,sanct,fest,around,endp,src])
