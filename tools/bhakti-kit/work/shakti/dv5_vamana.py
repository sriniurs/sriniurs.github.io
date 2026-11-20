exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Vāmana · Daśāvatāra 5 · srini.presents','Vāmana, the dwarf, fifth avatāra of Viṣṇu: the generous demon king Bali, Aditi’s prayer, the Brahmin boy with an umbrella, the gift of three steps, Śukra’s warning, Trivikrama spanning earth and heaven, the Gaṅgā born from his foot, Bali sent to Sutala with Viṣṇu as his gatekeeper, the Ṛgveda’s three strides, Onam and Tṛkkākara, Bali Pāḍyami in Karnataka, and Trivikrama in stone at Bādāmi and Mahābalipuram. An illustrated reference guide.')
def DWARF(x,y,s=1,umb=True): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-16 30 q-2 -26 16 -30 q18 4 16 30z" fill="#ffd60a"/><circle cy="-12" r="12" fill="#5b8fe0"/><path d="M-6 -24 h12 l-2 -6 h-8z" fill="#3a2a1a"/>'
 +('<path d="M-36 -36 q36 -24 72 0z" fill="#e8d8b0"/><path d="M0 -36 v40"/>' if umb else '')+'<path d="M16 8 h10 v14 h-10z" fill="#c9a26b"/><path d="M-10 -2 l20 0" stroke="#fff" stroke-width="1.5"/></g>')
def GIANT(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-20 0 v-90 M20 0 l70 -120" stroke="#3b6fd0" stroke-width="22"/><path d="M-30 -80 q-6 -80 30 -90 q40 10 34 90z" fill="#ffd60a"/>'
 '<circle cy="-190" r="20" fill="#3b6fd0"/><path d="M-18 -206 h36 l-6 -18 h-24z" fill="#e0a800"/><path d="M-26 -140 l-40 -30 M26 -140 l40 -30" stroke="#3b6fd0" stroke-width="10"/></g>')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A small boy with an umbrella beside a giant blue figure striding across earth and sky">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/>'+STAR+'<rect y="236" width="380" height="32" fill="#5a9a4a"/>'+GIANT(250,240,1.0)+DWARF(80,224,1.1)+'</svg>')
cov=cover_dv('DAŚĀVATĀRA 5 OF 10','VĀMANA',16,'Three small steps that measured the worlds',art)
fw=foreword_dv('Keśava dhṛta-vāmana-rūpa,',[
 'The fifth avatāra is a little boy with an umbrella and a water-pot. <b>Bali</b>, the good and generous demon king, grandson of Prahlāda, had conquered heaven itself. At his great sacrifice he promised to give anyone anything they asked. The boy, <b>Vāmana</b>, asked for just three steps of land.',
 'Bali laughed and agreed, though his guru warned him. Then the boy grew. With one step he covered the earth, with the second the heavens, and there was nowhere left for the third, so Bali offered his own head. Viṣṇu sent him to rule the underworld, and promised to stand guard at his door.',
 'In Kerala, Bali comes home every year at <b>Onam</b>; in Karnataka he is remembered on <b>Bali Pāḍyami</b>. This guide tells the story and its long life, from the Ṛgveda’s three strides to the festivals of today.'],
 'Wasn’t Bali a good king? Why trick him?','That is the great question of this story. The texts honour Bali as much as Vāmana.',
 series_note_dv(5))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Avatāra','<b>Fifth</b> of the ten; first in human form; Tretā Yuga'),('Form','<b>A dwarf</b> Brahmin boy, who grows into <b>Trivikrama</b>, “of the three steps”'),
 ('Deed','Takes back the three worlds from Bali with three strides'),('Texts','Bhāgavata Purāṇa 8.15–23; Vāmana Purāṇa; Ṛgveda 1.154 (the three strides)'),
 ('Bali','Generous demon king, grandson of Prahlāda; sent to rule Sutala'),('Festivals','Onam (Kerala); Bali Pāḍyami (Karnataka, Mahārāṣṭra)'),
 ('Temple','Tṛkkākara Vāmanamūrti, near Kochi'),('Art','Trivikrama panels at Bādāmi, Mahābalipuram, Ellora')])
 +talk("The first human avatāra?","Yes, and a tiny one. After fish, tortoise, boar and man-lion, God comes as a child.")))
pages.append(page('names','NAMES','Dwarf and giant',facts([
 ('Vāmana','Dwarf'),('Trivikrama','“Of the three strides”'),('Urukrama · Urugāya','“Wide-striding”: Vedic names of Viṣṇu'),('Upendra','“Younger Indra”: born to Aditi after Indra'),('Ulagaḷanda Perumāḷ','Tamil: “the Lord who measured the world”'),('Tṛkkākarayappan','Kerala: the Lord of Tṛkkākara')])))
pages.append(page('bali','BALI, THE GENEROUS DEMON','Grandson of Prahlāda',fig(560,160,'A crowned king giving gifts to a line of people',
 '<rect width="560" height="160" fill="#fff4dc"/>'+KING(170,140,1.1)+''.join(person(300+i*50,146,c,'#c98b5a',.7) for i,c in enumerate(('#e08a2a','#3b8fd0','#2a9d6f','#e05a3a'))))+facts([
 ('Family','Son of Virocana, grandson of Prahlāda'),
 ('Virtue','Just, devoted and so generous that no one left his court empty-handed'),
 ('Power','With his guru Śukrācārya’s rites he defeated Indra and ruled the three worlds'),
 ('The problem','Even a good ruler of heaven upset the order: the gods were homeless'),
 ('Name','Mahābali, “great Bali”, as Kerala calls him')])
 +talk("A demon who was a good king?","Asura doesn't always mean wicked. Bali is one of the most loved figures in these stories.")))
pages.append(page('aditi','ADITI’S PRAYER','The mother of the gods',facts([
 ('Grief','Aditi, mother of Indra and the gods, grieved for her exiled sons'),
 ('The vow','Her husband, the sage Kaśyapa, taught her the payovrata, a twelve-day vow of milk'),
 ('The promise','Viṣṇu appeared and promised to be born as her son'),
 ('The birth','He was born as a dwarf Brahmin boy, and the gods gave him his thread, staff, umbrella, deerskin and water-pot')])))
pages.append(page('gift','THREE STEPS OF LAND','The request',fig(560,180,'A small boy with an umbrella before a king pouring water from a pot into his hand, while a guru warns',
 '<rect width="560" height="180" fill="#fdf1e8"/><rect y="150" width="560" height="30" fill="#d8c49a"/>'+DWARF(160,140,1.3)+KING(330,150,1.1)+person(470,150,'#f4f4f4','#c98b5a',.9)+'<path d="M300 100 q-40 -10 -110 10" stroke="#5ab0f0" stroke-width="4" fill="none" stroke-dasharray="4 4"/>')+'''<div class="steps">
<div><b>The sacrifice.</b> Bali was holding a great horse sacrifice at Bhṛgukaccha on the Narmadā, giving gifts to all.</div>
<div><b>The boy.</b> Vāmana arrived, glowing. Bali offered him villages, gold, elephants. The boy asked only for three steps of land, measured by his own feet.</div>
<div><b>The warning.</b> Śukrācārya saw who the boy was and begged Bali to refuse. Bali would not break his word.</div>
<div><b>The water.</b> A gift was sealed by pouring water. Folk tellings say Śukra hid in the spout of the pot to block it, and Vāmana cleared it with a blade of grass, costing the guru an eye.</div>
</div>'''))
pages.append(page('steps','TRIVIKRAMA','The three strides',fig(560,200,'A giant figure with one foot on the earth and the other raised into the stars, a king bowing below',
 '<rect width="560" height="200" fill="#1d1040"/>'+STAR+'<rect y="176" width="560" height="24" fill="#5a9a4a"/>'+GIANT(300,190,.85)+KING(130,186,.7))+facts([
 ('Growth','The boy grew until his head passed the stars'),
 ('First step','The whole earth'),
 ('Second step','The heavens, up to the world of Brahmā'),
 ('Third step','There was nothing left. Bali bowed and said: “Place it on my head.”'),
 ('The Gaṅgā','Brahmā washed the foot that reached his world; that water became the heavenly Gaṅgā, which flows from Viṣṇu’s foot (Viṣṇupadī)')])
 +talk("The Gaṅgā came from his foot?","In this story, yes. That is why Gaṅgā is called Viṣṇupadī.")))
pages.append(page('sutala','BALI IN SUTALA','The guard at his door',facts([
 ('Sutala','Viṣṇu sent Bali to Sutala, a realm below the earth more splendid than heaven'),
 ('The boon','Viṣṇu himself would stand at Bali’s door, mace in hand, as his gatekeeper'),
 ('The future','Bali will be Indra in a coming age (the Sāvarṇi Manvantara)'),
 ('Prahlāda','His grandfather came to rejoice, for Bali had won the Lord himself'),
 ('Return','Kerala and Karnataka traditions say he may visit his people once a year')])
 +talk("God became his doorman?","That's how the Bhāgavata honours Bali. He gave everything; he got God.")))
pages.append(page('vedic','THE THREE STRIDES OF THE ṚGVEDA','The oldest root',facts([
 ('Ṛgveda 1.154','Viṣṇu “who measured out the earthly realms in three strides”, in whose highest step there is a well of honey'),
 ('Urukrama','He is praised as wide-striding (urukrama, urugāya)'),
 ('Brāhmaṇas','The Śatapatha Brāhmaṇa tells how the gods, as Viṣṇu the dwarf, won from the demons as much land as he could lie upon'),
 ('Meaning','The three steps were read as earth, sky and heaven, or as the sun’s rising, zenith and setting')])
 +'<div class="panel reading"><p><i>chalayasi vikramaṇe balim adbhuta-vāmana, pada-nakha-nīra-janita-jana-pāvana; keśava dhṛta-vāmana-rūpa jaya jagadīśa hare</i></p><p class="small">Jayadeva, Gītagovinda: “Wondrous dwarf, by your strides you outwit Bali; the water from your toenail purifies the people.”</p></div>'))
pages.append(page('onam','ONAM','Kerala welcomes Mahābali',fig(560,170,'A floral carpet in a circle with a crowned king figure beside it',
 '<rect width="560" height="170" fill="#fff4dc"/>'+''.join(f'<circle cx="200" cy="96" r="{r}" fill="{c}" stroke="#111" stroke-width="1.5"/>' for r,c in ((70,'#ffd60a'),(56,'#e0501a'),(42,'#f2a6c0'),(28,'#2a9d6f'),(14,'#fff')))+KING(420,150,1.1))+facts([
 ('When','The Malayalam month of Chingam (Aug–Sep), ten days from Atham to Tiruvōṇam'),
 ('Belief','Mahābali returns to see his people, and they show him they are happy'),
 ('Customs','Flower carpets (pookkalam), the great feast (sadya), boat races, new clothes'),
 ('Vāmana too','At Tṛkkākara, Vāmana is honoured as well'),
 ('Old record','Tṛkkākara temple inscriptions hold the earliest known mention of Onam, from 861 CE')])
 +talk("Kerala celebrates the defeated king?","Lovingly. Onam remembers a golden age when 'all men were equal'.")))
pages.append(page('thrikkakara','TṚKKĀKARA','The Vāmana temple',facts([
 ('Where','Tṛkkākara, near Kochi, Kerala, said to be Mahābali’s capital'),
 ('Deity','Vāmana, shown about to place his foot on Bali; also called Tṛkkākarayappan'),
 ('Divya Deśam','One of the 108 Viṣṇu temples sung by the Āḻvārs'),
 ('Two temples','A Śiva temple stands beside it, said to be the one Bali worshipped at'),
 ('Ten avatāras','During Onam, the deity is dressed each day as a different avatāra')])
 +'<div class="key">See: <a href="'+DVS+'overview/">All ten avatāras</a></div>'))
pages.append(page('pradyami','BALI PĀḌYAMI','Karnataka and Mahārāṣṭra',facts([
 ('When','Kārttika Śukla Pratipadā, the day after Dīpāvalī’s new moon'),
 ('Karnataka','Bali Pāḍyami: homes welcome Bali, with lamps and images made of cow dung or rice flour'),
 ('Mahārāṣṭra','Bali Pratipadā; the saying “Iḍā pīḍā javo, Balīcē rājya yevo”: may troubles go and Bali’s rule return'),
 ('Meaning','The good king’s yearly visit, at the brightest festival of the year')])
 +talk("So Karnataka has its own Onam?","In spirit, yes. Bali's day sits right in Dīpāvalī.")))
pages.append(page('art','TRIVIKRAMA IN STONE','Bādāmi, Mahābalipuram, Ellora',facts([
 ('Bādāmi','Caves 2 and 3 (6th c., Chalukya): huge Trivikrama panels, leg raised to the sky'),
 ('Mahābalipuram','The Varāha cave (7th c., Pallava) has a dramatic Trivikrama'),
 ('Ellora','Daśāvatāra cave (Cave 15), 8th c.'),
 ('Ulagaḷanda Perumāḷ','Kāñcīpuram: a towering image of Trivikrama in a Divya Deśam'),
 ('Tirukkōvalūr','Another Divya Deśam of Trivikrama in Tamil Nadu')])))
pages.append(page('festivals','THROUGH THE YEAR','His days',facts([
 ('Vāmana Jayantī','Bhādrapada Śukla Dvādaśī (Aug–Sep)'),('Onam','Chingam (Aug–Sep), Kerala'),('Bali Pāḍyami','Kārttika (Oct–Nov), Karnataka and Mahārāṣṭra'),('Trivikrama','Honoured in Vaiṣṇava temples on Ekādaśīs')])))
pages.append(page('meaning','WHAT VĀMANA TEACHES','The wisdom of three steps',facts([
 ('Humility','The greatest came smallest'),
 ('Keep your word','Bali gave even his head rather than break a promise'),
 ('Giving wins God','Bali lost the worlds and gained the Lord'),
 ('Ego is the third step','There is no room left but yourself; offer it')])
 +talk("What should I take from Vāmana?","Ask little, give all. And when there's nowhere left, bow your head.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Vāmana','Dwarf'),('Trivikrama','Of the three strides'),('Asura','Demon, anti-god'),('Sutala','A realm below the earth'),('Viṣṇupadī','Gaṅgā, from Viṣṇu’s foot'),('Pookkalam','Onam flower carpet'),('Pāḍyami','First day of the bright fortnight'),('Payovrata','Vow of milk')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Vāmana, the dwarf, fifth avatāra of Viṣṇu; Trivikrama.</div>
<div><b>Story.</b> Bali promises three steps; the boy grows; earth, heaven, and Bali’s head.</div>
<div><b>After.</b> Bali rules Sutala with Viṣṇu at his door; Gaṅgā flows from the foot.</div>
<div><b>Today.</b> Onam in Kerala; Bali Pāḍyami in Karnataka; Tṛkkākara.</div>
<div><b>Lesson.</b> Small asks, big gifts, a promise kept.</div>
</div>'''+talk("One line to remember?","Three little steps, and a king who gave his head.")+'<div class="key">Next: <a href="'+DVS+'parashurama/">Paraśurāma, Rāma with the axe</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Bhāgavata Purāṇa 8.15–23; Vāmana Purāṇa; Ṛgveda 1.154; Śatapatha Brāhmaṇa 1.2.5; Jayadeva, Gītagovinda 1.</p>
<p><b>Temple and festivals:</b> Wikipedia, “Thrikkakara Temple” (Vāmana about to step on Bali; earliest Onam record of 861 CE; Parasurāma founding tradition; ten-avatāra decorations); Kerala Tourism (Mahābali’s capital; two temples; Divya Deśam); Wikipedia, “Onam”; Bali Pratipadā from Karnataka and Maharashtra traditions.</p>
<p><b>Sources differ / unverified:</b> Śukra’s lost eye is a folk addition; the place of the sacrifice (Bhṛgukaccha in some texts); the Vāmana Jayantī date; Bādāmi cave numbering of the Trivikrama panels. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('bali','Bali, the Generous Demon'),('aditi','Aditi’s Prayer'),('gift','Three Steps of Land'),('steps','Trivikrama'),('sutala','Bali in Sutala'),('vedic','The Ṛgveda’s Three Strides'),
 ('onam','Onam'),('thrikkakara','Tṛkkākara'),('pradyami','Bali Pāḍyami'),('art','Trivikrama in Stone'),('festivals','Through the Year'),('meaning','What Vāmana Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV5_Vamana.html',head,cov,fw,pages,toc)
