"""Gaṇapati in the Veda and the Gītā overview: a picture on every page, new pages to reach 15."""
import re, sys
from fx import *
R='/home/claude/srini-bhakti/'
def haspic(s): return re.search(r'<svg(?![^>]*class="av")',s) or '<img' in s
def tpl_of(h): return re.search(r'<div class="talk">.*?</div></div>',h,re.S).group(0)
def mk_talk(tpl,z,b):
    t=re.sub(r'(<span class="who">ZAPPY:</span>)[^<]*',lambda m:m.group(1)+' '+z,tpl,count=1)
    return re.sub(r'(<span class="who">PROF\. BOLT:</span>)[^<]*',lambda m:m.group(1)+' '+b,t,count=1)
def page(id,title,sub,fig,ps,tk,tpl,key=''):
    return f'<section class="page" id="{id}">\n  <h2 class="page-title">{title}</h2>\n  <div class="sub">{sub}</div>\n{fig}\n<div class="panel reading">'+''.join(f'<p>{p}</p>' for p in ps)+'</div>\n  '+mk_talk(tpl,*tk)+(f'\n  <div class="key">{key}</div>' if key else '')+'\n</section>'
def S(label,inner,bg='#fff3cf',h=170): return svg(560,h,label,f'<rect width="560" height="{h}" fill="{bg}"/>'+inner)
def fire_alt(label): return S(label,g(280,160,1.4,fire())+g(130,160,1,sage())+g(430,160,1,sage('#fff')),'#fde9c8')
def chariot(x=280,y=160,s=1):
    return g(x,y,s,'<rect x="-70" y="-40" width="140" height="34" fill="#c98a3a" stroke="#6a4a2a"/><circle cx="-40" cy="0" r="22" fill="none" stroke="#6a4a2a" stroke-width="5"/><circle cx="40" cy="0" r="22" fill="none" stroke="#6a4a2a" stroke-width="5"/><path d="M60 -80 v-40" stroke="#6a4a2a" stroke-width="3"/><path d="M60 -120 l30 8 l-30 8z" fill="#e0a800"/>'+g(-30,-40,.55,krishna())+g(30,-40,.55,person('#c0392b')))
def armies(label): return S(label,''.join(g(x,165,.35,person('#8e1f17')) for x in range(20,200,22))+chariot(280,150,.8)+''.join(g(x,165,.35,person('#1d4f8a')) for x in range(380,560,22)),'#fde9c8')
RIG={'foreword':S('A Vedic fire altar with two priests chanting',g(280,160,1.3,fire())+g(130,160,1,sage())+g(430,160,1,sage('#fff')),'#fde9c8'),
 'full':S('An open palm-leaf manuscript beside a lamp and a Gaṇeśa',g(200,150,1.3,book())+g(330,160,1,lamp())+g(450,160,.9,ganesha())),
 'd1':S('A seer chanting to Bṛhaspati, lord of prayer',g(170,160,1,sage())+g(380,160,1.1,god()),'#e9e3f5'),
 'd2':S('Indra with his thunderbolt among storm-gods',g(280,160,1.1,god())+g(380,80,.8,vajra())+''.join(g(x,165,.4,person('#5a8ab8')) for x in (80,130,450,500)),'#dfe9f6'),
 'd3':S('Gaṇeśa with curved trunk and tusk above a lamp',g(280,165,1.3,ganesha())+g(140,160,1,lamp())+g(420,160,1,lamp())),
 'end':S('Three verses as three lamps before Gaṇeśa',g(150,160,1,lamp())+g(280,160,1,lamp())+g(410,160,1,lamp())+g(280,90,.6,ganesha()))}
RNEW=[
 ('ganas','WHO ARE THE HOSTS?','Gaṇa: a troop, a band',S('Three groups: priests, storm-gods and Śiva’s attendants',g(120,160,.8,sage())+g(280,160,.8,god())+g(440,160,.9,shiva())),
  ['<b>Gaṇa.</b> A troop or company. In the Ṛgveda the gaṇas are bands such as the priests’ hymns or the Maruts, the storm-gods who ride with Indra.','<b>Gaṇapati.</b> So “lord of the hosts” first named Brahmaṇaspati and Indra, each the leader of a band.','<b>Later.</b> In the Purāṇas the gaṇas are Śiva’s attendants, and Gaṇeśa becomes their lord: the same word with a new face.'],
  ('Same word, different lords?','Words travel, Zappy. This one found a home with Gaṇeśa.'),'<b>Gaṇa</b>: a host.'),
 ('history','HOW GAṆEŚA APPEARED','From word to god',S('A timeline from a fire altar to a carved elephant-headed god',g(90,160,.8,fire())+'<path d="M150 130 H420" stroke="#8e1f17" stroke-width="4" stroke-dasharray="10 6"/>'+g(470,160,1,ganesha(c='#9a9a9a'))),
  ['<b>Vedic.</b> The word gaṇapati appears, but not the elephant-headed god.','<b>Early images.</b> Scholars date the first clear images of the elephant-headed Gaṇeśa to around the 4th–5th centuries CE, in the Gupta period.','<b>Purāṇas.</b> The Gaṇeśa and Mudgala Purāṇas, and the Gāṇapatya tradition, gather his stories and make him supreme. Read our <a href="/ganesha/hymns/atharvashirsha-1/">Atharvaśīrṣa</a> guide.'],
  ('So Gaṇeśa is younger than the Veda?','In images and stories, scholars think so, Zappy. Devotees see him as beginningless.'),'From a word <b>to a god</b>.'),
 ('chant','CHANTING THE VERSES','How they are used today',S('A family chanting before a Gaṇeśa at the start of a pūjā',g(160,160,1,namaste('#c0392b'))+g(260,160,1,namaste('#1d4f8a'))+g(420,165,1.2,ganesha())),
  ['<b>First of all.</b> “Gaṇānāṃ tvā” opens countless pūjās, weddings and house-warmings; the gāyatrī is chanted in daily worship.','<b>Accent.</b> Vedic verses carry pitch accents (svaras); learn them from a teacher or a good recording rather than from print alone.','<b>Without accents.</b> Many devotees recite the words simply, with attention. Both are common.'],
  ('Do I need the accents?','For Vedic chanting, yes, Zappy. For prayer from the heart, attention matters most.'),'Begin <b>with these</b>.')]
GITA={'foreword':armies('Two armies facing each other, a chariot between them'),'contents':None,
 'what':S('An open book beside Kṛṣṇa',g(180,150,1.3,book())+g(400,160,1,krishna())),
 'setting':S('A dice game in a palace hall',g(280,150,1,palace())+'<rect x="250" y="130" width="14" height="14" fill="#fff" stroke="#111"/><rect x="290" y="134" width="14" height="14" fill="#fff" stroke="#111"/>'),
 'who':S('Kṛṣṇa, Arjuna, a blind king and Sañjaya',g(110,160,.9,krishna())+g(230,160,.9,person('#c0392b'))+g(350,160,.9,person('#5a3a6a',seat=True))+g(470,160,.9,person('#1d4f8a'))),
 'map':svg(560,80,'Eighteen small lamps in a row','<rect width="560" height="80" fill="#fff8ec"/>'+''.join(g(26+k*30.5,62,.32,lamp()) for k in range(18))),
 'keyverses':S('Kṛṣṇa teaching Arjuna on the chariot',chariot(280,150,1.2),'#dfe9f6'),
 'paths':S('Four paths leading up to one summit','<path d="M280 30 L60 165 M280 30 L210 165 M280 30 L350 165 M280 30 L500 165" stroke="#b08a5a" stroke-width="5" stroke-dasharray="10 6"/>'+g(280,40,.6,sun()),'#e3f5e9'),
 'teachers':S('Three teachers with books',g(140,160,1,sage())+g(280,160,1,sage('#fff'))+g(420,160,1,sage('#ffd60a'))),
 'howto':S('A palm-leaf book open at two pages',g(280,150,1.6,book())),
 'end':S('A lamp in a windless place',g(280,160,1.8,lamp()),'#20243a'),
 'sources':None}
GNEW=[
 ('vishvarupa','THE COSMIC FORM','Chapter 11: Arjuna sees everything',S('A vast many-armed form filling the sky above a tiny chariot',g(280,170,2.2,vishnu())+chariot(470,165,.45),'#20243a',200),
  ['<b>The vision.</b> In chapter 11 Arjuna asks to see Kṛṣṇa’s universal form. Given divine sight, he sees all worlds, all gods and all beings in one body, and time itself devouring the armies.','<b>Terror and wonder.</b> Arjuna trembles and begs Kṛṣṇa to return to his familiar four-armed, then two-armed, form.','<b>Read it.</b> <a href="/vishnu/bhagavad-gita/chapter-11/">Chapter 11</a> in our series, verse by verse.'],
  ('Arjuna got scared?','Who wouldn’t, Zappy? Then he asked for his friend back.'),'All things <b>in one</b>.'),
 ('jayanti','GĪTĀ JAYANTĪ','The Gītā’s birthday',S('Devotees reading the Gītā by lamplight',g(170,160,1,person('#c0392b',seat=True))+g(280,150,1.2,book())+g(400,160,1,lamp())),
  ['<b>When.</b> Tradition marks the day the Gītā was spoken on Mokṣadā Ekādaśī, the eleventh day of the bright fortnight of Mārgaśīrṣa (November–December).','<b>How.</b> Many read or chant the whole Gītā, or a chapter, that day; Kurukṣetra holds a great festival.','<b>Every day.</b> But any day is a good day to begin chapter 1.'],
  ('The Gītā has a birthday?','And a big party at Kurukṣetra, Zappy.'),'Read it <b>on its day</b>.')]
def run(f,pics,new,anchor='end',toc_before='end',num='•',renum=False):
    h=open(R+f).read(); tpl=tpl_of(h)
    def fix(m):
        sid=m.group(1); s=m.group(0)
        if haspic(s): return s
        p=pics.get(sid)
        if not p: return s
        mm=re.search(r'<div class="sub">.*?</div>',s) or re.search(r'</h2>',s)
        return s[:mm.end()]+'\n'+p+'\n'+s[mm.end():]
    h=re.sub(r'<section class="page" id="([^"]*)">.*?</section>',fix,h,flags=re.S)
    for (pid,title,sub,fig,ps,tk,key) in new:
        if f'id="{pid}"' in h: continue
        gi=h.find(f'<section class="page" id="{anchor}"'); h=h[:gi]+page(pid,title,sub,fig,ps,tk,tpl,key)+'\n'+h[gi:]
        li=f'<li><span class="num">{num}</span><a href="#{pid}">{title.title().replace("’S","’s")}</a></li>'
        k=h.find(f'<li><span class="num">',h.find('<ul class="toc'))
        ai=h.find(f'<a href="#{toc_before}">',h.find('<ul class="toc')); ls=h.rfind('<li>',0,ai)
        h=h[:ls]+li+h[ls:]
    if renum:
        tm=re.search(r'<li class="part">THIS OVERVIEW</li>(.*?)<li><span class="num">∑',h,re.S)
        c=[0]
        def rn(m): c[0]+=1; return f'<li><span class="num">{c[0]}</span>'
        body=re.sub(r'<li><span class="num">[^<]*</span>',rn,tm.group(1))
        h=h[:tm.start(1)]+body+h[tm.end(1):]
    open(R+f,'w').write(h); print(f,len(re.findall(r'<section class="page',h)))
run('ganesha/hymns/ganapati-rigveda/index.html',RIG,RNEW,'end','end')
run('vishnu/bhagavad-gita/overview/index.html',GITA,GNEW,'howto','howto',renum=True)
