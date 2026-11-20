exec(open('/home/claude/work/shakti/ps_common.py').read())
head=head_navy('Aruṇācaleśvara, Tiruvaṇṇāmalai · Pañcabhūta Sthala of Fire · srini.presents',
 'Aruṇācaleśvara (Aṇṇāmalaiyār) temple, Tiruvaṇṇāmalai: Śiva as fire (Agni liṅga), the endless column of light that Brahmā and Viṣṇu could not measure, the hill that is Śiva, Ardhanārīśvara, Kārttikai Dīpam, Girivalam and the eight liṅgas, the Hoysala king Vallāḷa, Aruṇagirinātar, and Ramaṇa Maharṣi. An illustrated reference guide.')
def HILLF(x,y,s=1,fire=True):
    f=EL('fire',0,-176,1.4) if fire else ''
    return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-170 0 L-60 -150 L0 -170 L60 -150 L170 0Z" fill="#8a5a3a"/><path d="M-60 -150 L0 -170 L60 -150 L30 -120 L-20 -130Z" fill="#a0704a"/>{f}</g>'
def COLUMN(x,y,h=240,w=50): return f'<g stroke="#111" stroke-width="2"><rect x="{x-w/2}" y="{y-h}" width="{w}" height="{h}" fill="#ff8c1a"/><rect x="{x-w/4}" y="{y-h}" width="{w/2}" height="{h}" fill="#ffd60a" stroke="none"/></g>'
def SWAN(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-20 0 q20 14 40 0 q-6 -14 -20 -10 q-2 -18 8 -24 l6 2 l-8 4 q-4 10 0 20" fill="#fff"/></g>'
def BOAR(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-26 0 q-2 -26 26 -26 q22 0 24 18 l8 4 l-8 4 q-4 4 -24 4z" fill="#5a4a4a"/><path d="M-20 0 v8 M10 0 v8" stroke-width="4"/><path d="M24 -6 q6 -6 2 -12" fill="none" stroke="#fff"/></g>'
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The Arunachala hill with a great flame on its peak and a tall temple tower at its foot">'
 '<rect width="380" height="268" fill="#2a0e0a" rx="8"/>'+STAR+HILLF(190,250,1.0)+GOPURAM(110,256,.8,'#e8d8b0',10)+GOPURAM(270,256,.55,'#e8d8b0',8)+'</svg>')
cov=cover('PAÑCABHŪTA 3 · FIRE','ARUṆĀCALEŚVARA',13,'Tiruvaṇṇāmalai: Śiva as fire',art)
fw=foreword('Aṇṇāmalaikku arōhara,',[
 'The third element burns. At <b>Tiruvaṇṇāmalai</b> Śiva is worshipped as <b>fire</b>, and the whole red hill of <b>Aruṇācala</b> is held to be his body. Here, the story says, he once stood as an endless column of flame that neither Brahmā nor Viṣṇu could measure.',
 'Every year on <b>Kārttikai Dīpam</b> a beacon is lit on the summit and seen for miles around. On full-moon nights tens of thousands walk barefoot around the hill. Below it spreads one of the largest temples in India, Aruṇācaleśvara, with towers raised by Hoysala and Vijayanagara kings. A sixteen-year-old boy came here in 1896 and stayed for life: <b>Ramaṇa Maharṣi</b>.',
 'This guide tells the stories of the column and the hill, the festival and the walk, and the saints of Aruṇācala.'],
 'A hill that is God?','Here the temple is at the foot, but the hill itself is the liṅga. People walk around it as they would a shrine.',
 series_note(prev=('jambukeshvara','Jambukeśvara, Tiruvānaikkāval (water)'),nxt=('kalahastishvara','Kāḷahastīśvara, Śrīkāḷahasti (air)')))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Element','<b>Fire</b> (Agni): the third Pañcabhūta Sthala'),
 ('Śiva as','<b>Aruṇācaleśvara</b> or <b>Aṇṇāmalaiyār</b>, Lord of the red hill'),
 ('Liṅga','The <b>Agni liṅga</b> in the temple, and the hill itself, about 800 m high, worshipped as Śiva'),
 ('Goddess','<b>Unnāmulai Ammaṉ</b> (Apītakucāmbā)'),
 ('Temple','About 10 hectares (25 acres); the eastern Rāja Gopuram is about 66 m tall'),
 ('Festival','<b>Kārttikai Dīpam</b> (Nov–Dec): the beacon on the summit'),
 ('Walk','<b>Girivalam</b>: about 14 km around the hill, barefoot, especially at full moon'),
 ('Saints','Aruṇagirinātar, Ramaṇa Maharṣi, and the Tēvāram poets')])
 +talk("Is this the biggest of the five?","It is one of the largest temples in India. And no other has a whole mountain as its liṅga.")))
pages.append(page('names','NAMES','The red hill',facts([
 ('Aruṇācala','<i>aruṇa</i> red, dawn-coloured + <i>acala</i> unmoving (mountain)'),
 ('Aṇṇāmalai','Tamil: <i>aṇṇā</i> unreachable + <i>malai</i> hill, the hill no one could reach the top of'),
 ('Tiruvaṇṇāmalai','The sacred Aṇṇāmalai: the town'),
 ('Unnāmulai','Tamil: “she whose breast was not suckled”'),
 ('Apītakucāmbā','The same name in Sanskrit'),
 ('Agni liṅga','The liṅga of fire')])
 +talk("Unreachable hill?","Because in the story no one could reach the top of the fire. The name keeps the story.")))
pages.append(page('column','THE ENDLESS COLUMN','Liṅgodbhava',fig(560,240,'A column of fire rising off the page, a swan flying up and a boar digging down',
 '<rect width="560" height="240" fill="#1d1040"/>'+COLUMN(280,240,240,60)+SWAN(370,40,1.4)+BOAR(190,210,1.3)+'<path d="M370 70 v-40" stroke="#fff" stroke-dasharray="4 4"/><path d="M190 190 v40" stroke="#fff" stroke-dasharray="4 4"/>')+'''<div class="steps">
<div><b>The quarrel.</b> Brahmā and Viṣṇu argued over which of them was the greater.</div>
<div><b>The column.</b> Between them blazed up a pillar of fire without beginning or end. Whoever found an end, they agreed, would be the greater.</div>
<div><b>The search.</b> Brahmā became a swan and flew up; Viṣṇu became a boar and dug down. Neither found the end.</div>
<div><b>The lie.</b> Brahmā claimed he had seen the top, and brought a falling ketakī flower as false witness. Śiva appeared from the column, praised Viṣṇu’s honesty, and cursed the lie.</div>
</div>'''))
pages.append(page('hill','THE FIRE BECOMES A HILL','Why the hill is Śiva',fig(560,190,'A column of fire cooling into a red hill',
 '<rect width="560" height="190" fill="#fde8d8"/>'+COLUMN(140,190,180,40)+'<path d="M190 100 h60" stroke="#111" stroke-width="3" marker-end="url(#a)"/><path d="M244 92 l10 8 l-10 8" fill="none" stroke="#111" stroke-width="3"/>'+HILLF(410,190,.8))+facts([
 ('The plea','The fire was too fierce for the world to bear; the gods asked Śiva to take a gentler form'),
 ('The hill','He cooled into the red hill of Aruṇācala, which keeps the fire within'),
 ('Older than mountains','Tradition calls it the oldest hill on earth; geologists do find very old rocks in this region'),
 ('Worship','Devotees bow to the hill, walk around it, and treat it as the liṅga itself'),
 ('The curses','Brahmā lost his worship in temples; the ketakī flower is not offered to Śiva')])
 +talk("So the beacon on Dīpam is the column again?","Exactly. Once a year the hill shows its fire.")))
pages.append(page('ardha','HALF OF ŚIVA','Ardhanārīśvara at Aruṇācala',fig(560,170,'A figure half Shiva and half Parvati',
 '<rect width="560" height="170" fill="#fdf1f6"/><g transform="translate(280 90)" stroke="#111" stroke-width="2"><path d="M-30 70 q-4 -66 30 -80 v80z" fill="#5b8fe0"/><path d="M0 -10 q34 14 30 80 h-30z" fill="#e05a8a"/><path d="M-16 -24 a16 16 0 0 1 16 -16 v32 a16 16 0 0 1 -16 -16z" fill="#5b8fe0"/><path d="M0 -40 a16 16 0 0 1 0 32z" fill="#f2c79b"/></g>')+facts([
 ('Her penance','Pārvatī did tapas at the foot of Aruṇācala'),
 ('The gift','Śiva gave her the left half of his body: he became Ardhanārīśvara, half woman'),
 ('Once a year','The Ardhanārīśvara image comes out on Kārttikai Dīpam, when the beacon is lit'),
 ('Meaning','Śiva and Śakti are one; neither is complete alone')])
 +talk("Half man, half woman?","Half Śiva, half Pārvatī. The Tamil hymns love this form.")))
pages.append(page('deepam','KĀRTTIKAI DĪPAM','The beacon on the summit',fig(560,210,'Crowds below a hill with a great flame burning on its peak at night',
 '<rect width="560" height="210" fill="#0b1030"/>'+STAR+HILLF(280,190,1.0)+''.join(f'<circle cx="{20+i*20}" cy="{200-(i%3)*3}" r="4" fill="#ffd60a"/>' for i in range(27)))+facts([
 ('When','Full moon of the Tamil month Kārttikai (Nov–Dec), at the end of a ten-day festival'),
 ('At dawn','Bharaṇi Dīpam: a lamp in the sanctum is used to light five lamps for the five elements, which are brought back together into one'),
 ('At dusk','As the Ardhanārīśvara image appears, the Mahā Dīpam is lit in a great vessel on the summit, fed with large quantities of ghee'),
 ('Seen','From far across the plain, and kept burning for several days'),
 ('Crowds','Reckoned in millions, among the largest gatherings in Tamil Nadu')])
 +talk("Five lamps made into one?","The five elements returning to their one source. The whole Pañcabhūta idea in one ritual.")))
pages.append(page('girivalam','GIRIVALAM','Walking around the hill',fig(560,200,'A dashed path circling a hill with eight small shrines around it',
 '<rect width="560" height="200" fill="#f4e6d0"/><ellipse cx="280" cy="100" rx="230" ry="84" fill="none" stroke="#111" stroke-width="2" stroke-dasharray="8 6"/>'+HILLF(280,140,.55,False)
 +''.join(f'<g>'+LINGA(280+230*__import__("math").cos(k*0.785-1.57),100+84*__import__("math").sin(k*0.785-1.57)+8,.22)+'</g>' for k in range(8)))+facts([
 ('Distance','About 14 km, done barefoot, clockwise, keeping the hill on the right'),
 ('When','Any day; above all at full moon and on Kārttikai Dīpam'),
 ('Eight liṅgas','The Aṣṭaliṅgas at the eight directions: Indra, Agni, Yama, Nirṛti, Varuṇa, Vāyu, Kubera and Īśāna'),
 ('Pace','Tradition says to walk slowly, “like a queen in her ninth month”, in silence or chanting'),
 ('Meaning','To circle the hill is to circle Śiva himself')])
 +talk("Why barefoot?","You're walking around God. Shoes come off, as at a sanctum door.")))
pages.append(page('smarana','LIBERATION BY REMEMBERING','Aruṇācala’s promise',facts([
 ('The verse','<i>darśanād abhrasadasi, jananāt kamalālaye, kāśyāṃ tu maraṇān muktiḥ, smaraṇād aruṇācale</i>'),
 ('Meaning','Liberation by seeing Cidambaram, by being born at Tiruvārūr, by dying at Kāśī, and by merely remembering Aruṇācala'),
 ('Why it matters','Of the four, Aruṇācala asks the least: only remembrance'),
 ('Ramaṇa','He loved to quote it')])
 +talk("Just thinking of it is enough?","That is the claim. The easiest of the four ways.")+'<div class="key">See also: <a href="'+PSS+'chidambaram/">Cidambaram</a> (liberation by seeing)</div>'))
pages.append(page('temple','THE TEMPLE','Four towers and five courtyards',fig(560,200,'A temple with a very tall eastern tower, three other towers and a pillared hall at the foot of a hill',
 '<rect width="560" height="200" fill="#fde8d8"/>'+HILLF(420,170,.7,False)+GOPURAM(150,196,.95,'#e8d8b0',11)+GOPURAM(300,196,.6,'#e8d8b0',8)+GOPURAM(400,196,.5,'#e8d8b0',7)+'<rect x="40" y="170" width="480" height="26" fill="none" stroke="#111" stroke-width="2"/>')+facts([
 ('Size','About 10 hectares; walls about 210 m on the east and west, 450–480 m on the north and south'),
 ('Rāja Gopuram','The eastern tower, about 66 m and eleven tiers, begun under Kṛṣṇadevarāya and completed by the Thanjavur Nāyaka Sevappa'),
 ('Other towers','Vallāḷa Mahārāja Gopuram; Kiḷi (parrot) Gopuram; the northern tower raised by the woman ascetic Ammaṇi Ammāḷ'),
 ('Inside','Five courtyards, a thousand-pillared hall and the underground Pātāla Liṅga shrine'),
 ('Oldest part','The main shrine of Aṇṇāmalaiyār; most of the rest is Chola to Nāyaka')])))
pages.append(page('vallala','THE HOYSALA KING','Vallāḷa and the son who was Śiva',facts([
 ('Who','Vīra Ballāḷa III, the last great Hoysala king of Karnataka, made Tiruvaṇṇāmalai his capital in the 14th century'),
 ('The tower','The Vallāḷa Mahārāja Gopuram is named after him'),
 ('The legend','He had no son to perform his funeral rites; Śiva promised to do it himself'),
 ('Every year','In the month of Māsi, Aruṇācaleśvara is taken in procession to perform the rites for Vallāḷa as his son'),
 ('Karnataka link','A Hoysala king of Karnataka remembered every year in a Tamil temple')])
 +talk("Śiva does a king's śrāddha?","Every year, the story says. A son's promise kept by God.")))
pages.append(page('arunagiri','THE PARROT TOWER','Aruṇagirinātar',fig(560,150,'A green parrot perched on a temple tower',
 '<rect width="560" height="150" fill="#e8f4e0"/>'+GOPURAM(280,150,.55,'#e8d8b0',8)+'<g transform="translate(330 30)" stroke="#111" stroke-width="2"><path d="M-10 14 q-6 -18 6 -24 q14 4 10 22 l-6 18z" fill="#2ac06f"/><path d="M2 -10 q8 -2 8 6 l-5 -1z" fill="#e04040"/></g>')+facts([
 ('Who','Aruṇagirinātar, a 15th-century poet of Tiruvaṇṇāmalai, devotee of Murugan'),
 ('Tiruppukaḻ','His great collection of songs to Murugan, still sung everywhere'),
 ('Turned back','Tradition says Murugan saved him when he tried to end his life by jumping from this tower'),
 ('The parrot','Legend says he took the form of a parrot; the Kiḷi Gopuram recalls it'),
 ('Shrine','A shrine of Murugan in the temple is tied to him')])))
pages.append(page('ramana','RAMAṆA MAHARṢI','The sage of Aruṇācala',fig(560,170,'A white-haired sage in a loincloth sitting before the red hill',
 '<rect width="560" height="170" fill="#fff4dc"/>'+HILLF(420,170,.6,False)+person(200,150,'#f4f4f4','#c98b5a',1)+'<path d="M186 104 q14 -12 28 0" stroke="#ddd" stroke-width="5" fill="none"/>')+facts([
 ('Arrival','Venkataraman, a boy of 16 from near Madurai, came to Tiruvaṇṇāmalai in 1896 after a sudden experience of the Self'),
 ('Pātāla Liṅga','He first sat in the underground shrine inside the temple, lost to the world'),
 ('The hill','He lived on Aruṇācala’s slopes, in Virūpākṣa cave and Skandāśramam, and never left it again'),
 ('Teaching','Self-inquiry: ask “Who am I?” and rest in the answer'),
 ('Hymns','He wrote five hymns to Aruṇācala, including the <i>Akṣaramaṇamālai</i>'),
 ('Died','1950; his āśrama at the foot of the hill draws seekers from all over the world')])))
pages.append(page('saints','OTHER SAINTS AND POETS','A hill of holy people',facts([
 ('Tēvāram','Appar and Campantar sang Aṇṇāmalai'),
 ('Māṇikkavācakar','Tradition says he composed the <i>Tiruvempāvai</i> here, sung in Mārkaḻi'),
 ('Guhai Namaśivāya','A 16th-century saint who lived in a cave on the hill'),
 ('Śeṣādri Svāmī','A saint of the town, contemporary of Ramaṇa'),
 ('Today','Many āśramas and seekers line the Girivalam path')])))
pages.append(page('festivals','THROUGH THE YEAR','Its great days',facts([
 ('Kārttikai Dīpam','Nov–Dec: ten days ending with the beacon'),
 ('Every full moon','Girivalam crowds'),
 ('Māsi Magam','Feb–Mar: the rites for Vallāḷa'),
 ('Tiruvūḍal','In Tai (Jan): a festival of the divine couple’s quarrel and reunion'),
 ('Mahāśivarātri','Night-long worship of the liṅga')])))
pages.append(page('meaning','WHAT FIRE TEACHES','The wisdom of the flame',facts([
 ('Humility','Neither Brahmā nor Viṣṇu could find the end'),
 ('Honesty','Viṣṇu admitted failure and was praised; Brahmā lied and was cursed'),
 ('Union','Śiva gave half of himself to Śakti here'),
 ('Inner fire','Ramaṇa’s question, “Who am I?”, burns away the ego')])
 +talk("What should I take from fire?","Admit what you can't measure. And let the fire burn what isn't you.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Aruṇa · Acala','Red · mountain'),('Liṅgodbhava','Śiva emerging from the liṅga of fire'),('Ketakī','Screw-pine flower'),('Dīpam','Lamp'),('Girivalam','Walking around the hill'),('Aṣṭaliṅga','Eight liṅgas of the eight directions'),('Pātāla','Underground'),('Ardhanārīśvara','Half-woman Lord')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Element.</b> Fire: the Agni liṅga, and the whole red hill of Aruṇācala.</div>
<div><b>Story.</b> The endless column that Brahmā and Viṣṇu could not measure.</div>
<div><b>Rites.</b> Kārttikai Dīpam on the summit; the 14 km Girivalam.</div>
<div><b>People.</b> Pārvatī as half of Śiva; Vallāḷa; Aruṇagirinātar; Ramaṇa.</div>
<div><b>Lesson.</b> Be honest about what you cannot measure.</div>
</div>'''+talk("One line to remember?","Just remembering Aruṇācala is enough, they say. Now you will.")+'<div class="key">Next element, air: <a href="'+PSS+'kalahastishvara/">Kāḷahastīśvara</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Arunachalesvara Temple” (Agni liṅga; area; walls; four gopurams; Rāja Gopuram; Vallāḷa and Kiḷi gopurams; Ammaṇi Ammāḷ; Tēvāram); Wikipedia, “Tiruvannamalai” (Girivalam 14 km; Aṣṭaliṅgas); Simple Wikipedia and Deccan Chronicle (Kārttikai Dīpam; Unnāmulai Ammaṉ); religionworld.in (Ardhanārīśvara on Dīpam).</p>
<p><b>Saints:</b> Ramanasramam publications; Aruṇagirinātar’s <i>Tiruppukaḻ</i>; Māṇikkavācakar’s <i>Tiruvācakam</i> (Tiruvempāvai). The “smaraṇād aruṇācale” verse is traditional (Skanda Purāṇa, Aruṇācala Māhātmya, as commonly cited).</p>
<p><b>Sources differ / unverified:</b> hill height (about 800–814 m); gopuram height (66 m or “216 ft”); the amount of ghee for the beacon; crowd numbers; the Vallāḷa rite’s details; the Aruṇagirinātar parrot legend; Ramaṇa’s hymn count follows his collected works. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('column','The Endless Column'),('hill','The Fire Becomes a Hill'),('ardha','Half of Śiva'),('deepam','Kārttikai Dīpam'),('girivalam','Girivalam'),('smarana','Liberation by Remembering'),
 ('temple','The Temple'),('vallala','The Hoysala King'),('arunagiri','The Parrot Tower'),('ramana','Ramaṇa Maharṣi'),('saints','Other Saints and Poets'),('festivals','Through the Year'),('meaning','What Fire Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/PS3_Arunachaleshvara.html',head,cov,fw,pages,toc)
