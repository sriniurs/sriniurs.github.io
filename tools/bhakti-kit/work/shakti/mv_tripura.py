exec(open('/home/claude/work/shakti/mv_common.py').read())
import math
head=head_red('Tripurasundarī · Daśa Mahāvidyā 3 · srini.presents',
 'Tripurasundarī, also Ṣoḍaśī, Lalitā and Rājarājeśvarī, the third of the Daśa Mahāvidyā: the most beautiful in the three worlds, the Lalitopākhyāna and Bhaṇḍāsura, the Lalitā Sahasranāma and Saundarya Laharī, Śrīvidyā and the Śrī Cakra, Bālā, and the Tripura Sundarī temple at Udaipur. An illustrated reference guide.')
def SRICHAKRA(x,y,r=80):
    g=f'<g transform="translate({x} {y})" stroke="#111" stroke-width="1.6"><rect x="{-r-24}" y="{-r-24}" width="{2*r+48}" height="{2*r+48}" fill="#ffe8a8"/>'
    g+=f'<circle r="{r+10}" fill="#f2a6c0"/>'+''.join(f'<ellipse cx="{(r+6)*math.cos(a*math.pi/8):.1f}" cy="{(r+6)*math.sin(a*math.pi/8):.1f}" rx="9" ry="5" transform="rotate({a*22.5} {(r+6)*math.cos(a*math.pi/8):.1f} {(r+6)*math.sin(a*math.pi/8):.1f})" fill="#e0115f"/>' for a in range(16))
    g+=f'<circle r="{r}" fill="#fff4cd"/>'
    for k,(h,up) in enumerate(((0.95,1),(0.7,1),(0.5,1),(0.3,1),(0.9,0),(0.75,0),(0.55,0),(0.4,0),(0.2,0))):
        s=r*h; dy=(-1 if up else 1)
        off=(k%3-1)*r*0.12
        g+=f'<path d="M{-s:.1f} {off+dy*-s*0.55:.1f} L{s:.1f} {off+dy*-s*0.55:.1f} L0 {off+dy*s*0.9:.1f}z" fill="none" stroke="{"#c0392b" if up else "#3b4fa0"}" stroke-width="2"/>'
    return g+'<circle r="4" fill="#c0392b"/></g>'
def LALITA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<rect x="-60" y="40" width="120" height="14" fill="#c9a26b"/>'+''.join(f'<rect x="{dx}" y="54" width="8" height="24" fill="#c9a26b"/>' for dx in (-56,-20,12,48))
 +'<path d="M-30 40 q-4 -50 30 -66 q34 16 30 66z" fill="#c0392b"/><path d="M-22 -10 l-26 -20 M22 -10 l26 -20 M-22 4 l-30 4 M22 4 l30 4" stroke="#f2a07a" stroke-width="7"/>'
 '<path d="M-52 -38 q-14 26 0 52" stroke="#2a9d6f" stroke-width="4" fill="none"/><path d="M48 -36 l6 -14 l6 14" stroke="#ff8c1a" stroke-width="3" fill="none"/><circle cx="-56" cy="10" r="6" fill="none" stroke="#e0a800" stroke-width="3"/><path d="M56 8 l8 -8 l4 6" stroke="#bbb" stroke-width="3" fill="none"/>'
 '<circle cy="-40" r="15" fill="#f2a07a"/><path d="M-14 -52 h28 l-4 -16 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/><path d="M-4 -70 a7 7 0 1 0 9 3" fill="none" stroke="#fff8c0" stroke-width="2"/>'
 '<circle cx="-5" cy="-42" r="2.4" fill="#111"/><circle cx="5" cy="-42" r="2.4" fill="#111"/><circle cy="-49" r="2" fill="#c0392b"/><path d="M-5 -33 q5 4 10 0" fill="none"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The red goddess Lalita Tripurasundari seated on a throne holding a sugarcane bow and flower arrows, with the Sri Chakra glowing behind her">'
 '<rect width="380" height="268" fill="#5a0e2a" rx="8"/>'+SRICHAKRA(190,120,90).replace('#ffe8a8','#5a0e2a')+LALITA(190,180,.95)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Tripurasundarī</b>: “the most beautiful in the three worlds” (or “of the three cities”)'),
 ('Also','<b>Ṣoḍaśī</b>, <b>Lalitā</b>, <b>Rājarājeśvarī</b>, <b>Kāmeśvarī</b>, <b>Śrī Mātā</b>, <b>Kāmākṣī</b>'),
 ('Place','<b>Third</b> of the ten Mahāvidyās; supreme Goddess of the <b>Śrīkula</b>'),
 ('Look','Red and radiant; four arms with <b>sugarcane bow</b>, <b>five flower arrows</b>, noose and goad; crescent moon'),
 ('Consort','<b>Kāmeśvara</b>, Śiva as Lord of Desire'),
 ('Texts','Lalitopākhyāna of the <b>Brahmāṇḍa Purāṇa</b>, <b>Lalitā Sahasranāma</b>, <b>Saundarya Laharī</b>, Tripura Rahasya'),
 ('Symbol','The <b>Śrī Cakra</b> (Śrī Yantra)'),
 ('Temples','Tripura Sundarī, Udaipur (Tripurā); Kāmākṣī, Kāñcī; Rājarājeśvarī shrines across the south')])
 +talk("The fierce Kālī and the beautiful Lalitā in one list?","That's the Mahāvidyās. Kālī dissolves, Lalitā delights: the same Mother, at both ends.")))
pages.append(page('names','HER NAMES','Sixteen, sport, queen of queens',facts([
 ('Tripurasundarī','<i>tri-pura</i> “three cities / three worlds” + <i>sundarī</i> “beautiful”'),
 ('Ṣoḍaśī','“Sixteen”: the ever-sixteen-year-old; also her sixteen-syllable mantra'),
 ('Lalitā','“She who plays”: the universe is her game'),
 ('Rājarājeśvarī','“Queen of kings of kings”'),
 ('Kāmeśvarī','Wife of Kāmeśvara, Lord of Desire'),
 ('Śrī Mātā','“Holy Mother”: the very first name in her Thousand Names'),
 ('Bālā','Her child form, Bālā Tripurasundarī')])
 +talk("Why sixteen?","The moon has sixteen digits; the sixteenth never wanes. She is the part of us that never fades.")))
pages.append(page('form','HER FORM','Desire turned divine',fig(560,210,'The red goddess seated on a throne, holding a sugarcane bow, flower arrows, a noose and a goad, with a crescent moon in her crown',
 '<rect width="560" height="210" fill="#fdf1e8"/>'+LALITA(280,120,1.3))+facts([
 ('Sugarcane bow','The mind: sweet, bendable'),
 ('Five flower arrows','The five senses, and the five arrows of Kāma'),
 ('Noose (pāśa)','Attachment, which she binds'),
 ('Goad (aṅkuśa)','Anger, which she steers'),
 ('Throne','Brahmā, Viṣṇu, Rudra and Īśvara as its legs, Sadāśiva as the seat'),
 ('Colour','Red, like the rising sun, like the hibiscus')])
 +talk("She sits on the gods?","In Śrīvidyā the five great gods are her furniture. That's how highly Śrīkula ranks her.")))
pages.append(page('bhanda','LALITOPĀKHYĀNA · BHAṆḌĀSURA','A demon from the ashes of love',fig(560,180,'A goddess rising from a sacrificial fire on a chariot shaped like a wheel, leading an army against a demon born from ashes',
 '<rect width="560" height="180" fill="#2a1a1a"/>'+FLAME(140,160,1.2)+LALITA(140,90,.55)+'<path d="M200 120 h120" stroke="#ffd166" stroke-width="3" stroke-dasharray="6 4"/>'+DEMON(420,150,1.1,'#4a4a4a')+'<path d="M380 160 q40 -10 80 0" stroke="#999" stroke-width="6" fill="none"/>'+T(420,40,'BHAṆḌA',13,'#ffd166'))+'''<div class="steps">
<div><b>From ashes.</b> When Śiva burned <b>Kāma</b>, the god of love, one of Śiva’s attendants shaped a figure from the ashes. It came to life as the demon <b>Bhaṇḍāsura</b>, and won a boon that made him almost unbeatable.</div>
<div><b>A world without desire.</b> Bhaṇḍa conquered the worlds; with love gone, nothing grew.</div>
<div><b>From the fire.</b> The gods offered themselves into a great sacrifice. From the fire rose <b>Lalitā</b>, on the Śrī Cakra chariot.</div>
<div><b>Victory.</b> With her generals Mantriṇī (Śyāmalā) and Daṇḍanāthā (Vārāhī), she destroyed Bhaṇḍa and his armies, and brought Kāma back to life.</div>
</div>'''+talk("She kills a demon born of dead desire, and revives desire?","Exactly. Love without wisdom becomes a demon; wisdom brings love back to life.")))
pages.append(page('texts','THE GREAT TEXTS','Thousand names and a wave of beauty',facts([
 ('Lalitopākhyāna','The tale of Lalitā in the Brahmāṇḍa Purāṇa, told by Hayagrīva to the sage Agastya'),
 ('Lalitā Sahasranāma','Her Thousand Names, in the same Purāṇa: one of the most-chanted hymns in India, beginning <i>śrī mātā</i>'),
 ('Lalitā Triśatī','Her three hundred names, built on her mantra’s syllables'),
 ('Saundarya Laharī','“The Wave of Beauty”, a hundred verses attributed to Ādi Śaṅkara, on her form and the Śrī Cakra'),
 ('Tripura Rahasya','A dialogue on her as pure consciousness')])
 +'<div class="key">See also: <a href="/bhakti/devi/lalita-pancharatnam/">Lalitā Pañcaratnam</a> on this site</div>'))
pages.append(page('srichakra','THE ŚRĪ CAKRA','Her diagram, her body',fig(560,240,'The Sri Chakra: nine interlocking triangles, four pointing up and five down, inside circles of lotus petals and a square enclosure, with a dot at the centre',
 '<rect width="560" height="240" fill="#fdf1e8"/>'+SRICHAKRA(280,120,90))+facts([
 ('Triangles','<b>Nine</b> interlocking triangles: four pointing up (Śiva), five pointing down (Śakti), making 43 small triangles'),
 ('Lotuses','Rings of eight and sixteen petals'),
 ('Gates','A square outer wall with four gates'),
 ('Bindu','The central dot: the Goddess herself, in union with Śiva'),
 ('Meru','A three-dimensional, mountain-shaped Śrī Cakra is also worshipped'),
 ('Worship','In Śrīvidyā the Śrī Cakra <b>is</b> her subtle form')])
 +talk("A drawing that is the Goddess?","As a map is the city for the traveller. Śrīvidyā walks inward from the gates to the dot.")))
pages.append(page('srividya','ŚRĪVIDYĀ','The path of the Śrīkula',facts([
 ('What','The Tantric tradition centred on Lalitā Tripurasundarī and the Śrī Cakra'),
 ('Mantra','The secret <b>pañcadaśī</b> (fifteen-syllable) and ṣoḍaśī (sixteen) mantras, given by a guru'),
 ('Worship','Navāvaraṇa pūjā: worship of the nine enclosures of the Śrī Cakra'),
 ('Where','Strong in the south: Kāñcī, Śṛṅgeri, and households of Tamil Nadu, Kerala and Karnataka'),
 ('Śaṅkara','Śaṅkara’s maṭhas are linked to Śrīvidyā worship by tradition')])
 +talk("Can I worship the Śrī Cakra at home?","Many do, with simple offerings and the Sahasranāma. The full rites and mantras come from a teacher.")))
pages.append(page('bala','BĀLĀ TRIPURASUNDARĪ','The girl Goddess',facts([
 ('Who','Lalitā’s child form, a girl of about nine'),
 ('Story','In the Lalitopākhyāna, Bālā rides out and kills Bhaṇḍa’s thirty sons'),
 ('Worship','Often the first step in Śrīvidyā; Kumārī pūjā honours her in girls'),
 ('Temple','Nemili in Tamil Nadu is famous for Bālā')])))
pages.append(page('udaipur','TRIPURA SUNDARĪ, UDAIPUR','The Goddess of Tripurā',fig(560,180,'A square red and white Bengal-style temple on a small tortoise-shaped hill beside a lake',
 '<rect width="560" height="180" fill="#cfe3f5"/><ellipse cx="280" cy="170" rx="220" ry="30" fill="#3a8a3a"/><path d="M120 170 q160 -80 320 0z" fill="#5a8a4a" stroke="#111"/><rect x="380" y="150" width="160" height="30" fill="#4aa3df"/>'
 +'<g transform="translate(280 140)" stroke="#111" stroke-width="2"><rect x="-50" y="-50" width="100" height="50" fill="#c0392b"/><path d="M-56 -50 q56 -40 112 0z" fill="#fff"/><path d="M-20 -80 q20 -16 40 0 v-4 h-40z" fill="#fff"/><rect x="-12" y="-30" width="24" height="30" fill="#5a1a1a"/></g>')+facts([
 ('Where','Udaipur (old Rangamati), Gomati district, Tripurā'),
 ('Built','By Mahārāja <b>Dhanya Mānikya</b> of Tripurā, c. 1501'),
 ('Kūrma Pīṭha','The low hill is shaped like a tortoise (kūrma)'),
 ('Śakti Pīṭha','Counted among the 51: Satī’s right foot, by common lists'),
 ('Images','Two: the large Tripura Sundarī and the small Choṭi Mā (Caṇḍī), in black stone'),
 ('Name of the state','One theory derives “Tripurā” from the Goddess')])
 +'<div class="key">See also: <a href="/bhakti/temples-of-india/18-shakti-peethas/kamakshi/">Kāmākṣī of Kāñcī</a>, Lalitā in the south</div>'))
pages.append(page('kanchi','IN THE SOUTH','Kāmākṣī and Rājarājeśvarī',facts([
 ('Kāmākṣī','At Kāñcī she sits as Lalitā in yoga, before a Śrī Cakra installed, by tradition, by Śaṅkara'),
 ('Rājarājeśvarī','Temples in Bengaluru, Kerala and elsewhere'),
 ('Navarātri','In the south, Navarātri ends with Lalitā’s worship'),
 ('Homes','Lalitā Sahasranāma is chanted on Fridays and full moons in countless homes')])))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of beauty',facts([
 ('Beauty is divine','The world’s beauty is her play (līlā), not a trap'),
 ('Desire purified','The bow and arrows of love, held by wisdom'),
 ('Inward journey','The Śrī Cakra: from the outer gates of the senses to the inner dot of the Self'),
 ('Third wisdom','After Kālī’s dissolution and Tārā’s rescue, Tripurasundarī’s bliss')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Tripura','Three cities, three worlds'),('Ṣoḍaśī','Sixteen'),('Lalitā','She who plays'),('Pāśa · Aṅkuśa','Noose · goad'),('Śrī Cakra','Her yantra'),
 ('Bindu','The central point'),('Āvaraṇa','Enclosure'),('Pañcadaśī','Fifteen-syllable mantra'),('Kūrma','Tortoise')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Tripurasundarī, Ṣoḍaśī, Lalitā: the beauty of the three worlds, third Mahāvidyā.</div>
<div><b>Form.</b> Red, with sugarcane bow, flower arrows, noose and goad; Kāmeśvara’s queen.</div>
<div><b>Story.</b> Born from the gods’ fire to slay Bhaṇḍa and revive Kāma.</div>
<div><b>Texts and yantra.</b> Lalitā Sahasranāma, Saundarya Laharī, the Śrī Cakra and Śrīvidyā.</div>
<div><b>Temples.</b> Udaipur in Tripurā; Kāmākṣī and Rājarājeśvarī in the south.</div>
</div>'''+talk("One line to remember?","Beauty, held by wisdom, is the Goddess herself.")+'<div class="key">The third Great Wisdom: <b>Tripurasundarī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p>Wikipedia, “Tripura Sundari” (names Kāmākṣī, Kāmeśvarī, Lalitā, Rājarājeśvarī, Ṣoḍaśī, Śrī Mātā, Bālā; noose, goad, arrows and sugarcane bow; Śrī Yantra; Śrīkula and Śrīvidyā; Lalitā Sahasranāma and Saundarya Laharī; Lalitopākhyāna of the Brahmāṇḍa Purāṇa; Tripura Rahasya; Bhaṇḍāsura; Kāmeśvara; Udaipur temple). Standard accounts of the Śrī Cakra (nine triangles, 43 triangles, bindu) and of the Udaipur temple (Dhanya Mānikya, 1501; Kūrma Pīṭha; two images).</p>
<p><b>Sources differ:</b> meanings of “Tripura” and “Ṣoḍaśī”; the Udaipur Pīṭha body part. <b>Not verified:</b> Nemili and Bālā’s thirty-sons episode as given; the state-name theory. Mantras are deliberately not given. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('form','Her Form'),('bhanda','Lalitopākhyāna · Bhaṇḍāsura'),('texts','The Great Texts'),('srichakra','The Śrī Cakra'),('srividya','Śrīvidyā'),('bala','Bālā Tripurasundarī'),
 ('udaipur','Tripura Sundarī, Udaipur'),('kanchi','In the South'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 3 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(20px,6.4vw,64px)">TRIPURASUNDARĪ</h1>
  <div class="series">ṢOḌAŚĪ · LALITĀ · A REFERENCE GUIDE</div>
  <div class="tag">The most beautiful in the three worlds</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>After the darkness of Kālī and the blue night of Tārā comes the dawn: <b>Tripurasundarī</b>, red as the rising sun, the most beautiful being in the three worlds. In the south she is <b>Lalitā</b>, whose Thousand Names are chanted in homes every Friday; in Tantra she is <b>Ṣoḍaśī</b>, forever sixteen.</p>
    <p>She holds a bow of sugarcane and arrows of flowers. She was born from the gods’ sacrificial fire to destroy a demon made from the ashes of Love, and to bring Love back. Her body is a diagram: the Śrī Cakra.</p>
    <p>This guide tells her story, her texts, her yantra and her temples.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Śrī Mātre Namaḥ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is the Lalitā Sahasranāma about this Goddess?","The very same. Lalitā, Tripurasundarī and Ṣoḍaśī are three names for the third Mahāvidyā.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms. Previous: <a href="{MVS}tara/">Tārā</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV03_Tripurasundari.html','w').write(head+b+tail())
print('ok',len(pages))
