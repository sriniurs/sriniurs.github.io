exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Bhuvaneśvarī · Daśa Mahāvidyā 4 · srini.presents',
 'Bhuvaneśvarī, the fourth of the Daśa Mahāvidyā: Queen of the Worlds and Goddess of space, Maṇidvīpa and the Trimūrti in the Devī Bhāgavata, the Devī Gītā, her bond with Tripurasundarī, the seed sound hrīṃ, and Bhuvaneśvarī as Kannada Tāyi of Karnataka: Hampi, Bhuvanagiri, the Mysuru Palace temple and Rājyotsava. An illustrated reference guide.')
def BHUV(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-60 54 q60 -30 120 0" fill="#f2a6c0"/><path d="M-30 50 q-4 -54 30 -66 q34 12 30 66z" fill="#e0115f"/>'
 '<path d="M-22 -8 l-26 -20 M22 -8 l26 -20 M-22 6 l-26 10 M22 6 l26 10" stroke="#f2c070" stroke-width="7"/><circle cx="-52" cy="-30" r="7" fill="none" stroke="#e0a800" stroke-width="3"/><path d="M48 -32 l8 -10 l4 6" stroke="#bbb" stroke-width="3" fill="none"/>'
 '<path d="M-50 18 l-4 8 l8 0" fill="#f2c070"/><path d="M50 18 v-10" stroke="#f2c070" stroke-width="5"/>'
 '<circle cy="-36" r="15" fill="#f2c070"/><path d="M-14 -48 h28 l-4 -16 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/><path d="M-5 -68 a8 8 0 1 0 11 3" fill="none" stroke="#fff8c0" stroke-width="2.5"/>'
 '<circle cx="-5" cy="-38" r="2.4" fill="#111"/><circle cx="5" cy="-38" r="2.4" fill="#111"/><path d="M-3 -46 h6" stroke="#c0392b" stroke-width="2"/><path d="M-6 -29 q6 5 12 0" fill="none"/></g>')
def GLOBE(x,y,r=60): return f'<g transform="translate({x} {y})" stroke="#111" stroke-width="2"><circle r="{r}" fill="#9fd0ea"/><path d="M{-r} 0 h{2*r} M0 {-r} v{2*r}" stroke="#3b6fd0"/><ellipse rx="{r*0.5}" ry="{r}" fill="none" stroke="#3b6fd0"/><ellipse rx="{r}" ry="{r*0.4}" fill="none" stroke="#3b6fd0"/><path d="M-20 -20 q10 -14 26 -6 q6 16 -10 20z M10 12 q14 -4 20 10 q-10 12 -22 4z" fill="#5a9a4a"/></g>'
FLAG='<g stroke="#111" stroke-width="1.5"><rect x="0" y="0" width="60" height="18" fill="#ffd60a"/><rect x="0" y="18" width="60" height="18" fill="#c0392b"/><path d="M0 0 v60" stroke-width="3"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The golden goddess Bhuvaneshvari seated with the globe of the worlds glowing behind her and a rising sun">'
 '<rect width="380" height="268" fill="#3a0e2a" rx="8"/>'+''.join(f'<circle cx="{(i*41)%380}" cy="{(i*23)%268}" r="1.4" fill="#fff"/>' for i in range(40))+GLOBE(190,110,90).replace('#9fd0ea','#1d3f73')+BHUV(190,170,1.2)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Bhuvaneśvarī</b>: “Queen (īśvarī) of the worlds (bhuvana)”'),
 ('Place','<b>Fourth</b> of the ten Mahāvidyās'),
 ('She is','The Goddess as <b>space</b> itself: the room in which everything exists'),
 ('Look','Golden or rising-sun red; smiling; crescent moon; three eyes; noose and goad; hands that bless and say “fear not”'),
 ('Texts','The <b>Devī Bhāgavata Purāṇa</b> calls her Ādi Parāśakti; its Devī Gītā'),
 ('Home','<b>Maṇidvīpa</b>, the jewel island in the ocean of nectar'),
 ('Seed sound','<b>hrīṃ</b>, the “hrīṃkāra”'),
 ('Karnataka','Worshipped as <b>Kannada Tāyi</b>, Mother Kannada: Hampi, Bhuvanagiri, the Mysuru Palace temple, Rājyotsava')])
 +talk("A Goddess who is empty space?","Not empty: spacious. Every star, every thought needs room. She is the room.")))
pages.append(page('names','HER NAMES','Queen of the three worlds',facts([
 ('Bhuvana','The worlds: <i>tribhuvana</i>, the three of earth (bhūḥ), sky (bhuvaḥ) and heaven (svaḥ)'),
 ('Īśvarī','Sovereign, queen'),
 ('Hrīṃkārī','“She who is the sound hrīṃ”: a name in the Lalitā Sahasranāma'),
 ('Ādi Parāśakti','“Supreme primal power”: her title in the Devī Bhāgavata'),
 ('Kannada Tāyi · Nāḍa Devī','“Mother Kannada”, “Goddess of the land”: her Karnataka names'),
 ('Bhuvaneśvara','Her consort: Śiva as Lord of the worlds')])
 +talk("So bhūr bhuvaḥ svaḥ in the Gāyatrī is her?","Those are her three worlds. She is the queen of exactly what the Gāyatrī names.")))
pages.append(page('form','HER FORM','The gentle sovereign',fig(560,200,'A golden goddess seated, smiling, with a crescent moon in her crown, holding a noose and goad, her other hands blessing',
 '<rect width="560" height="200" fill="#fdf1e8"/>'+GLOBE(280,90,80)+BHUV(280,130,1.2))+facts([
 ('Colour','Golden, or red like the rising sun'),
 ('Face','Smiling, three-eyed, with a crescent moon'),
 ('Noose and goad','She draws beings in, and guides them'),
 ('Varada and abhaya','Her other hands give boons and say “do not fear”'),
 ('Seat','A throne, or a lotus; sometimes on Śiva'),
 ('Mood','Saumya, gentle: a mother nursing the world')])))
pages.append(page('space','THE GODDESS OF SPACE','Ākāśa, the first element',facts([
 ('Ākāśa','Of the five elements, space (ākāśa) comes first; the others arise within it'),
 ('Kālī and Bhuvaneśvarī','Kālī is <b>time</b>; Bhuvaneśvarī is <b>space</b>: together, the frame of the world'),
 ('Room to be','Nothing can exist without space, so she is the ground of every created thing'),
 ('The heart','Teachers say her true seat is the space of the heart (hṛdayākāśa)'),
 ('Fourth wisdom','After Kālī, Tārā and Tripurasundarī, the Goddess as the world’s own vastness')])
 +talk("Time first, then space?","Kālī ends things; Bhuvaneśvarī makes room for them. Between them, a universe.")))
pages.append(page('manidvipa','MAṆIDVĪPA AND THE TRIMŪRTI','The gods who became women',fig(560,180,'Three gods in a flying chariot arriving at a jewel island in a sea of nectar, where a golden goddess sits enthroned',
 '<rect width="560" height="180" fill="#bfe3f0"/><path d="M220 160 Q380 100 540 160 V180 H220z" fill="#ffe8a8" stroke="#111"/>'+''.join(f'<path d="M{260+i*40} 150 l10 -20 l10 20z" fill="#e0115f" stroke="#111"/>' for i in range(6))+BHUV(400,110,.6)
 +'<g transform="translate(120 80)" stroke="#111" stroke-width="2"><path d="M-70 0 h140 l-20 20 h-100z" fill="#e0a800"/>'+''.join(person(dx,0,c,'#f2c79b',.5) for dx,c in ((-40,'#c0392b'),(0,'#3b6fd0'),(40,'#fff')))+'</g>')+'''<div class="steps">
<div><b>A question.</b> In the Devī Bhāgavata, Brahmā, Viṣṇu and Śiva once wondered who was greatest. A celestial chariot carried them across the ocean of nectar to <b>Maṇidvīpa</b>.</div>
<div><b>The vision.</b> There they saw the Goddess, Bhuvaneśvarī, enthroned. Under her gaze the three gods found themselves turned into women, attendants of the Goddess.</div>
<div><b>The gift.</b> Humbled, they praised her. She gave each his power: Sarasvatī to Brahmā, Lakṣmī to Viṣṇu, Kālī (Gaurī) to Śiva, and sent them to create, keep and end the worlds.</div>
</div>'''+talk("The Trimūrti work for her?","In the Devī Bhāgavata, yes. Every creator, keeper and destroyer is borrowing her power.")))
pages.append(page('devigita','THE DEVĪ GĪTĀ','The Goddess teaches',facts([
 ('Where','Book 7 of the Devī Bhāgavata Purāṇa'),
 ('Setting','The Goddess appears to Himavat, king of the mountains, in her cosmic form as Bhuvaneśvarī'),
 ('Teaching','She explains that she is Brahman, the self of all; she teaches yoga, devotion and knowledge'),
 ('Model','Built on the Bhagavad Gītā, with the Goddess in Kṛṣṇa’s place'),
 ('Cosmic form','Like Kṛṣṇa’s viśvarūpa, she shows the worlds within her body')])
 +'<div class="key">See also: <a href="/bhakti/devi/devi-mahatmya/">The Devī Māhātmya series</a></div>'))
pages.append(page('sun','HER BOND WITH TRIPURASUNDARĪ','The Sun’s helper',facts([
 ('A modern story','A Hindi source retold by Kinsley: the sages gave Soma to the Sun; empowered by <b>Tripurasundarī</b>, the Sun made the three worlds'),
 ('Then','The Goddess “took an appropriate form and pervaded and directed the triple world”: that form is Bhuvaneśvarī'),
 ('So','Bhuvaneśvarī is Tripurasundarī as she governs the created world'),
 ('In Śrīvidyā','The two are worshipped side by side; hrīṃ belongs to both')])
 +'<div class="key">Previous: <a href="'+MVS+'tripurasundari/">Tripurasundarī</a></div>'))
pages.append(page('karnataka','KANNADA TĀYI','The Goddess of Karnataka',fig(560,180,'A golden goddess with a red and yellow flag beside her, the Hampi temple tower and the Mysore Palace dome in the background',
 '<rect width="560" height="180" fill="#fff4cd"/><g transform="translate(90 170)" stroke="#111" stroke-width="1.6">'+''.join(f'<rect x="{-40+k*4}" y="{-k*16-16}" width="{80-k*8}" height="16" fill="{"#e8d8b8" if k%2 else "#d8c8a8"}"/>' for k in range(7))+'</g>'
 +'<g transform="translate(470 170)" stroke="#111" stroke-width="2"><rect x="-60" y="-50" width="120" height="50" fill="#f2e6c8"/><path d="M-24 -50 q0 -40 24 -50 q24 10 24 50z" fill="#c9a26b"/></g>'+BHUV(280,110,.9)+'<g transform="translate(350 40)">'+FLAG+'</g>')+facts([
 ('Mother Kannada','Bhuvaneśvarī is revered as <b>Kannada Tāyi</b> or Nāḍa Devī, the deity of Kannada identity and of the state'),
 ('Vijayanagara','By tradition she blessed Harihara and Bukka in founding the empire; an image of her stands in the <b>Virūpākṣa</b> temple, Hampi'),
 ('Rājyotsava','On <b>1 November</b>, Karnataka’s formation day, her image is honoured across the state, including at the Vidhāna Saudha'),
 ('Official image','The state government has adopted an official image of Bhuvaneśvarī as Karnāṭaka Māte')])
 +talk("A Mahāvidyā is Karnataka's mother?","The Queen of the Worlds became the queen of one land too. Kannadigas call her Tāyi.")))
pages.append(page('mysuru','MYSURU AND BHUVANAGIRI','Her Karnataka temples',facts([
 ('Mysuru Palace','A Bhuvaneśvarī temple at the <b>north gate</b> of the palace fort, built in <b>1951</b> by Mahārāja <b>Jayacāmarājendra Woḍeyar</b>, matching the Varāhasvāmi temple on the south side'),
 ('Sūrya Maṇḍala','A copper Sun-disc moved from the palace into the temple by the Mahārāja'),
 ('Rājyotsava','On 1 November she is dressed in finery; in 2020 she received a new silver kavaca'),
 ('Bhuvanagiri','A 17th-century hilltop temple near Siddāpur, Uttara Kannaḍa: said to be the only one in Karnataka with daily worship of Bhuvaneśvarī, and the centre of Rājyotsava rites'),
 ('Hampi','The image in the Virūpākṣa complex is honoured but has no regular daily rites')])
 +'<div class="key">More Mysuru: <a href="/bhakti/temples-of-india/around-mysuru/">Temples around Mysuru</a></div>'))
pages.append(page('temples','ACROSS INDIA','Other shrines',facts([
 ('Kāmākhyā','Her temple crowns the Nīlācala hill above the main shrine'),
 ('Pudukkoṭṭai','A Bhuvaneśvarī temple in Tamil Nadu founded by Śrī Śāntānanda Svāmī'),
 ('Gondal, Gujarat','A dedicated temple founded in 1946'),
 ('Ernakulam, Kerala','Worshipped as Añcumana Devī'),
 ('Abroad','Temples in the USA and Australia'),
 ('Not Bhubaneswar','The Odisha city is named for Śiva as Tribhuvaneśvara (Liṅgarāja), not for her')])))
pages.append(page('festivals','THROUGH THE YEAR','Her days',facts([
 ('Navarātri','Both seasons; in Śrīvidyā homes she is honoured with Lalitā'),
 ('Bhuvaneśvarī Jayantī','Her own festival day in the lunar calendar'),
 ('Āḍi Pūram','The Tamil festival of the Goddess in Āḍi month'),
 ('1 November','Kannada Rājyotsava in Karnataka')])))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of space',facts([
 ('Spaciousness','Make room: in the mind, in the home, in the heart'),
 ('Sovereignty','The whole world is her kingdom, and we are her subjects and children'),
 ('Gentleness','Power need not frighten; the Queen of all worlds smiles'),
 ('Belonging','A land, a language, a people can be held as the Mother’s body')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Bhuvana','World'),('Īśvarī','Queen'),('Ākāśa','Space'),('Maṇidvīpa','Jewel island'),('Bīja','Seed syllable'),('Varada · Abhaya','Boon-giving · fear-not gestures'),('Tāyi','Mother (Kannada)'),('Rājyotsava','State formation day'),('Kavaca','Armour, covering')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Bhuvaneśvarī, Queen of the Worlds, fourth Mahāvidyā: the Goddess as space.</div>
<div><b>Form.</b> Golden, smiling, crescent-crowned, noose and goad, blessing hands.</div>
<div><b>Stories.</b> The Trimūrti at Maṇidvīpa; the Devī Gītā; Tripurasundarī governing the world.</div>
<div><b>Karnataka.</b> Kannada Tāyi: Hampi, Bhuvanagiri, the Mysuru Palace temple of 1951, Rājyotsava.</div>
<div><b>Lesson.</b> Make room; the room itself is holy.</div>
</div>'''+talk("One line to remember?","Everything you love needs space to exist. That space is her.")+'<div class="key">The fourth Great Wisdom: <b>Bhuvaneśvarī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Goddess:</b> Wikipedia, “Bhuvaneshvari” (fourth Mahāvidyā; Ādi Parāśakti in the Devī Bhāgavata; Maṇidvīpa; noose and goad; lion; festivals; bhūḥ, bhuvaḥ, svaḥ; Kinsley’s Sun myth tying her to Tripurasundarī; the Trimūrti and their śaktis; temples at Gondal, Ernakulam, Pudukkoṭṭai, abroad; state goddess of Karnataka; Bhuvanagiri). Devī Bhāgavata Purāṇa, Books 3 and 7 (Maṇidvīpa; Devī Gītā).</p>
<p><b>Karnataka:</b> The Hans India and Star of Mysore (Mysuru Palace temple, north gate, built 1951 by Jayacāmarājendra Woḍeyar; copper Sūrya Maṇḍala; silver kavaca 2020). Deccan Herald (Bhuvanagiri, 17th c., only daily worship; Hampi image without regular rites; Vijayanagara installation; Nāḍa Devī statue and official image). indianetzone (north side opposite Varāhasvāmi). newkerala (Rājyotsava at Vidhāna Saudha).</p>
<p><b>Sources differ:</b> details of the Trimūrti story between retellings; Vijayanagara founding legend (tradition). The Bhubaneswar note reflects the city’s usual etymology. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('form','Her Form'),('space','The Goddess of Space'),('manidvipa','Maṇidvīpa and the Trimūrti'),('devigita','The Devī Gītā'),('sun','Her Bond with Tripurasundarī'),
 ('karnataka','Kannada Tāyi'),('mysuru','Mysuru and Bhuvanagiri'),('temples','Across India'),('festivals','Through the Year'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 4 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,7vw,70px)">BHUVANEŚVARĪ</h1>
  <div class="series">DAŚA MAHĀVIDYĀ · A REFERENCE GUIDE</div>
  <div class="tag">Queen of the worlds, Mother of Kannada</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Kālī is time. The fourth Great Wisdom is <b>space</b>: <b>Bhuvaneśvarī</b>, Queen of the three worlds, the golden, smiling Mother in whom everything has room to be. In the Devī Bhāgavata, Brahmā, Viṣṇu and Śiva flew to her jewel island and came back knowing whose power they wielded.</p>
    <p>In Karnataka she is something more: <b>Kannada Tāyi</b>, Mother Kannada. Her image stands at Hampi; a Mahārāja built her a temple at the gate of the Mysuru Palace; every first of November the whole state honours her.</p>
    <p>This guide tells her stories, her meaning and her temples.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Bhuvaneśvarī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("The Goddess honoured on Kannada Rājyotsava is a Mahāvidyā?","The very same Bhuvaneśvarī. Few people know the Tantric Queen of the Worlds is also Kannada Tāyi.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms. Previous: <a href="{MVS}tripurasundari/">Tripurasundarī</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV04_Bhuvaneshvari.html','w').write(head+b+tail())
print('ok',len(pages))
