exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Jvālāmukhī · Vaiṣṇavī of Jvālā · The 18 Śakti Pīṭhas · srini.presents',
 'Jvālāmukhī in the Kangra valley, the fifteenth of the 18 Śakti Pīṭhas: the Goddess as living flames with no image, Satī’s tongue, the nine flames, Vaiṣṇavī in the hymn, Akbar’s umbrella and Dhyānu Bhagat, Gorakhnāth’s boiling pot, the Katoch kings and Ranjit Singh’s gilded dome, and the natural gas beneath. An illustrated reference guide.')
def k(lat,lon): return 40+(lon-75.95)*900, 20+(32.3-lat)*450
def KMAP(w=560,h=300):
    o=f'<rect width="{w}" height="{h}" fill="#e7f0d8"/>'+''.join(f'<path d="M{x} 50 l40 -40 l40 40z" fill="#fff" stroke="#888"/>' for x in (180,260,340,420,500))+T(470,64,'DHAULĀDHĀR',11,'#555')
    a=k(32.2,76.6);b=k(31.95,76.2);c=k(31.85,75.95)
    o+=f'<path d="M{a[0]:.0f} {a[1]+40:.0f} Q{k(32.0,76.4)[0]:.0f} {k(32.0,76.4)[1]:.0f} {b[0]:.0f} {b[1]:.0f} T{c[0]:.0f} {c[1]+20:.0f}" stroke="#4aa3df" stroke-width="7" fill="none"/>'+T(f'{b[0]-10:.0f}',f'{b[1]-14:.0f}','BEĀS',11,'#1d4f9a','end')
    for nm,la,lo,col,side in (('JVĀLĀMUKHĪ',31.876,76.324,'#c0392b','r'),('Kāṅgṛā (Vajreśvarī)',32.10,76.27,'#bbb','r'),('Cāmuṇḍā',32.15,76.36,'#bbb','r'),('Dharamshala',32.22,76.32,'#bbb','l'),('Cintpūrṇī',31.80,76.03,'#bbb','r')):
        x,y=k(la,lo); r=8 if col=='#c0392b' else 6
        o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',nm,12,'#111','start' if side=='r' else 'end')
    return o+T(w-10,h-8,'simplified, not to scale',10,'#555','end')
def FLAMES(x,y,s=1,n=9): return f'<g transform="translate({x} {y}) scale({s})">'+''.join(f'<g transform="translate({(i-(n-1)/2)*26} {(i%3)*8})"><path d="M-9 0 q-4 -20 6 -32 q2 12 6 14 q4 -10 2 -18 q12 16 -2 36z" fill="{"#4aa3ff" if i%2 else "#ff8c1a"}" stroke="#111" stroke-width="1.2"/><path d="M-3 0 q-2 -10 3 -14 q2 6 4 6 q2 -2 0 -6 q6 8 -2 14z" fill="#ffd60a"/></g>' for i in range(n))+'</g>'
def CHATRA(x,y,s=1,c='#e0a800'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-40 0 q40 -40 80 0z" fill="{c}"/><path d="M0 0 v40"/><path d="M-40 0 q10 6 20 0 q10 6 20 0 q10 6 20 0 q10 6 20 0" fill="none"/></g>'
def DOME(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-80" y="-50" width="160" height="50" fill="#f2e6c8"/><rect x="-20" y="-40" width="40" height="40" fill="#cfd8e0"/>'
 '<path d="M-50 -50 q0 -50 50 -70 q50 20 50 70z" fill="#e0a800"/><circle cy="-124" r="6" fill="#e0a800"/><path d="M0 -130 v-14"/>'+''.join(f'<path d="M{dx} -50 q0 -20 10 -30 q10 10 10 30z" fill="#e0a800"/>' for dx in (-80,60))+'</g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Blue and orange flames rising from cracks in a rock wall inside a temple, a golden dome above">'
 '<rect width="380" height="268" fill="#2a0e0e" rx="8"/><rect x="40" y="150" width="300" height="90" fill="#6a5a4a" stroke="#111" stroke-width="2"/>'+FLAMES(190,200,1.2)+DOME(190,120,.8)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Jvālāmukhī</b>, “the flame-mouthed”, or Jvālā Jī; <b>Vaiṣṇavī</b> in the hymn'),
 ('Form','No image: <b>flames</b> that burn on their own from cracks in the rock'),
 ('Where','<b>Jawalamukhi</b> town, Kangra district, Himachal Pradesh, below the Dhaulādhār range'),
 ('Pīṭha','Satī’s <b>tongue</b> (jihvā) fell here'),
 ('Hymn','<i>jvālāyāṃ vaiṣṇavī devī</i>: “Vaiṣṇavī Devī at Jvālā”'),
 ('Flames','Nine, by the usual count, for nine forms of the Goddess'),
 ('Temple','Built first by Rājā <b>Bhūmi Cand</b> Katoch; gilded dome from <b>Ranjit Singh</b>'),
 ('Legends','Akbar’s golden umbrella; Dhyānu Bhagat; Gorakhnāth’s pot')])
 +talk("A goddess who is fire?","No stone, no metal: just flame from the earth. Here the Mother speaks with a tongue of fire.")))
pages.append(page('where','WHERE IT IS','The Kangra valley',fig(560,300,'Simplified map of the Kangra valley: Jwalamukhi south of Kangra town and Chamunda, below the snowy Dhauladhar, with Chintpurni to the south-west and the Beas river',KMAP())
 +'<div class="g2"><div>'+minimap([15],'Map of India with Jwalamukhi marked in Himachal Pradesh')+'</div><div class="panel reading small"><p><b>Devī’s valley.</b> Kangra is full of goddess shrines: Vajreśvarī at Kangra town, Cāmuṇḍā near Dharamshala, Cintpūrṇī to the south-west, and Jvālā Jī in the low hills between.</p></div></div>'))
pages.append(page('names','THE NAMES','Flame-mouth, Vaiṣṇavī',facts([
 ('Jvālāmukhī','<i>jvālā</i> “flame” + <i>mukhī</i> “mouthed”'),
 ('Jvālā Jī · Jvālā Devī','The everyday names'),
 ('Vaiṣṇavī','The hymn’s name: the Goddess as Viṣṇu’s power'),
 ('Nagarkoṭ','An old name of the Kangra fort and kingdom, often used for the region'),
 ('Unmatta Bhairava','Her Bhairava in the Pīṭha lists')])))
pages.append(page('pitha','THE PĪṬHA','Where the tongue fell',fig(560,170,'Shiva carrying Sati’s body as Vishnu’s discus cuts it, a small flame falling onto Himalayan foothills',
 '<rect width="560" height="170" fill="#1a0e1e"/>'+STAR+SHIVA(150,40,.7)+SATI(220,60,.9,-8)+CHAKRA(300,70,14)+'<path d="M300 170 Q400 100 520 170z" fill="#3a6a3a"/>'+FLAMES(410,130,.6,3))+'''<div class="steps">
<div><b>The tongue.</b> When Satī’s body was cut by Viṣṇu’s discus, her <b>tongue</b> fell in these hills.</div>
<div><b>Fire with it.</b> Some tellings say the fire of her yogic power fell with it, or her burning clothes, and the flame has never gone out.</div>
<div><b>No image needed.</b> So the Goddess is worshipped here as flame alone.</div>
</div>'''+talk("Why a tongue, and why fire?","The tongue speaks and tastes; Agni, fire, is called the gods' tongue. The two go together.")))
pages.append(page('flames','THE NINE FLAMES','Nine forms of the Mother',fig(560,180,'A rock wall inside the sanctum with nine flames of blue and orange coming out of cracks, priests offering at a pit in front',
 '<rect width="560" height="180" fill="#3a2a1a"/><rect x="60" y="40" width="440" height="120" fill="#6a5a4a" stroke="#111" stroke-width="2"/>'+FLAMES(280,120,1.4)+'<rect x="200" y="150" width="160" height="20" fill="#2a1a0a" stroke="#111"/>')+'<table class="ct"><tr><th>#</th><th>Flame</th><th>#</th><th>Flame</th></tr>'
 +''.join(f'<tr><td>{2*i+1}</td><td><b>{a}</b></td><td>{2*i+2 if b else ""}</td><td><b>{b}</b></td></tr>' for i,(a,b) in enumerate((('Mahākālī','Annapūrṇā'),('Caṇḍī','Hiṅglāj'),('Vindhyavāsinī','Mahālakṣmī'),('Sarasvatī','Ambikā'),('Añjanī','')))) +'</table>'
 +facts([('Fuel','No oil, no wick: the flames rise from gaps in the rock'),('Offerings','Flowers, sweets and milk are offered into pits before the flames'),('Count','Most say nine; some say seven, for seven divine sisters')])))
pages.append(page('vaishnavi','VAIṢṆAVĪ AT JVĀLĀ','Which Goddess does the hymn mean?','''<div class="g2">
<div class="card bg-red"><h4>🔥 Jvālāmukhī</h4><p>Most lists of the Aṣṭādaśa Pīṭhas read <i>jvālāyām</i> as “at Jvālā” and place No. 15 here, at the flames of Kangra, with Satī’s tongue.</p></div>
<div class="card bg-blue"><h4>🏔️ Vaiṣṇo Devī</h4><p>Some readers take <i>vaiṣṇavī devī</i> as <b>Vaiṣṇo Devī</b> of the Trikūṭa hills in Jammu, whose cave also holds a sacred flame. That shrine is not usually counted among the 51 Pīṭhas.</p></div>
</div>
<div class="panel reading"><p><b>The usual answer.</b> This series follows the common reading: Jvālāmukhī is the Pīṭha, and “Vaiṣṇavī” is a name of the Goddess there, the power of Viṣṇu.</p></div>'''
 +talk("Is it the same Goddess anyway?","Pilgrims on the Nau Devī circuit visit both. To them, she's one Mother in many hills.")))
pages.append(page('bhumichand','LEGEND · THE COWHERD AND THE KING','How the flames were found',fig(560,170,'A cowherd watching a little girl drinking milk from his cow at the forest edge; then a king’s soldiers finding flames in the rock',
 '<rect width="560" height="170" fill="#e7f0d8"/>'+person(90,150,'#ffd60a','#c98b5a',1)+'<g transform="translate(190 150)" stroke="#111" stroke-width="2"><rect x="-30" y="-30" width="56" height="24" rx="8" fill="#fff"/><circle cx="32" cy="-30" r="10" fill="#fff"/><path d="M-24 -6 v18 M16 -6 v18"/></g>'+person(250,150,'#c0392b','#f2c79b',.6)
 +'<path d="M300 100 h30" stroke="#111" stroke-width="3"/><path d="M330 100 l-10 -6 v12z" fill="#111"/><rect x="360" y="110" width="160" height="50" fill="#6a5a4a" stroke="#111"/>'+FLAMES(440,140,.7,5)+KING(380,104,.7))+'''<div class="steps">
<div><b>The cow.</b> A cowherd found his cow giving no milk. He followed her and saw a little girl come out of the forest and drink it.</div>
<div><b>The dream.</b> He told the king, <b>Bhūmi Cand Katoch</b> of Kangra, a devotee of Durgā, who had dreamt of a sacred place in the hills.</div>
<div><b>The flames.</b> The king’s men searched and found flames burning from the rock. Bhūmi Cand built a temple around them and appointed priests.</div>
<div><b>The Pāṇḍavas.</b> Tradition adds that the Pāṇḍavas came later and renewed the temple.</div>
</div>'''))
pages.append(page('akbar','LEGEND · AKBAR’S UMBRELLA','The fire that would not go out',fig(560,180,'Soldiers pouring water channels onto flames that keep burning; an emperor offering a golden umbrella that turns dull',
 '<rect width="560" height="180" fill="#3a2a1a"/><rect x="40" y="90" width="220" height="70" fill="#6a5a4a" stroke="#111"/>'+FLAMES(150,140,.8,5)+'<path d="M40 60 q60 0 80 60" stroke="#4aa3df" stroke-width="10" fill="none"/>'
 +KING(360,160,1.1,'#2a5a3a')+CHATRA(450,90,.9)+'<path d="M450 70 l20 -20 M470 90 l20 -6" stroke="#ffd166" stroke-width="2"/>'+CHATRA(510,130,.5,'#8a6a4a'))+'''<div class="steps">
<div><b>The test.</b> The Mughal emperor <b>Akbar</b>, the story goes, heard of the flames and set out to put them out: he had water channelled onto them, and tried to smother them with iron.</div>
<div><b>They burned on.</b> The flames kept burning. Humbled, Akbar offered the Goddess a <b>golden umbrella</b> (chatra).</div>
<div><b>Refused.</b> The gold turned into a dull, unknown metal: the Goddess, says the legend, did not accept it.</div>
<div><b>Still there.</b> A metal umbrella is kept in the temple; it is brass or copper. Whether it is Akbar’s is unknown.</div>
</div>'''+talk("Did Akbar really come?","He campaigned in these hills, so it's possible. The umbrella story is legend; the metal umbrella is real.")))
pages.append(page('dhyanu','LEGEND · DHYĀNU BHAGAT','A devotee’s head',facts([
 ('Who','<b>Dhyānu Bhagat</b>, a devotee of Jvālā Jī in Akbar’s time, leading pilgrims to the shrine'),
 ('The challenge','Akbar, the story goes, stopped the pilgrims and cut off the head of Dhyānu’s horse: “If your Goddess is real, let her restore it”'),
 ('The answer','Dhyānu prayed at the flames, offering his own head; the Goddess restored the horse, and Dhyānu too'),
 ('Remembered','Dhyānu is credited with spreading the Goddess’s fame; a 1978 film tells his story')])
 +talk("Same story as the umbrella?","Two halves of one legend: first the miracle, then the emperor's gift.")))
pages.append(page('gorakh','GORAKH ḌIBBĪ','The pot that boils cold',fig(560,170,'A small pool of water bubbling as if boiling, a yogi with a begging bowl walking away',
 '<rect width="560" height="170" fill="#fdf1e8"/><ellipse cx="220" cy="130" rx="80" ry="22" fill="#9fd0ea" stroke="#111" stroke-width="2"/>'+''.join(f'<circle cx="{180+i*20}" cy="{124+(i%2)*6}" r="5" fill="#fff" stroke="#4aa3df"/>' for i in range(5))+person(430,150,'#ff8c1a','#c98b5a',1)+'<ellipse cx="456" cy="120" rx="10" ry="5" fill="#7a5a2a"/>')+facts([
 ('Where','A small shrine just above the main temple'),
 ('Legend','<b>Gorakhnāth</b>, the great yogi, came here. The Goddess put water on to heat for him while he went to beg for rice. He never came back, so the water waits for him, still bubbling'),
 ('The pool','The water bubbles as if boiling but is cold to the touch: gas rising through it'),
 ('Flame','A flame can be lit just above its surface')])
 +talk("Boiling but cold?","Gas bubbles, not heat. The legend says it's still waiting for Gorakhnāth's rice.")))
pages.append(page('science','THE SCIENCE OF THE FLAME','Gas from the earth',facts([
 ('What burns','<b>Natural gas</b> seeping up through cracks in the rock, mostly methane'),
 ('Lit by','Kept lit by the priests; once lit, the jets burn steadily'),
 ('Below','Geologists link the seeps to gas-bearing rocks in the Himalayan foothills'),
 ('Exploration','The area has been surveyed for gas; the shrine’s flames have never been tapped'),
 ('Belief','For devotees, the cause doesn’t matter: the flame that rises unbidden from the earth is the Goddess')])
 +talk("So it's just gas?","The gas is how. Why here, and why for so many centuries, is the question pilgrims answer with faith.")))
pages.append(page('temple','THE TEMPLE','Gold dome, silver doors',fig(560,200,'A temple with a gilded dome and pinnacles, silver doors, set against green hills',
 '<rect width="560" height="200" fill="#cfe3f5"/>'+HILL(100,200,240,100,'#3a7a3a')+HILL(460,200,240,100,'#3a7a3a')+DOME(280,190,1.2))+facts([
 ('Style','A modern building, often called <b>Indo-Sikh</b>, set against a hill'),
 ('Dome','Gilded with gold given by <b>Mahārājā Ranjit Singh</b>'),
 ('Doors','Silver-plated folding doors from his son <b>Kharak Singh</b>'),
 ('Bell','A great bell given by a king of Nepal, by tradition'),
 ('Sanctum','A square pit in the floor with the flames in the rock wall'),
 ('Around','Gorakh Ḍibbī, the Caturbhuj temple and smaller shrines')])))
pages.append(page('history','HISTORY','Katoch, Mughal and Sikh',tl([
 ('Legend','The Pāṇḍavas worship here; the Mahābhārata praises the region.'),
 ('Medieval','Rājā <b>Bhūmi Cand</b> Katoch of Kangra builds the first temple.'),
 ('16th c.','<b>Akbar</b>’s campaigns in the hills; the umbrella and Dhyānu legends.'),
 ('1809','<b>Ranjit Singh</b> meets the Kangra ruler <b>Sansār Cand</b> here and seals an agreement at the temple.'),
 ('c. 1813–15','Ranjit Singh gilds the dome in thanksgiving.'),
 ('Later','Kharak Singh’s silver doors; the present temple completed in the 19th century.')])
 +'<div class="panel reading small"><p><b>Dates differ:</b> sources give 1809, 1813 or 1815 for Ranjit Singh’s visit and gift, and 1835 for the completion of the present building.</p></div>'))
pages.append(page('naudevi','THE NAU DEVĪ CIRCUIT','Nine goddesses of the hills',facts([
 ('Jvālā Jī','Kangra: the flames'),('Vajreśvarī','Kangra town: the fortress goddess'),('Cāmuṇḍā','Near Dharamshala'),('Cintpūrṇī','Una: she who ends worry'),
 ('Nainā Devī','Bilaspur: on a hilltop above the Gobind Sagar'),('Mansā Devī','Near Chandigarh'),('Kālikā','Kalka'),('Śākambharī','Saharanpur'),('Vaiṣṇo Devī','Jammu: the cave of the three Mothers')])
 +talk("Pilgrims do all nine?","Many do, in one long journey through the hills. Jvālā Jī is the fiery heart of it.")))
pages.append(page('festivals','THROUGH THE YEAR','Two Navarātris',facts([
 ('Navarātri','Both, in <b>Caitra</b> (spring) and <b>Āśvina</b> (autumn): great fairs at the temple'),
 ('Ārtī','Five times a day the flames receive ārtī'),
 ('Offerings','Rabri, milk, sweets and coconuts; the flames “taste” them, by belief'),
 ('Melā','Crowds from Punjab and Himachal, singing <i>bheṭeṃ</i>, the Mother’s songs')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Jvālā','Flame'),('Mukha','Mouth, face'),('Jihvā','Tongue'),('Chatra','Umbrella, canopy'),('Ḍibbī','Small box or pot'),('Bhagat','Devotee'),('Nau','Nine (Hindi)'),('Bheṭ','Devotional song to the Mother')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Pīṭha.</b> Satī’s tongue in the Kangra hills: Vaiṣṇavī of Jvālā in the hymn.</div>
<div><b>The Goddess.</b> Nine flames from the rock, no image, no fuel but the earth’s own gas.</div>
<div><b>The legends.</b> The cowherd and King Bhūmi Cand; Akbar’s refused umbrella; Dhyānu’s head; Gorakhnāth’s pot.</div>
<div><b>The temple.</b> Katoch first, gold dome from Ranjit Singh, silver doors from Kharak Singh.</div>
<div><b>The circuit.</b> The fiery heart of the Nau Devī pilgrimage.</div>
</div>'''+talk("One line to remember?","An emperor tried to drown her flame; she kept burning, and kept his gold out.")+'<div class="key">The fifteenth seat of the Mother: <b>Jvālāmukhī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Jawalamukhi” (Bhūmi Cand’s dream and temple; gilded dome, pinnacles, silver door; Dhaulādhār; flames from natural gas; Akbar’s umbrella turning to an unknown metal; Ranjit Singh 1815; pit above the temple). Wikipedia, “Jwala Ji” (natural cave and gas; Pāṇḍavas renewing the temple; tongue and fire or clothes falling; Dhyānu Bhagat film 1978; seven or nine flames). bharattemples.com (tongue; nine flames named; Kharak Singh’s silver doors). esamskriti.com (umbrella is brass or copper; Akbar’s visit likely but unconfirmed). static.jatland.com (water channel; 1809 agreement with Sansār Cand; dome after the Afghan war). pilgrimaide.com (completed 1835; Dhyānu popularised the shrine). praveenmusafir.com (cowherd and girl; Nepal bell). samanyagyan.com and boldsky.com (Gorakh Ḍibbī; Gorakhnāth). dinamalar (1813; flames from gaps in rock).</p>
<p><b>Sources differ:</b> 1809, 1813 or 1815 for Ranjit Singh; seven or nine flames; whether the hymn’s Vaiṣṇavī means this shrine or Vaiṣṇo Devī. <b>Not verified, tradition only:</b> Dhyānu’s horse; Akbar’s visit; Gorakh Ḍibbī’s story; gas exploration nearby; the Nau Devī list as given. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('pitha','The Pīṭha'),('flames','The Nine Flames'),('vaishnavi','Vaiṣṇavī at Jvālā'),('bhumichand','Legend · The Cowherd and the King'),('akbar','Legend · Akbar’s Umbrella'),
 ('dhyanu','Legend · Dhyānu Bhagat'),('gorakh','Gorakh Ḍibbī'),('science','The Science of the Flame'),('temple','The Temple'),('history','History'),('naudevi','The Nau Devī Circuit'),('festivals','Through the Year'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 15 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,7vw,70px)">JVĀLĀMUKHĪ</h1>
  <div class="series">VAIṢṆAVĪ OF JVĀLĀ · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess who is a living flame</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>In the low hills of Kangra, inside a temple with a golden dome, there is no statue. There is a rock wall, and out of its cracks rise small flames, blue and orange, burning without oil or wick. This is <b>Jvālāmukhī</b>, the flame-mouthed Goddess, where Satī’s tongue fell.</p>
    <p>A cowherd found her; a king built her temple; an emperor, the story goes, tried to put her out and then offered her gold, which she refused. A Sikh mahārājā gilded her dome.</p>
    <p>This guide tells those stories, counts the flames, and looks at what science says burns here.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mātā Jvālā Jī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Have the flames ever gone out?","Not in living memory, and legend says never. The priests keep watch, just in case.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Jvalamukhi.html','w').write(head+b+tail())
print('ok',len(pages))
