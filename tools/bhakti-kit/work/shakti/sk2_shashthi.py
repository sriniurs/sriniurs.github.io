exec(open('/home/claude/work/shakti/sk_common.py').read())
head=head_navy('The Ṣaṣṭhī Story: Skanda Ṣaṣṭhī and Subrahmaṇya Ṣaṣṭhī · Subrahmaṇya Ṣaṣṭhī 2 · srini.presents',
 'Why Skanda is worshipped on Ṣaṣṭhī, the sixth lunar day: the war with Tārakāsura and Śūrapadma, the mango tree split into the peacock and the rooster, Sūrasaṃhāram at Tiruccendūr, the wedding with Devasenā, and how Karnataka keeps Subrahmaṇya Ṣaṣṭhī in Mārgaśīrṣa with chariots at Kukke and Ghāṭi. An illustrated reference guide.')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The six-faced god hurling his spear at a giant mango tree in the sea, which splits apart; a peacock and a rooster fly out of it">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+'<rect y="200" width="380" height="68" fill="#1d6fb8"/>'
 +MANGOTREE(270,220,1.05,split=True)+'<path d="M120 120 L250 120" stroke="#e0a800" stroke-width="4" stroke-dasharray="8 5"/>'+SKANDA(90,170,1.05,vel=False)
 +'<path d="M128 132 L180 100" stroke="#7a5a2a" stroke-width="4"/><path d="M180 100 q12 -4 22 -20 q-18 2 -26 12z" fill="#e0a800" stroke="#111" stroke-width="2"/>'
 +PEACOCK(220,90,.35)+ROOSTER(330,90,.9)+'</svg>')
cov=cover('PART 2 OF 4','THE ṢAṢṬHĪ STORY',13,'The war of Skanda, and the day we remember it',art)
fw=foreword('Vetrivel Murugaṉukku Arōharā,',[
 'Skanda was born for a war. On the sixth day of the bright fortnight, the tradition says, he finished it: the demon king was struck down, and from his body came the peacock Skanda rides and the rooster on his flag.',
 'That sixth day, <b>Ṣaṣṭhī</b>, became his day. Tamil Nadu keeps <b>Skanda Ṣaṣṭhī</b> in Aippasi with six days of fasting and the great <b>Sūrasaṃhāram</b> on the beach at Tiruccendūr. A month later, Karnataka and the Telugu lands keep <b>Subrahmaṇya Ṣaṣṭhī</b> in Mārgaśīrṣa, with chariots at Kukke and offerings at the cobra’s anthill.',
 'This part tells the war, explains the two Ṣaṣṭhīs, and shows how the day is kept.'],
 'Two Ṣaṣṭhīs for one god?','Two regions, two months, one victory. Tamil Nadu remembers the war; Karnataka remembers the wedding and the serpent.',
 series_note(prev=('skanda','Who is Skanda?'),nxt=('kukke','Kukke Subrahmaṇya')))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Ṣaṣṭhī','The <b>sixth lunar day</b>; every bright-fortnight Ṣaṣṭhī is sacred to Skanda'),
 ('Skanda Ṣaṣṭhī','Tamil Nadu: Ṣaṣṭhī of <b>Aippasi</b> (Kārttika in the lunar calendar), after six days of fasting'),
 ('Subrahmaṇya Ṣaṣṭhī','Karnataka, Andhra Pradesh and Telangana: Ṣaṣṭhī of <b>Mārgaśīrṣa</b> (Nov–Dec)'),
 ('Also called','<b>Campā Ṣaṣṭhī</b>, Kukke Ṣaṣṭhī; Subbarāyana Ṣaṣṭhī in Kannada homes'),
 ('The story','Victory over <b>Tāraka</b> and, in the Tamil telling, <b>Śūrapadma</b>; then the wedding with <b>Devasenā</b>'),
 ('Big events','<b>Sūrasaṃhāram</b> at Tiruccendūr; <b>Brahmaratha</b> chariot at <b>Kukke</b>'),
 ('Observed by','Fasting, worship at the anthill and nāga stones, temple chariots'),
 ('Next','<b>Ghāṭi</b> keeps its chariot on the Ṣaṣṭhī of the following month, Puṣya')])
 +talk("Is it the same day every year?","Same lunar day, different calendar date. Check your pañcāṅga each year.")))
pages.append(page('which','WHICH ṢAṢṬHĪ IS WHICH?','Three names, three months',facts([
 ('Monthly Ṣaṣṭhī','Every bright Ṣaṣṭhī: a small fast for Skanda, all year round'),
 ('Skanda Ṣaṣṭhī (Kanda Ṣaṣṭi)','Aippasi (Oct–Nov): Tamil Nadu, Sri Lanka, Malaysia. Six days; the war on day six, the wedding on day seven'),
 ('Subrahmaṇya Ṣaṣṭhī','Mārgaśīrṣa (Nov–Dec): Karnataka and the Telugu states; drik pañcāṅgas call it “the next Ṣaṣṭhī after Sūrasaṃhāram”'),
 ('Campā Ṣaṣṭhī, Maharashtra','The same Mārgaśīrṣa day ends the six-day festival of <b>Khaṇḍobā</b> at Jejuri, a form of Śiva'),
 ('Puṣya Ṣaṣṭhī','The month after: Ghāṭi Subrahmaṇya’s chariot festival'),
 ('Why “Campā”?','Often said to be for the campaka flower, dear to Skanda; explanations differ')])
 +talk("So Kukke Ṣaṣṭhī and Jejuri's Campā Ṣaṣṭhī fall on one day?","Yes. Two sons of the same family, you could say: Śiva's son at Kukke, Śiva himself as Khaṇḍobā at Jejuri.")))
pages.append(page('six','WHY THE SIXTH DAY?','Sixes everywhere',facts([
 ('Six mothers','Nursed by the six Kṛttikās'),
 ('Six faces','Ṣaṇmukha: one face per mother'),
 ('Six days of war','In the Tamil telling the battle with Śūrapadma lasts six days'),
 ('Six syllables','Śa-ra-va-ṇa-bha-va'),
 ('Six abodes','The Āṟupaṭai Vīṭu of Tamil Nadu'),
 ('Six enemies','A common teaching: the six inner foes (ṣaḍripu) of desire, anger, greed, delusion, pride and envy, which Skanda’s vel destroys')])
 +talk("Is the six enemies idea in the Purāṇa?","It's a teaching built on the story, very popular in Ṣaṣṭhī sermons. Read it as a meaning, not a fact.")))
pages.append(story('general','THE GENERAL OF THE GODS','A boy takes command',560,180,'The young six-faced god being crowned as general, gods offering him weapons, a banner with a rooster behind',
 '<rect width="560" height="180" fill="#eaf1fb"/>'+FLAG(420,170,1.2)+SKANDA(280,100,.8)+CROWD(110,170,5,22)+'<g transform="translate(200 140)" stroke="#111" stroke-width="2"><path d="M-6 -4 l18 -30" stroke="#bbb" stroke-width="4"/></g>',
 [('Grown in days.','The child of the reeds grew in six days into a young warrior.'),
  ('Made general.','The gods made him <b>Devasenāpati</b>, commander of their army. Each gave a gift: Pārvatī the <b>vel</b>, others weapons, a banner and a mount.'),
  ('The march.','With the gods behind him, Kumāra marched against Tāraka’s city.'),
  ('The brothers.','In the Tamil telling, Śūrapadma ruled with his brothers <b>Siṃhamukha</b>, lion-faced, and <b>Tāraka</b>, elephant-faced.'),
  ('The messenger.','Skanda first sent his commander <b>Vīrabāhu</b> to offer peace. Śūrapadma refused.')]))
pages.append(story('taraka','TĀRAKA AND THE KRAUÑCA HILL','The first victory',560,180,'The young god throwing his spear right through a mountain, behind which a demon falls',
 '<rect width="560" height="180" fill="#2a1a2a"/>'+HILL(330,180,240,150,'#6a5a7a')+'<path d="M140 100 L460 90" stroke="#e0a800" stroke-width="5" stroke-dasharray="10 6"/>'+SKANDA(90,110,.75,vel=False)+DEMON(480,140,1.1,'#5a2a2a'),
 [('The battle.','Tāraka fought with every trick of illusion. He hid behind the mountain <b>Krauñca</b>, which his ally guarded.'),
  ('The spear.','Skanda hurled his vel. It pierced the Krauñca mountain right through, and killed <b>Tāraka</b>.'),
  ('Krauñca.','Old texts remember Skanda as <b>Krauñcabhettā</b>, “the piercer of Krauñca”. In some tellings Krauñca is a demon ally of Tāraka.'),
  ('The boon kept.','Brahmā’s boon held: only Śiva’s son could kill Tāraka, and he did.'),
  ('In the south.','The Tamil Kanda Purāṇam goes on: Siṃhamukha falls next, and then the king, Śūrapadma.')]))
pages.append(story('surapadma','ŚŪRAPADMA AND THE MANGO TREE','Pride split in two',560,190,'A giant mango tree standing in the sea, split down the middle by a golden spear, with a peacock and a rooster flying out',
 '<rect width="560" height="190" fill="#0b2a4a"/>'+STAR+'<rect y="150" width="560" height="40" fill="#1d6fb8"/>'+MANGOTREE(330,170,1.05,split=True)+SKANDA(110,130,.8,vel=False)
 +'<path d="M150 110 L310 100" stroke="#e0a800" stroke-width="5" stroke-dasharray="10 6"/>'+PEACOCK(420,80,.32)+ROOSTER(490,90,.8),
 [('Six days.','The war raged for six days. One by one, Śūrapadma’s sons and brothers fell.'),
  ('Shape-shifting.','On the last day the demon king took one form after another. At last he became a huge <b>mango tree</b> standing in the sea.'),
  ('The vel strikes.','Skanda hurled his vel and split the tree in two.'),
  ('Mercy.','Even then he did not destroy him. One half became the <b>peacock</b> he rides, the other the <b>rooster</b> on his banner.'),
  ('The meaning.','The enemy is not killed but turned into a servant. Many read it as the ego, split and tamed, carrying the god.')],
 talk("He spared the worst demon?","He spared what was left after the pride was gone. That's the Ṣaṣṭhī lesson.")))
pages.append(page('soorasamharam','SŪRASAṂHĀRAM','The war re-enacted on the beach',fig(560,180,'Crowds on a seashore at evening watching a figure of the god face a giant demon effigy beside a temple tower',
 '<rect width="560" height="180" fill="#f2a65a"/><rect y="120" width="560" height="60" fill="#1d6fb8"/><rect y="140" width="560" height="40" fill="#f2e0b0"/>'+GOPURAM(80,150,.8)+SKANDA(270,120,.55)+DEMON(380,150,1.4,'#5a2a2a')+CROWD(170,180,14,26))+facts([
 ('Where','<b>Tiruccendūr</b>, Murugan’s seashore abode, where he camped for the war'),
 ('When','Evening of Skanda Ṣaṣṭhī, the sixth day of the Aippasi festival'),
 ('What','Murugan’s image meets effigies of the demon, who keeps changing heads; finally the tree and the peacock'),
 ('Next day','<b>Tirukkalyāṇam</b>, his wedding with Devasenā'),
 ('Fast','Many devotees fast for all six days, some on one meal, some on milk and fruit; others keep it on Ṣaṣṭhī alone'),
 ('Elsewhere','Kept in Murugan temples across Tamil Nadu, Sri Lanka, Malaysia and Singapore')])))
pages.append(story('wedding','THE WEDDING AT KUMĀRA PARVATA','Karnataka’s Ṣaṣṭhī',560,180,'A forested mountain peak; below it the young god and a crowned bride under a canopy, gods around, and a river flowing',
 '<rect width="560" height="180" fill="#cfe3f5"/>'+HILL(300,150,420,140,'#3a7a3a')+'<rect y="150" width="560" height="30" fill="#4aa3df"/><path d="M190 140 h220 v-60 h-220z" fill="none" stroke="#e0a800" stroke-width="4"/><path d="M180 80 h240 l-20 -18 h-200z" fill="#c0392b" stroke="#111" stroke-width="2"/>'
 +GENTLE(260,120,.55)+SKANDA(330,110,.55,vel=False)+CROWD(40,175,4,20)+CROWD(460,175,4,20),
 [('After the war.','In the Karnataka tradition, after victory Skanda came with his brother Gaṇeśa to <b>Kumāra Parvata</b> in the Western Ghats.'),
  ('Indra’s gift.','There <b>Indra</b> gave him his daughter <b>Devasenā</b> in marriage.'),
  ('The day.','The wedding took place on <b>Mārgaśīrṣa śuddha Ṣaṣṭhī</b>. That is Karnataka’s Subrahmaṇya Ṣaṣṭhī.'),
  ('The river.','Holy waters brought from every river for the wedding flowed together as the <b>Kumāradhārā</b>, the river at Kukke.'),
  ('The serpent.','Nearby, the serpent king <b>Vāsuki</b> was praying in a cave. Skanda stayed to protect him. That story is Part 3.')],
 f'<div class="key">Visit it: <a href="{SKS}kukke/">Kukke Subrahmaṇya</a> (Part 3)</div>'))
pages.append(page('karnataka','HOW KARNATAKA KEEPS IT','At home and at the anthill',fig(560,160,'A family offering milk and flowers at an anthill with stone serpent images, a lamp burning',
 '<rect width="560" height="160" fill="#eef5e8"/>'+ANTHILL(300,150,1.1)+''.join(f'<g transform="translate({x} 150)" stroke="#111" stroke-width="2"><rect x="-12" y="-44" width="24" height="44" rx="10" fill="#9a9a8a"/><path d="M0 -6 q-8 -10 0 -18 q8 -8 0 -16" fill="none" stroke="#5a5a4a" stroke-width="3"/></g>' for x in (390,430))
 +CROWD(120,150,4,30)+'<g transform="translate(220 150)" stroke="#111" stroke-width="2"><path d="M-10 0 h20 l-4 -10 h-12z" fill="#e0a800"/><path d="M0 -10 q-4 -8 0 -14 q4 6 0 14z" fill="#ff8c1a"/></g>')+facts([
 ('Fast','Many fast till the pūjā, or keep one meal'),
 ('The anthill','Milk, turmeric, flowers and a lamp offered at the cobra’s anthill or at nāga stones under a peepal tree'),
 ('Feeding','In many homes a young bachelor boy is fed and honoured as the boy-god Subrahmaṇya'),
 ('Temples','Chariot festivals at Kukke Subrahmaṇya and Subrahmaṇya shrines across the state'),
 ('Mysuru','Ṣaṣṭhī is kept at Mysuru’s Subrahmaṇya temples, such as the one at Bannimaṇṭap'),
 ('Snake vows','A day to fulfil vows made for children, health and freedom from “sarpa doṣa”')])))
pages.append(page('chant','WHAT TO CHANT','Prayers for the day',facts([
 ('Om Śaravaṇabhava','The six-syllabled name, chanted aloud by devotees everywhere'),
 ('Subrahmaṇya Bhujaṅgam','Śaṅkara’s hymn in the snake-gliding bhujaṅga metre; it names Kukke’s liṅga'),
 ('Kanda Ṣaṣṭi Kavacam','A 19th-century Tamil “armour” song by Devarāya Svāmigaḷ, sung through the Ṣaṣṭhī fast'),
 ('Tiruppugaḻ','Arunagirinātar’s 15th-century Tamil songs to Murugan'),
 ('Tirumurukāṟṟuppaṭai','Nakkīrar’s ancient guide to the Six Abodes'),
 ('Skanda Purāṇa','Reading of the birth and war chapters')])
 +talk("Do I need a special mantra?","His name is enough. Initiated mantras come from a guru; this guide doesn't print them.")
 +f'<div class="key">Simplest of all: say his name six times, once for each face. Meet him first in <a href="{SKS}skanda/">Part 1</a>.</div>'))
pages.append(page('meaning','WHAT ṢAṢṬHĪ TEACHES','The war inside',facts([
 ('The demon','Śūrapadma is pride: “I am the doer, I own everything”'),
 ('The vel','Clear knowledge, which pierces illusion'),
 ('The split tree','The ego cut in two, not wiped out: its energy turned to service'),
 ('Six days','Six inner enemies, overcome one day at a time'),
 ('The wedding','Victory is followed by union: power joined to grace')])
 +talk("So the fast is a little war of my own?","Exactly. Six days of saying no to the six enemies, then the sweet on day seven.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Ṣaṣṭhī','Sixth lunar day'),('Śuddha / śukla','Bright fortnight'),('Sūrasaṃhāram','Destruction of Śūra'),('Tirukkalyāṇam','Holy wedding'),('Krauñca','The mountain the vel pierced'),
 ('Ṣaḍripu','The six inner enemies'),('Brahmaratha','The great temple chariot'),('Sarpa doṣa','Affliction believed to come from harming serpents'),('Pañcāṅga','Hindu almanac')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The day.</b> Ṣaṣṭhī, the sixth lunar day: Skanda’s day.</div>
<div><b>Two festivals.</b> Skanda Ṣaṣṭhī in Aippasi (Tamil Nadu); Subrahmaṇya Ṣaṣṭhī in Mārgaśīrṣa (Karnataka, Telugu states).</div>
<div><b>The war.</b> Tāraka and Krauñca; Śūrapadma split as a mango tree into peacock and rooster.</div>
<div><b>The wedding.</b> Devasenā at Kumāra Parvata; the Kumāradhārā river.</div>
<div><b>Keeping it.</b> Fast, worship at the anthill, chariots at Kukke and Ghāṭi.</div>
</div>'''+talk("What's next?","The serpent's own temple. Part 3: Kukke Subrahmaṇya, where Vāsuki hid from Garuḍa.")
 +f'<div class="key">Part 2: the Ṣaṣṭhī story. Next: <a href="{SKS}kukke/">Kukke Subrahmaṇya</a> 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Story:</b> Wikipedia, “Kartikeya” (Tāraka killed with the vel; Siṃhamukha; Śūrapadma as a mango tree split into peacock and rooster; Kanda Ṣaṣṭi in Aippasi or Kārttikai; Kanda Ṣaṣṭi Kavacam, Tiruppugaḻ). Kālidāsa’s Kumārasambhava and the Mahābhārata for Tāraka and Krauñca, retold briefly.</p>
<p><b>Festival:</b> Drik Panchang, “Subrahmanya Sashti” (Mārgaśīrṣa, “next Skanda Sashti after Soorasamharam”, also Kukke Subramanya Sashti); hindutone.com (Telugu and Karnataka usage; Campā Ṣaṣṭhī and Khaṇḍobā at Jejuri on the same tithi); bhaktibharat.com (campaka flower explanation); Kukke temple tradition (kukkedevasthanam.org.in; holidify.com) for the wedding on Mārgaśīrṣa śuddha Ṣaṣṭhī and the Kumāradhārā; Wikipedia, “Ghati Subramanya” (Puṣya śuddha Ṣaṣṭhī).</p>
<p><b>Interpretations:</b> the six enemies, the ego in the split tree, and the meaning of the vel are common teachings. <b>Not verified from a primary text:</b> the order of the demons’ deaths over six days; feeding a bachelor boy (a widespread home custom, varying by family). Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('which','Which Ṣaṣṭhī Is Which?'),('six','Why the Sixth Day?'),('general','The General of the Gods'),('taraka','Tāraka and the Krauñca Hill'),('surapadma','Śūrapadma and the Mango Tree'),
 ('soorasamharam','Sūrasaṃhāram'),('wedding','The Wedding at Kumāra Parvata'),('karnataka','How Karnataka Keeps It'),('chant','What to Chant'),('meaning','What Ṣaṣṭhī Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/SK2_Shashthi.html',head,cov,fw,pages,toc)
