"""Pañca Kedār: a picture on every page, fact tables (outside At a Glance) turned into reading text, and new pages to reach 15."""
import re, sys
from fx import *
REPO='/home/claude/srini-bhakti/temples-of-india/pancha-kedar/'
def peaks(bg='#dfe9f6'):
    return (f'<rect width="560" height="200" fill="{bg}"/>'
      '<path d="M0 140 L80 60 L150 120 L240 30 L330 115 L420 50 L500 110 L560 70 V200 H0z" fill="#8a9aae"/>'
      '<path d="M80 60 L100 80 L60 80z M240 30 L268 62 L212 62z M420 50 L444 76 L396 76z" fill="#fff"/>'
      '<path d="M0 165 q140 -20 280 -6 t280 0 V200 H0z" fill="#7aa36a"/>')
def shrine(x=280,y=170,s=1.0,c='#8a8a92'):
    return g(x,y,s,f'<rect x="-34" y="-50" width="68" height="50" fill="{c}" stroke="#444"/><path d="M-30 -50 Q0 -120 30 -50z" fill="{c}" stroke="#444"/><rect x="-3" y="-132" width="6" height="14" fill="#e0a800"/><rect x="-10" y="-34" width="20" height="34" fill="#3a2a1a"/><path d="M-40 0 h80" stroke="#555" stroke-width="4"/>')
def doli(x,y,s=1):
    return g(x,y,s,'<rect x="-60" y="-12" width="120" height="6" fill="#6a4a2a"/><rect x="-22" y="-44" width="44" height="34" rx="6" fill="#c0392b" stroke="#8e1f17"/><path d="M-26 -44 Q0 -62 26 -44z" fill="#e0a800"/>'+g(-48,26,.45,person('#1d4f8a'))+g(48,26,.45,person('#1d4f8a')))
def H(label,extra='',bg='#dfe9f6',tmp=True,h=200):
    return svg(560,h,label,peaks(bg)+(shrine() if tmp else '')+extra)
def bull(x=280,y=170,s=1): return g(x,y,s,nandi())
def ring5(hi=None):
    names=['Kedārnāth','Tuṅganāth','Rudranāth','Madhyamaheśvar','Kalpeśvar']; parts=['hump','arms','face','navel','hair']
    o=peaks('#eef3fa')
    for k,(n,p) in enumerate(zip(names,parts)):
        x=70+k*105; c='#c0392b' if hi==k else '#8a8a92'
        o+=shrine(x,150,.55,c)+lab(x,170,n,11)+lab(x,186,p,10)
    return svg(560,200,'The five Kedār shrines in a row, each labelled with the part of the bull',o)
def walk(label,n=4,bg='#e3f5e9'):
    o=peaks(bg)+'<path d="M40 190 Q200 150 300 160 T520 110" fill="none" stroke="#b08a5a" stroke-width="7" stroke-dasharray="12 8"/>'+shrine(500,110,.5)
    o+=''.join(g(80+k*70,185-k*10,.42,person('#c0392b')) for k in range(n))
    return svg(560,200,label,o)
def winter(label,seat='the winter seat'):
    o='<rect width="560" height="200" fill="#e9eef5"/><path d="M0 120 L120 40 L240 110 L360 30 L480 100 L560 60 V200 H0z" fill="#fff"/>'+shrine(140,110,.5,'#aab')+lab(140,128,'summer shrine (closed)',11)+'<path d="M190 120 Q280 170 380 160" fill="none" stroke="#c0392b" stroke-width="4" stroke-dasharray="8 6"/>'+doli(300,165,.7)+shrine(440,190,.7,'#c98a5a')+lab(440,198,seat,11)
    return svg(560,200,label,o)
def flowers(label):
    o=peaks('#e3f5e9')+''.join(f'<circle cx="{30+(k*53)%520}" cy="{170+(k*17)%26}" r="5" fill="{["#c0392b","#e0a800","#9b59b6","#fff"][k%4]}"/>' for k in range(30))
    return svg(560,200,label,o)
def cave(label,inner=''):
    return svg(560,200,label,'<rect width="560" height="200" fill="#e3e0d8"/><path d="M60 200 Q100 40 280 30 Q460 40 500 200z" fill="#8a7a6a"/><path d="M170 200 Q200 90 280 84 Q360 90 390 200z" fill="#3a2e24"/>'+inner+g(130,190,1,lamp())+g(430,190,1,lamp()))
def lakeview(label):
    return svg(560,200,label,peaks('#dfe9f6')+'<ellipse cx="280" cy="180" rx="150" ry="16" fill="#8fb8de"/><path d="M160 180 L240 196 L330 182 L400 194" stroke="#fff" opacity=".5"/>'+shrine(470,170,.45))

PICS={
 'kedarnath':{'glance':H('Kedārnāth temple below snow peaks'),'hump':H('A pilgrim embracing a rough triangular rock liṅga',g(150,190,1,namaste('#c0392b'))+'<path d="M330 190 L380 120 L430 190z" fill="#6a6a72"/>',tmp=False),
   'nara':svg(560,200,'Two sages worshipping an earthen liṅga',peaks('#fde9c8')+g(170,190,1,sage())+g(390,190,1,sage('#fff'))+g(280,190,1,linga())),
   'temple':H('A massive grey stone temple with a Nandi before it',bull(120,190,.9)),'priests':H('A priest with a lamp before the temple',g(140,190,1,person('#e0a800'))+g(190,185,1,lamp())),
   'seasons':winter('A palanquin carrying the god down from the closed shrine to Ukhimath','Omkāreśvar, Ukhimath'),'meaning':H('A strong figure holding the hump of a bull sinking into the earth',bull(150,195,1),tmp=True),
   'flood':H('A large boulder lodged behind the temple, splitting a flood',''),},
 'tungnath':{'glance':H('Tuṅganāth on a high ridge'),'arms':H('A small dark liṅga in a stone shrine',g(140,190,1,linga())),'temple':H('A small stone temple with smaller shrines round it',shrine(160,180,.5)+shrine(400,180,.5)),
   'priests':winter('The god carried down to the Mārkaṇḍeya temple at Makkumath','Makkumath'),'meaning':H('Open arms on a summit',g(120,190,1,namaste('#c0392b'))),'chandra':H('A rocky summit above the temple, a crescent moon',g(480,40,.6,moon()),tmp=True)},
 'rudranath':{'glance':cave('A rock cave shrine among meadows','<circle cx="280" cy="150" r="26" fill="#2f4f8a"/><circle cx="270" cy="145" r="3" fill="#fff"/><circle cx="290" cy="145" r="3" fill="#fff"/>'),'face':cave('A natural rock face decorated with eyes and a blue throat','<circle cx="280" cy="140" r="30" fill="#6a6a72"/><circle cx="268" cy="134" r="4" fill="#fff"/><circle cx="292" cy="134" r="4" fill="#fff"/><path d="M262 172 h36" stroke="#2f4f8a" stroke-width="8"/>'),
   'meadows':flowers('High meadows full of wild flowers'),'priests':winter('The god carried down to the Gopīnāth temple in Gopeśvar','Gopīnāth, Gopeśvar'),'meaning':cave('A devotee face to face with the god in the cave',g(200,195,.9,namaste('#c0392b')))},
 'madhyamaheshwar':{'glance':H('A stone temple in a green valley below four peaks'),'navel':H('A navel-shaped liṅga and a small water spout',g(150,190,1,linga())+'<path d="M420 140 q10 30 0 50" stroke="#5a8ab8" stroke-width="5" fill="none"/>'),
   'budha':lakeview('A tiny shrine by a small lake mirroring snow peaks'),'priests':winter('The god carried down to the Omkāreśvar temple at Ukhimath','Omkāreśvar, Ukhimath'),'valley':walk('A path through villages and forest in a green valley',3),
   'meaning':H('A balanced scale before the temple','<path d="M100 110 h120 M160 110 v60" stroke="#6a4a2a" stroke-width="4"/><path d="M95 110 l-15 30 h30z M225 110 l-15 30 h30z" fill="#e0a800"/>')},
 'kalpeshwar':{'glance':cave('A small cave shrine under a rock in a farming valley'),'jata':cave('A rock like matted locks with a stream falling from it','<path d="M250 100 q10 40 -10 90 M280 96 q-6 50 6 94 M310 100 q14 40 -4 90" stroke="#5a4a3a" stroke-width="7" fill="none"/><path d="M280 96 v100" stroke="#8fb8de" stroke-width="4"/>'),
   'urgam':svg(560,200,'Terraced fields and orchards in a valley',peaks('#e3f5e9')+''.join(f'<path d="M0 {120+k*18} h560" stroke="#6a9a4a" stroke-width="10"/>' for k in range(4))+g(130,140,.8,tree('#2f7a3a'))+g(450,140,.8,tree('#2f7a3a'))),
   'complete':ring5(4),'meaning':cave('An open cave door with a lamp burning',g(280,190,1.2,lamp())),'kalpa':svg(560,200,'A sage meditating under a great tree',peaks('#e3f5e9')+g(300,190,2,tree('#2f7a3a'))+g(200,190,1,sage()))},
 'overview':{'head':H('A temple in the Kathmandu valley with a pagoda roof','<path d="M380 150 h90 l-12 -18 h-66z M392 132 h66 l-10 -16 h-46z M402 116 h46 l-23 -20z" fill="#8e1f17"/>',tmp=False),'five':ring5(),
   'shankara':svg(560,200,'A young teacher with a staff walking to the mountains',peaks('#fde9c8')+g(200,190,1.1,sage())+shrine(440,180,.6)),'kedarakhanda':svg(560,200,'An old book open before the peaks',peaks('#fde9c8')+g(280,180,1.3,book())),
   'meaning':ring5(),'glossary':H('Snow peaks and a stone shrine')}}
def haspic(s): return re.search(r'<svg(?![^>]*class="av")',s) or '<img' in s
def tpl_of(h): return re.search(r'<div class="talk">.*?</div></div>',h,re.S).group(0)
def mk_talk(tpl,z,b):
    t=re.sub(r'(<span class="who">ZAPPY:</span>)[^<]*',lambda m:m.group(1)+' '+z,tpl,1)
    return re.sub(r'(<span class="who">PROF\. BOLT:</span>)[^<]*',lambda m:m.group(1)+' '+b,t,1)
def page(id,title,sub,fig,ps,tk,tpl,key=''):
    return f'<section class="page" id="{id}"><h2 class="page-title">{title}</h2><div class="sub">{sub}</div>\n{fig}\n<div class="panel reading">'+''.join(f'<p>{p}</p>' for p in ps)+'</div>'+mk_talk(tpl,*tk)+(f'<div class="key">{key}</div>' if key else '')+'</section>'
def gen(slug,sid,title):
    T=title.lower()
    return H(f'{title.title()}: a Himalayan shrine scene')

NEW={
'kedarnath':[
 ('samadhi','ĀDI ŚAṄKARA','The teacher’s resting place',svg(560,200,'A seated stone statue of a young teacher behind the temple',peaks('#eef3fa')+shrine(160,180,.7)+g(400,190,1.3,sage('#fff'))),
  ['<b>The tradition.</b> Ādi Śaṅkara, the great teacher of Advaita, is said to have ended his life at Kedārnāth at the age of thirty-two, after revitalising the Himalayan shrines. (Tradition; other places claim his last days too.)','<b>The samādhi.</b> His memorial behind the temple was swept away in the 2013 flood. A new shrine with a large seated statue of Śaṅkara was built in its place in 2021.','<b>Read more.</b> Our '+'<a href="/temples-of-india/12-jyotirlingas/kedarnath/">Kedārnāth Jyotirliṅga</a> guide.'],
  ('Śaṅkara ended his journey here?','So the Kedār tradition holds, Zappy. Others say Kāñcī.'),'Śaṅkara’s <b>resting place</b>.'),
 ('walk','THE WALK UP','From Gaurīkuṇḍ to the god',walk('Pilgrims walking up a mountain path to the temple, some on ponies',5),
  ['<b>On foot.</b> The road ends at Gaurīkuṇḍ; from there pilgrims walk about 16–18 km up the Mandākinī valley. The path was rebuilt after 2013.','<b>Other ways.</b> Ponies, palanquins and helicopters carry those who cannot walk.','<b>Bhairavnāth.</b> Above the town stands the shrine of Bhairava, Kedārnāth’s guardian, who is said to watch over the temple through the closed winter months. (Tradition.)','<b>Season.</b> Weather turns fast at 3,500 m; follow local advisories.'],
  ('Sixteen kilometres uphill?','One step at a time, Zappy. Like Bhīma, don’t let go.'),'Walk <b>with care</b>.')],
'tungnath':[
 ('chopta','THE WALK FROM CHOPTA','The shortest of the Kedār walks',walk('A short path from a roadhead meadow up to a ridge temple',4),
  ['<b>From Chopta.</b> The road reaches Chopta, a meadow among rhododendron forest; the paved path to the temple is about 3.5 km, steep but short.','<b>Candraśilā.</b> Many continue another kilometre or so to the summit above.','<b>Practical.</b> The air is thin; walk slowly and carry warm clothes even in summer.'],
  ('The shortest walk to the highest temple?','The paradox of Tuṅganāth, Zappy.'),'Short, steep, <b>high</b>.'),
 ('forest','FORESTS AND MEADOWS','Rhododendron and bugyāl',flowers('Rhododendron trees in flower and a high meadow'),
  ['<b>Rhododendron.</b> Below the temple, forests of red rhododendron bloom in spring.','<b>Bugyāl.</b> Above, open alpine meadows, green in summer and buried in snow in winter.','<b>Sanctuary.</b> The area lies within the Kedārnāth Wildlife Sanctuary; the Himālayan monal, Uttarakhand’s state bird, is often seen.'],
  ('Is the monal colourful?','Like a rainbow with wings, Zappy.'),'A <b>garden</b> on the way.'),
 ('doli','THE ḌOLĪ','The god goes down for winter',winter('The palanquin carrying the god down to Makkumath','Makkumath'),
  ['<b>Closing.</b> After Dīpāvalī the temple closes and the god’s image is carried down in a ḍolī, a palanquin, to the Mārkaṇḍeya temple at Makkumath.','<b>Opening.</b> In spring it is carried up again, with villages greeting it along the way.','<b>A festival.</b> The procession is one of the region’s great local celebrations.'],
  ('The god travels?','Twice a year, Zappy, carried on shoulders.'),'Down in winter, <b>up in spring</b>.'),
 ('second','THE SECOND KEDĀR','Hump, then arms',ring5(1),
  ['<b>Order.</b> Kedārnāth, Tuṅganāth, Rudranāth, Madhyamaheśvar, Kalpeśvar: the hump, then the arms, then the face, the navel and the hair.','<b>Why arms second.</b> In the legend the forelegs came up nearest the hump, so many pilgrims go here next. (Tradition; routes vary.)','<b>All five.</b> Our '+'<a href="/temples-of-india/pancha-kedar/overview/">overview</a> tells the whole story.'],
  ('Do people do all five?','Some, Zappy. It takes about two weeks on foot.'),'The <b>arms</b>, second of five.')],
'rudranath':[
 ('trek','THE HARDEST WALK','Through forest and meadow',walk('A long path climbing through forest to high meadows',5),
  ['<b>Long.</b> Rudranāth is usually counted the hardest of the five: about 20 km from the roadhead, through oak and rhododendron forest and up to high meadows.','<b>Routes.</b> Paths start from Sagar village near Gopeśvar, or from Maṇḍal by way of the Anusūyā Devī temple.','<b>Practical.</b> Usually two days each way for most walkers; check routes and weather locally.'],
  ('Two days to see a face?','The longest walk to the closest meeting, Zappy.'),'The <b>hardest</b> walk.'),
 ('nilakantha','NĪLAKAṆṬHA','The blue-throated god',svg(560,200,'Śiva drinking poison from the churning ocean, his throat turning blue',f'<rect width="560" height="200" fill="#20243a"/><path d="M0 160 q70 -20 140 0 t140 0 t140 0 t140 0 V200 H0z" fill="#2f4f8a"/>'+g(280,150,1.3,shiva())+'<circle cx="280" cy="80" r="10" fill="#2f4f8a"/>'),
  ['<b>The story.</b> When gods and demons churned the ocean, the poison Hālāhala rose first. Śiva drank it to save the world; Pārvatī held his throat so it would not go down, and it turned blue.','<b>At Rudranāth.</b> The face here is worshipped as Nīlakaṇṭha, the blue-throated: the god who swallows the world’s poison.','<b>A reading.</b> Many see in him the strength to hold pain without passing it on. (Interpretation.)'],
  ('He drank poison for us?','And kept it in his throat, Zappy, so it would harm no one.'),'He <b>holds</b> the poison.'),
 ('kunds','THE SACRED PONDS','Water round the shrine',lakeview('Small mountain ponds near the shrine'),
  ['<b>Kuṇḍs.</b> Several small sacred ponds lie near the temple, among them the Sūrya-, Candra-, Tārā- and Mānasa-kuṇḍs.','<b>Bathing.</b> Pilgrims wash or sprinkle themselves before darśan.','<b>Views.</b> On clear days Nandā Devī, Triśūl and other peaks stand across the valley.'],
  ('Ponds named after the sun and moon?','And the stars, Zappy. A sky on the ground.'),'Sun, moon <b>and stars</b>.'),
 ('gopinath','GOPĪNĀTH','The winter seat',svg(560,200,'An old stone temple with a tall metal trident in its courtyard',peaks('#eef3fa')+shrine(220,185,.9)+'<path d="M400 190 V40 M380 50 q20 30 40 0 M400 40 l-8 -16 M400 40 l8 -16" stroke="#555" stroke-width="5" fill="none"/>'),
  ['<b>Gopeśvar.</b> In winter Rudranāth’s image is carried down to the Gopīnāth temple in Gopeśvar, the Chamoli district headquarters.','<b>The trident.</b> Gopīnāth is famous for a tall ancient metal trident in its courtyard, bearing old inscriptions.','<b>Year-round worship.</b> So the face of Śiva is worshipped all year: in the cave in summer and in the town in winter.'],
  ('A trident older than the temple?','Very old indeed, Zappy. Its inscriptions are studied by historians.'),'Winter in <b>Gopeśvar</b>.')],
'madhyamaheshwar':[
 ('trek','FROM RĀNSĪ','The walk to the middle',walk('A path from a village through forest to a high green valley',4),
  ['<b>Roadhead.</b> The walk starts at Rānsī village, beyond Ukhimath, and goes by way of Gauṇḍār: about 16 km.','<b>Villages.</b> The path passes small villages and homestays; the god’s ḍolī comes this way each season.','<b>Practical.</b> Many take two days up; check weather and routes locally.'],
  ('Sixteen kilometres again!','The middle is never at the roadside, Zappy.'),'Walk <b>to the middle</b>.'),
 ('temple','THE TEMPLE','A stone shrine and its neighbours',H('A stone temple with two small shrines beside it',shrine(130,185,.45)+shrine(430,185,.45)),
  ['<b>The shrine.</b> A stone temple in the north Indian style, with the navel-shaped liṅga in the sanctum.','<b>Neighbours.</b> Small shrines beside it are dedicated to Pārvatī and to Ardhanārīśvara, Śiva and Pārvatī as one.','<b>Setting.</b> Meadows all round and Chaukhamba behind.'],
  ('Ardhanārīśvara is half Śiva, half Pārvatī?','One body, two halves, Zappy.'),'Śiva <b>with Pārvatī</b>.'),
 ('ukhimath','UKHIMATH IN WINTER','Two Kedārs under one roof',winter('The god carried down to Ukhimath for winter','Omkāreśvar, Ukhimath'),
  ['<b>Omkāreśvar temple.</b> In winter both Kedārnāth’s and Madhyamaheśvar’s images rest at Ukhimath.','<b>The ḍolī.</b> The return of the god to the mountains in spring is marked by a village fair.','<b>Ūṣā and Aniruddha.</b> Ukhimath is linked by tradition with the wedding of Ūṣā, Bāṇāsura’s daughter, and Kṛṣṇa’s grandson Aniruddha. (Tradition.)'],
  ('Two gods share a winter home?','Good neighbours, Zappy.'),'A shared <b>winter home</b>.'),
 ('third','THE FOURTH KEDĀR','The navel in the five',ring5(3),
  ['<b>Order.</b> Kedārnāth, Tuṅganāth, Rudranāth, Madhyamaheśvar, Kalpeśvar.','<b>The centre.</b> The navel is the body’s middle; Madhyamaheśvar keeps the centre of Śiva. (Interpretation.)','<b>Overview.</b> The full legend is in our <a href="/temples-of-india/pancha-kedar/overview/">overview</a>.'],
  ('Fourth, but called middle?','Middle of the body, Zappy, not of the list.'),'The <b>navel</b> of the five.')],
'kalpeshwar':[
 ('reach','REACHING KALPEŚVAR','The easiest of the five',walk('A short path from a village to a cave temple',3),
  ['<b>Close to the road.</b> A road now runs up the Urgam valley close to Devgrām; the last stretch is a short walk.','<b>Low.</b> At about 2,200 m it is far lower than the other Kedārs.','<b>Practical.</b> Roads in the valley can be affected by landslides in the monsoon; check locally.'],
  ('An easy Kedār at last!','A kind ending, Zappy.'),'The <b>gentle</b> one.'),
 ('cave','THE CAVE SHRINE','Worship under the rock',cave('A small stone shrine set under an overhanging rock'),
  ['<b>The shrine.</b> A small temple set under a natural rock overhang; inside, the rock formation worshipped as Śiva’s locks.','<b>Offerings.</b> Water, flowers and lamps, as at a liṅga.','<b>Simplicity.</b> No great tower or hall: the mountain itself is the roof.'],
  ('The rock is the roof?','The best roof, Zappy. It has lasted longer than any temple.'),'The mountain <b>as roof</b>.'),
 ('ganga','HAIR AND THE GAṄGĀ','Why the locks matter',svg(560,200,'A river falling from the sky into Śiva’s matted hair',f'<rect width="560" height="200" fill="#dfe9f6"/><path d="M280 0 Q260 60 280 110" stroke="#8fb8de" stroke-width="14" fill="none"/>'+g(280,195,1.4,shiva())+river(560,190)),
  ['<b>Bhagīratha.</b> King Bhagīratha prayed for the Gaṅgā to come down to earth; Śiva agreed to break her fall.','<b>In the locks.</b> She fell into his jaṭā and wandered there until he let her out in gentle streams.','<b>Here.</b> In the land of the Gaṅgā’s sources, among the streams that feed the Alakanandā, the god of the matted hair keeps watch.'],
  ('A river lost in his hair?','For a long time, Zappy, until he let her out kindly.'),'Hair that <b>tamed a river</b>.'),
 ('winter','OPEN IN WINTER','When the others close',svg(560,200,'A cave shrine lit by a lamp while snow falls',f'<rect width="560" height="200" fill="#e9eef5"/>'+''.join(f'<circle cx="{(k*47)%560}" cy="{(k*31)%180}" r="3" fill="#fff"/>' for k in range(40))+'<path d="M140 200 Q200 90 280 84 Q360 90 420 200z" fill="#5a4a3a"/>'+g(280,190,1.3,lamp())),
  ['<b>All year.</b> Kalpeśvar is the one Kedār that stays open through winter.','<b>Villagers.</b> The people of the Urgam valley keep up the worship through the snowy months.','<b>For winter pilgrims.</b> Those who come out of season can still complete a Kedār darśan here, along with the winter seats at Ukhimath, Makkumath and Gopeśvar.'],
  ('Śiva doesn’t take a holiday?','Not here, Zappy.'),'The door <b>stays open</b>.')],
}
def run(slug):
    f=REPO+slug+'/index.html'; h=open(f).read(); tpl=tpl_of(h)
    h=h.replace('news reports on winter closure (2026)','news reports on winter closure').replace(' (2026)','')
    pics=PICS.get(slug,{})
    def fix(m):
        sid=m.group(1); s=m.group(0)
        if sid in ('contents','sources','glance'): pass
        # tables outside glance -> reading text
        if sid!='glance':
            t=re.search(r'<table class="ct[^"]*">(.*?)</table>',s,re.S)
            if t:
                rows=re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td></tr>',t.group(1))
                ps=''.join(f'<p><b>{a}.</b> {b}{"" if b.rstrip().endswith((".","?","!")) else "."}</p>' for a,b in rows)
                s=s[:t.start()]+s[t.end():]
                if '<div class="panel reading">' in s: s=s.replace('<div class="panel reading">','<div class="panel reading">'+ps,1)
                else: s=s.replace('</section>','<div class="panel reading">'+ps+'</div></section>')
        if sid in ('contents','sources') or haspic(s): return s
        title=re.search(r'<h2 class="page-title">(.*?)</h2>',s).group(1)
        p=pics.get(sid,'X')
        if p is None: return s
        if p=='X': p=gen(slug,sid,title)
        mm=re.search(r'<div class="sub">.*?</div>',s) or re.search(r'</h2>',s)
        return s[:mm.end()]+'\n'+p+'\n'+s[mm.end():]
    h=re.sub(r'<section class="page" id="([^"]*)">.*?</section>',fix,h,flags=re.S)
    for (pid,title,sub,fig,ps,tk,key) in NEW.get(slug,[]):
        if f'id="{pid}"' in h: continue
        p=page(pid,title,sub,fig,ps,tk,tpl,key)
        anchor='meaning' if f'id="meaning"' in h else 'end'
        gi=h.find(f'<section class="page" id="{anchor}"'); h=h[:gi]+p+'\n'+h[gi:]
        tm=re.search(r'(<ul class="toc">)(.*?)(</ul>)',h,re.S)
        items=re.findall(r'<li><span class="num">[^<]*</span><a href="#([^"]*)">([^<]*)</a></li>',tm.group(2))
        k=[i for i,(a,b) in enumerate(items) if a==anchor][0]
        t=title.title().replace('’S','’s')
        items.insert(k,(pid,t))
        li=''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{b}</a></li>' for i,(a,b) in enumerate(items))
        h=h[:tm.start(2)]+'\n    '+li+'\n'+h[tm.end(2):]
    open(f,'w').write(h)
    print(slug,len(re.findall(r'<section class="page',h)))
for s in (sys.argv[1:] or ['overview','kedarnath','tungnath','rudranath','madhyamaheshwar','kalpeshwar']): run(s)
