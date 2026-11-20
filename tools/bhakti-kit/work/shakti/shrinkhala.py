exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Śṛṅkhalā Devī · Pradyumna · The 18 Śakti Pīṭhas · srini.presents',
 'Śṛṅkhalā Devī of Pradyumna, the third of the 18 Śakti Pīṭhas, the seat with no temple: Pandua in Hooghly, its minaret and ruined mosque, the disputed history of the site, the Ṛṣyaśṛṅga and Rukmiṇī legends, and the other places that claim the Goddess. An illustrated reference guide.')
def bg(lat,lon): return 60+(lon-87.6)*300, 20+(23.6-lat)*130
RIV=[(23.6,88.30),(23.22,88.36),(22.99,88.40),(22.57,88.36),(22.19,88.19),(21.70,88.10)]
def BMAP(marks,w=560,h=280):
    rv='M'+' L'.join(f'{bg(a,b)[0]:.0f} {bg(a,b)[1]:.0f}' for a,b in RIV)
    g=''
    for la,lo,t,side,col in marks:
        x,y=bg(la,lo); r=8 if col=='#c0392b' else 5
        g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',t,12,'#111','start' if side=='r' else 'end')
    return (f'<rect width="{w}" height="{h}" fill="#eef5e0"/><path d="M0 {bg(21.75,0)[1]:.0f} Q200 {bg(21.6,0)[1]:.0f} {w} {bg(21.8,0)[1]:.0f} V{h} H0z" fill="#4aa3df"/>'
     +f'<path d="{rv}" stroke="#4aa3df" stroke-width="6" fill="none"/>'+T(bg(22.4,88.32)[0]+14,bg(22.4,88.3)[1],'HOOGHLY',11,'#1d4f9a','start')
     +T(w-20,h-12,'BAY OF BENGAL',12,'#fff','end')+T(40,40,'WEST BENGAL',13,'#2e5a2e','start')+g+T(w-10,18,'simplified, not to scale',10,'#555','end'))
def MINAR(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-22 0 L-14 -150 H14 L22 0z" fill="#c98b6a"/>'
 +''.join(f'<path d="M{-22+k*1.6:.0f} {-k*30} H{22-k*1.6:.0f}" stroke-width="3"/>' for k in range(1,5))+'<path d="M-14 -150 h28 l-4 -10 h-20z" fill="#b07a5a"/>'
 +''.join(f'<path d="M{-18+j*6} 0 L{-12+j*4} -150" stroke="#8a5a3a" stroke-width="1"/>' for j in range(7))+'<rect x="-5" y="-16" width="10" height="16" fill="#3a2a1a"/></g>')
def MOSQUE(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-90" y="-30" width="180" height="30" fill="#c98b6a"/>'
 +''.join(f'<path d="M{-80+k*20} 0 v-16 a6 6 0 0 1 12 0 v16z" fill="#5a3a2a"/>' for k in range(8))+'<path d="M-90 -30 l10 -6 h160 l10 6" fill="#b07a5a"/></g>')
def DOOR(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-30" y="-70" width="60" height="70" fill="#9a8a7a"/><rect x="-18" y="-58" width="36" height="58" fill="#3a2a1a"/><path d="M-30 -70 h60 M-26 -64 h52" stroke-width="3"/><circle cy="-64" r="4" fill="#e0a800"/></g>'
CHAIN=lambda x,y,n=6: ''.join(f'<ellipse cx="{x+k*16}" cy="{y}" rx="10" ry="6" fill="none" stroke="#e0a800" stroke-width="4" transform="rotate({0 if k%2 else 0} {x+k*16} {y})"/>' for k in range(n))
MOTHER=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-28 60 q-4 -60 28 -70 q32 10 28 70z" fill="#c0392b"/><circle cy="-22" r="12" fill="#f2c79b"/><path d="M-12 -32 h24 l-4 -14 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/><ellipse cx="0" cy="20" rx="16" ry="9" fill="#fff4cd"/><circle cx="-10" cy="16" r="6" fill="#f2c79b"/><path d="M-20 10 q-10 20 20 20 q24 0 18 -22" fill="none" stroke="#f2c79b" stroke-width="6"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A tall brick minaret on a flat Bengal plain at dusk, an old stone doorway, and the faint golden outline of a Goddess with a chain">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/><circle cx="300" cy="70" r="34" fill="#ffd166" opacity=".5"/><rect y="220" width="380" height="48" fill="#5a7a3a"/>'
 +MINAR(110,226,1.2)+DOOR(200,226,.9)+'<g opacity=".55">'+MOTHER(300,140,1.6).replace('#c0392b','#ffd166')+'</g>'+CHAIN(250,236,6)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Śṛṅkhalā Devī</b>, “the Goddess of the chain”: Pīṭha no. 3 of the eighteen'),
 ('Hymn line','<i>pradyumne śṛṅkhalā devī</i>: “Śṛṅkhalā Devī in Pradyumna”'),
 ('Usual site','<b>Pandua</b>, Hooghly district, West Bengal, about 60 km north of Kolkata'),
 ('Body part','Satī’s <b>stomach</b>, in the usual lists'),
 ('Pīṭha name','<b>Bhavatāriṇī Pīṭha</b> in some lists'),
 ('Temple','<b>None standing.</b> Only a <b>38 m minaret</b> and a ruined mosque, both protected monuments'),
 ('Tradition','That a Śṛṅkhalā temple stood here and was destroyed in the Sultanate period; dates and details are disputed'),
 ('Other claims','<b>Gaṅgāsāgar</b>, <b>Śṛṅgeri</b>, a Hooghly Goddess temple, and one list that puts Pradyumna in <b>Gujarat</b>')])
 +talk("A Śakti Pīṭha with no temple?","The only one of the eighteen with nothing standing. This guide is about a Goddess you can't see.")))
pages.append(page('where','WHERE IT IS','Up the Hooghly from Kolkata',fig(560,280,'Simplified map of southern West Bengal with the Hooghly river: Pandua marked in red north of Kolkata, Tribeni on the river, and Gangasagar at the river mouth',
 BMAP([(23.08,88.28,'PANDUA','l','#c0392b'),(22.99,88.40,'Tribeni','r','#bbb'),(22.57,88.36,'Kolkata','r','#bbb'),(21.64,88.08,'Gaṅgāsāgar','r','#ffd166')]))+'''<div class="panel reading">
<p><b>The town.</b> Pandua (often “Choṭo Pāṇḍuyā”, to tell it from the bigger Pandua in Malda) lies on the Grand Trunk Road and the Howrah–Bardhaman railway, inland from the Hooghly river.</p>
<p><b>The landmark.</b> Its tall minaret can be seen from trains and from the road.</p>
<p><b>Old ground.</b> This was the Saptagram–Tribeni region, one of Bengal’s busiest river ports in the Middle Ages.</p>
</div>'''))
pages.append(page('names','HER NAMES','Chain, bond and mother',facts([
 ('Śṛṅkhalā','“Chain” or “fetter”: one reading, the Goddess bound to Śiva; another, the mother bound by love to her newborn'),
 ('Pradyumna','The hymn’s place name; also the name of Kṛṣṇa and Rukmiṇī’s son, the god of love reborn'),
 ('Bhavatāriṇī','“She who carries us across the ocean of becoming”: the pīṭha’s name in some lists'),
 ('Pandua / Pāṇḍuyā','The town; local legend links it to a king <b>Pāṇḍu</b>'),
 ('Melā Talā','“The fairground”: the field around the minaret, where a great fair is held')])
 +talk("A goddess named 'chain'? That sounds scary.","Not a prison chain. A bond, like a mother's to her baby. The chain is love.")))
pages.append(page('pitha','THE PĪṬHA','Where Satī’s stomach fell',fig(560,150,'Shiva carrying Sati across a night sky, a glowing piece falling onto a river plain in Bengal',
 '<rect width="560" height="150" fill="#2a0805"/>'+STAR+SHIVA(140,60,.7)+SATI(162,64,.55,-10)+'<path d="M190 80 q80 10 190 40" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="4 4" fill="none"/><circle cx="382" cy="120" r="6" fill="#ffd166"/><rect y="130" width="560" height="20" fill="#3a5a2a"/><path d="M300 140 q60 -8 120 0 t120 0" stroke="#4aa3df" stroke-width="5" fill="none"/>'+T(440,24,'PRADYUMNA',14,'#ffd166'))+'''<div class="panel reading">
<p><b>The verse.</b> <i>pradyumne śṛṅkhalā devī</i>: third in the hymn, after Laṅkā and Kāñcī, and the first in the north.</p>
<p><b>What fell here.</b> Satī’s <b>stomach</b>, say the usual lists. The image fits her name: the womb-mother, bound to the child.</p>
<p><b>The puzzle.</b> “Pradyumna” is not the name of any town today. Most writers place it at Pandua in Hooghly; nobody has found an old inscription that settles it.</p>
</div>'''))
pages.append(page('today','THE SITE TODAY','A minaret, a mosque, a door',fig(560,220,'A flat field with a tall tapering brick minaret, the long low ruin of a mosque with many arches, and an old stone doorway',
 '<rect width="560" height="220" fill="#fdf1e8"/><rect y="190" width="560" height="30" fill="#7aa86a"/>'+MINAR(110,196,1.15)+MOSQUE(330,196,1.1)+DOOR(500,196,.8)+T(110,214,'MINAR · 38 m',11,'#111')+T(330,214,'BARI MASJID (RUIN)',11,'#111')+T(500,214,'OLD DOORWAY',11,'#111'))+'''<div class="g2">
<div class="card bg-yellow"><h4>🗼 The minar</h4><p>A tapering brick tower about <b>38 m</b> (125 ft) high, with a spiral stair inside, among the tallest in Bengal. It lost some height in a 19th-century earthquake and was repaired by the ASI.</p></div>
<div class="card bg-red"><h4>🕌 The Bari Masjid</h4><p>The “big mosque”, also called the 22-door mosque: a long brick ruin, no longer in use. Both buildings are <b>Monuments of National Importance</b>.</p></div>
</div><div class="panel reading small"><p><b>The doorway.</b> Visitors report an old stone doorway at the site, kept locked, which local people identify as the entrance of a Hindu temple. Its origin has not been published.</p></div>'''))
pages.append(page('history1','HISTORY · THE KING','Rāja Pāṇḍu and the Sultanate',fig(560,150,'A local king’s fort on one side and an approaching army with banners on the other, a well between them',
 '<rect width="560" height="150" fill="#ffe9c4"/><rect x="40" y="70" width="120" height="70" fill="#c98b6a" stroke="#111" stroke-width="2"/>'+''.join(f'<rect x="{40+k*24}" y="58" width="14" height="12" fill="#c98b6a" stroke="#111"/>' for k in range(5))+KING(100,62,.6)
 +'<ellipse cx="280" cy="130" rx="26" ry="8" fill="#4aa3df" stroke="#111" stroke-width="2"/>'+T(280,110,'THE WELL',10,'#1d4f9a')+''.join(person(x,140,'#2a7a4a','#c98b5a',.7)+f'<path d="M{x+6} 104 v-30 l14 6 l-14 6" fill="#2a7a4a" stroke="#111"/>' for x in (400,440,480,520)))+'''<div class="steps">
<div><b>The legend.</b> Local tradition says a Hindu king, <b>Pāṇḍu Rāja</b>, ruled here, with a magic well that brought the dead back to life. A Sufi warrior, <b>Shāh Sufīuddīn</b>, came against him; when the well’s secret was revealed, the king fell.</div>
<div><b>The history.</b> Historians find <b>no evidence</b> of a king named Pāṇḍu, but several minor Hindu rulers held the Saptagram–Pandua area. Sultanate armies reached Tribeni by the late 13th century and Pandua in the early 14th.</div>
<div><b>Shāh Sufīuddīn</b> is remembered as the builder of the Bari Masjid; his dargāh stands nearby.</div>
</div>'''))
pages.append(page('history2','HISTORY · THE MINAR','Two dates, three readings',facts([
 ('Date 1','<b>c. 1340</b>: built by Shāh Sufīuddīn as a victory tower (older local histories and several travel writers)'),
 ('Date 2','<b>1477</b>: built by Sultan <b>Shamsuddīn Yūsuf Shāh</b> of Bengal (cited in recent references)'),
 ('Reading 1','A <b>victory tower</b>, later used to give the call to prayer for the Bari Masjid'),
 ('Reading 2','Built with the mosque <b>in place of the Śṛṅkhalā temple</b>, which was destroyed: the local Hindu tradition, put in print by Partha Sharma (2018)'),
 ('Reading 3','The tower was once the top of a <b>Hindu temple</b>, a Viṣṇu temple, or an observatory, later converted: a view some local historians hold')])
 +'''<div class="panel reading"><p><b>What can be said.</b> No inscription or excavation report we found names a Śṛṅkhalā temple here. Equally, nothing rules one out. The tradition that the Goddess stood at Pandua is old enough that most pīṭha lists name it.</p></div>'''
 +talk("So was the temple here or not?","Nobody can prove it either way. The tradition says yes, the stones are silent, and the books disagree on the date.")))
pages.append(page('rishya','THE LEGEND · ṚṢYAŚṚṄGA','The deer-horned sage',fig(560,160,'A young sage with a small horn on his forehead walking from the plains towards wooded hills, the Goddess’s light going with him',
 '<rect width="560" height="160" fill="#eef6e4"/>'+HILL(460,160,200,100,'#3a7a3a')+HILL(380,160,140,70,'#4a8a4a')+person(200,130,'#ff8c1a','#c98b5a',1.1)+'<path d="M198 86 l4 -14 l4 14" fill="#e2cfa8" stroke="#111"/>'+'<circle cx="250" cy="80" r="14" fill="#ffd166" opacity=".8"/>'+'<path d="M260 100 q80 10 160 -10" stroke="#c9a26b" stroke-width="3" stroke-dasharray="6 5" fill="none"/>'+T(460,30,'ŚṚṄGERI',13,'#2e5a2e'))+'''<div class="steps">
<div><b>The sage.</b> <b>Ṛṣyaśṛṅga</b>, the boy with a deer’s horn on his brow, raised in the forest by his father and pure as a child, is a famous figure of the Rāmāyaṇa and Mahābhārata.</div>
<div><b>A devotee.</b> A story told about this pīṭha makes him a devotee of Śṛṅkhalā, who built her temple where Satī’s stomach fell.</div>
<div><b>To the south.</b> At her command, it says, he went south to the hills that bear his name, <b>Ṛṣyaśṛṅga-giri</b>, the origin of the name <b>Śṛṅgeri</b>, and the Goddess went with him.</div>
</div><div class="panel reading small"><p>This is a popular story; it is not part of Śṛṅgeri’s own temple tradition, which honours Śāradā, and no Śṛṅkhalā shrine is known there.</p></div>'''))
pages.append(page('rukmini','THE LEGEND · RUKMIṆĪ','A mother bound by a vow',fig(560,150,'Krishna and Rukmini pulling a cart carrying the sage Durvasa; Rukmini later alone outside a city gate holding a baby',
 '<rect width="560" height="150" fill="#fff4cd"/><g transform="translate(150 120)" stroke="#111" stroke-width="2"><rect x="-40" y="-30" width="80" height="24" fill="#c98b6a"/><circle cx="-26" r="10" fill="#7a5a2a"/><circle cx="26" r="10" fill="#7a5a2a"/></g>'+person(150,96,'#fff','#c98b5a',.6)+person(60,128,'#3b6fd0','#5b8fe0',.8)+person(90,128,'#c0392b','#f2c79b',.8)
 +'<rect x="380" y="40" width="140" height="100" fill="#e2cfa8" stroke="#111" stroke-width="2"/><rect x="430" y="80" width="40" height="60" fill="#5a3a1a" stroke="#111"/>'+T(450,32,'DVĀRAKĀ',11,'#7a1d12')+MOTHER(330,90,.7))+'''<div class="steps">
<div><b>The test.</b> After their wedding, a story goes, Kṛṣṇa and Rukmiṇī pulled the sage <b>Durvāsas</b> in his cart. Rukmiṇī grew thirsty and Kṛṣṇa gave her water without asking the sage.</div>
<div><b>The curse.</b> Durvāsas ordered the couple to live apart for twelve years. Rukmiṇī stayed outside the city.</div>
<div><b>The child.</b> There she bore <b>Pradyumna</b>, who was stolen as a baby by a demon. The mother bound by a vow and by love for her lost child is read as Śṛṅkhalā, and the son’s name as the hymn’s “Pradyumna”.</div>
</div><div class="panel reading small"><p>The curse story is best known from Dvārakā in Gujarat, where Rukmiṇī’s temple stands outside the city. It may explain why one list places this pīṭha in Gujarat. The link to Śṛṅkhalā is a modern devotional reading.</p></div>'''))
pages.append(page('claims','WHERE IS SHE NOW?','Five answers',fig(560,120,'Five map pins with question marks',
 '<rect width="560" height="120" fill="#fdf1e8"/>'+''.join(f'<path d="M{x} 70 q-14 -20 0 -36 q14 16 0 36z" fill="{c}" stroke="#111" stroke-width="2"/>'+T(x,96,t,11,'#7a1d12') for x,t,c in ((60,'PANDUA','#c0392b'),(170,'GAṄGĀSĀGAR','#ffd166'),(280,'ŚṚṄGERI','#ffd166'),(390,'HOOGHLY','#ffd166'),(500,'GUJARAT','#ffd166'))))+facts([
 ('Pandua','The usual identification, on the strength of local tradition and the stone remains'),
 ('Gaṅgāsāgar','Some place the Goddess at the mouth of the Hooghly, at Sāgar island'),
 ('Śṛṅgeri','The Ṛṣyaśṛṅga story says she went south with the sage'),
 ('A Hooghly temple','One writer suggests a Goddess temple elsewhere in the district, such as <b>Haṃseśvarī</b> at Bansberia'),
 ('Gujarat','At least one published list gives “Pradyumna (Gujarat)”')])
 +talk("Five places for one Goddess?","When a temple vanishes, the Goddess gets claimed everywhere. That's a kind of love too.")))
pages.append(page('mela','THE FAIR','A field that still gathers people',fig(560,170,'A crowded fairground around the minaret with stalls, a giant wheel and families',
 '<rect width="560" height="170" fill="#ffe9c4"/><rect y="140" width="560" height="30" fill="#7aa86a"/>'+MINAR(80,146,.75)+''.join(f'<rect x="{x}" y="100" width="44" height="40" fill="{c}" stroke="#111" stroke-width="2"/><path d="M{x-4} 100 l26 -16 l26 16z" fill="#c0392b" stroke="#111"/>' for x,c in ((160,'#fff4cd'),(230,'#dcecff'),(300,'#fde4e4')))
 +'<circle cx="440" cy="80" r="46" fill="none" stroke="#111" stroke-width="3"/>'+''.join(f'<path d="M440 80 L{440+46*__import__("math").cos(k*0.785):.0f} {80+46*__import__("math").sin(k*0.785):.0f}" stroke="#111"/>' for k in range(8))+'<path d="M420 140 L440 80 L460 140" stroke="#111" stroke-width="3" fill="none"/>'+'')+'''<div class="panel reading">
<p><b>Melā Talā.</b> Every year in the Bengali month of <b>Māgh</b> (around February), a great fair is held on the field around the minaret. It runs for about a month.</p>
<p><b>Everyone comes.</b> Hindus and Muslims from the district come together for it: one of the few things on this ground that everyone shares.</p>
</div>'''+talk("A month-long fair on the old temple ground?","Whatever stood here, people never stopped gathering. The fair is the site's living memory.")))
pages.append(page('around','AROUND PANDUA','The old river country',facts([
 ('Tribeni','“Three braids”, where the Hooghly splits: a sacred bathing place, with one of Bengal’s oldest mosques'),
 ('Saptagram','The great medieval river port of the region, later silted up'),
 ('Mahanad','A village with an old Kālī temple, linked to the Pāṇḍu Rāja legend'),
 ('Bansberia','The <b>Haṃseśvarī</b> temple, a striking Tantric temple of the early 19th century'),
 ('Gaṅgāsāgar','The river’s mouth, with the Kapila Muni temple and a famous winter bathing festival')])
 +talk("Lots of history for a quiet bit of Bengal!","River ports made kings, and kings made temples and mosques. The Hooghly carried all of it.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Śṛṅkhalā','Chain, fetter, bond'),('Pradyumna','Son of Kṛṣṇa and Rukmiṇī; the hymn’s place name'),('Bhavatāriṇī','She who carries across the sea of existence'),
 ('Minar','A tower, often beside a mosque'),('Masjid','Mosque'),('Dargāh','The tomb-shrine of a Sufi'),('Melā','Fair'),('Māgh','Bengali month, January–February'),
 ('Ṛṣyaśṛṅga','The deer-horned sage'),('ASI','Archaeological Survey of India')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Goddess.</b> Śṛṅkhalā, the Goddess of the bond, third in the hymn; Satī’s stomach is said to have fallen here.</div>
<div><b>The place.</b> Pandua in Hooghly, by most accounts; “Pradyumna” is not a town name today.</div>
<div><b>What stands.</b> A 38 m minaret, a ruined mosque, an old doorway; no temple.</div>
<div><b>The history.</b> Disputed: two dates for the minar, and a temple tradition with no inscription to settle it.</div>
<div><b>The legends.</b> Ṛṣyaśṛṅga took her south; Rukmiṇī, the mother bound by a vow; four other places that claim her.</div>
</div>'''+talk("One line to remember?","The one seat of the eighteen with no temple. She's remembered without a building.")+'<div class="key">The third seat of the Mother: <b>Śṛṅkhalā of Pradyumna</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>The site:</b> Wikipedia, “Pandua, Hooghly”: Pāṇḍu Rāja legend and lack of evidence; minor Hindu rulers; Sultanate arrival; Shāh Sufīuddīn and the Bari Masjid (14th c.); minar 38 m, 1477, Shamsuddīn Yūsuf Shāh; the claim that minar and mosque replaced the Śṛṅkhalā temple (citing Partha Sharma, <i>The Forgotten Shivalinga of the Sati Shaktipeeths</i>, 2018); Monuments of National Importance. Rangan Datta (rangan-datta.info): the 1340 date and the view that the minar was part of a Viṣṇu temple. Ghumakkar.com: earthquake damage and ASI repair; the stone door; Melā Talā in Māgh. Wikipedia, “Shakta pithas” (stomach; Bhavatāriṇī Pīṭha).</p>
<p><b>Legends and claims:</b> behindeverytemple.org and templesinindiainfo.com (name meanings; Ṛṣyaśṛṅga; Rukmiṇī; Gaṅgāsāgar, Śṛṅgeri and Haṃseśvarī claims; the fair). hindupedia.com (Pradyumna listed under Gujarat). hindu-blog.com and sringeri.net (Śṛṅgeri’s name from Ṛṣyaśṛṅga).</p>
<p><b>Sources differ:</b> the minar’s date and builder (c. 1340 or 1477). <b>Not verified:</b> that a Śṛṅkhalā temple stood at Pandua or was replaced by the mosque; the stone doorway’s origin; the Ṛṣyaśṛṅga and Rukmiṇī links (devotional stories). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('pitha','The Pīṭha'),('today','The Site Today'),('history1','History · The King'),('history2','History · The Minar'),('rishya','Legend · Ṛṣyaśṛṅga'),('rukmini','Legend · Rukmiṇī'),
 ('claims','Where Is She Now?'),('mela','The Fair'),('around','Around Pandua'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 3 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚṚṄKHALĀ DEVĪ</h1>
  <div class="series">PRADYUMNA · PANDUA · A REFERENCE GUIDE</div>
  <div class="tag">The seat with no temple</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>The hymn’s third name is the hardest to visit, because there is nothing to visit: <i>pradyumne śṛṅkhalā devī</i>.</p>
    <p>Most writers place her at <b>Pandua</b>, a town in Bengal’s Hooghly district, where a tall brick minaret and a ruined mosque stand on an open field. Tradition says her temple stood there; historians argue about what really happened.</p>
    <p>This guide sets out what is known, what is told, and where else people look for the Goddess of the chain.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā Śṛṅkhalā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("How do you write a guide about a temple that isn't there?","Carefully. Tell the story, show the stones, and say plainly what nobody knows.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Shrinkhala.html','w').write(head+b+tail())
print('ok',len(pages))
