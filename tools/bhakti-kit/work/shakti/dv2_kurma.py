exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Kūrma · Daśāvatāra 2 · srini.presents','Kūrma, the tortoise, second avatāra of Viṣṇu: Durvāsa’s curse, the churning of the ocean of milk on Mount Mandara and the serpent Vāsuki, Śiva drinking the poison, the fourteen treasures, Lakṣmī’s return, Dhanvantari and the nectar, Mohinī, Rāhu and Ketu, the Kumbha Melā, the tortoise in the Gītā and yoga, and the Kūrma temples at Śrīkūrmam and Gavirangapura. An illustrated reference guide.')
def MOUNT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 0 L-6 -140 L6 -140 L30 0Z" fill="#8a7a6a"/><path d="M-26 -30 L26 -30 M-20 -70 L20 -70 M-14 -110 L14 -110" stroke="#5a4a3a"/></g>'
def ROPE(x1,x2,y): return f'<path d="M{x1} {y} q{(x2-x1)/4} -16 {(x2-x1)/2} 0 q{(x2-x1)/4} 16 {(x2-x1)/2} 0" stroke="#3a6a3a" stroke-width="8" fill="none"/>'
def CHURN(W=560,H=200):
    return (f'<rect width="{W}" height="{H}" fill="#eef7fb"/><rect y="{H-60}" width="{W}" height="60" fill="#f4f4f0"/>'+''.join(f'<path d="M{i*40} {H-50} q20 -8 40 0" stroke="#cfe8f6" stroke-width="2" fill="none"/>' for i in range(W//40+1))
      +AV(2,W/2,H-34,1.0)+MOUNT(W/2,H-50,.9)+ROPE(90,W-90,H-110)+''.join(person(x,H-80,'#3a3a5a','#5a7a5a',.6) for x in (50,90))+''.join(person(x,H-80,'#e0a800','#f2c79b',.6) for x in (W-90,W-50)))
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A great tortoise bearing a mountain in the ocean while gods and demons pull a serpent wound around it">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/><g transform="translate(-90 40)">'+CHURN(560,200)+'</g></svg>')
cov=cover_dv('DAŚĀVATĀRA 2 OF 10','KŪRMA',16,'The tortoise who held up the churning',art)
fw=foreword_dv('Keśava dhṛta-kacchapa-rūpa,',[
 'The second avatāra is a great tortoise at the bottom of the ocean, with a mountain on his back. The gods had lost their strength and their good fortune, and the only cure was the nectar of immortality hidden in the <b>ocean of milk</b>.',
 'To churn it, gods and demons used <b>Mount Mandara</b> as the churning rod and the serpent <b>Vāsuki</b> as the rope. But the mountain began to sink, until Viṣṇu came as <b>Kūrma</b> and took its weight. Out of the churning came poison, which Śiva drank, then fourteen treasures, Lakṣmī herself, and at last the nectar.',
 'This guide tells the whole story of the churning, and the tortoise in yoga, temples and the Gītā.'],
 'Why a tortoise?','Its shell is the strongest base there is. Something steady had to hold the world while it was stirred.',
 series_note_dv(2))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Avatāra','<b>Second</b> of the ten; Satya Yuga'),('Form','<b>A tortoise</b>; sometimes Viṣṇu above with a tortoise body'),
 ('Deed','Bears Mount Mandara on his back during the churning of the ocean of milk (Samudra Manthana)'),('Texts','Bhāgavata Purāṇa 8.5–8.11; Viṣṇu Purāṇa 1.9; Mahābhārata, Ādi Parva'),
 ('Vedic seed','Prajāpati takes the form of a tortoise in the Śatapatha Brāhmaṇa'),('Results','Lakṣmī returns; Dhanvantari brings the nectar; Śiva drinks the poison'),
 ('Temples','Śrīkūrmam (Andhra), Gavirangapura (Karnataka), Kurmai (Andhra)'),('Day','Kūrma Jayantī, Vaiśākha full moon')])
 +talk("The tortoise doesn't do much, does he?","He holds still while everything else whirls. Without him, nothing works.")))
pages.append(page('names','NAMES','Tortoise of the Lord',facts([
 ('Kūrma','Tortoise'),('Kacchapa','Another word for tortoise; Jayadeva’s: <i>dhṛta-kacchapa-rūpa</i>'),('Ākūpāra','The cosmic tortoise who bears the earth'),('Kūrmanātha','Lord Kūrma, at Śrīkūrmam'),('Samudra Manthana','“Churning of the ocean”'),('Kṣīrasāgara','The ocean of milk')])))
pages.append(page('curse','WHY THE GODS LOST EVERYTHING','Durvāsa’s garland',facts([
 ('The gift','The sage Durvāsa gave Indra a garland of divine flowers'),
 ('The insult','Indra placed it on his elephant Airāvata, who threw it to the ground'),
 ('The curse','Durvāsa cursed Indra and the gods to lose their Śrī: their fortune, strength and glory'),
 ('The result','Lakṣmī left them; the demons (asuras) defeated the weakened gods'),
 ('The plan','Viṣṇu told the gods to make peace with the demons and churn the ocean together for the nectar of immortality (amṛta)')])
 +talk("All that from dropping a garland?","Disrespect to a gift costs dearly in these stories. Fortune leaves where it is not honoured.")))
pages.append(page('churn','THE CHURNING','Mountain, serpent and tortoise',fig(560,200,'A tortoise bearing a mountain in the ocean, with demons pulling the serpent from one side and gods from the other',CHURN(560,200))+'''<div class="steps">
<div><b>The rod.</b> Mount Mandara was uprooted and carried to the ocean of milk.</div>
<div><b>The rope.</b> The great serpent Vāsuki was wound around it. The demons took the head end; the gods the tail.</div>
<div><b>The sinking.</b> As they began to churn, the mountain sank into the ocean floor.</div>
<div><b>Kūrma.</b> Viṣṇu became a vast tortoise, dived beneath the mountain and held it on his back. The churning went on for ages; in some tellings Viṣṇu also sat on top of the mountain to steady it.</div>
</div>'''))
pages.append(page('poison','THE POISON','Śiva becomes Nīlakaṇṭha',fig(560,170,'Shiva drinking dark poison from a cup while Parvati holds his throat, which turns blue',
 '<rect width="560" height="170" fill="#1d2a3a"/>'+SHIVA(300,100,.9)+'<path d="M260 60 q-30 -30 -60 -10" stroke="#3a1a5a" stroke-width="10" fill="none"/><circle cx="300" cy="72" r="6" fill="#3b6fd0" stroke="#111"/>'+GENTLE(400,110,.7))+facts([
 ('Hālāhala','The first thing churned up was a deadly poison that began to burn the worlds'),
 ('Śiva','At the gods’ plea, Śiva gathered it in his palm and drank it'),
 ('Pārvatī','She pressed his throat so it would not go down; it stayed there, turning his throat blue'),
 ('Name','He is Nīlakaṇṭha, “blue-throated”'),
 ('Lesson','Before any treasure comes up, someone must swallow the poison')])))
pages.append(page('treasures','THE FOURTEEN TREASURES','What the ocean gave',fig(560,150,'A row of treasures rising from the ocean: a white horse, a white elephant, a cow, a moon, a jewel and a goddess on a lotus',
 '<rect width="560" height="150" fill="#eef7fb"/>'+OCEAN(560,30,120,'#cfe8f6')+''.join(f'<circle cx="{40+i*60}" cy="70" r="24" fill="{c}" stroke="#111" stroke-width="2"/>' for i,c in enumerate(('#fff','#eee','#f4e6d0','#fff8c0','#e04040','#f08aa6','#e8d8b0','#2a9d6f','#ffd60a'))))+facts([
 ('Animals','Kāmadhenu the wish-cow; Uccaiḥśravas the white horse; Airāvata the white elephant'),
 ('Things','The Kaustubha jewel; the Pārijāta tree; the conch Pāñcajanya; the moon'),
 ('Beings','The apsaras; Vāruṇī, goddess of wine'),
 ('Lakṣmī','Rose on a lotus and chose Viṣṇu as her lord'),
 ('Dhanvantari','Last came the physician of the gods, holding the pot of amṛta'),
 ('Our note','The list of fourteen varies from text to text')])))
pages.append(page('mohini','MOHINĪ AND THE NECTAR','How the gods got immortality',facts([
 ('The grab','The demons seized the pot of nectar'),
 ('Mohinī','Viṣṇu appeared as Mohinī, an enchanting woman, and offered to share it fairly'),
 ('The trick','She served the gods first; the demons, charmed, waited'),
 ('Rāhu','One demon slipped into the gods’ line; the Sun and Moon pointed him out, and Viṣṇu’s discus cut off his head just as he drank'),
 ('Rāhu and Ketu','His immortal head became Rāhu, his body Ketu; they chase the Sun and Moon, causing eclipses')])
 +talk("So eclipses are a revenge story?","In the myth, yes. Rāhu never forgave the Sun and Moon.")+'<div class="key">See: <a href="/bhakti/temples-of-india/pancha-bhuta-sthalas/kalahastishvara/">Śrīkāḷahasti and its Rāhu–Ketu rites</a></div>'))
pages.append(page('kumbha','DROPS OF NECTAR','The Kumbha Melā',facts([
 ('The drops','As the nectar pot was carried away, drops fell at four places on earth'),
 ('Four cities','Prayāga, Haridvāra, Ujjain and Nāsik'),
 ('Kumbha Melā','Every twelve years the Kumbha Melā is held at each, in turn, when the planets are in a set position'),
 ('Largest','The Prayāga Mahā Kumbha draws tens of millions of pilgrims'),
 ('Kumbha','“Pot”: the pot of nectar')])
 +'<div class="key">See: <a href="/bhakti/temples-of-india/18-shakti-peethas/madhaveshwari-prayaga/">Prayāga</a></div>'))
pages.append(page('vedic','THE COSMIC TORTOISE','Older ideas',facts([
 ('Śatapatha Brāhmaṇa','Prajāpati takes the form of a tortoise to create living beings; kūrma is linked with kaśyapa, the sage-father of creatures'),
 ('Ākūpāra','The great tortoise that supports the world'),
 ('In ritual','A living tortoise was placed in the fire altar in some Vedic rites'),
 ('Foundation','Temple builders lay a kūrma-śilā, a tortoise stone, in foundations and below flag-staffs')])))
pages.append(page('yoga','THE TORTOISE IN THE GĪTĀ','Withdrawing the senses',facts([
 ('Gītā 2.58','The wise one draws the senses back from their objects as a tortoise draws in its limbs'),
 ('Pratyāhāra','This withdrawal is a stage of yoga in Patañjali’s system'),
 ('Kūrma-nāḍī','Yoga Sūtra 3.31: concentration on the “tortoise channel” brings steadiness'),
 ('Kūrmāsana','The tortoise pose in haṭha yoga')])
 +'<div class="panel reading"><p><i>yadā saṃharate cāyaṃ kūrmo ’ṅgānīva sarvaśaḥ, indriyāṇīndriyārthebhyas tasya prajñā pratiṣṭhitā</i></p><p class="small">“When, like a tortoise drawing in its limbs, one draws the senses back from their objects, one’s wisdom is steady.” Bhagavad Gītā 2.58</p></div>'))
pages.append(page('srikurmam','ŚRĪKŪRMAM','The great Kūrma temple',fig(560,170,'A temple by the sea with a tank and tortoises in a pen',
 '<rect width="560" height="170" fill="#fff4dc"/>'+TEMPLE(200,150,2.6)+'<rect x="330" y="120" width="180" height="40" fill="#cfe8f6" stroke="#111" stroke-width="2"/>'+''.join(AV(2,350+i*40,140,.3) for i in range(4)))+facts([
 ('Where','Śrīkūrmam village, Śrīkākuḷam district, Andhra Pradesh, near the Bay of Bengal'),
 ('Unique','The only known pre-14th-century temple dedicated to the Kūrma avatāra'),
 ('Sanctum','Both a tortoise image and Viṣṇu with Lakṣmī; the deity faces west'),
 ('History','Inscriptions begin in the 11th–12th centuries; re-established under the Eastern Gaṅga king Anantavarman Coḍagaṅga; Rāmānuja is linked to it'),
 ('Living tortoises','Kept in a dedicated part of the temple'),
 ('Murals','Old Odisha-style paintings line the circumambulatory hall')])))
pages.append(page('others','OTHER KŪRMA SHRINES','Karnataka and Andhra',facts([
 ('Gavirangapura','Śrī Gaviraṅganātha Svāmī temple, Chitradurga district, Karnataka, where Viṣṇu is worshipped as a tortoise'),
 ('Kurmai','Śrī Kūrma Varadarāja Svāmī temple, Chittoor district, Andhra Pradesh'),
 ('In other temples','Kūrma appears in Daśāvatāra panels everywhere, and tortoise images face many sanctums in South India'),
 ('Stamp','India Post issued a stamp of the Śrīkūrmam temple in 2013')])))
pages.append(page('festivals','THROUGH THE YEAR','His days',facts([
 ('Kūrma Jayantī','Vaiśākha Pūrṇimā (Apr–May), by common calendars'),
 ('Śrīkūrmam','The Dolotsavam (swing festival) draws large crowds'),
 ('Kumbha Melā','The festival of the nectar drops')])))
pages.append(page('meaning','WHAT KŪRMA TEACHES','The wisdom of the tortoise',facts([
 ('Be the base','Great work needs someone steady underneath'),
 ('Withdraw','Like the tortoise, draw in the senses to find calm'),
 ('Poison first','Every churning brings up poison before treasure'),
 ('Fortune needs respect','Lakṣmī leaves when gifts are despised')])
 +talk("What should I take from Kūrma?","When life is churning, be the tortoise: still, strong and underneath it all.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Kūrma · Kacchapa','Tortoise'),('Manthana','Churning'),('Amṛta','Nectar of immortality'),('Hālāhala','The world-burning poison'),('Mohinī','Viṣṇu’s enchanting female form'),('Dhanvantari','Physician of the gods'),('Pratyāhāra','Withdrawal of the senses'),('Kumbha','Pot')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Kūrma, the tortoise, second avatāra of Viṣṇu.</div>
<div><b>Story.</b> Gods and demons churn the ocean with Mandara and Vāsuki; Kūrma holds the mountain up.</div>
<div><b>Results.</b> Poison for Śiva, fourteen treasures, Lakṣmī, and the nectar shared by Mohinī.</div>
<div><b>Echoes.</b> Rāhu and Ketu, the Kumbha Melā, the Gītā’s tortoise; Śrīkūrmam.</div>
<div><b>Lesson.</b> Stay steady while the world churns.</div>
</div>'''+talk("One line to remember?","No nectar without a tortoise underneath.")+'<div class="key">Next: <a href="'+DVS+'varaha/">Varāha, the boar</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Bhāgavata Purāṇa 8.5–8.11; Viṣṇu Purāṇa 1.9; Mahābhārata, Ādi Parva 15–17; Śatapatha Brāhmaṇa 7.5.1.5; Bhagavad Gītā 2.58; Yoga Sūtra 3.31.</p>
<p><b>Temples:</b> Wikipedia, “Kurmanathaswamy temple, Srikurmam” (only pre-14th-century Kūrma temple; tortoise and Viṣṇu with Lakṣmī; inscriptions from 11th–12th c.; murals; 2013 stamp; Gavirangapura and Kurmai); Wikipedia, “Sri Kurmam” (Anantavarman Coḍagaṅga; Dolotsavam); Wikimedia Commons (living tortoises).</p>
<p><b>Sources differ / unverified:</b> the list of fourteen treasures; whether Viṣṇu also sat atop Mandara; the Kūrma Jayantī date; the claim that Śrīkūrmam is the “only” Kūrma temple (other shrines exist). Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('curse','Why the Gods Lost Everything'),('churn','The Churning'),('poison','The Poison'),('treasures','The Fourteen Treasures'),('mohini','Mohinī and the Nectar'),('kumbha','Drops of Nectar'),
 ('vedic','The Cosmic Tortoise'),('yoga','The Tortoise in the Gītā'),('srikurmam','Śrīkūrmam'),('others','Other Kūrma Shrines'),('festivals','Through the Year'),('meaning','What Kūrma Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV2_Kurma.html',head,cov,fw,pages,toc)
