exec(open('/home/claude/work/devim/dmc.py').read())
exec(open('/home/claude/work/devim/p13.py').read().split("SRC=[")[0].split("C=8")[1])
C='RV 10.125'
DS=['ahaṁ rudrebhirvasubhiścarāmy / ahamādityairuta viśvadevaiḥ | / ahaṁ mitrāvaruṇobhā bibharmy / ahamindrāgnī ahamaśvinobhā || 1||',
'ahaṁ somamāhanasam bibharmy / ahaṁ tvaṣṭāramuta pūṣaṇaṁ bhagam | / ahaṁ dadhāmi draviṇaṁ haviṣmate / suprāvye yajamānāya sunvate || 2||',
'ahaṁ rāṣṭrī saṃgamanī vasūnām / cikituṣī prathamā yajñiyānām | / tāṁ mā devā vyadadhuḥ purutrā / bhūristhātrāṁ bhūryāveśayantīm || 3||',
'mayā so annamatti yo vipaśyati / yaḥ prāṇiti ya īm śṛṇotyuktam | / amantavo māṁ ta upa kṣiyanti / śrudhi śruta śraddhivam te vadāmi || 4||',
'ahameva svayamidam vadāmi / juṣṭam devebhiruta mānuṣebhiḥ | / yaṁ kāmaye taṃ tamugraṁ kṛṇomi / taṁ brahmāṇaṁ tamṛṣiṁ taṁ sumedhām || 5||',
'ahaṁ rudrāya dhanurā tanomi / brahmadviṣe śarave hantavā u | / ahaṁ janāya samadaṁ kṛṇomy / aham dyāvāpṛthivī ā viveśa || 6||',
'ahaṁ suve pitaramasya mūrdhan / mama yonirapsvantaḥ samudre | / tato vi tiṣṭhe bhuvanānu viśvo / tāmūm dyāṁ varṣmaṇopa spṛśāmi || 7||',
'ahameva vāta iva pra vāmy / ārabhamāṇā bhuvanāni viśvā | / paro divā para enā pṛthivyai / tāvatī mahinā saṁ babhūva || 8||']
FV=[dict(n=str(k+1),lines=L(s)) for k,s in enumerate(DS)]
def full_html(vs,ch): return ''.join(fp(f'{v["n"]}',v['lines']) for v in vs)
def DSV(n,theme,scene,mean,words,point,key):
    v=VP('', str(n), DS[n-1], theme, scene, mean, words, point, key, lab=f'VERSE {n} · DEVĪ SŪKTA')
    return v
V=[
DSV(1,'“I MOVE WITH THE RUDRAS”',
 sc('A radiant woman, Vak, walking among groups of Vedic gods: the Rudras, Vasus, Adityas, Mitra and Varuna, Indra and Agni, the twin Ashvins',GLOW(110,60,50)+DEVI(110,10,.55,False,'#fff')+GODS(150,.4,6,20,36)+T(110,150,'RUDRAS · VASUS · ĀDITYAS',9)),
 'I move with the Rudras and the Vasus, with the Ādityas and all the gods. I uphold both Mitra and Varuṇa; I uphold Indra and Agni, and both the Aśvins.',
 [('aham','<b>I</b>'),('carāmi','<b>I move</b>'),('bibharmi','<b>I uphold, carry</b>'),('ubhā','<b>both</b>')],
 '<b>The oldest hymn of the Goddess.</b> This is Ṛgveda 10.125, the hymn of <b>Vāk</b>, the seer-daughter of the sage Ambhṛṇa. It is the Devī Sūkta the merchant chanted on the riverbank (Part 18), and many recite it after the Devī Māhātmya. Every verse begins with “I”: the Goddess speaks of herself.',
 'The Goddess speaks: <b>“I move with all the gods.”</b>'),
DSV(3,'“I AM THE QUEEN”',
 sc('The Goddess crowned as queen, gathering treasures, standing in many places at once as small copies of her glow across the land',GLOW(110,40,40)+DEVI(110,0,.55,False,'#ffd60a')+''.join(GLOW(30+k*40,130,10)+DEVI(30+k*40,104,.15,False) for k in range(5))),
 'I am the queen, the gatherer of treasures, the knowing one, first among those worthy of worship. The gods have set me in many places, I who abide in many places and enter into many things.',
 [('rāṣṭrī','<b>queen, sovereign</b>'),('saṃgamanī vasūnām','<b>gatherer of treasures</b>'),('cikituṣī','<b>the knowing one</b>'),('purutrā','<b>in many places</b>'),('bhūri-āveśayantīm','<b>entering many things</b>')],
 '<b>Many places, one queen.</b> “The gods set me in many places”: the seed of the whole Devī Māhātmya idea that she takes many forms, and of “yā devī sarvabhūteṣu”, the Goddess in all beings.',
 'She abides in many places, <b>one queen in all</b>.'),
DSV(5,'“WHOM I LOVE, I MAKE MIGHTY”',
 sc('The Goddess touching three people who become a strong warrior, a priest and a wise seer',GLOW(110,40,30)+DEVI(110,0,.45,False,'#fff')+person(40,150,'#c0392b','#c98b5a',.7)+person(110,150,'#ffd60a','#c98b5a',.7)+SAGE(180,150,.7)+T(40,100,'UGRA',9)+T(110,100,'BRAHMĀ',9)+T(180,100,'ṚṢI',9)),
 'I myself declare this, welcomed by gods and by men: whom I love, I make mighty; him I make a brahmā (a priest), him a seer, him wise.',
 [('svayam vadāmi','<b>I myself declare</b>'),('juṣṭam','<b>welcomed, cherished</b>'),('yaṃ kāmaye','<b>whom I love</b>'),('ugram','<b>mighty</b>'),('sumedhām','<b>wise</b>')],
 '<b>Grace.</b> Strength, priesthood, vision and wisdom are her gifts to whomever she loves. Compare the boons of chapter 13: she gave the king his power and the merchant his wisdom.',
 'Strength and wisdom <b>are her gifts</b>.'),
DSV(8,'“I BLOW LIKE THE WIND”',
 sc('A great wind sweeping across all the worlds, the Goddess’s form stretching beyond the sky and beyond the earth',
  '<rect width="220" height="160" fill="#dfe9f6"/>'+''.join(f'<path d="M0 {30+k*24} q60 -16 110 0 t110 0" fill="none" stroke="#9fd3f0" stroke-width="3"/>' for k in range(5))+GLOW(110,70,70)+DEVI(110,0,.85,False,'#fff')),
 'I blow forth like the wind, laying hold of all the worlds. Beyond the sky, beyond this earth: so great have I become in my greatness.',
 [('vāta iva','<b>like the wind</b>'),('ārabhamāṇā','<b>taking hold of</b>'),('bhuvanāni viśvā','<b>all the worlds</b>'),('paraḥ divā','<b>beyond the sky</b>'),('mahinā','<b>by greatness</b>')],
 '<b>Beyond everything.</b> The hymn ends where the Devī Māhātmya ends: she is in all the worlds, and beyond them. This verse is the Vedic root of “ekaivāhaṃ”, “I alone” (Part 15).',
 'In all the worlds, <b>and beyond them</b>.'),
]
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The three great forms of the Goddess, dark Mahakali, golden Mahalakshmi and white Mahasarasvati, standing together, with the Vedic Vak glowing above them">'
 '<rect width="380" height="268" fill="#3a1414" rx="8"/>'+GLOW(190,60,70)+DEVI(190,0,.55,False,'#fff')+DEVI(80,90,.85,False,'#2b2140','#3a3a5a')+DEVI(190,100,.85,False,'#ffd60a')+DEVI(300,90,.85,False,'#f5f5f5')
 +T(80,262,'MAHĀKĀLĪ',13,'#fff')+T(190,262,'MAHĀLAKṢMĪ',13,'#fff')+T(300,262,'MAHĀSARASVATĪ',13,'#fff')+'</svg>')
st_ds=storypage('sukta','THE DEVĪ SŪKTA','Ṛgveda 10.125 · the hymn the merchant chanted',
 panels('Three panels: an ancient Vedic seer-woman singing; the merchant chanting on the riverbank; a modern reader closing the book with the hymn',[
  ('#fff3d0','VĀK SPEAKS',DEVI(72,10,.55,False,'#fff')+FIRE(72,170,.5)),
  ('#e7f4ea','THE MERCHANT',MERCH(72,170,1.0)+'<path d="M0 150 q36 -8 72 0 t72 0 V190 H0z" fill="#4aa3df"/>'),
  ('#fde4e4','AFTER THE TEXT',person(72,170,'#ff8c1a','#c98b5a',.9)+'<rect x="56" y="110" width="32" height="20" fill="#fff3b0" stroke="#111"/>')]),
 ['<b>The oldest voice.</b> The Devī Sūkta is the 125th hymn of the 10th maṇḍala of the Ṛgveda, eight verses. Tradition names its seer Vāk, daughter of the sage Ambhṛṇa.',
  '<b>“I”.</b> Unusually for the Veda, the hymn is in the first person: the divine power describes herself.',
  '<b>In the story.</b> Chapter 13 says the merchant Samādhi chanted “the supreme Devī Sūkta” on the riverbank.',
  '<b>In practice.</b> Many recite it after the 13 chapters; some also before.',
  '<b>Here.</b> All eight verses for chanting, with four of them explained.'],
 ("A Vedic hymn in a Purāṇa series?","The Devī Māhātmya roots itself in the Veda by naming this hymn. Read them together and you see the same Goddess, thousands of years apart: 'I alone', and 'I move with all the gods'."),
 'The Devī Māhātmya’s <b>Vedic root</b>.')
st_p=storypage('pradhanika','SECRET 1 · PRĀDHĀNIKA RAHASYA','The primary secret: where the gods and goddesses come from',
 panels('Three panels: golden Mahalakshmi alone in the void; Mahakali and Mahasarasvati coming from her; three pairs of gods and goddesses',[
  ('#2b2140','MAHĀLAKṢMĪ',DEVI(72,20,.6,False,'#ffd60a')+GLOW(72,60,40)),
  ('#fff3d0','TAMAS · SATTVA',DEVI(40,30,.45,False,'#2b2140','#3a3a5a')+DEVI(104,30,.45,False,'#f5f5f5')),
  ('#fde4e4','THREE PAIRS',GOD(24,90,.4,'#ff8c1a','#e0a800')+DEVI(48,40,.25,False,'#fff')+GOD(72,90,.4,'#fff','#9fd3f0')+DEVI(96,40,.25,False,'#2a9d6f')+GOD(118,90,.4,'#ffd60a','#3b6fd0')+DEVI(130,90,.25,False,'#c0392b')+T(72,170,'BRAHMĀ · RUDRA · VIṢṆU',8))]),
 ['<b>Mahālakṣmī first.</b> King Suratha asks Medhas for the “secret”. Medhas: Mahālakṣmī, made of all three guṇas, is first of all, golden, filling the void.',
  '<b>Mahākālī.</b> Seeing the void, she takes a form of pure <i>tamas</i>: Mahākālī, dark, sword and head in hand. Her names include Mahāmāyā, Kālarātri, hunger, thirst and sleep.',
  '<b>Mahāsarasvatī.</b> Then a form of pure <i>sattva</i>, moon-bright, with book and vīṇā: Mahāsarasvatī, Vāk, Bhāratī.',
  '<b>Three pairs.</b> Mahālakṣmī brings forth Brahmā and Lakṣmī; Mahākālī, Rudra (Śiva) and Sarasvatī; Mahāsarasvatī, Viṣṇu and Gaurī.',
  '<b>Three marriages.</b> She gives Sarasvatī to Brahmā, Gaurī to Rudra and Lakṣmī to Viṣṇu. Brahmā creates, Viṣṇu sustains, Rudra dissolves.'],
 ("So Lakṣmī is Śiva's sister?","In this secret teaching, yes: each god is born beside another god's consort. It's a puzzle on purpose. The point is that all of them come from the one Mahālakṣmī."),
 'All gods and goddesses <b>come from the one Mahālakṣmī</b>.')
st_v=storypage('vaikrtika','SECRET 2 · VAIKṚTIKA RAHASYA','The secret of the forms: how to picture the three',
 panels('Three panels: ten-faced Mahakali; eighteen-armed Mahalakshmi; eight-armed Mahasarasvati',[
  ('#2b2140','10 FACES',''.join(f'<circle cx="{36+(k%5)*18}" cy="{40+(k//5)*18}" r="8" fill="#3a3a5a" stroke="#111"/>' for k in range(10))+DEVI(72,40,.45,True,'#2b2140','#3a3a5a')),
  ('#fff3d0','18 ARMS',''.join(f'<path d="M72 80 l{50*math.cos(math.pi+k*0.185):.0f} {40*math.sin(math.pi+k*0.185):.0f}" stroke="#f2c79b" stroke-width="3"/>' for k in range(18))+DEVI(72,40,.45,False,'#ffd60a')),
  ('#f5f5f5','8 ARMS',''.join(f'<path d="M72 80 l{40*math.cos(math.pi+k*0.45):.0f} {30*math.sin(math.pi+k*0.45):.0f}" stroke="#f2c79b" stroke-width="3"/>' for k in range(8))+DEVI(72,40,.45,False,'#fff'))]),
 ['<b>One Goddess, three ways.</b> She is named Śarvā, Caṇḍikā, Durgā, Bhadrā and Bhagavatī, and pictured in three forms, one for each carita.',
  '<b>Mahākālī</b> (first carita, Brahmā’s hymn): ten faces, ten arms, ten feet, dark as collyrium, thirty eyes; sword, arrow, mace, conch, discus, sling, club, bow and a head.',
  '<b>Mahālakṣmī</b> (second carita, Mahiṣa): born of all the gods’ light; a thousand arms, worshipped with eighteen, from rosary and lotus to bell and noose.',
  '<b>Mahāsarasvatī</b> (third carita, Śumbha): born from Gaurī’s body, eight-armed, traditionally holding bell, trident, plough, conch, pestle, discus, bow and arrows.',
  '<b>Worship.</b> The rest of this rahasya describes how the three and their attendants are worshipped.'],
 ("Why does each carita have its own Goddess?","The Purāṇa tells three stories; this secret gives each a form to meditate on. That's why each part of this series started by naming the carita's deity."),
 'Kālī, Lakṣmī, Sarasvatī: <b>a form for each story</b>.')
st_m=storypage('murti','SECRET 3 · MŪRTI RAHASYA','The secret of the images: the forms she promised in chapter 11',
 panels('Three panels: golden Nanda with lotus; red Raktadantika; blue Shakambhari with vegetables',[
  ('#fff3b0','NANDĀ',DEVI(72,20,.55,False,'#ffd60a')+MOUNT('lotus',72,150,.8)),
  ('#fde4e4','RAKTADANTIKĀ',DEVI(72,20,.55,False,'#c0392b','#e05a3a')),
  ('#dfe9f6','ŚĀKAMBHARĪ',DEVI(72,20,.55,False,'#3b6fd0','#6a8ad0')+''.join(f'<circle cx="{40+k*16}" cy="160" r="6" fill="#2a9d6f" stroke="#111"/>' for k in range(5)))]),
 ['<b>The promised forms.</b> In chapter 11 (Part 16) the Devī promised to return. This rahasya describes how to picture those forms.',
  '<b>Nandā</b>, born to Nanda: golden, on a golden lotus, holding lotus, goad, noose and conch; she is Lakṣmī, Kamalā, Śrī.',
  '<b>Raktadantikā</b>: red garments, red weapons, red eyes and teeth; terrible, yet caring for her devotee like a loving spouse.',
  '<b>Śākambharī</b>: blue, with eyes like blue lotuses, holding greens and fruits; she is also Śatākṣī and Durgā.',
  '<b>Bhīmā and Bhrāmarī</b> follow: the terrible one of the Himālaya and the Goddess of the bees.'],
 ("Do people still worship these forms?","Yes. Nandā Devī in the Himalaya, Śākambharī and Banashankari, Bhrāmarī at Srisailam. The promises of chapter 11 live on as temples."),
 'Her promised forms <b>live on as temples</b>.')
WEEK=[('Day 1','Ch. 1','First carita · Mahākālī','6'),('Day 2','Ch. 2–3','Mahiṣa · Mahālakṣmī','7–8'),('Day 3','Ch. 4','Śakrādi stuti','9'),('Day 4','Ch. 5–8','Yā devī · Dhūmralocana · Kālī · Raktabīja','10–13'),('Day 5','Ch. 9–10','Niśumbha · Śumbha','14–15'),('Day 6','Ch. 11','Nārāyaṇī stuti','16'),('Day 7','Ch. 12–13','Fruits · the boons','17–18')]
week=f'''<section class="page" id="week">
  <h2 class="page-title">READING IT IN SEVEN DAYS</h2>
  <div class="sub">One common way to read the 13 chapters</div>
  <table class="ct"><tr><th>Day</th><th>Chapters</th><th>What happens</th><th>Our parts</th></tr>
  {''.join(f'<tr><td><b>{d}</b></td><td>{c}</td><td>{w}</td><td>{" · ".join(plink(x) for x in p.split("–")) if "–" in p else plink(p)}</td></tr>' for d,c,w,p in WEEK)}
  </table>
  <div class="panel reading pt"><b>Before and after.</b> The limbs come first: Kavacam, Argalā, Kīlakam ({plink(1)} to {plink(4)}). After chapter 13, many recite the Devī Sūkta, the three rahasyas and a prayer asking pardon for mistakes (kṣamā prārthanā). Practice varies by family and tradition: follow your own teacher.</div>
  {talk("Seven days? Not nine?","Many read the text over the nine nights of Navarātri instead, or all at once on Aṣṭamī. The seven-day split is one popular scheme. The Devī herself says even one devoted reading is enough.")}
  <div class="key">Read it at your own pace: <b>one devoted reading is enough</b>.</div>
</section>
'''
SER=[('1','Devī Kavacam I','The Nine Durgās'),('2','Devī Kavacam II','Armour for every limb'),('3','Argalā Stotram','“Rūpaṃ dehi”'),('4','Kīlakam','The pin'),('5','The Frame','King, merchant, sage'),('6','Chapter 1','Madhu and Kaiṭabha'),('7','Chapter 2','The Goddess is born'),('8','Chapter 3','Mahiṣāsura slain'),('9','Chapter 4','Śakrādi stuti'),('10','Chapter 5','Yā devī sarvabhūteṣu'),('11','Chapter 6','Dhūmralocana'),('12','Chapter 7','Cāmuṇḍā'),('13','Chapter 8','Raktabīja'),('14','Chapter 9','Niśumbha'),('15','Chapter 10','Śumbha'),('16','Chapter 11','Nārāyaṇī stuti'),('17','Chapter 12','The fruits of reading'),('18','Chapter 13','The boons'),('19','The Closing','Sūkta and rahasyas')]
series=f'''<section class="page" id="series">
  <h2 class="page-title">THE WHOLE SERIES · 19 PARTS</h2>
  <div class="sub">The Devī Māhātmya in chanting order</div>
  <table class="ct"><tr><th>Part</th><th>Text</th><th>Story</th></tr>
  {''.join(f'<tr><td><b>{plink(p)}</b></td><td>{t}</td><td>{d}</td></tr>' for p,t,d in SER)}
  </table>
  <div class="key">Nineteen parts, <b>one Goddess</b>. 🙏</div>
</section>
'''
P=dict(n=19,ch='',out='/home/claude/work/devim/Devi_Mahatmya_Part19.html',
 title='The Closing · Part 19 · Devī Māhātmya series · srini.presents',
 desc='Devī Māhātmya, Part 19: the closing. The Ṛgvedic Devī Sūkta the merchant chanted, the three secrets (Prādhānika, Vaikṛtika and Mūrti rahasyas) on Mahākālī, Mahālakṣmī and Mahāsarasvatī, a seven-day reading plan and a map of the whole series.',
 h1='THE CLOSING',series='DEVĪ MĀHĀTMYA · PART 19 · SŪKTA AND RAHASYAS',tag='The Vedic hymn and the three secrets · explained and illustrated',cover=cover,
 how='The <b>Devī Sūkta</b> in full for chanting, four of its verses explained, the <b>three rahasyas</b> in comic panels, a seven-day reading plan and a map of all 19 parts.',
 where=[f'In {plink(18)}, the king and the merchant worshipped a clay image on a riverbank for three years. She appeared: one received his kingdom, the other knowledge. The 700 verses were complete.',
  'This last part gathers what is read <b>after</b> the text: the Vedic <b>Devī Sūkta</b> the merchant chanted, and the three <b>rahasyas</b> (“secrets”) that Medhas tells the king about Mahākālī, Mahālakṣmī and Mahāsarasvatī.'],
 wtalk=("There's more after chapter 13?","The story is done, but the recitation tradition adds a Vedic hymn and three short 'secret' teachings. They explain who the three Goddesses of the three caritas really are."),
 fulls=[('THE DEVĪ SŪKTA IN ONE GO','Ṛgveda 10.125, all eight verses',FV)],
 fulltoc='The Devī Sūkta in One Go',
 fullnote='Text as given on devimahatmyam.aurobharati.in (Devī Sūktam); Vedic accent marks omitted. Verse numbers are those of the hymn.',
 seq=[st_ds]+V+[st_p,st_v,st_m,week,series],
 toc=[('THE DEVĪ SŪKTA',[('sukta','The Devī Sūkta')]+V),('THE THREE SECRETS',[('pradhanika','Prādhānika Rahasya'),('vaikrtika','Vaikṛtika Rahasya'),('murti','Mūrti Rahasya')]),('READING THE WHOLE',[('week','Reading It in Seven Days'),('series','The Whole Series')])],
 end=['<b>The Devī Sūkta.</b> Ṛgveda 10.125: “I move with the Rudras… I am the queen… whom I love I make mighty… I blow like the wind, beyond sky and earth.”',
  '<b>Prādhānika rahasya.</b> Mahālakṣmī is first; from her come Mahākālī and Mahāsarasvatī, then Brahmā, Viṣṇu and Rudra with their consorts.',
  '<b>Vaikṛtika rahasya.</b> How to picture the three: ten-faced Mahākālī, eighteen-armed Mahālakṣmī, eight-armed Mahāsarasvatī.',
  '<b>Mūrti rahasya.</b> The forms promised in chapter 11: Nandā, Raktadantikā, Śākambharī, Bhīmā, Bhrāmarī.',
  '<b>The whole.</b> Three limbs, thirteen chapters, the sūkta and the secrets: one Goddess, in every being, who comes whenever she is remembered.'],
 endsub='The closing in five lines',
 next=("Is that the end?","Of this series, yes: all 19 parts. Of the Goddess, never. As she says in chapter 11: whenever trouble arises, I will descend. Go back to Part 1 any Navarātri, and begin again."),
 endkey='<b>one Goddess, in every being, who comes whenever she is remembered</b>.',
 foot='Study notes on the Devī Sūkta (Ṛgveda 10.125) and the three rahasyas recited after the Devī Māhātmya. The sūkta is given as on devimahatmyam.aurobharati.in, without accent marks; the rahasyas are summarised in our words from the translations there. The weapons of Mahāsarasvatī follow her traditional meditation verse; the seven-day plan is one common scheme and practice varies. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.')
build(P)
