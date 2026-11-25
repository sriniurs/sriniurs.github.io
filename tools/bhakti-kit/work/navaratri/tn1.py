from tn_common import *
import math
i=0
M=[('Paggu','Apr–May'),('Beṣa','May–Jun'),('Kārtel','Jun–Jul'),('Āṭi','Jul–Aug'),('Sōṇa','Aug–Sep'),('Nirnāla','Sep–Oct'),('Bontel','Oct–Nov'),('Jārde','Nov–Dec'),('Perārde','Dec–Jan'),('Ponni','Jan–Feb'),('Māyi','Feb–Mar'),('Suggi','Mar–Apr')]
def wheel(cx=280,cy=118,r=92):
    o=g(cx,cy,1,sun(20))
    for k,(m,d) in enumerate(M):
        a=math.radians(-90+k*30); x,y=cx+r*math.cos(a),cy+r*math.sin(a)
        col=['#4aa3df','#4aa3df','#4aa3df','#4aa3df','#2a9d6f','#2a9d6f','#e0a800','#e0a800','#e0a800','#c0392b','#c0392b','#c0392b'][k]
        o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="22" fill="{col}"/>'+txt(x,y+1,m,10,font=NS,weight='700',fill='#fff')+txt(x,y+12,d,7,font=NS,fill='#fff')
    return o+T(470,228,'the twelve solar months',9)
fw=foreword(i,['On the Tuḷu coast the year does not follow the moon. It follows the sun, the rain and the rice. Its twelve months have their own names, <b>Paggu</b> to <b>Suggi</b>, and each carries its own days: the new year of Bisu, the bitter bark of Āṭi, the first sheaves of Koral, the lamps for King Bali, the three days when the Earth rests.',
 'This guide walks the year month by month: how the months are counted, the farming cycle behind them, and every observance that shapes life in Uḍupi and Dakṣiṇa Kannaḍa, from <b>Bisu</b> in April to the harvest songs of <b>Suggi</b>.',
 'It opens our series on the '+L('/tulunadu/festivals/','festivals of Tulu Nadu')+'. The coast’s guardians are in '+L('/tulunadu/daiva/','Daiva and Nāga traditions')+'; its words in '+L('/tulunadu/start-here/','Start Here')+'.'],
 [('z','Why does a region need its own calendar?'),('b','Because the rain here is not like the rain anywhere else. A calendar built round the monsoon tells you when to plough, when to rest and when to feast.')])
gl=glance([('What','The traditional solar calendar of Tuḷunāḍu (Uḍupi, Dakṣiṇa Kannaḍa, Kāsaragoḍu)'),('Months','12: Paggu, Beṣa, Kārtel, Āṭi, Sōṇa, Nirnāla, Bontel, Jārde, Perārde, Ponni (Puyintel), Māyi, Suggi'),('New year','Bisu, the first day of Paggu, mid-April'),('Counting','By the sun: a month begins when the sun enters a new sign'),('First and last day','Tiṅgoḍe (or siṅgoḍe) and saṅkrānti'),('The lean month','Āṭi, the heaviest rain; no weddings'),('Season closes','Pattanāje, 10th of Beṣa (late May)'),('Season opens','Jārde, around Dīpāvali'),('Farming','Built round the paddy: sowing, harvest, rest'),('Shared with','Kerala’s Malayalam months and the Tamil solar months')],
 S('A wheel of the twelve Tuḷu months around the sun',wheel(),'#fff3cf',235),
 [('z','Paggu is April?'),('b','Mid-April to mid-May. Every Tuḷu month straddles two English ones, because it starts when the sun changes sign, around the 14th to 17th.')],'Twelve months <b>set by the sun and the rain</b>.')
sun_=reading('sun','SUN, NOT MOON','How the Tuḷu months are counted',
 S('The sun moving from one zodiac sign to the next, marking the first day of a new month',g(110,110,1.4,sun(24))+'<path d="M160 110 q120 -80 240 0" fill="none" stroke-dasharray="6 5" stroke-width="2"/>'+g(400,110,1.4,sun(24))+T(110,170,'saṅkrānti · last day')+T(400,170,'tiṅgoḍe · first day')+T(280,40,'the sun enters a new sign'),'#dfe9f6',190),
 ['<b>A solar calendar.</b> Most of India counts festivals by the moon. Tuḷunāḍu counts its months by the sun (the <i>saura</i> reckoning): a month starts when the sun passes into a new sign of the zodiac.',
  '<b>First and last days.</b> The first day of a Tuḷu month is <b>tiṅgoḍe</b> (also siṅgoḍe); the last is <b>saṅkrānti</b>, the day of the sun’s crossing. Each month has 30 or 31 days.',
  '<b>Matching months.</b> Paggu is the solar month Meṣa (Aries), so Bisu falls on the same day as Viṣu in Kerala and the Tamil new year. Āṭi is Karkāṭaka, Ponni is Makara, and so on round the year.',
  '<b>The moon still matters.</b> Inside the solar frame the new moon and the full moon mark the great days: Āṭi amāse, the Dīpāvali new moon, the full moons of the temples. Lunar festivals like Gaṇeśa Cauti and Navarātri also find their place.',
  '<b>Names.</b> Sources spell the months in many ways: Beṣa or Beśya, Bontel or Bontyolu, Ponni or Puyintel. They are the same months.'],
 [('z','So a Tuḷu date is fixed against the English calendar?'),('b','Almost. Bisu is always 14 or 15 April, Pattanāje 24 or 25 May. The sun keeps better appointments than the moon.')],'A month begins <b>when the sun changes house</b>.')
seasons=reading('seasons','THE YEAR OF THE RICE','Rain, sowing, harvest and rest',
 S('Three scenes: monsoon rain over flooded fields, green paddy, and golden harvest sheaves',
  '<rect x="0" y="0" width="186" height="190" fill="#bcd3ea"/>'+''.join(f'<path d="M{x} {y} l-6 14" stroke="#1d4f8a" stroke-width="2"/>' for x in range(20,186,24) for y in (30,70))+'<rect y="140" width="186" height="50" fill="#4aa3df"/>'+T(93,180,'rain · sowing',11,fill='#fff')
  +'<rect x="187" width="186" height="190" fill="#d8efc8"/>'+''.join(g(200+k*22,150,.7,'<path d="M0 0 q-6 -20 0 -40 M0 0 q8 -18 4 -36" fill="none" stroke="#2f7a3a" stroke-width="3"/>') for k in range(8))+T(280,180,'growing')
  +'<rect x="374" width="186" height="190" fill="#f3e3a8"/>'+''.join(g(394+k*24,150,.8,'<path d="M0 0 q-4 -30 6 -48 M0 0 q4 -26 -6 -44" fill="none" stroke="#b8860b" stroke-width="4"/>') for k in range(7))+T(467,180,'harvest · rest'),'#fff',190),
 ['<b>The calendar is a farmer’s calendar.</b> Its days tell people when to plough, sow, transplant, harvest and rest. Many of its observances, especially those for the daivas, follow the paddy year.',
  '<b>Three crops.</b> The farming year is divided into three paddy seasons, <b>Enelu</b>, <b>Suggi</b> and <b>Kolake</b>: Enelu begins with the monsoon at the end of May; Suggi is the crop grown after Dīpāvali and harvested by March–April.',
  '<b>Three weathers.</b> The year is also spoken of as <b>aregāla</b> (summer), <b>maryāla</b> (rain) and <b>chaligāla</b> (cold).',
  '<b>Work and festival take turns.</b> The great outdoor season of the coast, temple jātres, bhūta kōlas, Kambaḷa races and Yakṣagāna, runs from Jārde (around Dīpāvali) to Pattanāje in late May. Then the monsoon arrives and the coast turns to its fields.',
  '<b>Māyi.</b> The month of Māyi marks the end of the agricultural year: the harvest is in, the fields lie fallow, and the coast has time for its gods.'],
 [('z','So festivals happen when there is no farm work?'),('b','That is the rhythm. The rain months are for the fields; the dry months for the gods, the races and the plays.')],'Rain for the fields, <b>dry months for the gods</b>.')
bisu=reading('bisu','PAGGU · BISU','The new year and the first sight',
 S('A Bisu kani arrangement: a lit standing lamp, a plate of rice, fruits, vegetables and a coconut on banana leaves, with a family looking at it',
  g(280,170,1,'<path d="M-150 0 h300 l-20 14 h-260z" fill="#3a9a4a"/>')+g(200,166,1.4,plate()+g(0,-6,.8,banana()))+g(280,166,1.3,coconut())+g(350,166,1.3,'<ellipse rx="16" ry="12" fill="#f4a020"/><ellipse cx="18" rx="12" ry="9" fill="#e0a800"/>')+g(140,168,.9,lamp())+g(420,168,.9,lamp())+g(60,180,1,namaste('#8e1f17'))+g(500,180,1,namaste('#1d4f8a')),'#fff3cf',195),
 ['<b>Bisu Parba.</b> Bisu, the first day of Paggu, is the new year and a harvest festival of Tuḷunāḍu, on 14 or 15 April. It is the same solar new year as Viṣu in Kerala and Sauramāna Yugādi.',
  '<b>Bisu kaṇi.</b> Early in the morning the house prepares the <b>kaṇi</b>, the “first sight”: lamps lit at both ends, banana leaves laid out, rice, fruits, vegetables, the new harvest arranged before the gods. The household sees it first thing in the new year.',
  '<b>Elders and juniors.</b> The family prays together before the kaṇi; the young bow to the elders and receive their blessings, and quarrels are meant to be mended.',
  '<b>The first seed.</b> In farming families new paddy seed is set aside in the morning, and in the evening a token sowing is made at the edge of the field: the agricultural year begins.',
  '<b>A day for beginnings.</b> Bisu is held lucky for starting anything new.'],
 [('z','What is the point of the first sight?'),('b','The belief is simple: what you see first in the year shapes the year. So you make sure it is a lamp, rice and fruit.')],'The year begins <b>with a lamp and the harvest</b>.')
patt=reading('pattanaje','BEṢA · PATTANĀJE','The day the festival season ends',
 S('A Yakṣagāna actor taking off his crown, rain clouds gathering over a temple',
  g(150,180,1.2,person('#c0392b'))+'<path d="M128 70 l22 -28 l22 28z" fill="#e0a800"/>'+'<path d="M300 60 q20 -30 50 -10 q30 -20 50 10 q30 0 20 24 h-140 q-10 -24 20 -24z" fill="#8a96a8"/>'+''.join(f'<path d="M{x} 96 l-5 12" stroke="#1d4f8a" stroke-width="2"/>' for x in range(320,440,16))+g(380,190,.7,tulu_temple()),'#e8eef5',200),
 ['<b>The tenth of Beṣa.</b> Pattanāje (“the tenth day”) falls on the tenth day of Beṣa, usually 24 or 25 May. It is a fixed deadline for celebration in Tuḷunāḍu.',
  '<b>Everything stops.</b> Annual chariot festivals, daiva nēmas, folk ritual dances, Kambaḷa and Yakṣagāna must conclude by this day. They resume in Jārde, around Dīpāvali. For the next six months only regular worship goes on in the temples.',
  '<b>The players rest.</b> The touring Yakṣagāna troupes end their season and the artistes rest through the rains. (Some troupes now also play in the monsoon.)',
  '<b>Offerings outside.</b> On Pattanāje many rites are held outside the house, at the daivasthāna, Guḷiga’s or Bhairava’s platform, with rice and food served on plantain leaves for the guardians.',
  '<b>Ten drops.</b> A Tuḷu saying holds that at least ten drops of rain should fall on Pattanāje; rain that day promises a good crop. Ploughing begins.'],
 [('z','Why stop so early, before the rain?'),('b','Because when the monsoon comes to this coast it comes all at once. Better to close the season on a fixed day than be washed out mid-festival.')],'The season closes <b>as the rain arrives</b>.')
aati=reading('aati','ĀṬI · THE LEAN MONTH','Rain, hunger and waiting',
 S('Heavy rain over a flooded village, a family sitting under the eaves',
  '<rect width="560" height="190" fill="#8a96a8"/>'+''.join(f'<path d="M{x} {y} l-8 18" stroke="#dfe9f6" stroke-width="2"/>' for x in range(10,560,20) for y in (20,70,120))+'<rect y="160" width="560" height="30" fill="#4aa3df"/>'+g(280,165,.9,tulu_temple('#a0522d','#5a2a10'))+g(200,165,.8,person('#8e1f17',seat=True))+g(240,165,.8,person('#1d4f8a',seat=True)),'#8a96a8',190),
 ['<b>Karkāṭaka.</b> Āṭi is the Tuḷu name for the solar month of Karkāṭaka, mid-July to mid-August, the heart of the monsoon.',
  '<b>A hard month.</b> The heaviest rain of the year falls, fields are flooded, the stored grain runs low and the new crop is not yet in. In the old farming economy this was the hungry month.',
  '<b>Nothing new begins.</b> For many families Āṭi is an inauspicious month: no weddings, no house-warmings, no temple festivals, and traditionally no buying of property, vehicles or gold.',
  '<b>Food for the rain.</b> Āṭi has its own dishes, made from what grows in the rains: leaves, shoots and tubers, and simple gruels. Many families keep a special Āṭi meal.',
  '<b>Its days.</b> Āṭi amāse with its bitter bark, the house-visits of Āṭi Kaḷeñja, and Nāgara Pañcamī for the serpents all fall in this month.'],
 [('z','A whole month without celebrations?'),('b','Without celebrations, not without rites. Āṭi is the month of protecting the house: medicine, guardians and serpents.')],'The month of <b>rain and protection</b>.')
amase=reading('amase','ĀṬI AMĀSE','The bitter bark of the pāle tree',
 S('Before dawn, a man peeling bark from a tall pāle tree with a stone, a cup of dark decoction beside him',
  '<rect width="560" height="190" fill="#2a3550"/>'+g(170,190,1.6,tree('#2f6a3a'))+g(250,186,1,person('#8e1f17'))+g(236,140,.5,'<ellipse rx="10" ry="7" fill="#9a9a9a"/>')+g(380,170,1,'<path d="M-14 0 h28 l-4 -24 h-20z" fill="#e9d6c0"/><ellipse cy="-24" rx="10" ry="3" fill="#5a3a1a"/>')+T(380,186,'pāleda kaṣāya',11,fill='#fff')+g(500,40,1,moon()),'#2a3550',190),
 ['<b>The new moon of Āṭi.</b> Āṭi amāse (also Deevige Karkāṭaka Amāvāsyā or Bhīmana Amāvāsyā) is the new moon of the month. On this day the coast drinks a bitter decoction.',
  '<b>The tree.</b> The <b>pāle</b> tree (Kannaḍa hāle, Sanskrit saptaparṇī, <i>Alstonia scholaris</i>) gives the bark. Before daybreak people go to it and peel off pieces of bark with a stone; no knife or sickle is used.',
  '<b>The decoction.</b> The bark is crushed and its juice mixed into a drink, <b>pāleda kaṣāya</b>, taken on an empty stomach. It is very bitter. The belief is that it protects against illness until the next Āṭi.',
  '<b>Afterwards.</b> Families follow it with <b>meṭṭeda gañji</b>, a gruel of rice, fenugreek and jaggery, and other simple foods.',
  '<b>Āṭi agel.</b> On the evening of the new moon many families make an offering for the ancestors, served on leaves.'],
 [('z','Why a stone and not a knife?'),('b','Custom says iron must not touch the tree. Whatever the reason, it slows you down: you take only what you can peel by hand.')],'Bitter at dawn, <b>well for a year</b>.')
kalenja=story('kalenja','ĀṬI KAḶEÑJA','The leaf-dressed visitor who drives away trouble',
 strip('Three panels: a man in a leaf costume and tall headgear arriving at a house in the rain; dancing to a drum before the family; receiving rice and coconut before moving on',
  [('<rect width="144" height="190" fill="#8a96a8"/>'+g(90,170,.6,tulu_temple())+g(40,170,1,person('#2f7a3a'))+'<path d="M26 92 l14 -34 l14 34z" fill="#e05050"/>','#8a96a8'),
   ('<rect width="144" height="190" fill="#e9f2e1"/>'+g(50,170,1,person('#2f7a3a'))+'<path d="M36 92 l14 -34 l14 34z" fill="#e05050"/>'+g(108,150,.8,drum('#c98a5a')),'#e9f2e1'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(50,170,1,person('#2f7a3a'))+'<path d="M36 92 l14 -34 l14 34z" fill="#e05050"/>'+g(104,160,1.1,plate()+g(0,-4,.6,coconut())),'#fff3cf')],
  ['he comes','he dances','he takes the bad away']),
 'A folk observance of the Āṭi month, performed by men of the Nalike community.',
 ['In the villages of Tuḷunāḍu, during Āṭi, a man of the <b>Nalike</b> community dresses as <b>Kaḷeñja</b> and goes from house to house.',
  'His costume is made of leaves and flowers; his tall headgear is made from the stems of <b>kepula</b> (ixora), and his face is painted.',
  'A companion beats a <b>tembare</b> drum and sings the <b>pāḍdana</b>, the oral Tuḷu song, as Kaḷeñja dances in the yard.',
  'The household gives him offerings in kind: traditionally rice, coconut and other things found in every Tuḷu home; today often money.',
  'He moves on to the next house, taking away, it is believed, the illness and misfortune of the rainy month. The custom is fading as fewer young people take it up.'],
 [('z','Who is Kaḷeñja?'),('b','A protecting spirit called down to the earth in the hardest month. People say he gives families courage that the worst of the rain is behind them.')],'A visitor of leaves <b>who carries off the rainy month</b>.')
naga=reading('naga','NĀGARA PAÑCAMĪ','Milk for the serpents of the grove',
 S('A serpent stone under a tree in a sacred grove, with a pot of milk, turmeric and flowers',g(280,180,2,tree('#2f6a3a'))+g(280,180,1.4,'<rect x="-30" y="-50" width="60" height="50" rx="10" fill="#8a8f9a"/><path d="M-10 -10 q-10 -20 0 -34 q10 -10 6 6 q-8 12 4 24" fill="none" stroke="#3a3a3a" stroke-width="4"/>')+g(200,180,1,'<path d="M-12 0 h24 l-4 -20 h-16z" fill="#c98a5a"/><path d="M-8 -22 q8 -6 16 0" fill="#fff8ec"/>')+g(360,180,1.2,lotus('#e0a800','#b8860b')),'#e9f2e1',195),
 ['<b>The serpents’ day.</b> Nāgara Pañcamī, the fifth day of the bright fortnight of Śrāvaṇa, falls in the rains of Āṭi or Sōṇa. On the coast it is one of the year’s great family days.',
  '<b>At the nāgabana.</b> Families go to their ancestral <b>nāgabana</b>, the sacred serpent grove, where stone images of the nāga stand under the trees.',
  '<b>The offering.</b> The stones are bathed with milk and tender coconut water, smeared with turmeric and decorated with flowers, especially the fragrant screw-pine (kēdige) of the season.',
  '<b>Why serpents.</b> On the coast the nāga is the guardian of the land, the water and the family line. Neglect of a grove is held to bring disease and trouble on a family.',
  '<b>Read more.</b> See '+L('/festivals/naga-panchami/','Nāga Pañcamī')+' and '+L('/tulunadu/daiva/nagamandala/','Nāgamaṇḍala')+'.'],
 [('z','Why the rainy season?'),('b','The rains flood the snakes out of their holes and into human space. It is the season people meet them most, and pray to them most.')],'The guardians of the land <b>bathed in milk</b>.')
koral=reading('koral','SŌṆA · KORAL PARBA','Bringing home the first sheaves',
 S('A farmer carrying a bundle of new paddy ears tied with leaves to the door of his house',
  '<rect y="140" width="560" height="50" fill="#d8efc8"/>'+''.join(g(20+k*20,150,.6,'<path d="M0 0 q-4 -26 6 -40" fill="none" stroke="#b8860b" stroke-width="3"/>') for k in range(8))+g(240,170,1.2,person('#8e1f17'))+g(262,110,1,'<path d="M0 0 q-10 -20 -4 -34 M0 0 q10 -20 6 -34 M0 0 v-36" fill="none" stroke="#b8860b" stroke-width="4"/><path d="M-12 -20 q-10 -6 -16 4 M12 -20 q10 -6 16 4" fill="#3a9a4a"/>')+g(420,170,1,tulu_temple())+T(420,186,'tied to the door and tools',10),'#fff3cf',195),
 ['<b>Koral.</b> A bundle of newly harvested paddy ears. <b>Koral Parba</b>, also called Tene Habba or Kadiru Kaṭṭuvudu (“tying the ears”), is the festival of the first harvest.',
  '<b>To the temple first.</b> In many villages the new ears are first offered to the deity at the temple or daivasthāna, then carried home in a new basket.',
  '<b>Tied everywhere.</b> The ears are tied with fresh bamboo, mango and jackfruit leaves and hung on the doorway, pillars, the granary and the farm tools, and today even on vehicles.',
  '<b>The new rice meal.</b> A feast is cooked from the new rice, with vegetable dishes and pāyasa. Before eating, the family offers it to the gods.',
  '<b>Its date.</b> It is held in Sōṇa or the following month, often around Gaṇeśa Cauti or Kanyā saṅkramaṇa; the day differs by village. Mangaluru’s Christians mark the same harvest at Monti Fest.'],
 [('z','Why tie rice to a scooter?'),('b','Because the family’s living now runs on it, just as it ran on the plough. The custom moves with the times.')],'The first rice goes <b>to the gods and the doorway</b>.')
nirnala=reading('nirnala','NIRNĀLA · CAUTI AND MĀRNEMI','Gaṇeśa, the Goddess and the tiger dancers',
 S('Painted pilivēṣa tiger dancers leaping to drums',g(140,180,1.2,tiger_dancer(1))+g(280,180,1.3,tiger_dancer(-1))+g(420,180,1.2,tiger_dancer(1))+g(500,170,.8,drum()),'#fde9c8',195),
 ['<b>Cauti.</b> Gaṇeśa Caturthī, called <b>Cauti</b> on the coast, comes at the start of the autumn festival run. See '+L('/ganesha/festivals/ganesha-chaturthi/','Gaṇeśa Caturthī')+'.',
  '<b>Kāvēri saṅkramaṇa.</b> The sun’s entry into Tulā (Libra), honoured as the day the river Kāverī rises; marked on the coast and above all in Koḍagu.',
  '<b>Mārnemi.</b> Navarātri on the coast is <b>Mārnemi</b>. Temples of the Goddess fill with crowds, and Maṅgaḷūru holds its Dasarā at Kudroḷi (Part 2 of this series).',
  '<b>Pilivēṣa.</b> At Aṣṭami and Mārnemi troupes of men painted head to foot as tigers, <b>pilivēṣa</b> (“tiger costume”), dance through the streets and from house to house to the beat of drums. Many say they honour the Goddess whose mount is the tiger.',
  '<b>Aṣṭami.</b> Kṛṣṇa’s birth, in Sōṇa, is celebrated grandly in Uḍupi (Part 3).'],
 [('z','Is the tiger paint uncomfortable?'),('b','Very, and it lasts for days. Dancers take it as a vow. The suffering is part of the offering.')],'Tigers in the street, <b>the Goddess in the temple</b>.')
tudar=reading('tudar','BONTEL · TUḌAR PARBA','Lamps for King Bali',
 S('A tall bamboo pole decorated with lamps in a harvested field at night, people with lanterns calling out',
  '<rect width="560" height="195" fill="#20243a"/><rect y="160" width="560" height="35" fill="#5a4a2a"/>'+g(280,165,1,'<path d="M0 0 v-120" stroke="#c9a36b" stroke-width="6"/>'+''.join(f'<path d="M-24 {-k*24} h48" stroke="#c9a36b" stroke-width="3"/>'+g(-24,-k*24,.35,lamp())+g(24,-k*24,.35,lamp()) for k in range(1,5)))+g(120,170,1,person('#8e1f17'))+g(146,120,.5,lamp())+g(440,170,1,person('#1d4f8a'))+g(466,120,.5,lamp())+g(500,40,1,'<circle r="2" fill="#fff"/>'),'#20243a',195),
 ['<b>Tuḍar parba.</b> “The festival of lamps” (tuḍar is a lamp): Dīpāvali on the coast, a three-day celebration in Bontel and Jārde.',
  '<b>The first day.</b> An oil bath, new clothes, lamps and sweets. Sweetened beaten rice, <b>bajil</b>, is the dish of the morning. Families who lost someone in the year hold <b>bajil paḍunu</b>, an offering of beaten rice in memory of them.',
  '<b>Bali comes home.</b> The third day, <b>Balipāḍyami</b>, belongs to <b>Bali Cakravarti</b> (Baliyendra), the generous king Vāmana sent to the underworld, whom the coast remembers as its own. Families raise a tall bamboo or a branch, the <b>Baliyendra mara</b>, decorated with lamps before the house.',
  '<b>Calling him.</b> Farmers walk into the harvested fields at night with lamps and torches, calling Bali to come and see the prosperity of the land. The cattle and the farm tools are worshipped too.',
  '<b>Read more.</b> See our '+L('/festivals/deepavali/','Dīpāvali')+' guide and the Vāmana story in '+L('/vishnu/dashavatara/','Daśāvatāra')+'.'],
 [('z','Is it sad that he never really arrives?'),('b','That is the beauty of it. You set out lamps every year for a king who loved his people. The calling is the devotion.')],'Lamps in the fields <b>for the king who loved his land</b>.')
jarde=reading('jarde','JĀRDE TO PONNI','The season reopens',
 S('A bhūta kōla performer, Kambaḷa buffaloes and a Yakṣagāna actor: the season begins',g(110,180,1.1,person('#c0392b'))+'<path d="M80 90 q30 -50 60 0z" fill="#e0a800"/>'+g(280,175,.7,'<rect x="-60" y="-30" width="120" height="30" rx="14" fill="#3a3a3a"/><circle cx="68" cy="-26" r="14" fill="#3a3a3a"/>')+T(280,190,'Kambaḷa')+g(450,180,1.1,person('#1d4f8a'))+'<path d="M428 92 l22 -30 l22 30z" fill="#e0a800"/>'+T(110,190,'kōla')+T(450,190,'Yakṣagāna'),'#fff3cf',200),
 ['<b>The doors open.</b> With Jārde, around Dīpāvali, the outdoor season of the coast begins again: daiva nēmas and kōlas, temple jātres, Kambaḷa races in the wet fields, and the Yakṣagāna troupes on the road.',
  '<b>Tuḷasi parba.</b> The <b>Tuḷasi</b> plant is worshipped and married to Kṛṣṇa (Tulasī Vivāha) around Utthāna Dvādaśī; lamps are lit at the tuḷasi platform.',
  '<b>Perārde.</b> The cold month of December–January, thick with nēmas: the guardians’ nights at house and village shrines.',
  '<b>Ponni.</b> Makara saṅkrānti opens Ponni; in Uḍupi it is the great chariot festival of Kṛṣṇa. At the end of Ponni comes Keḍḍasa.',
  '<b>Read more.</b> '+L('/tulunadu/daiva/bhuta-kola/','Bhūta Kōla')+', '+L('/tulunadu/culture/kambala/','Kambaḷa')+', '+L('/tulunadu/culture/yakshagana/','Yakṣagāna')+'.'],
 [('z','How do they fit so much into six months?'),('b','Every village has its own day. Over a season, a person can go to a kōla, a race or a play almost every week.')],'Six months of <b>races, plays and guardians</b>.')
kedd=reading('keddasa','PONNI · KEḌḌASA','Three days when the Earth rests',
 S('The Earth as a resting mother, a plough set aside, a leaf with offerings',
  '<rect y="150" width="560" height="45" fill="#8a6a3a"/>'+g(280,160,1.2,devi(sari='#2a9d6f',items=()))+g(120,150,.9,'<path d="M-40 0 l60 -30 M10 -24 l16 22" stroke="#7a5a2a" stroke-width="6"/>')+T(120,186,'the plough rests',10,fill='#fff')+g(440,160,1,'<path d="M-40 0 q40 -20 80 0z" fill="#3a9a4a"/>'+g(-14,-6,.6,banana())+g(16,-6,.5,coconut()))+T(440,186,'offerings on a leaf',10,fill='#fff'),'#e9f2e1',195),
 ['<b>The Earth’s season.</b> Keḍḍasa, also Bhūmi Pūje, is the festival of Mother Earth, held over the last three days of Ponni, usually in February.',
  '<b>Three days.</b> They are named Keḍḍasa, Naḍu (middle) Keḍḍasa and Kaḍe (last) Keḍḍasa.',
  '<b>Bhūmi Devī rests.</b> The belief is that the Earth goddess menstruates in these days and becomes fertile for the coming crops. As for a woman in her period, she is left to rest: all farm work stops and no one digs or ploughs.',
  '<b>Her bath and her meal.</b> At the end she is honoured as after a bath: offerings of oil, soap-nut, kuṅkuma and food are laid out on banana leaves for her. Only after these rites may the earth be dug again.',
  '<b>Hunting.</b> With the fields closed, men of farming communities traditionally went hunting in these days.'],
 [('z','A festival for the Earth’s period?'),('b','A way of saying the land is a living mother who must rest before she gives. Assam’s Ambubāchī and Odisha’s Raja Parba say the same thing.')],'The land is a mother <b>who must rest</b>.')
maayi=reading('maayi','MĀYI AND SUGGI','The year closes',
 S('A bhūta kōla at night with torches, and women singing harvest songs at a threshing floor',
  '<rect width="280" height="190" fill="#20243a"/>'+g(140,180,1.2,person('#c0392b'))+'<path d="M110 92 q30 -60 60 0z" fill="#e0a800"/>'+g(70,150,1,'<path d="M0 0 v-40" stroke="#c98a5a" stroke-width="5"/>'+flame(1))+g(210,150,1,'<path d="M0 0 v-40" stroke="#c98a5a" stroke-width="5"/>'+flame(1))
  +'<rect x="280" width="280" height="190" fill="#f3e3a8"/><ellipse cx="420" cy="160" rx="110" ry="18" fill="#d8b878"/>'+g(360,170,1,person('#8e1f17'))+g(420,170,1,person('#2a9d6f'))+g(480,170,1,person('#e0a800')),'#fff',190),
 ['<b>Māyi.</b> The month of Māyi (February–March) closes the agricultural year: the Suggi crop is in and the fields rest. Village jātres and daiva festivals crowd these weeks.',
  '<b>Kaṅgilu.</b> In Māyi the <b>Nalike</b> community’s Kaṅgilu dance goes round the villages with song and drum, a seasonal blessing like Āṭi Kaḷeñja.',
  '<b>Suggi.</b> The last month, March–April, takes its name from the harvest. Its songs, the <b>suggi</b> songs, were sung by women at the threshing floor and in the fields.',
  '<b>Into Bisu.</b> Suggi ends with saṅkrānti, and the next morning the family looks at the Bisu kaṇi again. The wheel turns.',
  '<b>A living calendar.</b> Few families farm now, but the calendar has outlived the paddy: Āṭi amāse, Tuḍar and Bisu are kept in flats in Maṅgaḷūru and Mumbai.'],
 [('z','Will the calendar survive without farming?'),('b','It already is surviving. The kaṣāya is drunk in cities. The meaning shifts from the field to the family, but the days hold.')],'Harvest in, <b>the wheel turns to Bisu</b>.')
endp=end(i,['<b>Sun.</b> Twelve solar months, Paggu to Suggi; each begins at the sun’s crossing.','<b>Rice.</b> The year follows the paddy: rain for the fields, dry months for the gods.','<b>Rains.</b> Pattanāje closes the season; Āṭi brings bitter bark, Kaḷeñja and the serpents.','<b>Harvest and lamps.</b> Koral brings the first sheaves; Tuḍar calls King Bali home.','<b>Rest.</b> Keḍḍasa lets the Earth rest; Suggi closes the year into Bisu.'],
 'Part 2 goes to Maṅgaḷūru for its people’s Dasarā at Kudroḷi.','A year set by the sun, the rain and the rice')
src=sources([('Calendar:','Wikipedia, “Tulu calendar”; Deccan Herald on the Tuḷu calendar; The Federal on Māyi and the farming year; mangaloreheritage.com (Tuḷu calendar, Pattanāje, Keḍḍasa, Āṭi, Āṭi amāse, Koral Parba, Tuḍar Parba); our '+L('/tulunadu/start-here/','Tulu Nadu: Start Here')+'.'),
 ('Observances:','Wikipedia: Bisu Parba, Pattanāje, Keḍḍaso, Āṭida Amāse, Āṭi Kaḷeñja; Deccan Herald on Yakṣagāna and Pattanāje, on Kadiru Kaṭṭuvudu and on Āṭi Kaḷeñja; tulupedia on Pattanāje; Udayavani and Deccan Chronicle on Āṭi amāse; NewsKarnataka on Kural Parba; Udayavani, The News Minute and Deccan Herald on Bali in Tuḷu Dīpāvali.')],
 'month spellings vary widely; the three paddy seasons and the three weather names are given as in one source each; Kaṅgilu is described only briefly as details were not checked; dates of Koral Parba and of the Āṭi agel offering differ by family and village.','Month names and seasons as in the sources above.')
finish(i,'PART 1 OF 9 · BISU · ĀṬI · TUḌAR · KEḌḌASA',covart('A wheel of the twelve Tuḷu months around the sun with paddy and a lamp',g(-60,-8,.9,wheel())+g(70,190,.8,'<path d="M0 0 q-4 -30 6 -48 M0 0 q4 -26 -6 -44" fill="none" stroke="#b8860b" stroke-width="4"/>')+g(380,186,1,lamp())),'Twelve months around the sun',
 'Month by month through the <b>Tuḷu year</b>: how it is counted, the <b>rice</b> that drives it, and every observance from <b>Bisu</b> to <b>Suggi</b>.',
 'The Tuḷu year explained and illustrated: the twelve solar months Paggu to Suggi, Bisu, Pattanāje, Āṭi amāse and pāle kaṣāya, Āṭi Kaḷeñja, Nāgara Pañcamī, Koral Parba, Pilivēṣa, Tuḍar Parba and King Bali, Keḍḍasa and the harvest.',
 [fw,gl,sun_,seasons,bisu,patt,aati,amase,kalenja,naga,koral,nirnala,tudar,jarde,kedd,maayi,endp,src])
