import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
import common_t
def head_navy(title,desc):
    h=open(common_t.SRC).read(); hd=h[:h.find('<div class="book">')]
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
head=head_navy('The Temples of Mysuru Palace · Temples around Mysuru · srini.presents',
 'The temples inside the Mysuru Palace fort: Lakṣmīramaṇa (1499), Trinayaneśvara, Śvetavarāha from Śrīmuṣṇam, Kille Veṅkaṭaramaṇa and the queen’s dream, Prasanna Kṛṣṇa, Bhuvaneśvarī, Gāyatrī, and the Kōḍi shrines. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def TEMPLE(x,y,s=1,c='#f2e6c8',top='#e2cfa8'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="{c}"/><path d="M-14 -16 h28 l-4 -10 h-20z M-10 -26 h20 l-4 -10 h-12z" fill="{top}"/><circle cy="-40" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def PALACE(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-90" y="-50" width="180" height="50" fill="#f6efe0"/>'
 +''.join(f'<path d="M{a} -50 v-14 h16 v14" fill="#f6efe0"/><path d="M{a-2} -64 q10 -18 20 0z" fill="#d97b6b"/>' for a in (-86,-40,24,70))
 +'<rect x="-14" y="-90" width="28" height="40" fill="#f6efe0"/><path d="M-18 -90 q18 -34 36 0z" fill="#e0a800"/><path d="M0 -124 v-10" />'
 +''.join(f'<path d="M{a} 0 v-24 a8 8 0 0 1 16 0 v24" fill="#e2d4b4"/>' for a in (-74,-50,-26,10,34,58))+'</g>')
def DEITY(x,y,s=1,skin='#3b6fd0',robe='#ffd60a',head=None):
    h=head or f'<circle cy="-34" r="12" fill="{skin}"/><path d="M-12 -46 h24 l-4 -20 h-16z" fill="#e0a800"/>'
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-20 60 h40 l-4 -60 h-32z" fill="{robe}"/><path d="M-16 4 q16 -14 32 0 v-26 q-16 -10 -32 0z" fill="{skin}"/><path d="M-16 -14 l-16 -22 M16 -14 l16 -22" stroke="{skin}" stroke-width="7"/>'+h+'</g>')
def BOAR(x,y,s=1): return DEITY(x,y,s,'#f2f2f2','#ffd60a','<path d="M-14 -24 q-4 -26 14 -26 q18 0 14 26z" fill="#f2f2f2"/><path d="M-6 -28 q-14 2 -12 10 q8 2 14 -4z" fill="#f2f2f2"/><path d="M-14 -22 l-6 -4" stroke="#fff" stroke-width="3"/><circle cx="2" cy="-38" r="2" fill="#111"/><path d="M-10 -50 h20 l-3 -12 h-14z" fill="#e0a800"/>')
def BABY(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cx="10" cy="0" rx="26" ry="12" fill="#3b6fd0"/><circle cx="-22" cy="-10" r="13" fill="#3b6fd0"/><path d="M-30 -22 q8 -12 18 -2" fill="none" stroke="#2e9a5a" stroke-width="3"/><path d="M-32 6 l-10 10 M-12 8 l-4 12 M24 8 l6 12 M34 6 l12 8" stroke="#3b6fd0" stroke-width="7"/><circle cx="-40" cy="16" r="5" fill="#fff"/></g>'
def GODDESS(x,y,s=1,robe='#c0392b'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-24 50 q-2 -60 24 -70 q26 10 24 70z" fill="{robe}"/><circle cy="-30" r="12" fill="#f2c79b"/><path d="M-12 -40 h24 l-4 -14 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/><path d="M-20 0 l-18 -18 M20 0 l18 -18" stroke="#f2c79b" stroke-width="6"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The domes of Mysuru Palace with temple towers rising at the corners of the fort, lit up at night">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="1.6" fill="#fff"/>' for a,b in ((40,30),(90,50),(300,24),(340,60),(200,20)))
 +PALACE(190,206,1.2)+TEMPLE(40,236,1.1)+TEMPLE(340,236,1.1)+TEMPLE(80,250,.8)+TEMPLE(300,250,.8)
 +''.join(f'<circle cx="{a}" cy="{b}" r="2" fill="#ffd166"/>' for a in range(90,300,10) for b in (148,))+'<rect y="250" width="380" height="18" fill="#2b2b3a"/></svg>')
pages=[]
glance=('<table class="ct"><tr><th>Temple</th><th>Deity</th><th>Date</th></tr>'+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a,b,c in (
 ('Lakṣmīramaṇa','Viṣṇu (Nambi Nārāyaṇa) with Lakṣmī','grant of 1499'),('Trinayaneśvara','Śiva, the three-eyed','before 1578'),
 ('Śvetavarāha','Viṣṇu as the white Boar','image c. 1673–1704; temple 1809'),('Ambujavallī Mahālakṣmī','Lakṣmī','beside Śvetavarāha'),
 ('Kille Veṅkaṭaramaṇa','Viṣṇu as Veṅkaṭaramaṇa','late 18th century'),('Prasanna Kṛṣṇa','Kṛṣṇa as a crawling child','1825–1829'),
 ('Bhuvaneśvarī','The Goddess of the worlds','1951'),('Gāyatrī','Sāvitrī, Gāyatrī, Sarasvatī','1953'),
 ('Kōḍi Bhairava · Kōḍi Someśvara','Śiva as Bhairava, and as Someśvara','old shrines by the fort')))+'</table>')
pages.append(page('glance','AT A GLANCE','A dozen temples inside a palace fort',glance+'''<div class="panel reading small"><p><b>How many?</b> Sources speak of about <b>twelve</b> temples in and around the fort. Most are protected monuments of the ASI. They span <b>450 years</b>, from a grant of 1499 to the last temple of 1953.</p></div>'''
 +talk("Temples inside a palace? Isn't the palace the main show?","For tourists, yes. For the kings, the temples came first! The palace burned and was rebuilt; the gods stayed put.")))
plan=fig(560,280,'Simplified plan of the Mysuru Palace fort with the palace in the middle and temples placed around it: Lakshmiramana on the west, Shvetavaraha and Mahalakshmi at the south gate, Bhuvaneshvari on the north, Trinayaneshvara and Gayatri in the south-east, Prasanna Krishna and Kille Venkataramana nearby, and the Kodi shrines outside. Not to scale.',
 '<rect width="560" height="280" fill="#eef6e4"/><rect x="60" y="30" width="440" height="220" fill="#f6f1e2" stroke="#7a5a2a" stroke-width="5"/>'+PALACE(280,170,.9)
 +''.join(TEMPLE(x,y,.55,c,'#e2cfa8')+T(x+(a=='start' and 22 or a=='end' and -22 or 0),y+(a=='middle' and 14 or -4),n,8,'#0b2a4a',a) for x,y,c,n,a in (
  (90,140,'#dfe9f6','LAKṢMĪRAMAṆA (W)','start'),(250,244,'#dfe9f6','ŚVETAVARĀHA','end'),(310,244,'#fde4e4','MAHĀLAKṢMĪ','start'),(280,60,'#fde4e4','BHUVANEŚVARĪ (N)','middle'),
  (470,236,'#e8e8f0','TRINAYANEŚVARA (SE)','end'),(470,140,'#fde4e4','GĀYATRĪ (E)','end'),(120,230,'#dfe9f6','KILLE VEṄKAṬARAMAṆA','start'),(150,70,'#dfe9f6','PRASANNA KṚṢṆA','start')))
 +'<rect x="270" y="244" width="20" height="10" fill="#7a5a2a"/>'+T(280,272,'SOUTH (VARĀHA) GATE',9,'#555')+'<rect x="500" y="130" width="10" height="20" fill="#7a5a2a"/>'+T(540,126,'JAYA MĀRTĀṆḌA',8,'#555','end')
 +T(520,20,'positions simplified, not to scale',9,'#555','end'))
pages.append(page('map','THE FORT AND ITS TEMPLES','Where they stand',plan+'''<div class="panel reading">
<p><b>The fort.</b> The palace stands inside a walled fort with gates on each side. The temples sit along its edges, so the royal house is ringed by its gods.</p>
<p><b>Pairs.</b> The palace’s own description pairs them: <b>Bhuvaneśvarī</b> in the north faces <b>Śvetavarāha</b> in the south, and <b>Gāyatrī</b> answers <b>Trinayaneśvara</b> in the south-east.</p>
</div>'''))
pages.append(page('why','WHY A PALACE FULL OF TEMPLES?','Kings who called Kṛṣṇa their ancestor',facts([
 ('Yadu lineage','The Woḍeyars trace their descent from the <b>Yadu</b> race of <b>Kṛṣṇa</b>; one king built a Kṛṣṇa temple just for that reason'),
 ('Coronations','Royal rites were held in the palace temples: Kṛṣṇarāja Woḍeyar III was crowned with ceremonies at Lakṣmīramaṇa'),
 ('Protection','Tradition says temples were placed at the fort’s gates and corners to guard the palace'),
 ('Dasara','Mysuru Dasara has been celebrated at the palace every year since the early 19th century, ending in the Vijayadaśamī procession of the goddess Cāmuṇḍeśvarī'),
 ('Fire and rebuilding','The old wooden palace burned in <b>1897</b>; the present palace by <b>Henry Irwin</b> was finished in <b>1912</b>. The temples are older than the palace you see today')])
 +talk("So the temples are older than the palace?","Most of them! The palace is barely a hundred years old. Lakṣmīramaṇa's first record is over five hundred.")))
pages.append(page('lakshmiramana','LAKṢMĪRAMAṆA','The oldest temple in Mysuru',fig(560,170,'The Lakshmiramana temple with its tall gateway tower and Vishnu with Lakshmi inside',
 '<rect width="560" height="170" fill="#dcecff"/>'+''.join(f'<path d="M{80+i*5} {160-i*22} h{70-i*10} l-3 -22 h{-(64-i*10)}z" fill="#e2cfa8" stroke="#111"/>' for i in range(5))+T(115,166,'GOPURA (1851)',9)
 +DEITY(330,120,1.1,'#2b2b3a')+GODDESS(420,128,.8,'#e05a8a'))+tl([
 ('1499','An inscription found at Banni Maṇṭapa (Cole’s Gardens) records a grant to <b>Lakṣmīramaṇa</b>: the earliest record of a temple in the city. One account credits Cāmarāja Woḍeyar II, another Tuḷuva Narasa Nāyaka of Vijayanagara.'),
 ('c. 1599','Royal annals tell of a half-blind Brahmin cured here through <b>Rāja Woḍeyar</b>’s intercession.'),
 ('1638–59','<b>Narasarāja Woḍeyar I</b> adds the maṇḍapa.'),
 ('30 June 1799','The coronation rites of the five-year-old <b>Kṛṣṇarāja Woḍeyar III</b> are held here, after the fall of Tipu.'),
 ('1851','Kṛṣṇarāja Woḍeyar III raises the gopura over the main gate.')])
 +'<div class="panel reading small"><p><b>The Lord.</b> Viṣṇu as <b>Nambi Nārāyaṇa</b>, with Lakṣmī: “Lakṣmī’s beloved”. The temple stands in the western part of the fort.</p></div>'))
pages.append(page('trinayanesvara','TRINAYANEŚVARA','The three-eyed Lord who came inside the walls',fig(560,150,'A Shiva temple on the bank of a big tank, with the fort wall being extended around it',
 '<rect width="560" height="150" fill="#eef3fa"/><rect x="0" y="100" width="560" height="50" fill="#4aa3df"/>'+TEMPLE(200,96,1.6,'#e8e8f0')
 +'<path d="M20 60 h300 v60" stroke="#7a5a2a" stroke-width="6" fill="none" stroke-dasharray="14 6"/><path d="M320 60 h220" stroke="#7a5a2a" stroke-width="6"/>'+T(420,52,'FORT EXTENDED (1600s)',10,'#7a5a2a')+T(420,136,'DŌḌḌAKERE (DĒVARĀYA SĀGARA)',10,'#fff'))+facts([
 ('Deity','Śiva as <b>Trinayaneśvara</b>, “Lord of the three eyes”'),
 ('Age','An ancient temple that stood <b>before Rāja Woḍeyar</b>’s time (before 1578; one account says 1569)'),
 ('Outside, then inside','It once stood <b>outside</b> the fort, on the bank of the great tank Dēvarāya Sāgara (Dōḍḍakere). When <b>Kaṇṭhīrava Narasarāja</b> and <b>Doḍḍa Dēvarāja</b> enlarged the fort, it came <b>inside</b> the walls'),
 ('Where','The south-east corner of the fort'),
 ('Style','Dravidian')])
 +talk("A temple that moved without moving?","The temple stayed exactly where it was. The palace walls came to it!")))
var=fig(560,170,'A white boar-headed Vishnu image travelling from Srimushnam in Tamil Nadu to Srirangapatna and then to Mysuru, with dates',
 '<rect width="560" height="170" fill="#fff4dc"/>'+''.join(TEMPLE(x,120,1.1)+T(x,146,n,10,'#0b2a4a')+T(x,162,d,9,'#555') for x,n,d in ((80,'ŚRĪMUṢṆAM','Tamil Nadu'),(280,'ŚRĪRAṄGAPAṬṬAṆA','c. 1673–1704'),(480,'MYSURU PALACE','1809')))
 +''.join(f'<path d="M{a} 100 h110" stroke="#111" stroke-width="2"/><path d="M{a+110} 94 l10 6 l-10 6z" fill="#111"/>' for a in (130,330))+BOAR(280,60,.5))
pages.append(page('varaha1','ŚVETAVARĀHA · I','The white Boar’s journey',var+'''<div class="steps">
<div><b>From Śrīmuṣṇam.</b> King <b>Cikka Dēvarāja Woḍeyar</b> (r. 1673–1704) obtained a stone image of <b>Śvetavarāha</b>, “the white Boar”, from <b>Śrīmuṣṇam</b> in Tamil Nadu, one of Viṣṇu’s self-manifested shrines.</div>
<div><b>To the capital.</b> He installed it in a new temple at Śrīraṅgapaṭṭaṇa, then his capital. A processional image there still carries an inscription naming him as donor.</div>
<div><b>A temple lost.</b> Later accounts, including the Mysore Gazetteer, say that temple was demolished in Tipu Sultan’s time.</div>
<div><b>To Mysuru.</b> After 1799 the capital returned to Mysuru, and in <b>1809</b> the image was installed in the present temple by the south gate, built by Dīvān <b>Pūrṇayya</b> at the wish of Kṛṣṇarāja Woḍeyar III (with the guidance, one account says, of Queen Lakṣmammaṇṇi).</div>
</div>'''))
pages.append(page('varaha2','ŚVETAVARĀHA · II','A Hoysaḷa-style temple of 1809',fig(560,150,'A Hoysala-style temple with a star-shaped plinth and carved doorway, beside a smaller Mahalakshmi shrine, and a painted hall with epic murals',
 '<rect width="560" height="150" fill="#f6f1e2"/><path d="M80 140 l20 -20 h120 l20 20z" fill="#c9a26b" stroke="#111"/>'+TEMPLE(160,120,1.8,'#e8dcc0','#d9c9a0')+TEMPLE(300,124,1.1,'#fde4e4')
 +'<rect x="370" y="40" width="160" height="90" fill="#fff" stroke="#111" stroke-width="2"/>'+''.join(f'<rect x="{378+i*38}" y="50" width="30" height="34" fill="{c}" stroke="#555"/>' for i,c in enumerate(('#e8a87c','#9ac1e0','#c7e0a0','#f0d080')))+T(450,110,'EPIC MURALS',10,'#7a5a2a'))+facts([
 ('Style','Built in the <b>Hoysaḷa</b> manner: moulded basement, ornate doorframe, carved pillars in the maṇḍapa'),
 ('Stone from afar','The Gazetteer records that Pūrṇayya used materials from a ruined <b>Hoysaḷa building in Shivamogga district</b>'),
 ('Murals','The inner hall’s walls carry Mysuru-style paintings of the <b>Rāmāyaṇa</b> and <b>Mahābhārata</b>'),
 ('Teachers','Inscribed images of the Śrīvaiṣṇava ācāryas <b>Vedānta Deśika</b> and a Jīyar'),
 ('Twin shrine','Beside it stands <b>Ambujavallī Mahālakṣmī</b>, the Goddess’s own temple'),
 ('The gate','The south gate of the fort is called the <b>Varāha gate</b> after it')])
 +'<div class="panel reading small"><p><b>Sources differ.</b> The ASI dates the temple’s style to Cikka Dēvarāja’s reign; most accounts give 1809 for the present building and the installation.</p></div>'))
pages.append(page('venkataramana','KILLE VEṄKAṬARAMAṆA','The queen’s dream',fig(560,170,'A queen asleep dreaming of Venkataramana; then servants secretly carrying a covered image at night',
 '<rect width="560" height="170" fill="#141f45"/><circle cx="500" cy="36" r="16" fill="#fff8d0"/><rect x="40" y="110" width="140" height="20" fill="#7a5a2a" stroke="#111"/>'+GODDESS(110,96,.7,'#7a3fa0')
 +'<g opacity=".85">'+DEITY(210,80,.6,'#2b2b3a')+'</g><path d="M150 70 q30 -20 50 -10" stroke="#fff" stroke-dasharray="4 4" fill="none"/>'
 +''.join(person(x,160,'#555','#8a5a3a',.6) for x in (340,400))+'<rect x="350" y="100" width="44" height="30" fill="#c9a26b" stroke="#111"/>'+T(450,160,'FROM BĀḶAMURI',10,'#fff'))+'''<div class="steps">
<div><b>A dynasty in eclipse.</b> By 1760 Hyder Ali held real power in Mysuru, and under Tipu Sultan the Woḍeyar family lived in confinement.</div>
<div><b>The dream.</b> Queen <b>Lakṣmammaṇṇi</b>, wife of Kṛṣṇarāja Woḍeyar II, dreamt that Lord <b>Veṅkaṭaramaṇa</b> told her to bring his image from the temple at <b>Bāḷamuri</b> and install it at Mysuru. If she did, the family would rule again.</div>
<div><b>Secretly.</b> She had the image brought without the Sultan’s knowledge.</div>
<div><b>Restored.</b> In 1799, after Tipu’s death, the British restored the Woḍeyars to the throne. The temple of the fort, <b>Kille Veṅkaṭaramaṇa</b>, keeps the story.</div>
</div>'''+'<div class="panel reading small"><p>The same queen’s secret letters to the British are part of the Melukōṭe story in our <a href="/bhakti/temples-of-india/around-mysuru/">Tipu Sultan special</a>.</p></div>'))
pages.append(page('krishna','PRASANNA KṚṢṆA','A temple for the family’s ancestor',fig(560,150,'Baby Krishna crawling with a butter ball, in a pillared hall painted with scenes from the Bhagavata, and rows of small bronze images',
 '<rect width="560" height="150" fill="#fdf3d8"/>'+BABY(150,100,1.4)+''.join(f'<g transform="translate({300+i*24} 130)" stroke="#111" stroke-width="1.4"><rect x="-6" y="0" width="12" height="6" fill="#a0522d"/><path d="M-5 0 q5 -26 10 0z" fill="#c9a26b"/><circle cy="-24" r="4" fill="#c9a26b"/></g>' for i in range(10))+T(410,146,'BRONZES',10,'#7a5a2a'))+facts([
 ('Why','The Woḍeyars claim descent from the Yadu race of <b>Kṛṣṇa</b>. <b>Kṛṣṇarāja Woḍeyar III</b> was saddened that there was no Kṛṣṇa temple in the palace, and built one'),
 ('When','Begun in <b>1825</b>, completed in <b>1829</b>, as an inscription records'),
 ('The Lord','A charming <b>crawling child Kṛṣṇa</b>, Bāla Kṛṣṇa, in chlorite schist'),
 ('Bronzes','About <b>40</b> bronze images of gods and saints in the side shrines'),
 ('Murals','The pillared hall is painted with scenes from the <b>Bhāgavata Purāṇa</b>, in the 19th-century Mysuru style'),
 ('Festival','Janmāṣṭamī, Kṛṣṇa’s birthday, is celebrated here every year')])
 +talk("A king built a temple to his great-great-great... grandfather?","Many greats! If your family line goes back to Kṛṣṇa, you'd want a temple for him at home too.")))
pages.append(page('bhuvanesvari','BHUVANEŚVARĪ','A temple of 1951',fig(560,170,'The Goddess Bhuvaneshvari seated in her shrine, and a large copper sun disc with a chariot of seven horses',
 '<rect width="560" height="170" fill="#fde4e4"/>'+GODDESS(180,120,1.4,'#c0392b')+'<circle cx="400" cy="80" r="60" fill="#d98b4b" stroke="#111" stroke-width="2"/><circle cx="400" cy="80" r="44" fill="#e8a060" stroke="#111"/>'
 +''.join(f'<path d="M{370+i*9} 96 l4 -10 l4 10" stroke="#5a3a1a" stroke-width="2" fill="none"/>' for i in range(7))+'<circle cx="400" cy="66" r="10" fill="#ffd166" stroke="#111"/>'+T(400,160,'COPPER SŪRYA MAṆḌALA',10,'#7a1d12'))+facts([
 ('Built','<b>1951</b>, by <b>Jayacāmarājendra Woḍeyar</b>, the last ruling Maharaja, soon after Mysuru joined the Indian Republic'),
 ('Where','The northern side of the fort, near the Balarāma gate, facing Śvetavarāha in the south'),
 ('The Goddess','<b>Bhuvaneśvarī</b>, “Queen of the worlds”, carved by the sculptor <b>Siddaliṅga</b> (Siddalingaswamy)'),
 ('Treasure','A great copper <b>Sūrya Maṇḍala</b>, the Sun on his chariot, moved here from the palace and used at <b>Ratha Saptamī</b>')])
 +'<div class="panel reading small"><p><b>A scholar-king.</b> Jayacāmarājendra Woḍeyar was a devoted Śākta, a philosopher and a patron of music; both of the palace’s newest temples are to the Goddess.</p></div>'))
pages.append(page('gayatri','GĀYATRĪ','The youngest temple',fig(560,150,'Three small shrines side by side for Savitri, Gayatri and Sarasvati',
 '<rect width="560" height="150" fill="#fdf3f3"/>'+''.join(TEMPLE(x,130,1.4,'#fde4e4')+GODDESS(x,100,.45,c)+T(x,146,n,10,'#7a1d12') for x,n,c in ((160,'SĀVITRĪ','#e0a800'),(280,'GĀYATRĪ','#c0392b'),(400,'SARASVATĪ','#f2f2f2'))))+facts([
 ('Built','<b>1953</b>, by Jayacāmarājendra Woḍeyar: the youngest temple of the palace'),
 ('Where','The east of the fort, beside the <b>Jaya Mārtāṇḍa</b> gate'),
 ('Three shrines','The inner sanctum holds three: <b>Sāvitrī</b>, <b>Gāyatrī</b> and <b>Sarasvatī</b>'),
 ('Gāyatrī','The goddess of the Gāyatrī mantra, the most sacred verse of the Vedas')])
 +'<div class="panel reading small"><p>Read our article on the <a href="/bhakti/devi/gayatri-mantra/">Gāyatrī Mantra</a>.</p></div>'
 +talk("Why a temple to a mantra?","Because Gāyatrī is both: the most sacred verse, and the Goddess who is that verse. A royal thank-you to the Veda itself.")))
pages.append(page('kodi','THE KŌḌI SHRINES','Bhairava and Someśvara by the old tank',facts([
 ('Kōḍi Bhairava','A temple of Śiva as <b>Bhairava</b>, the fierce guardian; its name, the palace says, comes from where it stood'),
 ('Kōḍi Someśvara','Śiva as <b>Someśvara</b>, Lord of the Moon'),
 ('Kōḍi','In Kannada, <i>kōḍi</i> is the outlet where a tank overflows; the name probably recalls a site by the overflow of an old tank'),
 ('Guardians','Bhairava temples traditionally guard towns and forts')])
 +'''<div class="panel reading"><p><b>The older city.</b> If the name is read this way, these small shrines recall a Mysuru of tanks and fields before the grand avenues: when Dōḍḍakere still lapped the fort, and Trinayaneśvara stood outside the walls.</p></div>'''))
pages.append(page('timeline','TIMELINE','450 years of palace temples',tl([
 ('1499','Grant to Lakṣmīramaṇa: the oldest record.'),
 ('before 1578','Trinayaneśvara stands outside the fort.'),
 ('1638–1673','Narasarāja I adds Lakṣmīramaṇa’s maṇḍapa; the fort is enlarged and Trinayaneśvara comes inside.'),
 ('1673–1704','Cikka Dēvarāja brings Śvetavarāha from Śrīmuṣṇam to Śrīraṅgapaṭṭaṇa.'),
 ('1760–1799','Hyder Ali and Tipu Sultan; Queen Lakṣmammaṇṇi brings Veṅkaṭaramaṇa from Bāḷamuri.'),
 ('1799','Kṛṣṇarāja Woḍeyar III crowned with rites at Lakṣmīramaṇa.'),
 ('1809','Śvetavarāha installed at the south gate.'),
 ('1825–29','Prasanna Kṛṣṇa built.'),
 ('1851','Lakṣmīramaṇa’s gopura.'),
 ('1897–1912','The old palace burns; the new palace rises.'),
 ('1951 · 1953','Bhuvaneśvarī and Gāyatrī.')])))
glossary=[('Kille','fort (Kannada, from Persian <i>qila</i>)'),('Lakṣmīramaṇa','“Lakṣmī’s beloved”, Viṣṇu'),('Trinayana','three-eyed, Śiva'),('Śveta','white'),('Varāha','Viṣṇu’s boar avatar'),('Prasanna','gracious, pleased'),('Bhuvaneśvarī','Queen of the worlds'),('Sūrya Maṇḍala','an image of the Sun’s disc'),('Ratha Saptamī','the Sun’s festival in Māgha'),('Kōḍi','the overflow of a tank'),('Bhairava','Śiva’s fierce guardian form'),('Dīvān','chief minister'),('Yadu','the clan of Kṛṣṇa')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','THE PALACE TEMPLES ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The oldest.</b> Lakṣmīramaṇa (grant of 1499), where Kṛṣṇarāja III was crowned; Trinayaneśvara, older than the walls around it.</div>
<div><b>The travellers.</b> Śvetavarāha from Śrīmuṣṇam via Śrīraṅgapaṭṭaṇa (1809); Veṅkaṭaramaṇa from Bāḷamuri, brought in secret by a queen.</div>
<div><b>The family god.</b> Prasanna Kṛṣṇa (1829), for the kings of the Yadu line.</div>
<div><b>The Goddesses.</b> Bhuvaneśvarī (1951) and Gāyatrī (1953), the last temples of the last Maharaja.</div>
<div><b>The guardians.</b> The Kōḍi shrines of Bhairava and Someśvara.</div>
</div>'''+talk("One line to remember?","The palace you photograph is a hundred years old. The temples around it carry five hundred years of the family's faith.")+'<div class="key">Behind the palace lights: <b>a royal family’s temples</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Official:</b> Mysuru Palace Board, “Temples inside Mysuru Palace Fort”: Kōḍi Bhairava; Lakṣmīramaṇa (1499 grant; c. 1599 cure; 30 June 1799); Śvetavarāha (Hoysaḷa style); Trinayaneśvara (Dēvarāya Sāgara; Kaṇṭhīrava and Doḍḍa Dēvarāja; south-east); Prasanna Kṛṣṇa (Yadu descent; 1825–1829); Kille Veṅkaṭaramaṇa (Lakṣmammaṇṇi; Bāḷamuri); Bhuvaneśvarī (1951; Sūrya Maṇḍala); Gāyatrī (1953; three shrines).</p>
<p><b>Other:</b> Wikipedia, “Group of temples at the Amba Vilas Palace” (Cāmarāja II and Narasa Nāyaka; Narasarāja I’s maṇḍapa; 1851 gopura; ASI dating; Pūrṇayya and Shivamogga; 1569 or pre-1578; 40 bronzes; Hyder and Tipu context). Wikipedia, “Mysore Palace” (Nambi Nārāyaṇa; 1809; Bhāgavata murals; Siddaliṅga; Ratha Saptamī; palace dates; Dasara). Star of Mysore (Mysore Gazetteer on Śrīmuṣṇam, Tipu-era demolition, 1809, Ambujavallī); mysore.org.uk (Deśika and Jīyar images); vayusutha.in (Lakṣmammaṇṇi and Pūrṇayya).</p>
<p><b>Not verified:</b> the exact count of temples; the meaning of Kōḍi as applied to these shrines; the age of the Kōḍi shrines. Plans are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('map','The Fort and Its Temples'),('why','Why a Palace Full of Temples?'),('lakshmiramana','Lakṣmīramaṇa'),('trinayanesvara','Trinayaneśvara'),('varaha1','Śvetavarāha · The Journey'),('varaha2','Śvetavarāha · The Temple'),('venkataramana','Kille Veṅkaṭaramaṇa'),('krishna','Prasanna Kṛṣṇa'),('bhuvanesvari','Bhuvaneśvarī'),('gayatri','Gāyatrī'),('kodi','The Kōḍi Shrines'),('timeline','Timeline'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,6vw,66px)">THE PALACE TEMPLES</h1>
  <div class="series">INSIDE THE MYSURU PALACE FORT · A REFERENCE GUIDE</div>
  <div class="tag">Five centuries of a royal family’s gods</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Millions come to Mysuru to see the palace lit up at night. Few notice the temples around it: a dozen shrines tucked along the fort walls, some older than the palace by four hundred years.</p>
    <p>Here a five-year-old king was crowned, a white Boar arrived from Tamil Nadu, a captive queen smuggled in a god, and the last Maharaja built two temples to the Goddess.</p>
    <p>This guide walks you round the fort, temple by temple.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Oṃ Namaḥ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Twelve temples inside one palace?","Twelve stories in one fort. Let's walk the walls, Zappy.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Palace_Temples.html','w').write(head+b+tail())
print('ok')
