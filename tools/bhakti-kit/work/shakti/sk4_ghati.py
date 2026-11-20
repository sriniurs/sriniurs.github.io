exec(open('/home/claude/work/shakti/sk_common.py').read())
head=head_navy('Ghāṭi Subrahmaṇya · Subrahmaṇya Ṣaṣṭhī 4 · srini.presents',
 'Ghāṭi Subrahmaṇya near Doḍḍaballāpura, Bengaluru: Subrahmaṇya as a seven-hooded serpent facing east and Lakṣmī Narasiṃha facing west, seen together in a mirror; the penance in serpent form, Narasiṃha’s protection from Garuḍa, the demon Ghaṭikāsura, the Ghorpaḍe rulers of Sandūr, thousands of nāga stones, and the Puṣya Ṣaṣṭhī chariot and cattle fair. An illustrated reference guide.')
NARA=lambda x,y,s=1:(f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-24 60 q-2 -64 24 -72 q26 8 24 72z" fill="#e0a800"/>'
 '<circle cy="-28" r="16" fill="#e8a04a"/><path d="M-16 -36 q-10 -14 -2 -22 M16 -36 q10 -14 2 -22 M-18 -22 q-8 10 -2 18 M18 -22 q8 10 2 18" stroke="#b8702a" stroke-width="5" fill="none"/>'
 '<circle cx="-6" cy="-30" r="2.5" fill="#111"/><circle cx="6" cy="-30" r="2.5" fill="#111"/><path d="M-6 -20 q6 6 12 0" fill="#c0392b"/><path d="M-14 -44 h28 l-4 -12 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/>'
 '<path d="M-20 0 l-18 -16 M20 0 l18 -16" stroke="#e8a04a" stroke-width="6"/></g>')
def MIRROR(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="3"><rect x="-40" y="-60" width="80" height="100" rx="8" fill="#d8ecf8"/>'
 '<path d="M-26 -40 l20 -14 M-26 -24 l36 -26" stroke="#fff" stroke-width="4"/></g>')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A seven-hooded cobra deity on one side and a lion-faced Narasimha on the other, with a mirror between them reflecting the lion face">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+HILL(190,268,420,120,'#2a5a3a')+NAGA(110,232,1.25)+NARA(280,186,1.15)+MIRROR(196,150,.6)+'</svg>')
cov=cover('PART 4 OF 4','GHĀṬI SUBRAHMAṆYA',12,'Two gods in one stone, near Bengaluru',art)
fw=foreword('Om Śrī Subrahmaṇyāya Namaḥ,',[
 'An hour north of Bengaluru, in the dry hills of Doḍḍaballāpura, stands a temple with one of the strangest images in Karnataka. Facing east is <b>Subrahmaṇya</b>, as a seven-hooded cobra. Facing west, on the back, is <b>Lakṣmī Narasiṃha</b>. You see the cobra directly, and Narasiṃha in a mirror.',
 'The story is the same theme as Kukke, told another way: the son of Śiva took the form of a serpent, and Viṣṇu himself, as Narasiṃha, guarded him from Garuḍa.',
 'This last part visits Ghāṭi, its legends, its forest of nāga stones and its chariot festival a month after Subrahmaṇya Ṣaṣṭhī.'],
 'Śiva’s son and Viṣṇu in one stone?','Back to back, protecting each other. Ghāṭi settles every Śaiva–Vaiṣṇava quarrel without a word.',
 series_note(prev=('kukke','Kukke Subrahmaṇya')))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Where','Ghāṭi Subrahmaṇya village near Tūbagere, <b>Doḍḍaballāpura</b> taluk, about 60 km north of Bengaluru'),
 ('God','<b>Subrahmaṇya</b> as a <b>seven-hooded cobra</b>, facing east'),
 ('With him','<b>Lakṣmī Narasiṃha</b>, facing west, seen in a mirror'),
 ('Image','Held to be <b>svayambhū</b>, self-manifested, from the earth; tradition says one stone'),
 ('Age','A recorded history of more than <b>600 years</b>'),
 ('Builders','First developed by the <b>Ghorpaḍe</b> rulers of <b>Sandūr</b>'),
 ('Known for','Vows for children, thousands of <b>nāga stones</b>; worship for Ketu'),
 ('Festival','<b>Brahmarathotsava</b> on <b>Puṣya śuddha Ṣaṣṭhī</b>, with a famous cattle fair')])
 +talk("Why a mirror?","Because the two gods face opposite ways. The mirror lets you see both at once without walking round.")))
pages.append(page('names','THE NAME','Pot, hill or demon?',facts([
 ('Ghaṭa sarpa','A popular explanation: the cobra’s spread hood looks like a pot (<i>ghaṭa</i>); the god lived here as a “pot-hooded serpent”'),
 ('Ghāṭ','Another: “ghāṭ”, the hill country where the temple stands'),
 ('Ghaṭikāsura','A third: the demon Ghaṭikāsura, said to have been killed here'),
 ('Full name','Śrī Ghāṭi Subrahmaṇya Svāmi Kṣetra'),
 ('Also','Counted among seven <b>svayaṃvyakta</b> (self-revealed) shrines of Subrahmaṇya')])
 +talk("Which one is right?","Traditions differ. All three tell you something about the place: a serpent, a hill and a victory.")))
pages.append(story('penance','THE SERPENT’S PENANCE','Why the god became a cobra',560,180,'A cobra coiled in deep meditation inside a cave in the hills, rays of light around it',
 '<rect width="560" height="180" fill="#eaf1fb"/>'+HILL(280,180,520,160,'#7a6a4a')+'<path d="M200 180 q0 -90 80 -90 q80 0 80 90z" fill="#2a2a2a" stroke="#111" stroke-width="2"/>'
 +''.join(f'<path d="M280 120 L{280+70*__import__("math").cos(a/6*3.14+3.14):.0f} {120+70*__import__("math").sin(a/6*3.14+3.14):.0f}" stroke="#ffd60a" stroke-width="2"/>' for a in range(1,6))+NAGA(280,176,.7),
 [('Penance.','Tradition says Subrahmaṇya came to these hills and did penance in the form of a serpent.'),
  ('Why?','Tellings differ. In one, it was before his war with Tāraka. In another, it was to atone after the killing in that war.'),
  ('Ghaṭikāsura.','A local story adds a demon, Ghaṭikāsura, whom the god destroyed here.'),
  ('The serpent clan.','While he was here as a serpent, he learnt that the nāgas around him lived in fear of Garuḍa.'),
  ('Next.','He turned to Viṣṇu for help. That is the next page.')]))
pages.append(story('narasimha','NARASIṂHA GUARDS THE NĀGAS','Viṣṇu stands behind',560,180,'A lion-faced Narasimha standing behind a seven-hooded cobra, holding up a hand to stop a great eagle',
 '<rect width="560" height="180" fill="#fdf1e8"/>'+NARA(300,110,.95)+NAGA(220,176,.75)
 +'<g transform="translate(470 60)" stroke="#111" stroke-width="2"><path d="M-60 0 q30 -30 60 0 q30 -30 60 0 q-30 14 -60 10 q-30 4 -60 -10z" fill="#e0701a"/><circle cx="-4" cy="4" r="10" fill="#e8b04a"/><path d="M-12 6 l-10 4 l10 4z" fill="#e0a800"/></g>'
 +'<path d="M330 90 l40 -20" stroke="#e8a04a" stroke-width="7"/>',
 [('A request.','Subrahmaṇya asked Viṣṇu to keep his mount <b>Garuḍa</b> from harming the serpents.'),
  ('Lakṣmī Narasiṃha.','Viṣṇu came with Lakṣmī as <b>Lakṣmī Narasiṃha</b> and stood guard over him.'),
  ('Protection.','Garuḍa could not touch the serpents here; Narasiṃha gave them <b>abhaya</b>, freedom from fear.'),
  ('Two in one.','Sages, one telling names Mārkaṇḍeya, prayed that both forms stay here together. So the image shows the cobra facing east and Narasiṃha facing west.'),
  ('Same theme.','At Kukke the son protects the serpent from Garuḍa; at Ghāṭi Viṣṇu himself holds his own eagle back.')],
 f'<div class="key">Compare: <a href="{SKS}kukke/">Kukke Subrahmaṇya</a>, where Vāsuki hides from Garuḍa</div>'))
pages.append(page('image','THE IMAGE AND THE MIRROR','How you see both gods',fig(560,190,'A plan of the sanctum: one stone with a cobra on the east face and Narasimha on the west face, and a large mirror placed so the devotee in front sees both',
 '<rect width="560" height="190" fill="#1a2a3a"/><rect x="170" y="40" width="220" height="130" fill="#3a2a1a" stroke="#111" stroke-width="2"/>'
 +'<rect x="270" y="70" width="20" height="80" fill="#6a6a6a" stroke="#111" stroke-width="2"/>'+NAGA(235,150,.5)+NARA(330,110,.45)+MIRROR(470,120,.6)
 +'<path d="M340 90 L460 100 M460 130 L120 150" stroke="#ffd60a" stroke-width="2" stroke-dasharray="6 4"/><g transform="translate(90 170)" stroke="#111" stroke-width="2"><path d="M-10 0 q0 -24 10 -26 q10 2 10 26z" fill="#c0392b"/><circle cy="-32" r="7" fill="#f2c79b"/></g>'
 +'<text x="236" y="32" font-family="Georgia" font-size="13" fill="#fff">east face</text><text x="300" y="186" font-family="Georgia" font-size="13" fill="#fff">west face</text>')+facts([
 ('East face','Subrahmaṇya as a seven-hooded cobra: the main darśan'),
 ('West face','Lakṣmī Narasiṃha, on the back of the same image'),
 ('The mirror','A large mirror in the sanctum shows Narasiṃha to devotees standing before Subrahmaṇya'),
 ('Svayambhū','Both are held to have risen from the earth, not carved by hands'),
 ('Sources differ','Most say one stone; some describe two images back to back')])))
pages.append(page('naga','THE FOREST OF NĀGA STONES','Vows for children',fig(560,170,'Rows and rows of small stone serpent images around a tree, with a woman tying a cradle to a branch',
 '<rect width="560" height="170" fill="#eef5e8"/><path d="M280 160 v-90" stroke="#7a4a1a" stroke-width="14"/><circle cx="280" cy="50" r="50" fill="#3a8a3a" stroke="#111" stroke-width="2"/>'
 +''.join(f'<g transform="translate({30+i*40} {150+(i%2)*14})" stroke="#111" stroke-width="2"><rect x="-10" y="-36" width="20" height="36" rx="8" fill="#9a9a8a"/><path d="M0 -6 q-6 -8 0 -14 q6 -6 0 -12" fill="none" stroke="#5a5a4a" stroke-width="2.5"/></g>' for i in range(14) if not 5<i<8)
 +'<path d="M310 70 l20 40" stroke="#7a5a2a" stroke-width="2"/><path d="M318 110 h24 l-4 10 h-16z" fill="#e0701a" stroke="#111" stroke-width="2"/>')+facts([
 ('Nāga stones','Thousands of stone serpent images stand near the temple, set up by devotees'),
 ('Harake','A vow (<i>harake</i> in Kannaḍa): couples pray here for children and return to fulfil it'),
 ('Nāga pratiṣṭhā','Installing a nāga stone is a common way of fulfilling a vow'),
 ('Ketu','The temple is also a centre of worship for Ketu, the shadow planet linked with serpents'),
 ('Sarpa doṣa','As at Kukke, devotees come for relief from troubles believed to follow harm to snakes')])))
pages.append(page('history','HISTORY','The Ghorpaḍes of Sandūr',facts([
 ('Recorded history','More than 600 years, by temple records'),
 ('Ghorpaḍe rulers','First developed by the Ghorpaḍes, rulers of the small state of <b>Sandūr</b>, who governed parts of Ballāri'),
 ('Style','A Dravidian-style temple with a gopura'),
 ('Priests','Tradition says one family has served as priests for generations'),
 ('Today','A major pilgrim centre of the Bengaluru North district')])
 +talk("Sandūr is far from Bengaluru, isn't it?","Over 300 km. Kings built for gods wherever their faith took them, not only at home.")))
pages.append(page('festival','THE CHARIOT AND THE CATTLE FAIR','Puṣya Ṣaṣṭhī at Ghāṭi',fig(560,190,'A temple chariot in front of a gopuram, with a crowd, and on the side rows of white bullocks with painted horns',
 '<rect width="560" height="190" fill="#f2c27a"/>'+GOPURAM(90,180,.8)+RATHA(250,180,1)+CROWD(300,186,5,18)
 +''.join(f'<g transform="translate({420+i*44} 170)" stroke="#111" stroke-width="2"><ellipse cx="0" cy="-12" rx="20" ry="12" fill="#f4f0e8"/><circle cx="20" cy="-22" r="7" fill="#f4f0e8"/><path d="M18 -28 l-4 -8 M24 -28 l4 -8" stroke="#c0392b" stroke-width="3"/><path d="M-12 0 v10 M10 0 v10" stroke="#f4f0e8" stroke-width="4"/></g>' for i in range(3)))+facts([
 ('Brahmarathotsava','The great chariot festival on <b>Puṣya śuddha Ṣaṣṭhī</b>, one lunar month after Subrahmaṇya Ṣaṣṭhī'),
 ('Cattle fair','Held around the festival; one of the best known in South India, with farmers from Karnataka, Tamil Nadu, Andhra Pradesh, Kerala and Maharashtra'),
 ('Subrahmaṇya Ṣaṣṭhī','Also kept with special worship'),
 ('Narasiṃha Jayantī','The other great festival, for the god on the west face'),
 ('Kārttika','Kārttika Pūrṇimā draws crowds too')])
 +talk("A cattle fair at a temple?","The old way. The god's festival was the farmers' market; bullocks were bought under his blessing.")))
pages.append(page('compare','KUKKE AND GHĀṬI','Two serpent shrines side by side',facts([
 ('Region','Kukke: rainforest of the west coast. Ghāṭi: dry hills near Bengaluru'),
 ('Form','Kukke: Subrahmaṇya above Vāsuki and Śeṣa. Ghāṭi: Subrahmaṇya himself as a seven-hooded cobra'),
 ('Protector','Kukke: Subrahmaṇya protects Vāsuki from Garuḍa. Ghāṭi: Narasiṃha protects the nāgas'),
 ('Partner','Kukke: Ādi Subrahmaṇya’s anthill. Ghāṭi: Lakṣmī Narasiṃha in the mirror'),
 ('Chariot','Kukke: Mārgaśīrṣa Ṣaṣṭhī. Ghāṭi: Puṣya Ṣaṣṭhī, a month later'),
 ('Shared','Nāga vows, sarpa doṣa, Ṣaṣṭhī, and the god of Karnataka’s serpents')])
 +f'<div class="key">Start the series again: <a href="{SKS}skanda/">Who is Skanda?</a></div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Ghaṭa','Pot'),('Svayambhū','Self-manifested'),('Svayaṃvyakta','Self-revealed'),('Abhaya','Freedom from fear'),('Harake','A vow (Kannaḍa)'),
 ('Nāga pratiṣṭhā','Installing a serpent stone'),('Ketu','Shadow planet'),('Brahmarathotsava','Great chariot festival'),('Puṣya','Lunar month after Mārgaśīrṣa')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Where.</b> Ghāṭi, near Doḍḍaballāpura, about 60 km from Bengaluru.</div>
<div><b>The image.</b> Subrahmaṇya as a seven-hooded cobra facing east; Lakṣmī Narasiṃha facing west, seen in a mirror.</div>
<div><b>The story.</b> The god’s penance as a serpent; Narasiṃha guards the nāgas from Garuḍa.</div>
<div><b>The people.</b> Thousands of nāga stones; vows for children; 600 years, the Ghorpaḍes of Sandūr.</div>
<div><b>The day.</b> Puṣya śuddha Ṣaṣṭhī: chariot and cattle fair.</div>
</div>'''+talk("Is the series over?","These four are done: the god, his day, and his two serpent homes. Śiva's family has more to tell.")
 +f'<div class="key">Part 4: Ghāṭi. The full series: <a href="{SKS}">Subrahmaṇya Ṣaṣṭhī</a> 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Ghati Subramanya” (near Tūbagere, Doḍḍaballāpura; about 60 km from Bengaluru; Bengaluru North district; Subrahmaṇya with seven-headed cobra facing east, Narasiṃha facing west, mirror; svayambhū; Ketu; 600 years; Ghorpaḍes of Sandūr; harake vows and nāga stones; Brahmarathotsava on Puṣya śuddha Ṣaṣṭhī; Narasiṃha Jayantī; December cattle fair). Bangalore Rural district site (penance in snake form). Incredible India (svayaṃvyakta kṣetra; Narasiṃha’s aid against Garuḍa; Ghaṭikāsura; the atonement telling). karnataka.com (temple history). hindutemples-india and murpriya blogs (ghaṭa sarpa; single stone; penance before the war). hindu-blog.com (Mārkaṇḍeya’s prayer).</p>
<p><b>Sources differ</b> on whether the image is one stone or two, the reason for the penance, and the meaning of “Ghāṭi”. <b>Not verified from a primary source:</b> the single priestly family; the Mārkaṇḍeya episode. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','The Name'),('penance','The Serpent’s Penance'),('narasimha','Narasiṃha Guards the Nāgas'),('image','The Image and the Mirror'),('naga','The Forest of Nāga Stones'),
 ('history','History'),('festival','The Chariot and the Cattle Fair'),('compare','Kukke and Ghāṭi'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/SK4_Ghati.html',head,cov,fw,pages,toc)
