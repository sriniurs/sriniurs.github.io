import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
src=open('/home/claude/work/mysuru/uttanahalli.py').read()
exec(src.split("head=head_red(")[0].split("from common_t import *",1)[1])
exec(src[src.find('def tl('):src.find('cover=(')])
head=head_red('The 18 Śakti Pīṭhas · Aṣṭādaśa Śakti Pīṭha Stotram · srini.presents',
 'The 18 great Śakti Pīṭhas: the legend of Satī and Dakṣa, the Aṣṭādaśa Śakti Pīṭha Stotram verse by verse with meanings, a map and table of all 18, the disputed sites, and how the count grew from 4 to 51 to 108. An illustrated reference guide.')
SER='/bhakti/temples-of-india/18-shakti-peethas/'
# --- the 18 ---
P=[ # n, goddess, stotram place, today, state, lat, lon, part, short
 (1,'Śāṅkarī','Laṅkā','Trincomalee (claimed)','Sri Lanka',8.58,81.23,'groin','Laṅkā'),
 (2,'Kāmākṣī','Kāñcīpura','Kanchipuram','Tamil Nadu',12.83,79.70,'navel','Kāñcī'),
 (3,'Śṛṅkhalā','Pradyumna','Pandua, Hooghly (claimed)','West Bengal',23.08,88.28,'stomach','Pradyumna'),
 (4,'Cāmuṇḍā','Krauñcapaṭṭaṇa','Mysuru','Karnataka',12.27,76.67,'hair','Mysuru'),
 (5,'Jogulāmbā','Alampura','Alampur','Telangana',15.88,78.13,'teeth','Alampur'),
 (6,'Bhramarāmbikā','Śrīśaila','Srisailam','Andhra Pradesh',16.07,78.87,'neck','Śrīśailam'),
 (7,'Mahālakṣmī','Kolhāpura','Kolhapur','Maharashtra',16.70,74.24,'eyes','Kolhāpur'),
 (8,'Ekavīrikā','Māhura','Mahur','Maharashtra',19.83,77.92,'hand','Māhur'),
 (9,'Mahākālī','Ujjayinī','Ujjain','Madhya Pradesh',23.18,75.77,'upper lip','Ujjain'),
 (10,'Puruhūtikā','Pīṭhikā','Pithapuram','Andhra Pradesh',17.12,82.25,'back','Pīṭhāpuram'),
 (11,'Girijā','Oḍhyāṇa','Jajpur (Birajā)','Odisha',20.85,86.33,'navel','Jājpur'),
 (12,'Māṇikyā','Dakṣavāṭikā','Draksharamam','Andhra Pradesh',16.79,82.06,'left cheek','Drākṣārāmam'),
 (13,'Kāmarūpī','Harikṣetra','Kāmākhyā, Guwahati','Assam',26.17,91.70,'yoni','Kāmākhyā'),
 (14,'Mādhaveśvarī','Prayāga','Prayagraj','Uttar Pradesh',25.43,81.85,'fingers','Prayāga'),
 (15,'Vaiṣṇavī','Jvālā','Jwalamukhi, Kangra','Himachal Pradesh',31.88,76.32,'tongue','Jvālāmukhī'),
 (16,'Māṅgalyagaurī','Gayā','Gaya','Bihar',24.78,85.00,'breast','Gayā'),
 (17,'Viśālākṣī','Vārāṇasī','Varanasi','Uttar Pradesh',25.32,83.01,'earrings','Vārāṇasī'),
 (18,'Sarasvatī','Kāśmīra','Śāradā (ruins), Neelum valley','Pakistan-administered Kashmir',34.79,74.19,'right hand','Śāradā')]
POLY='21,163 40,174 26,177 46,195 66,190 68,214 75,246 87,281 107,318 120,333 128,325 140,309 146,290 151,274 149,252 173,240 193,221 219,204 224,186 243,185 246,175 242,155 238,136 256,134 280,127 312,109 332,111 324,128 308,153 295,167 286,182 275,165 271,152 258,145 244,132 238,121 208,119 180,121 150,104 139,82 123,65 132,44 121,33 92,34 79,45 88,62 96,68 88,80 80,91 70,97 51,116 40,130 43,141 33,154'
def xy(lat,lon): return 42+(lon-70.4)*11, 193+(20.89-lat)*11
LANKA=' '.join(f'{xy(a,b)[0]:.0f},{xy(a,b)[1]:.0f}' for a,b in ((9.8,80.0),(8.5,81.3),(7,81.8),(6,80.6),(6.4,79.9),(8,79.8)))
GANGA='<path d="M126 83 L136 104 L158 126 L180 143 L208 142 L236 153" fill="none" stroke="#4aa3df" stroke-width="2.5"/>'
def LAND(): return f'<polygon points="{POLY}" fill="#f4e6d0" stroke="#111" stroke-width="2"/><polygon points="{LANKA}" fill="#f4e6d0" stroke="#111" stroke-width="2"/>'+GANGA
def minimap(hi,label):
    g=''
    for n,_,_,_,_,la,lo,_,sh in P:
        x,y=xy(la,lo)
        if n in hi:
            right = x<215 and n not in (5,12,14)
            g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#c0392b" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(10 if right else -10):.0f}',f'{y+4:.0f}',f'{n} {sh}',13,'#111','start' if right else 'end')
        else: g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#bbb" stroke="#111" stroke-width="1.2"/>'
    return f'<svg width="230" height="190" viewBox="0 0 230 190" role="img" aria-label="{label}"><rect width="230" height="190" fill="#fdf1e8"/><g transform="translate(12 -4) scale(0.52)">'+LAND()+g+'</g></svg>'
# --- figures ---
def FLAME(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-34" y="0" width="68" height="18" fill="#c9a26b"/><path d="M-24 0 q-8 -34 10 -52 q2 22 10 24 q2 -30 18 -44 q-6 30 8 40 q8 -10 6 -22 q16 26 -4 54z" fill="#ff8c1a"/><path d="M-10 0 q-2 -16 8 -24 q2 12 8 12 q4 -8 2 -14 q10 14 -2 26z" fill="#ffd60a"/></g>'
def KING(x,y,s=1,c='#7a5a2a',head='#f2c79b'): return f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,c,head,1)+'<path d="M-12 -40 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800" stroke="#111" stroke-width="1.5"/></g>'
def SHIVA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-22 70 q-4 -60 22 -70 q26 10 22 70z" fill="#5b8fe0"/><circle cy="-14" r="13" fill="#5b8fe0"/>'
 '<path d="M-10 -26 q10 -24 20 0" fill="#3a2a1a"/><path d="M4 -34 a6 6 0 1 0 8 4" fill="none" stroke="#fff8c0" stroke-width="2.4"/><path d="M-6 -16 h3 M3 -16 h3"/><path d="M0 -22 v4" stroke="#c0392b"/>'
 '<path d="M-26 70 h52" stroke="#d9a066" stroke-width="5"/><path d="M-18 12 q-16 6 -12 22" fill="none" stroke="#5b8fe0" stroke-width="7"/></g>')
def SATI(x,y,s=1,rot=0): return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke="#111" stroke-width="2"><path d="M-40 0 q40 -14 80 0 q-40 12 -80 0z" fill="#c0392b"/><circle cx="-46" cy="-2" r="9" fill="#f2c79b"/><path d="M-55 -4 q-10 10 -4 24" fill="none" stroke="#2b1a0e" stroke-width="5"/><path d="M-30 4 h50" stroke="#e0a800" stroke-width="3"/></g>'
def CHAKRA(x,y,r=16): return f'<g transform="translate({x} {y})" stroke="#111" stroke-width="2"><circle r="{r}" fill="#ffd60a"/>'+''.join(f'<path d="M0 0 L{r*1.25*__import__("math").cos(k*0.785):.1f} {r*1.25*__import__("math").sin(k*0.785):.1f}" stroke="#e0a800" stroke-width="3"/>' for k in range(8))+f'<circle r="{r*0.35:.0f}" fill="#fff"/></g>'
STAR=''.join(f'<circle cx="{a}" cy="{b}" r="1.6" fill="#fff"/>' for a,b in ((40,20),(120,40),(500,30),(460,60),(300,14),(220,30),(380,22),(80,60)))
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Shiva striding across the night sky carrying Sati, Vishnu’s discus spinning beside them, and glowing points falling onto a map of India and Sri Lanka">'
 '<rect width="380" height="268" fill="#2a0805" rx="8"/>'+STAR.replace('500','340').replace('460','300')
 +f'<g transform="translate(110 70) scale(0.55)">'+LAND()+''.join(f'<circle cx="{xy(p[5],p[6])[0]:.0f}" cy="{xy(p[5],p[6])[1]:.0f}" r="6" fill="#ffd166" stroke="#c0392b" stroke-width="2"/>' for p in P)+'</g>'
 +SHIVA(84,92,.95)+SATI(108,96,.7,-12)+CHAKRA(160,44,14)
 +''.join(f'<path d="M{a} {b} l{c} {d}" stroke="#ffd166" stroke-width="2" stroke-dasharray="3 4"/>' for a,b,c,d in ((130,110,40,60),(120,120,80,90),(150,100,60,30)))+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Śakti Pīṭha','A “seat of the Goddess”: a shrine where, the legend says, a part of <b>Satī’s</b> body fell to earth'),
 ('The legend','Satī gives up her life at her father <b>Dakṣa’s</b> sacrifice; grieving <b>Śiva</b> carries her body; it falls in pieces across the land'),
 ('How many?','<b>4</b>, <b>7</b>, <b>18</b>, <b>51</b>, <b>52</b>, <b>64</b> or <b>108</b>, depending on the text'),
 ('The 18','The <b>Aṣṭādaśa Mahā Śakti Pīṭhas</b>, named in a five-verse hymn traditionally attributed to <b>Ādi Śaṅkara</b>'),
 ('Where','From <b>Laṅkā</b> in the south to <b>Kashmir</b> in the north, <b>Kolhapur</b> in the west to <b>Kāmākhyā</b> in the east'),
 ('Pairs','At each pīṭha the Goddess is joined by Śiva as her guardian, <b>Bhairava</b>'),
 ('Hardest to reach','Laṅkā, Pradyumna and Kashmir, whose shrines were lost or now stand outside India'),
 ('In this series','One guide for each of the 18, then one or two round-ups for the other pīṭhas of the 51 list')])
 +talk("Eighteen temples from one story?","One sorrow, scattered over a whole subcontinent. That's why the land itself is called the Mother's body.")))
pages.append(page('meaning','WHAT IS A ŚAKTI PĪṬHA?','Seat, power and guardian',fig(560,170,'A seated Goddess on a pedestal on the left; on the right, a fierce Bhairava guardian with a trident and dog',
 '<rect width="560" height="170" fill="#fde4e4"/><rect x="90" y="120" width="140" height="22" fill="#e2cfa8" stroke="#111" stroke-width="2"/>'+GENTLE(160,70,.9).replace('#e05a8a','#c0392b')+T(160,162,'ŚAKTI',13,'#7a1d12')
 +'<g transform="translate(400 70)">'+FIERCE(0,0,.85,'#2b2b3a')+'</g><path d="M450 30 v110 M440 34 q10 -16 20 0 M450 18 v16" stroke="#111" stroke-width="3" fill="none"/><path d="M330 140 q10 -16 24 -8 q8 -10 14 2 v12 h-38z" fill="#5a4a3a" stroke="#111" stroke-width="1.5"/>'+T(400,162,'BHAIRAVA',13,'#7a1d12'))+'''<div class="panel reading">
<p><b>The words.</b> <i>Pīṭha</i> means a seat or pedestal, the throne a deity sits on. <i>Śakti</i> means power, and it is also a name of the Goddess herself: the energy without which, Śākta teachers say, even Śiva cannot move.</p>
<p><b>The idea.</b> A Śakti Pīṭha is a place where the Goddess is believed to be present in a special way, because a part of Satī’s body, or one of her ornaments, came to rest there.</p>
<p><b>Two at every seat.</b> Tradition pairs each pīṭha’s Goddess with a form of Śiva called <b>Bhairava</b>, who guards the shrine. Their names differ from place to place; the 51-list names both for every site.</p>
</div>'''))
leg1=fig(560,200,'King Daksha seated by a blazing sacrificial fire with gods around him; Sati, uninvited, standing before him; Shiva absent on a distant mountain',
 '<rect width="560" height="200" fill="#ffe9c4"/>'+FLAME(280,150,1.3)+KING(150,186,1)+T(150,198,'DAKṢA',12,'#7a1d12')
 +''.join(person(x,186,c,'#f2c79b',.7) for x,c in ((60,'#3b6fd0'),(100,'#2a9d6f')))+GENTLE(420,120,.9).replace('#e05a8a','#c0392b')+T(420,196,'SATĪ',12,'#7a1d12')
 +HILL(510,80,90,60,'#cfd8e8')+SHIVA(510,36,.32)+T(510,96,'KAILĀSA',9,'#555'))
pages.append(page('legend1','THE LEGEND · I','Satī at her father’s sacrifice',leg1+'''<div class="steps">
<div><b>A daughter’s choice.</b> <b>Satī</b>, daughter of the prajāpati <b>Dakṣa</b>, married <b>Śiva</b>, the ash-smeared ascetic of the mountains, against her father’s wishes.</div>
<div><b>The insult.</b> Dakṣa held a great sacrifice and invited every god but Śiva. Satī went anyway, hoping to make peace. Before the assembled gods, Dakṣa poured scorn on her husband.</div>
<div><b>Her answer.</b> Unable to bear it, Satī gave up her body. In most tellings she enters the sacrificial fire; in others she burns through yogic power alone.</div>
</div>'''+talk("She went even though she wasn't invited?","She went as a daughter. What she found there was a father who would not honour her husband.")))
pages.append(page('legend2','THE LEGEND · II','Vīrabhadra destroys the sacrifice',fig(560,170,'A huge many-armed fierce warrior bursting into the sacrifice, the fire scattered, a goat-headed Daksha kneeling',
 '<rect width="560" height="170" fill="#2a0805"/>'+STAR+FLAME(150,140,.9)+'<g transform="translate(300 90)">'+FIERCE(0,0,1.2,'#2b2b3a')+'</g>'
 +'<g transform="translate(450 150)" stroke="#111" stroke-width="2"><path d="M-18 0 q-2 -40 18 -46 q20 6 18 46z" fill="#7a5a2a"/><ellipse cy="-58" rx="12" ry="14" fill="#eee"/><path d="M-10 -68 q-12 -10 -4 -20 M10 -68 q12 -10 4 -20" fill="none" stroke-width="3"/></g>'+T(450,164,'DAKṢA, GOAT-HEADED',10,'#ffd166'))+'''<div class="steps">
<div><b>Śiva’s fury.</b> Hearing of Satī’s death, Śiva tore a lock from his matted hair and dashed it down. From it rose <b>Vīrabhadra</b>, a terrible warrior, with the goddess <b>Bhadrakālī</b> and Śiva’s hosts.</div>
<div><b>The sacrifice wrecked.</b> They smashed the altars, scattered the gods, and Vīrabhadra cut off Dakṣa’s head.</div>
<div><b>Peace restored.</b> At the gods’ pleading, Śiva let the sacrifice be completed and brought Dakṣa back to life with the head of a goat.</div>
</div><div class="panel reading small"><p>The older tellings end here. The scattering of Satī’s body, which gives us the pīṭhas, was added later (see “How the Idea Grew”).</p></div>'''))
pages.append(page('legend3','THE LEGEND · III','Śiva’s grief and the falling body',fig(560,190,'Shiva dancing across the sky with Sati’s body on his shoulder, Vishnu’s discus following, pieces falling to the land below',
 '<rect width="560" height="190" fill="#2a0805"/>'+STAR+SHIVA(220,70,.95)+SATI(250,76,.75,-10)+CHAKRA(330,40,18)
 +'<path d="M0 190 Q140 150 280 170 T560 160 V190z" fill="#5a3a2a"/>'+''.join(f'<path d="M{a} {b} q6 30 {c} {d}" stroke="#ffd166" stroke-width="2.4" stroke-dasharray="4 4" fill="none"/><circle cx="{a+c}" cy="{b+d}" r="5" fill="#ffd166"/>' for a,b,c,d in ((280,100,30,64),(300,90,90,72),(250,110,-60,60),(320,70,150,96)))
 +T(330,76,'SUDARŚANA',10,'#ffd166'))+'''<div class="steps">
<div><b>A god undone by grief.</b> Śiva lifted Satī’s body and wandered the worlds with it, dancing in sorrow and rage. The worlds began to shake.</div>
<div><b>Viṣṇu’s discus.</b> To free him and save creation, <b>Viṣṇu</b> sent his discus, <b>Sudarśana</b>, after them. It cut the body piece by piece as Śiva walked.</div>
<div><b>The seats.</b> Wherever a part or an ornament fell, the earth became holy: a pīṭha, where the Goddess stays, and where Śiva stays with her as Bhairava.</div>
</div><div class="panel reading small"><p><b>Tellings differ.</b> In some, Viṣṇu uses arrows; in others the body falls apart in Śiva’s dance with no discus at all. The number of pieces also varies: 51, 52, 108.</p></div>'''))
counts=[('4','The four great pīṭhas of tantra; in the Buddhist <b>Hevajra Tantra</b>: Jālandhara, Oḍḍiyāna, Pūrṇagiri, Kāmarūpa'),
 ('7','The <b>Kālikā Purāṇa</b>, an Assamese text that makes Kāmarūpa the greatest'),
 ('18','The <b>Aṣṭādaśa</b> stotram; the <b>Kulārṇava Tantra</b> also has a list of 18'),
 ('42','The <b>Kubjikā Tantra</b>'),
 ('51','The <b>Pīṭhanirṇaya</b> (Mahāpīṭhanirūpaṇa), with a Goddess and a Bhairava for each; also the Bengali almanacs'),
 ('52','A Bengali tradition, which scholars think grew from variant copies of the 51-list'),
 ('64','Credited to the <b>Brahmāṇḍa Purāṇa</b>'),
 ('108','The <b>Devī Bhāgavata</b> and the <b>Matsya Purāṇa</b>: 108 names of the Goddess and her places')]
pages.append(page('howmany','HOW MANY PĪṬHAS?','Four, eighteen, fifty-one, a hundred and eight','<table class="ct"><tr><th>Count</th><th>Where it comes from</th></tr>'+''.join(f'<tr><td><b style="font-size:20px">{a}</b></td><td>{b}</td></tr>' for a,b in counts)+'</table>'
 +'''<div class="g2"><div class="card bg-yellow"><h4>🔤 Fifty-one letters</h4><p>A popular explanation links the 51 pīṭhas to the 51 letters of the Sanskrit alphabet: the Goddess as sound, spread over the land.</p></div>
<div class="card bg-red"><h4>🗺 Lists don’t agree</h4><p>Different texts give different places, body parts, Goddess names and Bhairavas for the same seat. No single list is “the” list.</p></div></div>'''
 +talk("So which number is right?","Each is right in its own tradition. This series follows the 18, then gathers the rest of the 51.")))
pages.append(page('growth','HOW THE IDEA GREW','What historians say',tl([
 ('Early','The <b>Dakṣa-yajña</b> story is old: Vīrabhadra and the ruined sacrifice appear in the epic and early Purāṇas. Historian <b>D. C. Sircar</b> dates its full form to about the <b>4th century CE</b>.'),
 ('Tantric','Tantric texts, Hindu and Buddhist, speak of <b>four great pīṭhas</b>; the Hevajra Tantra names Jālandhara, Oḍḍiyāna, Pūrṇagiri and Kāmarūpa.'),
 ('Medieval','The <b>falling body</b> joins the story, explaining why each pīṭha is holy. The Kālikā Purāṇa gives seven seats.'),
 ('Later medieval','The <b>Pīṭhanirṇaya</b> sets out 51 pīṭhas, each with a Goddess and a Bhairava; the Devī Bhāgavata lists 108.'),
 ('Hymn','The short <b>Aṣṭādaśa Śakti Pīṭha Stotram</b> picks 18 great seats and becomes the list best known in South India.')])
 +'''<div class="panel reading"><p><b>Sircar’s view.</b> In his study <i>The Śākta Pīṭhas</i>, Sircar argued that the lists grew by imagination and local pride as much as by old memory, which is why they disagree. For devotees, the holiness of a place does not depend on a list.</p>
<p><b>The land as body.</b> Scholars also note what the story does: by spreading one Goddess’s body over the subcontinent, it makes the whole land her body, and every pilgrimage a visit to her.</p></div>'''))
# --- stotram verses ---
V=[ ('v1','VERSE 1 · PĪṬHAS 1–4','FROM LAṄKĀ TO MYSURU',['laṅkāyāṃ śāṅkarī devī','kāmākṣī kāñcikāpure |','pradyumne śṛṅkhalā devī','cāmuṇḍā krauñcapaṭṭaṇe ‖1‖'],(1,2,3,4),
  'Śāṅkarī Devī in Laṅkā, Kāmākṣī in the city of Kāñcī, Śṛṅkhalā Devī in Pradyumna, Cāmuṇḍā in Krauñcapaṭṭaṇa.',
  'The hymn starts at the island’s edge, goes to Kāñcī in Tamil Nadu, jumps to Bengal, and comes back to Mysuru.',
  [('laṅkā','<b>Laṅkā</b>: the island of Sri Lanka'),('śāṅkarī','“she of Śaṅkara”, <b>Śiva’s consort</b>'),('kāmākṣī','she whose <b>eyes</b> (akṣi) are <b>love</b> (kāma)'),('pradyumna','an old place name, usually taken as <b>Pandua</b>, Bengal'),('śṛṅkhalā','“the <b>chain</b>”, she who binds and frees'),('krauñcapaṭṭaṇa','the town of <b>Krauñca</b>: Mysuru')]),
 ('v2','VERSE 2 · PĪṬHAS 5–8','ACROSS THE DECCAN',['alampure jogulāmbā','śrīśaile bhramarāmbikā |','kolhāpure mahālakṣmī','māhuryām ekavīrikā ‖2‖'],(5,6,7,8),
  'Jogulāmbā in Alampura, Bhramarāmbikā on Śrīśaila, Mahālakṣmī in Kolhāpura, Ekavīrikā in Māhura.',
  'Four Goddesses of the Deccan: on the Tuṅgabhadrā, on the Kṛṣṇā’s hill, in southern Maharashtra and in its eastern forests.',
  [('jogulāmbā','“Yoga-mother” (Yogāmbā), the Goddess of <b>Alampur</b>'),('bhramarāmbikā','the Mother of <b>bees</b> (bhramara), consort of Mallikārjuna'),('mahālakṣmī','the <b>great Lakṣmī</b>, Ambābāī of Kolhapur'),('ekavīrikā','the <b>“sole heroine”</b>, linked with Reṇukā of Mahur')]),
 ('v3','VERSE 3 · PĪṬHAS 9–12','UJJAIN AND THE EASTERN COAST',['ujjayinyāṃ mahākālī','pīṭhikāyāṃ puruhūtikā |','oḍhyāṇe girijā devī','māṇikyā dakṣavāṭike ‖3‖'],(9,10,11,12),
  'Mahākālī in Ujjayinī, Puruhūtikā in Pīṭhikā, Girijā Devī in Oḍhyāṇa, Māṇikyā in Dakṣavāṭikā.',
  'From Ujjain in central India to three seats near the Bay of Bengal: two in the Godāvarī delta and one in Odisha.',
  [('mahākālī','the <b>great Kālī</b>, beside Mahākāla'),('pīṭhikā','“the little seat”: <b>Pithapuram</b>'),('puruhūtikā','she who is <b>invoked by many</b>'),('oḍhyāṇa','<b>Odisha</b>: here Jajpur'),('girijā','“born of the mountain”: <b>Pārvatī</b>, worshipped as Birajā'),('dakṣavāṭikā','“Dakṣa’s garden”: <b>Drākṣārāmam</b>')]),
 ('v4','VERSE 4 · PĪṬHAS 13–16','INTO THE NORTH AND EAST',['harikṣetre kāmarūpī','prayāge mādhaveśvarī |','jvālāyāṃ vaiṣṇavī devī','gayā māṅgalyagaurikā ‖4‖'],(13,14,15,16),
  'Kāmarūpī in Harikṣetra, Mādhaveśvarī at Prayāga, Vaiṣṇavī Devī at Jvālā, Māṅgalyagaurī at Gayā.',
  'Assam’s Kāmākhyā, the river-meeting at Prayāga, the eternal flames of Kangra, and Gayā of the ancestors.',
  [('kāmarūpī','she who takes <b>any form she wishes</b>; Kāmarūpa is Assam'),('harikṣetra','“Hari’s field”: here taken as the <b>Kāmākhyā</b> region'),('mādhaveśvarī','queen beside <b>Mādhava</b> (Viṣṇu) at Prayāga'),('jvālā','“flame”: <b>Jwalamukhi</b>'),('vaiṣṇavī','the Goddess as <b>Viṣṇu’s power</b>'),('māṅgalyagaurī','<b>Gaurī of good fortune</b>')]),
 ('v5','VERSE 5 · PĪṬHAS 17–18','KĀŚĪ AND KASHMIR',['vārāṇasyāṃ viśālākṣī','kāśmīre tu sarasvatī |','aṣṭādaśa supīṭhāni','yogināmapi durlabham ‖5‖'],(17,18),
  'Viśālākṣī in Vārāṇasī, and Sarasvatī in Kashmir. These eighteen holy seats are hard to reach even for yogis.',
  'The list ends at Kāśī and in the far north at the old Śāradā temple, and admits the journey is not easy.',
  [('viśālākṣī','she of <b>wide eyes</b>'),('kāśmīra','<b>Kashmir</b>'),('sarasvatī','the Goddess of <b>learning</b>, Śāradā'),('aṣṭādaśa','<b>eighteen</b>'),('supīṭhāni','<b>excellent seats</b>'),('yogināmapi durlabham','<b>rare even for yogis</b>')])]
for vid,title,theme,lines,hi,mean,plain,words in V:
    pages.append(f'''<section class="page" id="{vid}">
  <h2 class="page-title">{title}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{theme}</span></div>
    <div class="iast">{''.join(f'<span class="cl">{l}</span>' for l in lines)}</div>
    <div class="vfig">{minimap(hi,'Map of India and Sri Lanka marking pithas '+', '.join(str(h) for h in hi))}<div class="mean">{mean}</div></div>
    <div class="plain">{plain}</div>
    <table class="ct"><tr><th>Word</th><th>Means</th></tr>{''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in words)}</table>
  </div>
</section>
''')
pages.append(page('phala','THE CLOSING VERSE','What the hymn promises','''<div class="sloka" style="margin-top:4px">
<div class="sloka-head"><span class="theme" style="font-size:22px">PHALAŚRUTI · THE FRUIT</span></div>
<div class="iast"><span class="cl">sāyaṅkāle paṭhennityaṃ</span><span class="cl">sarvaśatruvināśanam |</span><span class="cl">sarvarogaharaṃ divyaṃ</span><span class="cl">sarvasampatkaraṃ śubham ‖6‖</span></div>
<div class="mean">Read it daily at dusk: it destroys all enemies, takes away all illness, is divine, auspicious, and brings every kind of wealth.</div>
<div class="plain">Chant it every evening. Many printed versions end here; some omit this verse.</div>
</div>
<div class="panel reading"><p><b>Who wrote it?</b> Tradition credits <b>Ādi Śaṅkara</b>, and it is chanted in the Śaṅkara maṭhas. Scholars do not list it among the works they accept as surely his (his commentaries and a few teaching texts), and many stotras were attributed to him over the centuries. So: “traditionally attributed”.</p>
<p><b>Why it matters.</b> Whatever its date, this short hymn fixed the 18 seats that most South Indian pilgrims know, and it is how most of them name the Goddess of each place.</p></div>'''
 +talk("A whole pilgrimage in five verses?","Eighteen places, eighteen names. Learn the verses and you carry the map in your head.")))
# big map
bm=''
OFF={5:(-9,5),6:(9,-5),10:(9,-6),12:(-7,9),14:(-9,-5),17:(0,11)}
for n,_,_,_,_,la,lo,_,sh in P:
    x0,y0=xy(la,lo); dx,dy=OFF.get(n,(0,0)); x,y=x0+dx,y0+dy
    if dx: bm+=f'<path d="M{x0:.0f} {y0:.0f} L{x:.0f} {y:.0f}" stroke="#111" stroke-width="1.5"/><circle cx="{x0:.0f}" cy="{y0:.0f}" r="2" fill="#111"/>'
    bm+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#c0392b" stroke="#111" stroke-width="1.5"/>'+T(f'{x:.0f}',f'{y+4:.0f}',str(n),11,'#fff')
key=''.join(T(452,40+i*22,f'{p[0]} {p[8]}',14,'#111','start') for i,p in enumerate(P))
pages.append(page('map','THE 18 ON ONE MAP','From the island to the mountains',fig(560,470,'Simplified map of India and Sri Lanka with the 18 Shakti Pithas numbered in order of the hymn, and a key listing them',
 '<rect width="560" height="470" fill="#fdf1e8"/><g transform="translate(-14 4) scale(1.3)">'+LAND()+bm+'</g><rect x="440" y="14" width="114" height="410" fill="#fff" stroke="#111" stroke-width="2"/>'+key
 +T(436,462,'Outline simplified; not an official boundary.',11,'#555','end'))
 +'<div class="key">Nine of the eighteen lie in the Deccan and the far South: <b>the hymn is a southern map of the Goddess</b>.</div>'))
def rows(a,b): return '<table class="ct"><tr><th>#</th><th>Goddess</th><th>Place today</th><th>Part</th></tr>'+''.join(f'<tr><td><b>{p[0]}</b></td><td><b>{p[1]}</b><br><small>{p[2]}</small></td><td>{p[3]}<br><small>{p[4]}</small></td><td>{p[7]}</td></tr>' for p in P[a:b])+'</table>'
pages.append(page('list1','THE 18 · I','Pīṭhas 1 to 9',rows(0,9)+'<div class="panel reading small"><p><b>Hymn name</b> in small type under each Goddess. <b>Body parts</b> follow the most common South Indian list; other lists differ, sometimes a lot.</p></div>'))
pages.append(page('list2','THE 18 · II','Pīṭhas 10 to 18',rows(9,18)+'<div class="panel reading small"><p>Cāmuṇḍā of Mysuru already has her own guide: <a href="/bhakti/temples-of-india/around-mysuru/chamundeshwari/">Cāmuṇḍeśvarī</a>.</p></div>'))
pages.append(page('pairs','ŚAKTI BESIDE ŚIVA','Where a pīṭha shares a famous Śiva temple',fig(560,120,'A Shiva linga and a Goddess shrine side by side in one temple courtyard',
 '<rect width="560" height="120" fill="#fdf1e8"/>'+TEMPLE(200,110,1.5,'#dfe8f5')+TEMPLE(360,110,1.5)+'<path d="M190 96 v-14 a10 10 0 0 1 20 0 v14z" fill="#3a3a3a" stroke="#111"/>'+GENTLE(360,62,.4).replace('#e05a8a','#c0392b')+T(200,20,'ŚIVA',12,'#1d4f9a')+T(360,20,'ŚAKTI',12,'#7a1d12'))
 +facts([('Śrīśailam','Bhramarāmbikā with <a href="/bhakti/temples-of-india/12-jyotirlingas/mallikarjuna/">Mallikārjuna</a>: both a jyotirliṅga and a Śakti Pīṭha'),
 ('Ujjain','Mahākālī near <a href="/bhakti/temples-of-india/12-jyotirlingas/mahakaleshwar/">Mahākāleśvara</a>, another jyotirliṅga'),
 ('Vārāṇasī','Viśālākṣī close to <a href="/bhakti/temples-of-india/12-jyotirlingas/kashi-vishwanath/">Kāśī Viśvanātha</a>'),
 ('Drākṣārāmam','Māṇikyāmbā in the Bhīmeśvara temple, one of the Pañcārāma shrines'),
 ('Pīṭhāpuram','Puruhūtikā in the Kukkuṭeśvara temple'),
 ('Alampur','Jogulāmbā among the Nava Brahma temples on the Tuṅgabhadrā'),
 ('Kāñcī','Kāmākṣī in the city of Ekāmbareśvara'),
 ('Trincomalee','Śāṅkarī by Koṇeśvaram, Laṅkā’s great Śiva temple')])
 +talk("So I could see a jyotirliṅga and a Śakti Pīṭha in one visit?","At Śrīśailam you get both in one complex. Śiva and Śakti, side by side, as the story says.")))
pages.append(page('disputed','THE HARD CASES','Where the hymn’s place is debated','''<div class="steps">
<div><b>1 · Laṅkā.</b> The Śāṅkarī temple at <b>Trincomalee</b>, beside Koṇeśvaram, is the usual claim. The old complex was destroyed by the Portuguese in <b>1622–24</b>; the present shrine is modern, and some historians call the site historically undetermined.</div>
<div><b>3 · Pradyumna.</b> Usually placed at <b>Pandua</b>, Hooghly, where only an old minaret and mosque stand; local tradition and some writers say they replaced the temple. Others look to <b>Gaṅgāsāgar</b>, or tell that the Goddess was taken to <b>Śṛṅgeri</b>.</div>
<div><b>8 · Ekavīrikā.</b> Most pilgrims treat <b>Reṇukā’s temple at Mahur</b> as the seat; a small <b>Ekavīrā</b> shrine near Mahur is also pointed out.</div>
<div><b>13 · Harikṣetra.</b> The word means “Hari’s field”; the Goddess’s name, <b>Kāmarūpī</b>, is what ties it to Kāmākhyā in Assam.</div>
<div><b>18 · Kashmir.</b> <b>Śāradā Pīṭha</b> stands in ruins across the Line of Control. A new Śāradā temple at <b>Teetwal</b>, Kupwara, with an image from Śṛṅgeri, opened in March 2023.</div>
</div>'''+talk("Five of eighteen are uncertain?","Uncertain on the map, not in devotion. We'll give every claim its due in each guide.")))
pages.append(page('adi','THE FOUR ĀDI PĪṬHAS','A different “first four”',fig(560,130,'Four temple outlines in a row with their names: Kamakhya, Vimala, Tara Tarini and Kalighat',
 '<rect width="560" height="130" fill="#fde4e4"/>'+''.join(TEMPLE(80+i*133,100,1.2)+T(80+i*133,124,n,12,'#7a1d12') for i,n in enumerate(('KĀMĀKHYĀ','VIMALĀ','TĀRĀ TĀRIṆĪ','KĀLĪGHĀṬ'))))
 +facts([('Kāmākhyā','Guwahati, Assam: the <b>yoni</b>; also in the 18'),('Vimalā','Inside the <b>Jagannātha</b> temple, Puri, Odisha: the <b>feet</b>'),('Tārā Tāriṇī','On a hill by the Ṛṣikulyā, near Berhampur, Odisha: the <b>breasts</b>'),('Kālīghāṭ','Kolkata, West Bengal: the <b>toes of the right foot</b>')])
 +'''<div class="panel reading small"><p>Popular lists call these four the <b>Ādi</b> (“first”) Śakti Pīṭhas. The textual basis for this grouping is thin, and it is not the same as the tantric four (Jālandhara, Oḍḍiyāna, Pūrṇagiri, Kāmarūpa). Vimalā, Tārā Tāriṇī and Kālīghāṭ are in the 51-list and will appear in the round-ups.</p></div>'''))
order=[(p[0],p[1],p[8]) for p in P]
pages.append(page('series','THIS SERIES','Eighteen guides, then the rest','<table class="ct"><tr><th>#</th><th>Guide</th><th>#</th><th>Guide</th></tr>'+''.join(f'<tr><td>{order[i][0]}</td><td><b>{order[i][1]}</b> · {order[i][2]}</td><td>{order[i+9][0]}</td><td><b>{order[i+9][1]}</b> · {order[i+9][2]}</td></tr>' for i in range(9))+'</table>'
 +'''<div class="g2"><div class="card bg-red"><h4>➕ Then the 51</h4><p>The other pīṭhas of the 51-list, from Kālīghāṭ to Hiṅglāj, gathered in one or two round-up guides at the end.</p></div>
<div class="card bg-yellow"><h4>✅ Already here</h4><p>No. 4, <a href="/bhakti/temples-of-india/around-mysuru/chamundeshwari/">Cāmuṇḍeśvarī of Mysuru</a>, from our Temples around Mysuru series.</p></div></div>'''))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Śakti','Power; the Goddess as the energy of all that is'),('Pīṭha','Seat or pedestal; a sacred site of the Goddess'),('Satī','Dakṣa’s daughter, Śiva’s first wife; reborn as Pārvatī'),
 ('Dakṣa','A prajāpati, a lord of creatures; Satī’s father'),('Yajña','A Vedic fire sacrifice'),('Vīrabhadra','The warrior Śiva created to destroy Dakṣa’s sacrifice'),
 ('Bhairava','Śiva as fierce guardian; paired with the Goddess at every pīṭha'),('Sudarśana','Viṣṇu’s discus'),('Aṣṭādaśa','Eighteen'),
 ('Stotram','A hymn of praise'),('Phalaśruti','The closing verse that names the fruit of reciting'),('Upapīṭha','A secondary seat of the Goddess')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The meaning.</b> A Śakti Pīṭha is a seat of the Goddess, where a part of Satī’s body is said to have fallen, guarded by Bhairava.</div>
<div><b>The legend.</b> Satī gives her life at Dakṣa’s sacrifice; Vīrabhadra wrecks it; Śiva wanders with her body until Viṣṇu’s discus divides it.</div>
<div><b>The numbers.</b> 4, 7, 18, 51, 52, 64 or 108, depending on the text; the 51-list and the 18-hymn are best known.</div>
<div><b>The 18.</b> From Laṅkā to Kashmir, in five verses traditionally credited to Ādi Śaṅkara; nine lie in the Deccan and the far South.</div>
<div><b>The hard cases.</b> Laṅkā, Pradyumna, Mahur, Harikṣetra and Kashmir are debated or out of reach.</div>
</div>'''+talk("One line to remember?","The Mother's body is the map of India. Each pīṭha is one place you can touch it.")+'<div class="key">Eighteen seats, <b>one Goddess</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>The pīṭhas and the legend:</b> Wikipedia, “Shakta pithas”: the 18-list with places, body parts and pīṭha names; counts of 51, 52, 64 and 108 and the texts named; the Kulārṇava (18), Kubjikā (42) and Kālikā Purāṇa (7); the Dakṣa-yajña, Vīrabhadra and the goat’s head; Viṣṇu’s discus; Bhairava at each pīṭha; the four Ādi pīṭhas (marked “citation needed” there). Wikipedia, “Pandua, Hooghly” (minaret of 1477; the temple claim).</p>
<p><b>History of the idea:</b> D. C. Sircar, <i>The Śākta Pīṭhas</i>, as summarised by mahavidya.ca (“The Sakta Pithas”): Pīṭhanirṇaya and its medieval date; the Dakṣa story by about the 4th century; the falling body as a later addition; the Hevajra Tantra’s four; Sircar on the lists’ variation.</p>
<p><b>The hymn:</b> templesinindiainfo.com and hindupedia.com (P. R. Ramachander’s translation); text checked against several printed versions. <b>Hard cases:</b> Wikipedia, “Koneswaram Temple” (destruction 1622–24); Tribune India, Daily Excelsior and Deccan Herald on the Teetwal Śāradā temple (March 2023); bhaktikalpa.com and tirthayatra.org on Ekavīrā at Mahur.</p>
<p><b>Sources differ:</b> body parts at many seats (e.g. Puruhūtikā: back or left hand; Ekavīrikā: right or left hand); the Mahur shrine; the Prayāga temple (Alopī Devī or Lalitā Devī). <b>Not verified:</b> the Śaṅkara authorship; that the Pandua mosque replaced the temple (tradition and one modern writer); the Śṛṅgeri and Gaṅgāsāgar claims for Pradyumna. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('meaning','What Is a Śakti Pīṭha?'),('legend1','Legend · Satī at the Sacrifice'),('legend2','Legend · Vīrabhadra'),('legend3','Legend · The Falling Body'),('howmany','How Many Pīṭhas?'),('growth','How the Idea Grew'),
 ('v1','Verse 1 · Laṅkā to Mysuru'),('v2','Verse 2 · Across the Deccan'),('v3','Verse 3 · Ujjain and the East Coast'),('v4','Verse 4 · North and East'),('v5','Verse 5 · Kāśī and Kashmir'),('phala','The Closing Verse'),
 ('map','The 18 on One Map'),('list1','The 18 · I'),('list2','The 18 · II'),('pairs','Śakti beside Śiva'),('disputed','The Hard Cases'),('adi','The Four Ādi Pīṭhas'),('series','This Series'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">THE 18 ŚAKTI PĪṬHAS</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,6vw,64px)">AṢṬĀDAŚA ŚAKTI PĪṬHA STOTRAM</h1>
  <div class="series">THE LEGEND · THE HYMN · THE MAP · A REFERENCE GUIDE</div>
  <div class="tag">Where the Mother’s body fell</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Śiva lost his wife Satī. Grieving, he carried her body across the worlds. Where it fell, the story says, the Goddess stayed: in a hill above Mysuru, on a river island at Prayāga, in a flame that burns from a rock in the Himalayan foothills.</p>
    <p>These are the <b>Śakti Pīṭhas</b>. Texts count them differently, but one short hymn, traditionally credited to Ādi Śaṅkara, names <b>eighteen</b>.</p>
    <p>This guide opens a new series: the story, the hymn verse by verse, and the map. A guide for each of the eighteen follows.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is this like the 12 Jyotirliṅgas, but for the Goddess?","Exactly. Twelve lights of Śiva, eighteen seats of Śakti. And three places hold both.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Ashtadasha_Shakti_Peetha.html','w').write(head+b+tail())
print('ok',len(pages))
