exec(open('/home/claude/work/shakti/common_s.py').read())
head=make_head('Badrīnāth · Abode of the North · srini.presents',
 'Badrīnāth in the Garhwal Himalaya: Nara-Nārāyaṇa’s penance, Lakṣmī as the badrī tree, Ādi Śaṅkara and the image from the Nārada Kuṇḍa, the Nambūdiri Rāval, the temple’s history, Tapta Kuṇḍa and Brahma Kapāla, Mānā and Vyāsa’s cave, the Pañca Badrī, and its place in both Char Dhams. An illustrated reference guide.')
def b(lat,lon): return 30+(lon-79.2)*900, 30+(30.95-lat)*900
def BMAP(w=560,h=300):
    g=f'<rect width="{w}" height="{h}" fill="#e7f0d8"/>'
    g+=''.join(f'<path d="M{x} {y} l40 -60 l40 60z" fill="#fff" stroke="#888"/>' for x,y in ((40,90),(150,70),(380,80),(470,100),(60,280),(420,290)))
    a=b(30.86,79.42);c=b(30.74,79.49);d=b(30.55,79.56)
    g+=f'<path d="M{b(30.80,79.43)[0]:.0f} {b(30.80,79.43)[1]:.0f} Q{c[0]-10:.0f} {c[1]-20:.0f} {c[0]+6:.0f} {c[1]:.0f} T{d[0]:.0f} {h}" stroke="#4aa3df" stroke-width="7" fill="none"/>'
    g+=f'<path d="M{a[0]:.0f} {a[1]:.0f} q10 30 -10 60" stroke="#4aa3df" stroke-width="4" fill="none"/>'
    for nm,la,lo,col,side in (('BADRĪNĀTH',30.744,79.491,'#1d4f9a','r'),('Mānā',30.773,79.496,'#bbb','r'),('Vasudhārā',30.785,79.44,'#bbb','l'),('Nara (peak)',30.76,79.42,'#fff','l'),('Nārāyaṇa (peak)',30.72,79.56,'#fff','r'),('Nīlakaṇṭha',30.73,79.39,'#fff','l'),('Pāṇḍukeśvar',30.63,79.55,'#bbb','r')):
        x,y=b(la,lo);r=8 if col=='#1d4f9a' else 6
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',nm,12,'#111','start' if side=='r' else 'end')
    x,y=b(30.62,79.53); g+=T(x-20,y,'ALAKANANDĀ',11,'#1d4f9a','end')
    x,y=b(30.80,79.47); g+=T(x+30,y-14,'Sarasvatī',11,'#1d4f9a','start')
    return g+T(w-10,h-8,'simplified, not to scale',10,'#555','end')
def BTEMPLE(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-60" y="-70" width="120" height="70" fill="#ff8c8c"/>'
 +''.join(f'<rect x="{-50+i*22}" y="-56" width="12" height="20" fill="#1d6fd0"/>' for i in range(5))+'<rect x="-14" y="-34" width="28" height="34" fill="#7a3a2a"/>'
 '<path d="M-66 -70 h132 l-12 -16 h-108z" fill="#e0a800"/><path d="M-30 -86 h60 l-10 -26 h-40z" fill="#ff8c8c"/><path d="M-12 -112 h24 l-12 -22z" fill="#e0a800"/><path d="M0 -134 v-14"/><path d="M0 -148 l14 5 l-14 5z" fill="#ff8c1a"/></g>')
def SAGE(x,y,s=1,c='#ff8c1a'): return f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,c,'#4a6fa0',1)+'<path d="M-24 18 q24 -14 48 0" stroke="#111" stroke-width="2" fill="#c9a26b"/><path d="M-8 -50 q8 -18 16 0" fill="#3a2a1a" stroke="#111"/></g>'
TREE=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-6" y="-60" width="12" height="60" fill="#7a5a2a"/><circle cy="-80" r="40" fill="#4a9a4a"/>'+''.join(f'<circle cx="{dx}" cy="{dy}" r="4" fill="#c0392b" stroke-width="1"/>' for dx,dy in ((-20,-90),(10,-100),(22,-76),(-8,-66),(0,-86)))+'</g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A brightly painted temple facade below two snow peaks, a river in front">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/><path d="M10 190 l90 -150 l90 150z" fill="#fff" stroke="#888"/><path d="M190 190 l90 -170 l90 170z" fill="#fff" stroke="#888"/>'
 '<rect y="190" width="380" height="78" fill="#8aa37a" rx="8"/><path d="M0 250 Q190 230 380 252" stroke="#4aa3df" stroke-width="12" fill="none"/>'+BTEMPLE(190,232,1.2)+T(80,180,'NARA',11,'#0d3f73')+T(290,180,'NĀRĀYAṆA',11,'#0d3f73')+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','<b>Badrīnārāyaṇa</b> (Badrī Viśāl): Viṣṇu seated in meditation, a small black stone image'),
 ('Where','Chamoli district, Uttarakhand, on the <b>Alakanandā</b>, about 3,100 m up in the Garhwal Himalaya'),
 ('Between','The <b>Nara</b> and <b>Nārāyaṇa</b> mountains, with <b>Nīlakaṇṭha</b> peak behind'),
 ('Old name','<b>Badarikāśrama</b>: the hermitage of the jujube trees'),
 ('Revived by','<b>Ādi Śaṅkara</b>, by tradition'),
 ('Priest','The <b>Rāval</b>, a Nambūdiri brāhmaṇa from Kerala'),
 ('Lists','The northern Dhām of the Char Dham; in the Himalayan Char Dham; a <b>Divya Deśam</b>; first of the <b>Pañca Badrī</b>'),
 ('Season','Open in summer; in winter the worship moves down to <b>Jyotirmaṭh</b>')])
 +talk("Why is it called Badrī?","Badarī is the jujube tree. The whole valley was once a jujube forest where Viṣṇu sat in penance.")))
pages.append(page('where','WHERE IT IS','Between two mountains',fig(560,300,'Simplified map of the upper Alakananda valley: Badrinath on the river between the Nara and Narayana peaks, Mana village just upstream, Vasudhara falls to the west and Pandukeshwar downstream',BMAP())
 +'''<div class="panel reading">
<p><b>The valley.</b> Badrīnāth sits on the right bank of the <b>Alakanandā</b>, one of the two rivers that become the Gaṅgā, in a high valley ringed with snow.</p>
<p><b>Two mountains.</b> The ranges on either side are named <b>Nara</b> and <b>Nārāyaṇa</b>, after the twin sages of the legend. <b>Nīlakaṇṭha</b>, a great snow pyramid, rises behind the temple.</p>
<p><b>Upstream.</b> <b>Mānā</b>, the last village before the high passes, lies just above, where the little <b>Sarasvatī</b> joins the Alakanandā.</p>
</div>'''))
pages.append(page('naranarayana','THE LEGEND · NARA-NĀRĀYAṆA','Penance since time began',fig(560,170,'Two sages seated in meditation side by side in a snowy forest',
 '<rect width="560" height="170" fill="#e6eef8"/>'+''.join(f'<path d="M{x} 110 l60 -90 l60 90z" fill="#fff" stroke="#888"/>' for x in (20,420))+TREE(250,160,.9)+SAGE(200,130,1.1)+SAGE(320,130,1.1,'#ffd60a')+T(200,166,'NARA',11,'#0d3f73')+T(320,166,'NĀRĀYAṆA',11,'#0d3f73'))+'''<div class="steps">
<div><b>The twin sages.</b> The Bhāgavata says Viṣṇu came as two sages, <b>Nara</b> and <b>Nārāyaṇa</b>, sons of Dharma, and did penance at Badarī for the good of all beings.</div>
<div><b>Arjuna and Kṛṣṇa.</b> In the Mahābhārata, Śiva tells Arjuna that in a former life he was Nara, doing fierce penance at Badarī with Nārāyaṇa. They were reborn as Arjuna and Kṛṣṇa.</div>
<div><b>Still sitting.</b> The two mountains that bear their names are said to be the sages themselves, still in meditation.</div>
</div>'''))
pages.append(page('lakshmi','THE LEGEND · THE BADRĪ TREE','Lakṣmī shades her Lord',fig(560,170,'Vishnu meditating in falling snow while a jujube tree spreads over him like an umbrella',
 '<rect width="560" height="170" fill="#dfe8f5"/>'+''.join(f'<circle cx="{(i*53)%560}" cy="{(i*37)%150}" r="3" fill="#fff"/>' for i in range(40))+TREE(280,160,1.3)+SAGE(280,150,.9,'#ffd60a')+'<circle cx="280" cy="94" r="6" fill="#e0a800" stroke="#111"/>')+'''<div class="steps">
<div><b>Snow and sun.</b> Viṣṇu sat so long in meditation here that he did not notice the snow, or later the burning sun.</div>
<div><b>The tree.</b> Lakṣmī took the form of a <b>badarī</b> (jujube) tree and spread over him, shielding him through all seasons.</div>
<div><b>The name.</b> Pleased, Viṣṇu named the place after her: <b>Badarī-nātha</b>, “Lord of the jujube”, the Lord who is hers.</div>
</div>'''+talk("So 'Badrīnāth' really means Lakṣmī's Lord?","Exactly. The name is a thank-you note from Viṣṇu to his wife.")))
pages.append(page('image','THE IMAGE','Badrī Viśāl',fig(560,180,'A small black stone image of Vishnu seated cross-legged in meditation, two hands raised holding conch and discus, under a gold canopy',
 '<rect width="560" height="180" fill="#2a1a3a"/><path d="M200 20 h160 l-20 30 h-120z" fill="#e0a800" stroke="#111" stroke-width="2"/><g transform="translate(280 150)" stroke="#111" stroke-width="2"><path d="M-50 0 q50 -30 100 0z" fill="#333"/><rect x="-26" y="-70" width="52" height="64" rx="16" fill="#333"/><circle cy="-88" r="20" fill="#333"/><path d="M-26 -60 l-24 -30 M26 -60 l24 -30" stroke="#333" stroke-width="10"/><circle cx="-52" cy="-96" r="9" fill="#fff"/><path d="M44 -104 a9 9 0 1 1 0 .1z" fill="#ffd60a"/></g>'
 +T(100,120,'Kubera',11,'#ffd166')+T(100,140,'Nārada',11,'#ffd166')+T(460,120,'Uddhava',11,'#ffd166')+T(460,140,'Nara-Nārāyaṇa',11,'#ffd166'))+facts([
 ('Image','Black <b>śālagrāma</b> stone, small, seated in <b>padmāsana</b>'),
 ('Hands','Two raised, holding <b>conch</b> and <b>discus</b>; two resting in the lap in yoga-mudrā'),
 ('Self-manifest','Counted among the eight <b>svayaṃ-vyakta</b> (self-manifested) images of Viṣṇu'),
 ('Beside him','<b>Kubera</b>, god of wealth; the sage <b>Nārada</b>; <b>Uddhava</b>, Kṛṣṇa’s friend; and <b>Nara-Nārāyaṇa</b>'),
 ('Around','About fifteen more images in the temple, among them Lakṣmī, Garuḍa, Narasiṃha and Gaṇeśa')])))
pages.append(page('shankara','ŚAṄKARA AND THE RIVER','The image found again',fig(560,170,'A young ascetic reaching into a river pool and lifting out a small black image',
 '<rect width="560" height="170" fill="#cfe3f5"/><path d="M0 110 Q280 90 560 112 V170 H0z" fill="#4aa3df"/><ellipse cx="300" cy="130" rx="70" ry="18" fill="#2a7ac0"/>'+person(240,100,'#ff8c1a','#d8a070',1.1)+'<g transform="translate(300 96)"><rect x="-8" y="-14" width="16" height="20" rx="4" fill="#333" stroke="#111"/></g><circle cx="300" cy="90" r="22" fill="#ffd166" opacity=".5"/>'+T(300,160,'NĀRADA KUṆḌA',11,'#fff'))+'''<div class="steps">
<div><b>Lost.</b> Tradition says the image had been hidden in the river long before, in troubled times; some accounts say it was thrown in.</div>
<div><b>Found.</b> <b>Ādi Śaṅkara</b> is said to have recovered it from the <b>Nārada Kuṇḍa</b>, a pool in the Alakanandā, and enshrined it in a cave near the hot springs.</div>
<div><b>Moved.</b> Centuries later, a <b>king of Garhwal</b> moved it to the present temple, in the 16th century by the usual account.</div>
<div><b>The priest.</b> Śaṅkara, from Kerala, began the custom that the chief priest, the <b>Rāval</b>, should be a <b>Nambūdiri</b> brāhmaṇa from Kerala. It holds to this day.</div>
</div>'''))
pages.append(page('rawal','THE RĀVAL','The south serves the north',facts([
 ('Who','A Nambūdiri brāhmaṇa from Kerala, the head priest'),
 ('Assisted by','The <b>Ḍimrī</b> paṇḍits, from the village of Ḍimmar in Garhwal'),
 ('Rite','The worship follows southern rules, unusual in a North Indian temple'),
 ('Offerings','Sugar candy, tulasī and dried fruit')])
 +'<div class="panel reading"><p><b>Two ends of India.</b> Badrīnāth’s god sits in the far north; his priest comes from the far south. It is the clearest single picture of what the Char Dham means: one country, held together by pilgrims and priests travelling its length.</p></div>'
 +talk("Does the Rāval go home in winter?","He goes down with the Lord to Jyotirmaṭh. Where Badrī Viśāl goes, his priest goes.")))
pages.append(page('temple','THE TEMPLE','A painted face in the snows',fig(560,200,'The temple front: a tall painted stone facade with arched windows in bright colours, a gilded roof and a tall gate, steps leading up from the river',
 '<rect width="560" height="200" fill="#cfe3f5"/>'+''.join(f'<path d="M{x} 150 l70 -120 l70 120z" fill="#fff" stroke="#888"/>' for x in (0,420))+'<rect y="150" width="560" height="50" fill="#a0a0a0"/>'+''.join(f'<rect x="{200+i*8}" y="{186-i*6}" width="{160-i*16}" height="6" fill="#ccc" stroke="#111" stroke-width=".8"/>' for i in range(5))+BTEMPLE(280,156,1.5))+facts([
 ('Look','A tall, brightly painted stone front with arched windows: often said to resemble a Buddhist vihāra'),
 ('Plan','Three parts: the <b>garbhagṛha</b> (sanctum), the <b>darśana maṇḍapa</b>, and the <b>sabhā maṇḍapa</b> where pilgrims gather'),
 ('Roof','A gilded roof over the sanctum'),
 ('Rebuilt','Again and again, after avalanches and earthquakes')])
 +talk("Why does it look so different from southern temples?","Snow, quakes and small valleys. Himalayan temples are built tight, tall and painted, not sprawling in stone.")))
pages.append(page('history','HISTORY','A shrine that keeps coming back',tl([
 ('Ancient','Badarikāśrama is praised in the Mahābhārata and the Purāṇas.'),
 ('Āḻvārs','Tamil saints sing of “Vadari”: it becomes one of the 108 <b>Divya Deśams</b>.'),
 ('8th–9th c.','<b>Ādi Śaṅkara</b> re-establishes worship, by tradition; the cave shrine near Tapta Kuṇḍa.'),
 ('16th c.','A king of Garhwal moves the image to the present temple.'),
 ('17th c.','The Garhwal kings enlarge the temple.'),
 ('1803','A great Garhwal earthquake badly damages it; the king of <b>Jaipur</b> funds the rebuilding.'),
 ('British era','The temple comes under British rule; the Garhwal king remains head of its committee.'),
 ('1948 onward','Managed under a state act, by a temple committee for Badrīnāth and Kedārnāth.')])
 +'<div class="panel reading small"><p><b>The Buddhist question.</b> One tradition says the region was once Buddhist and the image was thrown into the river until Śaṅkara restored it. Others read the vihāra-like front as simply Himalayan style. The evidence is thin either way.</p></div>'))
pages.append(page('sacred','AROUND THE TEMPLE','Springs, a skull and a stone',facts([
 ('Tapta Kuṇḍa','Hot sulphur springs just below the temple: pilgrims bathe here before darśana, in air near freezing'),
 ('Nārada Kuṇḍa','The pool in the river where the image was found'),
 ('Sūrya Kuṇḍa','A second sacred pool'),
 ('Brahma Kapāla','A flat rock by the river where <b>śrāddha</b> rites for ancestors are done; held to give the dead the greatest peace'),
 ('Pañca Śilā','Five sacred rocks around the springs, named after Nārada, Narasiṃha, Varāha, Garuḍa and Mārkaṇḍeya')])
 +talk("Hot water in the snows?","God's own geyser. Tradition says Agni lives in Tapta Kuṇḍa, keeping it warm for the pilgrims.")))
pages.append(page('mana','MĀNĀ','Vyāsa’s cave and Bhīma’s bridge',fig(560,170,'A sage writing in a cave while an elephant-headed scribe writes beside him; a single huge rock laid across a roaring stream',
 '<rect width="560" height="170" fill="#e6eef8"/><path d="M20 170 Q60 40 200 40 Q300 60 300 170z" fill="#8a7a6a" stroke="#111" stroke-width="2"/><ellipse cx="160" cy="130" rx="90" ry="40" fill="#3a2a1a"/>'+SAGE(130,140,.8)+'<g transform="translate(200 140) scale(.8)" stroke="#111" stroke-width="2"><circle cy="-30" r="18" fill="#f2a6b0"/><path d="M-6 -20 q-6 20 6 26" stroke="#f2a6b0" stroke-width="7" fill="none"/><rect x="-16" y="-12" width="32" height="30" fill="#ffd60a"/></g>'
 +'<path d="M340 170 v-60 h200 v60" fill="#4aa3df"/><path d="M330 112 q100 -20 220 0 l-10 14 h-200z" fill="#9a8a7a" stroke="#111" stroke-width="2"/>'+T(440,100,'BHĪMA PUL',11,'#0d3f73'))+facts([
 ('Mānā','The last village up the valley, just above Badrīnāth'),
 ('Vyāsa Guphā','The cave where <b>Vyāsa</b> is said to have composed the Mahābhārata'),
 ('Gaṇeśa Guphā','Where <b>Gaṇeśa</b> wrote it down as Vyāsa dictated'),
 ('Bhīma Pul','A great rock across the <b>Sarasvatī</b>, said to have been laid by <b>Bhīma</b> so Draupadī could cross'),
 ('Vasudhārā','A high waterfall beyond Mānā, on the path the Pāṇḍavas are said to have taken on their last journey to heaven')])))
pages.append(page('panch','THE PAÑCA BADRĪ','Five Badrīs of Garhwal','<table class="ct"><tr><th>Badrī</th><th>Where</th><th>What to know</th></tr>'
 '<tr><td><b>Viśāla Badrī</b></td><td>Badrīnāth</td><td>The great one: this temple</td></tr>'
 '<tr><td><b>Yogadhyāna Badrī</b></td><td>Pāṇḍukeśvar</td><td>Viṣṇu in meditation; said to be installed by King Pāṇḍu</td></tr>'
 '<tr><td><b>Bhaviṣya Badrī</b></td><td>Near Jyotirmaṭh</td><td>“Badrī of the future”: where Viṣṇu will be worshipped when the road to Badrīnāth closes</td></tr>'
 '<tr><td><b>Vṛddha Badrī</b></td><td>Near Jyotirmaṭh</td><td>“Old Badrī”: worshipped here before Śaṅkara, by tradition</td></tr>'
 '<tr><td><b>Ādi Badrī</b></td><td>Near Karṇaprayāg</td><td>“First Badrī”: a cluster of old stone temples</td></tr></table>'
 +'<div class="panel reading small"><p>Some lists make seven, the <b>Sapta Badrī</b>, adding Ardha Badrī and Dhyāna Badrī; others swap one name for another.</p></div>'))
pages.append(page('season','THE YEAR AT BADRĪNĀTH','Six months with men, six with gods',facts([
 ('Opening','In spring; the date is fixed each year on <b>Vasanta Pañcamī</b>'),
 ('Closing','Late autumn, after the first snows'),
 ('Winter','The festival image goes down to <b>Jyotirmaṭh</b>, where worship continues'),
 ('The lamp','A lamp is left burning in the closed temple; tradition says it is found still alight in spring'),
 ('Belief','For six months people worship here; for the six of winter, the gods (and Nārada) take over'),
 ('Festival','<b>Mātā Mūrti kā Melā</b>, honouring the mother of Nara-Nārāyaṇa')])))
pages.append(page('connect','IN BOTH CHAR DHAMS','The hinge of two circuits',facts([
 ('Bada Char Dham','The northern abode, for <b>Satya Yuga</b>; with Purī, Rāmeśvaram and Dvārakā'),
 ('Chota Char Dham','The last stop, after Yamunotrī, Gaṅgotrī and Kedārnāth'),
 ('Paired with','<a href="/bhakti/temples-of-india/12-jyotirlingas/kedarnath/">Kedārnāth</a>, Śiva’s shrine on the next ridge'),
 ('Śaṅkara’s maṭha','<b>Jyotirmaṭh</b> just below: the northern seat, for the Atharva Veda'),
 ('Divya Deśam','One of the 108 Viṣṇu shrines sung by the Āḻvārs')])
 +'<div class="key">More: <a href="/bhakti/temples-of-india/char-dham/">Char Dham, the two circuits</a></div>'
 +talk("Kedārnāth and Badrīnāth are a pair?","Śiva and Viṣṇu on neighbouring ridges. Tradition says do both, Kedār first.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Badarī · Badrī','Jujube tree'),('Āśrama','Hermitage'),('Viśāla','Great, vast'),('Śālagrāma','Sacred black stone of Viṣṇu'),('Svayaṃ-vyakta','Self-manifested'),
 ('Rāval','Chief priest of Badrīnāth'),('Kuṇḍa','Pool, spring'),('Kapāla','Skull; here a flat rock'),('Śrāddha','Rites for ancestors'),('Guphā','Cave'),('Pul','Bridge')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The place.</b> High on the Alakanandā, between the Nara and Nārāyaṇa mountains.</div>
<div><b>The legend.</b> Viṣṇu’s endless penance as Nara-Nārāyaṇa; Lakṣmī became the badrī tree over him.</div>
<div><b>The image.</b> A small black śālagrāma in meditation, found by Śaṅkara in the Nārada Kuṇḍa.</div>
<div><b>The custom.</b> A Nambūdiri priest from Kerala; the temple open in summer, worship in Jyotirmaṭh in winter.</div>
<div><b>The place in the lists.</b> Northern Dhām, Himalayan Dhām, Divya Deśam, first of the Pañca Badrī.</div>
</div>'''+talk("One line to remember?","The Lord who sits in snow, under his wife's shade, served by a priest from the other end of India.")+'<div class="key">Jai Badrī Viśāl! 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Badrinath Temple” (Alakanandā, Chamoli; image in padmāsana with conch and discus; Kubera, Nārada, Uddhava, Nara-Nārāyaṇa and fifteen more images; Nārada and Sūrya Kuṇḍas; Śaṅkara in the 9th c.; the Buddhist tradition; Nambūdiri Rāval; Garhwal kings and Jaipur after 1803; British era; 1948 act). New World Encyclopedia, “Badrinath temple” (cave by Tapta Kuṇḍa; 16th-c. move; 17th-c. expansion; Ḍimrī paṇḍits; prasāda; Pañca Badrī; winter move to Jyotirmaṭh). Shri Badarinath–Kedarnath Temple Committee website (śālagrāma image; Uddhava and Nara-Nārāyaṇa positions). Bhāgavata Purāṇa and Mahābhārata (Nara-Nārāyaṇa; Arjuna as Nara), as summarised by tirthayatra.org and templepurohit.com.</p>
<p><b>Around:</b> Wikipedia, “Sapta Badri”; shubhpanchang.com (Mānā, Vyāsa and Gaṇeśa Guphā; three-part plan); storiesofsnatan.blogspot.com and boldsky.com (Mānā caves; Tapta Kuṇḍa; Pañca Badrī list).</p>
<p><b>Sources differ:</b> Śaṅkara’s date (8th or 9th c.); the image’s height; whether it was hidden in the Nārada Kuṇḍa or the Tapta Kuṇḍa. <b>Not verified, tradition only:</b> the lamp found alight in spring; the Pañca Śilā names; the Mātā Mūrti festival; Bhīma Pul; Vasudhārā and the Pāṇḍavas. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('naranarayana','Legend · Nara-Nārāyaṇa'),('lakshmi','Legend · The Badrī Tree'),('image','The Image'),('shankara','Śaṅkara and the River'),('rawal','The Rāval'),
 ('temple','The Temple'),('history','History'),('sacred','Around the Temple'),('mana','Mānā'),('panch','The Pañca Badrī'),('season','The Year at Badrīnāth'),('connect','In Both Char Dhams'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
bk=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ABODE OF THE NORTH</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">BADRĪNĀTH</h1>
  <div class="series">CHAR DHAM · A REFERENCE GUIDE</div>
  <div class="tag">The Lord in the jujube forest</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>High in the Garhwal Himalaya, where the Alakanandā runs between two mountains named after two sages, Viṣṇu is said to sit in meditation that has never ended. Lakṣmī stands over him as a tree.</p>
    <p>His temple is open for only half the year. His priest comes from Kerala, at the other end of India. And his abode is the one place that belongs to <b>both</b> Char Dhams: the great circle around India and the four shrines of the Himalaya.</p>
    <p>This guide tells the legends, the history and the sacred places of <b>Badrīnāth</b>.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Jai Badrī Viśāl,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why only half the year?","Snow. From late autumn to spring the valley is buried, so the Lord's worship moves down to Jyotirmaṭh.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Badrinath.html','w').write(head+bk+tail())
print('ok',len(pages))
