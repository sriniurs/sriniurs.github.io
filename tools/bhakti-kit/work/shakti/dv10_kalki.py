exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Kalki · Daśāvatāra 10 · srini.presents','Kalki, the tenth avatāra of Viṣṇu, still to come: the signs of the Kali Yuga, the rider on the white horse with a blazing sword, Viṣṇuyaśas and the village of Śambhala, Paraśurāma as his teacher, the dawn of a new Satya Yuga, the Mahābhārata, Bhāgavata, Viṣṇu Purāṇa and Kalki Purāṇa, the yuga clock, the Buddhist Kālacakra kings of Shambhala, and Kalki temples at Jaipur and Sambhal. An illustrated reference guide.')
def RIDER(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-60 0 q-6 -36 34 -38 q30 0 44 -20 l10 10 l-6 8 q4 26 -24 40z" fill="#f4f4f4"/><path d="M-50 0 v30 M-24 2 v28 M4 0 v30 M16 -2 v28" stroke="#f4f4f4" stroke-width="7"/><path d="M-50 0 v30 M-24 2 v28 M4 0 v30 M16 -2 v28" stroke="#111" stroke-width="1"/>'
 '<path d="M28 -50 q10 -10 4 -20" fill="none" stroke="#bbb" stroke-width="4"/><path d="M-66 -30 q-20 10 -26 30" fill="none" stroke="#ddd" stroke-width="6"/>'
 '<path d="M-26 -36 q-2 -30 14 -36 q16 6 14 36z" fill="#3b6fd0"/><circle cx="-12" cy="-80" r="10" fill="#3b6fd0"/><path d="M-22 -88 h20 l-3 -10 h-14z" fill="#e0a800"/><path d="M0 -60 l50 -50" stroke="#e8e8e8" stroke-width="5"/><path d="M0 -60 l50 -50" stroke="#ffd60a" stroke-width="1.5"/></g>')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A rider on a white horse raising a blazing sword against a dark stormy sky, with a dawn breaking on the horizon">'
 '<rect width="380" height="268" fill="#1d1d2a" rx="8"/><rect y="200" width="380" height="68" fill="#e07a4a"/><circle cx="300" cy="210" r="30" fill="#ffd60a"/><rect y="226" width="380" height="42" fill="#3a2a2a"/>'+''.join(f'<path d="M{30+i*70} 20 l-8 26 l10 0 l-8 22" stroke="#ffd60a" stroke-width="2.5" fill="none"/>' for i in range(5))+RIDER(190,212,1.35)+'</svg>')
cov=cover_dv('DAŚĀVATĀRA 10 OF 10','KALKI',18,'The rider on the white horse',art)
fw=foreword_dv('Keśava dhṛta-kalki-śarīra,',[
 'The last avatāra has not yet come. When the dark age, the <b>Kali Yuga</b>, reaches its lowest point, the Purāṇas say, Viṣṇu will be born as <b>Kalki</b> in the village of <b>Śambhala</b>, to a Brahmin named Viṣṇuyaśas. He will ride a white horse and carry a blazing sword, end the rule of the wicked, and open the door to a new golden age.',
 'His story is told in the Mahābhārata, the Viṣṇu and Bhāgavata Purāṇas, and in a whole later text, the <b>Kalki Purāṇa</b>, where Paraśurāma is his teacher. Buddhist texts too speak of Kalki kings of a hidden land called Shambhala.',
 'This guide explains what the texts say, how the yuga clock works, and why the series ends not with a full stop but with hope.'],
 'When will he come?','By the traditional count, the Kali Yuga has hundreds of thousands of years left. No one can give a date.',
 series_note_dv(10))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Avatāra','<b>Tenth</b> and last; at the end of the Kali Yuga; still to come'),('Form','A warrior on a <b>white horse</b> (Devadatta) with a blazing sword'),
 ('Birth','In the village of Śambhala, to Viṣṇuyaśas and Sumati'),('Deed','Ends the age of darkness and begins a new Satya Yuga'),
 ('Texts','Mahābhārata, Vana Parva; Viṣṇu Purāṇa 4.24; Bhāgavata Purāṇa 1.3 and 12.2; Kalki Purāṇa'),('Teacher','Paraśurāma, the immortal sixth avatāra'),
 ('Temples','Kalki temple, Jaipur; Kalki Dhām, Sambhal (UP)'),('Day','Kalki Jayantī, Śrāvaṇa Śukla Ṣaṣṭhī')])
 +talk("An avatāra in the future tense?","The only one. The series ends with a promise.")))
pages.append(page('names','NAMES','The destroyer of filth',facts([
 ('Kalki · Kalkin','Often explained as “destroyer of filth (kalka)”, or linked with “time” (kāla)'),('Viṣṇuyaśas','His father’s name; in the Mahābhārata, the name of Kalki himself'),('Śambhala','His birthplace'),('Devadatta','His white horse'),('Ratnamaru','His sword, in the Kalki Purāṇa'),('Padmā','His bride, an avatāra of Lakṣmī, in the Kalki Purāṇa')])))
pages.append(page('kaliyuga','THE DARK AGE','Signs of the Kali Yuga',fig(560,170,'A dim, smoky city with crooked buildings and grey figures',
 '<rect width="560" height="170" fill="#3a3a44"/>'+''.join(f'<rect x="{20+i*60}" y="{60+(i%3)*20}" width="40" height="{110-(i%3)*20}" fill="#5a5a66" stroke="#111" transform="rotate({(i%2)*4-2} {40+i*60} 170)"/>' for i in range(9))+''.join(f'<circle cx="{40+i*70}" cy="40" r="{20+(i%2)*6}" fill="#6a6a74" opacity=".7"/>' for i in range(8)))+facts([
 ('Dharma','Dharma stands on one leg out of four'),
 ('Rulers','Kings plunder rather than protect'),
 ('Wealth','Money becomes the measure of worth, birth and virtue'),
 ('Life','Lifespans shrink; truth and kindness become rare'),
 ('Faith','Religion becomes show; scriptures are sold'),
 ('Text','Lists of these signs fill Bhāgavata 12.2 and the Mahābhārata’s Vana Parva')])
 +talk("Sounds a bit like the news?","Every generation has thought so. That's why the texts still feel alive.")))
pages.append(page('clock','THE YUGA CLOCK','How long is an age?',fig(560,150,'Four bars of decreasing length for the four ages',
 '<rect width="560" height="150" fill="#eef3fa"/>'+''.join(f'<rect x="30" y="{14+i*32}" width="{w}" height="24" fill="{c}" stroke="#111" stroke-width="2"/>'+T(40+w+10,30+i*32,f'{n}: {y}',12).replace('text-anchor="middle"','text-anchor="start"') for i,(n,y,w,c) in enumerate((('Satya','1,728,000 yrs',400,'#fff3c0'),('Tretā','1,296,000 yrs',300,'#dff0d8'),('Dvāpara','864,000 yrs',200,'#dcecff'),('Kali','432,000 yrs',100,'#e8e0f0')))))+facts([
 ('Four ages','Satya, Tretā, Dvāpara and Kali, in the ratio 4:3:2:1'),
 ('Kali','432,000 years by the Purāṇic count'),
 ('Start','Traditionally 3102 BCE, when Kṛṣṇa left the world; about 5,100 years have passed'),
 ('Mahāyuga','The four together, 4.32 million years, then the cycle repeats'),
 ('Other views','Some modern teachers propose much shorter cycles; the Purāṇic numbers are given here')])))
pages.append(page('birth','BORN IN ŚAMBHALA','The coming',fig(560,170,'A village under a starry sky with a light descending on one house',
 '<rect width="560" height="170" fill="#0b1030"/>'+STAR+''.join(TEMPLE(80+i*100,160,1.2,'#d8c49a') for i in range(5))+'<path d="M280 0 L240 140 L320 140Z" fill="#ffd60a" opacity=".35"/>')+facts([
 ('Bhāgavata 12.2.18','He will be born in the house of the noble Brahmin Viṣṇuyaśas, in the village of Śambhala'),
 ('Mahābhārata','Mārkaṇḍeya tells the Pāṇḍavas that a Brahmin named Kalki Viṣṇuyaśas will arise, and weapons and a horse will come to him by thought alone'),
 ('Viṣṇu Purāṇa','A part of Vāsudeva will be born in Śambhala as Kalki, endowed with the eight powers'),
 ('Kalki Purāṇa','His mother is Sumati; his brothers Kavi, Prājña and Sumantra')])))
pages.append(page('training','THE TEACHER AND THE HORSE','Kalki Purāṇa',fig(560,170,'A sage with an axe teaching a young man, a white horse waiting',
 '<rect width="560" height="170" fill="#fff4dc"/>'+AV(6,170,110,1.4)+person(300,150,'#3b6fd0','#5b8fe0',1)+'<g transform="translate(440 140)" stroke="#111" stroke-width="2"><path d="M-40 0 q-4 -30 26 -30 q24 0 30 -16 l8 8 l-4 6 q2 22 -18 32z" fill="#f4f4f4"/><path d="M-34 0 v24 M-10 0 v24 M14 0 v24" stroke="#f4f4f4" stroke-width="6"/></g>')+facts([
 ('Paraśurāma','The immortal sixth avatāra teaches Kalki the Vedas and the arts of war on Mount Mahendra'),
 ('Śiva','Gives him the horse Devadatta, a parrot that knows all things, and a sword'),
 ('Padmā','He marries Padmāvatī of Siṃhala, an avatāra of Lakṣmī'),
 ('Two avatāras meet','The sixth teaches the tenth')])
 +'<div class="key">See: <a href="'+DVS+'parashurama/">Paraśurāma</a></div>'))
pages.append(page('battle','THE END OF THE DARK AGE','Sword and white horse',fig(560,190,'A rider on a white horse with a blazing sword charging across a dark plain',
 '<rect width="560" height="190" fill="#2a2a3a"/><rect y="160" width="560" height="30" fill="#3a2a2a"/>'+RIDER(300,170,1.2))+facts([
 ('The ride','On his white horse, sword blazing like a comet, he sweeps across the earth'),
 ('The wicked','He ends the rule of the cruel and false, and the demon Kali himself'),
 ('Jayadeva','Praises him wielding a sword “like a comet” to destroy the wicked'),
 ('Our note','Older texts use words for foreign or impure rulers that reflect their times; we follow the general sense, the end of tyranny')])))
pages.append(page('satya','THE NEW GOLDEN AGE','Satya Yuga returns',facts([
 ('Renewal','After Kalki, people’s minds become pure as crystal, says the Bhāgavata'),
 ('Dharma','Dharma stands again on all four legs'),
 ('Cycle','The wheel of ages turns: Satya, Tretā, Dvāpara, Kali, and Satya again'),
 ('Back to Matsya','The cycle that began with a fish in Manu’s hands turns back to its start')])
 +talk("So it all starts again?","That's the Hindu idea of time: a wheel, not a line. Every ending is a beginning.")))
pages.append(page('texts','WHERE THE STORY COMES FROM','Older and later texts',facts([
 ('Mahābhārata','Vana Parva 188–191: the earliest full account, told by Mārkaṇḍeya'),
 ('Viṣṇu Purāṇa','4.24: Kalki’s coming at the end of the Kali Yuga'),
 ('Bhāgavata','1.3.25 lists him; 12.2 tells the signs of Kali and his coming'),
 ('Kalki Purāṇa','A later Upapurāṇa, a whole book of his life and battles; scholars date it to the last few centuries'),
 ('Development','Scholars see the Kalki idea growing over many centuries, partly in response to invasions and hard times')])))
pages.append(page('shambhala','SHAMBHALA','Hindu and Buddhist',facts([
 ('Where?','Some identify Śambhala with Sambhal in Uttar Pradesh; others see it as a hidden or symbolic land'),
 ('Kālacakra','The Buddhist Kālacakra Tantra (11th c.) tells of the kings of Shambhala called Kalkis; the 25th, Raudra Cakrin, will defeat the forces of darkness'),
 ('Shared idea','A hidden kingdom, a future righteous king, a final battle: Hindu and Buddhist forms grew side by side'),
 ('Modern','Shambhala became a byword in the West for a hidden paradise')])))
pages.append(page('temples','KALKI TEMPLES','Waiting for him',fig(560,150,'A small temple with a white horse statue standing outside',
 '<rect width="560" height="150" fill="#eef3fa"/>'+TEMPLE(220,140,2.4)+'<g transform="translate(380 130)" stroke="#111" stroke-width="2"><rect x="-30" y="0" width="60" height="10" fill="#c9a26b"/><path d="M-26 0 q-4 -24 20 -24 q18 0 24 -12 l6 6 l-4 4 q2 18 -14 26z" fill="#f4f4f4"/></g>')+facts([
 ('Jaipur','A Kalki temple in Jaipur, built under Sawai Jai Singh II in the 18th century; a white horse stands before it, said to have a hoof wound that will heal when Kalki comes'),
 ('Sambhal','The Śrī Kalki Dhām project in Sambhal, Uttar Pradesh, had its foundation stone laid in 2024'),
 ('In art','Kalki closes every Daśāvatāra panel, as at Tṛkkākara during Onam'),
 ('Our note','Kalki is mostly worshipped as part of the ten rather than in his own temples')])))
pages.append(page('claims','CLAIMS AND CAUTION','Many have said “I am Kalki”',facts([
 ('Claimants','Over the centuries many people have claimed to be Kalki'),
 ('Tradition','The texts describe a world-changing figure at the end of a 432,000-year age; no claimant has matched it'),
 ('Wisdom','Teachers warn against those who use the name to gather followers or money'),
 ('Inner reading','Some read Kalki as the inner power that cuts through ignorance, in any age')])
 +talk("What if someone says they're Kalki?","Be polite and keep your wallet. The texts describe someone the whole world couldn't miss.")))
pages.append(page('festivals','THROUGH THE YEAR','His day',facts([
 ('Kalki Jayantī','Śrāvaṇa Śukla Ṣaṣṭhī (Jul–Aug), by common calendars'),('Daśāvatāra festivals','He closes the procession of the ten'),('Onam','The last of the avatāra decorations at Tṛkkākara')])))
pages.append(page('meaning','WHAT KALKI TEACHES','The wisdom of hope',facts([
 ('Hope','No darkness lasts forever'),('Justice','Tyranny has an end'),('Time is a wheel','Every ending opens a beginning'),('Inner Kalki','Cut through your own ignorance now; no need to wait')])
 +talk("What should I take from Kalki?","Don't wait for a rider. Be a little light in your own dark age.")))
pages.append(page('ten','THE TEN TOGETHER','The whole series',
 '<div class="steps">'+''.join(f'<div><b>{n}. <a href="{DVS}{s}/">{nm}</a></b>: {d}.</div>' for n,nm,s,f,y,d in DV)+'</div>'
 +talk("Fish to horseman: done?","All ten. Yuge yuge: he comes again and again.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Kali Yuga','The dark age'),('Mahāyuga','The four ages together'),('Śambhala','Kalki’s birthplace'),('Devadatta','His horse'),('Upapurāṇa','A secondary Purāṇa'),('Kālacakra','“Wheel of time”: a Buddhist Tantra'),('Satya Yuga','The age of truth'),('Mārkaṇḍeya','The long-lived sage who tells of Kalki')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Kalki, tenth avatāra, still to come.</div>
<div><b>When.</b> At the end of the Kali Yuga, the dark age.</div>
<div><b>Story.</b> Born in Śambhala; taught by Paraśurāma; the white horse and blazing sword.</div>
<div><b>After.</b> A new Satya Yuga; the wheel turns again.</div>
<div><b>Lesson.</b> Hope, justice, and the inner sword that cuts ignorance.</div>
</div>'''+talk("One line to end the series?","The ten avatāras say one thing: whenever the world falls, he comes.")+'<div class="key">The Daśāvatāra is complete: <a href="'+DVS+'">back to the series</a> 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Mahābhārata, Vana Parva 188–191 (Mārkaṇḍeya on the Kali Yuga and Kalki Viṣṇuyaśas); Viṣṇu Purāṇa 4.24; Bhāgavata Purāṇa 1.3.25 and 12.2.18–20 (Śambhala, Viṣṇuyaśas, Devadatta); Kalki Purāṇa (Paraśurāma, Padmā, Śiva’s gifts); Jayadeva, Gītagovinda 1.</p>
<p><b>Buddhist:</b> Kālacakra Tantra tradition of the Kalki kings of Shambhala.</p>
<p><b>Temples:</b> Kalki temple, Jaipur (Sawai Jai Singh II); Śrī Kalki Dhām, Sambhal, foundation stone 2024 (news reports).</p>
<p><b>Sources differ / unverified:</b> the meaning of “Kalki”; the date of the Kalki Purāṇa; the location of Śambhala; the yuga lengths (Purāṇic count used); the Jaipur horse legend; Kalki Jayantī date. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('kaliyuga','The Dark Age'),('clock','The Yuga Clock'),('birth','Born in Śambhala'),('training','The Teacher and the Horse'),('battle','The End of the Dark Age'),('satya','The New Golden Age'),
 ('texts','Where the Story Comes From'),('shambhala','Shambhala'),('temples','Kalki Temples'),('claims','Claims and Caution'),('festivals','Through the Year'),('meaning','What Kalki Teaches'),('ten','The Ten Together'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV10_Kalki.html',head,cov,fw,pages,toc)
