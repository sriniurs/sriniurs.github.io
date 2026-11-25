from tn_common import *
from fig2 import krishna_child
i=2
MATHAS=['Pejāvara','Palimāru','Adamāru','Puttige','Sōde','Kāṇiyūru','Śirūru','Kṛṣṇāpura']
def square():
    o='<rect width="560" height="240" fill="#e9f2e1"/><rect x="120" y="30" width="320" height="180" fill="#d9c7a0"/><rect x="150" y="55" width="260" height="130" fill="#e9f2e1"/>'
    o+=T(280,24,'Ratha Bīdi · Car Street (procession always clockwise)',10)
    o+=g(250,140,.7,tulu_temple('#e0a800','#b8860b'))+T(250,160,'Kṛṣṇa Maṭha',10)+'<rect x="300" y="100" width="60" height="40" fill="#4aa3df"/>'+T(330,154,'Madhva Sarovara',9)
    o+=g(190,110,.4,tulu_temple())+T(190,124,'Anantēśvara',9)+g(370,180,.4,tulu_temple())+T(370,194,'Candramaulīśvara',9)
    for k,m in enumerate(MATHAS):
        x=[100,100,100,100,460,460,460,460][k]; y=[50,95,140,185][k%4]
        o+=f'<rect x="{x-14}" y="{y-10}" width="28" height="16" fill="#a0522d"/>'+txt(x+(-20 if x<200 else 20),y+2,m,9,'end' if x<200 else 'start',font=NS,weight='700')
    return o+T(500,234,'simplified, not to scale',9)
fw=foreword(i,['In Uḍupi the year is a chain of chariots. Seven nights of them in January, a raft of lamps on the temple tank, a clay Kṛṣṇa pulled round the square while cowherds smash pots of curd, and every second January the night when the Lord passes from one svāmi to the next.',
 'This guide is the festival year of the <b>Kṛṣṇa Maṭha</b>: the Saptotsava and Makara Saṅkrānti, the <b>Paryāya</b>, the eight maṭhas, <b>Kṛṣṇa Janmāṣṭamī</b> with its midnight offering, <b>Viṭla Piṇḍi</b> and the curd pots, the huli vēṣa, and the days of Madhva.',
 'The temple itself is in '+L('/tulunadu/temples/udupi-srikrishna/','Uḍupi Śrīkṛṣṇa')+'. Previous: '+L('/tulunadu/festivals/mangaluru-dasara/','Maṅgaḷūru Dasarā')+'.'],
 [('z','A whole year of festivals for one image?'),('b','For one image and eight monasteries that take turns serving it. Uḍupi never runs out of reasons to pull a chariot.')])
gl=glance([('Where','Śrī Kṛṣṇa Maṭha, Uḍupi, on the square called Ratha Bīdi (Car Street)'),('Deity','Bālakṛṣṇa with a churning rod, installed by Madhvācārya'),('Served by','Eight Mādhva maṭhas (Aṣṭa Maṭhas), in turn'),('Paryāya','Handover every two years on 18 January, in even years'),('Saptotsava','Seven nights of chariots ending at Makara Saṅkrānti'),('Janmāṣṭamī','By the solar month: the aṣṭamī of Siṃha, with a midnight arghya'),('Viṭla Piṇḍi','Next day: a clay Kṛṣṇa on the golden chariot and the curd pots (mosaru kuḍike)'),('Tigers','Huli vēṣa troupes, above all at Aṣṭami'),('Madhva','Madhva Jayantī (Vijayadaśamī) and Madhva Navamī'),('Season','Chariots nightly from Utthāna Dvādaśī to the Bhāgīrathī festival')],
 S('The Kṛṣṇa Maṭha with three chariots before it',g(280,190,1.1,tulu_temple('#e0a800','#b8860b',160))+g(100,195,1.1,RATHA(0,0,1,'#c0392b'))+g(460,195,1,RATHA(0,0,1,'#1d4f8a'))+g(170,200,.7,RATHA(0,0,1,'#2a9d6f')),'#e3eaf3',210),
 [('z','Why 18 January?'),('b','It is the date the Paryāya has kept for generations, fixed by the solar calendar of the coast.')],'One image, eight maṭhas, <b>a year of chariots</b>.')
sq=reading('square','THE TEMPLE SQUARE','Car Street and the eight maṭhas',svg(560,240,'Simplified plan of Uḍupi’s Car Street with the Kṛṣṇa Maṭha, Madhva Sarovara, Anantēśvara, Candramaulīśvara and the eight maṭhas',square()),
 ['<b>Ratha Bīdi.</b> The Kṛṣṇa Maṭha stands inside a square of streets, <b>Car Street</b>, wide enough for the great chariots. Every procession circles it, always clockwise.',
  '<b>Three shrines.</b> Kṛṣṇa’s maṭha is the youngest of three on the square: <b>Anantēśvara</b>, an ancient Śiva temple, and <b>Candramaulīśvara</b>, Śiva of the Moon, are older. Kṛṣṇa’s festivals always honour them.',
  '<b>Madhva Sarovara.</b> The temple tank beside the shrine, where Madhva first bathed the image; its water is honoured as the Gaṅgā, Bhāgīrathī.',
  '<b>Eight maṭhas.</b> Around the square stand the eight monasteries Madhva founded: Pejāvara, Palimāru, Adamāru, Puttige, Sōde, Kāṇiyūru, Śirūru and Kṛṣṇāpura. Their svāmis serve Kṛṣṇa in turn.',
  '<b>The kitchen.</b> Free meals are served every day; the Bhojanaśāle and the open hall, the Rājāṅgaṇa, are part of every festival.'],
 [('z','Clockwise only?'),('b','Pradakṣiṇā: you keep the deity on your right. A chariot follows the same rule as a pilgrim.')],'A square of streets <b>built for chariots</b>.')
sapt=story('saptotsava','SAPTOTSAVA','Seven nights to Makara Saṅkrānti',
 strip('Three panels: a decorated raft with lamps floating on the temple tank; three chariots on Car Street at night; the great chariot pulled by day',
  [('<rect width="144" height="190" fill="#20243a"/>'+g(72,170,1,tank(130))+g(72,150,.9,raft()),'#20243a'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(40,170,.7,RATHA(0,0,1,'#c0392b'))+g(100,170,.6,RATHA(0,0,1,'#1d4f8a')),'#20243a'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(72,170,.9,RATHA(0,0,1,'#c0392b'))+g(30,180,.6,crowd(4,40,0,.6)),'#fff3cf')],
  ['the raft','three chariots','Cūrṇotsava']),'The great winter festival of the Kṛṣṇa Maṭha, marking the day the image was installed.',
 ['For seven nights before Makara Saṅkrānti, the festival images ride round Car Street each evening.',
  'On the earlier nights only the two smaller chariots run.',
  'On Saṅkrānti night the images are carried in the golden palanquin to Madhva Sarovara and floated three times round the tank on a decorated raft.',
  'Then three chariots: Kṛṣṇa in the great <b>Brahmaratha</b>, Mukhyaprāṇa (Hanumān) in the <b>Garuḍa Ratha</b>, and Anantēśvara with Candramaulīśvara in the <b>Mahāpūjā Ratha</b>.',
  'The next day is <b>Cūrṇotsava</b>, the daylight run of the great chariot.'],
 [('z','Why Saṅkrānti?'),('b','Tradition holds that Madhva installed the image on Makara Saṅkrānti. The festival is the image’s own birthday.')],'Seven nights of chariots <b>for the image’s birthday</b>.')
prep=reading('paryaya-prep','PARYĀYA · GETTING READY','Plantains, rice and firewood',
 S('Workers planting plantain saplings, stacking sacks of rice and a pile of firewood',g(110,180,1.1,banana())+g(70,190,1,person('#2a9d6f'))+g(280,190,1,'<rect x="-50" y="-40" width="100" height="40" fill="#e9d6c0"/><path d="M-50 -20 h100 M-16 -40 v40 M16 -40 v40" stroke-width="1.5"/>')+T(280,205,'akki · rice',10)+g(450,190,1,''.join(f'<rect x="-50" y="{-k*10}" width="100" height="8" rx="4" fill="#8a6a3a"/>' for k in range(1,6)))+T(450,205,'kaṭṭige · firewood',10)+T(110,205,'bāḷe · plantain',10),'#fff3cf',215),
 ['<b>Two years of service.</b> At each Paryāya one of the eight maṭhas takes charge of Kṛṣṇa’s worship and of the kitchen that feeds every visitor, for two years.',
  '<b>Bāḷe muhūrta.</b> Long before the day, the incoming maṭha plants plantains, the first of a chain of auspicious starts.',
  '<b>Akki muhūrta.</b> Then rice is stored for the kitchen.',
  '<b>Kaṭṭige muhūrta.</b> Then firewood is stacked: enough to cook for two years of pilgrims.',
  '<b>A last pilgrimage.</b> The incoming svāmi travels to holy places beforehand, because once in office he may not leave Uḍupi.'],
 [('z','Plantains before the ceremony?'),('b','A kitchen that will feed thousands a day needs leaves to serve on and fruit to offer. The planning starts in the soil.')],'Two years of feeding <b>begin with a sapling</b>.')
paryaya=story('paryaya','PARYĀYA · THE HANDOVER','The night the Lord changes hands',
 strip('Three panels: a svāmi bathing at dawn in a tank; a night procession through lit streets; one svāmi handing a vessel and ladle to another',
  [('<rect width="144" height="190" fill="#20243a"/>'+g(72,170,1,tank(120))+g(72,150,.8,sage('#ff8c1a')),'#20243a'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(72,170,.8,sage('#ff8c1a'))+lamps_row(16,180,7,18,.4)+g(72,60,.6,fireworks()),'#20243a'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(40,170,.8,sage('#ff8c1a'))+g(104,170,.8,sage('#ff8c1a'))+g(72,110,.6,'<ellipse rx="14" ry="10" fill="#c9a36b"/>'),'#fff3cf')],
  ['Daṇḍatīrtha','through the town','the vessel and the ladle']),'The Paryāya of 18 January, every second year, in even-numbered years.',
 ['Before dawn the incoming svāmi bathes at <b>Daṇḍatīrtha</b> near Kāpu, where Madhva studied.',
  'He rides in procession through the night-lit town, with tableaux and music, to Car Street.',
  'He worships first at <b>Anantēśvara</b> and <b>Candramaulīśvara</b>, then takes darśan of Kṛṣṇa.',
  'The outgoing svāmi receives him and hands over the <b>Akṣaya Pātra</b>, the vessel from Madhva, and the <b>sattuga</b>, the serving ladle.',
  'He takes his seat on the <b>Sarvajña Pīṭha</b>, Madhva’s throne, and the darbār begins. For two years he stands in for Madhva.'],
 [('z','A ladle as a symbol of power?'),('b','Of service. Whoever holds the ladle holds the kitchen, and the kitchen is half of Uḍupi’s worship.')],'Power handed over <b>as a ladle</b>.')
mathas=reading('mathas','THE EIGHT MAṬHAS','Madhva’s eight monasteries',
 S('Eight small monastery buildings in a ring around a central temple',g(280,140,.8,tulu_temple('#e0a800','#b8860b'))+''.join(g(280+190*__import__('math').cos(__import__('math').radians(k*45)),130+70*__import__('math').sin(__import__('math').radians(k*45)),.35,tulu_temple()) for k in range(8)),'#e3eaf3',200),
 ['<b>Founded by Madhva.</b> Madhvācārya (13th century), the teacher of Dvaita Vedānta, installed the Kṛṣṇa image and gave its worship to eight disciples, each the head of a maṭha: the <b>Aṣṭa Maṭhas</b>.',
  '<b>Their names.</b> '+', '.join(MATHAS[:-1])+' and '+MATHAS[-1]+'. Their buildings stand on the streets around the square.',
  '<b>Paired.</b> The maṭhas are traditionally grouped in four pairs, the partners standing in for each other when needed. (Traditions differ on the details.)',
  '<b>Taking turns.</b> In tradition the turn was once short; the great svāmi <b>Vādirāja</b> of Sōde (16th century) is credited with fixing it at two years. With eight maṭhas, a svāmi’s turn comes round every sixteen years.',
  '<b>Svāmis for life.</b> Each maṭha is headed by a sannyāsin who takes a successor as a young disciple; many svāmis serve three or four Paryāyas in a lifetime.'],
 [('z','How long is the full cycle?'),('b','Eight maṭhas times two years: sixteen years before a svāmi’s turn comes again.')],'Eight turns, <b>sixteen years round</b>.')
janma=reading('janmashtami','KṚṢṆA JANMĀṢṬAMĪ','The midnight offering',
 S('The child Kṛṣṇa in a cradle at midnight, a svāmi pouring an offering of water, tulasī leaves heaped below',
  '<rect width="560" height="200" fill="#20243a"/>'+g(500,40,1,moon())+g(280,180,1.3,krishna_child())+g(400,180,1,sage('#ff8c1a'))+g(380,120,.7,'<path d="M0 0 q10 -10 20 0" fill="none" stroke="#8fd3ff" stroke-width="3"/>')+g(140,190,1,''.join(f'<ellipse cx="{x}" cy="{-y}" rx="6" ry="3" fill="#3a9a4a"/>' for x in range(-40,41,10) for y in (0,6,12))),'#20243a',200),
 ['<b>By the sun.</b> Most of India keeps Kṛṣṇa’s birth on the lunar aṣṭamī of Śrāvaṇa. Uḍupi follows the solar calendar of the coast and keeps it on the aṣṭamī in the solar month of <b>Siṃha</b>, so its date can differ from the rest of the country.',
  '<b>Lakṣa tulasī.</b> The day begins with the <b>Lakṣa Tulasī Arcane</b>, worship with a hundred thousand tulasī leaves; in some years a crore.',
  '<b>Arghya.</b> At the moment of the birth, near midnight, the Paryāya svāmi offers <b>arghya</b>, milk and holy water with bilva leaves, to the newborn Kṛṣṇa, and devotees offer it after him.',
  '<b>The sweets.</b> The maṭha kitchens make laddus (uṇḍe) and cakkulis by the lakh for the next day’s prasāda; one year’s report counts about 1.5 lakh of each and some 80 cooks.',
  '<b>Little Kṛṣṇas.</b> Children dressed as Kṛṣṇa compete in “Muddu Kṛṣṇa” contests at the Rājāṅgaṇa.'],
 [('z','Why does the date move?'),('b','Because the coast counts by the sun. Uḍupi and the rest of India sometimes celebrate a month apart.')],'Kṛṣṇa born <b>at midnight, by the sun</b>.')
vitla=story('vitla-pindi','VIṬLA PIṆḌI','The clay Kṛṣṇa and the curd pots',
 strip('Three panels: a clay Kṛṣṇa on the golden chariot; cowherds swinging sticks at clay pots hung from tall poles; the clay image immersed in the tank',
  [('<rect width="144" height="190" fill="#fff3cf"/>'+g(72,180,.9,RATHA(0,0,1,'#e0a800'))+g(72,96,.5,krishna_child()),'#fff3cf'),
   ('<rect width="144" height="190" fill="#e9f2e1"/>'+g(72,60,1,'<path d="M-50 0 h100" stroke="#8a6a3a" stroke-width="5"/><path d="M-40 0 v120 M40 0 v120" stroke="#8a6a3a" stroke-width="5"/>'+g(0,14,1,pot_hanging()))+g(50,170,1,person('#2a9d6f'))+'<path d="M56 100 l20 -40" stroke-width="3"/>','#e9f2e1'),
   ('<rect width="144" height="190" fill="#bcd3ea"/>'+g(72,180,1,tank(130))+g(72,160,.5,krishna_child()),'#bcd3ea')],
  ['the golden chariot','mosaru kuḍike','into the tank']),'The day after Aṣṭami: Śrī Kṛṣṇa Līlotsava, “Viṭla Piṇḍi”.',
 ['A special <b>clay image</b> of Kṛṣṇa is made for the day. In the afternoon it is set on the <b>golden chariot</b>.',
  'Led by the Paryāya svāmi and the svāmis of the other maṭhas, the chariot is pulled round Car Street.',
  'Around the square stand tall wooden frames (<i>gopuras</i>) with earthen pots of milk, curd and coloured water hung high.',
  'Men dressed as cowherds, the <b>Gollas</b>, smash them with long sticks: <b>mosaru kuḍike</b>, “the curd pot”, Kṛṣṇa’s childhood raids re-enacted.',
  'Finally the clay image is immersed in Madhva Sarovara, and the festival ends with the closing bath.'],
 [('z','Why a clay image, not the real one?'),('b','The real one never leaves the shrine. The clay Kṛṣṇa can be pulled, splashed and given back to the water, like a child after play.')],'A child-god’s games <b>re-enacted on the street</b>.')
huli=reading('huli','HULI VĒṢA IN UḌUPI','Tigers for Kṛṣṇa',
 S('Tiger dancers on a stage on Car Street with tāse drummers',g(280,150,1,'<rect x="-160" y="0" width="320" height="16" fill="#a0522d"/>')+g(200,150,1.2,tiger_dancer())+g(300,150,1.3,tiger_dancer(-1))+g(390,150,1.2,tiger_dancer())+g(80,190,.9,drum())+g(500,190,.9,drum()),'#fde9c8',205),
 ['<b>Uḍupi’s tigers.</b> In Uḍupi the <b>huli vēṣa</b> (tiger costume) belongs above all to Kṛṣṇa Janmāṣṭamī; troupes prepare for weeks.',
  '<b>The stage.</b> Troupes perform on a stage on Car Street and through the town to the beat of tāse drums, drawing large crowds.',
  '<b>The same art as Maṅgaḷūru.</b> It is the same tiger dance that fills Maṅgaḷūru at Navarātri (Part 2): two festivals, one art.',
  '<b>Other vēṣas.</b> The streets also fill with other costumed figures and tableaux.',
  '<b>Why tigers for Kṛṣṇa?</b> No single explanation is agreed; the tigers belong to the coast’s festivals more than to any one deity. (Traditions differ.)'],
 [('z','Tigers for the Goddess and for Kṛṣṇa?'),('b','The tiger is the coast’s festival animal. It turns up wherever the coast celebrates.')],'The coast’s tigers <b>dance for Kṛṣṇa too</b>.')
madhva=reading('madhva','THE DAYS OF MADHVA','Jayantī and Navamī',
 S('Madhvācārya seated teaching, with a book, and the Uḍupi image behind',g(220,190,1.6,sage('#ff8c1a'))+g(220,120,.6,'<rect x="-14" y="-18" width="28" height="18" fill="#fff8e7"/>')+g(420,190,1,tulu_temple('#e0a800','#b8860b')),'#e3eaf3',200),
 ['<b>Madhva Jayantī.</b> The founder’s birthday is kept on <b>Vijayadaśamī</b>, so Uḍupi’s Dasarā is also Madhva’s day.',
  '<b>Madhva Navamī.</b> The day Madhva is held to have vanished from sight while teaching, in Māgha. Tradition places it at Anantēśvara.',
  '<b>Places of his life.</b> <b>Pājaka</b>, his birthplace; <b>Malpe</b>, where the ship came ashore with the image; <b>Daṇḍatīrtha</b>, where he studied.',
  '<b>Other festivals.</b> Ratha Saptamī, Hanumān Jayantī for Mukhyaprāṇa, Navarātri, Dīpāvali, Gītā Jayantī.',
  '<b>The season of chariots.</b> Chariot processions run nightly from Utthāna Dvādaśī in autumn to the <b>Bhāgīrathī</b> festival at the start of the monsoon.'],
 [('z','A teacher who vanished?'),('b','So the tradition says: he was teaching the Aitareya Upaniṣad, and the students saw only flowers where he had sat.')],'The founder’s days <b>bookend the year</b>.')
endp=end(i,['<b>Square.</b> The Kṛṣṇa Maṭha, two Śiva temples and eight maṭhas round Car Street.','<b>Winter.</b> Saptotsava: seven nights of chariots, the raft and Cūrṇotsava.','<b>Every two years.</b> Paryāya: the vessel and the ladle pass on 18 January.','<b>Aṣṭami.</b> By the sun; tulasī, midnight arghya, laddus and tigers.','<b>Viṭla Piṇḍi.</b> A clay Kṛṣṇa, curd pots smashed, the image returned to the tank.'],
 'Part 4 goes to Dharmasthaḷa for the Lakṣa Dīpotsava, a hundred thousand lamps.','Uḍupi’s year of chariots')
src=sources([('The maṭha:','Our '+L('/tulunadu/temples/udupi-srikrishna/','Uḍupi Śrīkṛṣṇa')+' guide (festivals, Paryāya, the square).'),('Janmāṣṭamī and Viṭla Piṇḍi:','Deccan Herald reports on arghya, Viṭla Piṇḍi and mosaru kuḍike; Deccan Chronicle (solar Siṃha month; laddus and cakkulis; huli vēṣa and the closing bath); Udayavani and The Hans India reports; OneIndia (2006).')],
 'the history of the two-year Paryāya (Vādirāja’s reform) and Madhva Navamī are given as tradition; the chariots used on each Saptotsava night follow our temple guide; quantities of prasāda are one year’s report.','Festival names as used by the maṭha.')
finish(i,'PART 3 OF 9 · CHARIOTS · PARYĀYA · VIṬLA PIṆḌI',covart('A clay Kṛṣṇa on a golden chariot with curd pots and tiger dancers',g(220,190,1.2,RATHA(0,0,1,'#e0a800'))+g(220,98,.6,krishna_child())+g(80,90,1,'<path d="M-40 0 h80" stroke="#8a6a3a" stroke-width="4"/>'+g(0,14,1,pot_hanging()))+g(80,190,1,tiger_dancer())+g(370,190,1,tiger_dancer(-1))),'Kṛṣṇa’s games on Car Street',
 'The festival year of Uḍupi’s <b>Kṛṣṇa Maṭha</b>: the <b>Saptotsava</b>, the <b>Paryāya</b> handover, the eight maṭhas, <b>Janmāṣṭamī</b> and <b>Viṭla Piṇḍi</b>.',
 'Uḍupi festivals explained and illustrated: Saptotsava and Makara Saṅkrānti, Cūrṇotsava, the Paryāya on 18 January and the eight maṭhas, Kṛṣṇa Janmāṣṭamī by the solar calendar, Viṭla Piṇḍi and mosaru kuḍike, huli vēṣa, and the days of Madhva.',
 [fw,gl,sq,sapt,prep,paryaya,mathas,janma,vitla,huli,madhva,endp,src])
