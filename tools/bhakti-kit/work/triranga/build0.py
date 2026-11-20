import sys; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
head=make_head('Triraṅga Darśanam · Three Raṅganāthas on the Kāverī · srini.presents',
 'Triraṅga Darśanam: the three Raṅganātha temples on the islands of the Kāverī, Ādi Raṅga at Śrīraṅgapaṭṭaṇa, Madhya Raṅga at Śivanasamudra and Antya Raṅga at Śrīraṅgam, and the tradition of seeing all three in one day in Dhanurmāsa. An illustrated reference guide.')
RIVER_PATH='M30 120 Q100 150 170 132 T320 104 T450 140 T560 146 T690 120'
def island(cx,cy,rx=34,ry=14): return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#dfeccf" stroke="#111" stroke-width="2"/>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The river Kaveri winding from west to east at dawn, with three islands, each holding a small reclining Ranganatha, labelled Adi, Madhya and Antya">'
 '<rect width="380" height="268" fill="#14315a" rx="8"/><rect y="150" width="380" height="118" fill="#2a5a3a"/>'+SUN(340,60,24)
 +'<path d="M0 200 C 70 170, 120 230, 190 200 S 300 170, 380 200" fill="none" stroke="#4aa3df" stroke-width="40"/>'
 +''.join(island(x,y,40,16)+RANGA(x,y-6,.42) for x,y in [(60,192),(190,200),(318,190)])
 +T(60,240,'ĀDI',16,'#ffd60a')+T(190,246,'MADHYA',16,'#ffd60a')+T(318,236,'ANTYA',16,'#ffd60a')+'</svg>')
mapfig=fig(720,250,'Schematic map of the Kaveri flowing west to east from Talakaveri in Kodagu to the Bay of Bengal, with three river islands marked: Srirangapatna (Adi Ranga) and Shivanasamudra (Madhya Ranga) in Karnataka, and Srirangam (Antya Ranga) in Tamil Nadu. Not to scale.',
 '<rect width="720" height="250" fill="#eef3fa"/><rect x="0" y="0" width="380" height="250" fill="#f6f1e2"/><rect x="380" y="0" width="340" height="250" fill="#eef6ee"/><path d="M380 0 V250" stroke="#888" stroke-width="2" stroke-dasharray="6 5"/>'
 +T(190,26,'KARNATAKA',14,'#555')+T(550,26,'TAMIL NADU',14,'#555')
 +f'<path d="{RIVER_PATH}" fill="none" stroke="#4aa3df" stroke-width="12" stroke-linecap="round"/>'
 +'<path d="M30 70 l14 -24 l14 24z" fill="#2a7a4a" stroke="#111" stroke-width="2"/>'+T(44,96,'Talakāveri',11)+T(44,108,'(source, Kodagu)',9,'#555')
 +'<path d="M690 120 h22" stroke="#4aa3df" stroke-width="12"/>'+T(700,100,'Bay of Bengal',11,'#111','end')
 +island(170,132)+RANGA(170,126,.3)+T(170,168,'ŚRĪRAṄGAPAṬṬAṆA',11,'#0d3f73')+T(170,182,'Ādi Raṅga',11,'#c0392b')
 +island(320,104)+RANGA(320,98,.3,youth=True)+T(320,74,'ŚIVANASAMUDRA',11,'#0d3f73')+T(320,62,'Madhya Raṅga',11,'#c0392b')
 +'<path d="M296 118 l-6 14 M346 118 l6 14" stroke="#fff" stroke-width="3"/>'
 +island(560,146,40,16)+RANGA(560,140,.32)+T(560,184,'ŚRĪRAṄGAM',11,'#0d3f73')+T(560,198,'Antya Raṅga',11,'#c0392b')
 +T(360,236,'Upstream (west) → downstream (east) · simplified, not to scale',10,'#555'))
glance=('<table class="ct"><tr><th></th><th>Ādi Raṅga</th><th>Madhya Raṅga</th><th>Antya Raṅga</th></tr>'
 '<tr><td><b>Place</b></td><td>Śrīraṅgapaṭṭaṇa</td><td>Śivanasamudra</td><td>Śrīraṅgam</td></tr>'
 '<tr><td><b>Region</b></td><td>Mandya district, Karnataka</td><td>Chamarajanagar district (Kollegāl taluk), Karnataka</td><td>Tiruchirappalli, Tamil Nadu</td></tr>'
 '<tr><td><b>Deity</b></td><td>Raṅganātha on the seven-hooded Ādiśeṣa, Lakṣmī at his feet</td><td>Jaganmohana Raṅga, the Lord in his <b>youthful</b> form</td><td>Raṅganātha (Periya Perumāḷ), facing south</td></tr>'
 '<tr><td><b>Oldest record</b></td><td>Inscription of <b>894 CE</b> (a Western Gaṅga chief)</td><td>Called ancient; no founding date recorded</td><td>Early Cōḻa origins; Pāṇḍya to Nāyaka additions</td></tr>'
 '<tr><td><b>Known for</b></td><td>Hoysaḷa and Vijayanagara work; tied to Rāmānuja</td><td>An island between the Gaganacukki and Bharacukki falls</td><td>First of the 108 Divya Deśams; 7 enclosures, 21 gopurams</td></tr></table>')
pages=[]
pages.append(page('glance','AT A GLANCE','Three temples, one river, one Lord',glance+talk("Three temples, all called Raṅganātha?","Yes! One Lord, resting on the same river at three places. 'Ādi', 'Madhya' and 'Antya' just mean first, middle and last, counting downstream.")))
pages.append(page('where','WHERE THEY ARE','Three islands on the Kāverī',mapfig+'''<div class="panel reading">
<p>The <b>Kāverī</b> rises at <b>Talakāveri</b> in the hills of Kodagu and flows east across Karnataka and Tamil Nadu to the Bay of Bengal.</p>
<p>At three places on its way, the river splits and joins again, wrapping an <b>island</b> in its arms. On each island stands a temple of Raṅganātha. Counting downstream, they are the <b>first</b> (Ādi), <b>middle</b> (Madhya) and <b>last</b> (Antya) Raṅga.</p>
<p>Two of the three are in Karnataka; the last, and largest, is in Tamil Nadu, where Śrīraṅgam island lies between the Kāverī and its branch, the Koḷḷiḍam.</p>
</div>'''))
ranga_fig=fig(560,200,'Vishnu as Ranganatha, reclining on the coiled serpent Adisesha whose seven hoods shade his head, with Lakshmi seated at his feet','<rect width="560" height="200" fill="#dcecff"/>'+RANGA(280,130,2.2)+T(120,40,'ĀDIŚEṢA',13,'#2a7a4a')+T(450,170,'LAKṢMĪ AT HIS FEET',12,'#c0392b')+T(280,30,'RAṄGANĀTHA',16,'#0d3f73'))
pages.append(page('ranga','WHO IS RAṄGANĀTHA?','Viṣṇu, at rest on the cosmic serpent',ranga_fig+'''<div class="g2">
<div class="card bg-blue"><h4>🛏 The posture</h4><p>Viṣṇu <b>reclines</b> on the coils of the serpent <b>Ādiśeṣa</b>, whose hoods shade his head. This form is called <i>anantaśayana</i>, “resting on Ananta”.</p></div>
<div class="card bg-yellow"><h4>🏛 The name</h4><p><i>Raṅga</i> means a stage or hall; <b>Raṅganātha</b> is “Lord of the Raṅga”. His island homes are each named Śrīraṅga: Śrīraṅgam, Śrīraṅgapaṭṭaṇa.</p></div>
</div>
<div class="panel reading"><p><b>Asleep, yet awake.</b> The reclining Lord is in <i>yoganidrā</i>, the sleep of yoga, holding the world in his rest. It is the same scene that opens the Devī Māhātmya’s first battle: <a href="/bhakti/devi/devi-mahatmya/part-6/">Viṣṇu asleep on Śeṣa on the cosmic ocean</a>.</p></div>'''))
story=fig(560,210,'Three panels: the river goddess Kaveri flowing with folded hands toward the reclining Vishnu; Vibhishana carrying the Ranganatha image which stops on the island of Srirangam; Indra praying at Shivanasamudra',
 ''.join(f'<rect x="{6+184*i}" y="6" width="178" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{95+184*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#dcecff','THE RIVER’S WISH'),('#ffe3c4','VIBHĪṢAṆA’S BURDEN'),('#ddf5ea','INDRA’S PENANCE')]))
 +'<path d="M10 140 q80 -20 170 0" fill="none" stroke="#4aa3df" stroke-width="14"/>'+person(60,120,'#4aa3df','#c98b5a',.9)+RANGA(130,110,.45)
 +person(250,150,'#7a3fa0','#c98b5a',1)+'<rect x="268" y="96" width="40" height="30" fill="#e0a800" stroke="#111" stroke-width="2"/>'+RANGA(288,92,.18)+'<path d="M300 160 h70" stroke="#4aa3df" stroke-width="8"/>'
 +person(470,150,'#ffd60a','#c98b5a',1)+'<path d="M450 40 l10 20 l-10 0 l10 20" stroke="#ffd60a" stroke-width="3" fill="none"/>'+RANGA(470,70,.35,youth=True),'#fff')
pages.append(page('story','THE STORIES','Why the Lord rests on these islands',story+'''<div class="steps">
<div><b>Many tellings.</b> Each temple has its own legends, and tellings differ from place to place. These are the best-known ones, given as tradition.</div>
<div><b>The river’s wish.</b> One popular telling links all three to the Kāverī herself: born to serve humanity, she longed to keep Viṣṇu close, and so at three places she wraps her arms around an island where he rests. At Śrīraṅgam, tradition also says the river goddess asked Raṅganātha to stay.</div>
<div><b>Vibhīṣaṇa’s burden.</b> Śrīraṅgam’s famous legend: the image was given by Rāma to Vibhīṣaṇa to carry to Laṅkā; it would not move past this island, so it stayed, and the Lord faces south, towards Laṅkā, to console him.</div>
<div><b>Indra’s penance.</b> At Madhya Raṅga, temple tradition tells of Indra, burdened by the sin of slaying the demon Vṛtra, finding release through Raṅganātha’s grace.</div>
<div><b>Ādi Raṅga.</b> At Śrīraṅgapaṭṭaṇa, the island town itself is named after the temple, the first Raṅga on the river.</div>
</div>'''))
def tpage(id_,title,sub,figure,rows,tk,note=''):
    n=f'<div class="note">{note}</div>' if note else ''
    return page(id_,title,sub,figure+facts(rows)+talk(*tk)+n)
pages.append(tpage('adi','ĀDI RAṄGA · ŚRĪRAṄGAPAṬṬAṆA','The first Raṅga, upstream',
 fig(560,170,'The Srirangapatna temple with a Vijayanagara-style gopuram on an island in the Kaveri, the reclining Ranganatha inside','<rect width="560" height="170" fill="#4aa3df"/>'+island(280,120,220,40)+'<path d="M140 120 v-60 h40 v60z M136 60 l24 -40 l24 40z" fill="#e2cfa8" stroke="#111" stroke-width="2"/><rect x="220" y="80" width="200" height="40" fill="#f6f1e2" stroke="#111" stroke-width="2"/>'+RANGA(330,104,.55)+T(160,150,'GOPURAM',11)),
 [('Deity','Raṅganātha reclining on Ādiśeṣa, whose <b>seven hoods</b> form a canopy; Lakṣmī at his feet, Śrīdevī, Bhūdevī and Brahmā beside him'),
  ('Founded','An inscription records the temple built in <b>894 CE</b> by Tirumalaiah, a chief under the <b>Western Gaṅga</b> dynasty; an earlier shrine may have stood here'),
  ('Hoysaḷas','King <b>Viṣṇuvardhana</b> (r. 1108–1152) granted the village to <b>Rāmānuja</b> as a seat of learning; Vīra Ballāḷa II’s inscription of 1210 records additions'),
  ('Later','The entrance gopuram is in the Vijayanagara style; the Woḍeyars of Mysore also contributed'),
  ('Shrines','Narasiṃha, Gopālakṛṣṇa, Śrīnivāsa, Hanumān, Garuḍa and the Āḻvārs'),
  ('Status','Protected by the Archaeological Survey of India as a monument of national importance')],
 ("Rāmānuja lived here?","The Hoysaḷa king gave him this village as a seat of learning. The great Śrīvaiṣṇava teacher links Ādi Raṅga and Antya Raṅga, where he spent his last years.")))
pages.append(tpage('madhya','MADHYA RAṄGA · ŚIVANASAMUDRA','The middle Raṅga, between the waterfalls',
 fig(560,170,'The Shivanasamudra temple on a river island with waterfalls on either side, the youthful Ranganatha inside','<rect width="560" height="170" fill="#4aa3df"/>'+island(280,110,170,40)+'<path d="M60 20 v130 M80 20 v130 M480 20 v130 M500 20 v130" stroke="#fff" stroke-width="6" stroke-dasharray="10 6"/>'+'<rect x="200" y="74" width="160" height="40" fill="#f6f1e2" stroke="#111" stroke-width="2"/>'+RANGA(285,98,.5,youth=True)+T(70,14,'GAGANACUKKI',10,'#fff')+T(490,14,'BHARACUKKI',10,'#fff')),
 [('Deity','Raṅganātha as <b>Jaganmohana</b> or <b>Mohana Raṅga</b>, “enchanter of the world”: of the three, the Lord in his <b>youthful</b> form'),
  ('Setting','An island of the Kāverī at Śivanasamudra, between the twin waterfalls <b>Gaganacukki</b> and <b>Bharacukki</b>'),
  ('Temple','Built in the <b>Drāviḍa</b> style; described as ancient, with no founding date on record; renovation began in 2021'),
  ('Legend','Temple tradition links the shrine to <b>Indra</b>’s release from the sin of slaying Vṛtra'),
  ('Nearby','The <b>Someśvara</b> temple, where tradition says Ādi Śaṅkara installed a Śrī Cakra, and a Vanadurgā temple')],
 ("Why is this one the 'young' Raṅganātha?","That's how devotees see him here: Jaganmohana, the charming youth. The first Raṅga, the young Raṅga, the great Raṅga: one Lord, three moods."),
 'Some local traditions place Madhya Raṅga at Sathyagāla, a village nearby on the Kāverī; Śivanasamudra is the usual identification.'))
pages.append(tpage('antya','ANTYA RAṄGA · ŚRĪRAṄGAM','The last Raṅga, and the greatest',
 fig(560,170,'The vast Srirangam temple seen from above as seven nested rectangles, with the tall Rajagopuram at the south entrance','<rect width="560" height="170" fill="#4aa3df"/>'+island(280,85,250,70)+''.join(f'<rect x="{140+k*12}" y="{30+k*7}" width="{280-k*24}" height="{110-k*14}" fill="none" stroke="#7a5a2a" stroke-width="2"/>' for k in range(7))+'<rect x="268" y="64" width="24" height="40" fill="#e0a800" stroke="#111"/><path d="M272 140 h16 l-2 -24 h-12z" fill="#e2cfa8" stroke="#111" stroke-width="2"/>'+T(280,162,'RĀJAGOPURAM',10)),
 [('Deity','Raṅganātha, <b>Periya Perumāḷ</b>, reclining on Ādiśeṣa and facing south; the Goddess as Raṅganāyakī'),
  ('Size','About <b>63 hectares</b> (155 acres) inside <b>seven</b> concentric enclosures, with <b>21</b> gopurams; often called one of the largest functioning Hindu temples'),
  ('Rājagopuram','About <b>73 m</b> high, 13 tiers; begun around 1500, completed and consecrated in <b>1987</b>'),
  ('Divya Deśam','Foremost of the <b>108</b>; the only one praised by all twelve Āḻvārs, in 247 hymns. Āṇḍāḷ, poet of the Tiruppāvai, is said to have merged into this Lord'),
  ('History','Cōḻa, Pāṇḍya, Hoysaḷa, Vijayanagara and Nāyaka patronage; raided in 1310–11 and 1323–27, the image was carried away for safety and reinstated in <b>1371</b>'),
  ('Rāmānuja','The teacher (1017–1137) lived and taught here; his preserved body is enshrined in the temple')],
 ("Seven walls?","Seven, one inside the other, like the layers of a mandala, with a whole town living within them. And at the centre, the Lord resting.")))
pages.append(page('why','ONE DAY, IN DHANURMĀSA','The tradition behind the journey','''<div class="g2">
<div class="card bg-blue"><h4>🌅 Dawn to dusk</h4><p>Triraṅga Darśanam means seeing all three Raṅganāthas on a <b>single day</b>, between dawn and dusk, following the river from the first to the last.</p></div>
<div class="card bg-yellow"><h4>🪔 In Dhanurmāsa</h4><p>The practice is especially linked with <b>Dhanurmāsa</b> (mid-December to mid-January), the holiest month of Viṣṇu worship, when temples open in the dark before dawn.</p></div>
</div>
<div class="panel reading">
<p><b>A vow, not a race.</b> The one-day journey is understood as a <i>saṅkalpa</i>, a personal vow. Teachers stress the intention behind it rather than speed; the same three temples seen with devotion on different days are no less blessed.</p>
<p><b>First, middle, last.</b> Some explain the order as a picture of a life: beginning, middle and end, or birth, life and liberation, all held in the one Lord.</p>
<p><b>The month of Raṅganātha.</b> Dhanurmāsa is also when Āṇḍāḷ’s <b>Tiruppāvai</b> is sung, a song to the Lord of Śrīraṅgam; and its <b>Vaikuṇṭha Ekādaśī</b> is Śrīraṅgam’s greatest festival, when the <i>Paramapada vāsal</i>, the gate of heaven, is opened.</p>
</div>'''+talk("Do I fail if I miss one?","No! The tradition stresses the vow and the devotion, not a stopwatch. See them with love, in a day or in a lifetime.")))
pancha=('<table class="ct"><tr><th>Raṅga</th><th>Temple and place</th><th>Note</th></tr>'
 '<tr><td><b>Ādi Raṅga</b></td><td>Raṅganātha, Śrīraṅgapaṭṭaṇa, Karnataka</td><td>First upstream</td></tr>'
 '<tr><td><b>Śrīraṅgam</b></td><td>Raṅganātha, Śrīraṅgam, Tamil Nadu</td><td>Divya Deśam</td></tr>'
 '<tr><td><b>Appala Raṅga</b></td><td>Appakkuḍattān Perumāḷ, Kōviladi, Tamil Nadu</td><td>Divya Deśam</td></tr>'
 '<tr><td><b>Sārṅgapāṇi</b></td><td>Sārṅgapāṇi temple, Kumbakōṇam, Tamil Nadu</td><td>Divya Deśam</td></tr>'
 '<tr><td><b>Parimala Raṅga</b></td><td>Parimaḷa Raṅganātha, Indaḷūr (Mayilāḍuturai), Tamil Nadu</td><td>Divya Deśam</td></tr></table>')
pages.append(page('family','THE WIDER FAMILY','The Pañcaraṅga Kṣetras: five Raṅgas on the Kāverī',pancha+'''<div class="panel reading">
<p><b>Three and five.</b> Triraṅga follows the three <i>island</i> temples. A second tradition counts <b>five</b> Raṅganātha temples on the Kāverī, the <b>Pañcaraṅga Kṣetras</b>. Śrīraṅgapaṭṭaṇa and Śrīraṅgam belong to both; Madhya Raṅga is usually counted only in the three.</p>
<p><b>Lists vary.</b> Some lists name other temples for the fifth place, such as the Vaṭaraṅga at Sīrkāḻi or the Raṅganātha temple at Nellore.</p>
<p><b>Other reclining Viṣṇus.</b> The same resting form is worshipped across the South, most famously as <b>Padmanābhasvāmi</b> in Thiruvananthapuram.</p>
</div>'''))
glossary=[('Raṅganātha','“Lord of the Raṅga”; Viṣṇu reclining on Ādiśeṣa'),('Ādi · Madhya · Antya','first · middle · last'),('Triraṅga Darśanam','seeing the three Raṅgas, traditionally in one day'),('Darśana','seeing the deity, and being seen'),('Ādiśeṣa / Ananta','the cosmic serpent on whom Viṣṇu rests'),('Yoganidrā','the yogic sleep of Viṣṇu'),('Dhanurmāsa','the solar month of Dhanus, mid-Dec to mid-Jan; Mārgaḻi in Tamil'),('Saṅkalpa','a formal vow or resolve'),('Divya Deśam','one of 108 Viṣṇu temples sung by the Āḻvārs'),('Āḻvārs','the twelve Tamil poet-saints of Viṣṇu'),('Prākāra','an enclosing wall and courtyard around a shrine'),('Gopuram','a temple gateway tower'),('Pañcaraṅga Kṣetras','the five Raṅganātha temples on the Kāverī'),('Śrīvaiṣṇava','the tradition of Viṣṇu and Lakṣmī taught by Rāmānuja')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','TRIRAṄGA ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>Three islands.</b> The Kāverī wraps three islands on its way east; on each rests Raṅganātha, Viṣṇu on Ādiśeṣa.</div>
<div><b>Ādi Raṅga.</b> Śrīraṅgapaṭṭaṇa, Karnataka: the first, recorded from 894 CE, linked to the Hoysaḷas and Rāmānuja.</div>
<div><b>Madhya Raṅga.</b> Śivanasamudra, Karnataka: the youthful Jaganmohana Raṅga, between two great waterfalls.</div>
<div><b>Antya Raṅga.</b> Śrīraṅgam, Tamil Nadu: first of the 108 Divya Deśams, seven walls, twenty-one gopurams.</div>
<div><b>The vow.</b> All three in one day, especially in Dhanurmāsa: a saṅkalpa of devotion, first to last.</div>
</div>'''+talk("What's in the next three guides?","One full guide for each Raṅga: legends, history, the temple and its festivals, in the same style as our Jyotirliṅga guides.")+'<div class="key">One river, one Lord, <b>three resting places</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Ādi Raṅga:</b> Wikipedia, “Ranganathaswamy Temple, Srirangapatna”, and the sources it cites (894 CE inscription of Tirumalaiah; Viṣṇuvardhana’s grant to Rāmānuja; Vīra Ballāḷa II, 1210; George Michell on Woḍeyar contributions; ASI protection).</p>
<p><b>Madhya Raṅga:</b> Wikipedia, “Ranganathaswamy Temple, Shivanasamudra” (location, Drāviḍa style, the youthful Jaganmohana form, the Someśvara temple); Tirthayatra.org and Deccan Herald for temple traditions (Indra legend); prtraveller blog for the Sathyagāla tradition.</p>
<p><b>Antya Raṅga:</b> Wikipedia, “Ranganathaswamy Temple, Srirangam” (63 ha; seven prākāras; 21 gopurams; Rājagopuram consecrated 25 March 1987; 247 Āḻvār hymns; raids of 1310–11 and 1323–27; reinstatement in 1371; Rāmānuja; Vibhīṣaṇa legend).</p>
<p><b>Triraṅga and Dhanurmāsa:</b> Deccan Herald, “The Triranga Yatra is thrice as nice”; Dharma Renaissance’s Triraṅga guide (the vow as saṅkalpa); Outlook Traveller on the Kāverī legend; Wikipedia, “Pancharanga Kshetrams”, for the five temples and variant lists.</p>
<p><b>Not verified:</b> founding dates for Madhya Raṅga; the details of the Indra legend, which vary by source; the symbolic readings of first, middle and last, which are interpretations.</p>
<p>Maps and diagrams are simplified illustrations, not to scale. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where They Are'),('ranga','Who Is Raṅganātha?'),('story','The Stories'),('adi','Ādi Raṅga'),('madhya','Madhya Raṅga'),('antya','Antya Raṅga'),('why','One Day, in Dhanurmāsa'),('family','The Wider Family'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">THREE TEMPLES · ONE DAY</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">TRIRAṄGA DARŚANAM</h1>
  <div class="series">THREE RAṄGANĀTHAS ON THE KĀVERĪ · A REFERENCE GUIDE</div>
  <div class="tag">Ādi Raṅga · Madhya Raṅga · Antya Raṅga</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>The Kāverī rises in the hills of Kodagu and runs east to the sea. Three times on the way she parts and joins again, holding an island in her arms, and on each island Viṣṇu lies at rest as <b>Raṅganātha</b>.</p>
    <p>To see all three in a single day, from the first to the last, is the <b>Triraṅga Darśanam</b>, a vow especially loved in the month of Dhanurmāsa. Two of the temples are in Karnataka; the third, Śrīraṅgam, is among the greatest temples in the world.</p>
    <p>This guide introduces all three. A full guide to each follows.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why does Viṣṇu keep lying down by rivers?","Resting on Ādiśeṣa is how he holds the world: still, watchful, at peace. Where the river makes an island, devotees see the cosmic ocean in small.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/triranga/Triranga_Darshanam.html','w').write(head+b+tail())
print('ok')
