exec(open('/home/claude/work/shakti/common_s.py').read())
src=open('/home/claude/work/shakti/chardham.py').read()
exec('def uk('+src.split('def uk(')[1].split('\ncover=(')[0])
head=head_red('Yamunotrī · Source of the Yamunā · srini.presents',
 'Yamunotrī, the westernmost of the Himalayan Char Dham: the goddess Yamunā, daughter of the Sun and sister of Death; the hot springs of Sūrya Kuṇḍa and the Divya Śilā; the sage Asita; Kālindī and Kṛṣṇa; Bhāī Dūj and her brother Śani at Kharsālī; who built the temple. An illustrated reference guide.')
def YAMUNA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 60 q-4 -60 30 -70 q34 10 30 70z" fill="#3b4fa0"/>'
 '<circle cy="-24" r="16" fill="#4a5a9a"/><path d="M-16 -30 q16 -24 32 0" fill="#111"/><circle cx="-5" cy="-24" r="2" fill="#111"/><circle cx="5" cy="-24" r="2" fill="#111"/><path d="M-5 -16 q5 3 10 0" fill="none"/>'
 '<path d="M-12 -40 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800"/><path d="M-26 0 l-20 -16 M26 0 l20 -16" stroke="#4a5a9a" stroke-width="7"/><circle cx="-48" cy="-18" r="7" fill="#f2a6b0"/>'
 '<g transform="translate(0 70)"><path d="M-40 0 q20 -20 40 0 q20 20 40 0" fill="none" stroke="#2a9d6f" stroke-width="3"/><path d="M30 -4 l14 4 l-14 4z" fill="#2a9d6f"/></g></g>')
SUN=lambda x,y,r=26: f'<g transform="translate({x} {y})"><circle r="{r}" fill="#ffd166" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M0 {-r-4} v-12" stroke="#ff8c1a" stroke-width="4" transform="rotate({a})"/>' for a in range(0,360,30))+'</g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The dark river goddess Yamuna on a turtle beside a small Himalayan temple, steam rising from a hot spring, the sun above a snowy peak">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/><path d="M180 140 l100 -120 l100 120z" fill="#fff" stroke="#888"/>'+SUN(320,50,20)
 +'<path d="M0 250 Q190 224 380 250 V268 H0z" fill="#4aa3df"/>'+TEMPLE(300,236,1,'#ffe1a8')+YAMUNA(120,160,1.2)
 +'<ellipse cx="220" cy="240" rx="26" ry="8" fill="#bfe3f0" stroke="#111"/>'+''.join(f'<path d="M{210+i*10} 232 q-6 -14 0 -26" stroke="#ddd" stroke-width="3" fill="none"/>' for i in range(3))+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Yamunā</b>: the river as a goddess, dark-skinned, riding a <b>turtle</b>'),
 ('Family','Daughter of <b>Sūrya</b> the Sun and <b>Saṃjñā</b>; twin sister of <b>Yama</b>, god of death'),
 ('Where','Uttarkashi district, Uttarakhand, about 3,200 m up, on a flank of <b>Bandarpūñch</b>'),
 ('The source','The <b>Champāsar glacier</b> on <b>Kalinda Parvata</b>, a little above the temple and hard to reach'),
 ('Springs','<b>Sūrya Kuṇḍa</b>, near boiling: pilgrims cook rice and potatoes in it'),
 ('Char Dham','The first and westernmost of the Himalayan four'),
 ('Season','Open from about <b>Akṣaya Tṛtīyā</b> to <b>Bhāī Dūj</b>; in winter she lives at <b>Kharsālī</b>')])
 +talk("A river goddess who is Death's sister?","And the Sun's daughter. Bathe in her, they say, and her brother will be kind to you.")))
pages.append(page('where','WHERE IT IS','The westernmost Dhām',fig(560,330,'Simplified map of Garhwal: Yamunotri at the head of the Yamuna in the west, Gangotri, Kedarnath and Badrinath further east',UKMAP())
 +'''<div class="panel reading"><p><b>Far west of the four.</b> Yamunotrī sits at the head of the Yamunā valley, on the western flank of the <b>Bandarpūñch</b> massif. Pilgrims usually start the Himalayan Char Dham here and go east.</p>
<p><b>The real source.</b> The river is born a little higher, on the <b>Champāsar glacier</b> below Kalinda Parvata. The way up is so hard that worship is done at the temple below.</p></div>'''))
pages.append(page('family','THE SUN’S CHILDREN','Yamunā, Yama and Śani',fig(560,180,'The sun with three children: a dark river goddess, a stern god of death holding a noose, and a dark god on a crow',
 '<rect width="560" height="180" fill="#fff4cd"/>'+SUN(280,46,30)+YAMUNA(140,110,.8)+f'<g transform="translate(280 160)">'+person(0,0,'#7a1d12','#4a5a9a',1.1)+'<path d="M22 -10 q20 -20 0 -40 q-14 6 0 20" stroke="#111" stroke-width="2" fill="none"/></g>'+f'<g transform="translate(430 160)">'+person(0,0,'#1a1a3a','#3a3a5a',1)+'<path d="M24 -2 l20 -6 l-6 12z" fill="#111"/></g>'
 +T(140,176,'YAMUNĀ',11,'#7a1d12')+T(280,176,'YAMA',11,'#7a1d12')+T(430,176,'ŚANI',11,'#7a1d12'))+'''<div class="steps">
<div><b>The parents.</b> <b>Sūrya</b>, the Sun, married <b>Saṃjñā</b>. She could not bear his blazing light and could not meet his eyes.</div>
<div><b>The twins.</b> Their children were <b>Yama</b>, who became lord of the dead, and his twin sister <b>Yamī</b>, who became the river <b>Yamunā</b>.</div>
<div><b>The shadow.</b> When Saṃjñā left, her shadow <b>Chāyā</b> took her place and bore <b>Śani</b> (Saturn). So Śani is Yamunā’s half-brother.</div>
<div><b>Kālindī.</b> The mountain at the source is <b>Kalinda</b>, a name of the Sun; so Yamunā is also <b>Kālindī</b>, “daughter of Kalinda”.</div>
</div>'''))
pages.append(page('bhaidooj','YAMA DVITĪYĀ','The brother who came to dinner',fig(560,160,'A sister marking her brother’s forehead with a tilaka and feeding him, a lamp between them',
 '<rect width="560" height="160" fill="#fdf1e8"/>'+person(200,130,'#3b4fa0','#4a5a9a',1.2)+person(360,130,'#7a1d12','#4a5a9a',1.2)+'<path d="M220 90 l120 -14" stroke="#4a5a9a" stroke-width="5"/><circle cx="352" cy="70" r="4" fill="#c0392b"/><path d="M270 150 l10 -16 l10 16z" fill="#ffd60a" stroke="#111"/><path d="M280 134 q-4 -10 0 -16 q4 6 0 16" fill="#ff8c1a"/>')+'''<div class="steps">
<div><b>The visit.</b> Yamunā longed for her brother to visit. At last, on the second day after Dīpāvalī, Yama came. She marked his brow, fed him, and asked a boon.</div>
<div><b>The boon.</b> “Any brother who visits his sister on this day, and any who bathes in my waters, need not fear you.” Yama agreed.</div>
<div><b>Bhāī Dūj.</b> So began <b>Yama Dvitīyā</b>, Bhāī Dūj or Bhāū Bīj, when sisters across India mark their brothers’ foreheads.</div>
<div><b>At Yamunotrī.</b> Bhāī Dūj is also the day Yamunotrī closes for winter.</div>
</div>'''+talk("So Bhāī Dūj started here?","With these two siblings, by the legend. Every tilaka on that day echoes Yamunā's.")))
pages.append(page('kalindi','KĀLINDĪ AND KṚṢṆA','The river of Vraja',facts([
 ('Kṛṣṇa’s river','Far downstream, the Yamunā flows past <b>Mathurā</b> and <b>Vṛndāvana</b>: the river of Kṛṣṇa’s childhood'),
 ('Kāliya','Where Kṛṣṇa danced on the serpent Kāliya and drove him from her waters'),
 ('A queen','In the Bhāgavata, <b>Kālindī</b> did penance by the river and became one of Kṛṣṇa’s eight chief queens'),
 ('Puṣṭimārga','Vallabhācārya’s <b>Yamunāṣṭaka</b> praises her as the one who brings souls to Kṛṣṇa'),
 ('Prayāga','At the end she meets the Gaṅgā and the hidden Sarasvatī at Prayāga')])
 +talk("Why is the Yamunā dark?","Her mother couldn't face the Sun's glare; the daughter carries the shadow. Kṛṣṇa, the dark one, loved her for it.")))
pages.append(page('asita','THE SAGE ASITA','Gaṅgā came to him',fig(560,160,'An old sage seated by a spring, with two streams, one blue-dark and one white, flowing beside him',
 '<rect width="560" height="160" fill="#e6eef8"/>'+HILL(120,160,240,120,'#3a7a3a')+HILL(440,160,240,120,'#3a7a3a')+'<path d="M250 0 Q240 80 260 160" stroke="#3b4fa0" stroke-width="12" fill="none"/><path d="M330 0 Q340 80 320 160" stroke="#fff" stroke-width="10" fill="none"/>'+person(290,150,'#ff8c1a','#d8b090',1))+'''<div class="steps">
<div><b>His hermitage.</b> The sage <b>Asita</b> is said to have lived here, bathing every day in both the Yamunā and the Gaṅgā.</div>
<div><b>Too old to walk.</b> When age stopped him crossing the mountains to the Gaṅgā, a stream of the Gaṅgā is said to have appeared beside the Yamunā for him.</div>
</div>'''+talk("A river came to an old man?","A holy one did. Faith that strong moves water.")))
pages.append(page('temple','THE TEMPLE','Rebuilt by snow and flood',fig(560,180,'A small temple with a pointed roof on a riverbank in a narrow valley, with a hot spring and a rock pillar beside it',
 '<rect width="560" height="180" fill="#cfe3f5"/>'+HILL(80,180,220,170,'#3a7a3a')+HILL(480,180,220,170,'#3a7a3a')+'<path d="M300 0 V180" stroke="#4aa3df" stroke-width="10"/>'+TEMPLE(220,160,1.3,'#ffe1a8')+'<ellipse cx="380" cy="160" rx="30" ry="10" fill="#bfe3f0" stroke="#111"/><rect x="420" y="120" width="16" height="44" fill="#8a7a6a" stroke="#111"/>'+T(428,112,'DIVYA ŚILĀ',9,'#555'))+facts([
 ('Image','A black stone image of Yamunā; a silver image too; Gaṅgā is worshipped beside her'),
 ('Builder','Disputed: a ruler of <b>Tehri Garhwal</b> (Sudarśan Śāh, 1839, or Pratāp Śāh), and/or <b>Mahārānī Guleriā</b> of Jaipur'),
 ('Damaged','Twice destroyed by snow and flood in the 19th century and rebuilt'),
 ('Priests','From <b>Kharsālī</b>, the village below')])
 +talk("Nobody knows who built it?","Several people did, one after another. In the Himalaya, every temple is a rebuild.")))
pages.append(page('springs','SŪRYA KUṆḌA AND THE DIVYA ŚILĀ','Cooking in the Sun’s spring',fig(560,160,'A boiling hot spring with pilgrims lowering small cloth bundles of rice into it',
 '<rect width="560" height="160" fill="#fdf1e8"/><ellipse cx="280" cy="120" rx="120" ry="30" fill="#bfe3f0" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{220+i*30} 100 q-6 -20 0 -40" stroke="#ccc" stroke-width="4" fill="none"/>' for i in range(5))
 +person(130,150,'#c0392b','#c98b5a',1)+person(430,150,'#2a9d6f','#c98b5a',1)+'<path d="M150 110 l60 0" stroke="#7a5a2a" stroke-width="2"/><circle cx="212" cy="118" r="8" fill="#fff" stroke="#111"/><path d="M410 110 l-60 0" stroke="#7a5a2a" stroke-width="2"/><circle cx="348" cy="118" r="8" fill="#fff" stroke="#111"/>')+facts([
 ('Sūrya Kuṇḍa','The hottest spring, named after Yamunā’s father: water close to boiling'),
 ('Prasāda','Rice and potatoes tied in muslin are dipped in it and cooked, then offered and taken home'),
 ('Gaurī Kuṇḍa','A milder spring where pilgrims bathe'),
 ('Divya Śilā','A rock pillar near Sūrya Kuṇḍa, worshipped <b>first</b>, before the goddess'),
 ('Others','Some accounts list five kuṇḍas: Sūrya, Tapta, Yamunā, Viṣṇu and Brahma')])))
pages.append(page('kharsali','KHARSĀLĪ','Winter with her brother',facts([
 ('Village','Kharsālī, below Yamunotrī: home of her priests'),
 ('Śani','A temple of <b>Śani</b>, held to be Yamunā’s brother, stands here'),
 ('Closing','On <b>Bhāī Dūj</b> her image is carried down from Yamunotrī to Kharsālī'),
 ('Opening','Around <b>Akṣaya Tṛtīyā</b> in spring, she is carried back up'),
 ('Escort','Tradition has Śani’s palanquin escorting his sister each way')])
 +talk("She spends winter at her brother's?","On Bhāī Dūj, of all days. Even the calendar is a family story here.")))
pages.append(page('meaning','WHY PILGRIMS COME','The first of four',facts([
 ('No untimely death','A bath in the Yamunā is said to keep Yama away until one’s time'),
 ('First stop','The Himalayan Char Dham traditionally begins here, west to east'),
 ('A sister’s blessing','Brothers and sisters come together, especially near Bhāī Dūj'),
 ('Purification','Her waters are held to cleanse sin; even the sight of her is blessed')])))
pages.append(page('connect','HOW IT CONNECTS','Rivers and lists',facts([
 ('Chota Char Dham','First of Yamunotrī, Gaṅgotrī, Kedārnāth, Badrīnāth'),
 ('Mathurā','Downstream: one of the <a href="/bhakti/temples-of-india/sapta-puri/">Saptapurī</a>, Kṛṣṇa’s birthplace, on her bank'),
 ('Prayāga','Where she joins the Gaṅgā; also a Śakti Pīṭha, Mādhaveśvarī'),
 ('Gaṅgotrī','Her sister source, across the ridge to the east')])
 +'<div class="key">More: <a href="/bhakti/temples-of-india/char-dham/">Char Dham, the two circuits</a></div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Yamunā · Yamī','The river goddess'),('Kālindī','Daughter of Kalinda (the Sun)'),('Kūrma','Turtle, her mount'),('Kuṇḍa','Spring, pool'),('Śilā','Rock'),
 ('Yama Dvitīyā','Bhāī Dūj, the second day after Dīpāvalī'),('Akṣaya Tṛtīyā','A spring festival day when the shrine opens'),('Chāyā','Shadow; Śani’s mother')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The goddess.</b> Yamunā: daughter of the Sun, twin of Yama, half-sister of Śani, beloved of Kṛṣṇa.</div>
<div><b>The place.</b> The westernmost Himalayan Dhām, below the glacier where she rises.</div>
<div><b>The springs.</b> Sūrya Kuṇḍa cooks the pilgrims’ rice; the Divya Śilā is worshipped first.</div>
<div><b>The festival.</b> Bhāī Dūj began with her, and on Bhāī Dūj she goes to winter with Śani at Kharsālī.</div>
<div><b>The blessing.</b> Bathe in her, and Death is kind.</div>
</div>'''+talk("One line to remember?","The Sun's dark daughter, who made Death promise to be gentle.")+'<div class="key">Jai Yamunā Maiyā! 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Shrine:</b> Wikipedia, “Yamunotri” (altitude; Bandarpūñch; westernmost shrine; temple built 1839 by Sudarśan Śāh; earlier small shrine; Pratāp Śāh; Mahārānī Guleriā of Jaipur; Sūrya Kuṇḍa, Divya Śilā, rice and potatoes in muslin; Champāsar glacier on Kalinda Parvata; sage Asita). Shri Badarinath–Kedarnath Temple Committee website (temple by Pratāp Śāh; priests from Kharsālī). shubhpanchang.com (Śani at Kharsālī as Yamunā’s brother; escort of her image; Gaurī Kuṇḍa; Guleriā rebuilding). ghumakkar.com (five kuṇḍas). bhaktikalpa.com (temple destroyed twice in the 19th c.; Asita and the Gaṅgā stream).</p>
<p><b>Legends:</b> Mārkaṇḍeya and other Purāṇas on Sūrya, Saṃjñā, Chāyā, Yama, Yamī and Śani; Bhāgavata Purāṇa on Kāliya and Kālindī; Vallabhācārya, Yamunāṣṭaka.</p>
<p><b>Sources differ:</b> who built the temple and when (Sudarśan Śāh 1839 or 1850, Pratāp Śāh, Mahārānī Guleriā, Narendra Śāh); the number of kuṇḍas. <b>Not verified, tradition only:</b> Śani’s palanquin as escort; the bath sparing untimely death. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('family','The Sun’s Children'),('bhaidooj','Yama Dvitīyā'),('kalindi','Kālindī and Kṛṣṇa'),('asita','The Sage Asita'),('temple','The Temple'),('springs','Sūrya Kuṇḍa and the Divya Śilā'),
 ('kharsali','Kharsālī'),('meaning','Why Pilgrims Come'),('connect','How It Connects'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
bk=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">SOURCE OF THE YAMUNĀ</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">YAMUNOTRĪ</h1>
  <div class="series">CHAR DHAM · A REFERENCE GUIDE</div>
  <div class="tag">The Sun’s daughter, Death’s sister</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>High in the western Garhwal Himalaya, a glacier melts into a dark, fast stream. That stream is a goddess: <b>Yamunā</b>, daughter of the Sun, twin sister of Yama, the god of death.</p>
    <p>At her small temple, pilgrims cook rice in a spring hot enough to boil it, and pray that her brother will be gentle with them. Every Bhāī Dūj, the festival she is said to have begun, she leaves for the winter to stay with her other brother, Śani, in the village below.</p>
    <p>This guide tells her family story, her shrine and her springs.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Yamunā Maiyā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is this the same Yamunā that flows through Delhi and Āgrā?","The very same, just born. Here she's a mountain stream; by Prayāga she's a great river meeting the Gaṅgā.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Yamunotri.html','w').write(head+bk+tail())
print('ok',len(pages))
