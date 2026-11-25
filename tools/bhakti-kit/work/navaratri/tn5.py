from tn_common import *
i=4
def pmap():
    o=map_frame(sea=False)+'<path d="M560 60 q-200 10 -300 30 q-60 20 -60 140" fill="none" stroke="#8fb8de" stroke-width="12"/>'+T(420,52,'Phalguṇī river',10,fill='#1d4f8a')
    o+=pin(250,140,'Rājarājeśvarī temple')+'<rect x="170" y="160" width="160" height="50" fill="#d8efc8" stroke-dasharray="5 4"/>'+T(250,190,'the Ceṇḍu field',10)+pin(340,196,'Sultān Kaṭṭe',.3)+pin(420,150,'Siṃhāsana Kaṭṭe',.3)
    o+=T(100,120,'village A',11,fill='#c0392b')+T(420,230,'village B',11,fill='#1d4f8a')+pin(60,60,'Mijār (ball makers)',.3)
    return o
fw=foreword(i,['For a month every spring, a village fifteen kilometres from Maṅgaḷūru turns into a fair. In the middle of it a goddess of clay, nine feet tall, receives the whole coast; and near the end, two villages play five days of football in front of her temple with a leather ball stitched by a cobbler family who have made it for generations.',
 'This is the <b>Poḷali Jātre</b>. This guide covers the clay Rājarājeśvarī and King Suratha who is said to have made her, the month from Mīna saṅkramaṇa to the final bath, the Siṃhāsana Kaṭṭe, and above all the <b>Poḷali Ceṇḍu</b>: who makes the ball, who carries it, how the game goes and what it means.',
 'The temple is in '+L('/tulunadu/temples/polali-rajarajeshwari/','Poḷali Rājarājeśvarī')+'; King Suratha’s story in '+L('/devi/devi-mahatmya/','Devī Māhātmya')+'. Previous: '+L('/tulunadu/festivals/laksha-deepotsava/','Lakṣa Dīpotsava')+'.'],
 [('z','Football as worship?'),('b','The Goddess likes a good game. And every family that touches the ball has a role in her service.')])
gl=glance([('Where','Śrī Rājarājeśvarī temple, Poḷali, Kariyaṅgaḷa village, Baṇṭvāḷa tālūk, about 19 km from Maṅgaḷūru'),('Goddess','Rājarājeśvarī (Lalitā Tripurasundarī), a seated clay image 9–10 ft tall'),('Founder','By tradition King Suratha of the Devī Māhātmya'),('When','A month: from Mīna saṅkramaṇa (mid-March) to the avabhṛtha (mid-April)'),('Day 4','The image goes to the Siṃhāsana Kaṭṭe'),('The Ceṇḍu','Five days of a ball game, starting seven days before the final bath'),('Ball makers','A hereditary cobbler family of Mijār'),('Ball carriers','An oil-miller family of Kaḍapu Kariya'),('Players','Two villages, one on each side of the temple'),('Then','The chariot festival and the closing bath')],
 S('A leather ball above a temple with two crowds facing each other',g(280,110,2.5,ball())+g(280,190,.9,tulu_temple())+g(110,190,1,crowd(5,140,0,.5))+g(450,190,1,crowd(5,140,0,.5)),'#e3eaf3',200),
 [('z','How big is the crowd?'),('b','Up to about five hundred have joined the game; the watchers are many more.')],'A month-long fair, <b>a five-day game</b>.')
place=reading('place','POḶALI','Hills, paddy and the Phalguṇī',svg(560,230,'Simplified map of Poḷali: the temple, the river, the Ceṇḍu field, the Sultān and Siṃhāsana kaṭṭes and the two villages',pmap()),
 ['<b>The setting.</b> Poḷali lies in Kariyaṅgaḷa village of Baṇṭvāḷa tālūk, ringed by low hills and paddy fields.',
  '<b>The river.</b> The Phalguṇī (Gurupura) flows past the north side of the temple and turns south behind it.',
  '<b>The field.</b> Before the temple lies the open ground where the Ceṇḍu is played, with the platform called the <b>Sultān Kaṭṭe</b> at its edge.',
  '<b>Two villages.</b> The game is played between the villages on either side of the temple.',
  '<b>Old names.</b> The place was Pural; inscriptions call the goddess Poraḷa Dēvi. The game is also called <b>Pural da Ceṇḍu</b>, “the ball of Pural”.'],
 [('z','Is Poḷali a town?'),('b','A village, with one of the oldest goddesses of the coast and, for a month, one of its biggest fairs.')],'A village goddess <b>with a field before her</b>.')
godd=reading('goddess','RĀJARĀJEŚVARĪ OF CLAY','The queen of kings',
 S('A tall seated goddess of clay with a crown, flanked by smaller clay figures',g(280,200,2.1,devi(sari='#c0392b',items=('lotus','hook')))+g(110,200,1,ganesha())+g(450,200,1.1,devi(sari='#3a3a50',items=('sword',),fierce=True)),'#f6e3e1',210),
 ['<b>The name.</b> <b>Rājarājeśvarī</b>, “Sovereign of the King of Kings”, is a name of Lalitā Tripurasundarī after her coronation. See '+L('/srividya/','Śrīvidyā')+'.',
  '<b>Of clay.</b> She is a seated image about nine to ten feet tall, made of clay from different soils mixed with herbal ingredients. A clay image of this size is described as probably the only one of its kind in Karnataka.',
  '<b>Lēpāṣṭagandha.</b> About every twelve years the images receive a fresh coat of earth mixed with eight fragrant and medicinal substances.',
  '<b>Her family.</b> Beside her are clay images of <b>Subrahmaṇya</b>, <b>Bhadrakāḷī</b> and <b>Mahāgaṇapati</b>, with Durgāparameśvarī.',
  '<b>Old worship.</b> An inscription near the temple is cited for the 8th century; the Āḷupa kings are credited with promoting her worship.'],
 [('z','Clay doesn’t last, does it?'),('b','This clay has lasted centuries, with care. The re-coating every twelve years is that care made into a festival.')],'A queen <b>made of the earth</b>.')
sur=story('suratha','STORY · KING SURATHA','The king who made a goddess of earth',
 strip('Three panels: a defeated king riding into a forest; the king and a merchant listening to a sage; the king shaping a clay goddess by a river',
  [('<rect width="144" height="190" fill="#e9f2e1"/>'+g(40,170,.8,tree('#2f6a3a'))+g(100,170,.9,person('#8e1f17')),'#e9f2e1'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(40,170,.8,sage())+g(90,170,.75,person('#8e1f17',seat=True))+g(122,170,.75,person('#1d4f8a',seat=True)),'#fff3cf'),
   ('<rect width="144" height="190" fill="#bcd3ea"/><rect y="160" width="144" height="30" fill="#4aa3df"/>'+g(50,160,.8,person('#8e1f17',seat=True))+g(104,160,.6,devi(sari='#c98a5a',items=())),'#bcd3ea')],
  ['a king undone','the sage’s teaching','an image of earth']),'From the frame story of the Devī Māhātmya, with the local tradition of Poḷali.',
 ['King <b>Suratha</b> lost a war, and his own ministers seized his treasury. He rode alone into the forest.',
  'At the hermitage of the sage <b>Medhas</b> he met a merchant, <b>Samādhi</b>, cast out by his own family.',
  'The sage told them the deeds of the Goddess: the slaying of Madhu and Kaiṭabha, of Mahiṣa, of Śumbha and Niśumbha.',
  'The two men went to a riverbank, made an image of the Goddess from <b>earth</b>, and worshipped it for three years. She appeared: Suratha won back his kingdom; Samādhi asked for wisdom.',
  'Poḷali’s tradition places that riverbank here: Suratha shaped this clay image, and set his own jewelled crown on her head.'],
 [('z','So the Devī Māhātmya’s clay image is this one?'),('b','So Poḷali believes. The text names no place; the coast gave the story a home.')],'A king’s clay goddess <b>by the Phalguṇī</b>.')
month=reading('month','THE MONTH','Mīna saṅkramaṇa to the final bath',
 svg(560,140,'Timeline of the Poḷali jātre from Mīna saṅkramaṇa to the avabhṛtha','<rect width="560" height="140" fill="#fff3cf"/>'+tl_strip([('Day 1','Mīna saṅkramaṇa'),('Day 4','Siṃhāsana Kaṭṭe'),('Weeks','nights, fair, plays'),('−7 days','Ceṇḍu begins'),('Ratha','chariot'),('End','avabhṛtha bath')],560,140)),
 ['<b>Day 1.</b> The festival begins on <b>Mīna saṅkramaṇa</b>, the sun’s entry into Pisces, in mid-March.',
  '<b>Day 4.</b> The festival image, set on a circular crown-frame called the <b>prabhāvaḷi</b>, is carried to the <b>Siṃhāsana Kaṭṭe</b>, a platform about 100 m from the temple, for a special worship.',
  '<b>The weeks.</b> Nightly processions, music, Yakṣagāna and a large fair around the temple.',
  '<b>The Ceṇḍu.</b> The five days of the ball game begin seven days before the final bath.',
  '<b>The end.</b> The great chariot festival (rathōtsava), and then the <b>avabhṛtha</b>, the closing bath of the festival image, in mid-April, just before Bisu.'],
 [('z','A whole month?'),('b','One of the longest festivals on the coast, and timed to end just before the Tuḷu new year.')],'A month of fair, <b>ending in a bath</b>.')
fair=reading('fair','THE FAIR AND THE NIGHTS','Processions, plays and stalls',
 S('A night fair with stalls, a giant wheel and a Yakṣagāna stage beside the temple','<rect width="560" height="200" fill="#20243a"/>'+''.join(g(50+k*70,190,.8,'<rect x="-28" y="-36" width="56" height="36" fill="#e9d6c0"/><path d="M-32 -36 l32 -16 l32 16z" fill="'+['#c0392b','#1d4f8a','#2a9d6f','#e0a800'][k%4]+'"/>') for k in range(4))+'<circle cx="380" cy="110" r="60" fill="none" stroke="#ffd60a" stroke-width="3"/>'+''.join(f'<path d="M380 110 l{60*__import__("math").cos(a/4):.0f} {60*__import__("math").sin(a/4):.0f}" stroke="#ffd60a"/>' for a in range(0,25,3))+g(500,190,.8,person('#c0392b'))+'<path d="M484 120 l16 -24 l16 24z" fill="#e0a800"/>','#20243a',200),
 ['<b>Every night.</b> The festival image is taken out in procession each night with drums and lamps.',
  '<b>Yakṣagāna.</b> Troupes play through the nights; temple festivals like this are the backbone of the Yakṣagāna season. See '+L('/tulunadu/culture/yakshagana/','Yakṣagāna')+'.',
  '<b>The fair.</b> Stalls of sweets, toys, bangles, household goods and rides fill the grounds: one of the great spring gatherings of Tuḷunāḍu.',
  '<b>From across the coast.</b> Devotees come from all over Dakṣiṇa Kannaḍa and beyond.',
  '<b>Before the rains.</b> Like every jātre it must finish well before Pattanāje in late May (see '+L('/tulunadu/festivals/tulu-year/','The Tuḷu Year')+').'],
 [('z','Is the fair religious?'),('b','On the coast the jātre is both: the Goddess at the centre, and the whole village celebrating around her.')],'A goddess at the centre <b>of a village fair</b>.')
ballp=reading('ball','THE BALL','Made by one family, carried by another',
 S('A cobbler stitching a leather ball; an oil-miller carrying it; the ball set in a swept courtyard',g(100,180,1,person('#8e1f17',seat=True))+g(140,160,1.4,ball('#8a4a2a'))+T(110,198,'Mijār: the makers',10)+g(280,180,1,person('#e0a800'))+g(300,120,1.2,ball('#8a4a2a'))+T(290,198,'Kaḍapu Kariya: the carriers',10)+g(460,170,1,'<ellipse rx="70" ry="14" fill="#e9d6c0"/>'+g(0,-10,1.3,ball('#8a4a2a')))+T(460,198,'Maḷali Ballāḷ’s yard',10),'#fff3cf',205),
 ['<b>Ceṇḍu.</b> Ceṇḍu in Kannaḍa, cend in Tuḷu: a ball. The game is <b>Poḷali Ceṇḍu</b> or <b>Pural da Ceṇḍu</b>.',
  '<b>The makers.</b> A hereditary <b>cobbler family of Mijār</b> stitches the leather ball each year; it is their right and their honour.',
  '<b>Worshipped first.</b> Before it leaves the maker’s house, the ball is worshipped there before the family’s goddess.',
  '<b>The carriers.</b> An <b>oil-miller family of Kaḍapu Kariya</b> fetches the ball from Mijār and announces the day the game will begin.',
  '<b>The first resting place.</b> They set it down in the freshly cleaned front yard of the <b>Maḷali Ballāḷ</b> house before it goes on to the temple.'],
 [('z','Why so many families for one ball?'),('b','Because the village is the team. Cobbler, oil-miller, landlord, priest: each has a part, and none can play without the others.')],'A ball that <b>passes through many hands</b>.')
gate=reading('gateway','THE BALL ON THE GATEWAY','The first evening',
 S('A leather ball and a palm-leaf umbrella set on top of a temple gateway at dusk','<rect width="560" height="200" fill="#e9b07a"/>'+g(280,190,1.8,tulu_temple('#a0522d','#5a2a10',140))+g(260,58,1.1,ball('#8a4a2a'))+g(300,58,1,'<path d="M-20 0 q20 -26 40 0z" fill="#d8b878"/><path d="M0 0 v14" stroke-width="2"/>'),'#e9b07a',200),
 ['<b>Handed to the priest.</b> On the day of the Ceṇḍu, the family brings the ball to the temple and hands it to the priest in charge.',
  '<b>On the gateway.</b> On the first evening the cobbler family places the ball and a <b>palm-leaf umbrella</b> on top of the temple gateway.',
  '<b>Worship.</b> The ball is worshipped there as an offering to the Goddess.',
  '<b>To the field.</b> After the worship, the priest carries it in a ceremonial walk to the field in front of the temple.',
  '<b>A ball as prasāda.</b> By the time it reaches the players, the ball has been blessed by the Goddess: it is her ball.'],
 [('z','Why an umbrella?'),('b','An umbrella is a mark of honour, held over kings and gods. The ball is given royal honours.')],'The ball <b>receives royal honours</b>.')
game=story('game','THE CEṆḌU','Two villages, one ball, five days',
 strip('Three panels: a man throwing the ball in from a platform; a mass of players kicking it across the field; the ball reaching one side and the crowd cheering',
  [('<rect width="144" height="190" fill="#d8efc8"/>'+g(50,160,.8,'<rect x="-30" y="-14" width="60" height="14" fill="#b08a62"/>'+g(0,-14,1,person('#f4f1ea')))+g(100,90,1,ball('#8a4a2a')),'#d8efc8'),
   ('<rect width="144" height="190" fill="#d8efc8"/>'+g(72,170,1,crowd(6,120,0,.55))+g(72,120,1,ball('#8a4a2a')),'#d8efc8'),
   ('<rect width="144" height="190" fill="#d8efc8"/>'+g(110,170,.9,crowd(3,50,0,.55))+g(130,120,1,ball('#8a4a2a'))+g(40,60,.6,fireworks()),'#d8efc8')],
  ['the throw-in','the scrum','one side wins']),'The Poḷali Ceṇḍu, from temple and press accounts.',
 ['<b>When.</b> Five days, starting seven days before the final bath (avabhṛtha).',
  '<b>Start.</b> The guttu families (old landed houses) wait at the Sultān Kaṭṭe; a man who holds the hereditary right throws the ball in.',
  '<b>Sides.</b> Two villages, one on each side of the temple. There is no fixed number of players; up to about five hundred have joined.',
  '<b>Aim.</b> To drive the ball to the opponents’ side. No referee, no fixed team size, no clock; trustees recall crowds so thick no one could see the ball once play began.',
  '<b>Meaning.</b> The contest stands for dharma against adharma; the chariot festival that follows marks the victory.'],
 [('z','Is it like modern football?'),('b','Only loosely. It is closer to the old village games of Europe than to a stadium match, and it is played for a Goddess.')],'A game <b>played as a rite</b>.')
sultan=reading('sultan','THE SULTĀN KAṬṬE','A platform with a story',
 S('A stone platform at the edge of a field with a figure in a turban watching a ball game',g(160,180,1.4,'<rect x="-60" y="-24" width="120" height="24" fill="#b08a62"/>'+g(0,-24,1,person('#2a9d6f',seat=True))+'<ellipse cy="-62" rx="12" ry="6" fill="#fff"/>')+g(400,180,1,crowd(6,200,0,.55))+g(400,110,1,ball('#8a4a2a')),'#d8efc8',195),
 ['<b>The name.</b> The platform at the edge of the field is called the <b>Sultān Kaṭṭe</b>, “the Sultan’s platform”.',
  '<b>The story.</b> Local tradition says <b>Tipu Sultān</b> admired the Poḷali Ceṇḍu and had a platform built to watch the game. (Tradition; not independently checked.)',
  '<b>Its use.</b> Today the guttu families gather there before the throw-in.',
  '<b>A many-sided past.</b> The coast’s temples passed under many rulers: Āḷupas, Vijayanagara, Keḷadi, Mysore. Stories like this one survive alongside the rites.',
  '<b>Read more.</b> On Tipu and the temples of Mysore, see '+L('/temples-of-india/around-mysuru/tipu-and-the-temples/','Tipu and the Temples')+'.'],
 [('z','Did Tipu really watch?'),('b','We don’t know. The platform is real; the story is what the village tells.')],'A platform, <b>and the story it carries</b>.')
ratha=reading('ratha','THE CHARIOT AND THE BATH','Victory and the close',
 S('A great chariot pulled by crowds, then the festival image bathed in the river',g(160,195,1.4,RATHA(0,0,1,'#c0392b'))+g(160,200,1,crowd(6,200,0,.45))+'<rect x="330" y="150" width="230" height="50" fill="#4aa3df"/>'+g(450,160,.8,devi(items=()))+g(400,160,.8,sage()),'#e3eaf3',205),
 ['<b>Rathōtsava.</b> After the Ceṇḍu the Goddess rides in the great chariot, pulled by the crowd: the victory the game foretold.',
  '<b>Avabhṛtha.</b> The festival closes with the <b>avabhṛtha</b>, the ritual bath of the festival image, in mid-April.',
  '<b>Why a bath.</b> Avabhṛtha is the old Vedic name for the bath that ends a great sacrifice: the festival is treated as one long offering, now complete.',
  '<b>Flag down.</b> With the bath the festival flag is lowered and the temple returns to its daily worship.',
  '<b>Then Bisu.</b> A day or two later the Tuḷu year turns at Bisu.'],
 [('z','Why does a festival end with a bath?'),('b','Every great rite ends by washing: you return to ordinary life clean.')],'Victory, then <b>a cleansing bath</b>.')
year=cards('year','THROUGH THE YEAR','The Goddess’s other days',
 S('A row of icons: paddy sheaves, lamps, a serpent, a moon and a liṅga',g(80,150,1.2,'<path d="M0 0 q-4 -30 6 -48 M0 0 q4 -26 -6 -44" fill="none" stroke="#b8860b" stroke-width="4"/>')+g(180,150,1,lamps_row(-30,0,4,20,.45))+g(280,150,1.5,'<path d="M-20 0 q0 -30 20 -30 q20 0 10 14 q-10 10 0 16" fill="none" stroke="#2a9d6f" stroke-width="6"/>')+g(380,130,1.6,moon())+g(480,150,.8,LINGA(0,0,1)),'#e3eaf3',170),
 [('🌾','Kadiru habba','The first sheaves of the new crop brought to the temple (Koral Parba).'),('🪔','Lights','Navarātri, Dīpāvali, and a Lakṣa Dīpotsava on the Kārtika new moon.'),('🐍','Subrahmaṇya','Subrahmaṇya Ṣaṣṭhī for the clay Subrahmaṇya.'),('❄️','Dhanurmāsa','The month of dawn worship in winter.'),('🔱','Śivarātri','The night of Śiva.'),('🎪','The jātre','The month-long spring festival and the Ceṇḍu.')],
 [('z','Busy goddess!'),('b','The queen of kings keeps a full court calendar.')],'A full court calendar <b>for the queen</b>.')
endp=end(i,['<b>Goddess.</b> Rājarājeśvarī of clay, said to be made by King Suratha.','<b>Month.</b> Mīna saṅkramaṇa to the avabhṛtha, with nightly processions and a great fair.','<b>Ball.</b> Stitched in Mijār, carried by Kaḍapu Kariya, worshipped on the gateway.','<b>Game.</b> Two villages, five days, dharma against adharma.','<b>Close.</b> The chariot and the closing bath, just before Bisu.'],
 'Part 6 goes to the island temple of Kaṭīl and its year of festivals.','A Goddess’s fair and her ball game')
src=sources([('The temple and game:','Our '+L('/tulunadu/temples/polali-rajarajeshwari/','Poḷali Rājarājeśvarī')+' guide; IndiaNetzone (Ceṇḍu, Mijār and Kaḍapu Kariya families, Maḷali Ballāḷ); Swarajya on the game and the priest’s walk to the field; NewsKarnataka on the ball maker and its worship; Bharatpedia on the Sultān Kaṭṭe tradition.')],
 'the Tipu Sultān story is local tradition; player numbers are recollections; the order of rites on the first evening follows our temple guide; the 8th-century inscription is as cited in secondary sources.','Festival structure as in our temple guide.')
finish(i,'PART 5 OF 9 · THE FAIR · THE BALL · THE GODDESS',covart('Two crowds of players chasing a leather ball before a temple',g(220,180,1,tulu_temple())+g(220,80,2,ball('#8a4a2a'))+g(80,190,1,crowd(4,100,0,.6))+g(360,190,1,crowd(4,100,0,.6))),'The ball game of the Goddess',
 'The <b>Poḷali Jātre</b>: the clay <b>Rājarājeśvarī</b> and King Suratha, a <b>month-long fair</b>, and the <b>Ceṇḍu</b>, the ball game played as a rite.',
 'Poḷali Jātre explained and illustrated: the clay Rājarājeśvarī and King Suratha, the month from Mīna saṅkramaṇa to the avabhṛtha, the Siṃhāsana Kaṭṭe, the Poḷali Ceṇḍu ball game, its makers and carriers, the Sultān Kaṭṭe and the chariot.',
 [fw,gl,place,godd,sur,month,fair,ballp,gate,game,sultan,ratha,year,endp,src])
