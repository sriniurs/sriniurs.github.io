exec(open('/home/claude/work/shakti/ps_common.py').read())
head=head_navy('Kāḷahastīśvara, Śrīkāḷahasti · Pañcabhūta Sthala of Air · srini.presents',
 'Śrīkāḷahastīśvara temple, Śrīkāḷahasti, Andhra Pradesh: Śiva as air (Vāyu liṅga) and the lamp that flickers in a windless sanctum, Vāyu’s penance at the camphor liṅga, the spider, snake and elephant who gave the town its name, Kaṇṇappa the hunter who gave his eyes, Jñānaprasūnāmbā, the Rāhu–Ketu rites, Dhūrjaṭi’s poems, and the Rāja Gopuram of 1516 that fell in 2010. An illustrated reference guide.')
def SNAKE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 10 q10 -14 20 0 q10 14 20 0 q10 -14 16 -2" fill="none" stroke="#3a6a3a" stroke-width="8"/><path d="M-30 10 q10 -14 20 0 q10 14 20 0 q10 -14 16 -2" fill="none" stroke="#111" stroke-width="1"/><path d="M26 -2 q10 -18 0 -26 q-12 6 -6 24z" fill="#3a6a3a"/><circle cx="24" cy="-16" r="1.8" fill="#ffd60a"/></g>'
def SPIDER(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M0 0 L{dx} {dy} L{dx*1.5} {dy+10}" fill="none"/>' for dx,dy in ((-14,-8),(-16,0),(-14,8),(-10,14),(14,-8),(16,0),(14,8),(10,14)))+'<circle r="7" fill="#2b2b2b"/><circle cy="-9" r="4" fill="#2b2b2b"/></g>')
def ELE(x,y,s=1,f=1): return (f'<g transform="translate({x} {y}) scale({s*f} {s})" stroke="#111" stroke-width="2"><path d="M-40 20 q-6 -50 36 -54 q40 4 36 54z" fill="#9a9aa8"/><path d="M28 -10 q22 6 20 40 q-2 8 -8 4" fill="none" stroke="#9a9aa8" stroke-width="10"/>'
 '<path d="M-30 20 v16 M-6 20 v16 M14 20 v16" stroke="#9a9aa8" stroke-width="11"/><circle cx="18" cy="-18" r="2.6" fill="#111"/></g>')
def VAYULINGA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-46 0 h92 l-8 -14 h-76z" fill="#7a7f8a"/>'
 '<path d="M-14 -14 v-60 q14 -16 28 0 v60z" fill="#f4f4f0"/>'+''.join(f'<path d="M{a} -82 q4 -10 8 0" fill="#3a6a3a"/>' for a in (-14,-8,-2,4,10))+'<path d="M-14 -40 l-12 6 M14 -40 l12 6" stroke="#fff8e7" stroke-width="5"/><circle cy="-20" r="4" fill="#2b2b2b"/></g>')
def LAMP(x,y,s=1,bend=0): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-16 0 h32 l-6 8 h-20z" fill="#c9a26b"/><path d="M-2 0 q{-6+bend} -14 {bend} -26 q{6+bend} 12 2 26z" fill="#ff8c1a"/></g>'
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A white Vayu linga with snake hoods on top, two oil lamps beside it with flickering flames, and a spider, a snake and an elephant around it">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+''.join(f'<path d="M{20+i*30} {60+(i%3)*20} q20 -10 40 0" stroke="#9fe0c0" stroke-width="2" fill="none" opacity=".6"/>' for i in range(11))
 +VAYULINGA(190,236,1.4)+LAMP(110,200,1.2,-6)+LAMP(270,200,1.2,6)+SPIDER(60,236,.9)+SNAKE(320,230,.9)+ELE(70,140,.6)+'</svg>')
cov=cover('PAÑCABHŪTA 4 · AIR','KĀḶAHASTĪŚVARA',13,'Śrīkāḷahasti: Śiva as air',art)
fw=foreword('Om Namaḥ Śivāya,',[
 'Air cannot be seen, only felt. At <b>Śrīkāḷahasti</b>, on the river Svarṇamukhī near Tirupati, Śiva is worshipped as <b>air</b>. In the sanctum there is no window to let a breeze in, yet a lamp beside the liṅga is said to flicker as if someone were breathing on it.',
 'The town takes its name from three devotees: a spider (<b>śrī</b>), a snake (<b>kāla</b>) and an elephant (<b>hasti</b>). Here too a hunter named Tiṇṇaṉ saw blood flowing from the liṅga’s eye and gave his own eye to stop it, becoming the saint <b>Kaṇṇappa</b>. In 2010 the great tower raised by Kṛṣṇadevarāya in 1516 fell to the ground; a new one now stands.',
 'This guide tells the stories of the breath, the three creatures and the hunter.'],
 'A lamp that moves with no wind?','That is what devotees see and believe. In the temple of air, the flame shows the breath of Śiva.',
 series_note(prev=('arunachaleshvara','Aruṇācaleśvara, Tiruvaṇṇāmalai (fire)'),nxt=('chidambaram','Naṭarāja, Cidambaram (space)')))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Element','<b>Air</b> (Vāyu): the fourth Pañcabhūta Sthala'),
 ('Śiva as','<b>Śrīkāḷahastīśvara</b>, Lord of Śrī, Kāla and Hasti'),
 ('Liṅga','The <b>Vāyu liṅga</b>: a tall white liṅga, said to be self-manifest'),
 ('Goddess','<b>Jñānaprasūnāmbā</b>, “mother of the flower of wisdom”'),
 ('Where','Śrīkāḷahasti, Tirupati district, Andhra Pradesh, on the Svarṇamukhī river, about 36 km from Tirupati'),
 ('Wonder','The flickering lamp in a windless sanctum'),
 ('Also','Kaṇṇappa’s shrine; famous Rāhu–Ketu rites; called Dakṣiṇa Kailāsa'),
 ('Tower','Kṛṣṇadevarāya’s gopuram of 1516 collapsed on 26 May 2010; rebuilt since')])
 +talk("The only one in Andhra?","Yes. The other four are in Tamil Nadu. Here the hymns are in Telugu as well as Tamil.")))
pages.append(page('names','NAMES','Spider, snake, elephant',facts([
 ('Śrī','The spider'),('Kāla','The snake (cobra)'),('Hasti','The elephant'),
 ('Śrīkāḷahasti','The town named after all three'),
 ('Tirukkāḷatti','Its Tamil name in the Tēvāram'),
 ('Dakṣiṇa Kailāsa','“Kailāsa of the South”, for the hills around it')])
 +talk("A town named after three animals?","Three devotees. In Śiva's eyes they were all equal.")))
pages.append(page('vayu','VĀYU’S PENANCE','How air came to the liṅga',fig(560,170,'The wind god meditating before a white camphor linga, with swirling air',
 '<rect width="560" height="170" fill="#e4f6ee"/>'+''.join(f'<path d="M{20+i*40} {40+(i%3)*30} q20 -10 40 0" stroke="#3a8a70" stroke-width="3" fill="none"/>' for i in range(13))+person(180,150,'#9fe0c0','#9fd0c0',1)+VAYULINGA(380,160,.9))+'''<div class="steps">
<div><b>The camphor liṅga.</b> In the first age, Vāyu, god of the wind, did penance for thousands of years before a liṅga of camphor (karpūra).</div>
<div><b>The boons.</b> Pleased, Śiva gave him three gifts: to be present everywhere, to be the life-breath of every creature, and to have the liṅga named after him.</div>
<div><b>The Vāyu liṅga.</b> So it became the liṅga of air, to be worshipped by all the worlds.</div>
</div>'''+talk("Camphor?","Camphor vanishes into the air when it burns. A good liṅga for the god of wind.")))
pages.append(page('three','THE SPIDER, THE SNAKE, THE ELEPHANT','Three devotees',fig(560,200,'A spider weaving, a snake placing a jewel and an elephant pouring water on a linga',
 '<rect width="560" height="200" fill="#f4f0e0"/>'+VAYULINGA(280,190,.9)+SPIDER(150,120,1.3)+'<g stroke="#bbb" fill="none">'+''.join(f'<path d="M150 120 L{150+40*__import__("math").cos(k*0.785):.0f} {120+40*__import__("math").sin(k*0.785):.0f}"/>' for k in range(8))+'</g>'+SNAKE(380,170,1.1)+'<circle cx="402" cy="146" r="5" fill="#e04040" stroke="#111"/>'+ELE(470,120,.8,-1))+'''<div class="steps">
<div><b>The spider</b> spun webs over the liṅga as a canopy against sun and dust; when a lamp burned the web, it tried to eat the flame to save the Lord.</div>
<div><b>The snake</b> brought precious gems from the underworld and laid them on the liṅga.</div>
<div><b>The elephant</b> bathed the liṅga with river water and leaves, washing away the gems as if they were dirt. The angry snake entered its trunk; the elephant beat its head against the liṅga and all three died together.</div>
<div><b>Liberation.</b> Śiva freed all three and made them one with the liṅga.</div>
</div>'''))
pages.append(page('linga','THE VĀYU LIṄGA','What you see',fig(560,200,'A tall white linga with snake hoods at the top, tusk shapes on the sides and a spider at the base, with two lamps',
 '<rect width="560" height="200" fill="#1d1d2a"/>'+VAYULINGA(280,190,1.6)+LAMP(160,150,1.4,-8)+LAMP(400,150,1.4,8))+facts([
 ('Shape','Tall, white, likened to an elephant’s trunk'),
 ('Marks','At its base a spider; on the sides two elephant tusks; at the top a five-hooded snake'),
 ('Not touched','By temple custom, offerings are made without the priests laying hands on the main liṅga, many accounts say'),
 ('Lamps','Lamps on either side are said to flicker though the sanctum has no opening for wind'),
 ('Self-manifest','Svayambhū: not made by human hands, by tradition')])
 +talk("Is the flicker real?","Devotees say they see it. The temple calls it Vāyu's breath. Believers see a sign; skeptics see air currents from crowds and lamps.")))
pages.append(page('kannappa','KAṆṆAPPA, THE HUNTER','The eyes he gave',fig(560,200,'A hunter with a bow placing his hand over his own eye, his foot on the linga, as Shiva\'s hand stops him',
 '<rect width="560" height="200" fill="#e8f4e0"/>'+LINGA(330,190,1.0,'#2b2f36','<circle cx="-6" cy="-40" r="3" fill="#e04040" stroke="none"/><circle cx="6" cy="-40" r="3" fill="#e04040" stroke="none"/>')+person(200,180,'#7a4a1a','#8a5a3a',1.2)+'<path d="M160 120 q-20 -30 0 -60" stroke="#7a4a1a" stroke-width="4" fill="none"/><path d="M260 180 l40 -6" stroke="#8a5a3a" stroke-width="10"/><path d="M420 40 q-30 10 -60 40" stroke="#5b8fe0" stroke-width="10"/>')+'''<div class="steps">
<div><b>A hunter’s worship.</b> Tiṇṇaṉ, a young hunter, found the liṅga in the forest and loved it at once. He bathed it with water carried in his mouth, decked it with flowers from his hair and offered the best of his hunt.</div>
<div><b>The test.</b> One day blood flowed from the liṅga’s right eye. Tiṇṇaṉ tried herbs, then dug out his own eye with an arrow and pressed it on the wound. The bleeding stopped.</div>
<div><b>The second eye.</b> Then the left eye bled. So he would not lose the place blind, he set his foot on the spot and raised the arrow to his other eye.</div>
<div><b>“Stop, Kaṇṇappa!”</b> Śiva’s hand caught his. Three times he cried “Niḷ Kaṇṇappa”. The hunter got back his sight and became Kaṇṇappa, “the one who gave his eye”.</div>
</div>'''))
pages.append(page('kannappa2','WHY KAṆṆAPPA MATTERS','Love over rule',facts([
 ('The other worshipper','A priest, Śivagocarīyār, came daily and was horrified to find meat and mouth-water on the liṅga; Śiva let him hide and watch the hunter’s devotion'),
 ('The lesson','Love counts more than ritual correctness'),
 ('Nāyaṉmār','Kaṇṇappa is one of the 63 Tamil Śaiva saints; his story is in the <i>Periya Purāṇam</i>'),
 ('Shrine','A shrine of Kaṇṇappa stands on a hill above the temple'),
 ('Retold','In Telugu, Tamil and Kannada poems and many films')])
 +talk("A priest learning from a hunter?","That's the point. The priest had rules; the hunter had love. Śiva chose love.")))
pages.append(page('goddess','JÑĀNAPRASŪNĀMBĀ','The Goddess of wisdom',facts([
 ('Name','“Mother of the flower of wisdom”; in Tamil Ñāṉappūṅkōtai'),
 ('Story','Pārvatī, cursed by Śiva to take a human form, did penance here and regained her divine body'),
 ('Gift','She is said to have taught her devotees a mantra of wisdom (Pañcākṣarī) here'),
 ('Shrine','A separate temple within the complex'),
 ('Students','Parents bring children to her before they begin learning')])))
pages.append(page('rahu','RĀHU–KETU AND ECLIPSES','A temple that stays open',facts([
 ('Rāhu–Ketu','The temple is famous for rites to ease the influence of the shadow planets Rāhu and Ketu'),
 ('Sarpa doṣa','People come for relief from “serpent affliction” in their horoscopes'),
 ('Eclipses','Unlike most temples, which shut during an eclipse, Śrīkāḷahasti is known for staying open'),
 ('Why','Tradition says the Lord here is beyond the planets: the 27 stars and 9 planets are on his kavaca'),
 ('Our note','These are beliefs and practices of the temple, described as they are held')])
 +talk("Do the rites work?","That's faith, not science. What's certain is that thousands come for them every day.")))
pages.append(page('temple','THE TEMPLE','Between river and hills',fig(560,200,'A temple at the foot of rocky hills beside a river, with a tall tower',
 '<rect width="560" height="200" fill="#e4f0f6"/><path d="M0 200 L80 90 L160 140 L240 70 L330 150 L420 90 L560 160 V200Z" fill="#a08a6a" stroke="#111" stroke-width="2"/><rect y="180" width="560" height="20" fill="#5ab0f0"/>'+GOPURAM(150,180,.8,'#e8d8b0',9)+TEMPLE(330,180,2.4)+TEMPLE(460,92,1.2))+facts([
 ('Setting','On the Svarṇamukhī, against rocky hills; parts of the temple are built into the hillside'),
 ('Pātāla Gaṇapati','An underground shrine of Gaṇeśa about 9 feet below ground'),
 ('Hundred-pillar hall','Carved for Kṛṣṇadevarāya in 1516'),
 ('Cholas','Chola kings of the 11th century built much of the inner temple'),
 ('Kaṇṇappa','His shrine on the hill above')])))
pages.append(page('gopuram','THE TOWER THAT FELL','26 May 2010',fig(560,200,'A tall temple tower on the left and a heap of fallen stones on the right',
 '<rect width="560" height="200" fill="#fdf1e8"/>'+GOPURAM(150,196,.9,'#e8d8b0',9)+'<path d="M140 30 l6 30 l-8 30 l6 30" stroke="#5a3a1a" stroke-width="3" fill="none"/>'
 +''.join(f'<rect x="{330+(i*37)%160}" y="{150+(i*13)%40}" width="26" height="14" fill="#d8c49a" stroke="#111" transform="rotate({(i*17)%40-20} {343+(i*37)%160} {157+(i*13)%40})"/>' for i in range(16)))+facts([
 ('Built','By Kṛṣṇadevarāya in 1516 to mark his victory over the Gajapatis of Odisha; about 37 m (120 ft)'),
 ('The crack','A thin crack noted about 25 years earlier grew into a deep fissure down its face'),
 ('The fall','At night on 26 May 2010 the whole tower came down; the main shrine was not damaged'),
 ('Why','The Archaeology Department found its foundation was only about one and a half feet deep'),
 ('After','An inquiry was ordered, and a new Rāja Gopuram has since been built')])
 +talk("Five hundred years on a foot and a half?","Stone towers are heavier than they look. It lasted a long time on very little.")))
pages.append(page('poets','POETS OF KĀḶAHASTI','Tamil and Telugu',facts([
 ('Tēvāram','Appar, Campantar and Cuntarar sang Tirukkāḷatti'),
 ('Dhūrjaṭi','A Telugu poet of Kṛṣṇadevarāya’s court, one of the Aṣṭadiggajas, wrote the <i>Śrī Kāḷahastīśvara Śatakam</i> and the <i>Kāḷahasti Māhātmyamu</i>'),
 ('Periya Purāṇam','Cēkkiḻār’s life of Kaṇṇappa'),
 ('Nakkīrar','Tradition links the Sangam poet Nakkīrar to this temple too')])
 +talk("A court poet of the Vijayanagara king?","Dhūrjaṭi. He wrote verses so moving that the king asked where their sweetness came from.")))
pages.append(page('festivals','THROUGH THE YEAR','Its great days',facts([
 ('Mahāśivarātri','The great festival, a Brahmotsavam of about two weeks'),
 ('Kailāsagiri pradakṣiṇa','Walking around the hills during the festival'),
 ('Kārttika Somavāra','Mondays of Kārttika'),
 ('Daily','Rāhu–Ketu rites through the day')])))
pages.append(page('meaning','WHAT AIR TEACHES','The wisdom of breath',facts([
 ('Unseen presence','Air is felt, not seen; so is the divine'),
 ('Every breath','Vāyu’s boon: the life-breath in every creature is his'),
 ('Love over rule','The hunter’s devotion was worth more than the priest’s'),
 ('Equal before God','A spider, a snake and an elephant, all liberated')])
 +talk("What should I take from air?","Every breath you take is a gift. And love, like air, doesn't need to be seen to be real.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Vāyu','Air, wind'),('Karpūra','Camphor'),('Śrī · Kāla · Hasti','Spider · snake · elephant'),('Svayambhū','Self-manifest'),('Rāhu · Ketu','Shadow planets'),('Kavaca','Armour, covering'),('Aṣṭadiggaja','The eight poets of Kṛṣṇadevarāya’s court'),('Pātāla','Underground')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Element.</b> Air: the Vāyu liṅga and the lamp that flickers without wind.</div>
<div><b>Stories.</b> Vāyu’s penance; the spider, snake and elephant; Kaṇṇappa’s eyes.</div>
<div><b>Goddess.</b> Jñānaprasūnāmbā, mother of wisdom.</div>
<div><b>History.</b> Chola shrine, Kṛṣṇadevarāya’s 1516 tower, its fall in 2010.</div>
<div><b>Lesson.</b> Love, like breath, is the real offering.</div>
</div>'''+talk("One line to remember?","A hunter gave his eye; Śiva gave it back. That's Kāḷahasti.")+'<div class="key">Last element, space: <a href="'+PSS+'chidambaram/">Naṭarāja, Cidambaram</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Srikalahasteeswara temple” (Vāyu liṅga; Vāyu and the camphor liṅga; spider, snake and elephant; 1516 gopuram and hall by Kṛṣṇadevarāya; collapse 26 May 2010 and shallow foundation; liṅga’s markings); The Hindu and Deccan Herald (collapse; inquiry; crack 25 years earlier); Incredible India and The Hans India (the three creatures; marks on the liṅga; flickering lamp); AP municipal administration site.</p>
<p><b>Saints and poets:</b> Cēkkiḻār, <i>Periya Purāṇam</i> (Kaṇṇappa Nāyaṉār); Dhūrjaṭi, <i>Śrī Kāḷahastīśvara Śatakam</i>; Tēvāram.</p>
<p><b>Sources differ / unverified:</b> gopuram height (120, 135 or 136 ft); the custom of not touching the liṅga; staying open in eclipses; the Pātāla Gaṇapati depth; Nakkīrar’s link; rebuilding dates. Rāhu–Ketu and eclipse practices are described as beliefs. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('vayu','Vāyu’s Penance'),('three','Spider, Snake, Elephant'),('linga','The Vāyu Liṅga'),('kannappa','Kaṇṇappa, the Hunter'),('kannappa2','Why Kaṇṇappa Matters'),('goddess','Jñānaprasūnāmbā'),
 ('rahu','Rāhu–Ketu and Eclipses'),('temple','The Temple'),('gopuram','The Tower That Fell'),('poets','Poets of Kāḷahasti'),('festivals','Through the Year'),('meaning','What Air Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/PS4_Kalahastishvara.html',head,cov,fw,pages,toc)
