exec(open('/home/claude/work/shakti/common_s.py').read())
import common_t as _ct
def head_navy(title,desc):
    h=open(_ct.SRC).read(); hd=h[:h.find('<div class="book">')]
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
PSS='/bhakti/temples-of-india/pancha-bhuta-sthalas/'
JY='/bhakti/temples-of-india/12-jyotirlingas/'
# key, element(sk), element(en), temple, Śiva name, Goddess, town, state, lat, lon, slug, colour
S5=[('earth','Pṛthvī','Earth','Ekāmbareśvara','Ekāmbaranātha','Kāmākṣī (Ēlavārkuḻali)','Kāñcīpuram','Tamil Nadu',12.847,79.700,'ekambareshvara','#a0703a'),
    ('water','Āpas (Appu)','Water','Jambukeśvara','Jambukeśvara','Akhilāṇḍeśvarī','Tiruvānaikkāval','Tamil Nadu',10.853,78.706,'jambukeshvara','#3b8fd0'),
    ('fire','Agni','Fire','Aruṇācaleśvara','Aṇṇāmalaiyār','Unnāmulai Ammaṉ (Apītakucāmbā)','Tiruvaṇṇāmalai','Tamil Nadu',12.231,79.068,'arunachaleshvara','#e0501a'),
    ('air','Vāyu','Air','Kāḷahastīśvara','Kāḷahastīśvara','Jñānaprasūnāmbā','Śrīkāḷahasti','Andhra Pradesh',13.750,79.700,'kalahastishvara','#7ab8a0'),
    ('space','Ākāśa','Space','Naṭarāja (Sabhānāyaka)','Naṭarāja','Śivakāmasundarī','Cidambaram','Tamil Nadu',11.399,79.693,'chidambaram','#6a4aa0')]
def LINGA(x,y,s=1,c='#2b2f36',top=''):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-46 0 h92 l-8 -14 h-76z" fill="#7a7f8a"/>'
            f'<path d="M-30 -14 h60 q14 0 14 -6 h-88 q0 6 14 6z" fill="#8a8f9a"/><path d="M-20 -20 v-34 a20 20 0 0 1 40 0 v34z" fill="{c}"/>'
            '<path d="M-12 -46 h24 M-12 -40 h24 M-12 -34 h24" stroke="#fff" stroke-width="2.5"/><circle cy="-30" r="3" fill="#e04040" stroke="none"/>'+top+'</g>')
def GOPURAM(x,y,s=1,c='#e8d8b0',n=7):
    t=''.join(f'<rect x="{-40+k*4}" y="{-18*(k+1)}" width="{80-k*8}" height="18" fill="{c if k%2==0 else "#d8c49a"}"/>' for k in range(n))
    top=-18*n
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">{t}'
            f'<path d="M{-40+n*4} {top} q{40-n*4} -26 {80-n*8} 0z" fill="#d9782f"/>'+''.join(f'<circle cx="{-28+n*4+i*((56-n*8)/4):.0f}" cy="{top-8}" r="3" fill="#e0a800"/>' for i in range(5))
            +'<rect x="-9" y="-30" width="18" height="30" fill="#5a3a1a"/></g>')
def EL(key,x,y,s=1):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
    if key=='earth': return g+'<path d="M-30 18 q30 -46 60 0z" fill="#c9a26b"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="2" fill="#7a5a2a" stroke="none"/>' for a,b in ((-10,8),(4,2),(14,10),(-2,12),(8,-4)))+'</g>'
    if key=='water': return g+'<path d="M0 -26 q22 28 0 44 q-22 -16 0 -44z" fill="#5ab0f0"/><path d="M-6 6 q6 6 12 0" fill="none" stroke="#fff"/></g>'
    if key=='fire': return g+'<path d="M-16 18 q-12 -26 6 -44 q2 16 10 18 q2 -18 14 -24 q-4 22 6 30 q4 14 -10 20z" fill="#ff8c1a"/><path d="M-6 18 q-4 -12 4 -18 q2 8 6 8 q4 -6 2 -10 q8 10 0 20z" fill="#ffd60a"/></g>'
    if key=='air': return g+'<path d="M-26 -10 q20 -10 36 0 q14 8 0 14 M-26 4 q26 -8 44 4 M-20 18 q16 -6 30 2" fill="none" stroke="#3a8a70" stroke-width="3.5"/></g>'
    return g+'<circle r="22" fill="#1d1040"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="1.6" fill="#fff" stroke="none"/>' for a,b in ((-10,-8),(8,-12),(12,6),(-6,10),(2,-2)))+'</g>'
COAST=[(14.6,80.12),(14.0,80.16),(13.6,80.3),(13.1,80.29),(12.6,80.2),(12.0,79.88),(11.5,79.78),(11.0,79.86),(10.3,79.86),(10.0,79.6)]
LON0,LON1,LAT0,LAT1=77.9,80.9,14.4,10.0
def mxy(lat,lon,W=560,H=300): return 20+(lon-LON0)*(W-40)/(LON1-LON0), 15+(LAT0-lat)*(H-30)/(LAT0-LAT1)
def SOUTHMAP(W=560,H=300,hi=None,labels=True):
    c=[mxy(a,b,W,H) for a,b in COAST]
    pts=f'0,0 '+' '.join(f'{x:.0f},{y:.0f}' for x,y in c)+f' {c[-1][0]:.0f},{H} 0,{H}'
    o=f'<rect width="{W}" height="{H}" fill="#cfe8f6"/><polygon points="{pts}" fill="#f4e6d0" stroke="#111" stroke-width="2"/>'
    x,y=mxy(13.08,80.27,W,H); o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#888"/><text x="{x+8:.0f}" y="{y+4:.0f}" font-family="Georgia" font-size="12" fill="#555">Chennai</text>'
    x,y=mxy(10.8,79.84,W,H); o+=f'<text x="{x+12:.0f}" y="{y:.0f}" font-family="Georgia" font-size="13" font-style="italic" fill="#3a6a9a">Bay of Bengal</text>'
    pos={'earth':('end',-14,5),'water':('start',14,5),'fire':('end',-14,5),'air':('end',-14,5),'space':('end',-14,5)}
    for k in S5:
        x,y=mxy(k[8],k[9],W,H); big=(hi is None or hi==k[0])
        o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{9 if big else 6}" fill="{k[11]}" stroke="#111" stroke-width="2"/>'
        if labels and big:
            an,dx,dy=pos[k[0]]
            o+=f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" text-anchor="{an}" font-family="Georgia" font-size="15" font-weight="700" fill="#111">{k[6]} · {k[2].lower()}</text>'
    return o
def series_note(prev=None,nxt=None):
    p=f' Previous: <a href="{PSS}{prev[0]}/">{prev[1]}</a>.' if prev else ''
    n=f' Next: <a href="{PSS}{nxt[0]}/">{nxt[1]}</a>.' if nxt else ''
    return f'<div class="panel reading small"><p>Part of <a href="{PSS}">the Pañcabhūta Sthalas</a>, Śiva’s five temples of the five elements.{p}{n}</p></div>'
def foreword(title_say,paras,q,a,note):
    ps=''.join(f'<p>{x}</p>' for x in paras)
    return f'''<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">{ps}
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#0b2a4a">{title_say}</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk(q,a)}
  {note}
</section>'''
def cover(burst,h1,size,tag,art):
    return f'''<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">{burst}</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp({size}px,{size*0.3:.1f}vw,{size*3}px)">{h1}</h1>
  <div class="series">PAÑCABHŪTA STHALAS · A REFERENCE GUIDE</div>
  <div class="tag">{tag}</div>
  {art}
  {CAST}
</section>'''
def contents(toc):
    return '<section class="page" id="contents">\n  <h2 class="page-title">CONTENTS</h2>\n  <ul class="toc">\n    '+''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))+'\n  </ul>\n</section>\n'
def build(path,head,cov,fw,pages,toc):
    b='<div class="book">\n\n'+cov+'\n\n'+fw+'\n\n'+contents(toc)+''.join(pages)+'</div>\n'
    open(path,'w').write(head+b+tail()); print('ok',len(pages))
