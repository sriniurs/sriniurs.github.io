import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
import common_t
def head_red(title,desc):
    h=open(common_t.SRC).read(); hd=h[:h.find('<div class="book">')]
    css,rest=hd[:hd.find('</style>')],hd[hd.find('</style>'):]
    for a,b in [('#0b2a4a','#7a1d12'),('#1d4f9a','#c0392b'),('#09283f','#7a1d12'),('#04101f','#2a0805'),('#2c5f9e','#d9822b')]: css=css.replace(a,b)
    hd=css+rest
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
head=head_red('Nimiṣāmbā · Gañjām, Śrīraṅgapaṭṭaṇa · Temples around Mysuru · srini.presents',
 'Nimiṣāmbā of Gañjām on the Kāverī: the Goddess who answers in a moment (nimiṣa). The yajña, the demons Jānu and Sumaṇḍala, the stone Śrīcakra, Mauktikeśvara, and the Woḍeyars. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def DEVI(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-26 70 q-4 -70 26 -84 q30 14 26 84z" fill="#c0392b"/><path d="M-20 10 q20 10 40 0" fill="none" stroke="#ffd60a" stroke-width="4"/>'
     '<path d="M-20 -6 l-20 -20 M20 -6 l20 -20" stroke="#f2c79b" stroke-width="7"/><path d="M-44 -30 l8 -12 l8 12z" fill="#bbb"/><circle cx="42" cy="-30" r="7" fill="#ffd60a"/>'
     '<circle cy="-28" r="13" fill="#f2c79b"/><path d="M-13 -36 q13 -12 26 0 v12 q4 10 4 20 M-13 -36 v12 q-4 10 -4 20" fill="none" stroke="#2b1a0e" stroke-width="4"/>'
     '<path d="M-14 -40 h28 l-4 -16 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/><circle cy="-30" r="1.8" fill="#c0392b"/><path d="M-5 -24 q5 3 10 0" fill="none"/></g>')
def CHAKRA(x,y,r=40):
    s=f'<g transform="translate({x} {y})" stroke="#111" stroke-width="1.6" fill="none"><rect x="{-r*1.2}" y="{-r*1.2}" width="{r*2.4}" height="{r*2.4}" fill="#fff4cd"/><circle r="{r}" fill="#ffe3e3"/><circle r="{r*0.8}"/>'
    for k in range(4):
        rr=r*0.75*(1-k*0.18)
        s+=f'<path d="M0 {-rr} L{rr*0.87} {rr*0.5} L{-rr*0.87} {rr*0.5}z" stroke="#c0392b"/><path d="M0 {rr} L{rr*0.87} {-rr*0.5} L{-rr*0.87} {-rr*0.5}z" stroke="#1d6fb8"/>'
    return s+'<circle r="2.6" fill="#c0392b"/></g>'
def FIRE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-30" y="-10" width="60" height="16" fill="#8a7a6a"/><path d="M-22 -10 q-6 -30 10 -40 q-2 16 8 18 q2 -24 18 -34 q-4 24 10 30 q8 -10 4 -20 q14 20 -4 46z" fill="#ff8c1a"/><path d="M-8 -10 q0 -16 10 -22 q0 14 8 16 q4 -4 2 -10 q8 10 -4 16z" fill="#ffd60a"/></g>'
def DEMON(x,y,s=1,c='#3a5a2a'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cy="-40" r="16" fill="{c}"/><path d="M-12 -54 l-6 -14 M12 -54 l6 -14"/><circle cx="-6" cy="-42" r="3" fill="#ffd60a"/><circle cx="6" cy="-42" r="3" fill="#ffd60a"/><path d="M-8 -32 l4 4 l4 -4 l4 4"  fill="none"/><path d="M-26 40 q26 -70 52 0z" fill="#2b2b2b"/><path d="M22 -10 l24 -30" stroke="#7a5a2a" stroke-width="5"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The Goddess Nimishamba rising in a golden glow above a sacred fire on the bank of the Kaveri, a Sri Chakra beside her">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/><circle cx="190" cy="110" r="90" fill="#ffd166" opacity=".3"/>'
 '<path d="M0 226 q190 -24 380 0 V268 H0z" fill="#4aa3df"/>'+FIRE(190,226,1.3)+DEVI(190,124,1.25)+CHAKRA(330,200,26)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','<b>Nimiṣāmbā</b>, a form of <b>Pārvatī</b>: the Mother who comes in a <i>nimiṣa</i>, a moment'),
 ('Before her','A rare <b>Śrīcakra</b> carved in stone, worshipped daily'),
 ('With her','<b>Mauktikeśvara</b> (Śiva), <b>Lakṣmīnārāyaṇa</b>, <b>Sūrya</b>, <b>Gaṇapati</b> and <b>Hanumān</b>: a Śiva-pañcāyatana temple'),
 ('Place','<b>Gañjām</b>, on the bank of the <b>Kāverī</b>, just outside Śrīraṅgapaṭṭaṇa, Mandya district, Karnataka'),
 ('Legend','The yajña of the sage <b>Mukthaka</b>, the demons <b>Jānu</b> and <b>Sumaṇḍala</b>, and the Goddess who came at once'),
 ('Built','Under the Woḍeyars of Mysuru: attributed to <b>Rāja Woḍeyar</b> (early 1600s), renovated under <b>Mummaḍi Kṛṣṇarāja Woḍeyar</b>'),
 ('Great festival','<b>Nimiṣāmbā Jayantī</b>, on Vaiśākha śukla daśamī (April–May)'),
 ('Belief','She clears her devotees’ troubles within a moment')])
 +talk("A goddess who answers in a minute? I'll take one!","That's exactly why the crowds come, Zappy. Her very name means 'Mother of the moment'.")))
mapfig=fig(560,230,'Schematic map: the island of Srirangapatna in the Kaveri, with Ganjam and the Nimishamba temple on the riverbank to the east, the Sangama beyond, and Karighatta hill across the Lokapavani. Not to scale.',
 '<rect width="560" height="230" fill="#eef6e4"/><path d="M0 70 C 160 40, 320 60, 560 50" fill="none" stroke="#4aa3df" stroke-width="18"/><path d="M0 180 C 160 200, 320 170, 560 120" fill="none" stroke="#4aa3df" stroke-width="18"/>'
 +'<path d="M20 80 C 160 54, 320 70, 500 70 C 520 90, 500 110, 480 116 C 320 160, 160 190, 20 170z" fill="#dfeccf" stroke="#111" stroke-width="2"/>'+T(150,128,'ŚRĪRAṄGAPAṬṬAṆA',11,'#7a1d12')
 +'<rect x="380" y="92" width="34" height="22" fill="#fdecea" stroke="#111" stroke-width="2"/>'+T(397,86,'NIMIṢĀMBĀ · GAÑJĀM',10,'#c0392b')
 +'<circle cx="520" cy="80" r="7" fill="#e0a800" stroke="#111"/>'+T(520,104,'SAṄGAMA',9,'#7a1d12')
 +'<path d="M470 0 C 480 30, 500 50, 520 76" stroke="#4aa3df" stroke-width="10" fill="none"/>'+'<path d="M400 40 Q420 6 440 40z" fill="#3a6a3a" stroke="#111"/>'+T(380,20,'KARIGHAṬṬA',9,'#555','end')
 +T(60,62,'KĀVERĪ',11,'#1d6fb8')+T(60,206,'KĀVERĪ',11,'#1d6fb8')+T(300,222,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','On the Kāverī at Gañjām',mapfig+'''<div class="panel reading">
<p><b>Gañjām.</b> The temple stands in <b>Gañjām</b>, once a thriving suburb of the Śrīraṅgapaṭṭaṇa fort, on the road east from the island town toward the saṅgama, past Tipu’s summer palace.</p>
<p><b>The river.</b> The temple stands right on the bank of the <b>Kāverī</b>.</p>
<p><b>Neighbours.</b> Across the Lokapāvanī rises <b>Karighaṭṭa</b> hill, and on the island stands <b>Ādi Raṅga</b>.</p>
</div>'''))
deity=fig(560,220,'Nimishamba seated in her shrine, crowned and four-armed, with a stone Sri Chakra on the floor before her',
 '<rect width="560" height="220" fill="#fde4e4"/><rect x="170" y="20" width="220" height="170" fill="#fff4cd" stroke="#111" stroke-width="2"/><path d="M160 20 h240 l-20 -14 h-200z" fill="#c9a26b" stroke="#111"/>'
 +DEVI(280,110,1.3)+CHAKRA(280,196,18)+T(280,216,'NIMIṢĀMBĀ · ŚRĪCAKRA',12,'#7a1d12'))
pages.append(page('deity','THE MOTHER OF THE MOMENT','Nimiṣāmbā',deity+'''<div class="g2">
<div class="card bg-red"><h4>⚡ Her name</h4><p><i>Nimiṣa</i> is the blink of an eye, a moment; <i>ambā</i> is mother. <b>Nimiṣāmbā</b>: the Mother who comes in a moment.</p></div>
<div class="card bg-yellow"><h4>🔱 Her form</h4><p>She is <b>Pārvatī</b>, Śiva’s consort, worshipped here as Śakti with a <b>Śrīcakra</b> before her.</p></div>
</div>
<div class="panel reading"><p><b>Why people come.</b> Devotees believe she removes obstacles and troubles within a moment: many come praying for obstacles to a marriage to be cleared, or for the end of a long worry.</p></div>'''))
leg1=fig(560,200,'A sage tending a great sacrificial fire; two horned demons attacking; the Goddess blazing out of the fire',
 '<rect width="560" height="200" fill="#fff4dc"/>'+person(90,180,'#ff8c1a','#c98b5a',1)+'<path d="M70 116 q20 -24 40 0" fill="#fff" stroke="#111"/>'+FIRE(230,190,1.4)
 +DEVI(230,96,.9)+DEMON(400,170,1)+DEMON(480,176,.9,'#5a3a6a')+'<path d="M260 80 l110 50" stroke="#ff8c1a" stroke-width="6" stroke-dasharray="10 6"/>'
 +T(90,196,'MUKTHAKA',11,'#7a1d12')+T(440,196,'JĀNU · SUMAṆḌALA',11,'#2b2b2b'))
pages.append(page('legends1','THE LEGEND · I','The yajña and the demons',leg1+'''<div class="steps">
<div><b>A yajña for the world.</b> The temple’s story tells that <b>Śiva</b>, as the sage <b>Mukthaka</b> (Mauktikeśvara), set out to perform a great yajña for the welfare of all beings.</div>
<div><b>The demons.</b> Two demons, <b>Jānu</b> and <b>Sumaṇḍala</b>, feared the yajña would end their rule. They sent army after army, and every army was beaten.</div>
<div><b>Their boon.</b> Then they came themselves, protected by a boon that <b>no weapon</b> could harm them, and the sage could not defeat them.</div>
<div><b>The prayer.</b> Mukthaka prayed to the Mother. In a moment Pārvatī appeared, rising, some tellings say, from the sacrificial fire.</div>
<div><b>Fire from her eyes.</b> No weapon could touch them, so she burned the demons with the fire of her eyes. The sage, overjoyed, named her <b>Nimiṣāmbā</b>: she came within a <i>nimiṣa</i>.</div>
</div>'''))
pages.append(page('legends2','THE LEGEND · II','Another telling: the king Muktarāja',facts([
 ('The king','In another telling, a king <b>Sumanaska</b> wished to hold a yajña for his people, and gave the task to the prince and to the royal sage <b>Muktarāja</b>'),
 ('The demons','The demons, named <b>Janumaṇḍala</b> and <b>Sumaṇḍala</b>, overpowered the prince and broke up the rite'),
 ('The penance','<b>Muktarāja</b>, a king of the Soma (Moon) line by some accounts and the Sun line by others, did penance here, carved a <b>Śrīcakra</b> on stone and began elaborate worship'),
 ('The answer','The Goddess appeared at once, destroyed the demons, and has stayed here ever since')])
 +'''<div class="panel reading"><p><b>Same heart, different details.</b> Whether the yajña was Śiva’s own or a king’s, both tellings agree: the demons could not be beaten by weapons, a devotee called, and the Mother came in a moment.</p>
<p>The same pattern runs through the <a href="/bhakti/devi/devi-mahatmya/">Devī Māhātmya</a>: when the gods are helpless, the Goddess appears and does what no weapon could.</p></div>'''
 +talk("Was it Śiva or a king who did the yajña?","Depends who's telling! Temples keep many versions. We give you both, and the one thing they agree on.")))
pages.append(page('srichakra','THE STONE ŚRĪCAKRA','The Goddess as a diagram',fig(560,220,'A Sri Chakra diagram of interlocking triangles inside circles, lotus rings and a square enclosure',
 '<rect width="560" height="220" fill="#fff9ec"/>'+CHAKRA(280,110,80))+'''<div class="panel reading">
<p><b>What it is.</b> The <b>Śrīcakra</b> (Śrī Yantra) is the Goddess drawn as geometry: interlocking triangles, nine in all, pointing up and down, surrounded by lotus petals and a square gateway frame. It is worshipped as her very form.</p>
<p><b>This one.</b> In front of Nimiṣāmbā is a Śrīcakra <b>carved in black stone</b>, with seed-syllables (<i>bīja</i>) and her mūla-mantra inscribed. It is described as rare and ancient, and receives daily pūjā.</p>
<p><b>The legend’s link.</b> In the Muktarāja telling, the king himself carved a Śrīcakra in stone during his penance here.</p>
</div>'''))
plan=fig(560,220,'Simplified plan: a Shiva-panchayatana temple with Nimishamba in the main shrine and shrines of Mauktikeshvara, Lakshminarayana, Surya, Ganapati and Hanuman, with steps down to the Kaveri',
 '<rect width="560" height="220" fill="#f6f1e2"/><rect x="100" y="20" width="360" height="150" fill="none" stroke="#7a5a2a" stroke-width="4"/>'
 +'<rect x="230" y="40" width="100" height="56" fill="#c0392b" stroke="#111"/>'+T(280,74,'NIMIṢĀMBĀ',11,'#fff')
 +''.join(f'<rect x="{x}" y="{y}" width="80" height="34" fill="#fff" stroke="#111"/>'+T(x+40,y+22,n,9) for x,y,n in ((120,40,'MAUKTIKEŚVARA'),(360,40,'LAKṢMĪNĀRĀYAṆA'),(120,116,'SŪRYA'),(360,116,'GAṆAPATI'),(240,116,'HANUMĀN')))
 +'<path d="M100 186 h360" stroke="#c9a26b" stroke-width="6"/><path d="M0 206 q280 -20 560 0 V220 H0z" fill="#4aa3df"/>'+T(280,200,'THE KĀVERĪ',9,'#fff'))
pages.append(page('temple','THE TEMPLE','A family of five shrines',plan+'''<div class="g2">
<div class="card bg-yellow"><h4>🕉 Śiva-pañcāyatana</h4><p>The temple gathers five deities in one compound: the Goddess with <b>Śiva as Mauktikeśvara</b>, <b>Lakṣmīnārāyaṇa</b>, <b>Sūrya</b> and <b>Gaṇapati</b>, with <b>Hanumān</b> as well.</p></div>
<div class="card bg-red"><h4>🔱 Mauktikeśvara</h4><p>The Śiva of the shrine bears the sage’s name: <b>Mauktikeśvara</b>, the Lord who took the form of Mukthaka for the yajña.</p></div>
</div>'''+talk("Viṣṇu in a Devī temple too?","Lakṣmīnārāyaṇa! In a pañcāyatana all the great gods sit together. Nobody gets left out.")))
pages.append(page('history','HISTORY','The Woḍeyars and their Goddess',tl([
 ('Legend','The yajña of Mukthaka, or of Muktarāja, at Gañjām; the Goddess appears.'),
 ('1610','<b>Rāja Woḍeyar</b> of Mysuru takes Śrīraṅgapaṭṭaṇa and makes it his capital.'),
 ('1610–17','The temple is attributed to Rāja Woḍeyar’s reign (Karnataka Tourism).'),
 ('19th c.','<b>Mummaḍi Kṛṣṇarāja Woḍeyar</b> (Kṛṣṇarāja Woḍeyar III) renovates the temple; some accounts credit him with installing the Goddess.'),
 ('Today','Managed by the Karnataka Hindu Religious and Charitable Endowments Department.')])
 +'''<div class="panel reading"><p><b>Sources differ.</b> Some sources date the temple to the mid-1500s; most link it to Rāja Woḍeyar’s reign (1578–1617, in Śrīraṅgapaṭṭaṇa from 1610); others say Mummaḍi Kṛṣṇarāja Woḍeyar built it “about 300 to 400 years ago”. Mummaḍi Kṛṣṇarāja ruled from 1799 to 1868, so his part is best read as renovation, as one source says.</p></div>'''))
pages.append(page('festivals','THROUGH THE YEAR','Festivals of Nimiṣāmbā',facts([
 ('Nimiṣāmbā Jayantī','The chief festival, on <b>Vaiśākha śukla daśamī</b> (April–May)'),
 ('Jātre','A fair in <b>Phālguna</b> (February–March), with special pūjās'),
 ('Navarātri','The nine nights of the Goddess'),
 ('Mahāśivarātri','All-night worship of Mauktikeśvara'),
 ('Every week','Crowds on vrata days: Saṅkaṣṭahara Caturthī, Navarātri and Ekādaśī'),
 ('Offerings','Abhiṣeka, alaṅkāra, ghee lamps; prasāda of sweet pongal, coconut laḍḍu and vibhūti')])
 +talk("What do people offer a goddess who's this quick?","Ghee lamps, coconuts, flowers and a lot of hope. She does the rest, in a moment!")))
pages.append(page('around','AROUND NIMIṢĀMBĀ','The island and the confluence',facts([
 ('The Kāverī','Flowing right past the temple'),
 ('Karighaṭṭa','Śrīnivāsa on his hill across the Lokapāvanī: Chikka Tirupati'),
 ('Ādi Raṅga','Raṅganātha on the island of Śrīraṅgapaṭṭaṇa'),
 ('The saṅgama','The meeting of the Kāverī branches and the Lokapāvanī, east of Gañjām')])
 +'''<div class="panel reading"><p><b>Śiva, Śakti and Viṣṇu in one view.</b> Within sight of each other stand the Goddess at Gañjām, Śrīnivāsa on Karighaṭṭa, and Raṅganātha on the island.</p>
<p>More temples around Mysuru: <a href="/bhakti/temples-of-india/around-mysuru/karighatta/">Karighaṭṭa</a>, <a href="/bhakti/temples-of-india/triranga/adi-ranga/">Ādi Raṅga</a> and <a href="/bhakti/temples-of-india/around-mysuru/nanjangud/">Nañjanagūḍu</a>.</p></div>'''))
glossary=[('Nimiṣa','the blink of an eye; a moment'),('Ambā','mother'),('Yajña','a sacred fire rite'),('Yajña-kuṇḍa','the fire pit of a yajña'),('Mauktikeśvara','Śiva of this temple, named after the sage Mukthaka'),('Śrīcakra','the Goddess as a sacred diagram (Śrī Yantra)'),('Bīja','a seed-syllable of a mantra'),('Mūla-mantra','the root mantra of a deity'),('Pañcāyatana','a temple of five deities together'),('Jayantī','an appearance-day festival'),('Vaiśākha śukla daśamī','the tenth day of the bright fortnight of Vaiśākha'),('Jātre','a temple fair'),('Saṅgama','a confluence'),('Woḍeyar','the royal house of Mysuru')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','NIMIṢĀMBĀ ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Goddess.</b> Nimiṣāmbā, Pārvatī who comes in a moment, with a stone Śrīcakra before her.</div>
<div><b>The place.</b> Gañjām on the Kāverī, just outside Śrīraṅgapaṭṭaṇa.</div>
<div><b>The legend.</b> A yajña attacked by Jānu and Sumaṇḍala, demons no weapon could harm; the sage prays, and she burns them with the fire of her eyes.</div>
<div><b>The temple.</b> A family of five shrines: Nimiṣāmbā, Mauktikeśvara, Lakṣmīnārāyaṇa, Sūrya, Gaṇapati, with Hanumān.</div>
<div><b>The festival.</b> Nimiṣāmbā Jayantī on Vaiśākha śukla daśamī; a fair in Phālguna.</div>
</div>'''+talk("One line to remember?","Call her, and she comes before you can blink. That's the promise in her name.")+'<div class="key">The Mother of the moment: <b>help in the blink of an eye</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Legend and temple:</b> Hindu Blog, “Nimishamba Temple in Ganjam”: Śiva as Mauktikeśvara or Mukthaka; Jānu and Sumaṇḍala; the weapon-proof boon; the fire from her eyes; Śiva-pañcāyatana; the shrines; the Krishna-śilā Śrīcakra with bīja and mūla-mantra; offerings; Nimiṣāmbā Jayantī on Vaiśākha śukla daśamī; the Phālguna jātre and other festivals. Hindu Blog (2013): king Sumanaska, the prince and Muktarāja; Janumaṇḍala and Sumaṇḍala. Other accounts: Mukthaka’s prayer and the Goddess from the yajña-kuṇḍa; Muktarāja of the Soma line (some say Sūrya line) carving the Śrīcakra.</p>
<p><b>History:</b> Karnataka Tourism (Rāja Woḍeyar, 1610–1617; Gañjām as a suburb of the fort); temple-information sites (Rāja Woḍeyar, 1578–1617; HRCE control); Deccan Herald (built by the mid-16th century, renovated by Mummaḍi Kṛṣṇarāja Woḍeyar); Hindupad (Mummaḍi Kṛṣṇarāja, 300–400 years ago).</p>
<p><b>Sources differ:</b> the builder and date; Śiva or the king Muktarāja as the performer of the yajña; the demons’ names; Soma or Sūrya line.</p>
<p><b>Not verified:</b> the age of the Śrīcakra (described as ancient). Mummaḍi Kṛṣṇarāja’s reign (1799–1868) is general knowledge. Maps and plans are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('deity','The Mother of the Moment'),('legends1','The Legend · The Yajña'),('legends2','The Legend · Muktarāja'),('srichakra','The Stone Śrīcakra'),('temple','The Temple'),('history','History'),('festivals','Through the Year'),('around','Around Nimiṣāmbā'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.4vw,80px)">NIMIṢĀMBĀ</h1>
  <div class="series">GAÑJĀM · ŚRĪRAṄGAPAṬṬAṆA · A REFERENCE GUIDE</div>
  <div class="tag">The Mother who comes in a moment</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>On the bank of the Kāverī, just outside Śrīraṅgapaṭṭaṇa, there is a Goddess who does not keep her devotees waiting.</p>
    <p>When demons no weapon could touch broke up a sacred yajña, a sage cried out, and the Mother came in the blink of an eye. So she is <b>Nimiṣāmbā</b>, the Mother of the moment.</p>
    <p>This guide tells her story, her Śrīcakra and her temple.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("In the blink of an eye? Really?","That's the faith of lakhs of devotees. Let's hear the story first, then you decide!")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Nimishamba.html','w').write(head+b+tail())
print('ok')
