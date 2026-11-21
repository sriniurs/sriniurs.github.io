exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Rāma · Daśāvatāra 7 · srini.presents','Rāma, prince of Ayodhyā, seventh avatāra of Viṣṇu: the Rāmāyaṇa in seven kāṇḍas, from Daśaratha’s sons to exile, Sītā’s abduction, Hanumān and Kiṣkindhā at Hampi, the bridge to Laṅkā, Rāvaṇa’s fall and the return; Rāma as maryādā puruṣottama, the many Rāmāyaṇas (Vālmīki, Kamba, Tulasīdāsa, Kumāra Vālmīki’s Kannada Torave), Rāmeśvaram, Bhadrācalam, Ayodhyā and Rāma Navamī. An illustrated reference guide.')
def RAMA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 50 q-4 -60 30 -70 q34 10 30 70z" fill="#ffd60a"/>'
 '<path d="M-22 -6 l-22 26 M22 -6 l26 -8" stroke="#3b6fd0" stroke-width="8"/><path d="M-50 -60 q-26 60 0 120" fill="none" stroke="#7a4a1a" stroke-width="5"/><path d="M-50 -60 v120" stroke="#ccc" stroke-width="1.5"/><path d="M40 -20 l20 -40" stroke="#7a4a1a" stroke-width="3"/>'
 '<circle cy="-36" r="15" fill="#3b6fd0"/><path d="M-12 -48 h24 l-4 -16 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/><circle cx="-5" cy="-38" r="2.4" fill="#fff"/><circle cx="5" cy="-38" r="2.4" fill="#fff"/><path d="M-6 -29 q6 4 12 0" fill="none"/><path d="M-3 -46 v-5 M3 -46 v-5" stroke="#fff" stroke-width="1.5"/></g>')
def MONKEY(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-20 40 q-2 -44 20 -50 q22 6 20 50z" fill="#e08a2a"/><path d="M20 30 q30 -10 26 -50" fill="none" stroke="#e08a2a" stroke-width="6"/>'
 '<circle cy="-20" r="14" fill="#e08a2a"/><ellipse cy="-14" rx="9" ry="7" fill="#f2c79b"/><circle cx="-4" cy="-22" r="2" fill="#111"/><circle cx="4" cy="-22" r="2" fill="#111"/><path d="M-30 0 v-30" stroke="#7a4a1a" stroke-width="5"/><circle cx="-30" cy="-36" r="9" fill="#e0a800"/></g>')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Rama with his bow, Sita beside him, Lakshmana and Hanuman kneeling">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/>'+STAR+RAMA(150,190,1.3)+GENTLE(230,200,.8)+person(300,240,'#e0a800','#f2c79b',.9)+MONKEY(80,236,.8)+'</svg>')
cov=cover_dv('DAŚĀVATĀRA 7 OF 10','RĀMA',18,'Prince of Ayodhyā, the ideal man',art)
fw=foreword_dv('Śrī Rāma Jaya Rāma,',[
 'The seventh avatāra is the most loved hero of India. <b>Rāma</b>, eldest son of King Daśaratha of Ayodhyā, gave up his throne to keep his father’s word, went into the forest for fourteen years with his wife <b>Sītā</b> and brother <b>Lakṣmaṇa</b>, lost Sītā to the demon king <b>Rāvaṇa</b>, and won her back with an army of vānaras and bears led by <b>Hanumān</b>.',
 'The story is the <b>Rāmāyaṇa</b>, first told by the poet Vālmīki and retold in every Indian language and across Asia. Rāma is <i>maryādā puruṣottama</i>, the best of men who kept every bound of duty. Kiṣkindhā, where he met Hanumān, is the boulder country of Hampi in Karnataka.',
 'This guide tells the epic in its seven books, and follows Rāma through poems, places and festivals.'],
 'Can a whole epic fit in one guide?','The outline can. And every chapter is a door into a thousand retellings.',
 series_note_dv(7))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Avatāra','<b>Seventh</b> of the ten; Tretā Yuga'),('Form','A prince with a <b>bow</b>, dark-blue, with Sītā, Lakṣmaṇa and Hanumān'),
 ('Parents','King Daśaratha and Queen Kausalyā of Ayodhyā'),('Deed','Defeats Rāvaṇa of Laṅkā and restores dharma'),
 ('Epic','The Rāmāyaṇa of Vālmīki, in seven kāṇḍas (books), about 24,000 verses'),('Title','Maryādā Puruṣottama: the ideal man who keeps every bound'),
 ('Places','Ayodhyā, Citrakūṭa, Pañcavaṭī, Kiṣkindhā (Hampi), Rāmeśvaram'),('Day','Rāma Navamī, Caitra')])
 +talk("Why is Rāma so loved?","He did the right thing every time, even when it cost him everything. People still try to live like that.")))
pages.append(page('names','NAMES','The one who delights',facts([
 ('Rāma','“Delightful”, “one who gives joy”'),('Rāghava','Of the Raghu dynasty'),('Dāśarathi','Son of Daśaratha'),('Kodaṇḍarāma','Rāma with the Kodaṇḍa bow'),('Sītārāma','Rāma with Sītā'),('Raghupati','Lord of the Raghus'),('Śrīrāma','The holy Rāma: also the two-syllable name chanted by millions')])))
pages.append(page('bala','1. BĀLA KĀṆḌA','Childhood and the bow',facts([
 ('Birth','Childless Daśaratha performed a sacrifice; four sons were born: Rāma, Bharata, Lakṣmaṇa and Śatrughna'),
 ('Viśvāmitra','The sage took the boys to protect his rites; Rāma killed the demoness Tāṭakā and freed Ahalyā from a curse'),
 ('Sītā','At Mithilā, King Janaka’s daughter, found in a furrow, was to marry whoever could string Śiva’s bow'),
 ('The bow','Rāma lifted, strung and broke it'),
 ('Paraśurāma','The axe-bearing avatāra came in anger and yielded to Rāma')])
 +'<div class="key">The meeting: <a href="'+DVS+'parashurama/">Paraśurāma</a></div>'))
pages.append(page('ayodhya','2. AYODHYĀ KĀṆḌA','The exile',fig(560,160,'A prince, his wife and his brother walking away from a palace towards a forest',
 '<rect width="560" height="160" fill="#fff4dc"/>'+TEMPLE(100,150,2.4)+''.join(f'<path d="M{380+i*36} 150 l12 -50 l12 50z" fill="#2a7a3a" stroke="#111"/>' for i in range(5))+RAMA(250,120,.6)+GENTLE(300,126,.45)+person(340,148,'#e0a800','#f2c79b',.5))+facts([
 ('The promise','Queen Kaikeyī claimed two boons Daśaratha once gave her: her son Bharata to be king, Rāma to go to the forest for fourteen years'),
 ('Rāma’s choice','He went calmly to keep his father’s word; Sītā and Lakṣmaṇa insisted on going with him'),
 ('Daśaratha','The king died of grief'),
 ('Bharata','Refused the throne, placed Rāma’s sandals on it and ruled as his deputy')])
 +talk("He just accepted it?","That's Rāma. His father's word mattered more than his own crown.")))
pages.append(page('aranya','3. ARAṆYA KĀṆḌA','The forest and the golden deer',facts([
 ('The forest','The three lived among sages at Citrakūṭa and Pañcavaṭī'),
 ('Śūrpaṇakhā','Rāvaṇa’s sister tried to seduce Rāma and attacked Sītā; Lakṣmaṇa cut off her nose'),
 ('The golden deer','A demon in disguise lured Rāma away; Lakṣmaṇa followed at Sītā’s urging'),
 ('The abduction','Rāvaṇa, disguised as a holy man, carried Sītā off to Laṅkā'),
 ('Jaṭāyu','The old vulture fought Rāvaṇa and fell; he lived only to tell Rāma'),
 ('Śabarī','A tribal woman devotee fed Rāma berries she had tasted first, and he ate them gladly')])))
pages.append(page('kishkindha','4. KIṢKINDHĀ KĀṆḌA','Hanumān and the monkey kingdom',fig(560,170,'A boulder-strewn landscape with a river, a vānara warrior bowing to Rama',
 '<rect width="560" height="170" fill="#f2e6c8"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*0.7}" fill="#c9a26b" stroke="#111" stroke-width="2"/>' for x,y,r in ((60,130,40),(130,110,30),(470,120,44),(520,90,26),(420,80,24)))+'<rect y="150" width="560" height="20" fill="#5ab0f0"/>'+RAMA(320,120,.7)+MONKEY(220,134,.8))+facts([
 ('Hanumān','At Ṛṣyamūka, Rāma met Hanumān, minister of the exiled vānara prince Sugrīva'),
 ('The pact','Rāma killed Sugrīva’s brother Vālī and made Sugrīva king; Sugrīva promised to find Sītā'),
 ('Hampi','Tradition places Kiṣkindhā around Hampi on the Tuṅgabhadrā; Añjanādri hill nearby is called Hanumān’s birthplace'),
 ('Places at Hampi','Ṛṣyamūka, Mālyavanta hill (where Rāma waited out the rains), Paṃpā Sarovar (Śabarī’s lake)')])
 +talk("The Rāmāyaṇa happened in Karnataka?","This part, by tradition. Hampi's boulders are Kiṣkindhā.")))
pages.append(page('sundara','5. SUNDARA KĀṆḌA','Hanumān’s leap',facts([
 ('The leap','Hanumān leaped across the ocean to Laṅkā'),
 ('Sītā found','He found her in the Aśoka grove, refusing Rāvaṇa, and gave her Rāma’s ring'),
 ('Laṅkā burns','Captured, his tail set on fire, he burned the city and leapt back'),
 ('The sign','He brought Rāma Sītā’s hair jewel (cūḍāmaṇi)'),
 ('Sundara','“The beautiful book”: much loved and recited on its own')])
 +talk("Why is it called beautiful?","Because hope returns in it. Sītā is found, and Hanumān shows what devotion can do.")))
pages.append(page('yuddha','6. YUDDHA KĀṆḌA','The bridge and the war',fig(560,170,'A long bridge of stones across the sea to an island with a golden city',
 '<rect width="560" height="170" fill="#cfe8f6"/>'+OCEAN(560,80,90,'#3b8fd0')+'<path d="M0 120 h80 V170 H0Z" fill="#5a9a4a"/><path d="M460 120 h100 V170 H460Z" fill="#5a9a4a"/>'+''.join(f'<ellipse cx="{90+i*24}" cy="118" rx="12" ry="6" fill="#c9a26b" stroke="#111"/>' for i in range(16))+''.join(f'<rect x="{480+i*14}" y="{80-i*6}" width="12" height="{40+i*6}" fill="#e0a800" stroke="#111"/>' for i in range(5)))+facts([
 ('Vibhīṣaṇa','Rāvaṇa’s good brother came over to Rāma'),
 ('Rāmeśvaram','Rāma worshipped Śiva on the shore before the crossing'),
 ('Rāma Setu','The vānaras built a bridge of floating stones across the sea'),
 ('The war','Kumbhakarṇa and Indrajit fell; Lakṣmaṇa was revived by the herb Hanumān fetched on a whole mountain'),
 ('Rāvaṇa','Rāma killed him with the brahmāstra'),
 ('Sītā','Her purity was proved by fire (agni parīkṣā)')])
 +'<div class="key">See: <a href="'+TI+'12-jyotirlingas/rameswaram/">Rāmeśvaram</a></div>'))
pages.append(page('uttara','7. UTTARA KĀṆḌA','Rāma-rājya and after',facts([
 ('Return','Rāma came home to Ayodhyā; the city lit lamps, remembered in Dīpāvalī in North India'),
 ('Rāma-rājya','His reign became the model of just and happy rule'),
 ('Sītā’s exile','Hearing gossip, Rāma sent Sītā away; in Vālmīki’s hermitage she bore the twins Lava and Kuśa'),
 ('The end','Sītā returned to the Earth, her mother; Rāma later entered the Sarayū and returned to Viṣṇu'),
 ('Debate','The Uttara Kāṇḍa is thought by many scholars to be a later addition, and its story of Sītā is much debated')])
 +talk("He sent Sītā away? That's not fair!","Many readers, and many later poets, felt the same. The Rāmāyaṇa leaves us to argue about it.")))
pages.append(page('ideal','MARYĀDĀ PURUṢOTTAMA','The ideal man',facts([
 ('Son','He gave up a kingdom for his father’s word'),('Brother','He and his brothers are models of loyalty'),('Husband','One wife, Sītā, in an age of many'),
 ('Friend','To Sugrīva, Vibhīṣaṇa, Guha the boatman and Śabarī alike'),('King','Rāma-rājya, rule for the people'),
 ('Rāvaṇa','Even his enemy was a great scholar and devotee of Śiva; tradition says Rāma honoured him in death')])
 +'<div class="key">Rāvaṇa’s past life: <a href="'+DVS+'varaha/">Jaya and Vijaya</a></div>'))
pages.append(page('ramayanas','MANY RĀMĀYAṆAS','Retold in every language',facts([
 ('Vālmīki','The Sanskrit Ādi Kāvya, “first poem”'),
 ('Kamban','Tamil Irāmāvatāram, 12th century'),
 ('Kannada','Nāgacandra’s Jain Rāmacandra Carite Purāṇa (Pampa Rāmāyaṇa, c. 1100) and Kumāra Vālmīki’s Torave Rāmāyaṇa (15th c.)'),
 ('Tulasīdāsa','Hindi Rāmacaritamānas, 16th century, the most read in the north'),
 ('Others','Kṛttivāsa (Bengali), Ezhuthachan (Malayalam), Molla (Telugu), Ādhyātma Rāmāyaṇa'),
 ('Asia','Thailand’s Ramakien, Indonesia’s Kakawin Rāmāyaṇa, Cambodia’s Reamker')])))
pages.append(page('temples','RĀMA’S TEMPLES','Where he is worshipped',facts([
 ('Ayodhyā','His birthplace by tradition; the new Rāma temple was consecrated on 22 January 2024'),
 ('Bhadrācalam','Telangana, on the Godāvarī; built by Bhakta Rāmadāsa in the 17th century'),
 ('Rāmeśvaram','Where Rāma worshipped Śiva; a Jyotirliṅga'),
 ('Śrīraṅgam','Rāma’s family deity, Raṅganātha, gifted to Vibhīṣaṇa, came to rest there'),
 ('Hampi','The Hazāra Rāma temple of Vijayanagara, its walls carved with the Rāmāyaṇa'),
 ('Karnataka','Kodaṇḍarāma temples across the state, as at Hiremagaḷūr and Vaḍayār')])
 +'<div class="key">See: <a href="'+TI+'triranga/antya-ranga/">Śrīraṅgam</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','His days',facts([
 ('Rāma Navamī','Caitra Śukla Navamī (Mar–Apr): his birthday, with Rāmāyaṇa readings and weddings of Sītā and Rāma'),
 ('Vijayadaśamī','Rāvaṇa’s effigies burned in North India; Rāmlīlā plays'),
 ('Dīpāvalī','In the north, his return to Ayodhyā'),
 ('Vivāha Pañcamī','Mārgaśīrṣa: Sītā and Rāma’s wedding')])))
pages.append(page('meaning','WHAT RĀMA TEACHES','The wisdom of the bow',facts([
 ('Keep your word','A promise is worth a kingdom'),('Bear hardship calmly','Exile without bitterness'),('Friendship across lines','Vānaras, a boatman, a tribal woman, a demon’s brother'),('Hard questions','Even the ideal king faces choices we still debate')])
 +talk("What should I take from Rāma?","Do your duty even when it hurts. And ask hard questions about it, as readers always have.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Kāṇḍa','Book of the epic'),('Maryādā','Bound, propriety'),('Setu','Bridge'),('Vānara','The forest people who served Rāma'),('Agni parīkṣā','Trial by fire'),('Rāma-rājya','Rule of Rāma'),('Ādi Kāvya','First poem'),('Kodaṇḍa','Rāma’s bow')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Rāma, prince of Ayodhyā, seventh avatāra of Viṣṇu.</div>
<div><b>Story.</b> Exile, Sītā’s abduction, Hanumān, the bridge, Rāvaṇa’s fall, Rāma-rājya.</div>
<div><b>Ideal.</b> Maryādā Puruṣottama: son, brother, husband, friend, king.</div>
<div><b>Everywhere.</b> Retold in every language; Kiṣkindhā at Hampi; Ayodhyā; Bhadrācalam.</div>
<div><b>Lesson.</b> Keep your word, and keep asking what duty means.</div>
</div>'''+talk("One line to remember?","Rāma kept every promise. That's why we still tell his story.")+'<div class="key">Next: <a href="'+DVS+'balarama-buddha/">Balarāma and the Buddha</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Vālmīki Rāmāyaṇa (seven kāṇḍas; critical edition notes on the Uttara Kāṇḍa); Kamban, Irāmāvatāram; Tulasīdāsa, Rāmacaritamānas; Kumāra Vālmīki, Torave Rāmāyaṇa; Nāgacandra, Rāmacandra Carite Purāṇa.</p>
<p><b>Places:</b> Hampi (Kiṣkindhā traditions, Hazāra Rāma temple) from Karnataka Tourism and ASI; Ayodhyā Rāma temple consecration, 22 January 2024 (news reports); Bhadrācalam and Bhakta Rāmadāsa; Rāmeśvaram from our Jyotirliṅga guide.</p>
<p><b>Sources differ / unverified:</b> the dates of Rāma and the epic; the identification of Kiṣkindhā with Hampi and of Añjanādri as Hanumān’s birthplace (other places also claim it); the Uttara Kāṇḍa’s authenticity; the honouring of Rāvaṇa in death varies by retelling. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('bala','Bāla Kāṇḍa'),('ayodhya','Ayodhyā Kāṇḍa'),('aranya','Araṇya Kāṇḍa'),('kishkindha','Kiṣkindhā Kāṇḍa'),('sundara','Sundara Kāṇḍa'),('yuddha','Yuddha Kāṇḍa'),('uttara','Uttara Kāṇḍa'),
 ('ideal','Maryādā Puruṣottama'),('ramayanas','Many Rāmāyaṇas'),('temples','Rāma’s Temples'),('festivals','Through the Year'),('meaning','What Rāma Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV7_Rama.html',head,cov,fw,pages,toc)
