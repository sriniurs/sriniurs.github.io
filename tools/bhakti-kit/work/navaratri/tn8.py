from tn_common import *
i=7
def dolu(s=1): return g(0,0,s,'<ellipse rx="30" ry="12" fill="#e9d6c0"/><path d="M-30 0 v50 q30 16 60 0 v-50" fill="#8e1f17"/><path d="M-30 8 l60 34 M30 8 l-60 34" stroke="#ffd60a" stroke-width="2"/><ellipse cy="50" rx="30" ry="10" fill="#e9d6c0"/>')
def boat(): return '<path d="M-50 0 h100 l-14 16 h-72z" fill="#c98a5a"/><path d="M0 0 v-50 l34 40z" fill="#fff8ec"/>'
def bmap():
    o=map_frame()+'<path d="M90 120 q140 -20 260 0 q80 14 210 -10" fill="none" stroke="#8fb8de" stroke-width="12"/>'+T(400,100,'Śāmbhavī',10,fill='#1d4f8a')
    o+='<path d="M90 160 q100 10 180 -36" fill="none" stroke="#8fb8de" stroke-width="10"/>'+T(170,180,'Nandinī',10,fill='#1d4f8a')
    o+=pin(300,110,'Bappanāḍu temple')+pin(360,160,'Mulki town')+pin(140,120,'Sasihitlu',.3)+pin(420,60,'to Uḍupi →',.3)+pin(420,210,'← to Maṅgaḷūru (29 km)',.3)
    return o
fw=foreword(i,['On the bank of the Śāmbhavī at Mulki stands a Goddess who chose her devotees widely: she stayed for a toddy-tapper’s coconut, called a Muslim trader in a dream to build her house, and had a Jain king raise it. Every April her chariot festival fills the town, her palanquin stops at the trader’s descendants’ door with prasāda, and her great drum is beaten so loud the coast has a saying about it.',
 'This is the <b>Bappanāḍu Jātre</b>. This guide covers the seven Durgās and their sandalwood boat, the tender coconut, Bappa Beary’s red river, the eight days of the festival, the chariots, the <b>prasāda for Bappa’s family</b>, and the <b>Bappanāḍu ḍōlu</b>.',
 'The temple is in '+L('/tulunadu/temples/bappanadu-durgaparameshwari/','Bappanāḍu Durgāparameśvarī')+'. Previous: '+L('/tulunadu/festivals/kodi-habba/','Koḍi Habba')+'.'],
 [('z','A Muslim trader and a Goddess?'),('b','The coast’s favourite story about itself. Every year the festival acts it out again at his family’s door.')])
gl=glance([('Where','Śrī Durgāparameśvarī temple, Bappanāḍu, Mulki, about 29 km north of Maṅgaḷūru'),('Goddess','Durgāparameśvarī in the form of a liṅga; “Uḷḷāḍi” to the Tuḷuvas'),('River','The Śāmbhavī, near its meeting with the Nandinī and the sea'),('Name','“Bappa’s land”, after Bappa Beary, a Muslim trader'),('Builders','By tradition the Jain Sāvanta of Mulki, with Bappa; first priest Baila Uḍupa'),('Jātre','Eight days from Mīna śuddha caturdaśī (March–April)'),('Climax','The night Brahma Rathōtsava'),('Harmony','Prasāda handed to Bappa’s descendants during the procession'),('Drum','The giant Bappanāḍu ḍōlu'),('Fair','About three weeks around the temple')],
 S('A great drum beside a temple, a chariot behind',g(140,190,1.6,dolu())+g(330,190,1.2,tulu_temple())+g(480,195,1,RATHA(0,0,1,'#c0392b')),'#e3eaf3',200),
 [('z','Is the drum played every day?'),('b','Its great days are the festival. The rest of the year it stands at the entrance like a guardian.')],'A Goddess, a trader, <b>and a drum</b>.')
place=reading('place','MULKI','Rivers, sea and a moving shore',svg(560,230,'Simplified map of Mulki with the Śāmbhavī and Nandinī rivers and the Bappanāḍu temple',bmap()),
 ['<b>The temple.</b> On the bank of the Śāmbhavī at Bappanāḍu, in Mulki town, beside the highway from Maṅgaḷūru to Uḍupi.',
  '<b>Two rivers.</b> Tradition places the Goddess’s first appearance at the meeting of the Śāmbhavī and the Nandinī; the Nandinī is the river of '+L('/tulunadu/festivals/katil-festivals/','Kaṭīl')+'.',
  '<b>A shifting shore.</b> European travellers in 1516 and 1623 found the area of today’s Mulki under water; later shifts of the river made the land the town stands on.',
  '<b>The Sāvantas.</b> A Jain family, the Sāvantas, ruled the Mulki region from the 14th to the 18th century; the family still lives at Paḍupaṇambūr.',
  '<b>Uḷḷāḍi.</b> Tuḷuvas call the Goddess <b>Uḷḷāḍi</b>, “the Lady”.'],
 [('z','The town wasn’t always there?'),('b','The rivers moved it into being. The Goddess was found in the water, and the land came later.')],'A Goddess found <b>where the rivers meet</b>.')
seven=story('seven','STORY · THE SEVEN DURGĀS','Dārikāsura and Bhadrakāḷī',
 strip('Three panels: seven goddesses before Viṣṇu; an old woman at a demon’s palace receiving weapons; a fierce goddess slaying the demon in the underworld',
  [('<rect width="144" height="190" fill="#e3eaf3"/>'+''.join(g(14+k*19,170,.42,devi(sari=['#c0392b','#e0a800','#1d4f8a','#2a9d6f','#8e1f17','#6a3d9a','#3a3a50'][k],items=())) for k in range(7)),'#e3eaf3'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(40,170,.8,person('#9a9a9a'))+g(104,170,.8,person('#6a3d9a'))+g(72,110,.5,trident()),'#fff3cf'),
   ('<rect width="144" height="190" fill="#3a2a50"/>'+g(60,170,.85,devi(skin='#3a3a50',sari='#1b1b1b',items=('sword','trident'),fierce=True))+g(116,170,.6,demon()),'#3a2a50')],
  ['seven sisters','the trick','Bhadrakāḷī']),'The story behind the Goddess of Bappanāḍu, as in our temple guide.',
 ['The demon <b>Dārikāsura</b>, with a boon from Brahmā, defeated the gods and even Viṣṇu, and gave Viṣṇu’s weapons to his wife to keep.',
  'The Goddess appeared as seven women, the <b>Sapta Durgās</b>, and promised to destroy him. With them went the daiva <b>Guḷiga</b>.',
  'One sister, <b>Bhagavatī</b>, came to the palace as an old woman begging for food and won the weapons from the demon’s wife.',
  'After seven days of battle Dārika fled to the underworld.',
  '<b>Bhadrakāḷī</b> found him there at evening, worshipping Śiva, and killed him. The same myth is the great story of the Goddess temples of Kerala.'],
 [('z','Seven sisters, and one of them is Bappanāḍu’s?'),('b','Bhagavatī, the one who stayed behind on this coast. The next page tells why.')],'Seven sisters <b>against one demon</b>.')
coco=story('coconut','STORY · THE BOAT AND THE COCONUT','Why she stayed at Mulki',
 strip('Three panels: a sandalwood boat sailing up the coast with goddesses aboard; a toddy-tapper offering a tender coconut; the goddess sinking into the earth as a stone',
  [('<rect width="144" height="190" fill="#bcd3ea"/><rect y="140" width="144" height="50" fill="#4aa3df"/>'+g(72,140,.9,boat()),'#bcd3ea'),
   ('<rect width="144" height="190" fill="#e9f2e1"/>'+g(40,170,.9,person('#5a3a1a'))+g(72,120,.8,coconut())+g(108,170,.8,devi(items=())),'#e9f2e1'),
   ('<rect width="144" height="190" fill="#c9a36b"/>'+g(72,160,1,LINGA(0,0,1))+'<path d="M40 120 q32 -30 64 0" fill="none" stroke="#ffd60a" stroke-width="3"/>','#c9a36b')],
  ['the sandalwood boat','a tender coconut','into the earth']),'The voyage of the sisters, as told at Bappanāḍu.',
 ['After the victory, Bhagavatī, her sisters and Guḷiga asked Viṣṇu for a boat to go down to earth; he gave them a <b>sandalwood tree</b>, and they made their boat from it.',
  'It sailed north up the coast, past Kāsaragōḍ, Kumbḷe, Mañjēśvara, Uḷḷāla and Kudroḷi, to Sasihitlu near Mulki. (Another telling has them walk north from Kanyākumārī.)',
  'At Mulki a <b>toddy-tapper</b> offered Bhagavatī a tender coconut, and she drank it.',
  'In one telling her sisters would not travel on with her after she accepted a drink from a man of low caste; they went on without her.',
  'She declared the man her devotee, chose to stay, and took the form of a liṅga in the earth between the rivers, unseen, until she was found.'],
 [('z','So the Goddess stayed for the one who served her?'),('b','That is the shape of the story. She stayed for a toddy-tapper’s coconut, and later chose a Muslim trader to build her house.')],'She stayed <b>where she was welcomed</b>.')
bappa=story('bappa','STORY · BAPPA’S BOAT','The trader and the red river',
 strip('Three panels: a trader’s boat stuck in a reddened river; the trader asleep dreaming of the Goddess; the trader, a king and a priest before a new temple',
  [('<rect width="144" height="190" fill="#bcd3ea"/><rect y="130" width="144" height="60" fill="#c0392b"/>'+g(72,134,.9,boat())+g(60,130,.6,person('#2a9d6f')),'#bcd3ea'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(50,170,.8,'<rect x="-30" y="-10" width="60" height="10" fill="#2a9d6f"/><circle cx="-34" cy="-8" r="7" fill="#c98a5a"/>')+g(100,110,.6,devi(items=('trident',),halo='#ffd60a')),'#20243a'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(30,170,.7,person('#2a9d6f'))+g(72,170,.7,person('#e0a800'))+g(114,170,.7,person('#f4f1ea'))+g(72,90,.45,tulu_temple()),'#fff3cf')],
  ['the red river','the dream','three builders']),'The founding of the temple, as tradition tells it.',
 ['<b>Bappa Beary</b>, a Muslim merchant, often said to be from Kerala, was carrying goods up the Śāmbhavī.',
  'Near Mulki his boat would not move, and he saw the water around it turn <b>red as blood</b>.',
  'He slept in the boat. The Goddess appeared in a dream, told him there is one God for the whole world, and asked him to have a temple built through the king of Mulki, with <b>Baila Uḍupa</b> as priest. She promised his name would be remembered for ever.',
  'Bappa gave his wealth; the Jain <b>Mulki Sāvanta</b> built the temple; the liṅga was found under the water and installed.',
  'Bappa settled nearby, and the place became <b>Bappanāḍu</b>, “Bappa’s land”.'],
 [('z','A Muslim, a Jain and a Brahmin build a Devī temple?'),('b','Each with his part. That is why the temple is held up as a symbol of the coast living together.')],'Her promise: <b>his name for ever</b>.')
jat=reading('jatre','THE EIGHT DAYS','From the flag to the great chariot',
 svg(560,150,'Timeline of the eight days of the Bappanāḍu jātre','<rect width="560" height="150" fill="#fff3cf"/>'+tl_strip([('Day 1','flag up'),('Day 2','bali, lamps'),('Day 3','to the market'),('Day 4','Koppaḷa'),('Day 5','Bakimāru'),('Day 6','tank lamps'),('Day 7','Candramaṇḍala'),('Day 8','Brahma Ratha')],560,150)),
 ['<b>Day 1.</b> <b>Dhvajārōhaṇa</b>, the flag raised, on Mīna śuddha caturdaśī. <b>Day 2.</b> Bali utsava and Āyana dīpōtsava.',
  '<b>Day 3.</b> <b>Pēṭe savāri</b>, the Goddess’s procession to the market (pēṭe). <b>Day 4.</b> Koppaḷa savāri.',
  '<b>Day 5.</b> Bakimāru dīpōtsava. <b>Day 6.</b> <b>Kere dīpōtsava</b>, lamps at the tank.',
  '<b>Day 7.</b> A morning chariot; at night the <b>Candramaṇḍala</b> chariot and śayanōtsava, the Goddess put to rest.',
  '<b>Day 8.</b> The doors opened (kavāṭa), and at night the great <b>Brahma Rathōtsava</b>; then the closing bath. The temple has several chariots for these days.'],
 [('z','What are Koppaḷa and Bakimāru?'),('b','Names of places or rites of the festival whose meaning we could not confirm. We give them as the temple does.')],'Eight days that <b>end in the great chariot</b>.')
prasada=reading('prasada','PRASĀDA FOR BAPPA’S FAMILY','The palanquin at the trader’s door',
 S('A palanquin stopping at a house; a priest handing flowers and sandal paste to a man at the door',g(140,190,1,'<rect x="-40" y="-30" width="80" height="30" fill="#e0a800"/><path d="M-60 -16 h120" stroke="#8a6a3a" stroke-width="5"/>')+g(100,196,.8,person('#f4f1ea'))+g(180,196,.8,person('#f4f1ea'))+g(330,190,1.1,person('#f4f1ea'))+g(360,120,.7,plate()+g(0,-4,.5,lotus('#e05050','#8e1f17')))+g(440,190,1.2,person('#2a9d6f'))+g(490,190,1,'<rect x="-40" y="-70" width="80" height="70" fill="#e9d6c0"/><path d="M-46 -70 l46 -26 l46 26z" fill="#a0522d"/>'),'#fff3cf',205),
 ['<b>The custom.</b> During the festival, as the Goddess’s palanquin reaches the house of Bappa Beary’s descendants, the priest hands them <b>gandha prasāda</b> (sandal paste) and flowers before going on.',
  '<b>Since Bappa’s time.</b> The family says the custom has run since Bappa’s own time; the family in turn offers flowers and fruit to the Goddess.',
  '<b>Kept in hard times.</b> In 2022, amid tensions on the coast, the temple management kept the custom and placed no restrictions on non-Hindus at the fair.',
  '<b>“Our village’s fair.”</b> Local residents of all communities call the jātre the fair of the whole village.',
  '<b>Her promise kept.</b> The Goddess promised Bappa his name would be remembered for ever; the prasāda at his family’s door is that promise, kept every year. (Interpretation.)'],
 [('z','Is Bappa’s story history or legend?'),('b','The records are thin. A 1607 copperplate names a Bappa; who he was is debated. The custom at the door is very real.')],'A promise <b>kept at a door every year</b>.')
drum=reading('dolu','THE BAPPANĀḌU ḌŌLU','The drum the whole coast knows',
 S('A giant drum at a temple entrance being beaten by drummers with curved sticks',g(280,190,2.6,dolu())+g(150,190,1.1,person('#c0392b'))+g(410,190,1.1,person('#1d4f8a'))+'<path d="M170 110 l40 -20 M390 110 l-40 -20" stroke-width="4"/>','#e3eaf3',210),
 ['<b>The drum.</b> An outsize <b>ḍōlu</b> stands by the temple’s main entrance; it has been shown as a heritage piece of Tuḷunāḍu at the Karāvaḷi Utsav in Maṅgaḷūru.',
  '<b>Known everywhere.</b> The beating of the Bappanāḍu ḍōlu is famous all over Tuḷunāḍu.',
  '<b>The drummers.</b> Festival drumming is the hereditary right of a particular community, to whom the temple pays an honorarium.',
  '<b>The saying.</b> “Go and beat the ḍōlu at Bappanāḍu” is a Tuḷu taunt for someone good for nothing, sent off to do noisy, useless work.',
  '<b>A great rite.</b> A scholar of Tuḷu ritual lists the Bappanāḍu ḍōlu among the seven great ritual events of Tuḷunāḍu.'],
 [('z','A drum famous enough to have its own insult?'),('b','That is fame. Every child on the coast knows what you mean.')],'A drum loud enough <b>to become a proverb</b>.')
ratha=reading('ratha','THE CHARIOT NIGHT','Brahma Rathōtsava',
 S('A tall decorated chariot at night drawn by crowds, a smaller chariot behind','<rect width="560" height="210" fill="#20243a"/>'+g(260,200,2,RATHA(0,0,1,'#c0392b'))+g(450,200,1.1,RATHA(0,0,1,'#e0a800'))+g(260,206,1,crowd(10,400,0,.4))+g(80,60,1,fireworks()),'#20243a',210),
 ['<b>The great night.</b> On the last night the Goddess rides in the <b>Brahma Ratha</b>, the temple’s largest and most decorated chariot, drawn through the night by the crowds.',
  '<b>Other chariots.</b> The temple keeps several chariots: smaller ones for the morning chariot and the <b>Candramaṇḍala</b> (“moon-disc”) chariot of the seventh night.',
  '<b>2025.</b> During the Brahma Rathōtsava in April 2025, the decorated upper part of the great chariot toppled. People moved away in time and no one was seriously hurt; the procession continued in a smaller chariot and all rites were completed.',
  '<b>Avabhṛtha.</b> The festival ends with the closing bath of the festival image.',
  '<b>The fair.</b> Around it, a fair of about three weeks.'],
 [('z','Was the 2025 accident taken as a bad omen?'),('b','The rites went on, in another chariot. What people remember is that no one was hurt.')],'The Goddess rides <b>through the night</b>.')
year=cards('year','THROUGH THE YEAR','The Goddess’s other days',
 S('Lamps and a moon over the temple',g(280,190,1.1,tulu_temple())+lamps_row(130,196,10,32,.45)+g(470,40,1,moon()),'#e3eaf3',200),
 [('🪔','Navarātri','Nine nights of special worship of the Goddess.'),('✨','Dīpōtsavas','Festivals of lamps through the year.'),('🌙','Ananta Caturdaśī','Observed at the temple.'),('❄️','Dhanurmāsa','Dawn worship in winter.'),('🎪','The fair','About three weeks round the jātre.'),('🙏','Every day','Worship three times a day: morning, noon and night.')],
 None,'A Goddess <b>worshipped all year</b>.')
endp=end(i,['<b>Goddess.</b> Durgāparameśvarī as a liṅga, one of seven sisters, who stayed for a coconut.','<b>Builders.</b> Bappa Beary, the Jain Sāvanta and the priest Baila Uḍupa.','<b>Eight days.</b> Flag, bali, market procession, lamps, Candramaṇḍala, Brahma Ratha.','<b>Harmony.</b> Prasāda handed to Bappa’s descendants every year.','<b>Drum.</b> The ḍōlu that became a proverb.'],
 'Part 9, the last, goes to the Siri Jātre and the women of the Siri epic.','The Goddess who chose her people widely')
src=sources([('Bappanāḍu:','Our '+L('/tulunadu/temples/bappanadu-durgaparameshwari/','Bappanāḍu Durgāparameśvarī')+' guide (stories, festival days, ḍōlu; its sources); Deccan Herald (2022) on gandha prasāda to Bappa’s descendant; mangaloreheritage.com (Uḷḷāḍi; Brahma Rathōtsava); templesofindia.org (honours to Bappa’s family; chariots); The Hindu, Deccan Herald, Deccan Chronicle and Free Press Journal on the 2025 chariot incident.')],
 'the meanings of Koppaḷa and Bakimāru savāri; Bappa’s historical identity; whether the sisters came by boat or on foot; a reported fire play at the jātre is not confirmed and is left out.','Festival days as in our temple guide.')
finish(i,'PART 8 OF 9 · THE DRUM · THE CHARIOT · BAPPA',covart('A giant drum, a temple and a palanquin stopping at a house',g(90,186,1.4,dolu())+g(230,186,1,tulu_temple())+g(370,186,1.1,RATHA(0,0,1,'#c0392b'))),'The drums of the river Goddess',
 'The <b>Bappanāḍu Jātre</b>: the seven Durgās and the coconut, <b>Bappa’s red river</b>, eight days of festival, <b>prasāda at Bappa’s door</b>, and the great <b>ḍōlu</b>.',
 'Bappanāḍu Jātre at Mulki explained and illustrated: Durgāparameśvarī as a liṅga, the seven Durgās and Dārikāsura, the sandalwood boat and tender coconut, Bappa Beary’s boat, the eight-day jātre, Brahma Rathōtsava, prasāda to Bappa’s family and the Bappanāḍu ḍōlu.',
 [fw,gl,place,seven,coco,bappa,jat,prasada,drum,ratha,year,endp,src])
