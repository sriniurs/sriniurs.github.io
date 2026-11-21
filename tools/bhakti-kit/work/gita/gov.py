exec(open('/home/claude/work/gita/gc.py').read())
def lnk(ch,v,t): return f'<a href="{GT}chapter-{ch}/#v{v}">{t}</a>'
head=make_head('Bhagavad Gītā · Overview · srini.presents','The Bhagavad Gītā explained: what it is, where it sits in the Mahābhārata, who is who, the 18 chapters at a glance, the key verses, the four yogas, and how the great teachers read it. Start here for the srini.presents series covering all 700 ślokas.')
head=head.replace('</style>',DDCSS,1)
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Krishna as charioteer and Arjuna on a white chariot between two armies, a glowing book of 18 chapters above them">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+GLOW(190,70,70,'#ffd60a',.3)+'<rect x="150" y="34" width="80" height="56" fill="#fff3b0" stroke="#111" stroke-width="3"/><path d="M190 34 v56" stroke="#111" stroke-width="2"/>'+T(190,68,'18 · 700',14)
 +'<path d="M0 230 h380 V268 H0z" fill="#c9a26b" stroke="#111"/>'+ARMY(6,236,5,'#7a2a6a',22,.7)+ARMY(268,236,5,'#1d6fb8',22,.7)+RATHA(180,244,1.2,armood='folded',arbow=False)+'</svg>')
CHS=''.join(f'<li><span class="num">{n}</span><a href="{GT}chapter-{n}/">{nm} · {en}</a></li>' for n,nm,en,_ in CH)
pages=[]
pages.append(textpage('what','WHAT IS THE GĪTĀ?','The essentials on one page',
 grid([('Name','<b>Bhagavad Gītā</b>, “the Song of the Lord”. Also called the Gītopaniṣad.'),('Size','<b>700 ślokas in 18 chapters</b> (Gītā Press count).'),
       ('Where','Chapters 25–42 of the <b>Bhīṣma Parva</b> of the Mahābhārata, the sixth of its eighteen books.'),('Speakers','<b>Kṛṣṇa</b> teaches; <b>Arjuna</b> asks; <b>Sañjaya</b> reports to the blind king <b>Dhṛtarāṣṭra</b>.'),
       ('Setting','The field of Kurukṣetra, on the first day of the great war, between two armies of one family.'),('Author','Traditionally <b>Vyāsa</b>, compiler of the Mahābhārata.'),
       ('Place in tradition','One of the three foundations of Vedānta (prasthāna-traya), with the Upaniṣads and the Brahma Sūtras.'),('Day','<b>Gītā Jayantī</b>: the bright ekādaśī of Mārgaśīrṣa (Mokṣadā Ekādaśī).')]),
 ("Why is it so loved?","It speaks to a person in crisis, in a few hundred verses, and gives not one answer but several paths, for different kinds of people."),
 'A conversation <b>on a battlefield</b>.'))
pages.append(textpage('setting','HOW DID IT COME TO THIS?','The story before the Gītā',
 '<div class="steps">'+''.join(f'<div>{s}</div>' for s in ['<b>Two families, one throne.</b> The blind king Dhṛtarāṣṭra rules Hastināpura. His hundred sons, led by Duryodhana, are the Kauravas; his late brother Pāṇḍu’s five sons are the Pāṇḍavas.',
  '<b>The dice.</b> Śakuni wins the Pāṇḍavas’ kingdom in a rigged game; Draupadī is insulted in the court.','<b>Exile.</b> Twelve years in the forest and one in hiding. On return, Duryodhana will not give even five villages.',
  '<b>Kṛṣṇa’s choice.</b> He offers one side his army and the other himself, unarmed. Arjuna chooses Kṛṣṇa as charioteer; Kṛṣṇa also goes to the Kaurava court to plead for peace, and fails.',
  '<b>The divine eye.</b> Vyāsa gives Sañjaya sight to see the whole war from the palace. After ten days, when Bhīṣma falls, Sañjaya tells the king everything, including the Gītā.'])+'</div>',
 ("So the Gītā is told in a flashback?","Yes. Sañjaya reports it on the tenth day of the war, to the blind king who started it all."),
 'A family war, <b>and a reluctant hero</b>.'))
pages.append(textpage('who','WHO IS WHO','The people of the Gītā',
 grid([('Kṛṣṇa','Arjuna’s cousin, friend and charioteer; for the Gītā, the Supreme Lord. Called Keśava, Mādhava, Govinda, Hṛṣīkeśa, Vāsudeva…'),('Arjuna','Third Pāṇḍava, the greatest archer; called Pārtha, Dhanañjaya, Guḍākeśa, Kaunteya, Bhārata…'),
  ('Dhṛtarāṣṭra','The blind king, father of the Kauravas; speaks only the first verse.'),('Sañjaya','His minister, given divine sight by Vyāsa; narrates the Gītā.'),
  ('Bhīṣma','The grandsire, bound by a vow to serve the throne; commander of the Kauravas.'),('Droṇa','Teacher of both sides in arms.'),
  ('Duryodhana','Eldest Kaurava, whose refusal to share led to the war.'),('Karṇa','Duryodhana’s friend, secretly Kuntī’s eldest son.')]),
 ("Why so many names for Kṛṣṇa and Arjuna?","Each name is chosen for the moment and often carries a hint. Watch for them as you read."),
 'Know the cast, <b>then read the play</b>.'))
pages.append(f'''<section class="page" id="map">
  <h2 class="page-title">THE 18 CHAPTERS</h2>
  <div class="sub">Three groups of six · tap a chapter to open it</div>
  <ul class="toc tight"><li class="part">1–6 · ACTION (KARMA)</li>{''.join(CHS.split('</li>')[k]+'</li>' for k in range(0,6))}<li class="part">7–12 · DEVOTION AND THE LORD (BHAKTI)</li>{''.join(CHS.split('</li>')[k]+'</li>' for k in range(6,12))}<li class="part">13–18 · KNOWLEDGE (JÑĀNA)</li>{''.join(CHS.split('</li>')[k]+'</li>' for k in range(12,18))}</ul>
  <div class="panel pt">Many teachers divide the Gītā into three ṣaṭkas (groups of six): the first on the Self and action, the middle on God and devotion, the last on knowledge and freedom. The divisions overlap: every part has action, devotion and knowledge in it.</div>
  {talk("Where should I start?","Chapter 2 is the Gītā in miniature. Chapter 12 is the shortest. Or begin at chapter 1 and walk with Arjuna.")}
  <div class="key">18 chapters, <b>three movements</b>.</div>
</section>
''')
KV=[(2,47,'“Your right is to action alone, never to its fruits.”'),(2,20,'“It is never born, nor does it ever die.”'),(2,22,'Bodies are like clothes the Self changes.'),(3,35,'“Better one’s own dharma, though imperfect.”'),(4,7,'“Whenever dharma declines…”'),(4,8,'“To protect the good… I come age after age.”'),
    (6,5,'“Lift yourself by yourself.”'),(6,19,'A lamp in a windless place.'),(9,26,'“A leaf, a flower, a fruit, water, with love.”'),(11,32,'“I am Time, destroyer of worlds.”'),(12,13,'“Hating none, friendly, compassionate.”'),(18,66,'“Take refuge in me alone; do not grieve.”')]
pages.append(textpage('keyverses','TWELVE FAMOUS VERSES','Tap one to jump to its two pages',
 '<div class="grid2">'+''.join(f'<div><h4>{lnk(c,v,f"{c}.{v}")}</h4>{t}</div>' for c,v,t in KV)+'</div>',None,'Start with these, <b>then read all 700</b>.'))
pages.append(textpage('paths','FOUR PATHS IN ONE BOOK','The yogas of the Gītā',
 grid([('Karma yoga','<b>Action without craving the fruit</b>, as an offering (chapters 2–5, 18). For the active.'),('Jñāna yoga','<b>Knowledge</b> of the Self as distinct from body and mind (chapters 2, 4, 13–15). For the reflective.'),
       ('Dhyāna yoga','<b>Meditation</b>: steadying the mind like a lamp in a windless place (chapters 5–6). For the contemplative.'),('Bhakti yoga','<b>Devotion</b>: love of the Lord, offering everything (chapters 7–12, 18). For the loving.')])
 +'<div class="panel pt">The Gītā does not force one path. It weaves them together, and the great commentators disagree on which is chief. That disagreement is part of its richness.</div>',
 ("Which path is best?","Kṛṣṇa says different paths suit different natures (3.3, 12.8–11, 13.24). Find yours, and walk it sincerely."),
 'Many paths, <b>one goal</b>.'))
pages.append(textpage('teachers','HOW THE GREAT TEACHERS READ IT','Commentators across the centuries',
 grid([('Śaṅkara (8th c.)','Advaita: the Self is one with Brahman; knowledge frees; action purifies the mind for knowledge. The oldest surviving full commentary.'),('Rāmānuja (11th–12th c.)','Viśiṣṭādvaita: souls and world are the body of the Lord; devotion and surrender (prapatti) lead to him.'),
       ('Madhva (13th c.)','Dvaita: God, souls and matter are eternally distinct; devotion to Viṣṇu with knowledge.'),('Jñāneśvar (13th c.)','The Jñāneśvarī, a beloved Marathi poetic commentary, reading the Gītā as a song of devotion and wisdom.'),
       ('Modern readers','Tilak saw a call to action (Gītā Rahasya); Gandhi a guide to selfless, non-violent work (Anāsakti Yoga); Vivekananda and Aurobindo a manifesto of strength and spiritual life.'),('Our approach','Where readings differ, we give the main ones without taking sides. Meanings are our own plain-English renderings.')]),
 None,'One text, <b>many readings</b>.'))
pages.append(textpage('howto','HOW THIS SERIES WORKS','Every śloka, two pages',
 '<div class="steps">'+''.join(f'<div>{s}</div>' for s in ['<b>In one go.</b> Each chapter starts with all its ślokas in IAST, for chanting straight through.',
  '<b>Page one of each śloka.</b> The chant, a picture, what it says in plain English, and a table of key words.','<b>Page two: the deep dive.</b> The context, how the teachers read it, and what it can mean for us today.',
  '<b>On one page.</b> Each chapter ends with a five-line summary and a link to the next.','<b>The text.</b> Gītā Press (Gorakhpur) reading and numbering, checked line by line against the IIT Kanpur Gita Supersite, in IAST.'])+'</div>',
 ("Can I print it?","Yes. Every page is designed to fit one A4 sheet."),
 'Chant it, read it, <b>live it</b>.'))
body=''.join(pages)
html=head+f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">SERIES OVERVIEW</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">THE BHAGAVAD GĪTĀ</h1>
  <div class="series">THE SONG OF THE LORD · 18 CHAPTERS · 700 ŚLOKAS</div>
  <div class="tag">Every śloka, explained and illustrated</div>
  {cover}
  {CAST}
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> Start here for the big picture: what the Gītā is, the story, the people, the map of all 18 chapters and the most famous verses. Then open any chapter, where every śloka has two pages.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    <p>On a battlefield, between two armies of one family, the greatest archer of his age drops his bow and refuses to fight. His charioteer, Kṛṣṇa, answers him. Their conversation, 700 verses long, is the <b>Bhagavad Gītā</b>.</p>
    <p>For over two thousand years it has been chanted in homes, argued over by philosophers, carried by soldiers and saints, and read by people facing every kind of crisis. It asks the oldest questions: who am I, what should I do, and how can I be free?</p>
    <p>This series takes all 18 chapters, every śloka on two pages, in plain English with comic illustrations, alongside our other <a href="/bhakti/scriptures/">scriptures</a> and the <a href="/bhakti/vishnu/dashavatara/">Daśāvatāra</a>.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--blue)">With the blessings of the Lord,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why read it now?","Because it was spoken to a person who was stuck. Most of us are, sometimes.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">THIS OVERVIEW</li>
    <li><span class="num">1</span><a href="#what">What Is the Gītā?</a></li><li><span class="num">2</span><a href="#setting">How Did It Come to This?</a></li><li><span class="num">3</span><a href="#who">Who Is Who</a></li>
    <li><span class="num">4</span><a href="#map">The 18 Chapters</a></li><li><span class="num">5</span><a href="#keyverses">Twelve Famous Verses</a></li><li><span class="num">6</span><a href="#paths">Four Paths</a></li>
    <li><span class="num">7</span><a href="#teachers">The Great Teachers</a></li><li><span class="num">8</span><a href="#howto">How This Series Works</a></li><li><span class="num">∑</span><a href="#end">On One Page</a></li>
    <li class="part">THE CHAPTERS</li>{CHS}
  </ul>
</section>
{body}
<section class="page" id="end">
  <h2 class="page-title">THE GĪTĀ ON ONE PAGE</h2>
  <div class="sub">The whole teaching in five lines</div>
  <div class="steps">
    <div><b>You are not the body.</b> The Self is never born and never dies (2.20).</div>
    <div><b>Act, but don’t grasp.</b> Your right is to action, not its fruits (2.47).</div>
    <div><b>Steady the mind.</b> Like a lamp in a windless place (6.19).</div>
    <div><b>See the Lord in all.</b> All is strung on him like pearls on a thread (7.7), and he lives in every heart (18.61).</div>
    <div><b>Love, and let go.</b> Take refuge in him; do not grieve (18.66).</div>
  </div>
  {talk("What's next?",f'Start with {chl(1,"Chapter 1: Arjuna’s Despair")}, and walk with Arjuna from his breakdown to “I will do as you say”.')}
  <div class="key">The Gītā: <b>know who you are, act without grasping, love the Lord</b>. 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Overview of the Bhagavad Gītā (Mahābhārata, Bhīṣma Parva). Story details come from the wider Mahābhārata. Dates of commentators are approximate and traditional. Where the great commentators read a verse differently, we say so. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
'''+tail()
open('/home/claude/work/gita/Gita_Overview.html','w').write(html)
print('ok', html.count('<section class="page'))
