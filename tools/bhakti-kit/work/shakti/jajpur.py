exec(open('/home/claude/work/shakti/common_s.py').read())
psrc=open('/home/claude/work/shakti/pithapuram.py').read()
exec('def GAYASURA('+psrc.split('def GAYASURA(')[1].split('\ndef PUR(')[0])
head=head_red('Girijā (Birajā) · Jājpur · The 18 Śakti Pīṭhas · srini.presents',
 'Girijā, called Birajā or Virajā, of Jājpur in Odisha, the eleventh of the 18 Śakti Pīṭhas: the navel of Satī, Brahmā’s fire-sacrifice on the Vaitaraṇī, the two-armed Mahiṣamardinī, Nābhi Gayā and the three Gayās, the Siṃhadhvaja chariot, the sixteen-day Durgā Pūjā, and Jājpur from the Bhauma-Karas to the Somavaṃśīs. An illustrated reference guide.')
def j(lat,lon): return 40+(lon-85.4)*260, 20+(21.3-lat)*220
def JMAP(w=560,h=300):
    coast=' '.join(f'{j(la,lo)[0]:.0f},{j(la,lo)[1]:.0f}' for la,lo in ((21.2,87.1),(20.95,86.95),(20.75,86.85),(20.55,86.75),(20.3,86.6),(20.15,86.45),(20.0,86.4)))
    g=f'<rect width="{w}" height="{h}" fill="#e7f0d8"/><polygon points="{w},0 {coast} {j(20.0,86.4)[0]:.0f},{h} {w},{h}" fill="#9ad1f5" stroke="#111" stroke-width="2"/>'
    a=j(21.15,85.85);b=j(20.83,86.34);c=j(20.75,86.85)
    g+=f'<path d="M{a[0]:.0f} {a[1]:.0f} Q{b[0]-40:.0f} {b[1]-50:.0f} {b[0]:.0f} {b[1]-4:.0f} T{c[0]:.0f} {c[1]:.0f}" stroke="#4aa3df" stroke-width="7" fill="none"/>'+T(f'{a[0]+40:.0f}',f'{a[1]+30:.0f}','VAITARAṆĪ',11,'#1d4f9a','start')
    for nm,la,lo,col,side in (('JĀJPUR · Birajā',20.84,86.34,'#c0392b','r'),('Cuttack',20.46,85.88,'#bbb','r'),('Bhubaneswar',20.27,85.84,'#bbb','r'),('Purī (Vimalā)',19.80,85.82,'#bbb','r')):
        x,y=j(la,lo)
        if y>h-6: continue
        r=8 if col=='#c0392b' else 6
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',nm,12,'#111','start' if side=='r' else 'end')
    return g+T(w-20,h-20,'BAY OF BENGAL',12,'#1d4f9a','end')+T(w-10,16,'simplified, not to scale',10,'#555','end')
def BIRAJA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-60 40 q30 -30 70 -10 l40 0 q10 10 0 20 h-100z" fill="#3a3a3a"/><path d="M24 30 q12 -16 30 -10" fill="none" stroke-width="3"/><circle cx="-56" cy="34" r="12" fill="#3a3a3a"/><path d="M-66 24 q-10 -10 -4 -18 M-48 22 q4 -12 12 -12" fill="none" stroke="#ddd" stroke-width="3"/>'
 '<path d="M-20 30 q-4 -60 20 -76 q24 16 20 76z" fill="#c0392b"/><circle cy="-58" r="14" fill="#f2c79b"/><path d="M-14 -64 q14 -20 28 0" fill="#111"/>'
 '<path d="M-14 -74 h28 l-4 -14 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/><circle cx="-5" cy="-58" r="2" fill="#111"/><circle cx="5" cy="-58" r="2" fill="#111"/>'
 '<path d="M14 -30 L-52 24" stroke="#7a5a2a" stroke-width="4"/><path d="M-52 24 l-6 -10 l12 2z" fill="#bbb"/><path d="M-14 -24 q-30 10 -24 46" fill="none" stroke="#f2c79b" stroke-width="7"/><path d="M28 30 q16 6 22 -6" fill="none" stroke="#f2c79b" stroke-width="5"/></g>')
def RATHA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-46" y="-36" width="92" height="26" fill="#7a5a2a"/><path d="M-42 -36 q42 -90 84 0z" fill="#c0392b"/><path d="M-26 -36 q26 -56 52 0" fill="#ffd60a"/>'
 '<path d="M0 -100 v-22"/><path d="M0 -122 h24 v14 h-24z" fill="#ffd60a"/><path d="M6 -112 l5 -4 l6 2 l2 4 l-6 2z" fill="#c0392b" stroke-width="1"/>'+''.join(f'<circle cx="{dx}" cy="-6" r="11" fill="#5a3a1a"/>' for dx in (-30,-10,10,30))+'</g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The two-armed Goddess Biraja spearing the buffalo demon, a sacrificial fire behind her and a river in front">'
 '<rect width="380" height="268" fill="#4a0e0e" rx="8"/><g transform="translate(300 120)"><path d="M-40 60 q-14 -60 14 -100 q4 30 16 34 q8 -50 30 -66 q-10 50 6 70 q14 -16 8 -36 q26 40 -6 98z" fill="#ff8c1a" opacity=".7"/></g>'
 +'<path d="M0 240 Q190 220 380 242 V268 H0z" fill="#4aa3df"/>'+BIRAJA(170,170,1.5)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Girijā</b> in the hymn; worshipped as <b>Birajā</b> or <b>Virajā</b>'),
 ('Form','A rare <b>two-armed Mahiṣamardinī</b>: spearing the buffalo-demon, pulling its tail'),
 ('Where','<b>Jājpur</b>, Odisha, on the <b>Vaitaraṇī</b> river'),
 ('Pīṭha','Satī’s <b>navel</b> (nābhi) fell here, by temple tradition'),
 ('Hymn place','<b>Oḍhyāṇa</b> (Oḍḍiyāna): “the navel ornament”'),
 ('Also','<b>Nābhi Gayā</b>: the navel of Gayāsura, a well for ancestor rites'),
 ('Festival','A sixteen-day <b>Durgā Pūjā</b> and <b>Siṃhadhvaja</b>, a chariot festival for the Goddess'),
 ('Temple','Present building usually dated to the 13th century; the image is far older')])
 +talk("Two navels in one place?","Satī's, and a giant's. Jājpur is where both stories meet.")))
pages.append(page('where','WHERE IT IS','On the Vaitaraṇī',fig(560,300,'Simplified map of coastal Odisha: Jajpur on the Vaitarani river, north of Cuttack and Bhubaneswar, Puri to the south',JMAP())
 +'<div class="g2"><div>'+minimap([11],'Map of India with Jajpur marked as the eleventh Shakti Pitha')+'</div><div class="panel reading small"><p><b>Odisha’s north.</b> Jājpur lies in the coastal plain north of Cuttack, on the <b>Vaitaraṇī</b>, the river named after the stream every soul must cross to reach Yama’s land.</p><p><b>Two Pīṭhas.</b> Odisha has Birajā here and Vimalā at Purī, both linked to the navel.</p></div></div>'))
pages.append(page('names','HER NAMES','Girijā, Birajā, Oḍḍiyāna',facts([
 ('Girijā','“Daughter of the mountain”: Pārvatī; the name in the Aṣṭādaśa Śakti Pīṭha hymn'),
 ('Virajā · Birajā','“The stainless one”, free of rajas; Odia pronounces V as B'),
 ('Oḍḍiyāna Pīṭha','Tantric name: <i>oḍḍiyāna</i> is a woman’s ornament worn at the navel'),
 ('Birajā Kṣetra','The old name of the whole town and region'),
 ('Jājpur','From <i>Yajñapura</i>, “city of the sacrifice”, or from King Yayāti')])
 +talk("The hymn's 'Oḍhyāṇa' is a piece of jewellery?","A navel ornament. The place is named after where it would sit: Satī's navel.")))
pages.append(page('pitha','THE PĪṬHA','Where the navel fell',fig(560,170,'Shiva carrying Sati’s body through the sky as Vishnu’s discus cuts it, a piece falling toward a river plain',
 '<rect width="560" height="170" fill="#1a0e1e"/>'+STAR+SHIVA(150,40,.7)+SATI(220,60,.9,-8)+CHAKRA(300,70,14)+'<circle cx="360" cy="120" r="8" fill="#ffd166" stroke="#111"/><path d="M340 100 l14 14" stroke="#ffd166" stroke-width="3"/><path d="M0 160 Q280 144 560 162" stroke="#4aa3df" stroke-width="8" fill="none"/>')+'''<div class="steps">
<div><b>The story.</b> When Satī gave up her body at Dakṣa’s sacrifice, Śiva carried it across the world in grief; Viṣṇu’s discus cut it, and where each part fell, a Pīṭha arose.</div>
<div><b>Here.</b> Temple tradition says Satī’s <b>navel</b> fell at Jājpur.</div>
<div><b>A shared claim.</b> The Tantra Cūḍāmaṇi puts the navel in <b>Utkala</b> (Odisha), with Vimalā as Goddess and Jagannātha as Bhairava; many lists read that as Purī. Others place the navel here. Both are honoured.</div>
</div>'''))
pages.append(page('brahma','LEGEND · BRAHMĀ’S FIRE','The Goddess from the sacrifice',fig(560,170,'Brahma with four heads seated before a sacrificial fire on a riverbank, the Goddess rising out of the flames',
 '<rect width="560" height="170" fill="#fdf1e8"/><path d="M0 160 Q280 146 560 162" stroke="#4aa3df" stroke-width="10" fill="none"/>'+FLAME(300,130,1.2)+'<g transform="translate(160 140)">'+person(0,0,'#ff8c1a','#f2c79b',1)+'<circle cx="-14" cy="-30" r="9" fill="#f2c79b" stroke="#111"/><circle cx="14" cy="-30" r="9" fill="#f2c79b" stroke="#111"/></g>'+BIRAJA(300,60,.55))+'''<div class="steps">
<div><b>The sacrifice.</b> The Brahmāṇḍa Purāṇa tells that <b>Brahmā</b> performed a great sacrifice on the bank of the Vaitaraṇī.</div>
<div><b>The Goddess.</b> From the <b>gārhapatya</b> fire rose Pārvatī, and told Brahmā to call her <b>Virajā</b>.</div>
<div><b>She stays.</b> Brahmā asked her to remain here as Śiva’s consort. She agreed, and around her arose the nine Durgās, the sixty-four Yoginīs and the Mātṛkās.</div>
<div><b>Yajñapura.</b> So the town became the “city of the sacrifice”: Jājpur.</div>
</div>'''))
pages.append(page('goddess','THE GODDESS','Two arms, one spear',fig(560,200,'The two-armed Goddess standing on a lion and a buffalo, driving a spear into the buffalo demon’s chest and pulling its tail',
 '<rect width="560" height="200" fill="#2a1a3a"/><path d="M200 20 h160 l-20 30 h-120z" fill="#e0a800" stroke="#111" stroke-width="2"/>'+BIRAJA(280,140,1.6))+facts([
 ('Form','<b>Dvibhujā</b>: two-armed Mahiṣamardinī, very rare among Durgā images'),
 ('Right hand','Drives a spear into the chest of <b>Mahiṣāsura</b>'),
 ('Left hand','Pulls the buffalo-demon’s tail'),
 ('Feet','One on the lion, one on the buffalo'),
 ('Age','Scholars date the image well before the present temple; some say the Gupta era'),
 ('Beside her','A shrine of <b>Bagalāmukhī</b>, one of the ten Mahāvidyās, rare in temples')])))
pages.append(page('nabhigaya','NĀBHI GAYĀ','The giant’s navel',fig(560,140,'A giant lying stretched across India, his head at Gaya, his navel at Jajpur and his feet at Pithapuram',
 '<rect width="560" height="140" fill="#fdf1e8"/>'+GAYASURA(70,80,420)+T(56,40,'HEAD · GAYĀ',12,'#7a1d12','start')+T(280,40,'NAVEL · JĀJPUR',12,'#7a1d12')+T(500,40,'FEET · PĪṬHĀPURAM',12,'#7a1d12','end')+'<circle cx="280" cy="70" r="8" fill="#c0392b" stroke="#111"/>')+facts([
 ('Gayāsura','A giant so holy that all who saw him were freed. The gods asked for his body as an altar; Viṣṇu pressed him down'),
 ('His wish','That the gods stay where his body lay, and that rites for the dead done there free the ancestors'),
 ('Three Gayās','<b>Śiro Gayā</b> (head) in Bihar, <b>Nābhi Gayā</b> (navel) here, <b>Pāda Gayā</b> (feet) at Pīṭhāpuram'),
 ('The well','Nābhi Gayā is a circular well in the temple grounds; <b>piṇḍas</b> for ancestors are dropped into it'),
 ('Belief','Tradition says the offerings vanish by the next morning')])
 +talk("Pīṭhāpuram has the feet, Jājpur the navel?","Two Śakti Pīṭhas, two Gayās. The Goddess and the giant keep meeting.")))
pages.append(page('vaitarani','THE VAITARAṆĪ','The river at the gate of death',facts([
 ('In myth','The <b>Vaitaraṇī</b> is the terrible river every soul must cross on the way to Yama; a cow given in charity helps the soul across'),
 ('On earth','Jājpur’s river bears the name: to bathe here is to cross it in life'),
 ('Mahābhārata','The Pāṇḍavas bathe in the Vaitaraṇī on their pilgrimage, in the Vana Parva'),
 ('Daśāśvamedha Ghāṭ','Where kings are said to have done horse sacrifices; the Somavaṃśī king <b>Yayāti</b> among them'),
 ('Pitṛ rites','With Nābhi Gayā, the river makes Jājpur a place for the dead as much as the living')])
 +talk("A real river named after the river of the dead?","Bathe in it now, the belief goes, and the other one will be easy.")))
pages.append(page('kshetra','BIRAJĀ KṢETRA','A town of shrines',facts([
 ('A crore of liṅgas','Tradition says Jājpur holds about a crore (ten million) Śiva-liṅgas'),
 ('Varāha','<b>Varāhanātha</b>, Viṣṇu as boar, is worshipped as a guardian of the Kṣetra'),
 ('Trilocaneśvara','A Śiva temple with fine carving on its hall'),
 ('Mātṛkās','Large old images of the Seven Mothers, among Odisha’s finest sculpture'),
 ('Four Kṣetras','Odisha counts four holy regions: Purī (Viṣṇu), Bhubaneswar (Śiva), Koṇārka (Sūrya) and Jājpur (the Goddess)')])))
pages.append(page('festivals','THROUGH THE YEAR','A chariot for the Goddess',fig(560,170,'A red and yellow chariot with a lion flag pulled by devotees',
 '<rect width="560" height="170" fill="#fff4cd"/><rect y="150" width="560" height="20" fill="#d8c8a8"/>'+RATHA(280,160,1.1)+''.join(f'<circle cx="{40+i*24}" cy="166" r="5" fill="#c98b5a"/>' for i in range(8))+''.join(f'<circle cx="{360+i*24}" cy="166" r="5" fill="#c98b5a"/>' for i in range(8)))+facts([
 ('Durgā Pūjā','The great festival: a sixteen-day worship (<b>Ṣoḍaśa Dinātmikā</b>), from the dark-fortnight aṣṭamī before Mahālayā to Āśvina Navamī'),
 ('Siṃhadhvaja','Her chariot, with a lion on its flag: the only chariot festival for a goddess in Odisha, by most accounts'),
 ('Suniā','The chariot’s building begins on Suniā, the Gajapati kings’ new year day'),
 ('Navarātri','Also kept as <b>Aparājitā Pūjā</b>')])
 +talk("Jagannātha has his chariots; she has hers?","One, with a lion flag. And unlike his, it doesn't head to an aunt's house; it circles her own town.")))
pages.append(page('history','HISTORY','Capital of kings',tl([
 ('Purāṇas','The Mahābhārata and Purāṇas praise the Vaitaraṇī and Virajā.'),
 ('Early centuries CE','The two-armed Mahiṣamardinī is carved and worshipped.'),
 ('8th–10th c.','The <b>Bhauma-Karas</b> rule from Virajā/Guhadevapāṭaka; Jājpur is their capital.'),
 ('10th–11th c.','The <b>Somavaṃśī</b> king <b>Yayāti Keśarī</b>, tradition’s founder of the temple, holds horse sacrifices here.'),
 ('13th c.','The present temple, in Kaliṅga style, is usually dated to this time.'),
 ('Later','Damage in the wars of the 16th century; the shrine restored and worship continued.')])
 +'<div class="panel reading small"><p><b>Dates don’t agree.</b> Tradition credits Yayāti Keśarī, who ruled around the 10th–11th century, but the present building is usually dated to the 13th. He may have built an earlier temple on the site.</p></div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Nābhi','Navel'),('Virajā','Stainless'),('Oḍḍiyāna','Navel ornament'),('Dvibhujā','Two-armed'),('Mahiṣamardinī','Slayer of the buffalo demon'),
 ('Piṇḍa','Rice-ball offering to ancestors'),('Gārhapatya','The household sacrificial fire'),('Kṣetra','Sacred field, region'),('Siṃhadhvaja','Lion-bannered'),('Yoginī','Attendant goddess; 64 in all')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Pīṭha.</b> Satī’s navel at Jājpur, the Oḍḍiyāna Pīṭha; Girijā in the hymn, Birajā to her people.</div>
<div><b>The Goddess.</b> Born from Brahmā’s fire on the Vaitaraṇī; a rare two-armed Mahiṣamardinī.</div>
<div><b>Nābhi Gayā.</b> Gayāsura’s navel: a well for the ancestors, one of the three Gayās.</div>
<div><b>The festivals.</b> Sixteen days of Durgā Pūjā and her own lion-flagged chariot.</div>
<div><b>The town.</b> Capital of the Bhauma-Karas; Yayāti’s sacrifices; a crore of liṅgas.</div>
</div>'''+talk("One line to remember?","Where the Mother's navel fell, the dead are fed and the Goddess rides a chariot.")+'<div class="key">The eleventh seat of the Mother: <b>Girijā of Jājpur</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Biraja Temple” (Jājpur; present temple 13th c.; Virajā/Girijā; Birajā Kṣetra and Pīṭha; Tantra Cūḍāmaṇi and Utkala; Oḍḍiyāna as navel ornament; Bagalāmukhī shrine; Nābhi Gayā well and pitṛ rites; a crore of liṅgas; sixteen-day Durgā Pūjā; Siṃhadhvaja; Aparājitā Pūjā). bhaktikalpa.com (two-armed image spearing Mahiṣa; Brahmāṇḍa Purāṇa: Brahmā’s yajña, Pārvatī from the gārhapatya fire, nine Durgās and sixty-four Yoginīs). tirthayatra.org and shubhpanchang.com (Nābhi Gayā; offerings vanishing; only chariot festival for a goddess in Odisha). bharattemples.com (Gupta-era dating; Varāha; Yayāti Keśarī). hindutemples-india.blogspot.com and maabiraja.com (Suniā and the chariot). imvoyager.com and inditales.com (Vaitaraṇī; Yajñapura; Odisha’s four Kṣetras). Google Arts &amp; Culture (Daśāśvamedha Ghāṭ and Yayāti; Trilocaneśvara). iskconbangalore.org (three Gayās).</p>
<p><b>Sources differ:</b> whether Utkala’s navel-Pīṭha is Birajā or Vimalā; who built the temple and when; the image’s age. <b>Not verified, tradition only:</b> offerings vanishing from the well; Bhauma-Kara capital name; 16th-century damage. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('brahma','Legend · Brahmā’s Fire'),('goddess','The Goddess'),('nabhigaya','Nābhi Gayā'),('vaitarani','The Vaitaraṇī'),
 ('kshetra','Birajā Kṣetra'),('festivals','Through the Year'),('history','History'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 11 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">GIRIJĀ</h1>
  <div class="series">BIRAJĀ OF JĀJPUR · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess born from Brahmā’s fire</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>On the Vaitaraṇī, a river named after the stream that the dead must cross, stands the shrine of <b>Birajā</b>, called <b>Girijā</b> in the Śakti Pīṭha hymn. Here, tradition says, Satī’s navel fell, and here Brahmā lit a sacrificial fire from which the Goddess rose.</p>
    <p>She has only two arms, rare for Durgā, and one of them drives a spear into the buffalo-demon. In her courtyard is a well where people feed their ancestors, at the navel of a giant whose body spans India. Once a year she rides out in her own chariot.</p>
    <p>This guide tells her legends, her festivals and the long history of Jājpur.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā Birajā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why is she called Girijā in the hymn but Birajā in Jājpur?","Girijā is Pārvatī, the mountain's daughter. Birajā, 'the stainless', is what her own people have always called her.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Girija_Jajpur.html','w').write(head+b+tail())
print('ok',len(pages))
