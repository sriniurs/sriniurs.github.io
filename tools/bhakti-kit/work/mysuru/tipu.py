import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
import common_t
def head_navy(title,desc):
    h=open(common_t.SRC).read(); hd=h[:h.find('<div class="book">')]
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
head=head_navy('Tipu Sultan and the Temples around Mysuru · srini.presents',
 'Tipu Sultan and the temples around Mysuru, from the record: gifts and grants to Śrīraṅgapaṭṭaṇa, Nañjanagūḍu, Kalale and Melukōṭe; Śṛṅgeri’s letters; Biḷigiri and Karighaṭṭa; and the disputed memories of Melukōṭe and the Masjid-i-Ala. Both sides, with sources.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def TEMPLE(x,y,s=1,c='#f2e6c8'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="{c}"/><path d="M-14 -16 h28 l-4 -10 h-20z M-10 -26 h20 l-4 -10 h-12z" fill="#e2cfa8"/><circle cy="-40" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def MOSQUE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-24" y="-20" width="48" height="20" fill="#f6f1e2"/><path d="M-14 -20 q14 -22 28 0z" fill="#e2e2d8"/><rect x="-34" y="-50" width="8" height="50" fill="#f6f1e2"/><rect x="26" y="-50" width="8" height="50" fill="#f6f1e2"/><path d="M-34 -50 l4 -8 l4 8 M26 -50 l4 -8 l4 8" fill="#e2e2d8"/></g>'
def CUP(x,y,s=1,c='#d8dde3'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-16 -30 h32 q-2 26 -16 28 q-14 -2 -16 -28z" fill="{c}"/><rect x="-3" y="-2" width="6" height="8" fill="{c}"/><rect x="-12" y="6" width="24" height="5" fill="{c}"/><path d="M-10 -24 q10 6 20 0" fill="none" stroke="#fff" stroke-width="2"/></g>'
def SCROLL(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-34" y="-44" width="68" height="80" fill="#fdf3d8"/><rect x="-40" y="-50" width="80" height="10" rx="5" fill="#c9a26b"/><rect x="-40" y="34" width="80" height="10" rx="5" fill="#c9a26b"/>'+''.join(f'<path d="M-24 {-28+i*10} h{40+(i%3)*6}" stroke="#7a5a2a" stroke-width="2"/>' for i in range(6))+'<circle cx="18" cy="24" r="7" fill="#c0392b"/></g>'
def TIGER(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle r="26" fill="#ff9f1c"/><path d="M-26 -6 l10 2 M-26 6 l10 0 M26 -6 l-10 2 M26 6 l-10 0 M-6 -26 l2 10 M6 -26 l-2 10" stroke-width="4"/><circle cx="-9" cy="-4" r="3" fill="#111"/><circle cx="9" cy="-4" r="3" fill="#111"/><path d="M-6 8 l6 4 l6 -4" fill="#fff"/><path d="M-20 -22 l-6 -10 l12 4z M20 -22 l6 -10 l-12 4z" fill="#ff9f1c"/></g>'
def FORT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-60" y="-30" width="120" height="30" fill="#c9a26b"/>'+''.join(f'<rect x="{-60+i*20}" y="-38" width="10" height="8" fill="#c9a26b"/>' for i in range(7))+'<path d="M-10 0 v-18 a10 10 0 0 1 20 0 v18z" fill="#5a3a1a"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A fort wall on a river island with a temple tower and a mosque rising behind it, silver temple cups and a royal letter in front, and a tiger emblem">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/><circle cx="310" cy="56" r="30" fill="#ffd166" opacity=".35"/>'
 '<path d="M0 214 q190 -22 380 0 V268 H0z" fill="#4aa3df"/>'+TEMPLE(130,150,1.6)+MOSQUE(250,150,1.4)+FORT(190,206,1.6)
 +CUP(60,250,.9)+CUP(100,252,.8)+SCROLL(320,226,.6)+TIGER(60,56,.9)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Who','<b>Tipu Sultan</b> (1751–1799), ruler of Mysuru from <b>1782</b> to <b>1799</b>, son of Hyder Ali; capital <b>Śrīraṅgapaṭṭaṇa</b>'),
 ('Gifts on record','Silver to <b>Raṅganātha</b> of Śrīraṅgapaṭṭaṇa; a jewelled cup and a green liṅga to <b>Nañjanagūḍu</b>; silver to <b>Kalale</b>; a decree and vessels at <b>Melukōṭe</b>'),
 ('Grants','About <b>156</b> temples on his grant lists; <b>34</b> endowment deeds (sanads) between 1782 and 1799'),
 ('Letters','About <b>30</b> Kannada letters to the <b>Śṛṅgeri</b> Śaṅkarācārya, found in <b>1916</b>'),
 ('Names','<b>Hakīm Nañjuṇḍa</b> at Nañjanagūḍu; “Raṅganātha” at <b>Biḷigiri</b>'),
 ('Battlefield','<b>Karighaṭṭa</b> hill in the siege of <b>1792</b>'),
 ('Disputed memories','The <b>Melukōṭe</b> killings remembered on Naraka Caturdaśī; the temple claim at the <b>Masjid-i-Ala</b>'),
 ('This guide','Gives the record and the disputes side by side, with sources, and leaves the verdict to you')])
 +talk("Was Tipu a friend of temples or an enemy?","That's the big fight, Zappy. Historians still argue. Let's look at the record, temple by temple, and keep both sides on the table.")))
pages.append(page('who','WHO WAS TIPU SULTAN?','The Tiger of Mysore, in brief',tl([
 ('1751','Born on 1 December at Devanahalli, son of <b>Hyder Ali</b>, the general who took power in the Woḍeyar kingdom of Mysuru.'),
 ('1782','Becomes ruler after Hyder Ali’s death in December; rules from <b>Śrīraṅgapaṭṭaṇa</b>.'),
 ('1780s–90s','Wars with the British East India Company, the Marāṭhās and the Nizām: the Second, Third and Fourth Anglo-Mysore Wars.'),
 ('1792','Siege of Śrīraṅgapaṭṭaṇa; by the <b>Treaty of Seringapatam</b> he gives up half his territory.'),
 ('1799','Killed on <b>4 May</b> defending the fort in the final siege. The British restore the Woḍeyars; <b>Pūrṇayya</b> becomes Dīvān.')])
 +'''<div class="panel reading"><p><b>The emblem.</b> Tipu used the tiger as his symbol everywhere: on his throne, his weapons and his soldiers’ uniforms. That is why he is called the <b>Tiger of Mysore</b>.</p>
<p><b>His kingdom.</b> Most of his subjects were Hindu, and several of his highest officers were Hindu. How he treated their temples is the question this guide looks at.</p></div>'''))
mapfig=fig(560,250,'Schematic map of the Mysuru region showing Srirangapatna with its fort, temple and mosque, Karighatta, Melukote to the north, Mysuru, Nanjangud and Kalale to the south, Biligiri Rangana Hills to the south-east, and an arrow toward Sringeri far to the north-west. Not to scale.',
 '<rect width="560" height="250" fill="#eef6e4"/><path d="M0 120 C 140 100, 300 140, 560 110" fill="none" stroke="#4aa3df" stroke-width="14"/>'
 +''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}" stroke="#111" stroke-width="2"/>'+T(x+(12 if a=="start" else -12 if a=="end" else 0),y+(4 if a!="middle" else -12),n,10,'#0b2a4a',a) for x,y,c,n,a in (
  (250,116,'#e0a800','ŚRĪRAṄGAPAṬṬAṆA','middle'),(300,96,'#3b6fd0','KARIGHAṬṬA','start'),(280,40,'#3b6fd0','MELUKŌṬE','start'),(220,170,'#bbb','MYSURU','end'),
  (240,214,'#0b2a4a','NAÑJANAGŪḌU','end'),(270,232,'#3b6fd0','KALALE','start'),(450,200,'#3b6fd0','BIḶIGIRI RAṄGANA BEṬṬA','end')))
 +'<path d="M120 70 l-80 -50" stroke="#111" stroke-width="2" stroke-dasharray="6 5"/><path d="M40 20 l12 2 l-6 8z" fill="#111"/>'+T(60,44,'to ŚṚṄGERI',10,'#555','start')+T(480,244,'simplified, not to scale',9,'#555'))
pages.append(page('map','THE TEMPLES IN THIS GUIDE','Around Tipu’s capital',mapfig+'''<div class="panel reading">
<p><b>The centre.</b> Tipu’s capital, the island fort of <b>Śrīraṅgapaṭṭaṇa</b>, held the great <b>Raṅganātha</b> temple. Within a short ride lay Karighaṭṭa, Nimiṣāmbā, Melukōṭe, Nañjanagūḍu and Kalale.</p>
<p><b>Farther out.</b> Biḷigiri Raṅgana Beṭṭa in the south-east forests, and <b>Śṛṅgeri</b>, far to the north-west in the Malnad, whose letters are the best-known record of all.</p>
</div>'''))
gifts=fig(560,160,'A row of silver temple cups, a silver camphor burner, a jewelled cup and a green linga, each labelled with its temple',
 '<rect width="560" height="160" fill="#f2f6ff"/>'+''.join(CUP(40+i*28,120,.7) for i in range(7))+T(124,150,'RAṄGANĀTHA · 7 CUPS',10,'#0b2a4a')
 +'<g transform="translate(260 120)" stroke="#111" stroke-width="2"><path d="M-12 0 h24 l-4 -20 h-16z" fill="#d8dde3"/><path d="M-4 -20 q4 -12 8 0" fill="#ff8c1a"/></g>'+T(260,150,'CAMPHOR BURNER',9)
 +CUP(350,120,.9,'#e0a800')+''.join(f'<circle cx="{340+i*7}" cy="102" r="3" fill="{c}"/>' for i,c in enumerate(('#c0392b','#2e9a5a','#1d6fb8')))+T(350,150,'NAÑJANAGŪḌU',10,'#0b2a4a')
 +''.join(CUP(440+i*22,120,.6) for i in range(4))+T(474,150,'KALALE · 4 CUPS',10,'#0b2a4a'))
pages.append(page('record','THE RECORD OF GIFTS','What the temples still hold',gifts+'<table class="ct"><tr><th>Temple</th><th>Recorded gift</th></tr>'
 +''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in (
 ('Raṅganātha, Śrīraṅgapaṭṭaṇa','Seven silver cups and a silver camphor burner'),
 ('Śrīkaṇṭheśvara, Nañjanagūḍu','A jewelled cup, still with the temple; a green (marakata or jade) liṅga'),
 ('Lakṣmīkānta, Kalale','Four silver cups, a silver plate and a silver spittoon'),
 ('Nārāyaṇasvāmi, Melukōṭe','A Kannada decree on temple recitation; gold and silver vessels inscribed with his name'),
 ('Across the kingdom','Regular annual grants to about <b>156</b> temples (listed by the Mysore Gazetteer’s editor Srikantaiah); <b>34</b> endowment sanads, 1782–1799')))+'</table>'
 +'''<div class="panel reading small"><p><b>And land.</b> Tipu is also recorded as taking back land grants to temples and Brahmins that had been made without proper authority; grants backed by a proper <b>sanad</b> were left alone.</p></div>'''))
pages.append(page('nanjangud','NAÑJANAGŪḌU','Hakīm Nañjuṇḍa, the physician',facts([
 ('The story','Temple tradition says Tipu’s royal elephant lost its sight; on the priests’ advice it was bathed in the Kapilā and its eyes washed with the Lord’s abhiṣeka water for 48 days, and it saw again'),
 ('The gift','A green <b>marakata</b> liṅga with an emerald necklace, still shown once a year at <b>Girijākalyāṇa</b>; and a jewelled cup'),
 ('The name','He called the Lord <b>Hakīm Nañjuṇḍa</b>, “Nañjuṇḍa the physician”'),
 ('A second version','The Mysore Gazetteer tells a similar elephant story of his father, <b>Hyder Ali</b>')])
 +'''<div class="panel reading"><p><b>Living memory.</b> Of all the Tipu stories around Mysuru, this one is kept by the temple itself: the gifts are still there, and the name is still used.</p>
<p>Full guide: <a href="/bhakti/temples-of-india/around-mysuru/nanjangud/">Nañjanagūḍu ➜</a></p></div>'''
 +talk("The Sultan named the god 'doctor'?","Hakīm is the Persian word for physician. A grateful patient's name for the healer, and it stuck.")))
fortfig=fig(560,180,'The island fort of Srirangapatna: inside the walls the Ranganatha temple tower and, nearby, the twin minarets of the Masjid-i-Ala; outside, the summer palace garden and the road east to Ganjam',
 '<rect width="560" height="180" fill="#eef6e4"/><path d="M0 150 q280 -20 560 0 V180 H0z" fill="#4aa3df"/><rect x="60" y="40" width="300" height="104" fill="#f6f1e2" stroke="#7a5a2a" stroke-width="5"/>'
 +TEMPLE(150,118,1.5)+MOSQUE(280,118,1.4)+T(150,138,'RAṄGANĀTHA',10,'#0b2a4a')+T(280,138,'MASJID-I-ALA',10,'#0b2a4a')
 +'<rect x="390" y="70" width="60" height="40" fill="#cfe6bf" stroke="#111"/>'+T(420,64,'SUMMER PALACE',9)+'<path d="M450 90 h70" stroke="#8a7a6a" stroke-width="3" stroke-dasharray="6 4"/>'+T(530,84,'GAÑJĀM',9,'#c0392b','end')+T(210,32,'THE FORT',10,'#7a5a2a'))
pages.append(page('srirangapatna','ŚRĪRAṄGAPAṬṬAṆA','A temple inside the Sultan’s fort',fortfig+'''<div class="panel reading">
<p><b>Raṅganātha.</b> The great temple of <b>Ādi Raṅga</b> stood inside Tipu’s fort, close to his palace, through his whole reign. The record lists his gift of <b>seven silver cups</b> and a <b>silver camphor burner</b> to it.</p>
<p><b>The summer palace.</b> East of the fort, his garden palace Dariya Daulat Bāgh (1784) stands on the road to <b>Gañjām</b>, where <a href="/bhakti/temples-of-india/around-mysuru/">Nimiṣāmbā</a>’s temple stands by the Kāverī.</p>
<p><b>The mosque.</b> Near the temple he built the Masjid-i-Ala, whose origin is disputed (see page “The Masjid-i-Ala”).</p>
<p>Full guide: <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga ➜</a></p>
</div>'''))
pages.append(page('melukote1','MELUKŌṬE · I','A decree for the recitation',fig(560,150,'A royal decree on a scroll beside gold and silver temple vessels, with the temple of Melukote on its hill behind',
 '<rect width="560" height="150" fill="#fff4dc"/><path d="M300 150 Q380 40 460 150z" fill="#8a9a6a" stroke="#111" stroke-width="2"/>'+TEMPLE(380,76,1)+SCROLL(140,92,.8)+CUP(240,130,.8,'#e0a800')+CUP(280,132,.7))+facts([
 ('The temple','The Nārāyaṇa temple of <b>Melukōṭe</b> (Tirunārāyaṇapura), the great Śrīvaiṣṇava centre where Rāmānuja lived'),
 ('The decree','A Kannada order that the Śrīvaiṣṇava invocatory verses at the temple be recited <b>in their traditional form</b>'),
 ('The vessels','Gold and silver vessels at the temple carry inscriptions naming the Sultan'),
 ('How it is read','Historians including <b>B. A. Saletore</b> and <b>Irfan Habib</b> cite these to describe Tipu as a protector of Hindu worship')])
 +talk("He told priests how to chant?","He ordered that the traditional form be kept. It's one of the most quoted pieces of the record.")))
pages.append(page('melukote2','MELUKŌṬE · II','Naraka Caturdaśī: a day of mourning','''<div class="panel reading">
<p><b>The memory.</b> The <b>Mandyam Iyengar</b> community of Melukōṭe remember a massacre of their people by Tipu’s soldiers on <b>Naraka Caturdaśī</b>, the day of Dīpāvaḷi in South India. Many families of the community still do not celebrate Dīpāvaḷi, and keep the day as one of mourning.</p>
<p><b>The context they give.</b> Community accounts link it to the Mysuru royal family’s attempts to restore Woḍeyar rule: the dowager queen <b>Lakṣmammaṇṇi</b> and the pradhāns <b>Tirumala Iyengar</b> and his brother, of the same community, were in secret correspondence with the British, which Tipu treated as treason.</p>
<p><b>The scale.</b> Accounts give about <b>700</b> to <b>800</b> killed; a few give higher figures.</p>
</div>'''+facts([
 ('Sources','Chiefly community history and oral tradition, including the community’s own published history; also later newspaper and magazine accounts'),
 ('Dates given','Differ widely: 1760, 1783 and 1790 all appear'),
 ('Contemporary records','We did not find a contemporary record of the event in the sources we checked; mainstream histories rarely mention it'),
 ('Today','The memory is real and living; it is also used heavily in present-day political debate over Tipu')])
 +'<div class="panel reading small"><p><b>Both on one hill.</b> The same town holds Tipu’s decree and vessels, and the community’s mourning. This guide records both and does not try to reconcile them.</p></div>'))
pages.append(page('masjid','THE MASJID-I-ALA','A mosque, and a disputed past',fig(560,160,'The twin-minaret Masjid-i-Ala inside the fort, with a question mark over a faint outline of a temple behind it',
 '<rect width="560" height="160" fill="#f2f6ff"/>'+'<g opacity=".25">'+TEMPLE(280,130,2.2)+'</g>'+MOSQUE(280,140,2)+'<text x="420" y="70" font-size="60" fill="#c0392b" font-family="Georgia">?</text>')+facts([
 ('Built','<b>1786–87</b>, inside the Śrīraṅgapaṭṭaṇa fort near the Bangalore Gate; Persian inscriptions name Tipu as the builder'),
 ('The claim','Hindu groups say it stands on the site of a <b>Hanumān</b> (Āñjaneya) temple, pointing to Hindu motifs on granite pillars, and have asked for permission to worship there'),
 ('The 1935 report','They cite the <b>1935 Annual Report</b> of the Mysore Archaeological Department, which records a tradition that a fakir made the young Tipu promise to turn the temple into a mosque, and that he kept the promise'),
 ('Today','An active mosque with a madrasa, and a <b>Monument of National Importance</b> under the Archaeological Survey of India')])
 +'<div class="panel reading small"><p><b>What we can say.</b> The report and the claim are on record; we found no court ruling or historians’ consensus settling the question. It remains disputed.</p></div>'))
pages.append(page('biligiri','BIḶIGIRI RAṄGANA BEṬṬA','A hunting trip and a new name',facts([
 ('Before Tipu','A copper plate of <b>1667</b> names the Lord of the white hill <b>Tiru Veṅkaṭanātha</b>'),
 ('The visit','Tradition says Tipu visited on a hunting expedition and called it a temple of <b>Raṅganātha</b>'),
 ('After','The name stuck: <b>Biḷigiri Raṅganātha</b>, as it is known today'),
 ('Pūrṇayya','Tipu’s officer <b>Pūrṇayya</b>, later Dīvān under the Woḍeyars, is also recorded as endowing the temple')])
 +'''<div class="panel reading"><p><b>A name from a Sultan.</b> If the tradition is right, one of Karnataka’s best-loved names for Viṣṇu came from a remark by Tipu.</p>
<p>Full guide: <a href="/bhakti/temples-of-india/around-mysuru/br-hills/">Biḷigiri Raṅgana Beṭṭa ➜</a></p></div>'''))
pages.append(page('karighatta','KARIGHAṬṬA','A temple hill in a war',fig(560,150,'Karighatta hill with its temple, British redcoat lines camped at its foot, and Tipu’s fort on the island beyond',
 '<rect width="560" height="150" fill="#eef6e4"/><path d="M40 150 Q140 30 240 150z" fill="#3a6a3a" stroke="#111" stroke-width="2"/>'+TEMPLE(140,62,.8)
 +''.join(f'<path d="M{x} 146 l8 -16 l8 16z" fill="#fff" stroke="#111"/>' for x in range(250,380,22))+''.join(f'<rect x="{x}" y="128" width="6" height="14" fill="#c0392b" stroke="#111"/>' for x in range(260,380,20))
 +'<path d="M380 140 q90 -20 180 0" stroke="#4aa3df" stroke-width="10" fill="none"/>'+FORT(480,130,.7))+tl([
 ('Feb 1792','Lord Cornwallis’s army, with Marāṭhā and Hyderabad allies, besieges Śrīraṅgapaṭṭaṇa. British records call the hill <b>Carigat</b> or <b>Karigaut Hill</b>.'),
 ('The fighting','Among the actions of the siege is an attack on Tipu’s post at Carigat Hill; later, badly exposed, Cornwallis pulls his command back to the hill.'),
 ('18 Mar 1792','The <b>Treaty of Seringapatam</b> ends the war.'),
 ('1799','Local legend says British cannons stood on the hill in the final siege; the records we found confirm only 1792.')])
 +'<div class="panel reading small"><p>Full guide: <a href="/bhakti/temples-of-india/around-mysuru/karighatta/">Karighaṭṭa ➜</a></p></div>'))
pages.append(page('sringeri','ŚṚṄGERI','The letters to the Śaṅkarācārya',fig(560,140,'Royal letters in Kannada passing between the Sultan’s court and the matha of Sringeri, with horsemen raiding in the background',
 '<rect width="560" height="140" fill="#fff4dc"/>'+SCROLL(120,80,.8)+SCROLL(200,86,.7)+'<path d="M250 70 h140" stroke="#111" stroke-width="2" stroke-dasharray="8 6"/><path d="M390 64 l10 6 l-10 6z" fill="#111"/>'+TEMPLE(470,110,1.3)+T(470,132,'ŚṚṄGERI MAṬHA',10,'#0b2a4a'))+tl([
 ('1791','Marāṭhā horsemen under <b>Raghunāth Rao Paṭvardhan</b> raid the Śṛṅgeri temple and maṭha, killing and wounding people, plundering it and displacing the image of the goddess <b>Śāradā</b>.'),
 ('The appeal','The Śaṅkarācārya petitions Tipu. He orders his officer at Bednur to give the Svāmī <b>200 rahatis</b> in cash and other gifts for the restoration.'),
 ('1790s','Letters continue between the court and the maṭha: about <b>30</b> in Kannada.'),
 ('1916','The letters are found by the Director of Archaeology in Mysuru.')])
 +'''<div class="panel reading"><p><b>Why it matters.</b> Śṛṅgeri is outside the Mysuru region, but these letters are the most cited document of Tipu’s dealings with Hindu religious institutions, so they belong in any account of this kind.</p></div>'''))
pages.append(page('officers','THE SULTAN’S HINDU OFFICERS','Who ran the kingdom',facts([
 ('Pūrṇayya','<b>Mīr Āsaf</b>, head of revenue; after 1799 Dīvān of Mysuru under the restored Woḍeyars'),
 ('Krishna Rao','Treasurer'),
 ('Shamaiya Iyengar','Minister of Post and Police; his brother Ranga Iyengar was also an officer'),
 ('Suba Rao','Chief Peshkar'),
 ('Moolchand, Sujan Rai','Agents at the Mughal court')])
 +'''<div class="panel reading"><p><b>Two readings.</b> Some take these appointments as evidence of an even-handed state; others note that a ruler of a mostly Hindu kingdom needed Hindu administrators whatever his personal views, and point out that men like Tirumala Iyengar also worked against him.</p></div>'''
 +talk("So Hindus ran his treasury and his police?","Yes, and his revenue. That's on record. What it tells us about his beliefs is where the arguing starts.")))
pages.append(page('views','TWO VIEWS OF TIPU','How historians read the record','''<div class="g2">
<div class="card bg-yellow"><h4>📜 The patron</h4><p>Historians such as <b>B. A. Saletore</b>, <b>Irfan Habib</b>, <b>Mohibbul Hasan</b>, <b>Kate Brittlebank</b> and <b>A. S. Chetty</b> point to the grants, gifts, decrees and Śṛṅgeri letters. Several argue that many persecution stories come from early British writers such as <b>Mark Wilks</b> and <b>James Kirkpatrick</b>, who fought against Tipu and had reason to paint him as a tyrant.</p></div>
<div class="card bg-blue"><h4>⚔️ The persecutor</h4><p>Critics point to campaigns in <b>Kodagu</b> and <b>Malabar</b>, the captivity of <b>Mangalorean Catholics</b>, accounts of forced conversions and destroyed temples and churches, and local memories such as <b>Melukōṭe</b>. Some read the temple gifts as political: buying loyalty in a Hindu-majority kingdom at war.</p></div>
</div>
<div class="panel reading"><p><b>Where the evidence sits.</b> Around Mysuru, the surviving objects and documents (cups, liṅga, decree, letters, sanads) mostly record patronage. The harshest accounts come mostly from the coast and the hills to the west, and from communal memory. Both are part of the history, and the debate over him remains live and political in Karnataka today.</p></div>'''
 +talk("So who's right?","Historians still disagree, and politics has made the debate louder. Our job here is to show you the record; the judging is yours.")))
pages.append(page('timeline','TIMELINE','Tipu and the temples',tl([
 ('1751','Tipu born at Devanahalli.'),
 ('1782','Becomes ruler of Mysuru; endowment sanads to temples follow through his reign.'),
 ('1784','Builds the Dariya Daulat Bāgh summer palace near Gañjām.'),
 ('1786–87','Builds the Masjid-i-Ala in the Śrīraṅgapaṭṭaṇa fort.'),
 ('1760–1790','The Melukōṭe killings, by the various dates given in community accounts.'),
 ('1791','Marāṭhā raid on Śṛṅgeri; Tipu sends aid.'),
 ('1792','Siege of Śrīraṅgapaṭṭaṇa; fighting at Karighaṭṭa; treaty in March.'),
 ('1799','Tipu killed on 4 May; the Woḍeyars restored.'),
 ('1916','The Śṛṅgeri letters found.'),
 ('1935','The Mysore Archaeological report on the Masjid-i-Ala tradition.')])))
glossary=[('Sanad','a royal deed granting land or income'),('Hakīm','physician (Persian)'),('Marakata','emerald'),('Mīr Āsaf','head of revenue in Tipu’s government'),('Dīvān','chief minister'),('Peshkar','a senior revenue official'),('Rahati','a coin of Tipu’s mint'),('Pradhān','minister'),('Naraka Caturdaśī','the day of Dīpāvaḷi in South India'),('Mandyam Iyengars','a Śrīvaiṣṇava community of Melukōṭe'),('Maṭha','a monastery of a religious order'),('Anglo-Mysore Wars','four wars (1767–1799) between Mysuru and the British East India Company'),('Monument of National Importance','a site protected by the Archaeological Survey of India')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The man.</b> Tipu Sultan, ruler of Mysuru 1782–1799, from the island fort of Śrīraṅgapaṭṭaṇa.</div>
<div><b>The gifts.</b> Silver to Raṅganātha and Kalale; a jewelled cup and green liṅga to Nañjanagūḍu; a decree and vessels at Melukōṭe; grants to about 156 temples; 34 sanads.</div>
<div><b>The names.</b> Hakīm Nañjuṇḍa; Biḷigiri Raṅganātha; Carigat Hill in the war records.</div>
<div><b>The letters.</b> About 30 Kannada letters to Śṛṅgeri after the Marāṭhā raid of 1791.</div>
<div><b>The disputes.</b> The Melukōṭe mourning on Naraka Caturdaśī; the temple claim at the Masjid-i-Ala; and two opposite readings of the man.</div>
</div>'''+talk("What do I take away from all this?","That history around Mysuru is written in silver cups, letters and memories, and they don't all say the same thing. Know all of it.")+'<div class="key">One Sultan, many temples: <b>read the whole record</b>.</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Life, gifts and views:</b> Wikipedia, “Tipu Sultan”: dates; the Śṛṅgeri raid, aid and about 30 letters found in 1916; the Melukōṭe decree and vessels; Nañjanagūḍu, Kalale and Raṅganātha gifts; about 156 temples and 34 sanads; Hindu officers; Kodagu, Malabar and Mangalore allegations; the views of Brittlebank, Hasan, Chetty, Habib and Saletore on Wilks and Kirkpatrick. New World Encyclopedia, “Tippu Sultan”: Kalale; Nañjanagūḍu cup; Saletore; the resumption of unauthorised grants. The 156-temple list is attributed to Srikantaiah, editor of the Mysore Gazetteer.</p>
<p><b>Melukōṭe memory:</b> community and press accounts (Swarajya, Organiser, community forums, and accounts citing <i>History and Vamshaparampara of Mandayam Sree Vaishnava Samudayam</i>), which give dates of 1760, 1783 and 1790 and figures of 700–800 or more.</p>
<p><b>Masjid-i-Ala:</b> Wikipedia, “Masjid-i-Ala” (1786–87; inscriptions; the Hanumān temple claim; the 1935 report, p. 61; ASI status).</p>
<p><b>Temples:</b> our guides to Nañjanagūḍu, Ādi Raṅga, Biḷigiri Raṅgana Beṭṭa, Karighaṭṭa and Nimiṣāmbā, and their sources. <b>1792 siege:</b> Wikipedia, “Siege of Seringapatam (1792)”; FIBIS. <b>Summer palace (1784):</b> Wikipedia, list of religious buildings of the Kingdom of Mysore.</p>
<p><b>Not verified:</b> the Melukōṭe date and toll; the 1935 tradition about the mosque; the Biḷigiri renaming (tradition). This guide takes no side in the debate. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('who','Who Was Tipu Sultan?'),('map','The Temples in This Guide'),('record','The Record of Gifts'),('nanjangud','Nañjanagūḍu'),('srirangapatna','Śrīraṅgapaṭṭaṇa'),('melukote1','Melukōṭe · The Decree'),('melukote2','Melukōṭe · The Mourning'),('masjid','The Masjid-i-Ala'),('biligiri','Biḷigiri Raṅgana Beṭṭa'),('karighatta','Karighaṭṭa'),('sringeri','Śṛṅgeri'),('officers','The Hindu Officers'),('views','Two Views of Tipu'),('timeline','Timeline'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MYSURU SPECIAL</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,6.6vw,72px)">TIPU SULTAN AND THE TEMPLES</h1>
  <div class="series">ŚRĪRAṄGAPAṬṬAṆA · NAÑJANAGŪḌU · MELUKŌṬE · ŚṚṄGERI · A REFERENCE GUIDE</div>
  <div class="tag">The record, and the disputes</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Visit the temples around Mysuru and the name <b>Tipu Sultan</b> keeps coming up: on a silver cup, in a god’s nickname, in a royal letter, on a battlefield, and in a day of mourning.</p>
    <p>Few figures in Indian history are argued over so fiercely. This guide does not try to settle the argument. It gathers what is on record, temple by temple, sets the disputed memories beside it, and names the sources for both.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Will you tell me if he was good or bad?","No, Zappy. I'll show you the cups, the letters and the memories. You make up your own mind.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Tipu_and_the_Temples.html','w').write(head+b+tail())
print('ok')
