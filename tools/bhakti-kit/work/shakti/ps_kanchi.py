exec(open('/home/claude/work/shakti/ps_common.py').read())
head=head_navy('Ekāmbareśvara, Kāñcīpuram · Pañcabhūta Sthala of Earth · srini.presents',
 'Ekāmbareśvara temple, Kāñcīpuram: Śiva as the earth (Pṛthvī liṅga), Pārvatī’s sand liṅga under the mango tree, the Vegavatī flood and Kāmākṣī’s embrace, the four-branched mango tree, the 1509 Rāja Gopuram of Kṛṣṇadevarāya, the Divya Deśam inside a Śiva temple, the Tēvāram and Sundarar’s eye, and the Paṅkuṉi Uttiram wedding. An illustrated reference guide.')
def MANGO(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-8 0 v-60 h16 v60z" fill="#7a4a1a"/>'
 +''.join(f'<path d="M0 -50 L{dx} {dy}" stroke="#7a4a1a" stroke-width="7"/><circle cx="{dx}" cy="{dy}" r="26" fill="#3a8a3a"/>' for dx,dy in ((-44,-80),(-16,-100),(16,-100),(44,-80)))
 +''.join(f'<path d="M{a} {b} q6 -2 8 6 q-6 6 -8 -6z" fill="{c}"/>' for a,b,c in ((-50,-74,'#ffd23f'),(-20,-96,'#ffb03a'),(12,-92,'#9fcf3a'),(40,-74,'#f08a2a')))+'</g>')
def SANDLINGA(x,y,s=1): return LINGA(x,y,s,'#c9a26b','<circle cx="-6" cy="-40" r="1.6" fill="#7a5a2a" stroke="none"/><circle cx="6" cy="-30" r="1.6" fill="#7a5a2a" stroke="none"/><circle cx="0" cy="-48" r="1.6" fill="#7a5a2a" stroke="none"/>')
def KAMAKSHI(x,y,s=1): return GENTLE(x,y,s)
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Kamakshi embracing a sand linga under a four-branched mango tree, with a tall temple tower behind">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+GOPURAM(320,250,1.05,'#e8d8b0',9)+MANGO(130,236,1.05)+SANDLINGA(170,250,.9)+KAMAKSHI(110,206,.8)+'</svg>')
cov=cover('PAÑCABHŪTA 1 · EARTH','EKĀMBAREŚVARA',14,'Kāñcīpuram: Śiva as the earth',art)
fw=foreword('Om Namaḥ Śivāya,',[
 'The first of the five elements is the one under your feet. At <b>Kāñcīpuram</b> Śiva is worshipped as <b>earth</b>: a liṅga said to be shaped from sand by the Goddess herself, under a single mango tree. That tree gave him his name, <b>Ekāmbareśvara</b>, “Lord of the one mango tree”.',
 'When the river Vegavatī flooded, Kāmākṣī threw her arms around the sand liṅga to save it, and the marks of her bangles are still pointed out today. Above the temple rises one of the tallest towers of South India, built by Kṛṣṇadevarāya in 1509, and inside its walls stands, unusually, a shrine of Viṣṇu.',
 'This guide tells the stories, walks through the temple and explains why earth is the ground of all worship.'],
 'Can a liṅga really be made of sand?','That is the tradition here. It is why water is not poured over it as at other shrines.',
 series_note(prev=('overview','Overview'),nxt=('jambukeshvara','Jambukeśvara, Tiruvānaikkāval (water)')))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Element','<b>Earth</b> (Pṛthvī): the first of the Pañcabhūta Sthalas'),
 ('Śiva as','<b>Ekāmbareśvara</b> or Ekāmbaranātha, “Lord of the one mango tree”'),
 ('Liṅga','The <b>Pṛthvī liṅga</b>, by tradition of sand; not bathed with water'),
 ('Goddess','Kāmākṣī, worshipped as Ēlavārkuḻali; the great Kāmākṣī temple is nearby'),
 ('Tree','The sacred mango (sthala vṛkṣa), with four branches for the four Vedas'),
 ('Size','About 9 hectares (23 acres), five courtyards, a thousand-pillared hall'),
 ('Tower','The southern Rāja Gopuram, 11 storeys, about 57–59 m, built by Kṛṣṇadevarāya from 1509'),
 ('Also','Nilāttiṅgaḷ Tuṇḍam, a Divya Deśam of Viṣṇu, inside the temple')])
 +talk("The biggest temple in Kāñcī?","Yes, the largest in a city of a thousand temples. And its tower is among the tallest in the South.")))
pages.append(page('names','HIS NAMES','The one mango',facts([
 ('Ekāmbareśvara','<i>eka</i> “one” + <i>āmra</i> “mango” + <i>īśvara</i> “Lord”'),
 ('Ekāmbaranātha','The same name with <i>nātha</i>, “master”'),
 ('Tiruvēkampam','The Tamil name of the temple in the Tēvāram'),
 ('Pṛthvī liṅga','“Liṅga of earth”: his element'),
 ('Ēlavārkuḻali','“She of the fragrant tresses”: the Goddess here'),
 ('Kampā','The river of the story, today a small stream; also called Vegavatī in the tellings')])
 +talk("Why name a god after a tree?","Because he appeared under it. The tree is the place where she prayed and he came.")))
pages.append(page('dark','THE DARKENED WORLD','Why Pārvatī came to earth',fig(560,170,'Parvati playfully covering Shiva\'s eyes on Kailasa while the whole world goes dark',
 '<rect width="560" height="170" fill="#1d1d2a"/><path d="M0 170 L120 60 L200 110 L300 30 L420 120 L560 50 V170Z" fill="#3a3a5a" stroke="#111" stroke-width="2"/>'+SHIVA(300,90,.8)+GENTLE(250,100,.7)+'<path d="M266 70 l18 2" stroke="#f2c79b" stroke-width="6"/>')+'''<div class="steps">
<div><b>A game.</b> On Kailāsa, Pārvatī playfully covered Śiva’s eyes with her hands.</div>
<div><b>Darkness.</b> His eyes are the sun and moon: the whole world went dark, and all creatures suffered for what was, to the gods, a moment.</div>
<div><b>Penance.</b> To make amends, Pārvatī came down to earth. At Kāñcī, under a single mango tree on the river bank, she shaped a liṅga from sand and began her tapas.</div>
</div>'''+talk("All that for a little joke?","A moment for gods is ages for us. She chose to make it right, the hard way.")))
pages.append(page('flood','THE FLOOD AND THE EMBRACE','Kāmākṣī holds on',fig(560,180,'A goddess embracing a sand linga as a river floods around them under a mango tree',
 '<rect width="560" height="180" fill="#dff2fb"/>'+MANGO(390,150,.8)+''.join(f'<path d="M{i*60-20} {120+(i%2)*10} q30 -14 60 0" stroke="#3b8fd0" stroke-width="5" fill="none"/>' for i in range(11))+'<rect y="150" width="560" height="30" fill="#5ab0f0"/>'+SANDLINGA(300,160,.9)+GENTLE(262,122,.75))+facts([
 ('The test','Śiva sent the river, Kampā or Vegavatī, rushing in flood to test her'),
 ('The embrace','Afraid the sand liṅga would wash away, she threw her arms around it'),
 ('The marks','Her bangles and breasts left marks on the liṅga, still pointed out by the priests; the liṅga is kept covered'),
 ('The reward','Śiva appeared as Ekāmbareśvara, and the two were married at this spot'),
 ('Names','He is called Taḻuvakkuḻainthār, “he who melted in her embrace”, in Tamil')])
 +talk("He sent the flood, then married her?","Testing and grace are one act in these stories. She held on; he gave himself.")))
pages.append(page('mango','THE MANGO TREE','Sthala vṛkṣa',fig(560,190,'A four-branched mango tree with four colours of mango behind a temple courtyard',
 '<rect width="560" height="190" fill="#fff8e7"/><rect y="160" width="560" height="30" fill="#d8c8a8"/>'+MANGO(280,170,1.3))+facts([
 ('Where','In the courtyard behind the sanctum, with the divine couple shown at its foot'),
 ('Four branches','Said to stand for the four Vedas: Ṛg, Yajus, Sāman and Atharvan'),
 ('Four tastes','Each branch is said to bear mangoes of a different taste'),
 ('Age','Claimed at 2,500 to 3,500 years; reports say the old trunk has died and a shoot from it is tended as its successor'),
 ('Meaning','“Eka-āmra”: one tree, one God, many fruits')])
 +talk("Is the tree really 3,500 years old?","That's the temple's claim. Botanists would doubt it; devotees treat the living shoot as the same tree.")))
pages.append(page('linga','THE EARTH LIṄGA','What makes this sanctum different',facts([
 ('Material','By tradition, sand: the liṅga Pārvatī made'),
 ('No water','Because sand would dissolve, water abhiṣeka is not done on the main liṅga; oil and unguents are used instead'),
 ('Covered','The liṅga is kept under a protective covering'),
 ('Somāskanda','A panel of Śiva, Pārvatī and baby Skanda stands behind the main shrine'),
 ('Earth’s lesson','Earth is the patient element: it bears everything and is worshipped gently')])
 +talk("No water on a Śiva liṅga? Isn't that unusual?","Very. Almost every Śiva temple pours water. Here earth is respected for what it is.")))
pages.append(page('noambal','WHY NO SEPARATE GODDESS SHRINE?','One Goddess for the whole city',facts([
 ('The rule','By local tradition, the Śiva temples of Kāñcī have no separate sanctum for the Goddess'),
 ('Why','Kāmākṣī of the Kāmakoṭi Pīṭha is the one Goddess of the city, and every Śiva of Kāñcī is her consort'),
 ('Here','Ēlavārkuḻali is shown with Ekāmbaranātha in the processional images'),
 ('Śakti Pīṭha','Kāmākṣī’s temple is one of the 18 Śakti Pīṭhas')])
 +'<div class="key">Read: <a href="/bhakti/temples-of-india/18-shakti-peethas/kamakshi/">Kāmākṣī, Kāñcī</a></div>'))
pages.append(page('vishnu','A VIṢṆU SHRINE INSIDE','Nilāttiṅgaḷ Tuṇḍam Perumāḷ',fig(560,150,'A small Vishnu shrine inside the courtyard of a large Shiva temple',
 '<rect width="560" height="150" fill="#eef3fa"/>'+TEMPLE(180,130,2)+TEMPLE(400,130,1.3,'#dcecff')+LINGA(180,96,.35)+'<circle cx="400" cy="100" r="8" fill="#3b6fd0" stroke="#111" stroke-width="2"/>')+facts([
 ('What','A shrine of Viṣṇu within the Ekāmbareśvara complex, counted among the 108 Divya Deśams sung by the Āḻvārs'),
 ('Name','Nilāttiṅgaḷ Tuṇḍam, “piece of the moon”: Viṣṇu cooled here by the moon’s light'),
 ('Story','Viṣṇu, scorched while helping at the churning of the ocean, was soothed here by Śiva’s moon'),
 ('Meaning','Śiva and Viṣṇu under one roof, in a city famous for both')])
 +talk("A Divya Deśam inside a Śiva temple?","One of the very few. Kāñcī likes to keep its two gods close.")))
pages.append(page('plan','INSIDE THE TEMPLE','A walk through the courtyards',fig(560,200,'Plan of a temple with five nested courtyards, a tank, a thousand-pillared hall and a tall southern tower',
 '<rect width="560" height="200" fill="#f4e6d0"/>'+''.join(f'<rect x="{40+i*30}" y="{14+i*16}" width="{480-i*60}" height="{172-i*32}" fill="none" stroke="#111" stroke-width="2"/>' for i in range(5))
 +'<rect x="250" y="88" width="60" height="24" fill="#c9a26b" stroke="#111" stroke-width="2"/><rect x="60" y="40" width="70" height="40" fill="#5ab0f0" stroke="#111" stroke-width="2"/><rect x="420" y="40" width="70" height="40" fill="#e8d8b0" stroke="#111" stroke-width="2"/>'
 +'<path d="M270 186 v14 M290 186 v14" stroke="#d9782f" stroke-width="8"/>'+T(280,104,'Sanctum',11)+T(95,64,'Tank',11)+T(455,64,'1000 pillars',10))+facts([
 ('Five courtyards','Five prākāras, one inside another, lead to the sanctum'),
 ('Gopurams','Four gateway towers; the southern Rāja Gopuram is the tallest'),
 ('Hall','The Āyirakkāl Maṇḍapam, a thousand-pillared hall'),
 ('Sahasraliṅga','A liṅga carved with 1,008 small liṅgas, in a corner shrine'),
 ('Tank','Śivagaṅgā Tīrtham, the temple tank')])))
pages.append(page('gopuram','THE RĀJA GOPURAM','Kṛṣṇadevarāya’s tower',fig(560,220,'A tall eleven-storey temple gateway tower',
 '<rect width="560" height="220" fill="#dff2fb"/>'+GOPURAM(280,214,1.0,'#e8d8b0',11)+person(150,200,'#7a5a2a','#f2c79b',.7)+T(150,140,'~1.7 m',11)+T(380,30,'≈ 57–59 m',13))+facts([
 ('Builder','Kṛṣṇadevarāya of Vijayanagara, begun in 1509'),
 ('Height','Eleven storeys, about 57 m by one measure and 59 m by another; among the tallest gopurams in South India'),
 ('Also','Vijayanagara kings added outer walls and the pillared hall before the sanctum'),
 ('Achyutarāya','His successor settled a land dispute between this temple and the Varadarāja (Viṣṇu) temple by dividing the lands equally')])
 +talk("A Vaiṣṇava–Śaiva land fight?","The temple's history records it. The king split it down the middle.")))
pages.append(page('history','A LONG HISTORY','Pallavas to the present',tl([
 ('Legend','Pārvatī’s sand liṅga under the mango tree'),
 ('Before 600','A shrine here is believed to predate the Pallava stone temples; the earliest structure has not survived'),
 ('7th c.','The Tēvāram saints sing Tiruvēkampam'),
 ('Pallavas','Kāñcī is their capital; the city fills with temples'),
 ('Cholas','Rebuild and enlarge; inscriptions record grants'),
 ('1509','Kṛṣṇadevarāya begins the Rāja Gopuram and outer walls'),
 ('16th c.','Achyutarāya divides lands between this temple and Varadarāja'),
 ('Today','Managed under Tamil Nadu’s endowments department; kumbhābhiṣekams renew it periodically')])))
pages.append(page('tevaram','SAINTS AND SONGS','The Tēvāram and Sundarar’s eye',facts([
 ('Tēvāram','Appar, Campantar and Cuntarar all sang this temple'),
 ('Sundarar','The saint had lost his sight; tradition says he regained the sight of his left eye at Kāñcī by singing to Ekāmbaranātha'),
 ('Pāṭal Peṟṟa Talam','One of the 275 temples praised in the Tēvāram'),
 ('Later poets','Kāñcī is praised in Tamil purāṇas such as the <i>Kāñcip Purāṇam</i>')])
 +talk("He got one eye back?","One here, the other at Tiruvārūr, as the story goes. Kāñcī gave the first.")))
pages.append(page('kanchi','THE CITY OF A THOUSAND TEMPLES','Kāñcī around the temple',facts([
 ('Saptapurī','Kāñcī is one of the seven cities of liberation'),
 ('Two halves','Śiva Kāñcī (big Kāñcī) around Ekāmbareśvara; Viṣṇu Kāñcī (little Kāñcī) around Varadarāja'),
 ('Kāmākṣī','The Goddess of the city, a Śakti Pīṭha'),
 ('Kailāsanātha','An early 8th-century Pallava stone temple of Śiva, older than Ekāmbareśvara’s present buildings'),
 ('Silk','Kāñcīpuram silk sarees are woven here; the city’s weavers serve its temples')])
 +'<div class="key">See: <a href="/bhakti/temples-of-india/sapta-puri/">The Saptapurī</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','Its great days',facts([
 ('Paṅkuṉi Uttiram','March–April: a festival of about thirteen days ending in the divine wedding of Ekāmbaranātha and Ēlavārkuḻali'),
 ('Mahāśivarātri','February–March'),
 ('Kārttikai','Lamps across the temple'),
 ('Pradoṣa','Twice a month, Nandi worship at dusk')])))
pages.append(page('meaning','WHAT EARTH TEACHES','The wisdom of the ground',facts([
 ('Patience','Earth bears everything, as Kāmākṣī endured her long tapas'),
 ('Holding on','In the flood, she did not let go'),
 ('Gentleness','Even worship adjusts to what earth can bear: no water poured'),
 ('Unity','One tree, four Vedas; one city, two gods')])
 +talk("What should I take from earth?","Stand firm, bear weight, and hold on to what you love when the flood comes.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Eka · Āmra','One · mango'),('Pṛthvī','Earth'),('Sthala vṛkṣa','Sacred tree of a temple'),('Prākāra','Courtyard enclosure'),('Abhiṣeka','Ritual bathing'),('Divya Deśam','One of 108 Viṣṇu temples sung by the Āḻvārs'),('Kumbhābhiṣeka','Reconsecration'),('Tīrtham','Sacred tank')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Element.</b> Earth: Śiva as the Pṛthvī liṅga of sand, Ekāmbareśvara.</div>
<div><b>Story.</b> Pārvatī’s penance under one mango tree; the flood; Kāmākṣī’s embrace.</div>
<div><b>Temple.</b> Five courtyards, a thousand pillars, Kṛṣṇadevarāya’s 1509 tower.</div>
<div><b>Surprises.</b> No water abhiṣeka; a Divya Deśam inside; Sundarar’s eye.</div>
<div><b>Lesson.</b> Stand firm; hold on through the flood.</div>
</div>'''+talk("One line to remember?","Earth is patient. Kāmākṣī held on, and Śiva melted.")+'<div class="key">Next element, water: <a href="'+PSS+'jambukeshvara/">Jambukeśvara</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Ekambareswarar Temple (Kanchipuram)” (Pṛthvī liṅga; sand liṅga under the mango tree; Vegavatī flood and Kāmākṣī’s embrace; 9.3 ha; Rāja Gopuram 57–59 m by Kṛṣṇadevarāya 1509–29; Achyutarāya and the lands; Tēvāram). Incredible India (gopuram and walls, 1509; mango tree claim). Lonely Planet (tree with four branches; Sahasraliṅga). Sangai Express (bangle marks; liṅga covered).</p>
<p><b>Tradition:</b> Kāñcī Purāṇam and temple sthala-purāṇa (darkened world; Taḻuvakkuḻainthār; Sundarar’s eye; no separate Ambal shrines in Kāñcī); Nālāyira Divya Prabandham (Nilāttiṅgaḷ Tuṇḍam).</p>
<p><b>Sources differ / unverified:</b> the tree’s age and present state; gopuram height (57, 59 or “192 ft” in various sources); the 40-acre figure in some guides against 23 acres; the date of the first shrine. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','His Names'),('dark','The Darkened World'),('flood','The Flood and the Embrace'),('mango','The Mango Tree'),('linga','The Earth Liṅga'),('noambal','Why No Goddess Shrine?'),('vishnu','A Viṣṇu Shrine Inside'),
 ('plan','Inside the Temple'),('gopuram','The Rāja Gopuram'),('history','A Long History'),('tevaram','Saints and Songs'),('kanchi','The City of a Thousand Temples'),('festivals','Through the Year'),('meaning','What Earth Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/PS1_Ekambareshvara.html',head,cov,fw,pages,toc)
