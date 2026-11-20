import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
import common_t
def head_navy(title,desc):
    h=open(common_t.SRC).read(); hd=h[:h.find('<div class="book">')]
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
head=head_navy('Talakāḍu · The Buried Temples · Temples around Mysuru · srini.presents',
 'Talakāḍu on the Kāverī: the Gaṅga capital buried under sand, the five liṅgas of the Pañcaliṅga Darśana, Vaidyeśvara and Kīrtinārāyaṇa, Alamelamma’s curse, and what science says about the dunes. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def TEMPLE(x,y,s=1,buried=0):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="#f2e6c8"/><path d="M-14 -16 h28 l-4 -10 h-20z M-10 -26 h20 l-4 -10 h-12z" fill="#e2cfa8"/><circle cy="-40" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
    if buried: g+=f'<path d="M{x-40*s} {y} Q{x} {y-buried*s} {x+40*s} {y}z" fill="#e8d29a" stroke="#111" stroke-width="1"/>'
    return g
def DUNES(y,w=560,c='#e8d29a'): return f'<path d="M0 {y} Q70 {y-40} 140 {y-10} T280 {y-14} T420 {y-6} T{w} {y-20} V{y+60} H0z" fill="{c}" stroke="#b89a5a" stroke-width="2"/>'
def LINGA(x,y,s=1,c='#3a3a3a'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 0 h60 l-6 -10 h-48z" fill="#8a8a8a"/><path d="M20 -6 h18 l-3 5 h-15z" fill="#8a8a8a"/><path d="M-12 -10 v-26 a12 12 0 0 1 24 0 v26z" fill="{c}"/><path d="M-8 -30 h16 M-8 -26 h16 M-8 -22 h16" stroke="#fff" stroke-width="2"/></g>'
def QUEEN(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cy="-36" r="12" fill="#f2c79b"/><path d="M-12 -40 q12 -16 24 0 v20 M-12 -40 v20" fill="none" stroke="#2b1a0e" stroke-width="4"/><path d="M-10 -48 h20 l-3 -8 h-14z" fill="#e0a800"/><path d="M-22 44 q22 -80 44 0z" fill="#7a3fa0"/><path d="M14 -10 l24 -16" stroke="#f2c79b" stroke-width="5"/><circle cx="40" cy="-28" r="5" fill="#ffd60a"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Temple towers half-buried in golden sand dunes beside the curving Kaveri, with only their tops showing">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/><circle cx="300" cy="60" r="34" fill="#ffd166" opacity=".4"/>'
 '<path d="M0 250 C 120 230, 200 268, 380 240 V268 H0z" fill="#4aa3df"/>'+TEMPLE(110,190,1.6)+TEMPLE(270,200,1.3)+DUNES(230,380)+TEMPLE(190,210,1.1,50)+LINGA(320,140,.0)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Place','<b>Talakāḍu</b> (Talakad), Mysuru district, Karnataka, on the left bank of the <b>Kāverī</b> where the river bends'),
 ('Famous for','A town of <b>30+ temples</b>, most now buried under sand dunes stretching about a mile'),
 ('Five liṅgas','<b>Vaidyeśvara</b>, <b>Pātāleśvara</b>, <b>Maraḷeśvara</b>, <b>Arkeśvara</b> and <b>Mallikārjuna</b>: the five faces of Śiva'),
 ('Rare festival','The <b>Pañcaliṅga Darśana</b>, held only when a rare combination falls in Kārtika: last in <b>2020</b>'),
 ('Capital','Seat of the <b>Western Gaṅgas</b>; taken by the <b>Cōḻas</b> (renamed Rājarājapura), then by the Hoysaḷa <b>Viṣṇuvardhana</b>'),
 ('Viṣṇu','<b>Kīrtinārāyaṇa</b>, built in <b>1117</b> to mark the Hoysaḷa victory'),
 ('The curse','<b>Alamelamma</b>, 1610: “May Talakāḍu turn to sand…”'),
 ('Science','Geologists and ecologists offer three explanations for the dunes')])
 +talk("A whole town under sand? Like a desert?","On the bank of a river, in green Karnataka! That's what makes it so strange, and so famous.")))
mapfig=fig(560,240,'Schematic map: the Kaveri bending around Talakadu, with sand dunes on the left bank covering the old town, Vaidyeshvara and Kirtinarayana among them, Malangi across the river, Vijayapura with Arkeshvara, and Mudukutore with Mallikarjuna on its hill. Not to scale.',
 '<rect width="560" height="240" fill="#eef6e4"/><path d="M0 60 C 200 40, 300 120, 260 180 C 230 220, 380 236, 560 210" fill="none" stroke="#4aa3df" stroke-width="20"/>'
 +'<path d="M30 110 Q110 70 190 100 Q230 130 210 170 Q140 200 60 180 Q20 150 30 110z" fill="#e8d29a" stroke="#b89a5a" stroke-width="2"/>'+T(110,92,'SAND DUNES · OLD TALAKĀḌU',10,'#7a5a2a')
 +''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}" stroke="#111"/>'+T(x+(9 if a=="start" else -9),y+4,n,9,'#0b2a4a',a) for x,y,c,n,a in ((90,130,'#0b2a4a','VAIDYEŚVARA','start'),(150,150,'#3b6fd0','KĪRTINĀRĀYAṆA','start'),(70,160,'#0b2a4a','PĀTĀLEŚVARA','start'),(120,176,'#0b2a4a','MARAḶEŚVARA','start')))
 +'<circle cx="330" cy="130" r="7" fill="#c0392b" stroke="#111"/>'+T(342,134,'MĀLAṄGI (across the river)',9,'#c0392b','start')
 +'<circle cx="460" cy="70" r="6" fill="#0b2a4a" stroke="#111"/>'+T(450,60,'ARKEŚVARA · VIJAYAPURA',9,'#0b2a4a','end')
 +'<path d="M430 236 Q470 170 510 236z" fill="#8a9a6a" stroke="#111"/><circle cx="470" cy="196" r="6" fill="#0b2a4a" stroke="#111"/>'+T(470,186,'MALLIKĀRJUNA · MUDUKUTORE',9,'#0b2a4a')+T(80,234,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','A river bend full of sand',mapfig+'''<div class="panel reading">
<p><b>The bend.</b> Talakāḍu lies on the left bank of the Kāverī, south-east of Mysuru, at the point where the eastward-flowing river changes course.</p>
<p><b>The sand.</b> Here the river spreads sand over a wide area. The old city lies under dunes nearly a mile long; once, only the tops of two gopurams showed above them.</p>
<p><b>The five liṅgas.</b> Three stand in the dunes around the old town; Arkeśvara is at Vijayapura nearby, and Mallikārjuna on the hill of Mudukutore.</p>
</div>'''))
pages.append(page('name','THE NAME','Tala, Kāḍu and the elephants',fig(560,170,'Two hunter brothers watching wild elephants worship a Shiva image in a tree; the elephants transform into sages',
 '<rect width="560" height="170" fill="#e8f5e2"/><circle cx="280" cy="60" r="44" fill="#3a8a3a" stroke="#111" stroke-width="2"/><rect x="272" y="96" width="16" height="74" fill="#6a4a2a" stroke="#111"/>'+LINGA(280,90,.7)
 +''.join(f'<g transform="translate({x} 160)" stroke="#111" stroke-width="2"><ellipse cy="-26" rx="30" ry="20" fill="#9a9aa8"/><circle cx="{d*30}" cy="-34" r="13" fill="#9a9aa8"/></g>' for x,d in ((190,1),(370,-1)))
 +person(80,166,'#7a5a2a','#8a5a3a',.8)+person(120,166,'#7a5a2a','#8a5a3a',.8)+T(100,162,'',8)+T(100,30,'TALA · KĀḌU',11,'#0b2a4a'))+'''<div class="steps">
<div><b>Two hunters.</b> Tradition tells of twin brothers of the Kirāta (hunter) people, <b>Tala</b> and <b>Kāḍu</b>, who found an image of Śiva in a tree being worshipped by wild elephants.</div>
<div><b>The elephants were sages.</b> The elephants were really ṛṣis in disguise. All of them, the brothers too, attained liberation, and the place took the brothers’ names: <b>Tala-kāḍu</b>.</div>
<div><b>Other names.</b> In Sanskrit it became <b>Daḷavana</b> (Daḷavanapura); the forest was <b>Gajāraṇya</b>, the elephant forest. Tradition also says <b>Rāma</b> halted here on his way to Laṅkā.</div>
</div>'''))
pl=('<table class="ct"><tr><th>Liṅga</th><th>Also called</th><th>Where</th></tr>'+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a,b,c in (
 ('Vaidyeśvara','Vaidyanātheśvara, the healer; with the Goddess Manonmaṇī','Talakāḍu, the chief temple'),('Pātāleśvara','Vāsukīśvara','Talakāḍu, in the dunes'),('Maraḷeśvara','Saikateśvara, “Lord of the sand”','Talakāḍu, in the dunes'),
 ('Arkeśvara','Lord of the Sun','Vijayapura, nearby'),('Mallikārjuna','with the Goddess Bhramarāmbā','Mudukutore hill, nearby')))+'</table>')
pages.append(page('pancalinga','THE FIVE LIṄGAS','Pañcaliṅga: the five faces of Śiva',fig(560,120,'Five lingas in a row, one for each face of Shiva',
 '<rect width="560" height="120" fill="#eef3fa"/>'+''.join(LINGA(70+i*105,100,1.1)+T(70+i*105,116,n,9,'#0b2a4a') for i,n in enumerate(('VAIDYEŚVARA','PĀTĀLEŚVARA','MARAḶEŚVARA','ARKEŚVARA','MALLIKĀRJUNA'))))+pl+'''<div class="panel reading">
<p><b>Five faces.</b> The five are held to stand for the five faces of Śiva (Sadyojāta, Vāmadeva, Aghora, Tatpuruṣa and Īśāna). One account names Arkeśvara as the Tatpuruṣa face and Mallikārjuna as the Vāmadeva face.</p>
<p><b>Sand and serpent.</b> Pātāleśvara is the Lord of the underworld, Vāsuki’s Lord; Maraḷeśvara, Saikateśvara, is the Lord of the sand itself.</p>
</div>'''))
pages.append(page('darshana','THE PAÑCALIṄGA DARŚANA','A festival that waits for the stars',facts([
 ('When','On the <b>new-moon day of Kārtika</b>, when it falls on a <b>Monday</b> and the auspicious <b>Kuhu yoga</b> coincides with the right star (Viśākhā in most accounts)'),
 ('How often','Not on a fixed cycle: gaps of 3, 5, 7, 9 or 12 years are described'),
 ('Recent','<b>2006</b>, <b>2009</b>, <b>2013</b> and <b>2020</b> (the last held quietly, during the pandemic)'),
 ('Next','After 2020, officials named <b>2033</b> as the next'),
 ('The round','Pilgrims bathe in the Kāverī and at the Gokarṇa tīrtha, worship Gokarṇeśvara, then visit all five liṅgas in a single auspicious window'),
 ('Sand cleared','Before each Darśana, the sand is cleared from the buried temples so they can be reached')])
 +'''<div class="panel reading small"><p><b>Sources differ</b> on the exact star (Viśākhā, Jyeṣṭhā), on whether the day is the new moon or full moon, and on the cycle. All agree it is rare, falls in Kārtika, and draws huge crowds.</p></div>'''
 +talk("It only happens when the stars line up?","And the calendar, and the weekday! Miss one, and you may wait seven years or more.")))
pages.append(page('vaidyesvara','VAIDYEŚVARA','The healer, and the grandest temple',fig(560,170,'The Vaidyeshvara temple with its tall entrance tower and two giant door guardians at the hall entrance',
 '<rect width="560" height="170" fill="#f6f1e2"/>'+TEMPLE(280,160,2.4)+''.join(f'<g transform="translate({x} 160)" stroke="#111" stroke-width="2"><rect x="-10" y="-80" width="20" height="80" fill="#8a8a8a"/><circle cy="-88" r="10" fill="#8a8a8a"/></g>' for x in (170,390))+T(170,40,'DVĀRAPĀLA',10)+T(390,40,'DVĀRAPĀLA',10))+facts([
 ('The Lord','<b>Vaidyeśvara</b>, Śiva the physician; his Goddess is <b>Manonmaṇī</b>'),
 ('Dates','Consecrated in the <b>10th century</b>, with additions up to the <b>14th</b>'),
 ('Style','The largest and most ornate temple of the group, mixing <b>Gaṅga</b>, <b>Cōḻa</b> and <b>Hoysaḷa</b> features'),
 ('Guardians','A pair of <b>10-ft</b> dvārapālas at the entrance of the dance hall'),
 ('The enclosure','A large prākāra wall with sculptures from Gaṅga, Hoysaḷa and Vijayanagara times; a five-headed serpent carved with a stone chain')])
 +'<div class="panel reading small"><p><b>The sick prince.</b> It was to this temple that the Vijayanagara viceroy came to pray for a cure, the start of Alamelamma’s story.</p></div>'))
pages.append(page('kirtinarayana','KĪRTINĀRĀYAṆA','A victory temple of 1117',fig(560,160,'A Hoysala temple on a raised platform with a tall standing Vishnu inside, the sand piled around it',
 '<rect width="560" height="160" fill="#eef3fa"/>'+DUNES(150)+'<rect x="180" y="80" width="200" height="60" fill="#e2cfa8" stroke="#111" stroke-width="2"/><rect x="170" y="140" width="220" height="12" fill="#c9a26b" stroke="#111"/><path d="M220 80 l60 -50 l60 50z" fill="#d9c9a0" stroke="#111" stroke-width="2"/>'
 +'<g transform="translate(280 136)" stroke="#111" stroke-width="2"><path d="M-10 0 h20 l-2 -34 h-16z" fill="#ffd60a"/><circle cy="-42" r="8" fill="#3b6fd0"/><path d="M-8 -50 h16 l-3 -10 h-10z" fill="#e0a800"/></g>')+facts([
 ('Built','<b>1117</b>, by the Hoysaḷa king <b>Viṣṇuvardhana</b>, after defeating the Cōḻas at Talakāḍu'),
 ('Title','Viṣṇuvardhana took the title <b>Talakāḍugoṇḍa</b>, “conqueror of Talakāḍu”'),
 ('The image','A tall standing <b>Nārāyaṇa</b>, about 2–2.5 m, on a Garuḍa pedestal'),
 ('Plan','A star-shaped (stellate) sanctum, an open vestibule and a hall with three entrances, on a raised platform (<i>jagati</i>)'),
 ('Rescued','Excavated from the dunes, its great gateway recovered; taken apart and rebuilt by the ASI')])
 +talk("Built for a victory?","Kīrti means fame. Kīrtinārāyaṇa: Viṣṇu of the famous victory. Kings liked to say thank you in stone!")))
pages.append(page('history','HISTORY','Capital, prize and ruin',tl([
 ('c. 350–999','The <b>Western Gaṅgas</b>; tradition says Harivarma lived at Daḷavanapura, and later Gaṅga kings were crowned here when it became their capital.'),
 ('Early 1000s','The <b>Cōḻas</b> defeat the Gaṅgas, take Talakāḍu and rename it <b>Rājarājapura</b>.'),
 ('1116–17','The Hoysaḷa <b>Viṣṇuvardhana</b> drives out the Cōḻas and builds Kīrtinārāyaṇa. Talakāḍu grows to seven towns and five maṭhas.'),
 ('14th c.','Vijayanagara rule; the minister <b>Mādhavamantri</b>, a native of Talakāḍu, builds an anicut (dam) across the Kāverī.'),
 ('1610','<b>Rāja Woḍeyar</b> of Mysuru takes Talakāḍu; Alamelamma’s curse.'),
 ('1600s on','The sands advance, burying temple after temple.'),
 ('1800s–today','Temples dug out again: Ānandeśvara and Gaurīśaṅkara in the 19th century; ASI excavations in 1992–93 and after.')])))
curse=fig(560,170,'A queen standing on the riverbank throwing her jewels into the Kaveri, with soldiers approaching behind her and a whirlpool forming in the river',
 '<rect width="560" height="170" fill="#e8f0fa"/><path d="M0 120 q280 -20 560 0 V170 H0z" fill="#4aa3df"/>'+QUEEN(200,110,1.1)
 +'<g transform="translate(330 146)" fill="none" stroke="#fff" stroke-width="3"><ellipse rx="40" ry="12"/><ellipse rx="26" ry="8"/><ellipse rx="12" ry="4"/></g>'
 +''.join(person(x,110,'#7a5a2a','#c98b5a',.6) for x in (60,90,120))+'<path d="M240 82 q30 -20 70 40" stroke="#e0a800" stroke-width="2" stroke-dasharray="4 4" fill="none"/>')
pages.append(page('curse','ALAMELAMMA’S CURSE','A queen, her jewels and the river',curse+'''<div class="steps">
<div><b>A dying viceroy.</b> Tirumala Rāya (Śrīraṅga Rāya), the Vijayanagara representative at Śrīraṅgapaṭṭaṇa, came to Talakāḍu to pray at Vaidyeśvara for a cure. His wife <b>Alamelamma</b> left Śrīraṅgapaṭṭaṇa in the care of <b>Rāja Woḍeyar</b> of Mysuru and joined him.</div>
<div><b>The jewels.</b> The story says Rāja Woḍeyar wanted her jewels, and when she would not give them, sent an army. In <b>1610</b> he took Talakāḍu.</div>
<div><b>The river.</b> Alamelamma went to the Kāverī, threw her jewels into the water, and drowned herself opposite Mālaṅgi.</div>
<div><b>The curse.</b> As she died, the story says, she spoke three lines:<br><i>Talakāḍu maraḷāgi, Mālaṅgi maḍuvāgi, Maisūru dhorege makkaḷāgade hōgali.</i><br>“May Talakāḍu turn to sand, Mālaṅgi become a whirlpool, and the kings of Mysuru have no heirs.”</div>
</div>
<div class="panel reading small"><p><b>A living legend.</b> Popular belief links the sand of Talakāḍu, the whirlpool at Mālaṅgi and the Woḍeyars’ many adoptions of heirs to these words. The tale itself comes from tradition; versions differ on the details.</p></div>'''))
sci=fig(560,150,'Three panels: a dam across the river, wind blowing sand from a riverbank, and cracks in the ground from an earthquake',
 '<rect width="560" height="150" fill="#f2f6ff"/>'+''.join(f'<rect x="{10+i*184}" y="10" width="172" height="130" rx="8" fill="#fff" stroke="#111" stroke-width="2"/>' for i in range(3))
 +'<path d="M20 90 h152" stroke="#4aa3df" stroke-width="16"/><rect x="80" y="70" width="20" height="40" fill="#8a7a6a" stroke="#111"/>'+T(96,130,'THE DAM',10,'#0b2a4a')
 +'<path d="M204 110 Q250 80 290 100 T350 96 V120 H204z" fill="#e8d29a" stroke="#b89a5a"/>'+''.join(f'<path d="M{a} {b} q20 -6 40 0" stroke="#555" stroke-width="2" fill="none"/>' for a,b in ((214,50),(234,64),(254,44)))+T(280,130,'THE WIND',10,'#0b2a4a')
 +'<path d="M388 100 l30 -10 l-10 20 l30 -14 l-6 18 l40 -12 l40 4" stroke="#7a5a2a" stroke-width="3" fill="none"/>'+T(464,130,'THE EARTH',10,'#0b2a4a'))
pages.append(page('science','WHY THE SAND?','Three scientific explanations',sci+facts([
 ('The dam','Ecologist <b>K. N. Ganeshaiah</b> argued that the <b>Mādhavamantri anicut</b> of 1336, still standing, changed the river’s flow and sediment, and with deforestation set off an ecological disaster'),
 ('The wind','Geologists <b>S. V. Srikantia</b> and <b>T. R. Anantharamu</b> (1997) traced the sand to a <b>point bar</b> on the river’s bend, blown north-east by the south-west monsoon winds and trapped by settlements into migrating dunes'),
 ('The earth','<b>A. B. Roy</b> and <b>M. S. Sethumadhav</b> linked the burial to <b>repeated earthquakes</b> and ground movement in the region'),
 ('What digs show','Stratigraphy suggests most of the sand came from the 17th century on: dunes advanced up to 9–10 ft a year, and some Hoysaḷa-period ground lies far below today’s surface')])
 +talk("So the curse wasn't real?","Science gives causes; faith gives meaning. Here the two tell the same story from different ends: in the 1600s the sand began to swallow the town.")))
pages.append(page('excavations','DIGGING OUT A CITY','What the sand has given back',facts([
 ('Ānandeśvara','Built by Cidānanda Svāmī, a contemporary of Hyder Ali, who is said to have crossed the flooded Kāverī on a plantain leaf'),
 ('Gaurīśaṅkara','A Kannada inscription dates it to <b>Cikka Dēvarāja Woḍeyar</b> (1672–1704)'),
 ('Pātāleśvara','A 10th-century Gaṅga core; four inscriptions on its walls, one Gaṅga-period Kannada and three Tamil'),
 ('Maraḷeśvara','Like Pātāleśvara, a Gaṅga-period sanctum and vestibule, its tower perhaps a Cōḻa renewal'),
 ('Finds','Walls, inscriptions, drainage pipes below the temple floors, and even a <b>Roman coin mould</b>'),
 ('Holding back the sand','Retaining walls and tree belts have slowed the dunes; the sand still has to be cleared for worship')])
 +'<div class="panel reading"><p><b>An archaeologist’s delight.</b> The ASI’s excavations of 1992–93 and later uncovered layer after layer of a town that was busy for more than a thousand years before the dunes came.</p></div>'))
pages.append(page('around','AROUND TALAKĀḌU','Along the river',facts([
 ('Mālaṅgi','Across the river: Jananāthapura of the Hoysaḷas, and the whirlpool of the curse'),
 ('Mudukutore','The hill of Mallikārjuna, fifth of the Pañcaliṅgas'),
 ('Vijayapura','Arkeśvara, the Lord of the Sun'),
 ('Somanāthapura','The Hoysaḷa Keśava temple of 1268, a short way upstream')])
 +'''<div class="panel reading"><p>More temples around Mysuru: <a href="/bhakti/temples-of-india/around-mysuru/nanjangud/">Nañjanagūḍu</a>, <a href="/bhakti/temples-of-india/triranga/madhya-ranga/">Madhya Raṅga</a> at Śivanasamudra downstream, and <a href="/bhakti/temples-of-india/around-mysuru/">the full series</a>.</p></div>'''))
glossary=[('Talakāḍu','“Tala and Kāḍu”, the hunter brothers'),('Daḷavana','the Sanskrit name of the town'),('Gajāraṇya','elephant forest'),('Pañcaliṅga','five liṅgas'),('Darśana','seeing the deity'),('Kuhu yoga','a rare auspicious conjunction'),('Kārtika','the autumn month sacred to Śiva'),('Vaidya','physician'),('Saikata','sandy'),('Dvārapāla','door guardian'),('Talakāḍugoṇḍa','“conqueror of Talakāḍu”'),('Anicut','a dam or weir across a river'),('Point bar','sand deposited on the inside of a river bend'),('Maraḷu','sand (Kannada)'),('Maḍu','whirlpool, deep pool (Kannada)')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','TALAKĀḌU ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The place.</b> A bend of the Kāverī where a royal city of 30+ temples lies under a mile of sand.</div>
<div><b>The liṅgas.</b> Vaidyeśvara, Pātāleśvara, Maraḷeśvara, Arkeśvara, Mallikārjuna: the five faces of Śiva, seen together at the rare Pañcaliṅga Darśana.</div>
<div><b>The history.</b> Gaṅga capital, Cōḻa Rājarājapura, Hoysaḷa victory and Kīrtinārāyaṇa (1117), Vijayanagara, then the Woḍeyars in 1610.</div>
<div><b>The curse.</b> Alamelamma’s three lines: sand for Talakāḍu, a whirlpool for Mālaṅgi, no heirs for Mysuru.</div>
<div><b>The science.</b> A dam, the monsoon wind, or the shaking earth: three explanations for the dunes.</div>
</div>'''+talk("One line to remember?","A queen's curse, a river's sand and five faces of Śiva, all waiting under the dunes for the right stars.")+'<div class="key">The city under the sand: <b>where history waits for the stars</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Town and history:</b> Wikipedia, “Talakadu”: location; 30+ temples; the dunes and their advance; Tala and Kāḍu; Daḷavana; Rāma; Harivarma; Cōḻas and Rājarājapura; Viṣṇuvardhana; seven towns and five maṭhas; Mālaṅgi; Alamelamma, 1610, and the curse; Vaidyeśvara; Kīrtinārāyaṇa; Ānandeśvara, Gaurīśaṅkara, the Pātāleśvara inscriptions; the Roman coin mould. Wikipedia, “Group of temples at Talakadu”: Gaṅga dates; Vaidyeśvara 10th–14th c.; Kīrtinārāyaṇa 1117 (Adam Hardy); Pātāleśvara and Maraḷeśvara plans. Deccan Herald (2025) and Live History India: Mādhavamantri; 10-ft dvārapālas; stratigraphy.</p>
<p><b>Pañcaliṅga:</b> indian-heritage.org (names, Manonmaṇī, Bhramarāmbā); Sanskriti Magazine (Kuhu yoga, Viśākhā, the round); The Hans India (Tatpuruṣa, Vāmadeva); Deccan Herald and Star of Mysore, 2020 (dates; next in 2033).</p>
<p><b>Science:</b> Ganeshaiah, <i>Current Science</i>; Srikantia &amp; Anantharamu, <i>J. Geol. Soc. India</i> 50(3), 1997; Roy &amp; Sethumadhav, <i>Current Science</i>.</p>
<p><b>Sources differ:</b> the Darśana’s star, moon phase and cycle; 1116 or 1117 for the Hoysaḷa victory; 1336 or about 1346 for the Mādhavamantri anicut. <b>Not verified:</b> whether a Darśana has been held since 2020. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('name','The Name'),('pancalinga','The Five Liṅgas'),('darshana','The Pañcaliṅga Darśana'),('vaidyesvara','Vaidyeśvara'),('kirtinarayana','Kīrtinārāyaṇa'),('history','History'),('curse','Alamelamma’s Curse'),('science','Why the Sand?'),('excavations','Digging Out a City'),('around','Around Talakāḍu'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">TALAKĀḌU</h1>
  <div class="series">PAÑCALIṄGA · VAIDYEŚVARA · KĪRTINĀRĀYAṆA · A REFERENCE GUIDE</div>
  <div class="tag">The temples under the sand</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>On a bend of the Kāverī, in the green heart of Karnataka, there is a desert. Under its dunes lies a royal city of more than thirty temples.</p>
    <p>This is <b>Talakāḍu</b>: capital of the Gaṅgas, prize of the Cōḻas and Hoysaḷas, home of five liṅgas of Śiva, and the place where a queen’s curse is said to have come true.</p>
    <p>This guide tells its legends, its temples, its history, and what science says about the sand.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Oṃ Namaḥ Śivāya,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A curse that came true? Spooky!","Spooky, beautiful and scientific, all at once. Hold on to your sandals, Zappy.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Talakadu.html','w').write(head+b+tail())
print('ok')
