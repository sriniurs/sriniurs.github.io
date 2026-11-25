from tn_common import *
i=5
def kmap():
    o=map_frame(sea=False)+'<path d="M0 60 q200 0 260 40 q20 12 40 0 q60 -40 260 -40" fill="none" stroke="#8fb8de" stroke-width="12"/><path d="M0 60 q200 0 260 80 q20 12 40 0 q60 -80 260 -80" fill="none" stroke="#8fb8de" stroke-width="12"/>'
    o+=g(280,122,.5,tulu_temple())+T(280,160,'the island shrine',10)+T(80,46,'Nandinī river',10,fill='#1d4f8a')
    o+=T(120,200,'Attūr',13,fill='#c0392b')+T(440,200,'Koḍettūr',13,fill='#1d4f8a')+T(280,36,'Kanakagiri (source) ← → the sea',9)
    return o
def flare(): return '<path d="M0 0 l26 -40" stroke="#8a6a3a" stroke-width="4"/>'+g(26,-40,1,flame(1.2,'#ff8c1a'))
fw=foreword(i,['The Goddess of Kaṭīl sits on a rock in the middle of a river. Once a year, at her spring festival, the villages on the two banks gather in her courtyard and pelt each other with burning palm fronds; when the fire is spent, they go home as friends. Through the rest of the year her troupes of actors travel the coast, playing her stories all night wherever a family has vowed a show to her.',
 'This guide is the festival year of <b>Kaṭīl Durgāparameśvarī</b>: the eight-day jātre from Mēṣa saṅkramaṇa, the utsavabali and the chariots, the <b>Tūtedhāra</b> fire play of Attūr and Koḍettūr, the flower month of Siṃha, Navarātri, the Nandinī’s day, and the <b>Kaṭīl Mela</b> with its vow shows.',
 'The temple and its legends are in '+L('/tulunadu/temples/katil-durgaparameshwari/','Kaṭīl Durgāparameśvarī')+'; her worship in a lamp in '+L('/tulunadu/culture/durga-namaskara/','Durgā Namaskāra')+'. Previous: '+L('/tulunadu/festivals/polali-jatre/','Poḷali Jātre')+'.'],
 [('z','Fire and theatre for one Goddess?'),('b','She loves both, the coast says. One is offered once a year in her courtyard; the other every night somewhere on the coast.')])
gl=glance([('Where','Kaṭīl, Dakṣiṇa Kannaḍa, near Maṅgaḷūru, on an island in the Nandinī'),('Goddess','Durgāparameśvarī, “Kaṭīlamma”; also Bhrāmarī, goddess of bees'),('Jātre','About eight days from the eve of Mēṣa saṅkramaṇa (mid-April)'),('Each day','Utsavabali; a silver-chariot procession; then the great rathōtsava'),('Fire play','Tūtedhāra (agni kēḷi): Attūr against Koḍettūr'),('Siṃha māsa','Her holy month (Aug–Sep), with special flower worship'),('Navarātri','Nine nights of the Goddess'),('Māgha pūrṇimā','The day the Nandinī first flowed'),('The Mela','Seven Yakṣagāna troupes touring Nov–May'),('Priests','The hereditary Āsraṇṇa family')],
 S('An island shrine in a river with fire torches flying above',g(280,170,1.1,tulu_temple())+'<path d="M0 180 h560 v20 h-560z" fill="#4aa3df"/>'+g(160,110,1,flare())+g(400,110,1,'<g transform="scale(-1 1)">'+flare()+'</g>'),'#e3eaf3',200),
 [('z','Is the island reachable?'),('b','By a footbridge from the bank. The river parts above the shrine and joins again below it.')],'A Goddess on a rock <b>who loves fire and theatre</b>.')
isl=reading('island','THE ISLAND','The middle of the land',svg(560,230,'Simplified map: the Nandinī parting round the island shrine, with Attūr and Koḍettūr on either bank',kmap()),
 ['<b>The river parts.</b> The Nandinī divides into two streams just above the shrine and joins again below it. The sanctum stands on the rock between, reached by a footbridge.',
  '<b>The name.</b> Kaṭi (“middle”) + iḷa (“land”): Kaṭīl, the land in the middle. Tradition says it marks the midpoint of the Nandinī’s course from Kanakagiri to the sea.',
  '<b>Two banks, two villages.</b> The banks belong to <b>Attūr</b> and <b>Koḍettūr</b>. Once a year they meet in the courtyard in the fire play.',
  '<b>The Goddess.</b> A self-manifest stone, shaped like a liṅga, dressed each day as the Mother.',
  '<b>Read more.</b> The full guide: '+L('/tulunadu/temples/katil-durgaparameshwari/','Kaṭīl Durgāparameśvarī')+'.'],
 [('z','Why does the fire play need two villages?'),('b','Because the river made two. The festival brings the two banks together, once a year, in her courtyard.')],'Two banks, <b>one Goddess between them</b>.')
nandini=story('nandini','STORY · NANDINĪ','The cow’s daughter who became a river',
 strip('Three panels: a sage before a heavenly cow in a drought; the cow refusing and the curse; the river flowing with the Goddess rising from a rock in the middle',
  [('<rect width="144" height="190" fill="#e9c98a"/>'+cracked(144,150)+g(44,150,.8,sage())+g(104,150,.7,'<ellipse rx="26" ry="14" cy="-30" fill="#f4f1ea"/><path d="M-18 -18 v18 M18 -18 v18" stroke-width="3"/><circle cx="28" cy="-38" r="9" fill="#f4f1ea"/>'),'#e9c98a'),
   ('<rect width="144" height="190" fill="#e9c98a"/>'+g(44,150,.8,sage())+g(104,140,.7,'<ellipse rx="26" ry="14" cy="-30" fill="#f4f1ea"/><circle cx="28" cy="-38" r="9" fill="#f4f1ea"/>')+'<path d="M60 70 l20 10 l-8 6 l20 10" fill="none" stroke="#e0501a" stroke-width="3"/>','#e9c98a'),
   ('<rect width="144" height="190" fill="#bcd3ea"/><rect y="130" width="144" height="60" fill="#4aa3df"/>'+g(72,150,.8,rock())+g(72,118,.55,devi(items=('trident','lotus'))),'#bcd3ea')],
  ['a drought','the curse','the river and the rock']),'From the legend of Kaṭīl, as in our temple guide.',
 ['A terrible drought struck the land. The sage <b>Jābāli</b> went to heaven to ask for <b>Nandinī</b>, daughter of Kāmadhenu, the wish-giving cow, so that sacrifices could bring rain.',
  'Nandinī refused to come down to an earth of sinners. Jābāli cursed her to go there as a river.',
  'She prayed to the Devī for release. The Goddess promised that Nandinī would flow as a holy river, and that she herself would rise in its middle.',
  'Nandinī burst out at Kanakagiri as a river and the rains returned.',
  'In the middle of her stream, the Goddess rose from a rock: Kaṭīlamma. Kaṭīl keeps the river’s birthday on <b>Māgha pūrṇimā</b>.'],
 [('z','And the bees?'),('b','That is her other story: Aruṇāsura, whose boon was proof against two- and four-footed creatures, killed by six-legged bees. It is told in our temple guide.')],'A curse that <b>became a blessing for the land</b>.')
jat=reading('jatre','THE JĀTRE','Eight days from Mēṣa saṅkramaṇa',
 svg(560,140,'Timeline of the Kaṭīl jātre','<rect width="560" height="140" fill="#fff3cf"/>'+tl_strip([('Eve','flag, Mēṣa eve'),('Daily','utsavabali'),('Nights','silver chariot'),('Peak','rathōtsava'),('Fire','Tūtedhāra'),('Close','bath, flag down')],560,140)),
 ['<b>Timing.</b> The annual jātre begins on the eve of <b>Mēṣa saṅkramaṇa</b>, the Tuḷu new year of Bisu in mid-April, and runs for about eight days.',
  '<b>Every day.</b> The festival image is taken out for <b>utsavabali</b> (see next page), with drums and lamps.',
  '<b>Chariots.</b> Kaṭīl has a silver chariot for the Goddess’s smaller processions and wooden chariots for the great <b>rathōtsava</b>.',
  '<b>Food.</b> The kitchen feeds thousands daily; at Mēṣa saṅkramaṇa the festival image is worshipped in the dining hall before heaps of rice and coconuts.',
  '<b>The fire.</b> Near the end comes the <b>Tūtedhāra</b>, the fire play, the festival’s best-known rite.'],
 [('z','The festival starts on the new year?'),('b','The Goddess opens the Tuḷu year with her own festival. The coast’s spring belongs to its goddesses.')],'The Tuḷu year opens <b>with her festival</b>.')
bali=reading('utsavabali','UTSAVABALI','Offerings to the guardians',
 S('A priest carrying the festival image on his head round the temple, another scattering rice offerings on stones',g(180,190,1.2,person('#f4f1ea'))+g(180,100,.7,'<path d="M-24 0 q24 -40 48 0z" fill="#e0a800"/>'+g(0,-10,.4,devi(items=())))+g(360,190,1.1,person('#f4f1ea'))+''.join(g(420+k*30,196,.8,'<rect x="-8" y="-10" width="16" height="10" fill="#8a8f9a"/><circle cy="-14" r="3" fill="#fff"/>') for k in range(4))+g(80,190,.8,drum()),'#fff3cf',200),
 ['<b>What it is.</b> <b>Utsavabali</b> (or śrībhūtabali) is the festival form of a daily temple rite: offerings of cooked rice are placed on the <b>balipīṭhas</b>, small stones round the temple that seat the deity’s attendants and guardians.',
  '<b>Carried round.</b> In coastal temples a priest carries the festival image on his head, often dancing to the drums, round the temple as the offerings are made.',
  '<b>Why.</b> Before the Goddess celebrates, every power in her household is fed: the guardians of the directions, her attendants, the bhūtas.',
  '<b>Daily in the jātre.</b> At Kaṭīl it is held every day of the festival.',
  '<b>A coastal style.</b> The image-dance on the priest’s head is a striking feature of Tuḷu and Kerala temple festivals. (General description.)'],
 [('z','Why feed the guardians first?'),('b','A good host feeds the household before the guests. The Goddess’s court eats first.')],'Every power in her house <b>is fed first</b>.')
fire=story('tutedhara','TŪTEDHĀRA','The fire play of Attūr and Koḍettūr',
 strip('Three panels: palm-frond bundles being lit; bare-chested men of two villages throwing burning fronds across the courtyard; the two groups embracing afterwards',
  [('<rect width="144" height="190" fill="#20243a"/>'+g(72,160,1,'<path d="M-30 0 l60 0" stroke="#d8b878" stroke-width="10"/>')+g(72,140,1.4,flame(1,'#ff8c1a')),'#20243a'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(30,170,.8,person('#c98a5a'))+g(114,170,.8,person('#c98a5a'))+g(72,80,1,flame(1,'#ff8c1a'))+'<path d="M40 100 q30 -40 60 -10" fill="none" stroke="#ffd60a" stroke-dasharray="4 4" stroke-width="2"/>','#20243a'),
   ('<rect width="144" height="190" fill="#3a2a50"/>'+g(56,170,.8,person('#f4f1ea'))+g(88,170,.8,person('#f4f1ea'))+'<path d="M64 120 h16" stroke-width="4"/>','#3a2a50')],
  ['the fronds lit','fire across the courtyard','friends again']),'The Tūtedhāra (agni kēḷi) of the Kaṭīl jātre, as described in our guide and in press reports.',
 ['After the Goddess’s abhiṣeka and the special sevās of the day, men of <b>Attūr</b> and <b>Koḍettūr</b> gather in the temple courtyard, bare-chested in white dhotis.',
  'Bundles of dried palm fronds, <b>tūte</b>, are lit.',
  'The two sides throw the burning bundles at each other across the courtyard, in front of the sanctum. The bundles are thrown, not held.',
  'The players take the sparks on their bodies as her blessing. Participants say injuries are rare, and are treated not with medicine but with the temple’s kuṅkuma.',
  'When the fire is spent, the two villages leave as friends. The rite is believed to cleanse sins and please the Goddess, who delights in an offering of fire.'],
 [('z','Throwing fire at your neighbours sounds dangerous!'),('b','It is a rite, not a riot. Generations have played it the same way, and the villagers say the Mother herself keeps the burns away.')],'Fire given to the Goddess <b>and to each other</b>.')
fmean=reading('fire-meaning','WHY FIRE','Readings of the Tūtedhāra',
 S('A goddess seated in a ring of flame, devotees bowing',g(280,190,1.6,devi(items=('trident','sword'),fierce=True))+''.join(g(280+150*__import__('math').cos(__import__('math').radians(a)),120+70*__import__('math').sin(__import__('math').radians(a)),.8,flame(1,'#ff8c1a')) for a in range(180,361,30))+g(80,190,1,namaste('#8e1f17'))+g(480,190,1,namaste('#1d4f8a')),'#20243a',200),
 ['<b>Fire for a fiery Goddess.</b> Durgā is a fierce, protecting Goddess; many say she “delights” in fire. The play is an offering suited to her.',
  '<b>Purification.</b> Participants describe the fire as cleansing: sins and ill will burn away. (Belief of participants.)',
  '<b>Rivalry made holy.</b> Two neighbouring villages could easily have been rivals. The rite lets them fight once a year, under her eyes, by her rules, and part as friends. (Interpretation.)',
  '<b>Courage.</b> Taking sparks on the body without flinching is a test of nerve and faith, like walking on coals in other festivals.',
  '<b>Kin across the coast.</b> Fire rites at temple festivals are found elsewhere on the coast too; Kaṭīl’s is the best known.'],
 [('z','Could it ever be banned?'),('b','It has been watched and filmed for years and goes on. The villages guard their right to it closely.')],'A rivalry <b>burnt away each year</b>.')
simha=reading('simha','SIṂHA MĀSA AND NAVARĀTRI','The Goddess’s holy months',
 S('Heaps of flowers being offered at the shrine; then a lit temple at night with the nine nights marked',g(140,190,1.1,tulu_temple())+''.join(g(80+k*24,196,.7,lotus(['#e05050','#ff8c1a','#e0a800'][k%3],'#8e1f17')) for k in range(6))+'<rect x="300" y="0" width="260" height="200" fill="#20243a"/>'+g(430,190,1,tulu_temple('#a0522d','#5a2a10'))+''.join(f'<circle cx="{320+k*26}" cy="40" r="8" fill="#ffd60a"/>' for k in range(9)),'#fff3cf',200),
 ['<b>Siṃha māsa.</b> The solar month of Siṃha (August–September) is the Goddess’s holy month at Kaṭīl. From <b>Siṃha saṅkramaṇa</b> special flower worship is offered.',
  '<b>Navarātri.</b> The nine nights of the Goddess draw huge crowds; the temple stays open late. See '+L('/festivals/navaratri/','Navarātri')+'.',
  '<b>Māgha pūrṇimā.</b> The day the Nandinī first flowed: the river’s own festival.',
  '<b>Every Friday and Tuesday.</b> The Goddess’s weekly days bring their own crowds.',
  '<b>Durgā Namaskāra.</b> Families of the coast often vow the lamp worship of Durgā to her. See '+L('/tulunadu/culture/durga-namaskara/','Durgā Namaskāra')+'.'],
 [('z','Why a flower month in the monsoon?'),('b','Because the rains make the coast bloom. She is offered what the season gives.')],'Flowers in the rains, <b>lamps at Navarātri</b>.')
mela=reading('mela','THE KAṬĪL MELA','The Goddess’s own theatre',
 S('A Yakṣagāna troupe performing at night on an open-air stage with a crowd watching','<rect width="560" height="200" fill="#20243a"/>'+g(280,150,1,'<rect x="-140" y="0" width="280" height="14" fill="#a0522d"/>')+g(220,150,1.2,person('#c0392b'))+'<path d="M200 66 l20 -30 l20 30z" fill="#e0a800"/>'+g(330,150,1.2,person('#1d4f8a'))+'<path d="M310 66 l20 -30 l20 30z" fill="#e0a800"/>'+g(160,150,.8,drum())+g(280,200,1,crowd(12,480,0,.42)),'#20243a',200),
 ['<b>The troupe.</b> The <b>Kaṭīl Śrī Durgāparameśvarī Prasādita Daśāvatāra Yakṣagāna Maṇḍaḷi</b>, the Kaṭīl Mela, was founded in the mid-19th century and plays in the Teṅkutiṭṭu style of the south.',
  '<b>Seven troupes.</b> One troupe for a century; more from the 1980s as demand grew. Today there are seven, more than any other Yakṣagāna organisation. Each troupe plays about 180 shows a year.',
  '<b>The tour.</b> The troupes set out after the rains, around late November, and return at the end of the season before Pattanāje. On the first and last days the shows run overnight before the Goddess.',
  '<b>Her favourite play.</b> The most requested story is <b>Śrī Devī Mahātme</b>, the Goddess’s own glory, from the '+L('/devi/devi-mahatmya/','Devī Māhātmya')+'.',
  '<b>Children too.</b> The <b>Śrī Durgā Makkaḷa Mela</b> trains children in every part of Yakṣagāna.'],
 [('z','Why does a temple run a theatre company?'),('b','Because the coast offers plays the way others offer flowers. Kaṭīl simply needed more flowers than anyone.')],'The coast offers plays <b>as others offer flowers</b>.')
harake=reading('harake','THE VOW SHOW','Harake Yakṣagāna',
 S('A family seated before a stage in their village, the Goddess in a small shrine beside the stage',g(160,190,1,tulu_temple())+g(160,130,.5,devi(items=('trident',)))+g(380,150,1,'<rect x="-100" y="0" width="200" height="12" fill="#a0522d"/>'+g(0,0,1.1,person('#c0392b'))+'<path d="M-20 -84 l20 -30 l20 30z" fill="#e0a800"/>')+g(380,196,1,crowd(6,180,0,.45)),'#fff3cf',205),
 ['<b>The vow.</b> When a family’s prayer to Kaṭīlamma is answered, it vows a night of Yakṣagāna to her: a <b>harake</b> (also called bayalāṭa sevā).',
  '<b>Where.</b> The Mela comes to the family’s own village or town and plays without tickets for anyone who comes.',
  '<b>She comes too.</b> It is believed the Goddess herself comes to the place where her Mela plays.',
  '<b>Booked for years.</b> So many families vow shows that bookings run years ahead; in one report the six troupes were booked several seasons in advance.',
  '<b>All night or shorter.</b> Shows were traditionally all-night; noise rules led to shorter formats for some years, and the Mela has since returned to all-night shows in season. (Practice varies.)'],
 [('z','A thank-you gift of a whole play?'),('b','A whole night of her stories, for the whole village. It is the coast’s grandest way of saying thank you.')],'A thank-you <b>the whole village shares</b>.')
endp=end(i,['<b>Island.</b> Kaṭīlamma rose from a rock in the Nandinī, the cow’s daughter turned river.','<b>Jātre.</b> Eight days from Mēṣa saṅkramaṇa: utsavabali, silver chariot, rathōtsava.','<b>Fire.</b> Tūtedhāra: Attūr and Koḍettūr throw burning fronds, then part as friends.','<b>Year.</b> Siṃha māsa flowers, Navarātri, Māgha pūrṇimā.','<b>Mela.</b> Seven troupes playing vow shows across the coast.'],
 'Part 7 goes north to Kōṭeśvara for the Koḍi Habba and its sugarcane.','The island Goddess through the year')
src=sources([('Kaṭīl:','Our '+L('/tulunadu/temples/katil-durgaparameshwari/','Kaṭīl Durgāparameśvarī')+' guide; ANI reports via LatestLY, NewKerala and Public TV on the Tūtedhāra; NewsKarnataka; The Asian Age; Deccan Chronicle (Mela tour; seventh troupe); Udayavani (Mela tour; time format); Deccan Herald (bookings); HinduTone (jātre structure); myOksha (dining hall worship at Mēṣa saṅkramaṇa).')],
 'the general description of utsavabali applies to coastal temples broadly; the Mela’s show format has changed over the years; the reading of the fire play as reconciling the villages is ours.','Festival structure as in our temple guide.')
finish(i,'PART 6 OF 9 · JĀTRE · FIRE PLAY · THE MELA',covart('Bare-chested men throwing burning fronds before an island temple at night','<rect width="440" height="196" fill="#20243a"/>'+g(220,180,1,tulu_temple('#a0522d','#5a2a10'))+g(70,190,1.1,person('#c98a5a'))+g(370,190,1.1,person('#c98a5a'))+g(140,90,1.2,flame(1,'#ff8c1a'))+g(300,70,1,flame(1,'#ff8c1a'))+'<path d="M90 120 q60 -70 120 -40" fill="none" stroke="#ffd60a" stroke-dasharray="4 4" stroke-width="2"/>'),'The fire play of Kaṭīl',
 'Kaṭīl’s year: the <b>jātre</b> from Mēṣa saṅkramaṇa, the <b>Tūtedhāra</b> fire play, the holy months, and the <b>Kaṭīl Mela</b> with its vow shows.',
 'Kaṭīl festivals explained and illustrated: the island Goddess Durgāparameśvarī, Nandinī’s story, the eight-day jātre from Mēṣa saṅkramaṇa, utsavabali, the Tūtedhāra fire play of Attūr and Koḍettūr, Siṃha māsa, Navarātri, and the Kaṭīl Yakṣagāna Mela and harake shows.',
 [fw,gl,isl,nandini,jat,bali,fire,fmean,simha,mela,harake,endp,src])
