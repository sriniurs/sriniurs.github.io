exec(open('/home/claude/work/shakti/common_s.py').read())
head=make_head('Dvārakā · Abode of the West · srini.presents',
 'Dvārakā, Kṛṣṇa’s city on the Arabian Sea: why Kṛṣṇa left Mathurā, the city built in the sea and swallowed by it, the Dvārakādhīś temple and its flag, Rukmiṇī’s temple and Durvāsā’s curse, Bet Dvārakā and Sudāmā, the Śāradā Pīṭha, the undersea finds and the debate over them. An illustrated reference guide.')
def d(lat,lon): return 40+(lon-68.85)*900, 20+(22.52-lat)*900
def DMAP(w=560,h=300):
    land=' '.join(f'{d(la,lo)[0]:.0f},{d(la,lo)[1]:.0f}' for la,lo in ((22.40,68.95),(22.30,68.97),(22.20,69.00),(22.10,69.05)))
    g=f'<rect width="{w}" height="{h}" fill="#bfe3f0"/><polygon points="{w},{d(22.42,0)[1]:.0f} {d(22.42,69.06)[0]:.0f},{d(22.42,0)[1]:.0f} {d(22.43,69.0)[0]:.0f},{d(22.43,69.0)[1]:.0f} {land} {d(22.10,69.05)[0]:.0f},{h} {w},{h}" fill="#e7f0d8" stroke="#111" stroke-width="2"/>'
    bx,by=d(22.46,69.11); g+=f'<ellipse cx="{bx:.0f}" cy="{by:.0f}" rx="40" ry="14" fill="#e7f0d8" stroke="#111" stroke-width="2"/>'
    gx,gy=d(22.236,68.968); g+=f'<path d="M{gx-30:.0f} {gy+6:.0f} q30 -4 60 6" stroke="#4aa3df" stroke-width="5" fill="none"/>'+T(f'{gx+10:.0f}',f'{gy+30:.0f}','Gomatī',11,'#1d4f9a','start')
    for nm,la,lo,col,side in (('DVĀRAKĀ',22.238,68.968,'#1d4f9a','r'),('Bet Dvārakā',22.46,69.11,'#bbb','r'),('Nāgeśvara',22.336,69.087,'#c0392b','r'),('Okhā',22.425,69.07,'#bbb','r')):
        x,y=d(la,lo); r=8 if col=='#1d4f9a' else 6
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',nm,12,'#111','start' if side=='r' else 'end')
    return g+T(30,270,'ARABIAN SEA',13,'#1d4f9a','start')+T(w-10,h-8,'simplified, not to scale',10,'#555','end')
def SHIKHARA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<rect x="{-40+k*3}" y="{-20-k*18}" width="{80-k*6}" height="18" fill="{"#f2e6c8" if k%2 else "#e2cfa8"}"/>' for k in range(6))
 +'<path d="M-26 -110 q26 -80 52 0z" fill="#e2cfa8"/><circle cy="-150" r="6" fill="#e0a800"/><path d="M0 -150 v-40"/><path d="M0 -190 q30 6 50 24 q-24 -4 -50 0z" fill="#ff8c1a"/><circle cx="20" cy="-180" r="4" fill="#fff" stroke-width="1"/><path d="M34 -174 a4 4 0 1 1 0 .1" fill="#fff" stroke-width="1"/></g>')
def KRISHNA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,'#ffd60a','#3b6fd0',1)+'<path d="M-12 -40 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800" stroke="#111" stroke-width="1.5"/><path d="M6 -56 q8 -10 4 -18" stroke="#2a9d6f" stroke-width="3" fill="none"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A tall temple spire flying a great flag above the sea, with a golden city drawn faintly under the waves">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/><rect y="180" width="380" height="88" fill="#2a7ac0" rx="8"/>'
 +''.join(f'<rect x="{30+i*44}" y="{200+(i%3)*8}" width="30" height="{40-(i%3)*8}" fill="#ffd166" opacity=".35"/>' for i in range(8))+SHIKHARA(190,184,.8)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','<b>Dvārakādhīś</b>: Kṛṣṇa as “King of Dvārakā”, four-armed, in black stone'),
 ('Where','Gujarat, at the western tip of the Saurāṣṭra peninsula, where the <b>Gomatī</b> meets the Arabian Sea'),
 ('Temple','The <b>Jagat Mandir</b>: five storeys, 72 pillars, present building 15th–16th century'),
 ('Legend','Kṛṣṇa’s capital, built on land won from the sea and taken back by it after he left'),
 ('Lists','Western Dhām of the Char Dham (<b>Dvāpara Yuga</b>); one of the <b>Saptapurī</b>; a Divya Deśam'),
 ('Maṭha','<b>Śāradā Pīṭha</b>, Śaṅkara’s western seat'),
 ('Nearby','Rukmiṇī’s temple, <b>Bet Dvārakā</b>, and <b>Nāgeśvara</b> Jyotirliṅga')])
 +talk("Is this the actual city Kṛṣṇa ruled?","Tradition says it stands on the same spot. The sea says the rest of it is underwater.")))
pages.append(page('where','WHERE IT IS','The western edge',fig(560,300,'Simplified map of the Dwarka coast: Dwarka at the Gomati mouth, the Rukmini temple just north, Nageshvara inland to the north-east, and the island of Bet Dwarka off Okha',DMAP())
 +'''<div class="panel reading"><p><b>Land’s end.</b> Dvārakā sits at the western tip of Saurāṣṭra, the last town before the open sea. The Gomatī creek meets the ocean right below the temple steps.</p>
<p><b>A city of three parts.</b> Tradition counts the mainland town, the island of <b>Bet Dvārakā</b> to the north and the Śiva shrine at <b>Nāgeśvara</b> in between as one sacred Dvārakā.</p></div>'''))
pages.append(page('names','THE NAMES','Gate, and gateway',facts([
 ('Dvārakā','From <i>dvāra</i>, “door, gate”: the gateway, to the sea and to liberation'),
 ('Dvārāvatī','“The city of many gates”: its name in the Saptapurī verse'),
 ('Kuśasthalī','The older name of the site, before Kṛṣṇa'),
 ('Dvārakādhīś','“Lord of Dvārakā”'),
 ('Raṇchoḍrāy','“The one who left the battlefield”: a Gujarati name of Kṛṣṇa here'),
 ('Jagat Mandir','“Temple of the world”; also Nija Mandir')])
 +talk("God is called 'the one who ran away'?","Proudly. He left the battle to save his people. Sometimes the bravest thing is to walk away.")))
pages.append(page('legend','THE LEGEND · LEAVING MATHURĀ','Why Kṛṣṇa moved west',fig(560,170,'A long caravan of carts and people leaving a city by a river, walking west toward the sea',
 '<rect width="560" height="170" fill="#fdf1e8"/><rect x="10" y="60" width="90" height="80" fill="#e2cfa8" stroke="#111" stroke-width="2"/><path d="M0 150 h110" stroke="#4aa3df" stroke-width="8"/>'
 +''.join(f'<g transform="translate({140+i*70} 140)" stroke="#111" stroke-width="1.6"><rect x="-22" y="-26" width="44" height="22" fill="#c9a26b"/><circle cx="-12" r="8" fill="#7a5a2a"/><circle cx="12" r="8" fill="#7a5a2a"/></g>' for i in range(4))
 +'<rect x="440" y="110" width="120" height="60" fill="#4aa3df"/>'+KRISHNA(410,140,.9))+'''<div class="steps">
<div><b>Attacked again and again.</b> After Kṛṣṇa killed the tyrant Kaṃsa, Kaṃsa’s father-in-law <b>Jarāsandha</b> attacked Mathurā seventeen times.</div>
<div><b>The move.</b> To spare his people, Kṛṣṇa led the Yādavas west to the coast, to <b>Kuśasthalī</b>.</div>
<div><b>A city from the sea.</b> He asked the ocean for land, and <b>Viśvakarmā</b>, the gods’ architect, built a golden city of many gates on it: Dvārakā.</div>
<div><b>Raṇchoḍ.</b> For leaving the fight, Kṛṣṇa earned the name “the one who left the battlefield”, worshipped here with love.</div>
</div>'''))
pages.append(page('sea','THE CITY UNDER THE SEA','When Kṛṣṇa left',fig(560,170,'A golden city with towers sinking beneath rising waves',
 '<rect width="560" height="170" fill="#cfe3f5"/>'+''.join(f'<rect x="{40+i*60}" y="{50+(i%3)*14}" width="40" height="{120-(i%3)*14}" fill="#ffd166" stroke="#111" stroke-width="1.5"/>' for i in range(8))+'<path d="M0 90 Q70 76 140 90 T280 90 T420 90 T560 90 V170 H0z" fill="#2a7ac0" opacity=".8"/>')+'''<div class="steps">
<div><b>The end of the Yādavas.</b> The Mahābhārata’s Mausala Parva tells how, years after the war, the Yādavas destroyed one another in a drunken brawl, and Kṛṣṇa left the world.</div>
<div><b>The sea returns.</b> Arjuna came to lead the survivors away. As they left, the ocean rose and swallowed Dvārakā, street by street.</div>
<div><b>What remains.</b> Tradition says the present temple stands on the spot of Kṛṣṇa’s own palace, the <b>Hari-gṛha</b>.</div>
</div>'''+talk("Is there really a city down there?","Divers have found walls, stone blocks and anchors offshore. What they are, and how old, is the argument.")))
pages.append(page('undersea','THE UNDERSEA FINDS','Evidence and argument','''<div class="g2">
<div class="card bg-blue"><h4>🌊 The finds</h4><p>From 1979 and through the 1980s, marine archaeologists led by <b>S. R. Rao</b>, later at the National Institute of Oceanography, mapped submerged walls, blocks and stone anchors off Dvārakā and Bet Dvārakā.</p></div>
<div class="card bg-red"><h4>🔎 The argument</h4><p>Rao saw a planned, walled port city matching the Mahābhārata’s description. Other scholars date many finds to much later periods and say they cannot be tied to Kṛṣṇa’s city.</p></div>
</div>
<div class="panel reading"><p><b>On land.</b> Excavations in the town in the 1960s found settlement layers many centuries old, and archaeology suggests an early temple on the site from around 200 BCE at the earliest.</p>
<p><b>Dating.</b> Rao himself noted that the undersea finds could not be dated directly and relied on pottery and sea-level change. The debate is open.</p></div>'''
 +talk("So archaeology proves the legend?","It proves people lived and built here very long ago. Whether it was his city is still argued.")))
pages.append(page('temple','THE JAGAT MANDIR','Five storeys by the sea',fig(560,230,'A five-storeyed carved temple with a tall spire flying a huge flag with the sun and moon, steps going down to a river',
 '<rect width="560" height="230" fill="#cfe3f5"/><rect y="190" width="560" height="40" fill="#4aa3df"/>'+''.join(f'<rect x="{360-i*0}" y="{190-i*6}" width="{120}" height="6" fill="#ccc" stroke="#111" stroke-width=".8" transform="translate({-i*10} 0)"/>' for i in range(6))+SHIKHARA(280,192,.8))+facts([
 ('Building','Five storeys on <b>72 pillars</b>; sanctum, antechamber and a great hall; Māru-Gurjara (Cālukya) style, of limestone and sandstone'),
 ('Founding','Tradition says <b>Vajranābha</b>, Kṛṣṇa’s great-grandson, built the first temple over the Hari-gṛha'),
 ('Two gates','<b>Svarga Dvāra</b>, the “gate to heaven”, opens onto <b>56 steps</b> down to the Gomatī; <b>Mokṣa Dvāra</b> leads to the town (sources differ on which is entry and which exit)'),
 ('Worship','Run in the <b>Puṣṭimārga</b> style of Vallabhācārya'),
 ('Also within','Shrines of Balarāma, Pradyumna, Aniruddha and others')])))
pages.append(page('flag','THE FLAG','52 yards, five times a day',facts([
 ('Size','A huge flag, said to be 52 yards long, flies from the spire'),
 ('Symbols','The <b>sun and moon</b>: Kṛṣṇa will be here as long as they shine'),
 ('Changed','Up to five times a day; families vow and sponsor a flag, and wait their turn'),
 ('52','Said to stand for the clans of the Yādavas'),
 ('56 steps','The steps to the Gomatī are said to stand for 56 Yādava rulers')])
 +talk("People queue to give a flag?","For years sometimes. Seeing your family's flag fly over Dvārakādhīś is a once-in-a-life moment.")))
pages.append(page('image','THE IMAGE','Raṇchoḍrāy',fig(560,170,'A black four-armed image of Krishna holding conch, discus, mace and lotus, richly dressed',
 '<rect width="560" height="170" fill="#2a1a3a"/><path d="M220 20 h120 l-20 26 h-80z" fill="#e0a800" stroke="#111" stroke-width="2"/><g transform="translate(280 160)" stroke="#111" stroke-width="2"><rect x="-22" y="-100" width="44" height="100" rx="12" fill="#222"/><circle cy="-112" r="16" fill="#222"/><path d="M-14 -126 h28 l-4 -12 l-6 5 l-4 -8 l-4 8 l-6 -5z" fill="#e0a800"/>'
 '<path d="M-22 -80 l-30 -20 M22 -80 l30 -20 M-22 -50 l-30 10 M22 -50 l30 10" stroke="#222" stroke-width="8"/><circle cx="-56" cy="-104" r="8" fill="#fff"/><path d="M52 -110 a8 8 0 1 1 0 .1z" fill="#ffd60a"/><rect x="-60" y="-42" width="6" height="30" fill="#bbb"/><circle cx="56" cy="-38" r="8" fill="#f2a6b0"/></g>'))+facts([
 ('Form','Four-armed Viṣṇu-Kṛṣṇa in black stone, holding conch, discus, mace and lotus'),
 ('The image’s story','After the 1472 raid the image was hidden; tradition credits Vallabhācārya with recovering one worshipped by Rukmiṇī'),
 ('Mīrābāī','A beloved legend says the poet-saint Mīrā merged into the image of Raṇchoḍrāy here'),
 ('Dress','Dressed many times a day as king, cowherd or child, in the Puṣṭimārga way')]))
pages.append(page('rukmini','RUKMIṆĪ’S TEMPLE','The queen who lives apart',fig(560,160,'A small carved temple standing alone outside the town, a sage raising his hand in a curse',
 '<rect width="560" height="160" fill="#fdf1e8"/>'+TEMPLE(330,150,1.2,'#f2c9a0')+person(140,150,'#ff8c1a','#c98b5a',1)+'<path d="M160 104 l20 -16" stroke="#c98b5a" stroke-width="5"/>'+T(140,40,'DURVĀSĀ',12,'#7a1d12'))+facts([
 ('Where','Just outside the town, a little to the north'),
 ('Temple','A small, finely carved shrine, usually dated to the 12th century'),
 ('Legend','Kṛṣṇa and Rukmiṇī pulled the sage <b>Durvāsā</b>’s chariot. When Rukmiṇī, thirsty, drank water without first offering him any, he cursed her to live apart from her husband'),
 ('So','Pilgrims see Dvārakādhīś in town and Rukmiṇī out here, and complete the visit only by seeing both'),
 ('Water','The curse is also said to make fresh water scarce here: pilgrims donate water at the temple')])
 +talk("A queen cursed for a sip of water?","Durvāsā was famous for his temper. Even Kṛṣṇa couldn't talk him down.")))
pages.append(page('bet','BET DVĀRAKĀ','The island home',facts([
 ('Where','An island off <b>Okhā</b>, at the mouth of the Gulf of Kachchh'),
 ('Also called','<b>Śaṅkhoddhāra</b>: where Viṣṇu is said to have slain the demon Śaṅkhāsura'),
 ('Tradition','Kṛṣṇa’s family residence, with palace-shrines for his queens'),
 ('Sudāmā','Where his poor childhood friend <b>Sudāmā</b> brought a handful of beaten rice, and went home rich without asking for anything'),
 ('Finds','Marine and land digs here have found Late Harappan pottery and later remains')])
 +talk("Sudāmā never even asked?","That's the point. Kṛṣṇa ate the rice, and Sudāmā found a palace where his hut had been.")))
pages.append(page('mathas','ŚĀRADĀ PĪṬHA AND NĀGEŚVARA','Śaṅkara and Śiva',facts([
 ('Śāradā Pīṭha','The western seat of Śaṅkara’s four maṭhas: <b>Sāma Veda</b>, the great saying <i>tat tvam asi</i>, first head <b>Hastāmalaka</b>'),
 ('Gomatī Ghāṭ','Pilgrims bathe where the Gomatī meets the sea before climbing to the temple'),
 ('Sudāmā Setu','A footbridge across the Gomatī'),
 ('Nāgeśvara','A Jyotirliṅga between Dvārakā and Bet Dvārakā, by one tradition the “Nāgeśa in Dārukāvana” of the hymn'),
 ('Somanātha','Down the coast: Dvārakā’s Śiva partner in the Char Dham pairs')])
 +'<div class="key">Full guides: <a href="/bhakti/temples-of-india/12-jyotirlingas/nageshwar/">Nāgeśvara</a> · <a href="/bhakti/temples-of-india/12-jyotirlingas/somnath/">Somanātha</a></div>'))
pages.append(page('history','HISTORY','Sacked, rebuilt, still standing',tl([
 ('Legend','Vajranābha raises the first temple over Kṛṣṇa’s palace.'),
 ('c. 200 BCE','Earliest likely date of a temple on the site, from archaeology.'),
 ('8th c.','<b>Ādi Śaṅkara</b> visits; the Śāradā Pīṭha, by tradition.'),
 ('12th c.','Rukmiṇī’s temple is built.'),
 ('1472–73','<b>Mahmud Begada</b>, Sultan of Gujarat, sacks the town and destroys the temple.'),
 ('15th–16th c.','The present Jagat Mandir is built and enlarged.'),
 ('16th c.','<b>Vallabhācārya</b>; worship follows the Puṣṭimārga.'),
 ('1960s onward','Excavations on land, then under the sea.')])))
pages.append(page('festivals','THROUGH THE YEAR','Kṛṣṇa’s calendar',facts([
 ('Janmāṣṭamī','Kṛṣṇa’s birthday, the greatest day, celebrated at midnight'),
 ('Holī','Phūl-dol, the swing festival, in spring'),
 ('Annakūṭa','A mountain of food offered after Dīpāvalī'),
 ('Tulasī Vivāha','Kṛṣṇa’s wedding to the tulasī plant'),
 ('Flag','Every day: the flag ceremony, up to five times')])
 +'<div class="key">The god here is a <b>king</b>, so his day is a royal one: waking, bathing, dressing, court, meals and rest.</div>'))
pages.append(page('connect','IN THE SACRED LISTS','Where Dvārakā appears',facts([
 ('Char Dham','The western abode, for <b>Dvāpara Yuga</b>'),
 ('Saptapurī','<b>Dvārāvatī</b>, last of the seven cities of liberation'),
 ('Divya Deśam','One of the 108 Viṣṇu shrines'),
 ('Paired with','Somanātha')])
 +'<div class="key">More: <a href="/bhakti/temples-of-india/char-dham/">Char Dham</a> · <a href="/bhakti/temples-of-india/sapta-puri/">The Saptapurī</a></div>'
 +talk("Dvārakā is in two lists at once?","Char Dham and Saptapurī both. Among the four Dhāms, only it is also a city of liberation.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Dvāra','Gate, door'),('Adhīśa','Lord, king'),('Svarga · Mokṣa','Heaven · liberation'),('Gṛha','House'),('Puṣṭimārga','Vallabha’s path of grace'),
 ('Raṇchoḍ','“Left the battlefield”'),('Ghāṭ','Bathing steps'),('Setu','Bridge'),('Dhvaja','Flag'),('Yādava','Kṛṣṇa’s clan')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The city.</b> Kṛṣṇa’s capital, built on land from the sea after he left Mathurā; swallowed by the sea when he left the world.</div>
<div><b>The temple.</b> The Jagat Mandir, five storeys on 72 pillars, sacked in 1472 and rebuilt.</div>
<div><b>The flag.</b> Sun and moon, changed up to five times a day.</div>
<div><b>Around.</b> Rukmiṇī apart, Sudāmā at Bet Dvārakā, Nāgeśvara between.</div>
<div><b>The lists.</b> Western Dhām, Saptapurī, Divya Deśam, Śaṅkara’s Śāradā Pīṭha.</div>
</div>'''+talk("One line to remember?","A king who walked away from a war and built a city on the sea, where his flag still flies.")+'<div class="key">Jai Dvārakādhīś! 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Dwarkadhish Temple” (Jagat Mandir; five storeys, 72 pillars; Māru-Gurjara; Vajranābha and the Hari-gṛha; archaeology suggesting c. 200 BCE at the earliest; Mahmud Begada, 1472/1473; rebuilt 15th–16th c.; Puṣṭimārga; flag with sun and moon changed up to five times a day; Mokṣa and Svarga Dvāras, 56 steps). Wikipedia, “Dwarka” (Rukmiṇī temple; Gomatī Ghāṭ; Bet Dvārakā; Vallabhācārya and the image). tirthayatra.org (52-yard flag; sponsoring families). behindeverytemple.org and temples.org (56 steps and Yādava rulers).</p>
<p><b>Archaeology:</b> S. R. Rao, “Marine archaeological explorations off Dwarka” and “Further excavations of the submerged city of Dwarka” (NIO); Hinduism Today on Rao’s findings and dating; anantamias.com (Late Harappan pottery at Bet Dvārakā); account of H. D. Sankalia’s 1963 excavation.</p>
<p><b>Sources differ:</b> 1472 or 1473; which gate is entry and which exit; what the undersea structures are and how old. <b>Not verified, tradition only:</b> Jarāsandha’s seventeen attacks as given here; Mīrābāī merging into the image; the curse and Dvārakā’s water; Śaṅkhāsura at Bet Dvārakā; the meaning of the 52 yards. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('legend','Legend · Leaving Mathurā'),('sea','The City Under the Sea'),('undersea','The Undersea Finds'),('temple','The Jagat Mandir'),('flag','The Flag'),('image','The Image'),
 ('rukmini','Rukmiṇī’s Temple'),('bet','Bet Dvārakā'),('mathas','Śāradā Pīṭha and Nāgeśvara'),('history','History'),('festivals','Through the Year'),('connect','In the Sacred Lists'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
bk=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ABODE OF THE WEST</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">DVĀRAKĀ</h1>
  <div class="series">CHAR DHAM · A REFERENCE GUIDE</div>
  <div class="tag">Kṛṣṇa’s city at the edge of the sea</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Kṛṣṇa grew up a cowherd by the Yamunā. He died a king by the sea. The kingdom in between was <b>Dvārakā</b>, a city of gates he built on land the ocean gave him, and which the ocean took back when he was gone.</p>
    <p>Today a tall temple stands on the shore where his palace is said to have been, flying a flag with the sun and moon. Divers search the water below for the rest of the city.</p>
    <p>This guide tells the story, the temple, the queens and friends around it, and the debate under the waves.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Jai Dvārakādhīś,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Kṛṣṇa of Vṛndāvan and Kṛṣṇa of Dvārakā: same person?","Same Kṛṣṇa, different chapters. Vṛndāvan is the boy with the flute; Dvārakā is the king with the crown.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Dvaraka.html','w').write(head+bk+tail())
print('ok',len(pages))
