import sys; sys.path.insert(0,'/home/claude/work/devim')
from common import *
head=make_head('Devī Kavacam · Part 1 · The Nine Durgās · Devī Māhātmya series · srini.presents',
 'Devī Kavacam, Part 1 of the Devī Māhātmya series: Mārkaṇḍeya’s question, the Nine Durgās, the seven Mothers on their mounts and their weapons, verses 1–17 explained in plain English with illustrations.',
 '  .long .vfig svg{max-height:100px}\n  .long .sloka .mean{font-size:12px}\n  .long .pt{font-size:13.5px}\n  .long .ct td{padding-top:2px;padding-bottom:2px}\n')
V=[
dict(n='1',lab='VERSE 1 · MĀRKAṆḌEYA ASKS',lines=[['yad guhyaṃ paramaṃ loke','sarvarakṣākaraṃ nṛṇām |'],['yan na kasyacid ākhyātaṃ','tan me brūhi pitāmaha ‖1‖']],theme='TELL ME THE SECRET',
 svg=svg('The young sage Markandeya with folded hands before four-faced Brahma seated on a lotus',MOUNT('lotus',150,128,1.4)+'<g stroke="#111" stroke-width="2"><circle cx="150" cy="70" r="14" fill="#e0a800"/><circle cx="136" cy="74" r="10" fill="#e0a800"/><circle cx="164" cy="74" r="10" fill="#e0a800"/><path d="M128 120 q-4 -36 22 -42 q26 6 22 42z" fill="#ff8c1a"/><path d="M150 40 v16" stroke="#fff" stroke-width="6"/></g>'+person(60,140,'#ff8c1a','#c98b5a',1)+T(150,30,'BRAHMĀ',11)+T(60,30,'MĀRKAṆḌEYA',11),R),
 mean='Mārkaṇḍeya said: O Grandsire, tell me that which is supremely secret in the world, which gives every protection to people, and which you have told to no one.',
 plain='The sage asks Brahmā: tell me the great secret that protects people completely, the one you have never shared.',
 words=[('guhyam paramam','<b>the supreme secret</b>'),('sarva-rakṣā-karam','<b>giving all protection</b>'),('nṛṇām','<b>for people</b>'),('na kasyacit ākhyātam','<b>told to no one</b>'),('pitāmaha','<b>Grandsire</b>: Brahmā')],
 point='<b>Where the Kavacam comes from.</b> It is not part of the Mārkaṇḍeya Purāṇa’s 13 chapters. It is one of three hymns, the <b>aṅgas</b> or “limbs”, chanted before the Devī Māhātmya: Kavacam, Argalā, Kīlakam. Here the sage Mārkaṇḍeya, narrator of the Purāṇa, asks Brahmā for it.',
 key='The recitation begins with <b>a request for protection</b>.'),
dict(n='2',lab='VERSE 2 · BRAHMĀ ANSWERS',lines=[['asti guhyatamaṃ vipra','sarvabhūtopakārakam |'],['devyās tu kavacaṃ puṇyaṃ','tac chṛṇuṣva mahāmune ‖2‖']],theme='THE GODDESS’S ARMOUR',
 svg=svg('A shining suit of armour made of light, with the Goddess’s crown above it',
  '<circle cx="110" cy="80" r="62" fill="#ffd60a" opacity=".3" stroke="none"/><g stroke="#111" stroke-width="2.5"><path d="M72 50 q38 -20 76 0 l-6 70 q-32 22 -64 0z" fill="#e0a800"/><path d="M110 40 v100 M80 72 h60 M84 96 h52" stroke="#a87800" fill="none"/><circle cx="110" cy="84" r="10" fill="#c0392b"/></g><path d="M96 34 h28 l-4 -14 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#ffd60a" stroke="#111" stroke-width="2"/>'+T(110,152,'KAVACA',12),R),
 mean='Brahmā said: There is, O brahmin, a most secret thing that helps all beings: the holy armour of the Devī. Listen to it, great sage.',
 plain='Brahmā replies: yes, there is such a secret, and it helps every creature. It is the Goddess’s own armour. Listen.',
 words=[('guhyatamam','<b>most secret</b>'),('vipra','<b>O brahmin</b>'),('sarva-bhūta-upakārakam','<b>helping all beings</b>'),('kavacam','<b>armour</b>, a protective shield'),('puṇyam','<b>holy</b>, meritorious'),('śṛṇuṣva','<b>listen!</b>')],
 point='<b>What a kavaca is.</b> A <i>kavaca</i> is armour. A kavaca hymn “puts on” the deity limb by limb, asking a different power to guard each part of the body. Part 2 of this series covers that head-to-foot armour.',
 key='The Goddess’s protection is <b>armour you put on by chanting</b>.'),
dict(n='3–5',lab='VERSES 3–5 · THE NINE DURGĀS',lines=[['prathamaṃ śailaputrī ca','dvitīyaṃ brahmacāriṇī |'],['tṛtīyaṃ candraghaṇṭeti','kūṣmāṇḍeti caturthakam ‖3‖'],['pañcamaṃ skandamāteti','ṣaṣṭhaṃ kātyāyanīti ca |'],['saptamaṃ kālarātrīti','mahāgaurīti cāṣṭamam ‖4‖'],['navamaṃ siddhidātrī ca','navadurgāḥ prakīrtitāḥ |'],['uktāny etāni nāmāni','brahmaṇaiva mahātmanā ‖5‖']],theme='NINE NAMES, NINE NIGHTS',
 svg=svg('Nine small goddesses in a row, numbered one to nine, each in a different colour',''.join(DEVI(22+22*k,30,.26,False,c)+T(22+22*k,128,str(k+1),12) for k,c in enumerate(['#c0392b','#fff','#ffd60a','#ff8c1a','#2a9d6f','#e05a8a','#222','#f5f5f5','#9b5de5']))+T(110,24,'NAVADURGĀ',14),R),
 mean='First is Śailaputrī, second Brahmacāriṇī, third Candraghaṇṭā, fourth Kūṣmāṇḍā; fifth Skandamātā, sixth Kātyāyanī, seventh Kālarātri, eighth Mahāgaurī; and ninth Siddhidātrī. These are proclaimed the Nine Durgās. These names were spoken by the great Brahmā himself.',
 words=[('nava-durgāḥ','<b>the Nine Durgās</b>'),('prakīrtitāḥ','<b>are proclaimed</b>'),('uktāni etāni nāmāni','<b>these names were spoken</b>'),('brahmaṇā eva','<b>by Brahmā himself</b>')],
 point='<b>The source of the nine nights.</b> These three verses are the classic list of the <b>Navadurgā</b>, the nine forms worshipped one per night of Navarātri, especially in North India. The next page meets all nine.',
 key='Nine forms, <b>one for each night of Navarātri</b>.'),
]
V2=[
dict(n='6–7',lab='VERSES 6–7 · NO HARM COMES',lines=[['agninā dahyamānas tu','śatrumadhye gato raṇe |'],['viṣame durgame caiva','bhayārtāḥ śaraṇaṃ gatāḥ ‖6‖'],['na teṣāṃ jāyate kiṃcid','aśubhaṃ raṇasaṅkaṭe |'],['nāpadaṃ tasya paśyāmi','śokaduḥkhabhayaṃ na hi ‖7‖']],theme='IN FIRE, IN BATTLE, IN FEAR',
 svg=svg('A frightened person surrounded by fire and enemies, protected by a glowing shield in the shape of the Goddess',FIRE(30,120,1)+FIRE(190,120,1)+person(150,150,'#444','#7a9a5a',.7)+person(178,150,'#444','#7a9a5a',.7)+'<circle cx="100" cy="98" r="44" fill="#ffd60a" opacity=".35" stroke="#e0a800" stroke-width="3"/>'+person(100,130,'#ff8c1a','#c98b5a',.9)+DEVI(100,0,.3,False),R),
 mean='One being burned by fire, one fallen among enemies in battle, one in a dangerous or impassable place, those stricken with fear who take refuge in her: nothing inauspicious befalls them in the crisis of battle. I see no calamity for such a one; no grief, no pain, no fear.',
 words=[('agninā dahyamānaḥ','<b>being burned by fire</b>'),('śatru-madhye raṇe','<b>among enemies in battle</b>'),('viṣame durgame','<b>in danger, in places hard to cross</b>'),('bhaya-ārtāḥ','<b>stricken with fear</b>'),('śaraṇaṃ gatāḥ','<b>who have taken refuge</b>'),('śoka-duḥkha-bhayam','<b>grief, pain, fear</b>')],
 point='<b>Refuge is the key word.</b> The promise is not for the brave or the strong but for the <i>bhaya-ārta</i>, those “stricken with fear”, who simply turn to her. Notice <i>durgame</i>: “a place hard to cross”, the very root of the name Durgā.',
 key='Those who turn to her in fear <b>are not left alone</b>.'),
dict(n='8',lab='VERSE 8 · THOSE WHO REMEMBER',lines=[['yais tu bhaktyā smṛtā nūnaṃ','teṣāṃ vṛddhiḥ prajāyate |'],['ye tvāṃ smaranti deveśi','rakṣase tān na saṃśayaḥ ‖8‖']],theme='REMEMBER HER, AND GROW',
 svg=svg('A seedling growing into a tall tree beside a person sitting in prayer, the Goddess watching over them',person(56,146,'#ff8c1a','#c98b5a',.9)+'<path d="M150 150 v-70" stroke="#7a5a3a" stroke-width="7"/><circle cx="150" cy="66" r="34" fill="#2a9d6f" stroke="#111" stroke-width="2"/><circle cx="196" cy="140" r="5" fill="#2a9d6f" stroke="#111"/><path d="M196 150 v-8" stroke="#2a7a4a" stroke-width="2"/>'+DEVI(56,0,.32,False)+T(110,24,'VṚDDHI',12),R),
 mean='For those who remember her with devotion, growth surely comes. O Queen of the gods, those who remember you, you protect them: there is no doubt.',
 plain='Remember her with love and you will flourish. Goddess, you guard all who remember you; of that there is no doubt.',
 words=[('bhaktyā smṛtā','<b>remembered with devotion</b>'),('vṛddhiḥ','<b>growth</b>, prosperity'),('prajāyate','<b>arises</b>'),('deveśi','<b>O Queen of the gods</b>'),('rakṣase','<b>you protect</b>'),('na saṃśayaḥ','<b>no doubt</b>')],
 point='<b>Just remember.</b> No complicated ritual is asked for: <i>smṛtā</i>, remembered. It echoes her own promise in the Devī Māhātmya (chapter 4): call on me in distress and I will come. Mid-verse, Brahmā turns and speaks to her directly: “you protect them”.',
 key='Remember her with love: <b>that is enough</b>.'),
dict(n='9–11',lab='VERSES 9–11 · THE MOTHERS ARRIVE',lines=[['pretasaṃsthā tu cāmuṇḍā','vārāhī mahiṣāsanā |'],['aindrī gajasamārūḍhā','vaiṣṇavī garuḍāsanā ‖9‖'],['māheśvarī vṛṣārūḍhā','kaumārī śikhivāhanā |'],['lakṣmīḥ padmāsanā devī','padmahastā haripriyā ‖10‖'],['śvetarūpadharā devī','īśvarī vṛṣavāhanā |'],['brāhmī haṃsasamārūḍhā','sarvābharaṇabhūṣitā ‖11‖']],theme='EACH ON HER MOUNT',
 svg=svg('A procession of goddesses riding an elephant, Garuda, a bull, a peacock and a swan',''.join(MOUNT(m,28+41*k,128,.62)+DEVI(28+41*k,40,.3,False,c) for k,(m,c) in enumerate([('elephant','#3b6fd0'),('garuda','#1d6fb8'),('bull','#fff'),('peacock','#ff8c1a'),('swan','#ffd60a')])),R),
 mean='Cāmuṇḍā seated on a corpse, Vārāhī seated on a buffalo, Aindrī mounted on an elephant, Vaiṣṇavī seated on Garuḍa; Māheśvarī mounted on a bull, Kaumārī riding a peacock; the goddess Lakṣmī seated on a lotus, lotus in hand, beloved of Hari; the white-formed goddess Īśvarī riding a bull; Brāhmī mounted on a swan, adorned with every ornament.',
 words=[('preta-saṃsthā','<b>seated on a corpse</b>'),('mahiṣa-āsanā','<b>seated on a buffalo</b>'),('gaja-samārūḍhā','<b>mounted on an elephant</b>'),('śikhi-vāhanā','<b>whose vehicle is the peacock</b>'),('haṃsa-samārūḍhā','<b>mounted on a swan</b>'),('sarva-ābharaṇa-bhūṣitā','<b>adorned with all ornaments</b>')],
 point='<b>The Mothers (Mātṛkās).</b> Each is the power (<i>śakti</i>) of a god, riding his mount: Aindrī of Indra, Vaiṣṇavī of Viṣṇu, Māheśvarī of Śiva, Kaumārī of Kumāra, Brāhmī of Brahmā, Vārāhī of the Boar. In chapter 8 they leave the gods’ bodies to fight beside the Devī. Meet them on the next page.',
 key='The gods’ own powers, as goddesses, <b>come to guard us</b>.'),
]
V3=[
dict(n='12–15',lab='VERSES 12–15 · ARMED FOR US',lines=[['ityetā mātaraḥ sarvāḥ','sarvayogasamanvitāḥ |'],['nānābharaṇaśobhāḍhyā','nānāratnopaśobhitāḥ ‖12‖'],['dṛśyante ratham ārūḍhā','devyaḥ krodhasamākulāḥ |'],['śaṅkhaṃ cakraṃ gadāṃ śaktiṃ','halaṃ ca musalāyudham ‖13‖'],['kheṭakaṃ tomaraṃ caiva','paraśuṃ pāśam eva ca |'],['kuntāyudhaṃ triśūlaṃ ca','śārṅgam āyudham uttamam ‖14‖'],['daityānāṃ dehanāśāya','bhaktānām abhayāya ca |'],['dhārayanty āyudhānītthaṃ','devānāṃ ca hitāya vai ‖15‖']],theme='SIXTEEN WEAPONS',
 svg=svg('A rack of divine weapons: conch, discus, mace, spear, plough, pestle, shield, axe, noose, trident and bow',
  '<g stroke="#111" stroke-width="2"><path d="M20 70 q10 -20 24 -6 q-4 14 -24 6z" fill="#fff"/><circle cx="64" cy="58" r="12" fill="#ffd60a"/><circle cx="64" cy="58" r="4" fill="#fff"/><path d="M92 84 v-36" stroke-width="4"/><circle cx="92" cy="44" r="8" fill="#e0a800"/><path d="M120 84 v-40 M114 50 l6 -12 l6 12" fill="none" stroke-width="3"/><path d="M150 84 v-40 M140 44 h20 M144 44 v10" fill="none" stroke-width="3"/><path d="M180 84 v-40" stroke-width="6"/><circle cx="40" cy="116" r="16" fill="#c9a26b"/><path d="M80 136 v-34 M74 104 q12 -12 14 4z" fill="#ccc" stroke-width="2"/><circle cx="118" cy="118" r="12" fill="none" stroke-width="3"/><path d="M152 136 v-40 M144 104 v-10 M160 104 v-10 M144 104 h16" fill="none" stroke-width="3"/><path d="M186 100 q16 18 0 36" fill="none" stroke-width="3"/><path d="M186 100 v36" stroke-width="1"/></g>',R),
 mean='All these Mothers, endowed with every power of yoga, rich in many ornaments and shining with many jewels, are seen mounted on chariots, the goddesses full of wrath. Conch, discus, mace, spear, plough and pestle; shield, javelin, axe and noose; lance, trident and the excellent bow Śārṅga: they hold these weapons to destroy the bodies of demons, to free their devotees from fear, and for the good of the gods.',
 words=[('sarva-yoga-samanvitāḥ','<b>with every yogic power</b>'),('krodha-samākulāḥ','<b>full of wrath</b>'),('daityānāṃ deha-nāśāya','<b>to destroy demons’ bodies</b>'),('bhaktānām abhayāya','<b>for the fearlessness of devotees</b>'),('devānāṃ hitāya','<b>for the good of the gods</b>')],
 point='<b>Wrath on our side.</b> The Mothers are fierce, but the verse says why: to destroy what harms, so that devotees need not fear.',
 key='Every weapon is held <b>so that we need not fear</b>.'),
dict(n='16',lab='VERSE 16 · SALUTATIONS',lines=[['namas te’stu mahāraudre','mahāghoraparākrame |'],['mahābale mahotsāhe','mahābhayavināśini ‖16‖']],theme='GREAT AND TERRIBLE',
 svg=svg('The eight-armed Goddess in fierce form, a person bowing at her feet',DEVI(110,0,.85)+person(40,150,'#ff8c1a','#c98b5a',.7),R),
 mean='Salutations to you, O greatly fierce one, of terrifying valour; of great strength, of great energy, destroyer of great fear.',
 plain='We bow to you, mighty and fierce, unstoppable in strength and courage, who destroys our greatest fears.',
 words=[('mahā-raudre','<b>O greatly fierce one</b>'),('mahā-ghora-parākrame','<b>of terrifying valour</b>'),('mahā-bale','<b>of great strength</b>'),('mahā-utsāhe','<b>of great energy</b>, zeal'),('mahā-bhaya-vināśini','<b>destroyer of great fear</b>')],
 point='<b>Five times “great”.</b> <i>Mahā</i> rings through the line: fierce, terrible, strong, energetic. And it ends where the hymn always ends: she is fierce so that she can destroy <i>our</i> fear.',
 key='Her fierceness <b>destroys our fear</b>.'),
dict(n='17',lab='VERSE 17 · THE ARMOUR BEGINS',lines=[['trāhi māṃ devi duṣprekṣye','śatrūṇāṃ bhayavardhini |'],['prācyāṃ rakṣatu mām aindrī','āgneyyām agnidevatā ‖17‖']],theme='EAST AND SOUTH-EAST',
 svg=svg('A compass rose with Aindri on her elephant guarding the east and the fire goddess guarding the south-east',
  '<circle cx="110" cy="84" r="60" fill="#fff" stroke="#111" stroke-width="2"/><path d="M110 24 v120 M50 84 h120 M68 42 l84 84 M152 42 l-84 84" stroke="#ccc" stroke-width="2"/>'+person(110,96,'#ff8c1a','#c98b5a',.6)+MOUNT('elephant',196,92,.5)+DEVI(196,40,.2,False,'#3b6fd0')+FIRE(176,150,.6)+T(196,28,'EAST',10)+T(176,118,'SE',10),R),
 mean='Protect me, O Devī, you who are hard to look upon, who increase the fear of enemies. In the east may Aindrī protect me; in the south-east, the goddess of fire.',
 plain='Guard me, Goddess too bright to look at, terror of all enemies. Let Aindrī guard my east, and the fire goddess my south-east.',
 words=[('trāhi mām','<b>protect me</b>'),('duṣprekṣye','<b>O you hard to look upon</b>'),('śatrūṇāṃ bhaya-vardhini','<b>increaser of enemies’ fear</b>'),('prācyām','<b>in the east</b>'),('āgneyyām','<b>in the south-east</b>'),('agni-devatā','<b>the goddess of fire</b>')],
 point='<b>From here, the armour.</b> The prayer now turns to space itself: one goddess for each of the ten directions, then one for every part of the body, head to foot. That is <b>Part 2</b>.',
 key='The armour starts: <b>a guardian for every direction</b>.'),
]
ND=[('ŚAILAPUTRĪ','Day 1 · daughter of the mountain','Pārvatī as Himālaya’s daughter; trident and lotus.',MINI('#c0392b',mount='bull')),
 ('BRAHMACĀRIṆĪ','Day 2 · the ascetic','She did penance to win Śiva; rosary and water-pot.',MINI('#fff','#f2c79b',sym='<circle cx="86" cy="60" r="8" fill="none" stroke="#7a5a3a" stroke-width="3" stroke-dasharray="2 2"/><path d="M28 56 h12 v14 h-12z" fill="#c9a26b" stroke="#111"/>')),
 ('CANDRAGHAṆṬĀ','Day 3 · the moon-bell','A half-moon like a bell on her brow; rides a tiger.',MINI('#ffd60a',mount='tiger',sym='<path d="M50 8 q10 10 20 0" fill="none" stroke="#e0a800" stroke-width="4"/>')),
 ('KŪṢMĀṆḌĀ','Day 4 · smile of creation','Said to have made the cosmic egg with her smile.',MINI('#ff8c1a',mount='lion',sym='<ellipse cx="94" cy="26" rx="12" ry="15" fill="#ffd60a" stroke="#111"/>')),
 ('SKANDAMĀTĀ','Day 5 · mother of Skanda','Holds baby Skanda (Kārttikeya) on her lap.',MINI('#2a9d6f',mount='lion',sym='<circle cx="74" cy="58" r="7" fill="#f2c79b" stroke="#111"/>')),
 ('KĀTYĀYANĪ','Day 6 · the warrior','Born to sage Kātyāyana; slayer of Mahiṣāsura.',MINI('#e05a8a',mount='lion',sym='<path d="M90 70 l14 -50" stroke="#ccc" stroke-width="4"/>')),
 ('KĀLARĀTRI','Day 7 · the dark night','Fierce and dark, she destroys all darkness; on a donkey.',MINI('#222','#3a3a5a','donkey')),
 ('MAHĀGAURĪ','Day 8 · the radiant white','Brilliant white, calm and gentle; on a white bull.',MINI('#f5f5f5','#fbe9e0','bull')),
 ('SIDDHIDĀTRĪ','Day 9 · giver of perfection','Grants the siddhis; seated on a lotus.',MINI('#9b5de5',mount='lotus'))]
MT=[('CĀMUṆḌĀ','on a corpse','The fierce slayer of Caṇḍa and Muṇḍa (chapter 7).',MINI('#5a2a2a','#7a6a5a','corpse')),
 ('VĀRĀHĪ','on a buffalo','Power of Varāha, the Boar.',MINI('#333',mount='buffalo')),
 ('AINDRĪ','on an elephant','Power of Indra; holds the thunderbolt.',MINI('#3b6fd0',mount='elephant')),
 ('VAIṢṆAVĪ','on Garuḍa','Power of Viṣṇu; conch and discus.',MINI('#1d6fb8',mount='garuda')),
 ('MĀHEŚVARĪ','on a bull','Power of Śiva; trident.',MINI('#fff',mount='bull')),
 ('KAUMĀRĪ','on a peacock','Power of Kumāra (Skanda); spear.',MINI('#ff8c1a',mount='peacock')),
 ('LAKṢMĪ','on a lotus','Lotus in hand, beloved of Hari.',MINI('#e05a8a',mount='lotus')),
 ('ĪŚVARĪ','on a bull','The white-formed goddess.',MINI('#f5f5f5','#fbe9e0','bull','#ddd')),
 ('BRĀHMĪ','on a swan','Power of Brahmā; adorned with every ornament.',MINI('#ffd60a',mount='swan'))]
def tiles(L): return '<div class="g3">'+''.join(f'<div class="tile">{s}<h4>{n}</h4><p class="nt2">{d}</p><p>{t}</p></div>' for n,d,t,s in L)+'</div>'
ALL=V+V2+V3
full1=''.join(fp(v['lab'].split(' · ')[0],v['lines']) for v in V+V2[:1])
full2=''.join(fp(v['lab'].split(' · ')[0],v['lines']) for v in V2[1:]+V3)
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The Goddess standing in golden armour of light, with nine smaller goddesses in an arc around her">'
 '<rect width="380" height="268" fill="#3a1414" rx="8"/><circle cx="190" cy="120" r="96" fill="#ffd60a" opacity=".22"/>'
 +''.join(DEVI(190+150*math.cos(math.pi+k*math.pi/8),196+150*math.sin(math.pi+k*math.pi/8)-90,.3,False,c) for k,c in enumerate(['#c0392b','#fff','#ffd60a','#ff8c1a','#2a9d6f','#e05a8a','#222','#f5f5f5','#9b5de5']))
 +'<path d="M150 120 q40 -24 80 0 l-6 90 q-34 20 -68 0z" fill="#e0a800" stroke="#111" stroke-width="3" opacity=".9"/>'+DEVI(190,40,1.0)+LION(190,248,.9)+'</svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: a reader begins the Devi Mahatmya by chanting the Kavacam, Argala and Kilakam; the thirteen chapters; the closing rahasyas">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#fde4e4','3 LIMBS FIRST'),('#fff3b0','13 CHAPTERS'),('#e7f4ea','3 SECRETS AFTER')]))
 +''.join(f'<rect x="{24+k*40}" y="{60}" width="30" height="90" fill="{c}" stroke="#111" stroke-width="2"/><text x="{39+k*40}" y="{110}" text-anchor="middle" font-family="Bangers" font-size="11" transform="rotate(-90 {39+k*40} 110)">{t}</text>' for k,(c,t) in enumerate([('#e0a800','KAVACA'),('#ff8c1a','ARGALĀ'),('#c0392b','KĪLAKA')]))
 +''.join(f'<rect x="{168+(k%5)*24}" y="{40+(k//5)*50}" width="20" height="42" fill="#fff" stroke="#111" stroke-width="2"/><text x="{178+(k%5)*24}" y="{66+(k//5)*50}" text-anchor="middle" font-family="Bangers" font-size="11">{k+1}</text>' for k in range(13))
 +''.join(f'<circle cx="{345+k*38}" cy="100" r="15" fill="#2a9d6f" stroke="#111" stroke-width="2"/><text x="{345+k*38}" y="105" text-anchor="middle" font-family="Bangers" font-size="13" fill="#fff">{k+1}</text>' for k in range(3))+'</svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 1 OF 19</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,76px)">DEVĪ KAVACAM</h1>
  <div class="series">DEVĪ MĀHĀTMYA · PART 1 · THE NINE DURGĀS</div>
  <div class="tag">The Goddess’s armour, verses 1–17 · explained and illustrated</div>
  {cover}
  {CAST}
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> This series follows the Devī Māhātmya in the order it is chanted, in 19 parts. Part 1 starts with the <b>Devī Kavacam</b>: first verses 1–17 for chanting, then the story, and one page for each verse or group, with the <b>Nine Durgās</b> and the <b>Mothers</b> each on a page of their own.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    <p>The <b>Devī Māhātmya</b>, also called the Durgā Saptaśatī or Caṇḍī Pāṭha, is the great scripture of the Goddess: 13 chapters of the Mārkaṇḍeya Purāṇa, traditionally counted as 700 mantras. Through every Navarātri it is chanted in temples and homes across India.</p>
    <p>Before the story begins, the reader puts on armour. The <b>Devī Kavacam</b>, “the Goddess’s armour”, asks her powers to guard every direction and every part of the body. It opens with one of the best-loved lists in Hindu worship: the <b>Nine Durgās</b> of the nine nights.</p>
    <p>This series will take you through the whole text, in the order it is chanted.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--red)">With the blessings of the Devī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why wear armour before reading a book?","Because the Devī Māhātmya is a war story, and a powerful one. Tradition says: protect yourself first, then open the door, then read.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 1–17 IN ONE GO</h2>
  <div class="sub">Devī Kavacam, first half</div>
  <div class="full">{full1}</div>
</section>

<section class="page" id="full2">
  <h2 class="page-title">IN ONE GO · CONTINUED</h2>
  <div class="sub">Verses 8–17</div>
  <div class="full">{full2}</div>
  <div class="note">Verse numbers follow shlokam.org (56 verses). Verses 18–56, the armour for each direction and limb, are in Part 2.</div>
</section>

<section class="page" id="story">
  <h2 class="page-title">THE STORY · HOW THE TEXT IS CHANTED</h2>
  <div class="sub">Three limbs, thirteen chapters, three secrets</div>
  {story_svg}
  <div class="panel" style="margin-top:12px">
    <span class="caption">The recitation in 5 frames</span>
    <div class="steps" style="margin:0">
      <div><b>The core.</b> The Devī Māhātmya proper is chapters 81–93 of the Mārkaṇḍeya Purāṇa: 13 chapters, three great battles of the Goddess.</div>
      <div><b>The three limbs (aṅgas).</b> Before it, readers chant the <b>Kavacam</b> (armour), the <b>Argalā</b> (the bolt) and the <b>Kīlakam</b> (the pin).</div>
      <div><b>Who speaks.</b> In the Kavacam, the sage Mārkaṇḍeya asks Brahmā, the creator, for the most secret protection.</div>
      <div><b>The 13 chapters.</b> The story of King Suratha, the merchant Samādhi and the sage Medhas, who tells them of the Goddess.</div>
      <div><b>The three secrets (rahasyas).</b> After the text come three short “secret” teachings on her forms.</div>
    </div>
  </div>
  {talk("Is the Kavacam in the Purāṇa?","Not in its 13 chapters. It belongs to the recitation tradition around it, like the Argalā and Kīlakam, and is chanted as part of the whole.")}
</section>

<section class="page" id="about">
  <h2 class="page-title">THIS SERIES · 19 PARTS</h2>
  <div class="sub">The Devī Māhātmya in chanting order</div>
  <table class="ct">
    <tr><th>Part</th><th>Text</th><th>What happens</th></tr>
    {''.join(f'<tr><td><b>{p}</b></td><td>{t}</td><td>{d}</td></tr>' for p,t,d in SERIES)}
  </table>
  <div class="note">Chapter 5’s hymn is already explained in full: <a href="/bhakti/devi/ya-devi-sarvabhuteshu/">Yā Devī Sarvabhūteṣu</a>. So is <a href="/bhakti/devi/mahishasura-mardini/">Mahiṣāsura Mardinī</a>, a later hymn on the chapter 2–3 story.</div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">In One Go</a></li>
    <li><span class="num">★</span><a href="#story">How It’s Chanted</a></li>
    <li><span class="num">ℹ</span><a href="#about">The 19 Parts</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    <li class="part">VERSES 1–17</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title().replace("’S","’s")}</a></li>' for v in ALL)}
    <li><span class="num">9</span><a href="#nd">Meet the Nine Durgās</a></li>
    <li><span class="num">M</span><a href="#mt">Meet the Mothers</a></li>
  </ul>
</section>
''']
for v in V: b.append(vpage(v))
b.append(f'''<section class="page" id="nd">
  <h2 class="page-title">MEET THE NINE DURGĀS</h2>
  <div class="sub">One form for each night of Navarātri</div>
  {tiles(ND)}
  <div class="note">Day order and iconography follow popular Navarātri tradition; details vary by region.</div>
</section>
''')
for v in V2:
    if v['n']=='9–11': v['words']=v['words'][:4]
    b.append(vpage(v).replace('<section class="page" id="v9–11">','<section class="page long" id="v9–11">'))
b.append(f'''<section class="page" id="mt">
  <h2 class="page-title">MEET THE MOTHERS</h2>
  <div class="sub">The Mātṛkās of verses 9–11, each on her mount</div>
  {tiles(MT)}
  <div class="note">The Kavacam names nine riders here; lists of the Mothers (seven or eight) vary between texts.</div>
</section>
''')
V3[0]['words']=[]
for v in V3: b.append(vpage(v).replace('<section class="page" id="v12–15">','<section class="page long" id="v12–15">'))
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 1 ON ONE PAGE</h2>
  <div class="sub">Verses 1–17 in five lines</div>
  <div class="steps">
    <div><b>Verses 1–2.</b> Mārkaṇḍeya asks Brahmā for the supreme secret of protection; Brahmā gives him the Goddess’s armour.</div>
    <div><b>Verses 3–5.</b> The Nine Durgās, Śailaputrī to Siddhidātrī: the goddesses of the nine nights.</div>
    <div><b>Verses 6–8.</b> In fire, battle or fear, those who take refuge in her come to no harm; those who remember her flourish.</div>
    <div><b>Verses 9–15.</b> The Mothers ride out on their mounts, armed to destroy demons and free devotees from fear.</div>
    <div><b>Verses 16–17.</b> Salutations to the fierce one, and the armour begins: Aindrī in the east, Agni’s goddess in the south-east.</div>
  </div>
  {talk("What comes next?","Part 2: the armour itself. A guardian for every direction, and a goddess for every part of the body, head to toe.")}
  <div class="key">Part 1: <b>turn to her in fear, and you are armoured</b>. 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Devī Kavacam, verses 1–17, chanted before the Devī Māhātmya (Durgā Saptaśatī). Text checked word by word against shlokam.org (56 verses); differences are spelling only (bhayārttāḥ, raṇasaṃkaṭe, bhayavarddhini). The Navadurgā day order and iconography follow popular tradition. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('/home/claude/work/devim/Devi_Mahatmya_Part01.html','w').write(head+''.join(b)+tail())
print('ok')
