exec(open('/home/claude/work/shakti/ps_common.py').read())
head=head_navy('Jambukeśvara, Tiruvānaikkāval · Pañcabhūta Sthala of Water · srini.presents',
 'Jambukeśvara temple, Tiruvānaikkāval (Thiruvanaikoil), Tiruchirappalli: Śiva as water (Appu liṅga) over an underground spring, the sage Jambu and the rose-apple tree, Akhilāṇḍeśvarī the student Goddess and the priest who dresses as her at noon, the spider and the elephant, the red-eyed Chola king Kocceṅgaṇ and his 70 temples, Śaṅkara’s earrings, and the wall built by Śiva himself. An illustrated reference guide.')
def ELEPHANT(x,y,s=1,f=1): return (f'<g transform="translate({x} {y}) scale({s*f} {s})" stroke="#111" stroke-width="2"><path d="M-40 20 q-6 -50 36 -54 q40 4 36 54z" fill="#9a9aa8"/><path d="M28 -10 q22 6 20 40 q-2 8 -8 4" fill="none" stroke="#9a9aa8" stroke-width="10"/><path d="M28 -10 q22 6 20 40 q-2 8 -8 4" fill="none" stroke="#111" stroke-width="1"/>'
 '<path d="M-30 20 v16 M-6 20 v16 M14 20 v16" stroke="#9a9aa8" stroke-width="11"/><circle cx="18" cy="-18" r="2.6" fill="#111"/><path d="M4 -26 q-14 2 -12 18 q10 2 14 -8z" fill="#8a8a98"/></g>')
def SPIDER(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M0 0 L{dx} {dy} L{dx*1.5} {dy+10}" fill="none"/>' for dx,dy in ((-14,-8),(-16,0),(-14,8),(-10,14),(14,-8),(16,0),(14,8),(10,14)))+'<circle r="7" fill="#2b2b2b"/><circle cy="-9" r="4" fill="#2b2b2b"/></g>')
def WEB(x,y,r=40): return f'<g transform="translate({x} {y})" stroke="#bbb" stroke-width="1" fill="none">'+''.join(f'<path d="M0 0 L{r*__import__("math").cos(k*0.785):.0f} {r*__import__("math").sin(k*0.785):.0f}"/>' for k in range(8))+''.join(f'<circle r="{r*q}"/>' for q in (.3,.55,.8))+'</g>'
def JAMBU(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-7 0 v-56 h14 v56z" fill="#7a4a1a"/><ellipse cy="-80" rx="58" ry="36" fill="#2f7a3a"/>'
 +''.join(f'<circle cx="{a}" cy="{b}" r="4" fill="#f4f0e0"/>' for a,b in ((-30,-84),(-10,-96),(14,-78),(34,-90),(-20,-66),(28,-66)))+'</g>')
def WATERLINGA(x,y,s=1): return LINGA(x,y,s,'#2b2f36','')+f'<g transform="translate({x} {y}) scale({s})">'+''.join(f'<path d="M{a} -4 q4 -8 8 0" stroke="#5ab0f0" stroke-width="3" fill="none"/>' for a in (-40,-24,16,32))+'<rect x="-50" y="0" width="100" height="6" fill="#5ab0f0" stroke="none"/></g>'
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A Shiva linga with water rising around it beneath a rose-apple tree, an elephant pouring water from its trunk and a spider weaving a web above">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+JAMBU(190,170,1.3)+WEB(190,96,34)+SPIDER(190,96,.9)+WATERLINGA(190,236,1.1)+ELEPHANT(310,222,.9,-1)+'<path d="M266 222 q-20 -2 -38 6" stroke="#5ab0f0" stroke-width="4" fill="none" stroke-dasharray="4 4"/></svg>')
cov=cover('PAÑCABHŪTA 2 · WATER','JAMBUKEŚVARA',14,'Tiruvānaikkāval: Śiva as water',art)
fw=foreword('Om Namaḥ Śivāya,',[
 'The second element flows. On the island of Śrīraṅgam in the Kāverī stands <b>Jambukeśvara</b>, where Śiva is worshipped as <b>water</b>. His liṅga sits in a low, small sanctum over a spring, and water quietly seeps up around it.',
 'The place is named for an elephant: <b>Tiru-āṉai-kkā</b>, “the holy grove of the elephant”. An elephant and a spider both worshipped here, quarrelled, and died; the spider was reborn as the red-eyed Chola king <b>Kocceṅgaṇ</b>, who built temples no elephant could enter. Here too the Goddess <b>Akhilāṇḍeśvarī</b> came as a student, and every noon a priest dressed as her still offers worship to Śiva.',
 'This guide tells the stories of the tree, the spider and the king, and walks through the five courtyards.'],
 'A priest dressed as a woman?','Every day at noon, as Akhilāṇḍeśvarī. It recalls her worship of Śiva here.',
 series_note(prev=('ekambareshvara','Ekāmbareśvara, Kāñcīpuram (earth)'),nxt=('arunachaleshvara','Aruṇācaleśvara, Tiruvaṇṇāmalai (fire)')))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Element','<b>Water</b> (Āpas; Appu in Tamil): the second Pañcabhūta Sthala'),
 ('Śiva as','<b>Jambukeśvara</b>, “Lord of the jambu (rose-apple) tree”'),
 ('Liṅga','The <b>Appu liṅga</b>, over an underground spring that keeps the sanctum wet'),
 ('Goddess','<b>Akhilāṇḍeśvarī</b>, “Queen of all the worlds”, in her own shrine facing east'),
 ('Where','Tiruvānaikkāval on Śrīraṅgam island, Tiruchirāppaḷḷi, Tamil Nadu, close to the Raṅganātha temple'),
 ('Built','By tradition by the early Chola king Kocceṅgaṇ (Kocceṅkaṭ Cōḻaṉ)'),
 ('Unique','A priest dressed as the Goddess performs the noon pūjā'),
 ('Name','Tiru-āṉai-kkā, “sacred elephant grove”, from the elephant who worshipped here')])
 +talk("Is the water really coming up from below?","The sanctum sits over a spring. Priests and visitors describe water seeping around the liṅga, more in the rains.")))
pages.append(page('names','NAMES','Tree, elephant and Goddess',facts([
 ('Jambukeśvara','<i>jambu</i>, the rose-apple tree, + <i>īśvara</i>'),
 ('Tiruvānaikkāval','<i>tiru</i> holy + <i>āṉai</i> elephant + <i>kā</i> grove'),
 ('Appu liṅga','Tamil <i>appu</i>, water'),
 ('Akhilāṇḍeśvarī','<i>akhila</i> all + <i>aṇḍa</i> worlds + <i>īśvarī</i> queen'),
 ('Jambukeśvaram','The Sanskrit name of the place'),
 ('Veṇ Nāval','The white jambu tree under which the liṅga stands')])
 +talk("The elephant got the town named after it?","And the spider got a kingdom. Both did well out of their devotion.")))
pages.append(page('jambu','THE SAGE AND THE ROSE-APPLE','Why “Jambukeśvara”',fig(560,170,'A sage meditating with a tree growing from his head, Shiva appearing beneath it',
 '<rect width="560" height="170" fill="#e8f4e0"/>'+JAMBU(280,120,.9)+person(280,150,'#e08a2a','#c98b5a',.8)+LINGA(420,160,.55)+person(140,150,'#5b8fe0','#5b8fe0',.7))+'''<div class="steps">
<div><b>The fruit.</b> A sage named Jambu did tapas, and Śiva gave him a rare rose-apple (jambu) fruit.</div>
<div><b>The seed.</b> Out of reverence the sage swallowed it whole, seed and all, rather than throw away anything from Śiva’s hand.</div>
<div><b>The tree.</b> A jambu tree sprang from his head, and he asked Śiva to stay forever beneath it. Śiva became Jambukeśvara, Lord of the jambu.</div>
</div>'''+talk("A tree from his head?","Sthala stories are vivid. The point: he wasted nothing that came from the Lord.")))
pages.append(page('student','THE STUDENT GODDESS','Akhilāṇḍeśvarī learns from Śiva',fig(560,170,'A goddess facing east and Shiva facing west, teaching her',
 '<rect width="560" height="170" fill="#fdf1f6"/>'+SHIVA(360,90,.8)+GENTLE(200,100,.8)+'<path d="M240 60 q60 -30 100 0" stroke="#e0a800" stroke-width="3" fill="none" stroke-dasharray="5 4"/>')+facts([
 ('Why she came','Pārvatī had laughed at Śiva’s austerity; he sent her to earth to do penance'),
 ('Her liṅga','She shaped a liṅga out of the water of the Kāverī, under the white jambu tree'),
 ('The lesson','Śiva appeared and taught her Śiva-jñāna, the knowledge of Śiva'),
 ('Facing','She sat facing east as the student; he faced west as the teacher. The two shrines still face each other that way'),
 ('Upadeśa sthala','A “place of teaching”: for this reason, it is said, no divine wedding festival is held here')])
 +talk("No wedding festival at a Śiva temple?","Here they are guru and disciple, not bride and groom. So the wedding is left out.")))
pages.append(page('noon','THE NOON PŪJĀ','A priest dressed as the Goddess',fig(560,170,'A priest in a red saree carrying a lamp towards a low sanctum',
 '<rect width="560" height="170" fill="#fff4dc"/><rect x="330" y="60" width="140" height="100" fill="#d8c49a" stroke="#111" stroke-width="2"/><rect x="380" y="110" width="40" height="50" fill="#2b1a0e" stroke="#111" stroke-width="2"/>'+person(250,140,'#c0392b','#c98b5a',1)+'<path d="M276 96 h20 l-4 8 h-12z" fill="#c9a26b" stroke="#111"/><path d="M286 96 q-6 -12 0 -20 q6 8 0 20z" fill="#ff8c1a" stroke="#111"/>')+facts([
 ('When','Every day at the noon pūjā (ucchi-kāla)'),
 ('What','A priest from the Goddess’s shrine puts on a saree and goes to Jambukeśvara’s sanctum to offer worship'),
 ('Why','He re-enacts Akhilāṇḍeśvarī worshipping Śiva here, as she did in her penance'),
 ('Also','After the pūjā he is said to worship the cow as well, as the Goddess would')])
 +talk("Do people come just to see this?","Many do. It's one of the most unusual daily rites in any Śiva temple.")))
pages.append(page('spider','THE SPIDER AND THE ELEPHANT','Two devotees, one quarrel',fig(560,190,'An elephant pouring water on a linga while a spider weaves a web over it',
 '<rect width="560" height="190" fill="#e8f4e0"/>'+JAMBU(280,150,.9)+WEB(280,74,32)+SPIDER(280,74,.8)+LINGA(280,184,.7)+ELEPHANT(430,160,.9,-1)+'<path d="M394 152 q-40 -4 -70 12" stroke="#5ab0f0" stroke-width="4" fill="none" stroke-dasharray="4 4"/>')+'''<div class="steps">
<div><b>Two cursed gaṇas.</b> Two of Śiva’s attendants, Mālyavān and Puṣpadanta, quarrelled and cursed each other: one became a spider, the other an elephant.</div>
<div><b>Two ways to worship.</b> The elephant brought Kāverī water in its trunk and bathed the liṅga every day. The spider spun a web over it to keep off falling leaves and the sun.</div>
<div><b>The quarrel.</b> The elephant thought the web was dirt and washed it away; the spider spun it again. At last the angry spider crept into the elephant’s trunk and bit it. In agony the elephant crushed itself and the spider died with it.</div>
</div>'''+talk("Who was right?","Both loved Śiva. Each thought the other was spoiling the worship. Śiva freed them both.")))
pages.append(page('king','THE RED-EYED KING','Kocceṅgaṇ Cōḻaṉ',fig(560,170,'A crowned Chola king with red eyes, and a temple raised on a high platform with steep steps',
 '<rect width="560" height="170" fill="#fdf1e8"/>'+KING(170,140,1.1)+'<circle cx="166" cy="98" r="2" fill="#e04040"/><circle cx="176" cy="98" r="2" fill="#e04040"/>'
 +'<rect x="320" y="100" width="160" height="60" fill="#c9a26b" stroke="#111" stroke-width="2"/>'+TEMPLE(400,100,1.8)+''.join(f'<rect x="{300-k*8}" y="{100+k*12}" width="20" height="12" fill="#d8c49a" stroke="#111"/>' for k in range(5)))+facts([
 ('Reborn','The elephant gained liberation; the spider was reborn as a Chola prince'),
 ('Red eyes','His mother, told that a child born at a certain hour would rule the world, asked to be held upside down to delay the birth; the baby was born with reddened eyes: Ko-ceṅ-kaṇ, “king of the red eyes”'),
 ('His vow','Remembering his past life, he built temples raised on high platforms with narrow entrances that no elephant could enter: the <b>māḍakkōyil</b>'),
 ('Seventy','He is credited with about 70 such temples; this one is the most famous'),
 ('Saint','He is one of the 63 Nāyaṉmārs')])
 +talk("He held a grudge from his last life?","Call it caution. The sanctum door here is still low and narrow.")))
pages.append(page('history','THE KING IN HISTORY','Between legend and record',facts([
 ('Sangam poem','The <i>Kaḷavaḻi Nāṟpatu</i> of the poet Poykaiyār celebrates a Chola king Ceṅkaṇāṉ who defeated the Cēra ruler Kaṇaikkāl Irumpoṟai'),
 ('Same king?','Tradition identifies him with Kocceṅgaṇ of the temples; historians place him in the early centuries CE, but dates are uncertain'),
 ('Uraiyūr','The early Chola capital, now part of Tiruchirāppaḷḷi'),
 ('Later builders','Cholas, Pāṇḍyas, Vijayanagara and Nāyaka rulers all added to the temple')])
 +talk("So was he real?","Probably a real early king, wrapped in a beautiful story.")))
pages.append(page('sanctum','THE WATER SANCTUM','What you see inside',fig(560,170,'A low sanctum doorway, with a linga in a pool of water seen through it',
 '<rect width="560" height="170" fill="#d8c49a"/><rect x="200" y="40" width="160" height="130" fill="#e8d8b0" stroke="#111" stroke-width="2"/><rect x="250" y="96" width="60" height="74" fill="#1d1d2a" stroke="#111" stroke-width="2"/>'+WATERLINGA(280,166,.45)+person(150,166,'#7a5a2a','#f2c79b',.9)+T(280,30,'low, narrow entrance',12))+facts([
 ('Entrance','The doorway to the sanctum is low and small; devotees bow to enter or to look'),
 ('Liṅga','Small, standing in a recess where water rises from the spring'),
 ('Wet','The water level rises in the rains; a cloth around the liṅga is often soaked'),
 ('Window','Devotees view the liṅga through a small opening with nine holes, according to many descriptions'),
 ('Lesson','The water liṅga can only be seen by bending low')])))
pages.append(page('earrings','ŚAṄKARA AND THE GODDESS','The Śrī Cakra earrings',fig(560,160,'A goddess wearing two large earrings shaped like Sri Chakras, with Ganesha in front of her',
 '<rect width="560" height="160" fill="#fde4ec"/>'+GENTLE(280,90,1)+CHAKRA(254,62,8)+CHAKRA(306,62,8)+'<g transform="translate(160 130)" stroke="#111" stroke-width="2"><circle r="20" fill="#e8a060"/><path d="M-6 6 q-10 14 -2 24" stroke="#e8a060" stroke-width="7" fill="none"/></g>')+facts([
 ('Fierce once','Tradition says Akhilāṇḍeśvarī was once very fierce'),
 ('Śaṅkara','Ādi Śaṅkara is said to have calmed her by placing a pair of <b>tāṭaṅka</b> (ear ornaments) shaped as Śrī Cakras in her ears'),
 ('Her son','He also placed Gaṇeśa (Prasanna Vināyaka) facing her, so that seeing her child she would soften'),
 ('Renewed','The earrings are re-polished and restored at intervals; the Kāñcī Kāmakoṭi Pīṭha is associated with this'),
 ('Om','Some say the Goddess and Vināyaka shrines together trace the shape of Om')])
 +talk("Earrings to calm a Goddess?","Not ordinary ones. Each is a Śrī Cakra, her own diagram of power, turned to grace.")))
pages.append(page('wall','THE WALL BUILT BY ŚIVA','Tiruneeṟṟāṉ Matil',facts([
 ('The story','When the outer wall was being built, Śiva came as a labourer, a siddha, and worked with the masons'),
 ('The wages','He paid the workers in sacred ash (vibhūti); for each one it turned to gold in proportion to the work done'),
 ('The name','The fifth enclosure wall is called Tiruneeṟṟāṉ Matil, “the wall of the one with holy ash”'),
 ('The scale','The outer wall runs for over a kilometre around the complex'),
 ('Meaning','Honest work is paid by the Lord exactly')])
 +talk("Ash that turned into gold?","Only as much as you had earned. A fair employer, Śiva.")))
pages.append(page('plan','THE FIVE COURTYARDS','Inside Jambukeśvaram',fig(560,200,'Plan of five nested courtyards with the Shiva sanctum facing west and the Goddess shrine facing east',
 '<rect width="560" height="200" fill="#f4e6d0"/>'+''.join(f'<rect x="{30+i*28}" y="{12+i*16}" width="{500-i*56}" height="{176-i*32}" fill="none" stroke="#111" stroke-width="2"/>' for i in range(5))
 +'<rect x="250" y="88" width="50" height="24" fill="#5ab0f0" stroke="#111" stroke-width="2"/>'+T(275,104,'Śiva → W',10)+'<rect x="150" y="40" width="70" height="22" fill="#f08aa6" stroke="#111" stroke-width="2"/>'+T(185,55,'Ambāl → E',10)
 +'<rect x="380" y="140" width="70" height="22" fill="#9fd0ea" stroke="#111" stroke-width="2"/>'+T(415,155,'Tank',10))+facts([
 ('Five prākāras','Five enclosures, the outermost the wall of Śiva the labourer'),
 ('Facing','Jambukeśvara faces west; Akhilāṇḍeśvarī faces east, in her own shrine in the second enclosure'),
 ('Halls','Pillared maṇḍapams with Nāyaka-period sculpture'),
 ('Jambu tree','A jambu tree grows by the sanctum as the sthala vṛkṣa'),
 ('Kocceṅgaṇ','A shrine to the king stands in a corridor')])))
pages.append(page('neighbours','ŚRĪRAṄGAM ISLAND','Two great temples side by side',facts([
 ('Raṅganātha','The great Viṣṇu temple of Śrīraṅgam is about 2.5 km away on the same island'),
 ('Kāverī and Koḷḷiḍam','The island lies between the two branches of the river'),
 ('Raṅga link','Śrīraṅgam is the Antya Raṅga of the Triraṅga series'),
 ('Tēvāram','Appar, Campantar and Cuntarar sang Tiruvānaikkā')])
 +'<div class="key">See: <a href="/bhakti/temples-of-india/triranga/antya-ranga/">Antya Raṅga, Śrīraṅgam</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','Its great days',facts([
 ('Paṅkuṉi Brahmotsavam','March–April, the main festival'),
 ('Pañcaprākāra Utsavam','A procession round all five courtyards'),
 ('Navarātri','For Akhilāṇḍeśvarī, dressed differently each day'),
 ('Āḍi Pūram','July–August, the Goddess’s festival'),
 ('Daily','The noon pūjā by the priest dressed as the Goddess')])))
pages.append(page('meaning','WHAT WATER TEACHES','The wisdom of the flowing element',facts([
 ('Humility','The water liṅga is seen only by bowing low'),
 ('Learning','Even the Goddess came here as a student'),
 ('Devotion has many forms','The web and the water were both worship'),
 ('Honest work','The wall paid in ash, turned gold by effort')])
 +talk("What should I take from water?","Flow, bow, learn. And don't wash away someone else's way of loving God.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Jambu','Rose-apple, Indian blackberry (nāval)'),('Appu','Water (Tamil)'),('Āṉai · Kā','Elephant · grove'),('Gaṇa','Attendant of Śiva'),('Māḍakkōyil','Temple on a raised platform'),('Tāṭaṅka','Ear ornament'),('Upadeśa','Teaching'),('Vibhūti','Sacred ash')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Element.</b> Water: the Appu liṅga over a spring, Jambukeśvara.</div>
<div><b>Stories.</b> The sage Jambu’s tree; Akhilāṇḍeśvarī the student; the spider and the elephant.</div>
<div><b>King.</b> Red-eyed Kocceṅgaṇ and his 70 temples no elephant could enter.</div>
<div><b>Wonders.</b> The noon priest dressed as the Goddess; Śaṅkara’s earrings; the wall of holy ash.</div>
<div><b>Lesson.</b> Bow low, keep learning, respect another’s devotion.</div>
</div>'''+talk("One line to remember?","Water finds the lowest place. So does wisdom.")+'<div class="key">Next element, fire: <a href="'+PSS+'arunachaleshvara/">Aruṇācaleśvara</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Jambukeswarar Temple, Thiruvanaikaval” (Appu liṅga; underground stream; Akhilāṇḍeśvarī’s penance and Śiva-jñāna; east–west facing; Mālyavān and Puṣpadanta; Kocceṅgaṇ); Wikipedia, “Akilandeswari” (noon pūjā by the priest dressed as a woman; elephant and spider); Dinamalar temple page (Kocceṅgaṇ’s birth to the Chola king and queen); AstroVed (70 māḍakkōyils; king’s shrine); trawell.in (distance to Śrīraṅgam; water in sanctum).</p>
<p><b>Literature:</b> <i>Kaḷavaḻi Nāṟpatu</i> (Poykaiyār); Tēvāram; Periya Purāṇam (Kocceṅgaṇ Nāyaṉār).</p>
<p><b>Sources differ / unverified:</b> date of Kocceṅgaṇ (2nd century CE to later); the nine-hole window; the cow worship after the noon pūjā; Om-shaped layout; details of the earrings’ renewal; length of the outer wall; the Pañcaprākāra festival’s month. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('jambu','The Sage and the Rose-Apple'),('student','The Student Goddess'),('noon','The Noon Pūjā'),('spider','The Spider and the Elephant'),('king','The Red-Eyed King'),('history','The King in History'),
 ('sanctum','The Water Sanctum'),('earrings','Śaṅkara and the Goddess'),('wall','The Wall Built by Śiva'),('plan','The Five Courtyards'),('neighbours','Śrīraṅgam Island'),('festivals','Through the Year'),('meaning','What Water Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/PS2_Jambukeshvara.html',head,cov,fw,pages,toc)
