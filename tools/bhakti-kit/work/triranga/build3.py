import sys; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
head=make_head('Antya Raṅga · Śrīraṅgam · Triraṅga · srini.presents',
 'Antya Raṅga, the Śrī Raṅganāthasvāmi temple at Śrīraṅgam: the last of the three Raṅgas and first of the 108 Divya Deśams. The vimāna from Brahmā to Vibhīṣaṇa, the Āḻvārs and Rāmānuja, the exile and return of the Lord, seven walls, Vaikuṇṭha Ekādaśī. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
island=lambda cx,cy,rx,ry: f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#dfeccf" stroke="#111" stroke-width="2"/>'
def GOP(x,y,s=1,tiers=13):
    return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-30+k*2} {-k*8} h{60-k*4} l-1 -8 h{-(58-k*4)}z" fill="{"#f2e6c8" if k%2 else "#e2cfa8"}"/>' for k in range(tiers))+f'<path d="M-6 {-tiers*8} q6 -12 12 0z" fill="#e0a800"/><rect x="-8" y="-16" width="16" height="16" fill="#7a5a2a"/></g>'
WALLS=lambda cx,cy,w,h,n=7: ''.join(f'<rect x="{cx-w/2+k*w/(2*n+2):.0f}" y="{cy-h/2+k*h/(2*n+2):.0f}" width="{w-k*w/(n+1):.0f}" height="{h-k*h/(n+1):.0f}" fill="none" stroke="#7a5a2a" stroke-width="2"/>' for k in range(n))
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The towering thirteen-tiered Rajagopuram of Srirangam rising over seven nested temple walls on a river island, with the reclining Lord shining above">'
 '<rect width="380" height="268" fill="#14315a" rx="8"/><circle cx="320" cy="56" r="22" fill="#ffd166"/>'
 +'<path d="M0 214 q190 -26 380 0 V268 H0z" fill="#4aa3df"/>'+island(190,224,170,30)+GOP(190,232,1.25)
 +RANGA(110,80,1.0)+'<path d="M226 120 l14 -26 l14 26z" fill="#e0a800" stroke="#111" stroke-width="2"/>'+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','Viṣṇu as <b>Raṅganātha</b>, <b>Periya Perumāḷ</b>, reclining on Ādiśeṣa and facing <b>south</b>; the festival image is <b>Namperumāḷ</b>; the Goddess is <b>Raṅganāyakī</b>'),
 ('Place','<b>Śrīraṅgam</b>, an island between the Kāverī and the Koḷḷiḍam, Tiruchirappalli, Tamil Nadu'),
 ('Divya Deśam','<b>First</b> of the 108; the only one sung by all twelve Āḻvārs, in <b>247</b> hymns'),
 ('Triraṅga','The <b>last</b> of the three island Raṅgas: <b>Antya Raṅga</b>'),
 ('Size','About <b>63 ha</b> (155 acres) inside <b>7</b> concentric walls, with <b>21</b> gopurams'),
 ('Rājagopuram','About <b>73 m</b>, 13 tiers; consecrated <b>1987</b>'),
 ('Builders','Cōḻas, Pāṇḍyas, Hoysaḷas, Vijayanagara, Nāyakas'),
 ('Teacher','<b>Rāmānuja</b> (1017–1137) lived and taught here; his body is enshrined in the temple'),
 ('Tradition','Śrīvaiṣṇava, Teṅkalai, with worship by the <b>Pāñcarātra</b> āgama'),
 ('Great festival','<b>Vaikuṇṭha Ekādaśī</b>, in the 20-day festival of Mārgaḻi'),
 ('Heritage','On UNESCO’s tentative list; UNESCO Asia-Pacific Award of Merit, 2017')])
 +talk("First of 108 AND last of three?","Both! First among the Divya Deśams, last on the river. Antya means 'final', and for many devotees this is where the journey ends.")))
mapfig=fig(560,260,'Schematic map: the island of Srirangam between the Kaveri on the south and the Kollidam on the north, with the great temple at its centre, the Jambukeswarar temple to its east, and Tiruchirappalli with the Rockfort across the Kaveri to the south. Not to scale.',
 '<rect width="560" height="260" fill="#4aa3df"/><path d="M20 130 C 120 60, 440 60, 540 130 C 440 200, 120 200, 20 130z" fill="#dfeccf" stroke="#111" stroke-width="2"/>'
 +WALLS(230,130,170,90)+'<rect x="222" y="122" width="16" height="16" fill="#e0a800" stroke="#111"/>'+T(230,190,'RAṄGANĀTHA TEMPLE',11,'#0d3f73')
 +'<rect x="390" y="110" width="50" height="34" fill="none" stroke="#7a5a2a" stroke-width="2"/>'+T(415,160,'TIRUVĀNAIKKĀ',10,'#0d3f73')
 +T(280,30,'KOḶḶIḌAM (north)',12,'#fff')+T(280,226,'KĀVERĪ (south)',12,'#fff')
 +'<rect x="0" y="236" width="560" height="24" fill="#f6f1e2"/><path d="M250 258 l20 -18 l20 18z" fill="#8a7a6a" stroke="#111"/>'+T(340,254,'TIRUCHIRAPPALLI · ROCKFORT',10,'#555','start')+T(110,254,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','An island between two rivers',mapfig+'''<div class="panel reading">
<p>Near the end of her journey, the Kāverī divides once more. The northern branch, the <b>Koḷḷiḍam</b>, and the Kāverī herself enclose the long island of <b>Śrīraṅgam</b>, beside the city of Tiruchirappalli.</p>
<p>The great temple fills the heart of the island; the town lives inside its outer walls. Just to the east stands Tiruvānaikkā, the Śiva temple of the water element; across the river rises the Rockfort.</p>
</div>'''))
deity=fig(560,240,'Periya Perumal, the great reclining Ranganatha facing south, and beside him the small golden festival image Namperumal',
 '<rect width="560" height="240" fill="#dcecff"/>'+RANGA(250,150,2.4)+'<g transform="translate(480 170)" stroke="#111" stroke-width="2"><circle cy="-46" r="12" fill="#e0a800"/><path d="M-18 20 q18 -60 36 0z" fill="#e0a800"/><path d="M-14 -58 h28 l-4 -12 h-20z" fill="#ffd60a"/></g>'
 +T(250,30,'PERIYA PERUMĀḶ',15,'#0d3f73')+T(480,212,'NAMPERUMĀḶ',12,'#c0392b'))
pages.append(page('deity','THE LORD OF ŚRĪRAṄGAM','Periya Perumāḷ and Namperumāḷ',deity+'''<div class="g2">
<div class="card bg-blue"><h4>🛏 Periya Perumāḷ</h4><p>“The Great Lord”: the reclining <b>mūlavar</b>, facing south. Unusually, the image is not of carved stone but of <b>sudhai</b>, a mix of lime, mortar and śālagrāma stones, coated with fragrant oil (<i>thailam</i>), so by tradition it is not bathed with water.</p></div>
<div class="card bg-yellow"><h4>✨ Namperumāḷ</h4><p>“Our Lord”: the <b>festival image</b> of five metals plated in gold, also called <b>Aḻagiya Maṇavāḷan</b>, “the beautiful bridegroom”. He goes out in procession, and he is the one who went into exile.</p></div>
</div>
<div class="panel reading"><p><b>The Goddess.</b> Raṅganāyakī has her own shrine in the second enclosure, with two fixed images and one festival image. By tradition she does not leave her shrine.</p></div>'''))
leg1=fig(560,200,'The golden vimana passing from Brahma to King Ikshvaku, to Rama, to Vibhishana, who sets it down on the island where it will not move',
 '<rect width="560" height="200" fill="#ffe3c4"/>'+''.join(f'<path d="M{70+k*140} 70 l14 -26 l14 26z" fill="#e0a800" stroke="#111" stroke-width="2"/>'+person(84+k*140,150,c,'#c98b5a',1)+T(84+k*140,186,n,11) for k,(c,n) in enumerate([('#ff8c1a','BRAHMĀ'),('#c0392b','IKṢVĀKU'),('#3b6fd0','RĀMA'),('#7a3fa0','VIBHĪṢAṆA')]))
 +''.join(f'<path d="M{110+k*140} 100 h80" stroke="#111" stroke-width="2" marker-end="url(#a)"/>' for k in range(3))+'<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0L8 4L0 8z" fill="#111"/></marker></defs>')
pages.append(page('legends1','THE LEGENDS · I','The vimāna that would not move',leg1+'''<div class="steps">
<div><b>From Brahmā.</b> The sacred <b>vimāna</b>, the shrine with the reclining Lord inside, arose from Brahmā’s austerities and stayed for ages in his world, Satyaloka.</div>
<div><b>To Ayodhyā.</b> King <b>Ikṣvāku</b> brought it to Ayodhyā, where it was worshipped by his descendants, the kings of the Sun dynasty, down to <b>Rāma</b>.</div>
<div><b>A gift to Vibhīṣaṇa.</b> After the war, Rāma gave it to <b>Vibhīṣaṇa</b>, the righteous brother of Rāvaṇa, to take to Laṅkā.</div>
<div><b>It would not move.</b> On the way, it was set down on this island and would not rise again. Vibhīṣaṇa gave it to the local king, <b>Dharmavarma</b>, on one condition: that the Lord should <b>face south</b>, towards Laṅkā.</div>
<div><b>So he faces south.</b> To this day Raṅganātha lies facing south, watching over Vibhīṣaṇa’s island.</div>
</div>'''))
leg2=fig(560,200,'A cowherd boy holding the image on the riverbank, then running up a great rock with Vibhishana chasing him; at the top, the boy revealed as Ganesha',
 '<rect width="560" height="200" fill="#ddf5ea"/><path d="M0 170 q140 -20 280 0 V200 H0z" fill="#4aa3df"/>'+person(80,160,'#ffd60a','#c98b5a',.9)+'<path d="M96 120 l10 -18 l10 18z" fill="#e0a800" stroke="#111"/>'
 +'<path d="M300 200 L380 60 L460 200z" fill="#8a7a6a" stroke="#111" stroke-width="2"/><rect x="368" y="44" width="24" height="18" fill="#f6f1e2" stroke="#111"/>'+'<g transform="translate(380 40)" stroke="#111" stroke-width="2"><circle r="9" fill="#e05a8a"/><path d="M-9 0 q-6 10 -2 14" fill="none" stroke="#e05a8a" stroke-width="4"/></g>'+person(320,180,'#7a3fa0','#c98b5a',.8)+T(380,190,'THE ROCKFORT',11))
pages.append(page('legends2','THE LEGENDS · II','Gaṇeśa, the river and the king',leg2+'''<div class="steps">
<div><b>A boy on the bank.</b> A popular local telling says that when Vibhīṣaṇa stopped to bathe in the Kāverī, he handed the image to a cowherd boy, asking him not to set it down. The boy set it down at once.</div>
<div><b>The chase.</b> Angry, Vibhīṣaṇa chased the boy up the great rock across the river and struck him on the head. The boy was <b>Gaṇeśa</b>, now worshipped at the summit as <b>Ucci Piḷḷaiyār</b>.</div>
<div><b>The river’s wish.</b> Another telling says the river goddess Kāverī asked Raṅganātha to stay with her on the island.</div>
<div><b>A flood and a king.</b> Tradition says a Kāverī flood later buried the shrine, and the early Cōḻa king <b>Kiḷḷivaḷavan</b> rebuilt the temple.</div>
</div>'''+talk("Gaṇeśa tricked Vibhīṣaṇa?","Lovingly! The gods wanted Raṅganātha to stay in the Kāverī country. And Raṅganātha still faces Laṅkā, so Vibhīṣaṇa is not forgotten.")))
alvars=('<table class="ct"><tr><th>Āḻvār</th><th>Hymns on Śrīraṅgam</th><th>Connection</th></tr>'
 '<tr><td><b>All twelve</b></td><td>247 in all</td><td>The only temple praised by every Āḻvār</td></tr>'
 '<tr><td><b>Toṇḍaraḍippoḍi</b></td><td>55</td><td>Sang only of Raṅganātha; his dawn hymn wakes the Lord</td></tr>'
 '<tr><td><b>Kulaśekhara</b></td><td>31</td><td>A king of Kerala who longed to serve at Śrīraṅgam</td></tr>'
 '<tr><td><b>Āṇḍāḷ</b></td><td>10</td><td>Poet of the Tiruppāvai; tradition says she merged into Raṅganātha here</td></tr>'
 '<tr><td><b>Tiruppāṇ</b></td><td>10</td><td>Sang only of Raṅganātha, describing the Lord from his feet upward</td></tr></table>')
pages.append(page('alvars','THE ĀḺVĀRS','Twelve poet-saints, one Lord',alvars+'''<div class="panel reading">
<p><b>The Tamil Veda.</b> The twelve <b>Āḻvārs</b>, Tamil poet-saints of the 6th to 9th centuries, sang the hymns later gathered as the <b>Nālāyira Divya Prabandham</b>, the 4,000 sacred verses. Temples they sang of are the <b>Divya Deśams</b>.</p>
<p><b>Āṇḍāḷ’s Lord.</b> The girl who wore the Lord’s garland sang her Tiruppāvai to this Raṅganātha, and tradition says she was united with him at Śrīraṅgam.</p>
</div>'''+talk("Is that why Tiruppāvai is sung here in Mārgaḻi?","Yes. Āṇḍāḷ's songs come home to her Lord every Dhanurmāsa.")))
pages.append(page('ramanuja','RĀMĀNUJA','The teacher of Śrīraṅgam','''<div class="panel reading">
<p><b>The great teacher.</b> <b>Rāmānuja</b> (traditionally 1017–1137), the teacher of <b>Viśiṣṭādvaita</b>, made Śrīraṅgam the centre of the Śrīvaiṣṇava tradition.</p>
<p><b>His works.</b> The <b>Śrī Bhāṣya</b>, his commentary on the Brahma Sūtras, and the <b>Gadya Traya</b>, three prose hymns of surrender, are linked with his years here.</p>
<p><b>His order.</b> Tradition credits him with organising the temple’s worship and service, which shaped how it is run to this day.</p>
<p><b>His presence.</b> Rāmānuja’s preserved body is enshrined within the temple, in a shrine of its own, revered as his <i>tirumeni</i>.</p>
<p><b>Two Raṅgas.</b> The same teacher received Śrīraṅgapaṭṭaṇa from the Hoysaḷa king: see <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga</a>. The first and last Raṅgas share him.</p>
</div>'''+talk("His body is still here, after 900 years?","That's the tradition and the temple's practice: he is honoured here, seated, as if still present among his people.")))
pages.append(page('history1','HISTORY · I','Dynasty after dynasty',tl([
 ('Early','Tradition names King <b>Dharmavarma</b> as the first builder and the early Cōḻa <b>Kiḷḷivaḷavan</b> as the one who rebuilt it after a flood.'),
 ('6th–9th c.','The twelve <b>Āḻvārs</b> sing of Raṅganātha in 247 hymns.'),
 ('Cōḻas','The Cōḻas build and endow the temple; Cōḻa work survives, for example in the Cakrattāḻvār shrine’s front hall.'),
 ('11th–12th c.','<b>Rāmānuja</b> leads the Śrīvaiṣṇava community from Śrīraṅgam.'),
 ('Pāṇḍyas, Hoysaḷas','Further patronage and building; inscriptions also name Marāṭhās and Gajapatis among donors.'),
 ('1336–1565','Under <b>Vijayanagara</b>, the thousand-pillared hall is built.'),
 ('Nāyakas','The Madurai Nāyakas add the Śeṣarāya and Garuḍa maṇḍapas; Chokkanātha Nāyaka rebuilds the Veṇugopāla shrine (1674).')])
 +'<div class="panel reading"><p><b>Never finished.</b> Each dynasty added a wall, a hall or a tower around the last. The temple grew outward from the Lord like rings in a tree.</p></div>'))
pages.append(page('history2','HISTORY · II','The Lord in exile, and his return',tl([
 ('1310–11','The army of <b>Malik Kāfūr</b> raids the temple.'),
 ('1323–27','Forces of <b>Muhammad bin Tughluq</b> invade. Tradition remembers some <b>13,000</b> devotees dying in the temple’s defence.'),
 ('The exile','<b>Piḷḷai Lokācārya</b> leads a band carrying Namperumāḷ away for safety, towards Tirunelveli; Raṅganāyakī is taken elsewhere. The Lord’s image wanders for decades.'),
 ('1371','Under <b>Kumāra Kampaṇa</b> of Vijayanagara the temple is restored and the image returns home.')])
 +'''<div class="panel reading">
<p><b>Tulukka Nācciyār.</b> Temple tradition remembers a Sultan’s daughter who loved the Lord’s image so deeply that she is honoured within the temple, shown in a niche on horseback: a story of devotion that crossed every border.</p>
<p><b>Vedānta Deśika.</b> The great teacher and poet of the 13th–14th centuries is closely associated with the temple and has a shrine here.</p>
</div>'''+talk("The Lord himself went into exile?","His festival image did, carried by devotees for decades. Many say the homecoming is part of why Namperumāḷ is so loved: 'our Lord', who came back.")))
plan=fig(560,260,'Simplified plan of seven nested enclosures, with the golden vimana at the centre and gopurams on the walls, the tallest Rajagopuram on the south',
 '<rect width="560" height="260" fill="#f6f1e2"/>'+WALLS(280,124,480,210)+'<path d="M270 114 l10 -18 l10 18z" fill="#e0a800" stroke="#111" stroke-width="2"/><rect x="266" y="114" width="28" height="18" fill="#e0a800" stroke="#111"/>'
 +GOP(280,262,.42)+T(280,250,'RĀJAGOPURAM (south)',9)+''.join(f'<rect x="{x-6}" y="{y-6}" width="12" height="12" fill="#e2cfa8" stroke="#111"/>' for x,y in [(280,34),(56,124),(504,124),(280,214),(150,124),(410,124)])+T(280,152,'GOLDEN VIMĀNA',9,'#0d3f73'))
pages.append(page('temple','SEVEN WALLS','The plan of the temple',plan+'''<div class="g2">
<div class="card bg-yellow"><h4>🧱 Seven prākāras</h4><p>Seven concentric enclosures, their walls together about <b>9.9 km</b> long, surround the shrine. The outer ones hold streets, houses and shops: a town inside the temple.</p></div>
<div class="card bg-blue"><h4>🏯 21 gopurams</h4><p>Twenty-one gateway towers, 17 of them major. The southern <b>Rājagopuram</b>, begun around 1500, was completed by the Ahobila Maṭha and consecrated on <b>25 March 1987</b>, about 73 m high.</p></div>
</div>
<div class="panel reading"><p><b>The golden vimāna.</b> Over the sanctum rises a gold-plated vimāna shaped like the Tamil letter for <b>Oṃ</b>, the <i>praṇava</i>, with an image of Paravāsudeva on its front.</p></div>'''))
pages.append(page('halls','HALLS AND SHRINES','Inside the walls',facts([
 ('Thousand-pillar hall','A vast granite hall from the Vijayanagara period, laid out like a theatre with a central aisle and seven side aisles on each side'),
 ('Śeṣarāya maṇḍapa','A Nāyaka hall whose pillars burst into <b>40 leaping horses and riders</b>, each carved from a single stone'),
 ('Garuḍa maṇḍapa','A Nāyaka hall with a great seated <b>Garuḍa</b> facing the Lord’s shrine'),
 ('Raṅga Vilāsa','A large hall covered with <b>murals of the Rāmāyaṇa</b>'),
 ('Raṅganāyakī','The Goddess’s shrine in the second enclosure'),
 ('Cakrattāḻvār','The shrine of the Lord’s discus as a deity, with Cōḻa and Vijayanagara halls'),
 ('Veṇugopāla','Kṛṣṇa with the flute, rebuilt by Chokkanātha Nāyaka in 1674'),
 ('Dhanvantari','A shrine of the divine physician, a form of Viṣṇu'),
 ('Teachers','Shrines of Rāmānuja and Vedānta Deśika')])
 +talk("A shrine to a discus?","Cakrattāḻvār: the Lord's own weapon, honoured as a devotee. In Śrīraṅgam, even the discus is a saint.")))
pages.append(page('vaikuntha','VAIKUṆṬHA EKĀDAŚĪ','The gate of heaven opens',fig(560,180,'A great golden gate swinging open, with devotees streaming through behind the festival image under a dawn sky','<rect width="560" height="180" fill="#1c2a55"/><rect y="120" width="560" height="60" fill="#f4b183" opacity=".5"/><rect x="230" y="30" width="100" height="140" fill="#ffd60a" opacity=".5"/><rect x="200" y="30" width="40" height="140" fill="#e0a800" stroke="#111" stroke-width="2"/><rect x="320" y="30" width="40" height="140" fill="#e0a800" stroke="#111" stroke-width="2"/>'+crowd(['#fff','#ffd60a','#ff8c1a','#3b6fd0','#e05a8a','#fff','#ffd60a'],250,10,172,.5)+T(280,22,'PARAMAPADA VĀSAL',13,'#fff'))+'''<div class="g2">
<div class="card bg-blue"><h4>🌞 Pagal Pattu</h4><p>“Ten days”: the first ten days of the Mārgaḻi festival.</p></div>
<div class="card bg-yellow"><h4>🌙 Rā Pattu</h4><p>“Ten nights”: the next ten. The <b>first</b> day of Rā Pattu is <b>Vaikuṇṭha Ekādaśī</b>.</p></div>
</div>
<div class="panel reading">
<p><b>The gate.</b> The <b>Paramapada Vāsal</b>, the gate of the supreme abode, opens only during these ten days. Namperumāḷ passes through it at dawn on Ekādaśī, and vast crowds follow him through.</p>
<p><b>The Tamil Veda sung.</b> The twenty days are an <i>adhyayana utsava</i>, a festival of recitation, when the Āḻvārs’ 4,000 verses are sung before the Lord.</p>
<p><b>In 2026,</b> Vaikuṇṭha Ekādaśī falls on 20 December.</p>
</div>'''))
pages.append(page('festivals','THROUGH THE YEAR','Festivals of Śrīraṅgam',facts([
 ('Mārgaḻi (Dec–Jan)','The 20-day festival and <b>Vaikuṇṭha Ekādaśī</b>; Āṇḍāḷ’s Tiruppāvai sung every dawn'),
 ('Thai (Jan–Feb)','<b>Rathotsava</b>, the temple car festival'),
 ('Paṅguni (Mar–Apr)','The Brahmotsava, with <b>Paṅguni Uttiram</b>: the <b>Sērtti Sēvai</b>, the one day a year Raṅganātha and Raṅganāyakī are seen together'),
 ('Citrā Pūrṇimā','Remembers <b>Gajendra Mokṣa</b>, the Lord’s rescue of the elephant king'),
 ('Āni (Jun–Jul)','<b>Jyeṣṭhābhiṣeka</b>: three days, with armour of <b>diamonds</b>, <b>pearls</b> and <b>gold</b> on successive days')])
 +talk("The Lord and the Goddess together just once a year?","She never leaves her shrine; he goes to her. Paṅguni Uttiram is that one meeting, and devotees wait all year to see them side by side.")))
pages.append(page('around','AROUND THE ISLAND','Śaiva neighbours and a famous rock',facts([
 ('Tiruvānaikkā','The <b>Jambukeśvara</b> temple, just east on the same island: one of the five Śiva temples of the elements, for <b>water</b>'),
 ('Rockfort','Across the Kāverī at Tiruchirappalli, the great rock with the Tāyumānavar Śiva temple and, at the summit, <b>Ucci Piḷḷaiyār</b>, the Gaṇeśa of the Vibhīṣaṇa story'),
 ('The Kāverī','The bathing ghāṭs where the river festivals of the island are held'),
 ('The Koḷḷiḍam','The northern branch that makes Śrīraṅgam an island')])
 +'<div class="panel reading"><p><b>Hari and Hara.</b> As at the other two Raṅgas, Viṣṇu’s island shares its waters with Śiva: Raṅganātha and Jambukeśvara, a short walk apart.</p></div>'))
pages.append(page('triranga','THE LAST OF THREE','Antya Raṅga in the Triraṅga',fig(560,120,'Three islands in a row along the river, the last one highlighted','<rect width="560" height="120" fill="#4aa3df"/>'+''.join(island(x,60,70,24)+RANGA(x,54,.36,youth=(i==1)) for i,x in enumerate([100,280,460]))+'<rect x="380" y="24" width="160" height="72" fill="none" stroke="#ffd60a" stroke-width="4" rx="8"/>'+T(100,112,'ĀDI',11,'#fff')+T(280,112,'MADHYA',11,'#fff')+T(460,112,'ANTYA · YOU ARE HERE',11,'#fff'))+'''<div class="panel reading">
<p><b>The end of the vow.</b> In the Triraṅga, Antya Raṅga comes <b>last</b>, after <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga</a> and <a href="/bhakti/temples-of-india/triranga/madhya-ranga/">Madhya Raṅga</a>. The vow ends here, at dusk, before the greatest of the three.</p>
<p><b>First, middle, last.</b> If the three are a life, this is its end: and for the Śrīvaiṣṇava, the end is the Lord’s own abode, the gate of Vaikuṇṭha that opens here every Mārgaḻi.</p>
<p>See the <a href="/bhakti/temples-of-india/triranga/">Triraṅga overview</a> for all three together.</p>
</div>'''))
glossary=[('Antya Raṅga','“the last Raṅga”: the Raṅganātha of Śrīraṅgam'),('Periya Perumāḷ','“the Great Lord”, the reclining mūlavar'),('Namperumāḷ','“our Lord”, the festival image'),('Aḻagiya Maṇavāḷan','“the beautiful bridegroom”, a name of Namperumāḷ'),('Raṅganāyakī','the Goddess of Śrīraṅgam'),('Vimāna','the tower over the sanctum'),('Praṇava','the sacred syllable Oṃ'),('Prākāra','an enclosing wall and courtyard'),('Divya Deśam','one of 108 Viṣṇu temples sung by the Āḻvārs'),('Nālāyira Divya Prabandham','the 4,000 Tamil verses of the Āḻvārs'),('Pagal Pattu · Rā Pattu','“ten days” · “ten nights” of the Mārgaḻi festival'),('Paramapada Vāsal','the gate of the supreme abode'),('Sērtti Sēvai','the joint darśan of the Lord and the Goddess'),('Teṅkalai','the southern school of Śrīvaiṣṇavism'),('Pāñcarātra','the āgama that governs the temple’s worship')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','ANTYA RAṄGA ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The place.</b> Śrīraṅgam, an island between the Kāverī and Koḷḷiḍam, Tamil Nadu: the last Raṅga and the first of the 108 Divya Deśams.</div>
<div><b>The Lord.</b> Periya Perumāḷ, reclining and facing south; Namperumāḷ, the golden festival image; Raṅganāyakī in her own shrine.</div>
<div><b>The legends.</b> The vimāna from Brahmā to Ikṣvāku, Rāma and Vibhīṣaṇa, which would not move; Gaṇeśa on the Rockfort.</div>
<div><b>The history.</b> Āḻvārs and Rāmānuja; Cōḻa to Nāyaka builders; the raids of the 1300s, the Lord’s exile and his return in 1371; the Rājagopuram of 1987.</div>
<div><b>The festivals.</b> Vaikuṇṭha Ekādaśī and the gate of heaven; the car festival; Sērtti Sēvai; the jewelled armour of Jyeṣṭhābhiṣeka.</div>
</div>'''+talk("So the Triraṅga is complete?","First, middle and last. One river, one Lord, three resting places. Now you know all three.")+'<div class="key">The last Raṅga: <b>where the journey ends at the gate of heaven</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Ranganathaswamy Temple, Srirangam”, and the sources it cites: area (63 ha); seven prākāras and walls of about 9,934 m; 21 gopurams; Rājagopuram (about 73 m, 13 tiers, consecrated 25 March 1987 by the Ahobila Maṭha); dynasties; 247 Āḻvār hymns and the hymn counts of Toṇḍaraḍippoḍi, Kulaśekhara, Āṇḍāḷ and Tiruppāṇ; the vimāna legend; Kiḷḷivaḷavan; the mūlavar of sudhai and the golden pañcaloha Namperumāḷ; Raṅganāyakī’s shrine; the thousand-pillar, Śeṣarāya, Garuḍa and Raṅga Vilāsa maṇḍapas; Veṇugopāla (1674); Cakrattāḻvār; raids of 1310–11 and 1323–27; Piḷḷai Lokācārya; reinstatement in 1371; Tulukka Nācciyār; Teṅkalai and Pāñcarātra; festivals; UNESCO tentative list and the 2017 award.</p>
<p><b>Other:</b> Hindutone and Drik Pañcāṅga (Vaikuṇṭha Ekādaśī on 20 December 2026). The Rockfort Gaṇeśa story, the adhyayana utsava and Tiruvānaikkā are widely recorded local tradition and general knowledge.</p>
<p><b>Not verified:</b> the 13,000 defenders (a figure from tradition); the dates of the Āḻvārs and of Rāmānuja (traditional); the details of the Gaṇeśa and Kāverī tellings, which vary.</p>
<p>Maps and plans are simplified illustrations, not to scale. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('deity','The Lord of Śrīraṅgam'),('legends1','Legends · The Vimāna'),('legends2','Legends · Gaṇeśa'),('alvars','The Āḻvārs'),('ramanuja','Rāmānuja'),('history1','History · I'),('history2','History · II'),('temple','Seven Walls'),('halls','Halls and Shrines'),('vaikuntha','Vaikuṇṭha Ekādaśī'),('festivals','Through the Year'),('around','Around the Island'),('triranga','The Last of Three'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TRIRAṄGA · 3 OF 3</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">ANTYA RAṄGA</h1>
  <div class="series">ŚRĪ RAṄGANĀTHASVĀMI · ŚRĪRAṄGAM · A REFERENCE GUIDE</div>
  <div class="tag">The last Raṅga, and the first of the 108</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>At the end of the Triraṅga, the Kāverī parts one last time, and between her and the Koḷḷiḍam lies <b>Śrīraṅgam</b>: seven walls, twenty-one towers, a whole town, and at the centre, facing south, the reclining Lord.</p>
    <p>This is the temple the twelve Āḻvārs all sang, where Āṇḍāḷ came to her Lord, where Rāmānuja taught, from which the Lord’s image went into exile, and to which it came home. Devotees simply call it <b>Kōyil</b>, “the temple”.</p>
    <p>This guide tells its legends, its saints and its long history.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("They just call it 'the temple'?","For Śrīvaiṣṇavas, 'Kōyil' with no other name means Śrīraṅgam. When you're first of 108, you don't need a surname.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/triranga/Antya_Ranga.html','w').write(head+b+tail())
print('ok')
