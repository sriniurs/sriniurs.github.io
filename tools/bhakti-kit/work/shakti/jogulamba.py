exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Jogulāmbā · Alampur · The 18 Śakti Pīṭhas · srini.presents',
 'Jogulāmbā of Alampur, the fifth of the 18 Śakti Pīṭhas: the fierce Goddess seated on a corpse with scorpion, frog and lizard in her hair, Bāla Brahmeśvara, the nine Chalukyan Navabrahma temples, the destruction of 1390 and the new temple of 2005, and the Tuṅgabhadrā–Kṛṣṇā confluence. An illustrated reference guide.')
def ap(lat,lon): return 40+(lon-77.2)*260, 20+(17.6-lat)*130
TUNGA=[(15.70,77.20),(15.80,77.60),(15.87,78.00),(15.90,78.15),(16.00,78.27)]
KRSNA=[(16.55,77.20),(16.40,77.60),(16.20,78.00),(16.00,78.27),(16.10,78.60),(16.08,78.87),(16.30,79.10)]
def pth(pts): return 'M'+' L'.join(f'{ap(a,b)[0]:.0f} {ap(a,b)[1]:.0f}' for a,b in pts)
def APMAP(marks,w=560,h=280):
    g=''
    for la,lo,t,side,col in marks:
        x,y=ap(la,lo); r=8 if col=='#c0392b' else 5
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',t,12,'#111','start' if side=='r' else 'end')
    return (f'<rect width="{w}" height="{h}" fill="#f1e6cf"/><path d="{pth(KRSNA)}" stroke="#4aa3df" stroke-width="6" fill="none"/><path d="{pth(TUNGA)}" stroke="#4aa3df" stroke-width="5" fill="none"/>'
     +T(ap(16.45,77.5)[0],ap(16.45,77.5)[1]-10,'KṚṢṆĀ',11,'#1d4f9a')+T(ap(15.72,77.45)[0],ap(15.72,77.45)[1]-14,'TUṄGABHADRĀ',11,'#1d4f9a')
     +T(30,30,'TELANGANA',13,'#7a5a2a','start')+T(w-20,h-14,'ANDHRA PRADESH',13,'#7a5a2a','end')+g+T(w-10,18,'simplified, not to scale',10,'#555','end'))
def JOGU(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-56 62 h112 l-8 -10 h-96z" fill="#9a9a9a"/><path d="M-50 52 q50 -12 100 0" stroke="#d8d0c0" stroke-width="10" fill="none"/>'
 '<path d="M-30 50 q-6 -50 30 -62 q36 12 30 62z" fill="#3a2a2a"/><path d="M-26 44 q26 12 52 0" fill="none" stroke="#e0a800" stroke-width="3"/>'
 '<path d="M-44 -44 q-20 40 0 70 M44 -44 q20 40 0 70" stroke="#1a1a1a" stroke-width="10" fill="none"/>'
 '<circle cy="-24" r="14" fill="#3a2a2a"/><circle cx="-5" cy="-27" r="2.6" fill="#fff"/><circle cx="5" cy="-27" r="2.6" fill="#fff"/><path d="M-3 -16 q3 14 6 0z" fill="#e04040"/>'
 '<path d="M-34 -40 q34 -40 68 0 q-10 -6 -34 -6 q-24 0 -34 6z" fill="#1a1a1a"/>'
 '<g transform="translate(-20 -52)"><ellipse rx="6" ry="3" fill="#7a9a3a"/><path d="M-6 0 l-6 -2 M6 0 l6 2" /></g>'
 '<g transform="translate(0 -60)"><ellipse rx="7" ry="5" fill="#5a9a5a"/><circle cx="-3" cy="-3" r="1.5" fill="#fff"/><circle cx="3" cy="-3" r="1.5" fill="#fff"/></g>'
 '<g transform="translate(20 -52)"><ellipse rx="5" ry="3" fill="#8a4a2a"/><path d="M5 0 q8 -6 4 -10 l-2 3" fill="none"/></g>'
 '<path d="M-22 4 l-22 -14 M22 4 l22 -14" stroke="#3a2a2a" stroke-width="6"/></g>')
def NAGARA(x,y,s=1,c='#d9c7a6'): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-28" y="-24" width="56" height="24" fill="{c}"/>'
 f'<path d="M-22 -24 Q-22 -70 0 -84 Q22 -70 22 -24z" fill="{c}"/>'+''.join(f'<path d="M-22 {-30-k*10} H22" stroke-width="1"/>' for k in range(5))+'<ellipse cy="-86" rx="10" ry="4" fill="#c9a26b"/><rect x="-6" y="-14" width="12" height="14" fill="#3a2a1a"/></g>')
POOL=lambda x,y,w=200: f'<rect x="{x-w/2}" y="{y}" width="{w}" height="18" fill="#4aa3df" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{x-w/2+10+k*30} {y+9} q8 -5 16 0" stroke="#fff" stroke-width="2" fill="none"/>' for k in range(int(w/30)))
GOPT=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-34+k*3} {-k*12} h{68-k*6} l-1 -12 h{-(66-k*6)}z" fill="{["#f7b2b2","#ffd166","#9ad1f5","#c9f0b0"][k%4]}"/>' for k in range(6))+''.join(f'<path d="M{-12+j*6} -72 l2 -10 l2 10z" fill="#e0a800"/>' for j in range(5))+'<rect x="-9" y="-20" width="18" height="20" fill="#5a3a1a"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The fierce Goddess Jogulamba with wild hair, a scorpion, frog and lizard on her head, seated on a corpse; old stone temples by a river behind">'
 '<rect width="380" height="268" fill="#2a0805" rx="8"/><circle cx="190" cy="110" r="90" fill="#7a1d12"/>'+''.join(f'<rect y="{230}" width="380" height="38" fill="#4aa3df"/>' for _ in (0,))
 +NAGARA(46,230,.9)+NAGARA(334,230,.9)+JOGU(190,150,1.7)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Jogulāmbā</b> (Yogāmbā), a fierce form of the Goddess: Pīṭha no. 5 of the eighteen'),
 ('Hymn line','<i>alampure jogulāmbā</i>: “Jogulāmbā in Alampura”'),
 ('Where','<b>Alampur</b>, Telangana, on the Tuṅgabhadrā near where it meets the Kṛṣṇā'),
 ('Body part','Satī’s <b>upper teeth</b>'),
 ('The image','Seated on a <b>corpse</b>, wild hair holding a <b>scorpion</b>, <b>frog</b> and <b>lizard</b>, with a skull'),
 ('Her Lord','Śiva as <b>Bāla Brahmeśvara</b>, in a Chalukya temple worshipped since <b>702 CE</b>'),
 ('Lost and found','Temple destroyed in <b>1390</b>; the image kept in Bāla Brahma for six centuries; a new temple in <b>2005</b>'),
 ('Neighbours','The nine <b>Navabrahma</b> temples (7th–8th c.), Saṅgameśvara and the Papanāśi group'),
 ('Also called','Dakṣiṇa Kāśī; the <b>western gate of Śrīśailam</b>; the district bears her name')])
 +talk("Scorpions and lizards in her hair? Is she scary?","Scary to whatever harms you. To her devotees she's the mother who guards the house.")))
pages.append(page('where','WHERE IT IS','Where two rivers meet',fig(560,280,'Simplified map of the Krishna and Tungabhadra rivers joining near Alampur, with Kurnool across the river, Srisailam downstream and Hyderabad to the north',
 APMAP([(15.88,78.13,'ALAMPUR','r','#c0392b'),(15.83,78.04,'Kurnool','l','#bbb'),(16.07,78.87,'Śrīśailam','r','#ffd166'),(17.39,78.49,'Hyderabad','r','#bbb'),(16.23,77.80,'Gadwal','l','#bbb'),(16.0,78.27,'Saṅgam','l','#9ad1f5')]))+'''<div class="panel reading">
<p><b>The town.</b> Alampur stands on the left bank of the <b>Tuṅgabhadrā</b>, close to where it flows into the <b>Kṛṣṇā</b>, across the river from Kurnool.</p>
<p><b>The confluence.</b> The meeting of the rivers, the Saṅgam, was holy ground; much of it now lies under the waters of the <b>Śrīśailam dam</b>.</p>
<p><b>Śrīśailam’s gate.</b> Alampur is called the <b>western gateway</b> to Śrīśailam, the next pīṭha in the hymn, downstream on the Kṛṣṇā.</p>
</div>'''))
pages.append(page('names','HER NAMES','Yoga, mother and guardian',facts([
 ('Jogulāmbā','The Telugu form of <b>Yogāmbā</b>, “Mother of yoga”: she grants siddhi in yoga'),
 ('Yogāmbā','Her Sanskrit name; the pīṭha is called the <b>Yoginī Pīṭha</b>'),
 ('Gṛha Caṇḍī','“Caṇḍī of the home”: protector of households'),
 ('Alampura','The hymn’s name; in older records Halampura, and “Hatampura” in an inscription of 1101'),
 ('Dakṣiṇa Kāśī','“Kāśī of the South”, for its many temples by the sacred river')])
 +talk("A fierce goddess who protects the home?","The fiercest guard dog is the one on your side. That's Gṛha Caṇḍī.")))
pages.append(page('pitha','THE PĪṬHA','Where Satī’s upper teeth fell',fig(560,150,'Shiva carrying Sati across a night sky, a glowing piece falling onto temples beside two joining rivers',
 '<rect width="560" height="150" fill="#2a0805"/>'+STAR+SHIVA(140,60,.7)+SATI(162,64,.55,-10)+'<path d="M190 80 q80 10 190 40" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><circle cx="382" cy="120" r="6" fill="#ffd166"/><path d="M300 150 L420 130 L560 140 M420 130 L520 100" stroke="#4aa3df" stroke-width="6" fill="none"/>'+NAGARA(450,128,.4)+T(440,24,'ALAMPURA',14,'#ffd166'))+'''<div class="panel reading">
<p><b>The verse.</b> <i>alampure jogulāmbā, śrīśaile bhramarāmbikā</i>: Alampur and Śrīśailam are named in the same breath, and stand on the same river system.</p>
<p><b>What fell here.</b> Satī’s <b>upper teeth</b> (<i>ūrdhva danta</i>). A fierce Goddess with bared teeth and outstretched tongue keeps the memory.</p>
<p><b>A Yoginī seat.</b> Among the eighteen, Alampur is the <b>Yoginī Pīṭha</b>: the seat of the Goddess as mistress of yoga and tantric power.</p>
</div>'''))
pages.append(page('goddess','THE GODDESS','Ugra: the fierce form',fig(560,230,'The Goddess seated on a reclining corpse, wild black hair spreading out with a scorpion, frog and lizard on her head, tongue out, inside a shrine ringed by a pool of water',
 '<rect width="560" height="230" fill="#fde4e4"/><rect x="160" y="10" width="240" height="190" fill="#f3e3c3" stroke="#111" stroke-width="2"/>'+JOGU(280,120,1.7)+POOL(280,204,360)
 +T(90,60,'SCORPION',12,'#7a1d12')+T(90,80,'FROG',12,'#7a1d12')+T(90,100,'LIZARD',12,'#7a1d12')+T(90,120,'SKULL',12,'#7a1d12')+T(470,80,'ON A',12,'#7a1d12')+T(470,100,'CORPSE',12,'#7a1d12'))+'''<div class="g2">
<div class="card bg-red"><h4>🔥 The image</h4><p>She sits in an <b>ugra</b> (fierce) form on a corpse, tongue out, her great mass of hair holding a <b>scorpion</b>, a <b>frog</b>, a <b>lizard</b> and a <b>skull</b>; some describe a bat or an owl as well.</p></div>
<div class="card bg-yellow"><h4>🦂 What they mean</h4><p>Devotees read them as her mastery over <b>poison</b> (scorpion), <b>disease</b> (frog) and hidden harm (lizard), and over death itself (corpse and skull).</p></div>
</div><div class="panel reading small"><p><b>With her</b> in the sanctum: her two attendant powers <b>Caṇḍī</b> and <b>Muṇḍī</b>, the Saptamātṛkās, Gaṇeśa and Vīrabhadra with a vīṇā. The new temple is ringed by a pool of water, said to cool her fiery form.</p></div>'''))
pages.append(page('brahmesvara','BĀLA BRAHMEŚVARA','Her Lord, and her refuge',fig(560,170,'An old Chalukya stone temple with a curved tower, a lingam inside, and the small Goddess image sheltered in a side niche',
 '<rect width="560" height="170" fill="#e6eef8"/>'+NAGARA(220,160,1.6)+'<path d="M206 156 v-16 a14 14 0 0 1 28 0 v16z" fill="#3a3a3a" stroke="#111"/>'+'<rect x="330" y="80" width="80" height="80" fill="#d9c7a6" stroke="#111" stroke-width="2"/>'+JOGU(370,124,.42)+T(370,74,'1390–2005',12,'#7a1d12'))+facts([
 ('Deity','Śiva as <b>Bāla Brahmeśvara</b>, Jogulāmbā’s consort'),('Temple','One of the nine Navabrahma temples, in continuous worship since <b>702 CE</b>'),
 ('The liṅga','Of irregular shape, likened by devotees to the hoof-print of a bull'),('Refuge','For about six centuries the Goddess’s image was kept here, after her own temple fell'),
 ('Today','Caṇḍī and Muṇḍī’s original images remain here; new ones were made for the new temple')])
 +talk("The Goddess lived in her husband's temple for 600 years?","Where else would she go? Bāla Brahmeśvara kept her safe until her house was rebuilt.")))
pages.append(page('legend','THE LEGENDS','Brahmā’s penance and the alchemist',fig(560,160,'Four-headed Brahma in meditation by a river, Shiva appearing before him as a lingam of light; on the right, an alchemist with a pot and herbs',
 '<rect width="560" height="160" fill="#ffe9c4"/>'+''.join(f'<circle cx="{140+d}" cy="70" r="10" fill="#f2c79b" stroke="#111"/>' for d in (-16,0,16))+person(140,110,'#c0392b','#f2c79b',1)+'<path d="M200 140 v-60 a20 20 0 0 1 40 0 v60z" fill="#ffd166" opacity=".8" stroke="#111"/>'
 +person(430,120,'#7a5a2a','#c98b5a',1)+'<ellipse cx="480" cy="128" rx="20" ry="10" fill="#c98b2a" stroke="#111"/><path d="M470 118 q10 -20 20 0" stroke="#2a7a4a" stroke-width="3" fill="none"/>'+T(430,24,'RASA SIDDHA',12,'#7a1d12'))+'''<div class="steps">
<div><b>Brahmā’s penance.</b> Local tradition says <b>Brahmā</b> did penance here to Śiva, who appeared to him. That is why the nine Śiva temples are all called “Brahma”: Bāla Brahma, Svarga Brahma and the rest.</div>
<div><b>The alchemist.</b> Another story tells of <b>Rasa Siddha</b>, a master of alchemy who could turn base metal to gold, said to have begun the temples at Śiva’s bidding. Some even say the nine names were the names of his medicinal herbs.</div>
<div><b>The Goddess.</b> In the Śakti story, she is here because Satī’s teeth fell here; in the local one, because Śiva and Brahmā’s holy ground needed a guardian.</div>
</div><div class="panel reading small"><p>These are local traditions; the inscriptions name Chalukya kings and queens as the builders.</p></div>'''))
pages.append(page('history','HISTORY','Thirteen centuries at Alampur',tl([
 ('Before 610s','The <b>Saṅgameśvara</b> temple at the confluence: a label inscription places it before Pulakeśin II, making it the oldest Chalukya temple here.'),
 ('640–753','The <b>Badami Chalukyas</b> build the nine Navabrahma temples.'),
 ('681–696','<b>Svarga Brahma</b> is built by Lokāditya Ela Arasa in honour of King Vinayāditya’s queen.'),
 ('702','<b>Bāla Brahma</b> begins its unbroken worship.'),
 ('9th–11th c.','Rāṣṭrakūṭas and later Chalukyas build the <b>Papanāśi</b> temples.'),
 ('1390','The Jogulāmbā temple is destroyed by the <b>Bahmani</b> army; the image is taken to Bāla Brahma.'),
 ('After 1390','Vijayanagara’s <b>Harihara II</b> is said to have sent troops and fortified the temple complex.'),
 ('1979','Saṅgameśvara is moved, stone by stone, before the Śrīśailam dam floods its site.'),
 ('2005','A new Jogulāmbā temple rises on the old site, <b>615 years</b> later, and the image returns.'),
 ('2016','Telangana names a new district <b>Jogulāmbā Gadwal</b>.')])))
pages.append(page('navabrahma','THE NINE BRAHMAS','Northern towers in the South',fig(560,170,'Nine small stone temples with curved northern-style towers in a walled courtyard by a river',
 '<rect width="560" height="170" fill="#f3e3c3"/><rect y="150" width="560" height="20" fill="#4aa3df"/>'+''.join(NAGARA(40+k*60,148,.55+(.1 if k in (3,7) else 0),'#d9c7a6' if k%2 else '#c9b796') for k in range(9)))
 +'<table class="ct"><tr><th>Temple</th><th>Note</th><th>Temple</th><th>Note</th></tr>'+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td><b>{c}</b></td><td>{d}</td></tr>' for a,b,c,d in (
 ('Kumāra Brahma','the earliest','Garuḍa Brahma',''),('Arka Brahma','a Chalukya queen’s liṅga','Viśva Brahma','richly carved'),('Vīra Brahma','','Padma Brahma','the largest, partly ruined'),
 ('Bāla Brahma','in worship since 702','Tāraka Brahma','southern-style tower'),('Svarga Brahma','681–696, the finest','','')))+'</table>'
 +'<div class="panel reading small"><p><b>Why they matter.</b> Eight of the nine have curved northern (<b>Nāgara</b>) towers, unusual this far south; their friezes even show Pañcatantra fables. Historians see them as a link to later Kākatīya temple art.</p></div>'))
pages.append(page('sangama','SAṄGAMEŚVARA','The temple that moved',fig(560,160,'A stone temple being taken apart block by block, numbered stones carried to a new site on high ground while water rises over the old one',
 '<rect width="560" height="160" fill="#eaf6ff"/><rect y="110" width="260" height="50" fill="#4aa3df"/>'+''.join(f'<rect x="{30+k*24}" y="{96-(k%3)*8}" width="18" height="12" fill="#d9c7a6" stroke="#111" stroke-width="1.2"/>' for k in range(8))
 +'<path d="M250 80 q60 -40 120 0" stroke="#111" stroke-width="2" stroke-dasharray="6 4" fill="none" marker-end=""/>'+NAGARA(450,140,1.1)+T(450,154,'REBUILT NEAR ALAMPUR',10,'#555')+T(130,150,'OLD SITE · KUḌAVELLI',10,'#fff'))+'''<div class="steps">
<div><b>At the confluence.</b> The Saṅgameśvara temple stood at <b>Kuḍavelli</b>, where the Tuṅgabhadrā meets the Kṛṣṇā, about 20 km from Alampur.</div>
<div><b>The dam.</b> The Śrīśailam reservoir was going to drown it. The Archaeological Survey took it apart <b>block by block</b>.</div>
<div><b>Rebuilt.</b> It was put back together near Alampur in <b>1979</b>, after years of work. The Navabrahma temples too were protected from the rising water.</div>
</div>'''))
pages.append(page('papanasi','PAPANĀŚI AND THE MUSEUM','More temples, more stones',facts([
 ('Papanāśi','A group of <b>23 temples</b>, 9th–11th c., about 2.5 km south-west of Alampur, by the Rāṣṭrakūṭas and later Chalukyas'),
 ('The museum','At the entrance of the Bāla Brahma complex: sculptures and inscriptions from the Navabrahma temples and the drowned villages'),
 ('Inscriptions','Old Kannada and Telugu records of kings, queens and gifts, from the 7th century onward')])
 +talk("So Alampur is really a museum town?","A living one. Worship never stopped at Bāla Brahma, even when the Goddess had no home.")))
pages.append(page('festivals','WORSHIP AND FESTIVALS','Her days',facts([
 ('Navarātri','The great festival of the Goddess, Dasara'),('Mahāśivarātri','For Bāla Brahmeśvara'),
 ('Tuesdays &amp; Fridays','Her weekly days'),('Amāvāsyā &amp; Pūrṇimā','New and full moon days, for special worship'),
 ('For the home','As Gṛha Caṇḍī, she is prayed to for the protection of the household')])
 +talk("Why is she prayed to for houses?","Because a scorpion, a frog and a lizard are what you'd find in an old house. She rules them all.")+'<div class="key">The Mother of yoga, <b>guardian of the home</b>.</div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Jogulāmbā / Yogāmbā','Mother of yoga'),('Ugra','Fierce'),('Śava','Corpse'),('Yoginī Pīṭha','A seat of the Goddess as yoginī'),('Gṛha Caṇḍī','Caṇḍī of the home'),
 ('Navabrahma','The nine “Brahma” Śiva temples'),('Nāgara','The northern style of temple tower'),('Saṅgama','A confluence'),('Siddhi','Spiritual power or attainment'),('Rasa Siddha','A master of alchemy')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Goddess.</b> Jogulāmbā, Mother of yoga, fierce, seated on a corpse with scorpion, frog and lizard in her hair; Satī’s upper teeth fell here.</div>
<div><b>Her Lord.</b> Bāla Brahmeśvara, worshipped since 702, who sheltered her image for six hundred years.</div>
<div><b>The place.</b> Alampur on the Tuṅgabhadrā, near the Kṛṣṇā, the western gate of Śrīśailam.</div>
<div><b>The history.</b> Nine Chalukya temples; destruction in 1390; Saṅgameśvara moved in 1979; a new temple in 2005.</div>
<div><b>The legends.</b> Brahmā’s penance and Rasa Siddha the alchemist.</div>
</div>'''+talk("One line to remember?","A fierce mother who waited six hundred years to go home, and did.")+'<div class="key">The fifth seat of the Mother: <b>Jogulāmbā of Alampur</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Jogulamba Temple, Alampur”: upper teeth; ugra form on a corpse with scorpion, frog and lizard; Bahmani destruction; Harihara II; image in Bāla Brahma; rebuilt 2005. Wikipedia, “Alampur”: Navabrahma (7th–8th c., Badami Chalukyas); 1390 destruction and 615 years; Saṅgameśvara’s pre-Pulakeśin inscription, Kuḍavelli, moved 1979; museum; Papanāśi (23 temples, 9th–11th c.); Halampura and the 1101 “Hatampura” inscription. ASI Hyderabad Circle: nine names; Kumāra Brahma earliest; Padma Brahma largest; Bāla Brahma in worship since 702. Navabrahma article (Svarga Brahma 681–696, Lokāditya Ela Arasa). telangana360.com (Arka Brahma inscription; Tāraka Brahma’s southern style). ecoheritage.cpreec.org (640–753; the bull-hoof liṅga). templepurohit.com, hinduscriptures.in, indianetzone.com (hair with bat and skull; Caṇḍī and Muṇḍī; Saptamātṛkās; Gṛha Caṇḍī). templeconnect.com (Yoginī Pīṭha; western gateway of Śrīśailam; Dakṣiṇa Kāśī). Outlook Traveller (Rasa Siddha and the herb names).</p>
<p><b>Sources differ:</b> creatures in her hair (some add a bat or owl); the start date of the Navabrahma group. <b>Not verified:</b> Harihara II’s fortification (said to be); the Brahmā and Rasa Siddha legends (local tradition). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('goddess','The Goddess'),('brahmesvara','Bāla Brahmeśvara'),('legend','The Legends'),('history','History'),('navabrahma','The Nine Brahmas'),
 ('sangama','Saṅgameśvara'),('papanasi','Papanāśi and the Museum'),('festivals','Worship and Festivals'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 5 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">JOGULĀMBĀ</h1>
  <div class="series">ALAMPUR · A REFERENCE GUIDE</div>
  <div class="tag">The fierce Mother of yoga</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>On the bank of the Tuṅgabhadrā, among nine Chalukya temples thirteen centuries old, sits a Goddess with bared teeth and wild hair full of creatures: <b>Jogulāmbā</b>.</p>
    <p>Her temple was destroyed in 1390. Her image waited in her husband’s shrine for six hundred years, until a new temple was built on the old site in 2005.</p>
    <p>This guide tells her story, and the story of Alampur’s temples: one moved stone by stone to escape a dam.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Jogulāmbā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why does her temple look so new next to such old ones?","It is new: built in 2005. The Goddess inside is the old one, home after six hundred years.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Jogulamba.html','w').write(head+b+tail())
print('ok',len(pages))
