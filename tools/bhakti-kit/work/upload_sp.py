import re,shutil,os
exec(open('/home/claude/work/upload_all.py').read().split('# --- Devi')[0])
S='shakti/'
TI='bhakti/temples-of-india'
SP=TI+'/18-shakti-peethas'
items=[('ashtadasha-shakti-peetha-stotram','Ashtadasha_Shakti_Peetha'),('shankari','Shankari'),('kamakshi','Kamakshi'),('shrinkhala','Shrinkhala'),('jogulamba','Jogulamba'),('bhramaramba','Bhramaramba'),
 ('mahalakshmi-kolhapur','Mahalakshmi_Kolhapur'),('ekavirika-mahur','Ekavirika_Mahur'),('mahakali-ujjain','Mahakali_Ujjain'),('puruhutika','Puruhutika'),('girija-jajpur','Girija_Jajpur'),('manikyamba-draksharamam','Manikyamba_Draksharamam'),
 ('kamakhya','Kamakhya'),('madhaveshwari-prayaga','Madhaveshwari_Prayaga'),('jwalamukhi','Jvalamukhi'),('mangalyagauri-gaya','Mangalyagauri_Gaya'),('vishalakshi-varanasi','Vishalakshi_Varanasi'),('sharada-kashmir','Sharada_Kashmir'),('51-shakti-peethas','Fifty_One_Pithas')]
for slug,f in items: cp(S+f+'.html',f'{SP}/{slug}')
cp(S+'Saptapuri.html',TI+'/sapta-puri'); cp(S+'Ahobilam.html',TI+'/ahobilam')
CD=TI+'/char-dham'
for slug,f in [('two-circuits','Char_Dham'),('badrinath','Badrinath'),('puri','Puri_Jagannatha'),('dvaraka','Dvaraka'),('yamunotri','Yamunotri'),('gangotri','Gangotri')]: cp(S+f+'.html',f'{CD}/{slug}')
# tiles for SP index
exec(open('/home/claude/work/shakti/common_s.py').read().split('# --- figures ---')[0])
DEVI='<circle cx="50" cy="30" r="12" fill="#f2c79b"/><path d="M36 18 h28 l-4 -12 l-6 6 l-4 -8 l-4 8 l-6 -6z" fill="#ffd60a"/><path d="M28 92 q-4 -42 22 -50 q26 8 22 50z" fill="#c0392b"/>'
LAMP='<path d="M24 80 h52 l-8 10 h-36z" fill="#c9a26b"/><path d="M50 78 q-16 -20 0 -44 q16 24 0 44z" fill="#ff8c1a"/><path d="M50 74 q-7 -10 0 -22 q7 12 0 22z" fill="#ffd60a"/>'
blurb={1:'Laṅkā: the first seat, the Trincomalee claim and the lost Pīṭha.',2:'Kāñcī: the Goddess of the loving eyes and the Śrī Cakra.',3:'Pradyumna: the chained Goddess and the Pandua debate.',
5:'Ālampur: the fierce Mother on the Tuṅgabhadrā and the Navabrahma temples.',6:'Śrīśailam: the bee-Goddess beside Mallikārjuna.',7:'Kolhāpur: Ambābāī, the Kiraṇotsava and the Karavīra legend.',
8:'Māhur: Ekavīrā or Reṇukā, Dattātreya and Paraśurāma.',9:'Ujjain: Mahākālī, Gaḍhkālikā, Harsiddhi and Kālidāsa.',10:'Pīṭhāpuram: Indra’s Goddess and the rooster at midnight.',
11:'Jājpur: Birajā born from Brahmā’s fire, and Nābhi Gayā.',12:'Drākṣārāmam: Dakṣa’s garden and the two-storey liṅga.',13:'Kāmākhyā: the yoni-stone, Ambubācī and the ten Mahāvidyās.',
14:'Prayāga: the empty doli of Alopī Devī at the Saṅgam.',15:'Jvālāmukhī: the Goddess as living flame.',16:'Gayā: Maṅgalā Gaurī above the city of the ancestors.',17:'Vārāṇasī: the wide-eyed Mother by Maṇikarṇikā.',18:'Kashmir: Śāradā, the ruined seat of learning.'}
SL={n:s for n,(s,_) in enumerate(items) if 0<n<=18}
SL={1:'shankari',2:'kamakshi',3:'shrinkhala',5:'jogulamba',6:'bhramaramba',7:'mahalakshmi-kolhapur',8:'ekavirika-mahur',9:'mahakali-ujjain',10:'puruhutika',11:'girija-jajpur',12:'manikyamba-draksharamam',13:'kamakhya',14:'madhaveshwari-prayaga',15:'jwalamukhi',16:'mangalyagauri-gaya',17:'vishalakshi-varanasi',18:'sharada-kashmir'}
tiles=[tile(f'/{SP}/ashtadasha-shakti-peetha-stotram/','#3a1414',LAMP,'Start here · the hymn','The Aṣṭādaśa Śakti Pīṭha Stotram','Śaṅkara’s hymn of eighteen seats, word by word, the story of Satī, and a map of all eighteen.')]
for n,g,_,today,_,_,_,_,sh in P:
    href='/bhakti/temples-of-india/around-mysuru/chamundeshwari/' if n==4 else f'/{SP}/{SL[n]}/'
    p=blurb.get(n,'Mysuru: Cāmuṇḍeśvarī on Cāmuṇḍi hill, slayer of Mahiṣa (in Temples around Mysuru).')
    tiles.append(tile(href,'#fde4e4',DEVI+f'<text x="50" y="76" text-anchor="middle" font-size="20" font-family="Georgia" fill="#fff" stroke="none">{n}</text>',f'Pīṭha {n} of 18 · {sh}',g,p))
tiles.append(tile(f'/{SP}/51-shakti-peethas/','#f3e3c3',LAMP,'Round-up','Beyond the Eighteen: the 51 Pīṭhas','All fifty-one seats of the Pīṭhanirṇaya, region by region, with body part, Goddess and Bhairava.'))
index(SP,'The 18 Śakti Pīṭhas','The 18 Mahā Śakti Pīṭhas of the Aṣṭādaśa hymn: an illustrated reference guide to each seat of the Goddess, from Laṅkā to Kashmir, plus a round-up of all 51.','/bhakti/temples-of-india/','Temples of India','#3a1414','#ffd27a','#fdf3f3','/bhakti/devi/devi-banner.jpg',
 'Where the parts of Satī’s body fell, the Goddess stays. Śaṅkara’s hymn names eighteen great seats; here is a full illustrated guide to each, in the hymn’s order, and a round-up of the fifty-one.',tiles)
# char dham index
TMP='<path d="M20 90 h60 l-4 -12 h-52z" fill="#c9a26b"/><path d="M30 78 v-24 h40 v24z" fill="#e8c27a"/><path d="M34 54 L50 18 L66 54Z" fill="#d9782f"/>'
CDt=[tile(f'/{CD}/two-circuits/','#0b2a4a','<circle cx="50" cy="50" r="30" fill="none" stroke="#ffd23f" stroke-width="4" stroke-dasharray="6 5"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#ffd23f"/>' for x,y in ((50,20),(80,50),(50,80),(20,50))),'Start here · overview','Char Dham: the two circuits','The four abodes at the four corners of India, the Himalayan four, the yugas and Śaṅkara’s maṭhas.'),
 tile(f'/{CD}/badrinath/','#dcecff',TMP,'North · in both circuits','Badrīnāth','Nara-Nārāyaṇa, the badrī tree, Śaṅkara and the Nambūdiri priest.'),
 tile(f'/{CD}/puri/','#dcecff',TMP,'East · Kali Yuga','Purī Jagannātha','The wooden Lord, Ratha Yātrā, Navakalevara and the great kitchen.'),
 tile('/bhakti/temples-of-india/12-jyotirlingas/rameswaram/','#0b2a4a',TMP,'South · in the Jyotirliṅga series','Rāmeśvaram','Rāma’s liṅga by the sea: the full guide in the 12 Jyotirliṅgas.'),
 tile(f'/{CD}/dvaraka/','#dcecff',TMP,'West · Dvāpara Yuga','Dvārakā','Kṛṣṇa’s city on the sea, the Jagat Mandir and its flag.'),
 tile(f'/{CD}/yamunotri/','#fde4e4',TMP,'Himalaya · first','Yamunotrī','The Sun’s daughter, Death’s sister, and the boiling spring.'),
 tile(f'/{CD}/gangotri/','#fde4e4',TMP,'Himalaya · second','Gaṅgotrī','Bhagīratha’s penance and Gaṅgā caught in Śiva’s hair.'),
 tile('/bhakti/temples-of-india/12-jyotirlingas/kedarnath/','#0b2a4a',TMP,'Himalaya · third · Jyotirliṅga','Kedārnāth','Śiva in the snows: the full guide in the 12 Jyotirliṅgas.')]
index(CD,'Char Dham','Char Dham: the all-India four abodes (Badrīnāth, Purī, Rāmeśvaram, Dvārakā) and the Himalayan Chota Char Dham (Yamunotrī, Gaṅgotrī, Kedārnāth, Badrīnāth), in illustrated reference guides.','/bhakti/temples-of-india/','Temples of India','#0b2a4a','#ffd23f','#eef3fa','/bhakti/temples-of-india/temples-banner.jpg',
 'Two circuits of four: the great circle around India, and the four shrines at the sources of the Gaṅgā. Badrīnāth belongs to both.',CDt)
# temples-of-india tiles
p=f'{R}/{TI}/index.html'; s=open(p).read()
new=[tile(f'/{SP}/','#3a1414',LAMP,'20 articles · hymn + 18 + round-up','The 18 Śakti Pīṭhas','Laṅkā to Kashmir: where Satī’s body fell, the eighteen great seats of the Goddess, and all fifty-one.','Open series ↗'),
 tile(f'/{CD}/','#0b2a4a','<circle cx="50" cy="50" r="30" fill="none" stroke="#ffd23f" stroke-width="4" stroke-dasharray="6 5"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#ffd23f"/>' for x,y in ((50,20),(80,50),(50,80),(20,50))),'6 articles · overview + 5 guides','Char Dham','The four abodes of India and the four Himalayan shrines: Badrīnāth, Purī, Dvārakā, Yamunotrī, Gaṅgotrī.','Open series ↗'),
 tile(f'/{TI}/sapta-puri/','#0b2a4a',''.join(f'<circle cx="{20+i*10}" cy="{50+(i%2)*14}" r="6" fill="#ffd23f"/>' for i in range(7)),'Guide','The Saptapurī','The seven cities of liberation: Ayodhyā, Mathurā, Haridvāra, Kāśī, Kāñcī, Ujjain and Dvārakā.'),
 tile(f'/{TI}/ahobilam/','#dcecff','<circle cx="50" cy="44" r="22" fill="#e08a2a"/><circle cx="50" cy="48" r="14" fill="#ffb84d"/><path d="M30 92 q-2 -30 20 -34 q22 4 20 34z" fill="#ffd60a"/>','Guide · Viṣṇu','Ahobilam','The nine Narasiṃhas of the Nallamala hills, Cheñcu Lakṣmī and the Ugra Stambha.')]
s=s.replace('\n  </ol>',''.join(new)+'\n  </ol>',1)
open(p,'w').write(s)
p=f'{R}/bhakti/index.html'; s=open(p).read()
s=s.replace('3 series · 31 articles','5 series · 58 articles').replace("Illustrated reference guides to India's great temples, the twelve jyotirliṅgas, the Triraṅga and the temples around Mysuru.","Illustrated reference guides to India's great temples: the 12 jyotirliṅgas, the 18 Śakti Pīṭhas, the Char Dham, the Triraṅga, the Saptapurī and more.")
open(p,'w').write(s)
print('done')
