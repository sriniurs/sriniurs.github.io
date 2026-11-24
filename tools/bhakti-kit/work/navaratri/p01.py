from pages import *
from fig import *
import math
i=0
rims=['#c0392b']*3+['#e0a800']*3+['#ffffff']*3
arc=''.join(g(70+k*37.5,70-int(30*math.sin(math.pi*k/8)),.95,lamp(rims[k])) for k in range(9))
COV=covart('Nine small oil lamps in an arc, three with red rims, three gold and three white, above a copper kalaśa crowned with mango leaves and a coconut, set on a pink lotus, with a golden trident on the left and a vīṇā on the right',
  arc+g(66,170,1.2,trident())+g(372,168,1.05,vina())+g(220,202,1.3,lotus())+g(220,186,1.15,kalasha()))
# figures
def timeline():
    o=['<path d="M14 150 H546" stroke="#111" stroke-width="3"/>']
    grp=[('DURGĀ','NIGHTS 1–3','#c0392b','#fde4e4',g(91,122,.68,trident())),('LAKṢMĪ','NIGHTS 4–6','#e0a800','#fff3cf',g(241,96,1.05,lotus())),('SARASVATĪ','NIGHTS 7–9','#ffffff','#eef2fb',g(388,98,.72,vina()))]
    for n,(nm,nt,col,bg,emb) in enumerate(grp):
        x0=22+n*150
        o.append(f'<rect x="{x0}" y="22" width="138" height="160" rx="10" fill="{bg}" stroke="#111" stroke-width="2"/>'+emb)
        o+= [g(x0+30+k*39,146,.9,lamp(col)) for k in range(3)]
        o.append(txt(x0+69,168,nm,17)+lab(x0+69,40,nt))
    o.append(g(496,150,1.45,flag())+txt(508,168,'DAY 10',17)+lab(508,184,'VIJAYADAŚAMĪ',10))
    return svg(560,200,'A timeline of the festival: nine lamps in three groups, under a trident for Durgā, a lotus for Lakṣmī and a vīṇā for Sarasvatī, and on the tenth day a saffron victory flag',''.join(o))
def wheel():
    o='<circle cx="280" cy="110" r="84" fill="#fff" stroke="#111" stroke-width="3"/><path d="M280 26 V194 M196 110 H364" stroke="#111" stroke-width="2"/>'
    q=[(330,70,'VASANTA','Caitra · spring','#a7c957'),(330,160,'ĀṢĀḌHA (gupta)','monsoon','#8fb8de'),(230,160,'ŚĀRADĀ','Āśvina · autumn','#e0a23a'),(230,70,'MĀGHA (gupta)','winter','#cfd8e6')]
    for x,y,a,b,c in q: o+=f'<circle cx="{x}" cy="{y}" r="30" fill="{c}" stroke="#111" stroke-width="2"/>'+lab(x,y-2,a,9.5)+lab(x,y+12,b,8.5)
    o+='<circle cx="230" cy="160" r="38" fill="none" stroke="#c0392b" stroke-width="4" stroke-dasharray="6 4"/>'
    o+=g(70,150,1,sun(20))+g(490,140,1,moon())+txt(70,196,'THE YEAR',15)+txt(490,196,'FOUR GATES',15)
    return svg(560,215,'A year wheel with the four Navarātris: Vasanta in Caitra (spring), Āṣāḍha Gupta (monsoon), Śāradā in Āśvina (autumn, circled as the great one) and Māgha Gupta (winter)',o)
def autumn():
    o=ground(560,200,150,'#e8d9a8')+''.join(g(x,150,.7,'<path d="M0 0 v-40" stroke="#c9a24a" stroke-width="3"/><ellipse cy="-46" rx="5" ry="12" fill="#e0b84a"/>') for x in range(30,250,18))
    o+=g(120,40,1,sun(18))+'<path d="M300 60 q20 -20 40 0 q20 -10 30 6 q-40 4 -70 -6z" fill="#fff" stroke="#111" stroke-width="2"/>'
    o+=g(440,150,1,devi(items=('trident','sword','lotus','abhaya')))+g(380,150,.8,beast('lion'),flip=True)
    o+=lab(140,190,'harvest in the fields',11)+lab(440,190,'the Mother comes home',11)
    return svg(560,200,'Autumn: ripe grain standing in the fields under a clear sky, and the Devī with her lion arriving',o)
def home():
    o=ground(560,200,160,'#e9d6c0')+g(90,160,1,kalasha())+g(160,150,.8,lamp('#c0392b'))
    o+=g(240,160,1,steps(5,150,100))+''.join(g(200+k*20,160-((k%5)+1)*20+0,1,'') for k in range(1))
    for r in range(5):
        for c in range(4-r//2): o+=g(190+c*30+r*6,160-r*20,.55,doll(['#c0392b','#1d6fb8','#2a9d6f','#e0a800'][c%4],crown=(r==4)))
    o+=g(420,160,1,person('#c0392b',seat=True))+g(420,118,.8,book())+g(500,160,.9,person('#2a9d6f'))
    o+=lab(90,190,'kalaśa')+lab(240,190,'gombe (dolls)')+lab(420,190,'reading the Devī Māhātmya')+lab(505,190,'visitors')
    return svg(560,200,'A Karnataka home at Navarātri: a kalaśa and lamp, doll steps, a devotee reading the Devī Māhātmya, and visitors arriving',o)
def india():
    o='<path d="M190 20 l60 -6 l40 20 l10 30 l60 10 l30 30 l-30 20 l-40 10 l-30 40 l-30 50 l-20 6 l-20 -40 l-30 -40 l-40 -20 l-10 -30 l10 -30 l20 -20z" fill="#f3e3c3" stroke="#111" stroke-width="2.5"/>'
    pts=[(345,100,'Bengal: Durgā Pūjā'),(160,105,'Gujarat: Garbā'),(240,60,'North: Rāmlīlā'),(225,35,'Kullu Dasarā'),(250,175,'Mysuru: Dasarā'),(280,150,'Golu · Bommala Koluvu'),(255,205,'Kerala: Vidyārambha')]
    for x,y,t in pts: o+=f'<circle cx="{x}" cy="{y}" r="6" fill="#c0392b" stroke="#111" stroke-width="2"/>'+lab(x+(10 if x>200 else -10),y+4,t,10.5).replace('text-anchor="middle"','text-anchor="'+('start' if x>200 else 'end')+'"')
    o+=lab(480,215,'simplified, not to scale',9)
    return svg(560,225,'A simplified map of India marking how regions keep the festival: Durgā Pūjā in Bengal, Garbā in Gujarat, Rāmlīlā in the north, Kullu Dasarā, the Mysuru Dasarā, doll displays in the south and Vidyārambha in Kerala',o)
def tenth():
    o=ground(560,200,160)+g(90,160,1.1,shami())+g(250,160,1,elephant())+g(400,160,.9,effigy())+g(400,166,.9,flames())+g(500,160,1,flag())
    o+=lab(90,190,'śamī (banni) tree')+lab(250,190,'Jambū Savāri')+lab(400,190,'Rāvaṇa burnt')+lab(500,190,'victory')
    return svg(560,200,'The tenth day: the śamī tree, an elephant carrying the golden howdah, a ten-headed Rāvaṇa effigy in flames, and a victory flag',o)
def series_fig():
    o=''
    for k in range(16):
        x=30+(k%8)*68; y=30+(k//8)*80
        col='#c0392b' if 3<=k<=11 else '#8e1f17'
        o+=f'<rect x="{x-24}" y="{y-20}" width="52" height="58" rx="8" fill="{"#fde4e4" if 3<=k<=11 else "#fff3cf"}" stroke="#111" stroke-width="2"/>'+txt(x+2,y+12,str(k+1),26,fill=col)
    o+=lab(275,190,'Parts 4–12 (pink): the nine Durgās, one per night',11)
    return svg(560,200,'Sixteen numbered tiles for the sixteen parts of the series, with parts four to twelve highlighted as the nine Durgās',o)
def kavaca_fig():
    o=''.join(g(22+k*22.5,120,.42,devi(sari=['#f4f1ea','#ff8c1a','#c0392b','#e0a800','#2a9d6f','#c0392b','#3a3a40','#ffffff','#7a3fa0'][k],items=('lotus',),third_eye=False)) for k in range(9))
    return svg(220,160,'Nine small goddess figures in a row, the nine Durgās named in the Devī Kavaca',o,cls='')
pages=[]
pages.append(foreword(i,[
 'Every autumn, for nine nights, homes and temples across India turn to the Goddess. In Mysuru the city lights up, the doll steps come out, and on the tenth day Cāmuṇḍeśvarī rides through the streets on an elephant. This is <b>Navarātri</b>, and in Karnataka its tenth day gives the whole season its name, <b>Dasarā</b>.',
 'This series walks through it in sixteen parts: the story behind the festival, how the nine nights begin, the <b>nine Durgās</b> one night at a time, the great days at the end, and the <b>Mysuru Dasarā</b>. It builds on our <a href="/devi/devi-mahatmya/">Devī Māhātmya</a> series, which tells the scripture verse by verse.',
 'This first part is the map: what the name means, the four Navarātris of the year, how the nights are counted, and how India keeps them.'],
 [('z','Is Navarātri one festival or many?'),('b','One festival with many faces. Bengal, Gujarat, Mysuru and Vārāṇasī all keep the same nine nights, and each does it in its own way. We will meet all of them.')]))
pages.append(glance([('Name','Navarātri, “nine nights”; Dasarā or Vijayadaśamī for the tenth day'),('When','From the first day of the bright fortnight of Āśvina (Śāradā Navarātri, the great one); three other Navarātris in the year'),('Length','Nine nights and a tenth day of victory'),('Worshipped','The Devī: as Durgā, Lakṣmī and Sarasvatī, or as the nine Durgās'),('Core text','The Devī Māhātmya (Durgā Saptaśatī), recited through the nights'),('In Karnataka','The Nāḍa Habba: doll steps, Sarasvatī Pūjā, Āyudha Pūjā, the Jambū Savāri in Mysuru'),('Closes with','Vijayadaśamī: śamī worship, new beginnings, victory')],
  svg(560,150,'The festival in one strip: a lamp for the nine nights, the Devī with trident and lotus, and a victory flag for the tenth day',g(110,135,1.2,lamp('#c0392b'))+g(280,140,1,devi(items=('trident','lotus','sword','abhaya')))+g(460,140,1,flag())+lab(110,146,'9 nights')+lab(470,146,'day 10')),
  [('z','So the tenth day isn’t one of the nine nights?'),('b','Right. Nine nights of worship, then a tenth day when the victory is celebrated. That is why you will hear both names, Navarātri and Dasarā.')]))
pages.append(reading('three','NINE NIGHTS, THREE GODDESSES','Why nine, why these three, and why the tenth day means victory',timeline(),[
 '<b>The name.</b> <b>Navarātri</b> is simply <i>nava</i> “nine” and <i>rātri</i> “night”: nine nights given to the Goddess. A tenth day closes it, <b>Vijayadaśamī</b>, “the victorious tenth”. In Karnataka the whole season is called <b>Dasarā</b> (from <i>Daśaharā</i>, a name tied to that tenth day), and in Mysuru it is the <b>Nāḍa Habba</b>, “the festival of the land”.',
 '<b>Three by three.</b> In South India the nine nights are often counted in threes: the first three for <b>Durgā</b> (often worshipped as Kālī), the next three for <b>Lakṣmī</b>, the last three for <b>Sarasvatī</b>. Many read this as a path for the seeker: first the Mother clears away what harms, then she grows what is good, then she gives knowledge.',
 '<b>The scripture behind it.</b> The count mirrors the three stories of the <a href="/devi/devi-mahatmya/">Devī Māhātmya</a>, presided over by Mahākālī, Mahālakṣmī and Mahāsarasvatī. The middle story, the slaying of Mahiṣāsura, is the one most homes connect with Navarātri; it gets its own part, '+link(1,'Part 2')+'.',
 '<b>Traditions differ.</b> Across the north, each night instead belongs to one of the <b>nine Durgās</b> (Navadurgā), from Śailaputrī on the first night to Siddhidātrī on the ninth. Bengal gathers its worship into the last days as Durgā Pūjā. These are not rival answers: they are different ways of counting the faces of one Goddess.'],
 [('z','So which is right: three goddesses, or nine Durgās?'),('b','Both. The Devī is one; three and nine are two ways of counting her. A Mysuru home keeps the three-by-three rhythm and still bows to Cāmuṇḍī, who is Durgā herself, every day of the festival.')],
 'Nine nights, counted three by three: <b>Durgā clears, Lakṣmī grows, Sarasvatī teaches</b>. The tenth day is victory.'))
pages.append(reading('four','FOUR NAVARĀTRIS IN A YEAR','Spring, monsoon, autumn and winter: four doors into the Goddess',wheel(),[
 '<b>Four seasons, four Navarātris.</b> The tradition speaks of four Navarātris, each beginning on the first day (<i>pratipadā</i>) of a bright fortnight: <b>Vasanta Navarātri</b> in Caitra (spring), <b>Āṣāḍha Navarātri</b> at the start of the monsoon, <b>Śāradā Navarātri</b> in Āśvina (autumn) and <b>Māgha Navarātri</b> in winter.',
 '<b>The two public ones.</b> Vasanta Navarātri, in spring, ends on the ninth day with <a href="/festivals/rama-navami/">Rāma Navamī</a> in many regions, and its first day is the new year of the Deccan, <a href="/festivals/ugadi/">Ugādi</a>. Śāradā Navarātri, in autumn, is the great festival that this whole series follows.',
 '<b>The two “hidden” ones.</b> The Āṣāḍha and Māgha Navarātris are called <b>Gupta</b>, “hidden”, because they are kept quietly, mostly by those doing personal sādhana, rather than with public celebration. In Śrīvidyā they are linked with <a href="/srividya/deities/varahi/">Vārāhī</a> and <a href="/srividya/deities/rajashyamala/">Rājaśyāmalā</a>, the two great ministers of Lalitā.',
 '<b>Why autumn wins.</b> The autumn festival is called <i>Śāradā</i> from <i>śarad</i>, autumn. It comes after the rains, when the harvest is ripening and the year turns toward the cool season. Texts and teachers differ on which Navarātri is the most important for which age; what is not in doubt is that the autumn one is the one India celebrates together.'],
 [('z','If there are four, why does everyone only talk about one?'),('b','Because the autumn one became the public festival: kings, temples and towns gathered around it. The others stayed quieter, kept at home or by people in a vow.')],
 'Four Navarātris a year; <b>Śāradā</b>, in autumn, is the great one.'))
pages.append(reading('autumn','WHY THE GODDESS COMES IN AUTUMN','The harvest, the season and the story',autumn(),[
 '<b>A harvest festival.</b> In many regions Śāradā Navarātri falls just as the monsoon crop is ripening. Grain is sown in a pot on the first day and grows green by the ninth; tools of work are worshipped on the ninth day; the tenth day starts new work. The festival sits in the farming year as naturally as it sits in the calendar of the Goddess.',
 '<b>The Goddess as Mother coming home.</b> In Bengal and much of the east, the Devī is welcomed as Umā, the married daughter visiting her parents’ home with her children, and sent off again on the tenth day. The mood is a family reunion as much as a war story.',
 '<b>Rāma’s autumn worship.</b> A tradition, best known from the Bengali Rāmāyaṇa of Kṛttivāsa, says that Rāma worshipped Durgā out of season, in autumn, before his battle with Rāvaṇa. That is why Bengal calls its Durgā Pūjā <i>akāla bodhana</i>, “the untimely awakening”. Vālmīki’s Rāmāyaṇa does not tell this story; it belongs to later regional tradition.',
 '<b>The victory.</b> Whatever the region, the festival ends in victory: the Devī over Mahiṣa, Rāma over Rāvaṇa, the Pāṇḍavas taking back their weapons. Each story gets its own page later in the series.'],
 [('z','A war story and a homecoming at the same time?'),('b','Yes. A mother fights for her children and then comes home to them. India keeps both moods in the same nine nights.')],
 'Autumn brings the harvest, the homecoming daughter, and the stories of victory.'))
pages.append(verse('v1','DEVĪ KAVACA 3–5','THE NINE DURGĀS, NAMED BY BRAHMĀ',[
 'prathamaṃ śailaputrī ca dvitīyaṃ brahmacāriṇī .','tṛtīyaṃ candraghaṇṭeti kūṣmāṇḍeti caturthakam .. 3 ..',
 'pañcamaṃ skandamāteti ṣaṣṭhaṃ kātyāyanīti ca .','saptamaṃ kālarātrīti mahāgaurīti cāṣṭamam .. 4 ..',
 'navamaṃ siddhidātrī ca navadurgāḥ prakīrtitāḥ .','uktānyetāni nāmāni brahmaṇaiva mahātmanā .. 5 ..'],kavaca_fig(),
 'First is Śailaputrī, second Brahmacāriṇī, third the one called Candraghaṇṭā, fourth Kūṣmāṇḍā. Fifth is Skandamātā, sixth Kātyāyanī, seventh Kālarātri and eighth Mahāgaurī. Ninth is Siddhidātrī. These are proclaimed as the nine Durgās; these names were spoken by great-souled Brahmā himself.',
 [('prathamam … navamam','first … ninth'),('navadurgāḥ','the nine Durgās'),('prakīrtitāḥ','are proclaimed'),('brahmaṇā','by Brahmā'),('mahātmanā','great-souled')],
 '<b>Where the list comes from.</b> These three verses are from the <b>Devī Kavaca</b>, the “armour” hymn traditionally recited before the Devī Māhātmya. Our <a href="/devi/devi-mahatmya/part-1/">Devī Māhātmya Part 1</a> reads them verse by verse. They are the oldest common source for the order of the nine Durgās used on the nine nights, and Parts 4 to 12 follow this order exactly.',
 None,
 'Śailaputrī to Siddhidātrī: <b>the order of the nine nights</b>, straight from the Devī Kavaca.',
 'Text as in the standard Devī Kavaca printed with the Durgā Saptaśatī (shlokam.org transliteration), verses 3–5.'))
pages.append(reading('home','HOW A HOME KEEPS THE NINE NIGHTS','Lamp, kalaśa, reading and visitors',home(),[
 '<b>The first morning.</b> Many homes install a <b>kalaśa</b>, a water pot crowned with mango leaves and a coconut, as the seat of the Goddess, and light a lamp that some keep burning through all nine nights. This is <b>Ghaṭasthāpana</b>, the subject of '+link(2,'Part 3')+'.',
 '<b>Reading and chanting.</b> The <a href="/devi/devi-mahatmya/">Devī Māhātmya</a> is read through the nine days, in full or in parts. Others chant the <a href="/srividya/lalita-sahasranama/">Lalitā Sahasranāma</a> or the <a href="/devi/ya-devi-sarvabhuteshu/">Yā Devī Sarvabhūteṣu</a> verses daily.',
 '<b>The dolls.</b> In Karnataka and Tamil Nadu, the doll steps go up on the first day: gods at the top, the paṭṭada gombe (the royal doll couple), village scenes below. Friends visit in the evenings to see them. This is '+link(12,'Part 13, Gombe Habba')+'.',
 '<b>Fasting and food.</b> Some fast through the nine days, some on particular days, some not at all; customs differ by family and region. Sweets and offerings change from night to night in many homes.'],
 [('z','Do we have to do all of this?'),('b','No. Each family keeps what it inherited. A lamp, a prayer and a story each night is already Navarātri.')],
 'Lamp, kalaśa, a reading, the dolls and visitors: <b>the rhythm of the nine nights at home</b>.'))
pages.append(reading('india','HOW INDIA KEEPS IT','One festival, many regional forms',india(),[
 '<b>East.</b> In Bengal, Odisha and Assam the last days become <b>Durgā Pūjā</b>: the Goddess with her children in a clay image in a pandal, worshipped from the sixth to the ninth day and taken to the river on the tenth.',
 '<b>West.</b> In Gujarat the nights are danced: <b>garbā</b> around a lamp in a pierced pot, and <b>dāṇḍiyā</b> with sticks, in praise of the Mother.',
 '<b>North.</b> In much of the north the nights belong to the nine Durgās, and <b>Rāmlīlā</b>, the staged Rāmāyaṇa, ends on the tenth day with Rāvaṇa’s effigy burnt. In Kullu the Dasarā begins on Vijayadaśamī itself and gathers the valley’s village deities.',
 '<b>South.</b> In Karnataka, Tamil Nadu and Andhra the dolls come out (<b>Gombe</b>, <b>Golu</b>, <b>Bommala Koluvu</b>); Sarasvatī Pūjā and Āyudha Pūjā mark the end; Kerala begins children’s learning with <b>Vidyārambha</b>. And in Mysuru the whole city keeps the royal <b>Dasarā</b>, '+link(15,'Part 16')+'.'],
 [('z','Which one is the real Navarātri?'),('b','All of them. The nine nights are the same; the way each region shows its love is different.')],
 'Bengal’s pandals, Gujarat’s dances, the north’s Rāmlīlā, the south’s dolls: <b>one Goddess, many festivals</b>.'))
pages.append(reading('tenth','THE TENTH DAY','Vijayadaśamī, the day of victory',tenth(),[
 '<b>A day of victory.</b> <b>Vijayadaśamī</b>, the tenth day of the bright fortnight of Āśvina, celebrates victory: the Devī’s over Mahiṣa, Rāma’s over Rāvaṇa, and good beginnings over hesitation.',
 '<b>The śamī tree.</b> In Karnataka, Andhra and Maharashtra the <b>śamī</b> tree (<i>banni</i> in Kannada) is worshipped, remembering the Pāṇḍavas, who hid their weapons in a śamī during their year in disguise. Its leaves are exchanged as “gold”.',
 '<b>New beginnings.</b> It is counted among the most auspicious days of the year to begin learning, a business or a journey. Kerala brings small children to write their first letters; Mysuru carries the Goddess to the banni tree on an elephant.',
 '<b>Its own part.</b> '+link(14,'Part 15')+' covers Mahānavamī and Vijayadaśamī in full, and '+link(15,'Part 16')+' the Mysuru procession.'],
 [('z','Why start things on that day?'),('b','Because it is the day victory was won. You begin under the sign of success.')],
 'Vijayadaśamī: <b>victory remembered, the śamī worshipped, new work begun</b>.'))
pages.append(cards('series','THE SIXTEEN PARTS','A map of this series',series_fig(),[
 ('🗺️','Foundations (1–3)','This overview; '+link(1,'the story of Mahiṣāsura')+'; '+link(2,'starting the nine nights')+' with the kalaśa and lamp.'),
 ('🌸','The nine Durgās (4–12)',link(3,'Śailaputrī')+', '+link(4,'Brahmacāriṇī')+', '+link(5,'Candraghaṇṭā')+', '+link(6,'Kūṣmāṇḍā')+', '+link(7,'Skandamātā')+', '+link(8,'Kātyāyanī')+', '+link(9,'Kālarātri')+', '+link(10,'Mahāgaurī')+', '+link(11,'Siddhidātrī')+'.'),
 ('🎎','The great days (13–15)',link(12,'Gombe Habba')+'; '+link(13,'Sarasvatī Pūjā and Durgāṣṭamī')+'; '+link(14,'Mahānavamī and Vijayadaśamī')+'.'),
 ('🐘','Mysuru (16)',link(15,'The Mysuru Dasarā')+': Vijayanagara, the Woḍeyars, the palace, Cāmuṇḍī Hill and the Jambū Savāri, with how the rest of India keeps the day.')],
 [('z','Can I read the nine Durgā parts on their own nights?'),('b','That is exactly how they are built: one part per night, each with her verse, her story and her meaning.')],
 'Three foundations, nine Durgās, three great days and the <b>Mysuru Dasarā</b>.'))
pages.append(end(i,['<b>Name.</b> Navarātri, nine nights; Vijayadaśamī or Dasarā, the tenth day.','<b>Four a year.</b> Vasanta, Āṣāḍha, Śāradā and Māgha; Śāradā, in autumn, is the great one.','<b>Counting.</b> Three by three (Durgā, Lakṣmī, Sarasvatī) or nine Durgās, one per night.','<b>At home.</b> Kalaśa and lamp, the Devī Māhātmya, the doll steps.','<b>Across India.</b> Durgā Pūjā, garbā, Rāmlīlā, Golu and the Mysuru Dasarā.'],
 'Part 2 tells the story behind it all: how the gods’ anger became a Goddess, and how she fought the buffalo demon Mahiṣa.','Navarātri, an overview'))
pages.append(sources([('Festival:','Wikipedia, “Navaratri” (four seasonal Navarātris; Śāradā as the most celebrated; Gupta Navarātris; regional forms). Drik Panchang, “Navratri” (South Indian three-by-three division). Organiser, “Meaning and Multiplicity of Navaratri” (Durgā, Lakṣmī, Sarasvatī reading).'),
 ('Verse:','Devī Kavaca 3–5 as printed with the Durgā Saptaśatī; transliteration from shlokam.org.'),('Regions:','Wikipedia, “Golu (festival)”, “Vijayadashami”, “Mysore Dasara”.')],
 'which Navarātri is “most important” in which age (texts differ); the Bengal tradition of Rāma’s autumn worship (from Kṛttivāsa, not Vālmīki); the derivation of “Dasarā”.',
 'Devī Kavaca numbered as in the common printed Durgā Saptaśatī.'))
build(i,'PART 1 OF 16 · NINE NIGHTS · ONE VICTORY',COV,'Nine lamps, one kalaśa, three goddesses',
 'First <b>what Navarātri is</b>: the name, the four Navarātris and how the nights are counted. Then a map of <b>the sixteen parts</b>, from the story to the nine Durgās to the <b>Mysuru Dasarā</b>.',
 'Navarātri explained: the name, the four Navarātris of the year, the nine nights counted three by three for Durgā, Lakṣmī and Sarasvatī, the nine Durgās of the Devī Kavaca, how India keeps the festival, and Vijayadaśamī. Part 1 of the illustrated Navarātri and Dasarā series.',pages)
print('p01 ok')
