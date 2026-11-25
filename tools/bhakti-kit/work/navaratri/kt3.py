from kt_common import *
i=2
def neem(): return '<path d="M0 0 q-10 -10 -4 -24 M0 0 q12 -8 8 -22 M0 0 v-26" fill="none" stroke="#2f7a3a" stroke-width="3"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="2.5" fill="#3a9a4a"/>' for x,y in [(-6,-20),(8,-18),(0,-26)])
def axe(): return '<path d="M0 0 v-60" stroke="#8a6a3a" stroke-width="4"/><path d="M0 -60 q18 4 20 20 q-12 -4 -20 -4z" fill="#9a9a9a"/>'
def ymap():
    o='<rect width="560" height="230" fill="#eadcc0"/><path d="M0 170 q180 -30 300 0 t260 -10" fill="none" stroke="#8fb8de" stroke-width="16"/>'+T(90,200,'Malaprabhā · Reṇukā Sāgara',10,fill='#1d4f8a')
    o+=g(300,130,1.8,mountain('#b08a62'))+pin(300,70,'Yellamma temple',.4)+T(300,148,'Yallammanagudda (Siddhācala / Rāmagiri)',9)
    o+=pin(470,100,'Savadatti town (5 km)')+pin(140,90,'to Dharwad (38 km)',.3)+pin(440,30,'to Belagavi',.3)
    return o+T(480,226,'simplified, not to scale',9)
fw=foreword(i,['On a bare hill above the Malaprabhā, five kilometres from Savadatti, sits the Goddess the Deccan calls <b>Yellamma</b>, “mother of all”. She is Reṇukā, wife of the sage Jamadagni and mother of Paraśurāma. Twice a year, on full-moon days, the hill takes in crowds counted in lakhs from Karnataka, Maharashtra, Goa and Andhra, many bathing in her tanks, many walking round with neem leaves in their mouths.',
 'This guide covers the hill and its names, Reṇukā’s story and its tellings, the temple of 1514 and its far older past, the shrines and sacred waters of the hill, the great full moons, the Goddess’s devotees, and, plainly, the devadāsī custom and its abolition.',
 'Part 3 of '+L('/temples-of-india/karnataka/','Temples of Karnataka')+'. Previous: '+L('/temples-of-india/karnataka/belur-halebidu/','Belūr and Haḷebīḍu')+'. Paraśurāma is in our '+L('/vishnu/dashavatara/','Daśāvatāra')+' series.'],
 [('z','The mother whose son beheaded her?'),('b','And who came back to life, and became the Mother of everyone who climbs her hill. Her story is hard, and that is why people trust her.')])
gl=glance([('Goddess','Reṇukā, called Yellamma (Ellamma), “mother of all”; Jagadambā'),('Family','Wife of the sage Jamadagni; mother of Paraśurāma'),('Place','Yallammanagudda, about 5 km from Savadatti (Saundatti), Belagavi district'),('Hill','Siddhācala or Rāmagiri range, over the Malaprabhā'),('Temple','Built 1514 by Bomappa Nāyaka of Raybag'),('Older','Traces of a temple from the 8th–11th c.; megalithic tombs and early pottery'),('Style','Cāḷukya and Rāṣṭrakūṭa'),('Great days','Two great full moons (Bharata and Banada Hunnime), crowds of lakhs'),('Managed by','The Government of Karnataka, since 1975'),('Pilgrims','Karnataka, Maharashtra, Goa, Andhra Pradesh, Telangana')],
 S('A temple on a hill over a river, pilgrims climbing',g(280,190,2,mountain('#b08a62'))+g(280,104,.6,tulu_temple('#c0392b','#8e1f17'))+'<path d="M0 200 h560" stroke="#8fb8de" stroke-width="14"/>'+g(160,180,.8,crowd(5,120,0,.5)),'#f6e3e1',210),
 [('z','Why “Yellamma”?'),('b','Commonly explained as “mother of all” (ella-amma) in Kannaḍa. Her devotees simply call her Amma.')],'The mother <b>of everyone who climbs</b>.')
where=reading('where','THE HILL','Yallammanagudda over the Malaprabhā',svg(560,230,'Simplified map of Yallammanagudda above the Malaprabhā near Savadatti',ymap()),
 ['<b>The hill.</b> The temple sits on a hilltop once called <b>Siddhācala</b>, now <b>Yallammanagudda</b>, “Yellamma’s hill”, part of an east–west range also called Rāmagiri.',
  '<b>The river.</b> It overlooks the <b>Malaprabhā</b>, dammed nearby at Navilutīrtha into a reservoir named <b>Reṇukā Sāgara</b> after the Goddess.',
  '<b>The town.</b> Savadatti (Saundatti) lies about 5 km away; Dharwad is about 38 km and Huballi about 58 km.',
  '<b>Ancient ground.</b> Megalithic tombs on the hill are older than any temple, and potsherds date from about the 3rd century BCE to the 3rd century CE.',
  '<b>Savadatti.</b> The town has its own fort and old temples, with Raṭṭa inscriptions.'],
 [('z','People were on this hill before the temple?'),('b','For two thousand years at least. A sacred hill tends to stay sacred.')],'A hill sacred <b>for two thousand years</b>.')
ren=story('renuka','STORY · REṆUKĀ','The pot of water and the axe',
 strip('Three panels: a woman carrying water in an unbaked pot by a river where heavenly beings bathe; a sage commanding a young man with an axe; the woman restored',
  [('<rect width="144" height="190" fill="#bcd3ea"/><rect y="140" width="144" height="50" fill="#4aa3df"/>'+g(40,170,.9,devi(sari='#c0392b',items=()))+g(62,86,.6,'<ellipse rx="12" ry="10" fill="#c9a36b"/>')+g(110,150,.6,person('#ffd60a')),'#bcd3ea'),
   ('<rect width="144" height="190" fill="#eadcc0"/>'+g(40,170,.9,sage())+g(104,170,.9,person('#8e1f17'))+g(120,150,.8,axe()),'#eadcc0'),
   ('<rect width="144" height="190" fill="#f6e3e1"/>'+g(72,170,1,devi(sari='#c0392b',items=('lotus',),halo='#ffd60a')),'#f6e3e1')],
  ['the unbaked pot','the father’s command','the mother restored']),'Reṇukā’s story, in the form told at the temple and in the Purāṇas (tellings differ).',
 ['<b>Reṇukā</b>, a king’s daughter, married the sage <b>Jamadagni</b>. So pure was she, the story goes, that she could carry river water home in a pot of unbaked clay, held together by her purity alone.',
  'One day at the river she saw a heavenly being (a gandharva) bathing with his companions, and for a moment her mind wavered. The pot dissolved.',
  'Knowing what had happened, Jamadagni ordered his sons to kill her. The elder sons refused. The youngest, <b>Paraśurāma</b>, obeyed and beheaded his mother with his axe.',
  'Pleased, Jamadagni offered him a boon. Paraśurāma asked that his mother be brought back to life (and his brothers restored), and she was.',
  'In one telling, in his haste the head of another woman, dark-skinned, was set on Reṇukā’s body, which explains the Goddess’s dark face here. Another account says Reṇukā became a satī after Jamadagni was killed by Kārtavīrya Arjuna.'],
 [('z','A son who kills his mother is a hero?'),('b','The story is not comfortable, and it is not meant to be. What the devotees hold on to is the end: the mother who was wronged, killed, and came back stronger, as the Mother of all.')],'Wronged, killed, <b>and restored as the Mother</b>.')
godd=reading('goddess','YELLAMMA','The Goddess on the hill',
 S('The Goddess with a dark face and a crown, a lamp and coconuts before her',g(280,200,2,devi(skin='#5a3a2a',sari='#c0392b',items=('trident','lotus')))+g(150,200,1,lamp())+g(420,200,1.2,coconut()),'#f6e3e1',210),
 ['<b>Her names.</b> Reṇukā; Yellamma or Ellamma; Jagadambā, “mother of the world”; and <b>Yelumakkaḷatāyi</b>, “mother of seven children”.',
  '<b>A fertility goddess.</b> She is revered as a fertility goddess and counted among the Saptamātṛkās, the seven mothers; many believe her a form of Kālī.',
  '<b>Older than her story.</b> Scholars think a goddess cult was present on the hill in the Cāḷukya period or before; the Reṇukā story gave the local Mother a place in the Purāṇic world. (Scholarly view.)',
  '<b>Her face.</b> The Goddess is shown with a dark face, explained by the story of the replaced head.',
  '<b>Her household.</b> Shrines on the hill honour Gaṇeśa, Mallikārjuna, Paraśurāma, Ekanātha and Siddheśvara.'],
 [('z','Mother of seven children?'),('b','A title of a mother goddess of the people. She is above all the mother everyone can come to.')],'A mother goddess <b>given a Purāṇic story</b>.')
hist=reading('history','THE TEMPLE OF 1514','Bomappa Nāyaka and the older temple',
 svg(560,150,'Timeline of the Yellamma hill','<rect width="560" height="150" fill="#fff3cf"/>'+tl_strip([('ancient','megaliths'),('3c BCE–3c CE','pottery'),('8th–11th c.','early temple'),('1514','Bomappa Nāyaka'),('1975','state management'),('1982','devadāsī ban')],560,150)),
 ['<b>1514.</b> The present temple was built in 1514 by <b>Bomappa Nāyaka of Raybag</b>.',
  '<b>Before him.</b> Archaeological evidence points to a temple on the site between the mid-8th and mid-11th centuries, in the early Rāṣṭrakūṭa or late Cāḷukya period.',
  '<b>Style.</b> The temple follows Cāḷukya and Rāṣṭrakūṭa styles: sanctum, antechamber and a large hall. Some sources note a Jain inscription referring to Rāṣṭrakūṭa kings.',
  '<b>1975.</b> The Government of Karnataka took over management, providing free rest houses and health centres for pilgrims.',
  '<b>A busy hill.</b> Hundreds come every day; lakhs on the great days.'],
 [('z','A Jain inscription in a Goddess temple?'),('b','The Deccan’s stones were reused and its faiths lived side by side. It is common in North Karnataka.')],'An old hill, <b>a 16th-century temple</b>.')
waters=reading('waters','THE SACRED WATERS','Tanks and the healing well',
 S('Pilgrims bathing in a stepped tank, a well, and three small pools',g(140,200,1,'<rect x="-100" y="-60" width="200" height="60" fill="#c9a36b"/><rect x="-80" y="-44" width="160" height="40" fill="#4aa3df"/>')+g(330,200,1,'<ellipse rx="40" ry="14" fill="#8a6a3a"/><ellipse rx="30" ry="9" fill="#4aa3df"/>')+T(330,218,'Jogaḷa Bhāvi',10)+''.join(g(440+k*40,200,.8,'<ellipse rx="16" ry="8" fill="#4aa3df"/>') for k in range(3))+T(480,218,'three kuṇḍas',10),'#eadcc0',225),
 ['<b>At the foot.</b> At the bottom of the hill pilgrims bathe in the <b>Yogarbāvi Satyammā kuṇḍa</b> before going up to worship.',
  '<b>Jogaḷa Bhāvi.</b> A well called <b>Jogaḷa Bhāvi</b> is believed to cure skin diseases.',
  '<b>Three kuṇḍas.</b> Behind the temple are three tanks: <b>Kuṅkuma kuṇḍa</b>, <b>Yoni kuṇḍa</b> and <b>Arihan kuṇḍa</b>, where devotees bathe and worship.',
  '<b>Paraśurāma Kṣetra.</b> Beside the temple is the place where Paraśurāma is believed to have done penance.',
  '<b>Why water.</b> In Reṇukā’s story everything turns on a pot of water. Her hill is full of it. (Interpretation.)'],
 [('z','A well that heals the skin?'),('b','So pilgrims believe, and they come in thousands to bathe. Faith and cool water both help.')],'A story of water, <b>a hill of waters</b>.')
nim=reading('nimmana','NEEM LEAVES','The vow of the neem',
 S('Pilgrims walking round a small temple holding neem twigs in their mouths',g(280,200,1,tulu_temple('#c0392b','#8e1f17'))+'<ellipse cx="280" cy="170" rx="220" ry="40" fill="none" stroke="#8a6a3a" stroke-width="2" stroke-dasharray="6 5"/>'+''.join(g(80+k*100,210,1,person(['#c0392b','#e0a800','#2a9d6f','#6a3d9a','#1d4f8a'][k]))+g(80+k*100,150,.6,neem()) for k in range(5)),'#f6e3e1',225),
 ['<b>Bevu.</b> Neem (bevu) is sacred to the Goddess across the Deccan; her devotees wear neem leaves and offer them.',
  '<b>The circling.</b> At the foot of the hill devotees perform <b>nimmana</b>, circling the Satyammā temple with neem leaves in their mouths; some also wear neem twigs on their clothes as a vow. (Practice varies.)',
  '<b>Why neem.</b> Neem is bitter, cooling and healing, the plant of mother goddesses who protect from disease. (Common belief.)',
  '<b>Vows.</b> Many come to fulfil a vow: for a child, for health, for a prayer answered.',
  '<b>The jōgatis.</b> Women devotees called jōgatis carry the Goddess’s image in a basket (jaga) on their heads and sing her songs. (Described here as a devotional tradition.)'],
 [('z','Leaves in the mouth?'),('b','A sign of humility before the Mother: you come silent and bitter-mouthed, and leave blessed.')],'Bitter leaves <b>for a healing mother</b>.')
full=reading('hunnime','THE GREAT FULL MOONS','Lakhs on the hill',
 S('A full moon over a hill crowded with pilgrims and carts','<rect width="560" height="210" fill="#20243a"/>'+g(480,40,1.4,moon())+g(280,200,2,mountain('#6a5a4a'))+g(280,110,.5,tulu_temple('#c0392b','#8e1f17'))+g(280,206,1,crowd(14,500,0,.42)),'#20243a',210),
 ['<b>Two great days.</b> Two full moons draw crowds of up to ten lakh each: <b>Bharata Hunnime</b> and <b>Banada Hunnime</b>.',
  '<b>Bharata Hunnime.</b> Commonly placed on the Māgha full moon (Jan–Feb); one source places it in Mārgaśira. (Sources differ.)',
  '<b>Banada Hunnime.</b> The Pauṣa full moon, day of Banaśaṅkarī too (see '+L('/temples-of-india/karnataka/banashankari/','Part 5')+'). (Sources differ on which moon is which.)',
  '<b>The jātre.</b> On the great days the Goddess’s image is taken out in procession and worshipped as Śakti; festivals run between about October and April.',
  '<b>From four states.</b> Carts, buses and tractors bring pilgrims from Karnataka, Maharashtra, Goa and Andhra Pradesh; many camp on the hill.'],
 [('z','Ten lakh on one hill?'),('b','So the counts say. The hill becomes a city for a few days.')],'A hill that becomes <b>a city for a full moon</b>.')
devad=reading('devadasi','THE DEVADĀSĪ CUSTOM','A history, and its end',
 S('A government building with a document and a temple in the background',g(380,200,1.2,tulu_temple('#c0392b','#8e1f17'))+g(150,200,1,'<rect x="-50" y="-60" width="100" height="60" fill="#e9d6c0"/><path d="M-40 -46 h80 M-40 -34 h80 M-40 -22 h60" stroke-width="1.5"/>')+T(150,214,'1982 Act',10),'#e3eaf3',215),
 ['<b>What it was.</b> Yellamma’s temple was long associated with the custom of <b>dedicating girls to the Goddess</b> as devadāsīs. Over time the custom came to mean exploitation and poverty for many of the women and girls dedicated.',
  '<b>Abolished.</b> The Government of Karnataka prohibited the practice by the <b>Karnataka Devadasis (Prohibition of Dedication) Act, 1982</b>.',
  '<b>Today.</b> Dedication is illegal; the state and voluntary groups have worked on rehabilitation of former devadāsīs and on preventing dedications.',
  '<b>Not the Goddess’s doing.</b> Devotees and reformers alike stress that the abuse of a custom is not the faith itself; the jātre is about the Mother’s power, not about any harm to her daughters.',
  '<b>Why we say this plainly.</b> A reference guide that skipped it would be dishonest.'],
 [('z','Is the practice gone?'),('b','It is banned, and much reduced. Reports of rare illegal dedications still surface and are prosecuted. The law is clear.')],'A hard history <b>ended by law</b>.')
devot=reading('devotees','HER CHILDREN','Everyone who comes',
 S('A diverse crowd of devotees: farmers, women with baskets on heads, families',''.join(g(60+k*70,200,1.1,person(['#c0392b','#e0a800','#2a9d6f','#6a3d9a','#1d4f8a','#ff8c1a','#8e1f17'][k])) for k in range(7))+g(130,110,.8,'<ellipse rx="20" ry="8" fill="#c98a5a"/>')+g(340,110,.8,'<ellipse rx="20" ry="8" fill="#c98a5a"/>'),'#f6e3e1',215),
 ['<b>The poor and the farmer.</b> Yellamma is above all a goddess of the rural Deccan; her pilgrims are farmers, labourers and their families.',
  '<b>Transgender devotees.</b> The temple is associated with transgender devotees (jōgappas), who are held to be among Reṇukā’s children and are a visible presence at the temple.',
  '<b>Women.</b> Women carry her songs and her image; the jātre is described as a celebration of women’s power in the form of Śakti.',
  '<b>Four states.</b> She is worshipped across Karnataka, Maharashtra (as Reṇukā of Māhūr and others), Goa and the Telugu lands.',
  '<b>Read more.</b> Reṇukā’s son is in '+L('/vishnu/dashavatara/','Paraśurāma, Daśāvatāra')+'.'],
 [('z','A goddess for those others turned away?'),('b','That is how many describe her: the Mother of everyone who has nowhere else to go.')],'The Mother of <b>those with nowhere else to go</b>.')
endp=end(i,['<b>Goddess.</b> Reṇukā, called Yellamma, “mother of all”, mother of Paraśurāma.','<b>Story.</b> The unbaked pot, the command, the axe, and the mother restored.','<b>Hill.</b> Yallammanagudda over the Malaprabhā; temple of 1514 on far older ground.','<b>Rites.</b> Sacred tanks, the healing well, neem leaves, the great full moons.','<b>History.</b> The devadāsī custom, banned in 1982.'],
 'Part 4 goes to Gāṇagāpura on the Bhīmā, the seat of the Guru Dattātreya.','The Mother on the hill')
src=sources([('Temple:','Wikipedia, “Yellamma Temple, Saundatti” (location, hill, 1514, earlier temple and megaliths, deity and names, legends, shrines, tanks, state management, devadāsī prohibition 1982, transgender devotees); Wikipedia, “Renuka” and “Parasgad”; Incredible India; Karnataka.com (Mārgaśira jātre, Jain inscription, devadāsī ban); festivalsofindia.in (Bharata and Banada Hunnime, Jogaḷa Bhāvi); CPREEC eco-heritage (crowds over ten lakh).')],
 'the months of Bharata and Banada Hunnime (sources disagree); the meaning of “Yellamma”; the neem-leaf customs and their regulation are described generally; the jōgati tradition is described generally.','Legend as commonly told; Purāṇic tellings differ.')
finish(i,'PART 3 OF 5 · REṆUKĀ · THE HILL · NEEM',covart('A dark-faced Goddess on a hill over a river with neem leaves',g(220,190,1.7,mountain('#b08a62'))+g(220,120,.8,devi(skin='#5a3a2a',sari='#c0392b',items=('trident',))) +g(70,190,1.3,neem())+g(370,190,1.3,neem())),'The Mother on the hill',
 'Reṇukā <b>Yellamma</b> of Savadatti: her hard <b>story</b>, the hill and its <b>waters</b>, neem vows, the <b>great full moons</b>, and the devadāsī custom and its end.',
 'Savadatti Yellamma temple explained and illustrated: Reṇukā, Jamadagni and Paraśurāma, Yallammanagudda over the Malaprabhā, the temple of 1514 and its older past, sacred tanks and Jogaḷa Bhāvi, neem vows, Bharata and Banada Hunnime, devotees and the abolition of the devadāsī custom.',
 [fw,gl,where,ren,godd,hist,waters,nim,full,devad,devot,endp,src])
