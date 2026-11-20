import sys; sys.path.insert(0,'/home/claude/work/devim')
from common import *
head=make_head('Kīlakam · Part 4 · Devī Māhātmya series · srini.presents',
 'Kīlakam, Part 4 of the Devī Māhātmya series: why the Saptaśatī is said to be “pinned” by Śiva, and how it is unlocked, all 14 verses explained in plain English with illustrations.')
def SHIVA(x=110,y=0,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2">'
     '<path d="M-10 26 q10 -30 20 0" fill="#7a5a3a"/><path d="M4 8 a7 7 0 1 0 0 12 a9 9 0 0 1 0 -12z" fill="#fff8c0"/>'
     '<circle cy="40" r="15" fill="#9fd3f0"/><path d="M-4 32 h8" stroke="#c0392b" stroke-width="2"/><path d="M-30 150 q-6 -70 30 -88 q36 18 30 88z" fill="#9fd3f0"/><path d="M-26 92 q26 -14 52 0" fill="none" stroke="#2a9d6f" stroke-width="4"/>'
     '<path d="M44 150 v-120 M34 40 v-14 M54 40 v-14 M34 40 h20" stroke="#111" stroke-width="3" fill="none"/></g>')
PIN=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-4 0 h8 l-2 40 h-4z" fill="#e0a800"/><rect x="-10" y="-8" width="20" height="10" rx="3" fill="#c46a1a"/></g>'
BOOK=lambda x,y,s=1,t='700': f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-30" y="-22" width="60" height="44" fill="#fff3b0"/><path d="M0 -22 v44" /><text x="0" y="6" text-anchor="middle" {F} font-size="14" stroke="none" fill="#c0392b">{t}</text></g>'
V=[
dict(n='1',lines=[['viśuddhajñānadehāya','trivedīdivyacakṣuṣe |'],['śreyaḥprāptinimittāya','namaḥ somārdhadhāriṇe ‖1‖']],theme='SALUTATIONS TO ŚIVA',
 svg=svg('Shiva with the crescent moon in his hair, three small scrolls of the Vedas glowing like eyes above him',SHIVA(110,0,.95)+''.join(f'<rect x="{30+k*20}" y="20" width="14" height="22" fill="#fff3b0" stroke="#111"/>' for k in range(3))+T(50,56,'3 VEDAS',9),R),
 mean='Mārkaṇḍeya said: Salutations to the one whose body is pure knowledge, whose divine eyes are the three Vedas, who is the means of attaining the highest good, and who wears the half-moon.',
 plain='We bow to Śiva: made of pure knowledge, seeing through the Vedas, the way to our highest good, the moon in his hair.',
 words=[('viśuddha-jñāna-deha','<b>whose body is pure knowledge</b>'),('trivedī-divya-cakṣus','<b>whose divine eyes are the three Vedas</b>'),('śreyaḥ-prāpti-nimitta','<b>the cause of attaining the highest good</b>'),('soma-ardha-dhārin','<b>wearer of the half-moon</b>')],
 point='<b>Why start with Śiva?</b> The Kavacam began with Brahmā, the Argalā with the Goddess. The Kīlakam opens with Śiva, because in this hymn it is Śiva who “pins” the Saptaśatī, and whose grace unlocks it.',
 key='The lock-keeper is greeted first: <b>Śiva</b>.'),
dict(n='2',lines=[['sarvam etad vijānīyān','mantrāṇām abhikīlakam |'],['so’pi kṣemam avāpnoti','satataṃ japyatatparaḥ ‖2‖']],theme='THE PIN OF ALL MANTRAS',
 svg=svg('A book of 700 verses held shut by a golden pin, a person reciting before it',BOOK(110,70,1.6)+PIN(110,30,1)+person(40,150,'#ff8c1a','#c98b5a',.8),R),
 mean='Know all this as the kīlaka, the pin, of the mantras. One who is always devoted to reciting it attains well-being.',
 plain='This text is the key that holds the power of all its mantras. Whoever recites it faithfully is kept safe.',
 words=[('vijānīyāt','<b>one should know</b>'),('abhikīlakam','<b>the pin</b>, the fastening'),('kṣemam','<b>well-being</b>, safety'),('japya-tatparaḥ','<b>devoted to recitation</b>')],
 point='<b>What is a kīlaka?</b> A <i>kīla</i> is a peg, wedge or pin. A kīlaka verse “fastens” the power of a mantra: it can lock it, and it can secure it in place. The same word appears in many mantras’ opening dedications (seer, metre, deity, seed, power, <i>kīlaka</i>).',
 key='The kīlaka is <b>the pin that fastens a mantra’s power</b>.'),
dict(n='3–4',lab='VERSES 3–4',lines=[['siddhyanty uccāṭanādīni','vastūni sakalāny api |'],['etena stuvatāṃ devī','stotramātreṇa siddhyati ‖3‖'],['na mantro nauṣadhaṃ tatra','na kiṃcid api vidyate |'],['vinā japyena siddhyeta','sarvam uccāṭanādikam ‖4‖']],theme='IT WORKS BY ITSELF',
 svg=svg('A single book glowing, while a shelf of medicines and other mantra-scrolls is pushed aside',BOOK(130,80,1.6)+'<circle cx="130" cy="80" r="50" fill="#ffd60a" opacity=".3" stroke="none"/><g stroke="#111" stroke-width="2"><rect x="16" y="90" width="12" height="24" fill="#2a9d6f"/><rect x="32" y="96" width="12" height="18" fill="#9b5de5"/><rect x="48" y="86" width="10" height="28" fill="#4aa3df"/></g><path d="M10 80 l56 40 M66 80 l-56 40" stroke="#c0392b" stroke-width="3"/>',R),
 mean='All undertakings succeed, even rites such as uccāṭana. For those who praise the Devī with this, she is won by the hymn alone. There, no other mantra, no medicine, nothing else is needed: without any other recitation, every rite succeeds.',
 words=[('siddhyanti','<b>succeed</b>'),('uccāṭana-ādīni','<b>rites like uccāṭana</b>, driving away'),('stotra-mātreṇa','<b>by the hymn alone</b>'),('na mantraḥ na auṣadham','<b>no mantra, no medicine</b>')],
 point='<b>Too powerful?</b> The text says the Saptaśatī alone accomplishes anything, even <i>uccāṭana</i> and similar rites aimed at others. That is the problem the next verses address: a power open to every purpose, good or harmful.',
 key='It needs nothing else, <b>and that is why it was locked</b>.'),
dict(n='5–6',lab='VERSES 5–6',lines=[['samagrāṇy api siddhyanti','lokaśaṅkām imāṃ haraḥ |'],['kṛtvā nimantrayāmāsa','sarvam evam idaṃ śubham ‖5‖'],['stotraṃ vai caṇḍikāyās tu','tac ca guptaṃ cakāra saḥ |'],['samāptir na ca puṇyasya','tāṃ yathāvan niyantraṇām ‖6‖']],theme='ŚIVA LOCKS IT',
 svg=svg('Shiva pressing a golden pin into a glowing book while worried people watch',SHIVA(60,10,.8)+BOOK(150,96,1.4)+PIN(150,50,1.1)+crowd(['#fff','#ffd60a','#3b6fd0'],150,22,156,.4),R),
 mean='“Everything succeeds by it”: seeing this concern of the world, Hara (Śiva) ordained that all of it should be for good. He made this hymn of Caṇḍikā secret; for its merit has no end. So he set a proper restraint upon it.',
 words=[('loka-śaṅkā','<b>the world’s concern</b>, fear'),('haraḥ','<b>Hara</b>: Śiva'),('guptaṃ cakāra','<b>made it hidden</b>, secret'),('niyantraṇām','<b>a restraint</b>, a control')],
 point='<b>The story of the lock.</b> Tradition reads these verses as a story: people feared what such a power could do, so Śiva “pinned” the text, keeping its full fruit for those who come to it the right way. The verses are terse, and editions differ here.',
 key='Śiva set a lock, <b>so the power serves only good</b>.',
 note='Some editions read guhyaṃ for guptaṃ and samāpnoti sa puṇyena tāṃ yathāvan nimantraṇām in verse 6.'),
dict(n='7–8',lab='VERSES 7–8',lines=[['so’pi kṣemam avāpnoti','sarvam eva na saṃśayaḥ |'],['kṛṣṇāyāṃ vā caturdaśyām','aṣṭamyāṃ vā samāhitaḥ ‖7‖'],['dadāti pratigṛhṇāti','nānyathaiṣā prasīdati |'],['itthaṃrūpeṇa kīlena','mahādevena kīlitam ‖8‖']],theme='GIVE, AND RECEIVE',
 svg=svg('Under a waning moon, a devotee offers a tray with both hands to the Goddess, who hands back a glowing gift',
  '<rect width="220" height="160" fill="#2b2140"/>'+STARS(10,7)+'<path d="M190 14 a12 12 0 1 0 0 24 a15 15 0 0 1 0 -24z" fill="#fff8c0"/>'+DEVI(150,10,.55,False)+person(60,150,'#ff8c1a','#c98b5a',.9)+'<path d="M76 116 h30" stroke="#e0a800" stroke-width="5"/><path d="M96 100 l10 6 l-10 6" fill="#ffd60a" stroke="#ffd60a"/><path d="M126 96 l-14 6 l14 6" fill="#ffd60a" stroke="#ffd60a"/>'+T(110,148,'8TH · 14TH',10,'#fff'),R),
 mean='Such a one too attains every well-being, no doubt: one who, with a collected mind, on the fourteenth or the eighth day of the dark fortnight, gives and receives. Otherwise she is not pleased. In this way, with such a pin, it was pinned by Mahādeva.',
 words=[('kṛṣṇāyāṃ caturdaśyām','<b>on the 14th of the dark fortnight</b>'),('aṣṭamyām','<b>on the 8th</b>'),('samāhitaḥ','<b>with a collected mind</b>'),('dadāti pratigṛhṇāti','<b>gives and receives</b>')],
 point='<b>The key to the lock.</b> “Gives and receives” is famously cryptic. A common reading: the devotee <b>offers everything</b> to the Goddess, and <b>receives it back</b> as her grace. Surrender is the key. See the page “How the Lock Opens”.',
 key='The pin comes out when we <b>give ourselves, and receive her grace</b>.'),
dict(n='9–10',lab='VERSES 9–10',lines=[['yo niṣkīlāṃ vidhāyaināṃ','nityaṃ japati saṃsphuṭam |'],['sa siddhaḥ sa gaṇaḥ so’pi','gandharvo jāyate naraḥ ‖9‖'],['na caivāpy aṭatas tasya','bhayaṃ kvāpīha jāyate |'],['nāpamṛtyuvaśaṃ yāti','mṛto mokṣam avāpnuyāt ‖10‖']],theme='UNPINNED',
 svg=svg('The golden pin lifted out of the book, light streaming out, a traveller walking without fear',BOOK(80,90,1.5)+PIN(80,20,1)+'<circle cx="80" cy="90" r="46" fill="#ffd60a" opacity=".3" stroke="none"/>'+person(170,146,'#ff8c1a','#c98b5a',.8)+'<path d="M140 150 h70" stroke="#7a5a3a" stroke-width="3" stroke-dasharray="8 5"/>',R),
 mean='One who unpins it and recites it every day, clearly, becomes a siddha, one of Śiva’s attendants, a gandharva. Wherever he wanders, no fear arises for him here; he does not fall to untimely death, and at death he attains liberation.',
 words=[('niṣkīlām vidhāya','<b>having unpinned it</b>'),('saṃsphuṭam','<b>clearly</b>, distinctly'),('siddhaḥ · gaṇaḥ','<b>a perfected one</b> · <b>Śiva’s attendant</b>'),('mokṣam avāpnuyāt','<b>attains liberation</b>')],
 point='<b>Clearly, every day.</b> Two conditions: the text is first <i>unpinned</i>, approached rightly, and then recited <i>saṃsphuṭam</i>, “distinctly”. Not mumbled, not rushed. The promise reaches from fearless wandering to liberation.',
 key='Unpinned and recited clearly, <b>it frees from fear</b>.'),
dict(n='11',lines=[['jñātvā prārabhya kurvīta','na kurvāṇo vinaśyati |'],['tato jñātvaiva sampannam','idaṃ prārabhyate budhaiḥ ‖11‖']],theme='KNOW, THEN BEGIN',
 svg=svg('A student with an open book listening to a teacher before starting to recite',person(60,148,'#fff','#c98b5a',1)+person(150,150,'#ff8c1a','#c98b5a',.9)+'<rect x="128" y="104" width="32" height="20" fill="#fff3b0" stroke="#111" stroke-width="2"/>'+T(110,30,'FIRST UNDERSTAND',11),R),
 mean='Having understood, one should begin and perform it. One who does it without understanding comes to ruin. Therefore the wise begin it only once they have understood it fully.',
 plain='Understand it first, then begin. Rushing in without understanding brings nothing. That is why the wise learn it before they start.',
 words=[('jñātvā','<b>having understood</b>'),('prārabhya kurvīta','<b>should begin and do it</b>'),('vinaśyati','<b>comes to ruin</b>'),('budhaiḥ','<b>by the wise</b>')],
 point='<b>Why this series exists.</b> The Kīlakam itself says: know first, then recite. Reading the meaning before chanting is not a luxury; the text asks for it.',
 key='<b>Understand, then chant</b>: the Kīlakam insists.'),
dict(n='12–13',lab='VERSES 12–13',lines=[['saubhāgyādi ca yat kiṃcid','dṛśyate lalanājane |'],['tat sarvaṃ tatprasādena','tena japyam idaṃ śubham ‖12‖'],['śanais tu japyamāne’smin','stotre sampattir uccakaiḥ |'],['bhavaty eva samagrāpi','tataḥ prārabhyam eva tat ‖13‖']],theme='EVEN SOFTLY',
 svg=svg('A woman quietly reciting at home with a lamp, flowers blooming and coins glowing around her',person(80,148,'#e05a8a','#c98b5a',1)+'<path d="M120 130 h20 l-4 10 h-12z" fill="#e0a800" stroke="#111" stroke-width="2"/><path d="M130 128 q-6 -12 0 -22 q6 10 0 22z" fill="#ff8c1a" stroke="#111"/>'+''.join(f'<circle cx="{150+k*16}" cy="{60+(k%2)*12}" r="6" fill="#ffd60a" stroke="#111"/>' for k in range(4))+''.join(f'<circle cx="{20+k*16}" cy="{40+(k%2)*10}" r="5" fill="#f08aa6" stroke="#111"/>' for k in range(4)),R),
 mean='Whatever good fortune and the like is seen in women, all of it is by her grace; so this auspicious hymn should be recited. Even when recited softly, this hymn brings great and complete prosperity; therefore it should surely be begun.',
 words=[('saubhāgya','<b>good fortune</b>, happiness in marriage'),('lalanā-jane','<b>among women</b>'),('tat-prasādena','<b>by her grace</b>'),('śanaiḥ','<b>softly</b>, slowly')],
 point='<b>No need to be loud.</b> Verse 13 says even a soft, slow recitation brings fullness. Verse 12 notes that every grace seen in women’s lives is the Goddess’s own; she is honoured in them.',
 key='Even recited softly, <b>it brings fullness</b>.'),
dict(n='14',lines=[['aiśvaryaṃ yatprasādena','saubhāgyārogyasampadaḥ |'],['śatruhāniḥ paro mokṣaḥ','stūyate sā na kiṃ janaiḥ ‖14‖']],theme='WHY WOULD WE NOT PRAISE HER?',
 svg=svg('The Goddess radiant with symbols of her gifts around her: crown, lotus, heart, coins, broken sword and a rising sun',
  '<circle cx="110" cy="76" r="70" fill="#ffd60a" opacity=".3" stroke="none"/>'+DEVI(110,0,.75,False)+''.join(f'<text x="{110+86*math.cos(k*1.047-1.57):.0f}" y="{82+60*math.sin(k*1.047-1.57):.0f}" text-anchor="middle" font-size="18">{e}</text>' for k,e in enumerate('👑🌸❤️💰⚔️☀️')),R),
 mean='She by whose grace come sovereignty, good fortune, health and wealth, the end of enemies and the highest liberation: why would people not praise her?',
 plain='Every blessing, from health and wealth to final freedom, comes by her grace. How could we not praise her?',
 words=[('aiśvaryam','<b>sovereignty</b>, greatness'),('ārogya','<b>health</b>'),('śatru-hāniḥ','<b>the end of enemies</b>'),('paraḥ mokṣaḥ','<b>the highest liberation</b>'),('na kim','<b>why not?</b>')],
 point='<b>A question to end on.</b> The three limbs close with a question that answers itself. The door is unbolted and unpinned; next the reader turns to the 700 verses themselves.',
 key='All blessings are hers: <b>how could we not praise her?</b>'),
]
full=''.join(fp(v.get('lab','VERSE '+v['n']),v['lines']) for v in V)
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Shiva lifting a golden pin out of a glowing book of 700 verses, with the Goddess appearing in the light">'
 '<rect width="380" height="268" fill="#3a1414" rx="8"/><circle cx="230" cy="140" r="100" fill="#ffd60a" opacity=".22"/>'
 +DEVI(240,20,.75,True)+BOOK(240,212,2.2)+PIN(240,120,1.4)+SHIVA(90,40,1.15)+'</svg>')
lock_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: the three limbs as armour, bolt and pin; Shiva pins the book; the devotee gives and receives and the pin comes out">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#fde4e4','ARMOUR · BOLT · PIN'),('#dfe9f6','ŚIVA PINS IT'),('#fff3b0','GIVE AND RECEIVE')]))
 +'<path d="M30 60 q20 -12 40 0 l-4 40 q-16 10 -32 0z" fill="#e0a800" stroke="#111" stroke-width="2"/><rect x="80" y="74" width="50" height="10" fill="#c46a1a" stroke="#111" stroke-width="2"/>'+PIN(78,120,1)
 +SHIVA(200,40,.6)+BOOK(250,140,1)+PIN(250,100,.8)
 +person(350,170,'#ff8c1a','#c98b5a',.8)+DEVI(420,30,.45,False)+'<path d="M362 130 h30" stroke="#e0a800" stroke-width="4"/>'+PIN(395,60,.7)+'</svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 4 OF 19</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.6vw,80px)">KĪLAKAM</h1>
  <div class="series">DEVĪ MĀHĀTMYA · PART 4 · THE PIN</div>
  <div class="tag">Why the Saptaśatī is “locked”, and how it opens · explained and illustrated</div>
  {cover}
  {CAST}
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> All 14 verses for chanting, then the story of the lock and how it opens. Then <b>one page for each verse or pair</b>: the chant, a picture, what it says, the key words, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">WHERE WE ARE</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    <p>The reader has put on the armour (<a href="/bhakti/devi/devi-mahatmya/part-1/">Kavacam</a>) and lifted the bolt (<a href="/bhakti/devi/devi-mahatmya/part-3/">Argalā</a>). One thing still holds the door: the <b>pin</b>.</p>
    <p>The <b>Kīlakam</b> is the strangest of the three limbs. It says the Saptaśatī is so powerful that Śiva himself “pinned” it, so that its full fruit comes only to those who approach it the right way. Its 14 verses are short and cryptic, and teachers have explained them in different ways.</p>
    <p>After this, the three limbs are complete, and the story begins.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--red)">With the blessings of the Devī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A book that's locked? Then how does anyone read it?","Anyone can read the words. The Kīlakam is about the fruit: it opens fully to those who give themselves to the Goddess.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">ALL 14 VERSES IN ONE GO</h2>
  <div class="sub">Kīlakam</div>
  <div class="full">{full}</div>
  <div class="note">Text checked against bhaktibharat.com (14 verses); sanskritdocuments.org has a different reading in verses 2–6 and 9.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">HOW THE LOCK OPENS</h2>
  <div class="sub">The pin, and the key</div>
  {lock_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The idea in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>Three limbs.</b> Armour (Kavacam) to protect, the bolt (Argalā) lifted, the pin (Kīlakam) removed.</div>
      <div><b>Too powerful.</b> The text says the Saptaśatī alone can accomplish anything, even rites meant to harm (verses 3–4).</div>
      <div><b>Śiva pins it.</b> Seeing the world’s concern, Śiva makes it secret and sets a restraint on it (verses 5–6, 8).</div>
      <div><b>Give and receive.</b> On the 8th or 14th of the dark fortnight, with a collected mind, the devotee “gives and receives” (verses 7–8).</div>
      <div><b>Know, then recite.</b> Understand it first, then recite it clearly every day (verses 9–11).</div>
    </div>
  </div>
  <div class="panel reading pt"><p><b>What does “give and receive” mean?</b> The words are cryptic and readings differ. A common one: offer everything you are and have to the Goddess, and receive it back as her grace. Others read it as an exchange with a teacher, or a ritual offering.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">←</span><a href="#foreword">Where We Are</a></li>
    <li><span class="num">🔤</span><a href="#full">In One Go</a></li>
    <li><span class="num">🔑</span><a href="#story">How the Lock Opens</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    <li class="part">THE 14 VERSES</li>
    {''.join(f'<li><span class="num">{v["n"].split("–")[0]}</span><a href="#v{v["n"]}">{v["theme"].title().replace("’S","’s")}</a></li>' for v in V)}
  </ul>
</section>
''']
for v in V:
    h=vpage(v)
    if len(v['lines'])>=4:
        h=h.replace(f'<section class="page" id="v{v["n"]}">',f'<section class="page long" id="v{v["n"]}">',1)
    b.append(h)
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 4 ON ONE PAGE</h2>
  <div class="sub">The Kīlakam in five lines</div>
  <div class="steps">
    <div><b>Verse 1.</b> Salutations to Śiva, pure knowledge, with the Vedas for eyes and the moon in his hair.</div>
    <div><b>Verses 2–4.</b> The Saptaśatī is the pin of all mantras; by itself it accomplishes everything.</div>
    <div><b>Verses 5–8.</b> So Śiva made it secret and pinned it; it opens to one who, collected, gives and receives.</div>
    <div><b>Verses 9–11.</b> Unpinned and recited clearly, it frees from fear; but understand it first, then begin.</div>
    <div><b>Verses 12–14.</b> Even softly recited it brings fullness; every blessing is hers. Why would we not praise her?</div>
  </div>
  {talk("So the three limbs are done?","Done! Armour on, bolt lifted, pin out. Part 5 opens the book: a dethroned king, a betrayed merchant and a sage in the forest.")}
  <div class="key">Part 4: <b>give yourself, receive her grace: the pin comes out</b>. 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Kīlakam, chanted before the Devī Māhātmya (Durgā Saptaśatī). Text checked word by word against bhaktibharat.com (14 verses); some editions (e.g. sanskritdocuments.org) read verses 2–6 and 9 differently. The verses are cryptic and their meaning is debated; the explanation of “give and receive” is one common traditional reading. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('/home/claude/work/devim/Devi_Mahatmya_Part04.html','w').write(head+''.join(b)+tail())
print('ok')
