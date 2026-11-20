exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Śāradā · Kashmir · The 18 Śakti Pīṭhas · srini.presents',
 'Śāradā of Kashmir, the eighteenth of the 18 Śakti Pīṭhas: the ruined temple-university in the Neelum valley, the Goddess of learning, Satī’s right hand, the Śāradā script, Śaṅkara on the Throne of Omniscience, Kalhaṇa and Al-Bīrūnī, the closed border since 1947, the 2005 earthquake, the Teetwal temple of 2023 and the corridor demand. An illustrated reference guide.')
def s(lat,lon): return 40+(lon-73.3)*260, 20+(35.0-lat)*260
def SMAP(w=560,h=300):
    o=f'<rect width="{w}" height="{h}" fill="#e7f0d8"/>'+''.join(f'<path d="M{x} {y} l30 -40 l30 40z" fill="#fff" stroke="#888"/>' for x,y in ((60,70),(160,50),(380,60),(470,80)))
    pts=[(34.88,74.6),(34.79,74.19),(34.6,73.95),(34.45,73.82),(34.38,73.78),(34.37,73.47)]
    o+='<path d="M'+' L'.join(f'{s(a,b)[0]:.0f} {s(a,b)[1]:.0f}' for a,b in pts)+'" stroke="#4aa3df" stroke-width="6" fill="none"/>'+T(f'{s(34.62,74.0)[0]+10:.0f}',f'{s(34.62,74.0)[1]:.0f}','NEELUM / KIṢANGAṄGĀ',11,'#1d4f9a','start')
    o+='<path d="M'+' L'.join(f'{s(a,b)[0]:.0f} {s(a,b)[1]:.0f}' for a,b in ((34.95,74.9),(34.75,74.45),(34.55,74.1),(34.40,73.80),(34.15,73.85),(33.9,74.0)))+'" stroke="#c0392b" stroke-width="2.5" stroke-dasharray="8 6" fill="none"/>'+T(f'{s(34.15,73.9)[0]+8:.0f}',f'{s(34.15,73.9)[1]:.0f}','Line of Control (simplified)',10,'#c0392b','start')
    for nm,la,lo,col,side in (('ŚĀRADĀ (ruins)',34.79,74.19,'#c0392b','l'),('Muzaffarabad',34.37,73.47,'#bbb','r'),('Teetwal (2023 temple)',34.38,73.78,'#e0a800','r'),('Srinagar',34.08,74.80,'#bbb','r'),('Harmukh',34.38,74.92,'#fff','l')):
        x,y=s(la,lo); r=8 if col=='#c0392b' else 6
        o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',nm,12,'#111','start' if side=='r' else 'end')
    return o+T(w-10,h-8,'simplified; borders not authoritative',10,'#555','end')
def SARADA(x,y,s_=1): return (f'<g transform="translate({x} {y}) scale({s_})" stroke="#111" stroke-width="2"><path d="M-30 60 q-4 -60 30 -70 q34 10 30 70z" fill="#fff"/><circle cy="-24" r="16" fill="#f2c79b"/><path d="M-16 -30 q16 -24 32 0" fill="#111"/>'
 '<path d="M-12 -40 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800"/><circle cx="-5" cy="-24" r="2" fill="#111"/><circle cx="5" cy="-24" r="2" fill="#111"/>'
 '<path d="M-40 10 h80" stroke="#7a5a2a" stroke-width="4"/><circle cx="-30" cy="10" r="10" fill="#c9a26b"/><circle cx="30" cy="10" r="10" fill="#c9a26b"/><rect x="-12" y="18" width="24" height="16" fill="#ffd166"/></g>')
def RUIN(x,y,sc=1): return (f'<g transform="translate({x} {y}) scale({sc})" stroke="#111" stroke-width="2"><rect x="-110" y="-20" width="220" height="20" fill="#9a8a7a"/>'+''.join(f'<rect x="{-100+i*14}" y="{-20-i*6}" width="14" height="{i*6}" fill="#8a7a6a"/>' for i in range(1,6))
 +'<rect x="-40" y="-110" width="80" height="90" fill="#a89a8a"/><path d="M-20 -20 v-50 l20 -24 l20 24 v50z" fill="#3a2a1a"/><path d="M-40 -110 l40 -30 l40 30" fill="none"/>'
 +'<path d="M-40 -60 l-20 10 M40 -80 l14 6" stroke-width="3"/>'+''.join(f'<rect x="{dx}" y="-8" width="16" height="10" fill="#8a7a6a"/>' for dx in (60,80,-90))+'</g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A roofless stone temple with a trefoil arch doorway on a high plinth, mountains behind, a river in front">'
 '<rect width="380" height="268" fill="#2a0e0e" rx="8"/><path d="M0 140 l80 -100 l80 100z M200 140 l90 -120 l90 120z" fill="#ddd" stroke="#888"/><rect y="140" width="380" height="128" fill="#4a6a3a" rx="8"/>'
 +RUIN(190,220,1.1)+'<path d="M0 250 Q190 236 380 252" stroke="#4aa3df" stroke-width="10" fill="none"/></svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Śāradā</b>: Sarasvatī as the Goddess of Kashmir, of learning and speech'),
 ('Hymn','<i>kāśmīre tu sarasvatī</i>: “Sarasvatī in Kashmir”'),
 ('Where','Village of <b>Sharda</b>, <b>Neelum valley</b>, Pakistan-administered Kashmir, near the Line of Control'),
 ('Pīṭha','Satī’s <b>right hand</b> fell here, by common lists'),
 ('Fame','A great <b>temple-university</b> of the 6th–12th centuries; the <b>Śāradā script</b> takes its name from it'),
 ('Śaṅkara','Tradition says he ascended its <b>Sarvajña Pīṭha</b>, the Throne of Omniscience'),
 ('Today','<b>In ruins</b>, unvisited by Indian pilgrims since 1947; damaged further in the 2005 earthquake'),
 ('Revival','A Śāradā temple at <b>Teetwal</b> on the Indian side (2023); a corridor is demanded')])
 +talk("The last Pīṭha is a ruin we can't even visit?","For now. But the Goddess of learning lives wherever someone studies. That's the consolation, and the hope.")))
pages.append(page('where','WHERE IT IS','A valley across the line',fig(560,300,'Simplified map of the Kashmir region: Sharada on the Neelum river in Pakistan-administered Kashmir, the Line of Control, Teetwal on the Indian side, Muzaffarabad and Srinagar',SMAP())
 +'<div class="g2"><div>'+minimap([18],'Map of India with Sharada marked in the far north')+'</div><div class="panel reading small"><p><b>The site.</b> About 1,980 m up, where the Madhumatī stream meets the Neelum (Kiṣangaṅgā), below Mount Harmukh, held by Kashmiri Paṇḍits to be Śiva’s abode.</p><p><b>The border.</b> It lies on the far side of the Line of Control, about 10 km from it.</p></div></div>'))
pages.append(page('names','THE NAMES','Śāradā, Sarasvatī, Sarvajña',facts([
 ('Śāradā','The Kashmiri name of Sarasvatī: “of autumn”, bright as the autumn moon'),
 ('Śāradā Pīṭha','“Seat of Śāradā”'),
 ('Sarvajña Pīṭha','“Seat of omniscience”: the throne that only the all-knowing may mount'),
 ('Kāśmīrapuravāsinī','“Dweller in Kashmir”, from a famous prayer'),
 ('Neelum · Kiṣangaṅgā','Two names of the same river')])
 +'<div class="panel reading"><p><b>A prayer known all over India</b>, said before study: <i>namaste śārade devi kāśmīrapuravāsini | tvām ahaṃ prārthaye nityaṃ vidyādānaṃ ca dehi me</i>: “Salutations, Śāradā Devī, who lives in Kashmir; I pray to you always: give me the gift of learning.”</p></div>'
 +talk("Children who've never heard of the ruin still say that prayer?","Every day, across India. The temple is closed; the prayer never was.")))
pages.append(page('pitha','THE PĪṬHA','Where the right hand fell',fig(560,170,'Shiva carrying Sati’s body as Vishnu’s discus cuts it, a hand falling toward a Himalayan valley',
 '<rect width="560" height="170" fill="#1a0e1e"/>'+STAR+SHIVA(150,40,.7)+SATI(220,60,.9,-8)+CHAKRA(300,70,14)+'<path d="M340 170 l60 -70 l60 70z M420 170 l70 -90 l70 90z" fill="#ddd"/><path d="M430 110 l4 -12 l4 10 l4 -12 l4 12" stroke="#ffd166" stroke-width="3" fill="none"/>')+'''<div class="steps">
<div><b>The right hand.</b> Common lists place Satī’s <b>right hand</b> at Śāradā: the hand that writes and gives.</div>
<div><b>Sarasvatī.</b> The Aṣṭādaśa hymn closes with her: <i>kāśmīre tu sarasvatī</i>. The eighteenth seat is the Goddess of learning.</div>
<div><b>Lists differ.</b> Some older lists do not count Śāradā among the 51; others name a different part. The hymn and Kashmiri tradition hold her dear.</div>
</div>'''))
pages.append(page('university','THE TEMPLE-UNIVERSITY','Where scholars came',fig(560,170,'Scholars seated on a terrace with palm-leaf manuscripts before a stone temple, mountains behind',
 '<rect width="560" height="170" fill="#cfe3f5"/><path d="M0 100 l80 -80 l80 80z M380 100 l90 -90 l90 90z" fill="#fff" stroke="#888"/><rect y="100" width="560" height="70" fill="#9a8a7a"/>'+TEMPLE(280,110,1.2,'#d8c8b8')
 +''.join(person(x,160,c,'#d8b090',.8)+f'<rect x="{x-14}" y="134" width="28" height="6" fill="#e8d8a8" stroke="#111"/>' for x,c in ((90,'#ff8c1a'),(160,'#c0392b'),(400,'#2a9d6f'),(470,'#ffd60a'))))+facts([
 ('Height','Between the 6th and 12th centuries, among the foremost centres of learning in the subcontinent'),
 ('Founding','Perhaps commissioned by the Kashmiri king <b>Lalitāditya Muktāpīḍa</b> (8th c.); no definite proof'),
 ('Scholars','Tradition links Kalhaṇa, Śaṅkara and others to it; Buddhist scholars too'),
 ('Hemacandra','The Jain grammarian asked for grammar texts kept here, to compile his own (per a 13th-c. Jain chronicle)'),
 ('Rāmānuja','Śrī Vaiṣṇava tradition says he came to consult an old commentary on the Brahma Sūtras kept here')])
 +talk("Was it a temple or a college?","Both, most likely. In old India, the Goddess of learning presided over the library.")))
pages.append(page('script','THE ŚĀRADĀ SCRIPT','Kashmir’s own letters',fig(560,140,'A palm-leaf manuscript in an old flowing script, with a stylus beside it',
 '<rect width="560" height="140" fill="#fdf1e8"/><rect x="40" y="40" width="480" height="60" rx="6" fill="#e8d8a8" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{60+i*22} 60 q6 -8 12 0 v14 q-6 6 -12 0" stroke="#3a2a1a" stroke-width="2" fill="none"/>' for i in range(20))+'<circle cx="80" cy="70" r="4" fill="#c0392b"/><circle cx="500" cy="70" r="4" fill="#c0392b"/><path d="M380 120 l120 -14" stroke="#7a5a2a" stroke-width="4"/>')
 +facts([
 ('Name','Called after the Pīṭha, where it was used so much'),
 ('Origin','It did not begin in Kashmir, scholars say, but took its name and fame from Śāradā'),
 ('Use','Kashmir’s chief script for centuries: Sanskrit and Kashmiri manuscripts, inscriptions'),
 ('Survival','Kept alive by Kashmiri Paṇḍit priests for horoscopes and ritual texts'),
 ('Family','An ancestor of later Himalayan scripts such as Ṭākarī')])))
pages.append(page('shankara','ŚAṄKARA AND THE THRONE','The southern door',fig(560,180,'A young ascetic climbing steps to a temple door while scholars debate around him, the goddess appearing above',
 '<rect width="560" height="180" fill="#efe4cc"/>'+RUIN(280,170,.9).replace('#a89a8a','#d8c8b8').replace('#3a2a1a','#ffd166')+person(200,150,'#ff8c1a','#e8b48a',1)+person(400,160,'#c0392b','#d8b090',.8)+person(460,160,'#2a9d6f','#d8b090',.8)+SARADA(280,50,.5))+'''<div class="steps">
<div><b>Four doors.</b> Tradition says the temple had four doors, for scholars of the four directions; the <b>southern</b> door had never been opened, for no southerner had proved himself all-knowing.</div>
<div><b>Śaṅkara arrives.</b> Ādi Śaṅkara came from Kerala, answered every challenger, philosophers of every school, and the southern door was opened for him.</div>
<div><b>The throne.</b> He ascended the <b>Sarvajña Pīṭha</b>, the Throne of Omniscience. The 14th-c. Mādhavīya Śaṅkaravijaya tells the story.</div>
<div><b>To the south.</b> Southern tradition links Śṛṅgeri’s Goddess Śāradā with this Kashmiri seat; even the Teetwal temple of 2023 received its image from Śṛṅgeri.</div>
</div>'''))
pages.append(page('texts','IN THE OLD BOOKS','Kalhaṇa, Bilhaṇa, Al-Bīrūnī',facts([
 ('Nīlamata Purāṇa','An early Kashmiri text listing sacred places, Śāradā among them'),
 ('Kalhaṇa','The <b>Rājataraṅgiṇī</b> (1148–49), Kashmir’s great chronicle, describes the shrine and a siege nearby'),
 ('Bilhaṇa','The 11th-c. Kashmiri poet credits his learning to Śāradā, “whose crown is gold from the Madhumatī”'),
 ('Al-Bīrūnī','In the 11th c. he wrote of a revered shrine with a wooden image of Śāradā, though from hearsay, never having entered Kashmir'),
 ('Aurel Stein','The British archaeologist photographed the ruins in 1893 and identified the site from Kalhaṇa')])
 +talk("A Muslim scholar wrote about it a thousand years ago?","Al-Bīrūnī listed it among India's most revered shrines. Its fame reached far beyond Kashmir.")))
pages.append(page('ruins','THE RUINS','What stands today',fig(560,200,'A roofless square stone temple on a high plinth, a doorway with a pointed trefoil arch, a long flight of steps, fallen blocks around',
 '<rect width="560" height="200" fill="#cfe3f5"/><path d="M0 120 l100 -100 l100 100z M340 120 l110 -110 l110 110z" fill="#fff" stroke="#888"/><rect y="120" width="560" height="80" fill="#5a7a4a"/>'+RUIN(280,192,1.3))+facts([
 ('Plan','A square shrine on a high stone plinth, in the Kashmiri style, reached by a long flight of steps'),
 ('Doorway','A tall doorway under a pointed, trefoil-style arch'),
 ('Roof','Gone; the walls stand open to the sky'),
 ('Damage','Centuries of neglect, then the <b>2005</b> Kashmir earthquake'),
 ('Stones','Blocks from fallen buildings have likely been reused by villagers over the years')])))
pages.append(page('partition','SINCE 1947','A pilgrimage cut off',tl([
 ('Before 1947','Kashmiri Paṇḍits made the pilgrimage, with <b>Teetwal</b> as a base on the way.'),
 ('1947','Partition and the war in Kashmir; the site falls on the Pakistani side of the line.'),
 ('2005','The Kashmir earthquake damages the ruins further.'),
 ('2007 onward','Visits by Kashmiri scholars from the other side revive the call to reopen it.'),
 ('2019','After the Kartarpur corridor opens for Sikh pilgrims, the <b>Save Sharda Committee</b> asks for a similar corridor.'),
 ('22 Mar 2023','A Śāradā temple and a gurdwārā at <b>Teetwal</b>, Kupwara, on the Indian side, are opened; the Union Home Minister says the government will try for a corridor.')])
 +'<div class="panel reading small"><p><b>Both sides.</b> Indian groups have complained of encroachments at the site; Pakistani writers have also argued for opening it to pilgrims. No corridor exists as of this writing.</p></div>'))
pages.append(page('teetwal','THE TEETWAL TEMPLE','The Goddess at the line',fig(560,170,'A small new temple and a gurdwara beside a river that marks the Line of Control, mountains on the far side',
 '<rect width="560" height="170" fill="#cfe3f5"/><path d="M300 100 l80 -90 l80 90 M400 100 l80 -70 l80 70" fill="#ddd" stroke="#888"/><rect y="100" width="560" height="70" fill="#7a9a5a"/><path d="M0 130 Q280 116 560 132" stroke="#4aa3df" stroke-width="14" fill="none"/><path d="M0 130 Q280 116 560 132" stroke="#c0392b" stroke-width="2" stroke-dasharray="8 6" fill="none"/>'
 +TEMPLE(140,120,1,'#ffe1a8')+TEMPLE(240,120,.8,'#fff')+T(240,62,'GURDWĀRĀ',9,'#555'))+facts([
 ('Where','Teetwal, in the Karnah area of Kupwara district, where the Kiṣangaṅgā marks the Line of Control'),
 ('Built by','The <b>Save Sharda Committee</b> Kashmir, with the Śṛṅgeri Śāradā Pīṭha; local Muslims supported it'),
 ('Opened','22 March 2023, with a gurdwārā opened soon after'),
 ('Purpose','A base camp for the old route, and a place to worship Śāradā within reach')])
 +talk("A Hindu temple, a gurdwārā and Muslim neighbours, at the border?","Built side by side, on the old pilgrim road. It's a small picture of what Kashmir once was.")))
pages.append(page('series','THE EIGHTEEN, COMPLETE','From Laṅkā to Kashmir',facts([
 ('1 Śāṅkarī','Laṅkā'),('2 Kāmākṣī','Kāñcī'),('3 Śṛṅkhalā','Pradyumna'),('4 Cāmuṇḍā','Mysuru'),('5 Jogulāmbā','Ālampur'),('6 Bhramarāmbā','Śrīśailam'),
 ('7 Mahālakṣmī','Kolhāpur'),('8 Ekavīrā','Māhur'),('9 Mahākālī','Ujjain'),('10 Puruhūtikā','Pīṭhāpuram'),('11 Girijā','Jājpur'),('12 Māṇikyāmbā','Drākṣārāmam'),
 ('13 Kāmarūpī','Kāmākhyā'),('14 Mādhaveśvarī','Prayāga'),('15 Vaiṣṇavī','Jvālāmukhī'),('16 Māṅgalyagaurī','Gayā'),('17 Viśālākṣī','Vārāṇasī'),('18 Sarasvatī','Kashmir (Śāradā)')])
 +'<div class="key">The hymn walks the land from the southern sea to the Himalayan north, and ends with <b>learning</b>.</div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Śāradā','Sarasvatī; “autumnal”'),('Sarvajña','All-knowing'),('Pīṭha','Seat'),('Vidyā','Learning'),('Lipi','Script'),
 ('Rājataraṅgiṇī','“River of kings”: Kalhaṇa’s chronicle'),('LoC','Line of Control'),('Corridor','A visa-free pilgrim route across a border')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Pīṭha.</b> Satī’s right hand in the Neelum valley: Sarasvatī of Kashmir, Śāradā.</div>
<div><b>The university.</b> A great seat of learning; the Śāradā script carries its name.</div>
<div><b>The legend.</b> Śaṅkara opens the southern door and mounts the Throne of Omniscience.</div>
<div><b>The present.</b> A ruin beyond the Line of Control, unvisited by Indian pilgrims since 1947.</div>
<div><b>The hope.</b> The Teetwal temple of 2023 and the call for a corridor.</div>
</div>'''+talk("One line to remember?","The Goddess of learning's house is in ruins, but every child who says her prayer keeps her seat warm.")+'<div class="key">The eighteenth seat of the Mother: <b>Śāradā of Kashmir</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Site and history:</b> Wikipedia, “Sharada Peeth” (ruined temple and centre of learning, Neelum valley, Pakistan-administered Kashmir; 1,981 m; Mount Harmukh; Śāradā script named after it though not born there; possibly Lalitāditya; Al-Bīrūnī’s hearsay account of a wooden image; pilgrims from Bengal by the 8th c.; Hemacandra; Rāmānuja; Śaṅkara’s southern door; Stein’s 1893 photograph; reuse of stones; about 10 km from the LoC; South Indian traditions). imp-art.org (8th–11th c. date; Mādhavīya Śaṅkaravijaya; Sarvajña Pīṭha). swarajyamag.com (Madhumatī confluence; Kalhaṇa; Bilhaṇa). hindutemples-india.blogspot.com (6th–12th c.; Nīlamata Purāṇa; Kalhaṇa 1148).</p>
<p><b>Modern:</b> organiser.org and brighterkashmir.com (2005 earthquake; Teetwal temple 22 March 2023; corridor talk from 2019; encroachment complaints; local Muslim support). Zee News (Teetwal temple with Śṛṅgeri Śāradā Maṭha). Deccan Herald, The Tribune, The Telegraph (corridor statement). esamskriti.com (Save Sharda memorandum at Kartarpur, 2019; gurdwārā 30 April 2023). Outlook (2007 visit). Dawn (Pakistani coverage).</p>
<p><b>Sources differ:</b> the part of Satī (right hand in common lists); the founder and date; Ashokan and Kaniṣka links made by some sites (not used here). <b>Not verified, tradition only:</b> the four doors; Rāmānuja’s visit; Śṛṅgeri’s link with this seat. Political names follow neutral usage. Maps are simplified and not authoritative. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('pitha','The Pīṭha'),('university','The Temple-University'),('script','The Śāradā Script'),('shankara','Śaṅkara and the Throne'),('texts','In the Old Books'),
 ('ruins','The Ruins'),('partition','Since 1947'),('teetwal','The Teetwal Temple'),('series','The Eighteen, Complete'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 18 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">ŚĀRADĀ</h1>
  <div class="series">SARASVATĪ OF KASHMIR · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess of learning, beyond the line</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>The Śakti Pīṭha hymn ends in Kashmir: <i>kāśmīre tu sarasvatī</i>. The last seat of the Mother is the Goddess of learning, <b>Śāradā</b>, whose temple in the Neelum valley was once among the great universities of Asia. Kashmir’s script was named after it; tradition says Śaṅkara mounted its Throne of Omniscience.</p>
    <p>Today it is a roofless ruin across the Line of Control, which Indian pilgrims have not reached since 1947. Yet children all over India still begin their lessons with a prayer to “Śāradā who lives in Kashmir”.</p>
    <p>This guide tells its story, its scholars, its ruin and the hopes of reopening it.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Namaste Śārade Devi,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why does the list end with learning?","Maybe that's the point: after all the forms of power, the last gift is knowledge.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Sharada_Kashmir.html','w').write(head+b+tail())
print('ok',len(pages))
