exec(open('/home/claude/work/shakti/common_s.py').read())
psrc=open('/home/claude/work/shakti/pithapuram.py').read()
exec('def gd('+psrc.split('def gd(')[1].split('\ndef ROOSTER(')[0])
head=head_red('Māṇikyāmbā · Drākṣārāmam · The 18 Śakti Pīṭhas · srini.presents',
 'Māṇikyāmbā of Drākṣārāmam, the twelfth of the 18 Śakti Pīṭhas: Dakṣa’s sacrifice on this very spot, Satī’s left cheek, Bhīmeśvara and the Pañcārāmas from Tārakāsura’s broken liṅga, the Sapta Godāvarī tank, Vyāsa’s Southern Kāśī, Śrīnātha’s Bhīmakhaṇḍam and the Eastern Chalukya king Bhīma. An illustrated reference guide.')
def MANI(x,y,s=1): return GENTLE(x,y,s).replace('#e05a8a','#c0392b')
def LINGA2(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-70" y="-10" width="140" height="10" fill="#c9a26b"/><path d="M-60 -10 v-6 h120 v6" fill="#c9a26b"/>'
 '<rect x="-18" y="-150" width="36" height="134" rx="18" fill="#e8eef2"/>'+''.join(f'<path d="M-14 {-140+k*8} q14 4 28 0" stroke="#333" stroke-width="2" fill="none"/>' for k in range(4))
 +'<path d="M-90 -80 h180" stroke="#7a5a2a" stroke-width="6"/><rect x="-90" y="-80" width="180" height="70" fill="none" stroke="#7a5a2a" stroke-width="2" stroke-dasharray="6 4"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The Goddess Manikyamba with a jewel, beside a tall crystal linga with dark stripes rising through two storeys">'
 '<rect width="380" height="268" fill="#4a0e0e" rx="8"/><circle cx="110" cy="40" r="24" fill="#ffd166" opacity=".7"/>'+LINGA2(270,250,1.3)+MANI(110,170,1.1)+'<circle cx="110" cy="108" r="7" fill="#e0115f" stroke="#111"/></svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Māṇikyāmbā</b>, “the ruby Mother”'),
 ('Lord','<b>Bhīmeśvara</b>: Śiva as a very tall liṅga, white with dark stripes on top'),
 ('Where','<b>Drākṣārāmam</b>, Konaseema district, Andhra Pradesh, in the Godāvarī delta'),
 ('Pīṭha','Satī’s <b>left cheek</b> fell here'),
 ('Hymn place','<b>Dakṣavāṭikā</b>: “Dakṣa’s garden”, where his sacrifice took place'),
 ('Also','One of the five <b>Pañcārāmas</b> and the three <b>Triliṅga</b> shrines of the Telugu land'),
 ('Built','By the Eastern Chalukya king <b>Bhīma I</b>, around 900 CE'),
 ('Nickname','<b>Dakṣiṇa Kāśī</b>, the Southern Kāśī')])
 +talk("The sacrifice where Satī died happened here?","That's this town's claim: Dakṣa's own garden. The story of all the Pīṭhas begins on this ground.")))
pages.append(page('where','WHERE IT IS','In the Godāvarī delta',fig(560,280,'Simplified map of the Godavari delta: Draksharamam south of Rajahmundry, near Kakinada, with Pithapuram and Samalkot to the north-east',
 GMAP([(16.79,82.06,'DRĀKṢĀRĀMAM','r','#c0392b'),(17.12,82.25,'Pīṭhāpuram','r','#bbb'),(17.05,82.17,'Sāmarlakoṭa','l','#bbb'),(17.00,81.78,'Rājamahendravaram','r','#bbb'),(16.96,82.24,'Kākināḍa','r','#bbb')]))
 +'<div class="g2"><div>'+minimap([10,12],'Map of India marking Pithapuram and Draksharamam, the tenth and twelfth Shakti Pithas')+'</div><div class="panel reading small"><p><b>Two Pīṭhas close together.</b> Drākṣārāmam and Pīṭhāpuram (No. 10) sit a short way apart in the same delta.</p><p><b>Delta country.</b> Paddy, coconut and canals: the Godāvarī splits into many mouths here before reaching the sea.</p></div></div>'))
pages.append(page('names','THE NAMES','Dakṣa’s garden',facts([
 ('Dakṣārāma','“Dakṣa’s pleasure-garden” → Drākṣārāmam'),
 ('Dakṣavāṭikā · Dakṣatapovana','Old names: Dakṣa’s garden, Dakṣa’s forest of penance'),
 ('Māṇikyāmbā','<i>māṇikya</i> “ruby” + <i>ambā</i> “mother”'),
 ('Bhīmeśvara','“Lord Bhīma”: after the Chalukya king Bhīma, or Śiva the mighty'),
 ('Dakṣiṇa Kāśī','“Southern Kāśī”: the name Vyāsa gave it')])
 +talk("A grape garden?","Drākṣā does mean grape, but the name is really Dakṣa-ārāma. The grapes crept in later.")))
pages.append(page('daksha','THE LEGEND · DAKṢA’S SACRIFICE','It began here',fig(560,170,'A grand sacrificial fire with a proud king presiding; a woman in red stepping toward it; an empty seat where Shiva should be',
 '<rect width="560" height="170" fill="#2a1a1a"/>'+FLAME(280,140,1.6)+KING(140,150,1.1,'#5a2a6a')+'<g transform="translate(420 150)">'+person(0,0,'#c0392b','#f2c79b',1)+'</g><rect x="470" y="120" width="40" height="30" fill="none" stroke="#ffd166" stroke-width="2" stroke-dasharray="4 3"/>'+T(490,112,'NO SEAT',10,'#ffd166'))+'''<div class="steps">
<div><b>The insult.</b> Dakṣa, chief of the Prajāpatis and Satī’s father, held a great sacrifice and invited every god except his son-in-law Śiva: a <b>nirīśvara yāga</b>, a sacrifice without the Lord.</div>
<div><b>Satī goes.</b> She went anyway, hoping for a welcome. Her father insulted her husband in front of everyone.</div>
<div><b>The fire.</b> Satī gave up her body in the sacrificial fire. Śiva’s fury destroyed the sacrifice; then, grieving, he carried her body across the world.</div>
<div><b>Here.</b> Drākṣārāmam holds that this was Dakṣa’s own garden, and that Satī’s <b>left cheek</b> later fell back on the same ground.</div>
</div>'''+talk("Don't other places claim the sacrifice too?","Kanakhal by Haridvār is the best-known claim. Drākṣārāmam's is the southern one. Both are honoured.")))
pages.append(page('goddess','MĀṆIKYĀMBĀ','The ruby Mother',fig(560,170,'A small shrine in the corner of a temple courtyard, the Goddess inside facing to her left',
 '<rect width="560" height="170" fill="#fdf1e8"/><rect x="40" y="40" width="480" height="120" fill="none" stroke="#7a5a2a" stroke-width="3"/>'+TEMPLE(280,130,1,'#ffe1a8')+'<rect x="60" y="90" width="80" height="60" fill="#ffd0c0" stroke="#111" stroke-width="2"/>'+MANI(100,140,.5)+'<path d="M70 60 l-20 0" stroke="#c0392b" stroke-width="3"/><path d="M50 60 l8 -5 v10z" fill="#c0392b"/>'+T(100,80,'facing left',10,'#7a1d12'))+facts([
 ('Shrine','In the back left corner of the temple enclosure, by most accounts'),
 ('Facing','She looks to her <b>left</b>: read as a sign of <b>vāmācāra</b>, the “left-hand” Tantric worship once offered here'),
 ('Local legend','A devoted girl named Māṇikyāmbā, who longed for Śiva, won Bhīmeśvara as her husband'),
 ('Equal footing','One of the few temples where Lord and Goddess are given equal importance')])
 +talk("Why would facing left matter?","In Tantra, 'left' is the secret, powerful path. Her gaze keeps the memory of how she was once worshipped.")))
pages.append(page('pancharama','THE PAÑCĀRĀMAS','One liṅga, five temples',fig(560,170,'A demon with a linga around his neck; a young six-faced warrior hurling a spear; the linga breaking into five glowing pieces',
 '<rect width="560" height="170" fill="#1a0e1e"/>'+'<g transform="translate(140 150)">'+person(0,0,'#5a4a6a','#5a4a6a',1.2)+'<circle cy="-10" r="8" fill="#fff" stroke="#111"/></g>'+'<g transform="translate(420 150)">'+person(0,0,'#ff8c1a','#f2c79b',1.1)+'<path d="M-20 -30 L-120 -60" stroke="#e0a800" stroke-width="4"/></g>'+''.join(f'<rect x="{230+i*22}" y="{60+(i%2)*20}" width="10" height="20" rx="5" fill="#fff" stroke="#ffd166" stroke-width="2"/>' for i in range(5)))+'<table class="ct"><tr><th>Ārāma</th><th>Place</th><th>Installed by</th></tr>'
 '<tr><td><b>Drākṣārāma</b></td><td>Drākṣārāmam</td><td>Sūrya, the Sun</td></tr><tr><td><b>Amarārāma</b></td><td>Amarāvatī</td><td>Indra</td></tr><tr><td><b>Somārāma</b></td><td>Bhīmavaram</td><td>Candra, the Moon</td></tr>'
 '<tr><td><b>Kṣīrārāma</b></td><td>Pālakollu</td><td>Viṣṇu</td></tr><tr><td><b>Kumārārāma</b></td><td>Sāmarlakoṭa</td><td>Kumāra (Skanda)</td></tr></table>'
 '<div class="panel reading small"><p><b>The legend.</b> The demon <b>Tārakāsura</b> wore a liṅga at his throat that made him unbeatable. <b>Kumāra</b> shattered it; the five pieces fell in the Telugu land and began to rejoin, chanting Oṃ, so five gods fixed them in place.</p></div>'))
pages.append(page('linga','BHĪMEŚVARA','A liṅga two storeys tall',fig(560,230,'A cutaway of a two-storey sanctum: a tall linga rising from the ground floor through the ceiling, with worshippers on the upper floor offering at its top',
 '<rect width="560" height="230" fill="#efe4cc"/>'+LINGA2(280,220,1.3)+person(160,120,'#c0392b','#c98b5a',.8)+person(400,120,'#2a9d6f','#c98b5a',.8)+T(70,40,'UPPER FLOOR',11,'#7a1d12','start')+T(70,210,'GROUND FLOOR',11,'#7a1d12','start'))+facts([
 ('Height','Very tall, around 2.6 m by one account (some say nearly 9 ft): it rises through two floors'),
 ('Worship','The base is seen on the ground floor; the top is bathed and worshipped from the upper floor'),
 ('Look','White, crystal-like stone with dark stripes on the upper part'),
 ('Svayambhū','Held to be self-born; tradition says Sūrya installed it'),
 ('Triliṅga','With Śrīśailam and Kāleśvaram, one of the three liṅgas said to give the Telugu land its name')])
 +'<div class="key">See also: <a href="/bhakti/temples-of-india/12-jyotirlingas/mallikarjuna/">Śrīśailam (Mallikārjuna)</a></div>'))
pages.append(page('vyasa','VYĀSA’S SOUTHERN KĀŚĪ','The hungry sage',fig(560,160,'An angry sage with raised hand in a city; a goddess offering him a bowl of food; then the sage walking south',
 '<rect width="560" height="160" fill="#fdf1e8"/>'+person(120,150,'#ff8c1a','#d8b090',1.1)+'<path d="M140 100 l20 -20" stroke="#d8b090" stroke-width="5"/>'+MANI(260,120,.5).replace('#c0392b','#ff8c1a')+'<ellipse cx="230" cy="110" rx="14" ry="6" fill="#fff" stroke="#111"/>'+'<path d="M330 120 h120" stroke="#111" stroke-width="3"/><path d="M450 120 l-10 -6 v12z" fill="#111"/>'+person(490,150,'#ff8c1a','#d8b090',.9))+'''<div class="steps">
<div><b>No alms.</b> In Kāśī, the sage <b>Vyāsa</b> and his disciples went a day without food. Furious, Vyāsa raised his hand to curse the city.</div>
<div><b>Annapūrṇā.</b> The Goddess Annapūrṇā fed them, and Śiva told the angry sage to leave Kāśī.</div>
<div><b>Go south.</b> The Goddess sent him to Drākṣārāmam, “equal to Kāśī”. Vyāsa settled here, worshipped Bhīmeśvara and called it <b>Dakṣiṇa Kāśī</b>.</div>
</div>'''+talk("Vyāsa got thrown out of Kāśī?","For losing his temper. Even the greatest sage had to learn patience, and found a second Kāśī in the bargain.")
 +'<div class="key">See also: <a href="/bhakti/temples-of-india/12-jyotirlingas/kashi-vishwanath/">Kāśī Viśvanātha</a></div>'))
pages.append(page('saptagodavari','SAPTA GODĀVARĪ','Seven rivers in one tank',facts([
 ('What','The temple tank, east of the shrine'),
 ('Legend','The seven sages, the <b>Saptarṣis</b>, each brought a stream of the Godāvarī here to bathe the Lord: seven Godāvarīs in one'),
 ('Late','The river was late in coming, by one telling; Śiva had already appeared on his own'),
 ('Bath','A dip here before darśana is held to equal bathing in the Godāvarī')])
 +talk("The Godāvarī came late for Śiva?","And he didn't wait. That's why they say Bhīmeśvara is self-born.")))
pages.append(page('temple','THE TEMPLE','A fortress of stone',fig(560,180,'A walled temple like a fortress with two concentric enclosures and a two-storey pillared shrine at the centre',
 '<rect width="560" height="180" fill="#efe4cc"/><rect x="40" y="30" width="480" height="140" fill="#d8c8a8" stroke="#111" stroke-width="3"/><rect x="100" y="60" width="360" height="100" fill="#e8dcc0" stroke="#111" stroke-width="2"/>'
 +''.join(f'<rect x="{150+i*30}" y="96" width="10" height="56" fill="#c9a26b" stroke="#111"/>' for i in range(9))+'<rect x="140" y="80" width="280" height="16" fill="#c9a26b" stroke="#111" stroke-width="2"/>'+TEMPLE(280,80,1,'#e2cfa8'))+facts([
 ('Builder','<b>Bhīma I</b> of the <b>Eastern Chalukyas</b> of Veṅgī, around 892–922 CE'),
 ('Plan','Two enclosing walls, like a fort; the inner shrine is built on two storeys'),
 ('Twin','The Kumārārāma temple at Sāmarlakoṭa, by the same king, follows almost the same plan'),
 ('Inscriptions','Hundreds, in Telugu, Sanskrit and Tamil: Chalukyas, Cholas, Velanāṭi Coḍas, Kākatīyas, Reḍḍis'),
 ('Later','Patronage from the Cholas and the Vijayanagara kings')])))
pages.append(page('srinatha','ŚRĪNĀTHA’S BHĪMAKHAṆḌAM','A poet’s praise',facts([
 ('Poet','<b>Śrīnātha</b>, the great Telugu poet of the Reḍḍi courts (c. 1400)'),
 ('Work','<b>Bhīmakhaṇḍam</b> (Bhīmeśvara Purāṇam): Drākṣārāmam’s glory in Telugu verse, based on the Skanda Purāṇa'),
 ('Tells','The Pañcārāmas, Vyāsa’s Southern Kāśī, Māṇikyāmbā and Bhīmeśvara'),
 ('Skanda Purāṇa','The Sanskrit source tradition credits to Vyāsa')])
 +talk("A whole book on one temple?","Śrīnātha wrote it like a love letter. Telugu readers still quote it.")))
pages.append(page('festivals','THROUGH THE YEAR','Śiva and Śakti together',facts([
 ('Mahāśivarātri','The great night of Bhīmeśvara, with the divine wedding (Kalyāṇam)'),
 ('Kārtika','Mondays and the full moon of Kārtika draw crowds to all five Pañcārāmas'),
 ('Navarātri','Māṇikyāmbā’s festival in Āśvina'),
 ('Pañcārāma yātrā','Pilgrims try to see all five ārāmas in one day, especially in Kārtika')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Ārāma','Garden, retreat'),('Māṇikya','Ruby'),('Nirīśvara yāga','A sacrifice without the Lord'),('Vāmācāra','Left-hand Tantric worship'),('Svayambhū','Self-born'),
 ('Triliṅga','The three liṅgas of the Telugu land'),('Saptarṣi','The seven sages'),('Prākāra','Enclosing wall'),('Kalyāṇam','Divine wedding')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Pīṭha.</b> Satī’s left cheek, on the ground where Dakṣa held his sacrifice: Māṇikyāmbā, facing left.</div>
<div><b>The Lord.</b> Bhīmeśvara, a striped liṅga two storeys tall; a Pañcārāma and a Triliṅga.</div>
<div><b>The legends.</b> Tārakāsura’s broken liṅga; Vyāsa’s Southern Kāśī; seven Godāvarīs in one tank.</div>
<div><b>The temple.</b> A stone fortress of the Eastern Chalukya king Bhīma, around 900 CE.</div>
<div><b>The poem.</b> Śrīnātha’s Bhīmakhaṇḍam.</div>
</div>'''+talk("One line to remember?","Where Satī's story began, her cheek came back to rest, beside the tallest liṅga in the delta.")+'<div class="key">The twelfth seat of the Mother: <b>Māṇikyāmbā of Drākṣārāmam</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Daksharamam” (Konaseema district; Pañcārāma and Triliṅga; 12th of the Aṣṭādaśa Pīṭhas; Dakṣatapovana and Dakṣavāṭikā; nirīśvara yāga; renovated by the Eastern Chalukyas; Sapta Godāvarī and the Saptarṣis). pilgrimaide.com (left cheek; Sūrya installed the liṅga; Vyāsa; Bhīma, 9th–10th c.; inscriptions; Chalukya-Chola style, two storeys, two prākāras). temples-site (Bhīma I, 892–922). myoksha.com (2.6 m liṅga; two storeys). bhaktikalpa.com (striped liṅga, nearly 9 ft; Vyāsa and Annapūrṇā; Dakṣiṇa Kāśī). religionworld.in (Māṇikyāmbā looks left; vāmamārga; local legend of the girl; Śrīnātha’s Bhīmakhaṇḍam). sakalam.org (shrine in the back left corner; vāmācāra). templefolks.com (Godāvarī came late; svayambhū; Triliṅga). gotirupati.com and thedivineindia.com (Tārakāsura and the five pieces).</p>
<p><b>Sources differ:</b> the liṅga’s height; Śrīnātha’s century (c. 1400; one source says 14th c.); whether Dakṣa’s sacrifice was here or at Kanakhal. <b>Not verified:</b> the Sāmarlakoṭa twin plan; the count of inscriptions. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('daksha','Legend · Dakṣa’s Sacrifice'),('goddess','Māṇikyāmbā'),('pancharama','The Pañcārāmas'),('linga','Bhīmeśvara'),('vyasa','Vyāsa’s Southern Kāśī'),
 ('saptagodavari','Sapta Godāvarī'),('temple','The Temple'),('srinatha','Śrīnātha’s Bhīmakhaṇḍam'),('festivals','Through the Year'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 12 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7.4vw,74px)">MĀṆIKYĀMBĀ</h1>
  <div class="series">DRĀKṢĀRĀMAM · A REFERENCE GUIDE</div>
  <div class="tag">The ruby Mother, in Dakṣa’s garden</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Every Śakti Pīṭha begins with one story: Dakṣa’s sacrifice, where Satī gave up her life. In the Godāvarī delta, the town of <b>Drākṣārāmam</b>, “Dakṣa’s garden”, says that sacrifice happened right here, and that Satī’s left cheek fell back on the same ground.</p>
    <p>There she is <b>Māṇikyāmbā</b>, the ruby Mother. Her Lord, <b>Bhīmeśvara</b>, is a striped liṅga so tall that it is worshipped from an upper floor, one of five pieces of a demon’s shattered liṅga.</p>
    <p>This guide tells those legends, the temple of an Eastern Chalukya king, and how Vyāsa found a second Kāśī here.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Māṇikyāmbā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is this a Śiva temple or a Goddess temple?","Both, equally. Bhīmeśvara draws the Śaivas, Māṇikyāmbā the Śāktas, and everyone visits both.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Manikyamba_Draksharamam.html','w').write(head+b+tail())
print('ok',len(pages))
