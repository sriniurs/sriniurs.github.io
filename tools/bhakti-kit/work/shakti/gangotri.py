exec(open('/home/claude/work/shakti/common_s.py').read())
src=open('/home/claude/work/shakti/chardham.py').read()
exec('def uk('+src.split('def uk(')[1].split('\ncover=(')[0])
head=head_red('Gaṅgotrī · Where Gaṅgā Came Down · srini.presents',
 'Gaṅgotrī, the Himalayan shrine of the goddess Gaṅgā: King Bhagīratha’s penance, Śiva catching the river in his hair, Jahnu and the name Jāhnavī, the Bhagīratha Śilā and the submerged liṅga, Gaumukha and the glacier, Amar Singh Thapa’s temple, Mukhbā in winter, and Gaṅgā Daśaharā. An illustrated reference guide.')
def GANGA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 60 q-4 -60 30 -70 q34 10 30 70z" fill="#fff"/>'
 '<circle cy="-24" r="16" fill="#f2c79b"/><path d="M-16 -30 q16 -24 32 0" fill="#111"/><circle cx="-5" cy="-24" r="2" fill="#111"/><circle cx="5" cy="-24" r="2" fill="#111"/><path d="M-5 -16 q5 3 10 0" fill="none"/>'
 '<path d="M-12 -40 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800"/><path d="M-26 0 l-20 -16 M26 0 l20 -16" stroke="#f2c79b" stroke-width="7"/><path d="M-52 -26 q-4 10 6 12 l4 -16z" fill="#e0a800"/>'
 '<g transform="translate(0 72)"><path d="M-44 0 q8 -14 24 -10 l30 -2 q14 -2 22 6 l-8 4 q-30 6 -60 6z" fill="#2a9d6f"/><circle cx="26" cy="-6" r="2" fill="#111"/></g></g>')
def SHIVA_CATCH(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-26 50 q-4 -50 26 -60 q30 10 26 60z" fill="#7aa8d8"/><circle cy="-24" r="16" fill="#9ac0e8"/>'
 '<path d="M-20 -36 q-20 -30 -10 -60 q10 20 30 10 q-4 -30 20 -40 q0 30 -10 50 q14 -10 20 -30 q10 30 -16 70z" fill="#5a3a1a"/><path d="M0 -150 q-30 40 -10 70 q20 20 10 40" stroke="#bfe3f0" stroke-width="14" fill="none"/>'
 '<circle cx="-5" cy="-24" r="2" fill="#111"/><circle cx="5" cy="-24" r="2" fill="#111"/><path d="M-4 -36 v6" stroke="#c0392b"/><path d="M14 -40 a6 6 0 1 1 0 .1" fill="#fff"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The river Ganga falling from the sky into Shiva’s matted hair, and a king with folded hands on a rock below">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/><path d="M200 0 Q160 60 190 110" stroke="#bfe3f0" stroke-width="24" fill="none" opacity=".8"/>'+SHIVA_CATCH(190,200,1)
 +'<path d="M0 250 Q190 230 380 252 V268 H0z" fill="#4aa3df"/><rect x="290" y="216" width="60" height="22" fill="#8a7a6a" stroke="#111"/>'+KING(320,214,.8)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Gaṅgā</b>, white-robed, riding a <b>makara</b>'),
 ('River','The <b>Bhāgīrathī</b>: named after King <b>Bhagīratha</b>; it becomes the Gaṅgā at Devaprayāg'),
 ('Where','Uttarkashi district, Uttarakhand, about 3,100 m up, on the bank of the Bhāgīrathī'),
 ('The source','<b>Gaumukha</b>, “the cow’s mouth”: the snout of the <b>Gaṅgotrī glacier</b>, a long walk upstream'),
 ('Legend','Bhagīratha’s penance brought Gaṅgā from heaven; Śiva caught her in his hair'),
 ('Temple','White granite, built by the Gorkha general <b>Amar Singh Thapa</b>'),
 ('Season','Open from <b>Akṣaya Tṛtīyā</b> to <b>Dīpāvalī</b>; in winter Gaṅgā lives at <b>Mukhbā</b>')])
 +talk("If this is where Gaṅgā starts, why is the river called Bhāgīrathī?","Because a king brought her. She keeps his name until she meets the Alakanandā.")))
pages.append(page('where','WHERE IT IS','The second of four',fig(560,330,'Simplified map of Garhwal: Gangotri at the head of the Bhagirathi, Yamunotri to the west, Kedarnath and Badrinath to the east, the rivers joining at Devaprayag',UKMAP())
 +'''<div class="panel reading"><p><b>The Bhāgīrathī valley.</b> Gaṅgotrī stands on the river’s right bank in a deep pine valley, ringed by high peaks. It is the second stop on the Himalayan Char Dham, after Yamunotrī.</p>
<p><b>Upstream.</b> The glacier’s snout, <b>Gaumukha</b>, lies much higher; beyond it is <b>Tapovana</b>, a meadow below the peak called <b>Śivaliṅga</b>.</p></div>'''))
pages.append(page('sagara','THE LEGEND · KING SAGARA','Sixty thousand sons',fig(560,170,'A sage in meditation opening his eyes, flames bursting out over a crowd of princes, a horse tied nearby',
 '<rect width="560" height="170" fill="#2a1a1a"/>'+person(140,140,'#ff8c1a','#d8b090',1.1)+'<g transform="translate(420 140)">'+''.join(f'<path d="M{-100+i*20} 20 q-10 -40 6 -70 q4 20 12 24 q4 -30 16 -40 q-6 30 4 46 q8 -10 4 -24 q14 24 -6 64z" fill="#ff8c1a" stroke="#c0392b"/>' for i in range(10))+'</g>'
 +'<g transform="translate(240 150)" stroke="#111" stroke-width="2"><rect x="-30" y="-30" width="50" height="22" rx="8" fill="#fff"/><circle cx="26" cy="-34" r="10" fill="#fff"/><path d="M-26 -8 v18 M10 -8 v18" /></g>')+'''<div class="steps">
<div><b>The horse.</b> King <b>Sagara</b> of Ayodhyā, of the Sun dynasty, held a great horse sacrifice. Indra stole the horse and hid it beside the sage <b>Kapila</b>.</div>
<div><b>The sons.</b> Sagara’s 60,000 sons dug through the earth to find it, found it by Kapila, and accused him of theft.</div>
<div><b>Ashes.</b> Kapila opened his eyes, and his fire burned them all to ashes. Only the waters of heaven, Gaṅgā, could purify them and free their souls.</div>
</div>'''))
pages.append(page('bhagiratha','THE LEGEND · BHAGĪRATHA','Bringing heaven down',fig(560,180,'A king standing on one leg in penance on a rock beside a river, snow peaks behind',
 '<rect width="560" height="180" fill="#cfe3f5"/>'+''.join(f'<path d="M{x} 120 l60 -100 l60 100z" fill="#fff" stroke="#888"/>' for x in (40,200,360))+'<path d="M0 170 Q280 150 560 172" stroke="#4aa3df" stroke-width="16" fill="none"/><rect x="230" y="134" width="100" height="26" fill="#8a7a6a" stroke="#111" stroke-width="2"/>'+KING(280,132,1)+T(280,176,'BHAGĪRATHA ŚILĀ',11,'#0d3f73'))+'''<div class="steps">
<div><b>Generations of effort.</b> Sagara’s grandson Aṃśumān and his son Dilīpa tried and failed. Dilīpa’s son <b>Bhagīratha</b> left his throne and did fierce penance, here by tradition, on a rock now called the <b>Bhagīratha Śilā</b>.</div>
<div><b>Brahmā agrees.</b> Pleased, Brahmā granted that Gaṅgā would descend. But her fall from heaven would shatter the earth.</div>
<div><b>One more penance.</b> So Bhagīratha prayed to <b>Śiva</b>, the only one strong enough to take her weight.</div>
</div>'''+talk("That's why we say a 'Bhagīratha effort'?","Three generations, one river. Any near-impossible task finished by sheer persistence is 'Bhagīratha prayatna'.")))
pages.append(page('shiva','ŚIVA AND THE RIVER','Caught in his hair',fig(560,200,'Shiva standing with his matted hair spread wide as the river Ganga falls into it from the sky and emerges as a gentle stream',
 '<rect width="560" height="200" fill="#1d2a4a"/>'+''.join(f'<circle cx="{(i*71)%560}" cy="{(i*29)%80}" r="2" fill="#fff"/>' for i in range(20))+SHIVA_CATCH(280,150,1.2)+'<path d="M300 200 q40 -10 80 -4 t120 0" stroke="#bfe3f0" stroke-width="8" fill="none"/>')+'''<div class="steps">
<div><b>The fall.</b> Proud Gaṅgā thought she would sweep Śiva away and fell with all her force.</div>
<div><b>The hair.</b> Śiva caught her in his matted locks, the <b>jaṭā</b>, and held her there, wandering in the tangles, until her pride was gone.</div>
<div><b>Released gently.</b> Then he let her out in a gentle stream. That is why Śiva is <b>Gaṅgādhara</b>, “bearer of Gaṅgā”.</div>
<div><b>The submerged liṅga.</b> In the river by the temple is a natural rock liṅga, said to mark where Śiva sat to receive her. It shows only in winter, when the water is low.</div>
</div>'''))
pages.append(page('jahnu','JAHNU AND THE SEA','The rest of the journey',facts([
 ('Bhagīratha leads','The king drove his chariot ahead; Gaṅgā followed him across the land'),
 ('Jahnu','She flooded the hermitage of the sage <b>Jahnu</b>, who drank her up in anger. At Bhagīratha’s plea, he let her out from his ear. So she is <b>Jāhnavī</b>, “Jahnu’s daughter”'),
 ('The sea','At last she reached the ocean, at <b>Gaṅgāsāgara</b>, flowed over the ashes, and freed the 60,000 sons'),
 ('Three worlds','She flows in heaven, on earth and in the underworld: <b>Tripathagā</b>')])
 +talk("So Gaṅgā has three fathers' names on her?","Bhāgīrathī for the king who called her, Jāhnavī for the sage who freed her, Gaṅgā for herself.")))
pages.append(page('temple','THE TEMPLE','White granite by the river',fig(560,180,'A white temple with a tall curved spire on a river bank, steps going down to the water',
 '<rect width="560" height="180" fill="#cfe3f5"/>'+HILL(80,180,220,160,'#2e6a2e')+HILL(480,180,220,160,'#2e6a2e')+'<rect y="150" width="560" height="30" fill="#4aa3df"/>'+TEMPLE(280,150,1.6,'#fff')+''.join(f'<rect x="{200+i*10}" y="{150-i*5}" width="{160-i*20}" height="5" fill="#ddd" stroke="#111" stroke-width=".8"/>' for i in range(4)))+facts([
 ('Builder','<b>Amar Singh Thapa</b>, the Gorkha general who ruled Garhwal for Nepal in the early 19th century'),
 ('Stone','White granite, with a curved tower'),
 ('Restored','Later in the 19th century; some accounts credit a ruler of Jaipur with renewing it'),
 ('Images','Gaṅgā, with Yamunā, Sarasvatī, Lakṣmī, Annapūrṇā, Bhagīratha and Ādi Śaṅkara, by most accounts'),
 ('Priests','The <b>Semvāl</b> family, from the village of <b>Mukhbā</b>')])
 +talk("A Nepali general built it?","During Nepal's rule over Garhwal. Faith crossed the border before borders did.")))
pages.append(page('around','AROUND GAṄGOTRĪ','Rock, liṅga, springs and caves',facts([
 ('Bhagīratha Śilā','The slab beside the temple where Bhagīratha meditated; Gaṅgā is said to have touched earth here'),
 ('Jalamagna Śivaliṅga','The submerged natural liṅga in the river, seen when the water falls'),
 ('Gaurī Kuṇḍa, Sūrya Kuṇḍa','Pools a little downstream where the river roars through narrow rock channels'),
 ('Pāṇḍava Guphā','Caves where the Pāṇḍavas are said to have done penance'),
 ('Bhairava','Bhairon Ghāṭī, below Gaṅgotrī, with a Bhairava temple that guards the way')])))
pages.append(page('gaumukh','GAUMUKHA','The cow’s mouth',fig(560,180,'A huge wall of ice with a dark cave at its base, a stream rushing out, a sharp snow peak beyond',
 '<rect width="560" height="180" fill="#cfe3f5"/><path d="M360 90 l60 -80 l60 80z" fill="#fff" stroke="#888"/><path d="M0 60 Q280 30 560 70 V140 H0z" fill="#e6f0f8" stroke="#888"/><ellipse cx="280" cy="130" rx="60" ry="30" fill="#2a3a4a"/>'+'<path d="M280 150 Q300 170 260 180 M260 150 Q240 170 280 180" stroke="#bfe3f0" stroke-width="10" fill="none"/>'+T(420,20,'ŚIVALIṄGA',11,'#0d3f73'))+facts([
 ('What','The snout of the <b>Gaṅgotrī glacier</b>, where the Bhāgīrathī bursts out of an ice cave'),
 ('Name','Its shape was once likened to a cow’s mouth: <b>gau-mukha</b>'),
 ('Retreating','The glacier has been shrinking; the snout has moved back and changed shape over the decades'),
 ('Beyond','<b>Tapovana</b>, a high meadow below the peaks <b>Śivaliṅga</b> and <b>Meru</b>'),
 ('Pilgrims','Some walk up to take water from the very source')])
 +talk("The 'cow's mouth' doesn't look like a cow any more?","Glaciers move. The ice retreats; the faith stays put.")))
pages.append(page('year','THE YEAR AT GAṄGOTRĪ','Summer up, winter down',facts([
 ('Opening','On <b>Akṣaya Tṛtīyā</b>, Gaṅgā’s image is carried up from Mukhbā'),
 ('Gaṅgā Daśaharā','Jyeṣṭha, the tenth bright day: the day Gaṅgā is said to have descended'),
 ('Closing','On <b>Dīpāvalī</b>, the temple shuts and she is carried in a palanquin to <b>Mukhbā</b>'),
 ('Winter','Worship continues at Mukhbā, the priests’ home village, near Harsil'),
 ('Gaṅgā jala','Pilgrims carry water home from here, for rites and the last hours of the dying')])))
pages.append(page('connect','HOW IT CONNECTS','One river, many places',facts([
 ('Chota Char Dham','Second of Yamunotrī, Gaṅgotrī, Kedārnāth, Badrīnāth'),
 ('Devaprayāg','Where the Bhāgīrathī meets the Alakanandā and becomes the Gaṅgā'),
 ('Haridvāra','Māyā of the <a href="/bhakti/temples-of-india/sapta-puri/">Saptapurī</a>: where she leaves the hills'),
 ('Kāśī','On her bank: <a href="/bhakti/temples-of-india/12-jyotirlingas/kashi-vishwanath/">Kāśī Viśvanātha</a>'),
 ('Prayāga','Where she meets the Yamunā from <a href="/bhakti/temples-of-india/char-dham/yamunotri/">Yamunotrī</a>'),
 ('Gaṅgāsāgara','Where she reaches the sea, and the ashes of Sagara’s sons')])
 +'<div class="key">More: <a href="/bhakti/temples-of-india/char-dham/">Char Dham, the two circuits</a></div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Bhāgīrathī','“Bhagīratha’s river”'),('Jāhnavī','“Jahnu’s daughter”'),('Jaṭā','Matted hair'),('Gaṅgādhara','Śiva, “bearer of Gaṅgā”'),('Makara','Gaṅgā’s mount, a crocodile-like creature'),
 ('Gaumukha','“Cow’s mouth”'),('Śilā','Rock slab'),('Jalamagna','Under water'),('Prayāga','Confluence'),('Daśaharā','“Removing ten (sins)”: Gaṅgā’s festival')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The legend.</b> Sagara’s sons burned to ashes; Bhagīratha’s penance brought Gaṅgā down to free them.</div>
<div><b>Śiva.</b> He caught her in his hair; the submerged liṅga marks where he sat.</div>
<div><b>The names.</b> Bhāgīrathī for the king, Jāhnavī for the sage, Gaṅgā for herself.</div>
<div><b>The place.</b> Amar Singh Thapa’s white temple by the Bhagīratha Śilā; Gaumukha above; Mukhbā in winter.</div>
<div><b>The circuit.</b> Second of the Himalayan Char Dham; her water flows on through Haridvāra, Kāśī and Prayāga to the sea.</div>
</div>'''+talk("One line to remember?","A king's stubborn love for his ancestors brought heaven's river to earth.")+'<div class="key">Har Har Gaṅge! 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Shrine:</b> Wikipedia, “Gangotri” (Bhāgīrathī from the Gaṅgotrī glacier; Bhagīratha’s penance; temple built by Amar Singh Thapa, restored in the 19th c.; closed from Dīpāvalī to Akṣaya Tṛtīyā; idol at Mukhbā near Harsil; Semvāl priests; Bhagīratha Śilā; submerged liṅga; Gaumukha). shubhpanchang.com (Thapa’s building in the early 19th c. during Gorkha rule of Garhwal; Mukhbā). ghumakkar.com and trawell.in (Jalamagna Śivaliṅga seen in winter; Gaurī and Sūrya Kuṇḍas). iskcondesiretree.com (renovation by a Jaipur ruler; Pāṇḍava sites). trekthehimalayas.com (images of Śaṅkara and Bhagīratha; palanquin to Mukhbā; Tapovana, Śivaliṅga, Meru).</p>
<p><b>Legends:</b> Rāmāyaṇa (Bāla Kāṇḍa) and Bhāgavata Purāṇa on Sagara, Kapila, Bhagīratha, Śiva and Jahnu.</p>
<p><b>Sources differ:</b> many websites say Thapa built the temple in the “early 18th century”, but he lived 1751–1816 and Gorkha rule in Garhwal was 1804–1815, so the early 19th century fits; who restored it later. <b>Not verified:</b> the full list of images in the sanctum; the Pāṇḍava caves. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('sagara','Legend · King Sagara'),('bhagiratha','Legend · Bhagīratha'),('shiva','Śiva and the River'),('jahnu','Jahnu and the Sea'),('temple','The Temple'),('around','Around Gaṅgotrī'),
 ('gaumukh','Gaumukha'),('year','The Year at Gaṅgotrī'),('connect','How It Connects'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
bk=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">WHERE GAṄGĀ CAME DOWN</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">GAṄGOTRĪ</h1>
  <div class="series">CHAR DHAM · A REFERENCE GUIDE</div>
  <div class="tag">A king’s penance, Śiva’s hair, heaven’s river</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Sixty thousand princes lay as ashes, and only the river of heaven could free them. Their descendant, King <b>Bhagīratha</b>, gave up his throne and sat in penance on a rock in the Himalaya until <b>Gaṅgā</b> agreed to come down, and <b>Śiva</b> agreed to catch her.</p>
    <p>That rock is beside a white temple at <b>Gaṅgotrī</b>. The river rushing past still carries the king’s name, the Bhāgīrathī, and high above, it pours out of a cave of ice.</p>
    <p>This guide tells the legend, the shrine and the places around it.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Har Har Gaṅge,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is the temple at the actual source?","Close. The true source is the glacier's mouth, higher up. The temple marks where Bhagīratha prayed.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Gangotri.html','w').write(head+bk+tail())
print('ok',len(pages))
