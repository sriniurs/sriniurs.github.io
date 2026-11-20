exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Mahākālī · Ujjain · The 18 Śakti Pīṭhas · srini.presents',
 'Mahākālī of Ujjain, the ninth of the 18 Śakti Pīṭhas: Gaḍhkālikā on Bhairav Parvat, where Satī’s upper lip is said to have fallen and Kālidāsa became a poet; Harsiddhi, the Ujjayinī pīṭha of the elbow with its Maratha lamp towers; Kālabhairava the guardian; and Mahākāla beside them all. An illustrated reference guide.')
def KALI(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse rx="34" ry="40" fill="#ff8c1a"/><ellipse rx="26" ry="32" fill="#ffa040" stroke="none"/>'
 '<path d="M-22 -10 q10 -8 18 0 M4 -10 q10 -8 18 0" fill="#fff"/><circle cx="-12" cy="-9" r="4" fill="#111"/><circle cx="12" cy="-9" r="4" fill="#111"/><circle cy="-24" r="5" fill="#c0392b"/>'
 '<path d="M-14 14 q14 10 28 0" fill="#fff"/><path d="M-6 18 q6 28 12 0z" fill="#e04040"/>'
 '<path d="M-30 -40 h60 l-6 -18 l-8 8 l-4 -12 l-4 10 l-4 -10 l-4 12 l-8 -8z" fill="#d8d8e0"/></g>')
def LAMPT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><path d="M-10 0 L-6 -120 H6 L10 0z" fill="#e8e2d0"/>'+''.join(f'<path d="M-12 {-10-k*11} h24" stroke-width="3"/>' for k in range(10))+''.join(f'<circle cx="{d*13}" cy="{-12-k*11}" r="2.4" fill="#ffd60a" stroke="none"/>' for k in range(10) for d in (-1,1))+'<path d="M-4 -124 l4 -10 l4 10z" fill="#ffd60a"/></g>'
def SHIKH(x,y,s=1,c='#f2e6c8'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-30" y="-24" width="60" height="24" fill="{c}"/><path d="M-22 -24 Q-20 -70 0 -90 Q20 -70 22 -24z" fill="{c}"/>'+''.join(f'<path d="M{-18+j*6} -30 Q{-14+j*4} -60 0 -86" fill="none" stroke-width="1"/>' for j in range(7))+'<path d="M0 -90 v-22"/><path d="M0 -112 l18 6 l-18 6z" fill="#ff8c1a"/></g>'
def UMAP(marks,w=560,h=300):
    g=''
    for x,y,t,side,col in marks:
        r=8 if col=='#c0392b' else 6
        g+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(x+(12 if side=='r' else -12),y+4,t,12,'#111','start' if side=='r' else 'end')
    return (f'<rect width="{w}" height="{h}" fill="#f1e6cf"/><path d="M200 300 C 180 240, 260 200, 230 150 S 160 80, 230 0" stroke="#4aa3df" stroke-width="12" fill="none"/>'+T(150,260,'KṢIPRĀ',12,'#1d4f9a')
     +'<ellipse cx="330" cy="215" rx="26" ry="14" fill="#9ad1f5" stroke="#111"/>'+T(330,240,'Rudra Sāgar',10,'#1d4f9a')+g+T(w-10,h-8,'schematic, not to scale',10,'#555','end')+T(w-14,22,'N ↑',13,'#111','end'))
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The saffron face of the Goddess Kalika with silver crown and red tongue, a stone lion facing her, two tall lamp towers ablaze, and a temple spire behind">'
 '<rect width="380" height="268" fill="#2a0805" rx="8"/><circle cx="190" cy="110" r="96" fill="#7a1d12"/>'+LAMPT(40,250,1.6)+LAMPT(340,250,1.6)+SHIKH(190,250,.8)+KALI(190,120,1.9)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Mahākālī</b>, the great Kālī: Pīṭha no. 9 of the eighteen'),
 ('Hymn line','<i>ujjayinyāṃ mahākālī</i>: “Mahākālī in Ujjayinī”'),
 ('Where','<b>Ujjain</b>, Madhya Pradesh, on the Kṣiprā: Avantikā of the seven holy cities'),
 ('Usual seat','<b>Gaḍhkālikā</b> on Bhairav Parvat, where Satī’s <b>upper lip</b> is said to have fallen'),
 ('Second seat','<b>Harsiddhi</b>, the “Ujjayinī pīṭha” of the 51-list, where her <b>elbow</b> fell'),
 ('Guardian','<b>Kālabhairava</b>, offered liquor as prasāda'),
 ('Her Lord','<b>Mahākāla</b>, the jyotirliṅga, in the same city'),
 ('Poet','<b>Kālidāsa</b>, by legend a dunce made a poet by Gaḍhkālikā'),
 ('Festivals','<b>Navarātri</b>, when Harsiddhi’s lamp towers blaze; the <b>Siṃhastha</b> Kumbha')])
 +talk("Mahākāla and Mahākālī in one city?","Great Time and the Great Goddess of Time. Of course they live together.")))
pages.append(page('where','WHERE IT IS','A city of Śiva and Śakti',fig(560,300,'Schematic map of Ujjain along the Kshipra river: Gadhkalika in the north on Bhairav Parvat, Kalabhairava and the Bhartrihari caves nearby, Harsiddhi near Rudra Sagar, Mahakala to its east, Ram Ghat on the river, Sandipani ashram to the east',
 UMAP([(250,70,'GAḌHKĀLIKĀ','r','#c0392b'),(275,36,'Kālabhairava','r','#bbb'),(270,100,'Bhartṛhari caves','r','#bbb'),(320,195,'Harsiddhi','l','#ffd166'),(370,190,'Mahākāla','r','#1d4f9a'),(220,200,'Rām Ghāṭ','l','#bbb'),(470,140,'Sāndīpani āśram','l','#bbb')]))+'''<div class="panel reading">
<p><b>The city.</b> Ujjain, old <b>Avanti</b>, stands on the east bank of the <b>Kṣiprā</b> in the Mālwā plateau. It is a jyotirliṅga city, a mokṣapurī and a Kumbha city all at once.</p>
<p><b>The Goddess’s places.</b> <b>Gaḍhkālikā</b> stands north of the old city on a rise called <b>Bhairav Parvat</b>, near the river; <b>Harsiddhi</b> stands close to Mahākāla, by the Rudra Sāgar lake.</p>
<p><b>Read more.</b> <a href="/bhakti/temples-of-india/12-jyotirlingas/mahakaleshwar/">Mahākāleśvara</a> · <a href="/bhakti/temples-of-india/sapta-puri/">the Saptapurī</a>.</p>
</div>'''))
pages.append(page('names','HER NAMES','Kālī of the fort',facts([
 ('Mahākālī','“The great Kālī”, the hymn’s name, and the Goddess of the Devī Māhātmya’s first episode'),
 ('Gaḍhkālikā','“Kālikā of the <b>gaḍh</b>”, the fort: the old fortified city of Ujjain'),
 ('Avantī','The Goddess named for the city: Avanti pīṭha'),
 ('Harsiddhi','“She who grants all success”, or “who vanquishes all”'),
 ('Maṅgala Caṇḍikā','Harsiddhi’s name in the 51-list')])
 +talk("Kālī of the fort? Is there a fort?","Old Ujjain was walled, and its oldest part was the gaḍh. She was the fort's own Goddess.")))
pages.append(page('pitha','THE PĪṬHA','The upper lip and the elbow',fig(560,150,'Shiva carrying Sati across a night sky, two glowing pieces falling onto a city by a river',
 '<rect width="560" height="150" fill="#2a0805"/>'+STAR+SHIVA(140,60,.7)+SATI(162,64,.55,-10)+'<path d="M190 80 q80 10 170 40" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><path d="M200 84 q120 10 220 30" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><circle cx="362" cy="120" r="6" fill="#ffd166"/><circle cx="422" cy="114" r="6" fill="#ffd166"/>'+SHIKH(470,148,.5)+T(440,24,'UJJAYINĪ',14,'#ffd166'))+'''<div class="panel reading">
<p><b>The verse.</b> <i>ujjayinyāṃ mahākālī, pīṭhikāyāṃ puruhūtikā</i>: Ujjain opens the hymn’s third verse.</p>
<p><b>Two pieces, one city.</b> The usual 18-list says Satī’s <b>upper lip</b> fell in Ujjain. The 51-list counts Ujjain twice: the <b>Bhairava Parvata</b> pīṭha (upper lip, Goddess Avantī) and the <b>Ujjayinī</b> pīṭha (elbow, Goddess Maṅgala Caṇḍikā).</p>
<p><b>Why it matters.</b> That double listing is why Ujjain has two pīṭha temples, and why sources point to different ones for the hymn’s Mahākālī.</p>
</div>'''))
pages.append(page('which','WHICH TEMPLE?','Three answers in one city','<table class="ct"><tr><th>Temple</th><th>Claim</th><th>Body part</th><th>Who says so</th></tr>'
 +'<tr><td><b>Gaḍhkālikā</b></td><td>Mahākālī of the 18; Avantī of the 51</td><td>Upper lip</td><td>Most temple and pilgrim sources</td></tr>'
 +'<tr><td><b>Harsiddhi</b></td><td>Ujjayinī pīṭha of the 51</td><td>Elbow (some say upper lip)</td><td>Madhya Pradesh Tourism; many lists</td></tr>'
 +'<tr><td><b>Mahākāla</b></td><td>Mahākālī as Mahākāla’s Śakti</td><td>Upper lip</td><td>Some reference lists</td></tr></table>'
 +'''<div class="panel reading"><p><b>Our reading.</b> The hymn names <b>Mahākālī</b>; Gaḍhkālikā is the temple of Kālī herself and is most often named as her seat, so this guide centres on it. Harsiddhi, a pīṭha in its own right, gets its own pages. One travel guide even says Gaḍhkālikā is not a pīṭha at all: in Ujjain, every claim has an opposite.</p></div>'''
 +talk("Can a city have two Śakti Pīṭhas?","Ujjain does: the 51-list counts it twice, once for the lip and once for the elbow.")))
pages.append(page('kalika','GAḌHKĀLIKĀ','The Goddess with the tongue',fig(560,220,'The saffron-painted stone face of Kalika with silver crown and protruding red tongue in the sanctum, a stone lion facing her from the entrance',
 '<rect width="560" height="220" fill="#fde4e4"/><rect x="170" y="10" width="220" height="200" fill="#f3e3c3" stroke="#111" stroke-width="2"/>'+KALI(280,110,2.2)
 +'<g transform="translate(480 200)" stroke="#111" stroke-width="2"><ellipse cy="-20" rx="40" ry="18" fill="#e0a800"/><circle cx="-38" cy="-30" r="18" fill="#c98b2a"/><circle cx="-42" cy="-30" r="10" fill="#e0a800"/></g>'+T(470,130,'LION',12,'#7a1d12'))+'''<div class="g2">
<div class="card bg-red"><h4>🔥 The image</h4><p>A stone image painted <b>saffron</b>, with a <b>silver crown</b>, wide eyes and a <b>protruding tongue</b>: Kālī smiling and fierce at once.</p></div>
<div class="card bg-yellow"><h4>🦁 The lion</h4><p>Her mount, a stone <b>lion</b>, sits at the entrance facing her. The temple faces <b>west</b>, toward the Kṣiprā.</p></div>
</div><div class="panel reading small"><p>Around her: a <b>Gaura Bhairava</b> shrine (one of Ujjain’s eight Bhairavas), Śiva shrines and a lamp pillar.</p></div>'''))
pages.append(page('kalidasa','THE LEGEND · KĀLIDĀSA','The fool who became a poet',fig(560,180,'A young man sitting on a tree branch while sawing it off; later the same man writing verses before the Goddess',
 '<rect width="560" height="180" fill="#ffe9c4"/><path d="M40 180 v-120" stroke="#7a5a2a" stroke-width="14"/><path d="M40 80 L200 70" stroke="#7a5a2a" stroke-width="10"/><circle cx="60" cy="60" r="34" fill="#3a8a3a"/>'+person(140,74,'#2a7a4a','#c98b5a',.7)+'<path d="M100 70 l6 14" stroke="#bbb" stroke-width="3"/>'
 +'<path d="M240 90 h40" stroke="#111" stroke-width="3"/><path d="M280 90 l-10 -6 v12z" fill="#111"/>'+person(350,170,'#ff8c1a','#c98b5a',1.1)+'<rect x="380" y="130" width="40" height="30" fill="#fff4cd" stroke="#111"/>'+KALI(480,80,.8))+'''<div class="steps">
<div><b>The fool.</b> Folk tradition says the young <b>Kālidāsa</b> was so simple that he was found sawing off the branch he sat on. Tricked into marrying a learned princess, he was mocked by her.</div>
<div><b>The Goddess.</b> In shame he turned to <b>Kālī</b>, and by her grace became the greatest poet of Sanskrit. Ujjain says this was <b>Gaḍhkālikā</b>; some tellings say she wrote on his tongue.</div>
<div><b>The poet.</b> His works, the <i>Meghadūta</i>, <i>Śakuntalā</i>, <i>Raghuvaṃśa</i>, made Ujjain immortal. Students still come to her before exams.</div>
</div><div class="panel reading small"><p>A legend: Kālidāsa’s life is almost unknown, and his link to Ujjain and to a King Vikramāditya is traditional.</p></div>'''))
pages.append(page('history','HISTORY','From ancient bricks to the Scindias',tl([
 ('Ancient','The temple board speaks of images and bricks from about the <b>1st century BCE</b> found at the site.'),
 ('Purāṇa','The <b>Avanti Khaṇḍa</b> of the Skanda Purāṇa counts Gaḍhkālikā among Ujjain’s Mother Goddesses.'),
 ('7th c.','King <b>Harṣavardhana</b> is said to have renovated the temple (one source gives 606).'),
 ('10th–13th c.','Further work under the <b>Paramāras</b> of Mālwā.'),
 ('19th–20th c.','Rebuilt by the <b>Scindia</b> rulers of Gwalior state; renovated again in <b>1944</b>.'),
 ('Today','The temple stands near the <b>Bhartṛhari caves</b> and Kālabhairava, north of the city.')])
 +talk("Was Harṣavardhana really here?","That's the tradition the temple and many guides repeat. Like much in Ujjain, it's old memory more than inscription.")))
pages.append(page('harsiddhi','HARSIDDHI','The Ujjayinī pīṭha',fig(560,200,'A temple with two tall white lamp towers covered in hundreds of lit oil lamps, at night',
 '<rect width="560" height="200" fill="#1a1a2a"/>'+STAR+LAMPT(140,196,1.4)+LAMPT(420,196,1.4)+SHIKH(280,196,1.0,'#e8e2d0')+GENTLE(280,140,.3).replace('#e05a8a','#ff8c1a'))+facts([
 ('Goddess','<b>Harsiddhi</b>, Maṅgala Caṇḍikā; an image smeared with turmeric and vermilion, with Mahālakṣmī and Mahāsarasvatī'),
 ('Pīṭha','The <b>Ujjayinī</b> pīṭha of the 51-list: Satī’s <b>elbow</b>; Bhairava <b>Kapilāmbara</b>'),
 ('Legend','The Skanda Purāṇa tells how Caṇḍī killed the demons who invaded Kailāsa; Śiva named her <b>Harsiddhi</b>, “she who vanquishes all”. Folk tales link her to King <b>Vikramāditya</b>'),
 ('Temple','Rebuilt in the <b>Maratha</b> period; its two <b>lamp towers</b> (dīpastambhas) are lit with hundreds of lamps in Navarātri'),
 ('Where','Between Mahākāla and the Rudra Sāgar lake')])))
pages.append(page('bhairava','KĀLABHAIRAVA','The guardian who drinks',fig(560,150,'A dark Bhairava face with large eyes and moustache in a shrine, a devotee offering a cup of liquor which the image seems to drink',
 '<rect width="560" height="150" fill="#fdf1e8"/><rect x="200" y="10" width="160" height="130" fill="#3a2a2a" stroke="#111" stroke-width="2"/><ellipse cx="280" cy="70" rx="40" ry="46" fill="#ff8c1a" stroke="#111" stroke-width="2"/><circle cx="264" cy="60" r="6" fill="#fff" stroke="#111"/><circle cx="296" cy="60" r="6" fill="#fff" stroke="#111"/><path d="M256 86 q24 -10 48 0" stroke="#111" stroke-width="5" fill="none"/>'
 +person(450,140,'#2a7a4a','#c98b5a',1)+'<path d="M420 96 l-80 -10" stroke="#c98b5a" stroke-width="5"/><rect x="330" y="78" width="14" height="16" fill="#ddd" stroke="#111"/>')+'''<div class="panel reading">
<p><b>The guardian.</b> Every Śakti Pīṭha has its Bhairava. Gaḍhkālikā’s is <b>Lambakarṇa</b> (“long-eared”) in the 51-list; in practice, pilgrims pair her with Ujjain’s famous <b>Kālabhairava</b> temple, close by.</p>
<p><b>The offering.</b> Kālabhairava is offered <b>liquor</b>, poured at his lips; devotees say the image drinks it, and some is given back as prasāda. It is one of the most talked-about rites in India.</p>
<p><b>Eight Bhairavas.</b> Ujjain keeps a circle of eight Bhairava shrines; Gaḍhkālikā’s compound holds one of them.</p>
</div>'''))
pages.append(page('mahakala','MAHĀKĀLA AND MAHĀKĀLĪ','Time and the Goddess of time',fig(560,160,'The Mahakala temple spire beside a fierce dark Goddess, an hourglass between them',
 '<rect width="560" height="160" fill="#0b2a4a"/>'+SHIKH(160,156,1.2,'#e8e2d0')+'<path d="M260 50 h40 l-20 30 l20 30 h-40 l20 -30z" fill="#ffd166" stroke="#111"/>'+KALI(420,80,1.1))+'''<div class="panel reading">
<p><b>Mahākāla</b>, “Great Time”, is Śiva who devours time itself; his south-facing liṅga in Ujjain is a jyotirliṅga.</p>
<p><b>Mahākālī</b> is his power: the Goddess as time, who even Time cannot outlast. In the <b>Devī Māhātmya</b> she is the first of the three great forms, who wakes Viṣṇu to slay Madhu and Kaiṭabha.</p>
<p><b>One city.</b> The hymn puts her here because this is Mahākāla’s city; some lists simply place her in his temple.</p>
</div><div class="panel reading small"><p>Read more: <a href="/bhakti/temples-of-india/12-jyotirlingas/mahakaleshwar/">Mahākāleśvara</a> · <a href="/bhakti/devi/devi-mahatmya/">Devī Māhātmya</a>.</p></div>'''))
pages.append(page('festivals','THROUGH THE YEAR','The Goddess’s calendar in Ujjain',facts([
 ('Navarātri','Both temples fill; Harsiddhi’s lamp towers are lit; Gaḍhkālikā is the students’ and poets’ Goddess'),
 ('Kālabhairava Aṣṭamī','The guardian’s own day'),
 ('Siṃhastha Kumbha','Every twelve years, when Jupiter is in Leo, the whole city fills for the bath in the Kṣiprā'),
 ('Mahāśivarātri','Mahākāla’s great night'),
 ('Before exams','Students pray at Gaḍhkālikā, Kālidāsa’s Goddess')])
 +'<div class="key">Ujjain: <b>Mahākāla, Mahākālī, Harsiddhi and Bhairava</b>, a full divine household.</div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Gaḍh','Fort'),('Kālikā','Kālī'),('Harsiddhi','She who grants success / vanquishes all'),('Dīpastambha','Lamp tower'),('Lambakarṇa','Long-eared: a Bhairava'),
 ('Avanti','Old name of Ujjain and its region'),('Siṃhastha','Ujjain’s Kumbha, when Jupiter is in Leo'),('Paramāra','Medieval dynasty of Mālwā'),('Bhairav Parvat','Bhairava’s hill, site of Gaḍhkālikā')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Goddess.</b> Mahākālī, worshipped as Gaḍhkālikā on Bhairav Parvat; Satī’s upper lip fell here.</div>
<div><b>The second seat.</b> Harsiddhi, the Ujjayinī pīṭha of the elbow, with its lamp towers.</div>
<div><b>The poet.</b> Kālidāsa, the fool made a poet by Kālī.</div>
<div><b>The guardian.</b> Kālabhairava, who drinks the liquor offered to him.</div>
<div><b>The city.</b> Mahākāla’s Ujjain: jyotirliṅga, mokṣapurī, Kumbha city and Śakti Pīṭha in one.</div>
</div>'''+talk("One line to remember?","In the city of Great Time, the Great Goddess of Time gave a fool his tongue.")+'<div class="key">The ninth seat of the Mother: <b>Mahākālī of Ujjain</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Gaḍhkālikā:</b> behindeverytemple.org (upper lip; 18 pīṭhas; Harṣavardhana; Gwalior; Kālidāsa; the tongue). veludharan.blogspot.com, 2026 (west-facing; lion; tongue; Gaura Bhairava; 1st c. BCE bricks per the temple board; 1944 renovation). Incredible India (saffron image, silver crown, lion; Gwalior state). Outlook Traveller (Kālidāsa; Harṣa in 606; Skanda Purāṇa Avanti Khaṇḍa). exploreourindia.com and others (Paramāras). trawell.in (the view that it is not a pīṭha). hindu-blog.com and templepurohit.com (Avantī; Bhairava Lambakarṇa).</p>
<p><b>Harsiddhi and the lists:</b> greenmesg.org (Pīṭhanirṇaya: Ujjayinī pīṭha, elbow, Maṅgala Caṇḍikā, Kapilāmbara; Bhairava Parvata pīṭha; Gaḍhkālikā as the Aṣṭādaśa seat). MP Tourism (Harsiddhi, elbow, Vikramāditya). sygic and Outlook (the Skanda Purāṇa name legend; Maratha rebuilding; lamp towers). apnisanskriti.com (turmeric and vermilion; some say upper lip). Wikipedia mirror of “Mahakaleshwar” (upper lip; Mahākālī). shubhpanchang.com (Kālabhairava’s liquor offering).</p>
<p><b>Sources differ:</b> which temple is the hymn’s seat; the body part at each. <b>Not verified:</b> Harṣavardhana’s renovation; the Kālidāsa legend; the 1st c. BCE finds (temple board). The city map is a schematic. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('which','Which Temple?'),('kalika','Gaḍhkālikā'),('kalidasa','Legend · Kālidāsa'),('history','History'),('harsiddhi','Harsiddhi'),
 ('bhairava','Kālabhairava'),('mahakala','Mahākāla and Mahākālī'),('festivals','Through the Year'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 9 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">MAHĀKĀLĪ</h1>
  <div class="series">UJJAIN · A REFERENCE GUIDE</div>
  <div class="tag">The Great Goddess in the city of Great Time</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Ujjain belongs to <b>Mahākāla</b>, Śiva as Great Time. The hymn says it belongs just as much to <b>Mahākālī</b>.</p>
    <p>North of the old city, on Bhairav Parvat, a saffron Kālī with a silver crown and a red tongue is said to have made a fool into Kālidāsa. Near Mahākāla, two lamp towers blaze for <b>Harsiddhi</b>. And a short walk away, Kālabhairava drinks what his devotees pour.</p>
    <p>This guide sorts out which temple is which, and why Ujjain has more than one claim to the Goddess.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mahākālī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Which temple is the real one?","That's what this guide is for. Short answer: most say Gaḍhkālikā, but Harsiddhi has a list on its side too.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Mahakali_Ujjain.html','w').write(head+b+tail())
print('ok',len(pages))
