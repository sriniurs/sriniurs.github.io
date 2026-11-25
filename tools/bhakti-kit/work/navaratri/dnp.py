"""Durgā Namaskāra Pūjā · standalone Devī article (red). SAMPLE build."""
import sys
import pages as PG
from pages import foreword,glance,reading,story,cards,end,sources,build,covart,verse
from fig import strip, svg, g, lab, txt, devi, sage, demon, god, lamp, lotus, trident, mountain, tree
from fig2 import panel
from fig3 import namaste
from dnfig import *
L=lambda u,t: f'<a href="{u}">{t}</a>'
PG.configure('/tulunadu/culture/',[('durga-namaskara','Durgā Namaskāra Pūjā','The Goddess Worshipped in a Lamp')],'red','Devī','Devī','Devī')
PG.CFG.update(backurl='/tulunadu/culture/',backname='Tulu Nadu Culture articles')
PG.OUT='outd/tulu/'
SAMPLE='--sample' in sys.argv
i=0
pp=[]
P_fw=(foreword(i,[
 'On the coast of Karnataka, as night falls in Navarātri, a family clears a floor, draws a lotus in red, yellow and white powders, and sets a tall brass lamp at its centre. The priest lights it and calls the Mother into the flame. For the next hours she is worshipped there, in the light itself. This is <b>Durgā Namaskāra Pūjā</b>.',
 'This guide takes it apart piece by piece: what the rite is and why it is called <i>namaskāra</i>; how the Goddess came to be called Durgā; the Vedic <b>Durgā Sūkta</b> that hails her as the colour of fire; the maṇḍala, the lamp and the letters of <b>mātṛkā-nyāsa</b>; the order of worship; when it is done; and how Udupi, Kaṭīl and Mysuru keep it.',
 'Her battles in full are in our '+L('/devi/devi-mahatmya/','Devī Māhātmya')+' series; the nine nights in '+L('/festivals/navaratri/','Navarātri')+'; the island Goddess of the coast in '+L('/tulunadu/temples/katil-durgaparameshwari/','Kaṭīl Durgāparameśvarī')+'.'],
 [('z','Is this the same as the Durgā Pūjā of Bengal?'),('b','Same Goddess, different rite. Bengal shapes her in clay and worships the image for days. Here there is no image at all: a lotus drawn on the floor and a flame at its heart.')]))
P_gl=(glance([
 ('What','A worship of Durgā invoked into a tall lamp at the centre of a drawn maṇḍala'),
 ('Also called','Durgā Dīpa Namaskāra, Durgādīpa Namaskāra; in some places Bhagavatī Sevā'),
 ('The Goddess','Durgā, invoked as Mahākālī, Mahālakṣmī and Mahāsarasvatī'),
 ('Her seat','A maṇḍala of coloured powders: a lotus, often with a six-pointed star'),
 ('The heart of it','Mātṛkā-nyāsa: the letters of the alphabet placed on her form'),
 ('Around her','The guardians of the eight directions (aṣṭa dikpālas)'),
 ('Recited','Durgā Sūkta; the Devī Māhātmya (Saptaśatī); often Lalitā Sahasranāma and Triśatī'),
 ('When','Navarātri; the monsoon month of Āṣāḍha; Tuesdays and Fridays; chosen tithis'),
 ('How long','One evening, or a vow kept over several days (up to twelve)'),
 ('Heartland','Coastal Karnataka (Udupi, Dakṣiṇa Kannaḍa) and its maṭhas; known across the South')],
 S('A tall lamp on a lotus maṇḍala with flowers and small lamps around it',g(280,150,.62,mandala_floor(190,.34,130,10)),'#f6e3e1',200),
 [('z','No idol anywhere in this table.'),('b','None is needed. The lamp is the image. Everything else on the floor is her seat and her court.')],
 'A lotus on the floor, <b>the Mother in the flame</b>.'))
P_what=(reading('what','WHAT IS DURGĀ NAMASKĀRA?','The Mother invited into a lamp',
 S('Two devotees with folded hands on either side of a lamp standing on a maṇḍala',g(280,150,.6,mandala_floor(190,.34,130,8))+g(70,180,1.3,namaste('#8e1f17'))+g(490,180,1.3,namaste('#1d4f8a'),flip=True),'#fff3cf',200),
 ['<b>The rite.</b> Durgā Namaskāra Pūjā is a worship of the Goddess in a lamp. The floor is cleaned, a maṇḍala is drawn in coloured powders, and a tall standing lamp is set at its centre and lit. The priest then invokes Durgā into the flame, and from that moment the lamp is treated as the Goddess herself.',
  '<b>Three in one.</b> She is called in as <b>Mahākālī, Mahālakṣmī and Mahāsarasvatī</b>, the three forms praised in the three movements of the '+L('/devi/devi-mahatmya/','Devī Māhātmya')+'. The guardians of the eight directions are worshipped around the edge of the maṇḍala, as the court around a queen.',
  '<b>Built of sound.</b> The central act is <b>mātṛkā-nyāsa</b>: the letters of the Sanskrit alphabet are placed, one by one, on the parts of her form. The Goddess in the lamp is invoked, limb by limb, out of the sounds of speech. (This is described here, not given as a practice; it is done by a trained priest.)',
  '<b>The salutations.</b> Then come the offerings and the long recitations: the Vedic Durgā Sūkta, the Devī Māhātmya, and in many homes the Lalitā Sahasranāma. Each offering ends in <i>namaḥ</i>, a bow. The name says plainly what the rite is: a pūjā of salutations, <i>namaskāra</i>, to Durgā in the lamp.',
  '<b>On the coast.</b> In Udupi and Dakṣiṇa Kannaḍa it is a familiar household rite. A family may hold a Gaṇahoma in the morning, a Satyanārāyaṇa Pūjā in the afternoon and close the day with Durgā Namaskāra at night; maṭhas hold it in Navarātri.'],
 [('z','Why a flame and not a picture of her?'),('b','A picture shows one form. A flame shows none and all of them at once: it moves, it lights everything around it, and you cannot hold it. Many say that is the nearest the eye can get to Śakti.')],
 'No image: <b>the flame is the Goddess</b>.'))
P_durgama=(story('durgama','STORY · HOW SHE BECAME DURGĀ','The demon Durgama, the hundred-eyed Mother and the greens',
 strip('Three panels: the demon Durgama carrying off the Vedas; the hundred-eyed Goddess weeping over a parched land and bringing out greens; the Goddess slaying Durgama with her trident',
  [panel([(demon('#3a2a5a'),1.25),(vedas_scroll(),1.1)],'#20243a'),
   (cracked()+g(36,150,.7,sage())+g(100,140,.85,devi(sari='#1d4f8a',items=('lotus','bow')))+g(100,166,.7,greens()),'#fde9c8'),
   panel([(devi(items=('trident','sword','discus','conch'),fierce=True),1.05),(demon('#3a2a5a'),.85)],'#f6e3e1')],
  ['Durgama takes the Vedas','Śatākṣī, Śākambharī','Durgā']),
 'Foretold by the Goddess herself in the Devī Māhātmya (11.49–50), and told in full in the Devī Bhāgavata Purāṇa (book 7, chapter 28).',
 ['The asura <b>Durgama</b>, “the hard to reach”, struck at the gods’ root: he made the <b>Vedas</b> vanish. The sages forgot them, the sacrifices stopped, and with them went the gods’ strength and the rain.',
  'A drought of a <b>hundred years</b> followed. Rivers dried, fields cracked, people and animals starved.',
  'The sages called on the Devī. She came with a hundred eyes to see them all at once, and wept at their misery; her tears ran as rivers. She is <b>Śatākṣī</b>, the hundred-eyed.',
  'From her own body she brought out greens, fruits and roots and fed the world till the rains came. She is <b>Śākambharī</b>, “she who bears the greens”.',
  'Durgama came with his army; she slew him and gave the Vedas back. She had foretold it in the Devī Māhātmya: she would slay the asura Durgama, and be famed as <b>Durgā Devī</b>.'],
 [('z','So “Durgā” means the one who killed Durgama?'),('b','That is her own reading. The word gives another: durgā, “hard to approach”, a fortress no evil enters. Together: what was impassable for us, she makes passable.')],
 'She ended the drought <b>and took the name of what she defeated</b>.'))
P_sukta2=(verse('sukta2','DURGĀ SŪKTA · VERSE 2','The fire-coloured Goddess',
 ['tām agnivarṇāṃ tapasā jvalantīṃ','vairocanīṃ karmaphaleṣu juṣṭām |','durgāṃ devīṃ śaraṇam ahaṃ prapadye','sutarasi tarase namaḥ ||'],
 svg(220,160,'The Goddess seen within the flame of a tall lamp, with a small boat crossing water below',
  '<rect width="220" height="160" fill="#20243a"/><path d="M0 130 q55 -10 110 0 t110 0 v30 h-220z" fill="#2a5a8a" stroke="none"/>'+g(40,136,.5,'<path d="M-24 0 h48 l-8 10 h-32z" fill="#c98a5a"/><path d="M0 0 v-26 l14 18z" fill="#fff8ec"/>')+g(140,128,.78,kaludipa(110,1))+'<path d="M140 18 q-28 30 0 52 q28 -22 0 -52z" fill="#ff8c1a" stroke="#e0501a" stroke-width="1.5" opacity=".85"/>'+g(140,62,.36,devi(items=(),halo='#ffd60a')),'#20243a'),
 'I take refuge in her: Durgā, the Goddess the colour of fire, blazing with the heat of her own austerity, the radiant one, sought for the fruit of everything we do. You who carry us across so surely, swift one, to you, salutation.',
 [('agni-varṇām','the colour of fire'),('tapasā jvalantīm','blazing with inner heat (tapas)'),('vairocanīm','the radiant, shining one'),('karma-phaleṣu juṣṭām','sought for the fruits of action'),('śaraṇam prapadye','I take refuge'),('sutarasi tarase','who carries across well, the swift')],
 '<b>Why a lamp.</b> The Durgā Sūkta, from the Mahānārāyaṇa Upaniṣad of the Kṛṣṇa Yajurveda, is sung to Agni and Durgā together; its first verse asks the fire to carry us across all difficulties, <i>durgāṇi</i>, like a boat over the sea. Many read the rite as this verse made visible: a fire-coloured Goddess honoured in a flame. (Interpretation.)',
 None,
 'The fire-coloured Mother <b>ferries us across</b>.',
 note='Text of the Durgā Sūkta (Mahānārāyaṇa Upaniṣad) as given on shlokam.org; Vedic accent marks omitted, and ē/ō written e/o. Verse numbered by its position in the hymn.'))
TOPL=lambda: g(170,120,1,mandala_top(84))
P_mandala=(reading('mandala','THE MAṆḌALA','A seat for the Goddess, drawn on the floor',
 S('Plan of a Durgā maṇḍala seen from above: outer square with four gates, a ring of eight lotus petals, a six-pointed star, and the lamp at the centre',
  TOPL()+'<path d="M262 40 L300 40" stroke="#111" stroke-width="1.5"/>'+txt(306,44,'four gates · four directions',11,'start',font='Noto Sans,sans-serif',weight='700')
  +'<path d="M232 92 L300 92" stroke="#111" stroke-width="1.5"/>'+txt(306,96,'eight-petalled lotus',11,'start',font='Noto Sans,sans-serif',weight='700')
  +'<path d="M196 118 L300 140" stroke="#111" stroke-width="1.5"/>'+txt(306,144,'six-pointed star',11,'start',font='Noto Sans,sans-serif',weight='700')
  +'<path d="M176 122 L300 188" stroke="#111" stroke-width="1.5"/>'+txt(306,192,'the lamp at the centre',11,'start',font='Noto Sans,sans-serif',weight='700')
  +lab(470,228,'simplified; designs vary',9),'#fffaf0',240),
 ['<b>A seat drawn on the floor.</b> Before anything else the ground is cleaned, traditionally with a wash that includes cow dung, and a maṇḍala is drawn in coloured powders: <b>raṅgavalli</b>, the same art as the rangoli at every Karnataka doorstep, raised here to a sacred plan. Many call it simply the <b>padma</b>, the lotus.',
  '<b>Its parts.</b> A common form has an outer square with a gate on each side for the four directions, a circle within it, an eight-petalled lotus, and at the heart a six-pointed star or a Devī yantra. Each family of priests has its own design, colours and proportions; there is no single correct drawing.',
  '<b>The centre.</b> At the very centre, the point called the <b>bindu</b>, stands the big lamp. Fresh red and maroon flowers are laid around it as her seat (āsana); smaller lamps are often set on the rim.',
  '<b>The colours.</b> Red, yellow, white, green and black powders are usual. Red, the Devī’s own colour, usually dominates.',
  '<b>What it means.</b> Many teachers read a maṇḍala as a map of the whole world folded to a point: the square of the earth, the lotus of unfolding life, the star where Śiva and Śakti meet, and the Goddess at the still centre. (Interpretation.)'],
 [('z','All that drawing, and it gets swept up afterwards?'),('b','That is part of the lesson. The seat is made with care, used with love and not clung to. What stays is what happened in you.')],
 'The world drawn as a lotus, <b>the Goddess at its centre</b>.'))
exec(open("dnp2.py").read())
build(i,'THE LAMP · THE LOTUS · THE MOTHER',
 covart('A tall brass lamp burning at the centre of a lotus maṇḍala, small lamps around it and red flowers',g(220,186,.6,mandala_floor(190,.34,140,10))+g(60,120,1.3,lotus('#c0392b','#8e1f17'))+g(380,120,1.3,lotus('#c0392b','#8e1f17'))),
 'The Mother invited into the lamp',
 'The <b>rite</b> step by step, the <b>stories</b> behind the name Durgā, the Vedic <b>Durgā Sūkta</b> to the fire-coloured Goddess, the maṇḍala and the lamp, and how the coast of Karnataka keeps it.',
 'Durgā Namaskāra Pūjā (Durgā Dīpa Namaskāra) explained and illustrated: the Goddess invoked in a lamp on a lotus maṇḍala, mātṛkā-nyāsa, the three forms, the Durgā Sūkta, how she got the name Durgā, the order of worship, when it is done, and the practice of Udupi, Kaṭīl and Mysuru.',pp)
print('pages',len(pp)+2)
