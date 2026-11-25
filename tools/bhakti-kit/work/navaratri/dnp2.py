# New pages for Durgā Namaskāra (exec'd from dnp.py)
from fig import mountain, conch, discus, bell, kalasha, book, vina, sword
from fig2 import fig_row
from fig3 import ganesha, arati, plate, coconut, banana, incense, lion
from fig import buffalo
NS='Noto Sans,sans-serif'
def T_(x,y,t,size=11,anchor='middle',fill='#111'): return txt(x,y,t,size,anchor,fill=fill,font=NS,weight='700',ls='.3')

P_name=reading('name','THE NAME','Durgā · dīpa · namaskāra',
 S('The word Durgā shown as a fortress with a gate, a lamp, and folded hands: the three parts of the name',
  g(110,150,1.3,fort())+T_(110,178,'DURGĀ · the fortress')+g(280,150,1.6,kaludipa(90,1))+T_(280,178,'DĪPA · the lamp')+g(450,150,1.4,namaste('#8e1f17'))+T_(450,178,'NAMASKĀRA · the bow'),'#fff3cf',190),
 ['<b>Durgā.</b> The usual explanation of the word is <i>dur-gā</i>, “hard to go to, hard to approach”: a fortress (<i>durga</i>) that no enemy can enter. The Goddess is that fortress for those who take refuge in her, and impassable for evil. The Devī Māhātmya adds a story: she earned the name by slaying the asura Durgama (told on its own page).',
  '<b>Dīpa.</b> Many priests and families say <b>Durgā Dīpa Namaskāra</b> or <b>Durgādīpa Namaskāra</b>, putting the lamp into the name. The Goddess worshipped is “Dīpa Durgā”, Durgā in the lamp.',
  '<b>Namaskāra.</b> <i>Namas</i> is the bow, the giving up of “I” before the deity; <i>namaskāra</i> is the act of bowing. One pūjā-service account says it directly: the salutation of Dīpa Durgā with these mantras is what is called Durgā Dīpa Namaskāra.',
  '<b>Other names.</b> In some places on the coast and in Kerala the same kind of lamp-and-maṇḍala worship of the Devī is called <b>Bhagavatī Sevā</b> or Bhagavatī Pūjā. Traditions differ on how far these are one rite or cousins.',
  '<b>Not Durgā Pūjā.</b> The name sounds close to Bengal’s Durgā Pūjā, but the two are different: no clay image, no immersion; a lamp, a drawn lotus and a night of salutations.'],
 [('z','So the whole name means “bowing to Durgā in the lamp”?'),('b','Exactly that. Three words, and each is a thing you can see on the floor: the fortress-Mother, the flame, and the people bowing.')],
 'Durgā, in the lamp, <b>saluted</b>.')

P_mahisha=story('mahisha','STORY · THE LIGHT OF ALL THE GODS','How Durgā was born, and Mahiṣāsura',
 strip('Three panels: light pouring out of the gods into one radiant form; the Goddess on her lion facing the buffalo-demon; the Goddess victorious with her trident',
  [panel([(god('#c0392b'),.7),(god('#e0a800'),.7),(god('#3a6ab8'),.7)],'#fff3cf'),
   ('<rect y="150" width="144" height="40" fill="#e9d6c0"/>'+g(46,150,.7,lion())+g(46,118,.55,devi(items=('sword','bow')))+g(108,152,.75,buffalo()),'#fde9c8'),
   panel([(devi(items=('trident','sword','discus','conch'),fierce=True),1.05)],'#f6e3e1')],
  ['the gods’ light','the battle','Mahiṣāsuramardinī']),
 'From the Devī Māhātmya, chapters 2–3, the middle movement of the text recited at Durgā Namaskāra.',
 ['The buffalo-demon <b>Mahiṣa</b> defeated the gods in a hundred-year war and took heaven for himself.',
  'The gods went to Viṣṇu and Śiva. As they told their story, a great light of anger poured out of every god, and the lights came together into one blazing form: <b>the Devī</b>.',
  'Each god gave her his weapon: Śiva the trident, Viṣṇu the discus, Varuṇa the conch, Indra the thunderbolt; the mountain Himavān gave her the lion.',
  'She rode into Mahiṣa’s armies. He changed shape, buffalo, lion, man with a sword, elephant, and back to buffalo; she saw through every form.',
  'She pinned him under her foot and struck him down with her trident and sword: she is <b>Mahiṣāsuramardinī</b>. Read it in full in '+L('/devi/devi-mahatmya/part-8/','Devī Māhātmya, Part 8')+'.'],
 [('z','She was made of all the gods’ light?'),('b','That is why a lamp suits her so well. A flame lit from many flames is still one flame.')],
 'All the gods’ light <b>in one flame</b>.')

P_three=reading('three','THREE MOTHERS IN ONE LAMP','Mahākālī, Mahālakṣmī, Mahāsarasvatī',
 S('Three goddesses, dark, red and white, standing around a single tall lamp',
  g(100,180,1.25,devi(skin='#3a3a50',sari='#1b1b1b',items=('sword','trident'),fierce=True,hair_open=True))+T_(100,196,'Mahākālī')+g(280,182,.95,kaludipa(110,1))+g(200,180,1.15,devi(sari='#c0392b',items=('lotus','discus')))+T_(200,196,'Mahālakṣmī')+g(400,180,1.15,devi(skin='#f6efe2',sari='#f4f1ea',items=('book','rosary')))+T_(400,196,'Mahāsarasvatī')+g(500,176,.55,vina()),'#f6e3e1',200),
 ['<b>Why three.</b> At Durgā Namaskāra the Goddess in the lamp is invoked in three forms: <b>Mahākālī, Mahālakṣmī and Mahāsarasvatī</b>. They are the presiding Goddesses of the three movements (caritas) of the Devī Māhātmya.',
  '<b>Mahākālī, the first movement.</b> As Yoganidrā, the sleep of Viṣṇu, she releases him to slay the demons <b>Madhu and Kaiṭabha</b> who threatened Brahmā. The dark power of the cosmic night. ('+L('/devi/devi-mahatmya/part-6/','Part 6')+')',
  '<b>Mahālakṣmī, the middle movement.</b> Born of the gods’ light, she slays <b>Mahiṣāsura</b>. The power of action and splendour. ('+L('/devi/devi-mahatmya/part-7/','Parts 7')+' and '+L('/devi/devi-mahatmya/part-8/','8')+')',
  '<b>Mahāsarasvatī, the last movement.</b> As Kauśikī, Kālī and Cāmuṇḍā she destroys <b>Śumbha and Niśumbha</b>, Caṇḍa, Muṇḍa and Raktabīja. The power of clear knowing. ('+L('/devi/devi-mahatmya/part-12/','Parts 12–15')+')',
  '<b>One flame.</b> The tradition is firm that they are not three goddesses but one Devī seen three ways, as dark, as red and as white. Many read them as the three qualities of nature, tamas, rajas and sattva, all held in the Mother. (Interpretation.)'],
 [('z','Three names, one lamp?'),('b','One flame. Look at it at night and it is dark around the wick, red in the middle, white at the tip. The lamp itself teaches the doctrine.')],
 'Dark, red, white: <b>one Mother</b>.')

P_sukta1=verse('sukta1','DURGĀ SŪKTA · VERSE 1','The boat across',
 ['jātavedase sunavāma somam','arātīyato nidahāti vedaḥ |','sa naḥ parṣadati durgāṇi viśvā','nāveva sindhuṃ duritātyagniḥ ||'],
 svg(220,160,'A boat with a flame at its prow crossing a rough sea',
  '<rect width="220" height="160" fill="#dfe9f6"/><path d="M0 110 q27 -14 55 0 t55 0 t55 0 t55 0 v50 h-220z" fill="#2a5a8a" stroke="none"/>'+g(110,112,1,boat())+g(150,104,1.1,flame(1))+'<path d="M20 30 l14 -10 l10 14 M170 26 l12 -8 l8 12" fill="none" stroke="#555" stroke-width="2"/>'),
 'To Jātavedas, the Fire who knows all that is born, let us press the soma. May he burn down what the hostile one plots. May that Fire carry us across all difficulties, as a boat carries across the sea, beyond all wrongs.',
 [('jāta-vedase','to the knower of all beings (Agni)'),('sunavāma somam','let us press the soma'),('nidahāti','may he burn away'),('parṣat ati durgāṇi viśvā','may he carry us across all hardships'),('nāvā iva sindhum','like a boat over the sea'),('durita ati','beyond all wrongs')],
 '<b>The hymn begins with fire.</b> The first verse is a Ṛgvedic mantra to Agni (Ṛgveda 1.99.1), and it sets the image that runs through the whole Durgā Sūkta: life as a sea of <i>durgāṇi</i>, hard passages, and the divine as the boat that carries us over. The next verse names the boat: Durgā.',
 None,
 'Life is a sea; <b>she is the boat</b>.',
 note='Text of the Durgā Sūkta (Mahānārāyaṇa Upaniṣad) as given on shlokam.org; Vedic accent marks omitted, ē/ō written e/o. The verse is also Ṛgveda 1.99.1.')

P_dm=verse('durge','DEVĪ MĀHĀTMYA 11.24','Protect us from fear',
 ['sarvasvarūpe sarveśe','sarvaśaktisamanvite |','bhayebhyastrāhi no devi','durge devi namo’stu te ||'],
 svg(220,160,'The Goddess with her hand raised in protection over a family with folded hands',
  '<rect width="220" height="160" fill="#f6e3e1"/>'+g(70,150,1.05,devi(items=('trident','abhaya')))+g(140,150,.9,namaste('#1d4f8a'))+g(178,150,.8,namaste('#8e1f17'))+g(200,150,.5,namaste('#e0a800'))),
 'You who are the form of everything, the Lady of all, endowed with every power: protect us from our fears, O Devī. O Durgā Devī, salutation to you.',
 [('sarva-svarūpe','whose form is everything'),('sarva-īśe','Lady of all'),('sarva-śakti-samanvite','endowed with every power'),('bhayebhyaḥ trāhi','protect from fears'),('durge devi','O Durgā, O Goddess'),('namaḥ astu te','salutation to you')],
 '<b>The namaskāra in one line.</b> In the gods’ hymn of chapter 11 nearly every verse ends “salutation to you”; this one names her Durgā and asks for freedom from fear. Its sister verse, <i>sarvamaṅgalamāṅgalye</i> (11.10), is among the most widely sung lines at any Devī pūjā. Read both on our '+L('/devi/devi-mahatmya/part-16/','Devī Māhātmya, Part 16')+' page.',
 None,
 'Every verse <b>ends in a bow</b>.',
 note='Text as on our Devī Māhātmya, Part 16 page (Aurobharati edition, numbering 11.24).')

def lamp_labeled():
    o=g(200,212,1.5,kaludipa(130,5))
    for y,t in [(30,'five wicks · five flames'),(52,'the bowl of oil or ghee'),(130,'the stem, with rings'),(206,'the broad base')]:
        o+=f'<path d="M262 {y} L320 {y}" stroke="#111" stroke-width="1.5"/>'+txt(326,y+4,t,11,'start',font=NS,weight='700')
    return o
P_lamp=reading('lamp','THE LAMP','The tall standing lamp at the centre',
 S('A tall five-wicked brass standing lamp with its parts labelled',lamp_labeled(),'#fff3cf',225),
 ['<b>A standing lamp.</b> The lamp at the centre is a tall brass or silver lamp on a stem, the kind kept in every coastal and Kannada home for festivals: in Kannada a <b>kālu-dīpa</b>, a footed lamp. A Kannada explainer describes exactly this: a kālu-dīpa set at the centre of the maṇḍala and decorated with flowers around it.',
  '<b>Wicks and oil.</b> It is filled with ghee or sesame oil and lit with one or several wicks; five-wicked lamps are common. It must burn steadily through the whole worship, so someone keeps watch to top it up.',
  '<b>From lamp to Goddess.</b> Before the invocation it is a lamp. After the āvāhana (invitation), the prāṇa-pratiṣṭhā (the gift of life) and the nyāsa, it is treated as Durgā herself: bathed with flowers, dressed, offered food, waved with lights and bowed to.',
  '<b>Why a lamp at all.</b> Light is the oldest image of the divine in Indian worship; the Durgā Sūkta calls her fire-coloured and blazing. A lamp also carries no single face, so all three forms can live in it at once. (Interpretation.)',
  '<b>Other lamps.</b> Smaller lamps often ring the maṇḍala, and in Kaṭīl and other coastal temples a related night worship, <b>raṅgapūjā</b>, uses rows of lamps on drawn patterns. See '+L('/tulunadu/temples/katil-durgaparameshwari/','Kaṭīl Durgāparameśvarī')+'.'],
 [('z','What if the lamp goes out in the middle?'),('b','That is why someone watches it the whole night. Most priests say: relight it quietly with a prayer and carry on. Fear is not the point of this worship; care is.')],
 'A household lamp <b>becomes the Mother</b>.')

P_items=cards('items','WHAT IS NEEDED','The things laid out before the worship',
 fig_row('A water pot, a coconut, flowers, incense, a lamp, a plate of offerings and a bell',[(kalasha(),1),(coconut(),1.3),(lotus('#c0392b','#8e1f17'),1.4),(incense(),1.2),(lamp(),1.5),(plate()+g(0,-4,.8,banana()),1.3),(bell(),1.3)],['kalaśa','coconut','flowers','incense','lamp','naivedya','bell'],gy=150),
 [('🪔','The lamp','The tall standing lamp, ghee or sesame oil, cotton wicks; small lamps for the rim.'),
  ('🎨','The maṇḍala','Coloured powders (red, yellow, white, green, black) for the raṅgavalli; a cleaned floor.'),
  ('🌺','Flowers and leaves','Fresh red and maroon flowers for her seat; leaves, tulasī and garlands.'),
  ('🟡','Turmeric, kuṅkuma, akṣata','Turmeric, kuṅkuma (vermilion), unbroken rice, sandal paste and perfume.'),
  ('🥥','Kalaśa and coconut','A water pot with mango leaves and a coconut; betel leaves and nuts.'),
  ('🍯','Naivedya','Fruits, sweets, the five sweet things (pañcakhādya), the household’s cooked offering.'),
  ('🔥','Incense and camphor','Incense sticks, dhūpa, camphor for the closing ārati.'),
  ('🔔','Bell and plates','A bell, ārati plate, small vessels for water and the offerings.')],
 [('z','That is a long list for a lamp.'),('b','Most of it is simply what you would put before an honoured guest. Families who cannot gather everything keep the lamp, the flowers and the sincerity.')],
 'Everything you would offer <b>an honoured guest</b>.',
 intro='A typical list, gathered from priests’ and pūjā-service lists in Karnataka. Families and priests differ; the priest usually brings the ritual items.')

def dikpala_fig():
    o=g(280,122,.9,mandala_top(84))
    pts=[('Indra · E',280,14),('Agni · SE',420,40),('Yama · S',480,122),('Nirṛti · SW',420,204),('Varuṇa · W',280,232),('Vāyu · NW',140,204),('Kubera · N',80,122),('Īśāna · NE',140,40)]
    for t,x,y in pts: o+=T_(x,y+4,t,11)
    return o
P_dik=reading('dikpalas','THE GUARDIANS AROUND HER','Gaṇapati, the kalaśa and the eight directions',
 S('The maṇḍala with the guardians of the eight directions named around it',dikpala_fig()+T_(490,238,'east at the top · arrangement varies',9),'#fffaf0',245),
 ['<b>First, the intention.</b> The worship opens like every formal pūjā: ācamana (sips of water), prāṇāyāma, and the <b>saṅkalpa</b>, the statement of who is worshipping, where, when, and for what. On the coast the family head usually makes it with the priest.',
  '<b>Gaṇapati and the kalaśa.</b> Gaṇapati is worshipped first so that the rite runs without obstacles, and a water pot (kalaśa) is set up and worshipped as the seat of the sacred waters. See our '+L('/home-puja/','simple home pūjā')+' for what each of these steps means.',
  '<b>The court of the Goddess.</b> Then the maṇḍala itself is honoured. Around its edge the <b>aṣṭa dikpālas</b>, the guardians of the eight directions, are invoked: Indra in the east, Agni in the south-east, Yama in the south, Nirṛti in the south-west, Varuṇa in the west, Vāyu in the north-west, Kubera in the north and Īśāna in the north-east.',
  '<b>Why the guardians.</b> They mark out the space as a whole world in small, closed on every side, before the queen of that world is invited to its centre. (Interpretation.)',
  '<b>Order varies.</b> Which deities are worshipped around the maṇḍala, and in what order, differs by priest and paddhati (ritual manual).'],
 [('z','Even Yama gets invited?'),('b','Every direction, and every power that keeps it. Nothing in her world is left outside her protection, not even death.')],
 'A whole world drawn, <b>guarded on all sides</b>.')

def letters_ring():
    ls=['a','ā','i','ī','u','ū','ṛ','ṝ','ḷ','e','ai','o','au','aṃ','aḥ','ka','kha','ga','gha','ṅa','ca','ja','ṭa','ta','pa','ma','ya','ra','la','va','śa','ṣa','sa','ha','ḷa','kṣa']
    o=''
    import math as m
    for k,t in enumerate(ls):
        a=m.radians(-90+k*360/len(ls)); o+=txt(280+180*m.cos(a),118+92*m.sin(a)+4,t,12,font=NS,weight='700',fill='#8e1f17' if k<16 else '#1d4f8a')
    return o
P_nyasa=reading('nyasa','MĀTṚKĀ-NYĀSA','The Goddess built out of letters',
 S('The Goddess in a flame, surrounded by a ring of the letters of the Sanskrit alphabet',letters_ring()+g(280,196,.85,kaludipa(110,1))+'<path d="M280 40 q-30 34 0 58 q30 -24 0 -58z" fill="#ff8c1a" stroke="#e0501a" opacity=".85"/>'+g(280,92,.36,devi(items=())),'#fff3cf',220),
 ['<b>The heart of the rite.</b> Every account of Durgā Namaskāra names one act above the others: <b>mātṛkā-nyāsa</b>. Durgā is invoked in the big lamp by placing the letters of the alphabet, one by one, on the parts of her form, so that every limb is worshipped with a different letter.',
  '<b>Mātṛkā.</b> The word means “little mother”, and it is the name for the letters of the Sanskrit alphabet, fifty or so, from <i>a</i> to <i>kṣa</i>. Śākta teaching holds that the letters are the Goddess as sound: everything that can be named comes out of them.',
  '<b>Nyāsa.</b> “Placing”. In nyāsa a syllable is set on a part of the body with a touch and a mantra. Here the priest places the letters on the Goddess in the lamp: the vowels on the head and face, the consonant groups on the limbs, in a fixed order. (A general description; the order differs between manuals.)',
  '<b>Not printed here.</b> The exact formulas, with their seed syllables, are taught from teacher to student and recited by the priest; this article describes them and does not give them.',
  '<b>What it says.</b> A Goddess made of the alphabet is a Goddess of speech, knowledge and all naming. Many read it this way: before we bow to her, we remember that every word we have ever spoken was hers. (Interpretation.)'],
 [('z','So the priest spells her out?'),('b','In a way. He places the whole alphabet on her, from the first sound to the last. When he is done, there is nothing sayable that is not her.')],
 'Every letter <b>a limb of the Mother</b>.')

P_offer=reading('offerings','THE OFFERINGS AND THE READINGS','Sixteen services and a night of recitation',
 S('A priest reading from a book before the lamp on the maṇḍala, devotees singing to one side',g(330,150,.58,mandala_floor(190,.34,130,8))+g(120,170,1.2,priest())+g(120,140,.7,book())+g(480,170,1,namaste('#8e1f17'))+g(530,170,.9,namaste('#1d4f8a')),'#fff3cf',195),
 ['<b>Sixteen services.</b> Once she is present in the lamp, Durgā is served as an honoured queen: water for the feet and hands, a bath (with flowers and sprinkled water), cloth, ornaments, turmeric and kuṅkuma, flowers, incense, lamp and food. This is the familiar <b>ṣoḍaśopacāra</b>, the sixteen services of any full pūjā.',
  '<b>Her names.</b> Kuṅkuma or flowers are offered while her names are recited: the 108 names (aṣṭottara) of Durgā, and in many homes the Lalitā Sahasranāma or the Lalitā Triśatī.',
  '<b>The Saptaśatī.</b> The Devī Māhātmya, “the seven hundred verses”, is recited in full or in part, often by several priests, with the Durgā Sūkta. Its three movements match the three forms invoked in the lamp.',
  '<b>Song.</b> In maṭhas and big gatherings bhajana groups sing devotional songs between the formal parts, and a scholar may speak about the Goddess.',
  '<b>Naivedya.</b> Food is offered last, with water sprinkled around it, before the closing rites.'],
 [('z','How long does all this take?'),('b','A few hours on one evening, more for a vow over several days. It is a night’s work, not a quick pūjā.')],
 'Served like a queen, <b>praised in her own scripture</b>.')

P_close=reading('namaskara','THE NAMASKĀRAS AND THE CLOSE','Bowing, ārati, prasāda and farewell',
 S('A devotee lying in full prostration before the lamp while another waves an ārati plate',g(360,160,.55,mandala_floor(190,.34,130,8))+g(130,170,1.3,prostrate())+g(232,128,.9,arati())+g(250,170,1,namaste('#1d4f8a')),'#fff3cf',190),
 ['<b>The bows.</b> The rite is named for its salutations, and it ends in them. After the offerings the family and the gathered devotees bow before the lamp, many in full prostration, <b>sāṣṭāṅga namaskāra</b> (“with eight limbs” touching the ground). Women often make the five-limbed bow, kneeling.',
  '<b>Pradakṣiṇā.</b> Circling clockwise around the maṇḍala or, where there is no room, turning in place.',
  '<b>Maṅgaḷārati.</b> The lamp-Goddess is waved with lights, camphor burning to nothing on the plate, with bells and a closing song. Then the ārati is taken: palms passed over the flame and touched to the eyes.',
  '<b>Prasāda.</b> Flowers, kuṅkuma and the offered food are given to all present as her grace. On the coast the evening usually ends with a meal.',
  '<b>Farewell.</b> The Goddess is respectfully asked to withdraw (visarjana) and pardon is begged for any fault in the worship. The maṇḍala, its work done, is later cleared. (Reported practice; details differ.)'],
 [('z','Why bow at the end and not at the start?'),('b','You bow at the start too. But by the end you have seen her served, sung and lit up for hours. The last bow is the one that comes by itself.')],
 'It ends as it is named: <b>in a bow</b>.')

P_when=cards('when','WHEN IT IS DONE','Nights, months and vows',
 S('A night sky with a moon over a house where a lamp burns on a maṇḍala',
  '<rect width="560" height="170" fill="#20243a"/>'+''.join(f'<circle cx="{(53*k)%560}" cy="{(29*k*k)%110+8}" r="1.5" fill="#fff8d0" stroke="none"/>' for k in range(1,24))+'<circle cx="470" cy="40" r="20" fill="#fff8d0"/>'+'<path d="M180 160 v-60 l100 -50 l100 50 v60z" fill="#c9a36b"/><rect x="230" y="104" width="100" height="56" fill="#3a2a1a"/>'+g(280,154,.27,mandala_floor(190,.34,130,8)),'#20243a',170),
 [('🌙','Navarātri','Above all in the nine nights of Śarad Navarātri, when maṭhas and temples hold it, often on Durgāṣṭamī or Mahānavamī. See '+L('/festivals/navaratri/','Navarātri')+'.'),
  ('🌧️','Āṣāḍha','The monsoon month of Āṣāḍha, Karkāṭaka (Āṭi) in the coastal solar calendar, is a favoured season.'),
  ('📅','Tuesdays and Fridays','The Devī’s weekdays; many start a vow on one of them.'),
  ('🌓','Tithis','Aṣṭamī, navamī, caturdaśī, pūrṇimā and amāvāsyā are named by different sources.'),
  ('🏠','Family occasions','A new house, a wedding, a vow fulfilled, or a hard time; often on the same day as a Gaṇahoma.'),
  ('🗓️','One night or many','Usually one evening; devoted families keep it as a vow of several days, up to twelve.')],
 [('z','So it can be done any time?'),('b','On a good day chosen with the priest. Navarātri is the great season, but a family in trouble does not wait for the calendar.')],
 'Navarātri above all, <b>and whenever the family needs her</b>.',
 intro='Sources and priests differ on the best days; these are the ones named most often. It is usually done in the evening or at night.')

def coast_map():
    o='<rect width="560" height="230" fill="#e9f2e1"/><path d="M0 0 h120 q-20 60 10 120 q-30 60 -10 110 h-120z" fill="#8fb8de" stroke="none"/>'+T_(50,120,'Arabian Sea',11,fill='#1d4f8a')
    pts=[('Mandārthi',230,42),('Uḍupi',190,78),('Kaṭīl',290,120),('Bappanāḍu',230,142),('Poḷali',330,170),('Maṅgaḷūru · Maṅgaḷādevī',230,206)]
    for t,x,y in pts: o+=g(x,y,.42,shrine())+txt(x+22,y-4,t,11,'start',font=NS,weight='700')
    o+=g(470,120,1,kaludipa(70,1))+T_(470,150,'the lamp in',10)+T_(470,163,'coastal homes',10)+T_(480,222,'simplified, not to scale',9)
    return o
P_coast=reading('coast','ON THE TUḶU COAST','Homes, maṭhas and the Durgā shrines',
 svg(560,230,'Simplified map of the Tuḷu coast with Durgā shrines at Mandārthi, Uḍupi, Kaṭīl, Bappanāḍu, Poḷali and Maṅgaḷūru',coast_map()),
 ['<b>A household rite.</b> In Uḍupi and Dakṣiṇa Kannaḍa, Durgā Namaskāra is above all something families do at home. A big family occasion may run from a Gaṇahoma in the morning through a Satyanārāyaṇa Pūjā in the afternoon to Durgā Namaskāra at night.',
  '<b>Maṭhas.</b> The Mādhva maṭhas of Uḍupi keep it as an annual Navarātri rite; the Pejavara Maṭha holds an annual Durgā Namaskāra even at its Mumbai branch. Uḍupi families who have moved to Bengaluru, Mysuru or Mumbai carry it with them.',
  '<b>A land of the Devī.</b> The coast is thick with great Durgā shrines: '+L('/tulunadu/temples/katil-durgaparameshwari/','Kaṭīl')+', '+L('/tulunadu/temples/mandarthi-durgaparameshwari/','Mandārthi')+', '+L('/tulunadu/temples/bappanadu-durgaparameshwari/','Bappanāḍu')+', '+L('/tulunadu/temples/polali-rajarajeshwari/','Poḷali')+' and '+L('/tulunadu/temples/mangaladevi/','Maṅgaḷādevī')+'. Their night worships with lamps and drawn patterns are close cousins of the household rite.',
  '<b>Raṅgavalli and night worship.</b> The coast’s love of drawn floor patterns, lamps and night-long devotion, seen also in '+L('/tulunadu/daiva/nagamandala/','Nāgamaṇḍala')+' and '+L('/tulunadu/culture/yakshagana/','Yakṣagāna')+', runs through Durgā Namaskāra too. (Our observation.)',
  '<b>Inland.</b> Mysuru keeps the Devī as Cāmuṇḍeśvarī on her hill and in the '+L('/festivals/navaratri/mysuru-dasara/','Mysuru Dasarā')+'; Durgā Namaskāra there is mostly the practice of coastal and Mādhva families. See '+L('/temples-of-india/around-mysuru/chamundeshwari/','Cāmuṇḍeśvarī')+'.'],
 [('z','Why is it so strong on the coast?'),('b','The coast is Devī country, with a great Durgā shrine every few miles and a priestly tradition in Uḍupi that keeps these rites alive in homes. Habits that live in homes last longest.')],
 'A home rite of <b>the Devī’s own coast</b>.')

P_katil=story('bees','STORY · THE MOTHER OF BEES','Kaṭīl’s Bhrāmarī and Aruṇāsura',
 strip('Three panels: the demon striking a rock with his sword; black bees bursting out of the rock; the Goddess seated in the middle of the river',
  [('<rect y="150" width="144" height="40" fill="#e9d6c0"/>'+g(46,150,1,demon('#3a2a5a'))+g(70,96,.6,sword())+g(106,152,.8,rock()),'#fde9c8'),
   ('<rect width="144" height="190" fill="#3a3a50"/>'+g(72,160,.9,rock())+g(72,110,1,bees(14,120,70)),'#3a3a50'),
   ('<rect width="144" height="190" fill="#dfe9f6"/><path d="M0 120 q36 -10 72 0 t72 0 v70 h-144z" fill="#2a5a8a" stroke="none"/>'+g(72,150,.8,rock())+g(72,118,.6,devi(items=('trident','lotus'))),'#dfe9f6')],
  ['the sword on the rock','the bees','Kaṭīlamma']),
 'The legend of '+L('/tulunadu/temples/katil-durgaparameshwari/','Kaṭīl Durgāparameśvarī')+', the great Durgā of the Tuḷu coast.',
 ['When the Goddess destroyed Śumbha and Niśumbha, their minister <b>Aruṇāsura</b> escaped and raised a new army.',
  'By penance he won from Brahmā a boon that no creature with <b>two legs or four</b> could kill him.',
  'The Goddess came to him as a beautiful woman and vanished into a rock. In rage he struck the rock with his sword.',
  'Out of the rock burst a swarm of black bees, <b>bhramaras</b>. Bees have six legs; the boon could not protect him, and they stung him to death. She is <b>Bhrāmarī</b>.',
  'At the gods’ prayer she stayed in the middle of the river Nandinī as the rock-born <b>Durgāparameśvarī</b> of Kaṭīl.'],
 [('z','What does a bee story have to do with a lamp pūjā?'),('b','Both are the coast’s Durgā: a Mother who comes in the smallest, plainest form, a bee, a flame, and is more than a match for any demon.')],
 'The smallest form, <b>the surest victory</b>.')

P_meaning=reading('meaning','WHAT IT MEANS','Readings of teachers and devotees',
 S('A devotee seated in meditation with a small flame glowing in the heart',g(280,178,2.2,heart())+g(280,150,1.4,namaste('#8e1f17'))+g(280,108,.9,flame(1.3)),'#f6e3e1',200),
 ['<b>The Goddess as light.</b> The simplest reading: the Mother is the light by which everything is seen. To worship her in a flame is to worship the seeing itself. (Interpretation.)',
  '<b>Crossing over.</b> The Durgā Sūkta’s image, the boat over the sea of difficulties, is what families come with: illness, debt, quarrels, fear. The rite says: you do not have to swim; take refuge, and be carried. (Interpretation.)',
  '<b>The world in a lotus.</b> The maṇḍala draws the whole world with the Goddess at its still centre, guarded on every side. Teachers read it as the shape of a centred life. (Interpretation.)',
  '<b>Made of speech.</b> Mātṛkā-nyāsa makes her out of the alphabet. Every word is hers; speaking carefully is a form of worship. (Interpretation.)',
  '<b>The bow.</b> The rite is named not for what is offered but for the bow. Whatever else is done, the essence is the surrender in “namaḥ”: not I, but you.'],
 [('z','Which reading is right?'),('b','Take the one that carries you across. They all point at the same flame.')],
 'Light, refuge, a centre, a word, <b>a bow</b>.')

P_words=cards('glossary','WORDS TO KNOW','The vocabulary of this guide',
 fig_row('A lamp, a lotus maṇḍala, folded hands and a letter',[(kaludipa(70,1),1),(mandala_top(30),1),(namaste('#8e1f17'),1),(lotus('#c0392b','#8e1f17'),1.3)],['dīpa','maṇḍala','namaskāra','padma'],h=140),
 [('🪔','Dīpa · kālu-dīpa','Lamp; a tall footed standing lamp.'),('🎨','Maṇḍala · raṅgavalli','The sacred diagram drawn in coloured powders.'),('🔤','Mātṛkā-nyāsa','Placing the letters of the alphabet on the Goddess’s form.'),('🙏','Namaskāra','Bow, salutation; sāṣṭāṅga is the full prostration.'),('🧭','Aṣṭa dikpālas','Guardians of the eight directions.'),('📜','Saptaśatī','The Devī Māhātmya, “seven hundred verses”.'),('📣','Saṅkalpa · āvāhana','The statement of intent; the invitation of the deity.'),('🔥','Visarjana','The respectful farewell at the end.')],
 None,'Words <b>to keep</b>.')

P_end=end(i,['<b>What.</b> Durgā invoked in a tall lamp at the centre of a drawn lotus maṇḍala, and saluted through a night of worship.',
 '<b>Name.</b> Durgā, the fortress-Mother who slew Durgama; dīpa, the lamp; namaskāra, the bow.',
 '<b>Rite.</b> Saṅkalpa, Gaṇapati, kalaśa, the guardians, mātṛkā-nyāsa, sixteen services, the Saptaśatī and Durgā Sūkta, bows, ārati, prasāda, farewell.',
 '<b>When.</b> Navarātri above all; Āṣāḍha, Tuesdays and Fridays, family occasions and vows.',
 '<b>Where.</b> The homes and maṭhas of the Tuḷu coast, and Uḍupi families everywhere.'],
 'Read the Goddess’s own coast in '+L('/tulunadu/temples/','Temples of Tulu Nadu')+', and her scripture in the '+L('/devi/devi-mahatmya/','Devī Māhātmya')+'.','Durgā Namaskāra Pūjā')

P_src=sources([
 ('The rite:','Descriptions of Durgā (Dīpa) Namaskāra by temple and pūjā-service sources in Karnataka: Poornaprajna Kshetra; SmartPuja (blog and service page); Harivara; PujanPujari; 99Pandit; AstroPuja (Bhagavatī Pūjā, Uḍupi); a Kannada news explainer (Public TV) on the coastal household practice and the kālu-dīpa; Daijiworld report on the annual Durgā Namaskāra at the Pejavara Maṭha, Mumbai.'),
 ('Scripture:','Durgā Sūkta from the Mahānārāyaṇa Upaniṣad (shlokam.org); its first verse is also Ṛgveda 1.99.1. Devī Māhātmya 11.24, 11.10 and 11.49–50, chapters 2–3, as on our '+L('/devi/devi-mahatmya/','Devī Māhātmya')+' series (devimahatmyam.aurobharati.in). Śākambharī and Durgama: Devī Bhāgavata Purāṇa 7.28 (summarised from Wikipedia, “Shakambhari”).'),
 ('Kaṭīl:','As in our '+L('/tulunadu/temples/katil-durgaparameshwari/','Kaṭīl Durgāparameśvarī')+' guide.')],
 'no classical manual for Durgā Namaskāra was found online; the order of rites, the maṇḍala design, the number of lamps and wicks, which texts are recited, the days preferred and the length of vows all differ by family, priest and maṭha, and are given here as commonly reported. The cleaning wash, the women’s five-limbed bow, the clearing of the maṇḍala afterwards, and “Bhagavatī Sevā” as another name are reported, not checked across traditions. Readings of the lamp, the three forms, the guardians and the letters are interpretation.',
 'Durgā Sūkta: Mahānārāyaṇa Upaniṣad, text as on shlokam.org, accents omitted; Devī Māhātmya numbering as in the Aurobharati edition.')

pp=[P_fw,P_gl,P_what,P_name,P_durgama,P_mahisha,P_three,P_sukta1,P_sukta2,P_dm,P_mandala,P_lamp,P_items,P_dik,P_nyasa,P_offer,P_close,P_when,P_coast,P_katil,P_meaning,P_words,P_end,P_src]
