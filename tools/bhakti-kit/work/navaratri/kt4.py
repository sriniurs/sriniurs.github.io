from kt_common import *
i=3
def datta(s=1):
    o='<path d="M-40 70 q40 -80 80 0z" fill="#ff8c1a"/>'
    for dx,c in [(-22,'#e0a800'),(0,'#8fd0f5'),(22,'#3a6ab8')]: o+=f'<circle cx="{dx}" cy="0" r="14" fill="#c98a5a"/><path d="M{dx-10} -10 q10 -14 20 0" fill="{c}"/>'
    return g(0,0,s,o)
def cow(): return '<ellipse rx="30" ry="15" cy="-24" fill="#f4f1ea"/><circle cx="30" cy="-32" r="10" fill="#f4f1ea"/><path d="M-20 -12 v12 M20 -12 v12" stroke-width="3"/>'
def dog(): return '<ellipse rx="16" ry="8" cy="-12" fill="#8a6a3a"/><circle cx="16" cy="-18" r="7" fill="#8a6a3a"/><path d="M-10 -6 v6 M10 -6 v6" stroke-width="2.5"/>'
def paduka(): return '<path d="M-22 0 q-8 -30 4 -50 q12 -8 14 10 q2 24 -6 40z" fill="#a0522d"/><path d="M8 0 q-8 -30 4 -50 q12 -8 14 10 q2 24 -6 40z" fill="#a0522d"/><circle cx="-12" cy="-32" r="3" fill="#e0a800"/><circle cx="18" cy="-32" r="3" fill="#e0a800"/>'
def gmap():
    o='<rect width="560" height="230" fill="#eadcc0"/><path d="M0 60 q200 40 300 110" fill="none" stroke="#8fb8de" stroke-width="16"/><path d="M560 40 q-160 60 -260 130" fill="none" stroke="#8fb8de" stroke-width="10"/><path d="M300 170 q60 40 100 60" fill="none" stroke="#8fb8de" stroke-width="18"/>'
    o+=T(90,60,'Bhīmā',11,fill='#1d4f8a')+T(480,52,'Amarjā',11,fill='#1d4f8a')+pin(300,170,'Saṅgama · Audumbara tree',.35)+pin(220,100,'Gāṇagāpura · Nirguṇa Maṭha')+pin(400,120,'Kalleśvara',.3)
    return o+pin(470,200,'Kalaburagi (about 40 km)',.3)+T(480,226,'simplified, not to scale',9)
fw=foreword(i,['In a village of the Kalaburagi plain, where the little Amarjā joins the Bhīmā, pilgrims from Maharashtra, Karnataka and the Telugu lands come to bow before a pair of wooden sandals. They are the <b>nirguṇa pādukās</b>, “the sandals without attributes”, of <b>Narasiṃha Sarasvatī</b>, held to be Dattātreya himself in human form, who lived here for twenty-four years and promised never to leave.',
 'This guide covers Dattātreya, the three gods in one; his first two human forms; the life of Narasiṃha Sarasvatī as the <b>Guru Caritra</b> tells it; the Nirguṇa Maṭha and its sandals; the saṅgama and its trees; the eight tīrthas; the custom of <b>madhukarī</b> alms; the reading of the Guru Caritra; and the Guru’s festivals.',
 'Part 4 of '+L('/temples-of-india/karnataka/','Temples of Karnataka')+'. Previous: '+L('/temples-of-india/karnataka/savadatti-yellamma/','Savadatti Yellamma')+'. On the Guru’s day, see '+L('/festivals/guru-purnima/','Guru Pūrṇimā')+'.'],
 [('z','Worshipping sandals?'),('b','The guru’s feet are the guru. Where his sandals rest, he is held to be present.')])
gl=glance([('Place','Gāṇagāpura (Deval Gāṇagāpura), Afzalpur taluk, Kalaburagi district'),('Rivers','The saṅgama of the Bhīmā and the Amarjā'),('Deity','Dattātreya as Śrī Narasiṃha Sarasvatī, his second human form'),('Main shrine','The Nirguṇa Maṭha with the nirguṇa pādukās'),('The Guru','Born at Kārañjā (Maharashtra), 14th century by tradition; lived here 24 years'),('Text','The Śrī Guru Caritra, the central book of the Datta tradition'),('Custom','Madhukarī: taking alms from five houses'),('Waters','The aṣṭa tīrthas, the eight sacred waters'),('Festivals','Datta Jayantī with a chariot; Narasiṃha Sarasvatī Jayantī; Thursday palanquin'),('Pilgrims','Above all from Maharashtra, Karnataka and the Telugu lands')],
 S('Dattātreya with three heads, a cow and four dogs, beside a pair of sandals',g(200,200,1.6,datta())+g(80,210,1,cow())+''.join(g(300+k*40,210,1,dog()) for k in range(4))+g(500,200,1.2,paduka()),'#fff3cf',220),
 [('z','Is it a temple or a monastery?'),('b','Both. The Nirguṇa Maṭha was the Guru’s house; it became his shrine.')],'The Guru’s sandals <b>where the rivers meet</b>.')
where=reading('where','THE SAṄGAMA','Where the Amarjā meets the Bhīmā',svg(560,230,'Simplified map: the Bhīmā and Amarjā meeting at Gāṇagāpura',gmap()),
 ['<b>The village.</b> Gāṇagāpura is in Afzalpur taluk of Kalaburagi district, in the dry plain of north Karnataka near the Maharashtra border.',
  '<b>The rivers.</b> The <b>Amarjā</b> joins the <b>Bhīmā</b> here; the meeting is the saṅgama, held extremely holy.',
  '<b>Two centres.</b> The Nirguṇa Maṭha in the village, and the Saṅgama a short distance away with its sacred tree and the Guru’s place of penance.',
  '<b>Old names.</b> The Guru Caritra calls the place Gāṇagāpura, Gāṇagabhavana and Gandharvapura.',
  '<b>Getting there.</b> A station of the same name lies on the Pune–Raichur railway some distance away. (Practical details change; check locally.)'],
 [('z','Why do gurus choose river meetings?'),('b','A saṅgama is a meeting of streams; a guru is where the seeker meets the truth. Rivers make good teachers.')],'Two rivers meet, <b>and so do guru and seeker</b>.')
who=reading('datta','WHO IS DATTĀTREYA','Brahmā, Viṣṇu and Śiva in one',
 S('Dattātreya with three heads and six arms, a cow behind him and four dogs at his feet',g(280,210,2,datta())+g(110,210,1.2,cow())+''.join(g(400+k*40,210,1.1,dog()) for k in range(4)),'#fff3cf',220),
 ['<b>Three in one.</b> <b>Dattātreya</b> is the three great gods, Brahmā, Viṣṇu and Śiva, in one person: often shown with three heads and six arms.',
  '<b>The guru of gurus.</b> He is worshipped above all as the <b>Ādi Guru</b>, the first teacher, the guru who teaches without a fixed form.',
  '<b>His companions.</b> A cow stands behind him and four dogs at his feet. Many read the cow as the earth or dharma and the dogs as the four Vedas. (Interpretation.)',
  '<b>The Avadhūta.</b> In the Bhāgavata he is the wandering sage who says he learned from twenty-four teachers in nature (its own page).',
  '<b>His tradition.</b> The <b>Datta sampradāya</b> is strongest in Maharashtra, Karnataka and the Telugu lands; its great book is the Guru Caritra.'],
 [('z','Why three heads?'),('b','Because creation, keeping and dissolving are one work. The guru who knows that is the one who can teach it.')],'Three gods, <b>one teacher</b>.')
anas=story('anasuya','STORY · ANASŪYĀ','How the three gods became one child',
 strip('Three panels: three gods disguised as mendicants at a hermitage; Anasūyā turning them into babies; the three becoming one child, Datta',
  [('<rect width="144" height="190" fill="#e9f2e1"/>'+''.join(g(30+k*40,170,.7,sage(['#e0a800','#8fd0f5','#3a6ab8'][k])) for k in range(3)),'#e9f2e1'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(40,170,.9,devi(sari='#c0392b',items=()))+''.join(g(84+k*22,170,.5,'<circle r="10" fill="#c98a5a"/><path d="M-10 10 q10 20 20 0" fill="#f4f1ea"/>') for k in range(3)),'#fff3cf'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(72,160,1,datta(.8)),'#fff3cf')],
  ['three guests','three babies','one Datta']),'The story of Datta’s birth, as commonly told in the Datta tradition and the Purāṇas (tellings differ).',
 ['The sage <b>Atri</b> and his wife <b>Anasūyā</b>, famed for her virtue, lived in a hermitage.',
  'To test her, the three gods Brahmā, Viṣṇu and Śiva came disguised as mendicants and asked her for food served in a way that would break her vow.',
  'By the power of her virtue she turned them into three infants, fed them as a mother, and kept her vow.',
  'Their wives came begging for their husbands back. Anasūyā restored them, and the three gods granted her a boon.',
  'She asked that they be born as her son. So <b>Datta</b> was born, “the given one”, son of Atri: <b>Dattātreya</b>.'],
 [('z','A test that ended in a birth?'),('b','A mother’s goodness turned three gods into her children. That is the Datta tradition’s first lesson.')],'Three gods <b>given as one son</b>.')
gurus=cards('teachers','THE TWENTY-FOUR TEACHERS','The Avadhūta’s lesson',
 S('A wandering sage looking at the earth, a river, a bee, a moth at a flame and a child',g(70,200,1.1,sage('#f4f1ea'))+g(170,200,1,mountain('#7a9a5a'))+'<path d="M220 200 q40 -20 80 0" stroke="#8fb8de" stroke-width="8" fill="none"/>'+g(350,150,1,bees(3,30,20))+g(420,190,.8,lamp())+g(500,200,.8,person('#e0a800')),'#e9f2e1',215),
 [('🌍','Earth','Patience: it bears everything.'),('🌬️','Air','To touch everything and cling to nothing.'),('🌊','Water','To be pure and to purify.'),('🐝','The bee','To take a little from many flowers.'),('🦋','The moth','A warning: drawn to the flame of desire, it burns.'),('🐍','The snake','To live without building a house.'),('🧒','The child','Joy without worry.'),('🏹','The arrow-maker','Concentration so total he did not see a king pass.')],
 None,'The whole world <b>as a teacher</b>.',
 intro='In the Bhāgavata Purāṇa (book 11), the Avadhūta, identified with Dattātreya, tells King Yadu that he learned from twenty-four teachers in nature. A selection, in our own plain words:')
forms=reading('forms','THE GURU IN HUMAN FORM','Śrīpāda Śrīvallabha and Narasiṃha Sarasvatī',
 S('Two saints in saffron with sandals beneath each',g(170,200,1.6,sage('#ff8c1a'))+g(170,214,.6,paduka())+T(170,226,'Śrīpāda Śrīvallabha',10)+g(400,200,1.6,sage('#ff8c1a'))+g(400,214,.6,paduka())+T(400,226,'Narasiṃha Sarasvatī',10),'#fff3cf',230),
 ['<b>Avatāras of the guru.</b> The Datta tradition holds that Dattātreya took human form again and again to teach.',
  '<b>The first.</b> <b>Śrīpāda Śrīvallabha</b>, born by tradition at Pīṭhāpuram in the Godāvarī country, and associated with Kuravapur on the Kṛṣṇā.',
  '<b>The second.</b> <b>Narasiṃha Sarasvatī</b>, the Guru of Gāṇagāpura, whose life fills most of the Guru Caritra.',
  '<b>Later saints.</b> The tradition counts later masters too, such as Svāmī Samartha of Akkalkoṭ, as forms of Datta. (Traditions differ on the list.)',
  '<b>A shared reverence.</b> The Śṛṅgeri Jagadguru, visiting, has noted that Narasiṃha Sarasvatī revered Ādi Śaṅkara and that the Datta tradition honours him. See '+L('/srividya/temples/sringeri-sharada/','Śṛṅgeri Śāradā')+'.'],
 [('z','The same god again and again?'),('b','The same teacher in new clothes, the tradition says, wherever students need him.')],'One guru, <b>many lives of teaching</b>.')
life=story('narasimha','STORY · NARASIṂHA SARASVATĪ','The Guru’s life, from the Guru Caritra',
 strip('Three panels: a silent child who speaks the Vedas at his thread ceremony; a young sannyāsin walking; the Guru seated under a tree by the river meeting',
  [('<rect width="144" height="190" fill="#fff3cf"/>'+g(72,170,.9,person('#f4f1ea'))+'<path d="M50 100 q22 -14 44 0" fill="none" stroke="#e0a800" stroke-width="3"/>','#fff3cf'),
   ('<rect width="144" height="190" fill="#eadcc0"/>'+g(72,170,.9,sage('#ff8c1a'))+'<path d="M90 100 v70" stroke="#8a6a3a" stroke-width="3"/>','#eadcc0'),
   ('<rect width="144" height="190" fill="#e9f2e1"/>'+g(100,170,.9,tree('#2f6a3a'))+g(50,170,.8,sage('#ff8c1a'))+'<rect y="176" width="144" height="14" fill="#4aa3df"/>','#e9f2e1')],
  ['the silent child','the wanderer','24 years at the saṅgama']),'The Guru’s life as the Śrī Guru Caritra tells it (tradition).',
 ['Narasiṃha Sarasvatī was born at <b>Kārañjā</b> in Vidarbha (Maharashtra) in the 14th century, named Narahari. The child spoke no word, only “Om”, until his sacred-thread ceremony, when he recited the Vedas.',
  'He took sannyāsa and the name Narasiṃha Sarasvatī, and wandered across India, teaching.',
  'He stayed at Narsobāwāḍī on the Kṛṣṇā, and then came to <b>Gāṇagāpura</b>, where he lived continuously for <b>twenty-four years</b>.',
  'Each morning he bathed at the saṅgama and did his practice under the <b>audumbara</b> (cluster-fig) tree; at midday he came to the village for alms.',
  'At the end, the tradition says, he left for Śrīśailam, crossing the river on a seat of flowers, promising to remain at Gāṇagāpura in his formless (nirguṇa) presence for ever.'],
 [('z','He promised never to leave?'),('b','That promise is why the sandals are called nirguṇa: he is held to be present without form, every day, at noon.')],'A promise <b>to stay without form</b>.')
math=reading('nirguna','THE NIRGUṆA MAṬHA','The sandals without attributes',
 S('A shrine with a pair of reddish sandals on a seat, a devotee with ash on his forehead bowing',g(280,200,1.3,tulu_temple('#e0a800','#b8860b',150))+g(280,170,1.3,paduka())+g(120,210,1,person('#f4f1ea'))+g(450,210,1,namaste('#ff8c1a')),'#fff3cf',220),
 ['<b>His house.</b> The <b>Nirguṇa Maṭha</b> stands on the site of the Guru’s āśrama; it is the main shrine of Gāṇagāpura.',
  '<b>The pādukās.</b> It holds the <b>nirguṇa pādukās</b>, the Guru’s sandals, brownish red, worshipped as his formless presence.',
  '<b>Ash first.</b> Devotees apply <b>bhasma</b> (sacred ash) and sit before the pādukās; they are believed to have healing power.',
  '<b>Sevās.</b> Among the offerings is the kesar lepana, saffron paste applied to the sandals, and many readings of the Guru Caritra.',
  '<b>The aśvattha.</b> A sacred aśvattha (peepal) tree stands in the maṭha; the Guru Caritra calls it as powerful as the wish-granting tree.'],
 [('z','Why “without attributes”?'),('b','Nirguṇa means beyond form. The sandals are the sign; the Guru himself is held to be the formless presence they point to.')],'A sign of the Guru <b>who has no form</b>.')
sang=reading('sangama','THE SAṄGAMA','Bath, tree and ash',
 S('Pilgrims bathing at a river meeting, a cluster-fig tree and a small temple, a mound of ash',g(280,200,1,'<rect x="-280" y="-20" width="560" height="20" fill="#4aa3df"/>')+g(150,190,1.4,tree('#2f6a3a'))+T(150,206,'audumbara',10)+g(300,190,.7,tulu_temple())+T(300,206,'Saṅgameśvara',10)+g(440,190,1,'<path d="M-40 0 q40 -40 80 0z" fill="#c9c9c9"/>')+T(440,206,'the ash hill',10),'#e9f2e1',215),
 ['<b>The bath.</b> Pilgrims bathe at the meeting of the Bhīmā and the Amarjā, held to wash away sins; many do so before going to the maṭha.',
  '<b>The audumbara.</b> Under the <b>audumbara</b> tree at the saṅgama the Guru did his practice; the tree is sacred to Datta across the tradition.',
  '<b>The tapobhūmi.</b> Opposite the Saṅgameśvara temple is marked the Guru’s place of penance.',
  '<b>The ash hill.</b> Near the saṅgama is a mound of ash; devotees bathe and apply the ash as purifying.',
  '<b>Thursdays.</b> Thursday is the guru’s day: crowds are largest, and at night the pādukās are carried in palanquin procession.'],
 [('z','An ash hill?'),('b','A mound of ash held sacred by long tradition. Pilgrims touch it to their foreheads, as they would temple bhasma.')],'Bath at the meeting, <b>practice under the fig</b>.')
tirtha=cards('tirthas','THE EIGHT TĪRTHAS','The sacred waters of Gāṇagāpura',
 S('Eight small water pools along a river',''.join(g(50+k*65,190,.9,'<ellipse rx="24" ry="10" fill="#4aa3df"/>') for k in range(8))+'<path d="M0 160 q280 -30 560 0" stroke="#8fb8de" stroke-width="8" fill="none"/>','#e9f2e1',210),
 [('💧','Narasiṃha (Ṣaṭkula) tīrtha','At the saṅgama itself; likened to Prayāga’s Triveṇī.'),('💧','Pāpavināśinī','“The destroyer of sins”.'),('💧','Vārāṇasī (Bhāgīrathī) tīrtha','Held equal to the Gaṅgā at Kāśī.'),('💧','Rudrapāda','Where Rudra’s feet are honoured.'),('💧','Cakra tīrtha','Associated with Viṣṇu’s discus.'),('💧','Koṭi tīrtha','“A crore of tīrthas” in one.'),('💧','Manmatha tīrtha','Named for Kāma.'),('💧','Śrīpāda tīrtha','Named for Śrīpāda Śrīvallabha.')],
 None,'Eight waters, <b>one pilgrimage</b>.',
 intro='The Guru Caritra names the sacred waters of the place; pilgrims make the round of the <b>aṣṭa tīrthas</b>. Lists differ slightly between sources.')
madhu=reading('madhukari','MADHUKARĪ','Alms from five houses',
 S('A pilgrim with a cloth bag receiving food at the doors of village houses',''.join(g(80+k*100,200,1,'<rect x="-34" y="-60" width="68" height="60" fill="#e9d6c0"/><path d="M-40 -60 l40 -24 l40 24z" fill="#a0522d"/><rect x="-10" y="-30" width="20" height="30" fill="#5a3a1a"/>') for k in range(5))+g(240,210,1,person('#ff8c1a'))+g(262,170,.7,'<ellipse rx="14" ry="10" fill="#e9d6c0"/>'),'#fff3cf',220),
 ['<b>The Guru’s noon.</b> The Guru Caritra says the Guru comes to the village every day at noon for alms (bhikṣā).',
  '<b>The custom.</b> So pilgrims practise <b>madhukarī</b>: they take alms from <b>five houses</b> in the village and eat it as the Guru’s prasāda; and they give alms too.',
  '<b>Like the bee.</b> Madhukarī means “like the honey-bee”: a little from many flowers, burdening none. (The bee is one of the Avadhūta’s teachers.)',
  '<b>Humility.</b> Begging for one meal, whatever one’s station, is a lesson in letting go of pride.',
  '<b>Annadāna.</b> The maṭha also feeds pilgrims.'],
 [('z','Even rich pilgrims beg?'),('b','That is the point. At the Guru’s village everyone eats from his hand.')],'Eat <b>like the bee</b>.')
gc=reading('gurucharitra','THE GURU CARITRA','The book of the tradition',
 S('A devotee reading a large book before a small Datta image, with a lamp',g(200,200,1.3,person('#f4f1ea',seat=True))+g(240,160,1,'<rect x="-30" y="-14" width="60" height="14" fill="#fff8e7"/><path d="M0 -14 v14" stroke-width="1.5"/>')+g(400,200,1.3,datta(.8))+g(480,200,1,lamp()),'#fff3cf',215),
 ['<b>The text.</b> The <b>Śrī Guru Caritra</b>, in Marathi verse, recounts the lives of Dattātreya, Śrīpāda Śrīvallabha and Narasiṃha Sarasvatī. It is the most important book of the Datta sampradāya.',
  '<b>Its author.</b> It is traditionally credited to Sarasvatī Gaṅgādhara, a devotee in the Guru’s line. (Tradition.)',
  '<b>Pārāyaṇa.</b> Devotees read it through in set periods, often seven days, as a vow; at Gāṇagāpura many readings are made for a particular wish or trouble.',
  '<b>The promise.</b> It records the Guru’s promise that he remains at Gāṇagāpura, taking alms at noon.',
  '<b>Other books.</b> The Datta Bāvanī and the Avadhūta Gītā are also loved in the tradition.'],
 [('z','A whole book in seven days?'),('b','Fifty-odd chapters, read with discipline: early rising, simple food, steady reading. The vow is the reading.')],'A life of the Guru <b>read as a vow</b>.')
heal=reading('healing','A PLACE OF HEALING','What pilgrims seek',
 S('A family sitting before the shrine, an older woman applying ash to a child’s forehead',g(280,200,1.2,tulu_temple('#e0a800','#b8860b'))+g(140,210,1,person('#8e1f17',seat=True))+g(180,210,.7,person('#e0a800',seat=True))+g(430,210,1,person('#1d4f8a',seat=True)),'#fff3cf',215),
 ['<b>Troubled minds.</b> Gāṇagāpura is widely believed to relieve the troubled: families bring members believed to be afflicted by “spirits” or unrest of mind.',
  '<b>What happens.</b> They bathe at the saṅgama, apply ash, sit before the pādukās, read the Guru Caritra and stay for days.',
  '<b>Faith and care.</b> Many find calm and comfort here. Modern medicine treats mental illness as illness; many families today seek both.',
  '<b>Health and wishes.</b> Others come for children, recovery, work or simply the Guru’s darśana.',
  '<b>The Guru as doctor.</b> In the Guru Caritra the Guru heals and restores; pilgrims come with that story in mind.'],
 [('z','Is it only for the troubled?'),('b','No. Most pilgrims simply come to see their Guru. But the troubled find a welcome there that they may not find elsewhere.')],'A welcome <b>for the troubled</b>.')
fest=cards('festivals','FESTIVALS','The Guru’s year',
 S('A chariot at night with a palanquin of sandals in procession','<rect width="560" height="200" fill="#20243a"/>'+g(160,195,1.3,RATHA(0,0,1,'#ff8c1a'))+g(400,190,1,'<rect x="-40" y="-30" width="80" height="30" fill="#e0a800"/><path d="M-60 -16 h120" stroke="#8a6a3a" stroke-width="5"/>'+g(0,-34,.7,paduka()))+g(480,40,1,moon()),'#20243a',200),
 [('🌕','Datta Jayantī','Mārgaśīrṣa pūrṇimā: Datta’s birthday, with a chariot festival.'),('🙏','Narasiṃha Sarasvatī Jayantī','The Guru’s birthday.'),('🙏','Śrīpāda Śrīvallabha Jayantī','The first human form’s birthday.'),('🪔','Kārtika','The month of lamps, and its full moon.'),('📿','Thursdays','The guru’s weekday; palanquin of the pādukās at night.'),('🌕','Full moons','Every pūrṇimā draws crowds; Guru Pūrṇimā above all.')],
 None,'A year of <b>the Guru’s days</b>.')
endp=end(i,['<b>Datta.</b> Brahmā, Viṣṇu and Śiva in one: the first guru, son of Atri and Anasūyā.','<b>The Guru.</b> Narasiṃha Sarasvatī lived here 24 years and promised to stay.','<b>Shrine.</b> The Nirguṇa Maṭha and the formless Guru’s sandals.','<b>Rites.</b> Bath at the saṅgama, the eight tīrthas, madhukarī, the Guru Caritra.','<b>Days.</b> Thursdays, full moons, Datta Jayantī.'],
 'Part 5, the last, goes to Bādāmi, to Banaśaṅkarī, the Goddess of the forest.','The Guru’s sandals where the rivers meet')
src=sources([('Gāṇagāpura:','Wikipedia, “Ganagapur” (location, rivers, Nirguṇa Maṭha, Kalleśvara, audumbara tree, noon bhikṣā); Hindu Blog (old names from the Guru Caritra, Thursday palkhi, ash, tapobhūmi); AstroVed (24 years, Nirguṇa Maṭha, aśvattha, tīrthas); Karnataka.com (Kārañjā, 14th century, ash and pādukās); kirtankar.com and saiamrithadhara.com (aṣṭa tīrthas, madhukarī, sevās); templeconnect (festivals); Śṛṅgeri Pīṭham (Jagadguru’s visit).'),('Datta:','Bhāgavata Purāṇa 11 (the Avadhūta’s 24 teachers), paraphrased; the Anasūyā story as commonly told.')],
 'the Guru’s dates, birthplace story, departure to Śrīśailam and the authorship of the Guru Caritra are tradition; lists of the eight tīrthas differ; healing beliefs are described, not endorsed as medical claims.','Story of the Guru as in the Guru Caritra tradition.')
finish(i,'PART 4 OF 5 · DATTĀTREYA · THE GURU · THE SANDALS',covart('Dattātreya with three heads beside a pair of sandals and a cluster-fig tree by a river',g(140,190,1.4,datta())+g(300,190,1.4,paduka())+g(390,190,1,tree('#2f6a3a'))+'<path d="M0 194 h440" stroke="#8fb8de" stroke-width="8"/>'),'The Guru’s seat on the Bhīmā',
 '<b>Gāṇagāpura</b>: <b>Dattātreya</b> and his human forms, the life of <b>Narasiṃha Sarasvatī</b>, the nirguṇa sandals, the saṅgama, <b>madhukarī</b> and the Guru Caritra.',
 'Gāṇagāpura Dattātreya explained and illustrated: Dattātreya, Anasūyā’s story and the 24 teachers, Śrīpāda Śrīvallabha and Narasiṃha Sarasvatī, the Nirguṇa Maṭha and pādukās, the Bhīmā–Amarjā saṅgama, aṣṭa tīrthas, madhukarī, the Guru Caritra and Datta Jayantī.',
 [fw,gl,where,who,anas,gurus,forms,life,math,sang,tirtha,madhu,gc,heal,fest,endp,src])
