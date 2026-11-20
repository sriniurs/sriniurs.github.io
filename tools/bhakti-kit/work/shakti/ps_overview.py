exec(open('/home/claude/work/shakti/ps_common.py').read())
head=head_navy('The Pañcabhūta Sthalas · Śiva’s Five Element Temples · srini.presents',
 'The Pañcabhūta Sthalas, Śiva’s five temples of the five elements: earth at Kāñcīpuram, water at Tiruvānaikkāval, fire at Tiruvaṇṇāmalai, air at Śrīkāḷahasti and space at Cidambaram. The five elements in the Upaniṣads, Śiva’s eight forms, a map, the “same longitude” claim, the Goddesses, the Tēvāram saints and the festivals. An illustrated reference guide.')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A Shiva linga at the centre, with five medallions around it for earth, water, fire, air and space">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+LINGA(190,200,1.5)
 +''.join(f'<circle cx="{x}" cy="{y}" r="30" fill="#fff8e7" stroke="#111" stroke-width="2"/>'+EL(k,x,y,.9) for k,x,y in (('earth',60,190),('water',80,80),('fire',190,46),('air',300,80),('space',320,190)))+'</svg>')
cov=cover('5 ELEMENTS · 5 TEMPLES','PAÑCABHŪTA STHALAS',13,'Śiva as earth, water, fire, air and space',art)
fw=foreword('Om Namaḥ Śivāya,',[
 'Everything you can touch is made of five things, say the old Indian thinkers: <b>earth, water, fire, air and space</b>. In the Tamil country and its northern edge, five great temples hold Śiva in each of these elements. Together they are the <b>Pañcabhūta Sthalas</b>, the five element shrines.',
 'At <b>Kāñcīpuram</b> he is a liṅga of sand. At <b>Tiruvānaikkāval</b> a spring wells up around him. At <b>Tiruvaṇṇāmalai</b> the whole hill is his column of fire. At <b>Śrīkāḷahasti</b> a lamp flickers in a windless room. At <b>Cidambaram</b> there is only an empty space and a garland of golden leaves.',
 'This guide explains the idea behind the five, shows where they are, and introduces each temple. Five detailed guides follow, one for each element.'],
 'Five temples, one God?','One Śiva, five ways to see him: in what you stand on, drink, cook with, breathe and live in.',
 series_note(nxt=('ekambareshvara','Ekāmbareśvara, Kāñcīpuram (earth)')))
pages=[]
pages.append(page('glance','AT A GLANCE','The five on one page','<table class="ct fact"><tr><td><b>Element</b></td><td><b>Temple · place · Goddess</b></td></tr>'+''.join(
 ('<tr><td>{EL_SVG}</td><td>'+f'<b>{k[1]} ({k[2].lower()})</b>: <a href="{PSS}{k[10]}/">{k[3]}</a>, {k[6]}, {k[7]} · {k[5]}</td></tr>').replace('{EL_SVG}',f'<svg width="54" height="54" viewBox="-27 -27 54 54">{EL(k[0],0,0,.9)}</svg>') for k in S5)+'</table>'
 +talk("Four in Tamil Nadu and one in Andhra?","Yes. Śrīkāḷahasti is just across the border, near Tirupati. All five sit in the old Tamil Śaiva world.")))
pages.append(page('elements','THE FIVE ELEMENTS','Pañca mahābhūta',facts([
 ('The idea','All matter is made of five “great elements” (mahābhūta): space, air, fire, water, earth'),
 ('Upaniṣad','The Taittirīya Upaniṣad (2.1) gives the order of creation: from the Self came space, from space air, from air fire, from fire water, from water earth'),
 ('Senses','Each element has its quality: space–sound, air–touch, fire–form, water–taste, earth–smell'),
 ('Sāṅkhya and Āyurveda','The same five build the body: bones and flesh are earth, blood water, digestion fire, breath air, the hollows space'),
 ('The sthalas','Each of the five temples makes one element the very body of Śiva')])
 +'<div class="panel reading"><p><i>tasmād vā etasmād ātmana ākāśaḥ sambhūtaḥ, ākāśād vāyuḥ, vāyor agniḥ, agner āpaḥ, adbhyaḥ pṛthivī</i></p><p class="small">“From this Self came space; from space, air; from air, fire; from fire, water; from water, earth.” Taittirīya Upaniṣad 2.1</p></div>'))
pages.append(page('ashtamurti','ŚIVA’S EIGHT FORMS','Aṣṭamūrti',fig(560,160,'Eight circles around Shiva: earth, water, fire, air, space, sun, moon and the worshipper',
 '<rect width="560" height="160" fill="#eef3fa"/>'+LINGA(280,140,.9)+''.join(f'<g>'+EL(k,x,y,.7)+'</g>' for k,x,y in (('earth',70,110),('water',130,60),('fire',210,36),('air',350,36),('space',430,60)))
 +'<circle cx="490" cy="110" r="16" fill="#ffd23f" stroke="#111" stroke-width="2"/><path d="M60 40 a14 14 0 1 0 14 18 a10 10 0 1 1 -14 -18z" fill="#fff8c0" stroke="#111" stroke-width="2"/>'+person(500,60,'#e08a2a','#f2c79b',.5),bg='#eef3fa')+facts([
 ('Aṣṭamūrti','The old Śaiva idea that Śiva has eight bodies: five elements, the sun, the moon and the sacrificer'),
 ('Kālidāsa','The opening verse of the <i>Abhijñānaśākuntalam</i> praises Śiva in these eight visible forms'),
 ('Śaṅkara','The Dakṣiṇāmūrti Stotram (v. 9) lists them: <i>bhūr ambhāṃsy analo ’nilo ’mbaram aharnātho himāṃśuḥ pumān</i>'),
 ('The sthalas','Five of the eight are given temples of their own')])
 +talk("So Śiva is not in the earth, he is the earth?","That's the Aṣṭamūrti view. The ground is one of his bodies.")))
pages.append(page('map','WHERE THEY ARE','Map of the five',fig(560,320,'Map of south India with the five element temples marked',SOUTHMAP(560,320))
 +facts([(f'{k[2]}',f'{k[6]}, {k[7]} · {k[8]:.2f}°N, {k[9]:.2f}°E') for k in S5])))
pages.append(page('longitude','THE “STRAIGHT LINE” CLAIM','Three temples on one meridian',facts([
 ('The claim','Popular posts say the five temples, or three of them, lie on one exact line of longitude'),
 ('What is true','Kāḷahasti (≈79.70°E), Kāñcīpuram (≈79.70°E) and Cidambaram (≈79.69°E) are within about 1–2 km of the same meridian'),
 ('What is not','Tiruvaṇṇāmalai (≈79.07°E) and Tiruvānaikkāval (≈78.71°E) lie well to the west'),
 ('Exaggerations','Claims of “exactly 79°41′ E” or “built with satellite precision” go beyond the evidence'),
 ('Our view','A striking coincidence for three of the five, worth noticing; no text claims it was planned')])
 +talk("So is it a mystery?","Three temples line up closely. That's a fun fact, not proof of ancient satellites.")))
pages.append(page('lingas','FIVE KINDS OF LIṄGA','What you actually see',facts([
 ('Earth · Kāñcī','A liṅga said to be made of sand, the Pṛthvī liṅga; it is not bathed with water'),
 ('Water · Tiruvānaikkāval','The Appu liṅga in a low sanctum where water seeps up from an underground spring'),
 ('Fire · Tiruvaṇṇāmalai','The Agni liṅga; the hill itself is worshipped as Śiva’s column of fire'),
 ('Air · Kāḷahasti','The Vāyu liṅga: a lamp beside it is said to flicker though no breeze enters'),
 ('Space · Cidambaram','The Ākāśa liṅga: an empty space behind a curtain, the “Cidambara Rahasyam”')])
 +talk("A liṅga that is not there?","At Cidambaram, yes. Space has no shape, so the sanctum shows nothing.")))
pages.append(page('goddesses','THE FIVE GODDESSES','Pārvatī in each',facts([(f'{k[6]}',f'<b>{k[5]}</b>'+{'earth':': Kāmākṣī worshipped the sand liṅga under the mango tree and held it in the flood','water':': she worshipped a liṅga made of water and became his student','fire':': “she whose breast was not suckled”; she won half of Śiva’s body here as Ardhanārīśvara','air':': “mother of the flower of wisdom”','space':': Śiva’s companion in the dance of bliss'}[k[0]]) for k in S5])
 +talk("Is Pārvatī always the one doing tapas?","In four of these stories, yes. She worships, he appears. The shrine marks the meeting.")))
pages.append(page('tevaram','THE TĒVĀRAM SAINTS','Sung by the Nāyaṉmārs',facts([
 ('Tēvāram','Hymns of three Tamil saints, Appar, Campantar (Sambandar) and Cuntarar (Sundarar), from the 7th–8th centuries'),
 ('Pāṭal Peṟṟa Talam','The 275 temples “that received a song”: all five Pañcabhūta Sthalas are among them'),
 ('Māṇikkavācakar','His <i>Tiruvācakam</i> is tied above all to Cidambaram'),
 ('Kaṇṇappar','The hunter-saint of Kāḷahasti is one of the 63 Nāyaṉmārs'),
 ('Koccheṅkaṭ Cōḻaṉ','The king of the Tiruvānaikkāval legend is also a Nāyaṉmār')])
 +'<div class="key">See also: <a href="'+JY+'">The 12 Jyotirliṅgas</a></div>'))
pages.append(page('compare','FIVE STHALAS AND TWELVE JYOTIRLIṄGAS','Two different lists',facts([
 ('Jyotirliṅgas','Twelve “liṅgas of light” across India, named in a Sanskrit hymn; Rāmeśvaram is the only one in Tamil Nadu'),
 ('Pañcabhūta','Five element shrines of the Tamil Śaiva tradition; none of them is a Jyotirliṅga'),
 ('Shared root','Both lists rest on Śiva as endless light: the Liṅgodbhava story belongs to Aruṇācala and to the Jyotirliṅgas'),
 ('Kāñcī','Also one of the 18 Śakti Pīṭhas, as Kāmākṣī'),
 ('Cidambaram','Also counted among the five halls where Śiva dances (Pañca Sabhai)')])
 +'<div class="key">Read: <a href="/bhakti/temples-of-india/18-shakti-peethas/kamakshi/">Kāmākṣī, Kāñcī</a></div>'))
pages.append(page('kings','WHO BUILT THEM','Pallavas to Nāyakas',tl([
 ('Legend','Koccheṅkaṭ Cōḻaṉ, an early Chola king, is credited with Tiruvānaikkāval'),
 ('7th–8th c.','Pallava Kāñcī; the Tēvāram saints sing all five shrines'),
 ('9th–10th c.','Chola kings Āditya I and Parāntaka I gild the roof of Cidambaram'),
 ('10th–13th c.','Cholas expand all five; stone inscriptions record their gifts'),
 ('1509–1529','Kṛṣṇadevarāya of Vijayanagara builds the tall gopurams of Kāñcī (1509) and Kāḷahasti (1516)'),
 ('16th–17th c.','Nāyaka rulers add halls and towers'),
 ('2010','Kāḷahasti’s Rāja Gopuram collapses; a new one is built')])))
pages.append(page('festivals','THROUGH THE YEAR','Their great days',facts([
 ('Kārttikai Dīpam','Tiruvaṇṇāmalai (Nov–Dec): the beacon on the hilltop'),
 ('Ārudrā Darśanam','Cidambaram (Dec–Jan) and Āni Tirumañjanam (Jun–Jul): Naṭarāja comes out'),
 ('Paṅkuṉi Uttiram','Kāñcīpuram (Mar–Apr): the wedding of Ekāmbaranātha and Kāmākṣī'),
 ('Mahāśivarātri','Kāḷahasti’s great festival (Feb–Mar)'),
 ('Paṅkuṉi Brahmotsavam','Tiruvānaikkāval; the noon pūjā by a priest dressed as the Goddess, daily')])))
pages.append(page('meaning','WHAT THEY TEACH','The wisdom of the five',facts([
 ('Earth','Patience and steadiness; Kāmākṣī held on through the flood'),
 ('Water','Flow and humility; the low doorway makes everyone bow'),
 ('Fire','Burning away ego; Brahmā and Viṣṇu could not find its end'),
 ('Air','Breath and life; a hunter offered his own eyes'),
 ('Space','Emptiness and freedom; the highest form is no form')])
 +talk("Which one is the most important?","Each tradition says its own. The idea is that you need all five, as the body does.")))
pages.append(page('series','THE FIVE GUIDES','Read on','<div class="steps">'+''.join(f'<div><b>{k[2]} · <a href="{PSS}{k[10]}/">{k[3]}, {k[6]}</a></b>: '+{'earth':'the sand liṅga, the mango tree with four branches, Kāmākṣī’s embrace and a tower 59 m tall.','water':'the spring in the sanctum, the spider and the elephant, the Chola king and the priest dressed as the Goddess.','fire':'the endless column of fire, the hill that is Śiva, Kārttikai Dīpam, Girivalam and Ramaṇa Maharṣi.','air':'the flickering lamp, the spider, snake and elephant, Kaṇṇappa’s eyes and the fallen tower.','space':'Naṭarāja’s dance, the secret of Cidambaram, the golden roof and the Dīkṣitars.'}[k[0]]+'</div>' for k in S5)+'</div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Bhūta','Element'),('Sthala · Talam','Sacred place'),('Pṛthvī · Āpas · Agni · Vāyu · Ākāśa','Earth · water · fire · air · space'),('Aṣṭamūrti','Śiva’s eight forms'),('Tēvāram','Tamil Śaiva hymns'),('Nāyaṉmār','The 63 Tamil Śaiva saints'),('Gopuram','Gateway tower'),('Girivalam','Walking around the hill')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Idea.</b> Five elements, five temples: Śiva as earth, water, fire, air and space.</div>
<div><b>Where.</b> Kāñcīpuram, Tiruvānaikkāval, Tiruvaṇṇāmalai, Śrīkāḷahasti, Cidambaram.</div>
<div><b>Roots.</b> The Taittirīya Upaniṣad’s order of creation; Śiva’s eight forms.</div>
<div><b>Saints.</b> All five sung in the Tēvāram.</div>
<div><b>Lesson.</b> The divine is in what you stand on, drink, cook with, breathe and live in.</div>
</div>'''+talk("One line to remember?","Look around you: five elements, and every one of them is Śiva.")+'<div class="key">Start with earth: <a href="'+PSS+'ekambareshvara/">Ekāmbareśvara, Kāñcīpuram</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Taittirīya Upaniṣad 2.1; Śaṅkara, Dakṣiṇāmūrti Stotram v. 9; Kālidāsa, <i>Abhijñānaśākuntalam</i> 1.1 (Aṣṭamūrti). Tēvāram (Appar, Campantar, Cuntarar); Māṇikkavācakar, <i>Tiruvācakam</i>.</p>
<p><b>Temples:</b> Wikipedia articles on Ekambareswarar Temple, Jambukeswarar Temple, Arunachalesvara Temple, Srikalahasteeswara Temple and Thillai Nataraja Temple; Incredible India (Kāñcī gopuram 1509; Kāḷahasti); The Hindu and Deccan Herald (Kāḷahasti collapse, 26 May 2010); Hinduism Today (Cidambaram 2014 Supreme Court ruling); Wikimedia note on the Chola gilding of the Cit Sabhā roof.</p>
<p><b>Coordinates:</b> approximate, from standard maps; the meridian comparison is our own arithmetic.</p>
<p><b>Sources differ / unverified:</b> the age of Kāñcī’s mango tree (2,500–3,500 years claimed; reports say the old trunk has died and a shoot from it is now tended); the date of Koccheṅkaṭ Cōḻaṉ; gopuram heights vary by source. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('elements','The Five Elements'),('ashtamurti','Śiva’s Eight Forms'),('map','Where They Are'),('longitude','The “Straight Line” Claim'),('lingas','Five Kinds of Liṅga'),('goddesses','The Five Goddesses'),('tevaram','The Tēvāram Saints'),
 ('compare','Sthalas and Jyotirliṅgas'),('kings','Who Built Them'),('festivals','Through the Year'),('meaning','What They Teach'),('series','The Five Guides'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/PS0_Pancha_Bhuta.html',head,cov,fw,pages,toc)
