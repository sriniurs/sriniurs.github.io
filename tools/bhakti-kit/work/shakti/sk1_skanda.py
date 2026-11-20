exec(open('/home/claude/work/shakti/sk_common.py').read())
head=head_navy('Who is Skanda? Subrahmaṇya, Kārttikeya, Murugan · Subrahmaṇya Ṣaṣṭhī 1 · srini.presents',
 'Who is Skanda, Śiva’s son? His many names (Kārttikeya, Kumāra, Ṣaṇmukha, Subrahmaṇya, Murugan), his birth in the reeds of Śaravaṇa and the six Kṛttikās, the six faces, the vel, the peacock and the rooster, Valli and Devasenā, the Praṇava and the fruit stories, the Six Abodes, and why Karnataka worships him as a serpent. An illustrated reference guide.')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The six-faced young god Skanda holding a tall spear, standing in front of a peacock with its tail spread, under a starry sky">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+'<circle cx="190" cy="120" r="96" fill="#e0701a" opacity=".3"/>'+PEACOCK(205,236,1.35)+SKANDA(160,170,1.2)+'</svg>')
cov=cover('PART 1 OF 4','WHO IS SKANDA?',13,'Śiva’s son, the six-faced god of the spear',art)
fw=foreword('Om Śaravaṇabhava,',[
 'He is the youngest of the gods and the general of their army. The north knows him as <b>Kārttikeya</b> or <b>Skanda</b>, Tamil Nadu as <b>Murugan</b>, and Karnataka as <b>Subrahmaṇya</b>, often worshipped in the form of a serpent.',
 'He was born for one job: to kill the demon Tāraka, whom no one but a son of Śiva could defeat. He was born in a bed of reeds, nursed by six star-mothers, given six faces, a spear by his mother and a peacock to ride.',
 'This first part meets the god himself. Part 2 tells the Ṣaṣṭhī story of his great war; Parts 3 and 4 visit his two great serpent shrines in Karnataka, Kukke and Ghāṭi.'],
 'Why so many names for one god?','Because almost every region of India loved him in its own way. Each name keeps one story.',
 series_note(nxt=('shashthi','The Ṣaṣṭhī Story')))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Who','Son of <b>Śiva</b> and <b>Pārvatī</b>; younger brother of Gaṇeśa in the south (in some northern tellings, the elder)'),
 ('Role','<b>Devasenāpati</b>, general of the gods’ army'),
 ('Born','In the reeds of the lake <b>Śaravaṇa</b>, raised by the six <b>Kṛttikās</b> (the Pleiades)'),
 ('Look','Ever young; one or six faces; holding the <b>vel</b> (spear)'),
 ('Mount and flag','The <b>peacock</b>; the <b>rooster</b> on his banner'),
 ('Consorts','<b>Devasenā</b> (Devayānai) and <b>Valli</b> in the south; a lifelong bachelor in many northern traditions'),
 ('Great deed','Killing the demons <b>Tāraka</b> and, in the Tamil telling, <b>Śūrapadma</b>'),
 ('Key day','<b>Ṣaṣṭhī</b>, the sixth lunar day: see Part 2')])
 +talk("Is he Śiva's son or Agni's?","Both, depending on the book. The fire carried Śiva's seed; most tellings call him Śiva's son.")))
pages.append(page('names','HIS NAMES','One god, many stories',facts([
 ('Skanda','“The one who leaps” or “attacks”: the spurt of Śiva’s energy'),
 ('Kumāra','“The youth”: he never grows old'),
 ('Kārttikeya','“Son of the Kṛttikās”, the six star-mothers who nursed him'),
 ('Ṣaṇmukha','“Six-faced” (Āṟumukham in Tamil)'),
 ('Śaravaṇabhava','“Born in the reeds”'),
 ('Guha','“The hidden one”, who lives in the cave of the heart'),
 ('Subrahmaṇya','Often read as “dear to the brāhmaṇas” or “of Brahman”; its meaning is debated'),
 ('Murugan','Tamil: “the beautiful”, the god of the hills; also Velan, “the spear-bearer”')])
 +talk("Which name should I use?","Any of them. In Karnataka, 'Subbarāya' or 'Subrahmaṇya Svāmi' is what grandmother says.")))
pages.append(story('why','WHY HE WAS BORN','A demon only a child could kill',560,180,'A huge demon on a throne laughing, while worried gods stand to one side and Shiva sits in meditation on a mountain',
 '<rect width="560" height="180" fill="#2a1a2a"/>'+DEMON(120,160,1.3,'#5a2a2a')+'<path d="M60 160 h120 v-20 h-120z" fill="#7a5a2a" stroke="#111" stroke-width="2"/>'+CROWD(250,170,5,20)+HILL(470,180,200,150,'#e8eef2')+SHIVA(470,70,.6),
 [('The boon.','The demon <b>Tāraka</b> won a boon from Brahmā: he could be killed only by a son of Śiva. Śiva, mourning Satī, was lost in meditation and had no wife. Tāraka felt safe.'),
  ('The terror.','Tāraka drove the gods from heaven. Indra and the gods went to Brahmā, who told them: only Śiva’s son can save you.'),
  ('Kāma’s arrow.','The gods sent <b>Kāma</b>, god of love, to wake Śiva. Śiva opened his third eye and burnt Kāma to ash.'),
  ('Pārvatī’s tapas.','Pārvatī won Śiva by her own fierce austerity, and they married. This is the story of Kālidāsa’s poem <b>Kumārasambhava</b>, “The Birth of the Prince”.'),
  ('The spark.','From Śiva came a blaze of energy so fierce that no one could hold it. Where it went next is the story of the birth.')],
 '<div class="key">Read more: <a href="'+FAM+'">Śiva’s Family and Symbols</a></div>'))
pages.append(story('birth','BORN IN THE REEDS','Fire, river, lake and six stars',560,190,'Six sparks falling into a lake of tall reeds, six babies on lotuses, and six women from the stars coming down to nurse them',
 '<rect width="560" height="190" fill="#0b2a4a"/>'+STAR+'<rect y="120" width="560" height="70" fill="#4aa3df"/>'
 +''.join(f'<path d="M{20+i*28} 190 v-{50+(i%3)*12}" stroke="#3a8a3a" stroke-width="4"/>' for i in range(20))
 +''.join(f'<g transform="translate({120+i*64} 140)" stroke="#111" stroke-width="1.5"><path d="M-14 0 q14 -14 28 0z" fill="#f2a6c0"/><circle cy="-10" r="7" fill="#e8a860"/></g>' for i in range(6))
 +''.join(f'<path d="M{130+i*60} 20 l-6 50" stroke="#ff8c1a" stroke-width="3" stroke-dasharray="4 4"/><circle cx="{130+i*60}" cy="18" r="5" fill="#ffd60a"/>' for i in range(6)),
 [('Agni carries it.','The fire-god <b>Agni</b> took Śiva’s blazing seed, but even he could not bear its heat.'),
  ('Gaṅgā cools it.','He gave it to the river <b>Gaṅgā</b>, who carried it to a lake of reeds, <b>Śaravaṇa</b>, in the Himalaya.'),
  ('Six boys.','There it became <b>six</b> shining boys, each on a lotus. In the Tamil Kanda Purāṇam, six sparks from Śiva’s six faces go straight there.'),
  ('Six mothers.','The six <b>Kṛttikās</b>, the stars of the Pleiades, came down and nursed them. So he is <b>Kārttikeya</b>.'),
  ('One child.','<b>Pārvatī</b> came and embraced all six at once, and they became one child with six faces and twelve arms.')],
 talk("Why six?","Six mothers, six faces, six days of war, the sixth lunar day. With Skanda, everything comes in sixes.")))
pages.append(page('six','THE SIX FACES','What Ṣaṇmukha sees',fig(560,170,'A six-faced young god, his heads in a row, with a ring of six small stars around him',
 '<rect width="560" height="170" fill="#eaf1fb"/>'+''.join(f'<circle cx="{280+120*__import__("math").cos(i*1.047)}" cy="{90+60*__import__("math").sin(i*1.047)}" r="7" fill="#ffd60a" stroke="#111" stroke-width="2"/>' for i in range(6))+SKANDA(280,110,1,vel=False))+facts([
 ('Six directions','North, south, east, west, above and below: he sees in every direction at once'),
 ('Six mothers','One face for each Kṛttikā who nursed him'),
 ('Six seasons','The six ṛtus of the Indian year'),
 ('Six qualities','A common teaching: wisdom, dispassion, strength, fame, wealth and divine power'),
 ('Six syllables','His six-syllabled name, Śa-ra-va-ṇa-bha-va, chanted by devotees as “Om Śaravaṇabhava”'),
 ('In art','Six-faced images are firmly established after about the 6th century; earlier ones usually show one face')])
 +talk("Are these meanings in the old books?","Some are, some are later teaching. The six mothers are the oldest reason.")))
pages.append(page('emblems','THE VEL, THE PEACOCK, THE ROOSTER','His three signs',fig(560,180,'A tall golden spear, a peacock with spread tail, and a rooster on a saffron flag',
 '<rect width="560" height="180" fill="#fdf1e8"/>'+VEL(90,170,1.1,110)+PEACOCK(280,165,.95)+FLAG(450,170,1.1))+facts([
 ('Vel','A spear with a leaf-shaped blade, given by his mother <b>Pārvatī</b>. Tamil devotees read its long shaft and broad tip as knowledge: deep, wide and sharp'),
 ('Peacock','His mount, Paravāṇi in Tamil. In the Tamil telling, it is half of the defeated demon Śūrapadma; many read it as pride tamed'),
 ('Rooster','On his banner (Cēval-koṭi); the other half of Śūrapadma, crowing at dawn'),
 ('Snake','Under the peacock’s feet in many images: the peacock eats snakes, yet in Karnataka the god himself is a serpent. More in Parts 3 and 4')])
 +'<div class="key">“Vetrivel Muruganukku Arōharā!”: Victory to Murugan of the conquering spear.</div>'))
pages.append(story('pranava','THE TEACHER OF HIS FATHER','The meaning of Om',560,170,'A small six-faced boy seated on a high seat explaining, while a large blue Shiva listens; a four-faced Brahma stands to one side, ashamed',
 '<rect width="560" height="170" fill="#eaf1fb"/>'+'<rect x="200" y="120" width="80" height="20" fill="#e0a800" stroke="#111" stroke-width="2"/>'+SKANDA(240,80,.6,vel=False)+SHIVA(380,80,.85)+'<g transform="translate(100 100)" stroke="#111" stroke-width="2"><path d="M-20 60 q-2 -54 20 -62 q22 8 20 62z" fill="#e0a800"/><circle cy="-12" r="12" fill="#f2c79b"/><circle cx="-12" cy="-10" r="7" fill="#f2c79b"/><circle cx="12" cy="-10" r="7" fill="#f2c79b"/></g>'
 +'<text x="300" y="40" font-family="Georgia" font-size="28" font-weight="700" fill="#c0392b">Om</text>',
 [('A question.','The boy Skanda asked Brahmā, the creator, what <b>Om</b> (the Praṇava) means. Brahmā could not explain it.'),
  ('The prison.','Skanda locked Brahmā up and took over creation himself.'),
  ('The father asks.','Śiva came to free Brahmā and asked his son: “Then you tell me what Om means.”'),
  ('Svāminātha.','Śiva sat as a disciple and the boy whispered the meaning in his ear. So he is <b>Svāminātha</b>, “teacher of the Lord”, at <b>Svāmimalai</b>.'),
  ('The point.','Wisdom does not depend on age. This is a Tamil temple tradition; versions differ.')]))
pages.append(story('fruit','THE FRUIT OF WISDOM','Round the world, or round your parents?',560,170,'A boy on a peacock flying round a globe, while the elephant-headed Ganesha walks around seated Shiva and Parvati',
 '<rect width="560" height="170" fill="#cfe3f5"/><circle cx="130" cy="95" r="50" fill="#4aa3df" stroke="#111" stroke-width="2"/><path d="M100 80 q20 -20 40 0 q20 20 0 30 q-30 6 -40 -30z" fill="#3a8a3a" stroke="#111" stroke-width="2"/>'
 +'<ellipse cx="130" cy="95" rx="72" ry="26" fill="none" stroke="#e0701a" stroke-width="3" stroke-dasharray="6 5"/>'+PEACOCK(200,70,.35)
 +SHIVA(390,90,.6)+GENTLE(440,100,.6)+'<ellipse cx="415" cy="110" rx="80" ry="40" fill="none" stroke="#e0701a" stroke-width="3" stroke-dasharray="6 5"/>'
 +'<g transform="translate(330 140)" stroke="#111" stroke-width="2"><circle r="14" fill="#e8b4a0"/><path d="M-8 6 q-10 14 2 20" fill="none" stroke="#e8b4a0" stroke-width="6"/></g>',
 [('One fruit.','The sage Nārada brought a single golden fruit (a mango, in most tellings) to Śiva and Pārvatī. Who should have it?'),
  ('The race.','“Whoever goes round the world first,” said Śiva. Skanda leapt on his peacock and flew off.'),
  ('Gaṇeśa’s answer.','Gaṇeśa simply walked round his parents: “You are my world.” He won the fruit.'),
  ('Palani.','Skanda came back, felt cheated, gave up his finery and went to live alone on the hill of <b>Palani</b>, as a young renunciant with a staff.'),
  ('Pazham nī.','Pārvatī followed: “<i>Pazham nī</i>”, “you are the fruit.” Folk etymology hears “Palani” in it.')],
 talk("So who was right?","Both. Gaṇeśa shows love for parents; Skanda shows that the seeker must leave home. The fruit was the lesson.")))
pages.append(page('consorts','DEVASENĀ AND VALLI','Two wives, two worlds',fig(560,160,'The young god in the middle with a lady in a crown on one side and a forest girl holding a sling on the other',
 '<rect width="560" height="160" fill="#fdf1e8"/>'+GENTLE(180,90,.75)+SKANDA(280,80,.75,vel=False)+'<g transform="translate(380 90) scale(.75)" stroke="#111" stroke-width="2"><path d="M-24 60 q-2 -64 24 -72 q26 8 24 72z" fill="#2a9d6f"/><circle cy="-28" r="12" fill="#c98a5a"/><path d="M-12 -36 q12 -12 24 0" fill="#3a2a1a"/><path d="M20 0 l26 -20" stroke="#c98a5a" stroke-width="6"/><path d="M46 -20 q8 -6 4 -14" fill="none" stroke="#7a5a2a" stroke-width="3"/></g>')+facts([
 ('Devasenā','Daughter of <b>Indra</b> (in the Skanda Purāṇa; Dakṣa’s in the Mahābhārata). Her name means “the army of the gods”: the general marries his army. In Tamil, <b>Devayānai</b>'),
 ('Valli','Daughter of a hill-tribe chief, who guarded millet fields with a sling. Murugan wooed her disguised as a hunter and an old man, with Gaṇeśa’s help as a wild elephant'),
 ('The pair','Many read them as the two powers: Devasenā, action (kriyā); Valli, desire or love (icchā); the vel, knowledge (jñāna)'),
 ('Kukke','Karnataka’s tradition places the wedding with Devasenā near <b>Kukke</b> on Mārgaśīrṣa Ṣaṣṭhī: see Part 3'),
 ('North','In many northern traditions he stays a bachelor, and women traditionally kept out of some of his shrines')])))
pages.append(page('abodes','THE SIX ABODES','Āṟupaṭai Vīṭu of Tamil Nadu',facts([
 ('Tirupparaṅkuṉṟam','Near Madurai: his wedding with Devasenā'),
 ('Tiruccendūr','On the seashore: victory over Śūrapadma; the great Sūrasaṃhāram of Skanda Ṣaṣṭhī'),
 ('Paḻani','The hill of the fruit: the renunciant boy with a staff (Daṇḍāyudhapāṇi)'),
 ('Svāmimalai','Near Kumbakoṇam: the teacher of Om'),
 ('Tiruttaṇi','Near Chennai: peace after the war, and his marriage to Valli'),
 ('Paḻamudircōlai','Near Madurai, in the forest: Valli and Devasenā together')])
 +talk("Six again?","Of course. The 'six camps' come from Nakkīrar's Tirumurukāṟṟuppaṭai, a guide for pilgrims well over 1,600 years old.")
 +'<div class="key">Many read the six as six chapters of his life: birth of wisdom, war, renunciation, teaching, peace, union.</div>'))
pages.append(page('history','HOW OLD IS HE?','From the Vedas to Kuṣāṇa coins',facts([
 ('Vedas','A bright boy called <b>Kumāra</b> appears in the Ṛg Veda; the Taittirīya Āraṇyaka names “Ṣaṇmukha”'),
 ('Upaniṣad','The Chāndogya Upaniṣad calls the sage Sanatkumāra by the name Skanda'),
 ('Grammar','Pāṇini and Patañjali know Skanda; Kauṭilya’s Arthaśāstra too'),
 ('Epics','The Rāmāyaṇa and Mahābhārata tell his birth, with Agni and Gaṅgā'),
 ('Coins','Kuṣāṇa and Yaudheya coins (1st–2nd c. CE) show him with spear and peacock'),
 ('Tamil','Sangam poems (early centuries CE) make Murugan god of the hills; the Tirumurukāṟṟuppaṭai gives six faces and twelve arms'),
 ('Purāṇa','The <b>Skanda Purāṇa</b>, the largest Purāṇa, carries his name; an early version existed by the 6th c.'),
 ('Poem','Kālidāsa’s <b>Kumārasambhava</b> (about 5th c.)')])))
pages.append(page('karnataka','SUBRAHMAṆYA IN KARNATAKA','The god who is a serpent',fig(560,170,'A seven-hooded cobra coiled on an anthill, with small stone serpent images around it',
 '<rect width="560" height="170" fill="#eef5e8"/>'+ANTHILL(280,160,1.3)+NAGA(280,110,.8)+''.join(f'<g transform="translate({x} 160)" stroke="#111" stroke-width="2"><rect x="-12" y="-44" width="24" height="44" rx="10" fill="#9a9a8a"/><path d="M0 -6 q-8 -10 0 -18 q8 -8 0 -16" fill="none" stroke="#5a5a4a" stroke-width="3"/></g>' for x in (90,140,420,470)))+facts([
 ('Serpent form','Along the west coast and across Karnataka, Subrahmaṇya is worshipped as a <b>nāga</b>, a cobra, often seven-hooded'),
 ('Anthills','The anthill (<i>huttu</i>), the cobra’s home, is worshipped as his shrine'),
 ('Nāga stones','Stone serpent images under trees; installed after vows, often for children'),
 ('Why?','An old serpent worship of the coast and the Malnāḍ joined the cult of Skanda. Scholars and traditions differ on how'),
 ('Great shrines','<b>Kukke Subrahmaṇya</b> (Part 3) and <b>Ghāṭi Subrahmaṇya</b> (Part 4)'),
 ('Festivals','<b>Nāgara Pañcamī</b> and <b>Subrahmaṇya Ṣaṣṭhī</b>')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Vel','Spear'),('Śaravaṇa','Lake of reeds where he was born'),('Kṛttikā','The Pleiades; his six nurses'),('Ṣaṇmukha','Six-faced'),
 ('Devasenāpati','General of the gods’ army'),('Praṇava','The sacred syllable Om'),('Nāga','Serpent, cobra'),('Huttu','Anthill (Kannada)'),('Ṣaṣṭhī','Sixth lunar day')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Skanda, Kārttikeya, Murugan, Subrahmaṇya: Śiva’s son, general of the gods.</div>
<div><b>Birth.</b> Śiva’s spark, carried by Agni and Gaṅgā to the reeds of Śaravaṇa; six Kṛttikās; one child with six faces.</div>
<div><b>Signs.</b> The vel from his mother, the peacock and the rooster.</div>
<div><b>Stories.</b> Teacher of Om to his father; the fruit and Palani; Devasenā and Valli.</div>
<div><b>Karnataka.</b> Worshipped as a serpent, at the anthill and at Kukke and Ghāṭi.</div>
</div>'''+talk("What's next?","The war he was born for. Part 2: the Ṣaṣṭhī story, Tāraka, Śūrapadma and the day we celebrate it.")
 +f'<div class="key">Part 1: who Skanda is. Next: <a href="{SKS}shashthi/">The Ṣaṣṭhī Story</a> 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Names, birth, consorts, history:</b> Wikipedia, “Kartikeya” (names and meanings; Rāmāyaṇa and Mahābhārata births; Skanda Purāṇa’s six sparks fused by Pārvatī; Kumārasambhava; Kanda Purāṇam; vel from Pārvatī; peacock and rooster from Śūrapadma; six heads established after the 6th c.; Kuṣāṇa and Yaudheya coins; Ṛg Veda 5.2, Taittirīya Āraṇyaka 10.1, Chāndogya ch. 7; Tolkāppiyam, Sangam and Tirumurukāṟṟuppaṭai; Devasenā as Indra’s or Dakṣa’s daughter; Valli; northern bachelor tradition; the Six Abodes).</p>
<p><b>Retold from tradition:</b> the Praṇava story (Svāmimalai) and the fruit story (Palani) are Tamil temple traditions; Kālidāsa’s Kumārasambhava for Tāraka and Kāma.</p>
<p><b>Interpretations:</b> the meanings of the six faces, the vel as knowledge, Valli and Devasenā as icchā and kriyā are common teachings, not fixed doctrine. <b>Traditions differ</b> on the meaning of “Subrahmaṇya”, on whether Gaṇeśa or Skanda is elder, and on how serpent worship joined Skanda’s cult. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','His Names'),('why','Why He Was Born'),('birth','Born in the Reeds'),('six','The Six Faces'),('emblems','The Vel, the Peacock, the Rooster'),
 ('pranava','The Teacher of His Father'),('fruit','The Fruit of Wisdom'),('consorts','Devasenā and Valli'),('abodes','The Six Abodes'),('history','How Old Is He?'),('karnataka','Subrahmaṇya in Karnataka'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/SK1_Skanda.html',head,cov,fw,pages,toc)
