"""Khaḍgamālā: a picture on every page and new pages to reach 14+. Edits the 13 live parts in place."""
import re, math, sys
from fx import *
REPO='/home/claude/srini-bhakti/srividya/khadgamala/'
RED='#8e1f17'; GOLD='#e0a800'
LAYERS=['bhupura','circles','p16','p8','t14','t10o','t10i','t8','t1','bindu']
def cakra(hi=(),w=300,label='The Śrīcakra',x=150,y=150,s=1.0):
    def c(k,base): return '#f2b8b0' if k in hi else base
    o=f'<g transform="translate({x} {y}) scale({s})">'
    # bhupura square with gates
    o+=f'<path d="M-140 -140 h110 v-12 h60 v12 h110 v110 h12 v60 h-12 v110 h-110 v12 h-60 v-12 h-110 v-110 h-12 v-60 h12z" fill="{c("bhupura","#fff8ec")}" stroke="{RED}" stroke-width="3"/>'
    for r in (122,116,110): o+=f'<circle r="{r}" fill="none" stroke="{GOLD if "circles" in hi else RED}" stroke-width="{3 if "circles" in hi else 1.5}"/>'
    o+=f'<circle r="104" fill="{c("p16","#fff3cf")}" stroke="{RED}" stroke-width="1.5"/>'
    for k in range(16):
        a=k*math.pi/8; o+=f'<ellipse cx="{92*math.cos(a):.1f}" cy="{92*math.sin(a):.1f}" rx="13" ry="7" transform="rotate({k*22.5} {92*math.cos(a):.1f} {92*math.sin(a):.1f})" fill="{c("p16","#fde4e4")}" stroke="{RED}" stroke-width="1"/>'
    o+=f'<circle r="78" fill="{c("p8","#fff3cf")}" stroke="{RED}" stroke-width="1.5"/>'
    for k in range(8):
        a=k*math.pi/4+math.pi/8; o+=f'<ellipse cx="{64*math.cos(a):.1f}" cy="{64*math.sin(a):.1f}" rx="15" ry="9" transform="rotate({k*45+22.5} {64*math.cos(a):.1f} {64*math.sin(a):.1f})" fill="{c("p8","#fde4e4")}" stroke="{RED}" stroke-width="1"/>'
    o+=f'<circle r="50" fill="{c("t14","#fff8ec")}" stroke="{RED}" stroke-width="1.5"/>'
    # simplified nine triangles
    for k,(r,up) in enumerate([(48,True),(44,False),(38,True),(34,False),(28,True),(24,False),(18,True),(14,False),(9,True)]):
        f='none'
        if (k<2 and 't14' in hi) or (2<=k<4 and 't10o' in hi) or (4<=k<6 and 't10i' in hi) or (6<=k<8 and 't8' in hi) or (k==8 and 't1' in hi): f='#f2b8b0'
        pts=[(r*math.cos(a),r*math.sin(a)) for a in ([-math.pi/2,math.pi/6,5*math.pi/6] if up else [math.pi/2,-math.pi/6,-5*math.pi/6])]
        o+='<path d="M'+' L'.join(f'{px:.1f} {py:.1f}' for px,py in pts)+f'z" fill="{f}" fill-opacity=".8" stroke="{RED}" stroke-width="1.3"/>'
    o+=f'<circle r="{5 if "bindu" in hi else 3}" fill="{"#c0392b" if "bindu" in hi else RED}"/>'
    if hi and 'bindu' in hi: o+='<circle r="12" fill="none" stroke="#e0a800" stroke-width="3"/>'
    return o+'</g>'
def cakra_svg(hi,label,note=''):
    return svg(560,320,label,f'<rect width="560" height="320" fill="#fffaf0"/>'+cakra(hi,x=280,y=160,s=1.0)+(lab(280,312,note,12) if note else ''))
def ring(n,label,col='#c0392b',bg='#fde4e4',center=None):
    n=max(1,min(n,16)); o=f'<rect width="560" height="230" fill="{bg}"/>'
    for k in range(n):
        a=-math.pi/2+k*2*math.pi/n; x=280+200*math.cos(a); y=118+88*math.sin(a)
        o+=g(x,y+28,.42,devi(sari=col,items=('lotus',)))
    o+=g(280,140,.55,center or devi(sari='#8e1f17',items=('lotus','rosary')))
    return svg(560,230,label,o)
def two(label,a,b,bg='#fff3cf',la='',lb=''):
    return svg(560,200,label,f'<rect width="560" height="200" fill="{bg}"/>'+g(180,180,.9,a)+g(380,180,.9,b)+(lab(180,195,la,12) if la else '')+(lab(380,195,lb,12) if lb else ''))
def hand(label,bg='#fff3cf'):
    o=f'<rect width="560" height="200" fill="{bg}"/>'+g(200,170,2.2,abhaya())+g(380,170,1.5,lotus())+'<circle cx="290" cy="80" r="60" fill="#e0a800" opacity=".15"/>'
    return svg(560,200,label,o)
def music(label): return svg(560,200,label,f'<rect width="560" height="200" fill="#e9e3f5"/>'+g(200,180,1.6,vina())+g(380,180,1,person('#1d4f8a',seat=True))+g(470,170,1,lamp())+'<path d="M300 60 q20 -20 40 0 M330 40 q20 -20 40 0" fill="none" stroke="#8e1f17" stroke-width="3"/>')
def chant(label): return svg(560,200,label,f'<rect width="560" height="200" fill="#fff8ec"/>'+g(200,185,1.2,person('#c0392b',seat=True))+g(330,185,1.2,lamp())+g(440,175,.55,devi(sari='#8e1f17',items=('lotus',)))+g(280,60,.8,book()))
def gem(label,c='#c0392b'): return svg(560,180,label,f'<rect width="560" height="180" fill="#fffaf0"/><path d="M280 30 l50 40 l-50 80 l-50 -80z" fill="{c}" stroke="#111" stroke-width="2"/><path d="M230 70 h100" stroke="#fff" stroke-width="2" opacity=".6"/>'+g(120,160,1,lamp())+g(440,160,1,lotus()))
def moon_ring(label):
    o='<rect width="560" height="200" fill="#20243a"/>'
    for k in range(15):
        x=40+k*34; ph=k/14
        o+=f'<circle cx="{x}" cy="90" r="13" fill="#2a2f48" stroke="#555"/><circle cx="{x-26*(1-ph)+13*(1-ph)}" cy="90" r="13" fill="#fff8d0" opacity="{0.2+0.8*ph:.2f}"/>'
    o+=lab(280,150,'the fifteen tithis of the bright fortnight, and the sixteenth beyond them',12).replace('fill="#111"','fill="#fff"')
    return svg(560,200,label,o)
def gurus(label): return svg(560,200,label,f'<rect width="560" height="200" fill="#fff3cf"/>'+g(140,180,1,shiva())+g(280,180,1,sage())+g(420,180,1,sage('#fff')))

PAGE_PICS={}  # id -> function(part) giving svg
def talk_tpl(h):
    return re.search(r'<div class="talk">.*?</div></div>',h,re.S).group(0)
def mk_talk(tpl,z,b):
    t=re.sub(r'(<span class="who">ZAPPY:</span>)[^<]*',r'\1 '+z.replace('\\','\\\\'),tpl,1)
    return re.sub(r'(<span class="who">PROF\. BOLT:</span>)[^<]*',r'\1 '+b.replace('\\','\\\\'),t,1)
def page(id,title,sub,fig,ps,tk,tpl,key=''):
    return f'<section class="page" id="{id}"><h2 class="page-title">{title}</h2><div class="sub">{sub}</div>\n{fig}\n<div class="panel reading">'+''.join(f'<p>{p}</p>' for p in ps)+'</div>'+mk_talk(tpl,*tk)+(f'<div class="key">{key}</div>' if key else '')+'</section>'

MUD={'Sarvasaṅkṣobhiṇī':('she who stirs all','the first shaking awake of a sleeping mind'),'Sarvavidrāviṇī':('she who melts all','hardness and resistance melting away'),'Sarvākarṣiṇī':('she who attracts all','attention drawn steadily inward'),'Sarvavaśaṅkarī':('she who brings all under her sway','the senses at last obedient'),'Sarvonmādinī':('she who intoxicates all','the joy that overwhelms calculation'),'Sarvamahāṅkuśā':('the great goad of all','the goad that turns the mind back when it wanders'),'Sarvakhecarī':('she who moves in space','awareness free as the sky'),'Sarvabījā':('the seed of all','everything returning to its seed'),'Sarvayoni (and Trikhaṇḍā)':('the source of all, and the three-part one','the source itself, and the union of the three')}
SID={'Aṇimā':'becoming as small as an atom','Laghimā':'becoming light','Mahimā':'becoming vast','Īśitva':'lordship','Vaśitva':'mastery','Prākāmya':'the fulfilment of every wish','Bhukti':'rightful enjoyment','Icchā':'the power of will','Prāpti (and Sarvakāma)':'attaining anything, and every desire fulfilled'}
CASES={5:'the accusative (dvitīyā)',6:'the instrumental (tṛtīyā)',7:'the dative (caturthī)',8:'the ablative (pañcamī)',9:'the genitive (ṣaṣṭhī)',10:'the locative (saptamī)',11:'the vocative (sambodhana)',12:'the nominative (prathamā)'}
HI={1:('bindu','t1'),2:('t1',),3:('t1','bindu'),4:('bhupura',),5:('p16',),6:('p8',),7:('t14',),8:('t10o',),9:('t10i',),10:('t8',),11:('t1',),12:('bindu',),13:tuple(LAYERS)}
GEMC={'Topaz':'#e0a800','Sapphire':'#1d4f8a','Cat’s eye':'#9a9a3a','Coral':'#e06a4a','Pearl':'#f4f1ea','Emerald':'#2a9d6f','Diamond':'#dfe9f6','Hessonite (gomedha)':'#c0582a','Ruby':'#c0392b'}
def count(gl):
    m=re.match(r'(\d+)',gl.get('Names','8')); return int(m.group(1)) if m else 8

def run(n):
    f=REPO+f'part-{n}/index.html'; h=open(f).read(); o=h
    tpl=talk_tpl(h)
    gl={}
    g_=re.search(r'<section[^>]*id="glance".*?</section>',h,re.S)
    if g_: gl={re.sub('<[^>]+>','',a):re.sub('<[^>]+>','',b) for a,b in re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td></tr>',g_.group(0))}
    hi=HI[n]; nm=count(gl)
    # 1. pictures for pages without one
    def haspic(s): return re.search(r'<svg(?![^>]*class="av")',s) or '<img' in s
    def pic_for(sid,title):
        T=title.lower()
        if sid in('contents','glossary','sources'): return None
        if sid=='foreword': return cakra_svg(hi,'The Śrīcakra with this part’s enclosure highlighted','this part’s place in the Śrīcakra (highlighted)')
        if sid=='glance': return gem(f'A {gl.get("Gem (booklet’s scheme)","gem")} between a lamp and a lotus',GEMC.get(gl.get('Gem (booklet’s scheme)',''),'#c0392b'))
        if sid.startswith('devis') or sid.startswith('line') or sid in('n1','n2','queens'): return ring(8 if sid in('n1','n2','queens') or sid.startswith('devis') and nm>8 else min(nm,10),'The devīs of this set drawn in a ring round the Goddess')
        if sid=='qy': return two('A crowned queen of the enclosure and a veiled yoginī',devi(sari='#8e1f17',items=('lotus','rosary')),devi(sari='#4a3a6a',items=('lotus',)),la='the queen',lb='the yoginī')
        if sid=='reading': return cakra_svg(hi,'The highlighted enclosure, with threads drawn inward to the centre')
        if sid=='end': return cakra_svg(hi,'The Śrīcakra, this part’s enclosure highlighted')
        if sid in('what','journey'): return cakra_svg(LAYERS,'The whole Śrīcakra, from the outer square to the bindu')
        if sid=='set1': return svg(560,200,'The Goddess Lalitā seated, a single lamp before her',f'<rect width="560" height="200" fill="#fde4e4"/>'+g(280,190,1.4,devi(sari='#8e1f17',items=('lotus','rosary')))+g(420,180,1,lamp()))
        if sid=='set2' or sid=='limbs': return ring(6,'Six limb devīs round the Goddess')
        if sid=='chant': return chant('A devotee chanting before a lamp and an image of the Goddess')
        if sid=='battle': return two('Devīs in battle array against a demon',devi(sari='#8e1f17',items=('trident','lotus')),demon(),la='the Nityās',lb='Bhaṇḍa’s army')
        if sid in('divya','siddha','manava'): return gurus('Three teachers: Śiva, a sage and a human teacher')
        if sid=='mayi': return ring(5,'Teachers in a ring round the Goddess, present in them')
        if sid=='salute': return chant('A devotee bowing before the Goddess')
        if sid=='whole': return cakra_svg(LAYERS,'The whole Śrīcakra')
        if sid=='map': return cakra_svg(hi,'This set on the Śrīcakra')
        return cakra_svg(hi,'The Śrīcakra')
    def fixsec(m):
        sid=m.group(1); s=m.group(0)
        if haspic(s): return s
        title=re.search(r'<h2 class="page-title">(.*?)</h2>',s).group(1)
        p=pic_for(sid,title)
        if not p: return s
        mm=re.search(r'<div class="sub">.*?</div>',s) or re.search(r'</h2>',s)
        return s[:mm.end()]+'\n'+p+'\n'+s[mm.end():]
    h=re.sub(r'<section[^>]*class="page[^"]*"[^>]*id="([^"]*)"[^>]*>.*?</section>',fixsec,h,flags=re.S)
    # 2. new pages
    new=[]
    if 4<=n<=12:
        av=n-3; tr=gl['Presiding Tripurā']; yo=gl['Yoginī']; mu=gl['Mudrā']; si=gl['Siddhi']; nmname=gl['Name'].split(':')[0]
        new.append(page('tripura','THE PRESIDING TRIPURĀ',f'{tr}, mistress of Āvaraṇa {av}',svg(560,220,f'The Goddess as {tr}, seated on a lotus within the highlighted enclosure',f'<rect width="560" height="220" fill="#fde4e4"/>'+cakra(hi,x=150,y=110,s=.62)+g(400,205,1.3,devi(sari='#8e1f17',items=('lotus','rosary')))),
          [f'<b>Who rules here.</b> Each of the nine enclosures has a presiding form of the Goddess, one of the nine Tripurās. Over Āvaraṇa {av}, <b>{nmname}</b>, presides <b>{tr}</b>.',
           f'<b>The yoginī.</b> With her is the yoginī of the enclosure, <b>{yo}</b>. The yoginīs grow more hidden as the garland moves inward: the manifest, the hidden, the more hidden, and so on to the supreme secret at the bindu.',
           f'<b>In the garland.</b> The Khaḍgamālā names the enclosure’s queen, its cakrasvāminī, and its yoginī at the end of each set; the Tripurā herself is honoured in the full Navāvaraṇa worship. Our <a href="/srividya/srichakra/">Śrīcakra series</a> gives each enclosure its own guide.'],
          ('Nine Tripurās for nine enclosures?','One Goddess, Zappy, wearing nine names as you walk in. The names change; she doesn’t.'),tpl,f'<b>{tr}</b> rules Āvaraṇa {av}.'))
        mm=MUD.get(mu,('',''))
        new.append(page('mudra','THE MUDRĀ AND THE SIDDHI',f'{mu} · {si}',hand(f'A hand in a gesture of blessing beside a lotus, for the mudrā {mu}'),
          [f'<b>The mudrā.</b> Each enclosure has a mudrā-devī, a power shown by a hand gesture in the worship. Here it is <b>{mu}</b>{", “"+mm[0]+"”" if mm[0] else ""}. The gestures themselves are taught within the tradition; we name them only.',
           f'<b>The siddhi.</b> Each enclosure also has a siddhi, an attainment. Here it is <b>{si}</b>: {SID.get(si,"an attainment")}. The ten siddhi-devīs stand at the outer square; each enclosure is linked with one of them.',
           f'<b>A reading.</b> Many teachers read the mudrā as {mm[1] or "a stage of the inner journey"}, and the siddhi not as a magic power but as an inner capacity ripening on the way to the centre. (Interpretation.)'],
          ('So I get a superpower in each enclosure?','The tradition warns against chasing them, Zappy. They’re signposts, not the goal.'),tpl,f'<b>{mu}</b> and <b>{si}</b>.'))
        song=gl.get('Dīkṣitar’s song','Kamalāmbike, rāga Toḍi' if n==4 else '')
        if n==4: song='Kamalāmbike āśrita-kalpalatike, rāga Toḍi'
        sname,_,raga=song.partition(', rāga ')
        new.append(page('song','DĪKṢITAR’S SONG','The Kamalāmbā Navāvaraṇa kṛti',music(f'A vīṇā and a singer before a lamp, for Dīkṣitar’s song {sname}'),
          [f'<b>The composer.</b> Muttusvāmi Dīkṣitar (1775–1835), one of the three great composers of Karnatak music, sang the nine enclosures of the Śrīcakra in nine songs to Kamalāmbā, the Goddess of Tiruvārūr in Tamil Nadu.',
           f'<b>This enclosure’s song.</b> For Āvaraṇa {av} he composed <b>{sname}</b>, in rāga <b>{raga}</b>.'+(f' Its text addresses the Goddess in {CASES[n]} case: the nine songs, with the dhyāna and maṅgala songs, run through the cases of Sanskrit grammar one by one.' if n in CASES else ' The songs, with the dhyāna and maṅgala songs, run through the cases of Sanskrit grammar one by one.'),
           '<b>How to use it.</b> Hearing the song after chanting the set is a lovely way to stay with the enclosure. Many recordings exist; listen with the names of this set in mind.'],
          ('A song for every enclosure?','Nine of them, Zappy, plus an opening and a closing one. A whole Śrīcakra in music.'),tpl,f'<b>{sname}</b> · rāga {raga}.'))
        new.append(page('practice','CHANTING THIS SET','Slowly, name by name',chant('A devotee chanting before a lamp with an image of the Goddess'),
          [f'<b>Aloud and steady.</b> Say each name of this set clearly, at an even pace, letting attention rest on each devī in her place on the diagram, starting from the west in front of you and moving anticlockwise.',
           '<b>Without the seeds.</b> In printed editions the names come with seed-syllables given at initiation. We do not print them; the names alone, said with attention, are how most householders recite.',
           '<b>With a teacher.</b> The full Navāvaraṇa worship, with mudrās and offerings, is learned from a teacher. Follow your own teacher’s order where it differs from ours.'],
          ('Can I just read the names?','With attention and respect, Zappy, yes. The rest comes with a teacher.'),tpl,'Name by name, <b>with attention</b>.'))
    elif n==1:
        new+= [page('sword','WHY A SWORD?','Khaḍga: protection and wisdom',svg(560,200,'A shining sword lying on a lotus before the Śrīcakra',f'<rect width="560" height="200" fill="#fde4e4"/>'+cakra(LAYERS,x=150,y=100,s=.55)+g(390,170,2,sword())+g(460,180,1,lotus())),
          ['<b>The promise.</b> Tradition says the hymn gives <b>khaḍga-siddhi</b>: a sword of protection that wins every battle, outer and inner.','<b>The other sword.</b> Many read the sword as wisdom, the blade that cuts the knot of separateness between the devotee and the Mother. (Interpretation.)','<b>A garland.</b> The names are strung one after another like flowers: a garland offered, and a sword received.'],('A sword made of names?','The sharpest kind, Zappy. It cuts fear.'),tpl,'A garland that is <b>a sword</b>.'),
          page('reciting','WHO RECITES IT','Householders and the Navāvaraṇa',chant('A householder chanting before a lamp'),
          ['<b>Widely recited.</b> The Khaḍgamālā is chanted across South India, often on Fridays and on Pūrṇimā, by people who do not perform the full Navāvaraṇa worship.','<b>A complete worship.</b> Many treat one recitation as worship of the whole Śrīcakra, done with the voice and the mind.','<b>The seeds.</b> In printed editions the opening is preceded by seed-syllables given by a teacher. We do not print them; the names alone are how most householders recite.'],('Do I need initiation?','For the seed-syllables and the full worship, a teacher, Zappy. The names with devotion are open to all who approach respectfully.'),tpl,'Recited <b>by many</b>.'),
          page('layers','THE NINE ENCLOSURES','The road map of the whole garland',cakra_svg(LAYERS,'The whole Śrīcakra with all nine enclosures'),
          ['<b>Outside in.</b> The outer square with its gates; the sixteen petals; the eight petals; the fourteen triangles; the two rings of ten; the eight triangles; the central triangle; and the bindu.','<b>One part each.</b> Parts 4 to 12 of this series take one enclosure each; Part 13 gathers the nine queens and the nine salutations.','<b>Before the gates.</b> The first three parts prepare: the Mother called, her limbs, her moon days and her teachers.'],('Nine rings to the centre?','Nine steps home, Zappy.'),tpl,'Nine steps <b>to the centre</b>.')]
    elif n==2:
        new+= [page('moon','THE MOON’S FIFTEEN DAYS','Why the Nityās are lunar',moon_ring('Fifteen moons waxing from new to full'),
          ['<b>Nityā means eternal.</b> The Nityās are the Goddess as time: one for each tithi, each lunar day, of the bright fortnight, and Lalitā herself as the sixteenth.','<b>Waxing and waning.</b> As the moon grows and shrinks, the Nityās are worshipped in turn, forwards in the bright half and, in many traditions, backwards in the dark half.','<b>In the Śrīcakra.</b> They are placed around the central triangle, fifteen on its sides and Lalitā at the centre.'],('Fifteen goddesses for fifteen moons?','And the sixteenth, beyond the phases, Zappy: the Mother herself.'),tpl,'The Goddess <b>as time</b>.'),
          page('guides','THE NITYĀS IN OUR SERIES','Each one in her own guide',ring(16,'Sixteen goddesses in a ring, the moon above'),
          ['<b>Guides.</b> Our <a href="/srividya/deities/nityas/">Nityā series</a> gives each Nityā her own illustrated guide: her form, colour, weapons and story.','<b>Here.</b> This part gives them in the Khaḍgamālā’s order, as names to be chanted.','<b>The sixteenth.</b> Mahānityā, Lalitā herself, closes the set.'],('Where can I see them?','In the Nityā guides, Zappy. One for each.'),tpl,'Sixteen <b>guides</b>.'),
          page('tithi','WORSHIP BY THE LUNAR DAY','Keeping the Nityās through the month',chant('A devotee before a lamp under the moon'),
          ['<b>Day by day.</b> Some devotees remember the Nityā of each tithi through the month: Kāmeśvarī on the first, Bhagamālinī on the second, and so on.','<b>Pūrṇimā.</b> The full moon, with Citrā the fifteenth, is especially honoured, and many recite the whole Khaḍgamālā then.','<b>With a teacher.</b> The detailed Nityā worship belongs to initiation; remembering their names needs only attention.'],('One goddess a day?','A month-long garland, Zappy.'),tpl,'A goddess <b>for every day</b>.')]
    elif n==3:
        new+= [page('oghas','THE THREE STREAMS','Divya, siddha and mānava',gurus('Śiva, a perfected sage and a human teacher in a row'),
          ['<b>Ogha.</b> A stream or flood: the flow of teaching from the Goddess to the world.','<b>Three streams.</b> Divya, the divine teachers; siddha, the perfected ones; mānava, the human teachers. The garland names them in that order.','<b>Why.</b> The tradition holds that knowledge reaches us through a living line; naming the teachers honours every link. (Tradition.)'],('Gods as teachers?','The first teachers, Zappy. Then sages, then people like your own teacher.'),tpl,'Three streams, <b>one water</b>.'),
          page('honour','HONOURING THE TEACHER','Guru, the bridge',svg(560,200,'A student bowing to a teacher seated before the Śrīcakra',f'<rect width="560" height="200" fill="#fff3cf"/>'+cakra(LAYERS,x=440,y=100,s=.5)+g(150,185,1.1,sage())+g(260,185,1,namaste('#c0392b'))),
          ['<b>In every worship.</b> Śrīvidyā begins and ends by honouring the guru; the garland places the teachers just before entering the Śrīcakra.','<b>Inside the circle.</b> In the Śrīcakra worship the teachers are placed within the central triangle, close to the Mother.','<b>For us.</b> Naming the line of teachers is a way of thanking everyone who carried the knowledge to us. Read our <a href="/festivals/guru-purnima/the-guru/">Guru</a> guide.'],('Why so close to the centre?','Because the teacher leads you there, Zappy.'),tpl,'The teacher <b>leads in</b>.'),
          page('chantg','CHANTING THE GURUS','A quiet set',chant('A devotee chanting before a lamp'),
          ['<b>Slowly.</b> These names are chanted quietly and with gratitude.','<b>Your own teacher.</b> Many add their own teacher’s name in their heart.','<b>Seeds omitted.</b> As everywhere in this series, seed-syllables and the guru-pādukā mantras are not printed; they are given by a teacher.'],('Can I add my teacher?','In your heart, Zappy. Every line ends with someone real.'),tpl,'With <b>gratitude</b>.')]
    elif n==13:
        rows=[('Trailokyamohana','Tripurā','Aṇimā','Toḍi'),('Sarvāśāparipūraka','Tripureśī','Laghimā','Kalyāṇī'),('Sarvasaṅkṣobhaṇa','Tripurasundarī','Mahimā','Śaṅkarābharaṇam'),('Sarvasaubhāgyadāyaka','Tripuravāsinī','Īśitva','Kāmbhoji'),('Sarvārthasādhaka','Tripurāśrī','Vaśitva','Bhairavī'),('Sarvarakṣākara','Tripuramālinī','Prākāmya','Punnāgavarāḷi'),('Sarvarogahara','Tripurāsiddhā','Bhukti','Śahānā'),('Sarvasiddhiprada','Tripurāmbā','Icchā','Ghaṇṭā'),('Sarvānandamaya','Mahātripurasundarī','Prāpti','Āhiri')]
        new+= [page('tripuras','THE NINE TRIPURĀS','One Goddess, nine names',ring(9,'Nine forms of the Goddess in a ring'),
          ['<b>The nine.</b> '+'; '.join(f'Āvaraṇa {k+1}, {r[0]}: <b>{r[1]}</b>' for k,r in enumerate(rows))+'.','<b>One Goddess.</b> They are not nine goddesses but one, named by the place she rules as the devotee walks in.'],('Nine names in a row!','Learn them as steps, Zappy.'),tpl,'Nine <b>Tripurās</b>.'),
          page('siddhis','THE NINE ATTAINMENTS','Siddhis, enclosure by enclosure',hand('A hand in blessing beside a lotus'),
          ['<b>The nine.</b> '+'; '.join(f'{k+1}, {r[2]}' for k,r in enumerate(rows))+', with Sarvakāma at the centre.','<b>A warning.</b> The tradition treats siddhis as signs on the road, not its goal. (Tradition.)','<b>Inner reading.</b> Lightness, vastness, mastery and will can be read as qualities of a mind growing free. (Interpretation.)'],('Should I want them?','Want her, Zappy. The rest is scenery.'),tpl,'Signs <b>on the road</b>.'),
          page('songs','DĪKṢITAR’S NAVĀVARAṆA','Nine songs for nine enclosures',music('A vīṇā and a singer'),
          ['<b>The set.</b> Muttusvāmi Dīkṣitar’s Kamalāmbā Navāvaraṇa kṛtis: a dhyāna song (Ānandabhairavī), then one for each enclosure, in rāgas '+', '.join(r[3] for r in rows)+', and a closing maṅgala song.','<b>The grammar.</b> The songs address the Goddess through the cases of Sanskrit one after another, so that the whole language bows to her.','<b>Listen.</b> Hearing the nine after the garland is a fine way to end. Each Khaḍgamālā part names its song.'],('Nine songs in a row?','A concert that is a pūjā, Zappy.'),tpl,'A Śrīcakra <b>in music</b>.'),
          page('after','AFTER THE GARLAND','Sitting at the centre',cakra_svg(('bindu',),'The bindu at the centre of the Śrīcakra'),
          ['<b>Silence.</b> After the last salutation, many sit quietly for a while: the walk has reached the centre.','<b>Offering.</b> A lamp, a flower, or simply folded hands.','<b>Again.</b> The garland is meant to be walked again and again; each time the names grow more familiar and the walk more inward. Begin again with <a href="/srividya/khadgamala/part-1/">Part 1</a>.'],('What do I do at the end?','Sit, Zappy. You’ve arrived.'),tpl,'Arrived <b>at the centre</b>.')]
    for p in new:
        pid=re.search(r'id="([^"]+)"',p).group(1)
        if f'id="{pid}"' in h: continue
        gi=h.find('<section class="page" id="glossary"')
        h=h[:gi]+p+'\n'+h[gi:]
        t=re.search(r'<h2 class="page-title">(.*?)</h2>',p).group(1).title().replace('’S','’s').replace('Dīkṣitar’S','Dīkṣitar’s')
        tm=re.search(r'(<ul class="toc[^"]*"[^>]*>)(.*?)(</ul>)',h,re.S)
        items=re.findall(r'<li><span class="num">([^<]*)</span><a href="#([^"]*)">([^<]*)</a></li>',tm.group(2))
        gidx=[k for k,(a,b,c) in enumerate(items) if b=='glossary'][0]
        items.insert(gidx,('',pid,t))
        li=''.join(f'<li><span class="num">{k+1}</span><a href="#{b}">{c}</a></li>' for k,(a,b,c) in enumerate(items))
        h=h[:tm.start(2)]+li+h[tm.end(2):]
    open(f,'w').write(h)
    secs=len(re.findall(r'<section[^>]*class="page',h))
    print(n,'pages',secs)
for n in (map(int,sys.argv[1:]) if len(sys.argv)>1 else range(1,14)): run(n)
