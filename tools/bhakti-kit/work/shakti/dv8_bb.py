exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Balarāma and the Buddha · Daśāvatāra 8 · srini.presents','The disputed eighth place of the Daśāvatāra: Balarāma, Kṛṣṇa’s elder brother with the plough, born from a transferred womb, Revatī, the Yamunā dragged by his plough, Balabhadra of Purī and the Indo-Greek coins; and the Buddha as an avatāra in the Purāṇas and Jayadeva, Gayā, the Buddhist view and the debate. Both lists explained, side by side. An illustrated reference guide.')
def BALA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 50 q-4 -60 30 -70 q34 10 30 70z" fill="#3b4fa0"/>'
 '<path d="M-22 -6 l-26 -10 M22 -6 l26 -10" stroke="#f4f0e8" stroke-width="8"/><path d="M-50 -50 v110" stroke="#7a4a1a" stroke-width="6"/><path d="M-50 60 q10 10 22 0" fill="none" stroke="#7a4a1a" stroke-width="6"/><path d="M50 -50 v70" stroke="#7a4a1a" stroke-width="9"/>'
 '<circle cy="-36" r="15" fill="#f4f0e8"/><path d="M-14 -48 q14 -26 28 0" fill="#3a6a3a"/><path d="M-14 -48 h28 l-4 -12 h-20z" fill="#e0a800"/><circle cx="-5" cy="-38" r="2.4" fill="#111"/><circle cx="5" cy="-38" r="2.4" fill="#111"/><path d="M-6 -29 q6 4 12 0" fill="none"/></g>')
def BUDDHA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-46 40 q46 -24 92 0 q-46 16 -92 0z" fill="#e08a2a"/><path d="M-30 30 q-4 -50 30 -60 q34 10 30 60z" fill="#e08a2a"/>'
 '<path d="M-14 24 q14 8 28 0" fill="#f2c79b"/><circle cy="-40" r="15" fill="#f2c79b"/><circle cy="-58" r="7" fill="#3a2a1a"/><path d="M-14 -44 q14 -18 28 0" fill="#3a2a1a"/>'
 '<path d="M-8 -40 q3 2 6 0 M2 -40 q3 2 6 0" fill="none"/><path d="M-4 -32 q4 2 8 0" fill="none"/><path d="M-12 -34 v8 M12 -34 v8" stroke="#f2c79b" stroke-width="3"/></g>')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Balarama with his plough and pestle on the left and the Buddha seated in meditation on the right">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/>'+STAR+'<path d="M190 30 v220" stroke="#ffd60a" stroke-width="3" stroke-dasharray="8 6"/>'+BALA(100,200,1.25)+BUDDHA(285,210,1.25)+'</svg>')
cov=cover_dv('DAŚĀVATĀRA 8 OF 10','BALARĀMA · BUDDHA',11,'The disputed eighth place',art)
fw=foreword_dv('Keśava dhṛta-haladhara-rūpa,',[
 'The lists of the ten avatāras agree on the first seven and on the last. In between they differ. In the South and in Śrī Vaiṣṇava tradition the eighth is <b>Balarāma</b>, Kṛṣṇa’s strong elder brother with the plough, and the ninth Kṛṣṇa. In many North Indian lists and several Purāṇas the eighth is Kṛṣṇa and the ninth is <b>the Buddha</b>. Jayadeva’s Gītagovinda praises both Balarāma and the Buddha, with Kṛṣṇa as the Lord of all ten.',
 'This guide gives both their due. Balarāma: born from a womb moved by divine power, dragging the Yamunā with his plough, standing beside Jagannātha at Purī, and already on coins in the 2nd century BCE. The Buddha: honoured in the Purāṇas and by Jayadeva for his compassion, while Buddhists themselves do not accept him as an avatāra of Viṣṇu.',
 'We set out the views fairly and let the reader see why the lists differ.'],
 'So who is really number eight?','It depends on whose list you hold. Both are honoured, and neither tradition is “wrong” by its own texts.',
 series_note_dv(8))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Place','<b>Eighth</b> (or ninth, for the Buddha) of the ten'),
 ('Balarāma','Kṛṣṇa’s elder brother; plough (hala) and pestle (musala); Dvāpara Yuga'),
 ('The Buddha','Gautama Buddha as counted in many Purāṇas; Kali Yuga'),
 ('Who lists Balarāma','Śrī Vaiṣṇava and Smārta lists of the South; the Gītagovinda'),
 ('Who lists the Buddha','Several Purāṇas (Agni, Garuḍa, Varāha and others) and many North Indian lists; the Gītagovinda'),
 ('Regional','Some lists place Jagannātha or Viṭhobā here'),
 ('Our approach','Both, side by side')])
 +talk("Why not just pick one?","Because millions hold each list. A fair guide shows both.")))
pages.append(page('lists','THE LISTS SIDE BY SIDE','Positions 8 and 9',
 '<table class="ct fact"><tr><td><b>Tradition</b></td><td><b>8th</b></td><td><b>9th</b></td></tr>'
 +''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c in (('Common North Indian list; several Purāṇas','Kṛṣṇa','Buddha'),('Śrī Vaiṣṇava, Smārta, Śaiva Siddhānta (South)','Balarāma','Kṛṣṇa'),('Gauḍīya Vaiṣṇava; Jayadeva','Balarāma','Buddha (Kṛṣṇa as source)'),('Odisha (Jagannātha tradition)','Balarāma','Jagannātha'),('Mahārāṣṭra (Vārkarī)','Kṛṣṇa','Viṭhobā')))+'</table>'
 +talk("So Kṛṣṇa is sometimes missing?","Only where he is seen as the source of all avatāras, above the list.")))
pages.append(page('bala-birth','BALARĀMA’S BIRTH','The moved womb',fig(560,160,'A goddess carrying a glowing embryo from one woman to another',
 '<rect width="560" height="160" fill="#1d1040"/>'+GENTLE(120,100,.8)+GENTLE(440,100,.8)+'<path d="M160 70 q120 -60 240 0" stroke="#ffd60a" stroke-width="3" stroke-dasharray="6 5" fill="none"/><circle cx="280" cy="40" r="12" fill="#fff8c0" stroke="#111"/>')+facts([
 ('The threat','King Kaṃsa was killing every child born to his sister Devakī'),
 ('The rescue','By Viṣṇu’s will, the goddess Yogamāyā moved Devakī’s seventh child into the womb of Rohiṇī, Vasudeva’s other wife, in Gokula'),
 ('Saṅkarṣaṇa','So he is called Saṅkarṣaṇa, “drawn out”'),
 ('Śeṣa','Many texts say he is Ādiśeṣa, the serpent on whom Viṣṇu rests, come down with him'),
 ('Name','Balarāma, “Rāma of strength”, or Balabhadra')])
 +talk("A womb transfer in an ancient story?","Told as divine power. Readers today find it remarkable.")))
pages.append(page('bala-deeds','THE STRONG ONE','Balarāma’s deeds',facts([
 ('Childhood','With Kṛṣṇa he grew up among the cowherds of Vraja; he killed the donkey-demon Dhenuka and the demon Pralamba'),
 ('Mathurā','With Kṛṣṇa he killed Kaṃsa’s wrestlers'),
 ('The Yamunā','When the river would not come to him, he dragged it with his plough; Jayadeva sings of it'),
 ('Revatī','His wife Revatī came from an earlier age and was very tall; he shortened her with a tap of his plough'),
 ('Hastināpura','Angered, he began to drag the whole city towards the Gaṅgā with his plough until the Kauravas begged him to stop')])
 +'<div class="panel reading"><p><i>vahasi vapuṣi viśade vasanaṃ jaladābhaṃ, hala-hati-bhīti-milita-yamunābham; keśava dhṛta-haladhara-rūpa jaya jagadīśa hare</i></p><p class="small">Jayadeva: “On your fair body you wear cloth dark as a rain cloud, dark as the Yamunā that fled in fear of your plough.”</p></div>'))
pages.append(page('bala-war','NEUTRAL AT KURUKṢETRA','The teacher who walked away',facts([
 ('Teacher','He taught the mace to both Duryodhana and Bhīma'),
 ('Neutral','Loving both sides, he would not fight in the Mahābhārata war; he went on pilgrimage along the Sarasvatī'),
 ('The last duel','He returned for the mace fight of Bhīma and Duryodhana, and was angry at Bhīma’s blow below the waist'),
 ('Departure','At the end of the Yādavas, he sat in meditation by the sea at Prabhāsa, and a white serpent left his mouth: Śeṣa returning')])))
pages.append(page('bala-farmer','LORD OF THE PLOUGH','Balarāma and farming',facts([
 ('Haladhara','“Plough-bearer”: the god of farmers and fertile fields'),
 ('Hal Ṣaṣṭhī','In North India, women keep the Hal Ṣaṣṭhī fast for their children’s welfare on his day'),
 ('Wine and strength','He is fond of wine (vāruṇī) and known for his temper and his kindness'),
 ('Ancient coins','Coins of the Indo-Greek king Agathocles, about 180 BCE, show Saṅkarṣaṇa with a plough and Vāsudeva-Kṛṣṇa with a wheel: among the oldest images of Hindu gods'),
 ('Mathurā','Early stone images of Saṅkarṣaṇa come from the Mathurā region')])))
pages.append(page('bala-puri','BALABHADRA OF PURĪ','With Jagannātha and Subhadrā',fig(560,160,'Three wooden deities side by side: a white one, a small yellow one, and a dark one, with chariots',
 '<rect width="560" height="160" fill="#fff4dc"/>'+''.join(f'<g transform="translate({x} 120)" stroke="#111" stroke-width="2"><rect x="-26" y="-60" width="52" height="70" rx="10" fill="{c}"/><circle cx="-10" cy="-36" r="7" fill="#fff"/><circle cx="10" cy="-36" r="7" fill="#fff"/><circle cx="-10" cy="-36" r="3" fill="#111"/><circle cx="10" cy="-36" r="3" fill="#111"/></g>' for x,c in ((180,'#f4f0e8'),(280,'#ffd60a'),(380,'#2a2a3a'))))+facts([
 ('At Purī','Balabhadra stands with his sister Subhadrā and brother Jagannātha'),
 ('Ratha Yātrā','His chariot, Tāladhvaja, leads the procession'),
 ('White','He is white, Jagannātha black, Subhadrā yellow'),
 ('Char Dham','Purī is the eastern Dhām')])
 +'<div class="key">Read: <a href="'+TI+'char-dham/bada-char-dham/puri/">Purī Jagannātha</a></div>'))
pages.append(page('buddha-purana','THE BUDDHA IN THE PURĀṆAS','How the avatāra list grew',fig(560,150,'The Buddha seated under a tree in meditation',
 '<rect width="560" height="150" fill="#eef7e8"/><ellipse cx="280" cy="50" rx="150" ry="42" fill="#2f7a3a" stroke="#111" stroke-width="2"/><rect x="270" y="70" width="20" height="40" fill="#7a4a1a" stroke="#111"/>'+BUDDHA(280,120,.8))+facts([
 ('Bhāgavata 1.3.24','At the start of the Kali age, the Lord will appear as Buddha, son of Añjanā, among the Kīkaṭas (Magadha), to bewilder the enemies of the gods'),
 ('Other Purāṇas','The Agni, Garuḍa, Varāha and other Purāṇas list the Buddha as an avatāra'),
 ('When','Scholars date the Buddha’s inclusion to roughly the Gupta age and after, as the list took shape'),
 ('Two portraits','Some Purāṇas show him as misleading the wicked; Jayadeva shows him as compassion itself'),
 ('Debate','Some Hindu writers say the Purāṇic Buddha is a different person from Gautama')])))
pages.append(page('jayadeva-buddha','JAYADEVA’S BUDDHA','The compassionate one',facts([
 ('Verse','Jayadeva praises the Buddha for condemning the Vedic rule of animal sacrifice, “with a heart full of compassion”'),
 ('Ahiṃsā','In this reading the Buddha is honoured for non-violence and kindness to animals'),
 ('Odisha','Jayadeva’s list (with Balarāma and Buddha) shaped worship and dance at Purī')])
 +'<div class="panel reading"><p><i>nindasi yajña-vidher ahaha śruti-jātaṃ, sadaya-hṛdaya darśita-paśu-ghātam; keśava dhṛta-buddha-śarīra jaya jagadīśa hare</i></p><p class="small">Jayadeva, Gītagovinda: “Ah, with a compassionate heart you condemned the Vedic rules that showed the killing of animals. Keśava, in the body of the Buddha, victory!”</p></div>'))
pages.append(page('buddhist','THE BUDDHIST VIEW','Not an avatāra of Viṣṇu',facts([
 ('Buddhism','Buddhist traditions see the Buddha as a fully awakened human teacher, not as an avatāra of any god'),
 ('Ambedkar','In 1956 B. R. Ambedkar and his followers took 22 vows on converting to Buddhism; one was not to believe the Buddha is an incarnation of Viṣṇu'),
 ('Respect','Many Hindus honour the Buddha deeply in either case'),
 ('Our view','Both views are reported here; this guide does not decide between them')])
 +talk("So Hindus count him and Buddhists don't?","Some Hindus count him, some lists don't, and Buddhists don't. All three are held sincerely.")))
pages.append(page('gaya','GAYĀ AND BODH GAYĀ','Two holy towns',facts([
 ('Bodh Gayā','Where the Buddha attained enlightenment under the Bodhi tree; the Mahābodhi temple is a UNESCO World Heritage Site'),
 ('Gayā','A few km away: the Viṣṇupada temple with Viṣṇu’s footprint, and the place for śrāddha rites to ancestors'),
 ('Meeting point','The two traditions have lived side by side here for over two thousand years'),
 ('Śakti Pīṭha','Gayā is also one of the eighteen Śakti Pīṭhas')])
 +'<div class="key">Read: <a href="/bhakti/temples-of-india/18-shakti-peethas/mangalyagauri-gaya/">Maṅgalyagaurī, Gayā</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','Their days',facts([
 ('Balarāma Jayantī','Śrāvaṇa Pūrṇimā in many places; Hal Ṣaṣṭhī in the north'),('Ratha Yātrā','Āṣāḍha (Jun–Jul), Purī'),('Buddha Pūrṇimā','Vaiśākha Pūrṇimā (Apr–May): birth, enlightenment and passing of the Buddha')])))
pages.append(page('meaning','WHAT THEY TEACH','Strength and compassion',facts([
 ('Balarāma','Strength in service; the farmer’s plough is sacred'),
 ('Neutrality','Sometimes the brave thing is to refuse a war'),
 ('The Buddha','Compassion for every living being'),
 ('The lists','Traditions can differ and still respect each other')])
 +talk("What should I take from this one?","Be strong like Balarāma, kind like the Buddha. And respect a list that isn't yours.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Hala · Musala','Plough · pestle'),('Saṅkarṣaṇa','“Drawn out”: Balarāma'),('Śeṣa','Cosmic serpent'),('Yogamāyā','Viṣṇu’s divine power'),('Ahiṃsā','Non-violence'),('Bodhi','Awakening'),('Kīkaṭa','Old name for Magadha'),('Śrāddha','Rite for ancestors')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The question.</b> Eighth place: Balarāma (South, Jayadeva) or the Buddha (many Purāṇas, North)?</div>
<div><b>Balarāma.</b> The moved womb, the plough, the dragged Yamunā, Balabhadra of Purī.</div>
<div><b>The Buddha.</b> In the Bhāgavata and Jayadeva; compassion against sacrifice.</div>
<div><b>Buddhists.</b> Do not see him as Viṣṇu’s avatāra; Ambedkar’s vow.</div>
<div><b>Lesson.</b> Strength and compassion; respect for other lists.</div>
</div>'''+talk("One line to remember?","Two great figures share one place. That's a feature, not a bug.")+'<div class="key">Next: <a href="'+DVS+'krishna/">Kṛṣṇa</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Lists:</b> Wikipedia, “Dashavatara” (positions 8 and 9 by tradition; Purāṇas with Kṛṣṇa and Buddha; Śrī Vaiṣṇava list); Encyclopaedia Britannica, “Dashavatara”.</p>
<p><b>Balarāma:</b> Bhāgavata Purāṇa 10.2 (womb transfer), 10.15 (Dhenuka), 10.65 (Yamunā), 9.3 (Revatī); Mahābhārata, Śalya Parva (pilgrimage, duel) and Mausala Parva (departure); Jayadeva, Gītagovinda 1; Agathocles coins (Ai-Khanoum hoard), from standard numismatic sources.</p>
<p><b>Buddha:</b> Bhāgavata Purāṇa 1.3.24; Jayadeva, Gītagovinda 1; Ambedkar’s 22 vows (1956); UNESCO, Mahābodhi Temple Complex.</p>
<p><b>Sources differ / unverified:</b> whether Balarāma is Viṣṇu or Śeṣa; dating of the Buddha’s inclusion; the identity of the Purāṇic Buddha with Gautama; regional lists vary. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('lists','The Lists Side by Side'),('bala-birth','Balarāma’s Birth'),('bala-deeds','The Strong One'),('bala-war','Neutral at Kurukṣetra'),('bala-farmer','Lord of the Plough'),('bala-puri','Balabhadra of Purī'),
 ('buddha-purana','The Buddha in the Purāṇas'),('jayadeva-buddha','Jayadeva’s Buddha'),('buddhist','The Buddhist View'),('gaya','Gayā and Bodh Gayā'),('festivals','Through the Year'),('meaning','What They Teach'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV8_Balarama_Buddha.html',head,cov,fw,pages,toc)
