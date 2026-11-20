exec(open('/home/claude/work/shakti/common_s.py').read())
import math
head=head_red('Kāmākṣī · Kāñcīpuram · The 18 Śakti Pīṭhas · srini.presents',
 'Kāmākṣī of Kāñcīpuram, the second of the 18 Śakti Pīṭhas: the Goddess seated in padmāsana with sugarcane bow and flower arrows, the Śrī Cakra, Bhaṇḍāsura and the mango tree, the golden Bangāru Kāmākṣī’s journey to Thanjavur, the Mūka Pañcaśatī and the Kāmakoṭi Pīṭham. An illustrated reference guide.')
def tn(lat,lon): return 140+(lon-78.9)*190, 14+(13.45-lat)*95
COAST=[(13.45,80.30),(13.08,80.29),(12.62,80.20),(12.2,79.97),(11.9,79.83),(11.4,79.78),(10.8,79.86),(10.3,79.86)]
def TNMAP(marks,w=560,h=280):
    land='M0 0 '+' '.join(f'L{tn(a,b)[0]:.0f} {tn(a,b)[1]:.0f}' for a,b in COAST)+f' L{tn(10.3,79.86)[0]:.0f} {h} L0 {h}z'
    g=''
    for la,lo,t,side,col in marks:
        x,y=tn(la,lo); r=8 if col=='#c0392b' else 5
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',t,12,'#111','start' if side=='r' else 'end')
    return (f'<rect width="{w}" height="{h}" fill="#dff0fa"/><path d="{land}" fill="#f1e6cf" stroke="#111" stroke-width="2"/>'
     +f'<path d="M{tn(12.4,78.9)[0]:.0f} {tn(12.4,78.9)[1]:.0f} Q{tn(11.6,79.3)[0]:.0f} {tn(11.6,79.3)[1]:.0f} {tn(11.37,79.83)[0]:.0f} {tn(11.37,79.83)[1]:.0f}" stroke="#4aa3df" stroke-width="2.5" fill="none"/>'
     +f'<path d="M30 {tn(10.9,78)[1]:.0f} Q200 {tn(10.95,79)[1]:.0f} {tn(10.9,79.85)[0]:.0f} {tn(10.9,79.85)[1]:.0f}" stroke="#4aa3df" stroke-width="3" fill="none"/>'+T(60,tn(10.9,78)[1]-6,'KĀVERĪ',10,'#1d4f9a','start')
     +T(w-40,h/2,'BAY OF BENGAL',12,'#1d4f9a','end')+T(60,30,'TAMIL NADU',13,'#7a5a2a','start')+g+T(w-10,h-8,'simplified, not to scale',10,'#555','end'))
def SRICAKRA(x,y,r=60):
    s=f'<g transform="translate({x} {y})" stroke="#111" stroke-width="1.5">'
    s+=f'<rect x="{-r*1.15:.0f}" y="{-r*1.15:.0f}" width="{r*2.3:.0f}" height="{r*2.3:.0f}" fill="#fff4cd"/>'
    s+=''.join(f'<path d="M{a} {b}" />' for a,b in ())
    s+=f'<circle r="{r}" fill="#fde4e4"/>'+''.join(f'<ellipse cx="{r*0.86*math.cos(k*math.pi/8):.1f}" cy="{r*0.86*math.sin(k*math.pi/8):.1f}" rx="{r*0.14:.1f}" ry="{r*0.07:.1f}" transform="rotate({k*22.5} {r*0.86*math.cos(k*math.pi/8):.1f} {r*0.86*math.sin(k*math.pi/8):.1f})" fill="#f7b2b2"/>' for k in range(16))
    s+=f'<circle r="{r*0.7:.0f}" fill="#fff"/>'
    for k,sc in enumerate((0.66,0.5,0.36,0.22)):
        s+=f'<path d="M0 {-r*sc:.1f} L{r*sc*0.87:.1f} {r*sc*0.5:.1f} L{-r*sc*0.87:.1f} {r*sc*0.5:.1f}z" fill="none" stroke="#c0392b" stroke-width="1.6"/>'
        s+=f'<path d="M0 {r*(sc-0.06):.1f} L{r*(sc-0.06)*0.87:.1f} {-r*(sc-0.06)*0.5:.1f} L{-r*(sc-0.06)*0.87:.1f} {-r*(sc-0.06)*0.5:.1f}z" fill="none" stroke="#1d4f9a" stroke-width="1.4"/>'
    return s+'<circle r="3" fill="#c0392b"/></g>'
def KAMAKSHI(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-40 60 q40 -20 80 0 q-40 16 -80 0z" fill="#f7b2b2"/><path d="M-34 52 q-4 -50 34 -62 q38 12 34 62z" fill="#c0392b"/><path d="M-30 44 q30 14 60 0" fill="none" stroke="#e0a800" stroke-width="4"/>'
 '<circle cy="-22" r="12" fill="#f2c79b"/><path d="M-12 -32 h24 l-4 -16 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/>'
 '<path d="M-22 -2 l-24 -16 M22 -2 l24 -16 M-20 14 l-22 2 M20 14 l22 2" stroke="#f2c79b" stroke-width="6"/>'
 '<path d="M-52 -40 q-10 24 4 40" stroke="#5a8a3a" stroke-width="4" fill="none"/><path d="M-52 -40 l8 40" stroke="#ccc" stroke-width="1"/>'
 '<path d="M44 -24 l14 -12 M46 -20 l16 -6 M44 -28 l8 -14" stroke="#e05a8a" stroke-width="3"/>'
 '<circle cx="-46" cy="16" r="6" fill="none" stroke="#e0a800" stroke-width="3"/><path d="M46 16 l10 -8 l-2 10" stroke="#bbb" stroke-width="3" fill="none"/></g>')
def MANGO(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-8" y="-60" width="16" height="60" fill="#7a5a2a"/><circle cy="-80" r="44" fill="#3a8a3a"/>'+''.join(f'<ellipse cx="{a}" cy="{b}" rx="5" ry="7" fill="#ffc107"/>' for a,b in ((-20,-70),(14,-90),(24,-62),(-6,-100)))+'</g>'
def LINGA(x,y,s=1,c='#c9a26b'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-26 0 h52 l-6 -10 h-40z" fill="#8a8a8a"/><path d="M-12 -10 v-26 a12 12 0 0 1 24 0 v26z" fill="{c}"/></g>'
def PARROT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.5"><ellipse rx="10" ry="14" fill="#2ecc71"/><circle cy="-14" r="7" fill="#2ecc71"/><path d="M5 -14 l6 3 l-6 2z" fill="#c0392b"/><path d="M-4 12 l-6 14" stroke="#1a7a3a" stroke-width="3"/></g>'
GOPK=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-34+k*3} {-k*12} h{68-k*6} l-1 -12 h{-(66-k*6)}z" fill="{"#f2e6c8" if k%2 else "#e2cfa8"}"/>' for k in range(7))+''.join(f'<path d="M{-14+j*5} -84 l2 -10 l2 10z" fill="#e0a800"/>' for j in range(7))+'<rect x="-9" y="-20" width="18" height="20" fill="#5a3a1a"/></g>'
VIM=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-20" width="52" height="20" fill="#f2e6c8"/><path d="M-20 -20 h40 l-6 -14 h-28z M-14 -34 h28 l-5 -12 h-18z" fill="#ffd60a"/><circle cy="-52" r="6" fill="#ffd60a"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The Goddess Kamakshi seated in lotus posture holding sugarcane bow and flower arrows, a Sri Chakra glowing behind her, a golden temple tower and a parrot">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/>'+SRICAKRA(190,124,96).replace('fill="#fff4cd"','fill="#9a2a1a"')+KAMAKSHI(190,150,1.5)+GOPK(54,262,.8)+VIM(330,250,1.4)+PARROT(320,60,1.2)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Kāmākṣī</b>, the Goddess as Lalitā Tripurasundarī: Pīṭha no. 2 of the eighteen'),
 ('Hymn line','<i>kāmākṣī kāñcikāpure</i>: “Kāmākṣī in the city of Kāñcī”'),
 ('Where','<b>Kāñcīpuram</b>, Tamil Nadu, the old Pallava capital and one of the seven holy cities'),
 ('Body part','Satī’s <b>navel</b> in the usual South Indian list; some lists say her back'),
 ('The image','Seated in <b>padmāsana</b>, holding <b>noose</b>, <b>goad</b>, <b>sugarcane bow</b> and <b>flower arrows</b>'),
 ('Before her','A <b>Śrī Cakra</b>, which temple tradition credits to Ādi Śaṅkara'),
 ('Only Goddess','The one great Goddess shrine of Kāñcī: the city’s Śiva temples have no separate Ammaṉ shrine'),
 ('Golden image','<b>Bangāru Kāmākṣī</b>, carried away for safety, now worshipped in <b>Thanjavur</b>'),
 ('Festivals','The <b>Māsi</b> festival ending in Māsi Pūram, Navarātri, and her Fridays')])
 +talk("Kāmākṣī: 'eyes of love'?","That's one reading. Another says her two eyes are Sarasvatī and Lakṣmī. Either way, one look from her is enough.")))
pages.append(page('where','WHERE IT IS','Kāñcī, between the hills and the sea',fig(560,280,'Simplified map of northern Tamil Nadu: Kanchipuram in red inland from Chennai and Mamallapuram, with Tiruvarur and Thanjavur on the Kaveri to the south',
 TNMAP([(12.83,79.70,'KĀÑCĪPURAM','l','#c0392b'),(13.08,80.27,'Chennai','l','#bbb'),(12.62,80.19,'Māmallapuram','l','#bbb'),(10.77,79.64,'Tiruvārūr','r','#ffd166'),(10.79,79.14,'Thanjavur','l','#ffd166'),(10.96,79.39,'Kumbakonam','r','#bbb')]))
 +'''<div class="panel reading">
<p><b>The city.</b> Kāñcīpuram lies on the Vegavatī and Pālār rivers, inland from Chennai. It was the capital of the <b>Pallavas</b> and is famous for its temples and its silk.</p>
<p><b>The yellow dots.</b> <b>Tiruvārūr</b> and <b>Thanjavur</b> are where the golden image of Kāmākṣī went in the 18th century (see “The Golden Kāmākṣī”).</p>
<p><b>A holy city.</b> Kāñcī is one of the seven <b>mokṣapurīs</b>, cities said to grant liberation, with Ayodhyā, Mathurā, Haridvār, Kāśī, Ujjain and Dvārakā.</p>
</div>'''))
pages.append(page('names','HER NAMES','Love, eyes and ten million',facts([
 ('Kāmākṣī','“She whose eyes are love”; or “she whose eyes are <b>ka</b> and <b>ma</b>”, Sarasvatī and Lakṣmī'),
 ('Kāmakoṭi','“Ten million desires”, or the summit of desire: the name of her seat, the <b>Kāmakoṭi Pīṭha</b>'),
 ('Kāmakoṭi Nāyaki','“Lady of the Kāmakoṭi”: the temple’s Tamil name, Kāmakōṭṭam'),
 ('Lalitā Tripurasundarī','The supreme Goddess of Śrīvidyā, “beautiful in the three worlds”'),
 ('Para Bhaṭṭārikā','“The supreme Lady”: the main image'),
 ('Śrī Mātā','“The holy Mother”, the first name of the Lalitā Sahasranāma')])
 +talk("Why so many names about love and desire?","In Śrīvidyā, desire isn't the enemy. The Goddess is the power that moves everything, and Kāmākṣī holds its bow.")))
pages.append(page('pitha','THE PĪṬHA','The navel of the earth',fig(560,150,'Shiva carrying Sati across a night sky, a glowing point falling onto a temple city by a river',
 '<rect width="560" height="150" fill="#2a0805"/>'+STAR+SHIVA(140,60,.7)+SATI(162,64,.55,-10)+'<path d="M190 80 q80 10 190 40" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><circle cx="382" cy="120" r="6" fill="#ffd166"/>'+GOPK(420,148,.6)+VIM(480,146,.8)+T(440,24,'KĀÑCĪ',14,'#ffd166'))+'''<div class="panel reading">
<p><b>The verse.</b> <i>kāmākṣī kāñcikāpure</i>: the second name of the hymn, straight after Laṅkā.</p>
<p><b>What fell here.</b> The usual South Indian list says Satī’s <b>navel</b>, which fits a local idea: Kāñcī as the <b>nābhi</b>, the navel or centre, of the earth. Other lists name her back.</p>
<p><b>A different emphasis.</b> At Kāñcī the Satī story is not the main story. Temple tradition stresses Kāmākṣī as Lalitā, who rose to kill <b>Bhaṇḍāsura</b>, and as Pārvatī, who did penance here and won Śiva back.</p>
</div>'''))
pages.append(page('goddess','THE GODDESS','Seated in the lotus posture',fig(560,220,'The Goddess Kamakshi seated cross-legged in lotus posture, four-armed, holding noose, goad, sugarcane bow and flower arrows, with a Sri Chakra in front of her',
 '<rect width="560" height="220" fill="#fff4cd"/><rect x="170" y="10" width="220" height="200" fill="#fde4e4" stroke="#111" stroke-width="2"/>'+KAMAKSHI(280,120,1.7)+SRICAKRA(470,110,50)+T(470,196,'ŚRĪ CAKRA',12,'#7a1d12')
 +T(90,60,'NOOSE · GOAD',12,'#7a1d12')+T(90,80,'SUGARCANE BOW',12,'#7a1d12')+T(90,100,'FIVE FLOWER',12,'#7a1d12')+T(90,116,'ARROWS',12,'#7a1d12'))+'''<div class="g2">
<div class="card bg-red"><h4>🪷 The pose</h4><p>Kāmākṣī sits in <b>padmāsana</b>, the lotus posture of a yogin, facing south-east. She is a Goddess in meditation, not in battle.</p></div>
<div class="card bg-yellow"><h4>🏹 The four</h4><p><b>Noose</b> (attachment held in check), <b>goad</b> (anger turned to good), <b>sugarcane bow</b> (the mind) and five <b>flower arrows</b> (the senses): the classic weapons of Lalitā.</p></div>
</div><div class="panel reading small"><p>Temple tradition says the one image holds three forms at once: gross (<i>sthūla</i>), subtle (<i>sūkṣma</i>) and causal (<i>kāraṇa</i>).</p></div>'''))
pages.append(page('forms','FIVE FORMS OF KĀMĀKṢĪ','One Goddess, five shrines',facts([
 ('Para Bhaṭṭārikā','The main image in the sanctum, in padmāsana'),
 ('Tapa Kāmākṣī','Kāmākṣī doing <b>penance</b>, to the right of the main image, near the Bila gate'),
 ('Añjana Kāmākṣī','To the left: linked with <b>Lakṣmī</b>, who did penance here to win back her beauty; also called <b>Arūpa Lakṣmī</b>. Devotees are given kuṅkuma here'),
 ('Bangāru Kāmākṣī','The <b>golden</b> Kāmākṣī: the original is in Thanjavur; Kāñcī keeps a five-metal image in her place'),
 ('Utsava Kāmākṣī','The festival image that goes out in procession')])
 +'<div class="panel reading"><p><b>Lakṣmī’s story.</b> Cursed to lose her beauty, Lakṣmī came to Kāmākṣī and did penance until it returned. That is why kuṅkuma is first offered at Añjana Kāmākṣī’s shrine and only then given to devotees.</p></div>'
 +talk("Why five Kāmākṣīs?","Five ways to meet her: as queen, as yogini, as giver of beauty, as gold, and as the one who walks the streets with you.")))
pages.append(page('chakra','THE ŚRĪ CAKRA','The diagram before the Goddess',fig(560,230,'A Sri Chakra diagram of interlocking triangles inside lotus petals and circles, with the Gayatri mandapa pillars around',
 '<rect width="560" height="230" fill="#fdf1e8"/>'+SRICAKRA(280,115,95)+''.join(f'<rect x="{x}" y="20" width="10" height="190" fill="#e2cfa8" stroke="#111"/>' for x in (40,70,480,510)))+'''<div class="steps">
<div><b>The diagram.</b> A <b>Śrī Cakra</b> (Śrī Yantra) is Lalitā’s own form drawn in geometry: nine interlocking triangles round a central point, ringed by lotus petals and a square with four gates.</div>
<div><b>Two founders.</b> Tradition says the sage <b>Durvāsas</b>, a form of Śiva, first set a Śrī Cakra before the Goddess; the present one is credited to <b>Ādi Śaṅkara</b>.</div>
<div><b>The Gāyatrī Maṇḍapa.</b> The sanctum hall has <b>24 pillars</b>, for the 24 syllables of the Gāyatrī mantra; its four walls are said to stand for the four Vedas.</div>
</div>'''))
pages.append(page('bhanda','THE LEGEND · BHAṆḌĀSURA','The gods as parrots',fig(560,180,'Gods hidden as green parrots in champaka trees; the Goddess bursting out of an opening in the ground to face a dark demon',
 '<rect width="560" height="180" fill="#ffe9c4"/>'+''.join(MANGO(x,170,.9).replace('#3a8a3a','#5aa05a').replace('#ffc107','#fff1a8') for x in (60,160))+''.join(PARROT(x,y,.8) for x,y in ((40,90),(80,76),(150,100),(178,70)))
 +'<ellipse cx="300" cy="166" rx="50" ry="10" fill="#3a2a1a" stroke="#111"/>'+KAMAKSHI(300,100,.8)+'<g transform="translate(470 160)">'+DEMON(0,0,1.3,'#3a2a5a')+'</g>'+T(470,24,'BHAṆḌĀSURA',12,'#7a1d12'))+'''<div class="steps">
<div><b>The demon.</b> <b>Bhaṇḍāsura</b>, born from the ashes of Kāma, the god of love, after Śiva burned him, grew so strong that he drove the gods from heaven.</div>
<div><b>Hiding as parrots.</b> The gods fled to Kāñcī and did penance in the form of <b>parrots</b>, perched in the campaka trees.</div>
<div><b>Through the Bila.</b> The Goddess rose through an opening in the earth, the <b>Bila</b>, and destroyed Bhaṇḍāsura. The Bila gate beside Tapa Kāmākṣī marks the spot, and leads to the sacred tree called the <b>Bilākāśa</b>.</div>
</div>'''+talk("Is that why she's shown with a parrot?","The parrot is the gods' own disguise. And in Kāñcī's songs, it's the bird that carries your prayer to her.")))
pages.append(page('mango','THE LEGEND · THE MANGO TREE','Pārvatī wins Śiva back',fig(560,180,'Parvati embracing a small sand lingam under a mango tree as a flood rises around them',
 '<rect width="560" height="180" fill="#eaf6ff"/>'+MANGO(280,150,1.2)+LINGA(300,150,.9)+GENTLE(250,100,.8)+'<path d="M0 150 q60 -12 120 0 t120 0 t120 0 t120 0 t120 0 V180 H0z" fill="#4aa3df" opacity=".8"/>'+T(80,40,'VEGAVATĪ IN FLOOD',12,'#1d4f9a'))+'''<div class="steps">
<div><b>A playful mistake.</b> Pārvatī once covered Śiva’s eyes in play, and the worlds went dark. To atone, she came down to earth and settled at Kāñcī.</div>
<div><b>The sand liṅga.</b> Under a <b>mango tree</b> by the Vegavatī she made a liṅga of earth and worshipped it. Śiva tested her with a flood; she held the liṅga in her arms to save it.</div>
<div><b>The wedding.</b> Pleased, Śiva appeared and married her. The liṅga is worshipped as <b>Ekāmbareśvara</b>, “Lord of the single mango tree”, the earth liṅga among Śiva’s five element temples.</div>
</div><div class="panel reading small"><p>This is why Kāmākṣī is called the consort of every Śiva in Kāñcī, and why the city’s Śiva temples have no Goddess shrine of their own.</p></div>'''))
pages.append(page('history','HISTORY','From the Pallavas to today',tl([
 ('5th–8th c.','The temple may have been founded by the <b>Pallava</b> kings of Kāñcī.'),
 ('9th c.','The Āḻvārs’ hymns in the Divya Prabandham praise the Viṣṇu shrine now inside the temple, Tirukkaḷvaṉūr.'),
 ('14th c.','Major rebuilding; one historian credits it to the <b>Cholas</b>. The temple is modified again in the 17th century.'),
 ('After 1565','With the fall of Vijayanagara, the temple’s attendants carry the <b>golden image</b> away for safety.'),
 ('1739–1781','The golden Kāmākṣī rests in the Tyāgarāja temple at <b>Tiruvārūr</b>.'),
 ('Late 18th c.','She is taken to <b>Thanjavur</b>, under the Maratha kings, and stays there.'),
 ('Today','About <b>5 acres</b>; administered by the state’s endowments department, with the head of the Kāñci Kāmakoṭi Pīṭham as hereditary trustee.')])
 +'<div class="panel reading small"><p>Dates for the early temple are uncertain; one legend even gives 1783 for its construction. The 14th-century Chola date comes from a single recent study.</p></div>'))
pages.append(page('golden','THE GOLDEN KĀMĀKṢĪ','From Kāñcī to Thanjavur',fig(560,170,'Priests carrying a small golden Goddess image in a palanquin along a road from Kanchi past Tiruvarur to Thanjavur',
 '<rect width="560" height="170" fill="#fff4cd"/><path d="M20 150 Q180 120 300 140 T540 120" stroke="#c9a26b" stroke-width="8" fill="none"/>'+GOPK(40,140,.5)+T(40,164,'KĀÑCĪ',11,'#7a1d12')+TEMPLE(300,140,.9)+T(300,164,'TIRUVĀRŪR',11,'#7a1d12')+TEMPLE(520,120,1.0,'#ffd60a')+T(520,150,'THANJAVUR',11,'#7a1d12')
 +'<g transform="translate(170 110)" stroke="#111" stroke-width="2"><path d="M-60 0 h120" stroke="#7a5a2a" stroke-width="5"/><rect x="-18" y="-30" width="36" height="30" fill="#c0392b"/><path d="M-22 -30 h44 l-22 -16z" fill="#e0a800"/>'+'</g>'+GENTLE(170,94,.25).replace('#e05a8a','#ffd60a')+person(116,120,'#ff8c1a','#c98b5a',.6)+person(224,120,'#ff8c1a','#c98b5a',.6))+'''<div class="steps">
<div><b>Why she left.</b> In the troubled years after Vijayanagara fell, the priests feared for the temple’s treasures. The golden image was carried south; tradition names a devotee called <b>Kāmākṣī Dāsar</b>.</div>
<div><b>A long road.</b> She rested for decades in Tiruvārūr, then came to <b>Thanjavur</b>, where the Maratha kings gave her a temple of her own: <b>Bangāru Kāmākṣī</b> (Telugu <i>bangāru</i>, “gold”). Her face is dark; her body, gold.</div>
<div><b>A composer’s goddess.</b> <b>Śyāmā Śāstri</b>, one of the Trinity of Carnatic music, was born into her priestly family and served her as priest. His songs to Kāmākṣī are among the loveliest in the music.</div>
</div>'''))
pages.append(page('kamakoti','THE KĀMAKOṬI PĪṬHAM','The maṭha and Ādi Śaṅkara',fig(560,130,'A small shrine to Adi Shankara with a saffron-robed teacher holding a staff, beside the temple tower',
 '<rect width="560" height="130" fill="#fdf1e8"/>'+GOPK(140,126,.9)+person(330,110,'#ff8c1a','#f2c79b',1.1)+'<path d="M352 30 v90" stroke="#7a5a2a" stroke-width="4"/>'+T(330,124,'ĀDI ŚAṄKARA',11,'#7a1d12')+TEMPLE(470,120,1.2))+'''<div class="g2">
<div class="card bg-red"><h4>🙏 The maṭha’s view</h4><p>The <b>Kāñci Kāmakoṭi Pīṭham</b> holds that Ādi Śaṅkara himself founded it at Kāñcī, consecrated the Śrī Cakra, and ended his life here. The maṭha is closely tied to the temple; its head is hereditary trustee.</p></div>
<div class="card bg-yellow"><h4>📚 The other view</h4><p>The <b>Śṛṅgeri</b> maṭha and many historians do not accept that Śaṅkara founded a maṭha at Kāñcī; they place his life in the 8th century and his death in the Himalaya. One view sees the Kumbakonam maṭha as a branch that grew independent.</p></div>
</div><div class="panel reading"><p><b>What both share.</b> Whatever its founding, the temple keeps a shrine to Śaṅkara, and the hymns and rites of Śrīvidyā linked with his name are central to worship here.</p></div>'''))
pages.append(page('hymns','IN THE HYMNS','Poets, a mute boy and a composer',fig(560,130,'A young boy who could not speak suddenly singing before the Goddess, verses flowing from him',
 '<rect width="560" height="130" fill="#fff4cd"/>'+person(140,110,'#ff8c1a','#c98b5a',1)+''.join(f'<text x="{180+k*34}" y="{70-k*8}" font-size="20">♪</text>' for k in range(5))+KAMAKSHI(440,80,.65))+facts([
 ('Mūka Pañcaśatī','<b>500 verses</b> in five centuries (Āryā, Pādāravinda, Stuti, Kaṭākṣa, Mandasmita), by <b>Mūka Kavi</b>, a mute boy who, the legend says, found his voice by her grace. The Kāmakoṭi maṭha counts him as one of its early heads'),
 ('Lalitā Sahasranāma','Temple tradition says <b>Hayagrīva</b> taught Lalitā’s thousand names to the sage <b>Agastya</b> here; a Hayagrīva shrine marks the spot'),
 ('Śyāmā Śāstri','Many kṛtis, most of them addressed to Kāmākṣī, sung to the golden image he served'),
 ('The 18 hymn','<i>Kāmākṣī kāñcikāpure</i>: the line that names her among the eighteen')])))
pages.append(page('temple','THE TEMPLE','What stands where',fig(560,200,'Plan view of the temple: outer wall, gopura, golden vimana over the sanctum, Gayatri mandapa, tank, and small shrines',
 '<rect width="560" height="200" fill="#f3e3c3"/><rect x="40" y="16" width="480" height="170" fill="#fff4cd" stroke="#111" stroke-width="3"/><rect x="250" y="160" width="60" height="26" fill="#e2cfa8" stroke="#111" stroke-width="2"/>'+T(280,198,'GOPURA',10,'#555')
 +'<rect x="220" y="40" width="120" height="90" fill="#fde4e4" stroke="#111" stroke-width="2"/>'+VIM(280,86,1.1)+T(280,120,'GĀYATRĪ MAṆḌAPA',10,'#7a1d12')
 +'<rect x="70" y="40" width="100" height="60" fill="#4aa3df" stroke="#111" stroke-width="2"/>'+T(120,74,'TANK',11,'#fff')
 +''.join(TEMPLE(x,y,.55)+T(x,y+14,t,9,'#555') for x,y,t in ((400,60,'HAYAGRĪVA'),(460,60,'ŚAṄKARA'),(400,120,'VARĀHA'),(460,120,'BANGĀRU'),(120,150,'BILA'))))+facts([
 ('Area','About <b>5 acres</b>, in the heart of the old city'),
 ('Vimāna','The sanctum tower is covered in gold'),
 ('Inner shrines','Tapa and Añjana Kāmākṣī, Bangāru and Utsava Kāmākṣī, Ādi Śaṅkara, Sarasvatī, Hayagrīva with Agastya, and <b>Kaḷvar Perumāḷ</b> (Varāha), a Divya Deśam moved inside when its own shrine fell'),
 ('Daily','Four services a day, beginning with worship of a <b>cow</b> and an <b>elephant</b> at dawn')])))
pages.append(page('festivals','THROUGH THE YEAR','Her festivals',facts([
 ('Māsi','The great annual festival (Feb–Mar), with chariot and float festivals, ending in <b>Māsi Pūram</b>'),
 ('Navarātri','Nine nights of the Goddess'),
 ('Āḍi &amp; Aippasi Pūram','Her star-days in the Tamil months of Āḍi and Aippasi'),
 ('Vasantotsavam','The spring festival in Vaikāsi'),
 ('Śaṅkara Jayanti','For Ādi Śaṅkara'),
 ('Fridays','Every Friday is hers; Fridays of <b>Āḍi</b> and <b>Tai</b> most of all')])
 +talk("Elephants in the dawn worship?","A cow and an elephant are honoured before the doors open. Kāñcī starts its day with the Goddess's own animals.")+'<div class="key">Māsi Pūram, Navarātri and her Fridays: <b>the Goddess’s calendar</b>.</div>'))
pages.append(page('city','THE CITY OF TEMPLES','Kāñcī around Kāmākṣī',fig(560,140,'Several temple towers of different heights across the city skyline',
 '<rect width="560" height="140" fill="#fdf1e8"/>'+''.join(GOPK(x,136,s) for x,s in ((60,.8),(170,1.1),(300,.9),(420,.7),(510,.9)))+''.join(T(x,24,t,10,'#7a1d12') for x,t in ((60,'KUMARAKOṬṬAM'),(170,'EKĀMBARA'),(300,'KĀMĀKṢĪ'),(420,'KAILĀSANĀTHA'),(510,'VARADARĀJA'))))+facts([
 ('Ekāmbareśvara','The earth liṅga of the mango-tree legend; Kāmākṣī’s consort'),
 ('Kailāsanātha','Pallava stone temple of about 700 CE, one of the oldest in the city'),
 ('Varadarāja','The great Viṣṇu temple of “Viṣṇu Kāñcī”'),
 ('Kumarakoṭṭam','Murukaṉ’s temple, between Śiva and Śakti'),
 ('Ādi Pīṭheśvarī','A small old shrine near Kumarakoṭṭam that some call the original Kāmākṣī; the temple’s “Ādi Kāmākṣī” shrine is identified as Kāḷikāmbā')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Kāmākṣī','She whose eyes are love'),('Kāmakoṭi','Her seat; also the name of the maṭha'),('Padmāsana','The lotus posture'),('Śrī Cakra','The diagram of Lalitā'),
 ('Śrīvidyā','The tradition of Lalitā worship'),('Bila','An opening in the earth; a cave'),('Bangāru','Gold (Telugu)'),('Utsava','Festival; the procession image'),
 ('Mokṣapurī','A city that grants liberation'),('Kṛti','A Carnatic song'),('Divya Deśam','One of the 108 Viṣṇu temples sung by the Āḻvārs')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Goddess.</b> Kāmākṣī, Lalitā Tripurasundarī, seated in padmāsana with noose, goad, sugarcane bow and flower arrows; the navel-seat of Satī.</div>
<div><b>The legends.</b> Bhaṇḍāsura and the parrot-gods; Pārvatī’s sand liṅga under the mango tree; Lakṣmī’s lost beauty.</div>
<div><b>The Śrī Cakra.</b> Durvāsas first, Śaṅkara after, in a hall of 24 pillars.</div>
<div><b>The gold.</b> Bangāru Kāmākṣī’s journey to Thanjavur, and Śyāmā Śāstri’s songs.</div>
<div><b>The voices.</b> The Mūka Pañcaśatī, the Lalitā Sahasranāma, and a debate over Śaṅkara and the maṭha.</div>
</div>'''+talk("One line to remember?","The one Goddess of a city of Śivas. Every temple in Kāñcī is her husband's.")+'<div class="key">The second seat of the Mother: <b>Kāmākṣī of Kāñcī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Kamakshi Amman Temple”: padmāsana facing south-east; noose, goad, sugarcane bow, flower arrows; three forms; five forms of Kāmākṣī; Śrī Yantra by Durvāsas and Śaṅkara; Gāyatrī Maṇḍapa (24 pillars, four Vedas); Bila gate and Bilākāśa; about 5 acres; Kāmakoṭi Pīṭham as trustee; Pallava founding (5th–8th c.); Chola 14th c. (Babu 2020); a legend of 1783; Āḻvārs; 1565; Tiruvārūr 1739–1781; Kāmākṣī Dāsar; panchaloha replacement; Añjana Kāmākṣī and Lakṣmī; Varāha (Kaḷvar Perumāḷ); Bhaṇḍāsura and the parrots; Pārvatī and Ekāmbareśvara; Gō and Gaja pūjā; Māsi festival, Pūrams, Vasantotsavam, Śaṅkara Jayanti, Fridays; only Śakti shrine of Kāñcī; Hayagrīva and Agastya; Ādi Kāmākṣī as Kāḷikāmbā. Wikipedia, “Thanjavur Bangaru Kamatchiamman Temple” (Śyāmā Śāstri’s family). Wikipedia, “Kanchi Kamakoti Peetham” (founding disputed; Śṛṅgeri’s position; the 1821 Kumbakonam view). kamakoti.org and other sources on the Mūka Pañcaśatī.</p>
<p><b>Sources differ:</b> body part (navel or back); the founding period; when the golden image reached Thanjavur and under which king. <b>Not verified:</b> the claim that the original Kāmākṣī shrine was Ādi Pīṭheśvarī, or a Jain shrine; the dates in the Kāmakoṭi maṭha’s own chronology. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('goddess','The Goddess'),('forms','Five Forms of Kāmākṣī'),('chakra','The Śrī Cakra'),('bhanda','Legend · Bhaṇḍāsura'),('mango','Legend · The Mango Tree'),
 ('history','History'),('golden','The Golden Kāmākṣī'),('kamakoti','The Kāmakoṭi Pīṭham'),('hymns','In the Hymns'),('temple','The Temple'),('festivals','Through the Year'),('city','The City of Temples'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 2 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">KĀMĀKṢĪ</h1>
  <div class="series">KĀÑCĪPURAM · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess whose eyes are love</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Kāñcīpuram is a city of Śiva temples, and of one Goddess. In the city’s great Śiva temples there is no separate shrine for his consort, because she lives in one place: <b>Kāmākṣī</b>, seated in yoga at the centre of the city.</p>
    <p>She is Lalitā, who rose from the earth to destroy Bhaṇḍāsura; Pārvatī, who held a sand liṅga through a flood; the Goddess of the Śrī Cakra, of a mute poet’s five hundred verses, and of a golden image that travelled to Thanjavur.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Kāmākṣī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is Kāmākṣī the same Goddess as Lalitā?","The same. Kāñcī is where Lalitā sits as Kāmākṣī, and the Śrī Cakra in front of her says so.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Kamakshi.html','w').write(head+b+tail())
print('ok',len(pages))
