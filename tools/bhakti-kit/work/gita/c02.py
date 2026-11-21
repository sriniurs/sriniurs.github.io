exec(open('/home/claude/work/gita/gc.py').read())
exec(open('/home/claude/work/gita/c02a.py').read()); exec(open('/home/claude/work/gita/c02b.py').read())
V=VA+VB
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Krishna, glowing, teaching Arjuna who kneels with folded hands; a flame-like light of the eternal Self rises between them">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+GLOW(190,90,80,'#ffd60a',.3)+GLOW(190,90,30,'#ffd60a',.8)+'<path d="M0 220 h380 V268 H0z" fill="#c9a26b" stroke="#111"/>'
 +KR(250,190,1.5)+AR(120,200,1.3,'folded',False)+'</svg>')
P=dict(ch=2,nv=72,V=V,per=[13,15,15,15,14],out='/home/claude/work/gita/Gita_Chapter02.html',
 title='The Undying Self · Bhagavad Gītā Chapter 2 · srini.presents',
 desc='Bhagavad Gītā chapter 2, Sāṅkhya Yoga, every śloka explained: Arjuna becomes Kṛṣṇa’s student; the Self that is never born and never dies; work without craving for the fruit; yoga as evenness and skill in action; the person of steady wisdom. All 72 ślokas in IAST, each on two pages.',
 burst='CHAPTER 2 OF 18',h1='THE UNDYING SELF',series='BHAGAVAD GĪTĀ · CHAPTER 2 · SĀṄKHYA YOGA',tag='The Gītā in miniature · every śloka explained',cover=cover,
 where=[f'In {chl(1)} Arjuna saw his grandfathers and teachers across the field, dropped his bow and sank down in grief.',
  'Chapter 2 is where the teaching starts, and many call it <b>the Gītā in miniature</b>. It holds almost every big idea of the book: the eternal Self, duty, action without craving for results, yoga as evenness of mind, and the portrait of the person of steady wisdom.'],
 wtalk=("If I read just one chapter?","Read this one. Everything later unfolds what Kṛṣṇa says here."),
 fullnote=FULLNOTE,
 secs=[('ARJUNA ASKS',1),('THE SELF',11),('DUTY AND HONOUR',31),('THE YOGA OF ACTION',39),('STEADY WISDOM',54)],
 end=['<b>The student (2.1–10).</b> Kṛṣṇa rebukes Arjuna’s weakness; Arjuna surrenders and asks to be taught.',
  '<b>The Self (2.11–30).</b> The real never ceases; the Self is never born and never dies; bodies are clothes it changes.',
  '<b>Duty (2.31–38).</b> A warrior should not flee a just war; fight with an even mind in victory or defeat.',
  '<b>Karma yoga (2.39–53).</b> Your right is to action, not its fruits; yoga is evenness, and skill in action.',
  '<b>Steady wisdom (2.54–72).</b> Content within, senses drawn in like a tortoise’s limbs, still as the ocean, free of “I” and “mine”.'],
 endsub='Chapter 2 in five lines',
 next=("What's next?",f'{chl(3)}: Karma Yoga. Arjuna is puzzled: if understanding is higher, why push me into this terrible work? Kṛṣṇa explains why no one can avoid action, and how to act as an offering.'),
 endkey='<b>the Self cannot die; act without craving the fruit</b>.',
 foot=FOOT(2,'Links to the Kaṭha and Bṛhadāraṇyaka Upaniṣads, and remarks about Vivekananda and Gandhi, are from the wider tradition, not the Gītā text. '))
build2(P)
