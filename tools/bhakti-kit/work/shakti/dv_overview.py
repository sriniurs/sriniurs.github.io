exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Daśāvatāra · The Ten Avatāras of Viṣṇu · srini.presents',
 'Daśāvatāra, the ten avatāras of Viṣṇu: Matsya, Kūrma, Varāha, Narasiṃha, Vāmana, Paraśurāma, Rāma, Balarāma or Buddha, Kṛṣṇa and Kalki. What an avatāra is, the Gītā’s promise, the different lists, the Vedic roots, the yugas, the evolution reading, the avatāras in art and temples, and Jayadeva’s Gītagovinda. An illustrated reference guide.')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Vishnu at the centre with ten small medallions around him for his ten avatars">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/>'+STAR+VISHNU(190,170,1.15)
 +''.join(f'<circle cx="{190+150*__import__("math").cos(-2.9+i*0.645):.0f}" cy="{150+105*__import__("math").sin(-2.9+i*0.645):.0f}" r="22" fill="#fff8e7" stroke="#111" stroke-width="2"/>'+AV(i+1,round(190+150*__import__("math").cos(-2.9+i*0.645)),round(150+105*__import__("math").sin(-2.9+i*0.645)),.42) for i in range(10))+'</svg>')
cov=cover_dv('TEN DESCENTS OF VIṢṆU','DAŚĀVATĀRA',15,'Fish to horseman: the ten avatāras',art)
fw=foreword_dv('Jaya Jagadīśa Hare,',[
 'Whenever the world loses its balance, says the Bhagavad Gītā, the Lord comes down to set it right. Those “descents” are the <b>avatāras</b>, and ten of them have been sung, painted and carved for over fifteen centuries: the <b>Daśāvatāra</b>.',
 'A fish that saves the seeds of life from the flood. A tortoise that carries a mountain. A boar who lifts the Earth. A man-lion who keeps a promise to a child. A dwarf who spans the universe in three steps. Then three Rāmas, the dark cowherd Kṛṣṇa, and a rider still to come.',
 'This guide explains what an avatāra is, why the lists differ, where the stories come from and how they are worshipped. Ten detailed guides follow, one for each avatāra.'],
 'Why does God need to come down?','The Gītā’s answer: to protect the good, end the wicked and restore dharma. Again and again.',
 series_note_dv(0).replace(' Next: <a href="'+DVS+'kurma/">Kūrma</a>.',' Next: <a href="'+DVS+'matsya/">Matsya</a>.'))
pages=[]
pages.append(page('glance','AT A GLANCE','The ten on one page','<table class="ct fact"><tr><td><b>#</b></td><td><b>Avatāra · form · deed</b></td></tr>'+''.join(
 f'<tr><td><svg width="50" height="50" viewBox="-28 -30 56 60">{AV(n,0,0,.55)}</svg></td><td><b>{n}. <a href="{DVS}{s}/">{nm}</a></b>, {f}: {d}</td></tr>' for n,nm,s,f,y,d in DV)+'</table>'))
pages.append(page('avatara','WHAT IS AN AVATĀRA?','The one who comes down',facts([
 ('Word','<i>ava</i> “down” + <i>tṛ</i> “to cross”: a descent, a crossing over'),
 ('Who','Above all Viṣṇu, the preserver, who keeps the world in order'),
 ('Why','To protect the good, remove evil and re-establish dharma'),
 ('How','By taking a form suited to the danger: fish for a flood, boar for the sunken Earth, man-lion for a riddle'),
 ('Not lesser','In the tradition each avatāra is fully God, not a part')])
 +'<div class="panel reading"><p><i>paritrāṇāya sādhūnāṃ vināśāya ca duṣkṛtām, dharma-saṃsthāpanārthāya sambhavāmi yuge yuge</i></p><p class="small">“To protect the good, to destroy the wicked, to establish dharma, I come into being age after age.” Bhagavad Gītā 4.8</p></div>'))
pages.append(page('lists','WHICH TEN?','The lists differ',facts([
 ('Shared core','Almost all lists agree on the first seven: Matsya, Kūrma, Varāha, Narasiṃha, Vāmana, Paraśurāma, Rāma, and on Kalki last'),
 ('Common list','Eighth Kṛṣṇa, ninth Buddha: found in several Purāṇas and in North Indian tradition'),
 ('South Indian','Śrī Vaiṣṇava and Smārta lists give Balarāma eighth and Kṛṣṇa ninth, without the Buddha'),
 ('Jayadeva','The Gītagovinda (12th c.) names Balarāma and Buddha, for Kṛṣṇa is the source of all'),
 ('Regional','Some lists place Jagannātha or Viṭhobā in the ninth place'),
 ('This series','Article 8 covers Balarāma and the Buddha together; Kṛṣṇa is article 9')])
 +talk("So which list is right?","Each tradition is right for itself. We show all of them and let you see why they differ.")))
pages.append(page('bhagavata','MORE THAN TEN','The Bhāgavata’s longer lists',facts([
 ('22 or more','The Bhāgavata Purāṇa (1.3) lists over twenty avatāras, including the Kumāras, Nārada, Kapila, Dattātreya, Ṛṣabha, Pṛthu, Dhanvantari, Mohinī and Vyāsa'),
 ('Innumerable','It adds that the avatāras are as countless as streams from an endless lake: <i>avatārā hy asaṅkhyeyāḥ</i>'),
 ('Kṛṣṇa','It ends with the famous line that Kṛṣṇa is the Lord himself: <i>kṛṣṇas tu bhagavān svayam</i>'),
 ('Pāñcarātra','Some Pāñcarātra texts count 39'),
 ('Why ten?','Ten became the classic set in poetry, temple art and festivals')])))
pages.append(page('vedic','OLDER THAN THE PURĀṆAS','Vedic roots',facts([
 ('Fish','The Śatapatha Brāhmaṇa (1.8.1) tells of Manu, a fish and the flood'),
 ('Tortoise','Prajāpati takes the form of a tortoise (kūrma) in the Śatapatha Brāhmaṇa'),
 ('Boar','In the Taittirīya texts Prajāpati as a boar raises the earth from the waters'),
 ('Three steps','The Ṛgveda (1.154) praises Viṣṇu for measuring the worlds in three strides, the seed of the Vāmana story'),
 ('Later','In the Purāṇas these deeds are given to Viṣṇu and arranged in order')])
 +talk("The fish story is older than Viṣṇu's role in it?","The Brāhmaṇa tells the flood without naming Viṣṇu. The Purāṇas made it his.")))
pages.append(page('yugas','THROUGH THE FOUR AGES','The avatāras in time',fig(560,170,'Four bands for the four ages with avatar icons placed in each',
 '<rect width="560" height="170" fill="#eef3fa"/>'+''.join(f'<rect x="{10+i*137}" y="20" width="130" height="130" fill="{c}" stroke="#111" stroke-width="2"/>'+T(75+i*137,40,y,13) for i,(y,c) in enumerate((('Satya','#fff3c0'),('Tretā','#dff0d8'),('Dvāpara','#dcecff'),('Kali','#e8e0f0'))))
 +''.join(AV(n,x,y,.42) for n,x,y in ((1,45,80),(2,105,80),(3,45,125),(4,105,125),(5,180,80),(6,240,80),(7,210,125),(8,320,95),(9,380,95),(10,490,95))))+facts([
 ('Satya Yuga','Matsya, Kūrma, Varāha, Narasiṃha'),
 ('Tretā Yuga','Vāmana, Paraśurāma, Rāma'),
 ('Dvāpara Yuga','Balarāma, Kṛṣṇa'),
 ('Kali Yuga','The Buddha (in lists that include him), and Kalki at its end'),
 ('Our age','Tradition says the Kali Yuga began when Kṛṣṇa left the world')])))
pages.append(page('evolution','AN EVOLUTION STORY?','A modern reading',facts([
 ('The idea','Fish (water), tortoise (water and land), boar (land), man-lion (half animal), dwarf (small man), then full humans with axe, bow and plough'),
 ('Who says it','A 19th–20th-century reading, popularised by writers comparing the list with Darwin'),
 ('Not scriptural','No Purāṇa presents the avatāras as evolution; the order follows the yugas and the stories'),
 ('Our view','An interesting pattern people notice, not a claim of the texts')])
 +talk("So did the sages know about evolution?","The pattern is striking, but the texts don't say so. Enjoy it as a reading, not a proof.")))
pages.append(page('gitagovinda','JAYADEVA’S DAŚĀVATĀRA','Gītagovinda, 12th century',facts([
 ('Poet','Jayadeva of Odisha and Bengal, 12th century'),
 ('Hymn','The opening song of the Gītagovinda praises all ten, each verse ending <i>keśava dhṛta … śarīra, jaya jagadīśa hare</i>'),
 ('Example','<i>pralaya-payodhi-jale dhṛtavān asi vedam</i>: “in the waters of dissolution you held the Veda” (Matsya)'),
 ('His list','Balarāma eighth and Buddha ninth; Kṛṣṇa is the Lord who takes all ten'),
 ('Sung','In Odissi dance, at Purī, and across India today')])
 +'<div class="key">See also: <a href="/bhakti/vishnu/">More hymns to Viṣṇu</a></div>'))
pages.append(page('art','IN STONE AND PAINT','The avatāras in art',facts([
 ('Udayagiri','Cave 5 near Vidiśā, Madhya Pradesh: a colossal Varāha relief of the Gupta age, early 5th century'),
 ('Deogarh','The Daśāvatāra temple at Deogarh, Uttar Pradesh, about 500 CE, one of the oldest stone temples of north India'),
 ('Bādāmi','Cave 3 in Karnataka (578 CE): Varāha, Narasiṃha and Trivikrama'),
 ('Gopurams','Rows of the ten crown many South Indian temple towers, as at Uḍupi'),
 ('Paintings','Ten-panel sets in Rajasthani, Pahāṛī and Kerala mural styles; the Gañjifā cards of Odisha and Sawantwadi')])))
pages.append(page('temples','WHERE THEY ARE WORSHIPPED','Temples of the ten',facts([
 ('Matsya','Vedanārāyaṇa, Nāgalāpuram (Andhra)'),('Kūrma','Kūrmanātha, Śrīkūrmam (Andhra)'),('Varāha','Bhū Varāha, Śrīmuṣṇam (Tamil Nadu); Tirumala'),
 ('Narasiṃha','Ahobilam, Siṃhācalam, Yādagiri'),('Vāmana','Tṛkkākara (Kerala), heart of Onam'),('Paraśurāma','Kerala and Konkan traditions'),
 ('Rāma','Ayodhyā, Bhadrācalam, Rāmeśvaram'),('Balarāma','Purī, as Balabhadra'),('Kṛṣṇa','Mathurā, Vṛndāvana, Dvārakā, Guruvāyūr, Uḍupi, Purī'),('Kalki','Shrines in Jaipur and elsewhere; Sambhal (UP) is his foretold birthplace')])
 +'<div class="key">See: <a href="'+TI+'ahobilam/">Ahobilam</a> · <a href="'+TI+'char-dham/">Char Dham</a></div>'))
pages.append(page('thrikkakara','ALL TEN IN ONE TEMPLE','Onam at Tṛkkākara',facts([
 ('Where','The Vāmanamūrti temple at Tṛkkākara, near Kochi, Kerala'),
 ('Ten days','During the Onam festival the deity is dressed each day as one of the avatāras'),
 ('The set','Matsya, Kūrma, Varāha, Narasiṃha, Vāmana, Paraśurāma, Rāma, Balarāma, Kṛṣṇa and Kalki, with Trivikrama'),
 ('Why here','Tradition says this was Mahābali’s capital, where Vāmana came')])
 +'<div class="key">Read: <a href="'+DVS+'vamana/">Vāmana</a></div>'))
pages.append(page('mahavidya','THE TEN AND THE TEN','Avatāras and Mahāvidyās',facts([
 ('The idea','Some Tantras pair each avatāra with one of the ten Mahāvidyās, the Goddess’s ten forms'),
 ('Examples','Kṛṣṇa with Kālī, Rāma with Tārā, Narasiṃha with Chinnamastā in one list'),
 ('Lists vary','The Guhyātiguhya and Muṇḍamālā Tantras do not agree on every pair'),
 ('Meaning','The Goddess is the power behind each of Viṣṇu’s descents')])
 +'<div class="key">Read: <a href="/bhakti/devi/dasha-mahavidya/">Daśa Mahāvidyā</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','Their birthdays',facts([
 ('Matsya Jayantī','Caitra (Mar–Apr)'),('Kūrma Jayantī','Vaiśākha full moon'),('Varāha Jayantī','Bhādrapada'),('Narasiṃha Jayantī','Vaiśākha (Apr–May)'),('Vāmana Jayantī','Bhādrapada; Onam in Kerala'),
 ('Paraśurāma Jayantī','Akṣaya Tṛtīyā'),('Rāma Navamī','Caitra'),('Balarāma Jayantī','Śrāvaṇa'),('Kṛṣṇa Janmāṣṭamī','Śrāvaṇa or Bhādrapada'),('Kalki Jayantī','Śrāvaṇa, by some calendars')])))
pages.append(page('meaning','WHAT THEY TEACH','The wisdom of the ten',facts([
 ('God takes our side','Whatever the danger, a form comes to meet it'),
 ('Every shape is holy','Fish, tortoise, boar: God is not ashamed of any body'),
 ('Promises kept','To Manu, Prahlāda and Bali, he keeps his word'),
 ('Hope','The tenth is still to come: no age is forever dark')])
 +talk("Why should I care about a fish and a tortoise?","Because they say God will become whatever is needed to save what matters. That includes you.")))
pages.append(page('series','THE TEN GUIDES','Read on','<div class="steps">'+''.join(f'<div><b>{n}. <a href="{DVS}{s}/">{nm}</a></b>, {f}: {d}.</div>' for n,nm,s,f,y,d in DV)+'</div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Avatāra','Descent'),('Daśa','Ten'),('Dharma','Right order'),('Yuga','Age of the world'),('Brāhmaṇa','Vedic ritual commentary'),('Purāṇa','Ancient story-text'),('Trivikrama','“Of the three steps”'),('Jayantī','Birthday festival')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Idea.</b> Viṣṇu comes down whenever dharma fails: Gītā 4.7–8.</div>
<div><b>The ten.</b> Matsya, Kūrma, Varāha, Narasiṃha, Vāmana, Paraśurāma, Rāma, Balarāma or Buddha, Kṛṣṇa, Kalki.</div>
<div><b>Lists.</b> The eighth and ninth places differ by region and sect.</div>
<div><b>Roots.</b> Vedic fish, tortoise, boar and three steps; Purāṇic order; Jayadeva’s hymn.</div>
<div><b>Lesson.</b> God takes whatever form the moment needs.</div>
</div>'''+talk("One line to remember?","Fish to horseman, he keeps coming back. Yuge yuge.")+'<div class="key">Start with the first: <a href="'+DVS+'matsya/">Matsya, the fish</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Bhagavad Gītā 4.7–8; Bhāgavata Purāṇa 1.3 (lists; <i>avatārā hy asaṅkhyeyāḥ</i>; <i>kṛṣṇas tu bhagavān svayam</i>); Śatapatha Brāhmaṇa 1.8.1 (flood); Ṛgveda 1.154 (three strides); Jayadeva, Gītagovinda 1.</p>
<p><b>Lists:</b> Wikipedia, “Dashavatara” (common list with Kṛṣṇa and Buddha in several Purāṇas; Śrī Vaiṣṇava list with Balarāma and Kṛṣṇa; Gauḍīya list with Balarāma and Buddha; Jagannātha and Viṭhobā variants); Encyclopaedia Britannica, “Dashavatara”.</p>
<p><b>Art and temples:</b> Wikipedia, “Udayagiri Caves” (Cave 5 Varāha; 401 CE inscription of Chandragupta II); “Kurmanathaswamy temple, Srikurmam”; “Vedanarayana Temple, Nagalapuram”; “Thrikkakara Temple” (avatāra decorations at Onam). Deogarh and Bādāmi from standard art histories.</p>
<p><b>Sources differ / unverified:</b> Jayantī months vary by calendar; Mahāvidyā pairings vary between Tantras; the evolution reading is modern. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('avatara','What Is an Avatāra?'),('lists','Which Ten?'),('bhagavata','More Than Ten'),('vedic','Vedic Roots'),('yugas','Through the Four Ages'),('evolution','An Evolution Story?'),('gitagovinda','Jayadeva’s Daśāvatāra'),
 ('art','In Stone and Paint'),('temples','Temples of the Ten'),('thrikkakara','All Ten in One Temple'),('mahavidya','Avatāras and Mahāvidyās'),('festivals','Through the Year'),('meaning','What They Teach'),('series','The Ten Guides'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV0_Dashavatara.html',head,cov,fw,pages,toc)
