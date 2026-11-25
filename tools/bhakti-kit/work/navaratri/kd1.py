from kd_common import *
i=0
def kmap():
    o='<rect width="560" height="240" fill="#d8e8c8"/>'+hills(560,90,'#7aa86a')
    o+='<path d="M120 60 C200 120 300 140 360 200 S500 220 560 230" fill="none" stroke="#4aa3df" stroke-width="7"/>'+T(470,236,'Kāverī',10,fill='#1d4f8a')
    for t,x,y in [('Talakāverī · Bhāgamaṇḍala',120,60),('Madikeri',260,110),('Pāḍi · Kakkabe',170,150),('Virājpēṭe',250,190),('Somavārpēṭe',380,90),('Kuśālanagar',420,170),('Brahmagiri',130,220)]: o+=pin(x,y,t,.35)
    return o+T(480,18,'simplified, not to scale',9)
fw=foreword(i,['High in the Western Ghats, where mist sits on the coffee and the Kāverī is born from a small spring, live the <b>Kodavas</b>: a people of farmers and soldiers who worship their river as mother, their ancestors as guardians and their guns as sacred, and who gather in great ancestral houses for festivals the rest of India barely knows.',
 'This twelve-part series is a reference to <b>Kodagu’s culture and festivals</b>. This first part introduces the land, the people and their language, the clans and ancestral houses, the dress, the martial tradition, the faith, the history, the food and even the hockey. The parts that follow take one subject each.',
 'Kodagu sits beside '+L('/tulunadu/','Tulu Nadu')+' under '+L('/karnataka-cultures/','Karnataka Cultures')+'. The Kāverī’s course below Kodagu runs through '+L('/temples-of-india/triranga/','the Triraṅga')+' and '+L('/temples-of-india/around-mysuru/','the temples around Mysuru')+'.'],
 [('z','Is Kodagu the same as Coorg?'),('b','Same place. Coorg is the old English form of Kodagu.')])
gl=glance([('Who','The Kodavas (Coorgs), a Dravidian people of Kodagu district, Karnataka'),('Number','About 1.5 to 1.6 lakh by estimates'),('Language','Kodava takk; a script by Dr. I. M. Muthanna adopted in 2022'),('Society','Patrilineal clans (okka) centred on ancestral houses (ainmane)'),('Ancestor','The guru kāraṇa, honoured at the kaimaḍa'),('Mother','The river Kāverī, their kuladēvī'),('Chief god','Igguthappa, god of rain and rice, at Pāḍi'),('Great festivals','Kailpoḷd, Kāverī Saṅkramaṇa, Puttari'),('Known for','Martial tradition, coffee, hockey, a distinctive dress'),('Joined Karnataka','1956 (then Mysore State)')],
 S('A Kodava couple in traditional dress before an ancestral house among misty hills with coffee',hills(560,110,'#5a9a5a')+g(280,210,1.2,ainmane())+g(110,210,1.2,kodava_man())+g(160,210,1.2,kodava_woman())+g(460,200,1,coffee())+g(500,200,1,coffee()),'#d8e8f0',215),
 [('z','How old is the community?'),('b','Historians agree the Kodavas have lived in Kodagu a very long time, probably among its earliest settled farmers.')],'Farmers, soldiers <b>and children of the Kāverī</b>.')
land=reading('land','THE LAND','Kodagu in the Western Ghats',svg(560,240,'Simplified map of Kodagu with Talakāverī, Madikeri, Pāḍi, Virājpēṭe, Somavārpēṭe, Kuśālanagar and the Kāverī',kmap()),
 ['<b>Hills.</b> Kodagu is a hill district of Karnataka in the Western Ghats, west of Mysuru, bordering Kerala. Its slopes are forest and coffee; its valley floors were paddy.',
  '<b>The Kāverī.</b> The river rises at <b>Talakāverī</b> on the Brahmagiri hills and flows east through Kodagu toward Mysuru and Tamil Nadu (see '+L('/kodagu/kaveri-sankramana/','Part 4')+').',
  '<b>Towns.</b> Madikeri (Mercara) is the headquarters; Virājpēṭe, Somavārpēṭe and Kuśālanagar are the other main towns.',
  '<b>Rain and mist.</b> Heavy monsoon rains, misty winters; one explanation of the name links it to mist or hills.',
  '<b>Nāḍ.</b> Villages are grouped in clusters called <b>nāḍ</b>, each with its village green (mand).'],
 [('z','Why is the coffee everywhere?'),('b','Coffee came to these hills centuries ago and transformed them in the 19th and 20th. Kodagu is now one of India’s great coffee districts.')],'Mist, coffee, <b>and a river’s birthplace</b>.')
name=reading('origins','NAME AND ORIGINS','Where the Kodavas come from',
 S('A moon-dynasty warrior and a scroll beside misty hills',hills(560,130,'#7aa86a')+g(160,200,1.4,kodava_man())+g(160,110,.8,moon())+g(380,180,1.2,'<rect x="-40" y="-50" width="80" height="50" fill="#fff8e7"/><path d="M-30 -36 h60 M-30 -24 h60 M-30 -12 h40" stroke-width="1.5"/>'),'#d8e8f0',215),
 ['<b>The legend.</b> A Purāṇic account, found in a Kāverī Purāṇa section of the Skanda Purāṇa, traces the Kodavas to <b>Candravarma</b>, a warrior of the lunar line who became the first king of Kodagu. (Legend.)',
  '<b>The historians.</b> Historians generally agree the Kodavas have lived in Kodagu for a very long time, probably among its earliest settled farmers.',
  '<b>Other theories.</b> Popular theories link them with distant peoples; these are not supported by mainstream history, and we leave them aside. (Neutral note.)',
  '<b>The name.</b> The meaning of “Kodava” and “Kodagu” is debated: links have been proposed with words for mist, hills or the west. (Sources differ.)',
  '<b>A distinct people.</b> Whatever their origin, the Kodavas have a distinct language, dress, clan system and festival calendar.'],
 [('z','Which origin is true?'),('b','The long settlement in Kodagu is the one thing all serious accounts agree on. The rest is legend and debate.')],'Long rooted <b>in their hills</b>.')
lang=reading('language','KODAVA TAKK','The language',
 S('A slate with a few letters and a village elder speaking to children',g(150,210,1.3,kodava_man('#f4f1ea'))+g(260,210,.9,person('#e0a800',seat=True))+g(310,210,.9,person('#c0392b',seat=True))+g(450,180,1.4,'<rect x="-50" y="-60" width="100" height="60" fill="#2a3a2a"/>'+txt(0,-28,'Kodava takk',12,fill='#fff',font=NS,weight='700')),'#fff3cf',215),
 ['<b>Takk.</b> The Kodava language, <b>Kodava takk</b> (“Kodava speech”), is a Dravidian language considered independent, with words borrowed from Kannaḍa and its neighbours.',
  '<b>Written.</b> Long written in the Kannaḍa script, it now also has a script devised by <b>Dr. I. M. Muthanna</b>, officially adopted in 2022.',
  '<b>Songs.</b> Much of Kodava tradition lives in songs: the pāṭṭs sung at festivals, weddings and in the fields.',
  '<b>Shared.</b> Several other communities of Kodagu also speak Kodava takk at home (see '+L('/kodagu/communities/','Part 12')+').',
  '<b>Words in this series.</b> We write Kodava terms in simple romanisation with marks; spellings vary between families.'],
 [('z','Is it a dialect of Kannaḍa?'),('b','No, its own Dravidian language, though neighbours for centuries.')],'A language <b>of song and the hills</b>.')
okka=reading('okka','OKKA AND AINMANE','Clan and house',
 S('A family tree branching from an ancestral house',g(280,210,1.4,ainmane())+''.join(f'<path d="M280 140 L{80+k*100} 60" stroke="#8a6a3a" stroke-width="3"/>'+g(80+k*100,60,.6,person(['#c0392b','#1d4f8a','#2a9d6f','#e0a800','#6a3d9a'][k])) for k in range(5)),'#fff3cf',215),
 ['<b>Okka.</b> Kodava society is built on the <b>okka</b>, the patrilineal clan: everyone bears the clan name before their own (as in K. M. Cariappa, of the Kodandera okka).',
  '<b>Ainmane.</b> Each okka has an <b>ainmane</b>, the ancestral house, the focus of family life, festivals and rites (see '+L('/kodagu/ainmane/','Part 7')+').',
  '<b>Land.</b> Settlements are spread across family farms and forest land; the historic <b>jamma</b> tenure, held mostly by Kodavas, kept estates largely intact.',
  '<b>Endogamous.</b> The community marries within itself, between different okkas.',
  '<b>Elders.</b> The head of the house, the <b>paṭṭedāra</b>, leads its rites, as at Puttari.'],
 [('z','Clan name first?'),('b','Always. You are your okka before you are yourself.')],'You are your clan <b>before yourself</b>.')
guru=reading('guru-karana','THE GURU KĀRAṆA','The ancestor at the head of the family',
 S('A small shrine for the ancestor beside an ancestral house, with a lamp and offerings',g(380,210,1.2,ainmane(160))+g(130,210,1.2,'<rect x="-30" y="-50" width="60" height="50" fill="#e9d6c0"/><path d="M-36 -50 l36 -24 l36 24z" fill="#7a3b1f"/>'+g(0,-10,.6,lamp()))+T(130,226,'kaimaḍa',10),'#fff3cf',230),
 ['<b>The founder.</b> Each family reveres its <b>guru kāraṇa</b>, the common ancestor at the head of the line.',
  '<b>Kaimaḍa.</b> He is honoured at a small family shrine, the <b>kaimaḍa</b>, with annual offerings.',
  '<b>The ancestors as guardians.</b> Kodava faith gives the ancestors a place close to the gods: they guard the family that remembers them.',
  '<b>At every festival.</b> Puttari and the other festivals begin with prayers to the ancestors at the ainmane.',
  '<b>Read more.</b> Ancestor rites, the kaimaḍa and the lamp are in '+L('/kodagu/ainmane/','The Ainmane')+'.'],
 [('z','Worshipping an ancestor?'),('b','Remembering and honouring him, asking his protection. In Kodagu the family is a sacred thing.')],'The family’s founder <b>as its guardian</b>.')
dress=reading('dress','KUPYA AND SĀRI','The Kodava dress',
 S('A man in a black kupya with red-gold sash and knife, and a woman in a sari pleated at the back with the end pinned at the shoulder',g(180,220,2,kodava_man())+g(380,220,2,kodava_woman('#c0392b')),'#fff3cf',230),
 ['<b>Kupya.</b> Men wore the <b>kupya</b>, a long wrap-around robe, usually black, tied at the waist with a red and gold sash (cele); today it is mostly worn at ceremonies and weddings.',
  '<b>Knives.</b> In the sash they carry ceremonial knives: the <b>pīcce katti</b> (a dagger) and the <b>oḍi katti</b>, a broad war-knife.',
  '<b>Turban.</b> A white or red turban (manḍe tuṇi) completes the dress.',
  '<b>The sari.</b> Kodava women wear the sari in their own style: the pleats at the <b>back</b> and the loose end brought over and pinned at the <b>right shoulder</b>.',
  '<b>Its legend.</b> Tradition links the sari style to the Kāverī (see '+L('/kodagu/kaveri-sankramana/','Part 4')+').'],
 [('z','Why pleats at the back?'),('b','There is a legend about the river pushing them back as she rushed away. We tell it in Part 4.')],'A dress <b>known at a glance</b>.')
mart=reading('martial','A MARTIAL PEOPLE','Soldiers and the gun',
 S('A row of Kodava men in uniform and in kupyas, a gun with a flower in its muzzle',''.join(g(80+k*80,210,1.2,kodava_man(['#3a5a3a','#1b1b1b','#3a5a3a','#1b1b1b'][k])) for k in range(4))+g(440,180,1.4,gun(60))+g(500,166,.6,lotus('#e05050','#8e1f17')),'#e3eaf3',215),
 ['<b>Soldiers.</b> The Kodavas have a strong military reputation. <b>Field Marshal K. M. Cariappa</b> and <b>General K. S. Thimayya</b> are among the best known of many who served.',
  '<b>The gun.</b> Kodavas are reported to be the only community in India allowed to keep firearms without a licence, an exemption dating from British-era arms laws. (As reported; the exemption has been debated in court.)',
  '<b>Sacred weapons.</b> Weapons are worshipped at Kailpoḷd, the festival of arms (see '+L('/kodagu/kailpodh/','Part 3')+').',
  '<b>Salutes.</b> Guns are fired at Puttari, at weddings and at funerals: salutes, not threats.',
  '<b>A culture of honour.</b> Courage and loyalty are the core of Kodava ideals.'],
 [('z','Is the gun a weapon or a symbol?'),('b','Today mostly a symbol and a farm tool against wild animals. At festivals, a sacred object.')],'A people <b>of soldiers and salutes</b>.')
faith=reading('faith','RIVER, GODS AND GROVES','The Kodava faith',
 S('A river spring with a small shrine, a god holding a pot of rain, and a sacred grove',g(120,210,1.1,'<ellipse rx="50" ry="14" fill="#4aa3df"/>'+g(0,-14,.5,devi(sari='#4aa3df',items=('pot',))))+g(300,210,1.2,god('#2a9d6f'))+g(470,210,1.6,tree('#2f6a3a'))+g(430,210,1.2,tree('#3a8a4a'))+T(120,226,'Kāverī',10)+T(300,226,'Igguthappa',10)+T(450,226,'dēvarakāḍu',10),'#d8e8f0',230),
 ['<b>Kāverī Amma.</b> The river <b>Kāverī</b> is the Kodavas’ kuladēvī, their patron mother.',
  '<b>Igguthappa.</b> <b>Igguthappa</b>, god of rain, rice and snakes, is the chief deity, at Pāḍi near Kakkabe.',
  '<b>Ancestors.</b> Ancestors are revered and called on at every rite.',
  '<b>Sacred groves.</b> <b>Dēvarakāḍu</b>, “god’s forests”, are sacred groves protected from felling and hunting, attached to village deities.',
  '<b>Weapons and nature.</b> The Kodava faith reveres ancestors, nature and weapons together, alongside the gods of the wider Hindu world: Śiva, Bhagavatī, Aiyappa.'],
 [('z','Why is the river a mother?'),('b','She rises in their hills and feeds their fields. A river that gives life is a mother everywhere in India; here she is family.')],'River, rain, ancestors <b>and the forest</b>.')
hist=reading('history','HISTORY','From the Gaṅgas to Karnataka',
 svg(560,150,'Timeline of Kodagu’s history','<rect width="560" height="150" fill="#fff3cf"/>'+tl_strip([('early','Gaṅgas'),('medieval','Hoysaḷas'),('16th c.','Vijayanagara'),('c. 1600','Hāleri Rājas'),('1834','annexed'),('1956','Mysore State')],560,150)),
 ['<b>Early rulers.</b> Kodagu was ruled at various times by the Gaṅgas, the Hoysaḷas and the Vijayanagara empire.',
  '<b>The Hāleri Rājas.</b> From about 1600 the Hāleri dynasty, Liṅgāyat rājas, ruled Kodagu from Madikeri.',
  '<b>1834.</b> The East India Company annexed Kodagu after a short, bloody campaign. It was later a separate province, Coorg State.',
  '<b>1956.</b> Coorg was merged into Mysore State, now Karnataka.',
  '<b>Coffee.</b> Coffee, introduced centuries ago, transformed Kodagu’s economy in the 19th and 20th centuries.'],
 [('z','Kodagu was once its own state?'),('b','Until 1956. Many Kodavas still feel a strong separate identity.')],'A small land <b>with a long history</b>.')
food=cards('food','KODAVA FOOD','Rice, pork and kachampuli',
 fig_row('Steamed rice balls, a pot of dark pork curry, a bottle of kachampuli and a sweet',[('<circle r="14" fill="#f4f1ea"/><circle cx="20" r="14" fill="#f4f1ea"/>',1.2),(pot(),1.2) if False else ('<path d="M-20 0 h40 l-6 -26 h-28z" fill="#5a3a1a"/><ellipse cy="-26" rx="16" ry="5" fill="#3a1a0a"/>',1.3),('<rect x="-8" y="-40" width="16" height="40" fill="#3a1a0a"/>',1.2),(plate()+'<ellipse cy="-8" rx="18" ry="8" fill="#c98a5a"/>',1.3),(coffee(),1.4)],['kaḍambuṭṭ','pandi curry','kachampuli','tambuṭṭ','coffee'],gy=150),
 [('🍚','Rice','Boiled rice is the staple of Kodagu.'),('🍛','Pandi curry','A deep brown pork curry soured with <b>kachampuli</b>, the vinegar of the Garcinia fruit.'),('⚪','Kaḍambuṭṭ','Steamed rice balls, the classic partner of pandi curry.'),('🍮','Tambuṭṭ','The banana and rice-flour sweet of Puttari.'),('🥣','Akki pāyasa','A rice sweet.'),('☕','Coffee','From the district’s own estates.')],
 None,'Rice, pork and kachampuli: <b>Kodagu on a plate</b>.',
 intro='Kodava cooking is a cuisine of rice, forest greens, pork and the sour kachampuli. More in '+L('/kodagu/kodava-year/','The Kodava Year and Its Food')+'.')
hockey=reading('hockey','THE HOCKEY FESTIVAL','A family tournament like no other',
 S('Teams of players with hockey sticks on a field, family banners on the side',g(280,200,1,'<rect x="-260" y="-80" width="520" height="80" fill="#4a8a4a"/><path d="M0 -80 v80" stroke="#fff" stroke-width="2"/>')+''.join(g(80+k*100,195,1,person(['#c0392b','#1d4f8a','#c0392b','#1d4f8a','#c0392b'][k]))+f'<path d="M{90+k*100} 160 l14 30 h8" stroke="#5a3a1a" stroke-width="3" fill="none"/>' for k in range(5)),'#d8e8c8',210),
 ['<b>A cradle of hockey.</b> Kodagu is often called a cradle of Indian field hockey.',
  '<b>Family teams.</b> The annual <b>Kodava Hockey Festival</b> is played between teams of families (okkas): hundreds of family teams take part.',
  '<b>A festival of the clans.</b> It brings the okkas together as the old festivals do, on a hockey field.',
  '<b>Sportspeople.</b> The community has produced athletes in hockey, cricket, tennis, athletics and motor racing.',
  '<b>Why here.</b> A martial tradition, a love of the outdoors and a strong family structure. (Common explanation.)'],
 [('z','A tournament of families?'),('b','Grandfathers, uncles, nephews on one team, all with the same clan name on their shirts.')],'Clans <b>on a hockey field</b>.')
series=cards('series','THIS SERIES','Twelve parts on Kodagu',
 S('Twelve small icons in a row: rice, gun, river, god, sticks, house, rings, goddess, temple, calendar, people',''.join(g(30+k*46,140,.6,[paddy(3,20,30),gun(40),'<ellipse rx="16" ry="6" fill="#4aa3df"/>',god('#2a9d6f'),'<path d="M-10 0 l20 -30 M10 0 l-20 -30" stroke="#8a6a3a" stroke-width="4"/>',ainmane(60),'<circle r="10" fill="none" stroke="#e0a800" stroke-width="4"/>',devi(items=()),tulu_temple(),'<rect x="-14" y="-20" width="28" height="20" fill="#fff8e7"/>',person('#1d4f8a'),kodava_man()][k]) for k in range(12)),'#fff3cf',170),
 [('1','The Kodavas','This page.'),('2','Puttari','The festival of new rice. '+L('/kodagu/puttari/','Read')),('3','Kailpoḷd','The festival of arms. '+L('/kodagu/kailpodh/','Read')),('4','Kāverī Saṅkramaṇa','The river rises at Talakāverī. '+L('/kodagu/kaveri-sankramana/','Read')),('5','Igguthappa','The god of rain and rice. '+L('/kodagu/igguthappa/','Read')),('6','Mand and dances','The village green. '+L('/kodagu/mand-and-dances/','Read')),('7','The ainmane','House and lamp. '+L('/kodagu/ainmane/','Read')),('8','Life rites','Birth, marriage, death. '+L('/kodagu/life-rites/','Read')),('9','Village deities','Bhagavatī and the kōlas. '+L('/kodagu/village-deities/','Read')),('10','Temples','Omkāreśvara, Bhāgamaṇḍala and more. '+L('/kodagu/temples/','Read')),('11','Year and food','Months and dishes. '+L('/kodagu/kodava-year/','Read')),('12','Communities','Gowdas, Airis and others. '+L('/kodagu/communities/','Read'))],
 None,'Twelve doors <b>into Kodagu</b>.')
endp=end(i,['<b>People.</b> The Kodavas, a Dravidian people of the Kodagu hills, speakers of Kodava takk.','<b>Family.</b> Clans (okka), ancestral houses (ainmane) and the founding ancestor (guru kāraṇa).','<b>Faith.</b> Kāverī the mother, Igguthappa the rain-god, the ancestors and the groves.','<b>Ways.</b> The kupya and the back-pleated sari, the gun, soldiers and hockey.','<b>Year.</b> Kailpoḷd, Kāverī Saṅkramaṇa and Puttari.'],
 'Part 2 is Puttari, the festival of new rice.','Children of the Kāverī')
src=sources([('People:','Wikipedia, “Kodava people” (identity, population, language and script, origins, okka, ainmane, guru kāraṇa and kaimaḍa, jamma tenure, dress, martial tradition and arms exemption, faith, festivals, history, coffee, cuisine, hockey); Deccan Herald on the mands and nāḍs.')],
 'origin theories are summarised neutrally; the arms exemption is “as reported”; the sari legend is told in Part 4 as tradition.','Kodava terms in simple romanisation.')
finish(i,'PART 1 OF 12 · THE LAND · THE CLANS · THE KĀVERĪ',covart('A Kodava man and woman in traditional dress before an ancestral house in misty hills with coffee',hills(440,100,'#5a9a5a')+g(220,190,1,ainmane(160))+g(80,190,1.1,kodava_man())+g(130,190,1.1,kodava_woman())+g(380,180,1,coffee())),'Children of the Kāverī',
 'The <b>Kodavas</b> of Kodagu: the land, the language, the <b>clans and ancestral houses</b>, the dress, the <b>martial tradition</b>, the faith, the history and the food.',
 'The Kodavas of Kodagu (Coorg) explained and illustrated: land and language, okka clans and the ainmane, the guru kāraṇa, the kupya and Kodava sari, the martial tradition, Kāverī and Igguthappa, history, food and the Kodava Hockey Festival; overview of a 12-part series.',
 [fw,gl,land,name,lang,okka,guru,dress,mart,faith,hist,food,hockey,series,endp,src])
