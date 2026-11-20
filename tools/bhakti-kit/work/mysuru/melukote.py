import sys; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
head=make_head('Melukōṭe · Tirunārāyaṇapura · Temples around Mysuru · srini.presents',
 'Melukōṭe (Tirunārāyaṇapura): Celuvanārāyaṇa, the image Rāmānuja brought home, Bībī Nācciyār, Yoga Narasiṃha on the hill, the Vairamuḍi diamond crown, and the Kalyāṇi. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def HILL(x,y,w,h,c='#7a8a5a'):
    return f'<path d="M{x-w/2} {y} Q{x-w/4} {y-h*0.6} {x-w/10} {y-h} Q{x} {y-h*1.06} {x+w/10} {y-h} Q{x+w/4} {y-h*0.6} {x+w/2} {y}z" fill="{c}" stroke="#111" stroke-width="2"/>'
def TEMPLE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="#f2e6c8"/><path d="M-14 -16 h28 l-4 -10 h-20z M-10 -26 h20 l-4 -10 h-12z" fill="#e2cfa8"/><circle cy="-40" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def LORD(x,y,s=1,skin='#3b6fd0',crown='#e0a800',gems=False):
    g=(f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-20 70 h40 l-4 -60 h-32z" fill="#ffd60a"/><path d="M-16 10 q16 -14 32 0 v-30 q-16 -10 -32 0z" fill="'+skin+'"/>'
     '<path d="M-16 -14 l-16 -22 M16 -14 l16 -22" stroke="'+skin+'" stroke-width="7"/><circle cx="-34" cy="-40" r="7" fill="#fff"/><circle cx="34" cy="-40" r="8" fill="#ffd60a"/>'
     f'<circle cy="-34" r="12" fill="{skin}"/><path d="M-12 -46 h24 l-4 -24 h-16z" fill="{crown}"/><path d="M-6 -36 h12" stroke="#fff" stroke-width="3"/>'
     '<path d="M-16 -4 q16 12 32 0" fill="none" stroke="#c0392b" stroke-width="4"/>')
    if gems: g+=''.join(f'<circle cx="{a}" cy="{b}" r="2.6" fill="#fff" stroke="#8fd0f5"/>' for a,b in ((-6,-52),(6,-52),(0,-62),(-4,-58),(4,-58)))
    return g+'</g>'
def NARASIMHA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-24 40 q24 -60 48 0z" fill="#ffd60a"/><path d="M-26 30 q26 -20 52 0" fill="none" stroke="#7a5a2a" stroke-width="4"/><circle cy="-8" r="18" fill="#e0a800"/><path d="M-18 -18 q-10 -16 6 -18 M18 -18 q10 -16 -6 -18" fill="#e0a800"/><circle cx="-7" cy="-10" r="3" fill="#111"/><circle cx="7" cy="-10" r="3" fill="#111"/><path d="M-8 2 q8 6 16 0" fill="none"/><path d="M-12 -26 h24 l-4 -14 h-16z" fill="#c0392b"/></g>'
def CROWN(x,y,s=1,c='#e0a800',gems='#8fd0f5'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-22 0 h44 l-4 -30 l-8 10 l-6 -20 l-4 14 l-4 -14 l-6 20 l-8 -10z" fill="{c}"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="3" fill="{gems}"/>' for a,b in ((-12,-8),(0,-10),(12,-8),(0,-24)))+'</g>'
def GARUDA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-60 -10 q30 -40 60 -10 q30 -30 60 10 q-30 0 -60 20 q-30 -20 -60 -20z" fill="#e0a800"/><circle cy="-14" r="10" fill="#c98b5a"/><path d="M-4 -12 l-10 6 l10 2z" fill="#e0a800"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Melukote: a temple at the foot of a hill and a small shrine on the summit, a stepped tank in front, and the Lord wearing a diamond crown">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/><circle cx="70" cy="50" r="28" fill="#ffd166" opacity=".35"/>'
 +HILL(150,250,280,160)+TEMPLE(150,94,.9)+TEMPLE(110,240,1.5)+'<rect x="170" y="226" width="80" height="30" fill="#4aa3df" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{170+i*6} {226+i*5} h{80-i*12}" stroke="#c9a26b" stroke-width="2"/>' for i in range(4))
 +LORD(300,150,1.25,gems=True)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','Viṣṇu as <b>Tirunārāyaṇa</b>; the festival image is <b>Celuvanārāyaṇa</b>, “the beautiful Nārāyaṇa”, first called <b>Rāmapriya</b>'),
 ('On the hill','<b>Yoga Narasiṃha</b>, said to have been installed by Prahlāda'),
 ('Place','<b>Melukōṭe</b> on the Yādavagiri hills, Pandavapura taluk, Mandya district, Karnataka, at about 1,030 m'),
 ('Old name','<b>Tirunārāyaṇapura</b>; also Yādavādri, Nārāyaṇādri, Vedādri, Yatiśaila'),
 ('Teacher','<b>Rāmānuja</b> lived here for 12–14 years in the 12th century'),
 ('Crowns','Three royal crowns, the greatest the diamond <b>Vairamuḍi</b>, kept in the Mandya treasury'),
 ('Great festival','The <b>Vairamuḍi Brahmotsava</b>, 13 days in Phālguna (March–April)'),
 ('Tradition','Teṅkalai Śrīvaiṣṇava; the Yatirāja maṭha; one of the 108 Abhimāna Kṣetras'),
 ('Learning','The <b>Academy of Sanskrit Research</b>, with some 11,000 manuscripts')])
 +talk("Is Melukōṭe a temple or a town?","Both! A whole hill town of temples, tanks and scholars. Rāmānuja's second home.")))
mapfig=fig(560,240,'Schematic map of Melukote: the Cheluvanarayana temple at the foot of the hill, the Kalyani tank beside it, the Yoga Narasimha temple on the hilltop, and the Raya Gopura; Tondanur and Srirangapatna further away. Not to scale.',
 '<rect width="560" height="240" fill="#eef6e4"/>'+HILL(300,230,360,190)+TEMPLE(300,58,.8)+T(300,26,'YOGA NARASIṂHA',10,'#0d3f73')
 +TEMPLE(200,210,1.2)+T(200,234,'CELUVANĀRĀYAṆA',10,'#0d3f73')+'<rect x="250" y="190" width="60" height="30" fill="#4aa3df" stroke="#111"/>'+T(280,234,'KALYĀṆI',10,'#1d6fb8')
 +''.join(f'<rect x="{390+i*10}" y="150" width="5" height="40" fill="#c9a26b" stroke="#111"/>' for i in range(4))+T(410,206,'RĀYA GOPURA',9,'#555')
 +T(60,60,'TOṆḌANŪR ↙',10,'#555','start')+T(520,224,'ŚRĪRAṄGAPAṬṬAṆA ↘',10,'#555','end')+T(500,20,'simplified, not to scale',9,'#555','end'))
pages.append(page('where','WHERE IT IS','A temple town on the Yādava hills',mapfig+'''<div class="panel reading">
<p><b>The hills.</b> Melukōṭe sits on the rocky <b>Yādavagiri</b> (Yadugiri) hills north of the Kāverī, the only town in Mandya district above 1,000 m. Its name means roughly “the high fort”.</p>
<p><b>Two temples.</b> <b>Celuvanārāyaṇa</b> stands in the town at the foot of the hill; <b>Yoga Narasiṃha</b> crowns the summit.</p>
<p><b>Around it.</b> The hills are a wildlife sanctuary, created in 1974 chiefly to protect <b>wolves</b>, with about 200 kinds of birds.</p>
</div>'''))
deity=fig(560,220,'The stone Tirunarayana in the sanctum and, in front, the small metal festival image Cheluvanarayana',
 '<rect width="560" height="220" fill="#dcecff"/><rect x="160" y="20" width="240" height="180" fill="#f6f1e2" stroke="#111" stroke-width="2"/>'+LORD(280,110,1.3,skin='#2b2b3a')+LORD(440,160,.6)+'<path d="M400 160 h20" stroke="#111"/>'
 +T(280,214,'TIRUNĀRĀYAṆA',12,'#0d3f73')+T(470,214,'CELUVANĀRĀYAṆA',10,'#c0392b'))
pages.append(page('deity','THE LORD OF MELUKŌṬE','Tirunārāyaṇa and Celuvanārāyaṇa',deity+'''<div class="g2">
<div class="card bg-blue"><h4>🪨 Tirunārāyaṇa</h4><p>The stone image in the sanctum, the <b>mūlavar</b>: Nārāyaṇa of Tirunārāyaṇapura.</p></div>
<div class="card bg-yellow"><h4>✨ Celuvanārāyaṇa</h4><p>The metal <b>festival image</b>, “the handsome Nārāyaṇa”, also called <b>Celuvapiḷḷe Rāya</b>, Selva Piḷḷai and Sampatkumāra. Inscriptions call him <b>Rāmapriya</b>, “Rāma’s beloved”.</p></div>
</div>
<div class="panel reading"><p><b>Also in the halls:</b> images of Rāmānuja, the Āḻvārs and <b>Yadugiri Ammanavaru</b>, the Goddess of the hill.</p></div>'''))
leg1=fig(560,170,'A sacred metal image passing down the ages from Brahma, to Rama, to Balarama, to the Yadava family',
 '<rect width="560" height="170" fill="#fff4dc"/>'+''.join(person(70+k*140,150,c,'#c98b5a',.9)+T(70+k*140,166,n,10) for k,(c,n) in enumerate((('#ff8c1a','BRAHMĀ'),('#3b6fd0','RĀMA'),('#fff','BALARĀMA'),('#ffd60a','YĀDAVAS'))))
 +''.join(LORD(70+k*140,60,.35) for k in range(4))+''.join(f'<path d="M{110+k*140} 70 h60" stroke="#111" stroke-width="2"/><path d="M{170+k*140} 64 l10 6 l-10 6z" fill="#111"/>' for k in range(3)))
pages.append(page('legends1','THE LEGENDS · I','Rāma’s beloved image',leg1+'''<div class="steps">
<div><b>For Brahmā.</b> The temple’s story says Brahmā asked Viṣṇu for an image to worship. Viṣṇu gave him one, which Brahmā’s son <b>Sanatkumāra</b> installed at Melukōṭe.</div>
<div><b>A second, of metal.</b> Brahmā later received a metal image too. It passed down the ages: worshipped by <b>Rāma</b>, then by <b>Balarāma</b>, then by the <b>Yādava</b> family.</div>
<div><b>Rāmapriya.</b> So the festival image was called <b>Rāmapriya</b>, “dear to Rāma”, and the hills <b>Yādavagiri</b>, the hills of the Yādavas.</div>
<div><b>Lost.</b> Over the centuries, the story goes, the image was lost, until Rāmānuja came.</div>
</div>'''))
leg2=fig(560,170,'Ramanuja in a dream seeing Vishnu point to the hill; then digging white sacred clay and finding a buried image',
 '<rect width="560" height="170" fill="#eef3fa"/>'+person(110,160,'#ff8c1a','#c98b5a',1)+'<path d="M90 98 q20 -24 40 0" fill="#fff" stroke="#111"/>'
 +'<g opacity=".7">'+LORD(200,70,.4)+'</g><path d="M140 80 q30 -20 50 -10" stroke="#555" stroke-dasharray="4 4" fill="none"/>'
 +HILL(400,170,260,90)+'<ellipse cx="400" cy="134" rx="40" ry="12" fill="#fff" stroke="#111"/>'+LORD(400,126,.3,skin='#2b2b3a')+T(400,164,'THE WHITE CLAY',10,'#0d3f73'))
pages.append(page('legends2','THE LEGENDS · II','Rāmānuja finds the Lord',leg2+'''<div class="steps">
<div><b>A dream.</b> After Rāmānuja came to the Hoysaḷa country, Viṣṇu appeared to him in a dream and sent him to Melukōṭe to find holy white earth, the clay for the Śrīvaiṣṇava <b>nāmam</b>.</div>
<div><b>A discovery.</b> Digging there, he found the clay and, with it, a buried image: the Lord <b>Tirunārāyaṇa</b>.</div>
<div><b>Installed.</b> Tradition dates the installation, by the Pāñcarātra āgama, to the Bahudhānya year, <b>1099</b>, in the month of Puṣya.</div>
<div><b>But older still.</b> A Mysore Archaeological Department report, based on inscriptions, says the deity was already well known before Rāmānuja worshipped here in <b>December 1098</b>.</div>
</div>'''+talk("So did Rāmānuja start the temple or not?","Inscriptions say there was worship here already; tradition says he found the Lord and made it great. Both can be true!")))
leg3=fig(560,180,'A princess in a palace playing with a small golden image as a doll; a sage calling out and the image running to him; the princess following',
 '<rect width="560" height="180" fill="#fdf3e8"/><rect x="30" y="40" width="190" height="130" fill="#f2e6c8" stroke="#111" stroke-width="2"/><path d="M30 40 q95 -50 190 0" fill="#e2e2d8" stroke="#111" stroke-width="2"/>'
 +'<g transform="translate(110 160)" stroke="#111" stroke-width="2"><circle cy="-50" r="12" fill="#f2c79b"/><path d="M-22 30 q22 -80 44 0z" fill="#e05a8a"/></g>'+LORD(170,140,.3)
 +person(400,170,'#ff8c1a','#c98b5a',1)+'<path d="M200 130 q100 -40 180 0" stroke="#e0a800" stroke-width="3" stroke-dasharray="6 5" fill="none"/>'+T(300,92,'“CELUVA PIḶḶE!”',13,'#c0392b'))
pages.append(page('legends3','THE LEGENDS · III','Bībī Nācciyār, the Sultan’s daughter',leg3+'''<div class="steps">
<div><b>The doll.</b> The festival image, the story goes, had been carried off to Delhi, where the Sultan’s daughter played with it as her doll and grew to love it.</div>
<div><b>“Celuva piḷḷe!”</b> Rāmānuja went to Delhi and called out, “Come, my darling child!” The image ran to him of its own accord. From then he was <b>Celuvapiḷḷe</b>, Celuvanārāyaṇa.</div>
<div><b>The princess.</b> The princess followed him to Melukōṭe and, in her devotion, became one with the Lord. She is honoured in the temple as <b>Bībī Nācciyār</b>.</div>
<div><b>A note on dates.</b> Historians point out the story cannot be literal: the Delhi Sultanate began in the 13th century, long after Rāmānuja. Śrīraṅgam and Madurai have similar <b>Tulukka Nācciyār</b> stories.</div>
</div>'''+talk("A Muslim princess honoured in a Vaiṣṇava temple?","Yes, as the Lord's own devotee. History may doubt the details; the devotion it celebrates is the point.")))
pages.append(page('ramanuja','RĀMĀNUJA AT MELUKŌṬE','The teacher’s second home',facts([
 ('Why here','Rāmānuja came into the Hoysaḷa country in the late 11th century, and became <i>rājaguru</i>, teacher to the Hoysaḷa court'),
 ('How long','About <b>12</b> years by most accounts (some say 14)'),
 ('The temple','King <b>Viṣṇuvardhana</b> granted <b>5,000 gadyāṇas</b> for the building, completed, tradition says, in <b>1104</b>'),
 ('The maṭha','The <b>Yadugiri Yatirāja maṭha</b> was set up so that a sannyāsī would manage the temple; it does to this day'),
 ('The Tamil Veda','Rāmānuja had the Āḻvārs’ hymns recited here, and Melukōṭe still follows the Teṅkalai tradition'),
 ('Openness','Tradition credits him with opening temple worship here to people of all communities on certain days')])
 +'''<div class="panel reading"><p><b>Two homes.</b> Rāmānuja lived and died at <a href="/bhakti/temples-of-india/triranga/antya-ranga/">Śrīraṅgam</a>, and spent his years of exile at Melukōṭe. Śrīvaiṣṇavas count both among their holiest places.</p></div>'''))
pages.append(page('narasimha','YOGA NARASIṂHA','The Lord on the summit',fig(560,170,'Yoga Narasimha seated in meditation with a band around his knees, on the hilltop, with Prahlada worshipping',
 '<rect width="560" height="170" fill="#ffe9c4"/>'+HILL(280,170,500,90,'#9a8a6a')+NARASIMHA(280,120,1.4)+person(400,112,'#ffd60a','#f2c79b',.6)+T(400,128,'PRAHLĀDA',9))+'''<div class="panel reading">
<p><b>Narasiṃha at peace.</b> On the hilltop the Lord sits as <b>Yoga Narasiṃha</b>: the fierce man-lion of the Hiraṇyakaśipu story, calm now, seated in meditation with a band around his knees.</p>
<p><b>Prahlāda’s Lord.</b> Tradition says that after Hiraṇyakaśipu’s death, his son <b>Prahlāda</b> worshipped Narasiṃha here as a śālagrāma, and installed the image.</p>
<p><b>A king’s crown.</b> <b>Kṛṣṇarāja Woḍeyar III</b> gave a gold crown to the shrine on the hill. A large pond lies on the summit beside it.</p>
</div>'''))
crowns=fig(560,150,'Three royal crowns side by side: the Rajamudi, the Krishnarajamudi and the diamond Vairamudi',
 '<rect width="560" height="150" fill="#f2f6ff"/>'+CROWN(120,110,1.6,'#e0a800','#c0392b')+CROWN(280,110,1.6,'#e0a800','#2e9a5a')+CROWN(440,110,1.9,'#f2f2f2','#8fd0f5')
 +T(120,140,'RĀJAMUḌI',11,'#0d3f73')+T(280,140,'KṚṢṆARĀJAMUḌI',11,'#0d3f73')+T(440,140,'VAIRAMUḌI',12,'#c0392b'))
pages.append(page('crowns','THE THREE CROWNS','Jewels kept in a treasury',crowns+facts([
 ('Rājamuḍi','A jewelled crown given by <b>Rāja Woḍeyar</b> (1578–1617)'),
 ('Kṛṣṇarājamuḍi','Given by <b>Kṛṣṇarāja Woḍeyar III</b> (from 1799)'),
 ('Vairamuḍi','The <b>diamond</b> crown (<i>vajra-mukuṭa</i>): the oldest and most precious, its origin unknown'),
 ('The legend','The demon <b>Virocana</b> stole the crown from Nārāyaṇa in Vaikuṇṭha, and <b>Garuḍa</b> won it back; a blue gem is said to have fallen at Nācciyār Kōyil in Thanjavur'),
 ('Kept where','All the crowns stay in the government treasury at <b>Mandya</b>, and are brought to Melukōṭe under heavy guard for the festivals')])
 +talk("Garuḍa fought a demon for a crown?","Of course, he's the Lord's own bodyguard! And now the police guard it instead.")))
fest=fig(560,170,'The Lord in the diamond crown riding golden Garuda in a night procession under the full moon, crowds with lamps',
 '<rect width="560" height="170" fill="#141f45"/><circle cx="480" cy="40" r="22" fill="#fff8d0"/>'+GARUDA(280,150,1.4)+LORD(280,106,.55,gems=True)+crowd(['#ffd60a','#ff8c1a','#fff','#e05a8a','#3b6fd0'],30,40,166,.45))
pages.append(page('vairamudi','THE VAIRAMUḌI BRAHMOTSAVA','A night in a diamond crown',fest+'''<div class="panel reading">
<p><b>When.</b> A <b>13-day</b> festival in Phālguna (March–April), from the Bharaṇī star to Hasta. <b>Garuḍotsava</b> is held a day before it begins.</p>
<p><b>The night.</b> On the great night, under the Puṣya star, the Lord wears the <b>Vairamuḍi</b> only for the night procession on a <b>golden Garuḍa</b>, which goes on until dawn. Devotees believe the crown must not see daylight.</p>
<p><b>The crowds.</b> Up to <b>four lakh</b> devotees come, from Karnataka, Tamil Nadu and Andhra Pradesh. The festival also includes the Kalyāṇotsava, Nāgavalli, the great car festival and Gajendra Mokṣa.</p>
<p><b>Back to the vault.</b> The next morning the crown is checked before officials and returned to the treasury.</p>
</div>'''))
pages.append(page('town','THE TEMPLE TOWN','Kalyāṇi, gopura and maṭhas',facts([
 ('Kalyāṇi','The great stepped tank, ringed with pillared maṇḍapas: one of the most photographed temple tanks in Karnataka'),
 ('Rāya Gopura','A gateway of tall stone pillars from the Vijayanagara period on the hill, never completed into a tower'),
 ('Raja Woḍeyar','A small relief of the king, about 1.5 ft high, on a pillar of the hall; he granted the temple an estate in <b>1614</b>'),
 ('Shrines','Of Rāmānuja, the Āḻvārs and Yadugiri Ammanavaru'),
 ('The 108','Melukōṭe is counted among the <b>108 Abhimāna Kṣetras</b>, the cherished places of Śrīvaiṣṇavism')])
 +'''<div class="panel reading"><p><b>On screen.</b> The Kalyāṇi and the Rāya Gopura have appeared in many films, including the Hindi film <i>Damini</i>.</p></div>'''))
pages.append(page('history','HISTORY','Nine hundred years on the hill',tl([
 ('Before 1098','Inscriptions show worship of the Lord here already.'),
 ('1098–99','Rāmānuja comes; the image is installed in Puṣya, Bahudhānya year.'),
 ('1104','The temple completed with Viṣṇuvardhana’s grant.'),
 ('Vijayanagara','Renovations and the gopura works.'),
 ('1614','Rāja Woḍeyar grants an estate; the Rājamuḍi.'),
 ('1780s–90s','Tipu Sultan: a decree on recitation, gold and silver vessels, and, it is believed, elephants and drums for the temple. The Mandyam Iyengar community also remembers a massacre on Naraka Caturdaśī.'),
 ('1799 on','Kṛṣṇarāja Woḍeyar III: the Kṛṣṇarājamuḍi and the gold crown for Narasiṃha.'),
 ('1854','The Veda Vedānta Bodhinī Sanskrit College is founded.'),
 ('1974','Melukōṭe Temple Wildlife Sanctuary.'),
 ('1977–78','The Academy of Sanskrit Research opens: 11,000 manuscripts and 35,000 books.')])
 +'<div class="panel reading small"><p>For the full, two-sided story of Tipu and Melukōṭe, see <a href="/bhakti/temples-of-india/around-mysuru/">Tipu Sultan and the Temples around Mysuru</a>.</p></div>'))
pages.append(page('learning','A TOWN OF LEARNING','Sanskrit, Tamil and Kannada',facts([
 ('Academy of Sanskrit Research','Set up by the Karnataka government; a 14-acre campus with a library of about 11,000 manuscripts and 35,000 books'),
 ('Sanskrit College','The Veda Vedānta Bodhinī Sanskrit College, since 1854'),
 ('Scholars','Home to poets and scholars including the Kannada poet <b>Pu. Ti. Narasimhachar</b>, and earlier Tirumalārya and Alasiṅgācār'),
 ('Mandyam Iyengars','The Śrīvaiṣṇava community that grew up around the temple')])
 +talk("Why so many scholars on one hill?","Rāmānuja's tradition is a tradition of study. Where he lived, the books followed!")))
pages.append(page('around','AROUND MELUKŌṬE','Rāmānuja country',facts([
 ('Toṇḍanūr','About 20 km away: Nambi Nārāyaṇa, Pārthasārathi, Yoga Narasiṃha and Rāmānuja temples, and a great lake'),
 ('Śrīraṅgapaṭṭaṇa','Ādi Raṅga, linked to Rāmānuja by tradition'),
 ('Talakāḍu','Kīrtinārāyaṇa, Viṣṇuvardhana’s victory temple of 1117')])
 +'''<div class="panel reading"><p>More: <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga</a> · <a href="/bhakti/temples-of-india/around-mysuru/">Temples around Mysuru</a> · <a href="/bhakti/temples-of-india/triranga/antya-ranga/">Śrīraṅgam</a>.</p></div>'''))
glossary=[('Melukōṭe','“the high fort”'),('Tirunārāyaṇapura','“the town of Śrī Nārāyaṇa”'),('Yādavagiri','the hill of the Yādavas'),('Celuva','handsome, beautiful (Kannada)'),('Piḷḷe','child, darling'),('Rāmapriya','“dear to Rāma”'),('Bībī Nācciyār','the Sultan’s daughter honoured as the Lord’s consort'),('Nāmam','the Śrīvaiṣṇava forehead mark'),('Gadyāṇa','a gold coin'),('Yatirāja','“king of ascetics”, a title of Rāmānuja'),('Vairamuḍi','diamond crown'),('Kalyāṇi','a stepped temple tank'),('Abhimāna Kṣetra','a cherished Śrīvaiṣṇava shrine'),('Teṅkalai','the southern school of Śrīvaiṣṇavism')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','MELUKŌṬE ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Lord.</b> Tirunārāyaṇa, and Celuvanārāyaṇa, Rāma’s beloved image; Yoga Narasiṃha on the hill.</div>
<div><b>The legends.</b> The image passed from Brahmā through Rāma and the Yādavas; Rāmānuja’s dream and the white clay; Bībī Nācciyār.</div>
<div><b>The teacher.</b> Rāmānuja’s twelve years, Viṣṇuvardhana’s grant, the Yatirāja maṭha.</div>
<div><b>The crowns.</b> Rājamuḍi, Kṛṣṇarājamuḍi and the diamond Vairamuḍi, worn only by night.</div>
<div><b>The town.</b> The Kalyāṇi, the Rāya Gopura, and a living centre of Sanskrit learning.</div>
</div>'''+talk("One line to remember?","A sage followed a dream, dug up white clay, and found the Lord. Nine hundred years later, the hill still glows.")+'<div class="key">The high town of the beautiful Lord: <b>Rāmānuja’s Melukōṭe</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Town:</b> Wikipedia, “Melukote”: location and height; the names; Celuvanārāyaṇa, Selva Piḷḷai, Rāmapriya; the image lost and found; the 1098 report; Yatirāja maṭha; Teṅkalai; 12 or 14 years; Vairamuḍi (13 days, up to 400,000, night procession, golden Garuḍa, Garuḍotsava, Mandya treasury, Virocana and Garuḍa); the three crowns; Yoga Narasiṃha and Prahlāda; the Kalyāṇi and <i>Damini</i>; Rāja Woḍeyar (1614, relief); Kṛṣṇarāja Woḍeyar III; the ASR; the 1854 college; the sanctuary (1974); Toṇḍanūr.</p>
<p><b>Temple:</b> Wikipedia, “Cheluvanarayana Swamy Temple”: Brahmā and Sanatkumāra; Rāma, Balarāma, the Yādavas; Bībī Nācciyār and the anachronism; the dream and the clay; 1099; 5,000 gadyāṇas; 1104; Tipu’s elephants and drums (believed); 108 Abhimāna Kṣetras. <b>Festival:</b> Karnataka Tourism (Bharaṇī to Hasta, Puṣya night); Hindu Blog; Deccan Herald.</p>
<p><b>Not verified:</b> the Rāya Gopura as “never completed” (widely said); Rāmānuja opening worship to all communities (tradition). For the Tipu record and the Melukōṭe massacre memory, see our special article. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('deity','The Lord of Melukōṭe'),('legends1','Legends · Rāma’s Beloved'),('legends2','Legends · Rāmānuja’s Dream'),('legends3','Legends · Bībī Nācciyār'),('ramanuja','Rāmānuja at Melukōṭe'),('narasimha','Yoga Narasiṃha'),('crowns','The Three Crowns'),('vairamudi','The Vairamuḍi Brahmotsava'),('town','The Temple Town'),('history','History'),('learning','A Town of Learning'),('around','Around Melukōṭe'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">MELUKŌṬE</h1>
  <div class="series">CELUVANĀRĀYAṆA · YOGA NARASIṂHA · A REFERENCE GUIDE</div>
  <div class="tag">Rāmānuja’s hill of the beautiful Lord</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>On a rocky hill north of the Kāverī, a great teacher once dug for white clay and found a god.</p>
    <p>That teacher was <b>Rāmānuja</b>, the god was <b>Tirunārāyaṇa</b>, and the hill became <b>Melukōṭe</b>: a town of temples and tanks, of Sanskrit scholars, of a Sultan’s daughter who loved the Lord, and of a diamond crown that only comes out at night.</p>
    <p>This guide tells its legends, its history and its festival.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Govinda Govinda,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A crown that only comes out at night?","Diamonds, a demon, Garuḍa and the police. Best festival story in Karnataka!")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Melukote.html','w').write(head+b+tail())
print('ok')
