exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Bagalāmukhī · Daśa Mahāvidyā 8 · srini.presents',
 'Bagalāmukhī or Pītāmbarā, the eighth of the Daśa Mahāvidyā: the yellow Goddess who stills the storm and seizes the demon Madan by the tongue, crane or bridle, the power of stambhana, the Haridrā Sarovara, and her three great temples at Datiā, Nalkheḍā and Bankhaṇḍī, with shrines from Nepal to Tamil Nadu and Karnataka. An illustrated reference guide.')
def BAGALA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-30 50 q-4 -54 30 -66 q34 12 30 66z" fill="#ffd60a"/>'
 '<path d="M-22 -8 l-30 6 M22 -8 l24 -26" stroke="#f2d040" stroke-width="7"/>'
 '<path d="M44 -32 l14 -32" stroke="#7a5a2a" stroke-width="7"/><circle cx="60" cy="-68" r="9" fill="#e0a800"/>'
 '<circle cy="-36" r="15" fill="#f2d040"/><path d="M-14 -48 h28 l-4 -16 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/><path d="M-5 -68 a8 8 0 1 0 11 3" fill="none" stroke="#fff" stroke-width="2.5"/>'
 '<circle cx="-5" cy="-38" r="2.4" fill="#111"/><circle cx="5" cy="-38" r="2.4" fill="#111"/><path d="M-3 -46 h6" stroke="#c0392b" stroke-width="2"/><path d="M-6 -29 q6 3 12 0" fill="none"/></g>')
def DEMON_D(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-20 40 q-2 -40 20 -48 q22 8 20 48z" fill="#3a6a3a"/><circle cy="-18" r="13" fill="#4a8a4a"/>'
 '<path d="M-10 -30 l-4 -10 M10 -30 l4 -10" stroke-width="3"/><circle cx="-4" cy="-20" r="2" fill="#fff"/><circle cx="4" cy="-20" r="2" fill="#fff"/><path d="M0 -12 q10 0 24 2" stroke="#e04040" stroke-width="4"/></g>')
def SCENE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+DEMON_D(-82,22,.9)+BAGALA(0,0,1)+'<path d="M-58 8 l-2 0" stroke="#e04040" stroke-width="4"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The yellow goddess Bagalamukhi raising a club and holding a green demon by the tongue, above a golden lake">'
 '<rect width="380" height="268" fill="#4a3a0a" rx="8"/><ellipse cx="190" cy="236" rx="170" ry="24" fill="#e0a800" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{40+i*44} 236 q10 -6 20 0" stroke="#fff3a0" stroke-width="2" fill="none"/>' for i in range(7))+SCENE(210,150,1.3)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Bagalāmukhī</b>: “crane-faced”, or “she whose face is the bridle”'),
 ('Also','<b>Pītāmbarā</b>, “she who wears yellow”'),
 ('Place','<b>Eighth</b> of the ten Mahāvidyās'),
 ('Power','<b>Stambhana</b>: stilling, stopping, paralysing; above all, stopping speech'),
 ('Look','Golden-yellow; yellow clothes, flowers and ornaments; club raised in one hand, a demon’s tongue in the other'),
 ('Birth','From the <b>Haridrā Sarovara</b>, the lake of turmeric, to calm a cosmic storm'),
 ('Temples','<b>Datiā</b> and <b>Nalkheḍā</b> (Madhya Pradesh), <b>Bankhaṇḍī</b> (Himachal)'),
 ('Sought for','Victory in disputes and protection from enemies')])
 +talk("A Goddess who grabs a tongue?","The tongue that lies and curses. She stops it mid-sentence.")))
pages.append(page('names','HER NAMES','Crane or bridle?',facts([
 ('Crane (baka)','Kinsley translates her name “she who has the face of a crane”; the crane stands utterly still before it strikes'),
 ('But…','Kinsley also notes she is rarely shown with a crane’s head'),
 ('Bridle (valgā)','Others say “bagalā” is a worn-down form of <i>valgā</i>, the bit in a horse’s mouth: she controls'),
 ('A Kāśī priest','Told Kinsley her true name is Valgāmukhī, for her power to control'),
 ('Pītāmbarā · Pītāmbarī','“Yellow-robed”: her name across North India'),
 ('Kalyāṇī','“The auspicious”: another reading of her name')])
 +talk("Which one is right?","Both are told. A crane's stillness and a horse's bit both mean control.")))
pages.append(page('form','HER FORM','The golden Goddess',fig(560,200,'A yellow goddess on a golden throne raising a club and holding a green demon by the tongue',
 '<rect width="560" height="200" fill="#fff8d0"/><rect x="200" y="70" width="160" height="120" rx="10" fill="#f2d040" stroke="#111" stroke-width="2"/>'+SCENE(300,120,1.2))+facts([
 ('Colour','Golden-yellow, with yellow clothes, garland and ornaments'),
 ('Hands','Left: the demon’s tongue; right: a raised club'),
 ('Four-armed','Some descriptions give her four arms and a third eye'),
 ('Seat','A golden throne; some images show a corpse beneath her'),
 ('Consort','Śiva as Nārada Bhairava')])))
pages.append(page('storm','THE STORM AND THE TURMERIC LAKE','Why she was born',fig(560,170,'A storm with dark clouds over the world, and a yellow goddess rising from a golden lake',
 '<rect width="560" height="170" fill="#4a5a7a"/>'+''.join(f'<ellipse cx="{60+i*110}" cy="{36+(i%2)*14}" rx="60" ry="22" fill="#2a2a3a" stroke="#111"/>' for i in range(5))
 +'<path d="M120 60 l-14 30 l12 0 l-10 26" stroke="#ffd60a" stroke-width="4" fill="none"/><path d="M460 60 l-14 30 l12 0 l-10 26" stroke="#ffd60a" stroke-width="4" fill="none"/>'
 +'<ellipse cx="280" cy="156" rx="150" ry="16" fill="#e0a800" stroke="#111" stroke-width="2"/>'+BAGALA(280,110,.7))+'''<div class="steps">
<div><b>The storm.</b> In the Satya Yuga a great storm began to destroy creation.</div>
<div><b>The austerity.</b> Viṣṇu, troubled, performed tapas on the shore of the <b>Haridrā Sarovara</b>, the lake of turmeric, in Saurāṣṭra.</div>
<div><b>The Goddess.</b> Pleased, the Goddess brought forth Bagalāmukhī from the lake. She stilled the storm and order returned.</div>
</div>'''+talk("Why turmeric?","Yellow is her colour. Turmeric, gold, the yellow robe: all of it points to her.")))
pages.append(page('madan','THE DEMON MADAN','Seizing the tongue',fig(560,170,'A yellow goddess grasping the tongue of a green demon, raising her club',
 '<rect width="560" height="170" fill="#fde8c0"/>'+SCENE(300,100,1))+facts([
 ('The boon','Madan won <b>vāk-siddhi</b> by austerity: whatever he said came true'),
 ('The misuse','He used it to harm and kill people'),
 ('The gods','Enraged, they turned to Bagalāmukhī'),
 ('The tongue','She caught his tongue and stilled his speech'),
 ('His wish','Before she slew him, he asked to be worshipped with her; she granted it. That is the figure at her feet')])
 +talk("He got worshipped after all that?","Even a demon who meets her is changed. His wish was to stay near her.")))
pages.append(page('swallow','A THIRD STORY','Shared with Dhūmāvatī',facts([
 ('Hunger','Kinsley records a myth in which the hungry Goddess swallows Śiva'),
 ('Two Goddesses','The same story is told of Dhūmāvatī; in this telling both Dhūmāvatī and Bagalāmukhī arise from it'),
 ('The crane','Like a crane swallowing its prey whole, she swallowed her husband: one reading of “crane-faced”'),
 ('Neighbours','At Datiā the two Goddesses share a temple complex')])
 +'<div class="key">Previous: <a href="'+MVS+'dhumavati/">Dhūmāvatī</a></div>'))
pages.append(page('stambhana','THE POWER TO STILL','Stambhana',facts([
 ('Stambhana','“Making rigid”: stopping motion, speech, thought'),
 ('Outward','Devotees pray to her for victory in lawsuits, debates and disputes'),
 ('Inward','Teachers say the real enemy is our own tongue and restless mind; she stills them'),
 ('Speech','She silences false speech and gives the power of true speech'),
 ('Eighth wisdom','After Dhūmāvatī’s emptiness, Bagalāmukhī’s stillness')])
 +talk("So she helps you win court cases?","Many believe so. The sages add: first win against your own tongue.")))
pages.append(page('yellow','ALL IN YELLOW','Her colour',facts([
 ('Dress','Yellow robes, yellow flowers, gold ornaments'),
 ('Offerings','Yellow sweets, turmeric, yellow flowers'),
 ('Worshippers','Devotees often wear yellow when they come to her'),
 ('Pītāmbara','Viṣṇu too is “yellow-robed”; her storm story begins with his tapas'),
 ('Haridrā','Turmeric: the lake she rose from')])))
pages.append(page('datia','PĪTĀMBARĀ PĪṬHA, DATIĀ','Her most famous temple',fig(560,160,'A yellow temple on a low hill beside a pond',
 '<rect width="560" height="160" fill="#fff8d8"/><path d="M0 160 q280 -80 560 0z" fill="#d8c8a8" stroke="#111"/>'
 +'<g transform="translate(240 100)" stroke="#111" stroke-width="2"><rect x="-70" y="-34" width="140" height="34" fill="#ffd60a"/><path d="M-46 -34 l46 -46 l46 46z" fill="#e0a800"/></g><ellipse cx="420" cy="130" rx="70" ry="12" fill="#e0a800" stroke="#111" stroke-width="2"/>')+facts([
 ('Where','Datiā, Madhya Pradesh, at the entrance to the town'),
 ('Founded','By a Swāmījī who settled here in the 1920s; the Bagalāmukhī shrine is dated to 1935 by some sources'),
 ('Haridrā Sarovara','A pond in front of the temple recalls the turmeric lake'),
 ('Dhūmāvatī','He also founded her temple in the same āśrama'),
 ('No money','The temple of Pītāmbarā does not accept money offerings'),
 ('Also','A Sanskrit library, and the Vanakhaṇḍeśvara Śiva temple')])))
pages.append(page('nalkheda','NALKHEḌĀ','The riverbank temple of Mālwā',facts([
 ('Where','Nalkheḍā, Āgar Mālwā district, Madhya Pradesh, on the <b>Lakhundar</b>, a tributary of the Narmadā'),
 ('Legend','Said to have been founded by Yudhiṣṭhira on Kṛṣṇa’s advice, to win the Mahābhārata war'),
 ('Image','A self-manifested image with three faces, called Triśakti Mātā'),
 ('Ground','Built on a cremation ground, as befits a Tantric seat'),
 ('History','Restored in 1815'),
 ('Days','Navarātri and Bagalāmukhī Jayantī; Tuesdays and Fridays')])
 +talk("Three old temples?","Datiā, Nalkheḍā and Bankhaṇḍī are the three most often named.")))
pages.append(page('bankhandi','BANKHAṆḌĪ AND BEYOND','Himachal, Nepal, the South',facts([
 ('Bankhaṇḍī','Kangra district, Himachal Pradesh, near Dehra; crowded on Fridays and at Navarātri'),
 ('Rāma','Local legend says the Goddess gave Rāma the brahmāstra here'),
 ('Koṭlā Fort','Another Kangra shrine, at the fort gate'),
 ('Kāmākhyā and Nepal','Shrines at Guwahati and at Lalitpur (Patan)'),
 ('Tamil Nadu','Kallidaikurichi, Tirunelveli district'),
 ('Karnataka','A lesser-known temple at Somalāpura, Sindhanūr taluk, Rāichūr district')])))
pages.append(page('festivals','THROUGH THE YEAR','Her days',facts([
 ('Bagalāmukhī Jayantī','Vaiśākha Śukla Aṣṭamī (April–May)'),
 ('Navarātri','The great days at all three temples'),
 ('Gupta Navarātri','Kept by Tantric worshippers'),
 ('Weekdays','Saturdays at Datiā; Tuesdays and Fridays at Nalkheḍā; Fridays at Bankhaṇḍī')])))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of stillness',facts([
 ('Hold your tongue','Speech can kill, as Madan’s did; restraint is power'),
 ('Be still','The crane waits motionless; the mind must too'),
 ('Stop the storm','Inside or outside, chaos can be stilled'),
 ('Truth wins','False words are seized; true words prevail')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Baka','Crane'),('Valgā','Bridle, bit'),('Pīta','Yellow'),('Haridrā','Turmeric'),('Stambhana','Stilling, paralysing'),('Vāk-siddhi','Power that makes words come true'),('Brahmāstra','Divine weapon'),('Siddha pīṭha','Seat of spiritual power')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Bagalāmukhī, Pītāmbarā, eighth Mahāvidyā: the Goddess of stillness.</div>
<div><b>Form.</b> Golden-yellow, club raised, a demon’s tongue in her grip.</div>
<div><b>Stories.</b> She rose from the turmeric lake to still the storm; she silenced Madan.</div>
<div><b>Temples.</b> Datiā, Nalkheḍā, Bankhaṇḍī; shrines from Nepal to Karnataka.</div>
<div><b>Lesson.</b> Still the tongue, still the mind.</div>
</div>'''+talk("One line to remember?","Power is not always in speaking. Sometimes it is in stopping.")+'<div class="key">The eighth Great Wisdom: <b>Bagalāmukhī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Goddess:</b> D. Kinsley, <i>Tantric Visions of the Divine Feminine</i> (1997), ch. on Bagalāmukhī (crane meaning; rarely shown with crane; Madan and vāk-siddhi; the swallowing myth; Valgāmukhī from a Kāśī priest). Wikipedia, “Bagalamukhi” (storm and Haridrā Sarovara; Madan’s boon of being worshipped; yellow; Pītāmbarā; Kalyāṇī; iconography; temple list incl. Guwahati, Lalitpur, Kotla, Kallidaikurichi, Somalāpura). Drik Panchang (valgā; Jayantī date).</p>
<p><b>Temples:</b> Wikipedia, “Pitambara Peeth” and “Datia”; Incredible India (Datiā). Wikipedia, “Bagalamukhi Temple, Nalkheda” (Lakhundar; one of three; restored 1815); MP Utsav portal (Nalkheḍā). Wikipedia, “Bagalamukhi Temple, Bankhandi”; Kangra district site.</p>
<p><b>Sources differ / unverified:</b> crane vs bridle; the Yudhiṣṭhira founding of Nalkheḍā and the Rāma–brahmāstra story at Bankhaṇḍī are legends; Datiā founding date given as 1920s or 1935; the Somalāpura temple is lesser known and not independently checked. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('form','Her Form'),('storm','The Storm and the Turmeric Lake'),('madan','The Demon Madan'),('swallow','A Third Story'),('stambhana','The Power to Still'),
 ('yellow','All in Yellow'),('datia','Pītāmbarā Pīṭha, Datiā'),('nalkheda','Nalkheḍā'),('bankhandi','Bankhaṇḍī and Beyond'),('festivals','Through the Year'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 8 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(20px,6.4vw,64px)">BAGALĀMUKHĪ</h1>
  <div class="series">DAŚA MAHĀVIDYĀ · A REFERENCE GUIDE</div>
  <div class="tag">The yellow Goddess who stills</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>The eighth Great Wisdom is dressed in gold. <b>Bagalāmukhī</b>, Pītāmbarā, “the yellow-robed”, rose from a lake of turmeric to still a storm that was tearing the world apart. In her best-known image she holds a demon by the tongue, club raised, stopping his deadly words mid-sentence.</p>
    <p>Her power is <i>stambhana</i>, stillness. Across North India people seek her for victory in disputes; teachers say the first tongue she stills is our own. Her great temples stand at Datiā, Nalkheḍā and Bankhaṇḍī.</p>
    <p>This guide tells her stories, her meaning and her temples.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Pītāmbarā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why is everything yellow?","She is Pītāmbarā. Yellow clothes, yellow flowers, even a yellow lake.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms. Previous: <a href="{MVS}dhumavati/">Dhūmāvatī</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV08_Bagalamukhi.html','w').write(head+b+tail())
print('ok',len(pages))
