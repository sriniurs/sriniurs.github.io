exec(open('/home/claude/work/up_lib.py').read())
CD='bhakti/temples-of-india/char-dham'
TMP='<path d="M20 90 h60 l-4 -12 h-52z" fill="#c9a26b"/><path d="M30 78 v-24 h40 v24z" fill="#e8c27a"/><path d="M34 54 L50 18 L66 54Z" fill="#d9782f"/>'
RING='<circle cx="50" cy="50" r="30" fill="none" stroke="#ffd23f" stroke-width="4" stroke-dasharray="6 5"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#ffd23f"/>' for x,y in ((50,20),(80,50),(50,80),(20,50)))
SNOW='<path d="M8 86 L34 34 L50 58 L66 26 L92 86Z" fill="#dfe9f6"/><path d="M28 46 l6 -12 l6 10 M60 38 l6 -12 l6 12" fill="#fff"/>'+''.join(f'<circle cx="{x}" cy="90" r="5" fill="#ffd23f"/>' for x in (26,42,58,74))
JY='/bhakti/temples-of-india/12-jyotirlingas/'
bada=[tile(f'/{CD}/bada-char-dham/badrinath/','#dcecff',TMP,'North · Satya Yuga','Badrīnāth','Nara-Nārāyaṇa, the badrī tree, Śaṅkara and the Nambūdiri priest.'),
 tile(f'{JY}rameswaram/','#0b2a4a',TMP,'South · in the Jyotirliṅga series','Rāmeśvaram','Rāma’s liṅga by the sea: the full guide in the 12 Jyotirliṅgas.'),
 tile(f'/{CD}/bada-char-dham/puri/','#dcecff',TMP,'East · Kali Yuga','Purī Jagannātha','The wooden Lord, Ratha Yātrā, Navakalevara and the great kitchen.'),
 tile(f'/{CD}/bada-char-dham/dvaraka/','#dcecff',TMP,'West · Dvāpara Yuga','Dvārakā','Kṛṣṇa’s city on the sea, the Jagat Mandir and its flag.')]
chota=[tile(f'/{CD}/chota-char-dham/yamunotri/','#fde4e4',TMP,'First · Yamunā’s source','Yamunotrī','The Sun’s daughter, Death’s sister, and the boiling spring.'),
 tile(f'/{CD}/chota-char-dham/gangotri/','#fde4e4',TMP,'Second · Gaṅgā’s source','Gaṅgotrī','Bhagīratha’s penance and Gaṅgā caught in Śiva’s hair.'),
 tile(f'{JY}kedarnath/','#0b2a4a',TMP,'Third · in the Jyotirliṅga series','Kedārnāth','Śiva in the snows: the full guide in the 12 Jyotirliṅgas.'),
 tile(f'/{CD}/bada-char-dham/badrinath/','#dcecff',TMP,'Fourth · also a Bada Dhām','Badrīnāth','The yātrā ends where the all-India circuit begins: Viṣṇu at Badrī.')]
B='/bhakti/temples-of-india/temples-banner.jpg'
index(CD+'/bada-char-dham','Bada Char Dham','The Bada (all-India) Char Dham: Badrīnāth in the north, Rāmeśvaram in the south, Purī in the east and Dvārakā in the west, in illustrated reference guides.',f'/{CD}/','Char Dham','#0b2a4a','#ffd23f','#eef3fa',B,
 'The four abodes at the four corners of India, linked by Śaṅkara’s maṭhas: one for each yuga.',bada)
index(CD+'/chota-char-dham','Chota Char Dham','The Chota (Himalayan) Char Dham of Uttarakhand: Yamunotrī, Gaṅgotrī, Kedārnāth and Badrīnāth, in illustrated reference guides.',f'/{CD}/','Char Dham','#0b2a4a','#ffd23f','#eef3fa',B,
 'The four Himalayan shrines of Uttarakhand, at the sources of the Yamunā and the Gaṅgā, visited west to east.',chota)
top=[tile(f'/{CD}/two-circuits/','#0b2a4a',RING,'Start here · overview','Char Dham: the two circuits','The four abodes at the four corners of India, the Himalayan four, the yugas and Śaṅkara’s maṭhas.'),
 tile(f'/{CD}/bada-char-dham/','#0b2a4a',RING,'4 Dhāms · all-India','Bada Char Dham','Badrīnāth, Rāmeśvaram, Purī and Dvārakā: north, south, east and west.','Open ↗'),
 tile(f'/{CD}/chota-char-dham/','#dfe9f6',SNOW,'4 Dhāms · Uttarakhand','Chota Char Dham','Yamunotrī, Gaṅgotrī, Kedārnāth and Badrīnāth in the Himalaya.','Open ↗')]
index(CD,'Char Dham','Char Dham: the all-India four abodes (Badrīnāth, Purī, Rāmeśvaram, Dvārakā) and the Himalayan Chota Char Dham (Yamunotrī, Gaṅgotrī, Kedārnāth, Badrīnāth), in illustrated reference guides.','/bhakti/temples-of-india/','Temples of India','#0b2a4a','#ffd23f','#eef3fa',B,
 'Two circuits of four: the great circle around India (Bada Char Dham), and the four shrines at the sources of the Gaṅgā (Chota Char Dham). Badrīnāth belongs to both.',top)
print('ok')
