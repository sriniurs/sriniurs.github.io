exec(open('/home/claude/work/shakti/hn_common.py').read())
head=head_vis('Who Hanumān Is · Hanumān 1 · srini.presents','Who is Hanumān? Son of the Wind and Añjanā, Rāma’s messenger and greatest devotee: his names (Āñjaneya, Māruti, Bajrangbalī), the Rudra and Vāyu traditions, his forms from Dāsa to Pañcamukha, the mace, the sindūr and the deathless life, Hanumān in the Mahābhārata, Jain and Southeast Asian tellings, Tuesday and Saturday worship and Hanumān Jayantī across India.')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Hanuman with his mace standing before a rising sun, a mountain of herbs beside him">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/>'+STAR+SUN(290,70,24)+MOUNTAIN(80,210,1.2)+HANUMAN(190,170,1.45)+'</svg>')
cov=cover_hn('HANUMĀN · PART 1 OF 6','WHO IS HANUMĀN?',16,'Son of the Wind, servant of Rāma',art)
fw=foreword_dv('Jai Hanumān,',[
 'Walk into almost any village in India and you will find him at the edge of it: a small orange figure with a mace, smeared with sindūr, guarding the road. <b>Hanumān</b> is everywhere. He is the strongest being in the Rāmāyaṇa and also its humblest. He leapt an ocean, carried a mountain and burned a city, and asked for nothing except to serve <b>Rāma</b>.',
 'In Vālmīki’s Rāmāyaṇa he is a minister of the vānara king Sugrīva and the son of the Wind. Later tradition makes him a portion of Śiva, a model brahmacārī, a scholar of grammar, the healer of Lakṣmaṇa and one of the seven who never die. In Karnataka he is also <b>Prāṇadevaru</b>, the life-breath itself.',
 'This first part is the reference page for Hanumān himself: who he is, what he is called, how he is shown and worshipped. The next four tell his story from birth to the end of the war, and the last visits his temples.'],
 'Is he a vānara or a god?','In Vālmīki he is a vānara, a forest people of great powers. Devotion made him a god who still listens.',
 series_note_hn(0))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Who','Vānara hero of the Rāmāyaṇa; minister of Sugrīva; Rāma’s messenger and devotee'),
 ('Parents','Mother <b>Añjanā</b>; father the vānara chief <b>Kesarī</b>; divine father <b>Vāyu</b>, the Wind'),
 ('Other traditions','A portion (aṃśa) of <b>Śiva</b> in the Purāṇas; the first avatāra of <b>Vāyu</b> for the Mādhvas'),
 ('Great deeds','Leap to Laṅkā, finding Sītā, burning Laṅkā, carrying the mountain of herbs'),
 ('Form','Vānara-faced warrior with a mace (gadā), often orange with sindūr'),
 ('Virtues','Strength, wisdom, speech, self-control, humility, total devotion'),
 ('Days','Tuesday and Saturday'),
 ('Hymns','Hanumān Cālīsā, Saṅkaṭmocan Aṣṭak, Bajrang Bāṇ, Āñjaneya Daṇḍakam')])
 +talk("Why does every village have a Hanumān?","He guards. People put him at the boundary so nothing bad gets in.")))
pages.append(page('names','HIS NAMES','Each name tells a story',facts([
 ('Hanumān','“The one with the jaw (hanu)”: his jaw was struck by Indra’s thunderbolt when he leapt at the sun'),
 ('Āñjaneya','Son of Añjanā'),('Māruti','Son of the Marut, the Wind; the usual name in Maharashtra'),
 ('Pavanaputra · Vāyuputra','Son of the Wind'),('Kesarīnandana','Joy of Kesarī, his vānara father'),
 ('Bajrangbalī','From vajra-aṅga: “strong one with limbs like the thunderbolt”'),
 ('Mahāvīra','The great hero'),('Rāmadūta','Rāma’s messenger'),
 ('Saṅkaṭmocan','The one who frees from trouble'),('Prāṇadevaru','“The god who is life-breath”: Karnataka, especially Mādhva homes')])))
pages.append(page('father','WHOSE SON?','Three ways of telling it',facts([
 ('Vālmīki','Añjanā, an apsaras born as a vānara, was the wife of <b>Kesarī</b>; the Wind god <b>Vāyu</b> embraced her and she bore Hanumān. So he is called the son of both'),
 ('Śiva Purāṇa','Hanumān is an aṃśa of <b>Śiva</b>, born to serve Viṣṇu as Rāma; hence “Rudrāvatāra” in many hymns'),
 ('Other Purāṇic tellings','Some say a portion of the divine pudding (pāyasa) from Daśaratha’s sacrifice was carried by a kite to Añjanā'),
 ('Mādhva','Hanumān is the first avatāra of <b>Vāyu</b> (Mukhyaprāṇa); Bhīma is the second, and the teacher Madhva the third')])
 +talk("So which one is true?","Each school tells it its own way. They all agree he was born to serve Rāma.")
 +'<div class="key">The full story: <a href="'+HNS+'birth/">Birth and Boyhood</a></div>'))
pages.append(page('forms','HIS FORMS','How Hanumān is shown',fig(560,150,'Three small figures of Hanuman: kneeling with folded hands, standing with a mace, and flying with a mountain',
 '<rect width="560" height="150" fill="#fff4dc"/>'+HANUMAN(100,92,.8,mace=False,fold=True)+HANUMAN(280,92,.8)+HANUMAN(440,96,.7)+MOUNTAIN(500,34,.8))+facts([
 ('Dāsa Hanumān','The servant: kneeling or standing with folded hands before Rāma; the form in Rāma temples'),
 ('Vīra Hanumān','The hero: striding, mace on the shoulder, tail raised; the guardian at village edges'),
 ('Sañjīvī Hanumān','Flying with the mountain of herbs on one palm'),
 ('Abhaya Hanumān','Right hand raised in “fear not”'),
 ('Yoga Hanumān','Seated in meditation, as at Ghaṭikācalam (Sholingur) and Hampi’s Yantroddhāraka shrine')])))
pages.append(page('panchamukha','PAÑCAMUKHA','The five-faced Hanumān',facts([
 ('East','<b>Hanumān</b>: removes impurity of mind'),
 ('South','<b>Narasiṃha</b>: removes fear'),
 ('West','<b>Garuḍa</b>: removes poison and black magic'),
 ('North','<b>Varāha</b>: grants prosperity'),
 ('Upward','<b>Hayagrīva</b>: grants knowledge'),
 ('Story','A later tradition: Hanumān took five faces to blow out five lamps at once and kill the demon Ahirāvaṇa (Mahirāvaṇa), who had carried Rāma and Lakṣmaṇa to the underworld'),
 ('Where','Pañcamukha shrines at Kumbakonam, Thiruvallur and Mantrālayam’s Pañcamukhi hill, among many')])
 +talk("Five faces? Isn't that a bit much?","Each face is a protection. People pray to the one they need.")))
pages.append(page('symbols','WHAT HE CARRIES','Mace, mountain, sindūr, tail',facts([
 ('Gadā','The mace: strength used in service'),
 ('The mountain','Droṇagiri or the Oṣadhi hill of herbs: healing, and doing more than asked'),
 ('Sindūr','Orange vermilion smeared over his body. A North Indian tale: he saw Sītā wear sindūr for Rāma’s long life, and covered himself in it'),
 ('Oil','Sesame oil poured over the image, especially on Saturdays'),
 ('The tail','Raised high in Vīra forms; the tail that burned Laṅkā'),
 ('Rāma’s name','Often written on his body or on the stones of the bridge; he is never shown far from it'),
 ('Kapidhvaja','His image on Arjuna’s chariot flag at Kurukṣetra')])))
pages.append(page('qualities','THE PERFECT SERVANT','What Vālmīki says of him',facts([
 ('Speech','When Rāma first heard him at Ṛṣyamūka, he told Lakṣmaṇa no one could speak like that without mastering the Ṛg, Yajur and Sāma Vedas and grammar: not one wrong word'),
 ('Buddhi','Wisdom: he judges people and moments well, as when he chooses how to reveal himself to Sītā'),
 ('Bala','Strength: he can grow huge or tiny at will'),
 ('Restraint','Tradition holds him a lifelong brahmacārī'),
 ('Humility','After every great deed he credits Rāma'),
 ('Forgetting','A boyhood curse made him forget his powers until reminded; Jāmbavān reminds him before the leap')])
 +talk("He forgot he was strong?","Until someone reminded him. Most of us need that reminder too.")))
pages.append(page('chiranjivi','THE ONE WHO STAYS','Cirañjīvī: living on',facts([
 ('Rāma’s boon','In the Uttara Kāṇḍa, when Rāma is leaving the world, Hanumān asks to stay as long as Rāma’s story is told; Rāma grants it'),
 ('The seven','A well-known verse names seven cirañjīvīs: Aśvatthāmā, Bali, Vyāsa, Hanumān, Vibhīṣaṇa, Kṛpa and Paraśurāma'),
 ('Where Rāma is told','A common belief: wherever the Rāmāyaṇa is recited, Hanumān is present, so a seat is left empty for him'),
 ('Gandhamādana · Kimpuruṣa','The Purāṇas place him on the Gandhamādana mountain or in Kimpuruṣa-varṣa, chanting Rāma’s name')])
 +'<div class="verse"><p><i>aśvatthāmā balir vyāso hanūmāṃś ca vibhīṣaṇaḥ<br>kṛpaḥ paraśurāmaś ca saptaite cirajīvinaḥ</i></p><p class="small">Aśvatthāmā, Bali, Vyāsa, Hanumān and Vibhīṣaṇa, Kṛpa and Paraśurāma: these seven live on.</p></div>'))
pages.append(page('mahabharata','IN THE MAHĀBHĀRATA','The old vānara on the path',fig(560,140,'A large warrior unable to lift the tail of an old vānara lying across a forest path',
 '<rect width="560" height="140" fill="#e6f2df"/>'+''.join(f'<path d="M{20+i*60} 120 l14 -60 l14 60z" fill="#2a7a3a" stroke="#111"/>' for i in range(9))+'<path d="M150 112 q120 -10 230 4" fill="none" stroke="#e08a2a" stroke-width="8"/>'+HANUMAN(110,90,.5,mace=False)+person(400,128,'#5a3a8a','#c98b5a',.9))+facts([
 ('Bhīma meets him','In the Vana Parva, Bhīma, looking for the Saugandhika flower, finds an old vānara lying across the path. Told to move his tail aside, Bhīma cannot lift it'),
 ('Brothers','The vānara is Hanumān, his elder brother: both are sons of Vāyu. He shows Bhīma a glimpse of the form that crossed the sea'),
 ('The promise','He promises to sit on Arjuna’s flag and roar with Bhīma in battle'),
 ('Kapidhvaja','So Arjuna’s chariot, driven by Kṛṣṇa, flies the Hanumān banner')])
 +talk("Bhīma couldn't lift a tail?","Pride met humility. That was the lesson.")))
pages.append(page('beyond','OTHER HANUMĀNS','Jain, Southeast Asian and folk tellings',facts([
 ('Jain','In Vimalasūri’s Prakrit Paumacariya, Hanumān is a vidyādhara prince of a royal clan whose banner bore a vānara; he marries and finally becomes a Jain ascetic'),
 ('Thailand','Hanuman of the Ramakien is a dashing white vānara hero with wives and children'),
 ('Indonesia · Cambodia','A favourite of shadow-puppet (wayang) and masked dance; in Cambodia’s Reamker he loves the mermaid Suvannamaccha'),
 ('Makaradhvaja','Later tellings give him a son born of a drop of his sweat swallowed by a great fish'),
 ('Ahirāvaṇa','The underworld rescue story, loved in Bengal, Odisha and the north, is from later Rāmāyaṇas, not Vālmīki')])))
pages.append(page('worship','HOW HE IS WORSHIPPED','Days, offerings and vows',facts([
 ('Tuesday (Maṅgalavāra)','His chief day across North India'),
 ('Saturday (Śanivāra)','A folk story: Hanumān freed Śani from Rāvaṇa’s prison, and Śani promised not to trouble Hanumān’s devotees'),
 ('Sindūr and oil','Vermilion mixed with sesame oil is smeared on the image'),
 ('Garlands','Vaḍa-mālā (garlands of urad vaḍas), veṭrilai (betel-leaf) garlands and butter coating in Tamil Nadu'),
 ('Recitation','The Hanumān Cālīsā, the Sundara Kāṇḍa and Rāma nāma'),
 ('Rāma first','Many temples say: worship Rāma and Hanumān is pleased')])
 +talk("Why butter?","It is cooling. Devotees say it soothes him after carrying the mountain.")))
pages.append(page('jayanti','HANUMĀN JAYANTĪ','One birthday, many dates',facts([
 ('North India','<b>Caitra Pūrṇimā</b>, the full moon of March–April'),
 ('Karnataka','<b>Hanumad Vrata</b>: Mārgaśīrṣa Śukla Trayodaśī (November–December)'),
 ('Andhra · Telangana','Vaiśākha Kṛṣṇa Daśamī, ending a 41-day Hanumān dīkṣā begun on Caitra Pūrṇimā'),
 ('Tamil Nadu · Kerala','The new moon of Mārgaḻi (Dhanu), usually with Mūla nakṣatra (December–January)'),
 ('Odisha','<b>Pana Saṅkrānti</b>, the Odia new year in mid-April')])
 +talk("Why so many birthdays?","No one agrees on the day. So everyone celebrates on theirs.")))
pages.append(page('karnataka','HANUMĀN IN KARNATAKA','Añjanādri, Prāṇadevaru and 732 idols',facts([
 ('Añjanādri','The hill near Hampi across the Tuṅgabhadrā is held by tradition to be his birthplace; 575 steps lead to the white temple on top. Other places also claim the birth'),
 ('Kiṣkindhā','The boulder country of Hampi is the vānara kingdom of the Rāmāyaṇa by tradition'),
 ('Yantroddhāraka','At Hampi, Vyāsatīrtha’s Hanumān seated in a hexagonal yantra'),
 ('732 Prāṇadevarus','Tradition credits the 16th-century saint Vyāsatīrtha with installing 732 Hanumān images across the Vijayanagara lands'),
 ('Village guardian','Āñjaneya stands at the edge of many villages and forts')])
 +'<div class="key">Next door: <a href="'+HNS+'temples/">Hanumān’s temples</a></div>'))
pages.append(page('maharashtra','MĀRUTI OF MAHARASHTRA','Samartha Rāmadāsa’s eleven',facts([
 ('Samartha Rāmadāsa','The 17th-century saint, a great Hanumān devotee, founded eleven Māruti temples in the Krishna valley'),
 ('Every village','A Māruti temple at the village gate, and a wrestling ground (ākhāḍā) beside it'),
 ('Wrestlers','Hanumān is the patron of the ākhāḍā; wrestlers salute him before a bout'),
 ('Bhīmarūpī','Rāmadāsa’s Marathi Māruti Stotra begins “bhīmarūpī mahārudrā”')])
 +talk("Wrestlers pray to him?","Who else? He's the strongest one there is.")))
pages.append(page('hymns','HIS HYMNS','What people chant to him',facts([
 ('Hanumān Cālīsā','Forty Awadhi verses attributed to Tulasīdāsa (16th c.): the most recited hymn in North India'),
 ('Hanumān Bāhuk','Tulasīdāsa’s prayer to Hanumān when his arm was in pain'),
 ('Saṅkaṭmocan Aṣṭak','Eight verses: “who doesn’t know you as the remover of troubles?”'),
 ('Bajrang Bāṇ','A fierce hymn; its authorship is disputed'),
 ('Āñjaneya Daṇḍakam','A Telugu prose-hymn, much chanted in Andhra and Telangana'),
 ('Sanskrit ślokas','“manojavaṃ mārutatulyavegam” and “buddhir balaṃ yaśo dhairyam”')])
 +'<div class="key">Verse by verse: <a href="/bhakti/vishnu/hanuman-chalisa/">Hanumān Cālīsā</a> · <a href="/bhakti/vishnu/sankatmochan-ashtak/">Saṅkaṭmocan Aṣṭak</a> · <a href="/bhakti/vishnu/hanuman-slokas/">Sanskrit ślokas</a></div>'))
pages.append(page('meaning','WHAT HANUMĀN TEACHES','Strength in service',facts([
 ('Power with humility','The strongest one in the story calls himself only a servant'),
 ('Remember who you are','He needed Jāmbavān to remind him of his strength'),
 ('Do more than asked','Asked for one herb, he brought the mountain'),
 ('Speak well','Rāma admired his speech before his strength'),
 ('Devotion is a path','Bhakti, not birth or form, made him great')])
 +talk("What should I take from Hanumān?","Be strong, and use it for something bigger than yourself.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Vānara','The vānara people of the Rāmāyaṇa'),('Aṃśa','Portion, part of a god'),('Gadā','Mace'),('Sindūr','Vermilion'),('Cirañjīvī','One who lives on'),('Dhvaja','Banner, flag'),('Brahmacārī','Celibate student'),('Prāṇa','Life-breath'),('Ākhāḍā','Wrestling ground')])))
pages.append(page('end','ON ONE PAGE','Hanumān in six lines','''<div class="steps">
<div><b>Who.</b> Son of Añjanā, Kesarī and the Wind; minister of Sugrīva; Rāma’s messenger.</div>
<div><b>Traditions.</b> A portion of Śiva; for Mādhvas the first avatāra of Vāyu.</div>
<div><b>Forms.</b> Dāsa, Vīra, Sañjīvī, Yoga and the five-faced Pañcamukha.</div>
<div><b>Lives on.</b> A cirañjīvī, present wherever Rāma’s story is told.</div>
<div><b>Worship.</b> Tuesday and Saturday; sindūr, oil, vaḍas, butter; the Cālīsā.</div>
<div><b>Lesson.</b> Strength, wisdom and humility, all for something higher.</div>
</div>'''+talk("One line to remember?","Wherever Rāma's name is said, Hanumān is listening.")+'<div class="key">Next: <a href="'+HNS+'birth/">Birth and Boyhood</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Vālmīki Rāmāyaṇa (Kiṣkindhā Kāṇḍa 3 on Hanumān’s speech; Kiṣkindhā 66 on his birth and jaw; Uttara Kāṇḍa on his boyhood and Rāma’s boon); Mahābhārata, Vana Parva (Bhīma and Hanumān); Śiva Purāṇa, Śatarudra Saṃhitā (Hanumān as Śiva’s aṃśa); Vimalasūri, Paumacariya; Tulasīdāsa, Hanumān Cālīsā and Hanumān Bāhuk; Samartha Rāmadāsa, Māruti Stotra.</p>
<p><b>Festivals:</b> regional Jayantī dates from Drik Panchang and standard almanacs. <b>Karnataka:</b> Añjanādri and Yantroddhāraka from Karnataka Tourism and Hampi guides; the 732 images from Mādhva tradition.</p>
<p><b>Sources differ / unverified:</b> his birthplace (Añjanādri near Hampi, Añjaneri near Nashik, Tirumala’s Añjanādri and Gumla in Jharkhand all claim it); the Śani, sindūr, Pañcamukha and Makaradhvaja stories are later or folk traditions, not Vālmīki; the authorship of the Cālīsā and Bajrang Bāṇ is traditional. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','His Names'),('father','Whose Son?'),('forms','His Forms'),('panchamukha','Pañcamukha'),('symbols','What He Carries'),('qualities','The Perfect Servant'),('chiranjivi','The One Who Stays'),('mahabharata','In the Mahābhārata'),('beyond','Other Hanumāns'),('worship','How He Is Worshipped'),('jayanti','Hanumān Jayantī'),('karnataka','Hanumān in Karnataka'),('maharashtra','Māruti of Maharashtra'),('hymns','His Hymns'),('meaning','What Hanumān Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
exec(open('/home/claude/work/shakti/hn1_x.py').read())
import re as _re
def _x(p):
    m=_re.search(r'id="([^"]+)"',p); k=m.group(1) if m else ''
    if k in EX: i=p.rfind('</section>'); p=p[:i]+'<div class="panel reading">'+''.join(f'<p>{t}</p>' for t in EX[k])+'</div>'+p[i:]
    return p
pages=[_x(p) for p in pages]
build('/home/claude/work/shakti/HN1_Who.html',head,cov,fw,pages,toc)
