from kt_common import *
i=4
def veg(): return '<ellipse cx="-14" rx="12" ry="9" fill="#e05050"/><ellipse cx="6" rx="10" ry="12" fill="#3a9a4a"/><path d="M22 4 q8 -20 2 -30" stroke="#e0a800" stroke-width="6" fill="none"/><ellipse cx="-2" cy="-14" rx="9" ry="6" fill="#6a3d9a"/>'
def stambha(): return '<rect x="-6" y="-110" width="12" height="110" fill="#a7a08c"/>'+''.join(f'<path d="M-14 {-20-k*20} h28" stroke="#8f8a7a" stroke-width="3"/>' for k in range(5))+'<path d="M-10 -110 h20 l-10 -14z" fill="#8f8a7a"/>'
def bmap():
    o='<rect width="560" height="230" fill="#e9c98a"/>'+g(130,120,1.6,mountain('#c0623a'))+'<ellipse cx="130" cy="160" rx="50" ry="18" fill="#4aa3df"/>'+T(130,190,'Bādāmi · caves · Agastya lake',9)
    o+=pin(330,130,'Banaśaṅkarī (Cōḷacagudda)')+'<rect x="300" y="150" width="60" height="30" fill="#4aa3df"/>'+T(330,196,'Haridrā tīrtha',9)
    o+=pin(470,60,'Paṭṭadakal',.3)+pin(490,180,'Aihoḷe',.3)
    return o+T(480,226,'simplified, not to scale',9)
fw=foreword(i,['A few kilometres from the red sandstone cliffs of Bādāmi, in what was once the forest of Tilakāraṇya, sits a Goddess on a lion beside a great square tank. She is <b>Banaśaṅkarī</b>, “Śaṅkarī of the forest”, and also <b>Śākambharī</b>, “she who bears the greens”: the Mother who fed the starving world from her own body, and the family goddess of the Cāḷukya kings who carved the caves nearby.',
 'This guide covers the forest and her names, the story of Durgama and the hundred-year drought, her eight-armed image, the Cāḷukyas and the Maratha chieftain who rebuilt her temple, the Haridrā tank and its lamp pillars, and the great January jātre with its chariot, its vegetable festival and its boats.',
 'Part 5, the last, of '+L('/temples-of-india/karnataka/','Temples of Karnataka')+'. Previous: '+L('/temples-of-india/karnataka/ganagapura-dattatreya/','Gāṇagāpura')+'. Śākambharī’s story is also told in '+L('/tulunadu/culture/durga-namaskara/','Durgā Namaskāra')+'.'],
 [('z','A goddess of vegetables?'),('b','A goddess of food in a land that knew famine. In a dry country, greens are a miracle.')])
gl=glance([('Goddess','Banaśaṅkarī (Vanaśaṅkarī), also Śākambharī; “Baḷavva” to many'),('Form','A black stone image with eight arms, seated on a lion'),('Place','Cōḷacagudda, near Bādāmi, Bāgalkoṭ district'),('Forest','Tilakāraṇya, the ancient forest that gave her the name “of the forest”'),('Story','Slayer of Durgama; feeder of the world in a famine'),('Patrons','Family goddess (kuladevī) of the Cāḷukyas'),('Rebuilt','1750, by the Maratha chieftain Parashuram Agale'),('Tank','Haridrā tīrtha, with lamp pillars'),('Jātre','January–February; chariot on the Pauṣa full moon'),('Devotees','Devāṅga weavers, some Deśastha families and many more')],
 S('A goddess with eight arms on a lion, beside a square tank with lamp pillars',g(150,200,1.4,lion())+g(150,160,1,devi(skin='#3a3a50',sari='#c0392b',items=('trident','sword','lotus','conch')))+'<rect x="290" y="140" width="220" height="70" fill="#4aa3df"/>'+g(300,140,.8,stambha())+g(500,140,.8,stambha()),'#f6e3e1',215),
 [('z','Bana or Vana?'),('b','The same word: forest. In Kannaḍa speech vana becomes bana.')],'The forest Mother <b>who fed the world</b>.')
where=reading('where','THE FOREST NEAR BĀDĀMI','Cōḷacagudda and Tilakāraṇya',svg(560,230,'Simplified map: Bādāmi, Banaśaṅkarī, Paṭṭadakal and Aihoḷe',bmap()),
 ['<b>Where.</b> The temple stands at <b>Cōḷacagudda</b>, a few kilometres from <b>Bādāmi</b> in Bāgalkoṭ district, north Karnataka.',
  '<b>Tilakāraṇya.</b> The place was a forest, the <b>Tilakāraṇya</b>; the Goddess of the forest is Vana- or Banaśaṅkarī.',
  '<b>Bādāmi.</b> Ancient Vātāpi, capital of the early Cāḷukyas, with its rock-cut cave temples above the Agastya lake.',
  '<b>Paṭṭadakal and Aihoḷe.</b> Nearby lie the Cāḷukya temple towns of Paṭṭadakal (a UNESCO site) and Aihoḷe.',
  '<b>Dry land.</b> This is red rock and black-soil country with little rain: a place where famine was a real fear.'],
 [('z','Was there really a forest here?'),('b','The name says so, and a few groves remain. Much of the old forest has gone to fields.')],'A forest goddess <b>in the dry Deccan</b>.')
names=reading('names','HER NAMES','Banaśaṅkarī, Śākambharī, Baḷavva',
 S('Greens and vegetables rising around a goddess',g(280,200,1.6,devi(skin='#3a3a50',sari='#2a9d6f',items=('lotus',)))+''.join(g(80+k*80,206,1.2,veg()) for k in [0,1,4,5]),'#e9f2e1',210),
 ['<b>Banaśaṅkarī.</b> “Śaṅkarī of the forest”: Śaṅkarī is Pārvatī, consort of Śaṅkara.',
  '<b>Śākambharī.</b> “She who bears (or nourishes with) the greens”: the Goddess who fed the world in famine.',
  '<b>Baḷavva.</b> A loving local name, “the mother”.',
  '<b>A form of Durgā.</b> Locals regard her as a form of Pārvatī and the sixth incarnation of Durgā.',
  '<b>Śatākṣī.</b> In the same story she is also the hundred-eyed Mother who wept for the world.'],
 [('z','So many names for one goddess?'),('b','Each name is a story. Forest, greens, mother: together they tell who she is.')],'Forest, greens, <b>mother</b>.')
story_=story('durgama','STORY · ŚĀKAMBHARĪ','The drought, the greens and Durgama',
 strip('Three panels: a cracked earth and sages praying; the Goddess with many eyes weeping as greens grow from her; the Goddess on her lion defeating a demon',
  [('<rect width="144" height="190" fill="#e9c98a"/>'+cracked(144,150)+g(72,150,.8,sage()),'#e9c98a'),
   ('<rect width="144" height="190" fill="#e9f2e1"/>'+g(72,150,.9,devi(sari='#2a9d6f',items=('lotus',)))+g(72,170,.8,greens()),'#e9f2e1'),
   ('<rect width="144" height="190" fill="#f6e3e1"/>'+g(50,170,.6,lion())+g(50,130,.5,devi(items=('trident','sword'),fierce=True))+g(110,170,.7,demon()),'#f6e3e1')],
  ['the drought','the greens','Durgama falls']),'From the Devī Māhātmya (11.46–50) and the Devī Bhāgavata (7.28); local tradition adds the Skanda and Padma Purāṇas.',
 ['The asura <b>Durgama</b> made the Vedas vanish; rites stopped, and with them the rain. A drought of a hundred years followed.',
  'The sages called on the Devī. She came with a hundred eyes (<b>Śatākṣī</b>) and wept at their misery; her tears ran as rivers.',
  'From her own body she brought forth greens, fruits and roots and fed the world: she is <b>Śākambharī</b>.',
  'She fought Durgama and slew him, restoring the Vedas; from him she took the name <b>Durgā</b>.',
  'Local tradition at Banaśaṅkarī says she rose from a sacrificial fire to defeat Durgama, and that this forest was where she fed the people. (Local tradition.) The full telling is in '+L('/tulunadu/culture/durga-namaskara/','Durgā Namaskāra')+'.'],
 [('z','Is this the same story as Durgā’s name?'),('b','The same. Banaśaṅkarī keeps the part about the greens at the centre: here she is above all the Mother who feeds.')],'She fed the world <b>from her own body</b>.')
form=reading('image','THE GODDESS IN THE SANCTUM','Eight arms on a lion',
 S('A black stone goddess with eight arms holding weapons, seated on a lion, crowned, in a dark sanctum','<rect width="560" height="215" fill="#3a2a2a"/>'+g(280,205,1.8,lion())+g(280,150,1.4,devi(skin='#3a3a50',sari='#c0392b',items=('trident','sword','discus','conch','bell','lotus')))+g(120,205,1,lamp())+g(440,205,1,lamp()),'#3a2a2a',215),
 ['<b>The image.</b> In the sanctum sits a <b>black stone</b> image of the Goddess with <b>eight arms</b>, seated on a <b>lion</b> (or lioness).',
  '<b>Her weapons.</b> In her hands she holds weapons and emblems of the warrior Goddess, such as the trident, sword and drum. (General description.)',
  '<b>Decked daily.</b> Like most living images she is dressed in silk and jewels, and her face is the focus of darśana.',
  '<b>Inscriptions.</b> Inscriptions are cited linking the image with a Cāḷukya king (Jagadekamalla); the date given in some sources, 603 CE, is disputed. (Sources differ.)',
  '<b>Fierce and kind.</b> Weapons for Durgama, greens for the hungry: the image holds both faces of the Mother. (Interpretation.)'],
 [('z','Eight arms and a lion, like Durgā?'),('b','She is Durgā. The forest and the greens are what make her Banaśaṅkarī.')],'Weapons for the demon, <b>food for the children</b>.')
hist=reading('history','CĀḶUKYAS AND MARATHAS','A goddess of kings, rebuilt',
 svg(560,150,'Timeline of the Banaśaṅkarī temple','<rect width="560" height="150" fill="#fff3cf"/>'+tl_strip([('7th c.','first temple'),('Cāḷukyas','kuladevī'),('medieval','inscriptions'),('1750','Maratha rebuild'),('today','great jātre')],560,150)),
 ['<b>The Cāḷukyas.</b> The Cāḷukyas regarded Banaśaṅkarī as their <b>kuladevī</b>, the family goddess, worshipped near their capital Vātāpi (Bādāmi).',
  '<b>The first temple.</b> The original temple is said to date from the 7th century, in the Drāviḍa style.',
  '<b>1750.</b> The present structure was rebuilt in <b>1750</b> by <b>Parashuram Agale</b>, a Maratha chieftain, in the Vijayanagara style.',
  '<b>A walled court.</b> The rebuilt temple stands in a high-walled enclosure with a pillared hall, a sanctum and a tower.',
  '<b>Many patrons.</b> Like all the Deccan’s great shrines, it has passed through Cāḷukya, Rāṣṭrakūṭa, Vijayanagara, Ādilshāhī and Maratha times.'],
 [('z','A Maratha rebuilt a Karnataka temple?'),('b','The Deccan did not have today’s borders. A goddess of the land drew devotion from all its rulers.')],'A kings’ goddess, <b>rebuilt by a chieftain</b>.')
tank=reading('haridra','THE HARIDRĀ TĪRTHA','The tank before the temple',
 S('A large square tank with stepped sides and pavilions, lamp pillars at the edge',g(280,200,1,'<rect x="-230" y="-120" width="460" height="120" fill="#c9a36b"/><rect x="-200" y="-100" width="400" height="80" fill="#4aa3df"/>'+''.join(g(x,-120,.5,'<rect x="-14" y="-20" width="28" height="20" fill="#e9d6c0"/><path d="M-18 -20 l18 -12 l18 12z" fill="#a0522d"/>') for x in (-200,-70,70,200)))+g(40,200,.8,stambha())+g(520,200,.8,stambha()),'#e9c98a',215),
 ['<b>The tank.</b> In front of the temple lies a large square tank, the <b>Haridrā tīrtha</b> (“turmeric tank”), with stepped sides and pavilions on three sides.',
  '<b>Its name.</b> Haridrā is turmeric, sacred to the Goddess and to married women. (The reason for the name is not recorded in our sources.)',
  '<b>Boats at the jātre.</b> During the jātre a <b>boat festival</b> (teppotsava) is held on the tank.',
  '<b>A meeting place.</b> The tank’s steps fill with pilgrims bathing and resting during the fair.',
  '<b>Water in a dry land.</b> A great tank before a goddess of plenty: in this country, water is the first blessing. (Interpretation.)'],
 [('z','A boat festival in a dry district?'),('b','On her tank, once a year. The Goddess floats where her people need water most.')],'A great tank <b>in a dry land</b>.')
pillars=reading('pillars','THE LAMP PILLARS AND THE TOWER','Lights and a gateway',
 S('Tall lamp pillars with tiers of lamps and a tower with a dome-like top',g(120,210,1.3,stambha())+lamps_row(98,96,3,22,.3)+g(250,210,1.3,stambha())+g(430,210,1.2,'<rect x="-30" y="-120" width="60" height="120" fill="#c9a36b"/><path d="M-36 -120 q36 -40 72 0z" fill="#a0522d"/>'),'#e9c98a',215),
 ['<b>Dīpa stambhas.</b> Tall <b>lamp pillars</b> stand by the tank and the temple; on festival nights they are lit with rows of lamps.',
  '<b>A Deccan custom.</b> Lamp pillars are a mark of Maratha-era and Deccan temples, from Kolhapur to here.',
  '<b>The “Victory Tower”.</b> A tower in the complex is described as blending Hindu and Islamic styles, a sign of the Deccan’s mixed building traditions. (As described.)',
  '<b>At night.</b> The lit pillars reflect in the tank during the jātre.',
  '<b>Read more.</b> On temple parts, see '+L('/temples-of-india/how-to-read-a-hindu-temple/','How to Read a Hindu Temple')+'.'],
 [('z','Why build a tower for lamps?'),('b','So that a whole village can see the Goddess is awake. A lit pillar is an announcement.')],'Lights <b>the whole village can see</b>.')
jat=reading('jatre','THE BANAŚAṄKARĪ JĀTRE','The great fair of the north',
 S('A chariot pulled by a crowd on the full moon, a fair with bullocks and stalls',g(150,205,1.6,RATHA(0,0,1,'#c0392b'))+g(150,210,1,crowd(6,200,0,.45))+g(420,205,1,'<ellipse rx="34" ry="14" cy="-24" fill="#f4f1ea"/><circle cx="34" cy="-32" r="10" fill="#f4f1ea"/><path d="M28 -44 l-6 -12 M40 -44 l6 -12" stroke-width="3"/>')+g(480,40,1.2,moon()),'#e3eaf3',215),
 ['<b>When.</b> The <b>Banaśaṅkarī Jātre</b> is held in January–February, around the Pauṣa month. The great day is the <b>Pauṣa full moon</b>, Banada Hunnime, “the forest’s full moon”, when the chariot is drawn.',
  '<b>The chariot.</b> The Goddess’s great chariot (ratha) is pulled by thousands.',
  '<b>Weeks long.</b> The fair runs for weeks, among the biggest of north Karnataka.',
  '<b>A cattle fair.</b> A large cattle fair is held alongside, as at many Deccan jātres.',
  '<b>Culture.</b> Cultural programmes fill the evenings.'],
 [('z','Banada Hunnime again, like Yellamma?'),('b','The same full moon: the Goddess’s great night across north Karnataka.')],'The forest’s full moon <b>and the great chariot</b>.')
palle=reading('palleda','PALLEDA HABBA','The festival of vegetables',
 S('Heaps of vegetables and greens offered before the Goddess',g(280,200,1.2,tulu_temple('#c0392b','#8e1f17'))+''.join(g(60+k*60,210,1.3,veg()) for k in range(4))+''.join(g(340+k*60,210,1.3,veg()) for k in range(4)),'#e9f2e1',215),
 ['<b>Palle.</b> During the jātre comes the <b>Palleda Habba</b>, the festival of vegetables (palya, greens).',
  '<b>What it is.</b> Vegetables and greens are offered to the Goddess as Śākambharī, in memory of the greens she gave the starving world.',
  '<b>Food shared.</b> The offerings are shared as prasāda: the Mother who fed the world feeds her devotees again.',
  '<b>Śākotsava.</b> Many temples of Śākambharī across India decorate the Goddess with vegetables at her festival; Banaśaṅkarī’s is the best known in Karnataka. (General.)',
  '<b>Read more.</b> On vegetables and offerings, see our '+L('/home-puja/','home pūjā')+' guide.'],
 [('z','Vegetables as offerings?'),('b','What else would you offer the Goddess of greens? She gave them first; we give them back.')],'The greens <b>given back to the Mother</b>.')
dev=reading('devotees','HER PEOPLE','Weavers, farmers and families',
 S('A weaver at a loom and a farmer with a plough, both with folded hands',g(160,210,1.2,person('#6a3d9a',seat=True))+g(220,180,1.1,'<rect x="-30" y="-50" width="60" height="50" fill="none" stroke="#8a6a3a" stroke-width="4"/><path d="M-30 -30 h60 M-30 -15 h60" stroke="#e0a800" stroke-width="2"/>')+g(400,210,1.2,person('#2a9d6f'))+g(460,210,1,'<path d="M-30 0 l40 -24 M4 -20 l12 18" stroke="#7a5a2a" stroke-width="5"/>'),'#f6e3e1',215),
 ['<b>The Devāṅgas.</b> The Goddess is the tutelary deity of the <b>Devāṅga</b> weaver community; families come from across the Deccan to their kuladevī.',
  '<b>Deśasthas.</b> She is also the family goddess of some Deśastha Brahmin families.',
  '<b>Farmers.</b> For the farmers of the black-soil plain, she is the goddess of plenty in a land of uncertain rain.',
  '<b>Her other temples.</b> Banaśaṅkarī temples stand in many towns; Bengaluru’s Banashankari neighbourhood is named after one.',
  '<b>Kuladevī.</b> For families who keep her as kuladevī, a visit at a wedding, a birth or the first tonsure of a child is a duty and a joy.'],
 [('z','Bengaluru’s Banashankari is named after her?'),('b','After her temple there. The forest Goddess reached the city.')],'The Mother of <b>weavers and farmers</b>.')
around=cards('around','AROUND BANAŚAṄKARĪ','The Cāḷukya country',
 S('Red cliffs with cave temples above a lake, and early stone temples',g(150,200,1.8,mountain('#c0623a'))+''.join(f'<rect x="{110+k*24}" y="140" width="16" height="22" fill="#5a3a1a"/>' for k in range(4))+'<ellipse cx="150" cy="200" rx="80" ry="14" fill="#4aa3df"/>'+g(380,200,1.2,vimana('#c9a36b',3))+g(480,200,1,vimana('#c9a36b',2)),'#e9c98a',215),
 [('🪨','Bādāmi caves','Rock-cut cave temples of the 6th century for Śiva, Viṣṇu and the Jinas, above the Agastya lake.'),('🛕','Paṭṭadakal','Cāḷukya temples of the 7th–8th centuries, a UNESCO World Heritage Site.'),('🏛️','Aihoḷe','Early experimental temples, often called a cradle of temple architecture.'),('🌊','Agastya lake','The ancient tank at Bādāmi, with Bhūtanātha temples on its shore.'),('🐘','Mahākūṭa','A group of early Śiva temples around a spring tank.'),('🌾','Kuḍalasaṅgama','Basavaṇṇa’s place on the Kṛṣṇā, in the same district.')],
 None,'The Mother <b>of the Cāḷukya country</b>.')
endp=end(i,['<b>Goddess.</b> Banaśaṅkarī, Śākambharī: Durgā of the forest who fed the world.','<b>Story.</b> Durgama, the hundred-year drought, the greens, the victory.','<b>History.</b> Kuladevī of the Cāḷukyas; rebuilt in 1750 by a Maratha chieftain.','<b>Place.</b> Eight-armed image on a lion; the Haridrā tank and lamp pillars.','<b>Jātre.</b> The Pauṣa full moon chariot, the vegetable festival and the boats.'],
 'This is the last part. Back to '+L('/temples-of-india/karnataka/','Temples of Karnataka')+', or read the coast’s festivals in '+L('/tulunadu/festivals/','Festivals of Tulu Nadu')+'.','The forest Mother who fed the world')
src=sources([('Temple:','Wikipedia, “Banashankari Amma Temple” (location, names, 7th century origins, inscription and 603 CE date, 1750 rebuild by Parashuram Agale, architecture, Haridrā tīrtha, lamp pillars, tower, legends, Cāḷukya kuladevī, Devāṅga and Deśastha devotees, jātre with chariot on Pauṣa full moon, Palleda Habba, boat festival, cattle fair).'),('Story:','Devī Māhātmya 11.46–50 and Devī Bhāgavata 7.28 as in our Durgā Namaskāra guide.')],
 'the 603 CE date and its link with Jagadekamalla (who is usually dated later); the meaning of the tank’s name; the description of the image’s weapons; the “Victory Tower” description.','Festival details as in the main source.')
finish(i,'PART 5 OF 5 · ŚĀKAMBHARĪ · THE TANK · THE JĀTRE',covart('A goddess on a lion with vegetables around her and a tank with lamp pillars',g(140,186,1.2,lion())+g(140,150,.9,devi(skin='#3a3a50',sari='#2a9d6f',items=('trident','lotus')))+''.join(g(250+k*40,190,1,veg()) for k in range(4))),'The forest Mother who fed the world',
 '<b>Banaśaṅkarī</b> of Bādāmi: the forest and her names, <b>Śākambharī</b>’s story, the Cāḷukya kuladevī, the <b>Haridrā tank</b>, and the great <b>jātre</b> with its chariot and vegetables.',
 'Banaśaṅkarī temple near Bādāmi explained and illustrated: Tilakāraṇya forest, Śākambharī and Durgama, the eight-armed image on a lion, the Cāḷukya kuladevī and the 1750 rebuild, Haridrā tīrtha, lamp pillars, the Banaśaṅkarī jātre, Palleda Habba and the Cāḷukya country.',
 [fw,gl,where,names,story_,form,hist,tank,pillars,jat,palle,dev,around,endp,src])
