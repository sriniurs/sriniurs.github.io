from data import talk,svg,T,LINGA
import math
D=dict
def ring(items,cx=110,cy=84,r=56,fs=9):
    o=''
    for k,(t,c) in enumerate(items):
        a=-math.pi/2+2*math.pi*k/len(items); x=cx+r*math.cos(a); y=cy+r*math.sin(a)
        o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="15" fill="{c}" stroke="#111" stroke-width="2"/><text x="{x:.0f}" y="{y+3:.0f}" text-anchor="middle" font-family="Bangers" font-size="{fs}">{t}</text>'
    return o
V=[
D(theme='HALF OF HIS BODY',
 svg=svg('Ardhanarishvara: a figure half Shiva in blue with matted hair and half Parvati in pink with jewels, and a small heap of ash at the side',
  '<g stroke="#111" stroke-width="2.5"><path d="M110 30 a20 20 0 0 0 0 40z" fill="#bcd4f0"/><path d="M110 30 a20 20 0 0 1 0 40z" fill="#f2c79b"/><path d="M110 70 v0 l-26 80 h26z" fill="#1d4f9a"/><path d="M110 70 l26 80 h-26z" fill="#e05a8a"/></g><path d="M110 26 v130" stroke="#111" stroke-width="1.5" stroke-dasharray="3 3"/>'
  '<path d="M92 26 q-6 -14 6 -16 q4 10 -6 16z" fill="#c9a26b" stroke="#111" stroke-width="1.5"/><circle cx="124" cy="22" r="5" fill="#ffd60a" stroke="#111"/>'
  '<ellipse cx="190" cy="148" rx="18" ry="5" fill="#999"/><text x="190" y="136" text-anchor="middle" font-family="Bangers" font-size="9">KĀMA\'S ASH</text><text x="60" y="20" text-anchor="middle" font-family="Bangers" font-size="10">ŚIVA</text><text x="166" y="20" text-anchor="middle" font-family="Bangers" font-size="10">PĀRVATĪ</text>'),
 mean='O destroyer of the cities, the Goddess saw Kāma, who took up his bow trusting in her beauty, burnt before her in an instant like straw. If she still thinks You are a slave to a woman, because You, devoted to self-restraint, joined her to half Your body: ah, O giver of boons, young women are innocent indeed!',
 plain='Pārvatī saw Śiva burn Kāma to ash. Yet because Śiva made her half of His body, she thinks He is ruled by love for her. The poet smiles: He is the master yogī; how innocent she is!',
 words=[('sva-lāvaṇya-āśaṃsā','<b>hoping through her own beauty</b>'),('puṣpāyudha','<b>the flower-armed one</b>: Kāma'),('pluṣṭam','<b>burnt</b>'),('straiṇam','<b>ruled by a woman</b>'),('dehārdha-ghaṭanāt','<b>because of joining (her) to half His body</b>'),('mugdhāḥ yuvatayaḥ','<b>young women are innocent</b>')],
 deep='<p><b>A gentle joke.</b> This is one of the playful verses. Pārvatī watched Kāma, the god of love who was helping her cause, burnt to ash by Śiva\'s third eye. Then Śiva made her half His own body as Ardhanārīśvara. She concludes He is lovestruck. The poet teases: You, who burnt love itself, a slave to love?</p><p><b>Two truths at once.</b> Śiva is both: the yogī who is free of desire, and the Lord who is never apart from Śakti. The verse holds them together with a smile.</p><p><b>Ardhanārīśvara.</b> The image of the Lord who is half woman expresses that Śiva and Śakti, consciousness and energy, are one.</p>',
 cards=('💡 Ardhanārīśvara','"The Lord who is half woman": Śiva and Pārvatī in one body.','💡 Puṣpāyudha','"Flower-weaponed": Kāma, whose bow is sugarcane and arrows flowers.'),
 inner='Love that is free of craving is still love. The yogī and the lover can be the same heart.',
 talk=('The hymn is teasing Pārvatī?','Gently. She thinks He\'s ruled by love; He burnt love to ash. Both are true: He is free, and He is never without her.'),
 key='The one who burnt desire <b>keeps Pārvatī as half of Himself</b>.'),
D(theme='INAUSPICIOUS, AND THE MOST AUSPICIOUS',
 svg=svg('A cremation ground at night with a funeral pyre, ash and a garland of skulls, and a crescent moon shining over a calm linga',
  '<rect width="220" height="160" fill="#1a1530"/><path d="M190 20 a12 12 0 1 0 8 18 a9 9 0 1 1 -8 -18z" fill="#fff6b0"/>'
  '<path d="M20 130 h70 l-6 10 h-58z" fill="#7a5a3a" stroke="#111" stroke-width="2"/><path d="M36 130 q10 -30 20 -10 q10 -24 18 10" fill="#ff8c1a" stroke="#111" stroke-width="1.5"/>'
  +''.join(f'<circle cx="{120+14*i}" cy="{70+6*abs(i-2)}" r="6" fill="#eee" stroke="#111" stroke-width="1.5"/>' for i in range(5))
  +f'<g transform="translate(150 140)">{LINGA}</g><text x="110" y="24" text-anchor="middle" font-family="Bangers" font-size="11" fill="#ffd60a">ŚIVAM · AUSPICIOUS</text>'),
 mean='You play in cremation grounds, O destroyer of Kāma; ghouls are Your companions; the ash of funeral pyres is Your ointment; even Your garland is a string of human skulls. Let all Your ways be inauspicious, then. Yet for those who remember You, O giver of boons, You are the supreme auspiciousness.',
 plain='Śiva lives among the dead, smears Himself with pyre ash and wears skulls. Everything about Him looks unlucky. Yet for anyone who remembers Him, He is the most auspicious of all.',
 words=[('śmaśāna','the <b>cremation ground</b>'),('piśācāḥ sahacarāḥ','<b>ghouls are Your companions</b>'),('citā-bhasma','<b>ash of the funeral pyre</b>'),('nṛ-karoṭī','<b>human skulls</b>'),('amaṅgalya','<b>inauspicious</b>'),('paramaṃ maṅgalam','<b>supreme auspiciousness</b>')],
 deep='<p><b>The great paradox.</b> Śiva\'s very name means "auspicious", yet He is pictured in the most inauspicious place of all, the burning ground. The verse grants the objection completely, "let all Your ways be inauspicious", and then turns it over.</p><p><b>Why the cremation ground?</b> It is where every pretence ends: wealth, status, body. The Lord who dwells there is the one who remains when everything else is burnt. Ash is what is left when all that changes has gone.</p><p><b>Smartṝṇām.</b> "For those who remember": the blessing is not in His surroundings but in our remembering Him.</p>',
 cards=('💡 Bhasma','Sacred ash worn by Śaivas: a reminder that all bodies end as ash.','💡 Kāśī','The great cremation ghāṭ, Maṇikarṇikā, is in Śiva\'s own city; see our Kāśī guide.'),
 inner='What looks fearful may be the doorway to freedom. The place where everything ends is where the One who never ends is found.',
 talk=('Skulls and ash, and He\'s the most auspicious?','That\'s the hymn\'s point. Outer appearances don\'t decide holiness. Remembering Him does.'),
 key='Inauspicious in looks, <b>supremely auspicious to all who remember Him</b>.'),
D(theme='THE YOGĪ\'S INNER LAKE',
 svg=svg('A yogi seated in meditation with eyes closed, a glowing light in the heart, sitting by a calm lake of nectar',
  '<rect x="0" y="120" width="220" height="40" fill="#9fd3f0"/><g stroke="#111" stroke-width="2.5"><circle cx="110" cy="46" r="14" fill="#f2c79b"/><path d="M70 120 q40 -70 80 0z" fill="#ff8c1a"/><path d="M78 120 h64" /></g>'
  '<path d="M104 46 h4 M112 46 h4" stroke="#111" stroke-width="2"/><circle cx="110" cy="90" r="9" fill="#ffd60a" stroke="#ff8c1a" stroke-width="2"/><circle cx="110" cy="90" r="18" fill="#ffd60a" opacity=".3"/>'
  '<text x="110" y="148" text-anchor="middle" font-family="Bangers" font-size="11" fill="#1d4f9a">A LAKE OF NECTAR</text><text x="110" y="20" text-anchor="middle" font-family="Bangers" font-size="11">WITHIN</text>'),
 mean='Drawing the mind inward and setting it in the heart, holding the breath as the scriptures teach, their hair standing on end with joy, their eyes brimming with tears of bliss: the yogīs see some inner reality and delight in it, as if plunged into a lake of nectar. That, surely, is You.',
 plain='Yogīs turn their minds inward, still the breath, and find a joy so deep they shiver and weep, like diving into a lake of nectar. What they find within is Śiva.',
 words=[('pratyak','<b>turned inward</b>'),('ātta-marutaḥ','<b>holding the breath</b>'),('prahṛṣyad-romāṇaḥ','<b>hair thrilling with joy</b>'),('pramada-salila','<b>tears of bliss</b>'),('hrada iva amṛtamaye','<b>as in a lake of nectar</b>'),('yaminaḥ','the <b>self-controlled</b>, yogīs')],
 deep='<p><b>From outer to inner.</b> Verses 23–24 showed Śiva\'s strange outer appearance; verse 25 turns within. The yogī withdraws the senses, settles the mind in the heart, and controls the breath (<i>prāṇāyāma</i>).</p><p><b>Signs of bliss.</b> Hair standing on end, tears of joy: the bodily signs of deep devotion and absorption, described in many traditions.</p><p><b>"That is You."</b> <i>Tat kila bhavān</i>: the reality the yogī meets inside is not something other than Śiva. The God of the cremation ground and the light in the heart are one.</p>',
 cards=('💡 Prāṇāyāma','Regulation of breath, a limb of yoga, used to steady the mind.','💡 Nirvāṇa Ṣaṭkam','Śaṅkara\'s "cidānanda-rūpaḥ śivo\'ham" describes the same inner Śiva.'),
 inner='The deepest temple is inside you. Turn the mind inward, and the lake of nectar is already there.',
 talk=('Why do the yogīs cry?','From joy, says the hymn. What they find inside is so sweet it overflows. And that sweetness is Śiva.'),
 key='The bliss the yogīs find within <b>is Śiva Himself</b>.'),
D(theme='YOU ARE EVERYTHING',
 svg=svg('Eight forms in a ring: sun, moon, wind, fire, water, sky, earth and the self, around a central linga',
  ring([('SUN','#ffd60a'),('MOON','#eee'),('WIND','#cfe3f5'),('FIRE','#ff8c1a'),('WATER','#4aa3df'),('SKY','#dcecff'),('EARTH','#9fae78'),('SELF','#f2c79b')],r=60,fs=8)
  +f'<g transform="translate(110 96) scale(.7)">{LINGA}</g>'),
 mean='"You are the sun, You are the moon, You are the wind, You are fire; You are the waters, You are space, You are the earth, and You are the Self": so the wise speak of You in such limited words. But we do not know any reality here that You are not.',
 plain='The wise list Śiva\'s eight forms: sun, moon, wind, fire, water, space, earth and Self. The poet says even that list is too small: there is nothing that He is not.',
 words=[('arkaḥ · somaḥ','<b>sun</b> · <b>moon</b>'),('pavanaḥ · hutavahaḥ','<b>wind</b> · <b>fire</b>'),('āpaḥ · vyoma','<b>waters</b> · <b>space</b>'),('dharaṇiḥ · ātmā','<b>earth</b> · <b>the Self</b>'),('paricchinnām giram','<b>limited speech</b>'),('yat tvaṃ na bhavasi','<b>that which You are not</b>')],
 deep='<p><b>Aṣṭamūrti.</b> The eight forms of Śiva: the five elements (earth, water, fire, wind, space), the sun, the moon and the sacrificer or Self. Kālidāsa opens his play <i>Śākuntalam</i> with a prayer to this eightfold Śiva.</p><p><b>The poet\'s correction.</b> Even this grand list is <i>paricchinna</i>, "limited". Saying "You are eight things" still leaves things out. So the poet turns it around: we know nothing that You are not.</p><p><b>Everything is Śiva.</b> The verse moves from naming forms to the Upaniṣadic vision that all is the Lord.</p>',
 cards=('💡 Aṣṭamūrti','The eight-formed Śiva; a famous temple tradition and Kālidāsa\'s opening prayer.','💡 Pañca-bhūta','The five elements; the South has a famous temple for each (a future series).'),
 inner='Look at the sun, the rain, the earth, your own self: you are looking at Him. There is nowhere He is not.',
 talk=('Eight forms isn\'t enough?','The poet says any list is too short. Name eight, name eight thousand: there\'s still nothing He isn\'t.'),
 key='Not eight forms only: <b>there is nothing He is not</b>.'),
D(theme='THE SYLLABLE OṂ',
 svg=svg('The letters A, U and M with their meanings, and a fourth silent dot above standing for the fourth state',
  ''.join(f'<rect x="{12+68*i}" y="60" width="60" height="56" rx="8" fill="{c}" stroke="#111" stroke-width="2.5"/><text x="{42+68*i}" y="94" text-anchor="middle" font-family="Bangers" font-size="22">{t}</text><text x="{42+68*i}" y="132" text-anchor="middle" font-family="Bangers" font-size="9">{s}</text>' for i,(t,c,s) in enumerate([('A','#ffe3c4','WAKING · ṚG'),('U','#dcecff','DREAM · YAJUS'),('M','#ece0fa','SLEEP · SĀMA')]))
  +'<circle cx="110" cy="26" r="8" fill="#ffd60a" stroke="#111" stroke-width="2"/><path d="M90 40 q20 10 40 0" fill="none" stroke="#111" stroke-width="2.5"/><text x="160" y="30" font-family="Bangers" font-size="10" fill="#c0392b">TURĪYA</text>'),
 mean='Through its three letters, beginning with A, the word Oṃ names the three Vedas, the three states, the three worlds and the three gods; and with its subtle after-sound it points to Your fourth state, beyond all change. So, O giver of refuge, the word Oṃ praises You both as the whole and in Your parts.',
 plain='Oṃ is made of A, U and M, which stand for every set of three: the Vedas, waking-dream-sleep, the three worlds, the three gods. The silence after it is the fourth state, beyond all. So Oṃ is the whole of Śiva.',
 words=[('trayī','the <b>three Vedas</b>'),('tisraḥ vṛttīḥ','the <b>three states</b>: waking, dream, deep sleep'),('akārādyaiḥ varṇaiḥ','<b>by the letters beginning with A</b>'),('turīyam dhāma','the <b>fourth state</b>'),('dhvanibhiḥ aṇubhiḥ','<b>by subtle sounds</b>'),('samasta-vyasta','<b>whole and in parts</b>')],
 deep='<p><b>The Māṇḍūkya teaching.</b> The Māṇḍūkya Upaniṣad says the syllable Oṃ is all this. Its parts A, U and M are the waking, dreaming and deep-sleep states; the silence beyond them is <b>turīya</b>, "the fourth", pure consciousness.</p><p><b>Sets of three.</b> The verse lines up every triad with A-U-M: the three Vedas, the three worlds (earth, sky, heaven), the three gods (Brahmā, Viṣṇu, Rudra).</p><p><b>Whole and parts.</b> <i>Samasta-vyasta</i>: Oṃ praises Śiva in His parts (each letter) and as a whole (the full syllable and its silence).</p>',
 cards=('💡 Turīya','"The fourth": the witness-consciousness underlying waking, dream and sleep.','💡 Praṇava','A name for Oṃ: the sacred syllable that begins and ends Vedic chanting.'),
 inner='Oṃ ends in silence. The fullest prayer is the quiet after the sound.',
 talk=('Oṃ has four parts, not three?','Three letters, and then the silence. That silence, the hymn says, is Śiva\'s own state.'),
 key='A, U, M and the silence: <b>Oṃ is the whole of Śiva</b>.'),
D(theme='THE EIGHT NAMES',
 svg=svg('Eight names of Shiva in a ring around a central linga: Bhava, Sharva, Rudra, Pashupati, Ugra, Mahadeva, Bhima, Ishana',
  ring([('BHAVA','#ffe3c4'),('ŚARVA','#dcecff'),('RUDRA','#ffe0e0'),('PAŚUPATI','#ddf5ea'),('UGRA','#ffd6a0'),('MAHĀN','#ece0fa'),('BHĪMA','#e0e0e0'),('ĪŚĀNA','#fff3b0')],r=60,fs=7)
  +f'<g transform="translate(110 96) scale(.7)">{LINGA}</g>'),
 mean='Bhava, Śarva, Rudra, Paśupati, and Ugra, with Mahādeva, and also Bhīma and Īśāna: this group of eight names; and the Veda itself dwells on each of them, O God. To You, the beloved, the supreme abode, I offer my salutation.',
 plain='Śiva\'s eight great names: Bhava, Śarva, Rudra, Paśupati, Ugra, Mahādeva, Bhīma, Īśāna. The Veda praises each. I bow to the beloved Lord they all name.',
 words=[('bhavaḥ','<b>Existence</b>, the source'),('śarvaḥ','the <b>Archer</b>, destroyer'),('rudraḥ','the <b>Roarer</b>, who removes sorrow'),('paśupatiḥ','<b>Lord of beings</b> (paśus)'),('ugraḥ · bhīmaḥ','the <b>Fierce</b> · the <b>Terrible</b>'),('mahān · īśānaḥ','the <b>Great God</b> · the <b>Ruler</b>')],
 deep='<p><b>An old list.</b> These eight names go back to the Vedic period: the Śatapatha Brāhmaṇa tells how the newborn Rudra was given eight names, and the Atharva Veda and the Śrī Rudram use many of them.</p><p><b>Gentle and fierce.</b> The names alternate: Bhava (existence) and Śarva (destroyer), Paśupati (protector) and Ugra (fierce), Mahādeva (great god) and Bhīma (terrible). Śiva is all of them at once.</p><p><b>Matching the eight forms.</b> Tradition links the eight names with the eight forms of verse 26: Bhava with water, Śarva with earth, Rudra with fire and so on.</p>',
 cards=('💡 Paśupati','"Lord of all creatures"; the name of the great temple in Kathmandu and of the Pāśupata school.','💡 Śrī Rudram','Many of these names recur in the Namakam; see our Rudram series.'),
 inner='Fierce and gentle, near and far: every name is a door. Use whichever opens your heart.',
 talk=('Why eight names?','An ancient Vedic set. Some are gentle, some fierce. Together they make one Lord.'),
 key='Eight names from the Veda, <b>one beloved Lord</b>.'),
D(theme='NEAREST AND FARTHEST',
 svg=svg('Opposites: a small dot and a huge circle, a child and an old man, near and far, all bowed to',
  '<circle cx="50" cy="56" r="4" fill="#111"/><circle cx="160" cy="56" r="40" fill="none" stroke="#111" stroke-width="3"/><text x="50" y="86" text-anchor="middle" font-family="Bangers" font-size="10">SMALLEST</text><text x="160" y="110" text-anchor="middle" font-family="Bangers" font-size="10">GREATEST</text>'
  '<g stroke="#111" stroke-width="2"><circle cx="40" cy="124" r="7" fill="#f2c79b"/><path d="M32 150 q8 -18 16 0z" fill="#4aa3df"/><circle cx="90" cy="118" r="9" fill="#f2c79b"/><path d="M78 150 q12 -26 24 0z" fill="#999"/></g><text x="64" y="158" text-anchor="middle" font-family="Bangers" font-size="9">YOUNGEST · OLDEST</text><text x="170" y="150" text-anchor="middle" font-family="Bangers" font-size="13" fill="#c0392b">NAMAḤ!</text>'),
 mean='Salutation to You, the nearest, and salutation to You, the farthest, O lover of the wilderness; salutation to You, the smallest, and to You, the greatest, O destroyer of Kāma; salutation to the oldest and to the youngest, O three-eyed one; salutation to You who are all this, and salutation to You who are beyond all.',
 plain='I bow to You, nearest and farthest, smallest and greatest, oldest and youngest; You who are everything, and beyond everything.',
 words=[('nediṣṭha · daviṣṭha','<b>nearest</b> · <b>farthest</b>'),('kṣodiṣṭha · mahiṣṭha','<b>smallest</b> · <b>greatest</b>'),('varṣiṣṭha · yaviṣṭha','<b>oldest</b> · <b>youngest</b>'),('priyadava','<b>lover of the wild</b>, of solitude'),('sarvasmai','<b>to the All</b>'),('atisarvāya','<b>to the One beyond all</b>')],
 deep='<p><b>Pairs of opposites.</b> Every line bows to two extremes at once, using Sanskrit superlatives ("-iṣṭha", "-most"). Śiva is the nearest (within the heart) and the farthest (beyond the universe); smaller than an atom and larger than space; older than time and ever young.</p><p><b>An Upaniṣadic echo.</b> The Kaṭha Upaniṣad says the Self is "smaller than the small, greater than the great"; the Īśa Upaniṣad that it is "far and near".</p><p><b>All, and beyond all.</b> The last line holds the whole hymn: Śiva is everything (<i>sarva</i>), and also beyond everything (<i>atisarva</i>).</p>',
 cards=('💡 Aṇoraṇīyān','"Smaller than the small, greater than the great": Kaṭha Upaniṣad 1.2.20.','💡 Namaskāra','This verse is often chanted alone as a short prayer of salutation.'),
 inner='Look for Him far away and you\'ll find Him near. Make Him small and He grows beyond the sky.',
 talk=('How can He be nearest and farthest?','Nearest, because He\'s your own Self; farthest, because no mind can reach His end. The verse bows to both.'),
 key='Nearest and farthest, all and beyond all: <b>namaḥ</b>.'),
D(theme='BEYOND THE THREE GUṆAS',
 svg=svg('Three coloured circles for rajas, tamas and sattva with Bhava, Hara and Mrida, and a fourth white glowing circle above for Shiva beyond them',
  ''.join(f'<circle cx="{x}" cy="114" r="24" fill="{c}" stroke="#111" stroke-width="2.5"/><text x="{x}" y="112" text-anchor="middle" font-family="Bangers" font-size="10">{a}</text><text x="{x}" y="124" text-anchor="middle" font-family="Bangers" font-size="8">{b}</text>' for x,c,a,b in [(44,'#e63946','BHAVA','RAJAS'),(110,'#5a5a7a','HARA','TAMAS'),(176,'#f5f5f5','MṚḌA','SATTVA')])
  +'<circle cx="110" cy="36" r="24" fill="#ffd60a" stroke="#111" stroke-width="2.5"/><circle cx="110" cy="36" r="34" fill="#ffd60a" opacity=".3"/><text x="110" y="40" text-anchor="middle" font-family="Bangers" font-size="12">ŚIVA</text>'),
 mean='Salutations again and again to Bhava, full of rajas, at the creation of the universe; salutations again and again to Hara, strong in tamas, at its dissolution; salutations again and again to Mṛḍa, rich in sattva, who brings happiness to people; salutations again and again to Śiva, in the radiant state beyond the three qualities.',
 plain='I bow to Śiva as Bhava who creates (rajas), Hara who dissolves (tamas), Mṛḍa who brings joy (sattva), and to Śiva, the pure light beyond all three.',
 words=[('bahula-rajase','<b>full of rajas</b>, activity'),('prabala-tamase','<b>strong in tamas</b>, rest'),('sattvodriktau','<b>abundant in sattva</b>, clarity'),('mṛḍa','the <b>Gracious</b>, giver of joy'),('nistraiguṇye','<b>beyond the three guṇas</b>'),('pramahasi pade','<b>in the radiant state</b>')],
 deep='<p><b>Back to verse 4.</b> In Part 1, verse 4 described one power working through three forms. Here the same idea becomes a chant: each line ends <i>namo namaḥ</i>.</p><p><b>The fourth line.</b> After the three working forms comes the fourth: Śiva <i>nistraiguṇya</i>, beyond all three qualities, pure radiance. Like the silence after Oṃ in verse 27, the fourth is the truest.</p><p><b>A new metre.</b> This verse changes rhythm (<i>hariṇī</i>), and verses 31–32 change again (<i>mālinī</i>): a sign that the hymn is moving toward its close.</p>',
 cards=('💡 Mṛḍa','"The gracious": a Vedic name of Rudra, as in "mṛḍayā naḥ", be gracious to us.','💡 Nirguṇa','"Beyond qualities": the Absolute, beyond sattva, rajas and tamas.'),
 inner='We meet God in creation, in endings and in joy. Beyond them all, He is simply light.',
 talk=('Four lines, four Śivas?','Three faces at work, and one beyond all work. The last is the truest Śiva, the hymn says.'),
 key='Creator, destroyer, gracious one, <b>and the light beyond them all</b>.'),
D(theme='AN OFFERING OF WORD-FLOWERS',
 svg=svg('Two hands offering flowers made of written syllables at the feet of a linga',
  f'<g transform="translate(150 120)">{LINGA}</g>'
  '<g stroke="#111" stroke-width="2.5"><path d="M20 140 q10 -30 40 -30 q20 0 30 10 l-10 10 q-20 -6 -30 10z" fill="#f2c79b"/></g>'
  +''.join(f'<g transform="translate({x} {y})"><circle r="12" fill="{c}" stroke="#111" stroke-width="1.5"/><text y="4" text-anchor="middle" font-family="Noto Sans" font-style="italic" font-size="9">{t}</text></g>' for x,y,c,t in [(70,90,'#f08aa6','śiva'),(96,70,'#ffd60a','oṃ'),(120,94,'#bcd4f0','hara'),(90,110,'#ddf5ea','bhava')])
  +'<text x="110" y="24" text-anchor="middle" font-family="Bangers" font-size="11">VĀKYA-PUṢPA</text>'),
 mean='Where is this weak mind of mine, ruled by afflictions, and where is Your eternal glory, which crosses every limit of qualities? Though I was alarmed by this thought, devotion made me bold and laid at Your feet, O giver of boons, this offering of flowers made of words.',
 plain='My mind is small and troubled; Your glory has no limit. That thought frightened me. But devotion gave me courage, and I have laid these word-flowers at Your feet.',
 words=[('kṛśa-pariṇati','<b>of weak growth</b>, small'),('kleśa-vaśyam','<b>under the sway of afflictions</b>'),('guṇa-sīmā','the <b>limit of qualities</b>'),('cakitam','<b>alarmed</b>'),('amandīkṛtya','<b>making bold</b>'),('vākya-puṣpa-upahāra','<b>an offering of word-flowers</b>')],
 deep='<p><b>The circle closes.</b> The hymn opened (verse 1) with the poet saying he cannot praise Śiva fully. Here, near the end, he says it again, but now as the giver of a gift: "word-flowers".</p><p><b>A flower thief.</b> Remember the story: Puṣpadanta lost his powers for stealing flowers meant for Śiva. Now he offers Śiva flowers of his own: the verses of this hymn.</p><p><b>Devotion\'s courage.</b> <i>Bhaktir ādhāt</i>: it was devotion, not his own skill, that put the offering at the Lord\'s feet.</p>',
 cards=('💡 Kleśas','The afflictions of the mind in yoga: ignorance, ego, attachment, aversion, fear.','💡 Mālinī','The metre of verses 31–32: fifteen syllables, pausing after the eighth.'),
 inner='Our words are small, our minds are troubled. Offer them anyway. Love makes the offering worthy.',
 talk=('He stole flowers, and now he offers word-flowers?','That\'s the beauty of it. The thief\'s fault and the poet\'s gift meet in one image.'),
 key='A small mind, a limitless Lord: <b>devotion offers the flowers anyway</b>.'),
D(theme='IF THE OCEAN WERE INK',
 svg=svg('Sarasvati writing forever with a branch of the wish-fulfilling tree as a pen, a black mountain as ink, the ocean as inkpot and the earth as paper',
  '<path d="M10 60 L40 20 L70 60Z" fill="#222" stroke="#111" stroke-width="2"/><text x="40" y="74" text-anchor="middle" font-family="Bangers" font-size="9">INK MOUNTAIN</text>'
  '<ellipse cx="40" cy="110" rx="32" ry="14" fill="#1d6fb8" stroke="#111" stroke-width="2"/><text x="40" y="140" text-anchor="middle" font-family="Bangers" font-size="9">OCEAN INKPOT</text>'
  '<path d="M90 150 q60 -10 120 0 v-40 q-60 -10 -120 0z" fill="#d9c79a" stroke="#111" stroke-width="2"/><text x="150" y="146" text-anchor="middle" font-family="Bangers" font-size="9">EARTH AS PAPER</text>'
  '<g stroke="#111" stroke-width="2.5"><circle cx="150" cy="40" r="12" fill="#f2c79b"/><path d="M130 100 q20 -50 40 0z" fill="#fff"/></g><path d="M170 70 L190 118" stroke="#2a9d6f" stroke-width="4"/><text x="196" y="66" font-family="Bangers" font-size="9">PEN</text><text x="150" y="20" text-anchor="middle" font-family="Bangers" font-size="10">ŚĀRADĀ</text>'),
 mean='If a black mountain were the ink, the ocean the inkpot, a branch of the best of heavenly trees the pen, and the earth the paper; and if Śāradā, the goddess of learning, took these and wrote for all time: even then, O Lord, she would not reach the end of Your qualities.',
 plain='Make a mountain into ink, the ocean into an inkpot, a branch of the wish-tree into a pen, the earth into paper, and let Sarasvatī write forever: she still could not finish describing Śiva\'s glories.',
 words=[('asita-giri','a <b>black mountain</b>'),('kajjalam','<b>ink</b>, lamp-black'),('sindhu-pātre','<b>in the ocean as inkpot</b>'),('sura-taruvara-śākhā','<b>a branch of the best of heavenly trees</b>'),('patram urvī','the <b>earth as paper</b>'),('śāradā','<b>Sarasvatī</b>, goddess of learning')],
 deep='<p><b>The most famous verse.</b> This is the verse people quote when they want to say something is beyond description, and it is often recited on its own. Its images are vast and simple: the biggest ink, the largest pot, the best pen, the widest page, the greatest writer, and endless time.</p><p><b>Back to the beginning.</b> Verse 1 said even Brahmā\'s words fall short. Verse 32 says even Sarasvatī, writing forever, could not finish. The hymn ends its praise as it began: in wonder.</p><p><b>Wish-tree pen.</b> The <i>sura-taru</i>, "tree of the gods", is the Pārijāta or Kalpavṛkṣa, the wish-fulfilling tree of heaven.</p>',
 cards=('💡 Śāradā','A name of Sarasvatī, goddess of speech and learning; Kashmir\'s Śāradā Pīṭha is named after her.','💡 Kalpavṛkṣa','The wish-fulfilling tree that rose from the churning of the ocean.'),
 inner='Some things can only be honoured by admitting they can\'t be told. Wonder is the last word of praise.',
 talk=('Even Sarasvatī couldn\'t finish?','Not if she wrote forever. That\'s how the poet ends his praise: not with a full stop, but with wonder.'),
 key='All the ink in the world, written forever: <b>still not the end of His glory</b>.'),
]
