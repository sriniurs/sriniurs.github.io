exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Viśālākṣī · Vārāṇasī · The 18 Śakti Pīṭhas · srini.presents',
 'Viśālākṣī of Vārāṇasī, the seventeenth of the 18 Śakti Pīṭhas: the wide-eyed Goddess of Kāśī, Satī’s jewelled earring and the name Maṇikarṇikā, Kāla Bhairava, Annapūrṇā and Viśvanātha, the Nagarathar temple of 1893 in southern style, Kajalī Tīj, and the Tamil trio of Kāmākṣī, Mīnākṣī and Viśālākṣī. An illustrated reference guide.')
def KASI(w=560,h=300):
    o=f'<rect width="{w}" height="{h}" fill="#e7f0d8"/><path d="M380 0 Q300 120 360 300 L{w} 300 L{w} 0z" fill="#9ad1f5" stroke="#111" stroke-width="2"/>'+T(470,150,'GAṄGĀ',14,'#1d4f9a')
    o+=''.join(f'<rect x="{326+(i*3)}" y="{60+i*30}" width="40" height="12" fill="#e2cfa8" stroke="#111" stroke-width="1"/>' for i in range(7))
    for nm,x,y,col,side in (('VIŚĀLĀKṢĪ (Mīr Ghāṭ)',300,150,'#c0392b','l'),('Maṇikarṇikā Ghāṭ',330,110,'#ff8c1a','l'),('Viśvanātha',250,130,'#3b6fd0','l'),('Annapūrṇā',260,170,'#bbb','l'),('Kāla Bhairava',180,80,'#333','l'),('Daśāśvamedha Ghāṭ',320,220,'#bbb','l')):
        o+=f'<circle cx="{x}" cy="{y}" r="7" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(x+(12 if side=='r' else -12),y+4,nm,11,'#111','start' if side=='r' else 'end')
    return o+T(w-10,16,'schematic, not to scale',10,'#555','end')
def VISA(x,y,s=1): return GENTLE(x,y,s).replace('#e05a8a','#c0392b')
def EYE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-40 0 q40 -30 80 0 q-40 30 -80 0z" fill="#fff"/><circle r="12" fill="#3a2a1a"/><circle r="5" fill="#111"/><circle cx="4" cy="-4" r="2" fill="#fff" stroke="none"/></g>'
def EARRING(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cy="-14" r="6" fill="#e0a800"/><path d="M-14 0 a14 14 0 1 0 28 0 a14 14 0 1 0 -28 0" fill="#e0a800"/><circle r="6" fill="#e0115f"/>'+''.join(f'<circle cx="{14*__import__("math").cos(a)}" cy="{14*__import__("math").sin(a)+16}" r="2.5" fill="#fff"/>' for a in (0.5,1.2,1.9,2.6))+'</g>'
def GOPURA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-40+k*6} {-k*16} h{80-k*12} l-2 -16 h{-(76-k*12)}z" fill="{"#f2e6c8" if k%2 else "#e8a050"}"/>' for k in range(5))+'<path d="M-14 -80 q14 -16 28 0z" fill="#e0a800"/><rect x="-12" y="-30" width="24" height="30" fill="#7a3a2a"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A large pair of eyes above the Ganga ghats at Varanasi, a jewelled earring falling toward the steps">'
 '<rect width="380" height="268" fill="#4a0e0e" rx="8"/><path d="M0 200 h380 v68 h-380z" fill="#4aa3df"/>'+''.join(f'<rect x="{i*38}" y="{180-(i%3)*6}" width="38" height="20" fill="#e2cfa8" stroke="#111" stroke-width="1"/>' for i in range(10))
 +EYE(130,80,1.3)+EYE(250,80,1.3)+EARRING(300,150,1.1)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Viśālākṣī</b>, “the wide-eyed”, a form of Pārvatī-Gaurī'),
 ('Hymn','<i>vārāṇasyāṃ viśālākṣī</i>'),
 ('Where','<b>Mīr Ghāṭ</b>, Vārāṇasī (Kāśī), Uttar Pradesh, by the Gaṅgā, near Maṇikarṇikā'),
 ('Pīṭha','Satī’s <b>earring</b> (karṇa-kuṇḍala), or its jewel, fell here'),
 ('Bhairava','<b>Kāla Bhairava</b>, the guardian of Kāśī'),
 ('Neighbours','Viśvanātha and Annapūrṇā, a short walk away'),
 ('Temple','Present building 1893, by the <b>Nāṭṭukkōṭṭai Nagarattār</b> of Tamil Nadu, in a southern style'),
 ('Festival','<b>Kajalī Tīj</b>, in Bhādrapada')])
 +talk("A Tamil-style temple in Kāśī?","Built by Tamil merchants. She's Viśvanātha's consort, so the South came north to honour her.")))
pages.append(page('where','WHERE IT IS','By the burning ghāṭ',fig(560,300,'Schematic map of central Varanasi: the ghats along the Ganga, Vishalakshi near Mir Ghat, Manikarnika Ghat just upstream, Vishvanatha and Annapurna inland, Kala Bhairava further north',KASI())
 +'<div class="g2"><div>'+minimap([16,17],'Map of India marking Gaya and Varanasi')+'</div><div class="panel reading small"><p><b>In the lanes.</b> The temple stands in the narrow lanes behind Mīr Ghāṭ, close to <b>Maṇikarṇikā</b>, the great cremation ghāṭ, and to Viśvanātha.</p><p><b>Kāśī.</b> One of the seven sacred cities and the city of liberation.</p></div></div>'))
pages.append(page('names','THE NAMES','Wide eyes, jewelled ear',facts([
 ('Viśālākṣī','<i>viśāla</i> “wide” + <i>akṣī</i> “eyed”'),
 ('Viśālākṣī Gaurī','Her fuller name in Kāśī'),
 ('Maṇikarṇī','“Jewel-eared”, after the Pīṭha legend'),
 ('Maṇikarṇikā','The ghāṭ named after the fallen ear-jewel'),
 ('Kāśī · Vārāṇasī · Avimukta','“City of light”; between the Varuṇā and Asī rivers; “never forsaken” by Śiva')])
 +talk("Why 'wide-eyed'?","Her gaze takes in the whole world, they say, and nothing escapes it. It's also a classic mark of beauty.")))
pages.append(page('pitha','THE PĪṬHA','The fallen earring',fig(560,170,'Shiva carrying Sati’s body as Vishnu’s discus cuts it, a jewelled earring falling toward river steps',
 '<rect width="560" height="170" fill="#1a0e1e"/>'+STAR+SHIVA(150,40,.7)+SATI(220,60,.9,-8)+CHAKRA(300,70,14)+EARRING(420,90,.9)+''.join(f'<rect x="{340+i*30}" y="{150-(i%2)*4}" width="30" height="14" fill="#e2cfa8" stroke="#111" stroke-width="1"/>' for i in range(7))+'<rect y="164" width="560" height="6" fill="#4aa3df"/>')+'''<div class="steps">
<div><b>The earring.</b> The Pīṭha-nirṇaya says Satī’s <b>kuṇḍala</b>, her earring, fell at Vārāṇasī; the Goddess is Viśālākṣī and the Bhairava Kāla Bhairava.</div>
<div><b>The jewel.</b> Many tellings say it was the jewel (<b>maṇi</b>) from her ear (<b>karṇa</b>), and so the place became <b>Maṇikarṇikā</b>.</div>
<div><b>Two Goddesses.</b> One tradition names two Pīṭha-goddesses in Kāśī: Viśālākṣī with Kāla Bhairava, and Annapūrṇā with Viśveśvara.</div>
<div><b>Lists vary.</b> Some later versions leave Vārāṇasī out of the 51; a few say her face fell here. The Aṣṭādaśa hymn counts her seventeenth.</div>
</div>'''))
pages.append(page('manikarnika','MAṆIKARṆIKĀ','Where Kāśī burns its dead',fig(560,170,'Steps down to the river with cremation fires burning, smoke rising, and a small square tank above the steps',
 '<rect width="560" height="170" fill="#cfd8e0"/><rect y="130" width="560" height="40" fill="#4aa3df"/>'+''.join(f'<rect x="{i*56}" y="{90+(i%2)*8}" width="56" height="40" fill="#d8c8a8" stroke="#111" stroke-width="1"/>' for i in range(10))
 +''.join(FLAME(x,118,.5) for x in (120,260,400))+''.join(f'<path d="M{x} 90 q-10 -30 6 -60" stroke="#999" stroke-width="5" fill="none"/>' for x in (120,260,400))+'<rect x="460" y="60" width="60" height="30" fill="#9fd0ea" stroke="#111"/>'+T(490,54,'KUṆḌA',10,'#111'))+facts([
 ('What','The most sacred cremation ghāṭ in India; fires burn day and night'),
 ('Belief','To die in Kāśī is liberation: Śiva whispers the <b>tāraka</b> mantra into the ear of the dying'),
 ('The kuṇḍa','Above the steps is the Maṇikarṇikā Kuṇḍa, said to have been dug by Viṣṇu at the dawn of creation'),
 ('Another legend','An earring of Śiva or Pārvatī fell into Viṣṇu’s tank; hence the name. The Pīṭha story is a third telling of the same name'),
 ('Nearby','Viśālākṣī stands only a few lanes away')])
 +talk("A Goddess temple next to the burning ghāṭ?","In Kāśī, death is the doorway. The wide-eyed Mother watches it.")))
pages.append(page('goddess','THE GODDESS','Two images, one Mother',fig(560,180,'The Goddess in a red sari and gold crown inside a small sanctum, a smaller older image behind her',
 '<rect width="560" height="180" fill="#2a1a3a"/><path d="M200 20 h160 l-20 30 h-120z" fill="#e0a800" stroke="#111" stroke-width="2"/>'+VISA(280,140,1)+'<rect x="330" y="70" width="40" height="70" rx="8" fill="#4a3a2a" stroke="#111" stroke-width="2"/>'+T(350,160,'older image',10,'#ffd166'))+facts([
 ('Form','A gracious standing Goddess, richly dressed and crowned'),
 ('Two images','Tradition says there are two: a newer one in front and an older, smaller one behind it'),
 ('Offerings','Sindūr, bangles, saris and flowers; women pray for marriage and children'),
 ('Ritual','Devotees often bathe in the Gaṅgā first, then come for darśana'),
 ('Annapūrṇā','Some say Viśālākṣī and Annapūrṇā, the giver of food, are the same Mother in two forms')])))
pages.append(page('bhairava','KĀLA BHAIRAVA','The kotwāl of Kāśī',fig(560,160,'A fierce dark god with a dog beside him, holding a staff, standing at a city gate',
 '<rect width="560" height="160" fill="#2a1a1a"/><rect x="380" y="20" width="140" height="130" fill="#6a5a4a" stroke="#111" stroke-width="2"/><rect x="420" y="70" width="60" height="80" fill="#2a1a0a"/>'
 +'<g transform="translate(220 150)">'+person(0,0,'#1a1a3a','#3a3a5a',1.3)+'<path d="M28 -10 v-70" stroke="#c9a26b" stroke-width="5"/></g><g transform="translate(300 146)" stroke="#111" stroke-width="2"><ellipse rx="24" ry="10" fill="#111"/><circle cx="-24" cy="-10" r="9" fill="#111"/><path d="M-30 -18 l-4 -8 l8 4z" fill="#111"/></g>')+facts([
 ('Who','Śiva’s fierce form; Viśālākṣī’s Bhairava'),
 ('Role','The <b>kotwāl</b>, police chief and guardian of Kāśī: no one may live or die there without his leave'),
 ('Brahmā’s head','Bhairava cut off Brahmā’s fifth head; it stuck to his hand until he reached Kāśī, where it fell'),
 ('Pilgrims','Many visit Kāla Bhairava first, to ask permission to stay in the city'),
 ('His vehicle','A dog')])))
pages.append(page('vishvanatha','VIŚVANĀTHA AND ANNAPŪRṆĀ','The household of Kāśī',facts([
 ('Viśvanātha','Śiva as Lord of the Universe, the Jyotirliṅga of Kāśī: Viśālākṣī’s Lord'),
 ('Annapūrṇā','The Goddess of food, who feeds all who live in Kāśī; her temple is near Viśvanātha'),
 ('Ḍhuṇḍhirāja','Gaṇeśa, who must be greeted near Viśvanātha'),
 ('Six key places','A pilgrimage to Kāśī is said to include the Gaṅgā, Viśvanātha, Viśālākṣī, Kāla Bhairava, Ḍhuṇḍhirāja and Daṇḍapāṇi')])
 +'<div class="key">Full guide: <a href="/bhakti/temples-of-india/12-jyotirlingas/kashi-vishwanath/">Kāśī Viśvanātha</a></div>'
 +talk("Father, mother, guardian, son?","Viśvanātha, Viśālākṣī and Annapūrṇā, Kāla Bhairava, Ḍhuṇḍhirāja. Kāśī is one divine family's home.")))
pages.append(page('temple','THE TEMPLE','The South in the lanes of Kāśī',fig(560,200,'A small temple with a colourful southern-style gateway tower at the end of a narrow lane, lions carved beside the door',
 '<rect width="560" height="200" fill="#efe4cc"/><rect x="0" y="0" width="140" height="200" fill="#d8c8a8" stroke="#111"/><rect x="420" y="0" width="140" height="200" fill="#d8c8a8" stroke="#111"/>'+GOPURA(280,196,1.6)
 +''.join(f'<g transform="translate({x} 190)" stroke="#111"><rect x="-12" y="-20" width="24" height="20" fill="#e8b84a"/><circle cy="-26" r="8" fill="#e8b84a"/></g>' for x in (200,360)))+facts([
 ('Built','<b>1893</b>, by the <b>Nāṭṭukkōṭṭai Nagarattār</b> (Chettiars), a merchant community from Chettinad, Tamil Nadu'),
 ('Style','A North Indian haveli-like building with southern features: a small Dravidian gopuram at the entrance'),
 ('Gateway','Carved lions at the door and a relief of Lakṣmī above'),
 ('Inside','Painted pillars before the shrine, and many Śiva-liṅgas around it'),
 ('Renewed','Renovated again in 1971 with the help of South Indian devotees')])
 +talk("Why would Tamil merchants build here?","The Nagarattār have served Kāśī for generations, funding rites at Viśvanātha too. For them, Kāśī is home.")))
pages.append(page('trio','KĀMĀKṢĪ, MĪNĀKṢĪ, VIŚĀLĀKṢĪ','The three “eyed” Goddesses',facts([
 ('Kāmākṣī','Kāñcī: “eyes of love”; also a Śakti Pīṭha (No. 2)'),
 ('Mīnākṣī','Madurai: “fish-eyed”'),
 ('Viśālākṣī','Kāśī: “wide-eyed”'),
 ('The saying','In Tamil homes the three are named together as the great Goddesses of Kāñcī, Madurai and Kāśī'),
 ('Why it matters','It explains the southern devotion to this northern shrine, and the Nagarattār temple')])
 +'<div class="key">See also: <a href="/bhakti/temples-of-india/18-shakti-peethas/kamakshi/">Kāmākṣī of Kāñcī</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','Kajalī Tīj and Navarātri',facts([
 ('Kajalī Tīj','The temple’s own festival: the third day of the dark fortnight of <b>Bhādrapada</b>, at the end of the rains; women sing kajalī songs'),
 ('Navarātri','Both seasons; the autumn one with Durgā Pūjā'),
 ('Annakūṭa','After Dīpāvalī, with Annapūrṇā'),
 ('Daily','Bath in the Gaṅgā, darśana, and sindūr for married women')])))
pages.append(page('history','HISTORY','Old shrine, new temple',tl([
 ('Purāṇas','The Devī Bhāgavata and Kāśī Khaṇḍa praise Viśālākṣī of Kāśī.'),
 ('Medieval','The shrine shares Kāśī’s many destructions and rebuildings.'),
 ('18th c.','Kāśī’s temples revive under the Marāṭhās; Ahilyābāī Holkar rebuilds Viśvanātha (1780).'),
 ('1893','The <b>Nagarattār</b> build the present Viśālākṣī temple.'),
 ('1971','Further renovation with South Indian help.')])
 +'<div class="panel reading small"><p><b>Origins.</b> No firm date is known for the first shrine; tradition places it in the Purāṇic past.</p></div>'))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Viśāla','Wide'),('Akṣī','Eyed'),('Maṇi','Jewel'),('Karṇa','Ear'),('Kuṇḍala','Earring'),('Tāraka mantra','The “crossing-over” mantra'),
 ('Kotwāl','Town police chief'),('Avimukta','Never forsaken'),('Ghāṭ','River steps'),('Kajalī','Rain-season songs of Bhādrapada')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Pīṭha.</b> Satī’s earring, or its jewel, in Kāśī: Viśālākṣī, the wide-eyed.</div>
<div><b>The place.</b> By Maṇikarṇikā, where Kāśī burns its dead and Śiva whispers liberation.</div>
<div><b>The family.</b> Viśvanātha her Lord, Annapūrṇā beside her, Kāla Bhairava at the gate.</div>
<div><b>The temple.</b> Built by Tamil Nagarattār merchants in 1893, with a southern gopuram.</div>
<div><b>The trio.</b> Kāmākṣī, Mīnākṣī, Viśālākṣī.</div>
</div>'''+talk("One line to remember?","In the city of last breaths, the Mother keeps her eyes wide open.")+'<div class="key">The seventeenth seat of the Mother: <b>Viśālākṣī of Vārāṇasī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Vishalakshi Temple” (Mīr Ghāṭ; Kāla Bhairava; jewel from Satī’s right earring, Maṇikarṇī; 1893 by the Nāṭṭukkōṭṭai Nagarattār; haveli style with a small Dravidian gopura; Kajalī Tīj in the dark fortnight of Bhādrapada; two Pīṭha goddesses, Viśālākṣī and Annapūrṇā; some versions omit Vārāṇasī; 1971 renovation; Kāśī’s six key places). greenmesg.org (Pīṭha-nirṇaya: kuṇḍala, Viśālākṣī, Kālabhairava). astroved.com (lions; Lakṣmī relief). trawell.in and pilgrimaide.com (gopuram; liṅgas; painted pillars). optimatravels.com (Devī Bhāgavata; festivals). yatradham (face also said to have fallen). thedivineindia.com (Annapūrṇā as Viśālākṣī). temples-site (Ahilyābāī; 1971).</p>
<p><b>Sources differ:</b> earring, jewel, or face; whether Vārāṇasī is among the 51. <b>Not verified, tradition only:</b> the two images; the Tamil saying as phrased; Bhairava’s permission. Maps are schematic. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('pitha','The Pīṭha'),('manikarnika','Maṇikarṇikā'),('goddess','The Goddess'),('bhairava','Kāla Bhairava'),('vishvanatha','Viśvanātha and Annapūrṇā'),
 ('temple','The Temple'),('trio','Kāmākṣī, Mīnākṣī, Viśālākṣī'),('festivals','Through the Year'),('history','History'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 17 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,7vw,70px)">VIŚĀLĀKṢĪ</h1>
  <div class="series">VĀRĀṆASĪ · A REFERENCE GUIDE</div>
  <div class="tag">The wide-eyed Mother of Kāśī</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>In the narrow lanes of Kāśī, a few steps from the ghāṭ where the city’s funeral fires never go out, stands the shrine of <b>Viśālākṣī</b>, the wide-eyed Goddess, wife of Viśvanātha. Here, tradition says, the jewel of Satī’s earring fell, and gave Maṇikarṇikā its name.</p>
    <p>Her temple, oddly for the North, has a small Tamil gateway: it was built by merchants from Chettinad, for whom she is one of three great “eyed” Goddesses, with Kāmākṣī and Mīnākṣī.</p>
    <p>This guide tells her story, her neighbours in Kāśī and the people who keep her temple.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Viśālākṣī Mā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Most pilgrims go to Viśvanātha. Do they miss her?","Many do, sadly. Tradition says a Kāśī pilgrimage without Viśālākṣī is incomplete.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Vishalakshi_Varanasi.html','w').write(head+b+tail())
print('ok',len(pages))
