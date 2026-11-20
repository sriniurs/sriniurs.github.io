import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
import common_t
def head_navy(title,desc):
    h=open(common_t.SRC).read(); hd=h[:h.find('<div class="book">')]
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
head=head_navy('Male Mahadēśvara Beṭṭa · Temples around Mysuru · srini.presents',
 'Male Mahadēśvara Beṭṭa (MM Hills): the saint who rode a tiger, the seven hills, Junje Gowda’s temple, Śravaṇāsura, Saṅkamma, and the Kamsāle singers of Kannada’s great oral epic. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def HILL(x,y,w,h,c='#3a6a3a'):
    return f'<path d="M{x-w/2} {y} Q{x-w/4} {y-h*0.6} {x-w/10} {y-h} Q{x} {y-h*1.06} {x+w/10} {y-h} Q{x+w/4} {y-h*0.6} {x+w/2} {y}z" fill="{c}" stroke="#111" stroke-width="2"/>'
def TEMPLE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="#f2e6c8"/><path d="M-12 -16 h24 l-4 -10 h-16z M-8 -26 h16 l-3 -9 h-10z" fill="#e2cfa8"/><circle cy="-38" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def TIGER(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cy="-26" rx="54" ry="22" fill="#ff9f1c"/>'
     +''.join(f'<path d="M{a} -46 q4 12 0 22" stroke-width="4" fill="none"/>' for a in (-30,-14,2,18,34))
     +'<circle cx="-56" cy="-36" r="18" fill="#ff9f1c"/><path d="M-66 -52 l-4 -8 l10 4z M-48 -52 l4 -8 l-10 4z" fill="#ff9f1c"/><circle cx="-62" cy="-38" r="2.4" fill="#111"/><path d="M-70 -28 l6 2" />'
     '<path d="M54 -30 q20 -10 18 -30" fill="none" stroke="#ff9f1c" stroke-width="7"/><rect x="-40" y="-8" width="10" height="16" fill="#ff9f1c"/><rect x="28" y="-8" width="10" height="16" fill="#ff9f1c"/></g>')
def SAINT(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-18 40 q-2 -44 18 -50 q20 6 18 50z" fill="#ff8c1a"/>'
     '<circle cy="-24" r="12" fill="#c98b5a"/><path d="M-12 -32 q12 -16 24 0" fill="#2b1a0e"/><path d="M-8 -26 h16" stroke="#fff" stroke-width="2"/><path d="M-8 -22 h16" stroke="#fff" stroke-width="2"/>'
     '<path d="M-6 -2 q6 8 12 0" fill="none" stroke="#5a3a1a" stroke-width="3"/><path d="M18 -10 v-46" stroke="#7a5a2a" stroke-width="3"/><path d="M8 -56 l10 -12 l10 12 M18 -56 v-12" fill="none" stroke="#555" stroke-width="3"/></g>')
def RIDER(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+TIGER(0,0,1)+SAINT(-4,-56,.8)+'</g>'
def CYMBAL(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cx="-12" rx="12" ry="6" fill="#e0a800"/><ellipse cx="12" rx="12" ry="6" fill="#e0a800"/><circle cx="-12" r="2" fill="#7a5a2a"/><circle cx="12" r="2" fill="#7a5a2a"/></g>'
def SINGER(x,y,s=1,c='#ffd60a'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cy="-36" r="11" fill="#8a5a3a"/><path d="M-12 -44 q12 -14 24 0" fill="#2b2b2b"/><path d="M-18 40 q18 -70 36 0z" fill="{c}"/><path d="M-14 -12 l-16 -10 M14 -12 l16 -10" stroke="#8a5a3a" stroke-width="6"/>'+CYMBAL(0,-26,.8)+'</g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The saint Mahadeshwara riding a tiger in front of seven forested hills with a temple on top">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/><circle cx="320" cy="54" r="30" fill="#ffd166" opacity=".35"/>'
 +''.join(HILL(x,268,120,h,'#2f5a2f') for x,h in ((40,120),(100,150),(170,170),(240,150),(300,130),(350,110),(200,100)))+TEMPLE(170,104,1.1)+RIDER(220,240,1.3)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','<b>Male Mahadēśvara</b> (“Mahadēśvara of the hills”, lovingly <b>Mādappa</b>): a saint revered as an incarnation of <b>Śiva</b>, worshipped as a <b>self-born liṅga</b>'),
 ('Mount','A <b>tiger</b>, the <i>huli vāhana</i>'),
 ('Place','Male Mahadēśvara Beṭṭa (MM Hills), Hanur taluk, Chamarajanagar district, Karnataka'),
 ('Hills','The <b>seven hills</b> of the legend, at about 3,000 ft; the highest peak of the range, Ponnāci Beṭṭa, is 1,514 m'),
 ('Saint’s time','The <b>15th century</b>, by historical evidence; about 600 years ago'),
 ('Builder','<b>Junje Gowḍa</b>, a Kuruba landlord, by legend'),
 ('Epic','The <b>Male Mādēśvara Kāvya</b>, one of Kannada’s two most famous oral epics, sung by the <b>Kamsāle</b> singers'),
 ('Pilgrims','Lakhs, from Karnataka, Tamil Nadu and Kerala'),
 ('Fairs','At <b>Dīpāvaḷi</b>, <b>Śivarātri</b> and <b>Ugādi</b>')])
 +talk("A saint who rode a tiger? For real?","That's how every song about him begins! Sit down, Zappy, this story takes seven nights to sing.")))
mapfig=fig(560,240,'Schematic map: the MM Hills between the Kaveri to the north and east and the Palar to the south, meeting at the south-east corner; the Biligiri Rangana hills to the west; the temple in the middle. Not to scale.',
 '<rect width="560" height="240" fill="#eef6e4"/><path d="M0 20 C 200 30, 400 10, 520 60 C 540 120, 530 180, 520 230" fill="none" stroke="#4aa3df" stroke-width="18"/><path d="M60 230 C 220 220, 380 236, 520 226" fill="none" stroke="#4aa3df" stroke-width="10"/>'
 +''.join(HILL(x,180,90,h,'#3a6a3a') for x,h in ((200,70),(260,90),(320,80),(380,70),(290,60)))+TEMPLE(290,98,.8)+T(290,200,'MALE MAHADĒŚVARA BEṬṬA',11,'#0b2a4a')
 +'<path d="M40 140 Q70 90 100 140z" fill="#5a8a4a" stroke="#111"/>'+T(70,160,'BR HILLS',10,'#0b2a4a')+T(300,40,'KĀVERĪ',12,'#1d6fb8')+T(300,220,'PĀLĀR',11,'#1d6fb8')
 +'<circle cx="520" cy="228" r="6" fill="#e0a800" stroke="#111"/>'+T(510,214,'confluence',9,'#555','end')+T(470,140,'TAMIL NADU →',10,'#555')+T(110,236,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','Hills between two rivers, two states',mapfig+'''<div class="panel reading">
<p><b>The hills.</b> MM Hills rise in the far south-east of Karnataka, beside Tamil Nadu. With the <b>Biḷigiri Raṅgana</b> hills, they form a bridge between the Eastern and Western Ghats.</p>
<p><b>The rivers.</b> The <b>Kāverī</b> bounds them on the north and east, the <b>Pālār</b> on the south; the two meet at the south-east corner of the forest.</p>
<p><b>The forest.</b> Sandalwood and bamboo cover the slopes, home to elephants, gaur, sambar and sloth bears; tigers and leopards are rarely seen. Much of it is now the <b>Male Mahadēśvara Wildlife Sanctuary</b>.</p>
</div>'''))
pages.append(page('saint','WHO WAS MAHADĒŚVARA?','Saint, healer, Śiva on earth',fig(560,170,'The young saint in saffron with a trident-staff, travelling from a distant temple through forests toward seven hills',
 '<rect width="560" height="170" fill="#fff4dc"/>'+TEMPLE(70,120,1.2)+T(70,140,'ŚRĪŚAILA',10,'#0b2a4a')+'<path d="M110 120 C 220 80, 300 150, 400 110" stroke="#111" stroke-width="2" stroke-dasharray="8 6" fill="none"/>'
 +SAINT(250,124,1)+''.join(HILL(x,170,70,h,'#3a6a3a') for x,h in ((440,90),(490,110),(530,80))))+facts([
 ('Birth','Born in the Kali Yuga, by legend, to <b>Uttarājamma</b> and <b>Candraśēkhara Mūrti</b> of the Ādi Jāmbava community'),
 ('Guides','Guided by the heads of the Vīraśaiva Liṅgāyat <b>Suttūr</b> and <b>Kunthūr</b> maṭhas'),
 ('Journey','Came from <b>Śrīśaila</b>, working miracles on the way, and settled on the seven hills to do penance'),
 ('Healer','Lived as a <i>siddha</i>, practising medicine and teaching non-violence; tradition tells of him curing diseased cattle'),
 ('Lineage','Liṅgāyats count him as their own; one account makes him the third head of the Haradanahaḷḷi maṭha')])
 +talk("Was he a real person or a god?","Both, for his devotees: a 15th-century saint who lived here, and Śiva himself in human form.")))
pages.append(page('tiger','THE TIGER RIDER','Huli vāhana',fig(560,200,'The saint riding calmly on a striped tiger through the forest',
 '<rect width="560" height="200" fill="#e8f5e2"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="28" fill="#5a9a4a" stroke="#111" stroke-width="2"/><rect x="{x-4}" y="{y+24}" width="8" height="{190-y}" fill="#6a4a2a"/>' for x,y in ((50,70),(510,60),(450,90)))
 +RIDER(270,190,1.6))+'''<div class="panel reading">
<p><b>His mount.</b> Mahadēśvara is said to have travelled the forest on a <b>tiger</b>, the <i>huli vāhana</i>, and to have worked many miracles around the hills to protect the people and sages living there.</p>
<p><b>Tamer of the wild.</b> For the forest people, a man who could ride a tiger was proof of his power over the jungle and all its dangers.</p>
<p><b>The great statue.</b> In <b>2023</b> a <b>108-ft</b> statue of Mahadēśvara on his tiger, trident in hand, was unveiled on a rock on the hilltop, visible from across the hills.</p>
</div>'''))
pages.append(page('hills','THE SEVEN HILLS','Eḷu male: Mahadēśvara’s mountains',fig(560,150,'Seven forested peaks in a row, each labelled',
 '<rect width="560" height="150" fill="#dcecff"/>'+''.join(HILL(50+i*76,130,96,60+(i%3)*14,'#3a6a3a')+T(50+i*76,146,n,9,'#0b2a4a') for i,n in enumerate(('ANUMALE','JĒNUMALE','KĀNUMALE','PACCHEMALE','PAVAḶAMALE','PONNĀCIMALE','KOṄGUMALE'))))+'''<div class="panel reading">
<p><b>The seven peaks.</b> Tradition names seven hills that together make up Male Mahadēśvara Beṭṭa: <b>Anumale, Jēnumale, Kānumale, Pacchemale, Pavaḷamale, Ponnācimale</b> and <b>Koṅgumale</b>. In the songs, the saint is the Lord of the seven hills.</p>
<p><b>Male means hill.</b> <i>Male</i> is Kannada for hill or hill-forest: <b>Male Mahadēśvara</b> is simply “Mahadēśvara of the hills”.</p>
<p><b>Ponnāci.</b> The highest point of the whole range is <b>Ponnāci Beṭṭa</b>, 1,514 m, clothed in evergreen forest.</p>
</div>'''+talk("Seven hills, like Tirumala?","Exactly the same idea: the Lord who lives on seven hills. In the south, seven hills is the address of a god!")))
epic=('<table class="ct"><tr><th>Part</th><th>What it tells</th></tr>'+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in (
 ('1','The saint’s miraculous birth, childhood and spiritual quest'),('2','How he wins over the rich <b>Junje Gowḍa</b> to build him a temple on the seven hills'),
 ('3','The destruction of the evil king <b>Śravaṇāsura</b>'),('4','<b>Saṅkamma</b>: the longest part, the ordeals of a proud wife who keeps her dignity'),
 ('5','<b>Bēvinaṭṭi Kāḷamma</b>: a comic tale of a vain, miserly woman'),('6','The simple, god-fearing couple <b>Mūgayya</b> and his wife become devotees'),
 ('7','The benediction, and a short retelling of the whole epic')))+'</table>')
pages.append(page('epic','THE EPIC OF MĀDAPPA','Male Mādēśvara Kāvya',epic+'''<div class="panel reading">
<p><b>An oral epic.</b> The <b>Male Mādēśvara Kāvya</b>, also called <i>Mādappana Kathe</i>, has been sung for centuries without a fixed written text. With the <i>Manteswamy Kāvya</i>, it is one of the two most renowned oral epics in Kannada.</p>
<p><b>Seven nights.</b> The full epic, in seven parts, can take seven nights to sing; pilgrims sing it on their way to the hill fairs.</p>
<p><b>A familiar shape.</b> Scholars note its outline echoes the Rāmāyaṇa: the god comes to earth to destroy an evil king.</p>
</div>'''))
leg=fig(560,190,'The saint arriving at a rich landlord’s house, cattle and granaries all around; then the landlord bowing; then a temple rising on the hill',
 '<rect width="560" height="190" fill="#fff4dc"/><rect x="40" y="90" width="110" height="70" fill="#e2cfa8" stroke="#111" stroke-width="2"/><path d="M30 90 l65 -40 l65 40z" fill="#c0392b" stroke="#111" stroke-width="2"/>'+SAINT(200,150,.9)
 +'<g transform="translate(300 170)" stroke="#111" stroke-width="2"><circle cx="-20" cy="-20" r="10" fill="#c98b5a"/><path d="M-30 -10 q20 -10 40 10 h-40z" fill="#fff"/></g>'+HILL(460,190,180,110)+TEMPLE(460,84,.9)
 +T(95,180,'JUNJE GOWḌA',11,'#0b2a4a')+T(460,180,'THE TEMPLE',11,'#0b2a4a'))
pages.append(page('legends','THE LEGENDS','Junje Gowḍa, Śravaṇāsura and Saṅkamma',leg+'''<div class="steps">
<div><b>Junje Gowḍa.</b> Junje Gowḍa was a wealthy Kuruba landlord, a devotee of the god Bēredēvara. Mahadēśvara came to his house and worked miracles there until Junje Gowḍa became his follower, and built his temple on the hill. His descendants are said to live still at Kadamboor in Hanur taluk.</div>
<div><b>Śravaṇāsura.</b> An evil king who oppressed the land. In the epic, Śiva comes down as Mahadēśvara above all to destroy him.</div>
<div><b>Saṅkamma.</b> The heart of the epic: a proud, virtuous wife who suffers and endures. Many listeners say her story is the most moving of all.</div>
</div>'''))
pages.append(page('kamsale','THE KAMSĀLE SINGERS','Keepers of the epic',fig(560,170,'Three devotees in a row dancing and clashing bronze cymbals, singing the epic',
 '<rect width="560" height="170" fill="#fdf3d8"/>'+SINGER(160,150,1.1,'#ffd60a')+SINGER(280,150,1.1,'#ff8c1a')+SINGER(400,150,1.1,'#ffd60a')
 +''.join(f'<path d="M{x} 50 q6 -10 12 0" fill="none" stroke="#e0a800" stroke-width="3"/>' for x in (130,250,370,430)))+facts([
 ('The name','<i>Kamsāle</i> comes from <i>kāṃsya tāḷa</i>, bronze cymbals: the singers keep time by clashing them as they dance'),
 ('The singers','Called <b>Dēvara Guḍḍas</b>, “servants of the god”, and <b>Kamsāleyavaru</b>'),
 ('A vow','Only those who have taken a <i>dīkṣā</i>, a vow of devotion to Mahadēśvara, may perform it; it is taught by a teacher'),
 ('Oral','They learn the songs by heart, with no printed text'),
 ('When','At the hill fairs of Dīpāvaḷi, Śivarātri and Ugādi, and on Kārtika Mondays')])
 +talk("They learn a seven-night epic by heart?","Every word, passed from teacher to student. Kannada's living library!")))
pages.append(page('temple','THE TEMPLE','The liṅga where the saint still sits',fig(560,170,'The temple courtyard with a great Nandi before the shrine, the linga in the sanctum, and a stream flowing nearby',
 '<rect width="560" height="170" fill="#f6f1e2"/><rect x="200" y="30" width="160" height="110" fill="#e2cfa8" stroke="#111" stroke-width="2"/><rect x="250" y="70" width="60" height="70" fill="#5a3a1a" stroke="#111"/>'
 +'<g transform="translate(280 136)" stroke="#111" stroke-width="2"><path d="M-22 0 h44 l-4 -8 h-36z" fill="#8a8a8a"/><path d="M-9 -8 v-20 a9 9 0 0 1 18 0 v20z" fill="#3a3a3a"/></g>'
 +'<ellipse cx="130" cy="140" rx="30" ry="14" fill="#bbb" stroke="#111"/><circle cx="104" cy="128" r="10" fill="#bbb" stroke="#111"/>'+T(130,166,'NANDI',10)
 +'<path d="M420 20 C 440 80, 470 120, 520 170" stroke="#4aa3df" stroke-width="10" fill="none"/>'+T(490,90,'ANTARAGAṄGE',9,'#1d6fb8'))+'''<div class="g2">
<div class="card bg-blue"><h4>🕉 The liṅga</h4><p>In the sanctum is a <b>self-born (svayambhū) liṅga</b>. Devotees believe Mahadēśvara is still there, deep in penance.</p></div>
<div class="card bg-yellow"><h4>💧 Antaragaṅge</h4><p>A pilgrimage here includes a dip in the <b>Antaragaṅge</b>, a stream fed by a spring that never runs dry.</p></div>
</div>
<div class="panel reading"><p><b>A hill town.</b> The temple grounds cover about <b>155 acres</b>, and the temple also holds lands in nearby villages. In <b>2023</b> a <b>silver chariot</b> was unveiled for the Lord.</p></div>'''))
pages.append(page('history','HISTORY','From saint to sanctuary',tl([
 ('15th c.','Mahadēśvara lives and does penance on the hills; by tradition, Junje Gowḍa builds the temple.'),
 ('Sālūr maṭha','The <b>Sālūr maṭha</b>, said to have been founded by Mahadēśvara himself, manages the temple for centuries.'),
 ('1953','The <b>Madras Government</b> takes over the temple: the hills then lay in Madras State’s Kollegal taluk.'),
 ('After 1956','With the formation of Karnataka, a trust committee under the Muzrāi Department takes charge.'),
 ('2013','The forest is notified as the <b>Male Mahadēśvara Wildlife Sanctuary</b>.'),
 ('2023','The 108-ft statue and the silver chariot are unveiled.')])
 +'<div class="panel reading small"><p><b>Note.</b> Sources agree on the 15th century for the saint and the temple’s origin, but give no inscriptional date for the building; Junje Gowḍa’s role comes from legend and the epic.</p></div>'))
pages.append(page('festivals','THE HILL FAIRS','When the hills fill with song',facts([
 ('Dīpāvaḷi','The great fair, with Kamsāle singers and pilgrims walking up the hills'),
 ('Mahāśivarātri','Night-long worship of the Lord of the hills; the great statue is lit up'),
 ('Ugādi','The Kannada New Year fair'),
 ('Kārtika Mondays','Special days of worship, when Kamsāle is most often seen')])
 +'''<div class="panel reading"><p><b>Walking and singing.</b> Many pilgrims, especially from the villages of Karnataka and Tamil Nadu, walk to the hills for the fairs, singing parts of the epic as they go.</p></div>'''
 +talk("Do they sing the whole epic on the way?","Some groups sing for seven nights! Others pick their favourite parts. Nobody is in a hurry here.")))
pages.append(page('people','THE PEOPLE OF THE HILLS','A god of the forest people',facts([
 ('Soligas','Mahadēśvara is the family god of the <b>Soligas</b> and other forest peoples of the hills; Soliga lore traces their origin to Kārayya, a son of Mahadēśvara'),
 ('Kurubas','Junje Gowḍa, the builder of legend, was a Kuruba landlord'),
 ('Liṅgāyats','Count the saint as one of their own; the maṭhas of Suttūr, Kunthūr and Sālūr are part of his story'),
 ('Two states','Kannada and Tamil devotees alike: the hills sit on the border')])
 +'''<div class="panel reading"><p><b>Everyone’s Mādappa.</b> A saint born to the Ādi Jāmbava community, guided by Liṅgāyat maṭhas, housed by a Kuruba landlord and worshipped by forest people: MM Hills gathers communities that rarely share one god.</p>
<p>Next door: <a href="/bhakti/temples-of-india/around-mysuru/br-hills/">Biḷigiri Raṅgana Beṭṭa</a>, where the Soligas call Viṣṇu their brother-in-law.</p></div>'''))
glossary=[('Male','hill, hill-forest (Kannada)'),('Mādappa','an affectionate name for Mahadēśvara'),('Huli vāhana','tiger mount'),('Eḷu male','the seven hills'),('Svayambhū','self-born, not made by hands'),('Siddha','a perfected sage and healer'),('Kāvya','a long poem; here an oral epic'),('Kamsāle','the cymbal song-and-dance of Mahadēśvara’s devotees'),('Dēvara Guḍḍa','a devotee-singer vowed to the god'),('Dīkṣā','initiation, a vow'),('Maṭha','a monastery'),('Muzrāi','the state department for temples'),('Antaragaṅge','“the hidden Gaṅgā”, a perennial stream'),('Jātre','a temple fair')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','MM HILLS ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Lord.</b> Male Mahadēśvara, Mādappa: a 15th-century saint seen as Śiva, worshipped as a self-born liṅga.</div>
<div><b>The place.</b> The seven hills between the Kāverī and the Pālār, in a wildlife sanctuary on the Karnataka–Tamil Nadu border.</div>
<div><b>The legends.</b> The tiger rider; Junje Gowḍa’s temple; Śravaṇāsura destroyed; Saṅkamma’s ordeal.</div>
<div><b>The epic.</b> The Male Mādēśvara Kāvya, seven parts, seven nights, sung by the Kamsāle singers.</div>
<div><b>The fairs.</b> Dīpāvaḷi, Śivarātri and Ugādi; the 108-ft statue and silver chariot of 2023.</div>
</div>'''+talk("One line to remember?","A saint on a tiger, seven hills, and an epic sung for six hundred years. That's Mādappa.")+'<div class="key">Lord of the seven hills: <b>the tiger-riding saint of the forest people</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Hills and temple:</b> Wikipedia, “Male Mahadeshwara Hills”: Hanur taluk; about 3,000 ft; Ponnāci Beṭṭa 1,514 m; 155.57 acres; the bridge of the Ghats; Kāverī and Pālār; the sanctuary (2013); flora and fauna; Junje Gowḍa; the 15th century; the svayambhū liṅga; the tiger; curing cattle; Liṅgāyat claim and the Haradanahaḷḷi maṭha. Wikipedia, “Junje Gowda”: Bēredēvara; Kadamboor. Wikipedia (archived), “Mahadeshwara”: Uttarājamma and Candraśēkhara Mūrti; Suttūr and Kunthūr; Śrīśaila; the seven peaks; the seven parts of the epic; Kamsāle; the fairs; Sālūr maṭha to 1953 and the Muzrāi trust; Antaragaṅge.</p>
<p><b>Epic:</b> Classical Kannada database, “Male Madeshvara Kavya” (oral epic; Dēvara Guḍḍas; kāṃsya tāḷa; with Manteswamy Kāvya). <b>Soligas:</b> Evolve Back, Wikipedia “Soliga people”. <b>Statue and chariot:</b> Deccan Herald and Star of Mysore, March 2023.</p>
<p><b>Not verified:</b> the third-abbot claim; the 1953 takeover detail (Kollegal’s place in Madras State until 1956 is general knowledge). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('saint','Who Was Mahadēśvara?'),('tiger','The Tiger Rider'),('hills','The Seven Hills'),('epic','The Epic of Mādappa'),('legends','The Legends'),('kamsale','The Kamsāle Singers'),('temple','The Temple'),('history','History'),('festivals','The Hill Fairs'),('people','The People of the Hills'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,6.2vw,68px)">MALE MAHADĒŚVARA BEṬṬA</h1>
  <div class="series">MM HILLS · MĀDAPPA · A REFERENCE GUIDE</div>
  <div class="tag">The saint who rode a tiger</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Far in the south-east of Karnataka, where the Kāverī and the Pālār wrap around a tangle of forested hills, a saint once rode in on a tiger.</p>
    <p>Six hundred years later he is <b>Male Mahadēśvara</b>, Śiva of the hills, lovingly called <b>Mādappa</b>. Lakhs climb to his temple, and singers with bronze cymbals still sing his epic through the night.</p>
    <p>This guide tells his story, his hills and his songs.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Oṃ Namaḥ Śivāya,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is it true they sing about him all night?","All night, for seven nights, if you want the full version! Grab a mat, Zappy.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/MM_Hills.html','w').write(head+b+tail())
print('ok')
