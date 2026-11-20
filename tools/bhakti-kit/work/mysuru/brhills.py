import sys; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
head=make_head('Biḷigiri Raṅgana Beṭṭa · Temples around Mysuru · srini.presents',
 'Biḷigiri Raṅgana Beṭṭa (BR Hills): the Lord of the white hill, Dakṣiṇa Tirupati, who married the Soliga girl Kusumāle. The giant sandals, Vasiṣṭha’s penance, Doḍḍa Sampige and the tiger reserve. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def HILL(x,y,w,h,c='#3a6a3a',cliff=False):
    s=f'<path d="M{x-w/2} {y} Q{x-w/4} {y-h*0.6} {x-w/10} {y-h} Q{x} {y-h*1.06} {x+w/10} {y-h} Q{x+w/4} {y-h*0.6} {x+w/2} {y}z" fill="{c}" stroke="#111" stroke-width="2"/>'
    if cliff: s+=f'<path d="M{x+w/14} {y-h*1.02} Q{x+w/5} {y-h*0.7} {x+w/7} {y-h*0.35} L{x-w/30} {y-h*0.5}z" fill="#f4f1e6" stroke="#111" stroke-width="1.6"/>'
    return s
def TEMPLE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="#f2e6c8"/><path d="M-10 -16 l10 -20 l10 20z" fill="#e2cfa8"/><circle cy="-38" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def LORD(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-20 70 h40 l-4 -60 h-32z" fill="#ffd60a"/><path d="M-16 10 q16 -14 32 0 v-30 q-16 -10 -32 0z" fill="#2b2b3a"/>'
     '<path d="M-16 -14 l-16 -22 M16 -14 l16 -22" stroke="#2b2b3a" stroke-width="7"/><circle cx="-34" cy="-40" r="7" fill="#fff"/><circle cx="34" cy="-40" r="8" fill="#ffd60a"/>'
     '<circle cy="-34" r="12" fill="#2b2b3a"/><path d="M-12 -46 h24 l-4 -22 h-16z" fill="#e0a800"/><path d="M-6 -36 h12" stroke="#fff" stroke-width="3"/>'
     '<path d="M-16 -4 q16 12 32 0" fill="none" stroke="#c0392b" stroke-width="4"/></g>')
def GIRL(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cy="-36" r="12" fill="#8a5a3a"/><path d="M-12 -40 q12 -16 24 0 q-2 14 -2 30" fill="#2b1a0e"/><path d="M-20 40 q20 -76 40 0z" fill="#e0a800"/><circle cx="-8" cy="-48" r="4" fill="#e05a8a"/><circle cx="0" cy="-50" r="4" fill="#fff"/></g>'
def SANDAL(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 0 q-6 -60 14 -70 q20 10 16 70z" fill="#8a5a2a"/><path d="M8 0 q-6 -60 14 -70 q20 10 16 70z" fill="#8a5a2a"/><path d="M-22 -40 q8 -6 16 0 M16 -40 q8 -6 16 0" stroke="#e0a800" stroke-width="3" fill="none"/></g>'
def TREE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-10" y="-70" width="20" height="70" fill="#6a4a2a"/><circle cy="-100" r="50" fill="#3a8a3a"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="4" fill="#ffd166"/>' for a,b in ((-24,-110),(10,-128),(28,-96),(-8,-84),(16,-70)))+'</g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A forested hill with a white rock cliff and a small temple on top; the Lord stands above with a giant pair of sandals beside him">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/><circle cx="310" cy="54" r="40" fill="#ffd166" opacity=".3"/>'
 +HILL(150,268,300,170,cliff=True)+TEMPLE(150,104,1.3)+LORD(300,140,1.2)+SANDAL(300,250,.6)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','Viṣṇu as <b>Biḷigiri Raṅganātha</b>, a <b>standing</b> form, once called <b>Tiru Veṅkaṭanātha</b>; the temple faces <b>east</b>'),
 ('Goddess','<b>Raṅganāyakī</b>, in her own shrine; in folk tradition also <b>Kusumāle</b>, the Soliga bride'),
 ('Place','The summit above the white cliff of <b>Biḷigiri</b>, Yelandur taluk, Chamarajanagar district, Karnataka'),
 ('Name','<b>Biḷigiri</b>, “white hill” (Sanskrit <b>Śvetādri</b>), for its pale rock face or its white mist'),
 ('Titles','<b>Dakṣiṇa Tirupati</b>, “the southern Tirupati”, in the Brahmāṇḍa Purāṇa telling'),
 ('Sage','<b>Vasiṣṭha</b> did penance here'),
 ('People','The <b>Soligas</b> of the forest call the Lord <b>bhāva</b>, brother-in-law'),
 ('Wonder','A giant pair of <b>sandals</b> that wear out and are replaced'),
 ('Oldest record','A <b>1667</b> copper plate of Mudduraju of Hadinadu'),
 ('Forest','<b>BRT Tiger Reserve</b> (2011), where the Eastern and Western Ghats meet')])
 +talk("God's brother-in-law? How does that work?","When the Lord marries your sister, you get family rights! The Soligas have had them for generations.")))
mapfig=fig(560,240,'Schematic map: the Biligiri Rangana hills forming a bridge between the Western Ghats on the west and the Eastern Ghats on the east, with the temple on the white cliff and Yelandur and Chamarajanagar below. Not to scale.',
 '<rect width="560" height="240" fill="#eef6e4"/><path d="M0 200 C 40 120, 60 60, 80 0" stroke="#2e6a2e" stroke-width="40" fill="none" opacity=".35"/><path d="M560 200 C 520 140, 500 80, 480 0" stroke="#2e6a2e" stroke-width="40" fill="none" opacity=".35"/>'
 +'<path d="M70 110 C 200 70, 360 70, 490 110" stroke="#3a6a3a" stroke-width="54" fill="none" opacity=".55"/>'+HILL(280,128,150,80,cliff=True)+TEMPLE(280,52,.6)
 +T(40,230,'WESTERN GHATS',10,'#2e6a2e','start')+T(520,230,'EASTERN GHATS',10,'#2e6a2e','end')+T(280,150,'BIḶIGIRI · TEMPLE',11,'#0d3f73')
 +'<circle cx="200" cy="196" r="6" fill="#e0a800" stroke="#111"/>'+T(212,200,'YELANDUR',10,'#0d3f73','start')+'<circle cx="120" cy="180" r="6" fill="#e0a800" stroke="#111"/>'+T(130,174,'CHAMARAJANAGAR',9,'#0d3f73','start')
 +'<circle cx="400" cy="96" r="5" fill="#fff" stroke="#111"/>'+T(410,86,'KAṬṬARI BEṬṬA (highest)',9,'#555','start')+T(470,16,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','A bridge between two mountain ranges',mapfig+'''<div class="panel reading">
<p><b>The hills.</b> The Biḷigiri Raṅgana hills rise in Chamarajanagar district, south-east of Mysuru. They form a <b>bridge</b> between the Western Ghats and the Eastern Ghats, so animals and plants of both ranges meet here.</p>
<p><b>The cliff.</b> The temple stands on the hill above a pale granite cliff: the “white hill” that gives the place its name. The highest peak of the range, Kaṭṭari Beṭṭa, is about 1,800 m.</p>
<p><b>The forest.</b> All around is the <b>Biḷigiri Raṅganātha Svāmi Temple Wildlife Sanctuary</b>, now the BRT Tiger Reserve: named after the temple itself.</p>
</div>'''))
deity=fig(560,220,'The standing Lord of the white hill with conch and discus, his consort Ranganayaki in her shrine, and images of Ramanuja beside',
 '<rect width="560" height="220" fill="#dcecff"/><rect x="150" y="186" width="200" height="14" fill="#c9a26b" stroke="#111"/>'+LORD(250,130,1.4)
 +'<g transform="translate(440 160)" stroke="#111" stroke-width="2"><circle cy="-34" r="12" fill="#f2c79b"/><path d="M-10 -46 h20 l-3 -12 h-14z" fill="#ffd60a"/><path d="M-22 50 q22 -80 44 0z" fill="#e05a8a"/></g>'
 +person(90,180,'#ff8c1a','#f2c79b',.8)+T(250,214,'BIḶIGIRI RAṄGANĀTHA',12,'#0d3f73')+T(440,214,'RAṄGANĀYAKĪ',11,'#c0392b')+T(90,214,'RĀMĀNUJA',10))
pages.append(page('deity','THE LORD OF THE WHITE HILL','Raṅganātha who stands',deity+'''<div class="g2">
<div class="card bg-blue"><h4>🧍 Standing, not reclining</h4><p>Unlike the Raṅgas of the Kāverī, who recline on Ādiśeṣa, the Lord here <b>stands</b>, like Veṅkaṭeśvara of Tirumala. The oldest record names him <b>Tiru Veṅkaṭanātha</b>.</p></div>
<div class="card bg-yellow"><h4>🛕 The shrine</h4><p>An east-facing Dravidian temple. <b>Raṅganāyakī</b> has her own shrine; there are images of <b>Rāmānuja</b> and other teachers, and pillars carved with Sarasvatī, Kṛṣṇa and Āñjaneya.</p></div>
</div>'''+talk("Then why is he called Raṅganātha?","There's a story: the name changed after a famous visitor. Turn the page!")))
pages.append(page('names','WHITE HILL, MANY NAMES','Biḷigiri, Śvetādri, Bilikal',facts([
 ('Biḷigiri','Kannada: “white hill”, for the pale cliff, or for the white mist that covers the hills much of the year'),
 ('Śvetādri','The same in Sanskrit: “the white mountain”'),
 ('Bilikal','“White rock”, the name in the 1667 copper plate'),
 ('Tiru Veṅkaṭanātha','The Lord’s name in that record'),
 ('Raṅganātha','Tradition says the name came after <b>Tipu Sultan</b>, visiting on a hunt, described it as a temple of Raṅganātha'),
 ('Dakṣiṇa Tirupati','“The southern Tirupati”, the name in the Brahmāṇḍa Purāṇa telling')])
 +'''<div class="panel reading"><p><b>On screen and in song.</b> The Lord is so loved in Karnataka that a famous song of the 1971 Kannada film <i>Śarapañjara</i> calls out to him by name: “Biḷigiri Raṅgayya”.</p></div>'''))
leg1=fig(560,190,'Sage Vasishtha in penance on the white hill; the Lord appearing to bless him; Rama and Lakshmana arriving through the forest',
 '<rect width="560" height="190" fill="#fff4dc"/>'+HILL(170,190,300,120,'#5a8a4a',cliff=True)+person(150,96,'#ff8c1a','#c98b5a',.9)+'<path d="M132 40 q18 -22 36 0" fill="#fff" stroke="#111"/>'
 +'<g transform="translate(250 40)" stroke="#111" stroke-width="2"><circle r="22" fill="#ffd60a" opacity=".5"/><circle cy="-2" r="9" fill="#2b2b3a"/><path d="M-8 -10 h16 l-3 -9 h-10z" fill="#e0a800"/></g>'
 +person(420,176,'#3b6fd0','#5a7ab0',1)+person(480,176,'#ffd60a','#f2c79b',1)+'<path d="M404 110 l-14 -26" stroke="#7a5a2a" stroke-width="4"/>'
 +T(150,184,'VASIṢṬHA',12,'#0d3f73')+T(450,184,'RĀMA · LAKṢMAṆA',11,'#0d3f73'))
pages.append(page('legends1','THE LEGENDS · I','Vasiṣṭha, and Rāma on the hill',leg1+'''<div class="steps">
<div><b>Vasiṣṭha’s penance.</b> Tradition says the sage <b>Vasiṣṭha</b>, guru of the Sun dynasty, did penance on these hills to the Lord as Veṅkaṭeśvara. The Lord appeared and blessed him.</div>
<div><b>Rāma passes by.</b> Another tradition says <b>Rāma and Lakṣmaṇa</b>, searching for Sītā, came this way and worshipped the Lord of the white hill.</div>
<div><b>Siddappāji shows the way.</b> In Soliga lore, it was their own forest god <b>Siddappāji</b> who showed Viṣṇu this cliff, after the Lord had slain a demon.</div>
</div>'''))
leg2=fig(560,200,'The Lord walking through the forest carrying a small pot, meeting a Soliga girl among the trees; later the two together, with Soliga people celebrating',
 '<rect width="560" height="200" fill="#e8f5e2"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="26" fill="#5a9a4a" stroke="#111" stroke-width="2"/><rect x="{x-4}" y="{y+20}" width="8" height="{150-y}" fill="#6a4a2a"/>' for x,y in ((40,60),(520,50),(300,40)))
 +LORD(170,120,1)+'<ellipse cx="206" cy="100" rx="10" ry="8" fill="#c98b5a" stroke="#111"/>'+GIRL(360,150,1.1)
 +'<path d="M250 70 q30 -26 60 0 q-30 28 -30 28 q0 0 -30 -28z" fill="#e05a8a" stroke="#111" stroke-width="2"/>'
 +T(170,194,'THE LORD',12,'#0d3f73')+T(360,194,'KUSUMĀLE',12,'#c0392b'))
pages.append(page('legends2','THE LEGENDS · II','The Lord who married a Soliga girl',leg2+'''<div class="steps">
<div><b>An errand.</b> The Brahmāṇḍa Purāṇa telling says the Lord set out for <b>Śvetādri</b>, the white mountain, to fetch soap-nut powder for his wife’s oil bath.</div>
<div><b>A meeting.</b> On the way he met a girl of the forest-dwelling <b>Soliga</b> people, fell in love, and stayed. The Soligas name her <b>Kusumāle</b> (also told as Pusumāle), daughter of Bomme Gowda, the first Soliga.</div>
<div><b>Family.</b> Since then the Soligas call the Lord <b>bhāva</b>, “brother-in-law”, and serve in his festivals as family.</div>
<div><b>Two traditions meet.</b> The story ties a forest people’s own lore to the great temple tradition: the Lord of the hill belongs to both.</div>
</div>'''+talk("He went shopping for soap-nut and came back married?","That's how the story goes! And it explains why he never went home: he's still here.")))
pages.append(page('sandals','THE LORD’S SANDALS','Footwear that wears out',fig(560,190,'A giant pair of leather sandals kept in the temple, next to a person for scale; footprints leading off into the forest',
 '<rect width="560" height="190" fill="#f6f1e2"/>'+SANDAL(220,170,1.9)+person(380,176,'#3b6fd0','#c98b5a',.8)
 +''.join(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="4" fill="#8a5a2a" opacity=".5"/>' for x,y in ((450,170),(470,150),(490,166),(510,146),(530,162))))+'''<div class="panel reading">
<p><b>The giant pair.</b> The temple keeps a huge pair of leather sandals, said to be the ones the Lord wears to walk his forest at night.</p>
<p><b>They wear out.</b> Devotees say the sandals become worn even though they are kept enclosed, and they are replaced with new ones.</p>
<p><b>A Soliga gift.</b> The Soligas offer the Lord a new pair of leather sandals, about <b>1 ft 9 in</b> long, once every two years.</p>
<p><b>Golden footprint.</b> Nearby is <b>Honnameṭṭi</b>, a stone said to hold the Lord’s footprint turned to stone.</p>
</div>'''+talk("Who's walking around in them at night?","Nobody has caught him at it. But the soles keep wearing down, and the Soligas keep making new ones!")))
pages.append(page('soligas','THE SOLIGAS AND THEIR LORD','People of the bamboo',facts([
 ('Who','The <b>Soligas</b>, a forest people of these hills, whose lore traces their origin to Kārayya, a son of <b>Male Mahadēśvara</b>'),
 ('Family','The Lord is their <b>bhāva</b>; Kusumāle is their daughter'),
 ('The festival','During the annual festival the deity is carried by <b>four Soliga youths</b>'),
 ('Sandals','A new pair of leather sandals every two years'),
 ('Their own gods','Siddappāji, the forms of Mahadēśvara, the tiger <b>Doḍḍanāyi</b>, and sacred trees and stones across the hills')])
 +fig(560,170,'A giant champak tree with yellow flowers, a sage sitting in meditation at its foot, a stream flowing toward him',
 '<rect width="560" height="170" fill="#eef6e4"/>'+TREE(280,170,1)+person(330,166,'#ff8c1a','#c98b5a',.7)+'<path d="M560 150 C 480 140, 420 160, 350 158" stroke="#4aa3df" stroke-width="8" fill="none"/>'+T(120,40,'DOḌḌA SAMPIGE',12,'#2e6a2e')+T(470,130,'BHĀRGAVĪ',10,'#1d6fb8'))
 +'''<div class="panel reading"><p><b>Doḍḍa Sampige.</b> A giant champak tree in the forest, sacred to the Soligas. The story goes that the sage <b>Paraśurāma</b> received seeds from a bird; one grew into this tree, where he sat in penance, and his mother <b>Reṇukā</b> flowed to him as the river <b>Bhārgavī</b>.</p></div>'''))
pages.append(page('history','HISTORY','From copper plate to tiger reserve',tl([
 ('Legend','Vasiṣṭha’s penance; the Lord marries Kusumāle.'),
 ('1667','A copper plate of <b>Mudduraju</b>, son of Trimalarājanāyaka of <b>Hadinadu</b>, names the Lord Tiru Veṅkaṭanātha of Bilikal; Mudduraju endows the temple with a village.'),
 ('18th c.','<b>Tipu Sultan</b> visits on a hunt and calls it a Raṅganātha temple; the name sticks.'),
 ('c. 1800','Dīvān <b>Pūrṇayya</b> of Mysuru also endows the temple: between them, two villages are given for its service.'),
 ('1974','The hills, temple and all, become the <b>BRT Wildlife Sanctuary</b>; enlarged in 1987.'),
 ('2011','Declared the <b>BRT Tiger Reserve</b>.')])
 +'''<div class="panel reading"><p><b>Hoysaḷa claim.</b> Some accounts credit the Hoysaḷa king Viṣṇuvardhana with the temple. The oldest dated record we found is the copper plate of 1667, so we give that as the earliest firm date.</p></div>'''))
fest=fig(560,170,'Four young men carrying the festival image on a palanquin up the hill, with a crowd following',
 '<rect width="560" height="170" fill="#ffe9c4"/>'+HILL(460,170,240,120,'#5a8a4a',cliff=True)
 +'<rect x="160" y="96" width="140" height="10" fill="#7a5a2a" stroke="#111"/><path d="M200 96 v-30 h60 v30" fill="#ffd60a" stroke="#111" stroke-width="2"/><circle cx="230" cy="78" r="8" fill="#2b2b3a"/>'
 +''.join(person(x,170,'#e8e8e8','#6b4a3a',.7) for x in (170,206,254,290))+crowd(['#fff','#ffd60a','#ff8c1a','#3b6fd0','#e05a8a'],20,26,166,.45))
pages.append(page('festivals','THE ANNUAL FESTIVAL','Carried by Soliga hands',fest+'''<div class="panel reading">
<p><b>Spring festival.</b> The temple’s main festival falls in spring (sources say March or April), with the car festival drawing pilgrims from far and wide.</p>
<p><b>Four youths.</b> The deity is carried by four <b>Soliga</b> young men: the family of the bride carrying the bridegroom.</p>
<p><b>Sandal offering.</b> Every two years the Soligas bring their gift of new leather sandals for the Lord.</p>
</div>'''))
pages.append(page('around','AROUND THE HILLS','The forest and its other shrines',facts([
 ('BRT Tiger Reserve','Tigers, elephants, gaur and more, where two mountain ranges meet'),
 ('Doḍḍa Sampige','The great champak tree of Paraśurāma’s penance'),
 ('Honnameṭṭi','The “golden footprint” stone of the Lord'),
 ('Male Mahadēśvara Beṭṭa','The great Śiva hill to the east, from whose lord the Soligas trace their origin')])
 +'''<div class="panel reading"><p><b>Two forest hills, two forms of Viṣṇu.</b> Gopālasvāmi plays his flute in Bandipur; Biḷigiri Raṅganātha stands on his white cliff in the BRT forest.</p>
<p>More temples around Mysuru: <a href="/bhakti/temples-of-india/around-mysuru/nanjangud/">Nañjanagūḍu</a> and <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga</a>.</p></div>'''))
glossary=[('Biḷigiri','“white hill” (Kannada)'),('Śvetādri','“white mountain” (Sanskrit)'),('Bilikal','“white rock”'),('Beṭṭa','hill'),('Dakṣiṇa Tirupati','“the southern Tirupati”'),('Bhāva','brother-in-law (Kannada)'),('Soliga','a forest people of these hills'),('Kusumāle','the Soliga bride of the Lord'),('Honnameṭṭi','“golden footprint”'),('Sampige','champak tree; <i>doḍḍa</i>, big'),('Bhārgavī','the river of Reṇukā, mother of Paraśurāma'),('Copper plate','a grant engraved on copper sheets'),('Dīvān','chief minister of a princely state'),('BRT','Biḷigiri Raṅganātha Temple (sanctuary and tiger reserve)')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','BR HILLS ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Lord.</b> Biḷigiri Raṅganātha, standing, once Tiru Veṅkaṭanātha, with Raṅganāyakī: Dakṣiṇa Tirupati.</div>
<div><b>The place.</b> A white cliff in the hills that bridge the Western and Eastern Ghats, in the BRT Tiger Reserve.</div>
<div><b>The legends.</b> Vasiṣṭha’s penance; Rāma’s visit; the soap-nut errand and the Soliga bride Kusumāle.</div>
<div><b>The wonders.</b> The giant sandals that wear out; Honnameṭṭi; Doḍḍa Sampige.</div>
<div><b>The history.</b> The copper plate of 1667; Tipu and the name Raṅganātha; Pūrṇayya’s grant; sanctuary in 1974, tiger reserve in 2011.</div>
</div>'''+talk("One line to remember?","The Lord who went out for soap-nut, married into the forest, and still walks it at night in his own sandals.")+'<div class="key">The Lord of the white hill: <b>brother-in-law to the forest</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Hills and sanctuary:</b> Wikipedia, “Biligiriranga Hills”: Kaṭṭari Beṭṭa about 1,800 m; the bridge between the Ghats; Chamarajanagar district; sanctuary 1974, enlarged 1987; tiger reserve 2011; “white hill” and its two explanations; the Soligas’ biennial sandal of 1 ft 9 in; the spring festival.</p>
<p><b>Temple and lore:</b> JLR Explore, “Gods of BR Hills”: Śvetādri; the 1667 copper plate of Mudduraju naming Tiru Veṅkaṭanātha of Bilikal; Tipu and the name Raṅganātha; the sandals; Siddappāji; Bomme Gowda and Pusumāle; four Soliga youths; Doḍḍa Sampige and Paraśurāma; Honnameṭṭi; Doḍḍanāyi. Deccan Herald, “White hills amidst green fields”: the Brahmāṇḍa Purāṇa telling and Dakṣiṇa Tirupati. Hindu Blog and temple-information sites: Kusumāle and <i>bhāva</i>; Vasiṣṭha; Rāma and Lakṣmaṇa; Pūrṇayya’s grant; east-facing; Rāmānuja and the pillar sculptures. Wikipedia, “Soliga people”: Kārayya and Male Mahadēśvara. Mysuru Infra Hub: the 1971 song.</p>
<p><b>Sources differ:</b> Kusumāle or Pusumāle; the festival month (March or April); Hoysaḷa Viṣṇuvardhana as builder.</p>
<p><b>Not verified:</b> the Hoysaḷa claim; the date of Pūrṇayya’s grant (given as c. 1800 from his term as Dīvān). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('deity','The Lord of the White Hill'),('names','White Hill, Many Names'),('legends1','Legends · Vasiṣṭha and Rāma'),('legends2','Legends · The Soliga Bride'),('sandals','The Lord’s Sandals'),('soligas','The Soligas and Their Lord'),('history','History'),('festivals','The Annual Festival'),('around','Around the Hills'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,6.6vw,72px)">BIḶIGIRI RAṄGANA BEṬṬA</h1>
  <div class="series">BR HILLS · DAKṢIṆA TIRUPATI · A REFERENCE GUIDE</div>
  <div class="tag">The Lord of the white hill</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Where the Western and Eastern Ghats reach out and touch, a pale cliff rises out of the forest: <b>Biḷigiri</b>, the white hill.</p>
    <p>On top stands the Lord the forest people call family. The Soligas say he married their daughter, and to this day they carry him in his festival and make him new sandals for his night walks.</p>
    <p>This guide tells the story of the Lord, the hill and its people.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Govinda Govinda,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A god with in-laws in the forest?","The best kind of in-laws: they carry you on their shoulders and make you shoes!")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/BR_Hills.html','w').write(head+b+tail())
print('ok')
