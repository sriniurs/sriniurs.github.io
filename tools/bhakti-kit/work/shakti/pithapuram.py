exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Puruhūtikā · Pīṭhāpuram · The 18 Śakti Pīṭhas · srini.presents',
 'Puruhūtikā of Pīṭhāpuram, the tenth of the 18 Śakti Pīṭhas: the Goddess worshipped by Indra, Kukkuṭeśvara the rooster-Śiva, Gayāsura and the three Gayās, the Pāda Gayā tank, Śrīpāda Śrīvallabha, and ancient Piṣṭapura from Samudragupta to the Mahārājas. An illustrated reference guide.')
def gd(lat,lon): return 40+(lon-81.6)*600, 20+(17.3-lat)*360
COASTG=[(17.30,82.62),(17.10,82.40),(16.98,82.32),(16.85,82.30),(16.70,82.22),(16.55,82.10)]
def GMAP(marks,w=560,h=280):
    sea=f'M{w} 0 '+' '.join(f'L{gd(a,b)[0]:.0f} {gd(a,b)[1]:.0f}' for a,b in COASTG)+f' L{gd(16.55,82.10)[0]:.0f} {h} L{w} {h}z'
    g=''
    for la,lo,t,side,col in marks:
        x,y=gd(la,lo); r=8 if col=='#c0392b' else 6
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',t,12,'#111','start' if side=='r' else 'end')
    riv=f'M0 {gd(17.15,81.6)[1]:.0f} L{gd(17.0,81.78)[0]:.0f} {gd(17.0,81.78)[1]:.0f} L{gd(16.85,81.95)[0]:.0f} {gd(16.85,81.95)[1]:.0f}'
    return (f'<rect width="{w}" height="{h}" fill="#e7f0d8"/><path d="{sea}" fill="#9ad1f5" stroke="#111" stroke-width="2"/>'
     +f'<path d="{riv}" stroke="#4aa3df" stroke-width="10" fill="none"/><path d="M{gd(16.85,81.95)[0]:.0f} {gd(16.85,81.95)[1]:.0f} L{gd(16.62,82.22)[0]:.0f} {gd(16.62,82.22)[1]:.0f} M{gd(16.85,81.95)[0]:.0f} {gd(16.85,81.95)[1]:.0f} L{gd(16.55,81.85)[0]:.0f} {h}" stroke="#4aa3df" stroke-width="6" fill="none"/>'
     +T(70,gd(17.12,81.6)[1]-10,'GODĀVARĪ',11,'#1d4f9a','start')+T(w-20,h-20,'BAY OF BENGAL',12,'#1d4f9a','end')+g+T(w-10,16,'simplified, not to scale',10,'#555','end'))
def ROOSTER(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cy="-20" rx="26" ry="18" fill="#f4f4f4"/><path d="M20 -26 q20 -30 6 -50 q-6 14 -14 20z" fill="#2a7a4a"/><path d="M24 -30 q16 -10 22 4" fill="none" stroke="#c0392b" stroke-width="4"/>'
 '<circle cx="-24" cy="-40" r="11" fill="#f4f4f4"/><path d="M-30 -50 q4 -10 8 -2 q4 -10 8 0" fill="#c0392b"/><path d="M-34 -40 l-10 3 l10 3z" fill="#e0a800"/><circle cx="-26" cy="-42" r="2" fill="#111"/><path d="M-28 -30 q2 8 6 0" fill="#c0392b"/>'
 '<path d="M-8 -2 v14 M8 -2 v14" stroke="#e0a800" stroke-width="3"/></g>')
def GAYASURA(x,y,w=420,s=1): return (f'<g transform="translate({x} {y})" stroke="#111" stroke-width="2"><path d="M0 0 q{w/2} -30 {w} 0 q-{w/2} 20 -{w} 0z" fill="#5a4a6a"/><circle cx="-14" cy="-6" r="18" fill="#5a4a6a"/><circle cx="-18" cy="-10" r="2.5" fill="#fff"/>'
 f'<path d="M{w} 0 l14 -14 M{w} 0 l14 10" stroke-width="5"/></g>')
def PUR(x,y,s=1): return GENTLE(x,y,s).replace('#e05a8a','#c0392b')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The Goddess Puruhutika with a white rooster crowing at midnight beside a temple tank, the moon above">'
 '<rect width="380" height="268" fill="#0b1a3a" rx="8"/><path d="M300 40 a24 24 0 1 0 18 40 a18 18 0 1 1 -18 -40z" fill="#fff8c0"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="1.6" fill="#fff"/>' for a,b in ((40,30),(120,50),(220,24),(350,120),(80,90)))
 +'<rect y="210" width="380" height="58" fill="#4aa3df"/>'+''.join(f'<rect x="{k*38}" y="{204-(k%2)*4}" width="38" height="10" fill="#e2cfa8" stroke="#111" stroke-width="1"/>' for k in range(10))
 +PUR(190,130,1.5)+ROOSTER(310,200,1.3)+'<path d="M260 150 q-10 -10 -4 -20 M248 154 q-16 -14 -8 -30" fill="none" stroke="#ffd166" stroke-width="2"/>'+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Puruhūtikā</b>, “she who was worshipped by Puruhūta (Indra)”; also <b>Rājarājeśvarī</b>. Pīṭha no. 10 of the eighteen'),
 ('Hymn line','<i>pīṭhikāyāṃ puruhūtikā</i>: “Puruhūtikā in Pīṭhikā”'),
 ('Where','<b>Pīṭhāpuram</b> (Pithapuram), Kakinada district, Andhra Pradesh, in the Godāvarī delta'),
 ('Body part','Satī’s <b>left hand</b> by most accounts; some say her back'),
 ('Her Lord','Śiva as <b>Kukkuṭeśvara</b>, “Lord in the form of a rooster”, a self-arisen liṅga'),
 ('Pāda Gayā','One of the <b>three Gayās</b>, where the feet of the giant <b>Gayāsura</b> lie; a sacred tank for rites to ancestors'),
 ('Saint','Birthplace of <b>Śrīpāda Śrīvallabha</b> (14th c.), honoured as an incarnation of Dattātreya'),
 ('Ancient town','<b>Piṣṭapura</b> of Samudragupta’s pillar (c. 350 CE) and the early Eastern Chalukyas')])
 +talk("A Śiva who's a rooster?","A rooster who crowed at midnight and ended a sacrifice early. You'll see why.")))
pages.append(page('where','WHERE IT IS','In the Godāvarī delta',fig(560,280,'Simplified map of the Godavari delta: Pithapuram in red near the coast north of Kakinada, Samalkot and Draksharamam nearby, Rajahmundry upriver',
 GMAP([(17.12,82.25,'PĪṬHĀPURAM','l','#c0392b'),(16.99,82.25,'Kakinada','l','#bbb'),(17.05,82.17,'Sāmalkoṭ','l','#bbb'),(16.79,82.06,'Drākṣārāmam','l','#ffd166'),(17.0,81.78,'Rājamahendravaram','r','#bbb')]))+'''<div class="panel reading">
<p><b>The town.</b> Pīṭhāpuram lies a short way inland from the sea, north of Kakinada, in the rich rice country of the <b>Godāvarī</b> delta.</p>
<p><b>Two pīṭhas close together.</b> <b>Drākṣārāmam</b>, home of the next-but-one pīṭha, Māṇikyāmbā, is a short distance away across the delta.</p>
<p><b>The temple.</b> The Kukkuṭeśvara complex stands on the town’s edge, with the Goddess’s shrine in its north-east corner.</p>
</div>'''))
pages.append(page('names','HER NAMES','Indra’s Goddess',facts([
 ('Puruhūtikā','From <b>Puruhūta</b>, “much invoked”, a name of <b>Indra</b>: the Goddess Indra worshipped'),
 ('Rājarājeśvarī','“Queen of kings”: the name used in daily worship'),
 ('Pīṭhikā','“The little seat”: the hymn’s name for the town; also Pīṭhikāpuri'),
 ('Piṣṭapura','The ancient name, in inscriptions from the 4th century'),
 ('Pāda Gayā','“Gayā of the feet”, also <b>Dakṣiṇa Gayā</b>, the southern Gayā')])
 +talk("The town's name means 'seat'?","Pīṭha-puram, the city of the seat. Some say the Goddess's seat gave the town its name.")))
pages.append(page('pitha','THE PĪṬHA','Where Satī’s hand fell',fig(560,150,'Shiva carrying Sati across a night sky, a glowing piece falling into a delta by the sea',
 '<rect width="560" height="150" fill="#2a0805"/>'+STAR+SHIVA(140,60,.7)+SATI(162,64,.55,-10)+'<path d="M190 80 q80 10 190 40" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><circle cx="382" cy="120" r="6" fill="#ffd166"/><rect x="420" y="120" width="140" height="30" fill="#4aa3df"/><rect y="132" width="420" height="18" fill="#5a8a3a"/>'+T(440,24,'PĪṬHIKĀ',14,'#ffd166'))+'''<div class="panel reading">
<p><b>The verse.</b> <i>ujjayinyāṃ mahākālī, pīṭhikāyāṃ puruhūtikā</i>: Ujjain, then straight to the eastern coast.</p>
<p><b>What fell here.</b> Satī’s <b>left hand</b>, by most local accounts; other lists say her back or the rear of her body.</p>
<p><b>Three-fold holy.</b> Pīṭhāpuram is at once a <b>Śiva</b> kṣetra (Kukkuṭeśvara), a <b>Śakti</b> Pīṭha (Puruhūtikā) and a <b>Gayā</b> for the dead, and, for many, a <b>Datta</b> kṣetra too.</p>
</div>'''))
pages.append(page('goddess','THE GODDESS','In the north-east corner',fig(560,200,'A small Goddess shrine in the corner of a temple courtyard, its walls carved with small panels of goddesses, the four-armed Goddess inside',
 '<rect width="560" height="200" fill="#fde4e4"/><rect x="40" y="20" width="480" height="170" fill="#f3e3c3" stroke="#111" stroke-width="2"/><rect x="330" y="30" width="180" height="150" fill="#fde4e4" stroke="#111" stroke-width="2"/>'
 +''.join(f'<rect x="{336+(k%6)*28}" y="{36+(k//6)*130}" width="24" height="12" fill="#e2cfa8" stroke="#111" stroke-width="1"/>' for k in range(12))+PUR(420,110,1.2)+'<path d="M392 90 l-16 -10 M448 90 l16 -10" stroke="#f2c79b" stroke-width="6"/>'+T(180,60,'KUKKUṬEŚVARA',12,'#1d4f9a')+TEMPLE(180,170,1.6,'#dfe8f5'))+'''<div class="g2">
<div class="card bg-red"><h4>🛕 Her shrine</h4><p>Puruhūtikā’s shrine stands in the <b>north-east corner</b> of the Kukkuṭeśvara complex. The image has <b>four arms</b>. Small carvings of all <b>eighteen</b> great pīṭhas run round its walls.</p></div>
<div class="card bg-yellow"><h4>🔱 Her worship</h4><p>In her worship, <b>Indra</b> is named as the seer and <b>Kukkuṭeśvara</b> as the guru. A local tale says the original image lies buried beneath the shrine.</p></div>
</div>'''+talk("All eighteen carved on one shrine?","A whole pilgrimage on four walls. Walk round her and you've greeted every one.")))
pages.append(page('indra','THE LEGEND · INDRA','How she got her name',fig(560,170,'Indra, king of the gods with a thunderbolt, kneeling in penance before the Goddess, his crown set aside',
 '<rect width="560" height="170" fill="#ffe9c4"/>'+PUR(380,90,1.2)+'<g transform="translate(200 160)">'+person(0,0,'#ffd60a','#f2c79b',1.2)+'</g><path d="M150 140 l10 -30 l8 14 l10 -26" stroke="#111" stroke-width="3" fill="none"/><path d="M110 150 h30 l-4 -10 h-22z" fill="#e0a800" stroke="#111"/>'+T(200,30,'INDRA',13,'#1d4f9a'))+'''<div class="steps">
<div><b>A king disgraced.</b> <b>Indra</b>, king of the gods, wronged <b>Ahalyā</b>, wife of the sage Gautama. The sage’s curse left him maimed and shamed.</div>
<div><b>The penance.</b> Leaving his throne, Indra came to <b>Pīṭhikāpuri</b> and did long penance to the Divine Mother.</div>
<div><b>The name.</b> She appeared, healed him and restored his fortune. Indra, “Puruhūta”, worshipped her ever after, and she became <b>Puruhūtikā</b>.</div>
</div>'''+talk("Even the king of the gods needed her help?","Especially him. Pride falls hardest, and the Mother picks it up.")))
pages.append(page('gaya','THE LEGEND · GAYĀSURA','The giant and the rooster',fig(560,200,'A giant demon lying stretched across the land, three gods disguised as priests performing a fire sacrifice on his chest, a white rooster crowing at midnight',
 '<rect width="560" height="200" fill="#0b1a3a"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="1.6" fill="#fff"/>' for a,b in ((40,30),(140,20),(260,40),(380,24),(500,30)))+'<path d="M480 30 a14 14 0 1 0 10 24 a10 10 0 1 1 -10 -24z" fill="#fff8c0"/>'
 +GAYASURA(70,150,400)+FLAME(250,128,.6)+''.join(person(x,128,'#fff','#c98b5a',.55) for x in (200,300))+ROOSTER(510,170,1.1)+T(60,190,'HEAD · GAYĀ',10,'#ffd166','start')+T(270,190,'NAVEL · JĀJPUR',10,'#ffd166')+T(470,120,'FEET · PĪṬHĀPURAM',10,'#ffd166','end'))+'''<div class="steps">
<div><b>The giant.</b> <b>Gayāsura</b>, a pious asura, grew so mighty by penance that he ruled the three worlds and displaced Indra.</div>
<div><b>The request.</b> Brahmā, Viṣṇu and Śiva came to him as Brahmins and asked for a holy place for a sacrifice. He offered his own body: it stretched from <b>Gayā</b> in Bihar to <b>Pīṭhāpuram</b>. The rite would last seven days, from cock-crow to cock-crow.</div>
<div><b>The rooster.</b> On the sixth night, Śiva took the form of a <b>rooster</b> and crowed at midnight. Thinking the rite complete, Gayāsura stirred, and the sacrifice was spoiled.</div>
<div><b>His boon.</b> Instead of asking for himself, he asked that Viṣṇu stay at his head, Brahmā at his navel and Śiva, as the rooster, at his feet, and that rites for the dead there should free the ancestors. So Śiva is <b>Kukkuṭeśvara</b>.</div>
</div>'''))
pages.append(page('trigaya','THE THREE GAYĀS','And three Śakti Pīṭhas',fig(560,150,'Map of eastern India with three points along a line: Gaya in Bihar, Jajpur in Odisha, Pithapuram in Andhra',
 '<rect width="560" height="150" fill="#eef3fa"/><g transform="translate(-100 -170) scale(1.2)">'+''.join(f'<circle cx="{xy(a,b)[0]:.0f}" cy="{xy(a,b)[1]:.0f}" r="8" fill="#c0392b" stroke="#111" stroke-width="1.5"/>' for a,b in ((24.78,85.0),(20.85,86.33),(17.12,82.25)))
 +f'<path d="M{xy(24.78,85.0)[0]:.0f} {xy(24.78,85.0)[1]:.0f} L{xy(20.85,86.33)[0]:.0f} {xy(20.85,86.33)[1]:.0f} L{xy(17.12,82.25)[0]:.0f} {xy(17.12,82.25)[1]:.0f}" stroke="#5a4a6a" stroke-width="6" stroke-dasharray="10 6" fill="none"/></g>'
 +T(160,14,'ŚIRO GAYĀ · HEAD',12,'#7a1d12','start')+T(175,66,'NĀBHI GAYĀ · NAVEL',12,'#7a1d12','start')+T(120,118,'PĀDA GAYĀ · FEET',12,'#7a1d12','start'))+'<table class="ct"><tr><th>Gayā</th><th>Place</th><th>Part of Gayāsura</th><th>Śakti Pīṭha</th></tr>'
 +'<tr><td><b>Śiro Gayā</b></td><td>Gayā, Bihar</td><td>Head</td><td>No. 16, Māṅgalyagaurī</td></tr><tr><td><b>Nābhi Gayā</b></td><td>Jājpur, Odisha</td><td>Navel</td><td>No. 11, Girijā (Birajā)</td></tr><tr><td><b>Pāda Gayā</b></td><td>Pīṭhāpuram, Andhra</td><td>Feet</td><td>No. 10, Puruhūtikā</td></tr></table>'
 +talk("All three Gayās have a Śakti Pīṭha?","All three! Gayāsura's body and Satī's body cross at the same three places.")))
pages.append(page('kukkuta','KUKKUṬEŚVARA','The rooster’s temple',fig(560,180,'A temple complex entered through a gateway, a large stepped tank in front, a huge reclining statue of Gayasura beside it, and the lingam shrine beyond',
 '<rect width="560" height="180" fill="#fdf1e8"/><rect x="40" y="90" width="260" height="70" fill="#4aa3df" stroke="#111" stroke-width="2"/>'+''.join(f'<rect x="{40+k*26}" y="80" width="26" height="10" fill="#e2cfa8" stroke="#111" stroke-width="1"/>' for k in range(10))+T(170,130,'PĀDA GAYĀ SAROVAR',11,'#fff')
 +GAYASURA(330,160,160)+TEMPLE(450,80,1.4,'#dfe8f5')+'<path d="M440 74 v-10 a10 10 0 0 1 20 0 v10z" fill="#3a3a3a" stroke="#111"/>')+facts([
 ('Lord','Śiva as <b>Kukkuṭeśvara</b>, a self-arisen (svayambhū) liṅga'),('Faces','The temple faces <b>north</b>'),
 ('The tank','<b>Pāda Gayā Sarovar</b> just inside the gate, with the footprints of Gayāsura and of Viṣṇu; a bath here is held equal to bathing in the Gaṅgā'),
 ('The statue','A huge figure of <b>Gayāsura</b> lying down, with the Trimūrti, tells the story by the tank'),
 ('Rites for the dead','<b>Piṇḍa-pradāna</b> here is held as meritorious as at Vārāṇasī')])))
pages.append(page('datta','ŚRĪPĀDA ŚRĪVALLABHA','A Datta saint’s birthplace',fig(560,140,'A young saffron-robed saint seated in meditation, a cow and a dog beside him, a small temple behind',
 '<rect width="560" height="140" fill="#fff4cd"/>'+TEMPLE(420,130,1.5)+person(220,120,'#ff8c1a','#f2c79b',1.1)+'<path d="M200 128 q20 -10 40 0" stroke="#ff8c1a" stroke-width="8" fill="none"/><circle cx="220" cy="64" r="22" fill="#ffd166" opacity=".5"/>'
 +'<g transform="translate(110 130)" stroke="#111" stroke-width="2"><ellipse cy="-14" rx="24" ry="12" fill="#fff"/><circle cx="-24" cy="-18" r="8" fill="#fff"/></g>')+'''<div class="panel reading">
<p><b>The saint.</b> <b>Śrīpāda Śrīvallabha</b>, born at Pīṭhāpuram in the <b>14th century</b>, is honoured by his followers as the first incarnation of <b>Dattātreya</b> in this age, before Narasiṃha Sarasvatī.</p>
<p><b>The shrine.</b> The <b>Śrīpāda Śrīvallabha Anagha Datta Kṣetram</b> in the town draws Datta devotees from Maharashtra, Karnataka and Andhra. Tradition says he too worshipped Puruhūtikā.</p>
<p><b>A Datta thread.</b> Māhur, the eighth pīṭha, is a Datta birthplace too: the hymn’s Goddesses keep meeting the Datta tradition.</p>
</div>'''))
pages.append(page('history','HISTORY','Ancient Piṣṭapura',tl([
 ('c. 350','<b>Samudragupta</b>’s Prayāga pillar names <b>Piṣṭapura</b> and its king Mahendra among those he defeated in the South.'),
 ('4th–5th c.','Vāsiṣṭha and Māṭhara kings rule here; inscriptions place Piṣṭapura in Kaliṅga.'),
 ('7th c.','<b>Pulakeśin II</b> takes the town; it is briefly the first capital of the <b>Eastern Chalukyas</b> before Veṅgī.'),
 ('12th–14th c.','Velanāṭi Choḍas (1186–1207), the <b>Pithapuram Chalukyas</b>, the Konas and the <b>Reḍḍi</b> kings.'),
 ('15th c.','The poet <b>Śrīnātha</b> mentions the town in his Bhīmeśvara Purāṇam.'),
 ('1571–1947','The Pithapuram family: jāgīr in 1571, zamīndārī in 1749, British settlement in 1802; its <b>Mahārājas</b> fund a great Telugu dictionary and the first Telugu typewriter.')])))
pages.append(page('kunti','KUNTĪ MĀDHAVA','Viṣṇu in the town too',facts([
 ('Kuntī Mādhava','The town’s great <b>Viṣṇu</b> temple, by tradition one of the <b>Pañca Mādhava</b> shrines, with Bindu Mādhava of Kāśī and Veṇī Mādhava of Prayāga'),
 ('Legend','Kuntī, mother of the Pāṇḍavas, is said to have worshipped Mādhava here'),
 ('Three in one town','Śiva (Kukkuṭeśvara), Śakti (Puruhūtikā) and Viṣṇu (Kuntī Mādhava), plus a Datta shrine')])
 +talk("Is there any god not worshipped in Pīṭhāpuram?","It would be hard to find one. Even the demon Gayāsura has a statue.")))
pages.append(page('festivals','THROUGH THE YEAR','Her days and the ancestors’ days',facts([
 ('Navarātri','In <b>Āśvayuja</b>, the Goddess’s great festival'),('Mahāśivarātri','Kukkuṭeśvara’s night'),
 ('Mahālaya','The fortnight of the ancestors, when pilgrims offer piṇḍas at Pāda Gayā'),('Kārtika','Lamps and baths in the month of Śiva'),('Datta Jayanti','At the Śrīpāda Śrīvallabha shrine')])
 +'<div class="key">The Goddess, the rooster and the ancestors: <b>Pīṭhāpuram’s three duties</b>.</div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Puruhūta','Much-invoked: Indra'),('Kukkuṭa','Rooster'),('Gayāsura','The pious giant whose body became three Gayās'),('Pāda · Nābhi · Śiras','Feet · navel · head'),
 ('Piṇḍa-pradāna','Offering rice balls to ancestors'),('Mahālaya','The ancestors’ fortnight'),('Svayambhū','Self-arisen'),('Piṣṭapura','The ancient town'),('Pañca Mādhava','Five Viṣṇu shrines named Mādhava')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Goddess.</b> Puruhūtikā, worshipped by Indra, in Kukkuṭeśvara’s temple; Satī’s left hand fell here.</div>
<div><b>The rooster.</b> Śiva crowed at midnight to end Gayāsura’s sacrifice, and stayed at his feet as Kukkuṭeśvara.</div>
<div><b>The three Gayās.</b> Head at Gayā, navel at Jājpur, feet here: and all three are Śakti Pīṭhas.</div>
<div><b>The saint.</b> Śrīpāda Śrīvallabha, Datta’s incarnation, born here in the 14th century.</div>
<div><b>The town.</b> Piṣṭapura of Samudragupta and the Eastern Chalukyas.</div>
</div>'''+talk("One line to remember?","A giant gave his body, a god became a rooster, and a king of gods found his Goddess.")+'<div class="key">The tenth seat of the Mother: <b>Puruhūtikā of Pīṭhāpuram</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple and legends:</b> templepurohit.com, religionworld.in and tirthayatra.org (shrine in the Kukkuṭeśvara complex, north-east corner; Pāda Gayā Sarovar; three Gayās; left hand). templesinindiainfo.com (Gayāsura’s sacrifice, the rooster at midnight, his boon; Indra and Gautama’s curse; the name). pilgrimaide.com (Gayāsura statue; eighteen pīṭhas carved on the walls; four arms). indianmandirs.blogspot.com (Indra as seer, Kukkuṭeśvara as guru; the buried image; Āśvayuja Navarātri). sanathanadharma.substack.com (north-facing; bath equal to the Gaṅgā). sakalam.org (rear portion of the body). memoriesandsuch.com and hindupad.com (Rājarājeśvarī). The Hans India (Dakṣiṇa Gayā; three-fold importance).</p>
<p><b>Town:</b> Wikipedia, “Pithapuram”: Samudragupta c. 350; Vāsiṣṭha and Māṭhara; Pulakeśin II and the Eastern Chalukyas; Velanāṭi Choḍas; Pithapuram Chalukyas; Reḍḍis; Śrīnātha; the estate (1571, 1749, 1802); the dictionary and typewriter; Kukkuṭeśvara svayambhū; Kuntī Mādhava; Śrīpāda Śrīvallabha (14th c.); piṇḍa-pradāna equal to Vārāṇasī.</p>
<p><b>Sources differ:</b> body part (left hand, back, rear). <b>Not verified:</b> the buried original image; the Pañca Mādhava grouping and Kuntī’s worship (tradition). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('goddess','The Goddess'),('indra','Legend · Indra'),('gaya','Legend · Gayāsura'),('trigaya','The Three Gayās'),('kukkuta','Kukkuṭeśvara'),
 ('datta','Śrīpāda Śrīvallabha'),('history','History'),('kunti','Kuntī Mādhava'),('festivals','Through the Year'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 10 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7.4vw,74px)">PURUHŪTIKĀ</h1>
  <div class="series">PĪṬHĀPURAM · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess of Indra, and the rooster at midnight</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>In a corner of a Śiva temple in the Godāvarī delta sits <b>Puruhūtikā</b>, the Goddess whom Indra, king of the gods, worshipped when he had lost everything.</p>
    <p>Her Lord is a rooster. Long ago, the story says, Śiva crowed at midnight to trick a giant, and the giant’s feet still rest here, beside a tank where pilgrims make offerings to their ancestors.</p>
    <p>This guide tells both stories, maps the three Gayās, and visits the old town of Piṣṭapura.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Puruhūtikā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why do people bring their ancestors here?","Because a giant asked for it. His feet are here, and his last wish was that the dead be freed at his feet.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Puruhutika.html','w').write(head+b+tail())
print('ok',len(pages))
