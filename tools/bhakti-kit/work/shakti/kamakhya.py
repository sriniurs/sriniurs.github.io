exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Kāmākhyā · Kāmarūpa · The 18 Śakti Pīṭhas · srini.presents',
 'Kāmākhyā on the Nīlācala hill at Guwahati, the thirteenth of the 18 Śakti Pīṭhas and greatest seat of Tantra: the yoni-stone and its spring, Satī, Kāmadeva reborn, Naraka and the unfinished steps, the Kālikā Purāṇa and Yoginī Tantra, the Daśa Mahāvidyā temples, Ambubācī Melā, bali, the Mlecchas, Koch and Ahoms, and the Nīlācala style. A detailed illustrated reference guide.')
def g(lat,lon): return 40+(lon-91.62)*2600, 30+(26.21-lat)*2600
def GMAP(w=560,h=300):
    out=f'<rect width="{w}" height="{h}" fill="#e7f0d8"/>'
    a=g(26.20,91.62);b=g(26.175,91.70);c=g(26.195,91.76);d=g(26.19,91.82)
    out+=f'<path d="M0 {a[1]-10:.0f} Q{b[0]:.0f} {b[1]-30:.0f} {c[0]:.0f} {c[1]-14:.0f} T{w} {d[1]-20:.0f}" stroke="#4aa3df" stroke-width="44" fill="none"/>'+T(90,a[1]-14,'BRAHMAPUTRA',12,'#1d4f9a','start')
    hx,hy=g(26.166,91.705); out+=f'<ellipse cx="{hx:.0f}" cy="{hy+10:.0f}" rx="70" ry="40" fill="#5a8a4a" stroke="#111" stroke-width="2"/>'+T(f'{hx:.0f}',f'{hy+44:.0f}','NĪLĀCALA',11,'#fff')
    ux,uy=g(26.202,91.745); out+=f'<ellipse cx="{ux:.0f}" cy="{uy:.0f}" rx="16" ry="8" fill="#5a8a4a" stroke="#111"/>'
    for nm,la,lo,col,side in (('KĀMĀKHYĀ',26.166,91.705,'#c0392b','t'),('Bhuvaneśvarī',26.163,91.712,'#ffd166','b'),('Umānanda (Bhairava)',26.202,91.745,'#bbb','r'),('Guwahati',26.15,91.76,'#bbb','r'),('Pāṇḍu',26.16,91.67,'#bbb','l')):
        x,y=g(la,lo); r=8 if col=='#c0392b' else 6
        out+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+(T(f'{x:.0f}',f'{y-30:.0f}',nm,13,'#111') if side=='t' else T(f'{x+10:.0f}',f'{y+16:.0f}',nm,11,'#fff','start') if side=='b' else T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',nm,12,'#111','start' if side=='r' else 'end'))
    return out+T(w-10,h-8,'simplified, not to scale',10,'#555','end')
def YONI(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-80 0 Q-40 -50 0 -8 Q40 -50 80 0 Q40 30 0 18 Q-40 30 -80 0z" fill="#6a5a4a"/>'
 '<path d="M-30 -2 Q0 20 30 -2 Q0 8 -30 -2z" fill="#4aa3df"/>'+''.join(f'<circle cx="{dx}" cy="{dy}" r="5" fill="#e0115f"/>' for dx,dy in ((-40,-10),(40,-10),(-20,-20),(20,-20),(0,-14)))
 +'<path d="M-60 -16 q60 20 120 0" stroke="#c0392b" stroke-width="3" fill="none"/></g>')
def NTEMPLE(x,y,s=1,c='#e8dcc0'): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-70" y="-40" width="140" height="40" fill="#bfae8f"/>'
 f'<path d="M-40 -40 q0 -70 40 -90 q40 20 40 90z" fill="{c}"/>'+''.join(f'<path d="M{dx-10} -40 q10 -40 10 -50 q0 10 10 50z" fill="{c}"/>' for dx in (-55,55))
 +''.join(f'<path d="M{-34+k*17} -40 q2 -40 {17-k*0} -80" stroke="#999" stroke-width="1" fill="none"/>' for k in range(5))+'<circle cy="-134" r="6" fill="#e0a800"/><path d="M0 -140 v-18"/><path d="M0 -158 l14 5 l-14 5z" fill="#c0392b"/></g>')
def KAMADEVA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,'#2a9d6f','#f2c79b',1)+'<path d="M24 -24 q14 -20 0 -40" stroke="#7a5a2a" stroke-width="3" fill="none"/><path d="M24 -24 v-40" stroke="#e0115f" stroke-width="1.5"/><circle cx="-2" cy="-62" r="6" fill="#e0115f"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A beehive-domed temple on a green hill above a great river, red cloth and hibiscus flowers in front">'
 '<rect width="380" height="268" fill="#4a0e0e" rx="8"/><path d="M0 230 Q190 210 380 232 V268 H0z" fill="#4aa3df"/><path d="M40 230 Q190 120 340 230z" fill="#3a6a3a"/>'
 +NTEMPLE(190,170,.95)+''.join(f'<circle cx="{120+i*22}" cy="{214+(i%2)*6}" r="6" fill="#e0115f" stroke="#111"/>' for i in range(7))+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Kāmākhyā</b>, the Goddess of desire and creation'),
 ('Form','No image: a <b>yoni</b>-shaped cleft in rock, kept wet by an underground spring'),
 ('Where','The <b>Nīlācala</b> hill, western Guwahati, Assam, above the <b>Brahmaputra</b>'),
 ('Pīṭha','Satī’s <b>yoni</b> fell here'),
 ('Hymn','<i>harikṣetre kāmarūpī</i>: “Kāmarūpī (she who takes any form she wishes) in Harikṣetra”'),
 ('Tantra','The greatest seat of Śākta Tantra; centre of the <b>Kulācāra</b> path'),
 ('Festival','<b>Ambubācī Melā</b>: the Goddess’s yearly menstruation; temple shut three days'),
 ('Complex','Temples of all ten <b>Mahāvidyās</b> on one hill'),
 ('Built','First temple 8th–9th c. (Mlecchas); rebuilt 1565 (Koch); added to by the Ahoms'),
 ('Bhairava','<b>Umānanda</b>, on an island in the Brahmaputra')])
 +talk("A temple with no image at all?","There's nothing carved because nothing needs to be. The rock and the spring are the Goddess.")))
pages.append(page('where','WHERE IT IS','A hill over the Brahmaputra',fig(560,300,'Simplified map of Guwahati: the Brahmaputra flowing past, Nilachal hill with Kamakhya and Bhuvaneshvari temples on top, and the small Umananda island in the river',GMAP())
 +'<div class="g2"><div>'+minimap([13],'Map of India with Kamakhya marked in Assam')+'</div><div class="panel reading small"><p><b>The blue hill.</b> <b>Nīlācala</b>, “the blue mountain”, also <b>Kāmagiri</b>, rises on the south bank of the Brahmaputra at Guwahati.</p><p><b>The river.</b> Bhairava Umānanda sits on a small island in mid-stream, facing the hill.</p></div></div>'))
pages.append(page('names','THE NAMES','Desire, form and place',facts([
 ('Kāmākhyā','“She who is called Desire” or “the one who grants desire”'),
 ('Kāmarūpa','“Form of desire”: old name of Assam, where Kāma regained his form'),
 ('Nīlācala · Kāmagiri','The blue hill · the hill of desire'),
 ('Kubjikā Pīṭha','Another Tantric name for the place'),
 ('Prāgjyotiṣa','“Light of the East”: the ancient kingdom, capital near Guwahati'),
 ('Kāmarūpī · Harikṣetra','The hymn’s names: the Goddess who takes any form, in “Hari’s field”')])
 +talk("Kāmarūpa is a place and a story?","A god burned to ash got his body back here. The land kept the name 'form of desire'.")))
pages.append(page('pitha','THE PĪṬHA','Where the yoni fell',fig(560,170,'Shiva carrying Sati’s body as Vishnu’s discus cuts it, a piece falling onto a hill above a river',
 '<rect width="560" height="170" fill="#1a0e1e"/>'+STAR+SHIVA(150,40,.7)+SATI(220,60,.9,-8)+CHAKRA(300,70,14)+'<path d="M300 170 Q400 90 500 170z" fill="#3a6a3a"/><circle cx="400" cy="110" r="8" fill="#e0115f" stroke="#111"/><path d="M370 80 l20 22" stroke="#ffd166" stroke-width="3"/><path d="M0 164 h560" stroke="#4aa3df" stroke-width="10"/>')+'''<div class="steps">
<div><b>The fall.</b> As Śiva carried Satī’s body, Viṣṇu’s discus cut it piece by piece. Her <b>yoni</b>, the source of creation, fell on Nīlācala.</div>
<div><b>The hill turned blue.</b> The Kālikā Purāṇa says the hill turned blue (nīla) as it received her: hence Nīlācala.</div>
<div><b>Among the oldest.</b> Old texts count Kāmākhyā among the four <b>Ādi</b> (first) Pīṭhas, with Vimalā (feet), Tārā-Tāriṇī (breasts) and Dakṣiṇa Kālikā (face).</div>
</div>'''+talk("Why is the yoni Pīṭha considered the greatest?","Because it stands for creation itself. Every other Pīṭha is a part; this is the source.")))
pages.append(page('kama','LEGEND · KĀMADEVA REBORN','The god of love gets his body back',fig(560,170,'Shiva opening his third eye and burning the god of love with fire; later the god of love restored, with his wife Rati beside him',
 '<rect width="560" height="170" fill="#fdf1e8"/>'+SHIVA(120,70,.8)+'<path d="M134 50 L230 100" stroke="#ff8c1a" stroke-width="6"/>'+FLAME(240,150,.8)+'<path d="M300 100 h40" stroke="#111" stroke-width="3"/><path d="M340 100 l-10 -6 v12z" fill="#111"/>'+KAMADEVA(410,150,1)+person(470,150,'#e0115f','#f2c79b',.9))+'''<div class="steps">
<div><b>The arrow.</b> To wake Śiva from meditation so he would marry Pārvatī, the gods sent <b>Kāma</b>, god of love, to shoot him with a flower arrow.</div>
<div><b>Ashes.</b> Śiva opened his third eye and burned Kāma to ashes. His wife <b>Rati</b> wept.</div>
<div><b>Form again.</b> The Kālikā Purāṇa says Kāma regained his form (<b>rūpa</b>) by the grace of the Goddess here; so the land is <b>Kāmarūpa</b>, and she is <b>Kāmākhyā</b>.</div>
<div><b>A temple for her.</b> In thanks, Kāma is said to have had Viśvakarmā build her a shrine.</div>
</div>'''))
pages.append(page('naraka','LEGEND · NARAKA AND THE STEPS','A demon in love',fig(560,180,'A demon carrying stones up a hill path at night, the path unfinished near the top; a rooster crowing on a rock',
 '<rect width="560" height="180" fill="#0b1a3a"/>'+STAR+'<path d="M0 180 Q280 20 560 180z" fill="#2e5a2e"/>'+''.join(f'<rect x="{80+i*30}" y="{170-i*18}" width="28" height="8" fill="#9a8a7a" stroke="#111"/>' for i in range(6))
 +'<g transform="translate(280 70)">'+person(0,0,'#5a4a6a','#5a4a6a',1)+'<rect x="-14" y="-60" width="28" height="12" fill="#9a8a7a" stroke="#111"/></g>'
 +'<g transform="translate(420 100) scale(.8)" stroke="#111" stroke-width="2"><ellipse cy="-20" rx="22" ry="15" fill="#f4f4f4"/><circle cx="-20" cy="-36" r="9" fill="#f4f4f4"/><path d="M-26 -44 q4 -8 8 -2 q4 -8 8 0" fill="#c0392b"/><path d="M-30 -36 l-8 3 l8 3z" fill="#e0a800"/></g>'+T(470,60,'COCK-A-',11,'#ffd166')+T(470,74,'DOODLE!',11,'#ffd166'))+'''<div class="steps">
<div><b>The suitor.</b> <b>Naraka</b>, the demon-king of Prāgjyotiṣa, wanted to marry Kāmākhyā.</div>
<div><b>The test.</b> She set a condition: build a stone stairway up Nīlācala in one night, before the cock crowed.</div>
<div><b>The trick.</b> He nearly finished. Just before dawn the Goddess made a rooster crow early. Naraka, beaten, killed the bird in rage.</div>
<div><b>The path.</b> The steep stone way up the hill is called the <b>Mekhelā-ujowā</b> path and linked to Naraka’s unfinished stairs. Kṛṣṇa later killed Naraka.</div>
</div>'''+talk("A rooster again? Like Pīṭhāpuram!","Gods in India love an early rooster. It's the oldest trick for ending a deadline.")))
pages.append(page('sanctum','THE SANCTUM','The cave of the spring',fig(560,210,'A cutaway of the temple: steep steps leading down into a dark cave below ground, a sloping rock with a water-filled cleft at the bottom, lamps glowing',
 '<rect width="560" height="210" fill="#e8dcc0"/><rect y="90" width="560" height="120" fill="#3a2a1a"/>'+''.join(f'<rect x="{140+i*16}" y="{90+i*12}" width="16" height="12" fill="#8a7a6a" stroke="#111"/>' for i in range(7))+YONI(360,180,1)
 +''.join(f'<g transform="translate({x} 150)"><path d="M-6 0 h12 l-3 -8 h-6z" fill="#e0a800"/><path d="M0 -8 q-4 -8 0 -14 q4 6 0 14" fill="#ff8c1a"/></g>' for x in (280,440))+T(60,60,'ABOVE: THE TEMPLE',11,'#7a1d12','start')+T(60,120,'BELOW: THE CAVE',11,'#ffd166','start'))+facts([
 ('Below ground','The <b>garbhagṛha</b> is a small, dark cave, reached down narrow, steep stone steps'),
 ('The stone','A sheet of stone slopes down from both sides into a <b>yoni</b>-shaped hollow, about ten inches deep'),
 ('The spring','The hollow is always full: a perennial underground spring feeds it'),
 ('Covered','The stone is kept under red cloth and flowers; pilgrims touch the water'),
 ('Facing','The temple faces east, but the yoni is worshipped facing north, by one account')])))
pages.append(page('kalika','THE TEXTS','Kālikā Purāṇa and Yoginī Tantra',facts([
 ('Kālikā Purāṇa','An Upapurāṇa of around the 10th–11th century, likely from Kāmarūpa: the fullest account of the Goddess, her rites, the hill and the land'),
 ('Iconography','There she has <b>six heads</b> of different colours, each with a third eye, and <b>twelve arms</b>'),
 ('Naraka','The Purāṇa makes Naraka, ancestor of Kāmarūpa’s kings, a devotee of the Goddess, tying king, land and Goddess together'),
 ('Yoginī Tantra','A later text (16th c.) that links Kāmākhyā closely with <b>Kālī</b> and dwells on the yoni as the source of creation'),
 ('Kulācāra','The Tantric “path of the clan” centred here')])
 +talk("A whole Purāṇa about one hill?","Kāmarūpa wrote its own scripture. That's how important this hill was to Assam's kings.")))
pages.append(page('mahavidya','THE TEN MAHĀVIDYĀS','Ten great wisdoms on one hill','<table class="ct"><tr><th>#</th><th>Mahāvidyā</th><th>Where on Nīlācala</th></tr>'
 +''.join(f'<tr><td>{i+1}</td><td><b>{a}</b></td><td>{b}</td></tr>' for i,(a,b) in enumerate((('Kālī','Own temple'),('Tārā','Own temple, near the main gate'),('Tripurasundarī','Inside the main temple, with Kāmākhyā'),('Bhuvaneśvarī','Own temple at the hilltop'),('Bhairavī','Own temple'),('Chinnamastā','Own temple'),('Dhūmāvatī','Own temple'),('Bagalāmukhī','Own temple'),('Mātaṅgī','Inside the main temple'),('Kamalā','Inside the main temple'))))+'</table>'
 +'<div class="panel reading small"><p><b>Why here?</b> The ten Mahāvidyās are ten faces of the one Goddess, from terrifying to gracious. Nowhere else are all ten worshipped together on one sacred hill.</p></div>'))
pages.append(page('ambubachi','AMBUBĀCĪ MELĀ','When the Goddess rests',fig(560,180,'A temple with doors closed and a red cloth over the entrance, crowds of pilgrims and sadhus camped around in the monsoon rain',
 '<rect width="560" height="180" fill="#9aa8b8"/>'+''.join(f'<path d="M{(i*37)%560} {(i*23)%90} l-6 14" stroke="#dfe8f5" stroke-width="2"/>' for i in range(40))+NTEMPLE(280,150,.8)+'<rect x="262" y="118" width="36" height="32" fill="#c0392b" stroke="#111" stroke-width="2"/>'
 +''.join(f'<g transform="translate({x} 172)"><path d="M-14 0 l14 -20 l14 20z" fill="{c}" stroke="#111"/></g>' for x,c in ((60,'#ff8c1a'),(110,'#ffd60a'),(160,'#c0392b'),(400,'#ff8c1a'),(450,'#2a9d6f'),(500,'#ffd60a'))))+facts([
 ('When','Mid-Āṣāḍha (June), at the height of the monsoon, as the Sun enters Mṛgaśirā’s last quarter'),
 ('Belief','The Goddess, like the earth soaked by rain, has her yearly <b>menstruation</b>'),
 ('Closed','The temple doors stay shut for <b>three days</b>; farming, digging and some rites pause across the region'),
 ('Reopening','On the fourth day she is bathed and the doors reopen to huge crowds'),
 ('Prasāda','Pieces of red cloth (<b>raktavastra</b>), said to be soaked in her flow, are prized'),
 ('Crowds','Sādhus, tāntrikas and householders gather in their hundreds of thousands')])
 +talk("A festival for menstruation?","For the earth's fertility. In Assam, the Goddess and the soil rest together, then wake.")))
pages.append(page('bali','WORSHIP AND BALI','An old Tantric rite',facts([
 ('Daily','Worship of the yoni-stone with flowers, red cloth, lamps; Kumārī pūjā of young girls as the Goddess'),
 ('Bali','Animal sacrifice still takes place: chiefly goats, buffaloes, pigeons and ducks, all male; females are never offered'),
 ('Substitutes','Many devotees offer pumpkins, sugarcane or gourds instead'),
 ('Debate','Some call it a living tradition; others oppose it on grounds of cruelty. Courts and governments have been asked to rule more than once'),
 ('Priests','Hereditary priestly families of the Nīlācala, the <b>Bordeuri</b> and others')])
 +talk("Do people still sacrifice animals here?","Yes, as Tantric rites have for centuries. It's argued over openly, and many offer fruit instead.")))
pages.append(page('festivals','THROUGH THE YEAR','More than Ambubācī',facts([
 ('Durgā Pūjā','In autumn, celebrated with great Tantric rites'),
 ('Manasā Pūjā · Deodhanī','In Śrāvaṇa, for the snake goddess, with trance dancers called Deodhanīs'),
 ('Pohān Biyā','A ritual wedding of Kāmeśvara and Kāmeśvarī in Pauṣa'),
 ('Vasantī Pūjā','The spring Durgā worship in Caitra'),
 ('Madandeul','Worship of Kāmadeva and Śiva, also in Caitra')])))
pages.append(page('temple','THE TEMPLE','The Nīlācala style',fig(560,220,'A temple with a beehive-shaped brick dome surrounded by smaller domes, on a cruciform stone base, with a pillared front hall',
 '<rect width="560" height="220" fill="#cfe3f5"/><rect y="190" width="560" height="30" fill="#5a8a4a"/>'+NTEMPLE(260,190,1.2)+'<rect x="340" y="150" width="160" height="40" fill="#bfae8f" stroke="#111" stroke-width="2"/><path d="M336 150 l84 -30 l84 30z" fill="#c9a26b" stroke="#111" stroke-width="2"/>'+T(420,210,'NAṬAMANDIRA',10,'#111'))+facts([
 ('Shape','A stone cruciform base topped by a polygonal, <b>beehive-like brick dome</b>, ringed by small domes: the <b>Nīlācala type</b>'),
 ('Four chambers','<b>Garbhagṛha</b> (the cave), <b>calanta</b>, <b>pañcaratna</b> and the <b>naṭamandira</b> (hall for music and dance)'),
 ('Old base','The lower stone parts belong to the early Kāmarūpa-era temple; the dome is Koch work'),
 ('Sculpture','Older stone carvings are set into the outer walls'),
 ('Naṭamandira','Built under the Ahom king Rājeśvar Siṃha; inscriptions of 1759 and 1782 inside')])))
pages.append(page('history1','HISTORY · TO 1565','From Mlecchas to Koch',tl([
 ('5th–7th c.','Archaeology hints at a structure this old under the temple.'),
 ('9th c.','First inscription to name Kāmākhyā: the Tezpur plates of <b>Vanamālavarman</b> of the <b>Mleccha</b> dynasty; a large 8th–9th-c. temple, Nāgara in style.'),
 ('10th–11th c.','The <b>Kālikā Purāṇa</b> is written; the temple complex grows.'),
 ('Early 16th c.','Tradition says the temple was destroyed, often blamed on <b>Kālāpāhāṛ</b>; historians doubt he reached here.'),
 ('Early 1500s','<b>Viśva Siṃha</b>, founder of the Koch dynasty, finds the ruins and revives worship.'),
 ('1565','His son King <b>Naranārāyaṇa</b> completes the rebuilding, supervised by his brother <b>Chilārāy</b>.')])
 +'<div class="panel reading small"><p><b>The dome.</b> After two failed tries at rebuilding the stone tower, a Koch artisan, <b>Meghamukdam</b>, is said to have built it in brick: the beginning of the Nīlācala style.</p></div>'))
pages.append(page('history2','HISTORY · AFTER 1565','The Ahom era',tl([
 ('Koch legend','A curse is said to forbid Koch royals from seeing the temple; it is still remembered.'),
 ('1658','The <b>Ahoms</b> under Jayadhvaj Siṃha take Kāmarūpa; their interest in the temple grows.'),
 ('c. 1700','<b>Rudra Siṃha</b> invites the Śākta teacher <b>Kṛṣṇarām Bhaṭṭācārya</b> from Nadia in Bengal.'),
 ('1714–44','<b>Śiva Siṃha</b> places the temple and hill under Kṛṣṇarām’s line, the <b>Parvatiyā Gosāins</b>.'),
 ('1759, 1782','<b>Rājeśvar Siṃha</b> and <b>Gaurīnāth Siṃha</b> build and record; the naṭamandira.'),
 ('1826','The British annex Assam; the temple carries on under its priests.'),
 ('2015','The Supreme Court hands administration to the <b>Bordeuri Samāj</b>.')])))
pages.append(page('umananda','UMĀNANDA AND THE GUARDIANS','Bhairava on an island',facts([
 ('Umānanda','Śiva as <b>Bhairava</b> of the Pīṭha, on Peacock Island in the Brahmaputra'),
 ('Legend','Śiva sat in meditation on this island; here Kāma is said to have shot his arrow'),
 ('Built','The temple there was raised by the Ahom king Gadādhar Siṃha’s officers, late 17th c.'),
 ('Saubhāgya Kuṇḍa','A sacred pool beside the main temple'),
 ('Gaṇeśa','Worshipped first, at the entrance')])
 +talk("The Bhairava is in the middle of a river?","Facing her hill across the water. You see one from the other.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Yoni','Womb, source; the female sign of creation'),('Kāma','Desire; the god of love'),('Rūpa','Form'),('Nīla','Blue'),('Garbhagṛha','“Womb-house”, the sanctum'),
 ('Ambubācī','“Water-flow”: the Goddess’s menses'),('Raktavastra','Red cloth'),('Bali','Sacrificial offering'),('Mahāvidyā','“Great wisdom”: ten forms of the Goddess'),
 ('Kulācāra','A Tantric path'),('Naṭamandira','Hall for music and dance'),('Kumārī','Young girl worshipped as the Goddess')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Pīṭha.</b> Satī’s yoni on Nīlācala: no image, a wet cleft in rock fed by a spring.</div>
<div><b>The legends.</b> Kāma regains his form; Naraka’s steps stop at the rooster’s crow.</div>
<div><b>Tantra.</b> The Kālikā Purāṇa, the Yoginī Tantra and all ten Mahāvidyās on one hill.</div>
<div><b>Ambubācī.</b> Three closed days of the Goddess’s menstruation; red cloth as prasāda.</div>
<div><b>History.</b> Mleccha kings, the Koch rebuilding of 1565, Ahom patrons, the Nīlācala dome.</div>
</div>'''+talk("One line to remember?","At Kāmākhyā the Goddess isn't carved; she flows.")+'<div class="key">The thirteenth seat of the Mother: <b>Kāmākhyā of Kāmarūpa</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple and history:</b> Wikipedia, “Kamakhya Temple” (Nīlācala; Kulācāra; Ambubācī; 8th–9th c. with rebuildings; Nīlācala type; four oldest pīṭhas; Tezpur plates of Vanamālavarman; 5th–7th-c. strata; Nāgara/Mālava plinth; tradition of destruction; Chilārāy; Meghamukdam; Ahoms from 1658; Rājeśvar 1759 and Gaurīnāth 1782 inscriptions; garbhagṛha cave, sloping stone, ten-inch hollow, perennial spring; four chambers; brick beehive dome; Kālikā Purāṇa and Naraka). Wikipedia, “Kamakhya” (six heads, twelve arms; Kāmarūpa; Naraka). sacredsites.com (Viśva Siṃha; Naranārāyaṇa 1565; British 1826). abhipedia (2015 Supreme Court; Bordeuri Samāj). templesinindiainfo.com (no image; spring; faces north; Mahāvidyā locations). greenmesg.org (Kubjikā Pīṭha; Kāmadeva regains form; kuṇḍas). encyclopedia.pub (four Ādi Pīṭhas). diversityassam.com (Naraka; Ambubācī three days; Mekhelā-ujowā path). bhaktidarshan.in (Yoginī Tantra and Kālī).</p>
<p><b>Sources differ:</b> the Kālāpāhāṛ story; dates of the Kālikā Purāṇa and Yoginī Tantra. <b>Not verified:</b> Kṛṣṇarām’s dates and the Parvatiyā Gosāins as given; the Koch curse; Umānanda’s builder; Pohān Biyā and Madandeul timing; the bali list. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('pitha','The Pīṭha'),('kama','Legend · Kāmadeva Reborn'),('naraka','Legend · Naraka and the Steps'),('sanctum','The Sanctum'),('kalika','The Texts'),('mahavidya','The Ten Mahāvidyās'),
 ('ambubachi','Ambubācī Melā'),('bali','Worship and Bali'),('festivals','Through the Year'),('temple','The Temple'),('history1','History · to 1565'),('history2','History · after 1565'),('umananda','Umānanda and the Guardians'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 13 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7.4vw,74px)">KĀMĀKHYĀ</h1>
  <div class="series">KĀMARŪPA · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess who is not carved, but flows</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>On a green hill above the Brahmaputra, pilgrims climb down steep stone steps into a dark cave. There is no statue at the bottom. There is a cleft in the rock, always wet from a spring, covered in red cloth and hibiscus. This is <b>Kāmākhyā</b>, where Satī’s yoni fell, the source of creation.</p>
    <p>Here the god of love got his body back, a demon-king lost a bet to a rooster, and once a year the temple shuts for three days while the Goddess rests, as the monsoon soaks the earth.</p>
    <p>This is the greatest seat of Tantra in India. This guide tells its legends, its rites, its ten Mahāvidyās and the kings who built and rebuilt it.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā Kāmākhyā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is Kāmākhyā scary? People talk about Tantra and black magic.","It's powerful, not sinister. Families come for blessings and children; the Tantra is about the power of creation.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Kamakhya.html','w').write(head+b+tail())
print('ok',len(pages))
