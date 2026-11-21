import sys,re,math,json
sys.path.insert(0,'/home/claude/work/devim')
import common as _cm
from common import *
_s5=open('/home/claude/work/devim/build5.py').read()
exec(_s5[_s5.index('def KING'):_s5.index('V=[')])
_s6=open('/home/claude/work/devim/build6.py').read()
exec(_s6[_s6.index('def VISHNU_SLEEP'):_s6.index('\nV=[')])

GT='/bhakti/vishnu/bhagavad-gita/'
TXT=json.load(open('/home/claude/work/gita/gita_iast.json'))
B='#e3f2fd'
CH=[(1,'Arjuna Viṣāda Yoga','Arjuna’s despair',47),(2,'Sāṅkhya Yoga','The undying Self',72),(3,'Karma Yoga','The path of action',43),
 (4,'Jñāna Karma Sannyāsa Yoga','Knowledge and action',42),(5,'Karma Sannyāsa Yoga','Renouncing and doing',29),(6,'Dhyāna Yoga','Meditation',47),
 (7,'Jñāna Vijñāna Yoga','Knowing and realising',30),(8,'Akṣara Brahma Yoga','The imperishable',28),(9,'Rāja Vidyā Rāja Guhya Yoga','The royal secret',34),
 (10,'Vibhūti Yoga','Divine glories',42),(11,'Viśvarūpa Darśana Yoga','The cosmic form',55),(12,'Bhakti Yoga','Devotion',20),
 (13,'Kṣetra Kṣetrajña Vibhāga Yoga','The field and its knower',34),(14,'Guṇatraya Vibhāga Yoga','The three guṇas',27),(15,'Puruṣottama Yoga','The supreme person',20),
 (16,'Daivāsura Sampad Vibhāga Yoga','Divine and demonic',24),(17,'Śraddhātraya Vibhāga Yoga','Three kinds of faith',28),(18,'Mokṣa Sannyāsa Yoga','Freedom by letting go',78)]
def chl(n,t=None): return f'<a href="{GT}chapter-{n}/">{t or "Chapter "+str(n)}</a>'
OVL=f'<a href="{GT}overview/">Overview</a>'

def make_head(title,desc):
    src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
    head=src[:src.find('<div class="book">')]
    head=re.sub(r'<!-- (seo|sitenav|bhaktitrail):auto -->.*?<!-- /\1:auto -->','',head,flags=re.S)
    head=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',head)
    head=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',head)
    head=head.replace('</style>','''  .iast .cl2{padding-left:2.2em}
  .full .ln2{padding-left:2.2em}
  .full p{margin:0 0 6px}
  .iast .spk,.full .spk{display:block;font-style:normal;font-family:Bangers,Impact,sans-serif;letter-spacing:1px;color:var(--blue);font-size:13px;margin-top:2px}
  .full .col{display:block;margin-top:10px;font-size:13px;color:#5b6f8a}
  .pt{font-size:14.5px;line-height:1.45;margin:8px 0}
  .toc.tight{gap:5px;grid-template-columns:repeat(3,1fr)}.toc.tight li{padding:3px 8px;font-size:13px}.toc.tight .part{font-size:16px}
  .vfig svg{max-height:150px;width:auto}
  .key a{color:#8fd3ff;text-decoration:underline}
  .grid2{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:8px 0}
  .grid2>div{border:3px solid var(--ink);background:#fff;padding:7px 9px;box-shadow:3px 3px 0 var(--ink);font-size:13.5px;line-height:1.4}
  .grid2 h4{margin:0 0 2px;font-family:Bangers,Impact,sans-serif;letter-spacing:1px;font-size:17px;color:var(--blue)}
  @media(max-width:720px){.iast .cl2{padding-left:1.4em}.full .ln2{padding-left:1.4em}.grid2{grid-template-columns:1fr}}
</style>''',1)
    return head
def tail():
    src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
    t=src[src.find('<script>\n  document.querySelectorAll'):]
    return re.sub(r'<!-- (seo|sitenav|bhaktitrail):auto -->.*?<!-- /\1:auto -->','',t,flags=re.S)

# ---------- text ----------
def vids(ch,nums):
    nums=str(nums)
    if '–' in nums: a,b=nums.split('–'); return [f'{ch}.{k}' for k in range(int(a),int(b)+1)]
    return [f'{ch}.{nums}']
def vlines(vid,num=True):
    v=TXT[vid]; b=list(v['body']); n=vid.split('.')[1]
    if num: b[-1]=b[-1]+f' ‖{n}‖'
    out=[('sp',s) for s in v['sp']]
    mid=v.get('mid')
    pairs=[]
    for i in range(0,len(b),2):
        pairs.append([b[i],b[i+1] if i+1<len(b) else ''])
    for k,p in enumerate(pairs):
        if mid and len(b)==2:
            out+= [[p[0],''],('sp',mid[1]),[p[1],'']]
        else: out.append(p)
    return out
def iast(lines):
    o='<div class="iast">'
    for x in lines:
        if x[0]=='sp': o+=f'<span class="spk">{x[1]}</span>'
        else:
            o+=f'<span class="cl">{x[0]}</span>'
            if x[1]: o+=f'<span class="cl cl2">{x[1]}</span>'
    return o+'</div>'
def fpv(vid):
    o=f'<p><span class="vn">{vid}</span>'
    for x in vlines(vid):
        if x[0]=='sp': o+=f'<span class="spk">{x[1]}</span>'; continue
        a,b=x
        for t,c in ((a,'ln'),(b,'ln ln2')):
            if not t: continue
            t=re.sub(r'\s*‖([\w–]+)‖$',r'<span class="end">‖ \1 ‖</span>',t)
            o+=f'<span class="{c}">{t}</span>'
    return o+'</p>'
def vnlines(nums,ch):
    out=[]
    for vid in vids(ch,nums): out+=vlines(vid)
    return out

def G(ch,nums,theme,scene,mean,words,point,key,tk=None,note=None,lab=None):
    n=str(nums)
    return dict(n=n,ch=ch,lab=lab or (('ŚLOKAS ' if '–' in n else 'ŚLOKA ')+f'{ch}.{n}'),lines=vnlines(n,ch),theme=theme,svg=scene,mean=mean,words=words,point=point,key=key,note=note,talk=tk)

def vpage(v):
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    tk=f"\n  {talk(*v['talk'])}" if v.get('talk') else ''
    nl=sum(1 for x in v['lines'] if x[0]!='sp')
    cls='page long' if nl>=4 or len(v['lines'])>=4 else 'page'
    return f'''<section class="{cls}" id="v{v['n']}">
  <h2 class="page-title">{v['lab']}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(v['lines'])}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>
    {'<table class="ct"><tr><th>Word</th><th>Means</th></tr>'+words+'</table>' if words else ''}
  </div>
  <div class="panel reading pt">{v['point']}</div>{tk}
  <div class="key">{v['key']}</div>{note}
</section>
'''
def sc(label,body,bg=B): return svg(label,body,bg)

def textpage(id_,title,sub,body,tk=None,key=None):
    return f'''<section class="page" id="{id_}">
  <h2 class="page-title">{title}</h2>
  <div class="sub">{sub}</div>
  {body}
  {talk(*tk) if tk else ''}
  {f'<div class="key">{key}</div>' if key else ''}
</section>
'''
def grid(items): return '<div class="grid2">'+''.join(f'<div><h4>{h}</h4>{t}</div>' for h,t in items)+'</div>'

# ---------- figures ----------
def KR(x,y,s=1,flute=False,arms4=False):
    a=('<path d="M-26 0 l-26 -22 M26 0 l26 -22" stroke="#3b6fd0" stroke-width="7"/><circle cx="-54" cy="-26" r="9" fill="#ffd60a" stroke="#111"/><path d="M48 -34 q8 -6 14 2 q-6 8 -14 4z" fill="#fff"/>') if arms4 else ''
    fl='<path d="M-40 -14 l70 -12" stroke="#7a4a1a" stroke-width="5"/>' if flute else '<path d="M-22 -4 l-14 10 M22 -4 l14 10" stroke="#3b6fd0" stroke-width="7"/>'
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">{a}<path d="M-30 50 q-4 -60 30 -70 q34 10 30 70z" fill="#ffd60a"/>'
     +fl+'<circle cy="-36" r="15" fill="#3b6fd0"/><path d="M-14 -46 h28 l-4 -12 h-20z" fill="#e0a800"/><path d="M4 -58 q12 -22 22 -8 q-10 2 -22 8z" fill="#2a9d6f"/><circle cx="18" cy="-60" r="3.5" fill="#3b8fd0"/>'
     '<circle cx="-5" cy="-38" r="2.4" fill="#fff"/><circle cx="5" cy="-38" r="2.4" fill="#fff"/><path d="M-6 -29 q6 5 12 0" fill="none"/><path d="M-18 -10 q18 14 36 0" fill="none" stroke="#f08aa6" stroke-width="3"/></g>')
def AR(x,y,s=1,mood='ok',bow=True):
    face={'ok':'<path d="M-6 -27 q6 5 12 0" fill="none"/>','sad':'<path d="M-6 -24 q6 -5 12 0" fill="none"/><path d="M-6 -33 l2 6 M6 -33 l-2 6" stroke="#3b8fd0" stroke-width="2"/>','wow':'<ellipse cy="-26" rx="4" ry="5" fill="#111"/>','folded':'<path d="M-6 -27 q6 5 12 0" fill="none"/>'}[mood]
    b=('<path d="M30 -60 q-22 50 0 100" fill="none" stroke="#7a4a1a" stroke-width="5"/><path d="M30 -60 v100" stroke="#ccc" stroke-width="1.5"/>' if bow else '')
    if mood=='folded': b='<path d="M-4 -6 l4 -16 l4 16z" fill="#c98b5a"/>'
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">{b}<path d="M-28 50 q-4 -58 28 -66 q32 8 28 66z" fill="#f4f4f4"/><path d="M-26 20 h52" stroke="#c0392b" stroke-width="6"/>'
     '<circle cy="-34" r="14" fill="#c98b5a"/><path d="M-14 -42 h28 l-3 -14 l-6 6 l-5 -9 l-5 9 l-6 -6z" fill="#ffd60a"/><circle cx="-5" cy="-36" r="2" fill="#111"/><circle cx="5" cy="-36" r="2" fill="#111"/>'+face+'</g>')
def HORSE4(x,y,s=1):
    return f'<g transform="translate({x} {y}) scale({s})">'+''.join(f'<g transform="translate({k*14} {-k*6})" stroke="#111" stroke-width="2"><rect x="-28" y="-14" width="50" height="22" rx="10" fill="#fdfdfd"/><path d="M18 -10 l14 -20 l8 4 l-8 22z" fill="#fdfdfd"/><path d="M-20 8 v16 M-6 8 v16 M8 8 v16 M16 8 v16" stroke-width="4"/></g>' for k in (3,2,1,0))+'</g>'
def RATHA(x,y,s=1,kr=True,ar=True,armood='ok',arbow=True,horses=True):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
    if horses: g+=HORSE4(70,-10,.8)
    g+='<path d="M0 -150 v120" stroke="#7a4a1a" stroke-width="4"/><path d="M0 -150 l34 8 l-34 10z" fill="#ff8c1a"/><circle cx="12" cy="-142" r="4" fill="#7a4a1a"/>'
    if ar: g+=AR(-18,-58,.62,armood,arbow)
    if kr: g+=KR(22,-52,.6)
    g+='<path d="M-44 -30 h96 l-8 22 h-80z" fill="#e0a800"/><circle cx="-26" cy="-4" r="16" fill="#fff"/><circle cx="-26" cy="-4" r="4" fill="#111"/><circle cx="30" cy="-4" r="16" fill="#fff"/><circle cx="30" cy="-4" r="4" fill="#111"/>'
    if horses: g+='<path d="M52 -26 q30 -10 50 -12" fill="none" stroke="#7a4a1a" stroke-width="2"/>'
    return g+'</g>'
def KINGB(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2"><path d="M-12 -46 h24 l-3 -12 l-5 5 l-4 -8 l-4 8 l-5 -5z" fill="#ffd60a"/>'
     '<circle cy="-30" r="12" fill="#c98b5a"/><path d="M-12 -32 h24" stroke="#555" stroke-width="5"/><path d="M-18 22 q18 -54 36 0z" fill="#7a2a6a"/></g>')
def SANJ(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2"><circle cy="-30" r="20" fill="#ffd60a" opacity=".35" stroke="none"/>'
     '<circle cy="-30" r="12" fill="#c98b5a"/><circle cy="-34" r="2.5" fill="#3b8fd0"/><path d="M-18 22 q18 -54 36 0z" fill="#fff"/></g>')
def SOLDIER(x,y,s=1,c='#c0392b'):
    return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cy="-26" r="8" fill="#c98b5a"/><path d="M-8 -32 h16 v-4 h-16z" fill="#888"/><path d="M-12 14 q12 -40 24 0z" fill="{c}"/><path d="M14 18 v-54" stroke="#7a5a3a" stroke-width="2.5"/><path d="M11 -36 l3 -8 l3 8z" fill="#ccc"/></g>'
def ARMY(x0,y,n,c='#c0392b',dx=18,s=.6): return ''.join(SOLDIER(x0+k*dx,y,s,c) for k in range(n))
def CONCH(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-16 0 q-4 -18 12 -22 q18 -2 22 14 q-14 -2 -18 10 q-10 6 -16 -2z" fill="#fff"/><path d="M-6 -14 q8 -2 12 4" fill="none"/></g>'
def YOGI(x,y,s=1,c='#ff8c1a',skin='#c98b5a',glow=True):
    gl=f'<circle cy="-34" r="22" fill="#ffd60a" opacity=".35" stroke="none"/>' if glow else ''
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2">{gl}<path d="M-34 14 q34 -22 68 0 q-34 12 -68 0z" fill="{c}"/>'
     f'<path d="M-16 6 q-2 -30 16 -34 q18 4 16 34z" fill="{c}"/><circle cy="-36" r="11" fill="{skin}"/><path d="M-6 -36 h4 M2 -36 h4" stroke-width="2"/>'
     '<path d="M-14 4 q-10 -4 -14 6 M14 4 q10 -4 14 6" fill="none"/></g>')
def LAMP(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-18 0 q18 14 36 0z" fill="#e0a800"/><path d="M0 -2 q-8 -14 0 -30 q8 16 0 30z" fill="#ffd60a"/><path d="M0 -6 q-3 -8 0 -16 q3 8 0 16z" fill="#ff8c1a" stroke="none"/></g>'
def TORT(x,y,s=1,hidden=False):
    legs='' if hidden else '<circle cx="34" cy="0" r="8" fill="#8ab070"/><path d="M-22 12 l-6 8 M22 12 l6 8" stroke="#8ab070" stroke-width="6"/>'
    return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">{legs}<ellipse rx="30" ry="16" fill="#5a8a3a"/><path d="M-16 -8 l10 8 l12 -8 l10 8" fill="none" stroke="#3a5a2a"/></g>'
def TREE_INV(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M0 -60 v90" stroke="#7a5a3a" stroke-width="8"/>'
     +''.join(f'<path d="M0 -60 q{d*20} -10 {d*40} -4" fill="none" stroke="#7a5a3a" stroke-width="3"/>' for d in (-1,1))
     +''.join(f'<circle cx="{dx}" cy="{dy}" r="14" fill="#2a9d6f"/>' for dx,dy in [(-30,20),(30,20),(0,36),(-16,4),(16,4)])+'</g>')
def COSMIC(x,y,s=1):
    st=''.join(f'<circle cx="{-30+15*(k%5)}" cy="{-10+14*(k//5)}" r="1.8" fill="#fff" stroke="none"/>' for k in range(20))
    arms=''.join(f'<path d="M0 0 l{70*math.cos(a):.0f} {50*math.sin(a):.0f}" stroke="#5b8fe0" stroke-width="6"/>' for a in [i*math.pi/7-math.pi for i in range(8)])
    heads=''.join(f'<circle cx="{dx}" cy="-46" r="11" fill="#5b8fe0"/>' for dx in (-36,-18,18,36))
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'+arms+heads+'<path d="M-36 70 q-6 -80 36 -86 q42 6 36 86z" fill="#1d3f8a"/>'+st+
     '<circle cy="-48" r="15" fill="#3b6fd0"/><path d="M-14 -58 h28 l-4 -12 h-20z" fill="#e0a800"/><circle cx="-5" cy="-50" r="3" fill="#ffd60a"/><circle cx="5" cy="-50" r="3" fill="#ffd60a"/></g>')
def GUNA3(x,y,s=1,labels=True):
    o=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
    for k,(c,t) in enumerate([('#fff8c0','SATTVA'),('#e05a3a','RAJAS'),('#2b2b3a','TAMAS')]):
        o+=f'<circle cx="{(k-1)*40}" cy="0" r="18" fill="{c}"/>'
        if labels: o+=f'<text x="{(k-1)*40}" y="34" text-anchor="middle" {F} font-size="10" stroke="none" fill="#111">{t}</text>'
    return o+'</g>'
FIELD='<rect width="220" height="160" fill="#ffe3c4"/><path d="M0 130 h220 V160 H0z" fill="#c9a26b" stroke="#111"/>'
SKY='<rect width="220" height="160" fill="#e3f2fd"/>'
NIGHT2='<rect width="220" height="160" fill="#0d1b3a"/>'
GLOW=lambda x,y,r,c='#ffd60a',o=.35: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{o}" stroke="none"/>'
WAVES=lambda y=120,c='#3b8fd0': f'<path d="M0 {y} q27 -12 55 0 t55 0 t55 0 t55 0 V160 H0z" fill="{c}" stroke="#111" stroke-width="2"/>'
def BUBBLE(x,y,t,w=90,s=10): return f'<rect x="{x-w/2}" y="{y-14}" width="{w}" height="22" rx="10" fill="#fff" stroke="#111" stroke-width="2"/>'+T(x,y+2,t,s)

# ---------- page builder ----------
def full_pages(ch,nv,per,extra0=None):
    ids=([extra0] if extra0 else [])+[f'{ch}.{k}' for k in range(1,nv+1)]
    pages=[];i=0;k=0
    while i<len(ids):
        n=per[k] if k<len(per) else per[-1]
        pages.append(ids[i:i+n]); i+=n; k+=1
    return pages
def build(P):
    ch=P['ch']; head=make_head(P['title'],P['desc'])
    seq=P['seq']
    vs=[x for x in seq if isinstance(x,dict)]
    fulls=''
    fp=full_pages(ch,P['nv'],P['per'],P.get('extra0'))
    for k,ids in enumerate(fp):
        last=(k==len(fp)-1)
        a=ids[0].split('.')[1]; b=ids[-1].split('.')[1]
        body=''.join(fpv(i) for i in ids)
        if last and f'col{ch}' in TXT: body+=f'<p><span class="col">{TXT["col"+str(ch)]}</span></p>'
        fulls+=f'''
<section class="page" id="full{k or ''}">
  <h2 class="page-title">{'THE CHAPTER IN ONE GO' if k==0 else 'IN ONE GO · CONTINUED'}</h2>
  <div class="sub">Chapter {ch}, ślokas {a}–{b}{' (of '+str(P['nv'])+')' if k==0 else ''}</div>
  <div class="full">{body}</div>{('<div class="note">'+P['fullnote']+'</div>') if last else ''}
</section>
'''
    toc=''
    for grp,items in P['toc']:
        toc+=f'<li class="part">{grp}</li>'
        for it in items:
            if isinstance(it,dict): toc+=f'<li><span class="num">{it["n"].split("–")[0]}</span><a href="#v{it["n"]}">{it["theme"].title().replace("’S","’s")}</a></li>'
            else: toc+=f'<li><span class="num">★</span><a href="#{it[0]}">{it[1]}</a></li>'
    where=''.join(f'<p>{p}</p>' for p in P['where'])
    out=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">{P['burst']}</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,{P.get('h1size',72)}px)">{P['h1']}</h1>
  <div class="series">{P['series']}</div>
  <div class="tag">{P['tag']}</div>
  {P['cover']}
  {CAST}
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> {P['how']}
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">WHERE WE ARE</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    {where}
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--blue)">With the blessings of the Lord,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk(*P['wtalk'])}
</section>
{fulls}
<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">←</span><a href="#foreword">Where We Are</a></li>
    <li><span class="num">🔤</span><a href="#full">The Chapter in One Go</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    {toc}
  </ul>
</section>
''']
    for x in seq: out.append(vpage(x) if isinstance(x,dict) else x)
    steps=''.join(f'<div>{s}</div>' for s in P['end'])
    out.append(f'''<section class="page" id="end">
  <h2 class="page-title">CHAPTER {ch} ON ONE PAGE</h2>
  <div class="sub">{P['endsub']}</div>
  <div class="steps">{steps}</div>
  {talk(*P['next'])}
  <div class="key">Chapter {ch}: {P['endkey']} 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">{P['foot']}</footer>
</div>
''')
    html=head+''.join(out)+tail()
    open(P['out'],'w').write(html)
    print('ok',P['out'])
FULLNOTE=('Text: the standard 700-verse Gītā as printed by Gītā Press, Gorakhpur, taken from the public-domain bhagavadgita.io edition and checked line by line against the IIT Kanpur Gita Supersite; '
 'transliterated into IAST. Words are run together as in the printed text (saṃhitā).')
def FOOT(ch,extra=''):
    return (f'Study notes on the Bhagavad Gītā, chapter {ch} (Mahābhārata, Bhīṣma Parva). Ślokas follow the Gītā Press text and numbering, checked against the IIT Kanpur Gita Supersite, in IAST. '
     'Where the great commentators (Śaṅkara, Rāmānuja, Madhva and others) read a verse differently, we say so; such readings are interpretation. '+extra+
     'Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.')

# ================= v2: every śloka, two pages =================
def S(label,left='K',right=None,cap=None,bg=B,extra=''):
    """quick scene: a speaker on the left, an icon/scene on the right, a caption bubble on top"""
    fig={'K':KR(58,118,.95),'A':AR(58,120,.95),'As':AR(58,120,.95,'sad',False),'Af':AR(58,120,.95,'folded',False),'S':SANJ(58,132,1.4),'D':KINGB(58,132,1.4),'KA':KR(40,118,.8)+AR(86,124,.7,'folded',False),'Y':YOGI(58,132,1.2),'P':person(58,132,'#ff8c1a','#c98b5a',1.2),'':''}[left]
    r=ICON(right) if right else ''
    c=BUBBLE(110,22,cap,max(80,len(cap)*7.2),10) if cap else ''
    return sc(label,fig+r+c+extra,bg)
def ICON(k,x=158,y=100,s=1):
    g=lambda inner: f'<g transform="translate({x} {y}) scale({s})">{inner}</g>'
    D={'fire':FIRE(0,30,1.1),'sun':SUN(0,-10,26),'moon':MOON(0,-10,18),'lamp':LAMP(0,20,1.8),'yogi':YOGI(0,40,1.1),'tort':TORT(0,10,1.1),'tree':TREE(0,56,1),'invtree':TREE_INV(0,10,.9),
       'ocean':WAVES(0)[0:0]+'<path d="M-50 10 q12 -10 25 0 t25 0 t25 0 t25 0 V50 H-50z" fill="#3b8fd0" stroke="#111" stroke-width="2"/>','guna':GUNA3(0,0,.9),'cosmic':COSMIC(0,0,.55),'conch':CONCH(0,0,2),
       'army':ARMY(-48,40,5,'#7a2a6a',22,.6),'armyb':ARMY(-48,40,5,'#1d6fb8',22,.6),'chariot':RATHA(0,64,.5),'scale':'<path d="M0 -40 v70 M-40 -20 h80" stroke="#111" stroke-width="4"/><path d="M-40 -20 l-14 26 h28z M40 -20 l-14 26 h28z" fill="#ffd60a" stroke="#111" stroke-width="2"/>',
       'heart':'<path d="M0 30 q-50 -30 -30 -54 q18 -16 30 6 q12 -22 30 -6 q20 24 -30 54z" fill="#e05a8a" stroke="#111" stroke-width="2"/>','book':'<rect x="-34" y="-24" width="68" height="48" fill="#fff3b0" stroke="#111" stroke-width="2.5"/><path d="M0 -24 v48" stroke="#111" stroke-width="2"/>',
       'light':GLOW(0,0,40,'#ffd60a',.5)+GLOW(0,0,18,'#ffd60a',.95),'om':GLOW(0,0,36,'#ffd60a',.45)+f'<text x="0" y="14" text-anchor="middle" {F} font-size="40">OṂ</text>','wheel':'<circle r="36" fill="none" stroke="#e0a800" stroke-width="6"/>'+''.join(f'<path d="M0 0 l{36*math.cos(k*.785):.0f} {36*math.sin(k*.785):.0f}" stroke="#e0a800" stroke-width="3"/>' for k in range(8)),
       'lotus':MOUNT('lotus',0,10,2),'cow':'<g stroke="#111" stroke-width="2"><ellipse rx="34" ry="18" fill="#fff"/><circle cx="-36" cy="-10" r="11" fill="#fff"/><path d="M-20 16 v18 M20 16 v18 M-8 16 v18 M8 16 v18"/></g>','mountain':'<path d="M-50 40 L-10 -30 L10 0 L30 -20 L60 40z" fill="#9fb3c8" stroke="#111" stroke-width="2"/><path d="M-18 -16 l8 -14 l8 14" fill="#fff"/>',
       'star':''.join(f'<text x="{(k*29)%90-45}" y="{(k*37)%80-40}" {F} font-size="12" fill="#ffd60a">✦</text>' for k in range(9)),'sword':'<path d="M-30 30 L30 -30" stroke="#ccc" stroke-width="7"/><path d="M-34 14 l20 20" stroke="#111" stroke-width="5"/>','bow':'<path d="M0 -50 q-30 50 0 100" fill="none" stroke="#7a4a1a" stroke-width="6"/><path d="M0 -50 v100" stroke="#999"/>',
       'demon':DEMON(0,30,1.1),'food':''.join(f'<circle cx="{-30+k*20}" cy="10" r="9" fill="{c}" stroke="#111"/>' for k,c in enumerate(['#e0a800','#2a9d6f','#c0392b','#fff8c0'])),'gift':'<rect x="-28" y="-20" width="56" height="44" fill="#c0392b" stroke="#111" stroke-width="2"/><path d="M0 -20 v44 M-28 0 h56" stroke="#ffd60a" stroke-width="5"/>',
       'family':''.join(person(-36+k*24,30,c,'#c98b5a',.55) for k,c in enumerate(['#fff','#ff8c1a','#7a2a6a','#2a9d6f'])),'crown':'<path d="M-30 20 h60 l-8 -34 l-12 12 l-10 -22 l-10 22 l-12 -12z" fill="#ffd60a" stroke="#111" stroke-width="2"/>',
       'storm':'<ellipse cx="0" cy="-10" rx="44" ry="20" fill="#5b6f8a" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{-30+k*15} 14 l-4 14" stroke="#3b8fd0" stroke-width="2"/>' for k in range(5)),'river':'<path d="M-50 -40 q40 30 0 50 q-30 20 50 40" fill="none" stroke="#3b8fd0" stroke-width="10"/>',
       'death':'<path d="M-30 40 h60 v-50 q-30 -26 -60 0z" fill="#999" stroke="#111" stroke-width="2"/>','seed':'<path d="M0 30 v-30" stroke="#2a9d6f" stroke-width="4"/><path d="M0 0 q-20 -10 -24 -26 q20 2 24 26 q4 -24 24 -26 q-4 16 -24 26z" fill="#9be38a" stroke="#111"/><ellipse cy="34" rx="20" ry="6" fill="#7a5a3a"/>',
       'mind':'<ellipse rx="44" ry="30" fill="#fff" stroke="#111" stroke-width="2"/>'+''.join(f'<path d="M{-30+k*15} {-6+(k%2)*10} q6 -8 12 0" fill="none" stroke="#c0392b" stroke-width="2"/>' for k in range(5)),'chain':''.join(f'<ellipse cx="{-36+k*18}" cy="0" rx="12" ry="7" fill="none" stroke="#555" stroke-width="4"/>' for k in range(5)),
       'gods':''.join(GOD(-40+k*20,30,.45,'#ffd60a','#c98b5a') for k in range(5)),'sage':SAGE(0,40,1.3),'king':KING(0,40,1.3),'brahma':BRAHMA(0,0,.6),'vishnu':KR(0,20,.9,arms4=True)}
    return g(D[k]) if k in D else g(k)
def X(n,theme,svg_,mean,words,ctx,read,life,key,tk=None,note=None):
    return dict(n=str(n),theme=theme,svg=svg_,mean=mean,words=words,ctx=ctx,read=read,life=life,key=key,talk=tk,note=note)
def vpageA(ch,v):
    vid=f'{ch}.{v["n"]}'; lines=vlines(vid)
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    nl=sum(1 for x in lines if x[0]!='sp')
    cls='page long' if nl>=3 else 'page'
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    return f'''<section class="{cls}" id="v{v['n']}">
  <h2 class="page-title">ŚLOKA {vid}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(lines)}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>
    <table class="ct"><tr><th>Word</th><th>Means</th></tr>{words}</table>
  </div>
  <div class="key">{v['key']}</div>{note}
</section>
'''
def vpageB(ch,v):
    vid=f'{ch}.{v["n"]}'
    tk=f"\n  {talk(*v['talk'])}" if v.get('talk') else ''
    return f'''<section class="page" id="d{v['n']}">
  <h2 class="page-title">ŚLOKA {vid} · DEEP DIVE</h2>
  <div class="sub">{v['theme'].capitalize() if False else v['theme']}</div>
  <div class="dd"><h4>🔎 In context</h4><p>{v['ctx']}</p></div>
  <div class="dd"><h4>📜 Looking deeper</h4><p>{v['read']}</p></div>
  <div class="dd"><h4>🌱 For today</h4><p>{v['life']}</p></div>{tk}
  <div class="key"><a href="#v{v['n']}" style="color:#8fd3ff">↑ {vid}</a> · {v['key']}</div>
</section>
'''
DDCSS='''  .dd{border:3px solid var(--ink);background:#fff;padding:9px 12px;margin:10px 0;box-shadow:4px 4px 0 var(--ink)}
  .dd h4{margin:0 0 4px;font-family:Bangers,Impact,sans-serif;letter-spacing:1px;font-size:19px;color:var(--blue)}
  .dd p{margin:0;font-size:15px;line-height:1.5}
  .toc.vt{grid-template-columns:repeat(4,1fr);gap:3px}.toc.vt li{padding:2px 6px;font-size:11.5px}
  @media(max-width:720px){.toc.vt{grid-template-columns:repeat(2,1fr)}}
</style>'''
def build2(P):
    ch=P['ch']; head=make_head(P['title'],P['desc']).replace('</style>',DDCSS,1)
    vs=P['V']; assert [v['n'] for v in vs]==[str(k) for k in range(1,P['nv']+1)], 'verse list incomplete'
    fulls=''
    fp=full_pages(ch,P['nv'],P['per'],P.get('extra0'))
    for k,ids in enumerate(fp):
        last=(k==len(fp)-1); a=ids[0].split('.')[1]; b=ids[-1].split('.')[1]
        body=''.join(fpv(i) for i in ids)
        if last and f'col{ch}' in TXT: body+=f'<p><span class="col">{TXT["col"+str(ch)]}</span></p>'
        fulls+=f'''
<section class="page" id="full{k or ''}">
  <h2 class="page-title">{'THE CHAPTER IN ONE GO' if k==0 else 'IN ONE GO · CONTINUED'}</h2>
  <div class="sub">Chapter {ch}, ślokas {a}–{b}{' (of '+str(P['nv'])+')' if k==0 else ''}</div>
  <div class="full">{body}</div>{('<div class="note">'+P['fullnote']+'</div>') if last else ''}
</section>
'''
    # sections: list of (title, first verse number, [extra story pages placed before that verse])
    secs=P['secs']; story=P.get('story',{})
    toc=''
    bounds=[s[1] for s in secs]+[P['nv']+1]
    for i,(t,a) in enumerate(secs):
        toc+=f'<li class="part">{t}</li>'
        for sid,stt in [(x[0],x[1]) for x in story.get(a,[])]: toc+=f'<li><span class="num">★</span><a href="#{sid}">{stt}</a></li>'
        for v in vs[a-1:bounds[i+1]-1]:
            tt=v['theme'].title().replace('’S','’s')
            toc+=f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{tt}</a></li>'
    where=''.join(f'<p>{p}</p>' for p in P['where'])
    out=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">{P['burst']}</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,{P.get('h1size',72)}px)">{P['h1']}</h1>
  <div class="series">{P['series']}</div>
  <div class="tag">{P['tag']}</div>
  {P['cover']}
  {CAST}
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> {P.get('how',HOW2)}
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">WHERE WE ARE</h2>
  <div class="panel bg-saffron halftone" style="font-size:17px;line-height:1.6">
    {where}
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--blue)">With the blessings of the Lord,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk(*P['wtalk'])}
</section>
{fulls}''']
    # contents may need 2 pages
    items=re.findall(r'<li.*?</li>',toc)
    per=P.get('tocper',44); chunks=[items[i:i+per] for i in range(0,len(items),per)]
    for k,c in enumerate(chunks):
        extra='<li class="part">START HERE</li><li><span class="num">←</span><a href="#foreword">Where We Are</a></li><li><span class="num">🔤</span><a href="#full">In One Go</a></li><li><span class="num">∑</span><a href="#end">On One Page</a></li>' if k==0 else ''
        out.append(f'''
<section class="page" id="contents{k or ''}">
  <h2 class="page-title">{'CONTENTS' if k==0 else 'CONTENTS · CONTINUED'}</h2>
  <ul class="toc tight vt">{extra}{''.join(c)}</ul>
</section>
''')
    for i,(t,a) in enumerate(secs):
        for x in story.get(a,[]): out.append(x[2])
        for v in vs[a-1:bounds[i+1]-1]: out.append(vpageA(ch,v)+vpageB(ch,v))
    steps=''.join(f'<div>{s}</div>' for s in P['end'])
    out.append(f'''<section class="page" id="end">
  <h2 class="page-title">CHAPTER {ch} ON ONE PAGE</h2>
  <div class="sub">{P['endsub']}</div>
  <div class="steps">{steps}</div>
  {talk(*P['next'])}
  <div class="key">Chapter {ch}: {P['endkey']} 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">{P['foot']}</footer>
</div>
''')
    open(P['out'],'w').write(head+''.join(out)+tail())
    print('ok',P['out'],'sections',sum(o.count('<section class="page') for o in out))
HOW2='The whole chapter <b>in one go</b> for chanting, then <b>every śloka on two pages</b>: first the chant, a picture, what it says and the key words; then a deep dive into its context, how the great teachers read it, and what it means for us today.'
