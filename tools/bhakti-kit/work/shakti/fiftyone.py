exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Beyond the Eighteen · The 51 Śakti Pīṭhas · srini.presents',
 'The 51 Śakti Pīṭhas of the Pīṭhanirṇaya (Tantra Cūḍāmaṇi), region by region: body part, Goddess and Bhairava at each seat, the four Ādi Pīṭhas, how the counts of 4, 18, 51, 52 and 108 differ, which sites are shared with Śaṅkara’s eighteen, and which are disputed. An illustrated reference round-up.')
IN18={'Kāñcīpuram':2,'Prayāga':14,'Vārāṇasī':17,'Jvālāmukhī':15,'Jājpur (Birajā)':11,'Kāmākhyā':13,'Ujjain (Bhairava Parvata)':9}
def tbl(rows):
    h='<table class="ct"><tr><th>Pīṭha</th><th>Part</th><th>Śakti</th><th>Bhairava</th></tr>'
    for p,part,sh,bh in rows:
        tag=f' <span style="color:#c0392b">★{IN18[p]}</span>' if p in IN18 else ''
        h+=f'<tr><td><b>{p}</b>{tag}</td><td>{part}</td><td>{sh}</td><td>{bh}</td></tr>'
    return h+'</table>'
KEY='<div class="panel reading small"><p><span style="color:#c0392b">★n</span> = also one of the eighteen (No. n), with its own article. Names follow common lists of the Pīṭhanirṇaya; sources differ.</p></div>'
BENGAL=[('Kālīghāṭ, Kolkata','right toes','Kālikā','Nakuleśa'),('Bahulā, Ketugrām','left arm','Bahulā','Bhīruka'),('Ujāni (Maṅgalakoṭ)','right wrist','Maṅgala Caṇḍikā','Kapilāmbara'),('Kṣīragrām','right great toe','Jugādyā','Kṣīrakhaṇḍaka'),
 ('Kirīṭkoṇā','crown','Vimalā','Saṃvarta'),('Kaṅkālītalā','bone (hip)','Devagarbhā','Ruru'),('Aṭṭahāsa','lips','Phullarā','Viśveśa'),('Nalhāṭī','tubular bones of the feet','Kālikā','Yogeśa'),
 ('Bakreśvar','between the eyebrows','Mahiṣamardinī','Vakranātha'),('Sainthiā','necklace','Nandinī','Nandikeśvara'),('Tamluk','left ankle','Kapālinī (Bhīmarūpā)','Sarvānanda'),('Khānākul','right shoulder','Kumārī','Śiva'),('Sālbāṛī','left leg','Bhrāmarī','Ambara')]
BANGLA=[('Sugandhā, Śikārpur','nose','Sunandā','Tryambaka'),('Jayantī, Sylhet','left thigh','Jayantī','Kramadīśvara'),('Śrīśaila (Jainpur), Sylhet','neck','Mahālakṣmī','Sambarānanda'),
 ('Chandranāth, Sītākuṇḍa','right arm','Bhavānī','Candraśekhara'),('Yaśoreśvarī, Iśvarīpur','palms and soles','Yaśoreśvarī','Caṇḍa'),('Bhavānīpur, Bogra','left anklet','Aparṇā','Vāmana')]
EAST=[('Kāmākhyā','yoni','Kāmākhyā','Umānanda'),('Tripurasundarī, Udaipur (Tripurā)','right leg','Tripurasundarī','Tripureśa'),('Vimalā, Purī','feet (Ādi list) / navel (some)','Vimalā','Jagannātha'),
 ('Tārā Tāriṇī, Ganjam','breasts (Ādi list)','Tārā Tāriṇī','Tumbeśvara'),('Jājpur (Birajā)','navel','Virajā','Varāha / Jagannātha'),('Mithilā','left shoulder','Umā','Mahodara')]
NORTH=[('Kurukṣetra','ankle','Sāvitrī (Bhadrakālī)','Sthāṇu'),('Vṛndāvana','ringlets of hair','Umā (Kātyāyanī)','Bhūteśa'),('Prayāga','fingers','Lalitā / Alopī','Bhava'),('Vārāṇasī','earring','Viśālākṣī','Kāla Bhairava'),
 ('Rāmagiri (Citrakūṭ)','right breast','Śivānī','Caṇḍa'),('Pañcasāgara (near Haridvāra?)','lower teeth','Vārāhī','Mahārudra'),('Jvālāmukhī','tongue','Siddhidā (Ambikā)','Unmatta'),('Amarnāth','throat','Mahāmāyā','Trisandhyeśvara'),('Śrī Parvata (Ladakh?)','right anklet','Śrīsundarī','Sundarānanda')]
WEST=[('Hiṅglāj, Balochistan','crown of the head','Koṭṭarī','Bhīmalocana'),('Śivaharkarāy, near Karachi','eyes','Mahiṣamardinī','Krodhīśa'),('Prabhāsa (Somnāth)','stomach','Candrabhāgā','Vakratuṇḍa'),('Ambājī, Gujarat','heart','Ambā','—'),
 ('Puṣkara','two bracelets','Gāyatrī','Sarvānanda'),('Virāṭ (Bairāṭ), Rajasthan','left toes','Ambikā','Amṛteśvara'),('Ujjain (Bhairava Parvata)','upper lip','Avantī','Lambakarṇa'),('Janasthāna (Nāsik)','chin','Bhrāmarī','Vikṛtākṣa'),
 ('Kālamādhava, Amarkaṇṭak','left buttock','Kālī','Asitāṅga'),('Śoṇa, Amarkaṇṭak','right buttock','Narmadā (Śoṇākṣī)','Bhadrasena')]
SOUTH=[('Kāñcīpuram','oḍḍiyāṇa (navel ornament) / skeleton','Kāmākṣī (Devagarbhā)','Kāla Bhairava'),('Kanyākumārī','back','Śarvāṇī','Nimiṣa'),('Śucīndram','upper teeth','Nārāyaṇī','Saṃhāra'),
 ('Koṭiliṅgeśvara, Rājamahendravaram','cheeks','Rākiṇī (Viśveśvarī)','Vatsanābha'),('Nainātīvu, Laṅkā','anklets','Indrākṣī (Nāgapūṣaṇī)','Rākṣaseśvara'),('Karṇāṭa (site unknown)','both ears','Jayadurgā','Abhīru')]
ABROAD=[('Guhyeśvarī, Kathmandu','both knees','Mahāśirā','Kapālī'),('Gaṇḍakī (Muktināth)','temple (cheek)','Gaṇḍakī Caṇḍī','Cakrapāṇi'),('Mānasa, Tibet','right hand','Dākṣāyaṇī','Amara')]
def NUMS():
    bars=[(4,'Ādi'),(18,'Mahā'),(51,'Pīṭhanirṇaya'),(52,'Bengal'),(108,'Devī Bhāgavata')]
    g='<rect width="560" height="180" fill="#fdf1e8"/>'
    for i,(n,l) in enumerate(bars):
        x=50+i*100;hh=n*1.3
        g+=f'<rect x="{x}" y="{150-hh:.0f}" width="60" height="{hh:.0f}" fill="#c0392b" stroke="#111" stroke-width="1.5"/>'+T(x+30,f'{144-hh:.0f}',str(n),14,'#111')+T(x+30,168,l,11,'#555')
    return g
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A stylised map of India and its neighbours dotted with many small red lamps">'
 '<rect width="380" height="268" fill="#4a0e0e" rx="8"/><g transform="translate(40 4) scale(.8)">'+LAND().replace('#f4e6d0','#f2e6c8')+''.join(f'<circle cx="{xy(la,lo)[0]:.0f}" cy="{xy(la,lo)[1]:.0f}" r="4" fill="#c0392b" stroke="#ffd166"/>' for la,lo in ((22.5,88.3),(23.6,87.7),(24.0,88.1),(23.4,87.9),(26.17,91.7),(19.8,85.8),(23.5,91.5),(24.9,91.9),(22.6,91.7),(25.3,83.0),(25.4,81.9),(29.97,76.8),(27.6,77.7),(31.88,76.3),(34.2,75.5),(25.5,65.5),(20.9,70.4),(24.3,72.8),(26.5,74.6),(23.2,75.8),(20.0,73.8),(22.7,81.8),(12.8,79.7),(8.08,77.55),(8.15,77.46),(17.0,81.8),(9.6,79.8),(27.7,85.35),(28.8,83.9),(20.85,86.3),(19.3,84.8),(24.78,85.0),(26.6,85.9),(23.4,89.1)))+'</g></svg>')
pages=[]
pages.append(page('counts','HOW MANY PĪṬHAS?','4, 18, 51, 52 or 108',fig(560,180,'Bar chart of the different counts of Shakti Pithas: 4 Adi, 18 Maha, 51 in the Pithanirnaya, 52 in a Bengal tradition, 108 in the Devi Bhagavata',NUMS())+facts([
 ('4','The <b>Ādi</b> (first) Pīṭhas: Kāmākhyā, Vimalā, Tārā Tāriṇī, Dakṣiṇa Kālikā'),
 ('18','The <b>Mahā</b> Pīṭhas of the Aṣṭādaśa hymn credited to Śaṅkara: our main series'),
 ('51','The <b>Pīṭhanirṇaya</b> (Mahāpīṭhanirūpaṇa) of the Tantra Cūḍāmaṇi: each with body part, Śakti and Bhairava'),
 ('52','A Bengal tradition adds one more'),
 ('108','The Devī Bhāgavata names 108 seats of the Goddess')])
 +talk("Why so many different numbers?","Different texts, different centuries, different regions. And the same Pīṭha is sometimes placed in two towns.")))
pages.append(page('adi','THE FOUR ĀDI PĪṬHAS','The first four',facts([
 ('Kāmākhyā, Assam','<b>yoni</b>: also No. 13 of the eighteen'),
 ('Vimalā, Purī','<b>feet</b>: inside the Jagannātha temple'),
 ('Tārā Tāriṇī, Ganjam, Odisha','<b>breasts</b>: on a hill by the Ṛṣikulyā river'),
 ('Dakṣiṇa Kālikā (Kālīghāṭ), Kolkata','<b>face</b> in this list; right toes in the Pīṭhanirṇaya')])
 +'<div class="key">Three of the four are in Odisha and Bengal: the old heartland of Śākta worship.</div>'))
pages.append(page('bengal','WEST BENGAL','The richest cluster','<div class="panel reading small"><p>Bengal holds more Pīṭhas than any other region, many in Birbhum and Bardhaman districts.</p></div>'+tbl(BENGAL)+KEY))
pages.append(page('kalighat','KĀLĪGHĀṬ','Kolkata’s Kālī',facts([
 ('Part','The toes of the right foot'),('Goddess','Kālī, with a long golden tongue and three great eyes'),('Bhairava','Nakuleśa'),('City','Kolkata takes its name, by one theory, from Kālīghāṭ'),('Ādi list','Counted among the four first Pīṭhas, as the face')])
 +talk("Is Kālīghāṭ in our eighteen?","No. Of Bengal's many Pīṭhas only Pradyumna (No. 3, Śṛṅkhalā) made Śaṅkara's list.")))
pages.append(page('bangladesh','BANGLADESH','Across the eastern border',tbl(BANGLA)+'<div class="panel reading small"><p>After 1947 several of these shrines lost most of their pilgrims; some are being restored. Chandranāth hill’s famous temple is the Bhairava’s; the Goddess’s shrine is below it.</p></div>'+KEY))
pages.append(page('east','THE EAST AND NORTH-EAST','Assam, Tripurā, Odisha, Mithilā',tbl(EAST)+'<div class="panel reading small"><p><b>The navel question.</b> Lists differ on whether Utkala’s navel-Pīṭha is Vimalā at Purī or Birajā at Jājpur. Both are honoured.</p></div>'+KEY))
pages.append(page('north','THE NORTH','Kurukṣetra to Kashmir',tbl(NORTH)+'<div class="panel reading small"><p><b>Hard to place:</b> Pañcasāgara and Śrī Parvata are disputed; Rāmagiri is placed at Citrakūṭ or near Maihar by different writers.</p></div>'+KEY))
pages.append(page('west','THE WEST AND CENTRE','Balochistan to the Narmadā',tbl(WEST)+'<div class="panel reading small"><p><b>Hiṅglāj</b> in Balochistan is still visited every spring, by Hindus from Pakistan and India alike. Ujjain’s Avantī is identified with <b>Harsiddhi</b> by many.</p></div>'+KEY))
pages.append(page('hinglaj','HIṄGLĀJ','The crown of the head',facts([
 ('Where','A cave shrine in the Hingol valley, Las Bela, Balochistan, Pakistan'),('Part','The brahmarandhra, crown of the head'),('Goddess','Koṭṭarī; Hiṅglāj Mātā'),
 ('Pilgrimage','A desert journey with a mud-volcano stop; local Muslims revere her too, as Nānī'),('Fame','Among the most visited Hindu shrines in Pakistan')])
 +talk("A Pīṭha in Balochistan still visited?","Every year. Hiṅglāj is proof that the Goddess's map is older than any border.")))
pages.append(page('south','THE SOUTH AND LAṄKĀ','Kāñcī to the islands',tbl(SOUTH)+'<div class="panel reading small"><p><b>Two Laṅkās.</b> The eighteen place Śāṅkarī in Laṅkā (Trincomalee is claimed); the fifty-one place Indrākṣī there, identified by many with <b>Nāgapūṣaṇī</b> at Nainātīvu. See our <a href="'+SER+'shankari/">Śāṅkarī</a> article.</p></div>'+KEY))
pages.append(page('abroad','THE HIMALAYA BEYOND','Nepal and Tibet',tbl(ABROAD)+facts([('Guhyeśvarī','By the Bāgmatī near Paśupatinātha; some texts give a different part'),('Muktināth','The Gaṇḍakī river, home of the śālagrāma stones'),('Mānasa','Lake Mānasarovar below Mount Kailāsa')])+KEY))
pages.append(page('shared','SHARED WITH THE EIGHTEEN','Where the two lists meet',facts([
 ('Shared','Kāñcī, Ujjain, Jājpur, Kāmākhyā, Prayāga, Jvālāmukhī, Vārāṇasī: on both lists'),
 ('Near-shared','Śrīśailam, Gayā, Drākṣārāmam, Kolhāpur, Māhur, Mysuru, Ālampur, Pīṭhāpuram, Śāradā and Laṅkā: in the eighteen, but missing or differently placed in common 51 lists'),
 ('Why','The eighteen is a southern, hymn-based list; the 51 is a Tantric, eastern list. They grew up apart'),
 ('Result','Together they make some sixty seats that pilgrims honour as Pīṭhas')])
 +talk("So the eighteen aren't just a subset of the 51?","No. Overlapping circles, not one inside the other.")))
SLUG={1:'shankari',2:'kamakshi',3:'shrinkhala',5:'jogulamba',6:'bhramaramba',7:'mahalakshmi-kolhapur',8:'ekavirika-mahur',9:'mahakali-ujjain',10:'puruhutika',11:'girija-jajpur',12:'manikyamba-draksharamam',13:'kamakhya',14:'madhaveshwari-prayaga',15:'jwalamukhi',16:'mangalyagauri-gaya',17:'vishalakshi-varanasi',18:'sharada-kashmir'}
def lk(n): return '/bhakti/temples-of-india/around-mysuru/chamundeshwari/' if n==4 else SER+SLUG[n]+'/'
pages.append(page('series','THE EIGHTEEN ON THIS SITE','Full guides',facts([(f'{n} {g}',f'<a href="{lk(n)}">{sh}</a>') for n,g,_,_,_,_,_,_,sh in P])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Pīṭha','Seat'),('Ādi','First'),('Mahā','Great'),('Upa-pīṭha','Lesser seat'),('Bhairava','Śiva as the Pīṭha’s guardian'),('Pīṭhanirṇaya','“Determination of the seats”: the 51-list text'),('Brahmarandhra','Crown of the head')])))
pages.append(page('end','ON ONE PAGE','The whole round-up in five lines','''<div class="steps">
<div><b>Counts.</b> 4 Ādi, 18 Mahā, 51 in the Pīṭhanirṇaya, 52 in Bengal, 108 in the Devī Bhāgavata.</div>
<div><b>Bengal.</b> The richest cluster: Kālīghāṭ, Bahulā, Aṭṭahāsa, Bakreśvar and more.</div>
<div><b>Beyond borders.</b> Bangladesh, Pakistan (Hiṅglāj), Nepal, Tibet and Laṅkā.</div>
<div><b>Overlap.</b> Seven seats are on both lists; the rest belong to one.</div>
<div><b>Disputes.</b> Many sites are claimed by two towns; the body parts vary between texts.</div>
</div>'''+talk("One line to remember?","However you count them, the Mother's body became the map of a whole civilisation.")+'<div class="key">Beyond the eighteen: <b>the fifty-one seats</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Lists:</b> the 51-seat table follows the widely reproduced Pīṭhanirṇaya-based list (as in religion.fandom.com, “Shakti Peethas”, derived from an older Wikipedia version), checked against hinduscriptures.com and other lists. Wikipedia, “Shakti Peetha” (counts of 51, 52, 64, 108; the 18 Mahā list; the four primary seats; disputes over Laṅkā, Śāradā, Guhyeśvarī; Sircar on the Bengal 52). encyclopedia.pub and the Kālikā Purāṇa verse on the four Ādi Pīṭhas.</p>
<p><b>Caution:</b> many entries are disputed. Body parts, Goddess names and Bhairavas vary between manuscripts and regional traditions; several sites (Pañcasāgara, Śrī Parvata, Karṇāṭa, Rāmagiri) are not securely located; some lists include Ambājī, Dantewāḍā or Panna. Treat the tables as a guide, not a final word. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('counts','How Many Pīṭhas?'),('adi','The Four Ādi Pīṭhas'),('bengal','West Bengal'),('kalighat','Kālīghāṭ'),('bangladesh','Bangladesh'),('east','The East and North-East'),('north','The North'),('west','The West and Centre'),('hinglaj','Hiṅglāj'),('south','The South and Laṅkā'),('abroad','The Himalaya Beyond'),('shared','Shared with the Eighteen'),('series','The Eighteen on This Site'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ROUND-UP</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,7vw,70px)">THE 51 PĪṬHAS</h1>
  <div class="series">BEYOND THE EIGHTEEN · A REFERENCE GUIDE</div>
  <div class="tag">Every seat of the Mother, region by region</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Śaṅkara’s hymn names eighteen great seats of the Goddess. But the older Tantric list, the <b>Pīṭhanirṇaya</b>, names <b>fifty-one</b>: each where a part of Satī’s body, or one of her ornaments, fell, each with its own Goddess and its own Bhairava.</p>
    <p>Many of them are in Bengal; others are in Bangladesh, Pakistan, Nepal, Tibet and Laṅkā. Some are great temples; some are a stone under a tree; a few nobody can find any more.</p>
    <p>This round-up walks the fifty-one region by region, marks which ones are also in the eighteen, and is honest about where the lists disagree.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Will there be full guides for all 51?","The eighteen have full guides. This page gathers the rest in one place.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Fifty_One_Pithas.html','w').write(head+b+tail())
print('ok',len(pages))
