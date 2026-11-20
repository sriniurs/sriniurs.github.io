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
head=head_red('Uttanahaḷḷi · Jvālāmukhī Tripurasundarī · Temples around Mysuru · srini.presents',
 'Jvālāmukhī Tripurasundarī of Uttanahaḷḷi, at the foot of Cāmuṇḍī Hills: Cāmuṇḍeśvarī’s sister, who helped her slay Raktabīja. The legends, the image, the Śivārcaka priests and Āṣāḍha Fridays. An illustrated reference guide.')
def tl(items): return '<div class="tl">'+''.join(f'<div><b class="yr">{y}</b> {t}</div>' for y,t in items)+'</div>'
def HILL(x,y,w,h,c='#5a8a4a'):
    return f'<path d="M{x-w/2} {y} Q{x-w/4} {y-h*0.6} {x-w/10} {y-h} Q{x} {y-h*1.06} {x+w/10} {y-h} Q{x+w/4} {y-h*0.6} {x+w/2} {y}z" fill="{c}" stroke="#111" stroke-width="2"/>'
def TEMPLE(x,y,s=1,c='#fde4e4'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-26" y="-16" width="52" height="16" fill="{c}"/><path d="M-14 -16 h28 l-4 -10 h-20z M-10 -26 h20 l-4 -10 h-12z" fill="#e2cfa8"/><circle cy="-40" r="3" fill="#e0a800"/><rect x="-5" y="-10" width="10" height="10" fill="#5a3a1a"/></g>'
def FIERCE(x,y,s=1,skin='#2b2b3a'):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-26 60 q-4 -64 26 -74 q30 10 26 74z" fill="#c0392b"/>'
     f'<path d="M-22 -4 l-24 -22 M22 -4 l24 -22 M-22 8 l-26 0 M22 8 l26 0" stroke="{skin}" stroke-width="6"/><path d="M-50 -30 l6 -14 l6 14z" fill="#bbb"/><path d="M44 -30 h12 v-12 h-12z" fill="#e0a800"/>'
     f'<circle cy="-30" r="14" fill="{skin}"/><path d="M-16 -36 q-6 -20 4 -22 M16 -36 q6 -20 -4 -22" stroke="#111" stroke-width="5" fill="none"/>'
     '<path d="M-12 -44 h24 l-4 -14 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/><circle cx="-5" cy="-33" r="2.6" fill="#fff"/><circle cx="5" cy="-33" r="2.6" fill="#fff"/><circle cy="-40" r="2" fill="#c0392b"/>'
     '<path d="M-3 -24 q3 16 6 0z" fill="#e04040"/><path d="M-10 -10 q10 6 20 0" fill="none" stroke="#ffd60a" stroke-width="3"/></g>')
def GENTLE(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-24 60 q-2 -64 24 -72 q26 8 24 72z" fill="#e05a8a"/><circle cy="-28" r="12" fill="#f2c79b"/>'
 '<path d="M-12 -38 h24 l-4 -14 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/><path d="M-20 0 l-18 -18 M20 0 l18 -18" stroke="#f2c79b" stroke-width="6"/><path d="M-40 -22 q4 -6 8 0" fill="#e05a8a"/><path d="M36 -22 l6 -10" stroke="#7a5a2a" stroke-width="3"/></g>')
def DEMON(x,y,s=1,c='#3a5a2a'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cy="-40" r="14" fill="{c}"/><path d="M-10 -52 l-5 -12 M10 -52 l5 -12"/><circle cx="-5" cy="-42" r="2.4" fill="#ffd60a"/><circle cx="5" cy="-42" r="2.4" fill="#ffd60a"/><path d="M-24 36 q24 -66 48 0z" fill="#2b2b2b"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Chamundi Hill with the hill temple on top and, at its foot, a small shrine with a fierce flame-faced Goddess">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/><circle cx="320" cy="50" r="30" fill="#ffd166" opacity=".35"/>'
 +HILL(150,268,320,190)+TEMPLE(150,82,.9)+TEMPLE(80,250,1.3)+'<path d="M300 250 q-10 -40 10 -70 q4 20 14 22 q4 -30 22 -40 q-8 30 6 48 q10 -10 6 -24 q16 30 -10 64z" fill="#ff8c1a" opacity=".55"/>'+FIERCE(300,190,1.1)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Deity','<b>Jvālāmukhī Tripurasundarī</b>, also called Jvālāmālinī: the Goddess as Śakti'),
 ('Relation','Revered as the <b>sister of Cāmuṇḍeśvarī</b>, the Goddess of Cāmuṇḍī Hills'),
 ('The battle','She helped Cāmuṇḍī slay the demon <b>Raktabīja</b>, whose every drop of blood became a new demon'),
 ('Place','<b>Uttanahaḷḷi</b>, at the foot of Cāmuṇḍī Hills, on the edge of Mysuru'),
 ('Her image','A fierce form with a long, outstretched <b>tongue</b>, compared to the Kālī of Kālīghāṭ'),
 ('Also here','The Goddess’s <b>footprints</b>; shrines of Gaṇeśa and Siddheśvara'),
 ('Worship','Under the Muzrāi (Endowments) Department; crowded on <b>Āṣāḍha Fridays</b>, with Cāmuṇḍī')])
 +talk("Cāmuṇḍī has a sister?","A fierce little sister! Most people drive straight up the hill and miss her. Big mistake, Zappy.")))
mapfig=fig(560,220,'Schematic map: Chamundi Hill with the Chamundeshwari temple on top, the hill road, and Uttanahalli with the Jwalamukhi temple at the foot; Mysuru city beside the hill. Not to scale.',
 '<rect width="560" height="220" fill="#eef6e4"/>'+HILL(300,210,340,180)+TEMPLE(300,40,.7)+T(300,16,'CĀMUṆḌEŚVARĪ',10,'#7a1d12')
 +'<path d="M150 200 C 200 160, 220 120, 280 60" stroke="#8a7a6a" stroke-width="3" stroke-dasharray="8 5" fill="none"/>'
 +TEMPLE(470,204,.8)+T(470,170,'UTTANAHAḶḶI · JVĀLĀMUKHĪ',10,'#c0392b')+'<path d="M380 150 C 420 170, 450 190, 470 200" stroke="#8a7a6a" stroke-width="3" stroke-dasharray="8 5" fill="none"/>'
 +'<rect x="10" y="150" width="90" height="60" fill="#e8e2d0" stroke="#111"/>'+T(55,140,'MYSURU',11,'#555')+T(450,24,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','At the foot of the Goddess’s hill',mapfig+'''<div class="panel reading">
<p><b>Below the hill.</b> The temple stands at <b>Uttanahaḷḷi</b>, a village at the foot of <b>Cāmuṇḍī Hills</b>, on Mysuru’s edge; a hill road branches down toward it from the top.</p>
<p><b>Raised and walled.</b> The shrine sits on slightly raised ground, inside a compound wall, with a new courtyard built around it.</p>
<p><b>One pilgrimage, two sisters.</b> Many families who worship Cāmuṇḍī on the hill also come down to pray to her sister.</p>
</div>'''))
pages.append(page('names','HER NAMES','Fire-faced, and beautiful in three worlds',facts([
 ('Jvālāmukhī','“She whose face is flame”: the fierce Goddess'),
 ('Jvālāmālinī','“Garlanded with flames”, a name used in some accounts'),
 ('Tripurasundarī','“The beauty of the three worlds”: the name of Lalitā, the gracious supreme Goddess'),
 ('Uri Māri','In a local folk story, the fiery sister born from Cāmuṇḍī’s sweat'),
 ('Ammanavaru','“The Mother”, as villagers simply call her')])
 +'''<div class="panel reading"><p><b>Fierce and gentle together.</b> The name joins two faces of the one Goddess: the flame that burns away evil, and the beauty that rules the worlds. Here she is both at once.</p></div>'''
 +talk("Why would a fierce goddess be called 'beautiful'?","Because for her devotees, the power that protects them is the most beautiful thing of all!")))
deity=fig(560,200,'The fierce Goddess in her sanctum with outstretched tongue, the festival image in a separate shrine, and footprints on a stone',
 '<rect width="560" height="200" fill="#fde4e4"/><rect x="140" y="20" width="200" height="170" fill="#fff4cd" stroke="#111" stroke-width="2"/>'+FIERCE(240,120,1.3)
 +GENTLE(430,130,.8)+T(430,192,'UTSAVA IMAGE',10,'#7a1d12')+''.join(f'<path d="M{x} 186 q-6 -14 0 -20 q6 6 0 20z" fill="#c9a26b" stroke="#111"/>' for x in (60,80))+T(70,160,'FOOTPRINTS',9,'#7a1d12'))
pages.append(page('deity','THE GODDESS','A fierce face at the foot of the hill',deity+'''<div class="g2">
<div class="card bg-red"><h4>👅 The image</h4><p>In the sanctum the Goddess has a long, outstretched <b>tongue</b>, much like the Kālī of Kālīghāṭ in Kolkata: the tongue that drank the demon’s blood.</p></div>
<div class="card bg-yellow"><h4>🪷 The festival image</h4><p>A gentler <b>utsava</b> (festival) image of Tripurasundarī has its own shrine.</p></div>
</div>
<div class="panel reading"><p><b>Footprints.</b> Stones in the temple grounds carry what devotees believe are the <b>Goddess’s footprints</b>. There are also shrines of <b>Gaṇeśa</b> and of Śiva as <b>Siddheśvara</b>.</p></div>'''))
leg1=fig(560,190,'Drops of blood falling from a demon and each becoming a new demon; the Goddess with her tongue spread out catching every drop',
 '<rect width="560" height="190" fill="#2a0805"/>'+DEMON(120,150,1.1)+''.join(DEMON(x,170,.5,'#4a6a3a') for x in (40,200,240))+''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#e04040"/>' for x,y in ((140,100),(160,120),(180,140)))
 +FIERCE(400,120,1.3,'#1a1a2a')+'<path d="M396 104 q-80 30 -200 40" stroke="#e04040" stroke-width="8" fill="none" opacity=".8"/>'+T(120,186,'RAKTABĪJA',11,'#ffd166')+T(400,186,'THE GODDESS',11,'#ffd166'))
pages.append(page('raktabija','THE LEGEND · I','Raktabīja: the demon of a thousand copies',leg1+'''<div class="steps">
<div><b>The demon.</b> In the <b>Devī Māhātmya</b>, the demon <b>Raktabīja</b>, “blood-seed”, had a terrible boon: every drop of his blood that touched the ground rose up as another Raktabīja.</div>
<div><b>An army of copies.</b> The more the Goddess’s forces wounded him, the more demons filled the battlefield.</div>
<div><b>The tongue.</b> The Goddess as <b>Cāmuṇḍā / Kālī</b> spread out her great tongue and drank every drop before it could fall, until Raktabīja was bled dry and slain.</div>
<div><b>At Uttanahaḷḷi.</b> Local tradition says it was Cāmuṇḍeśvarī’s sister, <b>Jvālāmukhī</b>, who helped her on that battlefield; hence the long tongue of her image.</div>
</div>'''+'<div class="panel reading small"><p>The full Raktabīja battle is in Chapter 8 of the Devī Māhātmya: follow our <a href="/bhakti/devi/devi-mahatmya/">Devī Māhātmya series</a>.</p></div>'))
leg2=fig(560,180,'Seven princess sisters leaving a northern city in different directions; the youngest, Chamundi, travelling south',
 '<rect width="560" height="180" fill="#fff4dc"/><rect x="230" y="20" width="100" height="50" fill="#e2cfa8" stroke="#111"/><path d="M226 20 l54 -16 l54 16z" fill="#c0392b" stroke="#111"/>'+T(280,84,'UJJAIN',10,'#7a1d12')
 +''.join(f'<g transform="translate({x} {y})">'+GENTLE(0,0,.35)+'</g>' for x,y in ((80,120),(150,140),(220,160),(340,160),(410,140),(480,120)))+'<g transform="translate(280 140)">'+FIERCE(0,0,.45,'#3a2a2a')+'</g>'+T(280,178,'CĀMUṆḌĪ, THE YOUNGEST',9,'#7a1d12'))
pages.append(page('sisters','THE LEGEND · II','Seven sisters and the sweat of the Goddess',leg2+'''<div class="steps">
<div><b>Seven daughters.</b> A local folk story says a king of Ujjain, <b>Bijjalarāya</b>, had seven warrior daughters. The eldest was Urimasaṇi, Piriyāpaṭṭaṇadamma; the youngest was <b>Cāmuṇḍī</b>.</div>
<div><b>South.</b> After a quarrel the sisters scattered across the south and settled. Only Cāmuṇḍī found no home, until she came to <b>Mahiṣamaṇḍala</b>, Mahiṣāsura’s land.</div>
<div><b>The war.</b> Mahiṣāsura wanted to marry her; she refused, and they fought. Every drop of his blood made demons. Hunting him, Cāmuṇḍī sweated, and from her sweat rose a fierce woman, <b>Uri Māri</b>, who said, “I will spread my tongue over all.”</div>
<div><b>A home for her.</b> Uri Māri drank the demon’s blood and the war was won. Grateful, Cāmuṇḍī asked her to live at the foot of the hill, at Uttanahaḷḷi. She is <b>Jvālāmukhī</b>, and those who worship Cāmuṇḍī pray to her too.</div>
</div>'''))
pages.append(page('foot','THE LEGEND · III','The sister who held the foot of the hill',fig(560,170,'Chamundi climbing the hill to fight Mahishasura at the top while her sister fights off demons at the foot',
 '<rect width="560" height="170" fill="#ffe9c4"/>'+HILL(300,170,380,150)+'<g transform="translate(300 40)">'+FIERCE(0,0,.45,'#3a2a2a')+'</g>'+DEMON(370,60,.5)
 +'<g transform="translate(120 140)">'+FIERCE(0,0,.6)+'</g>'+''.join(DEMON(x,166,.45) for x in (40,200,230)))+'''<div class="panel reading">
<p><b>An oral telling.</b> Some old Mysuru families tell it this way: when Cāmuṇḍī climbed the hill to fight Mahiṣāsura at the top, her younger sister stayed at its foot and slew as many demons as she could there, so that fewer reached the summit.</p>
<p><b>Elder or younger?</b> The tellings differ on which sister was older, and even on which demon the sister helped to kill: Raktabīja, Mahiṣāsura, or both. All agree she fought beside Cāmuṇḍī, and stayed at the hill’s foot.</p>
</div>'''+talk("So who's older, Cāmuṇḍī or Jvālāmukhī?","Depends on who's telling! In every version, though, she's the sister who never let Cāmuṇḍī fight alone.")))
pages.append(page('history','HISTORY','Royal patrons and old priests',tl([
 ('Woḍeyar times','The temple’s image is said to have been installed under the <b>Woḍeyars</b>, whose family Goddess was Cāmuṇḍeśvarī.'),
 ('Hill and foot','Researcher Shalva Pille Iyengar records that the <b>Śivārcakas</b>, the earlier priests of the Cāmuṇḍeśvarī temple, were given the Jvālāmukhī temple, renovated, after they protested when worship on the hill changed hands.'),
 ('Mummaḍi Kṛṣṇarāja','He brought priests from Kāñcīpuram to the hill temple on the advice of the Kāñci seer; old styles of worship continued at the foot of the hill.'),
 ('Today','A temple of the Karnataka Muzrāi (Endowments) Department, recently renovated, with a new courtyard around it.')])
 +'''<div class="panel reading small"><p><b>Note.</b> No dated inscription for the temple appeared in the sources we checked; the order of events in the middle rows is the researcher’s account as reported, not a recorded date.</p></div>'''))
pages.append(page('festivals','THROUGH THE YEAR','When the sisters are worshipped',facts([
 ('Āṣāḍha Fridays','The four or five Fridays of Āṣāḍha (June–July), when vast crowds come to Cāmuṇḍī Hills; the administration plans for both <b>Cāmuṇḍeśvarī</b> and <b>Tripurasundarī</b> together'),
 ('Navarātri','The nine nights of the Goddess, the time of Mysuru Dasara'),
 ('Fridays and Tuesdays','The Goddess’s days, when local families visit'),
 ('Abhiṣeka','The morning bath of the Goddess, early each day')])
 +'''<div class="panel reading"><p><b>A Mysuru vow.</b> Āṣāḍha Friday worship, kept as a <i>vrata</i> by many Mysuru families, has grown hugely in recent decades; many make the climb to Cāmuṇḍī and the visit to Uttanahaḷḷi on the same day.</p></div>'''))
pages.append(page('around','AROUND UTTANAHAḶḶI','Cāmuṇḍī Hills',facts([
 ('Cāmuṇḍeśvarī','The Goddess on the summit, family deity of the Woḍeyars'),
 ('The Nandi','The great stone bull on the hill steps, from Doḍḍa Dēvarāja’s time'),
 ('The steps','The thousand steps to the summit, built in the 17th century'),
 ('Mysuru','The palace and its temples below the hill')])
 +'''<div class="panel reading"><p>More: <a href="/bhakti/temples-of-india/around-mysuru/">Temples around Mysuru</a> · <a href="/bhakti/devi/mahishasura-mardini/">Mahiṣāsura Mardinī</a> · <a href="/bhakti/devi/devi-mahatmya/">Devī Māhātmya</a>.</p></div>'''))
glossary=[('Jvālāmukhī','she whose face is flame'),('Jvālāmālinī','garlanded with flame'),('Tripurasundarī','beauty of the three worlds; Lalitā'),('Raktabīja','“blood-seed”, the demon whose blood multiplied'),('Cāmuṇḍā','the fierce Goddess who slew Caṇḍa and Muṇḍa'),('Uri Māri','the fiery sister of the folk tale'),('Mahiṣamaṇḍala','Mahiṣāsura’s land: Mysuru'),('Śivārcaka','an old class of temple priests'),('Utsava mūrti','festival image'),('Āṣāḍha','the month of June–July'),('Vrata','a vow of worship'),('Muzrāi','the state temple department')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','UTTANAHAḶḶI ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Goddess.</b> Jvālāmukhī Tripurasundarī: flame-faced and beautiful, Cāmuṇḍī’s sister.</div>
<div><b>The place.</b> Uttanahaḷḷi, at the foot of Cāmuṇḍī Hills.</div>
<div><b>The legends.</b> She drank Raktabīja’s blood; she was born of Cāmuṇḍī’s sweat as Uri Māri; she held the foot of the hill.</div>
<div><b>The temple.</b> A long-tongued image like Kālīghāṭ’s Kālī, a festival image, the Goddess’s footprints.</div>
<div><b>The worship.</b> Āṣāḍha Fridays and Navarātri, together with Cāmuṇḍī on the hill.</div>
</div>'''+talk("One line to remember?","Before you climb to Cāmuṇḍī, greet her sister at the gate. She did the hard work at the bottom!")+'<div class="key">The sister at the foot of the hill: <b>flame-faced, ever ready</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Hindu Temples of India (blog), “Jwalamukhi Tripurasundari Temple, Uthanahalli”: sister of Cāmuṇḍī; Raktabīja; raised compound; the long-tongued image like Kālīghāṭ; utsava shrine; Gaṇeśa and Siddheśvara; footprints. Wikipedia, “Chamundeshwari Temple”: Jvālāmālinī Tripurasundarī, sister who helped slay Raktabīja. Hindupad: installed under the Woḍeyars; new courtyard. Wanderlog: Muzrāi Department.</p>
<p><b>Legends:</b> Religion World: Bijjalarāya’s seven daughters; Mahiṣamaṇḍala; Uri Māri and the tongue; Jvālāmukhī at Uttanahaḷḷi. Itslife (reader’s account): the sister at the foot of the hill. The Raktabīja story is from the Devī Māhātmya, chapter 8.</p>
<p><b>History and worship:</b> Deccan Herald, 2017 (Shalva Pille Iyengar on the Śivārcakas and Kāñci priests); Deccan Herald on Āṣāḍha Fridays and orders covering both temples.</p>
<p><b>Not verified:</b> the founding date; the Śivārcaka handover date; Navarātri and weekly practice at this temple (general). Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('deity','The Goddess'),('raktabija','Legend · Raktabīja'),('sisters','Legend · Seven Sisters'),('foot','Legend · The Foot of the Hill'),('history','History'),('festivals','Through the Year'),('around','Around Uttanahaḷḷi'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,76px)">UTTANAHAḶḶI</h1>
  <div class="series">JVĀLĀMUKHĪ TRIPURASUNDARĪ · A REFERENCE GUIDE</div>
  <div class="tag">Cāmuṇḍī’s sister at the foot of the hill</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Everyone in Mysuru knows Cāmuṇḍeśvarī on her hill. Fewer know that at the foot of that hill lives her sister.</p>
    <p>She is <b>Jvālāmukhī Tripurasundarī</b> of <b>Uttanahaḷḷi</b>: flame-faced, long-tongued, the Goddess who, the stories say, drank the demon’s blood so Cāmuṇḍī could win.</p>
    <p>This guide tells her names, her legends and her temple.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why the long tongue?","That tongue won a war! Turn the pages and you'll see how.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Uttanahalli.html','w').write(head+b+tail())
print('ok')
