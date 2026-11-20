exec(open('/home/claude/work/shakti/sk_common.py').read())
head=head_navy('Kukke Subrahmaṇya · Subrahmaṇya Ṣaṣṭhī 3 · srini.presents',
 'Kukke Subrahmaṇya, on the Kumāradhārā in Dakṣiṇa Kannaḍa: Subrahmaṇya as the serpent lord, Vāsuki hiding from Garuḍa in the Biladvāra cave, the three-tier sanctum with Vāsuki and Śeṣa, the Garuḍa pillar, Ādi Subrahmaṇya’s anthill, Śaṅkara’s Kukke liṅga, the nāga rites, Kumāra Parvata and the Campā Ṣaṣṭhī chariot. An illustrated reference guide.')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A seven-hooded cobra coiled in front of a sloping-roofed Karnataka temple, with forested hills and a river below">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+HILL(80,230,240,170,'#2a6a3a')+HILL(300,230,260,190,'#3a7a3a')+'<rect y="226" width="380" height="42" fill="#1d6fb8"/>'
 +KTEMPLE(250,224,1.05)+NAGA(110,222,1.15)+'</svg>')
cov=cover('PART 3 OF 4','KUKKE SUBRAHMAṆYA',12,'The serpent lord on the Kumāradhārā',art)
fw=foreword('Om Śrī Subrahmaṇyāya Namaḥ,',[
 'Deep in the forests of the Western Ghats, where the Kumāradhārā river comes down from <b>Kumāra Parvata</b>, Śiva’s son is worshipped not as a warrior with a spear but as the lord of serpents.',
 'Here, the story goes, the great serpent <b>Vāsuki</b> hid in a cave from <b>Garuḍa</b>, and Subrahmaṇya promised to stay with him forever. So at <b>Kukke</b> the god and the serpent are worshipped together, and families from all over India come for the rites of the nāgas.',
 'This part tells the stories, walks through the shrine, and explains the festival that makes Kukke the heart of Subrahmaṇya Ṣaṣṭhī.'],
 'A god worshipped as a snake?','As the snake’s protector, and in the snake. At Kukke the two cannot be separated.',
 series_note(prev=('shashthi','The Ṣaṣṭhī Story'),nxt=('ghati','Ghāṭi Subrahmaṇya')))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Where','Subrahmaṇya village, Kaḍaba taluk, <b>Dakṣiṇa Kannaḍa</b>, Karnataka, on the <b>Kumāradhārā</b> river'),
 ('God','<b>Subrahmaṇya</b> as lord of the serpents, with <b>Vāsuki</b> and <b>Śeṣa</b>'),
 ('Setting','Forest of the Western Ghats, below <b>Kumāra Parvata</b>'),
 ('Legend','Vāsuki’s refuge from Garuḍa; Skanda’s wedding with Devasenā'),
 ('Known for','Rites for the nāgas: sarpa saṃskāra, āśleṣā bali, nāga pratiṣṭhā'),
 ('Worship','Daily rites follow Madhvācārya’s <b>Tantrasāra Saṅgraha</b>'),
 ('Festival','<b>Campā Ṣaṣṭhī</b> (Mārgaśīrṣa śuddha Ṣaṣṭhī) with the great chariot'),
 ('Tradition','One of the seven sacred places said to be set up by <b>Paraśurāma</b> on the west coast')])
 +talk("Why is everyone here for snakes?","Because the serpent king himself lives here, under the god's protection. Who better to ask?")))
pages.append(page('names','ITS NAMES','Kukke, Subrahmaṇya, Subbappa',facts([
 ('Kukke Subrahmaṇya','The temple’s common name; “Kukke” is tied to the old <b>Kukke liṅga</b> worshipped here'),
 ('Subrahmaṇya','Also the name of the village around the temple'),
 ('Kukke Śrī Subrahmaṇya Svāmi','The full temple name'),
 ('Subbappa, Subbarāya','Affectionate Kannaḍa and Tuḷu names for the god'),
 ('Annadāta Subbappa','“Subbappa the giver of food”: the temple is known for feeding pilgrims'),
 ('Ahipeśvara','“Lord of serpents”: an old name of the Kukke liṅga')])))
pages.append(story('vasuki','VĀSUKI AND GARUḌA','The serpent who hid in a cave',560,190,'A great eagle swooping down at the mouth of a cave in a forested hill, where a many-hooded serpent hides',
 '<rect width="560" height="190" fill="#cfe3f5"/>'+HILL(300,190,460,170,'#3a7a3a')+'<path d="M260 190 q0 -60 50 -60 q50 0 50 60z" fill="#1a1a1a" stroke="#111" stroke-width="2"/>'+NAGA(310,186,.65,5,coil=False)
 +'<g transform="translate(130 60)" stroke="#111" stroke-width="2"><path d="M-60 0 q30 -30 60 0 q30 -30 60 0 q-30 14 -60 10 q-30 4 -60 -10z" fill="#e0701a"/><circle cx="0" cy="4" r="10" fill="#e8b04a"/><path d="M6 6 l10 4 l-10 4z" fill="#e0a800"/></g>',
 [('The enemy.','<b>Garuḍa</b>, the eagle who carries Viṣṇu, was the old enemy of the serpents and hunted them to eat.'),
  ('The hiding place.','<b>Vāsuki</b>, king of serpents and a great devotee of Śiva, hid in a cave called <b>Biladvāra</b> near the Kumāradhārā, deep in prayer.'),
  ('The fight.','In one telling Garuḍa found him and attacked, until the sage Kaśyapa, father of both, asked him to spare Śiva’s devotee.'),
  ('Śiva’s answer.','Vāsuki prayed to Śiva for safety. Śiva sent him to his son: “Subrahmaṇya will protect you.”'),
  ('The promise.','Subrahmaṇya came, blessed Vāsuki and promised to stay here with him forever. So worship of Vāsuki here is worship of Subrahmaṇya.')],
 talk("Isn't the peacock also a snake-eater?","Yes, and still it is the snake who gets refuge. That's the point: the god protects even his mount's prey.")))
pages.append(story('wedding','THE WEDDING AND THE RIVER','Kumāra Parvata and the Kumāradhārā',560,170,'A tall forested peak with a river streaming down from it past a temple',
 '<rect width="560" height="170" fill="#eaf1fb"/>'+HILL(200,170,320,160,'#2a6a3a')+'<path d="M200 20 q30 60 0 90 q-30 30 60 60" fill="none" stroke="#4aa3df" stroke-width="8"/>'+KTEMPLE(420,160,.7),
 [('After the war.','In this tradition, after killing Tāraka and Śūrapadma, Skanda came with <b>Gaṇeśa</b> to the peak now called <b>Kumāra Parvata</b>.'),
  ('The wedding.','Indra gave him <b>Devasenā</b> on Mārgaśīrṣa śuddha Ṣaṣṭhī, with the gods present.'),
  ('The river.','Waters of all the sacred rivers brought for the wedding flowed down as the <b>Kumāradhārā</b>, “the stream of Kumāra”.'),
  ('The vel washed.','Another telling says he washed his vel in this river after the war.'),
  ('The bath.','So pilgrims bathe in the Kumāradhārā before entering the temple.')],
 f'<div class="key">The full war story: <a href="{SKS}shashthi/">The Ṣaṣṭhī Story</a> (Part 2)</div>'))
pages.append(page('sanctum','THE SANCTUM','God above, serpents below',fig(560,190,'A three-level shrine: the six-faced god on top, a many-hooded serpent in the middle, and a coiled serpent at the base, with a silver pillar in front',
 '<rect width="560" height="190" fill="#1a2a3a"/><path d="M190 186 h180 v-170 h-180z" fill="#3a2a1a" stroke="#111" stroke-width="2"/>'
 +NAGA(280,180,.55,5)+NAGA(280,132,.55,7,'#2a6a5a',coil=False)+SKANDA(280,66,.42,vel=False)
 +'<g transform="translate(470 186)" stroke="#111" stroke-width="2"><rect x="-8" y="-150" width="16" height="150" fill="#d0d8e0"/><path d="M-20 -150 q20 -30 40 0z" fill="#d0d8e0"/><path d="M-14 -166 q14 -10 28 0" fill="#e0701a"/></g>')+facts([
 ('Top','<b>Subrahmaṇya</b>, seated, the lord of the shrine'),
 ('Middle','<b>Vāsuki</b>, king of serpents, whom he protects'),
 ('Base','<b>Śeṣa</b> (Ādiśeṣa), the serpent Viṣṇu rests on'),
 ('Garuḍa pillar','A silver-covered pillar stands between the sanctum and the entrance; tradition says it shields devotees from the fiery breath of Vāsuki')])
 +talk("Garuḍa guards the people from the serpent here?","Neatly balanced. Garuḍa can't touch Vāsuki, and Vāsuki's breath can't touch you.")))
pages.append(page('adi','ĀDI SUBRAHMAṆYA AND BILADVĀRA','The anthill and the cave',fig(560,170,'A small shrine with a large anthill inside, and nearby a dark cave opening in the rock',
 '<rect width="560" height="170" fill="#eef5e8"/>'+KTEMPLE(170,160,.8,'#f2e6c8','#7a3a2a')+ANTHILL(170,150,.5)+'<path d="M330 160 q10 -90 100 -90 q90 0 100 90z" fill="#7a6a5a" stroke="#111" stroke-width="2"/><path d="M400 160 q0 -50 30 -50 q30 0 30 50z" fill="#1a1a1a" stroke="#111" stroke-width="2"/>')+facts([
 ('Ādi Subrahmaṇya','A short walk north of the main gopura: a separate shrine where an <b>anthill</b> (valmīka) in the sanctum is worshipped every day'),
 ('Why “Ādi”','“The first”: held to be the original seat of the serpent god'),
 ('Biladvāra','“The door of the hole”: the cave where Vāsuki is said to have hidden and prayed'),
 ('Kāśikaṭṭe Gaṇapati','An old Gaṇeśa shrine nearby, said in tradition to be set up by Nārada'),
 ('Darpaṇa tīrtha','A stream behind the temple, flowing into the Kumāradhārā')])))
pages.append(page('linga','THE KUKKE LIṄGA AND ŚAṄKARA','A liṅga in Skanda’s home',facts([
 ('Kukke liṅga','Before the present image, worship centred on the <b>Kukke liṅga</b>, also called <b>Ahipeśvara</b>, “lord of serpents”'),
 ('Śaṅkara','The biographies of Ādi Śaṅkara record his visit here'),
 ('The hymn','In the <b>Subrahmaṇya Bhujaṅgam</b>, attributed to Śaṅkara, a verse praises the god as the “Kukke liṅga”'),
 ('The metre','Bhujaṅga, “the serpent”: a gliding metre, fitting for a serpent shrine'),
 ('Two lineages','A Śṛṅgeri maṭha and the Chandramauḷīśvara shrine stand in the precincts; the Subrahmaṇya Maṭha of the Mādhva tradition is beside the temple')])
 +talk("A Śiva liṅga in Subrahmaṇya's temple?","Father and son share the house. The son's name was first written on the father's stone.")))
pages.append(page('rites','THE NĀGA RITES','Why families come to Kukke',fig(560,150,'Priests and a family seated before a sacred fire, with a small serpent image and lamps',
 '<rect width="560" height="150" fill="#fdf1e8"/>'+FLAME(280,140,.9)+CROWD(110,145,4,26)+CROWD(370,145,4,26)+NAGA(470,140,.4,5))+facts([
 ('Sarpa saṃskāra','A two-day rite, like last rites for a serpent, done by those who believe they harmed a snake, in this life or another'),
 ('Āśleṣā bali','A rite on the day of the Āśleṣā star, sacred to the serpents'),
 ('Nāga pratiṣṭhā','Installing a stone serpent image, often after a vow'),
 ('Sought for','Children, health, marriage, and relief from <b>sarpa doṣa</b>, the trouble believed to follow harm to serpents'),
 ('Tradition','Kept by the temple’s priests; details and rules are given by the temple')])
 +talk("Do these rites really work?","That's for the believer. What's certain is how old the trust in them is along this coast.")))
pages.append(page('festival','CAMPĀ ṢAṢṬHĪ AT KUKKE','The great chariot',fig(560,190,'A tall red and gold temple chariot pulled by a crowd with ropes, in front of the temple',
 '<rect width="560" height="190" fill="#f2c27a"/>'+KTEMPLE(110,180,.8)+RATHA(330,180,1.05)+'<path d="M370 160 L540 170" stroke="#7a5a2a" stroke-width="3"/>'+CROWD(400,186,9,18))+facts([
 ('When','<b>Mārgaśīrṣa śuddha Ṣaṣṭhī</b>, the day of the wedding: Subrahmaṇya Ṣaṣṭhī'),
 ('Festival','A run of days with processions, ending in the <b>Brahmaratha</b>, the great chariot, pulled by devotees'),
 ('Other days','<b>Kiru Ṣaṣṭhī</b>, the “small Ṣaṣṭhī”; <b>Nāgara Pañcamī</b>; <b>Nāgārādhane</b>'),
 ('Crowds','The busiest days of the year at Kukke'),
 ('Feeding','Pilgrims are fed by the temple, true to the name Annadāta Subbappa')])))
pages.append(page('history','HISTORY','Priests, maṭhas and the State',facts([
 ('Paraśurāma kṣetra','Counted among the seven holy places of the coast said to be set up by Paraśurāma'),
 ('Style','Built in the Karnataka coastal style: sloping tiled roofs, wood, granite'),
 ('Stewards','The Koojugodu Kattemane family long served as chief administrators, with close ties to Śṛṅgeri'),
 ('Priests','Priesthood passed between Brahmin communities in the 19th century; the Śrī Subrahmaṇya Sabhā was founded in 1908'),
 ('Today','Run by the Karnataka Endowment Department; among the state’s richest temples by income')])
 +talk("Why so many groups in one temple's story?","Big temples gather many hands. The god stays the same; the stewards change.")))
pages.append(page('around','AROUND KUKKE','The sacred landscape',facts([
 ('Kumāra Parvata','The peak above Kukke, sacred as the place of the wedding'),
 ('Kumāradhārā','The river of the wedding waters, where pilgrims bathe'),
 ('Garuḍa folklore','Locals say Garuḍa never flies over the temple or the peak, out of respect for Vāsuki’s refuge'),
 ('Serpent country','The coast of Tuḷunāḍu is full of nāga groves (nāga-bana), honoured by every family'),
 ('In this series','<a href="'+SKS+'ghati/">Ghāṭi Subrahmaṇya</a>, the serpent shrine near Bengaluru')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Nāga','Serpent, cobra'),('Vāsuki','King of serpents'),('Śeṣa','The serpent who bears Viṣṇu'),('Garuḍa','Viṣṇu’s eagle'),('Biladvāra','Cave door'),
 ('Valmīka','Anthill'),('Sarpa saṃskāra','Rite for a serpent'),('Brahmaratha','The great chariot'),('Nāga-bana','Sacred serpent grove')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Where.</b> Kukke, on the Kumāradhārā in the forests of Dakṣiṇa Kannaḍa.</div>
<div><b>The story.</b> Vāsuki hid from Garuḍa in Biladvāra; Subrahmaṇya promised to stay with him forever.</div>
<div><b>The shrine.</b> Subrahmaṇya above, Vāsuki and Śeṣa below, a Garuḍa pillar in front; the anthill at Ādi Subrahmaṇya.</div>
<div><b>The rites.</b> Sarpa saṃskāra, āśleṣā bali, nāga pratiṣṭhā.</div>
<div><b>The day.</b> Campā Ṣaṣṭhī, the wedding day, with the great chariot.</div>
</div>'''+talk("What's next?","A second serpent shrine, with a secret: two gods in one stone. Part 4: Ghāṭi Subrahmaṇya.")
 +f'<div class="key">Part 3: Kukke. Next: <a href="{SKS}ghati/">Ghāṭi Subrahmaṇya</a> 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple and legend:</b> Wikipedia, “Kukke Subramanya Temple” (Kumāradhārā, Dakṣiṇa Kannaḍa; Subrahmaṇya as Nāga; Paraśurāma’s seven sites; Vāsuki and Garuḍa; Kumāra Parvata and Devasenā; Ṣaṣṭhī, Kiru Ṣaṣṭhī, Nāgara Pañcamī, Nāgārādhane; Koojugodu Kattemane family, Śṛṅgeri maṭha and Chandramauḷīśvara shrine; priests and the 1908 Sabhā; Tantrasāra Saṅgraha). Wikipedia, “Subramanya, Karnataka” (Kukke / Ahipeśvara liṅga; Śaṅkara; Ādi Subrahmaṇya anthill about 250 m away; Biladvāra; Darpaṇa tīrtha). kukkedevasthanam.org.in (Skanda Purāṇa, Sahyādri Khaṇḍa; Campā Ṣaṣṭhī as the wedding). gosai.com (Kaśyapa stopping Garuḍa; Bhujaṅgam’s Kukke liṅga). imvoyager.com (three-tier sanctum). traveltriangle.com (Garuḍa pillar). navrangindia blog (wedding waters forming the river).</p>
<p><b>Traditions differ</b> on the details of the Vāsuki story and the wedding. <b>Not verified from a primary source:</b> the Garuḍa folklore, the order of the three tiers, the meaning of “Kukke”, the temple’s income ranking. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Its Names'),('vasuki','Vāsuki and Garuḍa'),('wedding','The Wedding and the River'),('sanctum','The Sanctum'),('adi','Ādi Subrahmaṇya and Biladvāra'),
 ('linga','The Kukke Liṅga and Śaṅkara'),('rites','The Nāga Rites'),('festival','Campā Ṣaṣṭhī at Kukke'),('history','History'),('around','Around Kukke'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/SK3_Kukke.html',head,cov,fw,pages,toc)
