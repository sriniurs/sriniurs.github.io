import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
import common_t
def head_navy(title,desc):
    h=open(common_t.SRC).read(); hd=h[:h.find('<div class="book">')]
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
head=head_navy('Tirumakūḍalu Narasipura · Temples around Mysuru · srini.presents',
 'Tirumakūḍalu Narasipura (T. Narasipura): the triple confluence of the Kāverī, Kapilā and hidden Sphaṭika Sarovara; Agastyeśvara and the sand liṅga; Guñja Narasiṃha, holier than Kāśī by a guñja seed; and South India’s Kumbha Mela. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def TEMPLE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="#f2e6c8"/><path d="M-14 -16 h28 l-4 -10 h-20z M-10 -26 h20 l-4 -10 h-12z" fill="#e2cfa8"/><circle cy="-40" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def LINGA(x,y,s=1,c='#3a3a3a',water=False):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 0 h60 l-6 -10 h-48z" fill="#8a8a8a"/><path d="M20 -6 h18 l-3 5 h-15z" fill="#8a8a8a"/>'
    g+= f'<path d="M-12 -10 v-22 h24 v22z" fill="{c}"/><ellipse cy="-32" rx="12" ry="4" fill="#4aa3df"/>' if water else f'<path d="M-12 -10 v-26 a12 12 0 0 1 24 0 v26z" fill="{c}"/>'
    return g+'</g>'
def NARASIMHA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-22 60 h44 l-4 -60 h-36z" fill="#ffd60a"/><circle cy="-10" r="18" fill="#e0a800"/><path d="M-18 -20 q-10 -16 6 -18 M18 -20 q10 -16 -6 -18" fill="#e0a800"/><circle cx="-7" cy="-12" r="3" fill="#111"/><circle cx="7" cy="-12" r="3" fill="#111"/><path d="M-8 0 q8 6 16 0" fill="none"/><path d="M-12 -28 h24 l-4 -16 h-16z" fill="#c0392b"/><path d="M16 14 l20 -10" stroke="#e0a800" stroke-width="7"/><circle cx="40" cy="2" r="5" fill="#c0392b"/><circle cx="43" cy="1" r="2" fill="#111"/></g>'
def GUNJA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.5"><ellipse rx="10" ry="8" fill="#c0392b"/><path d="M4 -7 a8 7 0 0 1 6 7 h-6z" fill="#111"/></g>'
def HANUMAN(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cy="-6" r="13" fill="#c98b5a"/><path d="M-6 -2 q6 6 12 0" fill="#e0a07a"/><path d="M-14 10 q14 30 28 0z" fill="#c0392b"/><path d="M-14 -2 l-26 -30 M14 -2 l26 -30" stroke="#c98b5a" stroke-width="7"/><path d="M14 18 q30 10 20 -20" fill="none" stroke="#c98b5a" stroke-width="4"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Two rivers meeting in a Y with a hidden third spring rising between them, temples on the banks, and pilgrims bathing">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/><circle cx="320" cy="50" r="26" fill="#ffd166" opacity=".4"/>'
 '<path d="M0 120 C 120 140, 170 170, 190 200" stroke="#4aa3df" stroke-width="40" fill="none"/><path d="M380 110 C 260 140, 210 170, 190 200" stroke="#5ab6e8" stroke-width="30" fill="none"/><path d="M190 200 V268" stroke="#4aa3df" stroke-width="56"/>'
 '<circle cx="190" cy="200" r="16" fill="#bff" stroke="#fff" stroke-width="3" opacity=".9"/>'+TEMPLE(80,104,1.3)+TEMPLE(300,96,1.3)
 +''.join(person(x,264,c,'#c98b5a',.55) for x,c in ((160,'#ff8c1a'),(185,'#fff'),(215,'#ffd60a')))+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Place','<b>Tirumakūḍalu Narasipura</b> (T. Narasipura), Mysuru district, south-east of Mysuru'),
 ('Name','<i>Tiru-mū-kūḍalu</i>, “the sacred meeting of three”, and <b>Narasipura</b>, the town of Narasiṃha'),
 ('Confluence','The <b>Kāverī</b>, the <b>Kapilā</b> (Kabini) and the hidden <b>Sphaṭika Sarovara</b>: a <i>trimakūṭa kṣetra</i> in the Skanda Purāṇa'),
 ('Śiva','<b>Agastyeśvara</b>: a liṅga of sand made by the sage Agastya, with water ever in its top'),
 ('Viṣṇu','<b>Guñja Narasiṃha</b>, holding a guñja berry: holier than Kāśī by the weight of one seed'),
 ('Titles','<b>Dakṣiṇa Kāśī</b> and South India’s <b>Prayāga</b>'),
 ('Kumbha Mela','Every <b>three years</b> since <b>1989</b>, at the confluence'),
 ('Deeper past','A <b>Neolithic</b> settlement, nearly 4,000 years old, dug up across the river')])
 +talk("Three rivers but I can only see two?","The third is hidden, Zappy, a lake that rises from below. Just like the Sarasvatī at Prayāga!")))
mapfig=fig(560,230,'Schematic map: the Kaveri from the west and the Kapila from the south meeting at T. Narasipura, with the hidden Sphatika Sarovara marked at the meeting point, Agastyeshvara and Gunja Narasimha temples on the banks, and the Neolithic site and Bhikshesvara across the river. Not to scale.',
 '<rect width="560" height="230" fill="#eef6e4"/><path d="M0 80 C 160 90, 240 110, 290 130 C 360 150, 460 150, 560 140" fill="none" stroke="#4aa3df" stroke-width="22"/><path d="M200 230 C 230 190, 260 160, 290 130" fill="none" stroke="#5ab6e8" stroke-width="14"/>'
 +'<circle cx="290" cy="130" r="12" fill="#bff" stroke="#1d6fb8" stroke-width="3" stroke-dasharray="4 3"/>'+T(310,118,'SAṄGAMA · SPHAṬIKA SAROVARA',10,'#1d6fb8','start')
 +TEMPLE(240,104,.7)+T(240,62,'AGASTYEŚVARA',9,'#0b2a4a')+TEMPLE(350,190,.7)+T(350,214,'GUÑJA NARASIṂHA',9,'#0b2a4a')
 +'<circle cx="300" cy="60" r="5" fill="#8a7a6a" stroke="#111"/>'+T(310,56,'BHIKṢEŚVARA · NEOLITHIC SITE',9,'#555','start')
 +T(60,70,'KĀVERĪ',12,'#1d6fb8')+T(190,222,'KAPILĀ',11,'#1d6fb8','end')+T(80,224,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','Where three become one',mapfig+'''<div class="panel reading">
<p><b>The rivers.</b> At T. Narasipura the <b>Kapilā</b> (the Kabini of Nañjanagūḍu) flows into the <b>Kāverī</b>. Tradition adds a third: the <b>Sphaṭika Sarovara</b>, a crystal lake said to rise unseen at the very meeting point.</p>
<p><b>Three-in-one.</b> The Skanda Purāṇa counts such places of three waters as <b>trimakūṭa kṣetras</b>, among the holiest of all bathing places.</p>
<p><b>A rich land.</b> The river-fed fields grow rice and silk; Talakāḍu, the old Gaṅga capital, lies in the same taluk.</p>
</div>'''))
pages.append(page('name','THE NAME','Three meetings and a Narasiṃha',facts([
 ('Tiru','Sacred, holy'),('Mū / Mu','Three'),('Kūḍalu','A meeting of rivers, a confluence'),
 ('Narasipura','The town of <b>Narasiṃha</b>, from the Guñja Narasiṃha temple'),
 ('Dakṣiṇa Kāśī','“Kāśī of the South”, for its holy waters and Śiva'),
 ('Dakṣiṇa Prayāga','South India’s Prayāga: two visible rivers and one hidden, like the Gaṅgā, Yamunā and Sarasvatī at Prayāgarāj')])
 +'<div class="panel reading"><p><b>Say it fast.</b> Locals shorten it to <b>T. Narasipura</b> or simply <b>Narsipur</b>, but the full name tells the whole story: a holy three-river meeting, with Narasiṃha on its bank.</p></div>'))
leg1=fig(560,190,'Sage Agastya by the river shaping a linga out of sand; in the sky, Hanuman flying in late carrying a linga from Kashi',
 '<rect width="560" height="190" fill="#fff4dc"/><path d="M0 160 q140 -14 280 0 t280 0 V190 H0z" fill="#4aa3df"/>'+person(140,160,'#ff8c1a','#c98b5a',1)+'<path d="M120 98 q20 -24 40 0" fill="#fff" stroke="#111"/>'
 +'<g transform="translate(220 160)"><path d="M-30 0 h60 l-6 -10 h-48z" fill="#e8d29a" stroke="#111" stroke-width="2"/><path d="M-12 -10 v-26 a12 12 0 0 1 24 0 v26z" fill="#e8d29a" stroke="#111" stroke-width="2"/></g>'
 +HANUMAN(430,70,1.3)+LINGA(470,40,.6)+'<path d="M560 40 q-50 0 -90 20" stroke="#ccc" stroke-width="2" stroke-dasharray="6 5" fill="none"/>'+T(140,184,'AGASTYA',11,'#0b2a4a')+T(430,128,'HANUMĀN',11,'#c0392b'))
pages.append(page('agastya','THE LEGEND OF AGASTYEŚVARA','A liṅga of sand',leg1+'''<div class="steps">
<div><b>The sage’s wish.</b> The sage <b>Agastya</b>, charmed by the meeting of the three waters, wanted to install a liṅga of Śiva here, and asked <b>Hanumān</b> to bring one from <b>Kāśī</b>.</div>
<div><b>The hour.</b> The auspicious moment came, and Hanumān had not returned. So Agastya shaped a liṅga out of the <b>river sand</b> and consecrated it: a <b>saikata liṅga</b>.</div>
<div><b>Hanumān’s anger.</b> Hanumān arrived, felt slighted, and struck off the top of the sand liṅga.</div>
<div><b>The water.</b> From that cut summit, water has welled up ever since, said to be the water of the Gaṅgā; priests give it to pilgrims as tīrtha. The liṅga Hanumān brought was installed nearby: the <b>Hanumān liṅga</b>.</div>
</div>'''+talk("Hanumān chopped a liṅga in a temper?","He's devoted, not perfect! And the story ends well: two liṅgas instead of one, and a spring of holy water.")))
ag=fig(560,170,'The flat-topped sand linga with water in its top, beside the Hanuman linga',
 '<rect width="560" height="170" fill="#eef3fa"/>'+LINGA(200,150,2.4,c='#c9b27a',water=True)+LINGA(400,150,2)+T(200,166,'AGASTYEŚVARA (SAIKATA)',11,'#0b2a4a')+T(400,166,'HANUMĀN LIṄGA',11,'#0b2a4a'))
pages.append(page('agastyesvara','AGASTYEŚVARA TEMPLE','The older temple of the town',ag+facts([
 ('The liṅga','A <b>saikata</b> (sand) liṅga with a hollow at the top that always holds water; when filled, it overflows through an opening called the <b>nābhi</b>, the navel'),
 ('Age','Older than the Guñja Narasiṃha temple; its complex holds work of the <b>Gaṅgas</b>, <b>Cōḻas</b>, <b>Hoysaḷas</b> and <b>Vijayanagara</b>'),
 ('Inside','The Hanumān liṅga in its own sanctum; pillared halls and old carvings'),
 ('Festival','An annual car festival and fair')])
 +'<div class="panel reading small"><p><b>Five liṅgas.</b> Tradition also names a local Pañcaliṅga of T. Narasipura: Agastyeśvara, the Hanumān liṅga, Someśvara, Mārkaṇḍeśvara, and Gargeśvara at Gargeśvari village.</p></div>'))
leg2=fig(560,190,'A washerman beating clothes on a stone by the river; in his dream Narasimha appears; then Narasimha seated holding a red gunja seed, set on a balance against Kashi',
 '<rect width="560" height="190" fill="#e8f5e2"/><path d="M0 160 q140 -14 280 0 V190 H0z" fill="#4aa3df"/><rect x="60" y="140" width="60" height="20" fill="#8a8a8a" stroke="#111"/>'+person(140,150,'#fff','#8a5a3a',.9)
 +'<g opacity=".8">'+NARASIMHA(190,60,.6)+'</g>'
 +'<g transform="translate(410 120)" stroke="#111" stroke-width="2"><path d="M0 -60 v60 M-70 -50 h140" /><path d="M-90 -50 l20 30 h-40z M50 -50 l20 30 h-40z" fill="none"/><path d="M-90 -20 h40" stroke-width="3"/><path d="M50 -20 h40" stroke-width="3"/></g>'
 +TEMPLE(340,98,.5)+T(340,116,'KĀŚĪ',9)+TEMPLE(480,104,.5)+GUNJA(500,92,.6)+T(480,122,'T. NARASIPURA + 1 GUÑJA',8,'#c0392b'))
pages.append(page('gunja','THE LEGEND OF GUÑJA NARASIṂHA','Holier than Kāśī by one seed',leg2+'''<div class="steps">
<div><b>A washerman’s wish.</b> A washerman who washed clothes every day at the confluence longed to go on pilgrimage to <b>Kāśī</b>.</div>
<div><b>A dream.</b> <b>Narasiṃha</b> appeared to him in a dream and told him that his image lay beneath the very stone on which he beat the clothes, and that there was no need to go to Kāśī.</div>
<div><b>One seed more.</b> The Lord declared that a pilgrimage here would bring merit greater than Kāśī’s by the weight of one <b>guñja</b> seed: the tiny red-and-black seed once used by goldsmiths as a weight.</div>
<div><b>The proof.</b> The image of Narasiṃha here holds a <b>guñja</b> berry in his hand, and a guñja tree grows before the temple gate.</div>
</div>'''+talk("A whole pilgrimage won by one tiny seed?","A guñja seed weighs about an eighth of a gram! It's the town's proudest boast: just a little holier than Kāśī.")))
nar=fig(560,180,'The temple of Gunja Narasimha with its tall gateway tower and pillared hall; Narasimha with Lakshmi inside holding a gunja seed',
 '<rect width="560" height="180" fill="#fff4dc"/><rect x="60" y="60" width="70" height="110" fill="#e2cfa8" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{60+i*5} {60-i*12} h{70-i*10} l-3 -12 h{-(64-i*10)}z" fill="#d9c9a0" stroke="#111"/>' for i in range(4))+T(95,176,'GOPURA',9)
 +'<rect x="180" y="100" width="140" height="70" fill="#f6f1e2" stroke="#111"/>'+''.join(f'<rect x="{190+i*34}" y="104" width="10" height="66" fill="#c9a26b" stroke="#111"/>' for i in range(4))+T(250,94,'FOUR-PILLARED MAṆḌAPA',9)
 +NARASIMHA(430,110,1.1)+'<g transform="translate(490 150)" stroke="#111" stroke-width="2"><circle cy="-36" r="10" fill="#f2c79b"/><path d="M-16 30 q16 -60 32 0z" fill="#e05a8a"/></g>')
pages.append(page('narasimha','GUÑJA NARASIṂHA TEMPLE','A Vijayanagara temple on the bank',nar+facts([
 ('Age','Vijayanagara period, about the <b>16th century</b>; often said to be about 450 years old'),
 ('Inscriptions','Records from the time of <b>Kṛṣṇadevarāya</b>, and many records in Nāgarī script'),
 ('Style','Dravidian with Hoysaḷa touches: an imposing gopura over the main gate, a four-pillared maṇḍapa before the sanctum, and a prākāra with minor shrines'),
 ('Patrons','Later, the <b>Daḷavāy</b> of Mysuru paid a yearly allowance for its upkeep (B. Lewis Rice)'),
 ('The Goddess','Narasiṃha is worshipped with <b>Mahālakṣmī</b>; there are shrines of the Āḻvārs and ācāryas'),
 ('Today','A protected monument of the Archaeological Survey of India')])))
mela=fig(560,170,'Crowds of pilgrims and sadhus bathing at the confluence at dawn, with flags and tents on the riverbank',
 '<rect width="560" height="170" fill="#ffe9c4"/><circle cx="480" cy="40" r="22" fill="#ffd166"/><path d="M0 110 q280 -20 560 0 V170 H0z" fill="#4aa3df"/>'
 +''.join(f'<path d="M{x} 110 l20 -40 l20 40z" fill="{c}" stroke="#111"/>' for x,c in ((40,'#ff8c1a'),(100,'#fff'),(380,'#ff8c1a')))
 +crowd(['#ff8c1a','#fff','#ffd60a','#c98b5a','#e05a8a','#ff8c1a'],150,30,150,.55)+''.join(f'<path d="M{x} 70 v-30 l16 8 l-16 8" fill="#c0392b" stroke="#111"/>' for x in (160,300)))
pages.append(page('kumbha','THE KUMBHA MELA','South India’s great bath',mela+'''<div class="panel reading">
<p><b>Since 1989.</b> T. Narasipura holds a <b>Kumbha Mela</b> every <b>three years</b>, begun in 1989: South India’s answer to the great melas of Prayāgarāj and Nāsik.</p>
<p><b>The bath.</b> Lakhs of devotees, and sādhus from across the country, take the holy dip at the confluence of the three waters.</p>
<p><b>Old waters, new festival.</b> The place is ancient; the Kumbha Mela here is recent. Both are part of its story.</p>
</div>'''+talk("Can I do the Kumbha bath without going all the way north?","That was exactly the idea! Every three years, Prayāga comes to Mysuru's doorstep.")))
pages.append(page('history','HISTORY','From the Stone Age to the Woḍeyars',tl([
 ('c. 2000 BCE','A <b>Neolithic</b> settlement on the left bank of the Kāverī, near the Bhikṣeśvara temple: burials, pots, stone and metal tools, beads and bangles (excavated 1959–65).'),
 ('Gaṅgas to Hoysaḷas','Agastyeśvara and the temples around it gather work of the Gaṅgas, Cōḻas and Hoysaḷas.'),
 ('16th c.','Vijayanagara: the Guñja Narasiṃha temple, with records of Kṛṣṇadevarāya’s time.'),
 ('Mysuru','The Daḷavāys and kings of Mysuru support the temples; Mādhva maṭhas, including the Vyāsarāja maṭha at Sosale, flourish nearby.'),
 ('1989','The first T. Narasipura Kumbha Mela.')])
 +'<div class="panel reading"><p><b>Sons of the soil.</b> The great Mādhva saint <b>Vyāsatīrtha</b>, guru of Purandara Dāsa, was born in this taluk, and the violinist <b>T. Chowdiah</b> was born in the town.</p></div>'))
pages.append(page('around','AROUND T. NARASIPURA','The Kāverī temple circuit',facts([
 ('Bhikṣeśvara, Mūlasthāneśvara, Ānandeśvara','Old temples around the town with Gaṅga-to-Vijayanagara work'),
 ('Sosale','The Vyāsarāja maṭha'),
 ('Mudukutore','Mallikārjuna on Somagiri, the new Śrīśaila'),
 ('Talakāḍu','The buried Gaṅga capital and its Pañcaliṅgas'),
 ('Somanāthapura','The Hoysaḷa Keśava temple of 1268')])
 +'''<div class="panel reading"><p>The Kapilā that meets the Kāverī here flows past <a href="/bhakti/temples-of-india/around-mysuru/nanjangud/">Nañjanagūḍu</a> upstream. More: <a href="/bhakti/temples-of-india/around-mysuru/mudukutore/">Mudukutore</a> · <a href="/bhakti/temples-of-india/around-mysuru/talakadu/">Talakāḍu</a>.</p></div>'''))
glossary=[('Tirumakūḍalu','sacred meeting of three (rivers)'),('Trimakūṭa kṣetra','a holy place where three waters meet'),('Sphaṭika Sarovara','the crystal lake, the hidden third river'),('Saikata liṅga','a liṅga of sand'),('Nābhi','navel; the overflow opening of the liṅga'),('Tīrtha','holy water, a holy bathing place'),('Guñja','the red-and-black seed of <i>Abrus precatorius</i>, gulaganji in Kannada'),('Dakṣiṇa Kāśī','Kāśī of the South'),('Prayāga','the triple confluence at Prayāgarāj'),('Kumbha Mela','a great bathing festival'),('Daḷavāy','commander-in-chief of the Mysuru kingdom'),('Neolithic','the New Stone Age')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','T. NARASIPURA ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The place.</b> The holy meeting of the Kāverī, the Kapilā and the hidden Sphaṭika Sarovara: Dakṣiṇa Kāśī and South India’s Prayāga.</div>
<div><b>Śiva.</b> Agastyeśvara, the sand liṅga Agastya made when Hanumān was late, with Gaṅgā water ever in its top.</div>
<div><b>Viṣṇu.</b> Guñja Narasiṃha, found under a washerman’s stone, holier than Kāśī by one guñja seed.</div>
<div><b>The history.</b> A Neolithic village; Gaṅga to Vijayanagara temples; Kṛṣṇadevarāya’s records.</div>
<div><b>The festival.</b> The Kumbha Mela every three years since 1989.</div>
</div>'''+talk("One line to remember?","Three rivers, a sand liṅga, and a seed that outweighs Kāśī. Not bad for a small town!")+'<div class="key">Where three waters meet: <b>Kāśī of the South, plus one seed</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Town:</b> Wikipedia, “Tirumakudalu Narasipura”: trimakūṭa kṣetra (Skanda Purāṇa); Kāverī, Kabini and Sphaṭika Sarovara; Guñja Narasiṃha (Vijayanagara, Kṛṣṇadevarāya inscriptions, Nāgarī records); Agastyeśvara older, with Gaṅga, Cōḻa, Hoysaḷa and Vijayanagara work; Bhikṣeśvara, Mūlasthāneśvara, Ānandeśvara; Kumbha Mela every three years since 1989; the Neolithic excavations (1959–65; M. Seshadri, 1971); Vyāsatīrtha and T. Chowdiah. Wikipedia, “Gunja Narasimha Swamy Temple”: 16th century; Daḷavāy patronage (B. Lewis Rice); the guñja tree and berry; gopura, maṇḍapa, prākāra; ASI protection.</p>
<p><b>Legends:</b> devotee and temple-information accounts (TNP Legends &amp; History; Hare Krsna SUN; Indianetzone; Yesveesbi): Agastya, Hanumān and the sand liṅga; the water and the nābhi; the Hanumān liṅga; the washerman’s dream and the guñja seed; the name. Trawell: the local Pañcaliṅga.</p>
<p><b>Not verified:</b> the local Pañcaliṅga list; the 450-year figure. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('name','The Name'),('agastya','Legend · Agastyeśvara'),('agastyesvara','Agastyeśvara Temple'),('gunja','Legend · Guñja Narasiṃha'),('narasimha','Guñja Narasiṃha Temple'),('kumbha','The Kumbha Mela'),('history','History'),('around','Around T. Narasipura'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,6vw,66px)">TIRUMAKŪḌALU NARASIPURA</h1>
  <div class="series">AGASTYEŚVARA · GUÑJA NARASIṂHA · A REFERENCE GUIDE</div>
  <div class="tag">Where three waters meet</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>South-east of Mysuru, the Kapilā runs into the Kāverī, and tradition says a third, hidden river rises to meet them. This is <b>Tirumakūḍalu</b>, the sacred meeting of three.</p>
    <p>On one bank Śiva sits as a liṅga of sand that a sage made in a hurry; on the other Narasiṃha holds a tiny red seed that makes this place, they say, just a little holier than Kāśī.</p>
    <p>This guide tells the stories of the rivers, the temples and the Kumbha Mela.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Hari Hara,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Holier than Kāśī? That's a big claim!","By exactly one seed. The people here are very precise about it!")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/T_Narasipura.html','w').write(head+b+tail())
print('ok')
