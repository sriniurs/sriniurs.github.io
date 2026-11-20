exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Kṛṣṇa · Daśāvatāra 9 · srini.presents','Kṛṣṇa, the ninth avatāra of Viṣṇu: birth in Kaṃsa’s prison and the stormy Yamunā, the butter thief of Gokula, Pūtanā, Kāliya and Govardhana, Rādhā and the rāsa, Mathurā and Dvārakā, the charioteer of the Mahābhārata, the Bhagavad Gītā and the cosmic form, the end at Prabhāsa, and the saints who loved him: Āṇḍāḷ, Mīrā, Sūrdās, Caitanya, Purandaradāsa and Kanakadāsa of Udupi. Temples from Udupi and Guruvāyūr to Purī, Dvārakā and Vṛndāvana. An illustrated reference guide.')
def KRISHNA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 50 q-4 -60 30 -70 q34 10 30 70z" fill="#ffd60a"/><path d="M-30 50 l-6 0 M30 50 l6 0"/>'
 '<path d="M-22 -8 l20 -2 M22 -8 l-6 -2" stroke="#3b6fd0" stroke-width="8"/><path d="M-40 -14 l70 -12" stroke="#7a4a1a" stroke-width="5"/><circle cx="-30" cy="-12" r="1.5" fill="#fff"/><circle cx="-18" cy="-14" r="1.5" fill="#fff"/>'
 '<circle cy="-36" r="15" fill="#3b6fd0"/><path d="M-14 -46 h28 l-4 -12 h-20z" fill="#e0a800"/><path d="M4 -58 q12 -22 22 -8 q-10 2 -22 8z" fill="#2a9d6f"/><circle cx="18" cy="-60" r="3.5" fill="#3b8fd0"/>'
 '<circle cx="-5" cy="-38" r="2.4" fill="#fff"/><circle cx="5" cy="-38" r="2.4" fill="#fff"/><path d="M-6 -29 q6 5 12 0" fill="none"/></g>')
def COW(x,y,s=1,f=1): return f'<g transform="translate({x} {y}) scale({s*f} {s})" stroke="#111" stroke-width="2"><path d="M-40 0 q-4 -30 30 -30 h30 q14 0 16 14 l10 2 v12 h-16z" fill="#fff"/><path d="M-30 0 v22 M20 0 v22" stroke-width="5"/><path d="M40 -18 l6 -8 M34 -18 l-2 -10" /><circle cx="-14" cy="-14" r="6" fill="#c9a26b" stroke="none"/></g>'
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Blue-skinned Krishna playing the flute with a peacock feather in his crown, cows around him by a river">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/>'+STAR+'<path d="M0 240 q190 -30 380 0 V268 H0Z" fill="#2a7a3a"/><path d="M0 254 q190 -18 380 0 V268 H0Z" fill="#3b8fd0"/>'+KRISHNA(190,190,1.35)+COW(70,224,.9)+COW(310,224,.9,-1)+'</svg>')
cov=cover_dv('DAŚĀVATĀRA 9 OF 10','KṚṢṆA',18,'Cowherd, charioteer, teacher of the Gītā',art)
fw=foreword_dv('Kṛṣṇāya Vāsudevāya,',[
 'The ninth avatāra is the one India knows most intimately. <b>Kṛṣṇa</b> was born at midnight in a prison, smuggled across a flooded river, and raised among cowherds as a butter-stealing child. He danced on a serpent’s heads, lifted a mountain like an umbrella, and played a flute that made the cowherd girls leave everything to dance with him.',
 'He grew up to kill the tyrant Kaṃsa, built the island city of Dvārakā, and became the charioteer of Arjuna at Kurukṣetra, where he spoke the <b>Bhagavad Gītā</b>. For many traditions he is not just one avatāra but the Lord himself, the source of all the others.',
 'This guide follows his life from Mathurā to Prabhāsa, and the saints and temples who keep him close, including Udupi in Karnataka.'],
 'One avatāra, so many stories?','The Bhāgavata gives him a whole book. Kṛṣṇa is child, lover, friend, king and teacher at once.',
 series_note_dv(9))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Avatāra','<b>Ninth</b> (or eighth) of the ten; end of the Dvāpara Yuga'),('Form','Dark blue, flute, peacock feather, yellow silk (pītāmbara)'),
 ('Parents','Born to Devakī and Vasudeva; raised by Yaśodā and Nanda in Gokula'),('Places','Mathurā, Vṛndāvana, Dvārakā, Kurukṣetra, Prabhāsa'),
 ('Texts','Bhāgavata Purāṇa book 10; Mahābhārata; Harivaṃśa; Viṣṇu Purāṇa book 5'),('Teaching','The Bhagavad Gītā, 700 verses in 18 chapters'),
 ('Svayaṃ Bhagavān','For many, the Lord himself: <i>kṛṣṇas tu bhagavān svayam</i>'),('Day','Kṛṣṇa Janmāṣṭamī')])
 +talk("Is Kṛṣṇa an avatāra or the source?","Both answers are held. For Gauḍīya Vaiṣṇavas and many others he is the source of all ten.")))
pages.append(page('names','NAMES','A thousand names',facts([
 ('Kṛṣṇa','“Dark”, “all-attractive”'),('Govinda · Gopāla','Protector of cows'),('Vāsudeva','Son of Vasudeva'),('Mādhava','Husband of Lakṣmī; also of the Madhu clan'),('Murāri','Slayer of Mura'),('Keśava','Of beautiful hair, or slayer of Keśī'),('Pārthasārathi','Charioteer of Arjuna'),('Mukunda · Hari · Acyuta','Giver of liberation · remover · the unfailing')])
 +'<div class="key">Hymns: <a href="/bhakti/vishnu/madhurashtakam/">Madhurāṣṭakam</a> · <a href="/bhakti/vishnu/acyutashtakam/">Acyutāṣṭakam</a></div>'))
pages.append(page('birth','MIDNIGHT IN THE PRISON','Birth and the Yamunā',fig(560,190,'A father carrying a baby in a basket on his head across a stormy river, a many-hooded serpent sheltering them',
 '<rect width="560" height="190" fill="#0b1030"/>'+''.join(f'<path d="M{40+i*90} 20 l-8 30 l10 0 l-8 26" stroke="#ffd60a" stroke-width="3" fill="none"/>' for i in range(6))+OCEAN(560,70,120,'#1d3f6a')+person(280,150,'#f4f4f4','#c98b5a',1.1)+'<path d="M260 90 h40 l-6 10 h-28z" fill="#c9a26b" stroke="#111"/>'+''.join(f'<path d="M{260+i*10} 80 q4 -24 0 -36" stroke="#3a6a3a" stroke-width="8" fill="none"/>' for i in range(5)))+'''<div class="steps">
<div><b>The prophecy.</b> A voice warned Kaṃsa that his sister Devakī’s eighth child would kill him. He imprisoned Devakī and Vasudeva and killed six of their children.</div>
<div><b>The birth.</b> At midnight on the eighth day of the dark fortnight, Kṛṣṇa was born. The guards slept, the chains fell, the doors opened.</div>
<div><b>The crossing.</b> Vasudeva carried him through the storm across the flooded Yamunā, the serpent Śeṣa spreading his hoods as an umbrella, to Nanda and Yaśodā in Gokula.</div>
<div><b>The swap.</b> He brought back Yaśodā’s newborn daughter, who rose from Kaṃsa’s hands as the goddess Yogamāyā and warned him his killer lived.</div>
</div>'''))
pages.append(page('gokula','THE BUTTER THIEF','Childhood in Gokula',fig(560,170,'A small blue child standing on a stool reaching a hanging pot of butter, friends and monkeys around',
 '<rect width="560" height="170" fill="#fff4dc"/><path d="M280 0 v40" stroke="#7a4a1a" stroke-width="3"/><path d="M262 40 h36 q6 30 -18 34 q-24 -4 -18 -34z" fill="#c9a26b" stroke="#111" stroke-width="2"/>'+KRISHNA(280,140,.7)+person(190,160,'#e0a800','#c98b5a',.6)+person(370,160,'#e05a3a','#c98b5a',.6))+facts([
 ('Makhan cor','He stole butter from every house in the village and fed it to his friends and the monkeys'),
 ('Yaśodā','When she looked into his mouth, she saw the whole universe in it'),
 ('Dāmodara','She tied him to a mortar with a rope; he dragged it between two trees and freed two cursed beings'),
 ('Pūtanā','The demoness who came to poison him with her milk; he drank her life away'),
 ('Meaning','God as a naughty child: love without fear')])
 +talk("God stealing butter?","Devotees love it. A God you can scold is a God you can love.")))
pages.append(page('vrindavana','VṚNDĀVANA','Serpent, mountain and cows',fig(560,180,'A boy holding up a whole mountain on one finger while people and cows shelter under it from rain',
 '<rect width="560" height="180" fill="#5a6a8a"/>'+''.join(f'<path d="M{30+i*50} 0 l-6 24" stroke="#cfe8f6" stroke-width="2"/>' for i in range(11))+'<path d="M140 70 q140 -70 280 0z" fill="#7a6a4a" stroke="#111" stroke-width="2"/><path d="M280 70 v40" stroke="#3b6fd0" stroke-width="6"/>'+KRISHNA(280,150,.55)+COW(170,166,.6)+COW(400,166,.6,-1)+person(220,166,'#e05a3a','#c98b5a',.5)+person(340,166,'#2a9d6f','#c98b5a',.5))+facts([
 ('Kāliya','The poison-serpent of the Yamunā: Kṛṣṇa danced on his hundred heads and drove him away'),
 ('Govardhana','When Indra sent a week of storms, Kṛṣṇa lifted Govardhana hill on his little finger as an umbrella for the people and cows'),
 ('Govinda','Indra bowed to him and named him Govinda'),
 ('Cowherd','He grazed cows with Balarāma and the boys in the forests of Vraja')])
 +'<div class="key">Hymn: <a href="/bhakti/vishnu/govinda-namalu/">Govinda Nāmālu</a></div>'))
pages.append(page('radha','RĀDHĀ AND THE RĀSA','The flute and the dance',fig(560,170,'Krishna playing the flute at the centre of a circle of dancing women under a full moon',
 '<rect width="560" height="170" fill="#1d1040"/><circle cx="470" cy="40" r="22" fill="#fff8c0"/>'+''.join(GENTLE(280+160*__import__("math").cos(a*0.785),120+30*__import__("math").sin(a*0.785),.4) for a in range(8))+KRISHNA(280,140,.6))+facts([
 ('The flute','His flute called the gopīs, cowherd women, from their homes on autumn nights'),
 ('Rāsa Līlā','He danced with all of them at once, a Kṛṣṇa for each gopī: the soul’s longing for God'),
 ('Rādhā','The beloved above all; not named in the Bhāgavata, she is central in the Gītagovinda and later devotion'),
 ('Meaning','Bhakti saints read the love of the gopīs as the highest love of the soul for God'),
 ('Holi','Rādhā and Kṛṣṇa’s play with colours is remembered at Holi in Vraja')])))
pages.append(page('mathura','MATHURĀ AND DVĀRAKĀ','Prince and king',facts([
 ('Kaṃsa','At sixteen Kṛṣṇa returned to Mathurā, broke the great bow, beat the king’s wrestlers and killed Kaṃsa'),
 ('Ugrasena','He freed his parents and restored Kaṃsa’s father to the throne'),
 ('Sāndīpani','He studied with the sage Sāndīpani at Ujjain, with his friend Sudāmā'),
 ('Dvārakā','Facing endless attacks, he moved the Yādavas to Dvārakā, a city on the western sea'),
 ('Rukmiṇī','He carried off Rukmiṇī, who loved him, from her own wedding; she is Lakṣmī'),
 ('Sudāmā','His poor friend came with a handful of rice and went home rich')])
 +'<div class="key">Read: <a href="'+TI+'char-dham/bada-char-dham/dvaraka/">Dvārakā</a></div>'))
pages.append(page('pandavas','FRIEND OF THE PĀṆḌAVAS','The Mahābhārata',facts([
 ('Kinship','Cousin and friend of the five Pāṇḍava brothers'),
 ('Draupadī','When she was humiliated in the dice hall, he made her sari endless'),
 ('Peace envoy','He went to Hastināpura to make peace; Duryodhana refused even five villages'),
 ('Choice','He offered Arjuna either his army or himself unarmed; Arjuna chose Kṛṣṇa'),
 ('Charioteer','He drove Arjuna’s chariot through the eighteen-day war')])))
pages.append(page('gita','THE BHAGAVAD GĪTĀ','The song of the Lord',fig(560,180,'A chariot between two armies, a charioteer turning to speak to a grieving archer',
 '<rect width="560" height="180" fill="#f4e6d0"/>'+''.join(person(30+i*28,150,'#c0392b','#c98b5a',.4) for i in range(5))+''.join(person(400+i*28,150,'#3b6fd0','#c98b5a',.4) for i in range(6))+'<path d="M200 140 h140 l-10 20 h-120z" fill="#c9a26b" stroke="#111" stroke-width="2"/><circle cx="220" cy="164" r="14" fill="#8a6a4a" stroke="#111" stroke-width="2"/><circle cx="320" cy="164" r="14" fill="#8a6a4a" stroke="#111" stroke-width="2"/>'+KRISHNA(240,120,.5)+person(310,138,'#f4f4f4','#c98b5a',.6))+facts([
 ('Setting','On the field of Kurukṣetra, Arjuna saw his kin in the enemy army and laid down his bow'),
 ('The answer','Kṛṣṇa’s teaching: 700 verses in 18 chapters, within the Mahābhārata’s Bhīṣma Parva'),
 ('Karma yoga','Act without attachment to the fruits of action'),
 ('Jñāna and bhakti','Know the undying Self; love and surrender to the Lord'),
 ('Promise','Whenever dharma declines, I come (4.7–8)')])
 +'<div class="panel reading"><p><i>karmaṇy evādhikāras te mā phaleṣu kadācana</i></p><p class="small">“Your right is to the action alone, never to its fruits.” Bhagavad Gītā 2.47</p></div>'))
pages.append(page('vishvarupa','THE COSMIC FORM','Viśvarūpa',facts([
 ('Chapter 11','Arjuna asked to see Kṛṣṇa’s true form; Kṛṣṇa gave him divine sight'),
 ('The vision','Countless faces, arms and eyes; all the gods and worlds inside one body; armies rushing into his mouths'),
 ('“I am Time”','Kṛṣṇa said: I am Time, the destroyer of worlds'),
 ('Oppenheimer','The physicist recalled this verse after the first atomic test in 1945'),
 ('Return','Afraid, Arjuna begged to see the gentle four-armed and two-armed form again')])
 +'<div class="key">Kṛṣṇa and Kālī: <a href="/bhakti/devi/dasha-mahavidya/kali/">Kālī</a> (paired in Tantric lists)</div>'))
pages.append(page('end-life','THE END AT PRABHĀSA','Departure of the Lord',facts([
 ('Gāndhārī’s curse','Grieving her hundred sons, Gāndhārī cursed the Yādavas to destroy each other'),
 ('The quarrel','At Prabhāsa, drunk Yādavas fought with reeds that turned to iron clubs'),
 ('The arrow','Kṛṣṇa sat under a tree; a hunter named Jarā mistook his foot for a deer and shot him'),
 ('Kali Yuga','Tradition says the Kali age began when he left the world, often dated to 3102 BCE'),
 ('Dvārakā','The sea swallowed the city')])))
pages.append(page('saints','THOSE WHO LOVED HIM','Saints and poets',facts([
 ('Āṇḍāḷ','Tamil Āḻvār saint, 8th c.: Tiruppāvai; she married Raṅganātha'),
 ('Jayadeva','Gītagovinda, 12th c.'),
 ('Mīrābāī','Rajput princess-poet, 16th c., who called Giridhara Gopāla her husband'),
 ('Sūrdās','Blind poet of Braj, 16th c.: songs of Kṛṣṇa’s childhood'),
 ('Caitanya','Bengal, 16th c.: ecstatic kīrtana; the Gauḍīya tradition'),
 ('Udupi','Purandaradāsa, father of Carnatic music, and Kanakadāsa, who saw Kṛṣṇa through a window in the wall')])
 +'<div class="key">Read: <a href="/bhakti/vishnu/tiruppavai/">Tiruppāvai</a> · <a href="/bhakti/vishnu/bhaja-govindam/">Bhaja Govindam</a></div>'))
pages.append(page('udupi','UDUPI','Kṛṣṇa of Karnataka',fig(560,170,'A small window in a temple wall through which a boy-Krishna image is seen, a man in a blanket outside',
 '<rect width="560" height="170" fill="#f2e6c8"/><rect x="200" y="20" width="160" height="150" fill="#e8d8b0" stroke="#111" stroke-width="2"/><rect x="250" y="60" width="60" height="50" fill="#1d1d2a" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{256+i*10} 60 v50" stroke="#c9a26b" stroke-width="3"/>' for i in range(5))+KRISHNA(280,104,.25)+person(120,160,'#3a3a3a','#8a5a3a',1))+facts([
 ('Madhvācārya','The 13th-century philosopher of Dvaita installed the image of Bālakṛṣṇa, said to have come in a ship’s ballast'),
 ('Aṣṭa Maṭhas','Eight monasteries take turns to worship, changing every two years at the Paryāya festival'),
 ('Kanakadāsa','Refused entry because of his caste, the poet sang outside; the wall cracked and the image turned to face him. The window is Kanakana Kiṇḍi'),
 ('Purandaradāsa','His thousands of Kannada songs shaped Carnatic music'),
 ('Facing west','So the Lord here looks through the window, westward')])
 +talk("The god turned around for a devotee?","That's Udupi's story. The window is still there.")))
pages.append(page('temples','OTHER GREAT TEMPLES','Across India',facts([
 ('Guruvāyūr','Kerala: the child Kṛṣṇa (Guruvāyūrappan)'),('Mathurā and Vṛndāvana','His birthplace and childhood land'),('Dvārakā','The western Dhām'),('Purī','Jagannātha, the eastern Dhām'),
 ('Nāthdvārā','Rajasthan: Śrīnāthjī, the child who lifted Govardhana'),('Paṇḍharpur','Mahārāṣṭra: Viṭhobā, standing on a brick'),('Śrīraṅgam','Raṅganātha, worshipped by Kṛṣṇa’s ancestors in some traditions')])
 +'<div class="key">See: <a href="'+TI+'char-dham/bada-char-dham/puri/">Purī</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','His days',facts([
 ('Janmāṣṭamī','Śrāvaṇa or Bhādrapada Kṛṣṇa Aṣṭamī: midnight birth; Dahi Handi in Mahārāṣṭra; Gokulāṣṭamī'),('Holi','Phālguna: colours with Rādhā in Vraja'),('Govardhana Pūjā','The day after Dīpāvalī'),('Gītā Jayantī','Mārgaśīrṣa Śukla Ekādaśī'),('Paryāya','Udupi, every two years'),('Ratha Yātrā','Purī, Āṣāḍha')])))
pages.append(page('meaning','WHAT KṚṢṆA TEACHES','The wisdom of the flute',facts([
 ('Love','God can be loved as a child, friend or beloved'),('Action','Do your duty without clinging to results'),('Joy','Play, music and dance are paths to God'),('Surrender','“Take refuge in me alone; I will free you”: Gītā 18.66')])
 +talk("What should I take from Kṛṣṇa?","Work hard, let go of results, and keep a little butter-thief joy in your heart.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Gopa · Gopī','Cowherd man · woman'),('Līlā','Divine play'),('Rāsa','Circle dance'),('Viśvarūpa','Cosmic form'),('Karma yoga','Path of selfless action'),('Paryāya','Udupi’s two-yearly change of maṭha'),('Svayaṃ Bhagavān','The Lord himself'),('Pītāmbara','Yellow silk')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Kṛṣṇa, ninth avatāra, for many the Lord himself.</div>
<div><b>Childhood.</b> Prison birth; the butter thief; Kāliya; Govardhana; Rādhā and the rāsa.</div>
<div><b>Adult.</b> Kaṃsa, Dvārakā, the Pāṇḍavas, the Gītā at Kurukṣetra, the cosmic form.</div>
<div><b>Devotion.</b> Āṇḍāḷ to Kanakadāsa; Udupi, Guruvāyūr, Purī, Dvārakā, Vṛndāvana.</div>
<div><b>Lesson.</b> Act without clinging; love without fear.</div>
</div>'''+talk("One line to remember?","The flute and the chariot: love and duty, in one God.")+'<div class="key">Next and last: <a href="'+DVS+'kalki/">Kalki</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Bhāgavata Purāṇa 10–11 (birth, childhood, rāsa, Mathurā, Dvārakā, Prabhāsa); Mahābhārata (Sabhā, Udyoga, Bhīṣma and Mausala Parvas); Bhagavad Gītā 2.47, 4.7–8, 11, 18.66; Harivaṃśa; Viṣṇu Purāṇa 5; Jayadeva, Gītagovinda.</p>
<p><b>Udupi:</b> Udupi Śrī Kṛṣṇa Maṭha traditions (Madhvācārya, Aṣṭa Maṭhas, Paryāya, Kanakana Kiṇḍi); Purandaradāsa and Kanakadāsa from Karnataka literary histories.</p>
<p><b>Other:</b> Oppenheimer’s recollection of Gītā 11.32 (1965 interview); the 3102 BCE Kali Yuga date is traditional.</p>
<p><b>Sources differ / unverified:</b> Kṛṣṇa’s historical dates; whether he is the eighth or ninth avatāra or the source; the Udupi image’s arrival story; Rādhā’s absence from the Bhāgavata is noted by scholars and explained differently by devotees. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('birth','Midnight in the Prison'),('gokula','The Butter Thief'),('vrindavana','Vṛndāvana'),('radha','Rādhā and the Rāsa'),('mathura','Mathurā and Dvārakā'),('pandavas','Friend of the Pāṇḍavas'),('gita','The Bhagavad Gītā'),
 ('vishvarupa','The Cosmic Form'),('end-life','The End at Prabhāsa'),('saints','Those Who Loved Him'),('udupi','Udupi'),('temples','Other Great Temples'),('festivals','Through the Year'),('meaning','What Kṛṣṇa Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV9_Krishna.html',head,cov,fw,pages,toc)
