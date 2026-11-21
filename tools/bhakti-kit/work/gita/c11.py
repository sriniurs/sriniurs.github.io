exec(open('/home/claude/work/gita/gc.py').read())
exec(open('/home/claude/work/gita/c11a.py').read()); exec(open('/home/claude/work/gita/c11b.py').read())
V=VA+VB2
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The cosmic form of Krishna filling the night sky, many heads and arms, sun and moon as eyes, a tiny Arjuna bowing below">'
 '<rect width="380" height="268" fill="#05122a" rx="8"/>'+STARS(14,3)+GLOW(190,110,120,'#ffd60a',.25)+COSMIC(190,120,1.6)+SUN(160,32,8)+MOON(220,32,7)+'<path d="M0 240 h380 V268 H0z" fill="#c9a26b" stroke="#111"/>'+AR(190,236,.6,'folded',False)+'</svg>')
P=dict(ch=11,nv=55,V=V,per=[14,14,14,13],out='/home/claude/work/gita/Gita_Chapter11.html',
 title='The Cosmic Form · Bhagavad Gītā Chapter 11 · srini.presents',
 desc='Bhagavad Gītā chapter 11, Viśvarūpa Darśana Yoga, every śloka explained: Arjuna receives the divine eye and sees the universal form, brighter than a thousand suns; “I am Time, destroyer of worlds”; “be merely the instrument”; Arjuna’s great hymn; and the return of the gentle form. All 55 ślokas in IAST, each on two pages.',
 burst='CHAPTER 11 OF 18',h1='THE COSMIC FORM',series='BHAGAVAD GĪTĀ · CHAPTER 11 · VIŚVARŪPA DARŚANA YOGA',tag='Brighter than a thousand suns · every śloka explained',cover=cover,
 where=[f'In {chl(10)} Kṛṣṇa named his glories and ended: the whole universe is one fragment of me.',
  'Now Arjuna asks to <b>see</b> it. Kṛṣṇa gives him a divine eye, and the universal form fills the sky: countless faces, the sun and moon as eyes, all gods within. Then the vision turns fierce: the warriors rushing into fiery mouths. “I am Time,” says Kṛṣṇa; “be merely my instrument.” Arjuna sings a great hymn, begs forgiveness, and asks for the gentle form again.'],
 wtalk=("Is this the most dramatic chapter?","Yes. Many say it is the climax of the Gītā: the moment Arjuna sees who his friend really is."),
 fullnote=FULLNOTE,
 secs=[('ARJUNA ASKS TO SEE',1),('THE DIVINE EYE',5),('WHAT ARJUNA SEES',15),('TIME, THE DESTROYER',26),('ARJUNA’S HYMN',35),('THE GENTLE FORM',45)],
 end=['<b>The request (11.1–8).</b> Arjuna asks to see the divine form; Kṛṣṇa gives him the divine eye.',
  '<b>The vision (11.9–25).</b> Brighter than a thousand suns; all gods and worlds within; no beginning, middle or end; the worlds tremble.',
  '<b>Time (11.26–34).</b> The warriors rush into his mouths like rivers to the sea, like moths to a flame. “I am Time; be merely my instrument.”',
  '<b>The hymn (11.35–46).</b> Arjuna bows a thousand times, begs forgiveness for treating him as a mere friend, and asks for the gentle form.',
  '<b>The gentle form (11.47–55).</b> This vision comes by grace and undivided devotion; work for me, love me, and hate no one.'],
 endsub='Chapter 11 in five lines',
 next=("What's next?",f'{chl(12)}: Devotion. After the overwhelming vision, Arjuna asks a simple question: who is the better yogi, the one who loves the personal Lord or the one who meditates on the formless? Kṛṣṇa’s answer, and the marks of the devotee dear to him.'),
 endkey='<b>be the Lord’s instrument, and hate no one</b>.',
 foot=FOOT(11,'The Oppenheimer remarks are documented history; they are not part of any traditional reading. '))
build2(P)
