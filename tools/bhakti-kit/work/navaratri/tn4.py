from tn_common import *
i=3
def dmap():
    o=map_frame(sea=False)+'<path d="M0 150 q160 -40 300 10 t260 -20" fill="none" stroke="#8fb8de" stroke-width="12"/>'+T(80,138,'Netrāvatī',10,fill='#1d4f8a')
    o+=pin(120,90,'Ujire · Janārdana temple')+pin(330,120,'Dharmasthaḷa · Mañjunātha')+pin(420,70,'Ratnagiri · Bāhubali',icon=mountain())
    o+='<path d="M126 92 C200 110 260 120 326 122" fill="none" stroke="#c0392b" stroke-width="3" stroke-dasharray="7 5"/>'+T(220,96,'padayātra',10,fill='#c0392b')
    o+=g(480,210,1,mountain('#5a7a4a'))+T(480,226,'Western Ghats',9)
    return o
fw=foreword(i,['At the end of Kārtika, when the nights are long and clear, a temple town at the foot of the Western Ghats lights a hundred thousand lamps. Every night for five nights Śiva as Mañjunātha comes out of his shrine, circles it sixteen times, and rides to a different platform in the town in a palanquin or a silver chariot. In the halls nearby, priests, scholars, poets and ministers talk about religion and literature, as they have since 1933.',
 'This is the <b>Lakṣa Dīpotsava</b> of Dharmasthaḷa. This guide covers why Kārtika is the month of lamps, the walk from Ujire, the nightly processions to the five <i>kaṭṭes</i>, the Sarva Dharma and Sāhitya Sammeḷanas, the Jain Samavasaraṇa pūjā that closes the festival, and what the lamps mean.',
 'The kṣetra itself is in '+L('/tulunadu/temples/dharmasthala-manjunatha/','Dharmasthaḷa Mañjunātha')+'; the lamp month in '+L('/festivals/kartika/','Kārtika Māsa')+'.'],
 [('z','A hundred thousand lamps? Who counts?'),('b','No one counts. Lakṣa means a lakh, and here it means “more lamps than you can count”.')])
gl=glance([('What','The festival of a hundred thousand lamps (lakṣa dīpa utsava) at Śrī Kṣetra Dharmasthaḷa'),('Deity','Śiva as Mañjunātha'),('When','The last five days of Kārtika, ending on the new moon (Nov–Dec)'),('Opening','A padayātra of thousands from Ujire; a state-level exhibition'),('Every night','16 circuits inside the temple, then a procession to a kaṭṭe (platform)'),('The five kaṭṭes','Hosakaṭṭe, Kañcimāru, Lalitōdyāna, Kere and Gaurimāru kaṭṭe'),('Last night','Gaurimāru kaṭṭe with the Aṣṭāvadhāna sevā'),('Gatherings','Sarva Dharma Sammeḷana and Sāhitya Sammeḷana, since 1933'),('Closing','Samavasaraṇa pūjā of Bhagavān Candranātha in the Jain basadi'),('Keepers','The Heggaḍe family, Dharmādhikārīs of the kṣetra')],
 S('A temple outlined in rows of small lamps at night','<rect width="560" height="200" fill="#20243a"/>'+g(280,180,1.4,tulu_temple('#a0522d','#5a2a10',180))+''.join(lamps_row(40,186-k*14,26,19,.3) for k in range(1))+lamps_row(150,96,14,19,.28)+lamps_row(110,140,19,19,.28),'#20243a',200),
 [('z','Is it the same as Dīpāvali?'),('b','No. Dīpāvali comes earlier in the month. The Lakṣa Dīpotsava fills the last days of Kārtika, just before its new moon.')],'Five nights, <b>a lakh of lamps</b>.')
place=reading('place','THE KṢETRA','Dharmasthaḷa on the Netrāvatī',svg(560,230,'Simplified map: Ujire, Dharmasthaḷa on the Netrāvatī, Ratnagiri and the Ghats',dmap()),
 ['<b>Where.</b> Dharmasthaḷa lies in Beḷtaṅgaḍi taluk of Dakṣiṇa Kannaḍa, where the coastal plain meets the first slopes of the Western Ghats, by the Netrāvatī.',
  '<b>Whose.</b> A Śiva shrine of Mañjunātha, served by Mādhva priests and kept by the Jain <b>Heggaḍe</b> family, beside the guardian deities, the Dharma Daivas, who came first.',
  '<b>The story in brief.</b> Tradition says four guardians of dharma came to the Jain chief Birmaṇṇa Pergaḍe, who welcomed them; the liṅga came later from Kadri. Read it in full in our '+L('/tulunadu/temples/dharmasthala-manjunatha/','Dharmasthaḷa')+' guide.',
  '<b>Ratnagiri.</b> On a hill above the town stands the 39 ft monolithic <b>Bāhubali</b>.',
  '<b>Ujire.</b> The neighbouring town, with the kṣetra’s colleges, where the festival walk begins.'],
 [('z','A Jain family running a Śiva festival?'),('b','That is Dharmasthaḷa. The festival ends in the Jain basadi, and nobody finds it strange.')],'A Śiva kṣetra <b>kept by a Jain house</b>.')
kart=reading('kartika','THE MONTH OF LAMPS','Why Kārtika',
 S('A woman lighting a row of clay lamps at dusk under a crescent moon','<rect width="560" height="190" fill="#3a2a50"/>'+g(480,40,1,moon())+g(120,170,1.2,person('#8e1f17',seat=True))+lamps_row(170,170,16,22,.5),'#3a2a50',190),
 ['<b>Kārtika.</b> The lunar month of Kārtika (October–November) is held across India as the holiest month for lamps: lamps on doorsteps, in temples, floated on rivers. See '+L('/festivals/kartika/','Kārtika Māsa')+'.',
  '<b>Lamps for Śiva and Viṣṇu.</b> Kārtika belongs to both: Kārtika Somavāras for Śiva, Utthāna Dvādaśī and Tulasī for Viṣṇu. A Śiva temple served by Vaiṣṇava priests fits it well.',
  '<b>Lakṣa dīpotsavas.</b> Many great temples of Karnataka hold a “lakh-lamp” festival in Kārtika; Dharmasthaḷa’s, in the last five days of the month, is the best known. Poḷali’s is on the Kārtika new moon too.',
  '<b>Nights at their longest.</b> In late Kārtika the nights are long and the rains have gone: the best season for a town of lamps.',
  '<b>The lamp’s meaning.</b> A lamp drives out darkness; in Kārtika many read it as knowledge driving out ignorance. (Interpretation.)'],
 [('z','Why do lamps matter so much in this month?'),('b','Old texts promise great merit for a lamp offered in Kārtika. In practice it is the month when the whole country agrees to light up together.')],'The holiest month <b>for a lamp</b>.')
pad=reading('padayatra','THE WALK FROM UJIRE','The padayātra that opens the festival',
 S('A long line of pilgrims walking along a road toward a temple, carrying flags',g(280,180,1,crowd(14,500,0,.55))+g(500,170,.5,tulu_temple())+g(40,170,.6,flagpole(60,'#ff8c1a')),'#fff3cf',195),
 ['<b>On foot.</b> On the first day, thousands of devotees gather at Ujire and walk to Dharmasthaḷa. The procession begins near the Janārdana temple of Ujire.',
  '<b>Ten thousand.</b> One report counted about 10,000 people on the walk.',
  '<b>Many padayātras.</b> Other groups walk in from farther away, some for days, in the weeks before the festival.',
  '<b>Received.</b> At the temple the Dharmādhikārī addresses the walkers.',
  '<b>Why walk.</b> A padayātra is an old form of pilgrimage: the journey itself is offered. (See also the Śivarātri padayātras to the same kṣetra.)'],
 [('z','Why not just drive?'),('b','Plenty do. But a pilgrimage on foot is the oldest kind there is. You arrive tired, and humbler.')],'The festival begins <b>on foot</b>.')
lamps=reading('lamps','A LAKH OF LAMPS','The town lit up',
 S('The temple, its gateway and the streets outlined with lamps; a devotee lighting one','<rect width="560" height="200" fill="#20243a"/>'+g(200,180,1.1,tulu_temple('#a0522d','#5a2a10',150))+lamps_row(40,190,24,21,.32)+lamps_row(120,120,8,20,.3)+g(450,190,1,person('#8e1f17'))+g(430,150,.6,lamp()),'#20243a',200),
 ['<b>Clay and electric.</b> The temple, its courtyards and the town are decorated with traditional oil lamps and electric lights through the five nights.',
  '<b>Not a number.</b> “Lakṣa” is a lakh, a hundred thousand; the name means a vast offering of light more than an exact count.',
  '<b>Offered by devotees.</b> Pilgrims bring and light lamps as their own offering; the kṣetra arranges the main illumination.',
  '<b>Darkness before the new moon.</b> The festival ends on the Kārtika new moon: the darkest night, lit brightest.',
  '<b>The glow.</b> Visitors describe the whole temple landscape seeming to glow from within.'],
 [('z','Is it like Dīpāvali night every night?'),('b','Quieter, and longer. Five nights of lamps with a procession at the centre of each.')],'The darkest nights, <b>lit brightest</b>.')
nightly=story('procession','THE NIGHTLY PROCESSION','From the sanctum to the kaṭṭe',
 strip('Three panels: the festival image carried round inside the temple; placed in a golden palanquin; drawn in a silver chariot to a platform under a tree',
  [('<rect width="144" height="190" fill="#20243a"/>'+g(72,150,.7,tulu_temple('#a0522d','#5a2a10'))+'<circle cx="72" cy="120" r="56" fill="none" stroke="#ffd60a" stroke-width="3" stroke-dasharray="6 5"/>'+T(72,186,'16 rounds',10,fill='#fff'),'#20243a'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(72,150,1,'<rect x="-30" y="-24" width="60" height="24" fill="#e0a800"/><path d="M-50 -12 h100" stroke="#8a6a3a" stroke-width="5"/><path d="M-26 -24 q26 -26 52 0" fill="#e0a800"/>')+g(40,170,.7,person('#f4f1ea'))+g(104,170,.7,person('#f4f1ea')),'#20243a'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(60,180,.75,RATHA(0,0,1,'#c9c9d6'))+g(118,180,.9,'<rect x="-24" y="-10" width="48" height="10" fill="#b08a62"/>'+tree('#2f6a3a')),'#20243a')],
  ['inside','the palanquin','the silver chariot']),'Each night of the Lakṣa Dīpotsava, as described in reports from the kṣetra.',
 ['After special worship in the sanctum, the festival image (utsava mūrti) of Mañjunātha is carried round inside the temple <b>sixteen times</b>.',
  'It is brought to the temple entrance and set in a <b>golden palanquin</b>.',
  'It goes out in procession, on some nights drawn in the decorated <b>silver chariot</b>, with music and lamps.',
  'It reaches a <b>kaṭṭe</b>, a raised platform under a tree or by water in the town, where a special pūjā is offered.',
  'Then it returns for another circuit at the temple entrance and goes back to the sanctum.'],
 [('z','Why a different platform each night?'),('b','So that the Lord visits his whole town, not just his temple. Each kaṭṭe has its own night.')],'The Lord goes out <b>to visit his town</b>.')
kattes=cards('kattes','THE FIVE KAṬṬES','A platform for each night',
 S('Five platforms under trees, each with lamps',''.join(g(60+k*110,180,.8,'<rect x="-36" y="-12" width="72" height="12" fill="#b08a62"/>'+tree(['#2f6a3a','#3a8a4a','#2a7a5a','#4a8a3a','#2f6a3a'][k])+lamps_row(-30,-14,4,20,.3)) for k in range(5)),'#e9f2e1',195),
 [('🆕','Hosakaṭṭe','“The new platform”: the opening night’s utsava.'),('🌳','Kañcimāru kaṭṭe','A night at the Kañcimāru platform.'),('🌸','Lalitōdyāna kaṭṭe','“The lovely garden”: the image goes in the golden palanquin to the garden for a special pūjā.'),('💧','Kere kaṭṭe','The platform by the tank (kere).'),('✨','Gaurimāru kaṭṭe','The last night: the silver chariot and the Aṣṭāvadhāna sevā.'),('🙏','Every night','16 circuits, procession, pūjā at the kaṭṭe, return.')],
 [('z','Always in that order?'),('b','Reports differ a little year to year. The last night is always Gaurimāru kaṭṭe.')],'Five nights, <b>five platforms</b>.',
 intro='The kṣetra’s published calendars name these utsavas for the festival nights. The order of the middle nights varies between years.')
ashta=reading('ashtavadhana','GAURIMĀRU KAṬṬE','The last night and the Aṣṭāvadhāna sevā',
 S('The silver chariot under a great tree at night, musicians and reciters seated in a row before it','<rect width="560" height="200" fill="#20243a"/>'+g(150,190,1.2,RATHA(0,0,1,'#c9c9d6'))+g(300,190,1.4,tree('#2f6a3a'))+''.join(g(380+k*24,190,.7,person(['#f4f1ea','#e0a800','#c0392b','#1d4f8a','#2a9d6f','#f4f1ea','#e0a800','#c0392b'][k],seat=True)) for k in range(8))+lamps_row(20,196,20,28,.3),'#20243a',200),
 ['<b>The climax.</b> On the last night the Lord rides in the silver chariot to <b>Gaurimāru kaṭṭe</b>.',
  '<b>Aṣṭāvadhāna sevā.</b> There the <b>Aṣṭāvadhāna</b> pūjā is offered: an “eightfold attention” service, in which the deity is honoured with a round of offerings of recitation, music and other arts. (General description; the exact eight vary by tradition.)',
  '<b>The lakh of lamps.</b> This is the night the lamps are fullest, the night the festival is named for.',
  '<b>Huge crowds.</b> Pilgrims from across the state fill the kṣetra.',
  '<b>Then the Jina.</b> The next day the festival moves to the basadi for the Samavasaraṇa pūjā (its own page).'],
 [('z','Eight services at once?'),('b','In turn, but before the same Lord: Veda, song, instruments, praise. Every art takes its turn to bow.')],'Every art <b>takes its turn to bow</b>.')
sarva=reading('sarvadharma','THE SARVA DHARMA SAMMEḶANA','A meeting of all religions',
 S('A stage with speakers of different faiths seated together, an audience below',g(280,120,1,'<rect x="-200" y="0" width="400" height="16" fill="#a0522d"/>')+''.join(g(140+k*70,120,1,person(['#ff8c1a','#f4f1ea','#2a9d6f','#1d4f8a','#8e1f17'][k],seat=True)) for k in range(5))+g(280,195,1,crowd(14,480,0,.45)),'#e3eaf3',205),
 ['<b>Since 1933.</b> In 1933 the then Dharmādhikārī, <b>Mañjayya Heggaḍe</b>, held the first <b>Sarva Dharma Sammeḷana</b>, “a conference of all religions”, with the festival. It has met every year since; recent sessions are numbered in the nineties.',
  '<b>Who comes.</b> Leaders and scholars of different faiths are invited to speak; the presiding guest is taken to the hall in procession.',
  '<b>When.</b> It is held on the fourth day of the festival, in the Amṛtavarṣiṇī auditorium.',
  '<b>The idea.</b> The kṣetra presents dharma as larger than any one creed: the meeting is the place’s own history, a Śiva temple, Vaiṣṇava priests and a Jain family, put on a stage.',
  '<b>Its voices.</b> Judges, ministers and religious teachers have inaugurated it; one devotee was honoured for attending it for over sixty years.'],
 [('z','A religious festival hosting other religions?'),('b','At Dharmasthaḷa it would be stranger not to.')],'All religions <b>at one festival</b>.')
sahi=reading('sahitya','THE SĀHITYA SAMMEḶANA','Literature at the festival',
 S('A scholar speaking at a lectern, books stacked beside, an audience listening',g(200,180,1.2,person('#1d4f8a'))+g(250,140,1,'<rect x="-20" y="0" width="40" height="40" fill="#8a6a3a"/>')+g(330,180,1,'<rect x="-30" y="-40" width="60" height="40" fill="#e9d6c0"/><path d="M-30 -26 h60 M-30 -12 h60" stroke-width="1.5"/>')+g(460,190,1,crowd(5,120,0,.5)),'#e3eaf3',200),
 ['<b>Also since 1933.</b> The <b>Sāhitya Sammeḷana</b>, a literary conference, began in the same year as the Sarva Dharma meeting, and is held on the fifth day.',
  '<b>Kannaḍa letters.</b> Leading Kannaḍa writers and scholars inaugurate and preside; the presidents of the Kannaḍa Sāhitya Pariṣat and celebrated scholars have opened recent sessions.',
  '<b>Religion and literature.</b> The festival pairs the two deliberately, as two ways of seeking dharma.',
  '<b>Lalita Kalā Goṣṭhi.</b> A fine-arts gathering is also held during the festival, with music, dance and Harikathā each evening.',
  '<b>An unusual festival.</b> Few temple festivals carry a literary conference of nearly a century.'],
 [('z','Poets at a temple festival?'),('b','Lamps are for seeing. Literature is another kind of lamp.')],'Another kind of lamp: <b>words</b>.')
expo=reading('exhibition','THE EXHIBITION AND THE STAGES','Village Karnataka on display',
 S('Stalls of a fair with farm tools, handicrafts and a stage with a dancer',''.join(g(60+k*90,180,.9,'<rect x="-36" y="-40" width="72" height="40" fill="#e9d6c0"/><path d="M-40 -40 l40 -20 l40 20z" fill="'+['#c0392b','#1d4f8a','#2a9d6f','#e0a800'][k]+'"/>') for k in range(4))+g(470,180,1.2,person('#c0392b'))+'<path d="M450 100 l20 -30 l20 30z" fill="#e0a800"/>','#fff3cf',195),
 ['<b>A state-level exhibition.</b> A large exhibition opens on the first day in the grounds of the kṣetra’s high school; it has run for over forty editions.',
  '<b>Rural life.</b> It shows the rural life of Tuḷunāḍu and Karnataka: farming, crafts, tools and the work of the kṣetra’s rural development programmes.',
  '<b>Evening stages.</b> Cultural programmes run every evening from about 5.30 pm: classical music, dance, Harikathā and bhajans.',
  '<b>A fair.</b> Around it, a festival market of the kind every coastal jātre has.',
  '<b>A whole town on holiday.</b> For five days Dharmasthaḷa is temple, conference, fair and theatre at once.'],
 [('z','What does an exhibition have to do with lamps?'),('b','Dharmasthaḷa’s idea of dharma includes the farmer and his tools. The exhibition is that idea in stalls.')],'Temple, fair and theatre <b>at once</b>.')
sama=reading('samavasarana','THE SAMAVASARAṆA PŪJĀ','The festival ends with the Jina',
 S('A Jain Tīrthaṅkara seated in meditation on a tiered circular platform, devotees around',g(280,190,1.2,''.join(f'<ellipse cy="{-k*14}" rx="{150-k*30}" ry="14" fill="{["#e9d6c0","#f2e6c8","#e0a800","#f6efe2"][k]}"/>' for k in range(4))+g(0,-56,.9,person('#f6efe2',seat=True)))+g(80,190,1,namaste('#1d4f8a'))+g(480,190,1,namaste('#8e1f17')),'#e3eaf3',200),
 ['<b>The basadi.</b> Beside the temple stands the Jain basadi of <b>Bhagavān Candranātha</b> (Candraprabha), the eighth Tīrthaṅkara, worshipped by the Heggaḍe family.',
  '<b>Samavasaraṇa.</b> In Jain teaching the samavasaraṇa is the great assembly hall the gods build for a Tīrthaṅkara to preach in, where all beings, humans and animals alike, sit to hear him.',
  '<b>The pūjā.</b> The day after Gaurimāru kaṭṭe, the festival closes with the <b>Samavasaraṇa Pūjā</b> of Candranātha.',
  '<b>Why it fits.</b> An assembly where every creature hears the same teaching is the Jain picture of what Dharmasthaḷa’s festival tries to be. (Interpretation.)',
  '<b>One festival, several faiths.</b> As at the Mahā Naḍāvaḷi, Śiva, the Jina and the daivas are honoured in one sequence.'],
 [('z','A Śiva festival ending in a Jain pūjā?'),('b','In Dharmasthaḷa the circle closes where the family that keeps it prays.')],'The circle closes <b>at the Jina’s feet</b>.')
anna=reading('annadana','FOOD AND REFUGE','The kṣetra’s four gifts',
 S('A long dining hall with people seated in rows on the floor eating from leaves',''.join(g(60+k*50,170,.7,person(['#8e1f17','#1d4f8a','#2a9d6f','#e0a800'][k%4],seat=True)) for k in range(10))+'<path d="M30 176 h500" stroke="#3a9a4a" stroke-width="6"/>','#fff3cf',190),
 ['<b>Annadāna.</b> The kṣetra feeds every pilgrim free of charge every day; at festival time the kitchens feed vast crowds.',
  '<b>Four gifts.</b> Dharmasthaḷa is known for four kinds of giving (dāna): food (anna), medicine (auṣadha), learning (vidyā) and freedom from fear (abhaya).',
  '<b>The guest first.</b> The founding story is about a family that never turned a guest away. The festival kitchen is that story every night.',
  '<b>Weddings.</b> The kṣetra also holds mass weddings (samūha vivāha) for families who cannot afford one, though not in the festival.',
  '<b>Read more.</b> See '+L('/tulunadu/temples/dharmasthala-manjunatha/','Dharmasthaḷa Mañjunātha')+'.'],
 [('z','Free food for everyone, every day?'),('b','Every day. Here, feeding the guest is the oldest worship there is.')],'The guest is fed <b>before the god is lit</b>.')
endp=end(i,['<b>When.</b> The last five days of Kārtika, the month of lamps.','<b>Opening.</b> A walk from Ujire and an exhibition of village Karnataka.','<b>Each night.</b> Sixteen circuits, palanquin or silver chariot, pūjā at a kaṭṭe.','<b>Words.</b> The Sarva Dharma and Sāhitya Sammeḷanas, since 1933.','<b>Close.</b> Gaurimāru kaṭṭe and the Aṣṭāvadhāna; then the Jina’s Samavasaraṇa pūjā.'],
 'Part 5 goes to Poḷali for its month-long fair and the ball game of the Goddess.','A hundred thousand lamps at Dharmasthaḷa')
src=sources([('The festival:','utsav.gov.in (Ministry of Culture) pages on the Lakṣa Dīpotsava; Udayavani reports (Lalitōdyāna utsava, Gaurimāru kaṭṭe and Samavasaraṇa pūjā, silver chariot, exhibition); Deccan Herald (Hosakaṭṭe utsava, 1933 sammeḷanas, Sarva Dharma Sammeḷana reports); Daijiworld (padayātra from Ujire; Samavasaraṇa pūjā); Star of Mysore (sammeḷana sessions and programme); HinduPad (kṣetra calendar listing the kaṭṭe utsavas).'),('The kṣetra:','Our '+L('/tulunadu/temples/dharmasthala-manjunatha/','Dharmasthaḷa Mañjunātha')+' guide.')],
 'the order of the kaṭṭe utsavas differs between years; the content of the Aṣṭāvadhāna sevā is described generally; the “four gifts” are as commonly described by the kṣetra; numbers of walkers and lamps are reports or traditional.','Utsava names as in the kṣetra calendar.')
finish(i,'PART 4 OF 9 · LAMPS · PROCESSIONS · SAMMEḶANAS',covart('A temple outlined with lamps at night and a silver chariot before it','<rect width="440" height="196" fill="#20243a"/>'+g(260,180,1.2,tulu_temple('#a0522d','#5a2a10',150))+g(90,186,1.1,RATHA(0,0,1,'#c9c9d6'))+lamps_row(20,192,21,20,.32)+lamps_row(190,118,9,18,.28)),'A lakh of lamps for Mañjunātha',
 'The <b>Lakṣa Dīpotsava</b> of Dharmasthaḷa: the lamp month, the <b>walk from Ujire</b>, five nights of <b>processions to the kaṭṭes</b>, the <b>sammeḷanas</b>, and the Jain close.',
 'Lakṣa Dīpotsava at Dharmasthaḷa explained and illustrated: Kārtika lamps, the padayātra from Ujire, the nightly procession of Mañjunātha to Hosakaṭṭe, Lalitōdyāna and Gaurimāru kaṭṭe, the Aṣṭāvadhāna sevā, Sarva Dharma and Sāhitya Sammeḷanas since 1933, and the Samavasaraṇa pūjā.',
 [fw,gl,place,kart,pad,lamps,nightly,kattes,ashta,sarva,sahi,expo,sama,anna,endp,src])
