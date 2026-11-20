exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Chinnamastā · Daśa Mahāvidyā 6 · srini.presents',
 'Chinnamastā or Chinnamastikā, Pracaṇḍa Caṇḍikā, the sixth of the Daśa Mahāvidyā: the self-beheaded Goddess who feeds her attendants Ḍākinī and Varṇinī, the Prāṇatoṣiṇī Tantra story, Kāma and Rati, the three streams and kuṇḍalinī, the Buddhist Chinnamuṇḍā, and the Rajrappa temple in Jharkhand. An illustrated reference guide.')
def CHIN(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<ellipse cy="64" rx="70" ry="12" fill="#e0115f"/><path d="M-30 60 q-4 -60 30 -70 q34 10 30 70z" fill="#e05a3a"/>'
 '<path d="M-24 -4 q24 24 48 0" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="3 4"/><path d="M-12 -14 q12 30 0 60" stroke="#2a9d6f" stroke-width="3" fill="none"/>'
 '<path d="M24 -6 l26 -24" stroke="#e05a3a" stroke-width="7"/><path d="M50 -30 l10 -16" stroke="#bbb" stroke-width="4"/>'
 '<path d="M-24 -6 l-30 -20" stroke="#e05a3a" stroke-width="7"/>'
 '<rect x="-8" y="-14" width="16" height="6" fill="#e05a3a"/>'
 '<path d="M0 -14 q-20 -30 -46 -30" stroke="#c0392b" stroke-width="4" fill="none"/><path d="M-4 -14 q-44 -24 -78 24" stroke="#c0392b" stroke-width="3" fill="none"/><path d="M4 -14 q44 -24 78 24" stroke="#c0392b" stroke-width="3" fill="none"/>'
 '<g transform="translate(-58 -46)"><circle r="13" fill="#e05a3a"/><path d="M-12 -10 h24 l-4 -14 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/><circle cx="-5" cy="-2" r="2.2" fill="#fff"/><circle cx="5" cy="-2" r="2.2" fill="#fff"/><path d="M-12 4 q-6 14 -2 24 M12 4 q6 14 2 24" stroke="#111" stroke-width="4" fill="none"/></g></g>')
def ATT(x,y,c,s=.6): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-20 60 q-2 -54 20 -62 q22 8 20 62z" fill="{c}"/><circle cy="-14" r="12" fill="{c}"/><circle cx="-4" cy="-16" r="2" fill="#111"/><circle cx="4" cy="-16" r="2" fill="#111"/><path d="M-12 -20 q-8 20 -4 40 M12 -20 q8 20 4 40" stroke="#111" stroke-width="4" fill="none"/></g>'
def SCENE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+ATT(-80,24,'#f2f2f2')+ATT(80,24,'#3a3a5a')+CHIN(0,0,1)+'</g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The red goddess Chinnamasta holding her own crowned head, three streams flowing to her head and two attendants, standing on a lotus">'
 '<rect width="380" height="268" fill="#1a0a14" rx="8"/>'+''.join(f'<circle cx="{(i*53)%380}" cy="{(i*29)%268}" r="1.4" fill="#fff"/>' for i in range(30))+SCENE(190,160,1.25)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Chinnamastā</b>: “she whose head is severed”; also Chinnamastikā, <b>Pracaṇḍa Caṇḍikā</b>'),
 ('Place','<b>Sixth</b> of the ten Mahāvidyās'),
 ('Look','Red as a hibiscus; she holds her own head in one hand and a blade in the other'),
 ('Three streams','From her neck flow three streams: one to her own head, two to her attendants <b>Ḍākinī</b> and <b>Varṇinī</b>'),
 ('Beneath her','<b>Kāma</b> and <b>Rati</b>, god and goddess of desire, on a lotus'),
 ('Sect','Worshipped in the Kālīkula stream of Śāktism'),
 ('Buddhist twin','<b>Chinnamuṇḍā</b>, the severed-head form of Vajrayoginī'),
 ('Temple','<b>Rajrappa</b>, Jharkhand, where two rivers meet')])
 +talk("A Goddess who cuts off her own head? Why?","To feed others. It is the most shocking image of giving in all of Hindu art.")))
pages.append(page('names','HER NAMES','Severed head, fierce Caṇḍikā',facts([
 ('Chinnamastā','<i>chinna</i> “cut” + <i>mastā</i> “head”'),
 ('Chinnamastikā','The name used at Rajrappa and Chintpūrṇī'),
 ('Pracaṇḍa Caṇḍikā','“Exceedingly fierce Caṇḍī”'),
 ('Joganī Mā','A western Indian name'),
 ('Sarvasiddhi','“All-accomplished”: her name in the Hindu Tantrasāra')])
 +talk("Is she a form of Kālī?","Part of the same Kālī family of fierce Goddesses, but with her own story.")))
pages.append(page('form','HER FORM','The image explained',fig(560,220,'The red goddess holding her own crowned head, three streams flowing to her head and to a white and a dark attendant, standing on a lotus',
 '<rect width="560" height="220" fill="#fde8e0"/>'+SCENE(280,130,1.2))+facts([
 ('Colour','Red as a hibiscus; naked, with loose hair'),
 ('Hands','Her own crowned head in the left, a curved blade (kartrī) in the right'),
 ('Ornaments','Garland of skulls; a serpent as her sacred thread'),
 ('Varṇinī','On her right: white, of <i>rajas</i> quality'),
 ('Ḍākinī','On her left: dark, of <i>tamas</i> quality'),
 ('Stance','Standing boldly, one leg forward, on Kāma and Rati')])))
pages.append(page('bath','THE BATH IN THE MANDĀKINĪ','Why she cut her head',fig(560,170,'A goddess and two companions bathing in a river, the companions looking hungry',
 '<rect width="560" height="170" fill="#bfe3f0"/><rect y="110" width="560" height="60" fill="#5a9ad0"/>'+ATT(200,94,'#f2f2f2',.7)+ATT(360,94,'#3a3a5a',.7)+BODY(280,90,.8,'#e05a3a','#e05a3a'))+'''<div class="steps">
<div><b>The bath.</b> The Prāṇatoṣiṇī Tantra tells that Pārvatī went to bathe in the Mandākinī river with her two companions, Jayā and Vijayā, also called Ḍākinī and Varṇinī.</div>
<div><b>The hunger.</b> Bathing, the Goddess grew dark with passion. Her companions grew hungry and begged her for food, again and again.</div>
<div><b>The gift.</b> Smiling, she cut off her own head. Three streams flowed: two into her companions’ mouths and one into her own. Then she returned to her form.</div>
</div>'''+talk("A mother feeding her children with herself?","That's how devotees read it. She gives her own life-force so that others live.")))
pages.append(page('sacrifice','OTHER TELLINGS','Sources differ',facts([
 ('War story','In another version she cut her head after a battle, to quench her helpers’ thirst for blood'),
 ('Mahāvidyā origin','With the other nine, she appeared when Satī showed her forms to Śiva before Dakṣa’s sacrifice'),
 ('Purāṇas','First named in the Mahābhāgavata Purāṇa (c. 950 CE) and the Devī Bhāgavata'),
 ('Avatāras','The Guhyātiguhya Tantra links her with Narasiṃha; the Muṇḍamālā with Paraśurāma'),
 ('Rarity','Her individual temples are few: her worship is thought powerful and best left to the trained')])))
pages.append(page('kama','STANDING ON DESIRE','Kāma and Rati',fig(560,150,'A red goddess standing on a lotus, under which two small figures lie',
 '<rect width="560" height="150" fill="#fff4cd"/><ellipse cx="280" cy="128" rx="160" ry="16" fill="#f2a6c0" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{150+i*26} 128 q13 -26 26 0" fill="#e0115f" stroke="#111" stroke-width="1.5"/>' for i in range(10))+'<path d="M220 118 h120" stroke="#3b6fd0" stroke-width="10"/><path d="M226 110 h108" stroke="#e05a3a" stroke-width="8"/>'+BODY(280,50,.8,'#e05a3a','#e05a3a',True))+facts([
 ('Kāma and Rati','God of love and his wife, together on a lotus beneath her'),
 ('Reading 1: mastery','She stands on desire: the mind controlling its urges'),
 ('Reading 2: energy','She draws her power from the life-force of desire itself'),
 ('Life, sex, death','Kinsley sees all three in one image: birth, passion and sacrifice')])
 +talk("Is she stopping desire or using it?","Teachers split on this. The answer might be both: desire, tamed and turned upward.")))
pages.append(page('kundalini','THREE STREAMS, THREE CHANNELS','A yogic reading',facts([
 ('Three channels','Iḍā, piṅgalā and suṣumnā, the three main nāḍīs of yoga'),
 ('The middle stream','Flowing to her own head: the suṣumnā, the central channel of kuṇḍalinī'),
 ('Severed head','Teachers read it as the ego cut away when the energy rises'),
 ('Ḍākinī and Varṇinī','Tamas and rajas; she herself is sattva'),
 ('Sixth wisdom','After Bhairavī’s fire, Chinnamastā’s total self-offering')])
 +talk("So the head she cuts is the ego?","That is the yogic reading. Cut the 'I', and the life-force flows freely.")))
pages.append(page('buddhist','CHINNAMUṆḌĀ','The Buddhist twin',facts([
 ('Who','The severed-head form of <b>Vajrayoginī</b> (or Vajravārāhī), in Tantric and Tibetan Buddhism'),
 ('Sādhanamālā','The Buddhist text calls her Sarvabuddhā, with attendants Vajravairocanī and Vajravarṇinī'),
 ('Two sisters','Mekhalā and Kanakhalā, disciples of Kṛṣṇācārya, cut off their heads, offered them to their guru, and danced'),
 ('Lakṣmīṅkarā','A princess-adept punished by the king, she carried her severed head through the city and was praised as Chinnamuṇḍā'),
 ('Origin debate','Scholar Benoytosh Bhattacharya argued the Hindu form came from the Buddhist one; Kinsley agrees but sees other influences too')])
 +talk("Hindu or Buddhist first?","Most scholars say the Buddhist form is older. Both traditions keep her.")))
pages.append(page('rajrappa','RAJRAPPA','Where two rivers meet',fig(560,170,'A temple on a hillock above a small waterfall where a smaller river joins a broader one',
 '<rect width="560" height="170" fill="#e8f4e0"/><path d="M0 140 Q200 120 560 150 V170 H0z" fill="#5a9ad0" stroke="#111"/><path d="M320 60 q20 40 10 80" stroke="#5a9ad0" stroke-width="16" fill="none"/><path d="M320 60 q20 40 10 80" stroke="#bfe3f0" stroke-width="4" fill="none" stroke-dasharray="6 6"/>'
 +'<path d="M120 140 q60 -60 140 0z" fill="#8ab070" stroke="#111"/><g transform="translate(190 96)" stroke="#111" stroke-width="2"><rect x="-30" y="-24" width="60" height="24" fill="#f2f2f2"/><path d="M-24 -24 q24 -46 48 0z" fill="#e8d8b8"/></g>'
 +'<text x="420" y="164" font-size="13">Damodar</text><text x="340" y="50" font-size="13">Bhairavī (Bherā)</text>')+facts([
 ('Where','Ramgarh district, Jharkhand, on a hillock where the <b>Bhairavī (Bherā)</b> falls into the <b>Damodar</b>'),
 ('Deity','A headless image of the Goddess standing on Kāma and Rati on a lotus'),
 ('Symbol','Devotees see the meeting of the rivers as her image: the active Bhairavī on the calm Damodar'),
 ('Complex','Shrines of the other Mahāvidyās, the Aṣṭamātṛkās, Dakṣiṇa Kālī, Śiva and Sūrya; its style is often compared with Kāmākhyā'),
 ('Rites','Kheer and animal sacrifice are offered; a large fair is held at Makara Saṅkrānti')])))
pages.append(page('temples','OTHER SHRINES','Himachal, Assam, Nepal',facts([
 ('Chintpūrṇī','Una district, Himachal Pradesh: the Goddess is worshipped as Chinnamastikā; counted as a Śakti Pīṭha by local tradition'),
 ('Kāmākhyā','She has her own shrine among the Mahāvidyā temples on Nīlācala'),
 ('Nepal','Chinnamastā temples, and Buddhist Chinnamuṇḍā images'),
 ('North India','Most of her few dedicated temples are in the north and east')])
 +'<div class="key">See also: <a href="/bhakti/temples-of-india/18-shakti-peethas/kamakhya/">Kāmākhyā</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','Her days',facts([
 ('Chinnamastā Jayantī','Vaiśākha Śukla Caturdaśī (April–May)'),
 ('Makara Saṅkrānti','The great bathing fair at Rajrappa'),
 ('Navarātri','Both seasons; Vijayadaśamī is kept at Rajrappa'),
 ('Mahāśivarātri','Also celebrated at Rajrappa')])))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of self-giving',facts([
 ('Give yourself','The highest gift is one’s own life-force'),
 ('Cut the ego','The head she holds is the “I” set aside'),
 ('Master desire','Stand on it; do not be ruled by it'),
 ('Life feeds life','Birth, love and death are one continuous stream')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Chinna','Cut, severed'),('Kartrī','Curved blade'),('Ḍākinī · Varṇinī','Her two attendants'),('Kāma · Rati','God of love · his wife'),('Nāḍī','Subtle channel'),('Suṣumnā','Central channel'),('Guṇa','Quality: sattva, rajas, tamas'),('Vajrayoginī','Buddhist Tantric goddess')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Chinnamastā, Pracaṇḍa Caṇḍikā, sixth Mahāvidyā: the self-beheaded Goddess.</div>
<div><b>Image.</b> Head in hand, three streams feeding herself and Ḍākinī and Varṇinī, standing on Kāma and Rati.</div>
<div><b>Story.</b> At the Mandākinī she fed her hungry companions with her own life.</div>
<div><b>Twin and temple.</b> Buddhist Chinnamuṇḍā; Rajrappa at the meeting of rivers.</div>
<div><b>Lesson.</b> Cut the ego; give yourself; master desire.</div>
</div>'''+talk("One line to remember?","The most frightening picture in the series is really a picture of giving.")+'<div class="key">The sixth Great Wisdom: <b>Chinnamastā</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Goddess:</b> D. Kinsley, <i>Tantric Visions of the Divine Feminine</i> (1997), ch. on Chinnamastā (dhyāna: hibiscus colour, Kāma and Rati, Varṇinī white and rajasic, Ḍākinī tamasic; Prāṇatoṣiṇī Tantra story at the Mandākinī). E. A. Benard, <i>Chinnamastā: The Aweful Buddhist and Hindu Tantric Goddess</i> (1994). Wikipedia, “Chhinnamasta” (names; Kālīkula; Chinnamuṇḍā; Sādhanamālā; Mekhalā and Kanakhalā; Lakṣmīṅkarā; Bhattacharya’s Buddhist-origin view; Mahābhāgavata c. 950 CE; avatāra links; rarity of temples).</p>
<p><b>Rajrappa:</b> Ramgarh district and Jharkhand Tourism official sites (confluence of Bhairavī and Damodar; resemblance to Kāmākhyā); Wikipedia, “Chhinnamasta Temple, Rajrappa” (image on Kāma and Rati; river symbolism; Mahāvidyā shrines; kheer and sacrifice; festivals).</p>
<p><b>Sources differ / unverified:</b> Chintpūrṇī’s identification as Chinnamastikā and as a Śakti Pīṭha is local tradition; the date of Chinnamastā Jayantī follows common almanacs. Meanings of Kāma and Rati differ between teachers. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('form','Her Form'),('bath','The Bath in the Mandākinī'),('sacrifice','Other Tellings'),('kama','Standing on Desire'),('kundalini','Three Streams, Three Channels'),
 ('buddhist','Chinnamuṇḍā'),('rajrappa','Rajrappa'),('temples','Other Shrines'),('festivals','Through the Year'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 6 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(20px,6.4vw,64px)">CHINNAMASTĀ</h1>
  <div class="series">DAŚA MAHĀVIDYĀ · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess who gives her own head</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>No image in Hindu art stops you like <b>Chinnamastā</b>. The sixth Great Wisdom holds her own severed head; three streams flow from her neck, into her own mouth and into the mouths of her two companions; she stands on the god and goddess of desire.</p>
    <p>Look longer and the horror turns into a lesson. In the Tantra’s story she cut her head to feed her hungry friends. Yogis read the three streams as the channels of kuṇḍalinī, and the severed head as the ego set aside. Buddhists know her too, as Chinnamuṇḍā.</p>
    <p>This guide tells her stories, her meaning and her temples, from Rajrappa to the Himalaya.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Chinnamastā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is this too scary to look at?","Look once, then read why. It is a picture of giving, not of harm.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms. Previous: <a href="{MVS}bhairavi/">Bhairavī</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV06_Chinnamasta.html','w').write(head+b+tail())
print('ok',len(pages))
