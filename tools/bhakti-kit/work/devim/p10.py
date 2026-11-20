exec(open('/home/claude/work/devim/dmc.py').read())
C=5
REF='namastasyai namastasyai namastasyai namo namaḥ'
FORMS=[('viṣṇumāyeti śabditā','14–16'),('cetanetyabhidhīyate','17–19'),('buddhirūpeṇa saṃsthitā','20–22'),('nidrārūpeṇa saṃsthitā','23–25'),('kṣudhārūpeṇa saṃsthitā','26–28'),('chāyārūpeṇa saṃsthitā','29–31'),('śaktirūpeṇa saṃsthitā','32–34'),('tṛṣṇārūpeṇa saṃsthitā','35–37'),('kṣāntirūpeṇa saṃsthitā','38–40'),('jātirūpeṇa saṃsthitā','41–43'),('lajjārūpeṇa saṃsthitā','44–46'),('śāntirūpeṇa saṃsthitā','47–49'),('śraddhārūpeṇa saṃsthitā','50–52'),('kāntirūpeṇa saṃsthitā','53–55'),('lakṣmīrūpeṇa saṃsthitā','56–58'),('vṛttirūpeṇa saṃsthitā','59–61'),('smṛtirūpeṇa saṃsthitā','62–64'),('dayārūpeṇa saṃsthitā','65–67'),('tuṣṭirūpeṇa saṃsthitā','68–70'),('mātṛrūpeṇa saṃsthitā','71–73'),('bhrāntirūpeṇa saṃsthitā','74–76')]
def ydsrc(f,n): return f'yā devī sarvabhūteṣu {f} | / {REF} || {n}||'
FD={n:ydsrc(f,n) for f,n in FORMS}
SRC={'9':'namo devyai mahādevyai śivāyai satataṁ namaḥ | / namaḥ prakṛtyai bhadrāyai niyatāḥ praṇatāḥ sma tām || 9||',
'10':'raudrāyai namo nityāyai gauryai dhātryai namo namaḥ | / jyotsnāyai cendurūpiṇyai sukhāyai satataṁ namaḥ || 10||',
'11':'kalyāṇyai praṇatāmṛddhyai siddhyai kurmo namo namaḥ | / nairṛtyai bhūbhṛtāṁ lakṣmyai śarvāṇyai te namo namaḥ || 11||',
'12':'durgāyai durgapārāyai sārāyai sarvakāriṇyai | / khyātyai tathaiva kṛṣṇāyai dhūmrāyai satataṁ namaḥ || 12||',
'13':'atisaumyātiraudrāyai natāstasyai namo namaḥ | / namo jagatpratiṣṭhāyai devyai kṛtyai namo namaḥ || 13||',
'77':'indriyāṇāmadhiṣṭhātrī bhūtānāṁ cākhileṣu yā | / bhūteṣu satataṁ tasyai vyāptyai devyai namo namaḥ || 77||',
'78–80':'citirūpeṇa yā kṛtsnametad vyāpya sthitā jagat | / namastasyai namastasyai namastasyai namo namaḥ || 78–80||',
'81':'stutā suraiḥ pūrvamabhīṣṭasaṁśrayā- / ttathā surendreṇa dineṣu sevitā | / karotu sā naḥ śubhaheturīśvarī / śubhāni bhadrāṇyabhihantu cāpadaḥ || 81||',
'82':'yā sāmprataṁ coddhatadaityatāpitai- / rasmābhirīśā ca surairnamasyate | / yā ca smṛtā tatkṣaṇameva hanti naḥ / sarvāpado bhaktivinamramūrtibhiḥ || 82||'}
SRC.update(FD)
ORDER=['9','10','11','12','13']+[n for f,n in FORMS]+['77','78–80','81','82']
FV=[dict(n=k,lines=L(SRC[k])) for k in ORDER]
def S(*ks): return ' / '.join(SRC[k] for k in ks)
HY='YĀ DEVĪ SARVABHŪTEṢU'
def YDP(a,b,theme,scene,mean,words,point,key):
    na=dict(FORMS)[a] if False else [n for f,n in FORMS if f==a][0]
    if b:
        nb=[n for f,n in FORMS if f==b][0]; n=na.split('–')[0]+'–'+nb.split('–')[1]; src=FD[na]+' / '+FD[nb]
    else: n=na; src=FD[na]
    v=VP(C,n,src,theme,scene,mean,words,point,key); v['lab']+=' · '+HY; return v
def ICON(e,x,y,s=28,lab=''): return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{s}">{e}</text>'+(T(x,y+20,lab,10) if lab else '')
def TWO(e1,l1,e2,l2): return sc(f'Two pictures side by side: {l1} and {l2}, each glowing with the Goddess’s light','<rect x="4" y="4" width="104" height="152" fill="#fff8ec" stroke="#111"/><rect x="112" y="4" width="104" height="152" fill="#fff8ec" stroke="#111"/>'+GLOW(56,70,36)+GLOW(164,70,36)+ICON(e1,56,82,40)+ICON(e2,164,82,40)+T(56,140,l1.upper(),11)+T(164,140,l2.upper(),11))
V=[
VP(C,'5–7','hṛtādhikārāstridaśāstābhyāṁ sarve nirākṛtāḥ | / mahāsurābhyāṁ tāṁ devīṁ saṁsmarantyaparājitām || 5|| / tayāsmākaṁ varo datto yathāpatsu smṛtākhilāḥ | / bhavatāṁ nāśayiṣyāmi tatkṣaṇātparamāpadaḥ || 6|| / iti kṛtvā matiṁ devā himavantaṁ nageśvaram | / jagmustatra tato devīṁ viṣṇumāyāṁ pratuṣṭuvuḥ || 7||',
 'THEY REMEMBERED THE BOON',
 sc('Exiled gods climbing the snowy Himalaya together, a thought bubble showing the Goddess’s promise',HIMA+GODS(150,.45,5,40,34)+'<ellipse cx="150" cy="40" rx="56" ry="26" fill="#fff" stroke="#111" stroke-width="2"/>'+DEVI(150,14,.25,False)+T(120,46,'“remember me”',8)),
 'Stripped of their offices and driven out by those two great asuras, the gods all remembered the unconquered Devī: “She gave us a boon: ‘Whenever you remember me in danger, I will at once destroy all your worst dangers.’” Resolved on this, the gods went to Himavān, lord of mountains, and there praised the Devī, Viṣṇumāyā.',
 [('hṛta-adhikārāḥ','<b>stripped of their offices</b>'),('aparājitā','<b>the unconquered one</b>'),('smṛtā','<b>remembered</b>'),('tat-kṣaṇāt','<b>that very moment</b>'),('viṣṇu-māyā','<b>the power of Viṣṇu</b>')],
 '<b>The boon is used.</b> At the end of chapter 4 the gods asked: “remember you, and you remove our dangers.” Now new tyrants, the brothers <b>Śumbha and Niśumbha</b>, have taken everything, and the gods do the one thing they were promised would work: they remember her.',
 'In danger, the gods <b>remember her promise</b>.'),
VP(C,'9–10',S('9','10'),'NAMO DEVYAI',
 sc('The gods with folded hands bowing to the Goddess on the snowy Himalaya, the moon above',HIMA+MOON(180,30,14)+DEVI(110,10,.6,False)+GODS(150,.45,4,40,46)),
 'Salutations to the Devī, to the Great Devī, to Śivā, the auspicious, always salutations; salutations to Prakṛti, to Bhadrā; with minds controlled we bow to her. Salutations to the fierce one, to the eternal one, to Gaurī, to the sustainer, salutations again and again; to her who is moonlight, whose form is the moon, to her who is happiness, always salutations.',
 [('namaḥ','<b>salutation</b>'),('śivā · bhadrā','<b>the auspicious · the kind</b>'),('prakṛti','<b>Nature</b>'),('raudrā','<b>the fierce</b>'),('dhātrī','<b>the sustainer</b>, nurse'),('jyotsnā · indu-rūpiṇī','<b>moonlight · moon-formed</b>')],
 '<b>The hymn opens.</b> The best-known prelude to “yā devī”. Fierce (raudrā) and moonlight-gentle (jyotsnā) sit side by side in one verse, as always in this text.',
 'Salutations to the fierce one, <b>and to the moonlight</b>.'),
VP(C,'11–13',S('11','12','13'),'MOST GENTLE, MOST FIERCE',
 sc('Half of the Goddess’s face calm and silver, the other half fierce and red, with a boat crossing a river below',
  '<path d="M110 20 a50 50 0 0 0 0 100z" fill="#fff8c0" stroke="#111" stroke-width="2"/><path d="M110 20 a50 50 0 0 1 0 100z" fill="#e05a3a" stroke="#111" stroke-width="2"/><circle cx="92" cy="62" r="4" fill="#111"/><circle cx="128" cy="62" r="4" fill="#111"/><path d="M118 52 l16 4" stroke="#111" stroke-width="3"/>'+'<path d="M0 140 q55 -10 110 0 t110 0" fill="none" stroke="#2a6ab0" stroke-width="4"/><path d="M90 136 h40 l-6 8 h-28z" fill="#c9a26b" stroke="#111"/>'+T(70,14,'ATI-SAUMYĀ',9)+T(150,14,'ATI-RAUDRĀ',9)),
 'To Kalyāṇī, who is the prosperity of those who bow, to Siddhi, we make salutations again and again; to Nairṛtī, to the Lakṣmī of kings, to Śarvāṇī, salutations to you. To Durgā, who carries across difficulties; to the essence, the doer of all; to Khyāti (fame), to Kṛṣṇā (the dark one), to Dhūmrā (the smoky one), always salutations. To her who is most gentle and most fierce we bow, salutations; salutations to the foundation of the world, to the Devī who is action, salutations again and again.',
 [('kalyāṇī','<b>the auspicious</b>'),('siddhi','<b>success, attainment</b>'),('durga-pārā','<b>who carries across difficulties</b>'),('sarva-kāriṇī','<b>doer of all</b>'),('ati-saumyā ati-raudrā','<b>most gentle, most fierce</b>'),('kṛti','<b>action</b>')],
 '<b>“Atisaumyā atiraudrā”.</b> In two words, the whole Devī Māhātmya: the gentlest and the fiercest. She is also <i>kṛti</i>, action itself, and the ground (pratiṣṭhā) the world stands on.',
 'Most gentle and <b>most fierce</b>, together.'),
YDP('viṣṇumāyeti śabditā',None,'SHE IS CALLED VIṢṆUMĀYĀ',
 sc('The Goddess at the heart of every being, a tiny glow inside each person, animal and plant, with Vishnu asleep on the ocean behind',OCEAN+VISHNU_SLEEP(110,104,.8)+''.join(GLOW(30+k*40,140,8)+person(30+k*40,156,'#ff8c1a','#c98b5a',.35) for k in range(5))+DEVI(110,0,.35,False)),
 'To the Devī who in all beings is called Viṣṇumāyā: salutations to her, salutations to her, salutations to her, salutations again and again.',
 [('yā devī','<b>the Goddess who</b>'),('sarva-bhūteṣu','<b>in all beings</b>'),('viṣṇu-māyā','<b>Viṣṇu’s power</b>'),('śabditā','<b>is called</b>'),('namas tasyai','<b>salutation to her</b>')],
 '<b>The pattern begins.</b> 21 times the gods will say “the Devī who in all beings is…”, each time followed by a triple “namas tasyai”. The first is <b>Viṣṇumāyā</b>: the power that held Viṣṇu in sleep in chapter 1, now found in every being.',
 'The first of 21: <b>she is Viṣṇumāyā in all beings</b>.'),
YDP('cetanetyabhidhīyate',None,'SHE IS CONSCIOUSNESS',
 sc('Many people, animals and a plant, each with a small flame of awareness in the head, all linked to one great flame',GLOW(110,40,30,'#ffd60a',.5)+FIRE(110,40,.5)+''.join(f'<path d="M110 50 L{30+k*40} 118" stroke="#e0a800" stroke-width="1.5"/>'+person(30+k*40,150,'#ff8c1a','#c98b5a',.4)+'<circle cx="'+str(30+k*40)+'" cy="118" r="4" fill="#ffd60a" stroke="#111"/>' for k in range(5))),
 'To the Devī who in all beings is called Consciousness: salutations to her, salutations to her, salutations to her, salutations again and again.',
 [('cetanā','<b>consciousness, awareness</b>'),('abhidhīyate','<b>is named</b>')],
 '<b>The deepest one first.</b> Before any quality, she is <i>cetanā</i>: the awareness by which anything is known at all. Every feeling and thought in the list that follows happens inside this awareness.',
 'The awareness in every being <b>is the Goddess</b>.'),
YDP('buddhirūpeṇa saṃsthitā','nidrārūpeṇa saṃsthitā','INTELLIGENCE AND SLEEP','TWO',
 'To the Devī who dwells in all beings as intelligence; to the Devī who dwells in all beings as sleep: salutations to her, salutations to her, salutations to her, salutations again and again.',
 [('buddhi','<b>intelligence</b>, discernment'),('nidrā','<b>sleep</b>'),('rūpeṇa saṃsthitā','<b>abides in the form of</b>')],
 '<b>Waking mind and sleep.</b> Buddhi is the clear mind of the day; nidrā is rest, the sleep that restores us. Both are holy. Remember: she was Yoganidrā, the sleep of Viṣṇu, in chapter 1.',
 'Clear thinking and deep sleep <b>are both her</b>.'),
YDP('kṣudhārūpeṇa saṃsthitā','chāyārūpeṇa saṃsthitā','HUNGER AND SHADE','TWO',
 'To the Devī who dwells in all beings as hunger; as shade: salutations to her, again and again.',
 [('kṣudhā','<b>hunger</b>'),('chāyā','<b>shade, shadow</b>, also reflection')],
 '<b>Even hunger?</b> Yes. Hunger keeps every creature alive and moving; it is her power at work. And <i>chāyā</i>, shade, is the cool rest she gives the tired, or, some say, the reflection of the Self in the mind.',
 'Hunger keeps life going: <b>that too is her</b>.'),
YDP('śaktirūpeṇa saṃsthitā','tṛṣṇārūpeṇa saṃsthitā','POWER AND THIRST','TWO',
 'To the Devī who dwells in all beings as power; as thirst: salutations to her, again and again.',
 [('śakti','<b>power, energy</b>'),('tṛṣṇā','<b>thirst</b>, also craving')],
 '<b>Śakti in name.</b> “Śakti” is her very name: the energy in every movement. <i>Tṛṣṇā</i> is thirst, and also craving. The text does not hide that desire, too, is her power, which is why the next lines balance it.',
 'All energy, <b>even craving, is her power</b>.'),
YDP('kṣāntirūpeṇa saṃsthitā','jātirūpeṇa saṃsthitā','PATIENCE AND BIRTH','TWO',
 'To the Devī who dwells in all beings as patience; as birth (or kind): salutations to her, again and again.',
 [('kṣānti','<b>patience, forbearance</b>'),('jāti','<b>birth</b>; also one’s kind or nature')],
 '<b>Forbearance.</b> Kṣānti is the strength to bear hurt without striking back. Jāti here means birth or kind: the way every creature is born into its own nature.',
 'Patience is <b>her strength in us</b>.'),
YDP('lajjārūpeṇa saṃsthitā','śāntirūpeṇa saṃsthitā','CONSCIENCE AND PEACE','TWO',
 'To the Devī who dwells in all beings as modesty; as peace: salutations to her, again and again.',
 [('lajjā','<b>modesty, conscience</b>, the sense of shame that stops wrong'),('śānti','<b>peace</b>')],
 '<b>The inner brakes.</b> Lajjā is the healthy shame that stops us before we do wrong. Śānti is the peace that follows a clean conscience. Brahmā already named both in chapter 1 (Part 6).',
 'Conscience and peace <b>are her presence within</b>.'),
YDP('śraddhārūpeṇa saṃsthitā','kāntirūpeṇa saṃsthitā','FAITH AND BEAUTY','TWO',
 'To the Devī who dwells in all beings as faith; as beauty (radiance): salutations to her, again and again.',
 [('śraddhā','<b>faith, trust</b>'),('kānti','<b>beauty, radiance</b>')],
 '<b>Faith.</b> Chapter 4 called her “śraddhā satām”, the faith of the good. Here she is faith in <i>all</i> beings. Kānti is the glow of beauty: in a face, a flower, a sunrise.',
 'Faith and beauty <b>shine with her light</b>.'),
YDP('lakṣmīrūpeṇa saṃsthitā','vṛttirūpeṇa saṃsthitā','FORTUNE AND LIVELIHOOD','TWO',
 'To the Devī who dwells in all beings as Lakṣmī (fortune); as livelihood (activity): salutations to her, again and again.',
 [('lakṣmī','<b>fortune, prosperity</b>'),('vṛtti','<b>livelihood</b>; also activity of the mind')],
 '<b>Prosperity and work.</b> Lakṣmī is the fortune we receive; vṛtti is the work by which we earn it. In yoga, vṛtti also means the movements of the mind. Wealth and work are both sacred here.',
 'Fortune and honest work <b>are both her</b>.'),
YDP('smṛtirūpeṇa saṃsthitā','dayārūpeṇa saṃsthitā','MEMORY AND COMPASSION','TWO',
 'To the Devī who dwells in all beings as memory; as compassion: salutations to her, again and again.',
 [('smṛti','<b>memory</b>; also tradition'),('dayā','<b>compassion, mercy</b>')],
 '<b>Why memory matters here.</b> The gods are on the Himālaya precisely because they <i>remembered</i> her (5.5–6). Memory is the thread that brings her back. Dayā, compassion, is why she answers.',
 'We remember her; <b>she answers with compassion</b>.'),
YDP('tuṣṭirūpeṇa saṃsthitā','mātṛrūpeṇa saṃsthitā','CONTENTMENT AND MOTHER','TWO',
 'To the Devī who dwells in all beings as contentment; as mother: salutations to her, again and again.',
 [('tuṣṭi','<b>contentment</b>'),('mātṛ','<b>mother</b>')],
 '<b>The heart of the list.</b> Many find this the most moving line: in every being she is the <b>Mother</b>. Every mother’s love, in humans and animals, is her. And tuṣṭi, contentment, is the end of craving (tṛṣṇā) named earlier.',
 'In every being, <b>she is the Mother</b>.'),
YDP('bhrāntirūpeṇa saṃsthitā',None,'SHE IS EVEN ERROR',
 sc('A rope on a path in dim light that a traveller mistakes for a snake, the Goddess watching gently',NIGHTSKY+MOON(180,30,12)+'<path d="M40 130 q30 -16 60 0 t60 0" fill="none" stroke="#c9a26b" stroke-width="5"/>'+person(40,110,'#888','#c98b5a',.7)+'<ellipse cx="80" cy="50" rx="40" ry="18" fill="#fff" stroke="#111"/>'+T(80,55,'a snake?!',10)+DEVI(170,40,.4,False)),
 'To the Devī who dwells in all beings as delusion (error): salutations to her, salutations to her, salutations to her, salutations again and again.',
 [('bhrānti','<b>delusion, error</b>, mistaking one thing for another')],
 '<b>The last form is the boldest.</b> Even <i>bhrānti</i>, error, is her: the Mahāmāyā of Part 5 who “drags even the wise into delusion”. Nothing, not even our mistakes, is outside her. That is why only she can free us from them.',
 'Even our errors <b>are held by her</b>.'),
VP(C,'77–80',S('77','78–80'),'CONSCIOUSNESS FILLS ALL',
 sc('The whole world, earth, sky and beings, inside a single golden glow with the Goddess at its heart',GLOW(110,80,76)+'<circle cx="110" cy="80" r="56" fill="#4aa3df" stroke="#111" stroke-width="2"/><path d="M70 70 q20 -10 40 4 t40 -4 M66 98 q30 10 60 0" stroke="#2a9d6f" stroke-width="6" fill="none"/>'+DEVI(110,40,.3,False)),
 'To her who presides over the senses of beings, who is in all beings always, to the all-pervading Devī, salutations again and again. To her who, in the form of consciousness (citi), pervades this whole world and abides in it: salutations to her, salutations to her, salutations to her, salutations again and again.',
 [('indriyāṇām adhiṣṭhātrī','<b>presiding over the senses</b>'),('vyāpti','<b>pervasion</b>'),('citi-rūpeṇa','<b>in the form of pure consciousness</b>'),('kṛtsnam','<b>whole</b>')],
 '<b>The hymn closes the circle.</b> It began with cetanā (awareness) and ends with <i>citi</i> (pure consciousness) filling the whole world. Everything between, intelligence and hunger, faith and error, was that one consciousness in many forms.',
 'One consciousness, <b>filling the whole world</b>.'),
VP(C,'81–82',S('81','82'),'MAY SHE END OUR DANGERS',
 sc('The gods bowing low on the Himalaya, a glow rising from their folded hands toward the Goddess',HIMA+GODS(150,.45,5,40,34)+''.join(f'<path d="M{40+k*34} 120 L110 50" stroke="#ffd60a" stroke-width="1.5" stroke-dasharray="3 3"/>' for k in range(5))+DEVI(110,0,.4,False)),
 'Praised long ago by the gods for the help they sought, and worshipped daily by the lord of gods: may she, the Ruler, the source of all good, bring us good and auspicious things and destroy our dangers. She who is now bowed to by us gods, tormented by arrogant demons; who, remembered by us with bodies bowed in devotion, at that very moment destroys all our dangers.',
 [('abhīṣṭa-saṃśrayāt','<b>for the help they sought</b>'),('śubha-hetuḥ','<b>the source of good</b>'),('uddhata-daitya-tāpita','<b>tormented by arrogant demons</b>'),('tat-kṣaṇam eva','<b>that very moment</b>'),('bhakti-vinamra','<b>bowed in devotion</b>')],
 '<b>Back to the promise.</b> The gods end by naming exactly what they are counting on: “remembered, she destroys all dangers at that very moment.” The boon of chapter 4, word for word.',
 'Remembered with devotion, <b>she ends dangers at once</b>.'),
VP(C,'84–88','evaṁ stavābhiyuktānāṁ devānāṁ tatra pārvatī | / snātumabhyāyayau toye jāhnavyā nṛpanandana || 84|| / sābravīttān surān subhrūrbhavadbhiḥ stūyate’tra kā | / śarīrakośataścāsyāḥ samudbhūtābravīcchivā || 85|| / stotraṁ mamaitatkriyate śumbhadaityanirākṛtaiḥ | / devaiḥ sametaiḥ samare niśumbhena parājitaiḥ || 86|| / śarīrakośādyattasyāḥ pārvatyā niḥsṛtāmbikā | / kauśikīti samasteṣu tato lokeṣu gīyate || 87|| / tasyāṁ vinirgatāyāṁ tu kṛṣṇābhūtsāpi pārvatī | / kāliketi samākhyātā himācalakṛtāśrayā || 88||',
 'KAUŚIKĪ AND KĀLIKĀ',
 sc('Parvati at the river Ganga; a radiant goddess stepping out of her body, and Parvati herself turning dark',HIMA+'<path d="M0 140 q55 -10 110 0 t110 0 V160 H0z" fill="#4aa3df" stroke="#111"/>'+DEVI(70,10,.6,False,'#2a9d6f','#2b2b3a')+GLOW(150,50,40)+DEVI(150,10,.6,False,'#fff','#f2c79b')+T(70,128,'KĀLIKĀ',10)+T(150,128,'KAUŚIKĪ',10)),
 'As the gods praised, Pārvatī came to bathe in the Gaṅgā. “Whom are you praising?” she asked. From the sheath of her body came forth Śivā and said: “This hymn is to me, from the gods driven out by Śumbha and defeated by Niśumbha.” Born from the sheath (kośa) of Pārvatī, she is sung as Kauśikī. Pārvatī herself then became dark, and is known as Kālikā, dwelling on the Himālaya.',
 [('jāhnavī','<b>the Gaṅgā</b>'),('śarīra-kośa','<b>the sheath of the body</b>'),('kauśikī','<b>“from the sheath”</b>'),('kṛṣṇā abhūt','<b>became dark</b>'),('kālikā','<b>the dark one</b>')],
 '<b>A strange, beautiful answer.</b> Pārvatī asks who is being praised; the answer steps out of her own body. The hymn was to her all along. Bright <b>Kauśikī</b> fights this carita; dark Pārvatī becomes <b>Kālikā</b>.',
 'The Goddess they praised <b>steps out of Pārvatī</b>.'),
VP(C,'119–121','kiṁ tvatra yatpratijñātaṁ mithyā tatkriyate katham | / śrūyatāmalpabuddhitvātpratijñā yā kṛtā purā || 119|| / yo māṁ jayati saṅgrāme yo me darpaṁ vyapohati | / yo me pratibalo loke sa me bhartā bhaviṣyati || 120|| / tadāgacchatu śumbho’tra niśumbho vā mahābalaḥ | / māṁ jitvā kiṁ cireṇātra pāṇiṁ gṛhṇātu me laghu || 121||',
 'THE VOW',
 sc('The Goddess smiling calmly on a mountain, speaking to a startled asura messenger; her speech bubble says: whoever conquers me in battle',HIMA+DEVI(150,10,.7,False)+ASURA(50,150,.9,'#3a5a6a')+SPEECH(84,30,'conquer me first!',110,10)),
 'The Devī said: “But I made a vow long ago, out of little understanding; how can I make it false? Hear it: He who conquers me in battle, who removes my pride, who is my equal in strength in the world, he shall be my husband. So let Śumbha come here, or the mighty Niśumbha. Let him conquer me and quickly take my hand. Why delay?”',
 [('pratijñā','<b>a vow</b>'),('alpa-buddhitvāt','<b>out of little understanding</b>: said with irony'),('darpaṃ vyapohati','<b>removes my pride</b>'),('prati-bala','<b>equal in strength</b>'),('pāṇiṃ gṛhṇātu','<b>let him take my hand</b> (marry)')],
 '<b>Hidden smile.</b> The text says she spoke “smiling deeply within” (5.116). Śumbha’s messenger offered her marriage to the lord of the three worlds. Her answer sounds humble and is a challenge: “Beat me first.” No one in the universe can, and she knows it.',
 '“Whoever conquers me in battle”: <b>a challenge dressed as a vow</b>.'),
]
for v in V:
    if v['svg']=='TWO':
        pass
# fill TWO scenes
TWOS={'20–25':('💡','intelligence','😴','sleep'),'26–31':('🍚','hunger','🌳','shade'),'32–37':('⚡','power','💧','thirst'),'38–43':('🤲','patience','👶','birth'),'44–49':('🙈','modesty','🕊️','peace'),'50–55':('🙏','faith','🌸','beauty'),'56–61':('🪷','fortune','🌾','livelihood'),'62–67':('🧠','memory','💗','compassion'),'68–73':('😊','contentment','🤱','mother')}
for v in V:
    if v['svg']=='TWO': v['svg']=TWO(*TWOS[v['n']])
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The gods on the snowy Himalaya with folded hands, and the radiant goddess Kaushiki stepping out of Parvati’s body, Parvati turning dark">'
 '<rect width="380" height="268" fill="#14214a" rx="8"/>'+''.join(f'<text x="{(41*k)%370+5}" y="{(29*k+13)%90+12}" font-size="9" fill="#fff">✦</text>' for k in range(18))
 +'<path d="M0 230 L70 120 L120 180 L190 80 L260 170 L310 110 L380 200 V268 H0z" fill="#dfe9f6" stroke="#111" stroke-width="2"/>'
 +GLOW(240,90,70)+DEVI(240,30,.8,False,'#fff')+DEVI(140,60,.6,False,'#2a9d6f','#2b2b3a')+''.join(GOD(40+k*34,258,.55,*c) for k,c in enumerate([('#ffd60a','#c98b5a'),('#fff','#9fd3f0'),('#ff8c1a','#e0a800'),('#2a9d6f','#c98b5a'),('#9b5de5','#c98b5a')]))+'</svg>')
st1=storypage('tyrants','NEW TYRANTS','Ślokas 5.1–8',
 panels('Three panels: two asura brothers on heaven’s throne; the gods driven out; the gods walking up the Himalaya',[
  ('#ffe3c4','ŚUMBHA & NIŚUMBHA',ASURA(50,150,1.0,'#3a5a6a')+ASURA(100,150,1.0,'#5a2a6a')),
  ('#dfe9f6','DRIVEN OUT',GODS(160,.4,4,20,34)+'<path d="M20 60 h100" stroke="#111" stroke-width="3" stroke-dasharray="6 4"/>'),
  ('#e3f2fd','TO THE HIMĀLAYA',HILLS+GODS(170,.3,3,40,30))]),
 ['<b>The third carita.</b> Its deity is <b>Mahāsarasvatī</b>. Two asura brothers, <b>Śumbha</b> and <b>Niśumbha</b>, proud of their strength, take the three worlds and the gods’ shares of sacrifice.',
  '<b>Everything taken.</b> They seize the offices of the Sun, Moon, Kubera, Yama, Varuṇa, Wind and Fire.',
  '<b>Driven out.</b> The gods, defeated and kingdomless, are cast out.',
  '<b>They remember.</b> “She gave us a boon: remember me in danger, and I will end your dangers at once.”',
  '<b>To the mountain.</b> They go to the Himālaya and praise her as Viṣṇumāyā. The hymn they sing is the most famous in all Goddess worship.'],
 ("New demons? Didn't she just win?","Every age has its own tyrants. That's the point of the three caritas: she came once, twice, and will come again, whenever she is remembered."),
 'New tyrants; <b>the old promise still holds</b>.')
st2=storypage('messenger','THE PROPOSAL','Ślokas 5.89–129',
 panels('Three panels: Chanda and Munda spying on the beautiful goddess; Shumbha on his throne surrounded by stolen treasures; the messenger before the smiling goddess',[
  ('#dfe9f6','CAṆḌA & MUṆḌA SEE HER',HILLS+DEVI(100,20,.45,False,'#fff')+ASURA(30,170,.5)+ASURA(54,170,.5,'#3a2a6a')),
  ('#fff3b0','ALL THE TREASURES','<rect x="30" y="60" width="86" height="80" fill="#ffd60a" stroke="#111"/>'+ASURA(72,130,.7,'#3a5a6a')+ELEPHANT(30,170,.4)+'<circle cx="120" cy="160" r="10" fill="#c0392b" stroke="#111"/>'),
  ('#fde4e4','“MARRY THE KING”',DEVI(100,10,.5,False,'#fff')+ASURA(36,170,.7,'#3a5a6a'))]),
 ['<b>Spies.</b> Śumbha’s servants Caṇḍa and Muṇḍa see Ambikā on the Himālaya in her most lovely form.',
  '<b>The report.</b> “You own every jewel of the three worlds: Indra’s elephant Airāvata, the Pārijāta tree, the horse Uccaiḥśravas, Brahmā’s swan-chariot, Kubera’s treasure, Varuṇa’s umbrella. Why not this jewel among women?”',
  '<b>The messenger.</b> Śumbha sends the asura Sugrīva: “Śumbha rules the three worlds and enjoys all the sacrifices. Marry me or my brother Niśumbha, and all that power is yours.”',
  '<b>The vow.</b> Smiling inwardly, she answers: “Whoever conquers me in battle shall be my husband. Let him come.”',
  '<b>The threat.</b> “Proud woman! Gods could not face them; will you, alone? Go, or be dragged by your hair.” She replies calmly: “Tell your king exactly what I said.”'],
 ("A proposal? In the middle of a war story?","Śumbha thinks everything beautiful should belong to him: elephant, tree, horse, and now the Goddess. Greed treats even the Divine as a jewel to own."),
 'Greed wants to own the Goddess; <b>she offers a fight instead</b>.')
P=dict(n=10,ch=5,out='/home/claude/work/devim/Devi_Mahatmya_Part10.html',
 title='Yā Devī Sarvabhūteṣu · Part 10 · Devī Māhātmya series · srini.presents',
 desc='Devī Māhātmya, Part 10: chapter 5. Oppressed by Śumbha and Niśumbha, the gods go to the Himālaya and sing “yā devī sarvabhūteṣu”, the 21 forms of the Goddess in all beings; Kauśikī steps out of Pārvatī; Śumbha’s proposal and her vow. Explained with illustrations.',
 h1='YĀ DEVĪ SARVABHŪTEṢU',h1size=64,series='DEVĪ MĀHĀTMYA · PART 10 · CHAPTER 5',tag='The Goddess in all beings · explained and illustrated',cover=cover,
 how='The whole <b>“yā devī” hymn</b> (ślokas 9–82) in full for chanting, then a page for each form of the Goddess, and the story of Kauśikī and Śumbha’s proposal in comic panels.',
 where=[f'In {plink(9)}, the gods sang the Śakrādi stuti and received a boon: “whenever we remember you, end our dangers.” The second carita closed.',
  'Chapter 5 opens the <b>third carita</b>, whose deity is <b>Mahāsarasvatī</b>. New tyrants, Śumbha and Niśumbha, rule heaven. The gods climb the Himālaya and sing the hymn chanted in every home: <b>“yā devī sarvabhūteṣu”</b>, the Goddess in every being.',
  'Our separate article on this hymn is <a href="/bhakti/devi/ya-devi-sarvabhuteshu/">Yā Devī Sarvabhūteṣu</a>; this part reads it inside its story.'],
 wtalk=("Twenty-one forms! Which one is the real Goddess?","All of them, and the awareness behind them. The hymn starts with consciousness, ends with consciousness, and finds her in everything between, even hunger and error."),
 fulls=[('THE HYMN IN ONE GO','Chapter 5, ślokas 9–37',FV[:13]),('IN ONE GO · CONTINUED','Ślokas 38–82',FV[13:])],
 fulltoc='The Hymn in One Go',
 fullnote='Text as given in the Devīmāhātmyam edition of devimahatmyam.aurobharati.in (129 ślokas in chapter 5), where each “yā devī” form counts as three ślokas (the triple namas tasyai); its numbering is followed.',
 seq=[st1]+V[:17]+[V[17],st2,V[18]],
 toc=[('THE STORY',[('tyrants','New Tyrants'),V[0]]),('THE HYMN',V[1:17]),('THE STORY CONTINUES',[V[17],('messenger','The Proposal'),V[18]])],
 end=['<b>New tyrants (5.1–7).</b> Śumbha and Niśumbha take the three worlds; the gods remember her boon and go to the Himālaya.',
  '<b>The prelude (5.9–13).</b> Salutations to the Devī: fierce and moonlike, Durgā who carries across, most gentle and most fierce.',
  '<b>The 21 forms (5.14–76).</b> In all beings she is Viṣṇumāyā, consciousness, intelligence, sleep, hunger… mother, and even error.',
  '<b>The close (5.77–82).</b> She is pure consciousness filling the world; remembered, she ends dangers at once.',
  '<b>Kauśikī (5.84–129).</b> She steps out of Pārvatī, who becomes Kālikā. Śumbha proposes marriage; she replies with her vow: “Conquer me first.”'],
 endsub='Chapter 5 in five lines',
 next=("What's next?",'Part 11: chapter 6. Śumbha, furious, sends Dhūmralocana with sixty thousand asuras to drag her by the hair. One sound from her, “huṃ”, is enough.'),
 endkey='<b>she is in every being, as every being</b>.',
 foot='Study notes on the Devī Māhātmya, chapter 5 (Mārkaṇḍeya Purāṇa). The hymn (ślokas 9–82) is given in full and other ślokas as in the Devīmāhātmyam edition of devimahatmyam.aurobharati.in, whose numbering is followed; editions differ in the number and order of the “yā devī” forms. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.')
build(P)
