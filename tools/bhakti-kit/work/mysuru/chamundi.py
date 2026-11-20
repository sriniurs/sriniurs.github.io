import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
exec(open('/home/claude/work/mysuru/uttanahalli.py').read().split("head=head_red(")[0].split("from common_t import *",1)[1])
exec("def _x():pass")
src=open('/home/claude/work/mysuru/uttanahalli.py').read()
exec(src[src.find('def tl('):src.find('cover=(')])
head=head_red('Cāmuṇḍeśvarī · Cāmuṇḍī Hills · Temples around Mysuru · srini.presents',
 'Cāmuṇḍeśvarī on Cāmuṇḍī Hills: Mysuru’s Nāḍa Devī and the Woḍeyars’ family Goddess. Mahiṣāsura and the name Mysuru, the Krauñca Pīṭha, the thousand steps and the great Nandi, the 1827 gopura, Āṣāḍha Fridays and Dasara. An illustrated reference guide.')
def NANDI(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cy="-30" rx="60" ry="30" fill="#3a3a3a"/><path d="M-50 -50 q-10 -30 10 -36 q20 0 18 30z" fill="#3a3a3a"/><path d="M-44 -82 l-8 -10 M-28 -80 l4 -12" stroke-width="4"/><path d="M-14 -58 q14 -14 28 0" fill="#3a3a3a"/><path d="M-50 -40 q10 6 20 0" fill="none" stroke="#e0a800" stroke-width="4"/><circle cx="-40" cy="-30" r="5" fill="#e0a800"/><rect x="-60" y="-4" width="120" height="6" fill="#8a8a8a"/></g>'
def MAHISHA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-22 70 v-50 h44 v50" fill="#5a3a6a"/><path d="M-30 20 q30 -30 60 0 v-20 q-30 -20 -60 0z" fill="#3a5a3a"/><circle cy="-16" r="16" fill="#3a5a3a"/><path d="M-12 -28 q-18 -20 -6 -30 M12 -28 q18 -20 6 -30" fill="none" stroke-width="5"/><path d="M-8 -18 h4 M4 -18 h4"/><path d="M-10 -6 q10 6 20 0" fill="none"/><path d="M30 0 l20 -50" stroke="#bbb" stroke-width="6"/><path d="M-30 0 q-30 -10 -24 -40 q6 6 10 2" fill="none" stroke="#2e6a2e" stroke-width="5"/></g>'
def LION(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cy="-20" rx="40" ry="18" fill="#e0a800"/><circle cx="-38" cy="-30" r="18" fill="#c98b2a"/><circle cx="-42" cy="-30" r="10" fill="#e0a800"/><path d="M40 -24 q20 -10 14 -26" fill="none" stroke="#e0a800" stroke-width="5"/><rect x="-30" y="-6" width="8" height="12" fill="#e0a800"/><rect x="22" y="-6" width="8" height="12" fill="#e0a800"/></g>'
def DURGA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+LION(0,40,1)+GENTLE(0,-30,.9).replace('#e05a8a','#c0392b')+''.join(f'<path d="M{a} -40 l{b} -16" stroke="#f2c79b" stroke-width="5"/>' for a,b in ((-18,-18),(18,18),(-18,-24),(18,24)))+'</g>'
def GOP(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-34+k*3} {-k*12} h{68-k*6} l-1 -12 h{-(66-k*6)}z" fill="{"#f2e6c8" if k%2 else "#e2cfa8"}"/>' for k in range(7))+''.join(f'<path d="M{-14+j*5} {-84} l2 -10 l2 10z" fill="#e0a800"/>' for j in range(7))+'<rect x="-9" y="-20" width="18" height="20" fill="#c0c0c0"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Chamundi Hill with its seven-tiered gopura on top, the great Nandi halfway up, and the Goddess on her lion slaying the buffalo demon">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/><circle cx="330" cy="46" r="26" fill="#ffd166" opacity=".4"/>'
 +HILL(150,268,300,200)+GOP(150,96,.9)+NANDI(110,200,.35)+''.join(f'<path d="M{100+i*6} {250-i*16} h12" stroke="#e2cfa8" stroke-width="2"/>' for i in range(9))+DURGA(300,180,1.0)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','<b>Cāmuṇḍeśvarī</b>, the Goddess as Durgā, slayer of <b>Mahiṣāsura</b>: an eight-armed image'),
 ('Titles','<b>Nāḍa Devī</b>, Goddess of the land of Karnataka; family Goddess of the <b>Woḍeyars</b>'),
 ('Place','The summit of <b>Cāmuṇḍī Hills</b>, about 1,060 m, beside Mysuru'),
 ('Name of a city','Mahiṣāsura’s land, <b>Mahiṣūru</b>, became <b>Mysuru</b>'),
 ('Śakti Pīṭha','Counted among the 18 great pīṭhas as the <b>Krauñca Pīṭha</b>, where Satī’s <b>hair</b> is said to have fallen'),
 ('Builders','Shrine from the <b>Hoysaḷa</b> era (12th c.); steps in <b>1659</b>; Nandi in <b>1664</b>; gopura by <b>Kṛṣṇarāja Woḍeyar III</b> (1827)'),
 ('On the hill','The <b>Mahābaleśvara</b> temple, older still; the great <b>Nandi</b>; the <b>Mahiṣāsura</b> statue'),
 ('Festivals','<b>Āṣāḍha Fridays</b>, the <b>Vardhanti</b>, <b>Navarātri</b>, and <b>Dasara</b>, when she rides the golden howdah')])
 +talk("The whole city is named after a demon?","After the demon she defeated! Every time you say Mysuru, you're telling her story.")))
mapfig=fig(560,230,'Schematic map of Chamundi Hill: the thousand steps climbing from the city, the Nandi on the way, the temple and Mahishasura statue at the top, the Mahabaleshwara temple nearby, the road, and Uttanahalli at the foot. Not to scale.',
 '<rect width="560" height="230" fill="#eef6e4"/>'+HILL(280,226,400,200)+GOP(270,40,.45)+T(300,20,'CĀMUṆḌEŚVARĪ',10,'#7a1d12','start')+MAHISHA(220,46,.25)+'<g transform="translate(330 40)">'+TEMPLE(0,0,.5,'#e8e8f0')+'</g>'+T(352,52,'MAHĀBALEŚVARA',8,'#555','start')
 +''.join(f'<path d="M{150+i*8} {216-i*12} h8" stroke="#7a5a2a" stroke-width="2"/>' for i in range(15))+T(140,210,'1,000 STEPS',9,'#7a5a2a','end')+NANDI(196,140,.18)+T(160,124,'NANDI',9,'#555','end')
 +'<path d="M420 226 C 400 160, 360 100, 300 50" stroke="#8a7a6a" stroke-width="3" stroke-dasharray="8 5" fill="none"/>'+TEMPLE(500,220,.5)+T(500,196,'UTTANAHAḶḶI',9,'#c0392b')
 +'<rect x="10" y="170" width="90" height="56" fill="#e8e2d0" stroke="#111"/>'+T(55,162,'MYSURU',11,'#555')+T(470,20,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','The hill above Mysuru',mapfig+'''<div class="panel reading">
<p><b>The hill.</b> Cāmuṇḍī Hills rise beside the city to about <b>1,060 m</b>. From the top you can see the palace, Karañji Lake and the spread of Mysuru below.</p>
<p><b>The ways up.</b> A stone stairway of about <b>1,000 steps</b>, built in 1659, climbs from the city, passing the great Nandi; a road winds up the other way.</p>
<p><b>A forest too.</b> The hill is a reserve forest: some 193 kinds of birds, 150 butterflies, and 442 flowering plants have been recorded on it.</p>
</div>'''))
pages.append(page('names','HER NAMES','From Cāmuṇḍā to Nāḍa Devī',facts([
 ('Cāmuṇḍā','The Goddess who slew the demons <b>Caṇḍa</b> and <b>Muṇḍa</b> in the Devī Māhātmya'),
 ('Cāmuṇḍeśvarī','“Queen Cāmuṇḍā”, as she is worshipped here'),
 ('Mahiṣāsura Mardinī','“Crusher of the buffalo demon”: the deed of this hill'),
 ('Nāḍa Devī','Goddess of the land (<i>nāḍu</i>): the state Goddess of Karnataka'),
 ('Krauñca Pīṭha','The name of this seat among the Śakti Pīṭhas, from <b>Krauñcapurī</b>, an old name of the region'),
 ('Mahābalādri','An older name of the hill, after its Śiva temple of Mahābaleśvara'),
 ('Cāmuṇḍī Beṭṭa','The hill as Mysuru calls it')])
 +talk("So she's Cāmuṇḍā AND Mahiṣāsura Mardinī?","One Goddess, many deeds. Each name is a victory she won.")))
deity=fig(560,210,'The eight-armed Goddess seated in a yogic posture in the sanctum, crowned, holding weapons, with the small golden festival image in front',
 '<rect width="560" height="210" fill="#fde4e4"/><rect x="150" y="16" width="260" height="184" fill="#fff4cd" stroke="#111" stroke-width="2"/>'
 +'<g transform="translate(280 120) scale(1.3)" stroke="#111" stroke-width="2"><path d="M-30 50 q-4 -50 30 -60 q34 10 30 60z" fill="#c0392b"/><path d="M-36 50 h72" stroke="#e0a800" stroke-width="6"/>'
 +''.join(f'<path d="M{d*16} {-6+k*8} l{d*(26-k*2)} {-10+k*6}" stroke="#f2c79b" stroke-width="5"/>' for d in (-1,1) for k in range(4))
 +'<circle cy="-24" r="12" fill="#f2c79b"/><path d="M-12 -34 h24 l-4 -16 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/></g>'
 +GENTLE(450,160,.6).replace('#e05a8a','#e0a800')+T(450,204,'UTSAVA (GOLD)',9,'#7a1d12')+T(280,206,'AṢṬABHUJĀ: EIGHT ARMS',10,'#7a1d12'))
pages.append(page('deity','THE GODDESS','Eight arms, seated in yoga',deity+'''<div class="g2">
<div class="card bg-red"><h4>🗡 Aṣṭabhujā</h4><p>The image in the sanctum has <b>eight arms</b>. She sits cross-legged in a yogic posture, her right heel pressed against the lowest of the seven <b>cakras</b>.</p></div>
<div class="card bg-yellow"><h4>✨ The festival image</h4><p>A golden <b>utsava</b> image goes out in procession; its consecration by a Maharaja is remembered each year at the <b>Vardhanti</b>.</p></div>
</div>
<div class="panel reading"><p><b>Power and stillness.</b> A warrior with eight weapons, seated in meditation: the Goddess who fought Mahiṣāsura is also the calm power at the root of every being.</p></div>'''))
leg1=fig(560,200,'The Goddess on her lion facing the buffalo demon Mahishasura, who emerges from a buffalo; the gods watching above',
 '<rect width="560" height="200" fill="#ffe9c4"/>'+DURGA(170,140,1.2)+'<g transform="translate(400 170)" stroke="#111" stroke-width="2"><ellipse cy="-20" rx="50" ry="22" fill="#3a3a3a"/><circle cx="-48" cy="-30" r="16" fill="#3a3a3a"/><path d="M-58 -44 q-10 -14 4 -16 M-40 -44 q10 -14 -4 -16" fill="none" stroke-width="4"/></g>'
 +MAHISHA(420,90,.6)+''.join(f'<circle cx="{x}" cy="24" r="8" fill="#ffd166" stroke="#111"/>' for x in (240,280,320)))
pages.append(page('mahisha','THE LEGEND · I','Mahiṣāsura and the hill',leg1+'''<div class="steps">
<div><b>The buffalo demon.</b> In the <b>Devī Māhātmya</b>, <b>Mahiṣāsura</b>, a demon who could change into a buffalo, defeated the gods and took heaven itself.</div>
<div><b>The Goddess born of light.</b> The gods’ combined anger blazed out as a single light, and from it rose the Goddess, armed with all their weapons, riding a lion.</div>
<div><b>The battle.</b> She destroyed his armies and his generals, and at last Mahiṣāsura himself, as he tried to escape from the buffalo’s body.</div>
<div><b>On this hill.</b> Mysuru’s tradition says the battle was fought here: Mahiṣāsura ruled this land, <b>Mahiṣūru</b>, “buffalo-town”, which became <b>Mysuru</b>.</div>
</div>'''+'<div class="panel reading small"><p>Read the battle verse by verse: <a href="/bhakti/devi/devi-mahatmya/">Devī Māhātmya</a> · <a href="/bhakti/devi/mahishasura-mardini/">Mahiṣāsura Mardinī</a>.</p></div>'))
pages.append(page('legends2','THE LEGEND · II','Folk tellings of the hill',fig(560,150,'The youngest of seven princess sisters arriving at a hill, and a young prince bowing before the Goddess',
 '<rect width="560" height="150" fill="#fdf3e8"/>'+HILL(140,150,240,110)+'<g transform="translate(140 60)">'+FIERCE(0,0,.45,'#3a2a2a')+'</g>'+person(420,146,'#e0a800','#c98b5a',.9)+'<path d="M404 96 h32 l-4 -10 h-24z" fill="#e0a800" stroke="#111"/>'+T(420,24,'YADURĀYA',10,'#7a1d12'))+'''<div class="steps">
<div><b>The youngest sister.</b> A Mysuru folk tale makes Cāmuṇḍī the youngest of seven warrior daughters of King Bijjalarāya of Ujjain, who came south, fought Mahiṣāsura here and stayed on the hill. Her fiery helper, Uri Māri, was given a home at the foot: see <a href="/bhakti/temples-of-india/around-mysuru/uttanahalli/">Uttanahaḷḷi</a>.</div>
<div><b>The founding prince.</b> Woḍeyar tradition says that in <b>1399</b> the young <b>Yadurāya</b>, by the Goddess’s grace, came to Mysuru and became the first Woḍeyar king. From then on she was the family’s Goddess.</div>
<div><b>Another view.</b> Some Jain scholars hold that the image was first a Jain <b>yakṣī</b>, Cāvuṇḍa or Vasantikā Devī, later worshipped as Cāmuṇḍī. This is a scholars’ claim, not the temple’s tradition.</div>
</div>'''))
pages.append(page('pitha','A ŚAKTI PĪṬHA','Where Satī’s hair fell',fig(560,150,'Shiva carrying Sati’s body across the sky, pieces falling to the earth; one strand of hair falling on a hill',
 '<rect width="560" height="150" fill="#2a0805"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="1.6" fill="#fff"/>' for a,b in ((40,20),(120,40),(500,30),(460,60),(300,14)))
 +person(260,90,'#3b6fd0','#8fd0f5',1)+'<path d="M280 70 q40 0 60 20" stroke="#c0392b" stroke-width="10" fill="none"/>'
 +'<path d="M340 90 q20 30 40 50" stroke="#2b1a0e" stroke-width="3" stroke-dasharray="4 4" fill="none"/>'+HILL(400,150,120,40)+T(400,146,'KRAUÑCA PĪṬHA',9,'#ffd166'))+'''<div class="panel reading">
<p><b>The story.</b> When Satī gave up her life at her father Dakṣa’s sacrifice, Śiva wandered the worlds carrying her body. Where its parts fell, the Goddess is worshipped as a <b>Śakti Pīṭha</b>, a seat of power.</p>
<p><b>Here.</b> Cāmuṇḍī Hills are counted among the <b>18 great Śakti Pīṭhas</b>, as the <b>Krauñca Pīṭha</b>, named after Krauñcapurī, an old name of the region. It is said that Satī’s <b>hair</b> fell here.</p>
<p><b>Lists differ.</b> Lists of the pīṭhas vary from text to text; the 18-pīṭha list is the one that includes Mysuru.</p>
</div>'''))
pages.append(page('history1','HISTORY · I','Before the Woḍeyars',tl([
 ('c. 950','The <b>Mahābaleśvara</b> temple on the hill, the oldest, from the Gaṅga era; the hill was once called Mahābalādri after it.'),
 ('12th c.','The Hoysaḷas: Viṣṇuvardhana is said to have expanded Mahābaleśvara, and the original Cāmuṇḍeśvarī shrine is thought to date from Hoysaḷa rule.'),
 ('1399','Woḍeyar tradition: Yadurāya founds the dynasty with the Goddess’s blessing.'),
 ('17th c.','Vijayanagara-era work on the temple’s tower, by some accounts.')])
 +'''<div class="panel reading"><p><b>Two temples, one hill.</b> Śiva as Mahābaleśvara was on the hill first; the Goddess’s fame grew around him until the hill itself took her name.</p></div>'''
 +talk("So Śiva was here first?","On this hill, yes. Now everyone says Cāmuṇḍī Beṭṭa. Śiva doesn't mind; she's his Śakti!")))
pages.append(page('history2','HISTORY · II','The Woḍeyars and their Goddess',tl([
 ('1610','<b>Rāja Woḍeyar</b> begins the royal celebration of the Goddess’s victory that grows into <b>Mysuru Dasara</b>.'),
 ('1659','<b>Doḍḍa Dēvarāja Woḍeyar</b> builds the stairway of about 1,000 steps.'),
 ('1664','He installs the great <b>Nandi</b> on the 700th step.'),
 ('1799 on','After Tipu’s fall, Mummaḍi <b>Kṛṣṇarāja Woḍeyar III</b> brings priests from Kāñcīpuram on the advice of the Kāñci seer.'),
 ('1827','Kṛṣṇarāja Woḍeyar III repairs the shrine and builds the seven-tiered <b>gopura</b> (some say 1830); he gives the <b>Siṃha Vāhana</b>, other vehicles and jewels.'),
 ('Later','Kṛṣṇarāja Woḍeyar IV builds Lalitādri, a palace on the hill.')])
 +'<div class="panel reading small"><p><b>A king at prayer.</b> Inside the temple stands a 6-ft statue of Kṛṣṇarāja Woḍeyar III, hands folded, with his three queens, Ramāvilāsa, Lakṣmīvilāsa and Kṛṣṇavilāsa, their names carved on the pedestals.</p></div>'))
pages.append(page('temple','THE TEMPLE','Gopura, silver doors and sanctum',fig(560,200,'The seven-tiered gopura with seven golden finials, silver doors at the entrance, and the small vimana over the sanctum behind',
 '<rect width="560" height="200" fill="#fdf3e8"/>'+GOP(200,196,1.9)+'<rect x="186" y="160" width="28" height="36" fill="#d8dde3" stroke="#111"/>'+'<g transform="translate(400 196)" stroke="#111" stroke-width="1.6"><rect x="-40" y="-40" width="80" height="40" fill="#e2cfa8"/><path d="M-24 -40 l24 -40 l24 40z" fill="#d9c9a0"/><circle cy="-84" r="4" fill="#e0a800"/></g>'+T(400,120,'VIMĀNA',10,'#7a1d12')+T(200,24,'7 TIERS · 7 KALAŚAS',10,'#7a1d12'))+facts([
 ('Plan','A quadrangular Dravidian temple: doorways, navaraṅga hall, antarāḷa and sanctum, inside a prākāra'),
 ('Gopura','A <b>seven-tiered</b> tower over the entrance, crowned by <b>seven gold kalaśas</b>'),
 ('Doors','The main doors are faced with <b>silver</b>, carved with forms of the Goddess'),
 ('Vimāna','A smaller tower over the sanctum'),
 ('Also inside','Gaṇeśa; Kālabhairava; the statue of Kṛṣṇarāja Woḍeyar III and his queens')])))
pages.append(page('nandi','THE STEPS AND THE NANDI','A climb with a giant bull',fig(560,190,'Stone steps winding up the hill with pilgrims, and a giant black Nandi halfway, decorated with garlands and bells',
 '<rect width="560" height="190" fill="#eef6e4"/>'+''.join(f'<path d="M{40+i*14} {180-i*8} h18" stroke="#7a5a2a" stroke-width="3"/>' for i in range(20))+NANDI(360,170,1.6)+person(240,104,'#ffd60a','#c98b5a',.4)+person(150,140,'#c0392b','#c98b5a',.4)+T(360,186,'4.9 m TALL · 7.6 m LONG · ONE STONE',10,'#333'))+facts([
 ('The steps','About <b>1,000</b> stone steps (often counted as 1,008), built by Doḍḍa Dēvarāja Woḍeyar in <b>1659</b>'),
 ('A pilgrim custom','Many devotees climb on foot, often marking each step with turmeric and kuṅkuma as a vow'),
 ('The Nandi','Installed in <b>1664</b> on the <b>700th step</b>, before a small Śiva shrine: about <b>4.9 m</b> tall and <b>7.6 m</b> long, carved from a single block of granite'),
 ('Black or white?','The stone is pale; years of oil abhiṣeka make it look black')])
 +talk("Do people really climb a thousand steps?","Thousands do, especially on Āṣāḍha Fridays. The Nandi is the halfway cheer-up point!")))
pages.append(page('mahisasura','THE MAHIṢĀSURA STATUE','The demon at the gate',fig(560,190,'A tall, brightly painted statue of the demon Mahishasura holding a sword in his right hand and a cobra in his left',
 '<rect width="560" height="190" fill="#e8f0fa"/>'+MAHISHA(280,110,1.6)+'<rect x="230" y="176" width="100" height="14" fill="#8a8a8a" stroke="#111"/>')+'''<div class="panel reading">
<p><b>The welcome.</b> A towering, brightly painted statue of <b>Mahiṣāsura</b>, sword in his right hand and a cobra in his left, stands on the hilltop near the temple.</p>
<p><b>Why the demon?</b> He is part of the hill’s story and of the city’s name. Visitors meet the defeated king first, then go in to the Goddess who defeated him.</p>
<p><b>A Mysuru icon.</b> With the Nandi and the gopura, he is one of the three sights every child of Mysuru remembers from the hill.</p>
</div>'''+talk("He looks scary!","He was. That's why we needed the Goddess. Now he's the hill's most photographed guest!")))
pages.append(page('festivals','THROUGH THE YEAR','Fridays, a birthday and Dasara',facts([
 ('Āṣāḍha Fridays','The Fridays of Āṣāḍha (June–July) are especially sacred: vast crowds come from across Karnataka and neighbouring states'),
 ('Vardhanti','The <b>Cāmuṇḍī Vardhanti</b> in Āṣāḍha marks the Maharaja’s consecration of the festival image, which is taken round the temple in a golden palanquin'),
 ('Navarātri','The chief festival: the Goddess is adorned in nine ways as the <b>Navadurgās</b>; on the 7th day, jewels given by the Maharajas are brought from the district treasury to adorn her'),
 ('Rathotsava','The car festival, with the Siṃha Vāhana given by Kṛṣṇarāja Woḍeyar III')])))
dasara=fig(560,180,'A great decorated elephant carrying a golden howdah with the Goddess’s idol in it, leading a procession past the illuminated palace',
 '<rect width="560" height="180" fill="#141f45"/>'+''.join(f'<circle cx="{a}" cy="40" r="2" fill="#ffd166"/>' for a in range(20,560,16))
 +'<g transform="translate(280 170)" stroke="#111" stroke-width="2"><ellipse cy="-50" rx="70" ry="40" fill="#8a8a96"/><circle cx="-70" cy="-70" r="26" fill="#8a8a96"/><path d="M-90 -60 q-16 40 2 60" fill="none" stroke="#8a8a96" stroke-width="12"/><path d="M-80 -86 q10 -10 22 0" fill="#c0392b"/><rect x="-46" y="-12" width="16" height="22" fill="#8a8a96"/><rect x="30" y="-12" width="16" height="22" fill="#8a8a96"/>'
 +'<path d="M-40 -84 h80 v-16 q-40 -40 -80 0z" fill="#e0a800"/><circle cy="-108" r="6" fill="#c0392b"/></g>'+T(280,20,'JAMBŪ SAVĀRI · VIJAYADAŚAMĪ',12,'#ffd166'))
pages.append(page('dasara','DASARA','The Goddess rides the golden howdah',dasara+'''<div class="panel reading">
<p><b>Since 1610.</b> Mysuru Dasara, Karnataka’s <b>Nāḍa Habba</b> (state festival), celebrates the Goddess’s victory over Mahiṣāsura. It grew from the celebration begun by Rāja Woḍeyar and is held at the palace every year.</p>
<p><b>The procession.</b> On <b>Vijayadaśamī</b>, the idol of Cāmuṇḍeśvarī is placed in the <b>golden howdah</b>, about <b>750 kg</b>, on the lead elephant, and the Jambū Savāri travels about 5.5 km from the palace to Bannimaṇṭapa, watched by lakhs.</p>
<p><b>Then and now.</b> Once the Maharaja rode in the howdah; today the Goddess herself does.</p>
</div>'''+talk("The Goddess rides an elephant through town?","Once a year, in gold! The hill's Goddess comes down to bless her city.")))
pages.append(page('around','AROUND THE HILL','The Goddess’s neighbourhood',facts([
 ('Mahābaleśvara','Śiva’s old temple on the summit, the hill’s first shrine'),
 ('Uttanahaḷḷi','Jvālāmukhī Tripurasundarī, Cāmuṇḍī’s sister, at the foot of the hill'),
 ('Lalitādri','A palace on the hill built under Kṛṣṇarāja Woḍeyar IV'),
 ('Mysuru Palace','The palace and its temples, where Dasara is held'),
 ('The forest','The Cāmuṇḍī Hills reserve forest, part of it set aside as a Daivavana, a sacred grove, in 2011')])
 +'''<div class="panel reading"><p>More: <a href="/bhakti/temples-of-india/around-mysuru/uttanahalli/">Uttanahaḷḷi</a> · <a href="/bhakti/temples-of-india/around-mysuru/palace-temples/">The Palace Temples</a> · <a href="/bhakti/temples-of-india/around-mysuru/">Temples around Mysuru</a>.</p></div>'''))
glossary=[('Cāmuṇḍā','the Goddess who slew Caṇḍa and Muṇḍa'),('Mahiṣāsura','the buffalo demon'),('Mahiṣūru','“buffalo-town”, the root of Mysuru'),('Nāḍa Devī','Goddess of the land'),('Nāḍa Habba','festival of the land: Dasara'),('Śakti Pīṭha','a seat of the Goddess where part of Satī fell'),('Krauñca','the old name of the region'),('Aṣṭabhujā','eight-armed'),('Vardhanti','anniversary of consecration'),('Āṣāḍha','the month of June–July'),('Siṃha Vāhana','the lion vehicle'),('Jambū Savāri','the elephant procession of Dasara'),('Howdah','the seat on an elephant'),('Yakṣī','a Jain or folk guardian goddess')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','CĀMUṆḌEŚVARĪ ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Goddess.</b> Cāmuṇḍeśvarī, eight-armed slayer of Mahiṣāsura: Nāḍa Devī and the Woḍeyars’ family Goddess.</div>
<div><b>The place.</b> Cāmuṇḍī Hills above Mysuru, the city named after the demon she defeated; a Śakti Pīṭha where Satī’s hair fell.</div>
<div><b>The history.</b> Mahābaleśvara (c. 950), a Hoysaḷa shrine, the steps of 1659, the Nandi of 1664, the gopura of 1827.</div>
<div><b>The sights.</b> The 1,000 steps, the single-stone Nandi, the Mahiṣāsura statue, the seven-tiered gopura.</div>
<div><b>The festivals.</b> Āṣāḍha Fridays, the Vardhanti, Navarātri, and Dasara’s golden howdah.</div>
</div>'''+talk("One line to remember?","A city named after a demon, watched over by the Goddess who beat him. That's Mysuru.")+'<div class="key">The Goddess of the hill: <b>Mysuru’s mother, Karnataka’s Nāḍa Devī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Chamundeshwari Temple”: Hoysaḷa shrine; Vijayanagara tower; 1659 steps; Aṣṭabhujā; Nandi of 1664 on the 700th step; Mahiṣāsura and Mahiṣūru; Nāḍa Devī; Krauñca Pīṭha and Satī’s hair; Āṣāḍha Fridays; Navarātri and the 7th-day jewels; Cāmuṇḍī Jayanti; Dasara as Nāḍa Habba; Mahābaleśvara; Uttanahaḷḷi. Wikipedia, “Chamundi Hills”: 1,060 m; 1827 renovation; the yogic posture; Mahiṣāsura statue; 1,008 steps; Nandi 4.9 × 7.6 m; ecology. Official temple site and mysore.org.uk (Siṃha Vāhana; KR III statue and queens; Lalitādri). Shastriya Kannada (Mahābaleśvara c. 950; Viṣṇuvardhana). Karnataka Tourism (Ganga-era Mahābaleśvara; gopura 1830; Nandi colour).</p>
<p><b>Dasara:</b> Wikipedia, “Golden Howdah”; Deccan Herald (750 kg; 5.5 km route). Imvoyager (1399 Yadurāya; 1610 Dasara). Deccan Herald, 2017 (Kāñci priests; the Jain yakṣī claim).</p>
<p><b>Sources differ:</b> 1827 or 1830 for the gopura; 1,000 or 1,008 steps. <b>Not verified:</b> the 1399 Yadurāya story (dynastic tradition); the pilgrims’ step custom (common practice). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('deity','The Goddess'),('mahisha','Legend · Mahiṣāsura'),('legends2','Legend · Folk Tellings'),('pitha','A Śakti Pīṭha'),('history1','History · Before the Woḍeyars'),('history2','History · The Woḍeyars'),('temple','The Temple'),('nandi','The Steps and the Nandi'),('mahisasura','The Mahiṣāsura Statue'),('festivals','Through the Year'),('dasara','Dasara'),('around','Around the Hill'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,6.2vw,68px)">CĀMUṆḌEŚVARĪ</h1>
  <div class="series">CĀMUṆḌĪ HILLS · NĀḌA DEVĪ · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess who gave Mysuru its name</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Every Mysurean grows up under one hill. On top of it sits the Goddess who, the city believes, defeated the buffalo demon Mahiṣāsura and gave <b>Mysuru</b> its name.</p>
    <p>She is <b>Cāmuṇḍeśvarī</b>: family Goddess of the Woḍeyars, Nāḍa Devī of Karnataka, and the Goddess who rides the golden howdah at Dasara.</p>
    <p>This guide tells her legends, her temple, her hill and her festivals.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Cāmuṇḍī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is this the most famous temple in Mysuru?","No contest! The city, the palace and Dasara all lead back to her.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Chamundeshwari.html','w').write(head+b+tail())
print('ok')
