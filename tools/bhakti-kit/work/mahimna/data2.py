from data import talk,svg,T,LINGA,bird
D=dict
STAR=lambda x,y,r=3,c='#ffd60a': f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
V=[
D(theme='ONE TOE ON KAILĀSA',
 svg=svg('Ravana with many arms straining under Mount Kailasa while Shiva presses down with one toe',
  '<path d="M20 120 L90 30 L130 60 L200 120Z" fill="#e8f0f8" stroke="#111" stroke-width="2.5"/><path d="M90 30 l12 14 l-24 0z" fill="#fff" stroke="#111" stroke-width="1.5"/>'
  '<g stroke="#111" stroke-width="2.5"><circle cx="110" cy="14" r="8" fill="#bcd4f0"/><path d="M110 22 v14" /><path d="M110 36 q-2 6 -6 10" fill="none"/></g><text x="150" y="20" font-family="Bangers" font-size="11" fill="#c0392b">ONE TOE</text>'
  +''.join(f'<path d="M110 150 L{40+16*i} 122" stroke="#7a3fa0" stroke-width="4"/>' for i in range(10))
  +'<circle cx="110" cy="150" r="10" fill="#7a3fa0" stroke="#111" stroke-width="2"/><text x="110" y="112" text-anchor="middle" font-family="Bangers" font-size="11">KAILĀSA</text>'),
 mean='That forest of arms, which had won its strength by serving You, he forced into a show of might even on Kailāsa, Your own dwelling. Then, when You idly moved the tip of Your big toe, he could not find a footing even in the netherworld. Surely the wicked, once they swell with power, lose their senses.',
 plain='Rāvaṇa\'s arms got their strength from worshipping Śiva, and he used them to lift Śiva\'s own mountain. One lazy press of Śiva\'s toe, and he sank to the underworld. Power makes the proud foolish.',
 words=[('bhuja-vanam','the <b>forest of arms</b>'),('tvat-sevā','<b>service to You</b>'),('vikramayataḥ','of one <b>showing off his strength</b>'),('alasa-calita','<b>idly moved</b>'),('aṅguṣṭha-śiras','the <b>tip of the big toe</b>'),('upacitaḥ muhyati khalaḥ','<b>the wicked, grown strong, grows deluded</b>')],
 deep='<p><b>The same arms.</b> Verse 11 praised Rāvaṇa\'s devotion; verse 12 shows what he did with its reward. The strength Śiva gave him, he turned against Śiva\'s own home, trying to lift Kailāsa.</p><p><b>One toe.</b> The poet\'s words are precise: <i>alasa-calita</i>, "idly moved". Śiva doesn\'t fight. He barely moves a toe, and Rāvaṇa finds no ground to stand on, even in the netherworld.</p><p><b>The moral.</b> <i>Upacito muhyati khalaḥ</i>: the wicked, when they grow strong, lose their judgement. Our Śiva Tāṇḍava article tells what happened next: trapped under the mountain, Rāvaṇa sang.</p>',
 cards=('💡 Pātāla','The lowest of the netherworlds in Purāṇic cosmology.','💡 Same story','The Śiva Tāṇḍava Stotram is said to be the song Rāvaṇa sang under this mountain.'),
 inner='Strength that came from grace, used against grace, collapses. Remember where your power came from.',
 talk=('So Rāvaṇa used Śiva\'s own gift against Him?','Exactly. And Śiva didn\'t even get up. The verse is about how small pride is next to the Lord.'),
 key='Strength from devotion, misused in pride: <b>one toe was enough</b>.'),
D(theme='BĀṆA, WHO BOWED',
 svg=svg('A thousand-armed figure bowing with all his hands folded before a linga',
  '<g transform="translate(160 132)">'+LINGA+'</g>'
  +''.join(f'<path d="M70 96 L{70+44*__import__("math").cos(a/10)} {96-44*__import__("math").sin(a/10)}" stroke="#c0703a" stroke-width="2"/>' for a in range(-6,38,3))
  +'<g stroke="#111" stroke-width="2.5"><circle cx="86" cy="98" r="11" fill="#f2c79b"/><path d="M50 140 q20 -40 40 -36 l10 24z" fill="#e63946"/></g><text x="70" y="26" text-anchor="middle" font-family="Bangers" font-size="11">1,000 ARMS · ONE BOW</text>'),
 mean='That Bāṇa, with the three worlds as his servants, put beneath him the wealth of Indra, high as it was: O giver of boons, that is no wonder in one who served Your feet. Whose rise does not come from bowing the head to You?',
 plain='The demon king Bāṇa outshone even Indra\'s heaven. No surprise: he worshipped Śiva\'s feet. Bowing to Śiva lifts anyone up.',
 words=[('ṛddhiḥ','<b>prosperity, wealth</b>'),('sutrāman','<b>Indra</b>, the good protector'),('adhaś cakre','<b>put beneath</b>, surpassed'),('parijana-vidheya','<b>at the command of his servants</b>'),('varivasitṛ','<b>one who serves</b>'),('avanatiḥ','<b>bowing</b>')],
 deep='<p><b>Bāṇāsura.</b> Son of Bali, a thousand-armed devotee of Śiva who is said to have played the drum during Śiva\'s dance. Pleased, Śiva became the guardian of his city, Śoṇitapura.</p><p><b>The paradox.</b> The last line is the heart: <i>na kasyāpy unnatyai bhavati śirasas tvayy avanatiḥ</i>, "whose rise does not come from bowing the head to You?" Bowing down is how one rises.</p><p><b>Contrast with Rāvaṇa.</b> Verse 12 showed devotion turned to pride; verse 13 shows devotion that keeps bowing, and so keeps rising.</p>',
 cards=('💡 Bāṇāsura','The thousand-armed king whose daughter Uṣā married Kṛṣṇa\'s grandson Aniruddha.','💡 Bali\'s son','His father Bali is the generous king humbled by Vāmana.'),
 inner='Bowing is not a loss of height. The head that bows to the highest is lifted highest.',
 talk=('Bowing makes you rise? That sounds backwards.','It\'s the poet\'s favourite kind of paradox. Pride sank Rāvaṇa; humility raised Bāṇa.'),
 key='Bow the head to Śiva, and <b>you rise</b>.'),
D(theme='THE BLUE THROAT',
 svg=svg('Shiva drinking dark poison rising from the churned ocean, his throat turning blue, gods and demons watching',
  '<rect x="0" y="120" width="220" height="40" fill="#1d6fb8"/><path d="M110 120 q-30 -30 0 -50 q30 -20 0 -40" fill="none" stroke="#2b2b2b" stroke-width="8" opacity=".75"/>'
  '<g stroke="#111" stroke-width="2.5"><circle cx="110" cy="26" r="14" fill="#bcd4f0"/><rect x="104" y="40" width="12" height="10" fill="#1d4f9a"/></g><text x="150" y="48" font-family="Bangers" font-size="11" fill="#1d4f9a">NĪLAKAṆṬHA</text>'
  '<text x="40" y="112" text-anchor="middle" font-family="Bangers" font-size="10">DEVAS</text><text x="180" y="112" text-anchor="middle" font-family="Bangers" font-size="10">ASURAS</text><text x="110" y="150" text-anchor="middle" font-family="Bangers" font-size="11" fill="#fff">THE CHURNED OCEAN</text>'),
 mean='When gods and demons were terrified that the universe would be destroyed before its time, You, O three-eyed one, moved by compassion, swallowed the poison. That dark stain in Your throat: does it not make You beautiful? Ah, even a blemish is praiseworthy in one whose passion is to break the fear of the world.',
 plain='When the churning of the ocean threw up a world-ending poison, Śiva drank it out of compassion. The blue mark it left on His throat is His most beautiful ornament.',
 words=[('akāṇḍa','<b>untimely</b>, before its time'),('brahmāṇḍa-kṣaya','<b>destruction of the universe</b>'),('kṛpā-vidheya','<b>moved by compassion</b>'),('kalmāṣaḥ kaṇṭhe','the <b>dark stain in the throat</b>'),('vikāraḥ api ślāghyaḥ','<b>even a blemish is praiseworthy</b>'),('bhuvana-bhaya-bhaṅga','<b>breaking the world\'s fear</b>')],
 deep='<p><b>The churning of the ocean.</b> Gods and demons churned the ocean of milk for the nectar of immortality. First came <b>Hālāhala</b>, a poison that could end the world. Everyone ran to Śiva. He drank it, and Pārvatī held His throat so it would not go down. It stayed there, turning His throat blue: <b>Nīlakaṇṭha</b>.</p><p><b>The blemish that adorns.</b> A mark on the throat would be a flaw on anyone else. On Śiva it is his glory, because it is the scar of compassion.</p><p><b>Before its time.</b> <i>Akāṇḍa</i>: the world has a proper time to end; Śiva will not let it end by accident.</p>',
 cards=('💡 Hālāhala','The poison from the churned ocean, before the nectar emerged.','💡 Pradoṣa','Tradition links Śiva\'s drinking of the poison to the pradoṣa twilight worship.'),
 inner='The marks we carry from protecting others are not scars to hide. They are the most beautiful thing about us.',
 talk=('Why is His throat blue in pictures?','From the poison. He held it in His throat to save the world. The hymn calls that mark beautiful.'),
 key='A scar of compassion is <b>an ornament, not a flaw</b>.'),
D(theme='KĀMA BURNT TO ASH',
 svg=svg('Kama with a sugarcane bow and flower arrows facing Shiva\'s open third eye shooting fire, leaving ash',
  '<g stroke="#111" stroke-width="2.5"><circle cx="170" cy="50" r="18" fill="#bcd4f0"/><path d="M170 44 l-4 6 l4 6 l4 -6z" fill="#e63946"/></g><path d="M152 50 L70 80" stroke="#ff8c1a" stroke-width="6"/>'
  '<g stroke="#111" stroke-width="2.5"><circle cx="50" cy="90" r="12" fill="#f2c79b" opacity=".5"/><path d="M30 140 q20 -40 40 0z" fill="#f08aa6" opacity=".5"/><path d="M78 70 q14 30 0 60" fill="none" stroke="#2a9d6f" stroke-width="4"/></g>'
  '<ellipse cx="50" cy="146" rx="30" ry="6" fill="#999"/><text x="50" y="30" text-anchor="middle" font-family="Bangers" font-size="11">KĀMA</text><text x="170" y="90" text-anchor="middle" font-family="Bangers" font-size="11">THIRD EYE</text>'),
 mean='Kāma, whose arrows never return having failed, anywhere among gods, demons and men, ever victorious in the world: O Lord, seeing You as just another god, he became a mere memory. An insult to the self-controlled brings no good.',
 plain='Kāma, the god of desire, had never missed. He aimed at Śiva as if He were an ordinary god, and was burnt to ash; now he lives only in memory. Don\'t mock those who are masters of themselves.',
 words=[('asiddhārthāḥ','<b>unsuccessful</b>'),('viśikhāḥ','<b>arrows</b>'),('itara-sura-sādhāraṇam','<b>as ordinary as other gods</b>'),('smaraḥ','<b>Kāma</b>, "the remembered"'),('smartavyātmā','one who <b>exists only as a memory</b>'),('vaśiṣu paribhavaḥ','<b>insulting the self-controlled</b>')],
 deep='<p><b>The story.</b> To make Śiva marry Pārvatī, so a son could be born to defeat the demon Tāraka, the gods sent Kāma, god of desire, to disturb Śiva\'s meditation. Kāma shot his flower arrow. Śiva opened His third eye, and Kāma was burnt to ash.</p><p><b>A pun.</b> Kāma\'s name <i>Smara</i> means "remembering". The poet says he became <i>smartavyātmā</i>, "one whose self is only to be remembered": bodiless, alive only in the mind. Kāma is still called <b>Anaṅga</b>, "the bodiless".</p><p><b>The lesson.</b> Desire wins everywhere, except against the one who is master of himself.</p>',
 cards=('💡 Anaṅga','"The bodiless": Kāma\'s name after being burnt; Rati\'s prayers later won him life without a body.','💡 Kumārasambhava','Kālidāsa\'s great poem tells this story at length.'),
 inner='Desire\'s arrows hit almost everyone. The calm mind is the one target they cannot hit.',
 talk=('Desire never misses?','Never, says the hymn, among gods, demons or people. Except once: with Śiva. That\'s why He\'s the yogī\'s Lord.'),
 key='Desire conquers all, <b>except the master of himself</b>.'),
D(theme='THE DANCE THAT SHAKES THE WORLDS',
 svg=svg('Shiva dancing with flying matted hair, the earth trembling below and planets knocked about the sky',
  '<circle cx="110" cy="150" r="30" fill="#2a9d6f" stroke="#111" stroke-width="2.5"/><path d="M70 130 l-6 -4 M150 130 l6 -4" stroke="#111" stroke-width="2"/>'
  '<g stroke="#bcd4f0" stroke-width="5" stroke-linecap="round"><circle cx="110" cy="54" r="10" fill="#bcd4f0"/><path d="M110 64 v30 M110 74 l-24 -10 M110 74 l26 -14 M110 94 l-16 20 M110 94 l20 8"/></g>'
  '<path d="M104 46 q-40 -30 -70 -10 M116 46 q40 -36 80 -14" fill="none" stroke="#c9a26b" stroke-width="3"/>'
  +STAR(30,30,7,'#ff8c1a')+STAR(190,40,6,'#ffd60a')+STAR(176,90,5,'#e63946')+STAR(40,90,6,'#4aa3df')
  +'<text x="110" y="20" text-anchor="middle" font-family="Bangers" font-size="11" fill="#c0392b">TĀṆḌAVA</text>'),
 mean='At the stamping of Your feet the earth is suddenly in danger; the sky, Viṣṇu\'s realm, with its planets struck by Your whirling, club-like arms, spins; the heavens are troubled again and again, their edges lashed by Your flying matted hair. You dance to protect the world; yet surely, sovereignty works in contrary ways!',
 plain='When Śiva dances to protect the world, the earth shakes, the planets scatter and the heavens are lashed by His hair. Even His care looks dangerous: divine power works in strange ways.',
 words=[('pādāghāta','the <b>stamping of feet</b>'),('saṃśaya-padam','<b>a state of danger</b>, doubt'),('bhuja-parigha','<b>arms like iron clubs</b>'),('graha-gaṇa','the <b>host of planets</b>'),('jaṭā-tāḍita','<b>lashed by matted hair</b>'),('vāmā vibhutā','<b>sovereignty is contrary</b>')],
 deep='<p><b>The cosmic dance.</b> Śiva dances the tāṇḍava at the end of time and also, says the verse, for the world\'s protection. The images are huge: the earth sinking under His feet, planets knocked by His arms, the sky lashed by His hair.</p><p><b>Vāmā.</b> <i>Vāmā</i> means "contrary", "crooked", even "beautiful": the poet plays on all of them. God\'s power works in ways that look like the opposite of what they are.</p><p><b>Viṣṇu\'s step.</b> The sky is called "Viṣṇu\'s step" (<i>padaṃ viṣṇoḥ</i>), from the story of Vāmana measuring the worlds in three steps.</p>',
 cards=('💡 Naṭarāja','Śiva as Lord of Dance; see our Śiva Tāṇḍava article.','💡 Vāmana','Viṣṇu\'s dwarf form, whose stride became the sky.'),
 inner='Sometimes protection feels like an earthquake. What shakes us may be what saves us.',
 talk=('He dances to protect the world, and it shakes?','That\'s the poet\'s wonder: divine care doesn\'t always feel gentle. The word vāmā means both "contrary" and "lovely".'),
 key='Even His protecting dance <b>shakes the worlds</b>.'),
D(theme='THE GAṄGĀ AS A DROP',
 svg=svg('A tiny drop of the Ganga in Shiva\'s hair beside a huge river encircling the whole earth like an island in the ocean',
  '<circle cx="150" cy="96" r="50" fill="#1d6fb8" stroke="#111" stroke-width="2.5"/><circle cx="150" cy="96" r="30" fill="#2a9d6f" stroke="#111" stroke-width="2"/><text x="150" y="100" text-anchor="middle" font-family="Bangers" font-size="10" fill="#fff">EARTH</text>'
  '<g stroke="#111" stroke-width="2.5"><circle cx="40" cy="80" r="16" fill="#bcd4f0"/><path d="M28 70 q12 -26 24 0" fill="#c9a26b"/></g><circle cx="44" cy="62" r="3" fill="#4aa3df" stroke="#111"/>'
  '<path d="M47 60 L100 60" stroke="#111" stroke-dasharray="3 3"/><text x="40" y="120" text-anchor="middle" font-family="Bangers" font-size="10">A DROP ON HIS HEAD</text><text x="150" y="20" text-anchor="middle" font-family="Bangers" font-size="10">…RINGS THE WORLD</text>'),
 mean='The stream of waters that spreads across the sky, its foam made brighter by the clusters of stars, is seen on Your head as small as a droplet. That same stream made the world like an island ringed by the sea. From this alone one can guess how vast and divine is the form You bear.',
 plain='The heavenly Gaṅgā spans the sky, sparkling with stars; on Śiva\'s head it looks like one drop. Yet it rings the whole earth. Imagine how great He must be!',
 words=[('viyad-vyāpī','<b>spreading across the sky</b>'),('tārā-gaṇa','<b>clusters of stars</b>'),('phena','<b>foam</b>'),('pṛṣata-laghu','<b>small as a droplet</b>'),('jaladhi-valaya','<b>ringed by the ocean</b>'),('unneyam','<b>can be inferred</b>')],
 deep='<p><b>The sky river.</b> The heavenly Gaṅgā is pictured as the Milky Way, its foam the stars. When she fell to earth, Śiva caught her in His hair, where she looked like a single drop.</p><p><b>Scale.</b> The verse works by comparison: the river that rings the world is a droplet on His head. So how big is the head? The poet lets us do the arithmetic.</p><p><b>Bhagīratha.</b> King Bhagīratha brought the Gaṅgā down to purify his ancestors\' ashes; Śiva softened her fall. (Our Tryambakeśvara guide tells how Gautama brought her south as the Godāvarī.)</p>',
 cards=('💡 Ākāśa-gaṅgā','The "sky Gaṅgā": the Milky Way in Indian tradition.','💡 Gaṅgādhara','"Bearer of the Gaṅgā": one of Śiva\'s names.'),
 inner='What looks huge to us is a drop to Him. What looks like a drop to Him can still ring our whole world.',
 talk=('The whole Gaṅgā is a drop?','On His head, yes. That\'s the poet\'s way of making us feel His size.'),
 key='The river that rings the earth <b>is a drop in His hair</b>.'),
D(theme='A CHARIOT MADE OF THE WORLD',
 svg=svg('A chariot whose body is the earth, with sun and moon as wheels, Mount Meru as the bow and Vishnu as the arrow, aimed at three cities in the sky',
  '<path d="M30 110 h110 l-10 20 h-90z" fill="#2a9d6f" stroke="#111" stroke-width="2.5"/><circle cx="50" cy="134" r="16" fill="#ffd60a" stroke="#111" stroke-width="2.5"/><circle cx="120" cy="134" r="16" fill="#eee" stroke="#111" stroke-width="2.5"/>'
  '<path d="M90 110 q-24 -50 0 -100" fill="none" stroke="#7a5a3a" stroke-width="5"/><path d="M90 10 L90 110" stroke="#111" stroke-width="1"/><path d="M90 60 L180 40" stroke="#1d6fb8" stroke-width="3"/>'
  +''.join(f'<rect x="{x}" y="{y}" width="24" height="16" fill="#9a9a9a" stroke="#111" stroke-width="2"/>' for x,y in [(176,20),(190,44),(166,58)])
  +'<text x="50" y="158" text-anchor="middle" font-family="Bangers" font-size="9">SUN</text><text x="120" y="158" text-anchor="middle" font-family="Bangers" font-size="9">MOON</text><text x="70" y="104" text-anchor="middle" font-family="Bangers" font-size="9">EARTH</text><text x="72" y="40" font-family="Bangers" font-size="9">MERU</text><text x="186" y="88" font-family="Bangers" font-size="9">TRIPURA</text>'),
 mean='The earth was the chariot, Brahmā the charioteer, the king of mountains the bow, the sun and moon the wheels, and the bearer of the discus the arrow. For You, wanting to burn the straw of the three cities, what was all this pomp? The Lord\'s mind plays with the things at its command; it is surely not dependent on them.',
 plain='To destroy the three demon cities, the gods built Śiva a chariot: earth, sun and moon, Mount Meru, Viṣṇu as the arrow. But Śiva didn\'t need any of it; He plays with these things, He doesn\'t depend on them.',
 words=[('rathaḥ kṣoṇī','<b>the chariot was the earth</b>'),('yantā śatadhṛtiḥ','<b>the charioteer was Brahmā</b>'),('agendraḥ dhanuḥ','<b>the king of mountains (Meru) the bow</b>'),('candrārkau','the <b>moon and sun</b>'),('tripura-tṛṇa','the <b>straw of the three cities</b>'),('na paratantrāḥ','<b>not dependent</b>')],
 deep='<p><b>Tripura.</b> Three demon brothers built three flying cities, of gold, silver and iron, that could be destroyed only by a single arrow when they lined up once in a thousand years. The gods made Śiva a chariot of the whole universe. In the end, many tellings say, Śiva burnt them with a smile.</p><p><b>Straw.</b> The poet calls the cities <i>tṛṇa</i>, "straw": the great war machine of the gods was hardly needed.</p><p><b>Play.</b> <i>Vidheyaiḥ krīḍantyaḥ</i>: the Lord plays with the things that serve Him. He uses the world\'s instruments, but is never bound by them.</p>',
 cards=('💡 Tripurāntaka','"Ender of the three cities": Śiva as the archer; a famous image in temple sculpture.','💡 Inner reading','Commentators read the three cities as three bodies or three impurities, burnt by knowledge.'),
 inner='God uses means, but is not limited by them. The tools serve the purpose; they are not the power.',
 talk=('Why build a chariot He didn\'t need?','For the gods\' sake, and for the story. The verse says He was playing: the real power was His.'),
 key='The whole universe as His chariot, <b>and He needed none of it</b>.'),
D(theme='VIṢṆU\'S EYE AND THE DISCUS',
 svg=svg('Vishnu offering lotuses at Shiva\'s feet, one lotus short, offering his own lotus-eye, and receiving the Sudarshana discus',
  '<g transform="translate(160 128)">'+LINGA+'</g>'
  +''.join(f'<g transform="translate({120+12*(i%6)} {148-0*i})"><circle r="4" fill="#f08aa6" stroke="#111"/></g>' for i in range(6))
  +'<g stroke="#111" stroke-width="2.5"><circle cx="54" cy="82" r="13" fill="#4a6fb8"/><path d="M34 140 q20 -46 40 0z" fill="#ffd60a"/></g><path d="M60 80 q8 -4 14 0 q-8 6 -14 0z" fill="#fff" stroke="#111"/>'
  '<g transform="translate(60 30)"><circle r="16" fill="none" stroke="#ff8c1a" stroke-width="4"/><path d="M-16 0 h32 M0 -16 v32 M-11 -11 l22 22 M11 -11 l-22 22" stroke="#ff8c1a" stroke-width="2"/></g><text x="110" y="26" font-family="Bangers" font-size="11">SUDARŚANA</text>'),
 mean='Hari, having set an offering of a thousand lotuses at Your feet, when one was missing, plucked out his own lotus eye. That overflowing devotion took the form of the discus, which now stays awake to protect the three worlds, O destroyer of the three cities.',
 plain='Viṣṇu worshipped Śiva with a thousand lotuses. One was missing, so he offered his own lotus-eye. His devotion became the Sudarśana discus, which guards the worlds.',
 words=[('sāhasram kamala-balim','an <b>offering of a thousand lotuses</b>'),('ekone','<b>when one was short</b>'),('netra-kamalam','his <b>lotus eye</b>'),('bhakty-udrekaḥ','<b>the overflow of devotion</b>'),('cakra-vapuṣaḥ','<b>in the form of the discus</b>'),('jāgarti','<b>stays awake, keeps watch</b>')],
 deep='<p><b>The story.</b> Viṣṇu vowed to worship Śiva with a thousand lotuses. Śiva, testing him, hid one. Rather than break his vow, Viṣṇu, whose eyes are called lotuses, plucked out one eye and offered it. Śiva restored the eye and gave him the <b>Sudarśana cakra</b>.</p><p><b>A beautiful link.</b> The verse says the discus is Viṣṇu\'s devotion itself, "transformed". The weapon that protects the world is made of love.</p><p><b>Hari and Hara.</b> Here Viṣṇu is Śiva\'s greatest devotee, as elsewhere Śiva is Viṣṇu\'s. Madhusūdana Sarasvatī\'s commentary reads the whole hymn for both.</p>',
 cards=('💡 Sudarśana','"Beautiful to see": Viṣṇu\'s discus, protector of the worlds.','💡 Kamalākṣa','"Lotus-eyed": a name of Viṣṇu, which makes the offering natural.'),
 inner='What you give completely comes back as the strength to protect others.',
 talk=('Viṣṇu worshipped Śiva?','In this story, wholeheartedly, even giving his eye. Śaiva and Vaiṣṇava stories are full of each god honouring the other.'),
 key='Viṣṇu\'s devotion <b>became the discus that guards the world</b>.'),
D(theme='THE WITNESS OF EVERY RITUAL',
 svg=svg('A sacrificial fire that has gone out, with a crescent moon showing night, while a wakeful third eye watches over it and passes on the fruit',
  '<rect width="220" height="160" fill="#16264a"/><path d="M70 130 h80 l-10 20 h-60z" fill="#c9a26b" stroke="#111" stroke-width="2.5"/><path d="M96 130 q4 -10 8 0 q4 -8 8 0" fill="none" stroke="#999" stroke-width="2"/>'
  '<path d="M190 20 a12 12 0 1 0 8 18 a9 9 0 1 1 -8 -18z" fill="#fff6b0"/><path d="M80 60 q30 -24 60 0 q-30 24 -60 0z" fill="#fff" stroke="#111" stroke-width="2.5"/><circle cx="110" cy="60" r="9" fill="#1d4f9a"/>'
  '<path d="M110 76 L110 122" stroke="#ffd60a" stroke-width="2" stroke-dasharray="4 3"/><text x="110" y="100" text-anchor="middle" font-family="Bangers" font-size="10" fill="#ffd60a" dx="40">FRUIT</text><text x="110" y="40" text-anchor="middle" font-family="Bangers" font-size="10" fill="#fff">AWAKE</text>'),
 mean='When the sacrifice is asleep, over and gone, You stay awake to join the sacrificers to its fruit. For how can a rite, once it has perished, bear fruit without the worship of the Lord? So, seeing You as the guarantor who grants the fruits of sacrifices, people put their faith in the Veda and devote themselves firmly to rituals.',
 plain='A ritual ends and is gone; how can it bear fruit later? Because Śiva stays awake and delivers the fruit. Knowing that, people trust the Veda and keep up their rites.',
 words=[('kratau supte','<b>when the sacrifice sleeps</b>, has ended'),('jāgrat','<b>awake</b>'),('phala-yoga','<b>joining with the fruit</b>'),('pradhvastam karma','an action <b>that has perished</b>'),('pratibhū','a <b>surety, guarantor</b>'),('śraddhā','<b>faith</b>')],
 deep='<p><b>An old puzzle.</b> The Mīmāṃsā school said a ritual creates an unseen power, <i>apūrva</i>, that later brings its result, with no need for God. Puṣpadanta disagrees: a deed that is finished cannot by itself produce anything. Someone must remember it and give the fruit. That is the Lord.</p><p><b>The guarantor.</b> <i>Pratibhū</i>: a surety, like someone who guarantees a loan. Śiva is the guarantee that every sincere act will bear fruit.</p><p><b>Why it matters.</b> If He watches over results, then no honest effort is wasted, even if the reward comes long after.</p>',
 cards=('💡 Apūrva','Mīmāṃsā\'s "unseen potency" left by a ritual, which later yields its result.','💡 Karma-phala','The fruit of action, which the Gītā asks us to offer to the Lord.'),
 inner='Nothing done sincerely is lost. Someone is awake when your work is finished.',
 talk=('Why does a ritual need God to work?','Because when it\'s over, it\'s gone. Puṣpadanta says someone has to carry it forward. That\'s Śiva, awake while the ritual sleeps.'),
 key='The ritual ends; <b>He stays awake and gives the fruit</b>.'),
D(theme='DAKṢA\'S BROKEN SACRIFICE',
 svg=svg('A great sacrificial altar overturned, with a broken pot and scattered offerings, and Virabhadra\'s trident above',
  '<path d="M40 120 h140 l-14 24 h-112z" fill="#c9a26b" stroke="#111" stroke-width="2.5"/><path d="M90 120 q6 -30 20 -36 q14 6 20 36" fill="#ff8c1a" stroke="#111" stroke-width="2"/>'
  '<path d="M150 110 l20 -14 l12 10 l-20 16z" fill="#c0703a" stroke="#111" stroke-width="2"/><path d="M170 96 l-6 -10" stroke="#111"/>'
  '<path d="M110 10 v60" stroke="#111" stroke-width="4"/><path d="M96 24 q14 -20 28 0 M110 10 v-4" fill="none" stroke="#111" stroke-width="4"/><path d="M96 24 v-10 M124 24 v-10" stroke="#111" stroke-width="4"/>'
  '<text x="110" y="92" text-anchor="middle" font-family="Bangers" font-size="11" fill="#fff">YAJÑA</text><text x="40" y="40" font-family="Bangers" font-size="11" fill="#c0392b">NO FAITH</text>'),
 mean='Dakṣa, skilled in rites, lord of embodied beings, was the sacrificer; the sages were the priests; the hosts of gods sat in the assembly; yet, O giver of refuge, the sacrifice was ruined by You, who delight in granting the fruits of sacrifice. Surely, sacrifices done without faith turn into harm for the one who performs them.',
 plain='Dakṣa\'s great sacrifice had everything: sages as priests, gods as guests. But without faith and without honouring Śiva, it was destroyed. Ritual without faith harms the doer.',
 words=[('kriyā-dakṣaḥ','<b>skilled in rites</b>'),('kratupatiḥ','the <b>lord of the sacrifice</b>, its patron'),('ārtvijyam','the <b>office of priest</b>'),('sadasyāḥ','<b>members of the assembly</b>'),('śaraṇada','<b>giver of refuge</b>'),('abhicāra','<b>harm</b>, a rite that rebounds')],
 deep='<p><b>Dakṣa\'s yajña.</b> Dakṣa, father of Satī, held a great sacrifice and pointedly left out his son-in-law Śiva. Satī went anyway, was insulted, and gave up her life in the sacrificial fire. Śiva\'s fury, as <b>Vīrabhadra</b>, destroyed the sacrifice.</p><p><b>Skilled but faithless.</b> The verse plays on the name: <i>kriyā-dakṣo dakṣaḥ</i>, "Dakṣa, dakṣa (skilled) in rites". Skill was not the problem; pride and lack of faith were.</p><p><b>Śakti Pīṭhas.</b> In many tellings, Śiva carried Satī\'s body across the world, and where its parts fell, the Śakti Pīṭhas arose.</p>',
 cards=('💡 Satī','Dakṣa\'s daughter and Śiva\'s first wife, later reborn as Pārvatī.','💡 Vīrabhadra','The fierce form born of Śiva\'s anger to destroy the sacrifice.'),
 inner='Perfect technique without humility is empty. What is offered without love does not reach.',
 talk=('Dakṣa did everything right, ritually.','Every detail, says the hymn: sages, gods, rules. Only the heart was missing. And that turned his sacrifice against him.'),
 key='All the right rituals, <b>no faith: the sacrifice fell</b>.'),
D(theme='THE HUNTER IN THE NIGHT SKY',
 svg=svg('The night sky with the deer constellation of Orion and an arrow, and the bright star Sirius as the hunter chasing it',
  '<rect width="220" height="160" fill="#0b1630"/>'+''.join(STAR(x,y,r) for x,y,r in [(120,40,3),(150,44,3),(126,72,2),(135,74,2),(144,76,2),(118,110,3),(154,108,3),(30,140,6),(70,20,1.5),(190,130,1.5),(200,20,1.5),(40,60,1.5)])
  +'<path d="M126 72 L144 76" stroke="#ffd60a" stroke-width="1"/><path d="M40 136 L120 80" stroke="#ff8c1a" stroke-width="2" stroke-dasharray="5 3"/>'
  '<text x="136" y="132" text-anchor="middle" font-family="Bangers" font-size="10" fill="#fff">THE DEER (MṚGAŚIRA)</text><text x="30" y="124" text-anchor="middle" font-family="Bangers" font-size="10" fill="#fff">THE HUNTER</text>'),
 mean='O Lord, when Prajāpati, the lord of creatures, overcome by desire, took the form of a stag and went after his own daughter, who had become a doe, Your arrow pierced him. He fled even to the sky, feathered with the arrow; and still today, as he trembles, the fury of You, the deer-hunter, does not let him go.',
 plain='When Brahmā, as a stag, chased his own daughter with wrong desire, Śiva shot him with an arrow. Brahmā fled to the sky, and there, as stars, the hunter still chases the deer.',
 words=[('prajānātha','the <b>lord of creatures</b>: Prajāpati, Brahmā'),('prasabham','<b>by force</b>, violently'),('rohit','a <b>red doe</b>'),('ṛśya','a <b>stag</b>'),('sapatrākṛtam','<b>pierced with a feathered arrow</b>'),('mṛga-vyādha','the <b>deer-hunter</b>')],
 deep='<p><b>An old Vedic story.</b> The Brāhmaṇas tell that Prajāpati desired his own daughter Uṣas, the dawn, and Rudra punished him with an arrow. The hymn retells it: Śiva upholds what is right even against the creator.</p><p><b>Written in the stars.</b> Tradition reads the story in the sky: the deer\'s head is the star group <b>Mṛgaśiras</b> (part of Orion); the hunter, <b>Mṛgavyādha</b>, is the bright star we call Sirius; the arrow lies between. "Still today", says the poet: look up on a winter night.</p><p><b>No one is above dharma.</b> Not even the creator escapes Rudra\'s justice.</p>',
 cards=('💡 Mṛgaśiras','"The deer\'s head": a nakṣatra (lunar mansion) in the constellation Orion.','💡 Mṛgavyādha','"The deer-hunter": the traditional Indian name for Sirius.'),
 inner='Dharma applies to everyone, even the most powerful. And its memory lasts as long as the stars.',
 talk=('A story about stars?','A story put in the stars. Ancient watchers saw a deer, an arrow and a hunter in the winter sky, and remembered this tale.'),
 key='Even the creator <b>is not above Rudra\'s justice</b>.'),
]
