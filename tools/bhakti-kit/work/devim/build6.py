import sys; sys.path.insert(0,'/home/claude/work/devim')
from common import *
exec(open('/home/claude/work/devim/build5.py').read().split("V=[")[0].split("head=make_head")[0])  # imports only
src5=open('/home/claude/work/devim/build5.py').read()
for name in ['def panels','def storypage']:
    i=src5.index(name); j=src5.index('\n\'\'\'\n',i)+5; exec(src5[i:j])
head=make_head('Madhu and Kaiṭabha · Brahmā’s Hymn · Part 6 · Devī Māhātmya series · srini.presents',
 'Devī Māhātmya, Part 6: chapter 1, ślokas 67–104. Two demons attack Brahmā, Brahmā’s great hymn to Yoganidrā wakes Viṣṇu, and Madhu and Kaiṭabha are slain. Explained in plain English with illustrations.')
def VISHNU_SLEEP(x,y,s=1,eyes_closed=True):
    e='<path d="M-6 -4 q3 2 6 0 M2 -4 q3 2 6 0" stroke="#111" fill="none"/>' if eyes_closed else '<circle cx="-3" cy="-4" r="1.6" fill="#111"/><circle cx="5" cy="-4" r="1.6" fill="#111"/>'
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-70 10 q70 24 140 0 q-10 14 -70 16 q-60 -2 -70 -16z" fill="#7aa86a"/>'+''.join(f'<circle cx="{-66+k*8}" cy="{-10+abs(k-2)*3}" r="7" fill="#7aa86a"/>' for k in range(5))
     +'<path d="M-50 4 q50 -20 100 -4" fill="none" stroke="#3b6fd0" stroke-width="14"/><circle cx="-50" cy="-6" r="10" fill="#3b6fd0"/>'
     +f'<g transform="translate(-50 -6)">{e}</g><path d="M-58 -16 h16 l-3 -10 h-10z" fill="#ffd60a"/></g>')
def BRAHMA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
  +MOUNT('lotus',0,26,1.0)+'<circle cx="-10" cy="-14" r="8" fill="#e0a800"/><circle cx="10" cy="-14" r="8" fill="#e0a800"/><circle cy="-18" r="10" fill="#e0a800"/><path d="M-16 20 q16 -34 32 0z" fill="#ff8c1a"/><path d="M0 -36 v8" stroke="#fff" stroke-width="5"/></g>')
DEMON=lambda x,y,s=1,c='#5a2a6a': f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2"><circle cy="-30" r="12" fill="#7a9a5a"/><path d="M-8 -40 l-4 -10 M8 -40 l4 -10" stroke-width="3"/><path d="M-5 -26 h10" /><path d="M-20 22 q20 -56 40 0z" fill="{c}"/><path d="M20 -10 l14 -20" stroke="#555" stroke-width="5"/></g>'
OCEAN='<rect width="220" height="160" fill="#1d3a6a"/><path d="M0 110 q27 -8 55 0 t55 0 t55 0 t55 0 V160 H0z" fill="#2a6ab0" stroke="#111"/>'
V=[
dict(n='73',lines=[['tvaṃ svāhā tvaṃ svadhā tvaṃ hi','vaṣaṭkāraḥ svarātmikā |'],['sudhā tvam akṣare nitye','tridhā mātrātmikā sthitā ‖73‖']],theme='YOU ARE THE SACRED SOUND',
 svg=svg('The syllable Om drawn large, split into its three sounds A, U, M, glowing over a sacred fire',FIRE(110,140,.9)+'<text x="110" y="92" text-anchor="middle" font-size="64" fill="#c0392b" font-family="serif">Oṃ</text>'+T(50,40,'A',18)+T(110,30,'U',18)+T(170,40,'M',18),R),
 mean='Brahmā said: You are Svāhā, you are Svadhā, you are the Vaṣaṭ cry; you are the soul of sound. You are the nectar, O imperishable, eternal one; you abide as the three measures (of Oṃ).',
 plain='You are every sacred word of offering, and the sound in all of them. You are the nectar, and the three sounds of Oṃ.',
 words=[('svāhā · svadhā · vaṣaṭ','<b>the ritual cries of offering</b>'),('svara-ātmikā','<b>whose self is sound</b>'),('sudhā','<b>nectar</b>'),('tridhā mātrā-ātmikā','<b>as the three measures</b>: A, U, M')],
 point='<b>Brahmā’s hymn begins.</b> With two demons coming to kill him and Viṣṇu fast asleep, Brahmā does not pray to Viṣṇu. He prays to <b>Yoganidrā</b>, the Goddess who holds Viṣṇu in sleep. And he starts with sound: every ritual word, and the syllable Oṃ itself.',
 key='Before anything else, <b>she is the sacred sound</b>.'),
dict(n='74',lines=[['ardhamātrāsthitā nityā','yānuccāryā viśeṣataḥ |'],['tvam eva sandhyā sāvitrī','tvaṃ devi jananī parā ‖74‖']],theme='THE SILENCE AFTER OṂ',
 svg=svg('A sound wave fading into a soft silent glow, with the dawn sun of Sandhya rising',
  '<path d="M10 80 q10 -30 20 0 t20 0 t20 0 q10 -16 20 0 t20 0 q10 -6 20 0" fill="none" stroke="#c0392b" stroke-width="3"/><circle cx="170" cy="80" r="28" fill="#ffd60a" opacity=".45" stroke="none"/>'+T(170,86,'½',18)+'<path d="M0 140 h220" stroke="#111"/>'+SUN(110,140,16),R),
 mean='You are the eternal half-measure, which cannot be uttered in any particular way. You alone are Sandhyā and Sāvitrī; you, O Devī, are the supreme mother.',
 plain='You are the silent half-beat after Oṃ that no voice can say. You are the twilight prayer and the Gāyatrī; you are the highest Mother.',
 words=[('ardha-mātrā','<b>the half-measure</b> of Oṃ'),('anuccāryā','<b>that cannot be uttered</b>'),('sandhyā','<b>the twilight prayer</b>'),('sāvitrī','<b>the Gāyatrī mantra</b>'),('jananī parā','<b>the supreme mother</b>')],
 point='<b>Beyond the sound.</b> After A, U and M, tradition speaks of a fourth, the <i>ardhamātrā</i>: the resonance as Oṃ fades into silence. Brahmā says she is that too. She is in the sound, and in the silence beyond it.',
 key='She is the sound, <b>and the silence after it</b>.'),
dict(n='75–76',lab='ŚLOKAS 1.75–76',lines=[['tvayaitad dhāryate viśvaṃ','tvayaitat sṛjyate jagat |'],['tvayaitat pālyate devi','tvam atsy ante ca sarvadā ‖75‖'],['visṛṣṭau sṛṣṭirūpā tvaṃ','sthitirūpā ca pālane |'],['tathā saṃhṛtirūpānte','jagato’sya jaganmaye ‖76‖']],theme='CREATE, SUSTAIN, DISSOLVE',
 svg=svg('A circle of three arrows: a sprouting seed, a full tree, and falling leaves returning to the earth, the Goddess in the centre',DEVI(110,30,.4,False)+'<circle cx="110" cy="80" r="62" fill="none" stroke="#111" stroke-width="2" stroke-dasharray="6 5"/>'+T(110,16,'SṚṢṬI',11)+T(30,140,'SAṂHṚTI',10)+T(190,140,'STHITI',11)+'<path d="M110 22 v10 M106 28 q4 -8 8 0" stroke="#2a7a4a" stroke-width="3" fill="none"/>',R),
 mean='By you this universe is borne; by you this world is created; by you, O Devī, it is protected; and at the end you always consume it. At its emanation you are the form of creation; in protecting, the form of preservation; and at the end, the form of dissolution, O you who are this whole world.',
 words=[('dhāryate · sṛjyate · pālyate','<b>is borne · is created · is protected</b>'),('atsi ante','<b>you consume at the end</b>'),('sṛṣṭi · sthiti · saṃhṛti','<b>creation · preservation · dissolution</b>'),('jagat-maye','<b>O you who are the world</b>')],
 point='<b>All three jobs are hers.</b> Usually creation is Brahmā’s, preservation Viṣṇu’s, dissolution Śiva’s. Here Brahmā himself says all three are the Goddess. It is a key idea of the Devī Māhātmya: she is the power behind the trinity.',
 key='Creation, preservation, dissolution: <b>three forms of one Goddess</b>.'),
dict(n='77',lines=[['mahāvidyā mahāmāyā','mahāmedhā mahāsmṛtiḥ |'],['mahāmohā ca bhavatī','mahādevī maheśvarī ‖77‖']],theme='SEVEN TIMES GREAT',
 svg=svg('Seven glowing stars in an arc, each labelled with a great name, above the Goddess',DEVI(110,40,.6,False)+''.join(f'<text x="{110+90*math.cos(math.pi+k*math.pi/6):.0f}" y="{90+70*math.sin(math.pi+k*math.pi/6):.0f}" text-anchor="middle" font-size="16" fill="#e0a800">★</text>' for k in range(7))+T(110,156,'MAHĀ ×7',12),R),
 mean='You are the great knowledge, the great illusion, the great intellect, the great memory, and the great delusion; the great Goddess, the great Ruler.',
 plain='You are the greatest wisdom and the greatest illusion, the greatest mind and memory, the greatest confusion: the great Goddess who rules all.',
 words=[('mahā-vidyā','<b>the great knowledge</b>'),('mahā-māyā','<b>the great illusion</b>'),('mahā-medhā · mahā-smṛtiḥ','<b>great intellect · great memory</b>'),('mahā-mohā','<b>the great delusion</b>')],
 point='<b>Wisdom and delusion, side by side.</b> Just as Medhas said in śloka 55, she is both <i>mahāvidyā</i> and <i>mahāmohā</i>. The name <i>Mahāvidyā</i> later becomes the title of the ten great tantric forms of the Goddess.',
 key='Greatest knowledge and greatest illusion: <b>both are she</b>.',
 note='Some editions read mahāsurī for maheśvarī.'),
dict(n='78',lines=[['prakṛtis tvaṃ ca sarvasya','guṇatrayavibhāvinī |'],['kālarātrir mahārātrir','moharātriś ca dāruṇā ‖78‖']],theme='THE THREE NIGHTS',
 svg=svg('Three night skies side by side, each darker than the last, with a different moon in each',''.join(f'<rect x="{k*73}" y="0" width="73" height="160" fill="{c}" stroke="#111"/>' for k,c in enumerate(['#2b2140','#1c1430','#0d0a18']))+STARS(18,5)+T(36,150,'KĀLA',10,'#fff')+T(110,150,'MAHĀ',10,'#fff')+T(183,150,'MOHA',10,'#fff')+''.join(f'<rect x="{80+k*14}" y="40" width="10" height="30" fill="{c}" stroke="#111"/>' for k,c in enumerate(['#fff','#c0392b','#222'])),R),
 mean='You are Prakṛti, the nature of all things, bringing forth the three guṇas. You are the Night of Time, the Great Night, and the terrible Night of Delusion.',
 plain='You are Nature, from whom the three qualities of everything arise. You are the dark night of destruction, the great night, and the fearful night of confusion.',
 words=[('prakṛtiḥ','<b>Nature</b>, the source of everything'),('guṇa-traya-vibhāvinī','<b>who brings forth the three guṇas</b>'),('kāla-rātriḥ','<b>the night of time</b>, of dissolution'),('mahā-rātriḥ','<b>the great night</b>'),('moha-rātriḥ','<b>the night of delusion</b>')],
 point='<b>Three nights.</b> Kālarātri is also the seventh of the Nine Durgās (Part 1). One popular tradition links the three nights to festivals: Mahārātri to Śivarātri, Moharātri to Kṛṣṇa Janmāṣṭamī, Kālarātri to Dīpāvalī. Darkness, too, is a form of the Mother.',
 key='Even the darkest night <b>is a form of the Mother</b>.'),
dict(n='79',lines=[['tvaṃ śrīs tvam īśvarī tvaṃ hrīs','tvaṃ buddhir bodhalakṣaṇā |'],['lajjā puṣṭis tathā tuṣṭis','tvaṃ śāntiḥ kṣāntir eva ca ‖79‖']],theme='EVERY GOOD QUALITY',
 svg=svg('Nine small symbols in a ring: lotus, crown, blushing face, lamp, grain, smile, dove-calm water, and a bowing figure',''.join(f'<text x="{110+62*math.cos(k*0.785):.0f}" y="{86+52*math.sin(k*0.785):.0f}" text-anchor="middle" font-size="18">{e}</text>' for k,e in enumerate('🌸👑☺️💡🌾😊🕊️🙏'))+DEVI(110,40,.35,False),R),
 mean='You are Śrī, you are the Ruler, you are modesty; you are intelligence, whose mark is understanding; shyness, nourishment, contentment; you are peace and patience.',
 plain='You are fortune and sovereignty, conscience and understanding, nourishment and contentment, peace and patience.',
 words=[('śrīḥ · īśvarī','<b>fortune</b> · <b>the ruler</b>'),('hrīḥ · lajjā','<b>modesty</b> · <b>shyness</b>'),('buddhiḥ bodha-lakṣaṇā','<b>intelligence, marked by understanding</b>'),('puṣṭiḥ · tuṣṭiḥ','<b>nourishment</b> · <b>contentment</b>'),('śāntiḥ · kṣāntiḥ','<b>peace</b> · <b>patience</b>')],
 point='<b>A first sketch of chapter 5.</b> Many of these qualities return in the 21 forms of <a href="/bhakti/devi/ya-devi-sarvabhuteshu/">“yā devī sarvabhūteṣu”</a>: lajjā, tuṣṭi, śānti, kṣānti. Brahmā names them here; in chapter 5 the gods bow to each one.',
 key='Every good quality in us <b>is a form of her</b>.'),
dict(n='80',lines=[['khaḍginī śūlinī ghorā','gadinī cakriṇī tathā |'],['śaṅkhinī cāpinī bāṇa-','bhuśuṇḍīparighāyudhā ‖80‖']],theme='ARMED',
 svg=svg('The eight-armed Goddess holding sword, trident, mace, discus, conch, bow, arrows and an iron club',DEVI(110,0,.9),R),
 mean='You are terrible, armed with sword and trident, with mace and discus; with conch and bow, arrows, sling and iron club.',
 plain='You are fearsome too: sword, trident, mace, discus, conch, bow, arrows, sling and club are in your hands.',
 words=[('khaḍginī · śūlinī','<b>sword-bearer</b> · <b>trident-bearer</b>'),('ghorā','<b>terrible</b>'),('gadinī · cakriṇī','<b>mace-bearer</b> · <b>discus-bearer</b>'),('śaṅkhinī · cāpinī','<b>conch-bearer</b> · <b>bow-bearer</b>'),('bhuśuṇḍī · parigha','<b>sling</b> · <b>iron club</b>')],
 point='<b>From qualities to weapons.</b> Right after peace and patience come weapons. It is the Devī Māhātmya’s rhythm everywhere: gentle and fierce side by side. Brahmā needs both right now.',
 key='The same Mother <b>holds peace and holds weapons</b>.'),
dict(n='81',lines=[['saumyā saumyatarāśeṣa-','saumyebhyas tv atisundarī |'],['parāparāṇāṃ paramā','tvam eva parameśvarī ‖81‖']],theme='GENTLER THAN ALL',
 svg=svg('The Goddess smiling softly, a lotus in her hand, the moon behind her',
  '<circle cx="150" cy="40" r="26" fill="#fff8c0" stroke="#111" stroke-width="2"/>'+DEVI(110,10,.8,False,'#f08aa6')+'<path d="M60 90 q-8 -16 0 -26 q8 10 0 26z" fill="#f08aa6" stroke="#111" stroke-width="2"/>',R),
 mean='You are gentle, gentler than all gentle things, and exceedingly beautiful. Beyond the high and the low, you alone are the Supreme Goddess.',
 plain='You are the gentlest of the gentle and the most beautiful. Higher than the highest, you are the Supreme.',
 words=[('saumyā','<b>gentle</b>'),('saumya-tarā','<b>gentler</b>'),('ati-sundarī','<b>exceedingly beautiful</b>'),('para-aparāṇām paramā','<b>highest of the high and the low</b>')],
 point='<b>Right after the weapons.</b> Verse 80 was terrible; verse 81 is the softest line in the hymn. It is the same pairing as “ati-saumyā ati-raudrā” in chapter 5: most gentle, most fierce.',
 key='Fiercer than any, and <b>gentler than all</b>.'),
dict(n='82',lines=[['yac ca kiṃcit kvacid vastu','sad asad vākhilātmike |'],['tasya sarvasya yā śaktiḥ','sā tvaṃ kiṃ stūyase mayā ‖82‖']],theme='HOW CAN I PRAISE YOU?',
 svg=svg('Brahma on his lotus looking up, small and amazed, at a vast glowing figure that fills the sky',
  '<circle cx="110" cy="70" r="80" fill="#ffd60a" opacity=".3" stroke="none"/>'+DEVI(110,0,1.0,False)+BRAHMA(40,124,.6),R),
 mean='Whatever thing exists anywhere, real or unreal, O Self of all, the power of all of it is you. How can you be praised by me?',
 plain='Whatever exists, real or not, its power is you. So how could I ever praise you enough?',
 words=[('yat kiṃcit kvacit vastu','<b>whatever thing, anywhere</b>'),('sat asat','<b>real or unreal</b>'),('akhila-ātmike','<b>O Self of all</b>'),('śaktiḥ','<b>the power</b>'),('kiṃ stūyase mayā','<b>how are you to be praised by me?</b>')],
 point='<b>Praise runs out.</b> If she is the power in everything, including the one praising, then praise is like a wave praising the ocean. Brahmā sees this and keeps praising anyway.',
 key='The power in everything, <b>even in the one who praises</b>.',
 note='Some editions read tadā for mayā.'),
dict(n='83',lines=[['yayā tvayā jagatsraṣṭā','jagatpātyatti yo jagat |'],['so’pi nidrāvaśaṃ nītaḥ','kas tvāṃ stotum iheśvaraḥ ‖83‖']],theme='EVEN VIṢṆU SLEEPS',
 svg=svg('Vishnu fast asleep on the coiled serpent on the cosmic ocean, a glowing Goddess-shaped sleep resting over his eyes',OCEAN+VISHNU_SLEEP(110,104,1.2)+'<path d="M40 70 q30 -20 60 0" fill="none" stroke="#ffd60a" stroke-width="3" stroke-dasharray="4 4"/>'+T(70,52,'Z z z',14,'#fff'),R),
 mean='You by whom even he who creates, protects and consumes the world has been brought under the power of sleep: who here is able to praise you?',
 plain='You have put even Viṣṇu, maker, keeper and ender of the world, to sleep. Who could praise you?',
 words=[('jagat-sraṣṭā','<b>creator of the world</b>'),('jagat-pāti','<b>protects the world</b>'),('atti','<b>consumes</b>'),('nidrā-vaśaṃ nītaḥ','<b>brought under sleep’s power</b>'),('kaḥ … īśvaraḥ','<b>who is able?</b>')],
 point='<b>The situation, plainly.</b> Viṣṇu is asleep and will not wake, because <i>she</i> is holding him in sleep. So Brahmā appeals directly to the power that holds even the preserver.',
 key='Even Viṣṇu <b>sleeps in her hands</b>.'),
dict(n='84',lines=[['viṣṇuḥ śarīragrahaṇam','aham īśāna eva ca |'],['kāritās te yato’tas tvāṃ','kaḥ stotuṃ śaktimān bhavet ‖84‖']],theme='THE TRINITY TAKES BODY THROUGH HER',
 svg=svg('Brahma, Vishnu and Shiva standing small in a row inside the glowing outline of the Goddess',
  '<circle cx="110" cy="80" r="70" fill="#ffd60a" opacity=".25" stroke="none"/>'+DEVI(110,-6,1.05,False,'#fde4e4')+person(70,140,'#ff8c1a','#e0a800',.6)+person(110,140,'#ffd60a','#3b6fd0',.6)+person(150,140,'#fff','#9fd3f0',.6)+T(70,156,'BRAHMĀ',8)+T(110,156,'VIṢṆU',8)+T(150,156,'ŚIVA',8),R),
 mean='Viṣṇu, I and Īśāna (Śiva) are all made to take bodies by you. Therefore, who could be able to praise you?',
 plain='Viṣṇu, Śiva and I all took our bodies because of you. Who has the power to praise you?',
 words=[('śarīra-grahaṇam','<b>the taking of a body</b>'),('aham','<b>I</b>: Brahmā'),('īśānaḥ','<b>Īśāna</b>: Śiva'),('kāritāḥ te','<b>made to do so by you</b>')],
 point='<b>The boldest line.</b> The three great gods of the Hindu trinity owe their very bodies to her. This is the heart of Śākta theology, spoken by Brahmā himself.',
 key='The trinity itself <b>takes form through her</b>.'),
dict(n='85–87',lab='ŚLOKAS 1.85–87',lines=[['sā tvam itthaṃ prabhāvaiḥ svair','udārair devi saṃstutā |'],['mohayaitau durādharṣāv','asurau madhukaiṭabhau ‖85‖'],['prabodhaṃ ca jagatsvāmī','nīyatām acyuto laghu |'],['bodhaś ca kriyatām asya','hantum etau mahāsurau ‖86–87‖']],theme='THE TWO REQUESTS',
 svg=svg('Brahma with folded hands; on one side two demons look dazed, on the other Vishnu opens his eyes',OCEAN+DEMON(40,140,.8)+DEMON(70,146,.7,'#3a2a6a')+'<path d="M30 92 q10 -10 20 0 q-10 10 0 0" fill="none" stroke="#ffd60a" stroke-width="2"/>'+VISHNU_SLEEP(160,104,.8,False)+BRAHMA(110,40,.6),R),
 mean='You, O Devī, thus praised for your own noble powers: delude these two invincible demons, Madhu and Kaiṭabha. And let Acyuta, the Lord of the world, be quickly awakened; let him be roused to slay these two great demons.',
 words=[('mohaya','<b>delude!</b>'),('durādharṣau','<b>the two invincible ones</b>'),('prabodham nīyatām','<b>let him be awakened</b>'),('laghu','<b>quickly</b>'),('hantum','<b>in order to slay</b>')],
 point='<b>Two requests, both granted.</b> First: confuse the demons. Second: wake Viṣṇu. Watch both come true on the next pages. The demons’ strange mistake is no accident; it is the Goddess answering Brahmā.',
 key='Delude the demons, <b>wake the Lord</b>.'),
]
full1=''.join(fp(v.get('lab','ŚLOKA 1.'+v['n']).replace('ŚLOKAS ','').replace('ŚLOKA ',''),v['lines']) for v in V[:6])
full2=''.join(fp(v.get('lab','ŚLOKA 1.'+v['n']).replace('ŚLOKAS ','').replace('ŚLOKA ',''),v['lines']) for v in V[6:])
for v in V:
    if 'lab' not in v: v['lab']='ŚLOKA 1.'+v['n']
    v['lab']+=' · BRAHMĀ’S HYMN'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Vishnu asleep on the serpent on the cosmic ocean, Brahma on a lotus rising from his navel, two demons approaching, and the Goddess rising like a dark star from Vishnu’s eyes">'
 '<rect width="380" height="268" fill="#14214a" rx="8"/>'+''.join(f'<text x="{(41*k)%370+5}" y="{(29*k+13)%120+12}" font-family="Bangers" font-size="9" fill="#fff">✦</text>' for k in range(20))
 +'<path d="M0 200 q47 -10 95 0 t95 0 t95 0 t95 0 V268 H0z" fill="#2a6ab0" stroke="#111"/>'+VISHNU_SLEEP(200,196,1.8)
 +'<path d="M148 182 q-8 -60 20 -96" fill="none" stroke="#2a7a4a" stroke-width="4"/>'+BRAHMA(168,70,1.0)
 +DEMON(40,230,1.1)+DEMON(80,236,1.0,'#3a2a6a')+'<circle cx="300" cy="70" r="40" fill="#5a2a8a" opacity=".55"/>'+DEVI(300,20,.5,False,'#2b2140','#7a6a9a')+'</svg>')
st1=storypage('sleep','THE SLEEPING LORD','Ślokas 1.67–72',
 panels('Three panels: Vishnu asleep on the serpent on the endless ocean; two demons born from his ear rising up; Brahma on his lotus, terrified, folding his hands',[
  ('#1d3a6a','ONE OCEAN','<rect width="145" height="198" fill="#1d3a6a"/>'+VISHNU_SLEEP(72,120,.9)+'<path d="M0 150 q36 -8 72 0 t72 0 V190 H0z" fill="#2a6ab0"/>'),
  ('#2b2140','BORN FROM HIS EAR','<rect width="145" height="198" fill="#2b2140"/>'+DEMON(50,150,1)+DEMON(100,150,1,'#3a2a6a')+'<circle cx="72" cy="40" r="10" fill="#3b6fd0" stroke="#111"/>'),
  ('#fff3b0','BRAHMĀ IN DANGER',BRAHMA(72,110,1.2)+DEMON(24,170,.6)+DEMON(124,170,.6,'#3a2a6a'))]),
 ['<b>The end of an age.</b> The whole universe has become a single ocean. Lord Viṣṇu lies on the serpent Śeṣa in <b>yoganidrā</b>, the sleep of yoga.',
  '<b>Two demons.</b> From the dirt of Viṣṇu’s ears arise two terrible demons, <b>Madhu</b> and <b>Kaiṭabha</b>.',
  '<b>Brahmā in danger.</b> Brahmā sits on the lotus that grows from Viṣṇu’s navel. The demons come to kill him.',
  '<b>Viṣṇu will not wake.</b> Brahmā sees the Lord asleep and the demons coming.',
  '<b>To whom does he pray?</b> Not to Viṣṇu, but to Yoganidrā, the Goddess dwelling in Viṣṇu’s eyes and holding him in sleep. The hymn that follows is Brahmā’s praise of her.'],
 ("Demons from earwax? That's gross!","It's meant to be! Even the dirt of the Lord's ear holds power, and power without wisdom turns demonic. And notice who Brahmā turns to: not the sleeper, but Sleep."),
 'With Viṣṇu asleep, <b>Brahmā prays to the Goddess who holds him</b>.')
st2=storypage('wake','THE LORD WAKES','Ślokas 1.88–93',
 panels('Three panels: a dark radiant goddess leaving Vishnu’s eyes, mouth and chest; Vishnu rising awake; Vishnu wrestling the two demons',[
  ('#2b2140','SHE LEAVES HIM','<rect width="145" height="198" fill="#2b2140"/>'+VISHNU_SLEEP(72,140,.9)+DEVI(72,10,.5,False,'#5a2a8a','#7a6a9a')+'<path d="M42 130 q10 -50 30 -70" stroke="#ffd60a" stroke-width="2" stroke-dasharray="3 3" fill="none"/>'),
  ('#dfe9f6','HE RISES',person(72,160,'#ffd60a','#3b6fd0',1.4)+'<path d="M58 70 h28 l-4 -12 h-20z" fill="#ffd60a" stroke="#111"/>'),
  ('#ffe3c4','5,000 YEARS',person(40,160,'#ffd60a','#3b6fd0',1)+DEMON(90,160,.9)+DEMON(120,160,.8,'#3a2a6a')+'<path d="M50 120 l30 -10" stroke="#111" stroke-width="3"/>')]),
 ['<b>She leaves.</b> Praised by Brahmā, the dark goddess Tāmasī leaves Viṣṇu’s eyes, mouth, nostrils, arms, heart and chest, and appears before Brahmā.',
  '<b>He wakes.</b> Freed from her, Janārdana (Viṣṇu) rises from his serpent bed on the ocean.',
  '<b>He sees.</b> He sees the two demons, red-eyed with fury, ready to devour Brahmā.',
  '<b>The fight.</b> Viṣṇu fights them with his bare arms, for <b>five thousand years</b>.',
  '<b>No winner.</b> The demons, proud of their great strength, cannot be beaten by force. Something else will decide it.'],
 ("Five thousand years and he couldn't win?","Not by strength alone. Remember Brahmā's first request: 'delude them'. The Goddess is about to answer it."),
 'The Lord wakes, <b>but strength alone is not enough</b>.')
st3=storypage('boon','THE STRANGEST BOON','Ślokas 1.94–104',
 panels('Three panels: the proud demons offering Vishnu a boon; Vishnu asking for their death; Vishnu slaying them on his thighs with his discus',[
  ('#ffe3c4','“CHOOSE A BOON!”',DEMON(40,160,1)+DEMON(80,160,1,'#3a2a6a')+person(120,160,'#ffd60a','#3b6fd0',.9)+'<ellipse cx="60" cy="50" rx="44" ry="20" fill="#fff" stroke="#111" stroke-width="2"/>'+T(60,56,'BOON?',11)),
  ('#dfe9f6','“DIE BY MY HAND”',person(72,160,'#ffd60a','#3b6fd0',1.2)+'<ellipse cx="72" cy="40" rx="52" ry="20" fill="#fff" stroke="#111" stroke-width="2"/>'+T(72,46,'BE SLAIN!',11)),
  ('#fde4e4','ON HIS THIGHS','<path d="M0 150 q36 -8 72 0 t72 0 V190 H0z" fill="#2a6ab0"/>'+person(72,150,'#ffd60a','#3b6fd0',1.2)+'<circle cx="110" cy="70" r="14" fill="#ffd60a" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M110 70 l{14*math.cos(k*0.785):.0f} {14*math.sin(k*0.785):.0f}" stroke="#111"/>' for k in range(8)))]),
 ['<b>Deluded.</b> Bewildered by Mahāmāyā, as Brahmā asked, the proud demons say: “We are pleased with your fighting. Choose a boon from us!”',
  '<b>The Lord’s choice.</b> Viṣṇu says: “If you are pleased, then be slain by me, both of you. What other boon do I need?”',
  '<b>Trapped.</b> Too late, they see the whole world is water. They say: “Then kill us where the earth is not flooded.”',
  '<b>The answer.</b> Viṣṇu takes them on his thighs, the one dry place, and cuts off their heads with his discus.',
  '<b>Her first coming.</b> Medhas ends: “Thus she arose, praised by Brahmā himself. Now hear more of her glory.”'],
 ("Why would demons offer their enemy a wish?","Because the Goddess muddled their minds: Brahmā's first request, granted. Delusion turned their own strength against them."),
 'She deluded the demons and woke the Lord: <b>her first great deed</b>.')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 6 OF 19</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,76px)">MADHU AND KAIṬABHA</h1>
  <div class="series">DEVĪ MĀHĀTMYA · PART 6 · CHAPTER 1, BRAHMĀ’S HYMN</div>
  <div class="tag">The Goddess who held Viṣṇu in sleep · explained and illustrated</div>
  {cover}
  {CAST}
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> The story in <b>comic panels</b>, and <b>Brahmā’s hymn</b> (ślokas 73–87) in full, one page for each verse: the chant, a picture, what it says, the key words, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">WHERE WE ARE</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    <p>In <a href="/bhakti/devi/devi-mahatmya/part-5/">Part 5</a>, a ruined king and a betrayed merchant asked the sage Medhas: why can’t we let go? He answered: Mahāmāyā drags even the wise into delusion; and when she is pleased, she sets us free. “Who is she?” asked the king.</p>
    <p>Medhas begins with her first coming, the <b>first carita</b>, whose deity is <b>Mahākālī</b>. Viṣṇu sleeps on the cosmic ocean; two demons attack Brahmā; and Brahmā sings one of the great hymns of the Goddess.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--red)">With the blessings of the Devī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Viṣṇu needs help? Isn't he the protector?","That's the surprise of this chapter. Even Viṣṇu is held by her, in sleep. The Goddess is the power even the gods depend on.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">BRAHMĀ’S HYMN IN ONE GO</h2>
  <div class="sub">Ślokas 1.73–79</div>
  <div class="full">{full1}</div>
</section>

<section class="page" id="full2">
  <h2 class="page-title">IN ONE GO · CONTINUED</h2>
  <div class="sub">Ślokas 1.80–87</div>
  <div class="full">{full2}</div>
  <div class="note">Text checked word by word against devimahatmyam.aurobharati.in; its readings are followed (verse 77 maheśvarī, verse 82 mayā).</div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">←</span><a href="#foreword">Where We Are</a></li>
    <li><span class="num">🔤</span><a href="#full">Brahmā’s Hymn in One Go</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    <li class="part">THE STORY</li>
    <li><span class="num">★</span><a href="#sleep">The Sleeping Lord</a></li>
    <li class="part">BRAHMĀ’S HYMN · ŚLOKAS 73–87</li>
    {''.join(f'<li><span class="num">{v["n"].split("–")[0]}</span><a href="#v{v["n"]}">{v["theme"].title().replace("Oṃ","Oṃ").replace("’S","’s")}</a></li>' for v in V)}
    <li class="part">THE STORY CONTINUES</li>
    <li><span class="num">★</span><a href="#wake">The Lord Wakes</a></li>
    <li><span class="num">★</span><a href="#boon">The Strangest Boon</a></li>
  </ul>
</section>
''',st1]
for v in V:
    h=vpage(v)
    if len(v['lines'])>=4: h=h.replace(f'<section class="page" id="v{v["n"]}">',f'<section class="page long" id="v{v["n"]}">',1)
    b.append(h)
b+= [st2,st3]
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 6 ON ONE PAGE</h2>
  <div class="sub">Chapter 1, ślokas 67–104, in five lines</div>
  <div class="steps">
    <div><b>The danger.</b> Viṣṇu sleeps on the cosmic ocean; Madhu and Kaiṭabha, born from his ears, attack Brahmā.</div>
    <div><b>The hymn (73–79).</b> Brahmā praises Yoganidrā: the sacred sound and the silence after Oṃ, creator, sustainer and dissolver, knowledge and delusion, every good quality.</div>
    <div><b>The hymn (80–87).</b> Armed and gentle, the power in all things, holding even Viṣṇu in sleep, giving the trinity their bodies: “delude the demons, wake the Lord.”</div>
    <div><b>Both granted.</b> She leaves Viṣṇu; he fights the demons for 5,000 years; deluded, they offer him a boon.</div>
    <div><b>The end.</b> “Be slain by me.” He kills them on his thighs, the only dry place. Thus she first arose.</div>
  </div>
  {talk("What's next?","Part 7: chapter 2, the second carita. The gods have lost heaven to the buffalo demon Mahiṣa, and their fury becomes a blazing light: the Goddess is born.")}
  <div class="key">Part 6: <b>even Viṣṇu sleeps and wakes by her will</b>. 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Devī Māhātmya, chapter 1, ślokas 67–104 (Mārkaṇḍeya Purāṇa). The story is retold in our words; Brahmā’s hymn (ślokas 73–87) was checked word by word against devimahatmyam.aurobharati.in, whose readings and numbering are followed; variant readings are noted. The festival links of the three nights are one popular tradition. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('/home/claude/work/devim/Devi_Mahatmya_Part06.html','w').write(head+''.join(b)+tail())
print('ok')
