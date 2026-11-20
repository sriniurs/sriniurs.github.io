import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
import common_t
def head_navy(title,desc):
    h=open(common_t.SRC).read(); hd=h[:h.find('<div class="book">')]
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
head=head_navy('Nañjanagūḍu · Śrīkaṇṭheśvara · Temples around Mysuru · srini.presents',
 'Śrīkaṇṭheśvara (Nañjuṇḍeśvara) temple at Nañjanagūḍu: the Lord who drank the poison, Dakṣiṇa Kāśī on the Kapilā, Gautama and Paraśurāma, Hakīm Nañjuṇḍa, the Pañca Mahā Rathotsava. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def LINGA(x,y,s=1,blood=False):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-46 0 h92 l-8 -14 h-76z" fill="#8a8a8a"/><path d="M34 -7 h26 l-4 6 h-22z" fill="#8a8a8a"/>'
     '<path d="M-18 -14 v-38 a18 18 0 0 1 36 0 v38z" fill="#3a3a3a"/><path d="M-12 -46 h24 M-12 -40 h24 M-12 -34 h24" stroke="#fff" stroke-width="2.4"/>'
     '<circle cx="0" cy="-30" r="3" fill="#c0392b" stroke="none"/>'+('<path d="M6 -22 q4 6 2 12" stroke="#c0392b" stroke-width="4" fill="none"/>' if blood else '')+'</g>')
def SHIVA(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-30 60 q30 -70 60 0z" fill="#ffb3c7"/><circle r="22" cy="-6" fill="#8fd0f5"/>'
     '<path d="M-14 -28 q14 -22 28 0 q-6 -6 -14 -4 q-8 -2 -14 4z" fill="#5a3a1a"/><path d="M-6 -36 q6 -6 12 0" fill="none" stroke="#fff" stroke-width="3"/>'
     '<path d="M-10 -4 q4 3 8 0 M2 -4 q4 3 8 0" fill="none"/><path d="M-6 8 q6 4 12 0" fill="none"/>'
     '<path d="M-12 18 q12 8 24 0" stroke="#1d4f9a" stroke-width="7" fill="none"/></g>')
GOP=lambda x,y,s=1,t=7: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-34+k*3} {-k*12} h{68-k*6} l-1 -12 h{-(66-k*6)}z" fill="{"#f2e6c8" if k%2 else "#e2cfa8"}"/>' for k in range(t))+''.join(f'<path d="M{-14+j*7} {-t*12} l2 -10 l2 10z" fill="#e0a800"/>' for j in range(5))+'<rect x="-9" y="-20" width="18" height="20" fill="#5a3a1a"/></g>'
def RATHA(x,y,s=1,c='#c0392b'):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cx="-18" cy="-6" r="8" fill="#7a5a2a"/><circle cx="18" cy="-6" r="8" fill="#7a5a2a"/>'
     '<rect x="-26" y="-30" width="52" height="18" fill="#a0522d"/><path d="M-22 -30 v-24 M22 -30 v-24" stroke-width="3"/>'
     f'<path d="M-30 -54 h60 l-30 -46z" fill="{c}"/><path d="M-26 -54 q26 10 52 0" fill="none" stroke="#ffd60a" stroke-width="3"/><circle cy="-102" r="4" fill="#e0a800"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Shiva with a blue throat above the tall gopuram of Nanjangud on the bank of the Kapila river">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/><circle cx="66" cy="54" r="20" fill="#ffd166"/>'
 '<path d="M0 222 q190 -20 380 0 V268 H0z" fill="#4aa3df"/>'+GOP(250,226,1.55)+SHIVA(100,140,1.5)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','Śiva as <b>Śrīkaṇṭheśvara</b> (“Lord with the blessed throat”) or <b>Nañjuṇḍeśvara</b> (“Lord who drank the poison”), as a <b>liṅga</b>'),
 ('Goddess','<b>Pārvatī</b>, in her own shrine'),
 ('Place','<b>Nañjanagūḍu</b> (Nanjangud), Mysuru district, Karnataka'),
 ('River','The right bank of the <b>Kapilā</b> (Kabini), a tributary of the Kāverī'),
 ('Titles','<b>Dakṣiṇa Kāśī</b>, “Kāśī of the South”; in the Śiva Purāṇa, <b>Garalapurī</b>, “the town of poison”'),
 ('Sages','<b>Gautama</b> installed the liṅga; <b>Paraśurāma</b> was freed of his sin here'),
 ('Healer','<b>Hakīm Nañjuṇḍa</b>, “Nañjuṇḍa the physician”, a name from Tipu Sultan'),
 ('Builders','Gaṅgas, Cōḻas, Hoysaḷas, Vijayanagara, Woḍeyars of Mysuru'),
 ('Size','About <b>385 × 160 ft</b>: among the largest temples in Karnataka'),
 ('Gopuram','About <b>120 ft</b>, built in <b>1845</b>, crowned by seven gilded kalaśas'),
 ('Great festival','<b>Dodda Jātre</b>, the <b>Pañca Mahā Rathotsava</b>: five chariots drawn on one morning')])
 +talk("A god named after poison?","Named after drinking it! He swallowed the world's poison so nobody else had to. That's the whole story of this temple.")))
mapfig=fig(560,250,'Schematic map: the Kapila river flowing past Nanjangud town and temple, with the Kaundinya (Gundlu) river joining it at the sangama called Parashurama Kshetra, and Mysuru to the north. Not to scale.',
 '<rect width="560" height="250" fill="#eef6e4"/><path d="M0 150 C 140 120, 260 190, 400 150 S 540 110, 560 120" fill="none" stroke="#4aa3df" stroke-width="22"/>'
 '<path d="M330 250 C 340 210, 360 190, 380 160" fill="none" stroke="#4aa3df" stroke-width="12"/>'
 +'<rect x="190" y="88" width="56" height="40" fill="#f2e6c8" stroke="#111" stroke-width="2"/>'+GOP(218,92,.28)+T(218,80,'ŚRĪKAṆṬHEŚVARA',11,'#0b2a4a')
 +'<circle cx="380" cy="156" r="9" fill="#e0a800" stroke="#111"/>'+T(380,190,'PARAŚURĀMA KṢETRA',10,'#0b2a4a','start')
 +T(100,118,'KAPILĀ (KABINI)',12,'#1d4f9a')+T(300,238,'KAUṆḌINYA (GUNDLU)',10,'#1d4f9a','end')
 +'<path d="M218 40 v-24" stroke="#111" stroke-width="2"/><path d="M212 22 l6 -10 l6 10z" fill="#111"/>'+T(248,26,'to MYSURU (north)',10,'#555','start')+T(470,236,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','On the Kapilā, south of Mysuru',mapfig+'''<div class="panel reading">
<p><b>The river.</b> The temple stands on the right bank of the <b>Kapilā</b>, better known as the Kabini, one of the Kāverī’s great tributaries. Pilgrims bathe at its ghāṭ before darśan.</p>
<p><b>The confluence.</b> Near the town the Kapilā is joined by the <b>Kauṇḍinya</b>, also called the Gundlu. The meeting place is the <b>saṅgama</b>, known as <b>Paraśurāma Kṣetra</b>.</p>
<p><b>Why “Kāśī of the South”.</b> As at Kāśī, a great Śiva shrine stands beside a sacred river and a confluence, and a bath and a darśan here are held to wash away sin.</p>
</div>'''))
poison=fig(560,220,'Gods and demons churning the ocean with Mount Mandara and the serpent Vasuki; dark poison rises, and Shiva drinks it, his throat turning blue while Parvati holds it there',
 '<rect width="560" height="220" fill="#dcecff"/><path d="M0 170 q70 -14 140 0 t140 0 t140 0 t140 0 V220 H0z" fill="#4aa3df"/>'
 '<path d="M90 172 l30 -110 l30 110z" fill="#8a7a6a" stroke="#111" stroke-width="2"/><path d="M40 120 q80 -16 160 0" stroke="#3a7a3a" stroke-width="8" fill="none"/>'
 +person(38,170,'#3a3a3a','#6b4a3a',.7)+person(206,170,'#ffd60a','#f2c79b',.7)
 +'<path d="M150 120 q40 -40 140 -60" stroke="#222" stroke-width="10" fill="none" opacity=".75"/>'+SHIVA(360,110,1.6)+'<g transform="translate(470 150)" stroke="#111" stroke-width="2"><circle cy="-30" r="14" fill="#f2c79b"/><path d="M-20 40 q20 -70 40 0z" fill="#c0392b"/><path d="M-14 -10 l-40 -6" stroke="#f2c79b" stroke-width="6"/></g>'
 +T(120,210,'THE CHURNING',12,'#0b2a4a')+T(360,210,'NAÑJUṆḌEŚVARA',12,'#0b2a4a')+T(470,210,'PĀRVATĪ',11,'#c0392b'))
pages.append(page('lord','THE LORD WHO DRANK THE POISON','Nañjuṇḍeśvara and Śrīkaṇṭheśvara',poison+'''<div class="steps">
<div><b>The churning.</b> Gods and demons churned the Ocean of Milk for the nectar of immortality, using Mount Mandara as the churning rod and the serpent Vāsuki as the rope.</div>
<div><b>The poison.</b> Before any treasure came up, a deadly poison, <b>hālāhala</b>, rose from the ocean and began to burn the worlds.</div>
<div><b>Śiva drinks it.</b> At the gods’ plea, Śiva swallowed it. Pārvatī pressed his throat so it went no further, and his throat turned blue: he became <b>Nīlakaṇṭha</b>.</div>
<div><b>The names.</b> In Kannada <i>nañju</i> is poison: <b>Nañjuṇḍa</b> is “the one who ate the poison”. In Sanskrit he is <b>Śrīkaṇṭha</b>, “the one with the blessed throat”, and the town is <b>Nañjanagūḍu</b>, “the abode of Nañjuṇḍa”.</div>
</div>'''+talk("Why is the throat 'blessed' if it's full of poison?","Because it saved the world! The mark of poison is the mark of his compassion. That's why devotees call it śrī, auspicious.")))
leg1=fig(560,190,'Sage Gautama installing a linga by the river; Shiva striking down the demon Keshi',
 '<rect width="560" height="190" fill="#fff4dc"/><path d="M0 160 q140 -16 280 0 V190 H0z" fill="#4aa3df"/>'+LINGA(170,150,1.2)+person(80,150,'#ff8c1a','#c98b5a',.9)+'<path d="M64 86 q16 -20 32 0" fill="#fff" stroke="#111"/>'
 +SHIVA(400,90,1.1)+'<path d="M424 100 l40 30" stroke="#111" stroke-width="4"/><path d="M458 118 l10 -18 l8 20z" fill="#bbb" stroke="#111"/>'+'<g transform="translate(500 156)" stroke="#111" stroke-width="2"><circle cy="-30" r="14" fill="#5a7a3a"/><path d="M-10 -42 l-4 -10 M10 -42 l4 -10"/><path d="M-22 26 q22 -60 44 0z" fill="#3a3a3a"/></g>'
 +T(130,184,'GAUTAMA',12,'#0b2a4a')+T(450,184,'KEŚĪ',12,'#c0392b'))
pages.append(page('legends1','THE LEGENDS · I','Gautama, and the demon Keśī',leg1+'''<div class="steps">
<div><b>Gautama’s liṅga.</b> Local tradition holds that the sage <b>Gautama</b> lived here for a time and installed the liṅga. His name lives on in the temple’s greatest chariot, the <b>Gautama Ratha</b>.</div>
<div><b>Garalapurī.</b> The Śiva Purāṇa calls the place <b>Garalapurī</b>, from <i>garala</i>, poison, the same idea as Nañjuṇḍa.</div>
<div><b>The demon Keśī.</b> A demon named <b>Keśī</b>, proud of boons from Brahmā and Viṣṇu, tormented the sages. At their prayer Śiva appeared and destroyed him.</div>
<div><b>A promise.</b> Śiva declared that a part of himself would remain here forever, making Garalapurī a place where sins are removed.</div>
</div>'''+talk("Same name as Kṛṣṇa's horse-demon Keśī?","Same name, different demon. Purāṇas recycle names a lot: always check which story you're in!")))
leg2=fig(560,190,'Parashurama clearing bushes with his axe; the axe strikes a hidden linga which bleeds; he presses wet mud from the riverbank onto it',
 '<rect width="560" height="190" fill="#e8f5e2"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="18" fill="#5a9a4a" stroke="#111"/>' for x,y in [(60,140),(96,130),(130,146)])
 +person(200,160,'#ff8c1a','#c98b5a',1)+'<path d="M214 100 l40 -30" stroke="#7a5a2a" stroke-width="5"/><path d="M246 64 q20 -6 20 14 q-12 -2 -20 -14z" fill="#bbb" stroke="#111" stroke-width="2"/>'
 +LINGA(330,160,1.3,True)+'<path d="M450 160 q20 -30 60 -10" fill="#7a5a2a" stroke="#111" stroke-width="2"/>'+T(480,130,'wet mud',11,'#5a3a1a')
 +T(200,184,'PARAŚURĀMA',12,'#0b2a4a')+T(330,184,'THE BLEEDING LIṄGA',11,'#c0392b'))
pages.append(page('legends2','THE LEGENDS · II','Paraśurāma, and Pārvatī’s jewel',leg2+'''<div class="steps">
<div><b>A heavy sin.</b> At his father Jamadagni’s command, <b>Paraśurāma</b> struck down his own mother, Reṇukā (in the story she is later restored to life). The sin of it stayed with him.</div>
<div><b>To Garalapurī.</b> On Nārada’s advice he came here. While clearing the bushes, his axe struck a hidden liṅga, and it <b>bled</b>.</div>
<div><b>The mud.</b> Śiva told him to press wet mud from the spot onto the wound, and the bleeding stopped. Paraśurāma was freed of his sin, and his own shrine stands at the saṅgama.</div>
<div><b>Pārvatī’s jewel.</b> Another legend tells that a jewel from Pārvatī’s crown fell into the Kabini. Śiva declared that she too would be present here, and the bathing place became the <b>Dakṣiṇa Maṇikarṇikā</b> ghāṭ, “the southern Maṇikarṇikā”, after Kāśī’s holiest ghāṭ.</div>
</div>'''))
hak=fig(560,190,'A royal elephant with a bandaged eye being bathed in the river by priests; later the elephant with bright eyes, and a green linga with an emerald necklace offered at the temple',
 '<rect width="560" height="190" fill="#fdf3e0"/><path d="M0 150 q140 -14 280 0 V190 H0z" fill="#4aa3df"/>'
 '<g transform="translate(140 140)" stroke="#111" stroke-width="2"><ellipse cx="0" cy="-40" rx="56" ry="36" fill="#9a9aa8"/><circle cx="-50" cy="-56" r="22" fill="#9a9aa8"/><path d="M-66 -46 q-10 30 4 50" fill="none" stroke="#9a9aa8" stroke-width="10"/><path d="M-60 -64 l16 0" stroke="#fff" stroke-width="6"/><rect x="-30" y="-10" width="12" height="20" fill="#9a9aa8"/><rect x="20" y="-10" width="12" height="20" fill="#9a9aa8"/><path d="M-20 -76 h40 v-10 h-40z" fill="#c0392b"/></g>'
 +T(140,184,'48 DAYS',13,'#0b2a4a')+'<path d="M260 100 h60" stroke="#111" stroke-width="3"/><path d="M320 94 l12 6 l-12 6z" fill="#111"/>'
 +'<g transform="translate(440 160)" stroke="#111" stroke-width="2"><path d="M-46 0 h92 l-8 -14 h-76z" fill="#8a8a8a"/><path d="M-18 -14 v-38 a18 18 0 0 1 36 0 v38z" fill="#2e9a5a"/><path d="M-30 -30 q30 34 60 0" fill="none" stroke="#e0a800" stroke-width="4"/>'+''.join(f'<circle cx="{-24+i*12}" cy="{-22+abs(i-2)*-3}" r="3" fill="#0a7a3a"/>' for i in range(5))+'</g>'+T(440,184,'THE EMERALD LIṄGA',11,'#0a7a3a'))
pages.append(page('hakim','HAKĪM NAÑJUṆḌA','The physician of Nañjanagūḍu',hak+'''<div class="steps">
<div><b>A sick elephant.</b> Temple tradition tells that the royal elephant of <b>Tipu Sultan</b> developed a disease of the eyes. On the priests’ advice it was bathed in the Kapilā and its eyes washed with the Lord’s abhiṣeka water for one <b>maṇḍala</b> of 48 days.</div>
<div><b>Sight restored.</b> On the 48th day the elephant could see again.</div>
<div><b>The gifts.</b> Tipu offered a green <b>marakata</b> (emerald, also described as jade) liṅga with a <b>makara-kaṇṭhi</b> necklace, which is still brought out once a year, at the <b>Girijākalyāṇa</b> festival.</div>
<div><b>The name.</b> He called the Lord <b>Hakīm Nañjuṇḍa</b>, “Nañjuṇḍa the physician”. The Mysore Gazetteer tells a similar story of his father, <b>Hyder Ali</b>.</div>
</div>'''+talk("So the Lord is a doctor too?","Devotees call him Vaidya Nañjuṇḍeśvara, the healer. People still come here praying for cures, and the old name from a Sultan's court says the same.")))
pages.append(page('history','HISTORY','A thousand years of builders',tl([
 ('9th–10th c.','The temple’s origins are traced to the <b>Western Gaṅgas</b>.'),
 ('c. 11th c.','The <b>garbhagṛha</b>, the sanctum, dates to the Cōḻa period.'),
 ('c. 13th c.','The hall in front of the sanctum, where devotees sit, is <b>Hoysaḷa</b> work.'),
 ('1517','A Kannada inscription linked to the father-in-law of <b>Kṛṣṇadevarāya</b> of Vijayanagara.'),
 ('Vijayanagara','A brick-and-mortar śikhara over the shrine; the <b>Pārvatī</b> and <b>Nārāyaṇa</b> shrines are added.'),
 ('1644','<b>Daḷavāyi Vikramarāya</b> installs the great stone <b>Nandi</b>, about 8 ft tall.'),
 ('18th c.','Hyder Ali and Tipu Sultan; the healing of the elephant and the emerald liṅga.'),
 ('1845','<b>Devājammaṇṇi</b>, queen of <b>Kṛṣṇarāja Woḍeyar III</b>, builds the great gopuram.')])
 +'<div class="panel reading"><p><b>Royal temple.</b> The Woḍeyars of Mysuru built the gopuram and several maṇḍapas and made many grants. A stone sculpture of Kṛṣṇarāja Woḍeyar III with his four queens stands inside the temple.</p></div>'))
plan=fig(560,250,'Simplified plan: the long rectangular temple with the gopuram on the east, the great Nandi, the Shiva sanctum, and the Parvati and Narayana shrines, inside an outer wall lined with niches',
 '<rect width="560" height="250" fill="#f6f1e2"/><rect x="30" y="40" width="500" height="180" fill="none" stroke="#7a5a2a" stroke-width="4"/>'
 +''.join(f'<rect x="{40+i*24}" y="46" width="10" height="10" fill="#d9c9a0" stroke="#7a5a2a"/><rect x="{40+i*24}" y="204" width="10" height="10" fill="#d9c9a0" stroke="#7a5a2a"/>' for i in range(21))
 +'<rect x="500" y="110" width="40" height="40" fill="#e2cfa8" stroke="#111" stroke-width="2"/>'+T(520,170,'GOPURAM',9)
 +'<ellipse cx="430" cy="130" rx="16" ry="10" fill="#bbb" stroke="#111"/>'+T(430,108,'NANDI',9)
 +'<rect x="200" y="100" width="140" height="60" fill="#fff" stroke="#111"/>'+T(270,96,'MAṆḌAPA',9)+'<rect x="120" y="110" width="50" height="40" fill="#0b2a4a" stroke="#111"/>'+T(145,170,'SANCTUM',9,'#0b2a4a')
 +'<rect x="100" y="64" width="50" height="28" fill="#fdecea" stroke="#111"/>'+T(125,82,'PĀRVATĪ',8,'#c0392b')+'<rect x="100" y="168" width="50" height="28" fill="#dfe9f6" stroke="#111"/>'+T(125,186,'NĀRĀYAṆA',8,'#1d6fb8')
 +T(280,32,'about 385 × 160 ft · simplified, not to scale',10,'#555')+T(280,240,'niches along the wall: 122 forms of Śiva',10,'#7a5a2a'))
pages.append(page('temple','THE TEMPLE','Plan and gopuram',plan+'''<div class="g2">
<div class="card bg-yellow"><h4>🏯 The gopuram</h4><p>About <b>120 ft</b> tall, raised in <b>1845</b> by Queen Devājammaṇṇi. Sources give it <b>seven</b> or <b>nine</b> tiers. It is crowned by <b>seven</b> gold-plated kalaśas, each about 3 m tall.</p></div>
<div class="card bg-blue"><h4>📐 The size</h4><p>About <b>385 × 160 ft</b>, some 50,000 sq ft: one of the largest temple complexes in Karnataka, with pillared maṇḍapas and yāḷi pillars at the main door.</p></div>
</div>'''))
pages.append(page('inside','INSIDE THE TEMPLE','Shrines, images and treasures',facts([
 ('Śrīkaṇṭheśvara','The liṅga in the Cōḻa-period sanctum'),
 ('Pārvatī','The Goddess’s shrine, added under Vijayanagara'),
 ('Nārāyaṇa','A Viṣṇu shrine in the same temple, also of the Vijayanagara period'),
 ('Nandi','The great stone bull of 1644, about 8 ft tall'),
 ('122 forms of Śiva','Images in niches along the outer enclosure, with Gaṇapati and the Saptamātṛkās'),
 ('65 liṅgas','Liṅgas of many sizes installed through the temple'),
 ('Vīrabhadra','A shrine of Śiva’s fierce form'),
 ('Royal sculpture','Kṛṣṇarāja Woḍeyar III with his four queens'),
 ('Vāhanas','The processional mounts on which the deities ride out at festivals')])
 +talk("Sixty-five liṅgas in one temple?","Kings, queens and devotees kept adding them over centuries. Walk the corridors and you're walking through a thousand years of offerings.")))
fest=fig(560,200,'Five temple chariots drawn in a row by crowds, the tallest Gautama Ratha in the middle',
 '<rect width="560" height="200" fill="#ffe9c4"/>'+RATHA(70,184,.9,'#e0a800')+RATHA(170,184,1.0,'#3b6fd0')+RATHA(280,184,1.55,'#c0392b')+RATHA(390,184,1.0,'#2e9a5a')+RATHA(490,184,1.1,'#e05a8a')
 +T(70,30,'GAṆAPATI',9)+T(170,30,'CAṆḌIKEŚVARA',9)+T(280,22,'GAUTAMA RATHA',11,'#c0392b')+T(390,30,'SUBRAHMAṆYA',9)+T(490,30,'PĀRVATĪ',9))
pages.append(page('rathotsava','THE FIVE CHARIOTS','Dodda Jātre: the Pañca Mahā Rathotsava',fest+'''<div class="panel reading">
<p><b>The big fair.</b> <b>Dodda Jātre</b>, “the great fair”, is the temple’s annual festival in spring (March–April). Its high point is the <b>Pañca Mahā Rathotsava</b>: <b>five</b> chariots drawn through the chariot streets on the same morning.</p>
<p><b>The five.</b> Chariots of <b>Gaṇapati</b>, <b>Caṇḍikeśvara</b>, <b>Subrahmaṇya</b> and <b>Pārvatī</b>, and the great <b>Gautama Ratha</b>, which carries Śrīkaṇṭheśvara.</p>
<p><b>The giant.</b> The Gautama Ratha rises nearly as high as the gopuram: reports put it at about <b>90 to 100 ft</b> and well over a hundred tonnes. It moves only because thousands pull together.</p>
<p><b>Only one.</b> It is described as the only festival in South India where five great chariots are drawn at once.</p>
</div>'''))
pages.append(page('festivals','THROUGH THE YEAR','Festivals of Nañjanagūḍu',facts([
 ('Dodda Jātre (Mar–Apr)','The great fair and the five-chariot festival'),
 ('Chikka Jātre','The “small fair”, a second car festival in the year'),
 ('Teppotsava','The Lord floated on the Kapilā on a decorated raft, during the fairs'),
 ('Girijākalyāṇa','The wedding of Śiva and Pārvatī; Tipu’s emerald liṅga and necklace are displayed'),
 ('Mahāśivarātri','Devotees bathe in the Kapilā at daybreak before darśan'),
 ('Kārtika','<b>Lakṣadīpotsava</b>, a hundred thousand lamps'),
 ('Every full moon','A chariot procession for Śrīkaṇṭheśvara')])
 +talk("Why name the biggest chariot after Gautama and not Śiva?","Because Gautama brought Śiva here! The chariot carries the Lord, but it remembers the sage who installed him.")))
pages.append(page('around','AROUND NAÑJANAGŪḌU','The confluence and nearby shrines',facts([
 ('Paraśurāma Kṣetra','The saṅgama of the Kapilā and Kauṇḍinya (Gundlu), with a shrine of <b>Paraśurāma</b> where he is said to have been freed of his sin'),
 ('Snāna ghāṭ','The bathing ghāṭ on the Kapilā below the temple'),
 ('Hemmaragāla','A Kṛṣṇa temple linked with the sage <b>Kauṇḍinya</b>, with the image of Gopāla playing the flute in the three-bend pose'),
 ('In the town','Shrines of Māruti and Basaveśvara near the saṅgama, a Rāghavendra Svāmī maṭha, and a large statue of Śiva near the temple')])
 +'''<div class="panel reading"><p><b>Hari and Hara.</b> As at the Raṅga temples upstream, Śiva and Viṣṇu sit side by side: a Nārāyaṇa shrine inside Śrīkaṇṭheśvara’s temple, and a Gopāla temple of the sage Kauṇḍinya nearby.</p>
<p>More temples around Mysuru: <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga</a> at Śrīraṅgapaṭṇa and <a href="/bhakti/temples-of-india/triranga/madhya-ranga/">Madhya Raṅga</a> at Śivanasamudra.</p></div>'''))
glossary=[('Nañjuṇḍeśvara','“the Lord who ate the poison” (Kannada <i>nañju</i>, poison)'),('Śrīkaṇṭheśvara','“the Lord with the blessed throat”'),('Nīlakaṇṭha','“blue-throated”, Śiva after drinking the poison'),('Hālāhala','the poison from the churning of the ocean'),('Garalapurī','“poison town”, the name in the Śiva Purāṇa'),('Dakṣiṇa Kāśī','“Kāśī of the South”'),('Maṇikarṇikā','Kāśī’s holiest ghāṭ; its southern namesake is here'),('Saṅgama','a confluence of rivers'),('Hakīm','Persian and Urdu for physician'),('Maṇḍala','a 48-day period of worship or observance'),('Marakata','emerald'),('Jātre','Kannada for temple fair: <i>dodda</i> big, <i>chikka</i> small'),('Ratha','temple chariot'),('Teppotsava','float festival on water'),('Gopuram','gateway tower')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','NAÑJANAGŪḌU ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Lord.</b> Śrīkaṇṭheśvara, Nañjuṇḍeśvara: Śiva who drank the hālāhala and saved the worlds.</div>
<div><b>The place.</b> Nañjanagūḍu on the Kapilā (Kabini), south of Mysuru: Dakṣiṇa Kāśī, the Garalapurī of the Śiva Purāṇa.</div>
<div><b>The legends.</b> Gautama installs the liṅga; Śiva destroys Keśī; Paraśurāma’s axe and the bleeding liṅga; Pārvatī’s jewel.</div>
<div><b>The history.</b> Gaṅga roots, Cōḻa sanctum, Hoysaḷa hall, Vijayanagara shrines, the Nandi of 1644, Tipu’s emerald liṅga, and the gopuram of 1845.</div>
<div><b>The festival.</b> Dodda Jātre: five chariots on one morning, led by the giant Gautama Ratha.</div>
</div>'''+talk("So what's the one thing to remember?","He swallowed the poison so others wouldn't have to. Come here with your poison, people say, and leave it with Nañjuṇḍa.")+'<div class="key">The Lord who drank the poison: <b>the healer of the South</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Srikanteshwara Temple, Nanjangud”: names and meaning; the Kapilā; Dakṣiṇa Kāśī; Garalapurī and Keśī (Śiva Purāṇa); Paraśurāma; Pārvatī’s jewel and the Dakṣiṇa Maṇikarṇikā ghāṭ; Tipu’s elephant, the 48-day maṇḍala, the marakata liṅga and necklace, Hakīm Nañjuṇḍa, and the Mysore Gazetteer’s Hyder Ali account; Gaṅga origins, Cōḻa sanctum, Hoysaḷa maṇḍapa, Vijayanagara additions; the Nandi (1644); the gopuram (1845); the 1517 inscription; 385 × 160 ft; seven kalaśas; 122 Śiva images; 65 liṅgas; the royal sculpture; Vīrabhadra; Dodda Jātre.</p>
<p><b>Town:</b> Wikipedia, “Nanjangud”: Gaṅga builders of the 9th–10th century; Gautama’s liṅga; the Kapilā–Kauṇḍinya confluence as Paraśurāma Kṣetra; Hemmaragāla.</p>
<p><b>Festivals:</b> Star of Mysore and Deccan Herald reports on the Pañca Mahā Rathotsava (the five chariots, Gautama Ratha); Mysuru district and temple-information sites (Chikka Jātre, Teppotsava, full-moon rathotsava, Lakṣadīpotsava, Śivarātri).</p>
<p><b>Sources differ:</b> the gopuram’s tiers (seven or nine); the Gautama Ratha’s height (about 90 to 100 ft) and weight (reports range from about 120 to 205 tonnes); jade or emerald for Tipu’s liṅga; Tipu or Hyder Ali in the elephant story.</p>
<p><b>Not verified:</b> the Keśī boons as told here, the Rāghavendra maṭha and other town shrines (general knowledge); the churning story is told from the Purāṇas in brief. Maps and plans are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('lord','The Lord Who Drank the Poison'),('legends1','Legends · Gautama and Keśī'),('legends2','Legends · Paraśurāma'),('hakim','Hakīm Nañjuṇḍa'),('history','History'),('temple','The Temple'),('inside','Inside the Temple'),('rathotsava','The Five Chariots'),('festivals','Through the Year'),('around','Around Nañjanagūḍu'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">NAÑJANAGŪḌU</h1>
  <div class="series">ŚRĪKAṆṬHEŚVARA · NAÑJUṆḌEŚVARA · A REFERENCE GUIDE</div>
  <div class="tag">The Lord who drank the poison</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>When the ocean was churned, the first thing to rise was not nectar but poison. Śiva drank it, and his throat turned blue.</p>
    <p>On the Kapilā, south of Mysuru, that Śiva is worshipped as <b>Nañjuṇḍeśvara</b>, the one who drank the poison, and <b>Śrīkaṇṭheśvara</b>, the one with the blessed throat. His town, Nañjanagūḍu, is called the <b>Kāśī of the South</b>.</p>
    <p>This guide tells its legends, its history, and the morning when five chariots roll at once.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Oṃ Namaḥ Śivāya,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Kāśī is in Vārāṇasī. How is this Kāśī?","A holy river, a great Śiva, a bath that washes away sin. Wherever those three meet, devotees see Kāśī.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Nanjangud.html','w').write(head+b+tail())
print('ok')
