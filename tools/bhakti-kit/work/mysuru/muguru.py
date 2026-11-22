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
head=head_red('Mūgūru · Tripurasundarī (Tibbādevī) and Deśeśvara · Temples around Mysuru · srini.presents',
 'Tripurasundarī of Mūgūru, called Tibbādevī, in T. Narasīpura taluk, with the Deśeśvara Śiva temple beside her: the black-stone Goddess with the Śrīcakra at her feet, the legend of Nawab Baba Saheb and the sprouting stalk, Mūkāsura and the village name, the Chiguru Oḍeyuva Jātre of the sister goddesses, the Jain heritage and the Śrīvidyā link. An illustrated reference guide.')
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
def STALK(x,y,s=1,leaf=True):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M0 0 v-60" stroke="#c9a26b" stroke-width="4"/>'
    if leaf: g+=''.join(f'<path d="M0 {-14-i*14} q{14*(1 if i%2 else -1)} -8 {22*(1 if i%2 else -1)} -2 q-10 6 -22 2z" fill="#6ac46a"/>' for i in range(4))
    return g+'</g>'
def LINGA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse cy="0" rx="30" ry="9" fill="#6a6a60"/><path d="M-12 0 v-30 q12 -16 24 0 v30z" fill="#3a3a3a"/><path d="M-8 -22 h16 M-8 -18 h16 M-8 -14 h16" stroke="#fff" stroke-width="1.5"/><circle cy="-26" r="2.5" fill="#c0392b"/></g>'
def SEATED(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 40 q-4 -46 30 -54 q34 8 30 54z" fill="#2b2b3a"/><path d="M-30 40 h60" stroke="#e0a800" stroke-width="3"/>'
 '<circle cy="-24" r="13" fill="#2b2b3a"/><path d="M-11 -34 h22 l-3 -13 l-5 5 l-3 -9 l-3 9 l-5 -5z" fill="#e0a800"/><circle cx="-4" cy="-26" r="2" fill="#fff"/><circle cx="4" cy="-26" r="2" fill="#fff"/><circle cy="-31" r="1.8" fill="#c0392b"/>'
 '<path d="M-22 0 l-20 -16 M22 0 l20 -16" stroke="#2b2b3a" stroke-width="6"/><path d="M-24 52 l24 -14 l24 14 l-24 14z" fill="none" stroke="#e0a800" stroke-width="2"/><path d="M-12 52 l12 -7 l12 7 l-12 7z" fill="none" stroke="#e0a800" stroke-width="1.5"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A walled village temple with an arched gateway and a tower of goddess figures; beside it a small Shiva shrine; a sprouting stalk in the foreground">'
 '<rect width="380" height="268" fill="#7a1d12" rx="8"/><circle cx="320" cy="50" r="30" fill="#ffd166" opacity=".35"/><rect y="220" width="380" height="48" fill="#6a8a3a"/>'
 '<rect x="60" y="130" width="190" height="90" fill="#f2e2c4" stroke="#111" stroke-width="2"/>'+''.join(f'<circle cx="{70+i*19}" cy="128" r="5" fill="#e05a8a" stroke="#111"/>' for i in range(10))
 +'<path d="M140 220 v-50 q15 -22 30 0 v50z" fill="#5a3a1a" stroke="#111" stroke-width="2"/>'+TEMPLE(155,120,1.6,'#fde4e4')
 +TEMPLE(300,214,1.0,'#e8eef2')+LINGA(300,196,.4)+STALK(40,250,.9)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Tripurasundarī</b>, known locally as <b>Tibbādevī</b>: “the beauty of the three worlds”, seen as the united Śakti of Brahmā, Viṣṇu and Maheśvara'),
 ('Place','<b>Mūgūru</b> (Muguru, Moogooru), a village of T. Narasīpura taluk, Mysuru district'),
 ('Her image','Black stone, seated, with a <b>Śrīcakra at her feet</b>'),
 ('Beside her','The <b>Deśeśvara Svāmi</b> temple, Śiva with Pārvatī, the village’s chief Śiva shrine'),
 ('Founding legend','A Muslim pāḷegār, <b>Nawab Baba Saheb</b>, and a dry jowar stalk that sprouted overnight'),
 ('Great festival','<b>Chiguru Oḍeyuva Jātre</b> around Saṅkrānti, when her “sister” goddesses come to visit'),
 ('Also here','Old <b>Jain</b> temples of Ādinātha and Pārśvanātha, and a shrine of <b>Rākasamma</b>, called her sister')])
 +talk("A goddess with a Śrīcakra in a village temple?","Yes! Tripurasundarī is Lalitā herself. Here she's also the village mother, Tibbādevī.")))
mapfig=fig(560,220,'Schematic map: Mysuru, the Kaveri and Kabini rivers meeting at T. Narasipura, Muguru to the south of it, and Talakadu and Somanathapura nearby. Not to scale.',
 '<rect width="560" height="220" fill="#eef6e4"/><path d="M0 70 C 120 80, 220 60, 300 90 S 470 140, 560 120" stroke="#5b8fe0" stroke-width="8" fill="none"/><path d="M120 220 C 180 170, 250 120, 300 92" stroke="#5b8fe0" stroke-width="6" fill="none"/>'
 +'<rect x="20" y="10" width="90" height="40" fill="#e8e2d0" stroke="#111"/>'+T(65,34,'MYSURU',11,'#555')+'<circle cx="300" cy="92" r="7" fill="#c0392b" stroke="#111"/>'+T(300,116,'T. NARASĪPURA',10,'#7a1d12')
 +TEMPLE(330,190,.8)+T(330,212,'MŪGŪRU',11,'#c0392b')+'<circle cx="480" cy="128" r="6" fill="#7a1d12"/>'+T(480,150,'TALAKĀḌU',10,'#7a1d12')+'<circle cx="410" cy="40" r="6" fill="#7a1d12"/>'+T(410,28,'SOMANĀTHAPURA',10,'#7a1d12')
 +T(80,200,'KABINI',9,'#1f5f90')+T(150,62,'KĀVERĪ',9,'#1f5f90')+T(470,212,'simplified, not to scale',9,'#555'))
pages.append(page('where','WHERE IT IS','South of the river-meeting',mapfig+'''<div class="panel reading">
<p><b>A Kāverī village.</b> Mūgūru lies in T. Narasīpura taluk, south of the town where the Kāverī and Kabini meet, in the old temple country that includes Talakāḍu, Somanāthapura and Muḍukutore.</p>
<p><b>A large village.</b> It is one of the bigger villages of the taluk, and its Goddess draws devotees from Mysuru, Mandya, Chāmarājanagara and Bengaluru.</p>
<p><b>Two shrines, one village.</b> Tripurasundarī’s walled temple and the Deśeśvara Śiva temple stand close together; with Rākasamma and the Jain temples they make Mūgūru a small temple town.</p>
</div>'''))
pages.append(page('names','HER NAMES','Tripurasundarī and Tibbādevī',facts([
 ('Tripurasundarī','“The beauty of the three cities or worlds”: the name of <b>Lalitā</b>, the supreme Goddess of the Śrīvidyā tradition'),
 ('Tibbādevī','The local name. <i>Tibba</i> is a mound or raised ground in Kannada; the name is often read as “the Goddess of the mound”. This is a common reading, not a recorded origin'),
 ('Ammanavaru','“The Mother”: how the village speaks of her'),
 ('Mūgūru’s Goddess','In the Mysore University encyclopedia’s list of great village goddesses, she is named among the famous ones of the region')])
 +'''<div class="panel reading"><p><b>Two faces of one Goddess.</b> Tripurasundarī is the high name, used in Sanskrit hymns and Śrīvidyā; Tibbādevī is the name of the fields and the festival. Mūgūru keeps both: a Śrīcakra at her feet, and a village jātre in her honour. That double life is common in Karnataka, where great Purāṇic goddesses are also the protecting mothers of particular villages.</p>
<p><b>The trinity in one.</b> Devotees and writers describe her as the united power of Brahmā, Viṣṇu and Maheśvara. This matches Śrīvidyā’s teaching that the three great gods are the Goddess’s instruments, even her throne.</p></div>'''
 +talk("So is she a village goddess or Lalitā?","Both, Zappy. For Mūgūru she's the mother at the centre of the village. For the scriptures she's Lalitā.")))
deity=fig(560,190,'A seated black-stone goddess in a sanctum with a Sri Chakra diagram at her feet',
 '<rect width="560" height="190" fill="#fde4e4"/><rect x="170" y="14" width="220" height="170" fill="#fff4cd" stroke="#111" stroke-width="2"/>'+SEATED(280,100,1.5)+T(280,186,'ŚRĪCAKRA AT HER FEET',10,'#7a1d12'))
pages.append(page('deity','THE GODDESS','Black stone and the Śrīcakra',deity+'''<div class="g2">
<div class="card bg-red"><h4>🖤 The image</h4><p>The Goddess is carved in <b>black stone</b> and shown <b>seated</b>, as a queen, rather than standing or fighting.</p></div>
<div class="card bg-yellow"><h4>🔺 The Śrīcakra</h4><p>A <b>Śrīcakra</b>, the yantra of Lalitā made of interlocking triangles, is placed near her feet and worshipped with her.</p></div>
</div>
<div class="panel reading"><p><b>Why the Śrīcakra matters.</b> In Śrīvidyā the Śrīcakra is the Goddess herself in geometric form: nine interlocking triangles around a central point, ringed by lotuses and a square enclosure. A temple that keeps one at the Goddess’s feet is announcing that she is Tripurasundarī in the full sense, not only a local guardian. Śaṅkara’s tradition is credited with placing Śrīcakras before goddesses across South India, most famously at Kāñcī.</p>
<p><b>Seated, not fierce.</b> Unlike the flame-faced Jvālāmukhī Tripurasundarī of Uttanahaḷḷi, Mūgūru’s Goddess is calm and seated: Tripurasundarī in her gentle, royal aspect.</p></div>'''))
templ=fig(560,170,'A walled temple compound with small goddess figures along the top of the walls, an arched entrance, and the main shrine raised on a platform with a tower',
 '<rect width="560" height="170" fill="#fff4dc"/><rect x="40" y="60" width="480" height="100" fill="#f2e2c4" stroke="#111" stroke-width="2"/>'+''.join(f'<circle cx="{52+i*24}" cy="58" r="5" fill="#e05a8a" stroke="#111"/>' for i in range(20))
 +'<path d="M250 160 v-60 q30 -30 60 0 v60z" fill="#5a3a1a" stroke="#111" stroke-width="2"/>'+'<rect x="230" y="20" width="100" height="10" fill="#c9a26b" stroke="#111"/>'+TEMPLE(280,20,1.4))
pages.append(page('temple','THE TEMPLE','High walls and a tower of goddesses',templ+facts([
 ('Walls','High walls all round, crowned with small statuettes of the Devī in many forms'),
 ('Gateway','No rājagopura: entry is through an arched <b>mahādvāra</b>'),
 ('Courtyard','A wide prākāra for circumambulation'),
 ('Shrine','The main shrine stands on a high platform in the centre, reached by a few steps'),
 ('Halls','A small four-pillared <b>mukhamaṇṭapa</b> with plain walls and pillars'),
 ('Tower','A medium-sized vimāna over the sanctum, with colourful figures of the Devī on every side')])
 +'''<div class="panel reading"><p><b>A village style.</b> The temple is not a carved Hoysaḷa monument like nearby Somanāthapura. Its plain walls and painted tower belong to the living village tradition, renewed many times. Its strength is its setting and its worship, not ornament.</p></div>'''))
leg1=fig(560,180,'A sleeping soldier with his head on a stone under a jamun tree by a lake, a bright light and a goddess appearing',
 '<rect width="560" height="180" fill="#1b2f5a"/><ellipse cx="120" cy="160" rx="110" ry="16" fill="#3b8fd0"/><path d="M300 170 v-80" stroke="#7a4a1a" stroke-width="10"/><circle cx="300" cy="80" r="44" fill="#2a7a3a" stroke="#111" stroke-width="2"/>'
 +'<ellipse cx="350" cy="166" rx="40" ry="8" fill="#5a3a8a" stroke="#111"/><circle cx="392" cy="160" r="8" fill="#c98b5a" stroke="#111"/><rect x="400" y="156" width="16" height="10" fill="#888" stroke="#111"/>'
 +'<circle cx="470" cy="80" r="50" fill="#ffd60a" opacity=".35"/>'+GENTLE(470,110,.7))
pages.append(page('legend1','THE LEGEND · I','Nawab Baba Saheb and the sprouting stalk',leg1+'''<div class="steps">
<div><b>The rest.</b> On an expedition, a Muslim pāḷegār (local chief) called <b>Nawab Baba Saheb</b> rested by a lake near present-day Hosahaḷḷi, sleeping under a jamun tree with his head on a stone.</div>
<div><b>The light.</b> He saw a brilliant light; his soldiers seemed frozen. Tripurasundarī appeared and told him he had laid his head on her sacred presence.</div>
<div><b>The test.</b> He doubted. He planted a <b>dried jowar stalk upside down</b> and said he would believe if it sprouted by the next evening.</div>
<div><b>The sprout.</b> It sprouted. He begged forgiveness and was allowed to build her temple at Mūgūru.</div>
</div><div class="panel reading small"><p>This is the temple’s own tradition, repeated by the temple community; it is not a recorded historical event. Its point is plain: the Goddess chose her own devotee, and he was a Muslim chief.</p></div>'''))
pages.append(page('legend2','THE LEGEND · II','Mūkāsura and the name of the village',fig(560,150,'A goddess standing over a fallen demon, a village growing around her temple',
 '<rect width="560" height="150" fill="#ffe9c4"/>'+GENTLE(200,90,.9)+DEMON(320,140,.8)+TEMPLE(460,140,1.0))+'''<div class="steps">
<div><b>The promise.</b> The Goddess promised to destroy the line of the demon <b>Mūkāsura</b>, whose descendants troubled the region, and to stay in that place forever.</div>
<div><b>The name.</b> From this promise, tradition says, the village came to be called <b>Mūgūru</b>: the place linked with Mūka’s end and the Goddess’s settling.</div>
<div><b>An old shrine.</b> Local accounts call the temple about <b>850 years</b> old. No inscription confirming this appeared in the sources we checked.</div>
</div>
<div class="panel reading"><p><b>Place-name legends.</b> Many Karnataka villages explain their names through a goddess’s victory over a demon: Mysuru itself is “Mahiṣa’s town”, the place of Mahiṣāsura. Mūgūru’s story follows that pattern. Linguists might suggest other roots for the name; the legend is what the village tells.</p></div>'''
 +talk("A demon called Mūka?","Mūka means 'mute'. In the Purāṇas, Arjuna and Śiva fight a demon Mūka who came as a boar. Whether it's the same demon, no one can say.")))
jat=fig(560,180,'Decorated carts with tender leaves and coconut fronds bringing several goddess images in procession to a temple',
 '<rect width="560" height="180" fill="#e6f2df"/>'+''.join(f'<g transform="translate({x} 150)"><rect x="-34" y="-20" width="68" height="20" fill="#c9a26b" stroke="#111"/><circle cx="-22" cy="4" r="10" fill="#7a4a1a" stroke="#111"/><circle cx="22" cy="4" r="10" fill="#7a4a1a" stroke="#111"/>'+GENTLE(0,-44,.35)+''.join(f'<path d="M{-30+k*12} -20 q4 -18 10 -24" stroke="#2a9d6f" stroke-width="3" fill="none"/>' for k in range(6))+'</g>' for x in (90,230,370))+TEMPLE(500,150,1.0))
pages.append(page('jatre','CHIGURU OḌEYUVA JĀTRE','The festival of new sprouts',jat+facts([
 ('When','Around <b>Saṅkrānti</b> (January–February), over about three days'),
 ('The name','“The fair of the sprouting shoot”, after the jowar stalk that sprouted in the founding legend'),
 ('The sisters','Images of goddesses from neighbouring villages, said to be Tibbādevī’s <b>sisters</b>, are brought to visit her'),
 ('Procession','They are taken round the village before coming to the temple'),
 ('The carts','The carts are decorated with tender leaves (chiguru), coconut fronds and areca spathes')])
 +'''<div class="panel reading"><p><b>A meeting of goddesses.</b> In the Mysuru region, village goddesses are often thought of as sisters who visit one another at festivals, as Uttanahaḷḷi’s Goddess is Cāmuṇḍī’s sister. At Mūgūru the visit is the whole point: the sisters arrive, take her darśan and are paraded together.</p>
<p><b>A big village fair.</b> Thousands come, from Mysuru, Bengaluru, Chāmarājanagara and beyond. Neighbouring villages organise free meals (anna santarpaṇe) for pilgrims, and in recent years a large <b>rathotsava</b>, a chariot festival, has been part of the celebrations, inaugurated by local seers and leaders.</p></div>'''))
pages.append(page('year','THROUGH THE YEAR','Her other days',facts([
 ('Āṣāḍha','A <b>flower festival</b> (hūvina utsava) in the month of Āṣāḍha (June–July)'),
 ('Fridays and Tuesdays','The Goddess’s days, when local families visit'),
 ('Navarātri','The nine nights of the Goddess'),
 ('Vows','Devotees make vows (harake) and offer fruit, flowers and new clothes when their wishes come true')])
 +'''<div class="panel reading"><p><b>Living worship.</b> Daily abhiṣeka with milk and tender coconut, kuṅkuma-arcane and betel-leaf offerings are common here. Many newly married couples come for her blessing, and women whose prayers have been answered return to offer thanks at the jātre.</p></div>'''))
deshe=fig(560,170,'A small stone Shiva temple with a linga and a Nandi in front, a Parvati shrine beside it',
 '<rect width="560" height="170" fill="#e8eef2"/>'+TEMPLE(230,160,2.0,'#e8eef2')+LINGA(230,130,.6)+'<ellipse cx="120" cy="150" rx="30" ry="14" fill="#ddd" stroke="#111" stroke-width="2"/><circle cx="96" cy="140" r="9" fill="#ddd" stroke="#111" stroke-width="2"/>'+TEMPLE(400,160,1.4,'#fde4e4')+GENTLE(400,120,.4)+T(400,166,'PĀRVATĪ',9,'#7a1d12'))
pages.append(page('desheshwara','DEŚEŚVARA','Śiva beside the Goddess',deshe+facts([
 ('Name','<b>Śrī Deśeśvara Svāmi</b> temple, also called the Śrī Deśeśvara Śiva–Pārvatī temple'),
 ('Deity','Śiva as a liṅga, with Pārvatī'),
 ('Meaning','<i>Deśa</i> + <i>īśvara</i>: “Lord of the land” or “Lord of the region”: a natural reading of the name'),
 ('Standing','Listed among the Śiva temples of Mysuru district as Mūgūru’s Śiva temple'),
 ('Age','Called ancient locally; no dated inscription appeared in the sources we checked')])
 +'''<div class="panel reading"><p><b>Śiva and Śakti in one village.</b> A great goddess and a Śiva temple side by side is the pattern of Śrīvidyā itself: Tripurasundarī with Kāmeśvara, Śakti with Śiva, never apart. In village life it means the Mother who protects and the Lord who rules the land watch over the same fields.</p>
<p><b>Lord of the land.</b> Deśeśvara, if the name is read as “lord of the region”, makes Śiva the guardian of the whole territory, while Tibbādevī is the mother of the village: a division of care found in many Karnataka villages.</p></div>'''
 +talk("Which do I visit first?","Local custom varies. Most pilgrims go to the Goddess and also bow to Deśeśvara. Together they're one blessing.")))
pages.append(page('others','THE OTHER SHRINES','Rākasamma and the Jain temples',facts([
 ('Rākasamma','A shrine to <b>Rākasamma</b>, regarded locally as Tibbādevī’s sister'),
 ('Ādinātha','A Digambara Jain temple of <b>Ādinātha</b>, the first Tīrthaṅkara, seated in paryaṅkāsana; an inscription on the pedestal is dated to about the 13th century'),
 ('Pārśvanātha','A second Jain temple of <b>Pārśvanātha</b>, standing in kāyotsarga'),
 ('The inscription','It records disciples of the teacher Bhānukīrti Paṇḍitadeva of the Mūla Saṅgha, Deśī Gaṇa, Pustaka Gaccha, Koṇḍakunda lineage, and the leaders of Mūgūru, renovating a temple and installing an image')])
 +'''<div class="panel reading"><p><b>Many faiths, one village.</b> Mūgūru has a Goddess whose temple tradition credits a Muslim chief, Jain temples whose inscription records the village’s own leaders, and a Śiva temple at its heart. Its history is a small picture of how Karnataka’s religious life has long been shared.</p></div>'''))
pages.append(page('srividya','THE ŚRĪVIDYĀ CONNECTION','Lalitā in a village',facts([
 ('Tripurasundarī','The supreme Goddess of Śrīvidyā, also called Lalitā and Rājarājeśvarī'),
 ('Śrīcakra','Her yantra, at the Goddess’s feet here'),
 ('Three cities','Tripura: the three worlds, three bodies or three states of waking, dream and deep sleep, whose beauty she is'),
 ('Hymns','The Lalitā Sahasranāma and the Lalitā Triśatī praise her')])
 +'''<div class="panel reading"><p>Read more: <a href="/bhakti/devi/lalita-trishati/">Lalitā Triśatī, all 300 names</a> · <a href="/bhakti/devi/lalita-pancharatnam/">Lalitā Pañcaratnam</a> · <a href="/bhakti/devi/dasha-mahavidya/">Ṣoḍaśī among the Mahāvidyās</a> · <a href="/bhakti/temples-of-india/around-mysuru/uttanahalli/">Uttanahaḷḷi’s Jvālāmukhī Tripurasundarī</a>.</p>
<p><b>Two Tripurasundarīs near Mysuru.</b> The flame-faced Jvālāmukhī at Uttanahaḷḷi and the calm, seated Tibbādevī at Mūgūru show the same Goddess in fierce and gentle aspects, within a short distance of each other.</p></div>'''))
pages.append(page('around','AROUND MŪGŪRU','The T. Narasīpura temple country',facts([
 ('T. Narasīpura','The meeting of the Kāverī and Kabini: Agastyeśvara and Guñja Narasiṃha'),
 ('Talakāḍu','Temples half-buried in sand, and the Pañcaliṅga Darśana'),
 ('Muḍukutore','Mallikārjuna on the hill above the Kāverī'),
 ('Somanāthapura','The great Hoysaḷa Keśava temple')])
 +'''<div class="panel reading"><p>More: <a href="/bhakti/temples-of-india/around-mysuru/t-narasipura/">T. Narasīpura</a> · <a href="/bhakti/temples-of-india/around-mysuru/talakadu/">Talakāḍu</a> · <a href="/bhakti/temples-of-india/around-mysuru/mudukutore/">Muḍukutore</a> · <a href="/bhakti/temples-of-india/around-mysuru/">all temples around Mysuru</a>.</p></div>'''))
glossary=[('Tripurasundarī','beauty of the three worlds; Lalitā'),('Tibbādevī','the local name of Mūgūru’s Goddess'),('Śrīcakra','the yantra of Lalitā'),('Mahādvāra','great gateway'),('Mukhamaṇṭapa','front hall'),('Vimāna','tower over the sanctum'),('Pāḷegār','local chief'),('Jātre','temple fair'),('Chiguru','tender shoot'),('Deśeśvara','lord of the land'),('Harake','vow')]
pages.append(page('glossary','GLOSSARY','Words used in this guide','<table class="ct">'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in glossary)+'</table>'))
pages.append(page('end','MŪGŪRU ON ONE PAGE','Everything in five lines','''<div class="steps">
<div><b>The Goddess.</b> Tripurasundarī, called Tibbādevī: black stone, seated, the Śrīcakra at her feet.</div>
<div><b>The Lord.</b> Deśeśvara, Śiva with Pārvatī, beside her.</div>
<div><b>The legends.</b> Nawab Baba Saheb and the sprouting stalk; Mūkāsura and the village name.</div>
<div><b>The festival.</b> Chiguru Oḍeyuva Jātre at Saṅkrānti, when her sister goddesses visit.</div>
<div><b>The village.</b> Rākasamma, Jain temples and a long shared history.</div>
</div>'''+talk("One line to remember?","A dry stalk sprouted, and a village got its Mother. Every Saṅkrānti her sisters come to visit.")+'<div class="key">Tibbādevī of Mūgūru: <b>Lalitā in a village</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple and image:</b> Deccan Herald, K. Karunakaran, “Goddess of beauty and power” (walls, mahādvāra, raised shrine, mukhamaṇṭapa, vimāna, black-stone seated image with the Śrīcakra, Chiguru Oḍeyuva Jātre with the sister goddesses). OneShortTrip, “Sri Tripurasundari Temple, Moogooru” (Tibbādevī; Nawab Baba Saheb legend; Mūkāsura and the name; three-day jātre; Āṣāḍha flower festival).</p>
<p><b>Village and festival:</b> Kannada Wikipedia, “Mūgūru” and “T. Narasīpura” (about 850 years; sister goddesses; Śiva temple and Rākasamma); Mysore University Viśvakośa, “Grāmadevate” (the decorated carts); Vichara Vistara news reports on the rathotsava and anna santarpaṇe.</p>
<p><b>Deśeśvara:</b> Śaivam.org list of Śiva temples of Mysuru district (“Muguru Shri Desheshwara Temple”); Wikimedia Commons (Desheshwara Swamy temple, Muguru). <b>Jain temples:</b> Jain Heritage Centres, “Muguru” (Ādinātha and Pārśvanātha; pedestal inscription, about 13th century).</p>
<p><b>Not verified:</b> the temple’s age (850 years is a local figure); the founding legend (temple tradition, not history); the meaning of “Tibbādevī” and “Deśeśvara” (readings of the names); Deśeśvara’s date and builder; the link of Mūkāsura with the Purāṇic Mūka. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','Her Names'),('deity','The Goddess'),('temple','The Temple'),('legend1','Legend · The Sprouting Stalk'),('legend2','Legend · Mūkāsura'),('jatre','Chiguru Oḍeyuva Jātre'),('year','Through the Year'),('desheshwara','Deśeśvara'),('others','Rākasamma and the Jain Temples'),('srividya','The Śrīvidyā Connection'),('around','Around Mūgūru'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">TEMPLES AROUND MYSURU</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,76px)">MŪGŪRU</h1>
  <div class="series">TRIPURASUNDARĪ AND DEŚEŚVARA · A REFERENCE GUIDE</div>
  <div class="tag">Tibbādevī and the Lord of the land</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>South of T. Narasīpura, where the Kāverī and Kabini meet, is a village whose Goddess sits in black stone with the Śrīcakra at her feet. She is <b>Tripurasundarī</b>, Lalitā herself; the village calls her <b>Tibbādevī</b>.</p>
    <p>Her temple’s legend begins with a Muslim chief, a dry stalk that sprouted overnight, and a promise to stay forever. Beside her stands <b>Deśeśvara</b>, Śiva, the Lord of the land.</p>
    <p>This guide tells their stories, their temples and the festival of new shoots, when the Goddess’s sisters come to visit.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("A Muslim chief built a Devī temple?","That's the temple's own story. The Goddess chose him. Read on!")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/mysuru/Muguru.html','w').write(head+b+tail())
print('ok')
