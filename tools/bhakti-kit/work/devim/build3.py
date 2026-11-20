import sys; sys.path.insert(0,'/home/claude/work/devim')
from common import *
EXTRA='''  .form{display:grid;grid-template-columns:92px 1fr;gap:10px;align-items:center;border:3px solid var(--ink);background:#fff;padding:4px 8px;margin:5px 0;box-shadow:4px 4px 0 var(--ink)}
  .form svg{width:92px;height:auto;display:block}
  .form h4{margin:0 0 2px;font-family:Bangers,Impact,sans-serif;letter-spacing:1px;font-size:18px;color:var(--red)}
  .form .ln{font-style:italic;font-size:13.5px;margin:0 0 3px}
  .form p{margin:0;font-size:13.5px;line-height:1.38}
  .refrain{text-align:center;font-style:italic;font-weight:bold;margin:4px 0 0}
  .big4{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:10px 0}
  .big4 div{border:3px solid var(--ink);background:#fff;padding:10px;box-shadow:4px 4px 0 var(--ink)}
  .big4 b.s{display:block;font-family:Bangers,Impact,sans-serif;font-size:26px;letter-spacing:1px;color:var(--red)}
  @media(max-width:720px){.form{grid-template-columns:84px 1fr}.form svg{width:84px}}
'''
head=make_head('Argalā Stotram · Part 3 · Devī Māhātmya series · srini.presents',
 'Argalā Stotram, Part 3 of the Devī Māhātmya series: “rūpaṃ dehi, jayaṃ dehi, yaśo dehi, dviṣo jahi”, all 25 verses explained in plain English with illustrations.',EXTRA)
def ico(inner,bg='#fff8ec'): return f'<svg viewBox="0 0 120 90" role="img" aria-hidden="true"><rect width="120" height="90" fill="{bg}"/>{inner}</svg>'
REF=('rūpaṃ dehi jayaṃ dehi','yaśo dehi dviṣo jahi')
V1=dict(n='1',lines=[['jayantī maṅgalā kālī','bhadrakālī kapālinī |'],['durgā kṣamā śivā dhātrī','svāhā svadhā namo’stu te ‖1‖']],theme='ELEVEN NAMES',
 svg=svg('Eleven small goddess figures in a semicircle, from bright Jayanti to dark Kali, around a fire with offerings',''.join(DEVI(110+86*math.cos(math.pi+k*math.pi/10),120+86*math.sin(math.pi+k*math.pi/10)-40,.2,False,c) for k,c in enumerate(['#ffd60a','#2a9d6f','#222','#3a1a3a','#5a2a2a','#c0392b','#9fd3f0','#fff','#ff8c1a','#e0a800','#7a5a3a']))+FIRE(110,130,.8),R),
 mean='Jayantī, Maṅgalā, Kālī, Bhadrakālī, Kapālinī; Durgā, Kṣamā, Śivā, Dhātrī, Svāhā, Svadhā: salutations to you.',
 plain='The Victorious, the Auspicious, the Dark One, the Gracious Kālī, the Skull-bearer; Durgā, Patience, the Kind One, the Nurse of all, and the offerings to gods and ancestors: we bow to you.',
 words=[('jayantī · maṅgalā','<b>the victorious</b> · <b>the auspicious</b>'),('kālī · bhadrakālī','<b>the dark one</b> · <b>the gracious Kālī</b>'),('kapālinī','<b>bearer of skulls</b>'),('kṣamā · dhātrī','<b>patience, forgiveness</b> · <b>the nurse, sustainer</b>'),('svāhā · svadhā','<b>the cry of offering to gods</b> · <b>to ancestors</b>')],
 point='<b>The most chanted line of the Saptaśatī.</b> Many people who know nothing else of the text know this verse. Eleven names run from fierce (Kālī, Kapālinī) to gentle (Kṣamā, Dhātrī) and end with <i>svāhā</i> and <i>svadhā</i>: she is even the offering itself.',
 key='Fierce and gentle, <b>even the offering is she</b>.')
V2=dict(n='2',lines=[['jaya tvaṃ devi cāmuṇḍe','jaya bhūtārtihāriṇi |'],['jaya sarvagate devi','kālarātri namo’stu te ‖2‖']],theme='VICTORY TO YOU',
 svg=svg('Crowds raising their hands and cheering “Jaya!” before the fierce goddess Chamunda',DEVI(110,0,.7)+crowd(['#ffd60a','#fff','#3b6fd0','#ff8c1a','#2a9d6f','#e05a8a','#fff','#ffd60a'],14,27,154,.45)+T(40,30,'JAYA!',14,'#c0392b')+T(186,30,'JAYA!',14,'#c0392b'),R),
 mean='Victory to you, O Devī Cāmuṇḍā! Victory to you who take away the pain of all beings! Victory to you, Devī, present everywhere! O Kālarātri, salutations to you.',
 plain='Victory to you, fierce Cāmuṇḍā, who ends the suffering of every creature; victory to you who are everywhere; Dark Night of destruction, we bow.',
 words=[('jaya','<b>victory!</b>'),('bhūta-ārti-hāriṇi','<b>remover of beings’ pain</b>'),('sarva-gate','<b>O all-pervading one</b>'),('kāla-rātri','<b>the night of time</b>, the dark night of dissolution')],
 point='<b>Three cheers.</b> Three times <i>jaya</i>, “victory!”, like a crowd cheering a champion. Then from verse 3 the pattern changes: every verse names one of her deeds and ends with the same four requests.',
 key='Jaya, jaya, jaya: <b>victory to the Mother</b>.')
CARDS=[
 ('3–6','HER FOUR GREAT VICTORIES','The battles of the Devī Māhātmya',[
  ('madhukaiṭabhavidrāvi','vidhātṛvarade namaḥ','3 · MADHU AND KAIṬABHA','You who routed Madhu and Kaiṭabha, and gave Brahmā his boon: salutations. (Chapter 1)',
   ico('<ellipse cx="60" cy="70" rx="44" ry="10" fill="#4aa3df" stroke="#111" stroke-width="2"/>'+person(36,64,'#5a2a6a','#7a9a5a',.7)+person(84,64,'#3a2a6a','#6a8a4a',.7)+'<path d="M60 10 l4 14 h-8z" fill="#f08aa6" stroke="#111"/>')),
  ('mahiṣāsuranirṇāśi','bhaktānāṃ sukhade namaḥ','4 · MAHIṢĀSURA','Destroyer of the buffalo demon Mahiṣa, giver of joy to devotees: salutations. (Chapters 2–4)',
   ico(MOUNT('buffalo',56,58,1.2)+'<path d="M96 10 l-20 60" stroke="#ccc" stroke-width="4"/>')),
  ('raktabījavadhe devi','caṇḍamuṇḍavināśini','5 · RAKTABĪJA, CAṆḌA, MUṆḌA','Slayer of Raktabīja, destroyer of Caṇḍa and Muṇḍa. (Chapters 7–8)',
   ico(''.join(f'<path d="M{20+k*20} {20+(k%2)*14} q-6 10 0 14 q6 -4 0 -14z" fill="#c0392b" stroke="#111"/>' for k,_ in enumerate(range(5)))+person(60,84,'#5a2a2a','#7a6a5a',.6))),
  ('śumbhasyaiva niśumbhasya','dhūmrākṣasya ca mardini','6 · ŚUMBHA AND NIŚUMBHA','Crusher of Śumbha, Niśumbha and Dhūmrākṣa. (Chapters 6, 9–10)',
   ico(person(40,82,'#3a2a6a','#6a8a4a',.8)+person(80,82,'#5a2a6a','#7a9a5a',.8)+'<path d="M26 28 h28 l-4 -10 l-6 6 l-4 -8 l-4 8 l-6 -6z M66 28 h28 l-4 -10 l-6 6 l-4 -8 l-4 8 l-6 -6z" fill="#ffd60a" stroke="#111"/>'))],
  '<b>The whole story in four lines.</b> These verses list the Goddess’s victories in the order the Devī Māhātmya tells them. Saying them is like reading the book’s contents page before you begin.','Four battles, four victories: <b>the whole story in brief</b>.'),
 ('7–11','FOR THOSE WHO BOW TO YOU','Her nature, and her devotees',[
  ('vanditāṅghriyuge devi','sarvasaubhāgyadāyini','7 · HER WORSHIPPED FEET','Goddess whose two feet are worshipped, giver of every good fortune.',
   ico('<ellipse cx="44" cy="56" rx="12" ry="22" fill="#f2c79b" stroke="#111" stroke-width="2"/><ellipse cx="76" cy="56" rx="12" ry="22" fill="#f2c79b" stroke="#111" stroke-width="2"/>'+''.join(f'<circle cx="{20+k*20}" cy="84" r="5" fill="#f08aa6" stroke="#111"/>' for k in range(5)))),
  ('acintyarūpacarite','sarvaśatruvināśini','8 · BEYOND THOUGHT','You whose form and deeds are beyond imagining, destroyer of all enemies.',
   ico('<path d="M30 45 q15 -25 30 0 q15 25 30 0 q-15 -25 -30 0 q-15 25 -30 0z" fill="none" stroke="#9b5de5" stroke-width="5"/>')),
  ('natebhyaḥ sarvadā bhaktyā','caṇḍike duritāpahe','9 · FOR THOSE WHO BOW','O Caṇḍikā, remover of wrongs, for those who always bow to you with devotion…',
   ico('<path d="M30 80 q4 -20 20 -24 l30 0" fill="none" stroke="#ff8c1a" stroke-width="10"/><circle cx="88" cy="56" r="9" fill="#c98b5a" stroke="#111" stroke-width="2"/>')),
  ('stuvadbhyo bhaktipūrvaṃ tvāṃ','caṇḍike vyādhināśini','10 · FOR THOSE WHO PRAISE','O Caṇḍikā, destroyer of illness, for those who praise you with devotion…',
   ico(person(44,80,'#ff8c1a','#c98b5a',.8)+'<text x="80" y="40" font-size="20">♪</text><text x="96" y="58" font-size="16">♪</text>')),
  ('caṇḍike satataṃ ye tvām','arcayantīha bhaktitaḥ','11 · FOR THOSE WHO WORSHIP','O Caṇḍikā, for those who worship you here always, with love…',
   ico('<path d="M50 70 h20 l-4 10 h-12z" fill="#e0a800" stroke="#111" stroke-width="2"/><path d="M60 68 q-8 -14 0 -26 q8 12 0 26z" fill="#ff8c1a" stroke="#111" stroke-width="2"/>'))],
  '<b>Who the requests are for.</b> Verses 9–11 name the devotee: one who bows, one who praises, one who worships. The four requests that follow are asked for them, and for ourselves.','Bow, praise, worship: <b>and ask</b>.'),
 ('12–17','WHAT WE ASK FOR','Health, strength, learning, fame',[
  ('dehi saubhāgyam ārogyaṃ','dehi me paramaṃ sukham','12 · HEALTH AND HAPPINESS','Give me good fortune and health; give me the highest happiness.',
   ico('<path d="M60 76 q-30 -20 -30 -38 a14 14 0 0 1 30 -6 a14 14 0 0 1 30 6 q0 18 -30 38z" fill="#e05a8a" stroke="#111" stroke-width="2"/><path d="M48 44 h8 l4 -8 l6 16 l4 -8 h10" stroke="#fff" stroke-width="3" fill="none"/>')),
  ('vidhehi dviṣatāṃ nāśaṃ','vidhehi balam uccakaiḥ','13 · STRENGTH','Bring about the end of those who hate; grant me great strength.',
   ico('<path d="M30 70 q0 -30 20 -30 h20 q10 0 10 10 v20z" fill="#f2c79b" stroke="#111" stroke-width="2.5"/><path d="M80 40 l14 -14 M86 54 h16 M80 66 l14 12" stroke="#ffd60a" stroke-width="3"/>')),
  ('vidhehi devi kalyāṇaṃ','vidhehi paramāṃ śriyam','14 · WELL-BEING','Grant welfare, O Devī; grant the highest prosperity.',
   ico('<path d="M34 76 q26 12 52 0 l-6 -26 h-40z" fill="#e0a800" stroke="#111" stroke-width="2"/><path d="M52 50 q8 -22 16 0" fill="#2a9d6f" stroke="#111" stroke-width="2"/>')),
  ('surāsuraśiroratna-','nighṛṣṭacaraṇe’mbike','15 · GODS AND DEMONS BOW','O Ambikā, whose feet are touched by the crown-jewels of gods and demons alike.',
   ico('<ellipse cx="60" cy="40" rx="12" ry="20" fill="#f2c79b" stroke="#111" stroke-width="2"/><path d="M20 82 h22 l-4 -12 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#ffd60a" stroke="#111"/><path d="M78 82 h22 l-4 -12 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#9b5de5" stroke="#111"/>')),
  ('vidyāvantaṃ yaśasvantaṃ','lakṣmīvantaṃ janaṃ kuru','16 · LEARNED, FAMOUS, PROSPEROUS','Make your devotee learned, renowned and prosperous.',
   ico('<rect x="16" y="40" width="30" height="36" fill="#fff3b0" stroke="#111" stroke-width="2"/><text x="60" y="66" text-anchor="middle" font-size="24" fill="#e0a800">★</text><circle cx="94" cy="62" r="12" fill="#ffd60a" stroke="#111" stroke-width="2"/>')),
  ('pracaṇḍadaityadarpaghne','caṇḍike praṇatāya me','17 · FOR ME, WHO BOWS','O Caṇḍikā, who crushes the pride of fierce demons, to me who bows before you…',
   ico(person(60,84,'#ff8c1a','#c98b5a',.9)+'<path d="M20 20 l20 20 M100 20 l-20 20" stroke="#c0392b" stroke-width="4"/>'))],
  '<b>From “them” to “me”.</b> Verse 12 turns personal: <i>dehi me</i>, “give <b>me</b>”. Health, strength, welfare, learning, fame. Verse 17 ends: “to me who bows”. Prayer has to become your own.','Health, strength, learning: <b>ask her plainly</b>.'),
 ('18–23','PRAISED BY ALL THE GODS','Brahmā, Kṛṣṇa, Śiva and Indra',[
  ('caturbhuje caturvaktra-','saṃstute parameśvari','18 · PRAISED BY BRAHMĀ','Four-armed one, praised by the four-faced Brahmā, Supreme Goddess.',
   ico('<circle cx="60" cy="44" r="16" fill="#e0a800" stroke="#111" stroke-width="2"/><circle cx="40" cy="48" r="11" fill="#e0a800" stroke="#111" stroke-width="2"/><circle cx="80" cy="48" r="11" fill="#e0a800" stroke="#111" stroke-width="2"/>'+T(60,84,'4 FACES',10))),
  ('kṛṣṇena saṃstute devi','śaśvadbhaktyā sadāmbike','19 · PRAISED BY KṚṢṆA','Goddess, Ambikā, praised by Kṛṣṇa with unending devotion.',
   ico('<circle cx="46" cy="40" r="14" fill="#3b6fd0" stroke="#111" stroke-width="2"/><path d="M52 28 q6 -14 2 -20" stroke="#2a9d6f" stroke-width="3" fill="none"/><path d="M40 60 l60 -10" stroke="#7a5a3a" stroke-width="5" stroke-linecap="round"/>')),
  ('himācalasutānātha-','saṃstute parameśvari','20 · PRAISED BY ŚIVA','Supreme Goddess, praised by Śiva, lord of the Himālaya’s daughter.',
   ico('<path d="M60 86 v-60 M48 30 v-10 M72 30 v-10 M48 30 h24" stroke="#111" stroke-width="3" fill="none"/><path d="M84 18 a10 10 0 1 0 0 20 a13 13 0 0 1 0 -20z" fill="#fff8c0" stroke="#111"/>')),
  ('indrāṇīpatisadbhāva-','pūjite parameśvari','21 · WORSHIPPED BY INDRA','Supreme Goddess, worshipped with true devotion by Indra, Indrāṇī’s husband.',
   ico('<path d="M60 10 l10 30 h-20z M60 80 l10 -30 h-20z" fill="#ffd60a" stroke="#111" stroke-width="2"/><circle cx="60" cy="45" r="7" fill="#e0a800" stroke="#111"/>')),
  ('devi pracaṇḍadordaṇḍa-','daityadarpavināśini','22 · MIGHTY ARMS','Goddess whose mighty arms destroy the pride of demons.',
   ico(DEVI(60,-4,.5))),
  ('devi bhaktajanoddāma-','dattānandodaye’mbike','23 · JOY WITHOUT BOUND','Ambikā, who gives boundless, ever-rising joy to her devotees.',
   ico(SUN(60,50,18)+''.join(f'<path d="M{60+24*math.cos(k*0.785):.0f} {50+24*math.sin(k*0.785):.0f} l{10*math.cos(k*0.785):.0f} {10*math.sin(k*0.785):.0f}" stroke="#ff8c1a" stroke-width="3"/>' for k in range(8))))],
  '<b>Even the gods are devotees.</b> Brahmā the creator, Kṛṣṇa (Viṣṇu), Śiva and Indra all appear as her worshippers. In the Devī Māhātmya’s view, the great gods draw their power from her.','Creator, preserver, destroyer: <b>all of them bow to her</b>.'),
]
V24=dict(n='24',lines=[['patnīṃ manoramāṃ dehi','manovṛttānusāriṇīm |'],['tāriṇīṃ durgasaṃsāra-','sāgarasya kulodbhavām ‖24‖']],theme='A COMPANION FOR THE CROSSING',
 svg=svg('Two people in a small boat rowing together across a wide sea towards a far shore',
  '<path d="M0 100 q55 -14 110 0 t110 0 V160 H0z" fill="#4aa3df" stroke="#111" stroke-width="2"/><path d="M60 100 h90 l-12 18 h-66z" fill="#c9a26b" stroke="#111" stroke-width="2"/>'+person(88,98,'#c0392b','#c98b5a',.6)+person(120,98,'#3b6fd0','#c98b5a',.6)+'<path d="M190 60 h30 v40 h-30z" fill="#2a9d6f" stroke="#111" stroke-width="2"/>'+SUN(40,30,12),R),
 mean='Give me a delightful wife who follows the ways of my mind, who helps carry me across the hard ocean of worldly life, and who is born of a good family.',
 plain='Give me a loving life-partner who understands me, and who helps me cross the difficult sea of life.',
 words=[('patnīṃ manoramām','<b>a delightful wife</b>'),('mano-vṛtta-anusāriṇīm','<b>in tune with my mind</b>'),('tāriṇīm','<b>one who helps carry across</b>'),('durga-saṃsāra-sāgara','<b>the hard-to-cross ocean of worldly life</b>'),('kula-udbhavām','<b>born of a good family</b>')],
 point='<b>A partner as a boat.</b> The verse is written in the voice of a man of its time, but its picture is of a companion who helps <i>tārayati</i>, ferry, across life. Note <i>durga</i> again: the “hard to cross” sea. Many readers today take it as a prayer for a loving life-partner.',
 key='Give me <b>a companion for the crossing</b>.')
V25=dict(n='25',lines=[['idaṃ stotraṃ paṭhitvā tu','mahāstotraṃ paṭhen naraḥ |'],['sa tu saptaśatīsaṃkhyā-','varam āpnoti sampadām ‖25‖']],theme='NOW OPEN THE BOOK',
 svg=svg('A great door with a heavy bolt sliding open, and the book of 700 verses glowing inside',
  '<rect x="40" y="20" width="140" height="130" fill="#7a3a1a" stroke="#111" stroke-width="3"/><rect x="110" y="20" width="70" height="130" fill="#8a4a2a" stroke="#111" stroke-width="3"/><rect x="60" y="76" width="70" height="10" fill="#e0a800" stroke="#111" stroke-width="2"/><path d="M60 81 h-30" stroke="#111" stroke-width="2" stroke-dasharray="4 3"/><circle cx="160" cy="86" r="26" fill="#ffd60a" opacity=".5"/><rect x="146" y="70" width="28" height="34" fill="#fff3b0" stroke="#111" stroke-width="2"/>'+T(160,92,'700',11)+T(96,14,'ARGALĀ',11),R),
 mean='Having recited this hymn, one should recite the great hymn (the Saptaśatī). Such a person gains the best of riches, as many as its seven hundred verses.',
 plain='Say this hymn first, then read the Saptaśatī. Every one of its 700 verses becomes a blessing.',
 words=[('idaṃ stotraṃ paṭhitvā','<b>having recited this hymn</b>'),('mahā-stotram','<b>the great hymn</b>: the Saptaśatī'),('sapta-śatī-saṃkhyā','<b>the count of seven hundred</b>'),('varam … sampadām','<b>the best of riches</b>')],
 point='<b>The bolt slides back.</b> <i>Argalā</i> means the wooden bar that locks a door. This hymn lifts it. The last verse says plainly what comes next: the “great hymn”, the 700 verses of the Saptaśatī.',
 key='The bolt is lifted: <b>now the door can open</b>.')
def cardpage(k,c):
    rng,theme,title,items,point,key=c
    cs=''.join(f'<div class="form">{s}<div><h4>{h}</h4><p class="ln">{a} {b_}</p><p>{m}</p></div></div>' for a,b_,h,m,s in items)
    return f'''<section class="page" id="c{k}">
  <h2 class="page-title">VERSES {rng}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{theme}</span></div>
    {cs}
    <p class="refrain">after each: {REF[0]} · {REF[1]}</p>
  </div>
  <div class="panel reading pt"><p>{point}</p></div>
  <div class="key">{key}</div>
</section>
'''
ALLV=[('1',V1['lines']),('2',V2['lines'])]
n=3
for c in CARDS:
    for a,b_,*_ in c[3]:
        ALLV.append((str(n),[[a,b_+' |'],[REF[0],REF[1]+f' ‖{n}‖']])); n+=1
ALLV+= [('24',V24['lines']),('25',V25['lines'])]
fulls=[''.join(fp('VERSE '+k,l) for k,l in ALLV[i:j]) for i,j in [(0,9),(9,18),(18,25)]]
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A great temple door with its golden bolt sliding back, light pouring out, and the Goddess visible inside">'
 '<rect width="380" height="268" fill="#3a1414" rx="8"/><rect x="80" y="20" width="220" height="240" fill="#ffd60a" opacity=".35"/>'
 +DEVI(190,40,.95)
 +'<rect x="40" y="20" width="110" height="240" fill="#7a3a1a" stroke="#111" stroke-width="3"/><rect x="230" y="20" width="110" height="240" fill="#7a3a1a" stroke="#111" stroke-width="3"/>'
 +''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#e0a800" stroke="#111"/>' for x in (60,130,250,320) for y in (50,140,230))
 +'<rect x="10" y="134" width="140" height="16" fill="#e0a800" stroke="#111" stroke-width="3"/><path d="M14 142 h-10" stroke="#fff" stroke-width="3"/></svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 3 OF 19</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,76px)">ARGALĀ STOTRAM</h1>
  <div class="series">DEVĪ MĀHĀTMYA · PART 3 · THE BOLT</div>
  <div class="tag">“Rūpaṃ dehi, jayaṃ dehi” · explained and illustrated</div>
  {cover}
  {CAST}
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> All 25 verses for chanting, then what “argalā” means and the famous <b>four requests</b>. Verses 1, 2, 24 and 25 get a page each; the 21 refrain verses come <b>four to six to a page</b>, each with a picture and its meaning.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">WHERE WE ARE</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    <p>In Parts <a href="/bhakti/devi/devi-mahatmya/part-1/">1</a> and <a href="/bhakti/devi/devi-mahatmya/part-2/">2</a>, the reader put on the <b>Devī Kavacam</b>, armour from crest to sole. Now comes the second limb: the <b>Argalā Stotram</b>.</p>
    <p>An <i>argalā</i> is a bolt, the heavy bar across a door. This hymn lifts it. Its 25 verses praise the Goddess for her victories and ask her, again and again, for four things: <b>rūpaṃ dehi, jayaṃ dehi, yaśo dehi, dviṣo jahi</b>.</p>
    <p>Twenty-one times the same line. By the end, nobody forgets it.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--red)">With the blessings of the Devī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Isn't it greedy to ask for victory and fame?","Wait for the Four Requests page! Teachers read them at two levels, the outer and the inner.")}
</section>
''',
''.join(f'''<section class="page" id="full{'' if k==0 else k+1}">
  <h2 class="page-title">{'ALL 25 VERSES IN ONE GO' if k==0 else 'IN ONE GO · CONTINUED'}</h2>
  <div class="sub">{['Verses 1–9','Verses 10–18','Verses 19–25'][k]}</div>
  <div class="full">{f}</div>{'<div class="note">Text checked against shlokam.org (25 verses).</div>' if k==2 else ''}
</section>
''' for k,f in enumerate(fulls)),
f'''<section class="page" id="refrain">
  <h2 class="page-title">THE FOUR REQUESTS</h2>
  <div class="sub">rūpaṃ dehi · jayaṃ dehi · yaśo dehi · dviṣo jahi</div>
  <div class="big4">
    <div><b class="s">RŪPAṂ DEHI</b><b>“Give form.”</b> Outer: beauty, a good presence. Inner: many teachers read <i>rūpa</i> as one’s true nature, the Self.</div>
    <div><b class="s">JAYAṂ DEHI</b><b>“Give victory.”</b> Outer: success in what we undertake. Inner: victory over oneself.</div>
    <div><b class="s">YAŚO DEHI</b><b>“Give glory.”</b> Outer: a good name. Inner: the honour of a life well lived.</div>
    <div><b class="s">DVIṢO JAHI</b><b>“Destroy the enemies.”</b> Outer: those who wish us harm. Inner: the six inner enemies, desire, anger, greed, delusion, pride and envy.</div>
  </div>
  <div class="panel reading pt"><p><b>Three “give”s and one “destroy”.</b> <i>Dehi</i> is the plainest Sanskrit word for “give”, the word a child says to its mother. The fourth line flips it: <i>jahi</i>, “strike down”. The outer meanings are the plain sense; the inner readings are those of later teachers.</p></div>
  {talk("So which meaning is right?","Both! Ask for the outer things honestly, like a child asking its mother, and let the inner meaning grow on you with each repetition.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">←</span><a href="#foreword">Where We Are</a></li>
    <li><span class="num">🔤</span><a href="#full">In One Go</a></li>
    <li><span class="num">4</span><a href="#refrain">The Four Requests</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    <li class="part">THE 25 VERSES</li>
    <li><span class="num">1</span><a href="#v1">Eleven Names</a></li>
    <li><span class="num">2</span><a href="#v2">Victory to You</a></li>
    {''.join(f'<li><span class="num">{c[0].split("–")[0]}</span><a href="#c{k}">{c[2]}</a></li>' for k,c in enumerate(CARDS))}
    <li><span class="num">24</span><a href="#v24">A Companion for the Crossing</a></li>
    <li><span class="num">25</span><a href="#v25">Now Open the Book</a></li>
  </ul>
</section>
''',vpage(V1),vpage(V2)]
for k,c in enumerate(CARDS): b.append(cardpage(k,c))
b+= [vpage(V24),vpage(V25)]
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 3 ON ONE PAGE</h2>
  <div class="sub">The Argalā Stotram in five lines</div>
  <div class="steps">
    <div><b>Verses 1–2.</b> Eleven names, Jayantī to Svadhā, and three cries of victory to Cāmuṇḍā.</div>
    <div><b>Verses 3–6.</b> Her four great victories: Madhu-Kaiṭabha, Mahiṣa, Raktabīja with Caṇḍa-Muṇḍa, Śumbha-Niśumbha.</div>
    <div><b>Verses 7–17.</b> For those who bow, praise and worship: give health, strength, welfare, learning and fame.</div>
    <div><b>Verses 18–23.</b> Brahmā, Kṛṣṇa, Śiva and Indra all praise her; she gives her devotees boundless joy.</div>
    <div><b>Verses 24–25.</b> A companion for life’s crossing; then, the bolt lifted, read the Saptaśatī.</div>
  </div>
  {talk("What comes next?","Part 4: the Kīlakam, the 'pin'. Why is the Saptaśatī said to be locked, and who locked it?")}
  <div class="key">Part 3: <b>rūpaṃ dehi, jayaṃ dehi, yaśo dehi, dviṣo jahi</b>. 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Argalā Stotram, chanted before the Devī Māhātmya (Durgā Saptaśatī). Text checked word by word against shlokam.org (25 verses). The inner readings of the refrain are those of later teachers and are given as such. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('/home/claude/work/devim/Devi_Mahatmya_Part03.html','w').write(head+''.join(b)+tail())
print('ok')
