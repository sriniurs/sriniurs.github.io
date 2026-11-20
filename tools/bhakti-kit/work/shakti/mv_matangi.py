exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Mātaṅgī · Daśa Mahāvidyā 9 · srini.presents',
 'Mātaṅgī, Rāja-Mātaṅgī and Ucchiṣṭa-Mātaṅgī, the ninth of the Daśa Mahāvidyā: the green Goddess of speech, music and the sixty-four arts, the Tantric Sarasvatī, born from the leftovers of the gods, Śyāmalā the minister of Lalitā, Kālidāsa’s Śyāmalā Daṇḍakam, and her temple at Modhera. An illustrated reference guide.')
def PARROT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.5"><path d="M-8 10 q-6 -16 6 -24 q12 4 10 18 l-4 20z" fill="#2ac06f"/><path d="M2 -14 q8 -2 8 6 l-5 -1z" fill="#e04040"/><circle cx="0" cy="-10" r="1.6" fill="#111"/></g>'
def VEENA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-60 0 h120" stroke="#7a4a1a" stroke-width="6"/><circle cx="-60" cy="6" r="14" fill="#c9a26b"/><circle cx="50" cy="8" r="11" fill="#c9a26b"/><path d="M-50 -3 h100" stroke="#ddd" stroke-width="1"/></g>'
def MAT(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-60 54 q60 -30 120 0" fill="#e0115f"/><path d="M-30 50 q-4 -54 30 -66 q34 12 30 66z" fill="#c0392b"/>'
 +VEENA(0,8,.8)+'<path d="M-22 -8 l-26 14 M22 -8 l24 14" stroke="#2a9d6f" stroke-width="7"/>'
 '<circle cy="-36" r="15" fill="#2a9d6f"/><path d="M-14 -48 h28 l-4 -16 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/><path d="M-5 -68 a8 8 0 1 0 11 3" fill="none" stroke="#fff8c0" stroke-width="2.5"/>'
 '<circle cx="-5" cy="-38" r="2.4" fill="#fff"/><circle cx="5" cy="-38" r="2.4" fill="#fff"/><path d="M-3 -46 h6" stroke="#ffd60a" stroke-width="2"/><path d="M-6 -29 q6 4 12 0" fill="none"/>'
 +PARROT(-42,-44,.9)+'</g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The emerald-green goddess Matangi playing a veena with a parrot on her shoulder, musical notes around her">'
 '<rect width="380" height="268" fill="#0e3a2a" rx="8"/>'+''.join(f'<text x="{30+(i*67)%330}" y="{40+(i*41)%200}" font-size="22" fill="#9fe0c0">♪</text>' for i in range(10))+MAT(190,160,1.35)+PARROT(320,230,1.3)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Mātaṅgī</b>: “daughter of Mātaṅga”'),
 ('Place','<b>Ninth</b> of the ten Mahāvidyās'),
 ('She rules','<b>Speech, music, learning and the sixty-four arts</b>: she is called the Tantric Sarasvatī'),
 ('Look','Emerald-green or dark blue; crescent moon; plays a <b>vīṇā</b>; often with a <b>parrot</b>'),
 ('Two forms','<b>Rāja-Mātaṅgī</b>, the royal musician; <b>Ucchiṣṭa-Mātaṅgī</b>, Goddess of the leftovers'),
 ('Śrīvidyā','As <b>Śyāmalā</b>, she is the minister (mantriṇī) of Lalitā Tripurasundarī'),
 ('Offering','Unusually, <i>ucchiṣṭa</i>: food already tasted'),
 ('Temple','Mātaṅgī Modheśvarī, Modhera, Gujarat')])
 +talk("A Goddess who wants leftovers?","The gods' leftovers. She turns what others throw away into grace.")))
pages.append(page('names','HER NAMES','Green, dark and royal',facts([
 ('Mātaṅgī','Daughter of the sage Mātaṅga; the word also hints at <i>mātaṅga</i>, elephant, and at forest peoples'),
 ('Rāja-Mātaṅgī','The royal Mātaṅgī with the vīṇā'),
 ('Ucchiṣṭa-Mātaṅgī · Ucchiṣṭa-Cāṇḍālinī','She of the leftovers; the outcaste woman'),
 ('Śyāmalā','“The dark one”, her Śrīvidyā name'),
 ('Mantriṇī','The minister of Lalitā'),
 ('Sumukhī','“Fair-faced”: another of her forms')])
 +talk("Royal and outcaste in one?","That's her secret. The palace and the cremation ground are both hers.")))
pages.append(page('form','HER FORM','Two Mātaṅgīs',fig(560,200,'A green goddess playing a veena with a parrot, seated on a red cushion',
 '<rect width="560" height="200" fill="#e4f6ec"/>'+MAT(280,130,1.25)+PARROT(140,170,1.2)+PARROT(420,170,1.2))+facts([
 ('Rāja-Mātaṅgī','Green, crescent-crowned, playing a ruby-studded vīṇā; seated on an altar flanked by two parrots; conch earrings and flower garlands'),
 ('Ucchiṣṭa-Mātaṅgī','Carries a noose, sword, goad and club'),
 ('Other texts','Some describe her as blue, with a skull bowl and sword'),
 ('Parrot','Repeats speech: the bird of words'),
 ('Vīṇā','The instrument of Sarasvatī: music and learning')])))
pages.append(page('leftovers','BORN FROM LEFTOVERS','The Ucchiṣṭa story',fig(560,160,'Four deities at a feast, morsels fallen on the ground, and a green maiden rising from them',
 '<rect width="560" height="160" fill="#fff4dc"/><rect x="60" y="100" width="440" height="20" fill="#c9a26b" stroke="#111" stroke-width="2"/>'+''.join(person(x,70,c,'#f2c79b',.6) for x,c in ((110,'#3b6fd0'),(190,'#e0115f'),(370,'#5b8fe0'),(450,'#e05a3a')))
 +''.join(f'<circle cx="{250+i*14}" cy="140" r="4" fill="#e0a800" stroke="#111"/>' for i in range(5))+BODY(280,90,.6,'#2a9d6f','#2a9d6f'))+'''<div class="steps">
<div><b>The feast.</b> Viṣṇu and Lakṣmī visited Śiva and Pārvatī, and a banquet of fine food was served.</div>
<div><b>The fallen food.</b> As the gods ate, some food fell to the ground. From it rose a beautiful maiden, who asked for their leftovers.</div>
<div><b>The blessing.</b> The four gave her their leftovers as prasāda. Śiva declared that worship of her would bear fruit, and that leftovers offered to her are sacred. She is Ucchiṣṭa-Mātaṅgī.</div>
</div>'''+talk("So the gods' plates made a Goddess?","What touched the gods became holy. She is that holiness, rising from the floor.")))
pages.append(page('tellings','OTHER TELLINGS','Sources differ',facts([
 ('Sage’s daughter','The sage Mātaṅga won a boon that the Divine Mother would be born as his daughter: Mātaṅgī'),
 ('Pārvatī in disguise','In another story Pārvatī comes to Śiva as a Cāṇḍāla (outcaste) woman, and he is drawn to her'),
 ('Huntress','The Svatantra Tantra has her help Mātaṅga subdue all creatures; scholars link her with hunter and forest peoples'),
 ('Ten forms','When Satī blocked Śiva’s path, Mātaṅgī stood in the north-west'),
 ('Avatāras','The Muṇḍamālā list pairs her with the Buddha; others with Rāma')])))
pages.append(page('sarasvati','THE TANTRIC SARASVATĪ','Speech and the arts',facts([
 ('Speech','She rules the spoken word, from the first sound to eloquence'),
 ('Music','The vīṇā is hers; musicians honour her'),
 ('Sixty-four arts','Music, dance, painting, poetry and the rest: all are hers'),
 ('Difference','Sarasvatī is pure and white; Mātaṅgī embraces the impure and the outsider'),
 ('Ninth wisdom','After Bagalāmukhī stills speech, Mātaṅgī gives it')])
 +talk("Two Goddesses of speech in a row?","One stops false speech, the next gives true speech. A neat pair.")))
pages.append(page('shyamala','ŚYĀMALĀ, THE MINISTER','Her place in Śrīvidyā',fig(560,160,'A green goddess on horseback with a veena leading an army before a queen on a throne',
 '<rect width="560" height="160" fill="#f2e6ff"/><g transform="translate(420 100)" stroke="#111" stroke-width="2"><rect x="-40" y="-20" width="80" height="60" fill="#e0a800"/></g>'+BODY(420,70,.7,'#f2a07a','#c0392b')+MAT(180,100,.7))+facts([
 ('Mantriṇī','In the Lalitopākhyāna she is Lalitā’s chief counsellor and minister'),
 ('In battle','She leads the army against Bhaṇḍāsura alongside Vārāhī, the commander'),
 ('Lalitā Sahasranāma','Praises Lalitā as pleased when Mantriṇī Ambā slew Viṣaṅga, Bhaṇḍa’s brother'),
 ('Kālidāsa','The <b>Śyāmalā Daṇḍakam</b>, ascribed to the poet, praises her ruby-studded vīṇā and sweet speech'),
 ('Navarātri','Śyāmalā Navarātri is kept in Māgha by some Śrīvidyā families')])
 +'<div class="key">See also: <a href="'+MVS+'tripurasundari/">Tripurasundarī</a></div>'))
pages.append(page('ucchishta','WHY LEFTOVERS?','Turning pollution upside down',facts([
 ('The rule','In orthodox practice, food touched by the mouth is impure, never offered to a deity'),
 ('Her rule','To Mātaṅgī, devotees offer ucchiṣṭa: the order is reversed'),
 ('Outsiders','She belongs to the edges: forests, outcastes, those left over'),
 ('Meaning','Some say she is herself the “leftover”: the Self that remains when all else perishes'),
 ('Lesson','Nothing and no one is beneath the Goddess')])
 +talk("Isn't that against all the rules?","On purpose. Tantra breaks a rule to show that the divine is everywhere.")))
pages.append(page('modhera','MĀTAṄGĪ MODHEŚVARĪ','Modhera, Gujarat',fig(560,160,'A white temple beside the ruins of a stepped sun temple tank',
 '<rect width="560" height="160" fill="#fff4dc"/>'+''.join(f'<rect x="{60+k*12}" y="{150-k*12}" width="{200-k*24}" height="12" fill="#d8b888" stroke="#111"/>' for k in range(6))
 +'<g transform="translate(400 130)" stroke="#111" stroke-width="2"><rect x="-60" y="-40" width="120" height="40" fill="#f2f2f2"/><path d="M-40 -40 l40 -50 l40 50z" fill="#e8e0d0"/><path d="M0 -90 v-14 l14 5 l-14 5" fill="#e04040"/></g>')+facts([
 ('Where','Modhera, North Gujarat, beside the famous Sun Temple'),
 ('Goddess','Modheśvarī, called <b>Mātaṅgī</b> because the sage Mātaṅga worshipped her'),
 ('Clan goddess','Kuladevī of the Modh communities'),
 ('Legend','She appeared to destroy a demon, Karṇāṭa, who troubled the brahmins at prayer'),
 ('History','Damaged in the invasions of the 13th–14th c.; the present temple was built 1962–66'),
 ('Navarātri','A major state-supported festival')])))
pages.append(page('south','IN THE SOUTH','Madurai and beyond',facts([
 ('Madurai','Śrīvidyā tradition sees <b>Mīnākṣī</b>, green and parrot-bearing, as Rāja-Mātaṅgī'),
 ('Śrīvidyā homes','Śyāmalā is worshipped alongside Lalitā and Vārāhī'),
 ('Hampi','The Mātaṅga hill at Hampi is named for the sage Mātaṅga of the Rāmāyaṇa, not for the Goddess'),
 ('Musicians','Carnatic musicians traditionally honour her as the Goddess of music')])
 +talk("Mīnākṣī is Mātaṅgī?","In Śrīvidyā reading, yes: the green Queen with the parrot. The temple's own tradition calls her Mīnākṣī.")))
pages.append(page('festivals','THROUGH THE YEAR','Her days',facts([
 ('Mātaṅgī Jayantī','Vaiśākha Śukla Tṛtīyā (Akṣaya Tṛtīyā), April–May'),
 ('Śyāmalā Navarātri','Māgha (January–February), the “hidden” Navarātri'),
 ('Navarātri','Both seasons; the great festival at Modhera'),
 ('Vasanta Pañcamī','Sarasvatī’s day; many honour Mātaṅgī too')])))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of the word',facts([
 ('Speak well','Words are sacred; the arts are worship'),
 ('Include','The outsider and the leftover belong to the Goddess too'),
 ('Learn','The sixty-four arts are paths to her'),
 ('Counsel','Wisdom serves power: she is the queen’s minister')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Ucchiṣṭa','Leftover, tasted food'),('Cāṇḍāla','Outcaste'),('Vīṇā','Stringed instrument'),('Mantriṇī','Minister, counsellor'),('Śyāmalā','The dark one'),('Prasāda','Food blessed by a deity'),('Daṇḍakam','A long hymn in prose-like metre'),('Kuladevī','Clan goddess')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Mātaṅgī, ninth Mahāvidyā: Goddess of speech, music and the arts, the Tantric Sarasvatī.</div>
<div><b>Form.</b> Green, crescent-crowned, vīṇā and parrot; or with noose, sword, goad and club.</div>
<div><b>Story.</b> Born from the leftovers of Śiva, Pārvatī, Viṣṇu and Lakṣmī.</div>
<div><b>Śrīvidyā and temples.</b> Śyāmalā, Lalitā’s minister; Modhera; Madurai in tradition.</div>
<div><b>Lesson.</b> Nothing is beneath the divine; every word is sacred.</div>
</div>'''+talk("One line to remember?","She makes music out of what the world throws away.")+'<div class="key">The ninth Great Wisdom: <b>Mātaṅgī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Goddess:</b> D. Kinsley, <i>Tantric Visions of the Divine Feminine</i> (1997), ch. on Mātaṅgī (leftovers story and prasāda; Śaktisaṅgama Tantra; Svatantra Tantra and Mātaṅga; Śāradātilaka). Wikipedia, “Matangi” (names; Rāja- and Ucchiṣṭa-Mātaṅgī; green and blue dhyānas; vīṇā and parrots; 64 arts; Kālidāsa’s Śyāmalā Daṇḍakam; north-west; Muṇḍamālā and the Buddha; leftover as the remaining Self). Wikipedia, “Mahavidya” (Prime Minister of Lalitā; Tantric Sarasvatī). Drik Panchang.</p>
<p><b>Modhera:</b> Incredible India and Government of India Utsav portal (Modheśvarī, sage Mātaṅga, demon Karṇāṭa, kuladevī); pilgrimdata.in (13th–14th c. damage; rebuilt 1962–66).</p>
<p><b>Sources differ / unverified:</b> the Mīnākṣī–Rāja-Mātaṅgī identification is a Śrīvidyā reading, not the temple’s official account; Jayantī date follows common almanacs; avatāra pairings differ; the Śyāmalā Daṇḍakam’s authorship by Kālidāsa is traditional. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('form','Her Form'),('leftovers','Born from Leftovers'),('tellings','Other Tellings'),('sarasvati','The Tantric Sarasvatī'),('shyamala','Śyāmalā, the Minister'),
 ('ucchishta','Why Leftovers?'),('modhera','Mātaṅgī Modheśvarī'),('south','In the South'),('festivals','Through the Year'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 9 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7.6vw,74px)">MĀTAṄGĪ</h1>
  <div class="series">DAŚA MAHĀVIDYĀ · A REFERENCE GUIDE</div>
  <div class="tag">The green Goddess of speech and music</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Bagalāmukhī stops the tongue. The ninth Great Wisdom, <b>Mātaṅgī</b>, sets it free. She is emerald-green, plays the vīṇā with a parrot at her side, and rules speech, music and the sixty-four arts: the Tantric Sarasvatī.</p>
    <p>Yet she was born from the food the gods left on their plates, and devotees offer her leftovers that no other deity would accept. In Śrīvidyā she is Śyāmalā, the minister of Queen Lalitā, praised in a hymn ascribed to Kālidāsa.</p>
    <p>This guide tells her stories, her meaning and her temples.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mātaṅgī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is she like Sarasvatī?","Sarasvatī in green, who also eats with the outcastes.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms. Previous: <a href="{MVS}bagalamukhi/">Bagalāmukhī</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV09_Matangi.html','w').write(head+b+tail())
print('ok',len(pages))
