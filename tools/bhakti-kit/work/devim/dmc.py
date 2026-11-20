import sys,re,math
sys.path.insert(0,'/home/claude/work/devim')
from common import *
_s5=open('/home/claude/work/devim/build5.py').read()
exec(_s5[_s5.index('def KING'):_s5.index('V=[')])
_s6=open('/home/claude/work/devim/build6.py').read()
exec(_s6[_s6.index('def VISHNU_SLEEP'):_s6.index('\nV=[')])
DM='/bhakti/devi/devi-mahatmya/'
def plink(n): return f'<a href="{DM}part-{n}/">Part {n}</a>'

# ---------- extra figures ----------
def BUFFALO(x,y,s=1,c='#2b2b2b'):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2">'
     f'<rect x="-34" y="-18" width="64" height="32" rx="14" fill="{c}"/><circle cx="34" cy="-14" r="14" fill="{c}"/>'
     '<path d="M26 -24 q-12 -16 2 -22 M42 -24 q12 -16 -2 -22" stroke="#ddd" stroke-width="4" fill="none"/>'
     '<circle cx="38" cy="-16" r="2.5" fill="#e33" stroke="none"/><path d="M-24 14 v14 M-8 14 v14 M12 14 v14 M24 14 v14" stroke="#111" stroke-width="4"/>'
     '<path d="M-34 -10 q-12 6 -10 20" fill="none" stroke="#111" stroke-width="3"/></g>')
def GOD(x,y,s=1,body='#ffd60a',skin='#c98b5a',crown=True):
    c='<path d="M-10 -44 h20 l-3 -10 l-4 4 l-3 -7 l-3 7 l-4 -4z" fill="#ffd60a"/>' if crown else ''
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2">{c}'
     f'<circle cy="-30" r="12" fill="{skin}"/><path d="M-18 22 q18 -54 36 0z" fill="{body}"/></g>')
def GODS(y=150,s=.6,n=5,x0=30,dx=40):
    cols=[('#ffd60a','#3b6fd0'),('#fff','#9fd3f0'),('#ff8c1a','#e0a800'),('#c0392b','#c98b5a'),('#2a9d6f','#c98b5a'),('#9b5de5','#c98b5a')]
    return ''.join(GOD(x0+k*dx,y,s,*cols[k%6]) for k in range(n))
def GLOW(x,y,r,c='#ffd60a',o=.35): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{o}" stroke="none"/>'
def KALI(x,y,s=1): return DEVI(x,y,s,True,'#2b2140','#3a3a5a','#111')
def ASURA(x,y,s=1,c='#5a2a6a',big=False):
    return DEMON(x,y,s*(1.3 if big else 1),c)
def SWORD(x,y,a=0,s=1): return f'<g transform="translate({x} {y}) rotate({a}) scale({s})" stroke="#111" stroke-width="2"><path d="M0 0 v-44 l4 -8 l4 8 v44z" fill="#ddd"/><path d="M-6 0 h20" stroke-width="4"/><path d="M4 0 v10" stroke-width="4"/></g>'
def TRIDENT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.5" fill="none"><path d="M0 40 v-70"/><path d="M-12 -40 q0 14 12 14 q12 0 12 -14 M0 -30 v-16"/></g>'
def ARROWS(x,y,n=5,s=1): return ''.join(f'<path d="M{x+k*10*s} {y} l{18*s} {-18*s}" stroke="#111" stroke-width="2"/><path d="M{x+k*10*s+18*s} {y-18*s} l-6 1 l1 -6z" fill="#111"/>' for k in range(n))
def SPEECH(x,y,t,w=80,s=11): return f'<ellipse cx="{x}" cy="{y}" rx="{w/2}" ry="16" fill="#fff" stroke="#111" stroke-width="2"/>'+T(x,y+4,t,s)
def CHARIOT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-24" y="-20" width="48" height="22" fill="#c9a26b"/><circle cx="-14" cy="6" r="10" fill="#fff"/><circle cx="14" cy="6" r="10" fill="#fff"/><path d="M0 -20 v-26" /><path d="M0 -46 l18 6 l-18 6z" fill="#c0392b"/></g>'
FLOWERS=lambda n=14: ''.join(f'<text x="{(37*k)%210+5}" y="{(23*k)%70+12}" font-size="11">🌸</text>' for k in range(n))
NIGHTSKY='<rect width="220" height="160" fill="#2b2140"/>'
BATTLE='<rect width="220" height="160" fill="#ffe3c4"/><path d="M0 130 h220 V160 H0z" fill="#c9a26b" stroke="#111"/>'
HIMA='<rect width="220" height="160" fill="#dfe9f6"/>'+HILLS
def ELEPHANT(x,y,s=1): return MOUNT('elephant',x,y,s)
def sc(label,body,bg=R): return svg(label,body,bg)

# ---------- verse source parsing ----------
def L(src):
    """'a / b || 3||' or 'a / b | / c / d || 3||' -> pairs"""
    src=src.replace('ṁ','ṃ').replace('Ṁ','Ṃ').strip()
    src=re.sub(r'\s*\|\|\s*([\d–\-]+)\s*\|\|\s*$',lambda m:' ‖'+m.group(1).replace('-','–')+'‖',src)
    src=re.sub(r'\s*\|\|\s*([\d–\-]+)\s*\|\|\s*/',lambda m:' ‖'+m.group(1)+'‖ /',src)
    src=re.sub(r'\s+\|\s*/',' | /',src)
    parts=[p.strip() for p in src.split(' / ')]
    if len(parts)%2: parts.append('')
    return [[parts[i],parts[i+1]] for i in range(0,len(parts),2)]

def VP(ch,n,src,theme,scene,mean,words,point,key,note=None,tk=None,lab=None):
    return dict(n=n,lab=lab or (('ŚLOKAS ' if ('–' in n or '-' in n) else 'ŚLOKA ')+f'{ch}.{n}'),lines=L(src),theme=theme,svg=scene,mean=mean,words=words,point=point,key=key,note=note,talk=tk)

def full_html(vs,ch):
    return ''.join(fp(f'{ch}.{v["n"]}',v['lines']) for v in vs)

# ---------- page builder ----------
def build(P):
    n=P['n']; ch=P.get('ch','')
    head=make_head(P['title'],P['desc'])
    seq=P['seq']
    vs=[x for x in seq if isinstance(x,dict)]
    for v in vs:
        if P.get('hymn'): v['lab']+=' · '+P['hymn']
    fulls=''
    for k,(ft,fsub,fv) in enumerate(P['fulls']):
        fulls+=f'''
<section class="page" id="full{k or ''}">
  <h2 class="page-title">{ft}</h2>
  <div class="sub">{fsub}</div>
  <div class="full">{full_html(fv,ch)}</div>{('<div class="note">'+P['fullnote']+'</div>') if (k==len(P['fulls'])-1 and P.get('fullnote')) else ''}
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
  <div class="burst yel">PART {n} OF 19</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,{P.get('h1size',76)}px)">{P['h1']}</h1>
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
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:var(--red)">With the blessings of the Devī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk(*P['wtalk'])}
</section>
{fulls}
<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">←</span><a href="#foreword">Where We Are</a></li>
    <li><span class="num">🔤</span><a href="#full">{P.get('fulltoc','The Verses in One Go')}</a></li>
    <li><span class="num">∑</span><a href="#end">On One Page</a></li>
    {toc}
  </ul>
</section>
''']
    for x in seq:
        if isinstance(x,dict):
            h=vpage(x)
            if len(x['lines'])>=4 or P.get('long'): h=h.replace(f'<section class="page" id="v{x["n"]}">',f'<section class="page long" id="v{x["n"]}">',1)
            out.append(h)
        else: out.append(x)
    steps=''.join(f'<div>{s}</div>' for s in P['end'])
    out.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART {n} ON ONE PAGE</h2>
  <div class="sub">{P['endsub']}</div>
  <div class="steps">{steps}</div>
  {talk(*P['next'])}
  <div class="key">Part {n}: {P['endkey']} 🙏</div>
  {FOLLOW}
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">{P['foot']}</footer>
</div>
''')
    open(P['out'],'w').write(head+''.join(out)+tail())
    print('ok',P['out'])
