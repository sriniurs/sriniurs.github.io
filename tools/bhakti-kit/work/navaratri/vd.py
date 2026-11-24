import pages as PG
from pages import *
from pages import foreword,glance,reading,story,cards,end,sources,build,covart
from fx import *
from fig import devi
PG.configure('/temples-of-india/',[('vaishno-devi','Vaiṣṇo Devī','The Mother in the Trikūṭa Cave')],'red','Temples of India','Devī','Temples of India')
PG.CFG['backurl']='/temples-of-india/'; PG.CFG['backname']='Temples of India'
PG.OUT='outd/vd/'
L=lambda u,t: f'<a href="{u}">{t}</a>'
RED='#c0392b'
def tri(x=280,y=170,s=1,c='#8a9a7a'):
    return g(x,y,s,f'<path d="M-200 0 L-120 -90 L-60 -40 L0 -130 L60 -40 L120 -100 L200 0z" fill="{c}" stroke="#111" stroke-width="2"/><path d="M0 -130 L18 -104 L-18 -104z M-120 -90 L-106 -70 L-134 -70z M120 -100 L134 -80 L106 -80z" fill="#fff"/>')
def cavemouth(x=280,y=170,s=1):
    return g(x,y,s,'<path d="M-90 0 Q-80 -110 0 -116 Q80 -110 90 0z" fill="#8a7a6a" stroke="#111" stroke-width="2"/><path d="M-34 0 Q-30 -60 0 -64 Q30 -60 34 0z" fill="#2a2018"/>')
def pindis(x=0,y=0,s=1):
    return g(x,y,s,'<path d="M-90 0 Q-90 -60 -60 -70 H60 Q90 -60 90 0z" fill="#7a6a5a" stroke="#111" stroke-width="2"/>'
      '<ellipse cx="-44" cy="-76" rx="20" ry="16" fill="#1b1b1b" stroke="#111" stroke-width="2"/>'
      '<ellipse cx="0" cy="-80" rx="20" ry="16" fill="#c9762a" stroke="#111" stroke-width="2"/>'
      '<ellipse cx="44" cy="-76" rx="20" ry="16" fill="#f1eee2" stroke="#111" stroke-width="2"/>'
      '<path d="M-60 -98 q20 -12 44 0 M-22 -102 q22 -12 44 0 M24 -98 q20 -12 40 0" stroke="#c0392b" stroke-width="5" fill="none"/>')
def mata(fierce=False,s=1):
    return devi(items=('sword','trident','discus','conch','lotus','abhaya') if not fierce else ('sword','trident','discus','mace'),fierce=fierce,third_eye=True)
def bhairon(): return demon('#4a3a5a')
def ram(): return g(0,0,1,god('#3a6ab8'))+g(22,-50,.6,'<path d="M0 0 q14 -30 0 -60" fill="none" stroke="#6a4a2a" stroke-width="5"/>')
def mapsv(hi=None,h=220):
    pts=[('Katra',70,190,'base town'),('Bāṇgaṅgā',140,170,'arrow stream'),('Caraṇ Pādukā',205,150,'footprints'),('Ardhkuwārī',285,118,'halfway · Garbh Jūn'),('Sāñjhī Chhat',365,82,'ridge'),('Bhavan',445,70,'the holy cave'),('Bhairon',505,38,'his temple')]
    o=f'<rect width="560" height="{h}" fill="#f6efe6"/>'+tri(300,h-6,1.25,'#c9d1bf')
    o+='<path d="M70 190 L140 170 L205 150 L285 118 L365 82 L445 70" fill="none" stroke="#c0392b" stroke-width="5" stroke-dasharray="10 7"/><path d="M445 70 L505 38" fill="none" stroke="#6a4a2a" stroke-width="4" stroke-dasharray="6 5"/>'
    for n,x,y,t in pts:
        big=n==hi
        o+=f'<circle cx="{x}" cy="{y}" r="{10 if big else 6}" fill="{RED if big else "#e0a800"}" stroke="#111" stroke-width="1.5"/>'+lab(x,y+20 if y<180 else y-14,n,12 if big else 11)+lab(x,y+33 if y<180 else y-27,t,9)
    o+=lab(470,h-8,'simplified, not to scale',10)
    return svg(560,h,'Schematic map of the pilgrim path from Katra up the Trikūṭa hill to the holy cave and the Bhairon temple'+(f', with {hi} marked' if hi else ''),o)
def jkmap():
    o='<rect width="560" height="220" fill="#eef3fa"/><path d="M20 210 Q120 60 300 40 Q480 30 540 120 L540 210z" fill="#dfe7d6" stroke="#9aa88a"/>'
    o+='<path d="M60 200 Q200 170 300 175 T540 160" stroke="#8fb8de" stroke-width="6" fill="none"/>'+lab(110,212,'river Cenāb (Chenab), simplified',9)
    o+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="#111" stroke-width="1.5"/>'+lab(x,y+18,n,11) for n,x,y,r,c in (('Jammu',150,150,7,'#1d4f8a'),('Katra',300,118,7,'#e0a800'),('Trikūṭa · Bhavan',350,78,11,RED),('Reasi',250,92,5,'#e0a800'),('Srinagar',420,40,6,'#1d4f8a')))
    o+=tri(360,70,.28,'#a9b49a')+lab(470,212,'simplified, not to scale',10)
    return svg(560,220,'Schematic map of Jammu, Katra and the Trikūṭa hill in the Jammu region',o)
S=lambda label,inner,bg='#fff3cf',h=190: svg(560,h,label,f'<rect width="560" height="{h}" fill="{bg}"/>'+inner)

pp=[]
pp.append(foreword(0,[
 'High in the Trikūṭa hills of the Jammu region, a cave holds no carved image at all. Inside are three small rounded rocks, and for millions of people they are the Mother herself: <b>Vaiṣṇo Devī</b>, called Mātā Rānī, Sherāwālī, “she who rides the lion”, and greeted with one cry: <b>“Jai Mātā Dī!”</b>',
 'This guide walks the whole way: who she is and why she is called Vaiṣṇavī, the four stories that make up her legend, every halt on the hill from Bāṇgaṅgā to the cave, what is seen inside the cave, the meaning of the three <b>piṇḍīs</b>, the Bhairon temple that completes the pilgrimage, the verse in the Mahābhārata, a thousand years of history, and Navarātri on the hill.',
 'For the Devī’s great battles read our '+L('/devi/devi-mahatmya/','Devī Māhātmya')+' series; for the nine nights, our '+L('/festivals/navaratri/','Navarātri')+' guides.'],
 [('z','A cave with no statue?'),('b','Just three rocks, Zappy. And people walk thirteen kilometres up a mountain to see them.')]))
pp.append(glance([('Where','Trikūṭa hill above Katra, Reasi district, Jammu region'),('Height','The holy cave (Bhavan) at about 1,585 m (5,200 ft)'),('Deity','Vaiṣṇo Devī: Mahākālī, Mahālakṣmī and Mahāsarasvatī as one'),('Form','Three natural rock heads, the piṇḍīs, on one rock about 5½ ft high'),('The walk','About 12 km from Katra; Ardhkuwārī halfway'),('Completion','Darśan of Bhairon Nāth, about 1.5 km beyond'),('Cry','“Jai Mātā Dī!”'),('Run by','Shri Mata Vaishno Devi Shrine Board (since 1986)'),('Festival','Navarātri, especially in Āśvina'),('Pilgrims','Many millions a year: among India’s most visited shrines')],
 S('Three peaks above a cave with a red flag','\n'+tri(280,185,1.2)+cavemouth(280,190,.6)+g(360,80,.7,flag(RED))),[('z','Ten million people a year?'),('b','In the busiest years, Zappy. Few shrines on earth draw more.')],'Three rocks, <b>one Mother</b>.'))
pp.append(reading('where','WHERE IT IS','Trikūṭa, the three-peaked hill',jkmap(),[
 '<b>The hill.</b> Trikūṭa means “three peaks”. The hill rises above the town of Katra in Reasi district, in the Jammu region, about 50 km north of Jammu city.',
 '<b>The cave.</b> The shrine, called the <b>Bhavan</b> (“the house”), is a natural cave at about 1,585 m on the hill’s flank. Pilgrims first see it from about 1.5 km away; the last stretch is level or gently downhill.',
 '<b>The town.</b> Katra is the base: every pilgrim begins here, and the walk up is about 12 km.',
 '<b>An old name.</b> The goddess was long known as Trikūṭā Devī, the goddess of the three-peaked hill. A Trikūṭa mountain is named already in the Ṛgveda, though identifying it with this hill is a later reading.'],
 [('z','Why “house” for a cave?'),('b','Because it is her home, Zappy. You don’t visit a temple, you visit the Mother at home.')],'The <b>Trikūṭa</b> hill.'))
pp.append(cards('who','WHO IS VAIṢṆO DEVĪ?','Three goddesses in one girl',S('Three goddesses joining their light into one young goddess',g(110,180,.9,devi(sari='#1b1b1b',items=('sword','trident'),fierce=True))+g(450,180,.9,devi(sari='#f1eee2',items=('book','rosary')))+g(280,185,1.05,devi(sari=RED,items=('lotus','discus','conch','abhaya')))+'<path d="M150 90 L230 100 M410 90 L330 100" stroke="#ffd60a" stroke-width="6"/>'),[
 ('🌸','Vaiṣṇavī','“Of Viṣṇu”: she is Viṣṇu’s power, and in the legend she longs to be one with him. Vaiṣṇo is the north Indian form of the name.'),
 ('🔱','Three in one','The legend says Mahākālī, Mahālakṣmī and Mahāsarasvatī joined their radiance (tejas) to create her. The cave keeps all three as piṇḍīs.'),
 ('🦁','Sherāwālī','“She of the lion”. Pictures show a young goddess in a red sari on a lion, often eight-armed, with sword, trident, discus, conch, mace, bow and lotus, one hand blessing.'),
 ('🙏','Mātā Rānī','“Mother Queen”. Other names: Trikūṭā, Ambā, Nārāyaṇī, Viṣṇumāyā and Ādikumārī, “the eternal maiden”.')],
 [('z','So is she Durgā?'),('b','Her pictures look very like Durgā, Zappy, and devotees see one Devī. The cave tradition keeps her as Vaiṣṇavī.')],'<b>Vaiṣṇavī</b>: Viṣṇu’s power.',
 'Vaiṣṇo Devī is the Great Goddess in one particular form: a young maiden of perfect purity, made of all three of the Devī’s great powers, living in a cave until the end of the age.'))
pp.append(story('birth','THE LEGEND, PART 1','A girl who wanted Viṣṇu',strip('Three panels: a girl born to a devout couple in the south; the girl meditating in a forest; Rāma meeting her and pointing north',[panel([(person('#1d4f8a'),.7),(devi(items=()),.6),(person(RED),.7)],'#fff3cf'),panel([(sage(RED),.9)],'#e3f5e9'),panel([(ram(),.8),(devi(items=('lotus',)),.7)],'#e3eaf3')],['born in the south','penance in the forest','Rāma’s promise']),'Retold from the Shrine Board’s account of the legend; tellings differ in details.',[
 'In the Tretā age the Devī sent a portion of herself to be born to <b>Ratnākar</b> and his wife, devout people in south India. The child was named <b>Vaiṣṇavī</b>.',
 'From childhood she hungered for knowledge. Turning inward, she learnt meditation and left home for the forest to do penance, wishing to merge with Viṣṇu.',
 'During his exile <b>Rāma</b> came to her. She knew him as Viṣṇu and asked to be one with him. He said the time was not right, and promised to return.',
 'He came back disguised as an old man, and she did not recognise him. Then he told her: her union would come in the <b>Kali age</b>, when he returns as <b>Kalki</b>.',
 'He asked her to go north to the foot of the <b>Trikūṭa</b> hills, meditate there and help those who suffer. She went, with great hardship, and set up her āśram.'],
 [('z','She’s waiting for Kalki?'),('b','So the story says, Zappy. Until then she stays a maiden in the cave.')],'Waiting <b>for Kalki</b>.'))
pp.append(story('shridhar','THE LEGEND, PART 2','Paṇḍit Śrīdhar’s feast',strip('Three panels: a poor priest worried; a young girl serving food to a large crowd from a small pot; a yogi demanding meat and wine',[panel([(person('#e0a800',seat=True),.9)],'#fde9c8'),panel([(devi(items=()),.6),(pot(),.6),(person('#1d4f8a'),.5)],'#fff3cf'),panel([(bhairon(),.8)],'#e9e3f5')],['a poor priest','food without end','Bhairon arrives']),'From the most widely told version, as summarised by the Shrine Board and standard accounts; tellings differ.',[
 '<b>Paṇḍit Śrīdhar</b> of Hansālī village near Katra was poor but devoted. A young girl appeared to him and asked him to hold a great feast, a <b>bhaṇḍārā</b>, for the village.',
 'He invited everyone, including <b>Gorakhnāth</b> and his yogīs. He had almost nothing to feed them.',
 'The girl served the whole crowd from one small pot, and the food never ran out.',
 'Gorakhnāth had sent his disciple <b>Bhairon Nāth</b> to test her. Bhairon demanded meat and wine; the girl refused, since this was a pure vegetarian feast.',
 'Bhairon grew infatuated and tried to seize her. She vanished and fled up the hill. Later, in a dream, she showed Śrīdhar the cave.'],
 [('z','A pot that never ran out?'),('b','The Mother’s kitchen, Zappy. Even today the hill feeds everyone who comes.')],'The feast that <b>never ended</b>.'))
pp.append(story('flight','THE LEGEND, PART 3','The flight up the hill',strip('Three panels: the goddess shooting an arrow into rock to make a stream; footprints on a rock; a narrow womb-shaped cave',[panel([(devi(items=('bow','arrow')),.6),(hanuman(),.5)],'#e3f5e9'),panel([('<ellipse cx="-14" cy="-10" rx="8" ry="14" fill="#c0392b"/><ellipse cx="14" cy="-10" rx="8" ry="14" fill="#c0392b"/><rect x="-50" y="0" width="100" height="10" fill="#8a7a6a"/>',1.0)],'#fde9c8'),panel([(cavemouth(0,0,.5),1),(devi(items=()),.4)],'#e9e3f5')],['Bāṇgaṅgā','Caraṇ Pādukā','Garbh Jūn']),'Traditional account of the halts on the path; tellings differ.',[
 '<b>Bāṇgaṅgā.</b> On the way up, she shot an arrow (<i>bāṇ</i>) into the rock and a stream sprang out. Many tellings say it quenched <b>Hanumān</b>’s thirst; she bathed and washed her hair there, so it is also called Bālgaṅgā, “hair-Gaṅgā”.',
 '<b>Caraṇ Pādukā.</b> She paused on a rock to look back for Bhairon, and left her footprints.',
 '<b>Ardhkuwārī.</b> Halfway up she entered a narrow womb-shaped cave and meditated there for <b>nine months</b>, with Hanumān guarding the door in many tellings.',
 '<b>Found.</b> Bhairon traced her at last. She made an opening at the far end of the cave with her trident and climbed on.',
 '<b>The cave.</b> She reached the holy cave high on the hill. Bhairon followed her even there.'],
 [('z','Nine months in a cave?'),('b','Like a baby in the womb, Zappy. That’s why it is called the womb cave.')],'Every halt <b>a shrine</b>.'))
pp.append(story('bhairon','THE LEGEND, PART 4','At the mouth of the cave',strip('Three panels: the goddess in fierce form with a sword facing Bhairon; a head flying to a far peak; the goddess becoming three rocks',[panel([(devi(items=('sword','trident'),fierce=True,hair_open=True),.7),(bhairon(),.6)],'#20243a'),panel([(tri(0,0,.32,'#8a9a7a')+'<circle cx="40" cy="-80" r="10" fill="#4a3a5a"/>',1)],'#e3eaf3'),panel([(pindis(0,0,.6),1)],'#f6e3e1')],['she strikes','the head flies','three piṇḍīs']),'Shrine Board account.',[
 'Bhairon found her in the cave and challenged her. She tried to avoid a fight, but he would not stop.',
 'The goddess took her terrible form (many say as Mahākālī or Caṇḍikā) and cut off his head just outside the cave mouth.',
 'His body fell at the entrance; his head flew about <b>1.5 km</b> to another spur of the hill.',
 'Dying, Bhairon understood and begged forgiveness. She gave him a boon: no pilgrimage to her would be complete without darśan of <b>him</b>.',
 'Then she gave up her human form and became a rock with three heads, the <b>piṇḍīs</b>, sunk in meditation for ever.'],
 [('z','She forgave him after all that?'),('b','And gave him a temple of his own, Zappy. A mother’s anger ends in mercy.')],'Anger that ends <b>in mercy</b>.'))
pp.append(reading('path','THE YĀTRĀ','From Katra to the cave',mapsv(),[
 '<b>Twelve kilometres.</b> The yātrā climbs about 12 km from Katra to the Bhavan, past every place in the legend. Pilgrims walk it day and night, calling “Jai Mātā Dī”.',
 '<b>The halts.</b> Bāṇgaṅgā, where many bathe; Caraṇ Pādukā with the footprints; <b>Ardhkuwārī</b> at the halfway point; then the high ridge of Sāñjhī Chhat; and the Bhavan.',
 '<b>Other darśans on the way.</b> Small shrines line the path; tradition honours the Bhūmikā temple near Katra, linked with Śrīdhar.',
 '<b>After the cave.</b> A further climb leads to <b>Bhairon</b>’s temple on the next spur, which completes the pilgrimage.',
 '<b>The walk itself.</b> Many see the climb as part of the worship: every step is a step towards the Mother. (Interpretation.)'],
 [('z','Day and night?'),('b','The hill never sleeps, Zappy. Lamps and voices go up it all night.')],'Twelve km <b>of prayer</b>.'))
pp.append(reading('ardhkuwari','ARDHKUWĀRĪ','The womb cave halfway up',S('A narrow cave in the rock with one pilgrim squeezing through',g(280,185,1.3,'<path d="M-160 0 Q-140 -120 0 -124 Q140 -120 160 0z" fill="#8a7a6a" stroke="#111" stroke-width="2"/><path d="M-110 -40 Q0 -70 110 -40" stroke="#2a2018" stroke-width="22" fill="none" stroke-linecap="round"/>')+g(200,140,.4,person('#c0392b'))),[
 '<b>The name.</b> Ardhkuwārī (Adhkuwārī) is the halfway point, about 6 km from Katra at roughly 4,800 ft. The Shrine Board links the name with <b>Ādikumārī</b>, “the eternal virgin”.',
 '<b>Garbh Jūn.</b> The narrow cave where she meditated for nine months is called <b>Garbh Jūn</b>, from <i>garbha-yoni</i>, “the womb”.',
 '<b>One at a time.</b> It is so narrow that only one person can pass at a time. Pilgrims believe that crawling through it cleanses them of sins, as if born again.',
 '<b>The second darśan.</b> After the holy cave, Ardhkuwārī is counted the most important stop of the yātrā.'],
 [('z','You crawl through it?'),('b','Slowly, Zappy. You come out the other side like a new baby, they say.')],'Born <b>again</b>.'))
pp.append(cards('inside','INSIDE THE HOLY CAVE','What pilgrims see on the way in',S('A long cave with a stream, rock shapes and the piṇḍīs at the far end',f'<rect x="20" y="40" width="520" height="130" rx="60" fill="#5a4a3a"/>'+'<path d="M40 160 L520 160" stroke="#8fb8de" stroke-width="8"/>'+pindis(470,150,.55)+g(90,140,.4,ganesha())+'<rect x="150" y="128" width="120" height="14" rx="7" fill="#3a2a2a"/>'+lab(210,120,'Bhairon’s torso',10)+lab(470,62,'piṇḍīs',11)+lab(300,178,'Caraṇ Gaṅgā',10),'#e9e3f5'),[
 ('🐘','Vakratuṇḍa Gaṇeśa','At the entrance, on the left, a rock form of Gaṇeśa, with symbols of Sūrya and Candra beside him.'),
 ('🪨','Bhairon’s torso','Once inside, pilgrims cross a rock about 14 ft long, held to be Bhairon’s body (dhaḍ).'),
 ('🐒','Lāṅgur Vīr','Beyond it, a symbol of Hanumān, the guard of the cave.'),
 ('💧','Caraṇ Gaṅgā','A stream said to flow from the Mother’s feet. In the old cave pilgrims wade through it.'),
 ('🐍','Śeṣa Nāga','The roof flares out and seems to rest on the many heads of the serpent Śeṣa.'),
 ('🙏','The piṇḍīs','At the end, on a raised rock, the three piṇḍīs, with a rock read as her raised hand of blessing.')],
 [('z','Gods carved by nature?'),('b','Devotees see thirty-three crore gods in that cave, Zappy. It is about 30 m long.')],'A cave <b>full of gods</b>.',
 'The natural cave is about 30 m (98 ft) long. Besides the piṇḍīs, devotees recognise many other forms in the rock. Because crowds became so large, tunnels were later built beside the old cave; the old one is opened when numbers allow.'))
pp.append(reading('pindis','THE THREE PIṆḌĪS','Kālī, Lakṣmī, Sarasvatī',S('Three rounded rock heads: dark, red-gold and white, under a canopy',g(280,205,1.45,pindis())+lab(120,60,'Mahākālī',13)+lab(280,18,'Mahālakṣmī',13)+lab(445,60,'Mahāsarasvatī',13)),[
 '<b>No idol.</b> The goddess is a rock about five and a half feet high, with three heads on top: the piṇḍīs. Everything else in the cave is decoration round them.',
 '<b>Three colours.</b> Devotees describe Mahāsarasvatī as whitish, Mahālakṣmī as yellow-red and Mahākālī as dark. Mahālakṣmī, in the middle, is often identified with Vaiṣṇo Devī herself.',
 '<b>Three qualities.</b> Many read them as the three guṇas: sattva (white, knowledge), rajas (red, effort and wealth) and tamas (dark, dissolution). (Interpretation.)',
 '<b>The Devī Māhātmya.</b> Mahākālī, Mahālakṣmī and Mahāsarasvatī are the goddesses of its three great episodes; read our '+L('/devi/devi-mahatmya/','Devī Māhātmya')+' series.',
 '<b>Svayambhū.</b> The piṇḍīs are self-manifested: never carved, never installed.'],
 [('z','Why would a goddess be a rock?'),('b','So nothing human stands between you and her, Zappy. Just stone, water and the Mother.')],'Three powers, <b>one rock</b>.'))
pp.append(reading('bhairo','BHAIRON NĀTH','The pilgrimage is complete here',S('A small temple on a high spur above clouds, a rock head inside',tri(280,185,1.1,'#a9b49a')+g(410,90,.55,palace())+'<circle cx="410" cy="70" r="8" fill="#4a3a5a"/>'+g(150,160,.8,flag(RED)),'#dfe9f6'),[
 '<b>Where.</b> The Bhairon temple stands on another spur of the hill, about 1.5 km from the holy cave and higher up, where his head is said to have fallen.',
 '<b>The rock.</b> Inside, a rock is worshipped as Bhairon’s head.',
 '<b>The boon.</b> Because of the boon, popular belief holds that the yātrā is not complete without his darśan, so pilgrims climb to him after seeing the Mother.',
 '<b>Who he was.</b> In the common version, the ablest disciple of Gorakhnāth; another version makes him a demon king of the hills. Traditions differ.',
 '<b>A reading.</b> The enemy becomes the guardian. Many see here the Devī’s way: she defeats ego, then turns it to her service. (Interpretation.)'],
 [('z','You visit the villain too?'),('b','He isn’t a villain any more, Zappy. She made him part of her house.')],'The enemy turned <b>guardian</b>.'))
pp.append(reading('mahabharata','IN THE MAHĀBHĀRATA','Arjuna’s hymn to Durgā',S('Kṛṣṇa and Arjuna on a chariot, Arjuna with folded hands before a goddess',g(160,180,.9,krishna())+g(240,180,.9,namaste('#c0392b'))+g(420,185,1,devi()),'#e3eaf3'),[
 '<b>Before the war.</b> In the Bhīṣma Parva (chapter 23), just before the Gītā, Kṛṣṇa tells Arjuna to pray to Durgā for victory. Arjuna sings a hymn of praise.',
 '<b>The line.</b> One verse (7 in common numbering) reads:<br><i>vedaśrutimahāpuṇye brahmaṇye jātavedasi |<br>jambūkaṭakacaityeṣu nityaṃ sannihitālaye ||</i>',
 '<b>Its meaning.</b> “You who are most holy in the Veda, devoted to Brahman, present in the sacred fire; you who dwell for ever in the shrines on the slopes of Jambū.”',
 '<b>The link.</b> Devotees and the shrine’s tradition read “the slopes of Jambū” as the hills of Jammu, and the hymn as Arjuna’s worship of this Devī. Scholars treat this as a traditional identification. (Interpretation.)'],
 [('z','Jambū is Jammu?'),('b','So tradition reads it, Zappy. It’s a beautiful link, honestly held as tradition.')],'<b>Jambū</b>’s Devī.'))
pp.append(reading('history','A THOUSAND YEARS ON THE HILL','From Trikūṭā Devī to the Shrine Board',S('A timeline with a cave, a king, a scroll and a modern building',''.join(g(x,170,.55,f) for x,f in ((70,cavemouth(0,0,.6)),(190,person('#8e1f17')),(310,book()),(430,palace())))+'<path d="M30 180 H530" stroke="#8e1f17" stroke-width="4"/>'),[
 '<b>Early worship.</b> The goddess was first known as Trikūṭā Devī. Kalhaṇa’s 12th-century chronicle already knows her worship as established; some scholars think she began as a local hill goddess.',
 '<b>Kings and priests.</b> The 19th-century chronicle <i>Rājdarśanī</i> records a visit by Raja Jas Dev of Jammu in 996. A deed of 1007 from Raja Kirpāl Dev gave the shrine’s service to the <b>Bāridārs</b>, Śrīdhar’s descendants, who kept it for centuries.',
 '<b>The Ḍogrās.</b> She is the family goddess of the Ḍogrā rulers of Jammu. Mahārāja Raṇjīt Dev built water points and shelters on the path in the 18th century; in 1846 Mahārāja Gulāb Singh placed it under the Dharmārth Trust.',
 '<b>The Shrine Board.</b> In 1986 control passed to the Shri Mata Vaishno Devi Shrine Board (Act of 1988), chaired ex officio by the Governor, now the Lieutenant Governor, of Jammu and Kashmir. Pilgrims grew from under a million a year in 1981 to many millions.',
 '<b>Other dates.</b> Tradition dates Śrīdhar’s finding of the cave very differently: some say about 700 years ago. Traditions differ.'],
 [('z','A deed from the year 1007!'),('b','A thousand years of paperwork, Zappy. And worship far older.')],'A <b>thousand years</b> of pilgrims.'))
pp.append(cards('worship','WORSHIP AND OFFERINGS','How the Mother is honoured',S('A plate with a red scarf, a coconut, sweets and a lamp',g(200,170,1.4,plate())+g(200,140,.9,coconut())+'<path d="M300 120 q60 -30 120 0 l-10 40 q-50 -20 -100 0z" fill="#c0392b" stroke="#111" stroke-width="2"/>'+g(470,170,1,lamp())),[
 ('🧣','Bheṇṭ','Pilgrims bring a gift (bheṇṭ) for the Mother: a red chunrī (scarf), a coconut, dry fruit, a little red cloth.'),
 ('🔔','Ārati','The goddess is worshipped with ārati morning and evening, in the cave and outside it.'),
 ('🍬','Prasād','Each pilgrim receives prasād to take home: blessed sweets and a token of the visit.'),
 ('📣','“Jai Mātā Dī”','The greeting, the prayer and the marching song of the hill, called out at every step.'),
 ('🎶','Bhajans','Devotional songs of the Mother in Ḍogrī, Punjabi and Hindi fill the path.'),
 ('🏘️','Bāridārs','The hereditary servants of the shrine, descendants of Śrīdhar, served it for centuries; the Bhūmikā temple near Katra honours Śrīdhar.')],
 [('z','What do people take home?'),('b','Prasād, a red thread, and the feeling of having been called, Zappy.')],'A gift <b>for the Mother</b>.'))
pp.append(reading('bulava','“SHE CALLS YOU”','The belief of the bulāvā',S('A path winding up a mountain under a starry sky with a single lamp at the top',f'<rect width="560" height="190" fill="#20243a"/>'+''.join(f'<circle cx="{(k*67)%560}" cy="{(k*29)%90}" r="2" fill="#fff"/>' for k in range(30))+tri(280,190,1.2,'#3a4a5a')+'<path d="M80 190 Q200 150 260 120 T300 70" stroke="#ffd60a" stroke-width="3" stroke-dasharray="4 6" fill="none"/>'+g(300,70,.6,lamp()),'#20243a'),[
 '<b>The bulāvā.</b> A belief shared by countless pilgrims: you go to Vaiṣṇo Devī only when the Mother calls you (her <i>bulāvā</i>). Until then, plans fall through; when she calls, the way opens. (Popular belief.)',
 '<b>Families.</b> Many families make the climb every year, or bring each new child, or come to give thanks for a wish granted.',
 '<b>For everyone.</b> People of many castes, regions and traditions walk side by side; the hill is open to all.',
 '<b>The cry.</b> Strangers greet each other on the path with “Jai Mātā Dī”, and the answer is the same.'],
 [('z','What if I plan and plan and can’t go?'),('b','Then, devotees say, you wait for her call, Zappy. It comes.')],'She <b>calls</b>.'))
pp.append(reading('navaratri','NAVARĀTRI ON THE HILL','The Mother’s great nights',S('Lamps and garlands along a mountain path, a flag, and a goddess on a lion',g(150,185,1,lion())+g(150,140,.7,devi())+''.join(g(x,180,.5,lamp()) for x in range(260,540,40))+g(500,90,.6,flag(RED)),'#fde9c8'),[
 '<b>Two Navarātris.</b> Both the spring (Caitra) and autumn (Āśvina) Navarātris draw vast crowds; the autumn one is the greatest.',
 '<b>What happens.</b> The cave and the Bhavan are decorated with flowers and lights; special worship and havans are held through the nine nights.',
 '<b>Kanyā pūjā.</b> As everywhere in north India, little girls are worshipped as the Devī on the eighth or ninth day; here, the Mother herself came as a girl.',
 '<b>Read more.</b> Our '+L('/festivals/navaratri/','Navarātri series')+', night by night; Dīpāvalī is also kept with lamps on the hill.'],
 [('z','A girl goddess worshipping girls!'),('b','That’s exactly why it matters here, Zappy.')],'Nine nights <b>on Trikūṭa</b>.'))
pp.append(reading('meaning','WHAT VAIṢṆO DEVĪ TEACHES','The meaning of the climb',S('A small pilgrim climbing towards a great motherly goddess at the top of a hill',tri(280,190,1.2,'#c9d1bf')+g(280,80,.9,devi())+g(130,175,.6,namaste('#1d4f8a'))),[
 '<b>Purity.</b> She is a maiden who refuses meat, wine and force. Many read her as the power of a pure mind that cannot be grabbed. (Interpretation.)',
 '<b>Patience.</b> She waits an entire age for Kalki. Devotees take her patience as a lesson. (Interpretation.)',
 '<b>All three powers.</b> Knowledge, prosperity and strength together in one rock: no devotee has to choose. (Interpretation.)',
 '<b>Mercy.</b> She ends the story not with victory alone but with forgiveness, giving her pursuer a home.',
 '<b>Effort.</b> Twelve kilometres of climbing: the Mother is reached by walking, and the walk is the prayer.'],
 [('z','Which lesson matters most?'),('b','Ask the pilgrims, Zappy. Each one carries a different one down the hill.')],'Purity, patience, <b>mercy</b>.'))
pp.append(cards('glossary','WORDS TO KNOW','The vocabulary of the hill',S('A row of symbols: three rocks, a footprint, a cave, a flag',g(90,170,.5,pindis())+'<ellipse cx="210" cy="140" rx="10" ry="18" fill="#c0392b"/><ellipse cx="236" cy="140" rx="10" ry="18" fill="#c0392b"/>'+cavemouth(350,175,.5)+g(480,150,.7,flag(RED)),'#fff3cf',170),[
 ('🪨','Piṇḍī','A natural rounded stone worshipped as the deity, not carved.'),('🏠','Bhavan','“The house”: the holy cave and the complex round it.'),
 ('👣','Caraṇ Pādukā','“Foot-sandals”: the rock with her footprints.'),('🏹','Bāṇgaṅgā','The “arrow-Gaṅgā” stream she made with an arrow.'),
 ('🤰','Garbh Jūn','“The womb”: the narrow cave at Ardhkuwārī.'),('🍲','Bhaṇḍārā','A community feast open to all, like Śrīdhar’s.'),
 ('🎁','Bheṇṭ','A gift or offering for the Mother.'),('📣','Jai Mātā Dī','“Victory to the Mother”: the pilgrims’ cry.')],
 [('z','Piṇḍī, bhavan, bheṇṭ!'),('b','Now you can walk the hill like a local, Zappy.')],'Words <b>of the hill</b>.'))
pp.append(end(0,['<b>Who.</b> Vaiṣṇavī: Kālī, Lakṣmī and Sarasvatī in one maiden, waiting for Kalki.','<b>Legend.</b> Śrīdhar’s feast, Bhairon’s chase, nine months in Garbh Jūn, the cave.','<b>The cave.</b> Three self-made piṇḍīs; Gaṇeśa, Hanumān, Śeṣa and the Caraṇ Gaṅgā on the way in.','<b>Completion.</b> Bhairon’s temple, by her boon.','<b>History.</b> From Trikūṭā Devī and the Ḍogrā kings to the Shrine Board.'],
 'More Devī shrines: the '+L('/temples-of-india/18-shakti-peethas/','18 Śakti Pīṭhas')+', and the Mother of our own hills, '+L('/temples-of-india/around-mysuru/chamundeshwari/','Cāmuṇḍeśvarī')+'.','Vaiṣṇo Devī, the Mother in the Trikūṭa cave'))
pp.append(sources([('Shrine and legend:','Shri Mata Vaishno Devi Shrine Board, “About the Shrine”, “Bhawan”, “Adhkuwari” and “Other Darshans inside the Cave” pages.'),('Reference:','Wikipedia, “Vaishno Devi” and “Vaishno Devi Temple” (history, Rājdarśanī, Kalhaṇa, the 1986 Board and the Act of 1988, pilgrim figures, iconography).'),('Mahābhārata verse:','Bhīṣma Parva 23, Arjuna’s Durgā hymn, as given by stotranidhi.com (verse 7); our own translation.'),('Further:','Green Message (greenmesg.org), Vaiṣṇo Devī sacred geography; travel writing on the cave’s inner darśans.')],
 'the Mahābhārata “Jambū” = Jammu identification (tradition); the dates of Śrīdhar’s discovery (from the 10th century to about 700 years ago, sources differ); Raja Jas Dev’s visit (a 19th-century chronicle); the right-arm or skull Śakti Pīṭha claims (disputed, not used here); Hanumān’s role at Bāṇgaṅgā and the cave door (popular tellings); the colours of the piṇḍīs (devotees’ descriptions).',
 'Study notes on Vaiṣṇo Devī; legend retold from the Shrine Board’s account.'))
build(0,'TRIKŪṬA · THE CAVE · THREE PIṆḌĪS · JAI MĀTĀ DĪ',
 covart('A young goddess on a lion before a three-peaked mountain with a cave and pilgrims climbing',tri(300,196,1.0,'#c9d1bf')+cavemouth(300,150,.4)+g(110,196,1.15,lion())+g(110,150,.85,devi())+''.join(g(x,196-(x-180)/4,.32,person(RED)) for x in range(200,300,24))+g(410,60,.55,flag(RED))),
 'The Mother of Trikūṭa','The Mother’s whole story in <b>four legend pages</b>, the <b>twelve-kilometre</b> path halt by halt, <b>inside the cave</b>, the three <b>piṇḍīs</b>, Bhairon’s temple, the Mahābhārata verse and a thousand years of history.',
 'Vaiṣṇo Devī explained and illustrated: Vaiṣṇavī born of three goddesses, Rāma’s promise, Śrīdhar’s feast, Bhairon Nāth’s chase, Bāṇgaṅgā, Caraṇ Pādukā and Garbh Jūn, the holy cave and its three piṇḍīs, the Bhairon temple, the Mahābhārata verse, history and Navarātri.',pp)
print('pages',len(pp)+2)
