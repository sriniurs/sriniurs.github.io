exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Narasiṃha · Daśāvatāra 4 · srini.presents','Narasiṃha, the man-lion, fourth avatāra of Viṣṇu: Hiraṇyakaśipu’s clever boon, the child Prahlāda, Holikā and Holi, the pillar, the threshold at twilight, Prahlāda calming the Lord, the forms Ugra, Yoga and Lakṣmī Narasiṃha, the Hampi monolith, Melukote, Siṃhācalam, Mangalagiri, Yādagiri and Ahobilam. An illustrated reference guide.')
def LION(x,y,s=1,rage=True):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 50 q-4 -60 30 -70 q34 10 30 70z" fill="#ffd60a"/>'
     '<path d="M-22 -6 l-30 -16 M22 -6 l30 -16 M-22 8 l-28 6 M22 8 l28 6" stroke="#e0a800" stroke-width="7"/><circle cx="-54" cy="-24" r="8" fill="#fff8e7"/><circle cx="54" cy="-24" r="8" fill="none" stroke="#e0a800" stroke-width="4"/>'
     '<circle cy="-36" r="24" fill="#c06a1a"/><circle cy="-34" r="15" fill="#e0a800"/><circle cx="-5" cy="-38" r="2.6" fill="#111"/><circle cx="5" cy="-38" r="2.6" fill="#111"/>'
     +('<path d="M-6 -26 l3 4 l3 -4 l3 4 l3 -4" fill="none" stroke="#fff" stroke-width="2"/>' if rage else '<path d="M-6 -27 q6 4 12 0" fill="none"/>')+'<path d="M-12 -58 h24 l-4 -12 h-16z" fill="#e0a800"/></g>')
def PILLAR(x,y,h=150,broken=False): return f'<g stroke="#111" stroke-width="2"><rect x="{x-20}" y="{y-h}" width="40" height="{h}" fill="#d8c49a"/><rect x="{x-28}" y="{y-h-10}" width="56" height="12" fill="#c8b48a"/>'+(f'<path d="M{x-20} {y-h*0.6} l12 10 l10 -14 l8 12 l10 -8" fill="none" stroke-width="3"/>' if broken else '')+'</g>'
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The man-lion bursting out of a broken pillar at twilight while a child with folded hands watches">'
 '<rect width="380" height="268" fill="#3a1a2a" rx="8"/><circle cx="320" cy="60" r="30" fill="#e05a3a"/><circle cx="60" cy="50" r="18" fill="#fff8c0"/>'+PILLAR(150,250,170,True)+LION(170,170,1.4)+person(300,240,'#ffd60a','#f2c79b',.9)+'</svg>')
cov=cover_dv('DAŚĀVATĀRA 4 OF 10','NARASIṂHA',13,'He came out of the pillar for a child',art)
fw=foreword_dv('Keśava dhṛta-narahari-rūpa,',[
 'The fourth avatāra keeps a promise to a little boy. The demon king <b>Hiraṇyakaśipu</b> had won a boon that seemed to make him unkillable: no man or beast, no weapon, not by day or night, not inside or outside, not on the ground or in the sky could kill him. His son <b>Prahlāda</b>, though, would not stop praying to Viṣṇu.',
 '“Is your Viṣṇu in this pillar?” the king roared, and struck it. Out burst <b>Narasiṃha</b>, half man and half lion, at twilight. He carried the king to the threshold, laid him on his lap, and tore him apart with his claws: every condition of the boon kept, and broken.',
 'This guide tells the story, explains the many forms of the man-lion, and visits his temples, from Hampi’s giant to the hills of Ahobilam.'],
 'Wasn’t that too violent?','The anger was for the tyrant who tortured his own child. To Prahlāda the man-lion was gentle.',
 series_note_dv(4))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Avatāra','<b>Fourth</b> of the ten; Satya Yuga'),('Form','<b>Half man, half lion</b>'),
 ('Deed','Slays Hiraṇyakaśipu to save the child Prahlāda'),('Texts','Bhāgavata Purāṇa 7.1–10; Viṣṇu Purāṇa 1.16–20; Nṛsiṃha Purāṇa'),
 ('Forms','Ugra (fierce), Yoga (seated in meditation), Lakṣmī Narasiṃha (with Lakṣmī)'),('Festival link','Holi, from the story of Holikā'),
 ('Temples','Ahobilam, Siṃhācalam, Mangalagiri, Yādagiri, Melukote; the Hampi monolith'),('Day','Narasiṃha Jayantī, Vaiśākha, at dusk')])
 +talk("The scariest avatāra?","And the most loving. He came for one child who trusted him.")))
pages.append(page('names','NAMES','Man-lion',facts([
 ('Narasiṃha · Nṛsiṃha','<i>nara</i> man + <i>siṃha</i> lion'),('Narahari','Jayadeva’s word: <i>dhṛta-narahari-rūpa</i>'),('Ugra Narasiṃha','The fierce form'),('Yoga Narasiṃha','Seated in yoga, knees bound by a band'),('Lakṣmī Narasiṃha','Calm, with Lakṣmī on his lap'),('Prahlāda Varada','The boon-giver to Prahlāda')])))
pages.append(page('boon','THE PERFECT BOON','Hiraṇyakaśipu’s plan',facts([
 ('Revenge','Hiraṇyakaśipu hated Viṣṇu, who as Varāha had killed his twin, Hiraṇyākṣa'),
 ('Tapas','He did fierce penance until Brahmā granted a boon'),
 ('The boon','No being made by Brahmā could kill him: not man or beast, not by day or night, not inside or outside, not on earth or in the sky, by no weapon'),
 ('Tyranny','Believing himself immortal, he conquered the three worlds and forbade the worship of Viṣṇu'),
 ('The loophole','Every rule had a gap: twilight, a threshold, a lap, claws, and a being both man and beast')])
 +'<div class="key">The twin brother: <a href="'+DVS+'varaha/">Varāha and Hiraṇyākṣa</a></div>'))
pages.append(page('prahlada','PRAHLĀDA','The child who would not stop praying',fig(560,170,'A small boy with folded hands sitting calmly among flames while a woman burns',
 '<rect width="560" height="170" fill="#2a1a1a"/>'+''.join(EL('fire',x,150,1.2) for x in (180,220,260,300,340,380))+person(280,130,'#ffd60a','#f2c79b',.8)+'<path d="M266 110 l14 -8 l14 8" fill="none" stroke="#f2c79b" stroke-width="3"/>')+facts([
 ('In the womb','Prahlāda heard the sage Nārada’s teaching while still in his mother Kayādhū’s womb'),
 ('At school','Asked what he had learned, he praised Viṣṇu'),
 ('Trials','His father had him attacked by soldiers, trampled by elephants, bitten by snakes, poisoned and thrown from a cliff; each time he was saved'),
 ('Holikā','His aunt Holikā, immune to fire, sat in a fire with him on her lap; she burned and he walked out unharmed'),
 ('Holi','The bonfire of Holikā Dahan, the night before Holi, remembers it')])
 +talk("So Holi comes from this story?","The bonfire on Holi eve does. Good survives the fire; Holikā doesn't.")))
pages.append(page('pillar','THE PILLAR','“Is he in this?”',fig(560,190,'An angry king striking a pillar in a palace hall with a small boy watching',
 '<rect width="560" height="190" fill="#4a2a1a"/>'+PILLAR(300,180,160)+KING(170,170,1.2)+'<path d="M200 110 l70 -6" stroke="#bbb" stroke-width="5"/>'+person(430,176,'#ffd60a','#f2c79b',.8))+'''<div class="steps">
<div><b>The question.</b> “Where is your Viṣṇu?” the king demanded. “Everywhere,” said Prahlāda.</div>
<div><b>The challenge.</b> “Is he in this pillar?” “He is.”</div>
<div><b>The blow.</b> The king struck the pillar with his fist (or his mace).</div>
<div><b>The roar.</b> The pillar split with a terrible sound, and the man-lion stepped out.</div>
</div>'''+talk("Was God hiding in the pillar?","Not hiding. Prahlāda said he was everywhere; the pillar just proved it.")))
pages.append(page('death','EVERY CONDITION KEPT','How the boon was beaten',fig(560,180,'The man-lion seated on a doorstep at sunset holding the demon king across his lap',
 '<rect width="560" height="180" fill="#e07a4a"/><circle cx="460" cy="60" r="30" fill="#ffd60a"/><rect x="200" y="140" width="160" height="16" fill="#8a6a4a" stroke="#111" stroke-width="2"/><rect x="200" y="20" width="18" height="120" fill="#8a6a4a" stroke="#111" stroke-width="2"/><rect x="342" y="20" width="18" height="120" fill="#8a6a4a" stroke="#111" stroke-width="2"/>'+LION(280,120,.9)+DEMON(280,140,.5))+facts([
 ('Not man nor beast','Narasiṃha was both'),('Not day nor night','At twilight (sandhyā)'),('Not inside nor outside','On the threshold of the palace'),
 ('Not earth nor sky','On his own lap'),('No weapon','With his claws'),('Not made by Brahmā','The Lord himself, not a created being')])))
pages.append(page('calm','THE RAGE AND THE CHILD','Who could calm him?',fig(560,170,'A small boy with folded hands before a seated lion-faced god, now calm',
 '<rect width="560" height="170" fill="#fff4dc"/>'+LION(320,130,1.0,False)+person(170,160,'#ffd60a','#f2c79b',.9))+facts([
 ('Fury','Even after the demon died, Narasiṃha’s anger shook the worlds'),
 ('The gods','Brahmā, Śiva and the gods were afraid to approach; even Lakṣmī hesitated'),
 ('Prahlāda','The child went forward and sang his praise; the Lord grew calm and placed his hand on the boy’s head'),
 ('His wish','Offered any boon, Prahlāda asked only for freedom from desire, and forgiveness for his father'),
 ('Śarabha','A Śaiva tradition says Śiva came as the Śarabha to calm him; Vaiṣṇava texts tell it differently')])
 +talk("Even Lakṣmī was scared?","The story says so. Only innocence could walk up to him.")))
pages.append(page('forms','FORMS OF NARASIṂHA','Fierce, meditating, gentle',fig(560,170,'Three figures: a fierce man-lion, a seated meditating man-lion with a band around his knees, and a calm man-lion with a goddess',
 '<rect width="560" height="170" fill="#eef3fa"/>'+LION(110,130,.8)+LION(280,130,.8,False)+'<path d="M254 160 q26 -14 52 0" stroke="#e04040" stroke-width="5" fill="none"/>'+LION(450,130,.8,False)+GENTLE(480,140,.45))+facts([
 ('Ugra','Standing, tearing the demon: the moment of rescue'),
 ('Yoga','Seated in meditation, a yoga band (yogapaṭṭa) around his knees'),
 ('Lakṣmī','Calm, with Lakṣmī on his left thigh: most loved in homes'),
 ('Sthauṇa','Emerging from the pillar'),
 ('Nava Narasiṃha','Nine forms, worshipped together at Ahobilam')])
 +'<div class="key">Read: <a href="'+TI+'ahobilam/">Ahobilam: the Nine Narasiṃhas</a></div>'))
pages.append(page('hampi','THE GIANT OF HAMPI','Lakṣmī Narasiṃha monolith',fig(560,180,'A giant seated man-lion carved from a single rock, with a person tiny beside it',
 '<rect width="560" height="180" fill="#f2e6c8"/>'+LION(280,170,1.9,False)+'<path d="M190 180 q90 -40 180 0" stroke="#5a3a2a" stroke-width="10" fill="none"/>'+person(450,178,'#7a5a2a','#c98b5a',.6))+facts([
 ('Where','Hampi, Vijayanagara, Karnataka'),
 ('What','A seated man-lion carved from a single granite boulder, about 6.7 m high, with a seven-headed serpent hood above'),
 ('When','1528, in the time of Kṛṣṇadevarāya'),
 ('Lakṣmī','A Lakṣmī figure once sat on his lap; it was broken in the sack of 1565, so he is often called Ugra Narasiṃha'),
 ('Restored','The yoga band and parts were restored by the Archaeological Survey of India')])
 +talk("Why was Lakṣmī removed?","She was smashed in the destruction of the city. Only her hand on his back remains.")))
pages.append(page('melukote','MELUKOTE','Yoga Narasiṃha on the hill',facts([
 ('Where','Melukote, Maṇḍya district, Karnataka, about 50 km from Mysuru'),
 ('Shrine','A hilltop temple of Yoga Narasiṃha above the town'),
 ('Prahlāda','Tradition says Prahlāda himself installed the image'),
 ('Rāmānuja','Melukote is a great centre of Śrī Vaiṣṇavism, where Rāmānuja lived for years'),
 ('Belief','Devotees climb the steps for courage and protection')])
 +'<div class="key">Full guide: <a href="'+TI+'around-mysuru/melukote/">Melukote</a></div>'))
pages.append(page('temples','OTHER GREAT TEMPLES','Andhra and Telangana',facts([
 ('Siṃhācalam','Near Vishakhapatnam: Varāha-Narasiṃha, covered all year in sandalwood paste; the true form is shown only on Akṣaya Tṛtīyā (Candanotsavam)'),
 ('Mangalagiri','Pānakāla Narasiṃha: devotees offer jaggery water, and tradition says the Lord drinks half of whatever is poured'),
 ('Yādagiri','Yādādri (Yādagirigutta), Telangana, rebuilt on a grand scale and reopened in 2022'),
 ('Ahobilam','Nine Narasiṃha shrines in the Nallamala hills, where the story is set'),
 ('Udayagiri','Cave 12 has one of the earliest Narasiṃha carvings, about 400 CE')])))
pages.append(page('ahobilam','WHERE IT HAPPENED','Ahobilam',facts([
 ('Tradition','Ahobilam is where Narasiṃha emerged and killed Hiraṇyakaśipu'),
 ('Ugra Stambha','A split rock pinnacle is pointed out as the pillar'),
 ('Name','“Aho balam!”, “What strength!”, cried the gods'),
 ('Nine shrines','Upper and Lower Ahobilam with nine Narasiṃhas')])
 +'<div class="key">Full guide: <a href="'+TI+'ahobilam/">Ahobilam</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','His days',facts([
 ('Narasiṃha Jayantī','Vaiśākha Śukla Caturdaśī (Apr–May), kept at dusk, the hour he appeared'),
 ('Holikā Dahan','The bonfire on the eve of Holi (Phālguna full moon)'),
 ('Candanotsavam','Siṃhācalam, on Akṣaya Tṛtīyā'),
 ('Pradoṣa','Twilight, his hour; some Vaiṣṇavas worship him then')])))
pages.append(page('meaning','WHAT NARASIṂHA TEACHES','The wisdom of the man-lion',facts([
 ('God is everywhere','Even in a pillar of stone'),
 ('No loophole for evil','Every clever plan has a gap'),
 ('Faith is protection','The child was safe in fire and before elephants'),
 ('Fierce love','Gentle to the devotee, terrible to the tyrant')])
 +talk("What should I take from Narasiṃha?","Trust like Prahlāda. Help comes from where you least expect, even from a pillar.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Nara · Siṃha','Man · lion'),('Sandhyā','Twilight'),('Stambha','Pillar'),('Yogapaṭṭa','Meditation band'),('Ugra','Fierce'),('Holikā Dahan','Holi-eve bonfire'),('Candana','Sandalwood'),('Pānaka','Jaggery drink')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Narasiṃha, the man-lion, fourth avatāra of Viṣṇu.</div>
<div><b>Story.</b> Hiraṇyakaśipu’s boon; Prahlāda’s faith; the pillar; death at twilight on the threshold.</div>
<div><b>Echoes.</b> Holikā and Holi; the child who calmed the Lord.</div>
<div><b>Temples.</b> Hampi’s giant, Melukote, Siṃhācalam, Mangalagiri, Yādagiri, Ahobilam.</div>
<div><b>Lesson.</b> God is everywhere, and fierce for those who trust him.</div>
</div>'''+talk("One line to remember?","Ask if he's in the pillar, and be ready for the answer.")+'<div class="key">Next: <a href="'+DVS+'vamana/">Vāmana, the dwarf</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Bhāgavata Purāṇa 7.1–10; Viṣṇu Purāṇa 1.16–20; Nṛsiṃha Purāṇa; Liṅga and Śiva Purāṇas (Śarabha).</p>
<p><b>Temples and art:</b> Hampi Lakṣmī Narasiṃha (1528; about 6.7 m; damaged 1565) from ASI and Karnataka Tourism; Melukote (Maṇḍya district) temple tradition; Siṃhācalam Candanotsavam; Mangalagiri Pānakāla; Yādādri reopening 2022; Udayagiri Cave 12 (Outlook Traveller); Ahobilam from our earlier guide.</p>
<p><b>Sources differ / unverified:</b> the details of Prahlāda’s trials; the Śarabha story is Śaiva and disputed by Vaiṣṇavas; the Hampi monolith’s height (6.7 m, sometimes 22 ft); the claim that Mangalagiri’s Lord drinks half the offering. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('boon','The Perfect Boon'),('prahlada','Prahlāda'),('pillar','The Pillar'),('death','Every Condition Kept'),('calm','The Rage and the Child'),('forms','Forms of Narasiṃha'),
 ('hampi','The Giant of Hampi'),('melukote','Melukote'),('temples','Other Great Temples'),('ahobilam','Where It Happened'),('festivals','Through the Year'),('meaning','What Narasiṃha Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV4_Narasimha.html',head,cov,fw,pages,toc)
