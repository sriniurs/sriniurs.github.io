from kt_common import *
i=1
STONE='#e3eaf3'
def frieze(w=520,rows=('elephants','lions','horsemen','scrolls')):
    cols=['#8f8a7a','#a7a08c','#9a9484','#b5ae9a']; o=''
    for k,r in enumerate(rows):
        y=20+k*36; o+=f'<rect x="20" y="{y}" width="{w}" height="32" fill="{cols[k%4]}"/>'
        for j in range(12):
            x=34+j*42
            if r=='elephants': o+=f'<ellipse cx="{x}" cy="{y+18}" rx="14" ry="10" fill="#6f6a5a"/><path d="M{x-14} {y+16} q-6 8 -2 14" stroke="#6f6a5a" stroke-width="3" fill="none"/>'
            elif r=='lions': o+=f'<circle cx="{x}" cy="{y+16}" r="9" fill="#6f6a5a"/><path d="M{x+6} {y+18} h12" stroke="#6f6a5a" stroke-width="5"/>'
            elif r=='horsemen': o+=f'<path d="M{x-12} {y+26} l6 -14 h14 l4 14" stroke="#6f6a5a" stroke-width="3" fill="none"/><circle cx="{x}" cy="{y+8}" r="4" fill="#6f6a5a"/>'
            else: o+=f'<path d="M{x-16} {y+16} q8 -12 16 0 t16 0" stroke="#6f6a5a" stroke-width="3" fill="none"/>'
        o+=txt(w+6,y+20,r,9,'start',font=NS,weight='700')
    return o
fw=foreword(i,['Eight centuries ago, in the green Malenāḍu country west of Hassan, the Hoysaḷa kings filled two towns with temples carved so finely from soft grey-green stone that people call them lace. At <b>Belūr</b> Viṣṇu stands as Cennakeśava, “the handsome Keśava”, ringed by dancing bracket-maidens; at <b>Haḷebīḍu</b>, the old capital, Śiva’s twin shrines carry friezes of elephants, lions and the epics running round the walls.',
 'This guide covers the Hoysaḷa story and its emblem of Saḷa and the tiger, the king Viṣṇuvardhana and queen Śāntalā, the stone and the star-shaped plan, the Belūr temple and its <b>madanikās</b>, the Haḷebīḍu temple and its friezes, the sculptors who signed their names, the sack of the capital, and the living worship at Belūr today.',
 'Part 2 of our '+L('/temples-of-india/karnataka/','Temples of Karnataka')+'. Previous: '+L('/temples-of-india/karnataka/hampi-virupaksha/','Hampi Virūpākṣa')+'. The Hoysaḷas also built '+L('/temples-of-india/around-mysuru/melukote/','Melukōṭe')+'’s patrons’ world; on reading temples, see '+L('/temples-of-india/how-to-read-a-hindu-temple/','How to Read a Hindu Temple')+'.'],
 [('z','Stone lace?'),('b','Soapstone is soft when cut and hardens in the air. The Hoysaḷa sculptors carved it like wood.')])
gl=glance([('Belūr','Cennakeśava (Viṣṇu) temple, consecrated 1117 by King Viṣṇuvardhana; still in worship'),('Haḷebīḍu','Hoysaḷeśvara (Śiva) temple, begun about 1121, completed about 1160; twin shrines'),('Where','Hassan district, Karnataka, about 16 km apart'),('Dynasty','The Hoysaḷas (c. 11th–14th century)'),('Stone','Chloritic schist (“soapstone”)'),('Plan','Star-shaped (stellate) shrines on a raised platform (jagati)'),('Famous for','Madanikās (bracket figures) at Belūr; friezes at Haḷebīḍu'),('Sculptors','Dāsoja, Cāvaṇa, Mallitamma at Belūr; Ketana, Mabala and others at Haḷebīḍu'),('Sacked','Early 14th century by Delhi Sultanate armies'),('UNESCO','2023, “Sacred Ensembles of the Hoysaḷas”')],
 S('A star-shaped Hoysaḷa temple on its platform',g(280,200,1.8,hoysala_star(110)),STONE,210),
 [('z','Why “sacred ensembles”?'),('b','UNESCO listed Belūr, Haḷebīḍu and Somanāthapura together as one great Hoysaḷa group.')],'Grey-green stone <b>carved like lace</b>.')
sala=story('sala','STORY · SAḶA AND THE TIGER','How the Hoysaḷas got their name',
 strip('Three panels: a monk in a forest temple; a tiger leaping; a young man striking the tiger',
  [('<rect width="144" height="190" fill="#e9f2e1"/>'+g(40,170,.8,tree('#2f6a3a'))+g(100,170,.8,sage('#f4f1ea')),'#e9f2e1'),
   ('<rect width="144" height="190" fill="#e9f2e1"/>'+g(72,150,1,'<ellipse rx="34" ry="14" fill="#f4a020"/><circle cx="34" cy="-8" r="12" fill="#f4a020"/><path d="M-20 -10 l4 20 M0 -12 l4 20 M20 -10 l-2 20" stroke-width="2.5"/>'),'#e9f2e1'),
   ('<rect width="144" height="190" fill="#e9f2e1"/>'+g(50,170,.9,person('#8e1f17'))+'<path d="M64 100 l30 -30" stroke-width="4"/>'+g(110,160,.7,'<ellipse rx="30" ry="12" fill="#f4a020"/>'),'#e9f2e1')],
  ['the monk','the tiger','“Hoy, Saḷa!”']),'The dynasty’s founding legend, carved as its emblem. (Tradition.)',
 ['In the hills of Malenāḍu a young man named <b>Saḷa</b> was with a Jain teacher at a forest shrine (tradition places it at Sosevūru, Aṅgaḍi).',
  'A <b>tiger</b> leapt out at them.',
  'The teacher cried, “<b>Hoy, Saḷa!</b>” (“Strike, Saḷa!”).',
  'Saḷa struck the tiger down.',
  'From that cry came the name <b>Hoysaḷa</b>, and the image of Saḷa fighting the tiger became the dynasty’s emblem, set before many of its temples.'],
 [('z','Is the tiger the Cōḷas?'),('b','Some read it so, since the Cōḷa emblem was a tiger. It is a nice reading. The legend itself is older than that victory. (Interpretation.)')],'A shout in the forest <b>named a dynasty</b>.')
king=reading('vishnuvardhana','VIṢṆUVARDHANA AND ŚĀNTALĀ','The king and the queen',
 S('A king and a dancing queen before a temple',g(150,200,1.4,person('#8e1f17'))+'<path d="M134 92 l16 -20 l16 20z" fill="#e0a800"/>'+g(300,200,1.3,person('#c0392b'))+'<path d="M282 118 q18 -30 36 0" stroke="#e0a800" stroke-width="3" fill="none"/>'+g(460,200,.9,hoysala_star(70)),STONE,210),
 ['<b>The king.</b> <b>Viṣṇuvardhana</b> (12th century) made the Hoysaḷas a great power. He is commonly described as born a Jain (as Biṭṭideva) who turned to Vaiṣṇavism, tradition says under the influence of Rāmānujācārya. (Tradition.)',
  '<b>Belūr, 1117.</b> He commissioned the Cennakeśava temple and consecrated it in 1117. It is commonly said to celebrate a victory over the Cōḷas at Talakāḍu. (Commonly said.)',
  '<b>Śāntalā.</b> His queen, <b>Śāntalā Devī</b>, sponsored the smaller <b>Kappe Cennigarāya</b> temple beside the main one. She is remembered in tradition as a great dancer, and many see her in the dancing figures of Belūr. (Tradition.)',
  '<b>Haḷebīḍu.</b> At his capital, Dorasamudra, his officer <b>Ketamalla</b> built the Hoysaḷeśvara temple from about 1121.',
  '<b>Tolerance.</b> Jain basadis stand beside the Śiva and Viṣṇu temples: the Hoysaḷas patronised all three.'],
 [('z','A Jain king built Viṣṇu’s temple?'),('b','A king who had become a Vaiṣṇava, with a Jain queen and Jain ministers. Karnataka’s history is full of such households.')],'A king, a queen, <b>and three faiths</b>.')
stone=reading('stone','THE STONE AND THE STAR','How Hoysaḷa temples are built',
 S('A star-shaped plan seen from above beside a block of grey-green stone being carved',g(160,120,1,'<polygon points="'+' '.join(f'{90*__import__("math").cos(__import__("math").radians(a*11.25)) if a%2==0 else 72*__import__("math").cos(__import__("math").radians(a*11.25)):.0f},{90*__import__("math").sin(__import__("math").radians(a*11.25)) if a%2==0 else 72*__import__("math").sin(__import__("math").radians(a*11.25)):.0f}' for a in range(32))+'" fill="#8f8a7a"/>')+g(400,190,1,'<rect x="-50" y="-60" width="100" height="60" fill="#7f8a7a"/>')+g(470,190,1,person('#1d4f8a',seat=True))+T(160,220,'star (stellate) plan',10)+T(420,220,'soapstone block',10),STONE,230),
 ['<b>Soapstone.</b> The temples are carved in <b>chloritic schist</b>, a fine-grained stone soft enough to carve in great detail when fresh, which hardens with time.',
  '<b>A star plan.</b> Hoysaḷa shrines are <b>stellate</b>: their walls step in and out in many points, so that light and shadow play across them all day.',
  '<b>The jagati.</b> The temples stand on a raised platform that follows the outline of the building, giving a walkway around it.',
  '<b>Lathe-turned pillars.</b> Inside, pillars look as if turned on a lathe, polished to a shine.',
  '<b>Layers of carving.</b> The outer walls carry bands of friezes at the base, then large images of gods above. Read more in '+L('/temples-of-india/how-to-read-a-hindu-temple/','How to Read a Hindu Temple')+'.'],
 [('z','Why a star?'),('b','More corners, more faces, more places for sculpture and for light. The plan is made for the eye.')],'A star of stone <b>that plays with light</b>.')
belur=reading('belur','CENNAKEŚAVA OF BELŪR','The handsome Keśava',
 S('The Belūr temple with a Vijayanagara gopura in front and a tall Viṣṇu image within',g(150,210,1.4,GOP(0,0,1,6))+g(380,210,1.6,hoysala_star(90))+g(380,150,.6,god('#1d4f8a')),STONE,220),
 ['<b>The god.</b> Viṣṇu as <b>Cennakeśava</b>, “the handsome Keśava”, also known as Vijayanārāyaṇa, stands in the sanctum.',
  '<b>Still in worship.</b> Unlike many Hoysaḷa temples, Belūr has been in worship for nine centuries; the god is taken out on an annual chariot (ratha).',
  '<b>Kappe Cennigarāya.</b> Queen Śāntalā’s smaller temple stands to the south of the main shrine.',
  '<b>The gateway.</b> The tall gopura at the entrance was added in the Vijayanagara era, replacing an earlier gateway that had been burnt.',
  '<b>The courtyard.</b> Smaller shrines, a stepped tank and pavilions fill the walled courtyard.'],
 [('z','Why “handsome”?'),('b','Cenna in Kannaḍa is “beautiful”. The god of the most beautiful temple got the most beautiful name.')],'The handsome god <b>in the most beautiful house</b>.')
mad=reading('madanikas','THE MADANIKĀS','Forty dancing figures under the eaves',
 S('A row of slender bracket figures of dancers, a woman with a mirror, a hunter, a woman with a parrot',''.join(g(60+k*90,200,1.4,bracket_figure()) for k in range(6))+T(150,214,'with a mirror',9)+T(330,214,'with a parrot',9),STONE,220),
 ['<b>What they are.</b> Under the eaves of the Belūr temple, angled as brackets between pillar and roof, stand the <b>madanikās</b> (also śilābālikās): carved figures of women dancing, dressing, playing music, hunting.',
  '<b>How many.</b> Forty were carved; 38 survive.',
  '<b>Famous ones.</b> A woman with a <b>mirror</b> (often called Darpaṇa Sundarī), a woman with a <b>parrot</b>, a huntress with a bow: each is carved down to the jewellery and fingernails.',
  '<b>Who carved them.</b> <b>Dāsoja</b> and his son <b>Cāvaṇa</b> of Baḷḷigāve are credited with madanikās; the sculptor <b>Mallitamma</b> is also named.',
  '<b>What they mean.</b> Many read them as the beauty of the world gathered at the god’s door. (Interpretation.)'],
 [('z','Dancers on a temple?'),('b','Dance was worship. And the figures do hold up the roof: beauty with a job to do.')],'Beauty <b>holding up the roof</b>.')
pillar=reading('pillars','THE PILLARS OF BELŪR','The Narasiṃha pillar and the turned columns',
 S('A hall of richly carved pillars, one covered in tiny figures',''.join(g(80+k*100,210,1,'<rect x="-14" y="-150" width="28" height="150" fill="#8f8a7a"/>'+''.join(f'<ellipse cy="{-20-j*26}" rx="20" ry="8" fill="#7f7a6a"/>' for j in range(5))) for k in range(5))+g(280,120,1,'<rect x="-16" y="-60" width="32" height="80" fill="#9a9484"/>'+''.join(f'<circle cx="{(j%3-1)*8}" cy="{-50+j*8}" r="2.5" fill="#6f6a5a"/>' for j in range(12))),STONE,220),
 ['<b>The hall.</b> Inside the main hall, dozens of pillars, no two alike, carry the roof; many look lathe-turned and shine with polish.',
  '<b>The Narasiṃha pillar.</b> One pillar is covered in miniature figures, including a tiny bull. Tradition says it once could be turned on its base; today it no longer rotates.',
  '<b>Ceilings.</b> Above, carved domed ceilings with hanging lotus pendants.',
  '<b>Dark and cool.</b> The hall is dim; guides use a lamp to show the carvings, as pilgrims once did with oil lamps.',
  '<b>A puzzle for scholars.</b> How the lathe-like finish was achieved on huge stone pillars is still discussed.'],
 [('z','A pillar that turned?'),('b','So people say. Whether or not it ever did, the carving on it is the real wonder.')],'Pillars <b>no two alike</b>.')
hal=reading('halebidu','HOYSAḶEŚVARA OF HAḶEBĪḌU','The twin shrines of the old capital',
 S('Two connected star-shaped shrines with two Nandi pavilions before them',g(200,200,1.3,hoysala_star(80))+g(370,200,1.3,hoysala_star(80))+g(200,214,.6,'<ellipse rx="40" ry="12" fill="#6f6a5a"/>')+g(370,214,.6,'<ellipse rx="40" ry="12" fill="#6f6a5a"/>'),STONE,220),
 ['<b>Dorasamudra.</b> Haḷebīḍu, “the old capital”, was <b>Dorasamudra</b>, the Hoysaḷa capital, beside a great lake.',
  '<b>Twin shrines.</b> The Hoysaḷeśvara temple is a Śiva temple with <b>two shrines</b> side by side, for the liṅgas Hoysaḷeśvara and Śāntaleśvara, each with its own <b>Nandi</b> pavilion. A small Sūrya shrine is attached.',
  '<b>Its dates.</b> Begun about 1121 and completed about 1160; an inscription names Ketamalla, Viṣṇuvardhana’s officer, as builder.',
  '<b>Towerless.</b> The original towers over the shrines are lost; the temple stands low and wide.',
  '<b>Two names.</b> The shrines are named for the dynasty and, by tradition, for the queen Śāntalā.'],
 [('z','A Śiva temple named after a queen?'),('b','Hoysaḷeśvara for the king’s line, Śāntaleśvara for the queen. Śiva receives the royal couple.')],'Śiva in two shrines <b>for a king and a queen</b>.')
friz=reading('friezes','THE FRIEZES','Elephants, lions, horsemen and the epics',
 svg(560,180,'Horizontal bands of carved friezes: elephants, lions, horsemen and scrolls','<rect width="560" height="180" fill="#e3eaf3"/>'+frieze(480)),
 ['<b>Bands round the base.</b> Running all round the Haḷebīḍu temple are horizontal bands: <b>elephants</b> at the bottom (strength), then <b>lions</b> (courage), <b>horsemen</b> (speed), and scrolls of foliage. (A common reading of the order.)',
  '<b>The stories.</b> Above them, friezes tell scenes from the <b>Rāmāyaṇa</b>, the <b>Mahābhārata</b> and the <b>Bhāgavata Purāṇa</b>: about 340 large reliefs and friezes in all.',
  '<b>Never repeating.</b> Visitors say no two elephants in the bottom row are alike. (Commonly said.)',
  '<b>Signed.</b> Sculptors’ names such as Manibāḷaki, Mābala and Ketana are carved on panels.',
  '<b>Gods.</b> Large images above include dancing Śiva, Gaṇeśa, and Kṛṣṇa lifting Govardhana.'],
 [('z','Can you read the Mahābhārata on a wall?'),('b','Walk round slowly and you can follow whole episodes. These walls were books for people who could not read.')],'A temple wall <b>that is also a book</b>.')
artists=reading('sculptors','THE SCULPTORS','Artists who signed their work',
 S('A sculptor carving a figure with chisel and mallet, his name inscribed on the base',g(200,200,1.3,person('#1d4f8a',seat=True))+g(330,200,1.6,bracket_figure())+'<rect x="290" y="200" width="80" height="14" fill="#8f8a7a"/>'+T(330,212,'Dāsoja',9),STONE,220),
 ['<b>Named artists.</b> Unusually for Indian temples, Hoysaḷa sculptors often <b>signed</b> their work on the panels.',
  '<b>At Belūr.</b> <b>Dāsoja</b> and his son <b>Cāvaṇa</b> of Baḷḷigāve, and <b>Mallitamma</b>, are among the names recorded.',
  '<b>At Haḷebīḍu.</b> Names such as <b>Manibāḷaki</b>, <b>Mābala</b> and <b>Ketana</b> appear.',
  '<b>Jakaṇācāri.</b> Popular tradition credits a legendary master sculptor, <b>Amarashilpi Jakaṇācāri</b>, with these temples; historians treat him as a figure of legend. (Tradition.)',
  '<b>Guilds.</b> The work was done by families and guilds of craftsmen over decades.'],
 [('z','Why sign a temple?'),('b','Pride, and perhaps devotion: a name at the god’s feet. We remember them nine centuries later.')],'Artists <b>who left their names</b>.')
sack=reading('sack','THE SACK OF THE CAPITAL','Dorasamudra plundered',
 S('A ruined temple with broken towers, a lake beside it',g(280,200,1.6,hoysala_star(110))+'<path d="M200 120 l20 -20 l10 14 l14 -24 l16 30" fill="none" stroke="#5a5a5a" stroke-width="3"/>'+'<rect x="0" y="190" width="160" height="30" fill="#4aa3df"/>',STONE,220),
 ['<b>Early 14th century.</b> Armies of the Delhi Sultanate under Alauddin Khilji invaded and plundered the Hoysaḷa capital.',
  '<b>1326.</b> Belūr and Haḷebīḍu were plundered again by an army of Muhammad bin Tughlaq.',
  '<b>The end of the dynasty.</b> The Hoysaḷas did not recover; within decades the Vijayanagara empire rose in the east (see '+L('/temples-of-india/karnataka/hampi-virupaksha/','Hampi')+').',
  '<b>Haḷebīḍu abandoned.</b> The capital became “the old capital”; its great temple fell out of worship and lost its towers.',
  '<b>Belūr lived.</b> Belūr’s temple was repaired, given a new gateway in the Vijayanagara period, and kept in worship.'],
 [('z','Why did Belūr survive in worship and not Haḷebīḍu?'),('b','A capital is a target; a temple town can recover. And Belūr had a living god people kept coming to.')],'One temple ruined, <b>one kept alive</b>.')
jain=cards('around','AROUND BELŪR AND HAḶEBĪḌU','More Hoysaḷa treasures',
 S('A Jain basadi, a small temple and a lake',g(120,200,1,'<rect x="-50" y="-60" width="100" height="60" fill="#a7a08c"/><path d="M-56 -60 h112 l-12 -20 h-88z" fill="#8f8a7a"/>')+T(120,214,'Jain basadis',10)+g(300,200,1,hoysala_star(60))+T(300,214,'Kedāreśvara',10)+'<rect x="400" y="160" width="140" height="40" fill="#4aa3df"/>'+T(470,214,'the old lake',10),STONE,220),
 [('🛕','Kedāreśvara','A smaller Śiva temple at Haḷebīḍu, also richly carved.'),('☸️','Jain basadis','A group of Jain temples at Haḷebīḍu (Bastihaḷḷi) with polished pillars.'),('🏛️','Somanāthapura','The third of the UNESCO Hoysaḷa ensemble, near Mysuru: the Keśava temple of 1268.'),('🌾','Malenāḍu','The green hill country of Hassan and Chikkamagaḷūru, with Śravaṇabeḷagoḷa not far away.'),('🛕','Melukōṭe','Rāmānuja’s town, linked in tradition with Viṣṇuvardhana. See '+L('/temples-of-india/around-mysuru/melukote/','Melukōṭe')+'.'),('📜','Inscriptions','Hundreds of Hoysaḷa inscriptions record gifts, builders and battles.')],
 None,'A whole Hoysaḷa world <b>nearby</b>.')
endp=end(i,['<b>Dynasty.</b> The Hoysaḷas, named for Saḷa who struck the tiger.','<b>Belūr.</b> Cennakeśava, 1117, Viṣṇuvardhana and Śāntalā; madanikās; still in worship.','<b>Haḷebīḍu.</b> Twin Śiva shrines from about 1121; friezes of elephants, lions and the epics.','<b>Craft.</b> Soapstone, star plans, signed sculptors.','<b>Fate.</b> Sacked in the 14th century; UNESCO World Heritage in 2023.'],
 'Part 3 goes north to Savadatti and the Goddess Yellamma.','Stone lace of the Hoysaḷas')
src=sources([('Temples:','Wikipedia, “Chennakeshava Temple, Belur” (1117, Viṣṇuvardhana, soapstone, Dāsoja and Cāvaṇa, Mallitamma, 40/38 madanikās, Śāntalā’s Kappe Cennigarāya, Narasiṃha pillar, Vijayanagara gopura, UNESCO 2023); Wikipedia, “Hoysaleswara Temple” (1121–1160, Ketamalla, twin shrines and Nandis, Sūrya shrine, 340 reliefs, artists’ names, invasions, UNESCO 2023).')],
 'the Saḷa legend, the Talakāḍu victory, Viṣṇuvardhana’s conversion under Rāmānuja, Śāntalā as dancer, the name “Darpaṇa Sundarī”, Jakaṇācāri and the order-meaning of the friezes are tradition or common description, not checked in the main sources.','Dates as in the main encyclopedia sources.')
finish(i,'PART 2 OF 5 · BELŪR · HAḶEBĪḌU · MADANIKĀS',covart('A star-shaped Hoysaḷa temple with a bracket figure and a carved frieze',g(250,186,1.5,hoysala_star(90))+g(80,190,1.5,bracket_figure())+g(400,190,1.5,bracket_figure())),'Stone lace of the Hoysaḷas',
 'The Hoysaḷa temples of <b>Belūr</b> and <b>Haḷebīḍu</b>: Saḷa and the tiger, the king and the queen, the <b>madanikās</b>, the <b>friezes</b>, and the sculptors who signed their names.',
 'Belūr Cennakeśava and Haḷebīḍu Hoysaḷeśvara explained and illustrated: the Hoysaḷa dynasty and Saḷa’s tiger, Viṣṇuvardhana and Śāntalā, soapstone and star plans, the madanikās and Narasiṃha pillar, the twin shrines and friezes, signed sculptors, the 14th-century sack and UNESCO listing.',
 [fw,gl,sala,king,stone,belur,mad,pillar,hal,friz,artists,sack,jain,endp,src])
