from tn_common import *
i=1
def nd(c,items=('trident','lotus')): return devi(sari=c,items=items)
fw=foreword(i,['Every Navarātri, a temple in the north-west of Maṅgaḷūru fills its great hall with ten goddesses: the nine forms of Durgā and, above them, Śāradā, the Goddess of learning. For ten days the city queues to see them. On the last night they ride out on lit floats with tigers dancing round them, and the city stays awake until they come home at dawn.',
 'This is the <b>Maṅgaḷūru Dasarā</b>, the common people’s Dasarā: no king, no state money, only a temple and its city. This guide covers how it began in 1991, the Navadurgās and Śāradā, the pilivēṣa tigers, the great procession, the widow priests, and the older Navarātri strands of Car Street and Maṅgaḷādevī.',
 'The temple itself is in our guide to '+L('/tulunadu/temples/kudroli-gokarnanatha/','Kudroḷi Gokarṇanātha')+'; the nine Durgās in '+L('/festivals/navaratri/','Navarātri and Dasarā')+'.'],
 [('z','Two Dasarās in one state?'),('b','Mysuru’s is a royal one with an elephant; Maṅgaḷūru’s is a people’s one with tigers. Both are worth seeing.')])
gl=glance([('What','The Navarātri–Dasarā festival of Maṅgaḷūru city'),('Centre','Kudroḷi Śrī Gokarṇanātha Kṣetra, a Śiva temple consecrated by Nārāyaṇa Guru in 1912'),('Since','1991, when the renovated temple opened and the Navadurgās were first installed'),('Goddesses','The nine Durgās with Śāradā, plus Ādiśakti and Mahāgaṇapati'),('Last three days','Śāradā Mahotsava'),('Vijayadaśamī','An all-night procession of floats through the city'),('Signature','Pilivēṣa tiger dancers'),('Patrons','The city’s devotees: no royal or government patronage'),('Crowds','Organisers estimate over 12 lakh temple visitors and 5 lakh on the route'),('Other strands','Car Street Śāradā Mahotsava; Maṅgaḷādevī’s chariot to Mārnamikaṭṭe')],
 S('Ten goddess figures in a row in a great hall, Śāradā in the centre',''.join(g(40+k*54,170,.55,nd(['#c0392b','#e0a800','#1d4f8a','#2a9d6f','#8e1f17','#6a3d9a','#3a3a50','#f4f1ea','#ff8c1a'][k])) for k in range(4))+g(280,175,.85,devi(skin='#f6efe2',sari='#f4f1ea',items=('book','rosary')))+''.join(g(334+k*54,170,.55,nd(['#2a9d6f','#8e1f17','#6a3d9a','#3a3a50','#ff8c1a'][k])) for k in range(5)),'#e3eaf3',200),
 [('z','Ten goddesses in one hall?'),('b','Nine Durgās around one Śāradā. Organisers say no other temple installs all of them together.')],'Nine Durgās, one Śāradā, <b>one city</b>.')
def citymap():
    o=map_frame()
    o+='<path d="M150 20 q60 80 40 200" fill="none" stroke="#8fb8de" stroke-width="10"/>'+T(196,30,'Phalguṇi river',9,fill='#1d4f8a')
    pts=[('Kudroḷi Gokarṇanātha',260,60),('Car Street · Veṅkaṭaramaṇa',300,110),('Hampankaṭṭa',360,150),('Maṅgaḷādevī',260,200),('Mārnamikaṭṭe',380,196)]
    for t,x,y in pts: o+=pin(x,y,t)
    o+='<path d="M268 64 C340 70 420 90 400 140 C380 170 300 150 268 70" fill="none" stroke="#c0392b" stroke-width="3" stroke-dasharray="7 5"/>'+T(470,80,'procession loop',10,fill='#c0392b')
    return o
where=reading('where','THE CITY OF THE GODDESS','Where the Dasarā happens',svg(560,230,'Simplified map of old Maṅgaḷūru with Kudroḷi, Car Street, Maṅgaḷādevī and Mārnamikaṭṭe, and the procession loop',citymap()),
 ['<b>Named for a Goddess.</b> Maṅgaḷūru takes its name from <b>Maṅgaḷādevī</b>, “the auspicious Goddess”, whose shrine stands near the river mouth. A Navarātri here has deep roots. See '+L('/tulunadu/temples/mangaladevi/','Maṅgaḷādevī')+'.',
  '<b>Kudroḷi.</b> The Gokarṇanātha temple lies in the north-west of the old city, near the harbour and the mouth of the Phalguṇi (Gurupura) river. The procession leaves from it and returns to it.',
  '<b>Car Street.</b> The old Gauḍa Sārasvata quarter around the Veṅkaṭaramaṇa temple holds its own Śāradā Mahotsava, a century old.',
  '<b>Mārnamikaṭṭe.</b> “The Navarātri platform”, with its śamī tree, where Maṅgaḷādevī’s chariot goes on Vijayadaśamī.',
  '<b>The route.</b> Through Lālbāgh, PVS junction, Hampankaṭṭa, GHS Road and New Chitra, back to Kudroḷi: some 10 km through the night.'],
 [('z','Is it one festival or several?'),('b','One city, several Navarātris. Since 1991 the Kudroḷi procession is the one the city calls “the” Dasarā.')],'One city, <b>several Navarātris</b>.')
temple=reading('temple','THE TEMPLE OF ALL','Kudroḷi, Nārāyaṇa Guru and Koragappa',
 S('The Kudroḷi temple gateway with a saint in white beside it',g(330,190,1.4,tulu_temple('#e0a800','#b8860b',150))+g(130,190,1.4,sage('#f4f1ea'))+T(130,205,'Nārāyaṇa Guru',10),'#e3eaf3',210),
 ['<b>A closed door.</b> In early 20th-century Maṅgaḷūru the <b>Billavas</b>, a large community of the coast, were barred from many temples. The Billava elder <b>Hoige Bazar Koragappa</b> resolved that they should have a temple of their own.',
  '<b>The Guru.</b> In 1908 he led a delegation to Kerala to invite <b>Śrī Nārāyaṇa Guru</b>, the saint who taught “one caste, one religion, one God”. In 1912 the Guru consecrated a liṅga at Kudroḷi and named it <b>Gokarṇanātha</b>.',
  '<b>Renewal.</b> From 1989 the temple was rebuilt through voluntary service (kar sevā) led by the Congress leader <b>B. Janārdhana Pūjāry</b>; the renovated temple, in Kerala style with gold-toned gateways, was inaugurated in 1991 by Rajiv Gandhi.',
  '<b>A Dasarā is born.</b> The same year the kṣetra began installing the Navadurgās for Navarātri. The idea of a “Maṅgaḷūru Dasarā” came from Pūjāry.',
  '<b>Open to all.</b> The festival carries the temple’s founding idea: a great celebration of the Goddess open to every community.'],
 [('z','A Śiva temple holds the Goddess festival?'),('b','Śiva’s house is the Goddess’s house too. And Kudroḷi’s hall was big enough for ten of her.')],'A temple for all <b>became a Dasarā for all</b>.')
nine=cards('navadurga','THE NAVADURGĀS','Nine forms of the Goddess in one hall',
 S('Nine goddess figures in a row',''.join(g(34+k*62,175,.62,nd(['#c0392b','#f4f1ea','#e0a800','#ff8c1a','#2a9d6f','#8e1f17','#3a3a50','#f6efe2','#e05050'][k])) for k in range(9)),'#e3eaf3',190),
 [('🏔️','Śailaputrī','Daughter of the mountain'),('📿','Brahmacāriṇī','The ascetic in penance'),('🔔','Candraghaṇṭā','With the bell-shaped moon'),('🌞','Kūṣmāṇḍā','Who laughed the cosmos into being'),('👶','Skandamātā','Mother of Skanda'),('⚔️','Kātyāyanī','Born in the sage Kātyāyana’s home'),('🌑','Kālarātri','The dark night that destroys fear'),('🤍','Mahāgaurī','The radiant white one'),('✨','Siddhidātrī','Giver of every perfection')],
 None,'All nine at once, <b>every day of the festival</b>.',
 intro='At Kudroḷi the nine images are consecrated together at the start of Navarātri, with Ādiśakti and Mahāgaṇapati. Read each Goddess in full in our '+L('/festivals/navaratri/','Navarātri')+' series.')
sharada=reading('sharada','ŚĀRADĀ','The Goddess of learning at the centre',
 S('A large seated Śāradā with a book and vīṇā, lit by lamps, people with folded hands below',g(280,200,2,devi(skin='#f6efe2',sari='#f4f1ea',items=('book','rosary')))+lamps_row(120,200,6,64,.6)+g(70,200,1,namaste('#8e1f17'))+g(490,200,1,namaste('#1d4f8a')),'#e3eaf3',210),
 ['<b>The centre of the hall.</b> Śāradā, the Goddess of learning (Sarasvatī), sits at the heart of the Kudroḷi Navarātri. Her image is described as one of the largest in the country.',
  '<b>Installation.</b> The festival begins with her consecration in the temple, together with the Navadurgās, Ādiśakti and Gaṇeśa.',
  '<b>Śāradā Mahotsava.</b> The last three days of Navarātri are her own festival, adding to the daily worship of the nine Durgās.',
  '<b>Why Śāradā.</b> In Karnataka Navarātri has long been a festival of learning: books and tools are worshipped, and children begin their letters. The coast’s Śāradā festivals carry that thread. See '+L('/festivals/navaratri/','Sarasvatī Pūjā')+'.',
  '<b>The Car Street Śāradā.</b> Another Śāradā Mahotsava, the city’s older one, is held at Car Street (its own page in this guide).'],
 [('z','Why so big?'),('b','A city festival needs a Goddess the city can see from the back of the queue.')],'Learning <b>at the heart of the festival</b>.')
days=reading('days','TEN DAYS IN THE HALL','Worship, music and plays',
 S('A temple stage with a Yakṣagāna actor, musicians and a crowd watching',g(280,150,1,'<rect x="-120" y="-20" width="240" height="20" fill="#a0522d"/>')+g(280,130,1.1,person('#c0392b'))+'<path d="M258 50 l22 -30 l22 30z" fill="#e0a800"/>'+g(200,130,.8,drum())+g(360,130,.8,person('#1d4f8a',seat=True))+g(280,200,1,crowd(12,480,0,.5)),'#fff3cf',205),
 ['<b>Daily pūjās.</b> Through the nine nights the Goddesses are worshipped morning and evening with lamps, flowers and ārati, and the hall fills with queues.',
  '<b>Stages.</b> The temple’s stages carry music, dance and <b>Yakṣagāna</b> every evening. See '+L('/tulunadu/culture/yakshagana/','Yakṣagāna')+'.',
  '<b>Homas.</b> Special fire offerings are held through the festival, including the Caṇḍikā hōma.',
  '<b>The city.</b> Streets around Kudroḷi are lit, and many of the city’s temples, homes and halls install their own Śāradā images.',
  '<b>Paid by the people.</b> The whole cost is borne by devotees and well-wishers of the city.'],
 [('z','How many come?'),('b','Organisers estimate over twelve lakh across the ten days. Treat the number as theirs; the queues are real.')],'Ten days of <b>queues, lamps and plays</b>.')
pili=reading('pilivesha','THE PILIVĒṢA','Maṅgaḷūru’s tiger dancers',
 S('Three tiger dancers in yellow and black stripes leaping to drums',g(120,190,1.4,tiger_dancer(1))+g(280,190,1.5,tiger_dancer(-1))+g(440,190,1.4,tiger_dancer(1))+g(530,170,.9,drum()),'#fde9c8',200),
 ['<b>The tigers.</b> <b>Pilivēṣa</b> (“tiger costume”, Kannaḍa huli vēṣa) is the Navarātri dance of the Tuḷu coast: men painted from head to foot in yellow, black and white tiger stripes, with tails and masks.',
  '<b>The dance.</b> To the beat of the <b>tāse</b> drums they leap, crouch and prowl; the best perform acrobatic feats, such as bending back to pick up money with their mouths.',
  '<b>Through the streets.</b> Troupes go from house to house and shop to shop during Navarātri, collecting gifts, and join the Dasarā procession in force, alongside bear dancers (karaḍi vēṣa).',
  '<b>A vow.</b> Many dancers take the paint as a vow (harake) to the Goddess. The paint stings and has to stay on for days.',
  '<b>Why tigers.</b> Many say they honour the Goddess whose mount is the tiger (or lion). (Popular explanation.)'],
 [('z','Is the paint safe?'),('b','It was harsh in the old days. Many troupes now use gentler paints. The vow stays the same.')],'Tigers who dance <b>as a vow to the Goddess</b>.')
proc=story('procession','THE ŚŌBHĀYĀTRE','The Vijayadaśamī procession',
 strip('Three panels: goddess images placed on lit floats outside the temple; a long night procession with umbrellas and tigers; images returning to the temple tank at dawn',
  [('<rect width="144" height="190" fill="#20243a"/>'+g(72,170,.9,float_cart(devi(items=('book',)),'#c0392b'))+g(72,80,.6,tulu_temple('#e0a800','#b8860b')),'#20243a'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(40,170,.7,float_cart(devi(items=('trident',)),'#1d4f8a'))+g(108,170,.8,tiger_dancer())+g(72,60,.6,fireworks()),'#20243a'),
   ('<rect width="144" height="190" fill="#f6c87a"/>'+g(72,190,.9,tank(140))+g(72,150,.6,devi(items=('book',))),'#f6c87a')],
  ['onto the floats','through the night','home at dawn']),'The last night of the Maṅgaḷūru Dasarā, as reported year after year.',
 ['On Vijayadaśamī evening the Navadurgās, Ādiśakti, Gaṇeśa and Śāradā are carried out of the temple and set on decorated, lit floats.',
  'The procession sets out from Kudroḷi in the evening. Before and around the goddesses come <b>75 to 100 tableaux</b>, from the temple and from groups across Dakṣiṇa Kannaḍa, Uḍupi and Kāsaragoḍu.',
  'With them: bands and ceṇḍe drums, hundreds of Kerala parasols, Yakṣagāna characters, ḍoḷḷu kuṇita, the giant dolls of Kalladka, bear dancers and tiger troupes. The whole 10 km route is lit.',
  'Through Lālbāgh, Hampankaṭṭa and GHS Road the city lines the streets all night: organisers count over five lakh people.',
  'In the early morning the goddesses return to Kudroḷi and are immersed in the temple tank.'],
 [('z','The whole night?'),('b','The whole night. People say the city does not sleep on Vijayadaśamī.')],'A city awake all night <b>behind its Goddesses</b>.')
widows=reading('widows','WOMEN AT THE ALTAR','Widows as priests',
 S('Two women in white performing ārati before the Goddess Śāradā',g(170,190,1.3,devi(skin='#f6efe2',sari='#f4f1ea',items=('book','rosary')))+g(330,190,1.2,person('#f4f1ea'))+g(350,130,.9,arati())+g(420,190,1.2,person('#f4f1ea')),'#e3eaf3',200),
 ['<b>Kept out.</b> On the coast, as in much of India, widows were long kept away from auspicious rites and festivals.',
  '<b>Together.</b> More than two thousand widows performed a Caṇḍikā hōma together at Kudroḷi.',
  '<b>Ordained.</b> At the start of a Dasarā two widows, <b>Lakṣmī Śānti</b> and <b>Indirā Śānti</b>, were ordained as priests and performed pūjā to Śāradā. Indirā Śānti later performed the ārati to Śāradā on the last day of the festival.',
  '<b>More.</b> Later, two more widows, from Scheduled Caste and Scheduled Tribe communities, were appointed priests in the temple’s shrines.',
  '<b>The Guru’s teaching.</b> The temple trust has presented these steps as following Nārāyaṇa Guru’s idea of a God for everyone.'],
 [('z','Did everyone agree?'),('b','Not everyone; reforms never please all. But the temple has kept to it, and the city still comes in its lakhs.')],'The temple’s founding idea, <b>carried further</b>.')
car=reading('carstreet','CAR STREET ŚĀRADĀ','The city’s older Navarātri',
 S('A Śāradā image arriving in procession at a temple street lined with lamps',g(280,190,.9,float_cart(devi(skin='#f6efe2',sari='#f4f1ea',items=('book','rosary')),'#e0a800'))+lamps_row(40,200,6,30,.5)+lamps_row(370,200,6,30,.5)+g(120,150,.6,tulu_temple())+g(440,150,.6,tulu_temple()),'#e3eaf3',205),
 ['<b>Śāradā Mahotsava.</b> In the Car Street area, around the Śrī Veṅkaṭaramaṇa temple of the Gauḍa Sārasvata community, a <b>Śāradā Mahotsava</b> has been held for about a century. Its 100th year was marked with the image installed by the Kāśī Maṭha’s svāmī.',
  '<b>The arrival.</b> The Śāradā image is brought to the maṭha premises in procession before Navarātri (reported as coming from a Bunder beedi works, its long-time patron).',
  '<b>The close.</b> Like Kudroḷi’s, it ends in a colourful procession and immersion.',
  '<b>Many Śāradās.</b> Across the city many associations and households install their own Śāradā for Navarātri, a custom older than the 1991 Dasarā.',
  '<b>One festival, many hands.</b> Kudroḷi, Car Street and Maṅgaḷādevī together make the city’s Navarātri.'],
 [('z','So Kudroḷi didn’t invent it?'),('b','It gave it a name and a scale. The love of Śāradā was already in the city’s streets.')],'An older thread <b>in the same weave</b>.')
mangala=reading('mangaladevi','MAṄGAḶĀDEVĪ AND THE ŚAMĪ','The chariot to Mārnamikaṭṭe',
 S('A temple chariot drawn to a platform with a śamī tree',g(160,195,1.3,RATHA(0,0,1,'#c0392b'))+g(400,195,1.5,'<rect x="-60" y="-14" width="120" height="14" fill="#b08a62"/>'+tree('#2f6a3a'))+T(400,210,'Mārnamikaṭṭe · śamī',10),'#e3eaf3',215),
 ['<b>The Goddess of the city.</b> At Bōḷāra, the city’s namesake Goddess Maṅgaḷādevī keeps Navarātri with special worship through the nine nights.',
  '<b>Vijayadaśamī.</b> On the tenth day her festival image rides out in a chariot to <b>Mārnamikaṭṭe</b>, “the Navarātri platform”, where a śamī tree stands.',
  '<b>The śamī.</b> Worshipping the śamī on Vijayadaśamī recalls Arjuna, who took his weapons back from a śamī tree before winning the war. See '+L('/festivals/navaratri/','Vijayadaśamī')+'.',
  '<b>Two chariots a year.</b> Maṅgaḷādevī rides out at her own spring festival and at Vijayadaśamī for the whole city.',
  '<b>The oldest strand.</b> This chariot is among the oldest Navarātri customs of Maṅgaḷūru.'],
 [('z','Why a tree?'),('b','Because victory starts with taking up what you once laid aside. The śamī kept Arjuna’s bow; it keeps our resolve.')],'The city’s Goddess <b>goes out to the śamī</b>.')
mysuru=reading('two','TWO DASARĀS','Maṅgaḷūru and Mysuru',
 S('An elephant with a golden howdah on one side, tiger dancers on the other',g(150,190,1.1,elephant())+T(150,205,'Mysuru · royal')+g(400,195,1.2,tiger_dancer())+g(470,195,1.1,tiger_dancer(-1))+T(430,205,'Maṅgaḷūru · the people'),'#e3eaf3',212),
 ['<b>Mysuru.</b> A royal festival: the palace, the Woḍeyar king’s private durbār, Cāmuṇḍeśvarī carried on an elephant in the Jambū Savārī, and the state’s support. See '+L('/festivals/navaratri/mysuru-dasara/','Mysuru Dasarā')+'.',
  '<b>Maṅgaḷūru.</b> A temple festival carried by its city: no royal or government patronage; devotees and philanthropists bear the cost.',
  '<b>Different centres.</b> Mysuru’s procession carries one Goddess on an elephant; Maṅgaḷūru’s carries ten on floats, with tigers.',
  '<b>Similar crowds.</b> Organisers in Maṅgaḷūru claim crowds that bear comparison with Mysuru’s.',
  '<b>Both Karnataka.</b> One marks the old kingdom of the plateau, the other the merchant city of the coast. Between them they show two faces of the same festival.'],
 [('z','Which is better?'),('b','Wrong question. Go to one each year.')],'A king’s festival <b>and a people’s festival</b>.')
endp=end(i,['<b>Where.</b> Kudroḷi Gokarṇanātha, the temple Nārāyaṇa Guru consecrated for all.','<b>Since.</b> 1991, when the Navadurgās were first installed in the renewed temple.','<b>Who.</b> The nine Durgās, Ādiśakti, Gaṇeśa and Śāradā at the centre.','<b>How.</b> Ten days of worship and plays, tigers in the streets, an all-night procession.','<b>Also.</b> Car Street’s Śāradā and Maṅgaḷādevī’s chariot to the śamī.'],
 'Part 3 goes to Uḍupi: Kṛṣṇa’s chariots, his birthday and the Paryāya.','The common people’s Dasarā')
src=sources([('The festival:','Our '+L('/tulunadu/temples/kudroli-gokarnanatha/','Kudroḷi Gokarṇanātha')+' and '+L('/tulunadu/temples/mangaladevi/','Maṅgaḷādevī')+' guides; Wikipedia, “Mangaluru Dasara”; Deccan Herald (“People power pervades Dasara”, “Kudla Dasara”, procession reports); The Hans India (several reports on the “common man’s Dasara”); Udayavani/PTI on organisers’ figures and the absence of state patronage.'),('Reform:','Deccan Herald report naming Indirā Śānti at the ārati; our Kudroḷi guide for these steps.')],
 'crowd and tableau numbers are organisers’ estimates and vary by year (50 to over 100 tableaux); the order of the route and start times vary; the Car Street image’s patron is as reported; the tiger-mount explanation of pilivēṣa is popular belief.','Names of the nine Durgās as installed at Kudroḷi.')
finish(i,'PART 2 OF 9 · NAVADURGĀ · ŚĀRADĀ · TIGERS',covart('Śāradā on a lit float with tiger dancers and fireworks at night','<rect width="440" height="196" fill="#20243a"/>'+g(220,186,1.3,float_cart(devi(skin='#f6efe2',sari='#f4f1ea',items=('book','rosary')),'#c0392b'))+g(80,190,1.1,tiger_dancer())+g(360,190,1.1,tiger_dancer(-1))+g(90,50,.9,fireworks())+g(360,40,.8,fireworks())),'The people’s Dasarā at night',
 'The <b>Navadurgās and Śāradā</b> of Kudroḷi, how the festival began, the <b>tiger dancers</b>, the <b>all-night procession</b>, and the city’s older Navarātri strands.',
 'Maṅgaḷūru Dasarā explained and illustrated: Kudroḷi Gokarṇanātha and Nārāyaṇa Guru, the Navadurgās and Śāradā since 1991, pilivēṣa tiger dancers, the Vijayadaśamī procession, widow priests, Car Street Śāradā Mahotsava and Maṅgaḷādevī’s chariot.',
 [fw,gl,where,temple,nine,sharada,days,pili,proc,widows,car,mangala,mysuru,endp,src])
