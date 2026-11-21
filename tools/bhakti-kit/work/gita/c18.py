exec(open('/home/claude/work/gita/gc.py').read())
for f in ('c18a','c18b','c18c'): exec(open(f'/home/claude/work/gita/{f}.py').read())
V=VA+VB+VC
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Arjuna standing tall with his bow raised, Krishna at the reins of the chariot, a sunrise of victory behind them">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+SUN(190,110,60)+GLOW(190,110,130,'#ff8c1a',.25)+'<path d="M0 220 h380 V268 H0z" fill="#c9a26b" stroke="#111"/>'+RATHA(170,234,1.35,armood='ok',arbow=True)+T(190,30,'MĀ ŚUCAḤ',22,'#ffd60a')+'</svg>')
P=dict(ch=18,nv=78,V=V,per=[14,16,16,16,16],out='/home/claude/work/gita/Gita_Chapter18.html',
 title='Freedom by Letting Go · Bhagavad Gītā Chapter 18 · srini.presents',
 desc='Bhagavad Gītā chapter 18, Mokṣa Sannyāsa Yoga, every śloka explained: renunciation and relinquishment, the five causes of action, knowledge, action, doer, happiness in three kinds, work as worship, “sarva-dharmān parityajya”, Arjuna’s answer, and Sañjaya’s last word. All 78 ślokas in IAST, each on two pages.',
 burst='CHAPTER 18 OF 18',h1='FREEDOM BY LETTING GO',h1size=60,series='BHAGAVAD GĪTĀ · CHAPTER 18 · MOKṢA SANNYĀSA YOGA',tag='Do not grieve · every śloka explained',cover=cover,
 where=[f'In {chl(17)} Kṛṣṇa showed how faith, food, worship and giving take on the colours of the three guṇas, and taught oṃ tat sat.',
  'Chapter 18, the longest, gathers the whole Gītā. True renunciation is letting go of the fruits, not of the work. Knowledge, action, the doer, understanding and even happiness come in three kinds. Work done as worship leads to perfection. Then come Kṛṣṇa’s last words, “abandon all dharmas and take refuge in me alone; do not grieve”, and Arjuna’s answer: “my delusion is gone; I will do as you say.”'],
 wtalk=("Is this the summary of everything?","Yes. Many read chapter 18 as the Gītā in brief, ending where chapter 1 began, with Arjuna on the chariot. Only now he stands up."),
 fullnote=FULLNOTE,
 secs=[('TRUE RENUNCIATION',1),('THE FIVE CAUSES',13),('THREE KINDS OF EVERYTHING',18),('WORK AS WORSHIP',41),('THE SUMMIT',50),('THE LAST WORDS',57),('THE GĪTĀ’S BLESSING',67)],
 end=['<b>Letting go (18.1–12).</b> Keep sacrifice, charity and austerity, but drop attachment and fruit: that is sāttvika tyāga.',
  '<b>Action and its kinds (18.13–40).</b> Five causes of every act; knowledge, action, doer, understanding, resolve and happiness in three kinds.',
  '<b>Work as worship (18.41–49).</b> Worship the Lord through your own work; your own dharma, even imperfect, is best.',
  '<b>The summit (18.50–66).</b> Become Brahman, reach supreme devotion, take refuge in the Lord; “abandon all dharmas, take refuge in me; do not grieve.”',
  '<b>The close (18.67–78).</b> Arjuna: “my delusion is gone; I will do as you say.” Where Kṛṣṇa and Arjuna are, there is victory.'],
 endsub='Chapter 18 in five lines',
 next=("And now?",f'The Gītā is complete. Go back to the {OVL} for the whole map, or begin again at {chl(1)}. As Sañjaya says, remember it again and again, and rejoice again and again.'),
 endkey='<b>take refuge in the Lord, do your duty, and do not grieve</b>.',
 foot=FOOT(18,'Readings of 18.66 differ sharply between the schools; we give the main ones without taking sides. '))
build2(P)
