exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Varāha · Daśāvatāra 3 · srini.presents','Varāha, the boar, third avatāra of Viṣṇu: the gatekeepers Jaya and Vijaya, the demon Hiraṇyākṣa, the Earth sunk in the cosmic ocean, the boar born from Brahmā’s nose, Bhūdevī lifted on his tusk, the Vedic Emūṣa, the great Udayagiri relief of 401 CE, Eran, Bādāmi and Mahābalipuram, the boar emblem of the Chalukyas and Vijayanagara, and Varāha temples at Śrīmuṣṇam, Tirumala and Kallahalli. An illustrated reference guide.')
def BOARMAN(x,y,s=1,earth=True):
    e='<circle cx="44" cy="-90" r="20" fill="#5ab0f0" stroke="#111" stroke-width="2"/><path d="M34 -96 q8 -6 14 2 q-6 8 -14 -2z M46 -84 q8 2 6 8" fill="#5a9a4a"/>' if earth else ''
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 50 q-4 -60 30 -70 q34 10 30 70z" fill="#ffd60a"/>'
     '<path d="M-22 -6 l-26 -14 M22 -6 l20 -30 M-22 8 l-24 10 M22 8 l26 8" stroke="#5a4a5a" stroke-width="7"/><circle cx="-50" cy="-22" r="8" fill="#fff8e7"/><circle cx="50" cy="16" r="8" fill="none" stroke="#e0a800" stroke-width="4"/>'
     '<path d="M-16 -22 q-6 -30 10 -40 q24 -6 34 10 l14 6 l-12 8 q-6 14 -26 18z" fill="#5a4a5a"/><path d="M28 -40 q10 -12 4 -22" fill="none" stroke="#fff" stroke-width="3"/><circle cx="10" cy="-44" r="2.4" fill="#fff"/>'
     f'<path d="M-6 -56 h20 l-3 -12 h-14z" fill="#e0a800"/>{e}</g>')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Vishnu with a boar\'s head rising from the ocean, holding the small blue Earth goddess on his tusk and shoulder">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/>'+STAR+OCEAN(380,70,198,'#1d5f9a')+BOARMAN(190,200,1.4)+'</svg>')
cov=cover_dv('DAŚĀVATĀRA 3 OF 10','VARĀHA',16,'The boar who lifted the Earth',art)
fw=foreword_dv('Keśava dhṛta-śūkara-rūpa,',[
 'The third avatāra dives. The demon <b>Hiraṇyākṣa</b> had dragged the Earth down into the bottom of the cosmic ocean. To bring her back, Viṣṇu came out of Brahmā’s nostril as a boar no bigger than a thumb, and in a moment grew as large as a mountain.',
 '<b>Varāha</b> plunged into the waters, fought the demon for a thousand years, and rose with the Earth goddess <b>Bhūdevī</b> resting on his tusk. That image, the boar-headed god lifting a small, grateful Earth, is one of the grandest in Indian art, carved in stone at Udayagiri in 401 CE. Kings of Karnataka took the boar as their emblem, and the gold coins of Vijayanagara were called varāhas.',
 'This guide tells the story and follows the boar through art, history and temples.'],
 'A pig saves the world?','A wild boar, digging where no one else could. The humblest animal does the greatest rescue.',
 series_note_dv(3))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Avatāra','<b>Third</b> of the ten; Satya Yuga'),('Form','<b>A boar</b>, or a man with a boar’s head'),
 ('Deed','Raises the Earth (Bhūdevī) from the cosmic ocean and slays Hiraṇyākṣa'),('Texts','Bhāgavata Purāṇa 3.13–19; Viṣṇu Purāṇa 1.4; Varāha Purāṇa'),
 ('Vedic seed','Prajāpati as a boar raises the earth (Taittirīya Saṃhitā; Śatapatha Brāhmaṇa)'),('Art','The colossal relief at Udayagiri, consecrated in 401 CE'),
 ('Emblem','Royal symbol of the Chalukyas and of Vijayanagara'),('Temples','Śrīmuṣṇam, Tirumala, Kallahalli (Karnataka)')])
 +talk("He fought for a thousand years?","In the Bhāgavata, yes. Gods take their time.")))
pages.append(page('names','NAMES','The boar of the Lord',facts([
 ('Varāha','Boar'),('Śūkara','Another word for boar; Jayadeva’s: <i>dhṛta-śūkara-rūpa</i>'),('Bhū Varāha','The boar with the Earth'),('Ādi Varāha','The first boar'),('Yajña Varāha','The boar whose body is the sacrifice'),('Emūṣa','The Vedic boar who raised the earth')])))
pages.append(page('gatekeepers','THE CURSED GATEKEEPERS','Jaya and Vijaya',fig(560,160,'Two gatekeepers at the gate of Vaikuntha stopping four child-sages',
 '<rect width="560" height="160" fill="#eef3fa"/><rect x="240" y="20" width="80" height="140" fill="#ffd60a" stroke="#111" stroke-width="2"/>'+person(200,140,'#3b6fd0','#5b8fe0',1)+person(360,140,'#3b6fd0','#5b8fe0',1)+''.join(person(x,150,'#f4f4f4','#f2c79b',.5) for x in (60,90,120,150)))+facts([
 ('Who','Jaya and Vijaya, the gatekeepers of Viṣṇu’s heaven, Vaikuṇṭha'),
 ('The insult','They blocked the four child-sages, the Kumāras, from seeing Viṣṇu'),
 ('The curse','To be born on earth, away from the Lord'),
 ('The choice','Seven births as devotees, or three as his enemies; they chose three, to return sooner'),
 ('Three births','Hiraṇyākṣa and Hiraṇyakaśipu; Rāvaṇa and Kumbhakarṇa; Śiśupāla and Dantavakra')])
 +talk("They chose to be his enemies?","Three lives of hating him was the faster way home. Even enmity keeps your mind on God.")+'<div class="key">The brother: <a href="'+DVS+'narasimha/">Narasiṃha and Hiraṇyakaśipu</a></div>'))
pages.append(page('sinking','THE SUNKEN EARTH','Hiraṇyākṣa',fig(560,170,'A golden-eyed demon dragging the blue Earth down into a dark ocean',
 '<rect width="560" height="170" fill="#0b1030"/>'+OCEAN(560,150,20,'#1d3f6a')+DEMON(220,110,.9)+'<circle cx="320" cy="140" r="22" fill="#5ab0f0" stroke="#111" stroke-width="2"/>')+facts([
 ('Who','Hiraṇyākṣa, “golden-eyed”, the first-born of the twin demons of Diti'),
 ('Boon','Made mighty by Brahmā’s boon, he roamed the worlds looking for a fight'),
 ('The crime','He seized the Earth and dragged her into the depths of the cosmic waters'),
 ('Another view','In other tellings the Earth simply lay under the waters of dissolution, and Brahmā needed it raised to begin creation')])))
pages.append(page('nostril','THE BOAR FROM BRAHMĀ’S NOSE','A tiny boar becomes a giant',facts([
 ('The sneeze','As Brahmā and the sages worried, a boar the size of a thumb came out of Brahmā’s nostril'),
 ('The growth','In a moment it grew as big as an elephant, then as big as a mountain'),
 ('The roar','Its grunt filled the worlds, and the sages praised it with the Vedas'),
 ('The dive','Sniffing for the Earth like a boar for a root, it plunged into the ocean')])
 +talk("God came out of a sneeze?","The Bhāgavata loves surprises. Small beginnings, cosmic results, again.")))
pages.append(page('rescue','THE RESCUE','The Earth on his tusk',fig(560,190,'A boar-headed god rising from the ocean holding the Earth goddess, a demon fallen below',
 '<rect width="560" height="190" fill="#1d2a4a"/>'+OCEAN(560,70,120,'#1d5f9a')+BOARMAN(280,170,1.1)+DEMON(120,170,.6))+'''<div class="steps">
<div><b>The finding.</b> At the bottom of the ocean, Varāha found the Earth and lifted her on his tusks.</div>
<div><b>The challenge.</b> Hiraṇyākṣa attacked, mocking him as a beast of the swamp. Varāha first set the Earth safely on the water.</div>
<div><b>The fight.</b> They fought with mace and discus, in a battle the Bhāgavata says lasted a thousand years.</div>
<div><b>The end.</b> Varāha struck the demon down with his hand. He set the Earth back in place, and Brahmā could begin creation again.</div>
</div>'''))
pages.append(page('bhudevi','BHŪDEVĪ','The Earth as his consort',facts([
 ('Bhūdevī','The Earth goddess, one of Viṣṇu’s two consorts with Śrīdevī (Lakṣmī)'),
 ('In art','She sits on Varāha’s arm or shoulder, small and grateful, gazing at him'),
 ('Varāha Purāṇa','Told by Varāha to Bhūdevī as she rested on his tusk'),
 ('Their son','In the Purāṇas, Naraka was born to Varāha and Bhūdevī; his defeat by Kṛṣṇa is remembered on Naraka Caturdaśī, part of Dīpāvalī'),
 ('Āṇḍāḷ','Śrī Vaiṣṇavas see the poet-saint Āṇḍāḷ as Bhūdevī born on earth')])))
pages.append(page('vedic','THE VEDIC BOAR','Emūṣa',facts([
 ('Taittirīya Saṃhitā','Prajāpati becomes a boar and raises the earth from the waters'),
 ('Śatapatha Brāhmaṇa','A boar named Emūṣa raised the earth, which was then only the size of a hand'),
 ('Ṛgveda','A boar is mentioned in hymns to Indra and Viṣṇu'),
 ('Yajña Varāha','Later texts make the boar’s body the sacrifice itself: his tusks the sacrificial posts, his tongue the fire')])))
pages.append(page('udayagiri','UDAYAGIRI, 401 CE','The great boar in stone',fig(560,190,'A rock-cut cave panel with a giant boar-headed god lifting the Earth, rows of small gods and sages behind',
 '<rect width="560" height="190" fill="#d8c49a"/><rect x="30" y="20" width="500" height="160" fill="#c8b48a" stroke="#111" stroke-width="2"/>'+''.join(f'<circle cx="{60+i*28}" cy="{40+(j*22)}" r="7" fill="#b8a47a" stroke="#111"/>' for i in range(17) for j in range(3) if not (6<i<11))+BOARMAN(280,170,1.05))+facts([
 ('Where','Cave 5, Udayagiri caves near Vidiśā, Madhya Pradesh'),
 ('When','Gupta period; an inscription in Cave 6 dates the site’s consecration to 401 CE under Chandragupta II'),
 ('What','A colossal man-boar lifting Bhūdevī, with rows of gods and sages watching and the rivers Gaṅgā and Yamunā flowing to the ocean'),
 ('Meaning','Scholars read it also as royal art: the Gupta king as the rescuer of the earth'),
 ('Eran','At nearby Eran stands a huge free-standing boar statue of about 500 CE, covered with small figures of sages')])))
pages.append(page('karnataka','THE BOAR OF KARNATAKA','Emblem of kings',fig(560,150,'A boar emblem with sun and moon above and a sword before it, on a gold coin',
 '<rect width="560" height="150" fill="#fff4dc"/><circle cx="280" cy="76" r="60" fill="#e0a800" stroke="#111" stroke-width="3"/>'+AV(3,280,86,.9).replace('<circle cx="-6" cy="-36" r="12" fill="#5ab0f0"/>','')+'<circle cx="250" cy="34" r="8" fill="#ffd60a" stroke="#111"/><path d="M306 28 a8 8 0 1 0 6 12 a6 6 0 1 1 -6 -12z" fill="#fff8c0" stroke="#111"/>')+facts([
 ('Bādāmi','The Chalukyas of Bādāmi took the boar (varāha lāñchana) as their royal emblem; Bādāmi Cave 2 and 3 (6th c.) carve Varāha in stone'),
 ('Vijayanagara','The boar, with sun, moon and sword, was Vijayanagara’s emblem; its gold coins were called varāhas (the “pagodas” of European traders)'),
 ('Mysore','Varāha coins and the boar remained known in the Mysore region for centuries'),
 ('Meaning','A king lifts and protects the land, as Varāha lifted the Earth')])
 +talk("So money in Karnataka was once named after Varāha?","For centuries. A varāha was a gold coin.")))
pages.append(page('art','MORE GREAT VARĀHAS','Mahābalipuram and Khajuraho',facts([
 ('Mahābalipuram','The Varāha cave, a 7th-century Pallava rock-cut shrine with a fine Bhū Varāha panel'),
 ('Khajuraho','A small 10th-century shrine holds a great free-standing boar, its body carved with hundreds of tiny gods'),
 ('Ellora','Varāha panels in the Daśāvatāra cave'),
 ('Two styles','Theriomorphic (a whole boar) in the north; man-boar in most of India')])))
pages.append(page('temples','VARĀHA TEMPLES','Where he is worshipped',fig(560,150,'A temple tower with a small boar-headed figure in its sanctum',
 '<rect width="560" height="150" fill="#eef3fa"/>'+GOPURAM(160,146,.55,'#e8d8b0',7)+TEMPLE(380,146,2.2)+AV(3,380,116,.35))+facts([
 ('Śrīmuṣṇam','Bhū Varāha Svāmī temple, Cuddalore district, Tamil Nadu: a self-manifested (svayam vyakta) image'),
 ('Tirumala','Tradition says Śrīnivāsa received his place on the hill from Varāha, and promised that pilgrims would see Varāha first'),
 ('Kallahalli','The Bhū Varāhanātha temple near Kṛṣṇarājapet, Maṇḍya district, Karnataka, with a large image of Varāha and Bhūdevī'),
 ('Others','Varāha shrines at Puṣkar and Khajuraho; Vārāhī, his Śakti, is one of the Mātṛkās')])))
pages.append(page('festivals','THROUGH THE YEAR','His days',facts([
 ('Varāha Jayantī','Bhādrapada (Aug–Sep), by common calendars'),
 ('Naraka Caturdaśī','Part of Dīpāvalī: the end of Naraka, son of Varāha and Bhūdevī'),
 ('Tirumala','Varāha is worshipped before Śrī Veṅkaṭeśvara')])))
pages.append(page('meaning','WHAT VARĀHA TEACHES','The wisdom of the boar',facts([
 ('Dig deep','He went to the bottom to find what was lost'),
 ('Care for the Earth','The earth is a goddess to be lifted, not dragged down'),
 ('No form is low','God chose the body of a wild boar'),
 ('Protect first, fight second','He set the Earth safe before facing the demon')])
 +talk("What should I take from Varāha?","When the world sinks, go down after it. And put the Earth somewhere safe before you fight.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Varāha · Śūkara','Boar'),('Bhūdevī','The Earth goddess'),('Hiraṇyākṣa','“Golden-eyed” demon'),('Lāñchana','Royal emblem'),('Svayam vyakta','Self-manifested'),('Vārāhī','Varāha’s Śakti'),('Kumāras','Four child-sages'),('Vaikuṇṭha','Viṣṇu’s heaven')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Varāha, the boar, third avatāra of Viṣṇu.</div>
<div><b>Story.</b> Born from Brahmā’s nose, he dives, kills Hiraṇyākṣa and lifts the Earth on his tusk.</div>
<div><b>Roots.</b> The Vedic boar Emūṣa; Jaya and Vijaya’s curse.</div>
<div><b>In history.</b> Udayagiri 401 CE; the Chalukya and Vijayanagara emblem; varāha coins.</div>
<div><b>Lesson.</b> Go deep for what is lost; care for the Earth.</div>
</div>'''+talk("One line to remember?","The Earth was lost, and a boar brought her home.")+'<div class="key">Next: <a href="'+DVS+'narasimha/">Narasiṃha, the man-lion</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Bhāgavata Purāṇa 3.13–19 and 3.16 (Jaya and Vijaya); Viṣṇu Purāṇa 1.4; Varāha Purāṇa; Taittirīya Saṃhitā 7.1.5; Śatapatha Brāhmaṇa 14.1.2.11 (Emūṣa).</p>
<p><b>Art and history:</b> Wikipedia, “Udayagiri Caves” (Cave 5 Varāha; 401 CE inscription of Chandragupta II); Smarthistory (Eran boar); MAP Academy (royal reading). Chalukya and Vijayanagara emblems and coins from standard numismatic histories.</p>
<p><b>Temples:</b> Śrīmuṣṇam and Tirumala temple traditions; Kallahalli Bhū Varāhanātha temple (Maṇḍya district).</p>
<p><b>Sources differ / unverified:</b> the thousand-year battle; Varāha Jayantī date; the size and date of the Kallahalli image; Naraka’s parentage differs in some texts. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('gatekeepers','The Cursed Gatekeepers'),('sinking','The Sunken Earth'),('nostril','The Boar from Brahmā’s Nose'),('rescue','The Rescue'),('bhudevi','Bhūdevī'),('vedic','The Vedic Boar'),
 ('udayagiri','Udayagiri, 401 CE'),('karnataka','The Boar of Karnataka'),('art','More Great Varāhas'),('temples','Varāha Temples'),('festivals','Through the Year'),('meaning','What Varāha Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV3_Varaha.html',head,cov,fw,pages,toc)
