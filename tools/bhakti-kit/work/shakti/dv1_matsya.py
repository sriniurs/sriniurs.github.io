exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Matsya · Daśāvatāra 1 · srini.presents','Matsya, the fish, first avatāra of Viṣṇu: the Śatapatha Brāhmaṇa flood and Manu, the Matsya Purāṇa and Bhāgavata versions, the little fish that outgrew every pot, the ship tied to its horn, the stolen Vedas and Hayagrīva, Matsya in art, the Vedanārāyaṇa temple at Nāgalāpuram and its sun festival, and other flood stories. An illustrated reference guide.')
def BOAT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-60 0 h120 l-20 22 h-80z" fill="#a0703a"/><path d="M0 0 v-50" stroke-width="3"/><path d="M0 -50 l36 30 h-36z" fill="#f4f0e0"/>'+''.join(person(dx,-2,'#e08a2a','#c98b5a',.35) for dx in (-40,-24,24,40))+'</g>'
def BIGFISH(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-90 0 q60 -50 130 0 q-70 50 -130 0z" fill="#e0a800"/><path d="M40 0 l40 -30 v60z" fill="#e0a800"/><circle cx="-62" cy="-8" r="5" fill="#fff"/><path d="M-80 -18 l-10 -30 l14 4z" fill="#bbb"/>'+''.join(f'<path d="M{a} -22 q8 22 0 44" fill="none" stroke="#b08000"/>' for a in (-30,-10,10))+'</g>'
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A great golden horned fish towing a boat by a rope tied to its horn over a stormy ocean">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/><g>'+OCEAN(380,90,178,'#1d5f9a')+'</g>'+BIGFISH(150,200,1.0)+'<path d="M60 172 q60 -60 180 -30" stroke="#c9a26b" stroke-width="3" fill="none"/>'+BOAT(290,168,1.0)+''.join(f'<path d="M{20+i*60} 40 l-10 20 h10 l-8 18" stroke="#ffd60a" stroke-width="3" fill="none"/>' for i in (0,5))+'</svg>')
cov=cover_dv('DAŚĀVATĀRA 1 OF 10','MATSYA',16,'The fish who saved the world',art)
fw=foreword_dv('Keśava dhṛta-mīna-śarīra,',[
 'The first avatāra begins with a tiny fish in a man’s cupped hands. “Protect me,” it says, “and I will protect you.” The man is <b>Manu</b>, father of humankind; the fish is <b>Matsya</b>, Viṣṇu himself.',
 'It grows too big for a pot, a pond, a lake and a river, and then it warns of a flood that will drown the world. Manu builds a ship and fills it with the seeds of life and the seven sages; the great horned fish tows it through the storm to safety. In later tellings Matsya also rescues the Vedas from a demon who stole them.',
 'This guide follows the story from the oldest Vedic prose to the Purāṇas, and to the temple where the sun touches the fish-god’s feet.'],
 'Is this like Noah’s ark?','Many cultures remember a great flood. India’s version has a fish as the saviour.',
 series_note_dv(1))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Avatāra','<b>First</b> of the ten; Satya Yuga'),('Form','<b>A fish</b>, often golden and horned; in temples a fish below, Viṣṇu above'),
 ('Saves','Manu, the seven sages, the seeds of all life, and the Vedas'),('Oldest text','Śatapatha Brāhmaṇa 1.8.1'),
 ('Purāṇas','Matsya Purāṇa, Bhāgavata Purāṇa (8.24), Agni Purāṇa'),('Enemy','Hayagrīva (or Śaṅkhāsura), the demon who stole the Vedas, in later versions'),
 ('Temple','Vedanārāyaṇa at Nāgalāpuram, Andhra Pradesh'),('Day','Matsya Jayantī, in Caitra')])
 +talk("The first avatāra is a fish?","Life began in water, and so does the story. The smallest creature saves everything.")))
pages.append(page('names','NAMES','Fish of the Lord',facts([
 ('Matsya','Fish'),('Mīna','Another word for fish; Jayadeva uses it: <i>dhṛta-mīna-śarīra</i>, “taking the body of a fish”'),
 ('Matsya-Nārāyaṇa','Viṣṇu as the fish'),('Vedanārāyaṇa','“Nārāyaṇa of the Vedas”, for recovering them'),('Ekaśṛṅga','“One-horned”, for the horn the ship was tied to'),('Śaphara','A small fish: how he first appears')])))
pages.append(page('brahmana','THE OLDEST TELLING','Śatapatha Brāhmaṇa 1.8.1',fig(560,170,'A man washing his hands at dawn finds a tiny fish in the water',
 '<rect width="560" height="170" fill="#fff4dc"/><circle cx="470" cy="50" r="26" fill="#ffd60a" stroke="#111" stroke-width="2"/>'+person(240,150,'#f4f4f4','#c98b5a',1.1)+'<path d="M270 110 q20 10 40 0" stroke="#c98b5a" stroke-width="8" fill="none"/>'+AV(1,292,106,.25)+'<rect x="280" y="120" width="40" height="10" fill="#5ab0f0" stroke="#111"/>')+'''<div class="steps">
<div><b>Morning water.</b> As Manu washed his hands, a little fish came into them. “Rear me,” it said, “and I will save you.”</div>
<div><b>Pot, trench, sea.</b> Manu kept it in a jar; when it outgrew that, in a trench; when it was a great fish, he took it to the sea.</div>
<div><b>The warning.</b> The fish told him the year of a coming flood, and told him to build a ship.</div>
<div><b>The horn.</b> When the flood rose, Manu tied the ship to the fish’s horn, and it drew him over the northern mountain. The place where the ship came down is called <i>Manor avasarpaṇam</i>, “Manu’s descent”.</div>
</div>'''+talk("No Viṣṇu in this version?","Not by name. Later the Purāṇas reveal that the fish was Viṣṇu.")))
pages.append(page('purana','THE PURĀṆA VERSION','Satyavrata and the growing fish',fig(560,170,'A fish shown growing in a cup, a pot, a pond and an ocean',
 '<rect width="560" height="170" fill="#eef3fa"/>'+''.join(f'<rect x="{x}" y="{150-h}" width="{w}" height="{h}" fill="#5ab0f0" stroke="#111" stroke-width="2"/>'+AV(1,x+w//2,150-h//2,sc) for x,w,h,sc in ((30,40,30,.18),(100,70,50,.3),(200,120,80,.5),(350,190,130,.95))))+facts([
 ('The king','Satyavrata, a royal sage, later the Manu of our age (Vaivasvata Manu)'),
 ('The river','He found the fish while offering water in the Kṛtamālā river in the south'),
 ('Ever larger','Cup, pot, well, lake, river, ocean: each time the fish grew to fill it'),
 ('The recognition','The king knew no ordinary fish could do this, and the Lord revealed himself'),
 ('The flood','In seven days the three worlds would sink; a ship would come for him')])))
pages.append(page('ship','THE SHIP OF SEEDS','Riding out the flood',fig(560,190,'A horned golden fish towing a boat with sages through a storm',
 '<rect width="560" height="190" fill="#1d2a4a"/>'+OCEAN(560,80,110,'#1d5f9a')+BIGFISH(180,140,.9)+'<path d="M100 120 q90 -60 210 -10" stroke="#3a6a3a" stroke-width="5" fill="none"/>'+BOAT(390,118,1.0))+facts([
 ('Aboard','Manu, the seven sages (saptarṣi), and seeds of every plant and creature'),
 ('The rope','In the Bhāgavata, the serpent Vāsuki served as the rope tied to the fish’s horn'),
 ('The teaching','Through the flood, Matsya taught Manu: this is said to be the Matsya Purāṇa'),
 ('After','When the waters fell, Manu began the new human race; we are “mānava”, children of Manu')])
 +talk("So humans are named after Manu?","Mānava, manuṣya: yes, the words for human come from his name.")))
pages.append(page('vedas','THE STOLEN VEDAS','Hayagrīva',facts([
 ('The theft','At the end of an age, as Brahmā slept, the demon Hayagrīva stole the Vedas from his mouth and hid in the ocean'),
 ('The rescue','Matsya killed the demon and returned the Vedas to Brahmā'),
 ('Another name','Some versions call the demon Śaṅkhāsura, who hid in a conch'),
 ('Two Hayagrīvas','Not to be confused with Hayagrīva, the horse-headed form of Viṣṇu who is himself a god of learning'),
 ('Meaning','Knowledge is the most precious thing to save from a flood')])
 +'<div class="panel reading"><p><i>pralaya-payodhi-jale dhṛtavān asi vedam, vihita-vahitra-caritram akhedam; keśava dhṛta-mīna-śarīra jaya jagadīśa hare</i></p><p class="small">Jayadeva, Gītagovinda 1.5: “In the waters of dissolution you held the Veda like a ship, untiring. Keśava, in the body of a fish, victory, Lord of the world!”</p></div>'))
pages.append(page('icon','MATSYA IN ART','How he is shown',fig(560,180,'Vishnu with four arms rising from the body of a fish',
 '<rect width="560" height="180" fill="#eef3fa"/>'+OCEAN(560,40,140)+'<g transform="translate(280 140)" stroke="#111" stroke-width="2"><path d="M-30 0 q60 -30 100 0 q-40 30 -100 0z" fill="#e0a800"/><path d="M70 0 l26 -20 v40z" fill="#e0a800"/></g>'+VISHNU(270,92,.8))+facts([
 ('As a fish','A great fish, sometimes horned, towing a boat'),
 ('Half and half','Upper body of four-armed Viṣṇu with conch and discus, lower body a fish'),
 ('With Hayagrīva','Shown slaying the demon and handing back the Vedas'),
 ('On gopurams','First in every row of the Daśāvatāra')])))
pages.append(page('purana-text','THE MATSYA PURĀṆA','A whole Purāṇa named for him',facts([
 ('One of 18','The Matsya Purāṇa is one of the eighteen Mahāpurāṇas'),
 ('Frame','Told by the fish to Manu during the flood'),
 ('Contents','Creation, genealogies of kings, vows and pilgrimages'),
 ('Art','It has chapters on temple building and image-making, studied by art historians'),
 ('Dates','Parts are thought to be among the older Purāṇic layers')])))
pages.append(page('temple','VEDANĀRĀYAṆA, NĀGALĀPURAM','The fish-god’s temple',fig(560,170,'Sun rays travelling through a temple corridor to reach the sanctum',
 '<rect width="560" height="170" fill="#fff4dc"/><circle cx="40" cy="60" r="26" fill="#ffd60a" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M66 {54+i*6} L470 {110+i*4}" stroke="#ffd60a" stroke-width="2"/>' for i in range(3))+GOPURAM(200,160,.5,'#e8d8b0',7)+'<rect x="440" y="80" width="90" height="80" fill="#d8c49a" stroke="#111" stroke-width="2"/>'+AV(1,485,120,.4))+facts([
 ('Where','Nāgalāpuram, Tirupati district, Andhra Pradesh, about 70 km from Tirupati'),
 ('Deity','Vedanārāyaṇa: Viṣṇu with a fish’s tail, with Śrīdevī and Bhūdevī'),
 ('Builder','Tradition credits Kṛṣṇadevarāya, who named the town after his mother Nāgāmbā'),
 ('Sūrya Pūjā','For a few days each year the setting sun’s rays travel down the temple and touch the deity, from the feet upwards'),
 ('Managed by','Tirumala Tirupati Devasthanams')])))
pages.append(page('floods','FLOODS AROUND THE WORLD','Comparisons',facts([
 ('Mesopotamia','The flood in the Epic of Gilgamesh, with Utnapishtim and his boat'),
 ('Bible','Noah’s ark in Genesis'),
 ('Greece','Deucalion and Pyrrha'),
 ('India','Manu and the fish'),
 ('Difference','In India the saviour is God as a creature, and what is saved is life and knowledge together')])
 +talk("Did they borrow from each other?","Scholars debate it. A great flood is a memory many peoples share.")))
pages.append(page('festivals','THROUGH THE YEAR','His days',facts([
 ('Matsya Jayantī','Caitra Śukla Tṛtīyā (Mar–Apr), by common calendars'),
 ('Nāgalāpuram','Brahmotsavam, Vaikuṇṭha Ekādaśī, and the Sūrya Pūjā (around March)'),
 ('Onam','Day one of the avatāra decorations at Tṛkkākara')])))
pages.append(page('meaning','WHAT MATSYA TEACHES','The wisdom of the fish',facts([
 ('Protect the small','A tiny fish turned out to be God'),
 ('Prepare','Manu listened and built the ship'),
 ('Save what matters','Seeds of life and seeds of knowledge'),
 ('Growth','What we nurture can outgrow every container')])
 +talk("What should I take from Matsya?","Look after the small things. One of them may carry you through the flood.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Matsya · Mīna','Fish'),('Manu','Father of humankind'),('Pralaya','Dissolution, deluge'),('Saptarṣi','Seven sages'),('Brāhmaṇa','Vedic prose text'),('Mānava','Human, descendant of Manu'),('Śṛṅga','Horn'),('Jayantī','Birthday')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Matsya, the fish, first avatāra of Viṣṇu.</div>
<div><b>Story.</b> A tiny fish grows huge, warns Manu of the flood and tows his ship by its horn.</div>
<div><b>Saved.</b> Manu, the sages, the seeds of life, the Vedas.</div>
<div><b>Texts and temple.</b> Śatapatha Brāhmaṇa, Matsya Purāṇa; Nāgalāpuram.</div>
<div><b>Lesson.</b> Protect the small; prepare for the flood.</div>
</div>'''+talk("One line to remember?","The first saviour was the size of a finger.")+'<div class="key">Next: <a href="'+DVS+'kurma/">Kūrma, the tortoise</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Śatapatha Brāhmaṇa 1.8.1 (Manu, fish, ship, northern mountain); Bhāgavata Purāṇa 8.24 (Satyavrata, Kṛtamālā, Vāsuki, Hayagrīva); Matsya Purāṇa 1–2; Jayadeva, Gītagovinda 1.5.</p>
<p><b>Temple:</b> Wikipedia, “Vedanarayana Temple, Nagalapuram” (Matsya form; TTD; Sūrya Pūjā); Wikipedia, “Nagalapuram” (Kṛṣṇadevarāya and Nāgāmbā; deity with consorts, facing west).</p>
<p><b>Sources differ / unverified:</b> the demon’s name (Hayagrīva or Śaṅkhāsura); the Matsya Jayantī date; exact Sūrya Pūjā days; comparisons with other flood myths are given for interest only. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('brahmana','The Oldest Telling'),('purana','The Purāṇa Version'),('ship','The Ship of Seeds'),('vedas','The Stolen Vedas'),('icon','Matsya in Art'),('purana-text','The Matsya Purāṇa'),
 ('temple','Vedanārāyaṇa, Nāgalāpuram'),('floods','Floods Around the World'),('festivals','Through the Year'),('meaning','What Matsya Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV1_Matsya.html',head,cov,fw,pages,toc)
