src=open('/home/claude/work/shakti/jogulamba.py').read()
exec(src.split("\ncover=(")[0])
head=head_red('Bhramarāmbikā · Śrīśailam · The 18 Śakti Pīṭhas · srini.presents',
 'Bhramarāmbikā of Śrīśailam, the sixth of the 18 Śakti Pīṭhas: the Goddess of bees who destroyed Aruṇāsura, the buzzing in the temple wall, Mallikārjuna beside her, Candravatī’s jasmine, Śivājī’s sword, and the Kumbhotsavam. An illustrated reference guide.')
import math
def BEE(x,y,s=1,r=0): return f'<g transform="translate({x} {y}) rotate({r}) scale({s})" stroke="#111" stroke-width="1.2"><ellipse rx="7" ry="4.5" fill="#ffd60a"/><path d="M-2 -4.5 v9 M2 -4.5 v9" stroke-width="2"/><ellipse cx="-2" cy="-6" rx="4" ry="3" fill="#dff3ff" opacity=".9"/><ellipse cx="3" cy="-6" rx="4" ry="3" fill="#dff3ff" opacity=".9"/><circle cx="8" r="2.4" fill="#111"/></g>'
def SWARM(cx,cy,n=24,rad=60,seed=3): return ''.join(BEE(cx+rad*math.cos(k*2.4+seed)*(0.3+(k%5)/6),cy+rad*0.6*math.sin(k*2.4+seed)*(0.3+(k%4)/5),.9,k*37%360) for k in range(n))
def BHRAM(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 60 q-4 -60 30 -70 q34 10 30 70z" fill="#c0392b"/><path d="M-26 52 q26 12 52 0" fill="none" stroke="#e0a800" stroke-width="4"/>'
 +''.join(f'<path d="M{d*16} {-4+k*9} l{d*(30-k*3)} {-14+k*8}" stroke="#f2c79b" stroke-width="5"/>' for d in (-1,1) for k in range(4))
 +'<circle cy="-22" r="12" fill="#f2c79b"/><path d="M-12 -32 h24 l-4 -16 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/><circle cx="-4" cy="-24" r="1.6" fill="#111"/><circle cx="4" cy="-24" r="1.6" fill="#111"/><path d="M-4 -16 q4 3 8 0" fill="none"/>'
 +'<path d="M-48 -26 l8 -12 M48 -26 l-6 -14" stroke="#bbb" stroke-width="3"/><circle cx="-50" cy="-8" r="5" fill="none" stroke="#e0a800" stroke-width="3"/></g>')
DGOP=lambda x,y,s=1,c='#f2e6c8': f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-34+k*3} {-k*12} h{68-k*6} l-1 -12 h{-(66-k*6)}z" fill="{c if k%2 else "#e2cfa8"}"/>' for k in range(7))+''.join(f'<path d="M{-14+j*5} -84 l2 -10 l2 10z" fill="#e0a800"/>' for j in range(7))+'<rect x="-9" y="-20" width="18" height="20" fill="#5a3a1a"/></g>'
WALL=lambda x,y,w,h: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#b8a888" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{x} {y+k*14} H{x+w}" stroke="#8a7a5a"/>' for k in range(1,int(h/14)))+''.join(f'<path d="M{x+((k%2)*20)+j*40} {y+k*14} v14" stroke="#8a7a5a"/>' for k in range(int(h/14)) for j in range(int(w/40)))
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The eight-armed Goddess Bhramaramba surrounded by a great swarm of golden bees, the temple tower on a forested hill behind her">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/>'+HILL(80,268,220,140,'#3a6a3a')+DGOP(70,150,.8)+SWARM(250,120,40,120)+BHRAM(220,160,1.5)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Bhramarāmbikā</b> (Bhramarāmbā), “Mother of the bees”: Pīṭha no. 6 of the eighteen'),
 ('Hymn line','<i>śrīśaile bhramarāmbikā</i>: “Bhramarāmbikā on Śrīśaila”'),
 ('Where','<b>Śrīśailam</b>, Andhra Pradesh, in the Nallamala hills above the Kṛṣṇā'),
 ('Body part','Satī’s <b>neck</b> (grīvā)'),
 ('Her Lord','<b>Mallikārjuna</b>, one of the twelve jyotirliṅgas, in the same temple complex'),
 ('Legend','She became a swarm of six-legged <b>bees</b> to destroy <b>Aruṇāsura</b>'),
 ('The wall','Pilgrims listen at the back wall of her shrine for the <b>hum of bees</b>'),
 ('The image','Eight-armed, with a <b>Śrī Yantra</b> before her'),
 ('Festivals','<b>Kumbhotsavam</b> in Caitra; nine-day <b>Dasara</b>; Mahāśivarātri with her Lord')])
 +talk("A goddess who turned into bees?","Thousands of them. A demon who couldn't be killed by anything with two or four legs met something with six.")))
pages.append(page('where','WHERE IT IS','The auspicious mountain',fig(560,280,'Simplified map of the Krishna and Tungabhadra rivers, with Srisailam marked in red on the Krishna gorge, Alampur upstream, Hyderabad to the north',
 APMAP([(16.07,78.87,'ŚRĪŚAILAM','l','#c0392b'),(15.88,78.13,'Alampur','r','#ffd166'),(17.39,78.49,'Hyderabad','r','#bbb'),(15.83,78.04,'Kurnool','l','#bbb')]))+'''<div class="panel reading">
<p><b>The hill.</b> Śrīśaila, “the auspicious mountain”, rises in the <b>Nallamala</b> forest above a deep gorge of the <b>Kṛṣṇā</b>. The river below is called <b>Pātālagaṅgā</b>, “the Gaṅgā of the underworld”, reached by a long flight of steps.</p>
<p><b>One complex.</b> Bhramarāmbā’s shrine and Mallikārjuna’s stand inside the same high walls.</p>
<p><b>Two pīṭhas in a row.</b> The hymn pairs her with <a href="/bhakti/temples-of-india/18-shakti-peethas/jogulamba/">Jogulāmbā of Alampur</a>, upstream, the “western gate” of Śrīśailam.</p>
</div>'''))
pages.append(page('names','HER NAMES','The Goddess of the bees',facts([
 ('Bhramarāmbā','<i>Bhramara</i>, the black bee, and <i>ambā</i>, mother: “Mother of bees”'),
 ('Bhrāmarī','Her name in the Devī Māhātmya and the Devī Bhāgavata'),
 ('Bhramarāmbikā','The hymn’s affectionate form: “little mother of bees”'),
 ('Brāhmaṇī Śakti','How the temple describes her power; she is also worshipped as <b>Mahālakṣmī</b>'),
 ('Śrīśaila','“The auspicious mountain”; in the epics, <b>Śrīparvata</b>')])
 +talk("Bhramara is a bee?","The big black bee that hums around flowers. Her name is literally a buzz.")))
pages.append(page('pitha','THE PĪṬHA','Where Satī’s neck fell',fig(560,150,'Shiva carrying Sati across a night sky, a glowing piece falling onto a forested hill above a river gorge',
 '<rect width="560" height="150" fill="#2a0805"/>'+STAR+SHIVA(140,60,.7)+SATI(162,64,.55,-10)+'<path d="M190 80 q80 10 190 40" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><circle cx="382" cy="120" r="6" fill="#ffd166"/>'+HILL(440,150,200,60,'#3a6a3a')+'<path d="M340 150 q100 -14 220 0" stroke="#4aa3df" stroke-width="5" fill="none"/>'+T(440,24,'ŚRĪŚAILA',14,'#ffd166'))+'''<div class="panel reading">
<p><b>The verse.</b> <i>śrīśaile bhramarāmbikā</i>: sixth in the hymn, right after Alampur.</p>
<p><b>What fell here.</b> Satī’s <b>neck</b>. In the 52-pīṭha lists too, Śrīśaila is counted.</p>
<p><b>Śiva and Śakti together.</b> Śrīśailam is often called the one temple where a <b>jyotirliṅga</b> and a <b>Śakti Pīṭha</b> share a single complex. Kāśī and Ujjain have both too, but in separate temples.</p>
</div>'''))
pages.append(page('goddess','THE GODDESS','Eight arms and a Śrī Yantra',fig(560,220,'The eight-armed Goddess holding weapons, in a silk sari and gold ornaments, with a Sri Yantra in front and bees around her',
 '<rect width="560" height="220" fill="#fde4e4"/><rect x="170" y="10" width="220" height="200" fill="#fff4cd" stroke="#111" stroke-width="2"/>'+SWARM(280,90,14,90)+BHRAM(280,120,1.6)
 +'<g transform="translate(470 120)" stroke="#111" stroke-width="1.5"><rect x="-44" y="-44" width="88" height="88" fill="#fff4cd"/><circle r="36" fill="#fde4e4"/>'+''.join(f'<path d="M0 {-30+k*6} L{26-k*5} {16-k*3} L{-26+k*5} {16-k*3}z" fill="none" stroke="#c0392b"/>' for k in range(3))+'</g>'+T(470,186,'ŚRĪ YANTRA',11,'#7a1d12'))+'''<div class="g2">
<div class="card bg-red"><h4>⚔️ Eight arms</h4><p>She is shown as a warrior Goddess with <b>eight arms</b>, each with a weapon, dressed in a silk sari and gold.</p></div>
<div class="card bg-yellow"><h4>🔯 The Śrī Yantra</h4><p>A <b>Śrī Yantra</b> is installed in front of her sanctum: the sign of the Goddess as Lalitā, as at Kāñcī.</p></div>
</div><div class="panel reading small"><p><b>Many faces.</b> In Navarātri she is dressed in turn as different Goddesses, among them Kālarātri, Rājarājeśvarī and Mahāgaurī.</p></div>'''))
pages.append(page('aruna','THE LEGEND · ARUṆĀSURA','Death on six legs',fig(560,200,'A demon with a boon scroll surrounded and overwhelmed by a huge swarm of bees, the Goddess directing them from a hilltop',
 '<rect width="560" height="200" fill="#ffe9c4"/>'+HILL(120,200,200,90,'#5a8a4a')+BHRAM(120,96,.7)+'<g transform="translate(400 170)">'+DEMON(0,0,1.6,'#3a2a5a')+'</g>'+SWARM(400,110,46,110,1)
 +'<rect x="440" y="150" width="40" height="22" fill="#fff4cd" stroke="#111"/>'+T(460,166,'2 · 4',10,'#111'))+'''<div class="steps">
<div><b>The boon.</b> The demon <b>Aruṇa</b> did fierce penance to Brahmā and won a boon: no creature with <b>two or four legs</b> could kill him. He drove the gods from heaven.</div>
<div><b>The loophole.</b> The gods prayed to the Goddess. She appeared surrounded by <b>bees</b>, which have <b>six legs</b>, and sent out swarm upon swarm.</div>
<div><b>The end.</b> The bees covered Aruṇāsura and his army and destroyed them. The Goddess, now <b>Bhrāmarī</b>, settled on Śrīśaila as Bhramarāmbā beside Mallikārjuna.</div>
</div>'''+talk("So the boon had a gap the size of a bee?","Every demon's boon has a gap. The Goddess always finds it.")))
pages.append(page('texts','IN THE TEXTS','A form foretold',fig(560,120,'An open palm-leaf manuscript with a bee drawn in its margin',
 '<rect width="560" height="120" fill="#fff4cd"/><rect x="120" y="30" width="320" height="60" rx="8" fill="#f3e3c3" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M140 {44+k*10} H420" stroke="#7a5a2a"/>' for k in range(4))+'<circle cx="160" cy="60" r="4" fill="#111"/><circle cx="400" cy="60" r="4" fill="#111"/>'+BEE(450,30,2,-20))+facts([
 ('Devī Māhātmya','In its eleventh chapter the Goddess foretells her own future forms. One of them: she will take the form of countless <b>bees</b> to slay the demon <b>Aruṇa</b>, and the world will call her <b>Bhrāmarī</b>'),
 ('Devī Bhāgavata','Tells the Aruṇāsura story in full, with Brahmā’s boon and the swarm'),
 ('Lakṣmī Tantra','Lakṣmī herself declares that she is Bhrāmarī'),
 ('Yoga','<b>Bhrāmarī prāṇāyāma</b>, the humming breath, is named after the bee')])
 +'<div class="panel reading small"><p>Read the prophecy in our <a href="/bhakti/devi/devi-mahatmya/">Devī Māhātmya</a> series.</p></div>'))
pages.append(page('hum','THE HUMMING WALL','Listen at the back of the shrine',fig(560,190,'A pilgrim pressing an ear to the stone wall behind the shrine, sound waves and small bees drawn inside the wall',
 '<rect width="560" height="190" fill="#fdf1e8"/>'+WALL(220,20,240,160)+''.join(BEE(260+k*44,60+(k%3)*36,.8,k*30) for k in range(5))+''.join(f'<path d="M{200-k*12} {80+k*2} q-10 20 0 40" stroke="#c0392b" stroke-width="2" fill="none"/>' for k in range(3))+person(140,150,'#2a7a4a','#c98b5a',1.1))+'''<div class="panel reading">
<p><b>The tradition.</b> Pilgrims put an ear to a small opening in the wall behind Bhramarāmbā’s shrine and listen. Many say they hear a low <b>humming</b>, like bees.</p>
<p><b>Two explanations.</b> Devotees hear the Goddess’s bees, still with her. Others say real bees have nested in the old granite walls. Either way, they have a good name: by every account, they have never stung a pilgrim.</p>
</div>'''+talk("Did you hear it?","Put your own ear to the wall one day and decide. That's the only fair test.")))
pages.append(page('jasmine','THE LEGEND · CANDRAVATĪ','The jasmine princess',fig(560,170,'A princess offering a jasmine garland to a natural rock lingam on which a cow pours milk, forest around',
 '<rect width="560" height="170" fill="#eef6e4"/>'+HILL(460,170,220,120,'#3a7a3a')+'<path d="M260 160 q-4 -40 20 -48 q24 8 20 48z" fill="#8a8a8a" stroke="#111" stroke-width="2"/>'+GENTLE(160,100,.9)+'<path d="M190 96 q40 -30 80 0" stroke="#fff" stroke-width="6" fill="none" stroke-dasharray="2 4"/>'
 +'<g transform="translate(360 150)" stroke="#111" stroke-width="2"><ellipse rx="36" ry="16" fill="#fff"/><circle cx="-36" cy="-8" r="10" fill="#fff"/><circle cx="6" cy="-4" r="6" fill="#111"/><path d="M-40 8 q-20 -10 -60 -6" stroke="#f4f4f4" stroke-width="3" fill="none"/></g>'+T(160,166,'CANDRAVATĪ',11,'#7a1d12'))+'''<div class="steps">
<div><b>A princess in the forest.</b> <b>Candravatī</b>, daughter of a king across the Kṛṣṇā, fled her home and settled on this hill with a few servants.</div>
<div><b>The cow.</b> She saw a cow pour its milk over a rock shaped like a liṅga. In a dream she learned it was Śiva, the Lord of Śrīparvata, and began to worship him.</div>
<div><b>The jasmine.</b> Every day she offered him garlands of <b>mallikā</b>, jasmine. When Śiva appeared, she asked him to wear her jasmine always. So he is <b>Mallikārjuna</b>.</div>
</div><div class="panel reading small"><p>The better-known story of how Śiva and Pārvatī came here to be near their son Kārttikeya is in our <a href="/bhakti/temples-of-india/12-jyotirlingas/mallikarjuna/">Mallikārjuna</a> guide.</p></div>'''))
pages.append(page('shivaji','ŚIVĀJĪ AND THE SWORD','A king at her feet, 1677',fig(560,170,'A Maratha king kneeling before the Goddess, who hands him a sword',
 '<rect width="560" height="170" fill="#fff4cd"/>'+BHRAM(380,100,1.1)+'<g transform="translate(220 150)">'+person(0,0,'#ff8c1a','#c98b5a',1.2)+'</g><path d="M246 100 L330 70" stroke="#ccc" stroke-width="5"/><path d="M200 102 h40 l-6 -10 h-28z" fill="#ff8c1a" stroke="#111"/>'+T(220,166,'ŚIVĀJĪ',12,'#7a1d12'))+'''<div class="steps">
<div><b>The visit.</b> In <b>1677</b>, during his southern campaign, the Maratha king <b>Śivājī</b> came to Śrīśailam.</div>
<div><b>The sword.</b> Tradition says the Goddess blessed his sword, and that it brought him victory after victory. A sculpture in the temple shows him kneeling before her to receive it.</div>
<div><b>His gift.</b> Śivājī is remembered as a builder here too: the <b>northern gopura</b> is credited to him.</div>
</div>'''+talk("The bee goddess gave Śivājī his sword?","That's the story Śrīśailam tells. The Marathas had their own Bhavānī of Tuljāpur too; it seems one goddess wasn't enough.")))
pages.append(page('history','HISTORY','Kings of the auspicious mountain',tl([
 ('2nd c.','<b>Sātavāhana</b> inscriptions are the earliest evidence of the shrine.'),
 ('Epics','The hill is praised as <b>Śrīparvata</b>, a great tīrtha.'),
 ('12th–14th c.','The <b>Kākatīyas</b> and then the <b>Reḍḍi</b> kings, devotees of “Bhramarāmbā Mallikārjuna”, build halls and the steps to Pātālagaṅgā.'),
 ('14th–15th c.','<b>Vijayanagara</b> kings, beginning with Harihara I, make most of the later additions.'),
 ('1677','<b>Śivājī</b> visits; the north gopura is credited to him.'),
 ('Today','The complex is run by the Śrīśaila Devasthānam; the Kṛṣṇā below is held by the Śrīśailam dam.')])
 +'<div class="panel reading small"><p>The Mallikārjuna guide covers the complex’s history in more detail.</p></div>'))
pages.append(page('kumbha','THE KUMBHOTSAVAM','Her own great day',fig(560,170,'Heaps of pumpkins, coconuts and lemons before the Goddess, a mound of rice, and forest people dancing',
 '<rect width="560" height="170" fill="#ffe9c4"/>'+BHRAM(100,90,.8)+''.join(f'<circle cx="{200+(k%8)*20}" cy="{150-(k//8)*16}" r="9" fill="{["#ffd60a","#e8a33a","#8a5a2a"][k%3]}" stroke="#111"/>' for k in range(24))
 +'<path d="M380 160 q40 -60 80 0z" fill="#fff" stroke="#111" stroke-width="2"/>'+''.join(person(x,150,'#2a7a4a','#7a4a2a',.7) for x in (500,535)))+'''<div class="steps">
<div><b>When.</b> The first Tuesday or Friday after the full moon of <b>Caitra</b>, at the start of the year.</div>
<div><b>Behind closed doors.</b> Priests worship the Goddess alone with the Navāvaraṇa, Triśatī and Khaḍgamālā rites; ordinary darśan pauses. Mallikārjuna is covered in <b>curd rice</b> and his doors stay shut until the next morning.</div>
<div><b>The offering.</b> She is smeared with turmeric and kuṅkuma and given a <b>sāttvika bali</b>, a “pure sacrifice”: heaps of cooked rice, broken <b>pumpkins</b>, coconuts, and more than <b>fifty thousand lemons</b>.</div>
<div><b>Kumbhārati.</b> In the evening a man dressed in a sari offers the lamp, and the doors open. The forest-dwelling <b>Cheñcu</b> people dance for her.</div>
</div>'''))
pages.append(page('festivals','THROUGH THE YEAR','Her other festivals',facts([
 ('Dasara','Nine days with Caṇḍī-yāga and Rudra-yāga, and the Goddess dressed as the nine Durgās'),
 ('Mahāśivarātri','The great festival of Mallikārjuna, when she is honoured with him'),
 ('Ugādi','The Telugu New Year, when pilgrims walk in from Karnataka and Maharashtra'),
 ('Kārtika','The month of lamps'),
 ('Fridays','Her weekly day; married women pray to her for the family')])
 +talk("Does the whole hill celebrate together?","Śiva's nights and the Goddess's nights. Śrīśailam is busy all year.")))
pages.append(page('akka','AKKA MAHĀDEVĪ','A poet who came to the mountain',fig(560,140,'A young woman saint walking through forest towards a cave by the river',
 '<rect width="560" height="140" fill="#eef6e4"/>'+HILL(420,140,260,110,'#3a7a3a')+'<ellipse cx="430" cy="120" rx="40" ry="20" fill="#2a1a0a"/>'+person(200,120,'#f4f4f4','#c98b5a',1)+'<path d="M180 70 q20 -10 40 0" stroke="#2b1a0e" stroke-width="6" fill="none"/><rect y="128" width="560" height="12" fill="#4aa3df"/>')+'''<div class="panel reading">
<p><b>The saint.</b> <b>Akka Mahādevī</b>, the 12th-century Kannada poet-saint of the Vīraśaiva movement, gave up everything for Śiva, whom she called “Cennamallikārjuna”, the beautiful Lord white as jasmine.</p>
<p><b>Her end.</b> Tradition says she came to Śrīśaila and lived her last days in a <b>cave</b> above the Kṛṣṇā, now called the Akka Mahādevī caves.</p>
<p><b>Why here.</b> Her vacanas are poems of love to Mallikārjuna; this is his mountain, and the Goddess beside him is the Mother she sought.</p>
</div>'''))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Bhramara','The black bee'),('Bhrāmarī','The Goddess as bees; also a humming breath'),('Grīvā','Neck'),('Śrīśaila','The auspicious mountain'),('Pātālagaṅgā','The Kṛṣṇā in the gorge below'),
 ('Mallikā','Jasmine'),('Sāttvika bali','A “pure” offering of food and fruit'),('Kumbhārati','The lamp offering of the Kumbhotsavam'),('Cheñcu','A forest people of the Nallamala'),('Vacana','A Kannada devotional verse')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Goddess.</b> Bhramarāmbikā, Mother of bees, eight-armed, with a Śrī Yantra before her; Satī’s neck fell here.</div>
<div><b>The legend.</b> Aruṇāsura’s boon left out six-legged creatures; she became a swarm of bees.</div>
<div><b>The place.</b> Śrīśailam, with Mallikārjuna beside her: a jyotirliṅga and a pīṭha in one complex.</div>
<div><b>The stories.</b> The humming wall, Candravatī’s jasmine, Śivājī’s sword, Akka Mahādevī’s cave.</div>
<div><b>The festival.</b> The Kumbhotsavam in Caitra: lemons, pumpkins, curd rice and closed doors.</div>
</div>'''+talk("One line to remember?","A boon that forgot about bees. Never underestimate the small ones.")+'<div class="key">The sixth seat of the Mother: <b>Bhramarāmbikā of Śrīśaila</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Mallikarjuna Temple, Srisailam”: Bhramarāmbā as Mallikārjuna’s consort; neck; 18 and 52 pīṭha lists; Sātavāhana inscriptions; Reḍḍi kings and the Pātālagaṅgā steps; Harihara I. Wikipedia, “Bhramari” (Aruṇāsura; Lakṣmī Tantra; Bhrāmarī prāṇāyāma). tirthayatra.org: eight arms, silk sari, Śrī Yantra; Navarātri forms; Śivājī and the sword in 1677; Akka Mahādevī caves; the Kumbhotsavam (timing, rites, curd rice, sāttvika bali with lemons and pumpkins, Kumbhārati, Cheñcu dance); Dasara; the Candravatī legend. hindu-blog.com (the two- and four-legged boon; eight arms; married women’s worship). trawell.in and behindeverytemple.org (the humming wall; bees that never sting). Our <a href="/bhakti/temples-of-india/12-jyotirlingas/mallikarjuna/">Mallikārjuna</a> guide (Kākatīyas; Śivājī’s north gopura; Ugādi walkers).</p>
<p><b>Not verified:</b> the source of the humming (devotional tradition and local explanation); the Śivājī sword story (temple tradition); the Candravatī legend (local tradition). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('goddess','The Goddess'),('aruna','Legend · Aruṇāsura'),('texts','In the Texts'),('hum','The Humming Wall'),('jasmine','Legend · Candravatī'),
 ('shivaji','Śivājī and the Sword'),('history','History'),('kumbha','The Kumbhotsavam'),('festivals','Through the Year'),('akka','Akka Mahādevī'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 6 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,6.6vw,68px)">BHRAMARĀMBIKĀ</h1>
  <div class="series">ŚRĪŚAILAM · A REFERENCE GUIDE</div>
  <div class="tag">The Mother of the bees</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>High on the auspicious mountain, above the gorge of the Kṛṣṇā, Śiva as <b>Mallikārjuna</b> shares his temple with the Goddess: <b>Bhramarāmbikā</b>, the Mother of bees.</p>
    <p>She defeated a demon whom nothing with two or four legs could kill, by becoming a swarm of six-legged bees. Pilgrims still press an ear to her temple wall to hear them hum.</p>
    <p>This guide tells her story, the princess who gave Śiva his jasmine name, the king who knelt for a sword, and the great Kumbhotsavam.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Bhramarāmbā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Isn't Śrīśailam Śiva's place?","It's both of theirs. One complex, a jyotirliṅga and a Śakti Pīṭha, side by side.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Bhramaramba.html','w').write(head+b+tail())
print('ok',len(pages))
