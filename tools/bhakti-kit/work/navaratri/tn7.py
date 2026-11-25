from tn_common import *
i=6
def couple(c1='#c0392b',c2='#1d4f8a'): return g(-14,0,1,person(c1))+g(14,0,1,person(c2))
def cane_pair(): return g(-6,0,1,sugarcane(70))+g(6,0,1,sugarcane(66))
def kmap():
    o=map_frame()+'<path d="M90 60 q120 10 200 -10" fill="none" stroke="#8fb8de" stroke-width="10"/>'+T(220,40,'Pañcagaṅgāvaḷi',9,fill='#1d4f8a')
    o+=pin(250,70,'Kundāpura')+pin(330,30,'Basrūr (old port)')+pin(240,140,'Kōṭeśvara')+'<rect x="290" y="130" width="50" height="30" fill="#4aa3df"/>'+T(316,176,'Kōṭi Tīrtha',9)
    o+=pin(200,200,'Kumbhāśi')+pin(420,120,'Śaṅkaranārāyaṇa')+pin(140,100,'Koḍi beach',.3)
    return o
fw=foreword(i,['For a few days every November or December, the roads into a small town south of Kundāpura disappear behind walls of sugarcane. Newly married couples in their wedding silks bathe in a great tank, circle it, worship Śiva together, and go home carrying a pair of canes. A king once vowed a temple here for the gift of children; when his chariot was not ready, his people made one of bamboo and sugarcane.',
 'This is the <b>Koḍi Habba</b> of Kōṭeśvara, “the fair of the newly-weds”. This guide covers the Lord of a crore, King Vasu’s vow, the great tank and its rites, the chariot, the couples and their sugarcane, and the fair.',
 'The temple is in '+L('/tulunadu/temples/koteshwara-kotilingeshwara/','Kōṭeśvara Kōṭiliṅgeśvara')+'. Previous: '+L('/tulunadu/festivals/katil-festivals/','Kaṭīl festivals')+'.'],
 [('z','A festival for newly-weds?'),('b','For newly-weds, and for everyone who remembers being one. Every couple of the area seems to have a Koḍi Habba photo.')])
gl=glance([('Where','Śrī Mahatōbhāra Kōṭiliṅgeśvara temple, Kōṭeśvara, Kundāpura taluk, Uḍupi district'),('Deity','Śiva as Kōṭiliṅgeśvara, “Lord of a crore of liṅgas”'),('When','Every year in the solar month of Vṛścika (November–December)'),('Story','King Vasu of Basrūr’s vow for children; the sugarcane chariot'),('Heart of it','Newly married couples'),('Their rite','Bath at Kōṭi Tīrtha, circling the tank, worship, a pair of sugarcanes home'),('The chariot','The Brahmaratha drawn round the car street'),('The tank','Kōṭi Tīrtha, about four acres'),('Crowds','Lakhs from across coastal Karnataka'),('Group','One of the seven Muktisthalas of Paraśurāma’s coast')],
 S('A newly married couple carrying a pair of sugarcanes before a temple chariot',g(140,195,1.4,RATHA(0,0,1,'#c0392b'))+g(320,190,1.3,couple())+g(370,190,1,cane_pair())+''.join(g(440+k*16,190,.8,sugarcane(60)) for k in range(6)),'#e3eaf3',200),
 [('z','Is it only for couples?'),('b','No, the whole coast comes. But couples are its heart.')],'A Lord who blesses <b>new families</b>.')
place=reading('place','KŌṬEŚVARA','Near the meeting of river and sea',svg(560,230,'Simplified map: Kundāpura, Basrūr, Kōṭeśvara with its tank, Kumbhāśi and Śaṅkaranārāyaṇa',kmap()),
 ['<b>Where.</b> Kōṭeśvara lies on the coastal plain a few kilometres south of <b>Kundāpura</b>, a town surrounded by water on three sides where the Pañcagaṅgāvaḷi reaches the sea.',
  '<b>Basrūr.</b> Up the river lies the old port of <b>Basrūr</b>, whose rulers are linked with the temple by inscriptions and by the story of King Vasu.',
  '<b>A Muktisthala.</b> Kōṭeśvara is one of the seven sacred places of Paraśurāma’s coast, with Kumbhāśi and Śaṅkaranārāyaṇa nearby. See '+L('/temples-of-india/muktisthalas/','The Seven Muktisthalas')+'.',
  '<b>Old name.</b> The town was once called <b>Dhvajapura</b>, “the town of the banner”.',
  '<b>The name of the fair.</b> Explanations of “Koḍi” vary: some connect it with the flag (koḍi) hoisted to open the festival, recalling Dhvajapura. (Traditions differ.)'],
 [('z','Dhvajapura and a flag festival?'),('b','Two old names that both speak of banners. Whatever the origin, banners have never been short at Koḍi Habba.')],'A town of banners <b>by the river mouth</b>.')
lord=reading('lord','THE LORD OF A CRORE','Kōṭiliṅgeśvara',
 S('A liṅga with a silver face; beneath, a well with many small liṅgas under water',g(280,110,1.6,LINGA(0,0,1))+'<circle cx="280" cy="62" r="16" fill="#d8d8e0"/>'+'<rect x="180" y="130" width="200" height="60" fill="#4aa3df"/>'+''.join(g(196+k*18,186,.15,LINGA(0,0,1)) for k in range(10)),'#e3eaf3',200),
 ['<b>The name.</b> <b>Kōṭi</b> is a crore, ten million. Tradition says countless sages, a crore of them, did penance here, and Śiva appeared to every one: the place became Kōṭi-īśvara, Kōṭeśvara.',
  '<b>The liṅga.</b> Śiva is worshipped as a liṅga dressed with a silver face of the Lord.',
  '<b>The hidden liṅgas.</b> Below the pedestal, it is said, lies a well holding about a thousand small liṅgas under water.',
  '<b>Brahmā.</b> Another tradition says Brahmā himself did penance here.',
  '<b>A blessing Lord.</b> He is the Lord who answered King Vasu’s prayer for children; couples come to him for the same blessing.'],
 [('z','You can’t see the thousand liṅgas?'),('b','No. You worship one, and by faith you worship them all.')],'One Lord who appears <b>to everyone at once</b>.')
shr=cards('temple','THE TEMPLE','Shrines the couples visit',
 S('A coastal temple with sloping tiled roofs and a stone Nandi before it',g(320,190,1.6,tulu_temple('#a0522d','#7a3b1f',160))+g(130,190,1.2,'<ellipse cx="0" cy="-20" rx="34" ry="20" fill="#8a8f9a"/><circle cx="30" cy="-36" r="12" fill="#8a8f9a"/><path d="M24 -48 l-4 -10 M36 -48 l4 -10" stroke-width="3"/>')+T(130,205,'Nandi',10),'#e3eaf3',210),
 [('🔱','Kōṭiliṅgeśvara','The liṅga with the silver face, over the well of liṅgas.'),('🐂','Nandi','A great stone bull facing the sanctum.'),('🐍','Subrahmaṇya','Śiva’s son, honoured with the nāgas.'),('🐘','Gaṇapati','The remover of obstacles.'),('🪈','Gōpālakṛṣṇa','Kṛṣṇa as the cowherd boy.'),('🪔','Jyēṣṭhālakṣmī','The elder sister of Lakṣmī, a rare shrine, worshipped to keep misfortune away.'),('🏹','Paṭṭābhirāma','Rāma crowned, in his own temple nearby.'),('🌾','Mārīyamma','The village Goddess, in a separate shrine.')],
 None,'A whole divine family <b>for the new family</b>.',
 intro='Kōṭeśvara is a classic coastal temple in the Kerala manner: sloping tiled roofs, carved woodwork and laterite walls.')
vasu=story('vasu','STORY · KING VASU’S VOW','The chariot of sugarcane',
 strip('Three panels: a king and queen praying before a liṅga; the king with a child; people building a chariot of bamboo and sugarcane',
  [('<rect width="144" height="190" fill="#fff3cf"/>'+g(40,170,.9,couple('#8e1f17','#e0a800'))+g(110,170,.5,LINGA(0,0,1)),'#fff3cf'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(60,170,.9,couple('#8e1f17','#e0a800'))+g(104,150,.6,'<circle r="10" fill="#c98a5a"/><path d="M-10 10 q10 20 20 0" fill="#f4f1ea"/>'),'#fff3cf'),
   ('<rect width="144" height="190" fill="#e9f2e1"/>'+''.join(g(30+k*16,170,.9,sugarcane(80)) for k in range(6))+'<path d="M24 100 h104 l-52 -40z" fill="#d8b878"/>','#e9f2e1')],
  ['the vow','the child','bamboo and cane']),'The story behind the Koḍi Habba, as told at the temple.',
 ['<b>Mahārāja Vasu</b>, a ruler of Basrūr, had no children for many years.',
  'He vowed to Kōṭiliṅgeśvara that if he were blessed with a child he would build the Lord a temple at Kōṭeśvara.',
  'Children were born to him, and he built the temple as he had promised.',
  'When the festival came, the temple chariot was not finished. Rather than let the Lord go without his procession, a chariot was made of <b>bamboo and sugarcane</b>, and the Lord was drawn round on it.',
  'The Koḍi Habba remembers that sugarcane chariot, and couples still come to the Lord who answered a king’s prayer for children.'],
 [('z','Did the sugarcane chariot hold up?'),('b','Long enough, says the story. Devotion was the real frame.')],'A king’s vow, <b>a chariot of cane</b>.')
tank_=reading('tirtha','KŌṬI TĪRTHA','The great tank',
 S('A large square tank with steps on all sides and a small pavilion in the middle; a couple circling it',g(280,180,1,'<rect x="-200" y="-110" width="400" height="110" fill="#c9a36b"/><rect x="-170" y="-90" width="340" height="80" fill="#4aa3df"/>'+g(0,-34,.6,'<rect x="-20" y="-30" width="40" height="30" fill="#e9d6c0"/><path d="M-26 -30 l26 -18 l26 18z" fill="#a0522d"/>'))+g(70,190,.9,couple()),'#e9f2e1',200),
 ['<b>The largest.</b> Beside the temple lies <b>Kōṭi Tīrtha</b>, a tank of about four acres, described as the largest temple tank (puṣkariṇī) in Karnataka.',
  '<b>Its shape.</b> Steps run down on all four sides to the water, with a small maṇḍapa in the middle. Fish swim in it.',
  '<b>Its power.</b> Its water is believed to heal.',
  '<b>At the festival.</b> Devotees, and especially couples, bathe in its waters and walk round it in the rite known locally as <b>suttakki sēve</b> before going into the temple.',
  '<b>A tunnel tale.</b> Local legend says an underground passage runs from the tank to Vaṇḍāru Kambaḷa Gadde, a race field some twenty kilometres away.'],
 [('z','Why walk round the tank?'),('b','Circling is how you honour anything sacred on this coast: a deity, a tree, a tank. You keep it on your right and go round.')],'A bath and a circle <b>before the Lord</b>.')
couples=reading('couples','THE NEWLY-WEDS','The heart of the fair',
 S('Several couples in wedding clothes, each carrying a pair of sugarcanes, walking toward the temple',''.join(g(70+k*120,190,1.1,couple(['#c0392b','#e0a800','#2a9d6f','#6a3d9a'][k],['#1d4f8a','#f4f1ea','#8e1f17','#e0a800'][k]))+g(110+k*120,190,.8,cane_pair()) for k in range(4)),'#fff3cf',200),
 ['<b>Who comes.</b> Couples married in the past year come from all over the coast, often in their wedding silks, sometimes with both families.',
  '<b>What they do.</b> They bathe at Kōṭi Tīrtha, circle it, worship Kōṭiliṅgeśvara together and watch the chariot.',
  '<b>The canes.</b> They take home a <b>pair of sugarcane</b> stalks, believed to bless them with healthy children, as the Lord blessed King Vasu.',
  '<b>Not only couples.</b> Many families buy canes too, as prasāda for the house.',
  '<b>A rite of the new household.</b> For many coastal couples, the Koḍi Habba is the first pilgrimage of married life. (Our observation.)'],
 [('z','Why do couples take home two sugarcanes, not one?'),('b','A pair for a pair! One for each of them, together, for the children they hope will come.')],'A pair of canes <b>for a new pair</b>.')
cane=reading('sugarcane','SUGARCANE EVERYWHERE','Walls of cane on every road',
 S('Stacks of sugarcane leaning against stalls along a road, with buyers',''.join(g(30+k*14,190,1,sugarcane(100-(k%3)*10)) for k in range(36))+g(280,196,1,crowd(6,260,0,.5)),'#e9f2e1',205),
 ['<b>The market.</b> In the days of the fair the roads into Kōṭeśvara are lined with stacks of sugarcane, brought in by growers and sellers from the region.',
  '<b>Bought in pairs.</b> Couples and families buy canes in pairs; the sight of thousands carrying cane home is the signature of the fair.',
  '<b>Why sugarcane.</b> It recalls the sugarcane chariot of King Vasu. Sugarcane is also an old sign of sweetness, fertility and plenty in Indian rites. (Interpretation.)',
  '<b>Kāma’s bow.</b> In the old poets, the god of love carries a bow of sugarcane; a fair of newly-weds with sugarcane fits well. (Interpretation.)',
  '<b>Season.</b> Vṛścika (Nov–Dec) is also when sugarcane is harvested in much of Karnataka.'],
 [('z','What do people do with all that cane?'),('b','Chew it, share it, offer it at the home shrine. Prasāda you can eat for a week.')],'The sweetest <b>reminder of an answered prayer</b>.')
ratha=reading('chariot','THE CHARIOT','The Brahmaratha on the car street',
 S('A great temple chariot drawn by a crowd on ropes, with drums and fireworks',g(320,195,1.8,RATHA(0,0,1,'#c0392b'))+'<path d="M260 180 L60 180" stroke="#8a6a3a" stroke-width="4"/>'+g(150,196,1,crowd(6,180,0,.5))+g(480,60,1,fireworks())+g(60,180,.9,drum()),'#e3eaf3',210),
 ['<b>The festival.</b> The Koḍi Habba opens with the hoisting of the temple flag and builds to the chariot day.',
  '<b>The Brahmaratha.</b> The festival image of Kōṭiliṅgeśvara is drawn round the car street on the great chariot by thousands of devotees.',
  '<b>Its company.</b> Folk dancers, drums, music and fireworks go with it.',
  '<b>Remembering Vasu.</b> Today’s chariot is wood; the festival remembers the day it had to be bamboo and cane. The bamboo chariot is described as the hallmark of the festival.',
  '<b>Rathōtsava.</b> On the coast a temple’s annual festival is often simply called its rathōtsava, its chariot festival. See also '+L('/tulunadu/festivals/udupi-festivals/','Uḍupi’s chariots')+'.'],
 [('z','How many pull the chariot?'),('b','As many as can reach a rope. Pulling is an offering; nobody wants to miss it.')],'Thousands of hands <b>on one rope</b>.')
fair=reading('fair','THE FAIR','A great fair of the coast',
 S('Fair stalls with toys, bangles and snacks, a giant wheel and crowds',''.join(g(60+k*90,190,.9,'<rect x="-36" y="-40" width="72" height="40" fill="#e9d6c0"/><path d="M-40 -40 l40 -20 l40 20z" fill="'+['#c0392b','#1d4f8a','#2a9d6f','#e0a800'][k]+'"/>') for k in range(4))+'<circle cx="460" cy="110" r="60" fill="none" stroke="#c0392b" stroke-width="3"/>'+g(280,200,1,crowd(10,520,0,.4)),'#fff3cf',205),
 ['<b>Lakhs.</b> The Koḍi Habba draws lakhs of people from across coastal Karnataka and beyond; it is counted among the most eagerly awaited fairs of the coast.',
  '<b>Stalls.</b> Sweets, toys, bangles, kitchenware, rides: the fair spreads through the town.',
  '<b>Seasonal.</b> It falls early in the coast’s festival season, after Dīpāvali, when the jātres and kōlas have just reopened (see '+L('/tulunadu/festivals/tulu-year/','The Tuḷu Year')+').',
  '<b>Other festivals.</b> Mahāśivarātri and Kārtika lamps are the temple’s other great days.',
  '<b>Around.</b> Pilgrims often go on to Kumbhāśi’s Ānegudde Vināyaka and to Śaṅkaranārāyaṇa.'],
 [('z','Is it noisy?'),('b','It’s a coastal fair. Very.')],'One of <b>the great fairs of the coast</b>.')
endp=end(i,['<b>Lord.</b> Kōṭiliṅgeśvara, who appeared to a crore of sages.','<b>Story.</b> King Vasu’s vow for children; the chariot of bamboo and sugarcane.','<b>Rite.</b> Bath and circling at Kōṭi Tīrtha, worship, a pair of canes home.','<b>Chariot.</b> The Brahmaratha drawn by thousands.','<b>Fair.</b> Lakhs of visitors in Vṛścika.'],
 'Part 8 goes to Bappanāḍu for its jātre and its great drums.','The fair of the newly-weds')
src=sources([('Kōṭeśvara:','Our '+L('/tulunadu/temples/koteshwara-kotilingeshwara/','Kōṭeśvara Kōṭiliṅgeśvara')+' guide; utsav.gov.in (Koḍi Habba, newly-weds, Vasu, bamboo chariot); Wikipedia, “Koteshwara”; Udupi Tourism (bamboo-and-bagasse chariot); Culture and Heritage (suttakki sēve, citing Daijiworld); Pilgrimaide; Tirthayatra (flag hoisting).')],
 'the meaning of “Koḍi” is not settled; the readings of sugarcane are ours; details of the order of rites at the tank vary by report.','Festival names as used locally.')
finish(i,'PART 7 OF 9 · NEWLY-WEDS · SUGARCANE · CHARIOT',covart('A newly married couple with a pair of sugarcanes before a chariot and a great tank',g(110,190,1.2,RATHA(0,0,1,'#c0392b'))+g(280,190,1.3,couple())+g(330,190,1,cane_pair())+''.join(g(370+k*12,190,.8,sugarcane(60)) for k in range(5))),'The fair of the newly-weds',
 'The <b>Koḍi Habba</b> of Kōṭeśvara: <b>King Vasu’s vow</b>, the great tank, the <b>newly-weds and their sugarcane</b>, the chariot and the fair.',
 'Koḍi Habba at Kōṭeśvara explained and illustrated: Kōṭiliṅgeśvara, King Vasu of Basrūr and the sugarcane chariot, Kōṭi Tīrtha and suttakki sēve, newly married couples and their pair of sugarcanes, the Brahmaratha and the fair.',
 [fw,gl,place,lord,shr,vasu,tank_,couples,cane,ratha,fair,endp,src])
