exec(open('/home/claude/work/shakti/hn_common.py').read())
GLOW=lambda x,y,r,c,o: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{o}"/>'
GATE=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-50 0 v-80 q50 -50 100 0 v80z" fill="#e0a800"/><path d="M-34 0 v-70 q34 -36 68 0 v70z" fill="#fff8d0"/><path d="M0 0 v-104" stroke="#e0a800" stroke-width="0"/>'+''.join(f'<circle cx="{-42+i*12}" cy="-88" r="3" fill="#c0392b"/>' for i in range(8))+'</g>'
VISHNU=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-20 40 q-4 -46 20 -52 q24 6 20 52z" fill="#ffd60a"/><circle cy="-22" r="14" fill="#4a7fd0"/><path d="M-12 -36 h24 l-4 -18 h-16z" fill="#e0a800"/><circle cx="-30" cy="-6" r="8" fill="none" stroke="#e0a800" stroke-width="4"/><path d="M28 -14 q-6 10 4 14 q8 -6 -4 -14" fill="#fff8e7"/><path d="M-20 0 l-10 -6 M20 0 l10 -6" stroke="#4a7fd0" stroke-width="6"/></g>'
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A golden gate opening at dawn, Vishnu shining within, devotees waiting">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+GLOW(190,160,110,'#ffd60a',.25)+GATE(190,240,1.6)+VISHNU(190,180,1.1)+''.join(person(40+i*30,262,c,'#c98b5a',.5) for i,c in enumerate(['#e05a8a','#4a7fd0','#2a9d6f']))+''.join(person(270+i*30,262,c,'#c98b5a',.5) for i,c in enumerate(['#ffd60a','#c0392b','#5a3a8a']))+'</svg>')
P_=P
pages=[
P_('glance','AT A GLANCE','The day on one page',[
 ('Date','<b>Sunday 20 December 2026</b> (Mārgaśīrṣa Śukla Ekādaśī; confirm in your local pañcāṅga)'),
 ('Names','Vaikuṇṭha Ekādaśī; Mukkoṭi Ekādaśī (Telugu, Kannada); Svargavāsal Ekādaśī (Tamil, Kerala); Mokṣadā Ekādaśī (North)'),
 ('Same day','Gītā Jayantī: the day the Gītā was spoken'),
 ('Main rite','Darśan through the northern gate, the Vaikuṇṭha dvāra'),
 ('Vow','Fasting, night vigil, and breaking the fast on Dvādaśī morning'),
 ('Great centres','Srirangam, Tirumala, Bhadrācalam and every Viṣṇu temple')],
 ("Why is this Ekādaśī so special?","Of 24 Ekādaśīs in a year, this is the one when Vaikuṇṭha's gate is opened.")),
P_('ekadashi','WHAT IS EKĀDAŚĪ?','The eleventh day',[
 ('Tithi','The eleventh lunar day of each fortnight: two a month, about 24 a year'),
 ('Viṣṇu’s day','Each Ekādaśī is sacred to Viṣṇu, with its own name and story'),
 ('Fast','Grains, especially rice, are avoided; many fast fully'),
 ('The goddess','The Padma Purāṇa tells of a goddess born from Viṣṇu who killed the demon Mura: Viṣṇu named her Ekādaśī'),
 ('Pāraṇa','The fast is broken on Dvādaśī, the twelfth day, within a set window')],
 ("A goddess called Ekādaśī?","Born from Viṣṇu's body while he slept. She saved him, and he made her day holy.")),
P_('margashirsha','THE BEST OF MONTHS','Mārgaśīrṣa and Mārgaḻi',[
 ('Gītā 10.35','Kṛṣṇa says: of months, I am Mārgaśīrṣa'),
 ('Dhanur māsa','In the solar calendar this is Dhanus, Mārgaḻi in Tamil, the month of dawn worship'),
 ('The gods’ dawn','Tradition: the six months of the sun’s southward journey are the gods’ night; Mārgaḻi is their dawn'),
 ('Two calendars','Vaikuṇṭha Ekādaśī is set by the Mārgaḻi month in the Tamil tradition, and by lunar Mārgaśīrṣa elsewhere; usually the same day')],
 extra='<div class="verse"><p><i>bṛhatsāma tathā sāmnāṃ gāyatrī chandasām aham<br>māsānāṃ mārgaśīrṣo ’ham ṛtūnāṃ kusumākaraḥ</i></p><p class="small">Of chants I am the Bṛhat Sāman, of metres the Gāyatrī; of months I am Mārgaśīrṣa, of seasons the flowering spring. (Gītā 10.35)</p></div>'),
P_('gate','THE NORTHERN GATE','Vaikuṇṭha dvāra',[
 ('What','A gate on the north side of the temple, kept shut all year'),
 ('Opened','Before dawn on Vaikuṇṭha Ekādaśī'),
 ('Meaning','Passing through it is passing through the gate of Vaikuṇṭha, Viṣṇu’s heaven'),
 ('Names','Paramapada vāsal (Srirangam), Svargavāsal, Vaikuṇṭha dvāram (Tirumala)'),
 ('Crowds','Devotees queue through the night for this one passage')],
 ("Walking through a door gets you to heaven?","It's a picture of what the day means: the gate of liberation opens."),
 figure=fig(560,140,'Devotees walking through an arched golden gate before dawn','<rect width="560" height="140" fill="#1b2f5a"/>'+GATE(280,138,1.2)+''.join(person(120+i*34,136,c,'#c98b5a',.55) for i,c in enumerate(['#e05a8a','#4a7fd0','#2a9d6f','#ffd60a']))+''.join(person(330+i*34,136,c,'#c98b5a',.55) for i,c in enumerate(['#c0392b','#5a3a8a','#ff9f1c','#2a9d6f'])))),
P_('story','WHY THE GATE OPENS','The story told in temples',[
 ('Madhu and Kaiṭabha','A popular South Indian telling: two asuras, defeated by Viṣṇu, asked that whoever saw him through a gate on this day reach Vaikuṇṭha'),
 ('Granted','Viṣṇu agreed; so the northern gate opens on this day'),
 ('Mukkoṭi','Another name: the “three crore” gods come to Vaikuṇṭha to see Viṣṇu on this day'),
 ('Source','These are temple and regional traditions; Purāṇic support is indirect')]),
P_('srirangam','SRIRANGAM','The greatest celebration',[
 ('Twenty-one days','The Adhyayana Utsavam: ten days of Pagal Pattu (day) and ten of Rāppattu (night), around the Ekādaśī'),
 ('Hymns','The 4,000 verses of the Āḻvārs (Divya Prabandham) are recited before Raṅganātha'),
 ('Mohinī','On the day before, Namperumāḷ (the festival image) appears as Mohinī'),
 ('The gate','Before dawn on the Ekādaśī, Raṅganātha passes through the Paramapada Vāsal, and devotees follow'),
 ('Nammāḻvār’s mokṣa','On the last day, the poet-saint Nammāḻvār’s liberation is enacted')],
 ("Twenty-one days for one day?","The day is the peak. The festival is the mountain."),
 extra=f'<div class="key">See: <a href="/bhakti/temples-of-india/triranga/">Triraṅga: Srirangam</a></div>'),
P_('araiyar','THE ARAIYAR','Dance and song for the Lord',[
 ('Araiyar sevai','A hereditary art of singing and enacting the Āḻvārs’ hymns before the deity'),
 ('Where','Srirangam, Śrīvilliputtūr and Āḻvār Tirunagari'),
 ('When','During the Adhyayana Utsavam'),
 ('Nāthamuni','Tradition credits the 10th-century ācārya Nāthamuni with collecting the hymns and starting the festival')]),
P_('tirumala','TIRUMALA','The Vaikuṇṭha Dvāram',[
 ('The passage','A passage around the sanctum, normally shut, opened for darśan'),
 ('Ten days','TTD now keeps it open for ten days from Vaikuṇṭha Ekādaśī, so more pilgrims can pass through'),
 ('Dvādaśī','On the next day, the Sudarśana Cakra is bathed in the Svāmi Puṣkariṇī tank'),
 ('Mukkoṭi','The Telugu name of the day'),
 ('Bhadrācalam','Sītā Rāmacandra Svāmī’s gate opening is the other great Telugu event')]),
P_('karnataka','IN KARNATAKA','Mukkoṭi Ekādaśī',[
 ('Gates','Many Veṅkaṭeśvara and Viṣṇu temples set up a decorated northern gate for the day'),
 ('Bengaluru','Long queues at Vaikuṇṭha-dvāra temples across the city'),
 ('Dhanurmāsa','Viṣṇu temples hold dawn pūjās all month, with pongal (huggi) as prasāda'),
 ('Homes','Fasting, Viṣṇu Sahasranāma, Gītā reading and night bhajans')],
 extra='<div class="key">Chant: <a href="/bhakti/vishnu/vishnu-sahasranama/">Viṣṇu Sahasranāma</a></div>'),
P_('mokshada','MOKṢADĀ EKĀDAŚĪ','The northern story',[
 ('Name','“The Ekādaśī that gives liberation”'),
 ('King Vaikhānasa','A king dreamt his father suffered in hell; a sage told him to keep this Ekādaśī and give its merit to his father'),
 ('Result','His father was freed'),
 ('Meaning','The fast can help not only oneself but one’s ancestors'),
 ('Source','Told in the Ekādaśī māhātmyas ascribed to the Brahmāṇḍa and Padma Purāṇas')]),
P_('gitajayanti','GĪTĀ JAYANTĪ','The Gītā’s birthday',[
 ('Tradition','Mārgaśīrṣa Śukla Ekādaśī is held to be the day Kṛṣṇa spoke the Gītā at Kurukṣetra'),
 ('Same day','So Gītā Jayantī falls with Vaikuṇṭha Ekādaśī'),
 ('Kurukṣetra','A large Gītā Mahotsav is held there each year'),
 ('Practice','Read the whole Gītā, or at least a chapter: many read Chapter 12 or 15'),
 ('Gītā 18.68','Kṛṣṇa says whoever teaches this to devotees is dearest to him')],
 ("Read 700 verses in one day?","Many do. Or read one chapter well. Our 18 chapters are online."),
 extra=f'<div class="key">Read: <a href="/bhakti/vishnu/bhagavad-gita/">Bhagavad Gītā, all 18 chapters</a> · <a href="/bhakti/vishnu/bhagavad-gita/chapter-12/">Ch 12, Bhakti</a> · <a href="/bhakti/vishnu/bhagavad-gita/chapter-15/">Ch 15</a></div>'),
P_('fast','HOW THE FAST IS KEPT','Levels of the vow',[
 ('Nirjala','No food or water, from sunrise to the next sunrise'),
 ('Phalāhāra','Fruit, milk and nuts only'),
 ('Ekabhukta','One meal without grains'),
 ('No grains','Rice and other grains, and often beans, are avoided by all'),
 ('Health','Children, the elderly, the sick, and pregnant women are traditionally excused; a light fast is fine')],
 ("Can diabetics fast?","Not without their doctor's advice. Tradition excuses the sick. Devotion matters more than hunger.")),
P_('rice','WHY NO RICE?','A belief and a reason',[
 ('Belief','A popular saying: on Ekādaśī, sin itself takes refuge in grains'),
 ('Medha','A story: the sage Medhas’s body became rice and barley, which are thus treated as living on this day'),
 ('Practical','A day of light eating rests the body; old texts saw fasting as cleansing'),
 ('Substitutes','Sābudāna, potato, rājgirā, fruits and milk')]),
P_('vigil','THE NIGHT VIGIL','Jāgaraṇa',[
 ('Stay awake','Many stay awake through the night of Ekādaśī'),
 ('How','Bhajans, the Viṣṇu Sahasranāma, Gītā reading, Divya Prabandham, stories'),
 ('Paramapada sopānam','In Tamil homes, the snakes-and-ladders board game of “steps to Vaikuṇṭha” is played to stay awake'),
 ('Gate at dawn','Vigil ends with the gate’s opening or dawn darśan')],
 ("Snakes and ladders?","An old Indian game. Ladders are virtues, snakes are vices. The last square is Vaikuṇṭha.")),
P_('parana','BREAKING THE FAST','Pāraṇa on Dvādaśī',[
 ('When','On the morning of Dvādaśī, Monday 21 December 2026, within the window in your pañcāṅga'),
 ('How','With tulasī water, then a simple sāttvika meal'),
 ('Feed first','Many first feed a guest or the needy'),
 ('Don’t miss it','The window matters: breaking too late is said to spoil the vow')]),
P_('ambarisha','KING AMBARĪṢA','A Dvādaśī story',[
 ('The king','A great devotee who kept Ekādaśī all his life'),
 ('Durvāsā','The sage came as a guest on Dvādaśī, then went to bathe and was late'),
 ('Dilemma','The pāraṇa window was passing; the king sipped water to keep the vow without eating before his guest'),
 ('Wrath','Durvāsā raged and sent a demon; Viṣṇu’s discus Sudarśana destroyed it and chased the sage through the worlds'),
 ('Lesson','Viṣṇu told Durvāsā to seek the king’s forgiveness: the devotee’s humility protects him'),
 ('Source','Bhāgavata Purāṇa, Book 9')]),
P_('andal','ĀṆḌĀḶ’S TIRUPPĀVAI','Mārgaḻi mornings',[
 ('Āṇḍāḷ','The woman Āḻvār of Śrīvilliputtūr'),
 ('Tiruppāvai','Thirty Tamil verses, one for each morning of Mārgaḻi'),
 ('Sung','At dawn in Viṣṇu temples and homes all month, including Tirumala, where it replaces the Suprabhātam'),
 ('Opening','“mārgaḻi tiṅgaḷ”: “in the month of Mārgaḻi, on this fine full-moon day”')],
 extra='<div class="key">See: <a href="/bhakti/vishnu/venkatesa-suprabhatam/">Veṅkaṭeśa Suprabhātam</a></div>'),
P_('meaning','WHAT THE DAY TEACHES','Gates, hunger and the Gītā',[
 ('Gate','Liberation is a door: it can be opened'),
 ('Fast','Hunger for a day reminds us what we really need'),
 ('Vigil','Stay awake to what matters'),
 ('Gītā','The same day the Lord gave the Gītā'),
 ('Ambarīṣa','Humility protects better than power')]),
P_('glossary','GLOSSARY','Words used in this guide',[
 ('Ekādaśī','The eleventh lunar day'),('Dvādaśī','The twelfth day'),('Pāraṇa','Breaking the fast'),('Vaikuṇṭha','Viṣṇu’s heaven'),('Dvāra · Vāsal','Gate'),('Paramapada','The supreme abode'),('Jāgaraṇa','Night vigil'),('Mukkoṭi','Three crore (the gods)'),('Āḻvār','Tamil Vaiṣṇava poet-saint'),('Adhyayana','Study, recitation')]),
page('end','ON ONE PAGE','The day in six lines','<div class="steps"><div><b>When.</b> Sunday 20 December 2026; pāraṇa on Monday 21 December.</div><div><b>Names.</b> Vaikuṇṭha, Mukkoṭi, Svargavāsal, Mokṣadā Ekādaśī; also Gītā Jayantī.</div><div><b>Gate.</b> The northern gate opens at dawn: Srirangam, Tirumala, Bhadrācalam and everywhere.</div><div><b>Vow.</b> Fast without grains, keep vigil, break the fast in time.</div><div><b>Read.</b> The Gītā, the Sahasranāma, the Tiruppāvai.</div><div><b>Lesson.</b> The door to the highest is open; walk through it humbly.</div></div>'+talk("One line?","Once a year the gate of Vaikuṇṭha stands open. Be there.")+FOLLOW),
page('sources','SOURCES &amp; NOTES','Where the facts come from','<div class="panel reading small"><p><b>Sources:</b> Bhagavad Gītā 10.35, 18.68; Bhāgavata Purāṇa, Book 9 (Ambarīṣa); Padma Purāṇa Ekādaśī māhātmya (Mura and the goddess Ekādaśī; Mokṣadā story); Srirangam temple tradition (Adhyayana Utsavam, Paramapada Vāsal, Nammāḻvār Mokṣam); TTD on the ten-day Vaikuṇṭha Dvāra darśan; 2026 date from almanac-based festival sites (20 December 2026, with Gītā Jayantī and Mokṣadā Ekādaśī the same day).</p><p><b>Sources differ / unverified:</b> one or two sites give 19 or 30 December 2026: follow your local pañcāṅga and temple; the Madhu–Kaiṭabha and Mukkoṭi explanations are temple traditions; the Medhas–grain story and the reasons for avoiding grains vary. Health advice here is general: consult your doctor before fasting. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p></div>'),
]
EX={'glance':['Vaikuṇṭha Ekādaśī is the biggest single day in the Viṣṇu temple year in South India. Millions queue before dawn at Tirumala, Srirangam and smaller temples to walk through a gate that is opened only now.','In 2026 it coincides with Mokṣadā Ekādaśī of the northern calendar and with Gītā Jayantī, so the whole country marks the same day in different ways: fasting, darśan through the gate, and reading the Gītā.'],
 'ekadashi':['Ekādaśī is the most widely kept fast in Vaiṣṇava tradition. Each of the year’s Ekādaśīs has a name, such as Nirjalā, Devaśayanī, Prabodhinī and Mokṣadā, and a story in the Ekādaśī māhātmyas.','The Mura story gives the fast its origin: while Viṣṇu rested in a cave, a radiant goddess sprang from his body and destroyed the demon Mura. Viṣṇu named her Ekādaśī and promised that those who fast on her day would be freed from sin.'],
 'margashirsha':['The solar month of Dhanus, Mārgaḻi in Tamil, runs from mid-December to mid-January. It is considered the dawn of the gods’ day, the brahma muhūrta of the year, and is given over to early-morning worship.','Kṛṣṇa’s words in the Gītā, “of months I am Mārgaśīrṣa”, give the month special sanctity. Mārgaśīrṣa may once have begun the year, which may be why it is called the best.'],
 'gate':['The Vaikuṇṭha dvāra is a symbol made physical. Viṣṇu temples are built as images of Vaikuṇṭha, and the northern gate stands for the passage from this world to his abode. Walking through it on this one day is taken as a foretaste of liberation.','Many smaller temples set up a decorated temporary gate on the north side for the day so that devotees everywhere can take part.'],
 'story':['The Madhu–Kaiṭabha telling is common in South Indian temple lore: the two asuras born from Viṣṇu’s ear during the cosmic sleep fought him, were defeated, and asked for a boon, that the gate of Vaikuṇṭha should open for all who come through it on this day.','The name Mukkoṭi, “three crores”, refers to the traditional 33 crore gods, who are said to throng to Vaikuṇṭha to see Viṣṇu on this day; devotees on earth join them.'],
 'srirangam':['The Adhyayana Utsavam at Srirangam is one of the great festivals of South India. Over twenty-one days the Nālāyira Divya Prabandham, the four thousand Tamil verses of the Āḻvārs, is recited in order before Raṅganātha, with the Tiruvāymoḻi of Nammāḻvār at its heart during the Rāppattu nights.','The opening of the Paramapada Vāsal before dawn on the Ekādaśī, with Namperumāḷ carried through it in procession, draws enormous crowds. The festival closes with the enactment of Nammāḻvār’s attaining of Vaikuṇṭha.'],
 'araiyar':['Araiyar sevai is a rare living art: the Araiyars sing and enact the Āḻvārs’ hymns in a mix of music, gesture and commentary, wearing tall caps, before the deity. It survives in only a few temples.','Tradition tells that Nāthamuni, the first great Śrīvaiṣṇava ācārya, recovered the lost hymns of Nammāḻvār and set them to music, and that the Srirangam festival grew from his work.'],
 'tirumala':['At Tirumala the Vaikuṇṭha Dvāram is a passage that circles the sanctum. In recent years TTD has kept it open for ten days so that more pilgrims can pass through, issuing tokens in advance.','On Dvādaśī, the Cakrasnānam bathes the Sudarśana Cakra in the temple tank. At Bhadrācalam in Telangana, Rāma’s temple holds a famous gate-opening, the Uttara Dvāra Darśanam.'],
 'karnataka':['In Karnataka the day is widely called Mukkoṭi Ekādaśī. Temples of Veṅkaṭeśvara and Viṣṇu build a festive northern gate, and city temples see queues through the night.','Dhanurmāsa pūjā at dawn, with huggi (pongal) as prasāda, is a long tradition in Mysuru and across the state.'],
 'mokshada':['The Mokṣadā story is typical of the Ekādaśī māhātmyas: a king, King Vaikhānasa of Campaka city, troubled by a dream of his father in hell, is told by the sage Parvata to keep this Ekādaśī and offer its merit to his father, who is then freed.','It reflects a strong Indian belief that a descendant’s good acts can help ancestors, also seen in śrāddha and in offerings at places like Gayā.'],
 'gitajayanti':['The tradition that the Gītā was spoken on Mārgaśīrṣa Śukla Ekādaśī is widely held and is the basis of Gītā Jayantī. Kurukṣetra in Haryana hosts a large Gītā Mahotsav around the date.','Many families read the whole Gītā aloud that day, often in a group, or a single chapter with care. Our series covers all 700 ślokas with meanings and deep dives.'],
 'fast':['The fast can be kept at many levels, and tradition is flexible: the ill, the elderly, children and pregnant women are excused or keep a light fast. Devotion, not strain, is the point.','Anyone with diabetes, heart disease or on regular medication should check with their doctor before fasting.'],
 'rice':['The belief that sin resides in grains on Ekādaśī is popular rather than scriptural in a strict sense; it is often told with the Medhas story, in which a sage’s body became rice and barley.','Whatever the reason, a grain-free day of light eating is the defining practice of Ekādaśī across India, and regional fasting foods have grown up around it.'],
 'vigil':['Jāgaraṇa, keeping awake, is an old part of Ekādaśī. It turns the night into worship and prepares the devotee for the dawn darśan.','The Paramapada sopānam game, an Indian ancestor of snakes and ladders, is still played in many Tamil homes on this night: its ladders are virtues and its snakes vices, and its last square is Vaikuṇṭha.'],
 'parana':['Breaking the fast correctly is part of the vow. The pāraṇa window on Dvādaśī morning is given in almanacs; many first offer tulasī water to Viṣṇu and feed a guest or the needy.','A traditional Dvādaśī meal in the South includes simple dishes such as agathi keerai (a leaf), amla and sundaikkai, chosen to restore the body gently.'],
 'ambarisha':['The Ambarīṣa story, in the Bhāgavata Purāṇa’s ninth book, is the classic tale of Dvādaśī. Faced with breaking the vow or insulting his guest, the king sips water, which counts as both eating and not eating.','Durvāsā’s fury and Sudarśana’s chase through all the worlds end when Viṣṇu tells the sage that he is bound to his devotees, and that only Ambarīṣa can save him. The king prays for the sage, and the discus stops.'],
 'andal':['Āṇḍāḷ, the only woman among the twelve Āḻvārs, wrote the Tiruppāvai as a vow kept by young women in Mārgaḻi. Its thirty verses are sung at dawn throughout the month, and in Tirumala during Mārgaḻi it replaces the Suprabhātam.','Vaikuṇṭha Ekādaśī falls within this month of dawn songs, so many devotees read the Tiruppāvai alongside the Gītā and the Sahasranāma.'],
 'meaning':['The day gathers several teachings: the door to the highest can be opened; fasting clears the mind; staying awake is a kind of devotion; and the Gītā, spoken on this day, explains how to live and how to be free.','The Ambarīṣa story adds the last lesson: humility protects the devotee more surely than power.']}
exec(open('/home/claude/work/shakti/vk_x.py').read())
pages=addx(pages,EX)
head=head_vis('Vaikuṇṭha Ekādaśī 2026 · Mukkoṭi · Gītā Jayantī · srini.presents','Vaikuṇṭha Ekādaśī 2026 (Mukkoṭi, Svargavāsal, Mokṣadā Ekādaśī) on Sunday 20 December, with Gītā Jayantī the same day: the northern gate, Srirangam’s Adhyayana Utsavam and Paramapada Vāsal, Tirumala’s Vaikuṇṭha Dvāram, fasting, vigil, pāraṇa and the story of Ambarīṣa.')
cov=cover_hn('VIṢṆU’S GREAT DAY','VAIKUṆṬHA EKĀDAŚĪ',13,'The day the gate of Vaikuṇṭha opens · 20 December 2026',art).replace('HANUMĀN · A REFERENCE GUIDE','FESTIVALS · A REFERENCE GUIDE')
fw=foreword_dv('Om Namo Nārāyaṇāya,',[
 'Once a year, before dawn, a gate that stays shut all year is opened on the north side of every great Viṣṇu temple. Pilgrims who have waited all night walk through it into the Lord’s presence. This is <b>Vaikuṇṭha Ekādaśī</b>, the day the gate of Vaikuṇṭha opens.',
 'In 2026 it falls on <b>Sunday 20 December</b>, and it is also <b>Gītā Jayantī</b>, the day the Bhagavad Gītā was spoken. This guide explains the day: what Ekādaśī is, why this one is special, how Srirangam and Tirumala keep it, how to fast and break the fast, and the stories behind it.'],
 'Do I have to fast?','Fast if you can, as much as you can. Reading the Gītā and visiting the gate are just as dear.',
 '<div class="panel reading small"><p>A festival guide in the <a href="/bhakti/vishnu/">Viṣṇu</a> section. Read with our <a href="/bhakti/vishnu/bhagavad-gita/">Bhagavad Gītā</a> for Gītā Jayantī.</p></div>')
toc=[(_re.search(r'id="([^"]+)"',p).group(1),_re.search(r'class="page-title">(.*?)<',p).group(1).title().replace('’S','’s')) for p in pages]
build('/home/claude/work/shakti/VK_Vaikuntha.html',head,cov,fw,pages,toc)
