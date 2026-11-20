import re,sys,math
sys.path.insert(0,'/home/claude/work/purusha')
from pdata import talk,svg,person,F,SUN,lab,crowd,MOON,STARS,FIRE
R='#fde4e4'
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
_css,_rest=head[:head.find('</style>')],head[head.find('</style>'):]
for _a,_b in [('#1d6fb8','#c0392b'),('#1d4f9a','#a02a1f'),('#0b2a4a','#3a1414'),('#2c5f9e','#d9822b'),('#dfe9f6','#fde4e4'),('#e3f2fd','#fdecea'),('#8fd0f5','#ffd27a'),('#0b3d6e','#6e1a0b'),('#5b6f8a','#8a5b5b'),('#04101f','#1f0604')]: _css=_css.replace(_a,_b)
head=_css+_rest
head=re.sub(r'<title>.*?</title>','<title>Yā Devī Sarvabhūteṣu · The Aparājitā Stuti · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Yā devī sarvabhūteṣu: the gods’ hymn from Devī Māhātmya chapter 5, all 28 verses and the 21 forms in which the Goddess dwells in every being, explained in plain English with illustrations.">',head)
head=head.replace('</style>','''  .iast .cl2{padding-left:2.2em}
  .full .ln2{padding-left:2.2em}
  .full p{margin:0 0 6px}
  .pt{font-size:14.5px;line-height:1.45;margin:8px 0}
  .toc.tight{gap:5px;grid-template-columns:repeat(3,1fr)}.toc.tight li{padding:3px 8px;font-size:13px}.toc.tight .part{font-size:16px}
  .vfig svg{max-height:150px;width:auto}
  .form{display:grid;grid-template-columns:120px 1fr;gap:10px;align-items:center;border:3px solid var(--ink);background:#fff;padding:8px;margin:8px 0;box-shadow:4px 4px 0 var(--ink)}
  .form svg{width:120px;height:auto;display:block}
  .form h4{margin:0 0 2px;font-family:Bangers,Impact,sans-serif;letter-spacing:1px;font-size:20px;color:var(--red)}
  .form .ln{font-style:italic;font-size:14px;margin:0 0 4px}
  .form p{margin:0;font-size:14px;line-height:1.4}
  .refrain{text-align:center;font-style:italic;font-weight:bold;margin:4px 0 0}
  @media(max-width:720px){.iast .cl2{padding-left:1.4em}.full .ln2{padding-left:1.4em}.form{grid-template-columns:90px 1fr}.form svg{width:90px}}
</style>''',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
FOLLOW='<div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>'

def DEVI(x=110,y=0,s=1,arms=True):
    a=('<path d="M-24 76 q-30 -6 -42 -30" fill="none" stroke="#f2c79b" stroke-width="7"/><path d="M24 76 q30 -6 42 -30" fill="none" stroke="#f2c79b" stroke-width="7"/>'
       '<path d="M-24 92 q-34 4 -46 22" fill="none" stroke="#f2c79b" stroke-width="7"/><path d="M24 92 q34 4 46 22" fill="none" stroke="#f2c79b" stroke-width="7"/>'
       '<path d="M-66 46 v-26" stroke="#7a5a3a" stroke-width="3"/><path d="M-72 22 l6 -12 l6 12 M-66 10 v-6" stroke="#ccc" stroke-width="3" fill="none"/>'
       '<circle cx="70" cy="114" r="8" fill="#fff" stroke="#111" stroke-width="2"/><path d="M66 46 l0 0" />'
       '<path d="M60 40 h14" stroke="#111" stroke-width="2"/><circle cx="66" cy="40" r="9" fill="none" stroke="#e0a800" stroke-width="4"/>') if arms else ''
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2">'+a+
     '<path d="M-14 26 h28 l-4 -18 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#ffd60a"/>'
     '<path d="M-17 36 q-6 30 4 40 M17 36 q6 30 -4 40" fill="#151515"/>'
     '<circle cy="42" r="15" fill="#f2c79b"/><circle cy="36" r="2" fill="#c0392b" stroke="none"/>'
     '<path d="M-30 150 q-6 -70 30 -88 q36 18 30 88z" fill="#c0392b"/><path d="M-26 110 q26 -16 52 0" fill="none" stroke="#ffd60a" stroke-width="4"/></g>')
LION=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-30" y="-14" width="56" height="26" rx="12" fill="#e0a800"/><circle cx="32" cy="-14" r="15" fill="#c46a1a"/><circle cx="34" cy="-14" r="9" fill="#e0a800"/><path d="M-30 -6 q-14 -6 -12 -20" fill="none"/></g>'
HILLS='<path d="M0 120 L40 70 L70 96 L110 50 L150 92 L180 64 L220 104 V160 H0Z" fill="#dfe9f6" stroke="#111" stroke-width="2"/><path d="M100 62 l10 -12 l10 12 M170 74 l10 -10 l8 10" stroke="#fff" stroke-width="4" fill="none"/>'
def ico(inner,bg='#fff'): return f'<svg viewBox="0 0 120 90" role="img" aria-hidden="true"><rect width="120" height="90" fill="{bg}"/>{inner}</svg>'
T=lambda x,y,t,s=12,c='#111': f'<text x="{x}" y="{y}" text-anchor="middle" {F} font-size="{s}" fill="{c}">{t}</text>'

# ---------------- the five opening verses ----------------
O=[
dict(n='1',lines=[['namo devyai mahādevyai','śivāyai satataṃ namaḥ |'],['namaḥ prakṛtyai bhadrāyai','niyatāḥ praṇatāḥ sma tām ‖1‖']],theme='SALUTATIONS TO THE GREAT GODDESS',
 svg=svg('Gods with folded hands bowing before the radiant Goddess on a Himalayan peak',HILLS+'<circle cx="110" cy="58" r="44" fill="#ffd60a" opacity=".45" stroke="none"/>'+DEVI(110,4,.62)+crowd(['#ffd60a','#fff','#3b6fd0','#ff8c1a'],22,22,148,.5)+crowd(['#2a9d6f','#fff','#ffd60a'],160,22,148,.5),R),
 mean='Salutations to the Devī, to the Great Devī, to the auspicious one, always salutations. Salutations to Prakṛti, to the gracious one: with minds controlled, we bow to her.',
 plain='We bow to the Goddess, the Great Goddess, the Kind One; to Nature herself, the Gracious One. With quiet minds, we bow.',
 words=[('devyai · mahādevyai','<b>to the Goddess</b> · <b>to the Great Goddess</b>'),('śivāyai','<b>to the auspicious one</b>'),('prakṛtyai','<b>to Prakṛti</b>: Nature, the source of all'),('bhadrāyai','<b>to the gracious, kind one</b>'),('niyatāḥ praṇatāḥ sma','<b>self-controlled, we have bowed</b>')],
 point='<b>She is Nature itself.</b> <i>Prakṛti</i> is the stuff of the world: matter, energy, mind. The gods begin by saluting the Goddess not as a distant queen but as the very nature of everything they see.',
 key='The first word of worship: <b>she is Nature herself</b>.'),
dict(n='2',lines=[['raudrāyai namo nityāyai','gauryai dhātryai namo namaḥ |'],['jyotsnāyai cendurūpiṇyai','sukhāyai satataṃ namaḥ ‖2‖']],theme='FIERCE AND GENTLE, MOON AND JOY',
 svg=svg('On one side a fierce red flame, on the other a gentle full moon with soft light, the Goddess between them','<rect width="220" height="160" fill="#2b2140"/>'+STARS(10,5)+FIRE(40,120,1)+'<circle cx="180" cy="50" r="22" fill="#fff8c0" stroke="#111" stroke-width="2"/><path d="M180 72 l-30 70 h60z" fill="#fff8c0" opacity=".25" stroke="none"/>'+DEVI(110,10,.55,False),R),
 mean='Salutations to the fierce one, to the eternal one; to Gaurī, to the sustainer, salutations again and again. To moonlight, to her whose form is the moon, to joy, always salutations.',
 plain='We bow to the Fierce One and the Eternal One, to fair Gaurī who holds up the world, to the cool moonlight, and to happiness itself.',
 words=[('raudrāyai','<b>to the fierce one</b>'),('nityāyai','<b>to the eternal one</b>'),('gauryai','<b>to Gaurī</b>, the fair one, Pārvatī'),('dhātryai','<b>to the sustainer</b>, the nurse of all'),('jyotsnāyai · indu-rūpiṇyai','<b>to moonlight</b> · <b>to her moon-form</b>'),('sukhāyai','<b>to joy</b>')],
 point='<b>Opposites in one breath.</b> Fierce (<i>raudrā</i>) and fair (<i>gaurī</i>), fire and moonlight: the hymn will keep holding opposites together. The Goddess is not only the pleasant half of life.',
 key='Fierce and gentle: <b>both are the Mother</b>.'),
dict(n='3',lines=[['kalyāṇyai praṇatāṃ vṛddhyai','siddhyai kurmo namo namaḥ |'],['nairṛtyai bhūbhṛtāṃ lakṣmyai','śarvāṇyai te namo namaḥ ‖3‖']],theme='FORTUNE AND MISFORTUNE',
 svg=svg('A balance scale: on one pan a golden crown and coins for fortune, on the other a broken pot for misfortune, the Goddess holding the beam',DEVI(110,0,.5,False)+'<path d="M40 86 H180" stroke="#111" stroke-width="4"/><path d="M110 76 v10" stroke="#111" stroke-width="4"/><path d="M40 86 l-18 30 h36z M180 86 l-18 30 h36z" fill="#fff" stroke="#111" stroke-width="2"/><path d="M28 112 h24 l-4 -10 l-4 4 l-4 -8 l-4 8 l-4 -4z" fill="#ffd60a" stroke="#111"/><path d="M168 112 q12 -16 24 0 l-6 -6 l-4 6 l-4 -8z" fill="#7a5a3a" stroke="#111"/>'+lab(40,140,'LAKṢMĪ',10)+lab(180,140,'NAIRṚTĪ',10),R),
 mean='To the auspicious one, to the growth of those who bow, to success, we offer salutations again and again. To Nairṛtī, to the fortune of kings, to Śarvāṇī: to you, salutations again and again.',
 plain='We bow to her as goodness, as growth for her devotees, as success; and as misfortune too, as the glory of kings, and as Śiva’s wife.',
 words=[('kalyāṇyai','<b>to the auspicious one</b>'),('praṇatāṃ vṛddhyai','<b>to the growth of those who bow</b>'),('siddhyai','<b>to success</b>'),('nairṛtyai','<b>to Nairṛtī</b>: decay, misfortune'),('bhūbhṛtāṃ lakṣmyai','<b>to the fortune of kings</b>'),('śarvāṇyai','<b>to Śarvāṇī</b>, wife of Śiva')],
 point='<b>Good luck and bad.</b> Lakṣmī is fortune; <i>Nairṛtī</i> is her opposite, the power of decline. The gods bow to both in one line. Whatever comes, prosperity or loss, comes through the same Mother.',
 key='Fortune and misfortune <b>both come from her hand</b>.',
 note='shlokam.org reads praṇatā for praṇatāṃ.'),
dict(n='4',lines=[['durgāyai durgapārāyai','sārāyai sarvakāriṇyai |'],['khyātyai tathaiva kṛṣṇāyai','dhūmrāyai satataṃ namaḥ ‖4‖']],theme='DURGĀ, WHO CARRIES US ACROSS',
 svg=svg('The Goddess on her lion carrying a small boat of people across a stormy river to the far shore',
  '<path d="M0 100 q55 -14 110 0 t110 0 V160 H0z" fill="#4aa3df" stroke="#111" stroke-width="2"/><path d="M50 118 h70 l-10 14 h-50z" fill="#c9a26b" stroke="#111" stroke-width="2"/>'+crowd(['#ff8c1a','#fff','#2a9d6f'],66,18,116,.35)+LION(170,96,.6)+DEVI(170,10,.42,False)+lab(40,30,'DURGA-PĀRĀ',11),R),
 mean='To Durgā, to her who carries us across difficulties, to the essence, to the cause of all; to fame, and to the dark one, to the smoky one, always salutations.',
 plain='We bow to Durgā, who ferries us across every hardship; the essence and maker of all; renowned, dark, smoke-coloured.',
 words=[('durgāyai','<b>to Durgā</b>: the hard-to-reach fortress'),('durga-pārāyai','<b>to her who takes us across hardship</b>'),('sārāyai','<b>to the essence</b>'),('sarva-kāriṇyai','<b>to the cause of all</b>'),('khyātyai','<b>to fame</b>, renown'),('kṛṣṇāyai · dhūmrāyai','<b>to the dark one</b> · <b>the smoky one</b>')],
 point='<b>The name Durgā.</b> <i>Durga</i> means a place hard to reach, a fortress, a difficulty. She is the fortress no one can take, and also the one who carries us through what is hard: <i>durga-pārā</i>, the “ferry across difficulty”.',
 key='Durgā: <b>the fortress, and the ferry across</b>.'),
dict(n='5',lines=[['atisaumyātiraudrāyai','natās tasyai namo namaḥ |'],['namo jagatpratiṣṭhāyai','devyai kṛtyai namo namaḥ ‖5‖']],theme='MOST GENTLE, MOST FIERCE',
 svg=svg('The Goddess shown half gentle with a lotus and half fierce with a sword, standing on the globe of the world',
  '<circle cx="110" cy="138" r="26" fill="#2a9d6f" stroke="#111" stroke-width="2"/><rect x="0" y="0" width="110" height="112" fill="#fde4ec"/><rect x="110" y="0" width="110" height="112" fill="#3a1a1a"/>'+DEVI(110,0,.62,False)+'<path d="M58 40 q-8 -14 0 -22 q8 8 0 22z" fill="#f08aa6" stroke="#111" stroke-width="2"/><path d="M164 70 l16 -50" stroke="#ccc" stroke-width="5"/>'+T(50,104,'SAUMYĀ',11)+T(170,104,'RAUDRĀ',11,'#fff'),R),
 mean='To her who is most gentle and most fierce, we bow, salutations again and again. Salutations to the support of the world, to the Devī who is action itself, salutations again and again.',
 plain='We bow to her who is the gentlest and the fiercest, who holds the world up, and who is every action.',
 words=[('ati-saumyā','<b>most gentle</b>'),('ati-raudrā','<b>most fierce</b>'),('natāḥ','<b>we have bowed</b>'),('jagat-pratiṣṭhā','<b>the foundation of the world</b>'),('kṛti','<b>action</b>, deed, creation')],
 point='<b>The whole hymn in one line.</b> <i>Ati-saumyā ati-raudrā</i>: the most gentle and the most fierce, at once. A mother is soft to her child and terrible to anything that threatens it. Next the gods name the 21 forms in which she lives in every being.',
 key='<b>Gentlest and fiercest</b>, at the same time.'),
]
# ---------------- the 21 forms ----------------
FORMS=[
('viṣṇumāyeti śabditā','VIṢṆUMĀYĀ','Viṣṇu’s māyā','Called <b>Viṣṇumāyā</b>: the power that makes the One appear as the many. In chapter 1 she even put Viṣṇu himself to sleep.',
 ico('<circle cx="60" cy="45" r="30" fill="#efe6ff" stroke="#111" stroke-width="2"/><path d="M30 45 q30 -30 60 0 q-30 30 -60 0z" fill="#fff" stroke="#111" stroke-width="2"/><circle cx="60" cy="45" r="9" fill="#3b6fd0" stroke="#111" stroke-width="2"/>'+''.join(f'<circle cx="{60+42*math.cos(k*1.05)}" cy="{45+34*math.sin(k*1.05)}" r="4" fill="#9b5de5"/>' for k in range(6)))),
('cetanety abhidhīyate','CETANĀ','consciousness','Called <b>consciousness</b>: the awareness by which you are reading this right now.',
 ico('<circle cx="60" cy="48" r="26" fill="#f2c79b" stroke="#111" stroke-width="2"/><circle cx="60" cy="40" r="8" fill="#ffd60a" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{60+12*math.cos(k*0.785):.0f} {40+12*math.sin(k*0.785):.0f} l{8*math.cos(k*0.785):.0f} {8*math.sin(k*0.785):.0f}" stroke="#e0a800" stroke-width="3"/>' for k in range(8)))),
('buddhirūpeṇa saṃsthitā','BUDDHI','intelligence','As <b>intelligence</b>: the power to understand, weigh and decide.',
 ico('<path d="M40 70 q-16 -10 -10 -30 q6 -22 30 -22 q26 0 32 22 q6 20 -12 30z" fill="#fde4ec" stroke="#111" stroke-width="2"/><path d="M60 20 v50 M44 40 q8 6 16 0 M60 50 q8 6 16 0" stroke="#111" stroke-width="2" fill="none"/><circle cx="96" cy="20" r="8" fill="#ffd60a" stroke="#111" stroke-width="2"/>')),
('nidrārūpeṇa saṃsthitā','NIDRĀ','sleep','As <b>sleep</b>: the rest that restores us each night. Even switching off is her.',
 ico('<rect width="120" height="90" fill="#2b2140"/><path d="M84 18 a14 14 0 1 0 0 28 a18 18 0 0 1 0 -28z" fill="#fff8c0"/><rect x="18" y="56" width="70" height="16" rx="6" fill="#bcd4f0" stroke="#111" stroke-width="2"/><circle cx="28" cy="52" r="8" fill="#f2c79b" stroke="#111" stroke-width="2"/>'+T(56,40,'Z z',14,'#fff'),'#2b2140')),
('kṣudhārūpeṇa saṃsthitā','KṢUDHĀ','hunger','As <b>hunger</b>: the drive that keeps every creature alive. That is why food is offered first to her.',
 ico('<ellipse cx="60" cy="62" rx="40" ry="14" fill="#c9a26b" stroke="#111" stroke-width="2"/><path d="M24 58 q36 -30 72 0" fill="#fff" stroke="#111" stroke-width="2"/><circle cx="48" cy="48" r="6" fill="#ffd60a" stroke="#111"/><circle cx="66" cy="44" r="6" fill="#2a9d6f" stroke="#111"/><path d="M50 20 q4 -8 0 -14 M64 20 q4 -8 0 -14" stroke="#999" stroke-width="2" fill="none"/>')),
('chāyārūpeṇa saṃsthitā','CHĀYĀ','shadow, shade','As <b>shadow</b>: the reflection of all things, and the shade that shelters the tired.',
 ico('<path d="M70 70 L84 30 L98 70z" fill="#2a7a4a" stroke="#111" stroke-width="2"/><path d="M84 70 v10" stroke="#7a5a3a" stroke-width="4"/><ellipse cx="56" cy="80" rx="40" ry="6" fill="#999" opacity=".6"/>'+SUN(22,20,10)+'<circle cx="52" cy="66" r="6" fill="#f2c79b" stroke="#111"/><path d="M46 80 q6 -14 12 0z" fill="#ff8c1a" stroke="#111"/>')),
('śaktirūpeṇa saṃsthitā','ŚAKTI','power','As <b>power</b>: the energy in every movement, every growing seed, every heartbeat.',
 ico('<path d="M66 8 L38 50 h18 L48 84 L84 36 H64z" fill="#ffd60a" stroke="#111" stroke-width="2.5"/>')),
('tṛṣṇārūpeṇa saṃsthitā','TṚṢṆĀ','thirst, desire','As <b>thirst</b> and desire. Even longing is her; what matters is where we turn it.',
 ico('<path d="M60 12 q-24 34 -24 50 a24 24 0 0 0 48 0 q0 -16 -24 -50z" fill="#4aa3df" stroke="#111" stroke-width="2.5"/><path d="M48 60 q4 12 14 12" stroke="#fff" stroke-width="3" fill="none"/>')),
('kṣāntirūpeṇa saṃsthitā','KṢĀNTI','patience','As <b>forbearance</b>: the strength to bear and forgive without hitting back.',
 ico('<path d="M0 70 h120" stroke="#111" stroke-width="2"/><path d="M60 70 v-40" stroke="#7a5a3a" stroke-width="6"/><circle cx="60" cy="30" r="22" fill="#2a9d6f" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{20+k*20} {10+(k%2)*6} l-6 14" stroke="#4aa3df" stroke-width="2"/>' for k in range(5)))),
('jātirūpeṇa saṃsthitā','JĀTI','birth, kind','As <b>birth</b>: the kind of life each being is born into, bird, fish, tree or human.',
 ico('<ellipse cx="34" cy="50" rx="16" ry="20" fill="#fff8ec" stroke="#111" stroke-width="2"/><path d="M60 70 v-26 q0 -10 10 -14 M60 50 q-10 -6 -14 -2" stroke="#2a7a4a" stroke-width="3" fill="none"/><path d="M80 60 q14 -12 28 0 q-14 12 -28 0z M108 60 l8 -6 v12z" fill="#4aa3df" stroke="#111" stroke-width="2"/>')),
('lajjārūpeṇa saṃsthitā','LAJJĀ','modesty','As <b>modesty</b>: the inner sense of shame that stops us before we do wrong.',
 ico('<circle cx="60" cy="44" r="22" fill="#f2c79b" stroke="#111" stroke-width="2"/><ellipse cx="48" cy="50" rx="6" ry="4" fill="#f08aa6"/><ellipse cx="72" cy="50" rx="6" ry="4" fill="#f08aa6"/><path d="M50 40 q4 -3 8 0 M62 40 q4 -3 8 0 M54 58 q6 4 12 0" stroke="#111" stroke-width="2" fill="none"/><path d="M36 30 q24 -30 48 0 l6 40 q-30 -20 -60 0z" fill="#c0392b" opacity=".8" stroke="#111" stroke-width="2"/>')),
('śāntirūpeṇa saṃsthitā','ŚĀNTI','peace','As <b>peace</b>: the stillness that remains when the storm inside settles.',
 ico('<path d="M0 60 q30 -4 60 0 t60 0 V90 H0z" fill="#9fd3f0" stroke="#111" stroke-width="2"/><path d="M48 52 q12 -24 24 0 q-12 -8 -24 0z" fill="#f08aa6" stroke="#111" stroke-width="2"/><path d="M40 56 q20 8 40 0" fill="#2a9d6f" stroke="#111" stroke-width="2"/>')),
('śraddhārūpeṇa saṃsthitā','ŚRADDHĀ','faith','As <b>faith</b>: the trust that lets us take the next step before we can see the end of the road.',
 ico('<path d="M40 76 q-4 -30 20 -40 q24 10 20 40z" fill="#ff8c1a" stroke="#111" stroke-width="2"/><circle cx="60" cy="28" r="10" fill="#f2c79b" stroke="#111" stroke-width="2"/><path d="M52 52 l8 -10 l8 10" fill="none" stroke="#111" stroke-width="2"/><path d="M60 4 v8 M76 10 l-6 6 M44 10 l6 6" stroke="#ffd60a" stroke-width="3"/>')),
('kāntirūpeṇa saṃsthitā','KĀNTI','radiance, beauty','As <b>radiance</b>: the glow of beauty in a face, a flower, a sunrise.',
 ico('<circle cx="60" cy="45" r="16" fill="#ffd60a" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{60+20*math.cos(k*0.524):.0f} {45+20*math.sin(k*0.524):.0f} l{10*math.cos(k*0.524):.0f} {10*math.sin(k*0.524):.0f}" stroke="#ff8c1a" stroke-width="3"/>' for k in range(12)))),
('lakṣmīrūpeṇa saṃsthitā','LAKṢMĪ','fortune','As <b>Lakṣmī</b>: prosperity, well-being, everything that makes a home flourish.',
 ico('<path d="M30 70 q30 14 60 0 l-6 -22 h-48z" fill="#e0a800" stroke="#111" stroke-width="2"/>'+''.join(f'<circle cx="{40+k*10}" cy="{44-(k%2)*4}" r="5" fill="#ffd60a" stroke="#111"/>' for k in range(5))+'<path d="M50 30 q10 -24 20 0 q-10 -6 -20 0z" fill="#f08aa6" stroke="#111" stroke-width="2"/>')),
('vṛttirūpeṇa saṃsthitā','VṚTTI','livelihood, activity','As <b>activity</b>: our work and livelihood, and the ceaseless movement of the mind.',
 ico('<circle cx="44" cy="46" r="20" fill="#ccc" stroke="#111" stroke-width="2"/><circle cx="44" cy="46" r="7" fill="#fff" stroke="#111" stroke-width="2"/><circle cx="82" cy="40" r="14" fill="#ffd60a" stroke="#111" stroke-width="2"/><circle cx="82" cy="40" r="5" fill="#fff" stroke="#111"/>')),
('smṛtirūpeṇa saṃsthitā','SMṚTI','memory','As <b>memory</b>: what we hold of the past, and the remembering of God.',
 ico('<rect x="26" y="20" width="68" height="50" fill="#fff3b0" stroke="#111" stroke-width="2"/><path d="M60 20 v50" stroke="#111"/><path d="M34 34 h20 M34 44 h20 M66 34 h20 M66 44 h20" stroke="#999" stroke-width="2"/><path d="M80 16 l6 16" stroke="#c0392b" stroke-width="4"/>')),
('dayārūpeṇa saṃsthitā','DAYĀ','compassion','As <b>compassion</b>: the urge to help when another suffers.',
 ico('<path d="M60 76 q-34 -22 -34 -42 a16 16 0 0 1 34 -6 a16 16 0 0 1 34 6 q0 20 -34 42z" fill="#e05a8a" stroke="#111" stroke-width="2.5"/>')),
('tuṣṭirūpeṇa saṃsthitā','TUṢṬI','contentment','As <b>contentment</b>: the quiet joy of “this is enough”.',
 ico('<circle cx="60" cy="45" r="28" fill="#ffd60a" stroke="#111" stroke-width="2.5"/><path d="M48 38 q4 -4 8 0 M64 38 q4 -4 8 0" stroke="#111" stroke-width="2.5" fill="none"/><path d="M46 52 q14 14 28 0" stroke="#111" stroke-width="2.5" fill="none"/>')),
('mātṛrūpeṇa saṃsthitā','MĀTṚ','mother','As the <b>mother</b>: in every mother, of every creature.',
 ico(person(56,74,'#c0392b','#f2c79b',.9)+'<circle cx="74" cy="56" r="7" fill="#f2c79b" stroke="#111" stroke-width="2"/><path d="M66 70 q8 -10 16 0z" fill="#ffd60a" stroke="#111" stroke-width="2"/>')),
('bhrāntirūpeṇa saṃsthitā','BHRĀNTI','error, confusion','As <b>error</b> and confusion. Even our mistakes happen within her: there is nowhere she is not.',
 ico('<path d="M20 80 q20 -60 40 -20 t40 -40" stroke="#111" stroke-width="3" fill="none" stroke-dasharray="5 4"/>'+T(36,30,'?',22,'#c0392b')+T(92,72,'?',22,'#c0392b')+T(64,46,'?',16,'#7a3fa0'))),
]
GROUPS=[('6–8','SHE IS IN ALL BEINGS AS…','The mind’s three powers','<b>Two names, then a pattern.</b> For the first two the gods say “she is <i>called</i>”: Viṣṇumāyā, consciousness. From buddhi on, the line becomes “she <i>dwells in the form of</i>…”. Nineteen times more.','Māyā, awareness, understanding: <b>the light of the mind is the Mother</b>.'),
 ('9–11','IN SLEEP, IN HUNGER, IN SHADOW','The body’s needs','<b>The ordinary is holy.</b> No grand qualities here: sleep, hunger, shade. The hymn finds the Goddess in what every animal shares.','Every night’s sleep and every meal: <b>she is there too</b>.'),
 ('12–14','POWER, DESIRE, PATIENCE','Energy and its use','<b>Thirst between power and patience.</b> Desire sits between energy and forbearance: the force that moves us, and the strength to hold it.','Power and patience: <b>both are her strength</b>.'),
 ('15–17','BIRTH, MODESTY, PEACE','How we live with others','<b>From birth to peace.</b> We are born into a kind; modesty keeps us decent among others; peace is where it leads.','She is in our birth, our conscience and our peace.'),
 ('18–20','FAITH, RADIANCE, FORTUNE','What makes life bright','<b>Lakṣmī among the forms.</b> The goddess of fortune is named as one form of the one Devī: in this hymn, every goddess is her.','Faith, beauty, prosperity: <b>gifts of one Mother</b>.'),
 ('21–23','WORK, MEMORY, COMPASSION','The mind at work','<b>Smṛti.</b> Memory also means remembering God. The gods are doing just that, in this hymn, in their hour of need.','Our work, our memory, our kindness: <b>all her forms</b>.'),
 ('24–26','CONTENTMENT, MOTHER, ERROR','The boldest ending','<b>Why end with error?</b> After the mother comes <i>bhrānti</i>, confusion. Nothing is outside the Goddess, not even our mistakes. That is the hymn’s most daring claim.','From the mother to our mistakes: <b>nothing is outside her</b>.')]
CL=[
dict(n='27',lines=[['indriyāṇām adhiṣṭhātrī','bhūtānāṃ cākhileṣu yā |'],['bhūteṣu satataṃ tasyai','vyāptyai devyai namo namaḥ ‖27‖']],theme='RULER OF THE SENSES',
 svg=svg('An eye, an ear, a nose, a tongue and a hand around the Goddess, each linked to her by a golden thread',DEVI(110,4,.55,False)+''.join(f'<path d="M110 70 L{x} {y}" stroke="#e0a800" stroke-width="2"/><circle cx="{x}" cy="{y}" r="14" fill="#fff" stroke="#111" stroke-width="2"/>'+T(x,y+5,t,11) for x,y,t in [(30,40,'EYE'),(190,40,'EAR'),(30,120,'NOSE'),(190,120,'HAND'),(110,148,'TONGUE')]),R),
 mean='She who presides over the senses of all beings, and who always pervades all beings: to her, the all-pervading Devī, salutations again and again.',
 plain='She rules every sense of every creature and fills them all. We bow to the Goddess who is everywhere.',
 words=[('indriyāṇām','<b>of the senses</b>'),('adhiṣṭhātrī','<b>presiding ruler</b>'),('akhileṣu bhūteṣu','<b>in all beings</b>'),('satatam','<b>always</b>'),('vyāptyai devyai','<b>to the all-pervading Goddess</b>')],
 point='<b>Inside every sense.</b> Seeing, hearing, tasting: none of it works on its own. The gods now sum up the 21 forms: she is the power behind every sense, and she fills every being.',
 key='Every sense works <b>by her power</b>.',
 note='Some editions read vyāptidevyai as one word.'),
dict(n='28',lines=[['citirūpeṇa yā kṛtsnam','etad vyāpya sthitā jagat |'],['namas tasyai namas tasyai','namas tasyai namo namaḥ ‖28‖']],theme='CONSCIOUSNESS FILLING THE WORLD',
 svg=svg('A golden light spreading from the Goddess to fill mountains, river, trees and people',
  '<circle cx="110" cy="70" r="90" fill="#ffd60a" opacity=".3" stroke="none"/><circle cx="110" cy="70" r="55" fill="#ffd60a" opacity=".35" stroke="none"/>'+HILLS.replace('#dfe9f6','#fff3b0')+DEVI(110,10,.5,False)+crowd(['#ff8c1a','#2a9d6f','#3b6fd0'],30,20,150,.4)+crowd(['#fff','#c0392b'],170,20,150,.4),R),
 mean='She who, in the form of consciousness, pervades this whole world and abides: salutations to her, salutations to her, salutations to her, salutations again and again.',
 plain='She fills the whole universe as pure consciousness. We bow to her, again and again.',
 words=[('citi-rūpeṇa','<b>in the form of consciousness</b>'),('kṛtsnam etad jagat','<b>this whole world</b>'),('vyāpya','<b>pervading</b>'),('sthitā','<b>abides</b>')],
 point='<b>From cetanā to citi.</b> The forms began with <i>cetanā</i>, consciousness in each being. They end with <i>citi</i>, consciousness filling the whole universe. What is in you is what is everywhere.',
 key='The awareness in you <b>fills the whole world</b>.'),
]
ALL=O+[None]+CL

def iast(lines): return '<div class="iast">'+''.join(f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>' for a,b in lines)+'</div>'
def fp(lab,lines):
    o=f'<p><span class="vn">{lab}</span>'
    for a,b in lines:
        b=re.sub(r'\s*‖(\w+)‖$',r'<span class="end">‖ \1 ‖</span>',b)
        o+=f'<span class="ln">{a}</span><span class="ln ln2">{b}</span>'
    return o+'</p>'
REF='namas tasyai namas tasyai namas tasyai namo namaḥ'
FF=[(f'VERSE {6+k}',[[f'yā devī sarvabhūteṣu {f[0]} |',f'{REF} ‖{6+k}‖']]) for k,f in enumerate(FORMS)]
full1=''.join(fp('VERSE '+v['n'],v['lines']) for v in O)+''.join(fp(l,x) for l,x in FF[:6])
full2=''.join(fp(l,x) for l,x in FF[6:])+''.join(fp('VERSE '+v['n'],v['lines']) for v in CL)

cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The radiant eight-armed Goddess on her lion on a Himalayan peak, with the gods bowing below and small symbols of her forms around her">'
 '<rect width="380" height="268" fill="#3a1414" rx="8"/><circle cx="190" cy="110" r="100" fill="#ffd60a" opacity=".25"/>'
 '<path d="M0 210 L70 130 L120 170 L190 100 L260 168 L310 128 L380 196 V268 H0Z" fill="#dfe9f6" stroke="#111" stroke-width="2"/>'
 +LION(190,196,1.1)+DEVI(190,2,1.05)
 +''.join(f'<text x="{190+160*math.cos(k*0.449-1.57):.0f}" y="{110+96*math.sin(k*0.449-1.57):.0f}" text-anchor="middle" font-size="16">{e}</text>' for k,e in enumerate('🌙😴🍚🌳⚡💧🙏✨🌸❤️🤱🌀🕯️📿'))
 +crowd(['#ffd60a','#fff','#3b6fd0','#ff8c1a'],40,26,258,.6)+crowd(['#2a9d6f','#fff','#ffd60a','#9b5de5'],262,26,258,.6)+'</svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: the demons Shumbha and Nishumbha seize heaven from the gods; the gods sing to the Goddess on the Himalaya; the Goddess Ambika emerges shining from Parvati’s body">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#3a1a1a','HEAVEN SEIZED'),('#dfe9f6','THE GODS SING'),('#fde4e4','AMBIKĀ APPEARS')]))
 +person(50,150,'#5a2a6a','#7a9a5a',1.1)+person(100,150,'#3a2a6a','#6a8a4a',1.1)+'<path d="M30 60 h40 l-6 -14 l-8 8 l-6 -12 l-6 12 l-8 -8z" fill="#ffd60a" stroke="#111" stroke-width="2"/>'
 +'<path d="M157 120 L190 70 L215 100 L240 60 L294 130 V182 H157Z" fill="#fff" stroke="#111" stroke-width="2"/>'+crowd(['#ffd60a','#fff','#3b6fd0','#ff8c1a','#2a9d6f'],172,26,170,.45)
 +'<circle cx="382" cy="90" r="48" fill="#ffd60a" opacity=".45"/>'+DEVI(382,24,.62,False)+person(342,170,'#2a2a5a','#3a3a6a',.7)+'</svg>')

b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">28 VERSES · 21 FORMS</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,76px)">YĀ DEVĪ<br>SARVABHŪTEṢU</h1>
  <div class="series">THE APARĀJITĀ STUTI · DEVĪ MĀHĀTMYA, CHAPTER 5</div>
  <div class="tag">The Goddess in every being · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First the whole hymn for chanting in one go. Then the story behind it, and <b>one page for each of the five opening verses</b>. The <b>21 forms</b> come three to a page, each with a picture and what it means. Last, the two closing verses.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    <p>“Yā devī sarvabhūteṣu śaktirūpeṇa saṃsthitā…” Few lines in Sanskrit are better known. Every Navarātri it rings out from pandals, temples and television sets: “to the Goddess who dwells in all beings as power: salutations to her, salutations to her, salutations to her, again and again.”</p>
    <p>It comes from the <b>Devī Māhātmya</b>, the great Purāṇic text of the Goddess. Driven from heaven, the gods stand on the Himālaya and praise her, not as a distant queen but as something inside every creature: its awareness, its hunger, its sleep, its faith, its mother, even its mistakes.</p>
    <p>Twenty-one forms. By the end, there is nowhere she is not.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--red)">With the blessings of the Devī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why say 'salutations to her' three times?","Each form gets three bows. The tradition even counts each line as three separate mantras, which is how the Devī Māhātmya reaches its famous total of 700.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">THE HYMN IN ONE GO</h2>
  <div class="sub">Verses 1–11</div>
  <div class="full">{full1}</div>
</section>

<section class="page" id="full2">
  <h2 class="page-title">IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 12–28</div>
  <div class="full">{full2}</div>
  <div class="note">Verse numbers follow the popular 28-verse stotram. Text checked against shlokam.org.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · THE GODS ON THE HIMĀLAYA</h2>
  <div class="sub">Why the gods sang this hymn</div>
  {story_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The story in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>Heaven seized.</b> Two demon brothers, Śumbha and Niśumbha, take over the three worlds and strip the gods of their powers.</div>
      <div><b>A promise remembered.</b> After slaying Mahiṣa (chapter 4), the Goddess had promised: “Remember me in distress, and I will come.”</div>
      <div><b>The hymn.</b> The gods go to the Himālaya and sing this praise: to the Goddess in every being.</div>
      <div><b>Ambikā appears.</b> Pārvatī comes to bathe in the Gaṅgā and asks whom they are praising. From her own body shines out Ambikā, who answers: “This hymn is for me.”</div>
      <div><b>The battle begins.</b> Śumbha’s servants see her beauty; the demon king sends a proposal. Her reply opens the great war of chapters 5–10.</div>
    </div>
  </div>
  {talk("She was hiding inside Pārvatī?","That's the point: the Goddess is inside every being. The gods just sang it, and here she shows it.")}
</section>

<section class="page" id="about">
  <h2 class="page-title">ABOUT THE HYMN</h2>
  <div class="sub">One hymn, many names</div>
  <div class="g2">
    <div class="card bg-red"><h4>📜 Where it comes from</h4><p><b>Devī Māhātmya</b> (Durgā Saptaśatī), chapter 5, part of the Mārkaṇḍeya Purāṇa.</p></div>
    <div class="card bg-yellow"><h4>🏷 Its names</h4><p><b>Aparājitā Stuti</b>, “praise of the Unconquered One”; also called the Tāntrika Devī Sūktam.</p></div>
  </div>
  <table class="ct">
    <tr><th>Verses</th><th>What they do</th></tr>
    <tr><td><b>1–5</b></td><td>Salutations to the Goddess by her many names: Nature, Gaurī, Durgā, gentle and fierce</td></tr>
    <tr><td><b>6–26</b></td><td>The 21 forms: “the Goddess who dwells in all beings as…”</td></tr>
    <tr><td><b>27–28</b></td><td>The summing up: ruler of the senses, consciousness filling the world</td></tr>
  </table>
  <div class="panel reading pt"><p><b>When it is chanted.</b> Every Navarātri, in daily Devī worship, and at the Aparājitā pūjā on Vijayadaśamī. <b>Not to be confused</b> with the Ṛg Vedic Devī Sūkta (10.125), “ahaṃ rudrebhir…”, which the Saptaśatī recitation also uses.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">In One Go</a></li>
    <li><span class="num">★</span><a href="#story">The Story</a></li>
    <li><span class="num">ℹ</span><a href="#about">About the Hymn</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    <li class="part">THE OPENING SALUTATIONS</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title()}</a></li>' for v in O)}
    <li class="part">THE 21 FORMS</li>
    {''.join(f'<li><span class="num">{g[0].split("–")[0]}</span><a href="#f{k}">{g[2]}</a></li>' for k,g in enumerate(GROUPS))}
    <li class="part">THE CLOSING</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title()}</a></li>' for v in CL)}
  </ul>
</section>
''']
def vpage(v):
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    return f'''<section class="page" id="v{v['n']}">
  <h2 class="page-title">VERSE {v['n']}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(v['lines'])}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>
    <div class="plain">{v['plain']}</div>
    <table class="ct"><tr><th>Word</th><th>Means</th></tr>{words}</table>
  </div>
  <div class="panel reading pt">{v['point']}</div>
  <div class="key">{v['key']}</div>{note}
</section>
'''
for v in O: b.append(vpage(v))
for k,(rng,theme,title,point,key) in enumerate(GROUPS):
    fs=FORMS[3*k:3*k+3]; a=int(rng.split('–')[0])
    cards=''.join(f'<div class="form">{f[4]}<div><h4>{6+3*k+i}. {f[1]} · {f[2]}</h4><p class="ln">yā devī sarvabhūteṣu {f[0]}</p><p>{f[3]}</p></div></div>' for i,f in enumerate(fs))
    b.append(f'''<section class="page" id="f{k}">
  <h2 class="page-title">VERSES {rng} · {title.upper()}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{theme}</span></div>
    {cards}
    <p class="refrain">after each: {REF}</p>
    <p class="center" style="margin:2px 0 0;font-size:14px">“To her: salutations, salutations, salutations, again and again.”</p>
  </div>
  <div class="panel reading pt"><p>{point}</p></div>
  <div class="key">{key}</div>
</section>
''')
for v in CL: b.append(vpage(v))
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">THE HYMN ON ONE PAGE</h2>
  <div class="sub">28 verses in five lines</div>
  <div class="steps">
    <div><b>The setting.</b> Driven from heaven by Śumbha and Niśumbha, the gods remember the Goddess’s promise and praise her on the Himālaya.</div>
    <div><b>Verses 1–5.</b> They bow to her as Nature, Gaurī, moonlight, fortune and misfortune, Durgā who carries us across, the gentlest and the fiercest.</div>
    <div><b>Verses 6–14.</b> She is in every being as Viṣṇu’s māyā, awareness, intelligence, sleep, hunger, shadow, power, desire, patience.</div>
    <div><b>Verses 15–26.</b> As birth, modesty, peace, faith, radiance, fortune, work, memory, compassion, contentment, the mother, and even error.</div>
    <div><b>Verses 27–28.</b> Ruler of every sense, she fills the whole world as consciousness. Then Ambikā steps out of Pārvatī to answer them.</div>
  </div>
  {talk("What's the one thing to remember?","Look at anything: a sleeping child, a hungry dog, your own mistake. The hymn says: she is there too. Bow.")}
  <div class="key">“Yā devī sarvabhūteṣu”: <b>the Goddess dwells in every being</b>. 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Aparājitā Stuti (“yā devī sarvabhūteṣu”), Devī Māhātmya chapter 5, Mārkaṇḍeya Purāṇa. Text checked word by word against shlokam.org; readings that differ between editions (praṇatāṃ / praṇatā, vyāptyai devyai / vyāptidevyai) are noted. Verse numbers follow the popular 28-verse stotram; in the Devī Māhātmya the hymn falls in chapter 5, where each “yā devī” verse is counted as three mantras. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('/home/claude/work/yadevi/Ya_Devi_Sarvabhuteshu.html','w').write(head+''.join(b)+tail)
print('ok')
