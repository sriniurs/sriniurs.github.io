import pages as PG
from pages import *
from pages import foreword,glance,reading,story,cards,end,sources,build,covart
from fx import *
PARTS=[('ashtavinayaka','The Aṣṭavināyaka','Eight Gaṇeśas round Pune'),('morgaon','Morgaon','Mayūreśvara, lord of the peacock'),('siddhatek','Siddhaṭek','The Gaṇeśa with the right-turned trunk'),('pali','Pālī','The Gaṇeśa named after a child'),('mahad','Mahaḍ','The boon-giver by the pond'),('theur','Theūr','The wish-jewel Gaṇeśa'),('lenyadri','Leṇyādri','Gaṇeśa in a Buddhist cave'),('ozar','Ojhar','The lord of obstacles, with a golden dome'),('ranjangaon','Rāñjaṇgāv','The great Gaṇapati whom Śiva worshipped'),
('gokarna','Gokarṇa','The boy who saved the ātmaliṅga'),('idagunji','Iḍagunji','The Gaṇeśa who came for the Kali age'),('hampi','Hampi’s Gaṇeśas','Mustard-seed and Bengal-gram Gaṇeśas'),('bengaluru-dodda-ganapati','Doḍḍa Gaṇapati','Bengaluru’s big Gaṇeśa'),('ucchi-pillaiyar','Ucchi Pillaiyār','Gaṇeśa at the top of the rock'),('pillaiyarpatti','Pillaiyārpaṭṭi','A Gaṇeśa carved into the living rock'),('madhur','Madhūr','The Gaṇeśa a boy drew on a wall'),('siddhivinayak-mumbai','Siddhivināyak, Mumbai','The city’s right-trunked Gaṇeśa')]
PG.configure('/ganesha/temples/',PARTS,'red','Gaṇeśa’s Temples','Lord','Gaṇeśa’s Temples')
PG.CFG['backurl']='/ganesha/temples/'; PG.CFG['backname']='Gaṇeśa temple guides'
PG.OUT='outd/gt/'
POS={'morgaon':(372,140),'siddhatek':(470,118),'pali':(110,132),'mahad':(92,96),'theur':(326,108),'lenyadri':(262,34),'ozar':(238,48),'ranjangaon':(392,74)}
NAMES={'morgaon':'Morgaon','siddhatek':'Siddhaṭek','pali':'Pālī','mahad':'Mahaḍ','theur':'Theūr','lenyadri':'Leṇyādri','ozar':'Ojhar','ranjangaon':'Rāñjaṇgāv'}
def amap(hi=None,h=180):
    o=f'<rect width="560" height="{h}" fill="#fbf3e6"/><path d="M60 0 q-20 90 30 {h}" fill="none" stroke="#7a9a6a" stroke-width="10" opacity=".5"/>'+lab(48,h-8,'Sahyādri ghats')
    o+=f'<circle cx="300" cy="112" r="9" fill="#1d4f8a"/>'+lab(300,98,'Pune')
    for k,(x,y) in POS.items():
        big=k==hi
        o+=f'<circle cx="{x}" cy="{y}" r="{11 if big else 6}" fill="{"#c0392b" if big else "#e0a800"}" stroke="#111" stroke-width="1.5"/>'+lab(x,y+(22 if y<150 else -14),NAMES[k],12 if big else 10)
    o+=lab(470,h-8,'simplified, not to scale',10)
    return svg(560,h,f'Schematic map of the eight Aṣṭavināyaka temples around Pune'+(f', with {NAMES[hi]} marked' if hi else ''),o)
def tscene(label,extra='',bg='#fde9c8',river_=False,hill=False):
    o=f'<rect width="560" height="170" fill="{bg}"/>'
    if hill: o+=g(420,160,1.6,mountain('#8a7a5a',False))
    if river_: o+=river(560,150)
    o+=g(140,150,1,tree('#2f6a3a'))+g(280,140,1.1,palace())+g(280,118,.42,ganesha())+g(470,150,1,lamp())+extra
    return svg(560,170,label,o)
def gimg(label,note='',flip=False,bg='#fff3cf'):
    o=f'<rect width="560" height="170" fill="{bg}"/><circle cx="280" cy="90" r="74" fill="#e0a800" opacity=".25"/>'+g(280,160,1.5,ganesha(c='#d35400'),flip=flip)+g(150,160,1.1,lamp())+g(410,160,1.1,lamp())+g(470,150,.9,mouse())+(lab(280,20,note,12) if note else '')
    return svg(560,170,label,o)
def gloss(i,words,tk):
    return cards('glossary','WORDS TO KNOW','The temple vocabulary of this guide',svg(560,120,'A lamp, a modaka, a mouse and a lotus in a row',f'<rect width="560" height="120" fill="#fff3cf"/>'+g(90,105,1.1,lamp())+g(210,100,1.4,modaka())+g(340,105,1.1,mouse())+g(470,105,1,lotus())),[(e,a,b) for e,a,b in words],tk)

L=lambda u,t: f'<a href="{u}">{t}</a>'
def temple(i,d):
    slug=PARTS[i][0]
    pp=[foreword(i,d['fw'],d['fwtk']), glance(d['glance'],amap(slug) if slug in POS else tscene('Temple scene'))]
    pp.append(reading('where','WHERE IT IS','The place and the road',amap(slug) if slug in POS else tscene('Temple scene',river_=True),d['where'],d['wtk'],d['wk']))
    pp.append(story('legend',d['lt'],d['ls'],d['strip'],d['lsrc'],d['lsteps'],d['ltk'],d['lk']))
    for p in d['more']: pp.append(reading(*p))
    pp.append(gloss(i,d['words'],d['gtk']))
    pp.append(end(i,d['end'],d['endnext'],PARTS[i][1]))
    pp.append(sources(d['src'],d['unver'],d['study']))
    build(i,d['kicker'],d['cov'],d['cap'],d['how'],d['desc'],pp)
    print(slug,len(pp)+2)
