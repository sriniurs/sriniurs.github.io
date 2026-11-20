src=open('/home/claude/work/shakti/kolhapur.py').read()
exec(src.split("\ncover=(")[0])
head=head_red('Ekavīrikā · Reṇukā of Māhur · The 18 Śakti Pīṭhas · srini.presents',
 'Ekavīrikā of Māhur, the eighth of the 18 Śakti Pīṭhas: Reṇukā, mother of Paraśurāma, worshipped as a face on Māhur hill; the beheading and revival, Dattātreya and the last rites, the three hills of Reṇukā, Datta and Anasūyā, Mātṛpura in the Devī Bhāgavata, Māhurgaḍ fort and the separate Ekavīrā shrine. An illustrated reference guide.')
def FACE(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse rx="34" ry="40" fill="#e0401a"/><ellipse rx="26" ry="32" fill="#f05a2a" stroke="none"/>'
 '<path d="M-20 -8 q8 -8 16 0 M4 -8 q8 -8 16 0" fill="#fff"/><circle cx="-12" cy="-7" r="4" fill="#111"/><circle cx="12" cy="-7" r="4" fill="#111"/><circle cy="-24" r="5" fill="#ffd60a"/>'
 '<path d="M-4 4 l4 10 l4 -10" fill="none"/><path d="M-10 22 q10 6 20 0" fill="#c0392b"/><circle cx="14" cy="10" r="3" fill="#ffd60a"/>'
 '<path d="M-40 -30 q40 -40 80 0" fill="none" stroke="#e0a800" stroke-width="6"/><path d="M-30 -44 h60 l-6 -16 l-8 8 l-4 -12 l-4 10 l-4 -10 l-4 12 l-8 -8z" fill="#e0a800"/></g>')
def PARASU(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,'#ff8c1a','#c98b5a',1)+'<path d="M-4 -46 q4 -10 8 0" fill="#2b1a0e" stroke="#111"/><path d="M18 -10 L34 -50" stroke="#7a5a2a" stroke-width="4"/><path d="M30 -54 q14 2 12 16 q-8 -2 -16 -6z" fill="#bbb" stroke="#111" stroke-width="1.5"/></g>'
def SAGE(x,y,s=1,c='#fff'): return f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,c,'#c98b5a',1)+'<path d="M-8 -22 q8 20 16 0" fill="#eee" stroke="#111" stroke-width="1.5"/><path d="M-6 -44 q6 -10 12 0" fill="#ddd" stroke="#111" stroke-width="1.5"/></g>'
def THREEHILLS(w=560,h=180,lab=True):
    s=f'<rect width="{w}" height="{h}" fill="#eef6e4"/>'+HILL(110,h,200,110,'#4a8a4a')+HILL(290,h,230,150,'#3a7a3a')+HILL(470,h,200,95,'#5a9a5a')
    s+=TEMPLE(110,h-108,.8)+TEMPLE(290,h-148,.8,'#f2e6c8')+TEMPLE(470,h-93,.8,'#f2e6c8')
    if lab: s+=T(110,h-140,'REṆUKĀ',12,'#7a1d12')+T(290,h-180+14,'DATTA ŚIKHARA',12,'#1d4f9a')+T(470,h-126,'ANASŪYĀ',12,'#7a5a2a')
    return s
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A large vermilion face of the Goddess Renuka with golden crown, on a forested hill with temples on three peaks behind">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/>'+HILL(70,268,170,120,'#3a6a3a')+HILL(190,268,190,170,'#2e5e2e')+HILL(320,268,170,110,'#4a7a4a')+FACE(190,130,1.9)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Ekavīrikā</b>, “the one heroine”: in Māhur she is <b>Reṇukā</b>, mother of Paraśurāma. Pīṭha no. 8 of the eighteen'),
 ('Hymn line','<i>māhuryām ekavīrikā</i>: “Ekavīrikā in Māhura”'),
 ('Where','<b>Māhur</b> (Māhurgaḍ), Nanded district, Maharashtra, among forested hills near the Pēṅgaṅgā'),
 ('The image','Only her <b>face</b>, large and covered in vermilion'),
 ('Body part','Lists differ (a hand, by most); Māhur’s own story is of Reṇukā’s <b>head</b>'),
 ('Three hills','<b>Reṇukā</b>, <b>Datta Śikhara</b> (Dattātreya) and <b>Anasūyā</b>'),
 ('Old name','<b>Mātṛpura</b> or Mātāpur, in the Devī Bhāgavata'),
 ('A second shrine','A small <b>Ekavīrā</b> temple nearby, said to be Reṇukā’s elder sister'),
 ('Festival','A great fair at <b>Vijayādaśamī</b>; Navarātri; daily offerings of <b>tāmbūl</b>')])
 +talk("Just a face? No body?","Just a face. And the story of why is one of the strangest in the Purāṇas.")))
pages.append(page('where','WHERE IT IS','Forest hills of the eastern Deccan',fig(560,290,'Simplified map of Maharashtra marking Mahur in red near the Telangana border, with Nanded, Kolhapur and Tuljapur',
 MHMAP([(19.83,77.92,'MĀHUR','l','#c0392b'),(19.15,77.31,'Nanded','l','#bbb'),(16.70,74.24,'Kolhapur','r','#ffd166'),(18.01,76.07,'Tuljāpur','r','#ffd166'),(20.39,73.91,'Saptaśṛṅgī','r','#ffd166'),(19.08,72.88,'Mumbai','r','#bbb')]))+'''<div class="panel reading">
<p><b>The town.</b> Māhur lies in the far east of Marathwada, a few kilometres inside it from the <b>Pēṅgaṅgā</b> river, which here divides Marathwada from Vidarbha. Telangana is close by.</p>
<p><b>The hills.</b> Teak forest and three hills, each with its temple; deer, peafowl and bears still live in the woods.</p>
<p><b>Its partner.</b> The hymn names Māhur right after <a href="/bhakti/temples-of-india/18-shakti-peethas/mahalakshmi-kolhapur/">Kolhapur</a>, at the other end of the state.</p>
</div>'''))
pages.append(page('names','HER NAMES','One Goddess, many names',facts([
 ('Ekavīrikā / Ekavīrā','“The one heroine”, “the sole hero’s mother”: one telling says she bore five sons, and one, Paraśurāma, was the hero'),
 ('Reṇukā','Daughter of King Reṇu, wife of the sage Jamadagni, mother of Paraśurāma'),
 ('Jagadambā','“Mother of the world”: Māhur’s Goddess as <i>Mātāpur-nivāsinī Jagadambā</i>'),
 ('Mātṛpura','“Mother’s city”: Māhur’s name in the Devī Bhāgavata'),
 ('Yellammā, Yamāī…','Reṇukā’s names across the Deccan and South: Yellammā, Yamāī, Ellai Ammaṉ, Padmākṣī')])
 +talk("Ekavīrā and Reṇukā are the same?","In Māhur, mostly yes. But there's a second shrine that says otherwise. We'll get there.")))
pages.append(page('pitha','THE PĪṬHA','The hymn says Ekavīrikā',fig(560,150,'Shiva carrying Sati across a night sky, a glowing piece falling onto forested hills',
 '<rect width="560" height="150" fill="#2a0805"/>'+STAR+SHIVA(140,60,.7)+SATI(162,64,.55,-10)+'<path d="M190 80 q80 10 190 40" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><circle cx="382" cy="120" r="6" fill="#ffd166"/>'+HILL(440,150,200,60,'#3a6a3a')+T(440,24,'MĀHURA',14,'#ffd166'))+'''<div class="panel reading">
<p><b>The verse.</b> <i>kolhāpure mahālakṣmī, māhuryām ekavīrikā</i>: the two Maharashtra seats, side by side.</p>
<p><b>What fell here?</b> The lists disagree: most say Satī’s <b>right hand</b>, some the left hand, the back or the shoulder.</p>
<p><b>Two stories in one place.</b> Māhur’s own tradition is not about Satī at all, but about another mother, <b>Reṇukā</b>, whose <b>head</b> rests here. The pīṭha and the local legend overlap, as they often do.</p>
</div>'''))
pages.append(page('which','EKAVĪRĀ OR REṆUKĀ?','Two shrines, two answers',fig(560,140,'Two hilltop shrines: the large Renuka temple on Mahur hill and a small single-hall Ekavira shrine by a river in forest',
 '<rect width="560" height="140" fill="#eef6e4"/>'+HILL(150,140,240,100,'#3a7a3a')+TEMPLE(150,44,1.2)+T(150,24,'REṆUKĀ · MĀHUR',12,'#7a1d12')+'<rect y="120" width="560" height="20" fill="#4aa3df"/>'+HILL(420,124,160,50,'#5a9a5a')+TEMPLE(420,78,.8,'#f2e6c8')+T(420,56,'EKAVĪRĀ',12,'#7a1d12'))+'''<div class="g2">
<div class="card bg-red"><h4>🛕 Reṇukā is Ekavīrā</h4><p>Most pilgrims, and Māhur’s own tradition, treat the <b>Reṇukā temple</b> on Māhur hill as the pīṭha: Reṇukā’s other name is Ekavīrā.</p></div>
<div class="card bg-yellow"><h4>🛕 Ekavīrā the elder sister</h4><p>A small <b>Ekavīrā</b> temple in the forest near Māhur, on the Pēṅgaṅgā, is pointed out as the true “Ekavīrikā”, said to be Reṇukā’s <b>elder sister</b>. Here too only the head is worshipped.</p></div>
</div>'''+talk("Which one do pilgrims visit?","Almost everyone climbs to Reṇukā. The Ekavīrā shrine is little known, even in Maharashtra.")))
pages.append(page('goddess','THE GODDESS','A face of vermilion',fig(560,220,'A large face of the Goddess covered in orange vermilion, with large eyes, a nose ring, and a crown, inside a shrine, with betel leaves offered before her',
 '<rect width="560" height="220" fill="#fde4e4"/><rect x="170" y="10" width="220" height="200" fill="#f3e3c3" stroke="#111" stroke-width="2"/>'+FACE(280,110,2.2)
 +''.join(f'<path d="M{430+k*30} 170 q12 -26 24 0 q-12 10 -24 0z" fill="#3a8a3a" stroke="#111"/>' for k in range(3))+T(470,200,'TĀMBŪL',12,'#7a1d12'))+'''<div class="g2">
<div class="card bg-red"><h4>🔴 Only the face</h4><p>The image in the sanctum is a large <b>face</b>, covered in <b>vermilion</b>. There is no body: the story says only her head came back.</p></div>
<div class="card bg-yellow"><h4>🍃 Tāmbūl</h4><p>Her special offering is <b>viḍā tāmbūl</b>, a folded betel leaf with nut and spices, given back to devotees as prasāda. She is also offered <b>puraṇpolī</b> every day.</p></div>
</div>'''+talk("Betel leaf to a goddess?","She's a mother receiving guests. In Maharashtra you offer a guest tāmbūl.")))
pages.append(page('legend1','THE LEGEND · I','The axe and the boon',fig(560,190,'The sage Jamadagni pointing in anger; his son Parashurama raising an axe; Renuka with her water pot; then the same family restored',
 '<rect width="560" height="190" fill="#ffe9c4"/>'+SAGE(90,170,1.1)+PARASU(200,170,1.1)+GENTLE(300,120,.8).replace('#e05a8a','#c0392b')+'<ellipse cx="330" cy="150" rx="10" ry="12" fill="#c98b2a" stroke="#111"/>'
 +'<path d="M370 100 h40" stroke="#111" stroke-width="3"/><path d="M410 100 l-10 -6 v12z" fill="#111"/>'+SAGE(450,170,.7)+GENTLE(500,130,.55).replace('#e05a8a','#c0392b')+PARASU(530,170,.6))+'''<div class="steps">
<div><b>The doubt.</b> <b>Reṇukā</b>, wife of the sage <b>Jamadagni</b>, went to fetch water and was lost for a moment in watching a prince at play in the river. Jamadagni, sensing her lapse, ordered his sons to kill her.</div>
<div><b>The obedient son.</b> Four sons refused. The youngest, <b>Paraśurāma</b>, obeyed and struck off her head with his axe.</div>
<div><b>The boon.</b> Pleased, Jamadagni offered a boon. Paraśurāma asked for his mother and brothers to live again. They were restored.</div>
</div><div class="panel reading small"><p>This is the Mahābhārata and Purāṇic story. Southern tellings add that her head was joined to another woman’s body, giving the Goddesses Yellammā and Māriyammaṉ.</p></div>'''))
pages.append(page('legend2','THE LEGEND · II','Māhur’s own story',fig(560,180,'Parashurama carrying his mother’s body on a pole across forested hills; the sage Dattatreya guiding him; a face rising out of the earth on the hilltop',
 '<rect width="560" height="180" fill="#eef6e4"/>'+HILL(440,180,240,120,'#3a7a3a')+FACE(440,70,.6)+PARASU(110,170,1.0)+'<path d="M80 100 h80" stroke="#7a5a2a" stroke-width="4"/><path d="M90 100 q30 20 60 0" fill="#c0392b" stroke="#111"/>'+SAGE(270,170,1.0,'#ffd60a')+T(270,80,'DATTĀTREYA',11,'#1d4f9a'))+'''<div class="steps">
<div><b>A second death.</b> In Māhur’s telling, the king <b>Sahasrārjuna</b> attacked the hermitage to seize the wish-giving cow, and Reṇukā was mortally hurt.</div>
<div><b>The last rites.</b> Paraśurāma, mad with grief, carried his mother away. The elders calmed him and sent him to perform her rites at <b>Māhur</b>, under the guidance of <b>Dattātreya</b>.</div>
<div><b>The face.</b> He was told his mother would appear again. A popular local telling adds that he was not to look back; he did, and only her <b>face</b> had risen from the earth. That is the face worshipped today.</div>
</div><div class="panel reading small"><p>Local tradition; versions differ in detail.</p></div>'''))
pages.append(page('hills','THE THREE HILLS','Reṇukā, Datta and Anasūyā',fig(560,180,'Three forested hills, each with a temple on top: Renuka on the first, Datta Shikhar on the tallest, Anasuya on the third',THREEHILLS())+'''<div class="steps">
<div><b>Reṇukā’s hill.</b> The Goddess’s temple, reached by a long flight of steps.</div>
<div><b>Datta Śikhara.</b> The highest of the three: Māhur is honoured as a birthplace of <b>Dattātreya</b>, the teacher in whom Brahmā, Viṣṇu and Śiva are one. Nearby, the <b>Devdeveśvar</b> temple of the Mahānubhāva sect is called Dattātreya’s place of rest.</div>
<div><b>Anasūyā’s hill.</b> For Datta’s mother, <b>Anasūyā</b>, wife of the sage Atri. The three gods came to her as beggars to test her purity; by its power she turned them into babies, and they were born as her son.</div>
</div>'''+talk("A Goddess, a guru and a mother on three hills?","Two mothers and the son of one of them. Māhur is a town of mothers.")))
pages.append(page('texts','IN THE TEXTS','Mātṛpura in the Devī Gītā',facts([
 ('Devī Bhāgavata','In the <b>Devī Gītā</b>, the Goddess lists her holy places; second among them is <b>Mātṛpura</b> in the Sahyādri, “where Devī Reṇukā dwells”'),
 ('Mahābhārata','The story of Reṇukā, Jamadagni and Paraśurāma (in the Vana Parva)'),
 ('The 18 hymn','<i>Māhuryām ekavīrikā</i>: the line that names her among the eighteen'),
 ('Poets','The Marathi saint-poet <b>Viṣṇudās</b> and others sang her āratīs, still sung at Māhur')])
 +talk("The Goddess herself names Māhur?","In the Devī Gītā she does, second on her own list. Not many places can say that.")))
pages.append(page('history','HISTORY','The temple and the fort',tl([
 ('Old','Rock-cut caves near the town, the <b>Pāṇḍav Leṇī</b>, show the hills were sacred long before the present temple.'),
 ('12th–13th c.','The Reṇukā temple is said to be the work of a <b>Yādava</b> king of Devagiri.'),
 ('12th c.','<b>Māhurgaḍ</b> fort is built on another hill; Yādavas and the Gond kings of Chandrapur are named as builders.'),
 ('1358–1527','The fort passes to the <b>Bahmanīs</b> and their successors; a Gond chief holds it for a time (1398).'),
 ('1527–1724','<b>Ahmadnagar</b>, the <b>Mughals</b> (from 1617), the <b>Marathas</b> (1670–89), the Mughals again.'),
 ('17th c.','The local jāgīrdār <b>Udārām Deśmukh</b> (d. 1632) and his wife <b>Sāvitrībāī</b>, “Rāi Bāgan”, the royal tigress, hold Māhur.'),
 ('1724–1948','Under the <b>Nizām</b> of Hyderabad, until Māhur joins India.')])))
pages.append(page('caves','THE PĀṆḌAV LEṆĪ','Caves in the hill',fig(560,140,'Rock-cut cave openings with pillars carved into a hillside',
 '<rect width="560" height="140" fill="#eef6e4"/><path d="M0 140 L0 50 Q280 10 560 50 L560 140z" fill="#8a7a6a" stroke="#111" stroke-width="2"/>'+''.join(f'<rect x="{110+k*130}" y="70" width="80" height="60" fill="#2a1a0a" stroke="#111" stroke-width="2"/>'+''.join(f'<rect x="{118+k*130+j*20}" y="70" width="8" height="60" fill="#8a7a6a"/>' for j in range(4)) for k in range(3)))+'''<div class="panel reading">
<p><b>The caves.</b> Near Māhur town are rock-cut caves known as the <b>Pāṇḍav Leṇī</b>, “caves of the Pāṇḍavas”, a name given to many old caves in Maharashtra.</p>
<p><b>Whose?</b> Sources disagree: some call them <b>Buddhist</b> monks’ caves, others date them to the <b>Vākāṭaka</b> or <b>Rāṣṭrakūṭa</b> age and compare them to Elephanta. What is clear is that the hills of Māhur were sacred long before the present temple.</p>
</div>'''))
pages.append(page('festivals','WORSHIP AND FESTIVALS','The Mother’s calendar',facts([
 ('Daily','Worship three times a day; <b>viḍā tāmbūl</b> and <b>puraṇpolī</b> offered and shared as prasāda'),
 ('Navarātri','Nine nights of the Goddess'),('Vijayādaśamī','A huge <b>fair</b>, the biggest day of Māhur’s year'),
 ('Datta Pūrṇimā','On Datta Śikhara, with a great worship and a feast'),('For mothers','Women pray to her for the protection and strength of their families')])
 +'<div class="key">Tāmbūl, puraṇpolī and a Dasara fair: <b>a mother’s house</b>.</div>'))
pages.append(page('across','REṆUKĀ ACROSS INDIA','The mother of many names',facts([
 ('Māhur','Reṇukā as a face; the eighteen-pīṭha seat'),('Saundatti, Karnataka','<b>Yellammā</b>, Reṇukā’s great southern shrine'),
 ('Kārlā, Maharashtra','<b>Ekvīrā Āī</b>, family Goddess of the Kolī fishing people, beside the Buddhist caves: a namesake, not the hymn’s seat'),
 ('Tamil Nadu','<b>Māriyammaṉ</b> and <b>Ellai Ammaṉ</b>, linked with Reṇukā in folk tellings'),('Amravati','An old <b>Ekavīrā Devī</b> temple beside Ambā Devī')])
 +talk("So which Ekavīrā is the hymn's?","Māhur's, by the hymn's own words: māhuryām. The others share her name and her story.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Ekavīrā','The one heroine'),('Reṇukā','Mother of Paraśurāma'),('Paraśu','Axe: Paraśurāma is “Rāma of the axe”'),('Mātṛpura','Mother’s city'),('Tāmbūl','Betel leaf with nut'),
 ('Puraṇpolī','Sweet stuffed flatbread of Maharashtra'),('Dattātreya','The guru who unites Brahmā, Viṣṇu and Śiva'),('Mahānubhāva','A Maharashtrian devotional sect'),('Leṇī','Caves (Marathi)'),('Gaḍ','Fort')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Goddess.</b> Ekavīrikā, in Māhur Reṇukā, worshipped as a face of vermilion.</div>
<div><b>The legends.</b> Paraśurāma’s axe and his boon; Māhur’s own story of her rites under Dattātreya and the face that rose.</div>
<div><b>The place.</b> Three hills: Reṇukā, Datta Śikhara and Anasūyā; Mātṛpura of the Devī Gītā.</div>
<div><b>The question.</b> Reṇukā’s temple, or the small Ekavīrā shrine said to be her elder sister?</div>
<div><b>The history.</b> A Yādava temple, a fort that changed hands a dozen times, caves older than both.</div>
</div>'''+talk("One line to remember?","A mother whose son took her head, and asked the gods to give it back.")+'<div class="key">The eighth seat of the Mother: <b>Ekavīrikā of Māhur</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Place and history:</b> Wikipedia, “Mahur, Maharashtra”: Nanded district; Pēṅgaṅgā border; three mountains (Datta Śikhara highest); Reṇukā as a Śakti Pīṭha; Vijayādaśamī fair; the Sahasrārjuna and Dattātreya legend; Dattātreya and Anasūyā; Mātṛpura in the Devī Bhāgavata; Māhurgaḍ (12th c.); Udārām Deśmukh and Sāvitrībāī; Devdeveśvar; Viṣṇudās. Wikipedia, “Mahur Fort”: Yādavas or Gond kings; Bahmanī 1358; Gond 1398; 1428; Ahmadnagar 1527; Mughals 1617; Marathas 1670–89; Nizām 1724–1948. Wikipedia, “Renuka”: the beheading and boon; Yellammā and Māriyammaṉ tellings; Ekvīrā and other names; Amravati temple. Wikipedia, “Ekvira” (Kārlā). nanded.gov.in and others (Yādava king, 800–900 years ago). bhaktikalpa.com, tirthayatra.org, hindupad.com (the separate Ekavīrā shrine; elder sister; head only). sawarkarcollegebeed.edu.in (tāmbūl, puraṇpolī, trikāl pūjā). Maharashtra Tourism, durgbharari.in, durgavaibhav (the caves: Buddhist, Vākāṭaka or Rāṣṭrakūṭa).</p>
<p><b>Sources differ:</b> the body part; the caves’ date and faith; who built the fort. <b>Not verified:</b> the “do not look back” detail (popular telling); the Ekavīrā elder-sister tradition. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('which','Ekavīrā or Reṇukā?'),('goddess','The Goddess'),('legend1','Legend · The Axe and the Boon'),('legend2','Legend · Māhur’s Own Story'),('hills','The Three Hills'),
 ('texts','In the Texts'),('history','History'),('caves','The Pāṇḍav Leṇī'),('festivals','Worship and Festivals'),('across','Reṇukā across India'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 8 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7.4vw,74px)">EKAVĪRIKĀ</h1>
  <div class="series">REṆUKĀ OF MĀHUR · A REFERENCE GUIDE</div>
  <div class="tag">The mother who came back as a face</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>On a forested hill in eastern Maharashtra, pilgrims climb to a Goddess who has no body, only a great face of vermilion: <b>Reṇukā</b>, mother of Paraśurāma, whom the hymn calls <b>Ekavīrikā</b>.</p>
    <p>Her son struck off her head at his father’s command, then asked for her life back. Māhur says she rose here, face first, from the earth.</p>
    <p>This guide follows her story, the three hills of Māhur, and the question of which shrine is the hymn’s.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Reṇukā Māyī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A son who killed his mother? That's a hard story.","Hard, and then healed. The boon he asked for was her life. That's the part Māhur remembers.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Ekavirika_Mahur.html','w').write(head+b+tail())
print('ok',len(pages))
