import sys; sys.path.insert(0,'/home/claude/work/devim')
from common import *
head=make_head('Devī Kavacam · Part 2 · Armour for Every Limb · Devī Māhātmya series · srini.presents',
 'Devī Kavacam, Part 2 of the Devī Māhātmya series: the guardians of the ten directions, a goddess for every part of the body, and the fruits of reciting, verses 18–56 explained in plain English with illustrations.',
 '  .long .vfig svg{max-height:100px}\n  .long .sloka .mean{font-size:12px}\n  .long .pt{font-size:13.5px}\n  .long .ct td{padding-top:2px;padding-bottom:2px}\n')
def BODY(x=110,y=0,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2">'
     '<circle cy="22" r="14" fill="#f2c79b"/><path d="M-18 40 h36 l6 60 h-48z" fill="#ffd60a"/><path d="M-18 42 l-14 52 M18 42 l14 52" stroke="#f2c79b" stroke-width="8"/>'
     '<path d="M-12 100 l-4 58 M12 100 l4 58" stroke="#c0392b" stroke-width="10"/></g>')
def glow(inner): return '<circle cx="110" cy="80" r="70" fill="#ffd60a" opacity=".25" stroke="none"/>'+inner
G=[
dict(n='18–20',lab='VERSES 18–20 · THE TEN DIRECTIONS',lines=[['dakṣiṇe’vatu vārāhī','nairṛtyāṃ khaḍgadhāriṇī |'],['pratīcyāṃ vāruṇī rakṣed','vāyavyāṃ mṛgavāhinī ‖18‖'],['udīcyāṃ pātu kaumārī','aiśānyāṃ śūladhāriṇī |'],['ūrdhvaṃ brahmāṇi me rakṣed','adhastād vaiṣṇavī tathā ‖19‖'],['evaṃ daśa diśo rakṣec','cāmuṇḍā śavavāhanā |'],['jayā me cāgrataḥ pātu','vijayā pātu pṛṣṭhataḥ ‖20‖']],theme='A GODDESS ON EVERY SIDE',
 svg=svg('A compass with a goddess in each of the eight directions, one above and one below, around a person in the centre',
  '<circle cx="110" cy="80" r="66" fill="#fff" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M110 80 L{110+66*math.cos(k*0.785-1.571):.0f} {80+66*math.sin(k*0.785-1.571):.0f}" stroke="#ddd" stroke-width="2"/>' for k in range(8))+person(110,92,'#ff8c1a','#c98b5a',.5)
  +''.join(T(110+50*math.cos(k*0.785-1.571),84+50*math.sin(k*0.785-1.571),t,8) for k,t in enumerate(['KAUMĀRĪ','ŚŪLA','AINDRĪ','AGNI','VĀRĀHĪ','KHAḌGA','VĀRUṆĪ','MṚGA']))+T(30,16,'↑ BRAHMĀṆĪ',8)+T(32,154,'↓ VAIṢṆAVĪ',8),R),
 mean='In the south may Vārāhī protect me; in the south-west, the sword-bearer; in the west, Vāruṇī; in the north-west, she who rides the deer. In the north may Kaumārī protect; in the north-east, the trident-bearer; above, Brahmāṇī; below, Vaiṣṇavī. So may Cāmuṇḍā, who rides a corpse, guard all ten directions. May Jayā protect me in front, and Vijayā behind.',
 words=[('dakṣiṇe · pratīcyām','<b>in the south</b> · <b>in the west</b>'),('udīcyām · aiśānyām','<b>in the north</b> · <b>in the north-east</b>'),('ūrdhvam · adhastāt','<b>above</b> · <b>below</b>'),('daśa diśaḥ','<b>the ten directions</b>')],
 point='<b>Ten directions, not four.</b> Indian thought counts eight compass points plus up and down. With verse 17 (east and south-east) every one now has a guardian. Then come front and back: Jayā and Vijayā, “Victory” and “Triumph”.',
 key='No direction is left open: <b>she guards all ten</b>.'),
dict(n='21–23',lab='VERSES 21–23 · HEAD AND FACE',lines=[['ajitā vāmapārśve tu','dakṣiṇe cāparājitā |'],['śikhām udyotinī rakṣed','umā mūrdhni vyavasthitā ‖21‖'],['mālādharī lalāṭe ca','bhruvau rakṣed yaśasvinī |'],['trinetrā ca bhruvor madhye','yamaghaṇṭā ca nāsike ‖22‖'],['śaṅkhinī cakṣuṣor madhye','śrotrayor dvāravāsinī |'],['kapolau kālikā rakṣet','karṇamūle tu śāṅkarī ‖23‖']],theme='FROM THE CREST DOWN',
 svg=svg('A face with labels for the crest, head, forehead, brows, eyes, ears, nostrils and cheeks','<circle cx="110" cy="84" r="50" fill="#f2c79b" stroke="#111" stroke-width="2.5"/><path d="M70 60 q40 -46 80 0" fill="#151515"/><path d="M110 30 v-16" stroke="#151515" stroke-width="6"/><circle cx="92" cy="80" r="5" fill="#111"/><circle cx="128" cy="80" r="5" fill="#111"/><path d="M84 70 q8 -4 16 0 M120 70 q8 -4 16 0" stroke="#111" stroke-width="2" fill="none"/><circle cx="110" cy="66" r="3" fill="#c0392b"/><path d="M110 84 v14 h6" stroke="#111" stroke-width="2" fill="none"/><ellipse cx="58" cy="86" rx="6" ry="12" fill="#f2c79b" stroke="#111" stroke-width="2"/><ellipse cx="162" cy="86" rx="6" ry="12" fill="#f2c79b" stroke="#111" stroke-width="2"/>'+T(110,12,'UDYOTINĪ',8)+T(110,46,'UMĀ',8)+T(30,80,'DVĀRAVĀSINĪ',7)+T(190,104,'KĀLIKĀ',8)+T(174,64,'ŚAṄKHINĪ',8),R),
 mean='Ajitā on my left side, Aparājitā on my right; may Udyotinī guard my crest, and Umā dwell on my head. Mālādharī on my forehead, Yaśasvinī my brows, Trinetrā between the brows, Yamaghaṇṭā my nostrils; Śaṅkhinī my eyes, Dvāravāsinī my ears, Kālikā my cheeks, Śāṅkarī the roots of my ears.',
 words=[('vāma · dakṣiṇa-pārśve','<b>on the left</b> · <b>on the right side</b>'),('śikhām · mūrdhni','<b>the crest</b> · <b>the head</b>'),('lalāṭe · bhruvau','<b>forehead</b> · <b>brows</b>'),('cakṣuṣoḥ · śrotrayoḥ','<b>the eyes</b> · <b>the ears</b>')],
 point='<b>Names that fit their place.</b> Trinetrā, the “three-eyed”, guards the spot between the brows, where the third eye is placed. Dvāravāsinī, “she who dwells at the door”, guards the ears, the doors of sound.',
 key='From crest to cheek, <b>each part has its guardian</b>.'),
dict(n='24–26',lab='VERSES 24–26 · MOUTH AND THROAT',lines=[['nāsikāyāṃ sugandhā ca','uttaroṣṭhe ca carcikā |'],['adhare cāmṛtakalā','jihvāyāṃ ca sarasvatī ‖24‖'],['dantān rakṣatu kaumārī','kaṇṭhadeśe tu caṇḍikā |'],['ghaṇṭikāṃ citraghaṇṭā ca','mahāmāyā ca tāluke ‖25‖'],['kāmākṣī cibukaṃ rakṣed','vācaṃ me sarvamaṅgalā |'],['grīvāyāṃ bhadrakālī ca','pṛṣṭhavaṃśe dhanurdharī ‖26‖']],theme='SPEECH IS GUARDED TOO',
 svg=svg('An open mouth with a tongue holding a small vina for Sarasvati, and speech bubbles coming out',glow('<path d="M60 70 q50 -30 100 0 q-50 60 -100 0z" fill="#c0392b" stroke="#111" stroke-width="2.5"/><path d="M70 72 h80" stroke="#fff" stroke-width="6" stroke-dasharray="8 3"/><path d="M90 92 q20 14 40 0" fill="#e05a8a" stroke="#111" stroke-width="2"/><path d="M170 50 q30 -20 40 6 q-10 20 -32 10z" fill="#fff" stroke="#111" stroke-width="2"/>')+T(110,140,'SARASVATĪ ON THE TONGUE',9),R),
 mean='Sugandhā on my nose, Carcikā on my upper lip, Amṛtakalā on my lower lip, Sarasvatī on my tongue. May Kaumārī guard my teeth, Caṇḍikā my throat, Citraghaṇṭā my uvula, Mahāmāyā my palate. Kāmākṣī my chin, Sarvamaṅgalā my speech, Bhadrakālī my neck, Dhanurdharī my spine.',
 words=[('jihvāyām sarasvatī','<b>Sarasvatī on the tongue</b>'),('kaṇṭha-deśe','<b>in the throat</b>'),('vācam','<b>speech</b>'),('pṛṣṭha-vaṃśe','<b>along the spine</b>')],
 point='<b>Not just body parts.</b> Sarasvatī, goddess of learning, guards the tongue; Sarvamaṅgalā, “all-auspicious”, guards <i>vāc</i>, speech itself. The armour protects what we say as well as what we are.',
 key='Sarasvatī on the tongue: <b>may our words be guarded</b>.'),
dict(n='27–29',lab='VERSES 27–29 · ARMS AND HEART',lines=[['nīlagrīvā bahiḥkaṇṭhe','nalikāṃ nalakūbarī |'],['skandhayoḥ khaḍginī rakṣed','bāhū me vajradhāriṇī ‖27‖'],['hastayor daṇḍinī rakṣed','ambikā cāṅgulīṣu ca |'],['nakhāñ chūleśvarī rakṣet','kukṣau rakṣet kuleśvarī ‖28‖'],['stanau rakṣen mahādevī','manaḥśokavināśinī |'],['hṛdaye lalitā devī','udare śūladhāriṇī ‖29‖']],theme='LALITĀ IN THE HEART',
 svg=svg('A figure with a glowing heart, labelled Lalita, and arms holding a sword and a thunderbolt',glow(BODY(110,0,.9)+'<path d="M110 70 q-10 -10 -10 -4 q0 6 10 14 q10 -8 10 -14 q0 -6 -10 4z" fill="#e05a8a" stroke="#111" stroke-width="2"/>')+T(170,62,'LALITĀ',11)+T(40,62,'VAJRA',10)+T(40,104,'DAṆḌA',10),R),
 mean='Nīlagrīvā the outer throat, Nalakūbarī the windpipe; Khaḍginī my shoulders, Vajradhāriṇī my arms; Daṇḍinī my hands, Ambikā my fingers; Śūleśvarī my nails, Kuleśvarī my sides. Mahādevī, destroyer of the mind’s grief, my chest; the goddess Lalitā my heart; Śūladhāriṇī my belly.',
 words=[('skandhayoḥ · bāhū','<b>the shoulders</b> · <b>the arms</b>'),('hastayoḥ · aṅgulīṣu','<b>the hands</b> · <b>the fingers</b>'),('manaḥ-śoka-vināśinī','<b>destroyer of the mind’s grief</b>'),('hṛdaye lalitā','<b>Lalitā in the heart</b>')],
 point='<b>The heart belongs to Lalitā.</b> The gentlest, most beautiful form of the Goddess is placed in the heart. Her neighbour is the one who “destroys the mind’s grief”: the armour reaches past the body to sorrow itself.',
 key='Lalitā guards the heart; <b>grief itself is driven out</b>.'),
dict(n='30–32',lab='VERSES 30–32 · DOWN TO THE FEET',lines=[['nābhau ca kāminī rakṣed','guhyaṃ guhyeśvarī tathā |'],['pūtanā kāmikā meḍhraṃ','gude mahiṣavāhinī ‖30‖'],['kaṭyāṃ bhagavatī rakṣej','jānunī vindhyavāsinī |'],['jaṅghe mahābalā rakṣet','sarvakāmapradāyinī ‖31‖'],['gulphayor nārasiṃhī ca','pādapṛṣṭhe tu taijasī |'],['pādāṅgulīṣu śrī rakṣet','pādādhastalavāsinī ‖32‖']],theme='NAVEL TO TOES',
 svg=svg('Legs and feet with labels at the hips, knees, ankles and toes',glow('<path d="M86 10 h48 l4 40 h-56z" fill="#c0392b" stroke="#111" stroke-width="2"/><path d="M94 50 l-6 90 M126 50 l6 90" stroke="#f2c79b" stroke-width="16"/><path d="M76 146 h22 M122 146 h22" stroke="#f2c79b" stroke-width="10" stroke-linecap="round"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#c0392b"/>' for x,y in [(92,92),(130,92),(90,136),(132,136)]))+T(36,30,'BHAGAVATĪ',9)+T(36,96,'VINDHYAVĀSINĪ',8)+T(184,136,'NĀRASIṂHĪ',8)+T(110,158,'ŚRĪ',10),R),
 mean='Kāminī my navel, Guhyeśvarī my private parts, and the goddesses below; Bhagavatī my hips, Vindhyavāsinī my knees; Mahābalā, giver of every wish, my shins; Nārasiṃhī my ankles, Taijasī the tops of my feet, Śrī my toes, and Talavāsinī the soles of my feet.',
 words=[('nābhau','<b>at the navel</b>'),('kaṭyām · jānunī','<b>the hips</b> · <b>the knees</b>'),('gulphayoḥ','<b>the ankles</b>'),('pāda-aṅgulīṣu · tala','<b>the toes</b> · <b>the soles</b>')],
 point='<b>Nothing is too low.</b> The armour does not skip the parts we do not mention or the feet that touch the dust. Vindhyavāsinī, “she who dwells in the Vindhyas”, guards the knees; Śrī herself, Lakṣmī, guards the toes.',
 key='Every part of us, <b>down to the soles</b>, is hers to guard.'),
dict(n='33–35',lab='VERSES 33–35 · INSIDE THE BODY',lines=[['nakhān daṃṣṭrākarālī ca','keśāṃś caivordhvakeśinī |'],['romakūpeṣu kauberī','tvacaṃ vāgīśvarī tathā ‖33‖'],['raktamajjāvasāmāṃsā-','nyasthimedāṃsi pārvatī |'],['antrāṇi kālarātriś ca','pittaṃ ca mukuṭeśvarī ‖34‖'],['padmāvatī padmakośe','kaphe cūḍāmaṇis tathā |'],['jvālāmukhī nakhajvālām','abhedyā sarvasandhiṣu ‖35‖']],theme='BLOOD, BONE AND JOINTS',
 svg=svg('A simple cutaway of a figure showing bones, blood and joints, each glowing',glow(BODY(110,0,.9)+''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#fff" stroke="#c0392b" stroke-width="2"/>' for x,y in [(84,84),(136,84),(99,94),(121,94),(96,140),(124,140)])+'<path d="M110 40 v50" stroke="#fff" stroke-width="4" stroke-dasharray="4 3"/>')+T(176,96,'ABHEDYĀ',10)+T(40,40,'PĀRVATĪ',10),R),
 mean='Daṃṣṭrākarālī my nails, Ūrdhvakeśinī my hair; Kauberī my pores, Vāgīśvarī my skin. Pārvatī my blood, marrow, fat, flesh, bone and tissue; Kālarātri my intestines, Mukuṭeśvarī my bile. Padmāvatī the lotus of my heart, Cūḍāmaṇi my phlegm, Jvālāmukhī the glow of my nails, Abhedyā every joint.',
 words=[('roma-kūpeṣu · tvacam','<b>the pores</b> · <b>the skin</b>'),('rakta · asthi','<b>blood</b> · <b>bone</b>'),('padma-kośe','<b>in the lotus-bud</b> (of the heart)'),('abhedyā sarva-sandhiṣu','<b>the Unbreakable</b>, in every joint')],
 point='<b>Into the tissues.</b> The armour goes past the skin: blood, marrow, bone, the body’s humours of bile and phlegm, as the āyurvedic body was understood. <i>Abhedyā</i>, “the Unbreakable”, holds every joint.',
 key='Inside and out, <b>she holds the body together</b>.'),
dict(n='36–38',lab='VERSES 36–38 · BREATH AND MIND',lines=[['śukraṃ brahmāṇi me rakṣec','chāyāṃ chatreśvarī tathā |'],['ahaṅkāraṃ mano buddhiṃ','rakṣen me dharmadhāriṇī ‖36‖'],['prāṇāpānau tathā vyānam','udānaṃ ca samānakam |'],['vajrahastā ca me rakṣet','prāṇaṃ kalyāṇaśobhanā ‖37‖'],['rase rūpe ca gandhe ca','śabde sparśe ca yoginī |'],['sattvaṃ rajas tamaś caiva','rakṣen nārāyaṇī sadā ‖38‖']],theme='THE SUBTLE BODY',
 svg=svg('A meditating figure with five breath currents and three coloured bands for the three gunas',glow(person(110,130,'#ff8c1a','#c98b5a',1.2)+''.join(f'<path d="M110 {60+k*10} q{30+k*6} -10 {50+k*6} 0" stroke="#4aa3df" stroke-width="2" fill="none"/>' for k in range(5))+''.join(f'<rect x="{20+k*16}" y="120" width="12" height="30" fill="{c}" stroke="#111"/>' for k,c in enumerate(['#fff','#c0392b','#222'])))+T(40,112,'GUṆAS',9)+T(176,40,'5 PRĀṆAS',10),R),
 mean='Brahmāṇī my vital seed, Chatreśvarī my shadow; Dharmadhāriṇī my ego, mind and intellect. Vajrahastā my five breaths, prāṇa, apāna, vyāna, udāna and samāna; Kalyāṇaśobhanā my life itself. Yoginī in taste, form, smell, sound and touch; and may Nārāyaṇī always guard my sattva, rajas and tamas.',
 words=[('ahaṅkāraṃ mano buddhim','<b>ego, mind, intellect</b>'),('prāṇa … samāna','<b>the five vital breaths</b>'),('rasa rūpa gandha śabda sparśa','<b>taste, form, smell, sound, touch</b>'),('sattvaṃ rajas tamaḥ','<b>the three guṇas</b>')],
 point='<b>Beyond flesh.</b> Now the armour covers the subtle body: the five breaths of yoga, the five sense-experiences, the mind and ego, and finally the three guṇas, the qualities of all nature. Nārāyaṇī, the Goddess as Viṣṇu’s power, guards them.',
 key='Breath, senses, mind: <b>the inner self is armoured too</b>.'),
dict(n='39–41',lab='VERSES 39–41 · LIFE AND LOVED ONES',lines=[['āyū rakṣatu vārāhī','dharmaṃ rakṣatu vaiṣṇavī |'],['yaśaḥ kīrtiṃ ca lakṣmīṃ ca','dhanaṃ vidyāṃ ca cakriṇī ‖39‖'],['gotram indrāṇi me rakṣet','paśūn me rakṣa caṇḍike |'],['putrān rakṣen mahālakṣmīr','bhāryāṃ rakṣatu bhairavī ‖40‖'],['panthānaṃ supathā rakṣen','mārgaṃ kṣemakarī tathā |'],['rājadvāre mahālakṣmīr','vijayā sarvataḥ sthitā ‖41‖']],theme='MY FAMILY, MY ROAD',
 svg=svg('A family walking together on a road towards a gate, with cattle beside them, under a protective glow',glow('<path d="M0 140 L90 90 H130 L220 140z" fill="#c9a26b" stroke="#111" stroke-width="2"/>'+person(80,124,'#c0392b','#c98b5a',.7)+person(104,124,'#3b6fd0','#c98b5a',.7)+person(124,130,'#ffd60a','#c98b5a',.5)+MOUNT('bull',170,120,.5,'#fff')+'<rect x="94" y="40" width="32" height="44" fill="#e0a800" stroke="#111" stroke-width="2"/>')+T(110,36,'RĀJADVĀRA',9),R),
 mean='Vārāhī my life span, Vaiṣṇavī my dharma; Cakriṇī my fame, honour, fortune, wealth and learning. Indrāṇī my family line; guard my cattle, O Caṇḍikā; Mahālakṣmī my children; Bhairavī my wife. Supathā my path, Kṣemakarī my road; Mahālakṣmī at the king’s gate; Vijayā everywhere.',
 words=[('āyuḥ · dharmam','<b>life span</b> · <b>dharma</b>'),('dhanaṃ vidyām','<b>wealth, learning</b>'),('gotram · putrān','<b>family line</b> · <b>children</b>'),('panthānam · mārgam','<b>my path</b> · <b>my road</b>')],
 point='<b>Armour for a whole life.</b> The prayer widens from the body to everything a person cares about: years, values, name, money, learning, family, animals, the journey, even one’s case at the king’s court. The language is of its time (“my wife”); the care is for everyone we love.',
 key='Not just me: <b>my family, my work, my road</b>.'),
dict(n='42',lab='VERSE 42 · THE GAPS',lines=[['rakṣāhīnaṃ tu yat sthānaṃ','varjitaṃ kavacena tu |'],['tat sarvaṃ rakṣa me devi','jayantī pāpanāśinī ‖42‖']],theme='WHATEVER WAS MISSED',
 svg=svg('A suit of armour with one small gap, which a golden hand closes',glow('<g stroke="#111" stroke-width="2.5"><path d="M72 40 q38 -20 76 0 l-6 80 q-32 22 -64 0z" fill="#e0a800"/><path d="M110 30 v108 M80 70 h60 M84 100 h52" stroke="#a87800" fill="none"/></g><rect x="118" y="76" width="16" height="16" fill="#fff" stroke="#111" stroke-width="2"/><path d="M160 60 q-20 4 -28 24" fill="none" stroke="#f2c79b" stroke-width="8"/>')+T(110,152,'JAYANTĪ',12),R),
 mean='Whatever place is left without protection, not covered by this armour: protect all of it for me, O Devī Jayantī, destroyer of sin.',
 plain='And anything I forgot to name, any gap in the armour: Goddess, guard that too.',
 words=[('rakṣā-hīnam','<b>without protection</b>'),('varjitaṃ kavacena','<b>left out by the armour</b>'),('tat sarvam rakṣa','<b>protect all of that</b>'),('jayantī','<b>the Victorious</b>'),('pāpa-nāśinī','<b>destroyer of sin</b>')],
 point='<b>The humble clause.</b> After naming every direction, limb, breath and loved one, the prayer admits it cannot list everything. So it hands the rest to her. It is a beautiful model for any prayer: name what you can, then trust.',
 key='Whatever I missed, <b>she covers</b>.'),
dict(n='43–45',lab='VERSES 43–45 · THE FRUITS BEGIN',lines=[['padam ekaṃ na gacchet tu','yadīcchec chubham ātmanaḥ |'],['kavacenāvṛto nityaṃ','yatra yatraiva gacchati ‖43‖'],['tatra tatrārthalābhaś ca','vijayaḥ sārvakāmikaḥ |'],['yaṃ yaṃ cintayate kāmaṃ','taṃ taṃ prāpnoti niścitam |'],['paramaiśvaryam atulaṃ','prāpsyate bhūtale pumān ‖44‖'],['nirbhayo jāyate martyaḥ','saṅgrāmeṣv aparājitaḥ |'],['trailokye tu bhavet pūjyaḥ','kavacenāvṛtaḥ pumān ‖45‖']],theme='NOT ONE STEP WITHOUT IT',
 svg=svg('A traveller wrapped in golden light stepping out on a journey, a sun rising ahead',glow(person(90,130,'#ff8c1a','#c98b5a',1.1)+'<circle cx="90" cy="100" r="34" fill="none" stroke="#e0a800" stroke-width="4" stroke-dasharray="6 4"/>'+SUN(180,40,16)+'<path d="M120 150 h90" stroke="#7a5a3a" stroke-width="4" stroke-dasharray="10 6"/>'),R),
 mean='If one wishes oneself well, one should not take even a single step without this armour. Covered by it always, wherever one goes, one gains wealth there, and victory in every aim. Whatever wish one thinks of, one surely attains; such a person gains matchless greatness on earth. One becomes fearless, unconquered in battle; covered by this armour, one is honoured in the three worlds.',
 words=[('padam ekaṃ na gacchet','<b>not take a single step</b>'),('kavacena āvṛtaḥ','<b>covered by the armour</b>'),('nirbhayaḥ','<b>fearless</b>'),('aparājitaḥ','<b>unconquered</b>')],
 point='<b>The phalaśruti.</b> From here the Kavacam lists the fruits of reciting it. Like every phalaśruti, it speaks in the language of praise: its central promise is the first word of verse 45, <i>nirbhaya</i>, fearless.',
 key='Its first gift: <b>to walk without fear</b>.'),
dict(n='46–47',lab='VERSES 46–47 · RARE EVEN FOR GODS',lines=[['idaṃ tu devyāḥ kavacaṃ','devānām api durlabham |'],['yaḥ paṭhet prayato nityaṃ','trisandhyaṃ śraddhayānvitaḥ ‖46‖'],['daivī kalā bhavet tasya','trailokyeṣv aparājitaḥ |'],['jīved varṣaśataṃ sāgram','apamṛtyuvivarjitaḥ ‖47‖']],theme='THREE TIMES A DAY',
 svg=svg('A sun at three points of its arc, dawn, noon and dusk, over a person reciting',person(110,150,'#ff8c1a','#c98b5a',.9)+'<path d="M20 120 Q110 -10 200 120" fill="none" stroke="#e0a800" stroke-width="2" stroke-dasharray="5 4"/>'+SUN(30,100,10)+SUN(110,40,12)+SUN(190,100,10)+T(30,126,'DAWN',8)+T(110,72,'NOON',8)+T(190,126,'DUSK',8),R),
 mean='This armour of the Devī is hard to obtain even for the gods. Whoever recites it daily, purified and full of faith, at the three junctions of the day, gains a divine spark and is unconquered in the three worlds; such a one lives a full hundred years, free from untimely death.',
 words=[('devānām api durlabham','<b>rare even for gods</b>'),('prayataḥ','<b>purified</b>, self-controlled'),('trisandhyam','<b>at the three junctions</b>: dawn, noon, dusk'),('daivī kalā','<b>a divine spark</b>'),('apamṛtyu-vivarjitaḥ','<b>free from untimely death</b>')],
 point='<b>Faith and regularity.</b> Two conditions frame the promise: <i>śraddhā</i>, faith, and <i>nityam</i>, every day. The three <i>sandhyās</i>, dawn, noon and dusk, are the classic Vedic times of prayer.',
 key='Recited daily with faith, <b>it becomes part of you</b>.'),
dict(n='48–52',lab='VERSES 48–52 · NOTHING CAN HARM',lines=[['naśyanti vyādhayaḥ sarve','lūtāvisphoṭakādayaḥ |'],['sthāvaraṃ jaṅgamaṃ caiva','kṛtrimaṃ cāpi yad viṣam ‖48‖'],['abhicārāṇi sarvāṇi','mantrayantrāṇi bhūtale |'],['bhūcarāḥ khecarāś caiva','jalajāś caupadeśikāḥ ‖49‖'],['sahajā kulajā mālā','ḍākinī śākinī tathā |'],['antarikṣacarā ghorā','ḍākinyaś ca mahābalāḥ ‖50‖'],['grahabhūtapiśācāś ca','yakṣagandharvarākṣasāḥ |'],['brahmarākṣasavetālāḥ','kuṣmāṇḍā bhairavādayaḥ ‖51‖'],['naśyanti darśanāt tasya','kavace hṛdi saṃsthite |'],['mānonnatir bhaved rājñas','tejovṛddhikaraṃ param ‖52‖']],theme='THE ARMOUR IN THE HEART',
 svg=svg('Dark shadowy shapes fleeing from a person whose heart glows with golden armour',person(110,140,'#ff8c1a','#c98b5a',1)+'<circle cx="110" cy="114" r="12" fill="#ffd60a" stroke="#e0a800" stroke-width="3"/>'+''.join(f'<path d="M110 114 L{110+90*math.cos(k*0.7):.0f} {80+60*math.sin(k*0.7):.0f}" stroke="#ffd60a" stroke-width="2"/>' for k in range(9))+''.join(f'<path d="M{x} {y} q10 -16 20 0 q-4 10 -10 6 q-6 4 -10 -6z" fill="#444" stroke="#111"/>' for x,y in [(10,40),(180,30),(20,120),(190,110)]),R),
 mean='All diseases perish, such as spider-bites and boils, and every poison, natural or man-made; all sorcery, spells and charms; and every harmful being of land, sky and water, from ḍākinīs and ghosts to rākṣasas and vetālas: all perish at the very sight of one who holds this armour in the heart. One’s honour before the king rises, and one’s radiance grows.',
 words=[('kavace hṛdi saṃsthite','<b>with the armour set in the heart</b>'),('darśanāt','<b>at the mere sight</b>')],
 point='<b>A traditional list of fears.</b> Disease, poison, sorcery, spirits: everything people then feared. These verses are a statement of faith, not medical claims. Note where the armour is worn: <i>hṛdi</i>, in the heart.',
 key='Worn in the heart, <b>the armour drives out fear</b>.'),
dict(n='53–56',lab='VERSES 53–56 · THE LAST WORD',lines=[['yaśasā vardhate so’pi','kīrtimaṇḍitabhūtale |'],['japet saptaśatīṃ caṇḍīṃ','kṛtvā tu kavacaṃ purā ‖53‖'],['yāvad bhūmaṇḍalaṃ dhatte','saśailavanakānanam |'],['tāvat tiṣṭhati medinyāṃ','santatiḥ putrapautrikī ‖54‖'],['dehānte paramaṃ sthānaṃ','yat surair api durlabham |'],['prāpnoti puruṣo nityaṃ','mahāmāyāprasādataḥ ‖55‖'],['labhate paramaṃ rūpaṃ','śivena saha modate ‖56‖']],theme='FIRST THE ARMOUR, THEN THE CAṆḌĪ',
 svg=svg('A book labelled Saptashati with a golden armour in front of it, and Shiva and the Goddess together above',glow('<rect x="40" y="70" width="70" height="70" fill="#fff3b0" stroke="#111" stroke-width="2"/><path d="M75 70 v70" stroke="#111"/>'+T(75,108,'700',14)+'<path d="M126 74 q20 -12 40 0 l-4 50 q-16 12 -32 0z" fill="#e0a800" stroke="#111" stroke-width="2"/>'+DEVI(170,-4,.3,False)+'<circle cx="196" cy="14" r="8" fill="#9fd3f0" stroke="#111" stroke-width="2"/><path d="M186 46 q10 -26 20 0z" fill="#9fd3f0" stroke="#111" stroke-width="2"/>'),R),
 mean='Such a one grows in fame on an earth adorned with his renown. One should chant the Saptaśatī, the Caṇḍī, only after first doing the Kavacam. As long as the earth bears its mountains, woods and forests, so long will his line of children and grandchildren endure. At the body’s end, by the grace of Mahāmāyā, he attains the supreme abode, rare even for the gods; he gains the highest form, and rejoices with Śiva.',
 words=[('japet saptaśatīm','<b>one should chant the 700 verses</b>'),('kṛtvā kavacaṃ purā','<b>having first done the Kavacam</b>'),('mahāmāyā-prasādataḥ','<b>by the grace of Mahāmāyā</b>'),('śivena saha modate','<b>rejoices with Śiva</b>')],
 point='<b>Why it comes first.</b> Verse 53 states the rule this series follows: chant the Kavacam <b>before</b> the Saptaśatī. The final promise reaches past this life: the supreme abode, and joy in the company of Śiva.',
 key='Armour first; <b>then the story of the Goddess</b>.'),
]
for v in G:
    if len(v['lines'])>=6: v['long']=True; v['words']=v['words'][:4]
for v in G:
    if v['n'] in ('43–45','48–52','53–56'): v['words']=[]
    if v['n']=='48–52': v['svg']=''
full=[fp(v['lab'].split(' · ')[0],v['lines']) for v in G]
LEFT=[('Crest','Udyotinī',(0,6)),('Head','Umā',(0,11)),('Forehead','Mālādharī',(0,15)),('Third eye','Trinetrā',(0,18)),('Eyes','Śaṅkhinī',(-5,22)),('Ears','Dvāravāsinī',(-14,22)),('Tongue','Sarasvatī',(-2,29)),('Teeth','Kaumārī',(2,28)),('Chin','Kāmākṣī',(0,34)),('Throat','Caṇḍikā',(0,37)),('Neck','Bhadrakālī',(-4,39)),('Spine','Dhanurdharī',(-8,60))]
RIGHT=[('Shoulders','Khaḍginī',(18,42)),('Heart','Lalitā',(6,56)),('Arms','Vajradhāriṇī',(24,62)),('Belly','Śūladhāriṇī',(4,78)),('Navel','Kāminī',(0,88)),('Hands','Daṇḍinī',(32,94)),('Hips','Bhagavatī',(16,100)),('Knees','Vindhyavāsinī',(14,128)),('Every joint','Abhedyā',(-14,128)),('Shins','Mahābalā',(15,140)),('Ankles','Nārasiṃhī',(16,152)),('Toes','Śrī',(17,158))]
S_,X0,Y0=2.3,230,22
P=lambda a: (X0+a[0]*S_, Y0+a[1]*S_)
def lab_(k,a,bn,anc,side):
    y=28+k*33; x=158 if side=='L' else 302
    ax,ay=P(anc)
    t=f'<text x="{x}" y="{y+4}" text-anchor="{"end" if side=="L" else "start"}" font-family="Bangers" font-size="11.5">{a.upper()} · <tspan fill="#c0392b">{bn}</tspan></text>'
    ln=f'<path d="M{x+(4 if side=="L" else -4)} {y} L{ax:.0f} {ay:.0f}" stroke="#c0392b" stroke-width="1"/><circle cx="{ax:.0f}" cy="{ay:.0f}" r="2.5" fill="#c0392b"/>'
    return ln+t
mapsvg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff8ec;max-width:100%" width="460" height="420" viewBox="0 0 460 420" role="img" aria-label="A body map: a figure in the centre with lines to the goddess who guards each part, from Udyotini at the crest to Shri at the toes">'
 +BODY(X0,Y0,S_)+''.join(lab_(k,a,b_,anc,'L') for k,(a,b_,anc) in enumerate(LEFT))+''.join(lab_(k,a,b_,anc,'R') for k,(a,b_,anc) in enumerate(RIGHT))+'</svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 2 OF 19</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,76px)">DEVĪ KAVACAM</h1>
  <div class="series">DEVĪ MĀHĀTMYA · PART 2 · ARMOUR FOR EVERY LIMB</div>
  <div class="tag">Verses 18–56 · explained and illustrated</div>
  <svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A person standing inside a ring of goddesses, one for each direction, wrapped head to foot in golden light"><rect width="380" height="268" fill="#3a1414" rx="8"/><circle cx="190" cy="134" r="110" fill="none" stroke="#ffd60a" stroke-width="3" stroke-dasharray="6 6"/>{''.join(DEVI(190+110*math.cos(k*0.785),134+110*math.sin(k*0.785)-30,.26,False,c) for k,c in enumerate(['#3b6fd0','#ff8c1a','#333','#2a9d6f','#ffd60a','#e05a8a','#9b5de5','#fff']))}<circle cx="190" cy="140" r="56" fill="#ffd60a" opacity=".35"/>{BODY(190,62,.9)}</svg>
  {CAST}
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> Verses 18–56 for chanting, then the whole armour on one picture, then <b>one page for each group of verses</b>: the directions, the body from crest to toes, the breath and mind, family and road, and the fruits of reciting.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">WHERE WE ARE</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    <p>In <a href="/bhakti/devi/devi-mahatmya/part-1/">Part 1</a>, the sage Mārkaṇḍeya asked Brahmā for the supreme secret of protection, and Brahmā began the <b>Devī Kavacam</b>: the Nine Durgās, the Mothers on their mounts, and in verse 17 the first two guardians of space.</p>
    <p>Now the armour goes on. First every direction, then the body from the crest of the head to the soles of the feet, then breath, mind, family and the road ahead. Last come the fruits of reciting it, and a rule: chant this before the Saptaśatī.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--red)">With the blessings of the Devī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why name every single body part?","Because that is how you 'put on' armour: piece by piece. Saying each name is like buckling each plate into place.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 18–56 IN ONE GO</h2>
  <div class="sub">Verses 18–35</div>
  <div class="full">{''.join(full[:6])}</div>
</section>

<section class="page" id="full2">
  <h2 class="page-title">IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 36–56</div>
  <div class="full">{''.join(full[6:])}</div>
  <div class="note">Verse numbers follow shlokam.org (56 verses). Verse 44 has three lines; verse 56 has one.</div>
</section>

<section class="page" id="map">
  <h2 class="page-title">THE ARMOUR AT A GLANCE</h2>
  <div class="sub">A goddess for each part of you</div>
  {mapsvg}
  <div class="panel reading pt"><p>The Kavacam names more than 60 guardians. This map shows 24 of them, from Udyotinī at the crest of the head to Śrī at the toes, with Abhedyā, “the Unbreakable”, in every joint. Breath, mind and the three guṇas have guardians too (verses 36–38).</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">←</span><a href="#foreword">Where We Are</a></li>
    <li><span class="num">🔤</span><a href="#full">In One Go</a></li>
    <li><span class="num">🗺</span><a href="#map">The Armour at a Glance</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    <li class="part">VERSES 18–56</li>
    {''.join(f'<li><span class="num">{v["n"].split("–")[0]}</span><a href="#v{v["n"]}">{v["theme"].title().replace("’S","’s")}</a></li>' for v in G)}
  </ul>
</section>
''']
for v in G:
    h=vpage(v)
    if v.get('long'): h=h.replace(f'<section class="page" id="v{v["n"]}">',f'<section class="page long" id="v{v["n"]}">',1)
    b.append(h)
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 2 ON ONE PAGE</h2>
  <div class="sub">Verses 18–56 in five lines</div>
  <div class="steps">
    <div><b>Verses 18–20.</b> A guardian for each of the ten directions, with Cāmuṇḍā over all; Jayā in front, Vijayā behind.</div>
    <div><b>Verses 21–35.</b> The body, crest to soles: Sarasvatī on the tongue, Lalitā in the heart, Śrī at the toes, Abhedyā in every joint.</div>
    <div><b>Verses 36–41.</b> Breath, senses, mind and the three guṇas; then life, dharma, wealth, family and the road ahead.</div>
    <div><b>Verse 42.</b> Whatever was missed: “Jayantī, guard that too.”</div>
    <div><b>Verses 43–56.</b> The fruits: fearlessness, long life, freedom from harm; and the rule, Kavacam first, then the Saptaśatī.</div>
  </div>
  {talk("What comes next?","Part 3: the Argalā Stotram, the 'bolt' that opens the door. Every verse ends 'rūpaṃ dehi, jayaṃ dehi, yaśo dehi, dviṣo jahi'.")}
  <div class="key">Part 2: <b>armoured from crest to sole, we begin</b>. 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Devī Kavacam, verses 18–56, chanted before the Devī Māhātmya (Durgā Saptaśatī). Text checked word by word against shlokam.org (56 verses); verse 49 follows its reading caupadeśikāḥ. The fruits of recitation (phalaśruti) are given as the text states them, as statements of faith. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('/home/claude/work/devim/Devi_Mahatmya_Part02.html','w').write(head+''.join(b)+tail())
print('ok')
