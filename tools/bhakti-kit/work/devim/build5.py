import sys; sys.path.insert(0,'/home/claude/work/devim')
from common import *
head=make_head('The Frame Story · Part 5 · Devī Māhātmya series · srini.presents',
 'Devī Māhātmya, Part 5: the frame story of chapter 1. A king who lost his kingdom, a merchant thrown out by his family, and the sage Medhas, who tells them of Mahāmāyā. Explained in plain English with illustrations.')
def KING(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2"><path d="M-12 -46 h24 l-3 -12 l-5 5 l-4 -8 l-4 8 l-5 -5z" fill="#ffd60a"/>'
  '<circle cy="-30" r="12" fill="#c98b5a"/><path d="M-6 -24 q6 6 12 0" fill="none"/><path d="M-18 22 q18 -54 36 0z" fill="#c0392b"/><path d="M18 -6 l14 -26" stroke="#ccc" stroke-width="3"/></g>')
def MERCH(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2"><path d="M-13 -40 q13 -12 26 0 q-13 6 -26 0z" fill="#ff8c1a"/>'
  '<circle cy="-30" r="12" fill="#c98b5a"/><path d="M-18 22 q18 -54 36 0z" fill="#ffd60a"/></g>')
def SAGE(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2"><path d="M-8 -42 q8 -12 16 0" fill="#ddd"/>'
  '<circle cy="-30" r="12" fill="#c98b5a"/><path d="M-9 -24 q9 22 18 0z" fill="#fff"/><path d="M-20 22 q20 -54 40 0z" fill="#ff8c1a"/><path d="M24 22 v-50" stroke="#7a5a3a" stroke-width="3"/></g>')
HORSE=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-28" y="-14" width="52" height="24" rx="10" fill="#7a5a3a"/><path d="M20 -10 l14 -22 l8 4 l-8 22z" fill="#7a5a3a"/><path d="M-20 10 v16 M-6 10 v16 M8 10 v16 M18 10 v16" stroke-width="4"/><path d="M-28 -8 q-12 4 -10 20" fill="none" stroke-width="3"/></g>'
TREE=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M0 0 v-40" stroke="#7a5a3a" stroke-width="7"/><circle cy="-56" r="26" fill="#2a9d6f"/></g>'
DEER=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse rx="16" ry="8" fill="#c9a26b"/><circle cx="16" cy="-10" r="6" fill="#c9a26b"/><path d="M14 -16 l-4 -8 M18 -16 l4 -8 M-10 6 v10 M8 6 v10" fill="none"/></g>'
TIGER=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse rx="18" ry="8" fill="#ff8c1a"/><circle cx="-18" cy="-8" r="7" fill="#ff8c1a"/><path d="M-4 -8 v14 M4 -8 v14 M12 -6 v12" stroke-width="2"/></g>'
def panels(label,frames):
    out=f'<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="{label}"><rect width="460" height="210" fill="#fff8ec"/>'
    for i,(bg,t,inner) in enumerate(frames):
        out+=f'<g><rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><g transform="translate({6+151*i} 6)">{inner}</g><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text></g>'
    return out+'</svg>'
def storypage(id_,title,sub,svgp,steps,tk,key):
    st=''.join(f'<div>{s}</div>' for s in steps)
    return f'''<section class="page" id="{id_}">
  <h2 class="page-title">{title}</h2>
  <div class="sub">{sub}</div>
  {svgp}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story</span>
    <div class="steps" style="margin:0">{st}</div>
  </div>
  {talk(*tk)}
  <div class="key">{key}</div>
</section>
'''
V=[
dict(n='2–3',lab='ŚLOKAS 1.2–3 · THE EIGHTH MANU',lines=[['sāvarṇiḥ sūryatanayo','yo manuḥ kathyate’ṣṭamaḥ |'],['niśāmaya tadutpattiṃ','vistarād gadato mama ‖2‖'],['mahāmāyānubhāvena','yathā manvantarādhipaḥ |'],['sa babhūva mahābhāgaḥ','sāvarṇis tanayo raveḥ ‖3‖']],theme='HOW A KING BECAME A MANU',
 svg=svg('The sage Markandeya speaking, and above him a golden figure of the future Manu Savarni, son of the Sun',SAGE(60,150,1.4)+SUN(160,40,22)+KING(160,140,1.1)+T(160,154,'SĀVARṆI',10),R),
 mean='Mārkaṇḍeya said: Sāvarṇi, son of the Sun, who is called the eighth Manu: hear from me in detail how he came to be; how, by the power of Mahāmāyā, that fortunate one, Sāvarṇi, son of Ravi (the Sun), became the lord of a Manu’s age.',
 words=[('sāvarṇiḥ sūrya-tanayaḥ','<b>Sāvarṇi, son of the Sun</b>'),('manuḥ aṣṭamaḥ','<b>the eighth Manu</b>'),('mahāmāyā-anubhāvena','<b>by the power of Mahāmāyā</b>'),('manvantara-adhipaḥ','<b>ruler of a Manu’s age</b>')],
 point='<b>The answer comes first.</b> The book opens by telling us how it ends: a king will become <b>Sāvarṇi, the eighth Manu</b>, the father of mankind in a future age, and all by the grace of the Goddess. How he gets there is the story.',
 key='A ruined king will become a Manu, <b>by her power</b>.'),
dict(n='42',lab='ŚLOKA 1.42 · THE KING’S QUESTION',lines=[['mamatvaṃ gatarājyasya','rājyāṅgeṣv akhileṣv api |'],['jānato’pi yathājñasya','kim etan munisattama ‖42‖']],theme='WHY CAN’T I LET GO?',
 svg=svg('The king and the merchant sitting before the sage, a thought cloud over the king showing his lost palace and elephants',SAGE(170,150,1.2)+KING(50,150,1)+MERCH(100,150,1)+'<ellipse cx="60" cy="40" rx="50" ry="28" fill="#fff" stroke="#111" stroke-width="2"/><rect x="34" y="34" width="28" height="22" fill="#e0a800" stroke="#111"/><path d="M34 34 l14 -12 l14 12" fill="#c0392b" stroke="#111"/><ellipse cx="84" cy="48" rx="12" ry="8" fill="#bbb" stroke="#111"/><circle cx="62" cy="80" r="5" fill="#fff" stroke="#111"/><circle cx="56" cy="92" r="3" fill="#fff" stroke="#111"/>',R),
 mean='The king said: I have lost my kingdom, and yet I still feel “mine” for every part of it. I know better, yet I am like one who does not know. What is this, O best of sages?',
 plain='I know it’s gone, and I know clinging is foolish. So why does my heart still say “mine”?',
 words=[('mamatvam','<b>“mine-ness”</b>, possessiveness'),('gata-rājyasya','<b>of one whose kingdom is gone</b>'),('rājya-aṅgeṣu','<b>in the parts of the kingdom</b>'),('jānataḥ api yathā ajñasya','<b>knowing, yet like one who doesn’t</b>'),('muni-sattama','<b>O best of sages</b>')],
 point='<b>The question of the whole book.</b> Knowing and letting go are not the same thing. The king knows his attachment is useless, and it still holds him. The merchant feels the same about the family who threw him out. The Devī Māhātmya is the sage’s answer.',
 key='<b>Knowing is not the same as letting go.</b> Why?'),
dict(n='55',lab='ŚLOKA 1.55 · EVEN THE WISE',lines=[['jñāninām api cetāṃsi','devī bhagavatī hi sā |'],['balād ākṛṣya mohāya','mahāmāyā prayacchati ‖55‖']],theme='MAHĀMĀYĀ',
 svg=svg('A great hand of light pulling the minds of wise men, shown as small glowing lamps, into a swirling cloud',
  '<path d="M110 90 m-60 0 a60 30 0 1 0 120 0 a60 30 0 1 0 -120 0" fill="#efe6ff" stroke="#9b5de5" stroke-width="3"/><path d="M80 90 q30 -30 60 0 q-30 20 -50 0" fill="none" stroke="#9b5de5" stroke-width="2"/>'+''.join(f'<path d="M{30+k*40} 30 q0 -8 6 -12 q6 4 6 12z" fill="#ffd60a" stroke="#111"/><path d="M{36+k*40} 34 q{70-k*40} 30 {74-k*40} 50" fill="none" stroke="#e0a800" stroke-width="2" stroke-dasharray="3 3"/>' for k in range(5))+T(110,150,'MAHĀMĀYĀ',13),R),
 mean='For she, the Devī, the Bhagavatī, Mahāmāyā, forcibly draws even the minds of the wise and casts them into delusion.',
 plain='The great power of illusion pulls even wise minds into confusion. That is who she is.',
 words=[('jñāninām api','<b>even of the wise</b>'),('cetāṃsi','<b>minds</b>'),('balāt ākṛṣya','<b>dragging by force</b>'),('mohāya prayacchati','<b>hands over to delusion</b>'),('mahā-māyā','<b>the Great Illusion</b>')],
 point='<b>The most famous verse of chapter 1.</b> Medhas’s answer is startling: the same Goddess they will learn to worship is the one who binds them. Attachment is not a personal failing to be ashamed of; it is a cosmic power. And so only her grace can release it.',
 key='The power that binds even the wise <b>is the Goddess herself</b>.'),
dict(n='56',lab='ŚLOKA 1.56 · CREATOR AND LIBERATOR',lines=[['tayā visṛjyate viśvaṃ','jagad etac carācaram |'],['saiṣā prasannā varadā','nṛṇāṃ bhavati muktaye ‖56‖']],theme='PLEASED, SHE FREES US',
 svg=svg('On the left the Goddess creating the world, stars and animals spilling from her hands; on the right she smiles and opens a cage, freeing a bird',
  DEVI(70,10,.6,False)+''.join(f'<circle cx="{20+k*14}" cy="{120+(k%2)*10}" r="4" fill="#2a9d6f" stroke="#111"/>' for k in range(6))+'<path d="M140 60 h50 v60 h-50z" fill="none" stroke="#111" stroke-width="2"/><path d="M190 60 l14 -10" stroke="#111" stroke-width="2"/><path d="M196 40 q8 -8 16 0 q-8 4 -16 0z" fill="#4aa3df" stroke="#111"/>'+T(166,140,'MUKTI',12),R),
 mean='By her this whole universe, moving and unmoving, is created. And she, when pleased, becomes the giver of boons, for the liberation of human beings.',
 plain='She makes the whole world, living and non-living. And when she is pleased, she grants us freedom.',
 words=[('tayā visṛjyate','<b>by her is created</b>'),('cara-acaram','<b>moving and unmoving</b>'),('prasannā','<b>pleased</b>, gracious'),('varadā','<b>giver of boons</b>'),('muktaye','<b>for liberation</b>')],
 point='<b>The same hand.</b> The power that creates the world and binds the mind is the one that frees it. That is why the sage tells them to turn to her: the way out of māyā runs through Mahāmāyā herself.',
 key='She who binds, <b>when pleased, sets us free</b>.'),
dict(n='57–58',lab='ŚLOKAS 1.57–58 · BOTH KNOT AND RELEASE',lines=[['sā vidyā paramā mukter','hetubhūtā sanātanī |'],['saṃsārabandhahetuś ca','saiva sarveśvareśvarī ‖57–58‖']],theme='KNOWLEDGE AND BONDAGE',
 svg=svg('The Goddess holding a rope in one hand and a lamp of knowledge in the other',DEVI(110,0,.85,False)+'<path d="M60 70 q-20 20 0 40 q20 20 0 40" fill="none" stroke="#c9a26b" stroke-width="5"/><path d="M160 80 h20 l-4 10 h-12z" fill="#e0a800" stroke="#111" stroke-width="2"/><path d="M170 78 q-8 -14 0 -24 q8 10 0 24z" fill="#ffd60a" stroke="#111"/>'+T(50,30,'BANDHA',11)+T(176,40,'VIDYĀ',11),R),
 mean='She is the supreme knowledge, eternal, the cause of liberation; and she alone is the cause of the bondage of worldly life. She is the queen of all queens.',
 plain='She is the highest wisdom that frees us, and also what ties us to the world. She rules over everything.',
 words=[('vidyā paramā','<b>the supreme knowledge</b>'),('mukteḥ hetu-bhūtā','<b>the cause of liberation</b>'),('saṃsāra-bandha-hetuḥ','<b>the cause of worldly bondage</b>'),('sarva-īśvara-īśvarī','<b>ruler of all rulers</b>')],
 point='<b>Not two powers, one.</b> Many traditions picture bondage and liberation as enemies. Here both are the Goddess: <i>avidyā</i> that ties, <i>vidyā</i> that frees. The difference is whether she is <i>prasannā</i>, pleased.',
 key='One Goddess is <b>both the knot and the release</b>.'),
dict(n='60',lab='ŚLOKA 1.60 · WHO IS SHE?',lines=[['bhagavan kā hi sā devī','mahāmāyeti yāṃ bhavān |'],['bravīti katham utpannā','sā karmāsyāś ca kiṃ dvija ‖60‖']],theme='THE KING ASKS',
 svg=svg('The king leaning forward eagerly to the sage, three question marks above him',SAGE(160,150,1.2)+KING(60,150,1.1)+''.join(T(40+k*22,40+(k%2)*10,'?',22,'#c0392b') for k in range(3)),R),
 mean='The king said: Lord, who is this Devī whom you call Mahāmāyā? How did she arise? And what are her deeds, O brahmin?',
 plain='Who is she? Where did she come from? What has she done?',
 words=[('kā hi sā devī','<b>who is that Goddess?</b>'),('katham utpannā','<b>how did she arise?</b>'),('karma asyāḥ kim','<b>what are her deeds?</b>'),('dvija','<b>O twice-born</b>: O brahmin')],
 point='<b>Three questions, three stories.</b> “Who is she, how did she arise, what has she done?” The rest of the Devī Māhātmya answers in three great episodes: Madhu and Kaiṭabha, Mahiṣāsura, and Śumbha and Niśumbha.',
 key='The rest of the book answers <b>one question: who is she?</b>'),
dict(n='64–66',lab='ŚLOKAS 1.64–66 · ETERNAL, YET SHE COMES',lines=[['nityaiva sā jaganmūrtis','tayā sarvam idaṃ tatam |'],['tathāpi tatsamutpattir','bahudhā śrūyatāṃ mama ‖64–65‖'],['devānāṃ kāryasiddhyartham','āvirbhavati sā yadā |'],['utpanneti tadā loke','sā nityāpy abhidhīyate ‖66‖']],theme='SHE APPEARS FOR THE GODS',
 svg=svg('The Goddess as a vast starry figure containing the world, and a small bright form of her stepping out to help the gods',
  '<rect width="220" height="160" fill="#2b2140"/>'+STARS(14,3)+DEVI(80,0,.95,False,'#3a2a6a')+'<circle cx="80" cy="96" r="16" fill="#2a9d6f" stroke="#111"/><circle cx="170" cy="96" r="40" fill="#ffd60a" opacity=".35" stroke="none"/>'+DEVI(170,40,.45)+crowd(['#fff','#ffd60a'],150,30,156,.35),R),
 mean='The sage said: She is eternal; the world is her form; all this is pervaded by her. Even so, hear from me how she arises in many ways. Whenever she manifests to accomplish the purpose of the gods, then, though eternal, she is said in the world to be “born”.',
 words=[('nityā','<b>eternal</b>'),('jagat-mūrtiḥ','<b>whose form is the world</b>'),('āvirbhavati','<b>she manifests</b>'),('deva-kārya-siddhi','<b>to fulfil the gods’ purpose</b>'),('utpannā iti abhidhīyate','<b>she is said to be “born”</b>')],
 point='<b>Never born, always arriving.</b> She was never created; she <i>is</i> the world. But whenever goodness is in trouble she “appears”, and we call that her birth. Like Kṛṣṇa’s promise in the Gītā (4.7–8), she comes when she is needed. The first such coming is Part 6.',
 key='Eternal, she still <b>comes whenever she is needed</b>.'),
]
full=''.join(fp(v['lab'].split(' · ')[0].replace('ŚLOKAS ','').replace('ŚLOKA ',''),v['lines']) for v in V)
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A king on horseback and a merchant on foot arriving at a forest hermitage where a sage sits under a tree among peaceful deer and tigers">'
 '<rect width="380" height="268" fill="#2a5a3a" rx="8"/><rect y="180" width="380" height="88" fill="#3a7a4a"/>'
 +TREE(300,180,1.6)+TREE(40,170,1.2)+SAGE(300,226,1.4)+DEER(220,224,1)+TIGER(240,250,1)
 +HORSE(110,224,1.4)+KING(110,198,1.2)+MERCH(180,244,1.1)+SUN(60,40,18)+'</svg>')
nest=('<svg class="fig" style="border:3px solid var(--ink);background:#fff8ec;max-width:100%" width="460" height="230" viewBox="0 0 460 230" role="img" aria-label="Nested boxes: Markandeya tells the story; inside it the sage Medhas speaks to the king and the merchant; inside that, the three deeds of the Goddess">'
 '<rect x="8" y="8" width="444" height="214" fill="#fde4e4" stroke="#111" stroke-width="3"/><text x="20" y="30" font-family="Bangers" font-size="15">MĀRKAṆḌEYA TELLS HOW SĀVARṆI BECAME MANU</text>'
 '<rect x="26" y="42" width="408" height="166" fill="#fff3b0" stroke="#111" stroke-width="3"/><text x="38" y="64" font-family="Bangers" font-size="14">THE SAGE MEDHAS TEACHES THE KING AND THE MERCHANT</text>'
 +''.join(f'<rect x="{44+k*130}" y="78" width="118" height="116" fill="{c}" stroke="#111" stroke-width="3"/><text x="{103+k*130}" y="100" text-anchor="middle" font-family="Bangers" font-size="13">{a}</text><text x="{103+k*130}" y="120" text-anchor="middle" font-family="Bangers" font-size="11">{b}</text><text x="{103+k*130}" y="140" text-anchor="middle" font-family="Bangers" font-size="11" fill="#c0392b">{c2}</text><text x="{103+k*130}" y="160" text-anchor="middle" font-family="Bangers" font-size="11">{d}</text>' for k,(c,a,b,c2,d) in enumerate([('#efe6ff','PRATHAMA','CHAPTER 1','MAHĀKĀLĪ','MADHU · KAIṬABHA'),('#ffe3c4','MADHYAMA','CHAPTERS 2–4','MAHĀLAKṢMĪ','MAHIṢĀSURA'),('#e7f4ea','UTTAMA','CHAPTERS 5–13','MAHĀSARASVATĪ','ŚUMBHA · NIŚUMBHA')]))+'</svg>')
s1=storypage('king','A KING LOSES EVERYTHING','Ślokas 1.4–16',
 panels('Three panels: King Suratha defeated in battle; his own ministers carrying off his treasury; the king riding alone into the forest',[
  ('#ffe3c4','DEFEATED',KING(50,150,1)+person(100,150,'#333','#7a6a5a',.9)+'<path d="M70 110 l20 -20 M84 110 l-14 -20" stroke="#ccc" stroke-width="3"/>'),
  ('#dfe9f6','BETRAYED',person(40,150,'#3b6fd0','#c98b5a',.8)+person(100,150,'#3b6fd0','#c98b5a',.8)+'<rect x="56" y="110" width="30" height="20" fill="#e0a800" stroke="#111" stroke-width="2"/>'),
  ('#e7f4ea','INTO THE FOREST',TREE(30,160,1)+TREE(120,160,1)+HORSE(76,150,1)+KING(76,124,.8))]),
 ['<b>A good king.</b> Long ago, in the age of the Manu Svārociṣa, King Suratha of the Caitra line ruled the whole earth and cared for his people like his own children.',
  '<b>Defeat.</b> Enemy kings attacked and defeated him. He retreated to his own city, reduced to ruling just that.',
  '<b>Betrayal.</b> There, his own powerful, corrupt ministers seized his army and his treasury. He had nothing left.',
  '<b>Into the forest.</b> Alone, on the pretext of hunting, the king rode into a deep forest and came to the hermitage of the sage <b>Medhas</b>, where wild animals lived in peace.',
  '<b>Still worrying.</b> Even there, he could not stop thinking: “Is my city safe? Are my elephants fed? Will those ministers waste my treasure?”'],
 ("He lost everything and he's still worrying about the elephants?","That's the point! His kingdom is gone, but his mind is still in the palace. Remember that for śloka 42."),
 'He lost his kingdom; <b>his mind did not leave it</b>.')
s2=storypage('merchant','A MERCHANT THROWN OUT','Ślokas 1.17–41',
 panels('Three panels: a merchant’s greedy wife and sons pushing him out of his house; the merchant sitting sadly in the forest; the king and the merchant meeting and talking',[
  ('#fff3b0','THROWN OUT','<rect x="70" y="60" width="66" height="90" fill="#e0a800" stroke="#111" stroke-width="2"/>'+person(100,150,'#e05a8a','#c98b5a',.8)+person(120,150,'#3b6fd0','#c98b5a',.7)+MERCH(40,150,1)),
  ('#e7f4ea','STILL WORRYING',TREE(110,160,1)+MERCH(60,150,1)+'<ellipse cx="80" cy="50" rx="40" ry="20" fill="#fff" stroke="#111" stroke-width="2"/>'+person(70,60,'#e05a8a','#c98b5a',.4)+person(92,60,'#3b6fd0','#c98b5a',.4)),
  ('#fde4e4','TWO FRIENDS',KING(50,150,1)+MERCH(100,150,1)+'<path d="M64 80 q14 -14 26 0" fill="none" stroke="#111" stroke-width="2"/>')]),
 ['<b>Another exile.</b> In the forest the king meets a man of the vaiśya (merchant) class, named <b>Samādhi</b>.',
  '<b>Thrown out by his own.</b> His wife and sons, greedy for wealth, had taken his money and driven him from his home.',
  '<b>And yet he worries.</b> “Are my wife and sons well? Are they happy, or in trouble?” He cannot stop loving those who threw him out.',
  '<b>Puzzled.</b> “Why does my mind run towards those who have no love for me?” he asks. “I know their faults, and still my heart goes to them.”',
  '<b>Together to the sage.</b> The two exiles go to Medhas and the king puts their shared question to him.'],
 ("Why would he still care about them?","Exactly the question! The king clings to a kingdom, the merchant to a family. Two stories, one puzzle."),
 'Wronged by those he loved, <b>he still loves them</b>.')
s3=storypage('answer','THE SAGE ANSWERS','Ślokas 1.43–54',
 panels('Three panels: a hungry mother bird feeding its chicks; a person dreaming of children who will care for them in old age; a whirlpool pulling people round',[
  ('#e7f4ea','BIRDS',TREE(110,170,1.1)+'<path d="M40 110 q20 -14 40 0 q-20 -4 -40 0z" fill="#ff8c1a" stroke="#111"/>'+''.join(f'<circle cx="{40+k*14}" cy="124" r="6" fill="#ffd60a" stroke="#111"/>' for k in range(3))),
  ('#fff3b0','HOPES',person(70,150,'#3b6fd0','#c98b5a',1)+'<ellipse cx="80" cy="56" rx="44" ry="24" fill="#fff" stroke="#111" stroke-width="2"/>'+person(70,70,'#ffd60a','#c98b5a',.4)+person(92,70,'#e05a8a','#c98b5a',.4)),
  ('#efe6ff','THE WHIRLPOOL','<path d="M72 100 m-50 0 a50 30 0 1 0 100 0 a50 30 0 1 0 -100 0 M52 100 a20 12 0 1 0 40 0 a20 12 0 1 0 -40 0" fill="none" stroke="#9b5de5" stroke-width="4"/>'+person(40,90,'#c0392b','#c98b5a',.4)+person(110,104,'#ffd60a','#c98b5a',.4))]),
 ['<b>Everyone knows things.</b> Medhas says: all creatures have knowledge of the world. Animals know too; some see by day, some by night.',
  '<b>Look at the birds.</b> Though hungry themselves, birds put grain into the beaks of their young, out of pure attachment.',
  '<b>Look at people.</b> Humans long for children, hoping to be cared for in return. Knowing is not enough to free anyone.',
  '<b>The whirlpool.</b> So beings are thrown into the whirlpool of attachment, the pit of delusion, by the power of Mahāmāyā.',
  '<b>Do not be surprised.</b> She is Viṣṇu’s yoganidrā, the power that keeps the world spinning. And then comes the great verse.'],
 ("So even animals have this problem?","Yes. That's why Medhas isn't scolding them. Attachment isn't a personal failing; it's built into the world. Now meet the one who built it."),
 'Attachment is not a flaw; <b>it is the power that turns the world</b>.')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 5 OF 19</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,76px)">THE KING, THE MERCHANT<br>AND THE SAGE</h1>
  <div class="series">DEVĪ MĀHĀTMYA · PART 5 · CHAPTER 1, THE FRAME</div>
  <div class="tag">Why can’t we let go? · explained and illustrated</div>
  {cover}
  {CAST}
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> The Devī Māhātmya is a story, so this part tells it in <b>comic panels</b>, with the <b>key verses</b> in full on their own pages: the chant, a picture, what it says, the key words, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">WHERE WE ARE</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    <p>The three limbs are done: armour on (<a href="/bhakti/devi/devi-mahatmya/part-1/">Kavacam</a>), bolt lifted (<a href="/bhakti/devi/devi-mahatmya/part-3/">Argalā</a>), pin out (<a href="/bhakti/devi/devi-mahatmya/part-4/">Kīlakam</a>). Now the book itself opens. (Many traditions also chant other preparatory hymns here; practice varies.)</p>
    <p>It begins not with a goddess but with two broken men: a king whose ministers stole his kingdom, and a merchant whose family stole his wealth. Both have lost everything. Both still cannot stop caring about what they lost.</p>
    <p>Their question, “why can’t I let go?”, is the door into the whole Devī Māhātmya.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--red)">With the blessings of the Devī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Where are the battles?","Patience! First the question. Every battle in this book is the sage's answer to it.")}
</section>

<section class="page" id="map">
  <h2 class="page-title">A STORY INSIDE A STORY</h2>
  <div class="sub">How the Devī Māhātmya is built</div>
  {nest}
  <div class="panel reading pt"><p>The Devī Māhātmya is chapters 81–93 of the Mārkaṇḍeya Purāṇa. The sage Mārkaṇḍeya tells how a king became the eighth Manu. Inside his story, the sage Medhas tells the king about the Goddess, in <b>three episodes (caritas)</b>, each with a different form of the Devī. This part covers the outer frame, chapter 1 up to śloka 66.</p></div>
  <div class="note">Śloka numbers follow the aurobharati edition (104 ślokas in chapter 1). Editions number them slightly differently.</div>
</section>

<section class="page" id="full">
  <h2 class="page-title">THE KEY VERSES IN ONE GO</h2>
  <div class="sub">Seven passages from chapter 1, ślokas 2–66</div>
  <div class="full">{full}</div>
  <div class="note">Text checked word by word against devimahatmyam.aurobharati.in. The full chapter has 104 ślokas; this part tells ślokas 1–66 as story, with these passages in full.</div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">←</span><a href="#foreword">Where We Are</a></li>
    <li><span class="num">▣</span><a href="#map">A Story Inside a Story</a></li>
    <li><span class="num">🔤</span><a href="#full">The Key Verses</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    <li class="part">THE STORY · CHAPTER 1, ŚLOKAS 1–66</li>
    <li><span class="num">2</span><a href="#v2–3">The Eighth Manu</a></li>
    <li><span class="num">★</span><a href="#king">A King Loses Everything</a></li>
    <li><span class="num">★</span><a href="#merchant">A Merchant Thrown Out</a></li>
    <li><span class="num">42</span><a href="#v42">Why Can’t I Let Go?</a></li>
    <li><span class="num">★</span><a href="#answer">The Sage Answers</a></li>
    <li><span class="num">55</span><a href="#v55">Mahāmāyā</a></li>
    <li><span class="num">56</span><a href="#v56">Pleased, She Frees Us</a></li>
    <li><span class="num">57</span><a href="#v57–58">Knowledge and Bondage</a></li>
    <li><span class="num">60</span><a href="#v60">Who Is She?</a></li>
    <li><span class="num">64</span><a href="#v64–66">She Appears for the Gods</a></li>
  </ul>
</section>
''']
def vp(v):
    h=vpage(v)
    if len(v['lines'])>=4: h=h.replace(f'<section class="page" id="v{v["n"]}">',f'<section class="page long" id="v{v["n"]}">',1)
    return h
b+= [vp(V[0]),s1,s2,vp(V[1]),s3]+[vp(v) for v in V[2:]]
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 5 ON ONE PAGE</h2>
  <div class="sub">Chapter 1, ślokas 1–66, in five lines</div>
  <div class="steps">
    <div><b>The promise.</b> Mārkaṇḍeya will tell how a king became Sāvarṇi, the eighth Manu, by Mahāmāyā’s power.</div>
    <div><b>Two exiles.</b> King Suratha, robbed by his ministers, and the merchant Samādhi, thrown out by his family, meet at the sage Medhas’s hermitage.</div>
    <div><b>The question.</b> “I know it is gone; why do I still feel it is mine?”</div>
    <div><b>The answer.</b> Mahāmāyā drags even the wise into delusion; she creates the world, binds it, and when pleased, frees it.</div>
    <div><b>Who is she?</b> Eternal, the world is her form; yet she appears whenever the gods need her. Here is the first time.</div>
  </div>
  {talk("How does it end for the king and the merchant?","Spoiler for chapter 13: the king gets his kingdom back and a future as Manu. The merchant asks for something else entirely. Wait and see!")}
  <div class="key">Part 5: <b>the power that binds us is the one who frees us</b>. 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Devī Māhātmya, chapter 1, ślokas 1–66 (Mārkaṇḍeya Purāṇa). The story is retold in our words; the seven passages quoted in full were checked word by word against devimahatmyam.aurobharati.in, whose numbering (104 ślokas in chapter 1) is followed. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('/home/claude/work/devim/Devi_Mahatmya_Part05.html','w').write(head+''.join(b)+tail())
print('ok')
