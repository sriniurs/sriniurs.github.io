exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Dhūmāvatī · Daśa Mahāvidyā 7 · srini.presents',
 'Dhūmāvatī, the Smoky One, the seventh of the Daśa Mahāvidyā: the widow Goddess on the crow-bannered chariot, the story of Satī swallowing Śiva, Nirṛti, Jyeṣṭhā and Alakṣmī, the winnowing basket, and her temples at Kāśī and the Pītāmbarā Pīṭha, Datiā. An illustrated reference guide.')
def CROW(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.5"><path d="M-16 0 q10 -14 26 -6 l10 -2 l-8 6 q-4 10 -20 8 l-10 8z" fill="#222"/><circle cx="6" cy="-6" r="1.6" fill="#fff"/></g>'
def DHUMA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-30 50 q-4 -54 30 -66 q34 12 30 66z" fill="#eeeeee"/>'
 '<path d="M-22 -8 l-28 -10 M22 -8 l26 -18" stroke="#9a9a9a" stroke-width="7"/>'
 '<path d="M-64 -24 q14 -12 28 0 q-14 14 -28 0z" fill="#c9a26b"/><path d="M-60 -24 h20 M-58 -20 h16" stroke="#8a6a3a"/>'
 '<path d="M48 -26 l8 -10" stroke="#9a9a9a" stroke-width="6"/>'
 '<path d="M-16 -44 q-14 30 -8 56 M16 -44 q14 30 8 56" stroke="#555" stroke-width="5" fill="none"/>'
 '<circle cy="-36" r="15" fill="#9a9a9a"/><path d="M-15 -42 q15 -16 30 0" fill="#f2f2f2"/>'
 '<circle cx="-5" cy="-36" r="2.4" fill="#111"/><circle cx="5" cy="-36" r="2.4" fill="#111"/><path d="M-8 -30 q2 -2 4 0 M4 -30 q2 -2 4 0" fill="none"/><path d="M-6 -26 q6 -3 12 0" fill="none"/></g>')
def CHARIOT(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-70 40 h140 l-10 -20 h-120z" fill="#6a5a4a"/>'
 '<circle cx="-40" cy="46" r="16" fill="#8a7a6a"/><circle cx="40" cy="46" r="16" fill="#8a7a6a"/><path d="M60 20 v-90" stroke-width="3"/><path d="M60 -70 h40 l-8 12 l8 12 h-40z" fill="#555"/>'+CROW(80,-58,.7)+DHUMA(0,-10,.8)+'</g>')
def SMOKE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" fill="#8a8a8a" opacity=".55"><circle r="30"/><circle cx="26" cy="-20" r="24"/><circle cx="-24" cy="-26" r="22"/><circle cx="6" cy="-46" r="20"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="An old grey-haired widow goddess with a winnowing basket riding a horseless chariot with a crow banner, wrapped in smoke">'
 '<rect width="380" height="268" fill="#2a2a30" rx="8"/>'+SMOKE(80,120,1.4)+SMOKE(300,100,1.6)+SMOKE(190,60,1.2)+CHARIOT(180,170,1.25)+CROW(60,40,1.2)+CROW(330,210,1)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Dhūmāvatī</b>: “the smoky one”'),
 ('Place','<b>Seventh</b> of the ten Mahāvidyās'),
 ('She is','The Goddess as <b>loss, old age and emptiness</b>: what is left when everything else is gone'),
 ('Look','An old, grey widow in white or soiled clothes; trembling hands; a winnowing basket; a boon-giving gesture'),
 ('Vehicle','A horseless chariot with a <b>crow</b> on its banner, or the crow itself'),
 ('Consort','None: she is the only widow among the Mahāvidyās'),
 ('Kin','Linked with the older goddesses <b>Nirṛti, Jyeṣṭhā and Alakṣmī</b>'),
 ('Temples','Kāśī; the Pītāmbarā Pīṭha at Datiā; Kāmākhyā')])
 +talk("Why would anyone worship misfortune?","You cannot wish it away. Better to know her face, and ask for her blessing too.")))
pages.append(page('names','HER NAMES','Smoke, widow, elder',facts([
 ('Dhūmāvatī','From <i>dhūma</i>, smoke: “she who is made of smoke”'),
 ('Dhūmrā','“The smoke-coloured”'),
 ('Vidhavā','The widow'),
 ('Jyeṣṭhā','“The elder”: a commentator on the Śāradātilaka Tantra identifies her with Jyeṣṭhā'),
 ('Dhūmāvatī Mā','Her name at Kāśī, as a protective mother')])
 +talk("A goddess made of smoke?","Smoke is what remains after the fire. She comes after everything has burned.")))
pages.append(page('form','HER FORM','The old widow',fig(560,210,'An old widow goddess in white on a horseless chariot with a crow banner, holding a winnowing basket',
 '<rect width="560" height="210" fill="#eeeef2"/>'+SMOKE(120,100,1)+SMOKE(450,90,1)+CHARIOT(280,120,1.2))+facts([
 ('Age','Old, thin, wrinkled, with grey dishevelled hair'),
 ('Colour','Smoky or dark, “like black clouds at the time of dissolution”'),
 ('Hands','Trembling: one holds a <b>winnowing basket</b>, one gives boons'),
 ('Dress','White or dirty clothes, the dress of a widow'),
 ('Crow','On her banner, or as her mount: a carrion bird, a sign of death'),
 ('Mood','Always hungry, always thirsty, never satisfied')])))
pages.append(page('swallow','THE GODDESS WHO ATE ŚIVA','The Prāṇatoṣiṇī Tantra story',fig(560,160,'A hungry goddess in the Himalaya facing Shiva seated in meditation',
 '<rect width="560" height="160" fill="#dfe8f4"/>'+'<path d="M0 160 L70 60 L130 110 L200 40 L300 120 L400 50 L480 100 L560 70 V160Z" fill="#c8d8e8" stroke="#111" stroke-width="2"/><path d="M190 52 l10 -12 l10 12 M390 62 l10 -12 l10 12" stroke="#fff" stroke-width="4" fill="none"/>'+SHIVA(360,80,.9)+BODY(200,96,.8,'#9a9a9a','#eeeeee',True))+'''<div class="steps">
<div><b>Hunger.</b> Satī, living with Śiva in the Himālaya, grew terribly hungry and asked him for food. He did not give it.</div>
<div><b>The swallow.</b> “Then I will eat you,” she said, and swallowed him. Smoke poured from her body.</div>
<div><b>The curse.</b> Śiva asked to be let out, and she released him. He then rejected her and said she would take the form of a widow: Dhūmāvatī.</div>
</div>'''+talk("She made herself a widow?","By her own act. Some read it as anger; others as a woman who needs no one.")))
pages.append(page('smoke','OTHER TELLINGS','Sources differ',facts([
 ('Satī’s pyre','Some say she rose from the smoke of Satī’s body burning in Dakṣa’s fire'),
 ('Durgā’s helper','An oral legend says Durgā created her in the battle with Śumbha and Niśumbha'),
 ('Kālī’s version','Another telling has Kālī, not Satī, swallow Śiva'),
 ('Ten forms','With the other Mahāvidyās, she appeared when Satī blocked Śiva’s path; she stands in the south-east'),
 ('Late arrival','She has no known history before the Mahāvidyā lists, which Kinsley places no earlier than the 12th century')])))
pages.append(page('elders','HER OLDER SISTERS','Nirṛti, Jyeṣṭhā, Alakṣmī',facts([
 ('Nirṛti','Vedic goddess of decay, need and bad luck; hymns ask her to stay away'),
 ('Jyeṣṭhā','“The elder”, sister of Lakṣmī: dark, ugly, with a crow banner; once widely worshipped in South India'),
 ('Alakṣmī','“Not-Lakṣmī”, the opposite of good fortune'),
 ('The difference','Jyeṣṭhā is married; Dhūmāvatī is always a widow'),
 ('Also','Linked with the four rainy months (Cāturmāsya), the inauspicious season')])
 +talk("So Lakṣmī has an ugly elder sister?","In the old stories, yes. In Bengal, Alakṣmī is even sent out of the house before Lakṣmī is welcomed.")))
pages.append(page('basket','THE BASKET AND THE CROW','Reading her symbols',facts([
 ('Winnowing basket','Separates grain from husk: the wisdom to tell the real from the passing'),
 ('Crow','A bird that eats the dead: the end that comes to all'),
 ('Horseless chariot','She goes nowhere, yet she is everywhere'),
 ('Widowhood','No partner, no home: the state of the renouncer who has let go'),
 ('Hunger','The emptiness that no worldly thing can fill')])
 +talk("A basket is wisdom?","Shake life hard enough and the husk blows away. What stays is the grain.")))
pages.append(page('who','WHO WORSHIPS HER','For those outside the household',facts([
 ('Ideal devotees','Bachelors, widows, renouncers and Tantric practitioners'),
 ('Householders','Traditionally keep their distance; her worship is quiet and private'),
 ('Places','Cremation grounds, forests and deserts are her haunts'),
 ('Seventh wisdom','After Chinnamastā gives herself away, Dhūmāvatī is what is left: emptiness')])
 +'<div class="key">Previous: <a href="'+MVS+'chinnamasta/">Chinnamastā</a></div>'))
pages.append(page('kashi','DHŪMĀVATĪ AT KĀŚĪ','The protective grandmother',facts([
 ('Kāśī','Her temple in Vārāṇasī is among the very few dedicated to her alone'),
 ('A change','Here she sheds her bad name and becomes a local protector'),
 ('Who comes','Even married couples worship her here, unlike elsewhere')])
 +talk("The scary widow becomes a grandmother?","In Kāśī, yes. Nearness makes even the fierce ones family.")+'<div class="key">More Kāśī: <a href="'+MVS+'bhairavi/">Tripurabhairavī</a></div>'))
pages.append(page('datia','THE PĪTĀMBARĀ PĪṬHA, DATIĀ','Two Mahāvidyās under one roof',fig(560,160,'A temple complex on a low hill with a yellow banner and a smaller grey shrine beside it',
 '<rect width="560" height="160" fill="#fff8d8"/><path d="M0 160 q280 -80 560 0z" fill="#d8c8a8" stroke="#111"/>'
 +'<g transform="translate(220 100)" stroke="#111" stroke-width="2"><rect x="-60" y="-30" width="120" height="30" fill="#ffd60a"/><path d="M-40 -30 l40 -40 l40 40z" fill="#e0a800"/></g>'
 +'<g transform="translate(380 108)" stroke="#111" stroke-width="2"><rect x="-34" y="-24" width="68" height="24" fill="#d8d8d8"/><path d="M-24 -24 l24 -26 l24 26z" fill="#9a9a9a"/></g>'+CROW(380,40,1))+facts([
 ('Where','Datiā, Madhya Pradesh, on a low hill at the edge of the town'),
 ('Founder','A Swāmījī who settled in Datiā in the 1920s and set up the Pītāmbarā Pīṭha of Bagalāmukhī'),
 ('Dhūmāvatī','He also founded a temple of Dhūmāvatī inside the same āśrama'),
 ('Rare pair','Two Mahāvidyās, Bagalāmukhī and Dhūmāvatī, worshipped in one complex'),
 ('Also','The Vanakhaṇḍeśvara Śiva temple, said to date from the Mahābhārata age')])))
pages.append(page('festivals','THROUGH THE YEAR','Her days',facts([
 ('Dhūmāvatī Jayantī','Jyeṣṭha Śukla Aṣṭamī (May–June)'),
 ('Navarātri','Both seasons, with the other Mahāvidyās'),
 ('Gupta Navarātri','Kept by Tantric worshippers'),
 ('Saturdays','The big day at Datiā')])))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of emptiness',facts([
 ('Face loss','Old age, grief and want come to everyone; she teaches us to look at them'),
 ('Let go','The widow and the renouncer have nothing left to lose'),
 ('Discernment','Winnow: keep the grain, let the husk fly'),
 ('Hidden grace','Her other hand still gives boons')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Dhūma','Smoke'),('Vidhavā','Widow'),('Śūrpa','Winnowing basket'),('Kāka','Crow'),('Nirṛti','Vedic goddess of decay'),('Jyeṣṭhā','The elder goddess'),('Alakṣmī','Misfortune'),('Cāturmāsya','The four rainy months')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Dhūmāvatī, the Smoky One, seventh Mahāvidyā: the widow Goddess.</div>
<div><b>Form.</b> Old, grey, trembling; winnowing basket; crow-bannered chariot.</div>
<div><b>Story.</b> Hungry Satī swallowed Śiva and was cursed to be a widow.</div>
<div><b>Kin and temples.</b> Nirṛti, Jyeṣṭhā, Alakṣmī; Kāśī; Datiā.</div>
<div><b>Lesson.</b> Look at loss; winnow; let go.</div>
</div>'''+talk("One line to remember?","When the fire has burned out, the smoke still teaches.")+'<div class="key">The seventh Great Wisdom: <b>Dhūmāvatī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Goddess:</b> D. Kinsley, <i>Tantric Visions of the Divine Feminine</i> (1997), ch. on Dhūmāvatī (dhyāna: cloud-dark, wrinkled, crow-like; Nirṛti, Jyeṣṭhā, Alakṣmī; widowhood; Mahāvidyā concept not before 12th c.). Wikipedia, “Dhumavati” (winnowing basket, horseless chariot, crow; Prāṇatoṣiṇī Tantra story; oral legend of Durgā; Kālī variant; south-east direction; Śāradātilaka commentator on Jyeṣṭhā; Cāturmāsya; devotees; Vārāṇasī temple as protective deity worshipped by married couples). Metropolitan Museum (winnowing tray as her identifier).</p>
<p><b>Datiā:</b> Wikipedia, “Pitambara Peeth”; Incredible India (Bagalāmukhī and Dhūmāvatī in one complex; 1920s); Wikipedia, “Datia” (Vanakhaṇḍeśvara).</p>
<p><b>Sources differ / unverified:</b> the pyre-smoke origin and Durgā legend are oral or regional; Jayantī date follows common almanacs; Saturday crowds at Datiā are reported by visitors. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('form','Her Form'),('swallow','The Goddess Who Ate Śiva'),('smoke','Other Tellings'),('elders','Her Older Sisters'),('basket','The Basket and the Crow'),
 ('who','Who Worships Her'),('kashi','Dhūmāvatī at Kāśī'),('datia','The Pītāmbarā Pīṭha, Datiā'),('festivals','Through the Year'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 7 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,7vw,70px)">DHŪMĀVATĪ</h1>
  <div class="series">DAŚA MAHĀVIDYĀ · A REFERENCE GUIDE</div>
  <div class="tag">The smoky widow Goddess</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Every other Goddess in this series is young, beautiful or terrible in her power. The seventh Great Wisdom, <b>Dhūmāvatī</b>, is old. She is a grey, trembling widow on a horseless chariot, a crow on her banner, a winnowing basket in her hand, forever hungry.</p>
    <p>The Tantra says she became a widow by swallowing Śiva himself. She is kin to the old goddesses of misfortune, and householders keep their distance. Yet in Kāśī she is a protecting grandmother, and at Datiā she shares a shrine with Bagalāmukhī.</p>
    <p>This guide tells her stories, her meaning and her temples.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Dhūmāvatī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is she unlucky to read about?","No. She is the Goddess who sits with you when things go wrong.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms. Previous: <a href="{MVS}chinnamasta/">Chinnamastā</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV07_Dhumavati.html','w').write(head+b+tail())
print('ok',len(pages))
