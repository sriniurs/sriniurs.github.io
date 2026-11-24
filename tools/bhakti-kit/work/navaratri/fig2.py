from fig import *
import re
def vishnu(sit=False): return devi(skin='#5a8ad0',sari='#e0a800',items=('discus','conch','mace','lotus'),halo='#fff3b0',seat=sit,third_eye=False)
def krishna_child(): return '<path d="M-10 0 l3 -18 h14 l3 18z" fill="#e0a800"/><circle cy="-25" r="9" fill="#5a8ad0"/><path d="M-6 -33 q6 -8 12 0" fill="#151515"/><path d="M4 -36 q8 -10 10 -2" fill="none" stroke="#2a9d6f" stroke-width="2"/><circle cx="-3" cy="-25" r="1.3" fill="#111"/><circle cx="3" cy="-25" r="1.3" fill="#111"/>'
def mortar(): return '<path d="M-16 0 l4 -30 h24 l4 30z" fill="#8a6a4a"/><path d="M-14 -30 h28" stroke-width="3"/>'
def sheshashayi():
    o='<path d="M-90 0 q90 20 180 0 q-10 -14 -40 -14 h-100 q-30 0 -40 14z" fill="#2a9d6f"/>'
    o+=''.join(f'<path d="M{70+k*9} -14 q8 -28 0 -50" fill="none" stroke="#2a9d6f" stroke-width="9"/>' for k in range(-2,3))
    o+='<path d="M-60 -18 h110 q10 -10 0 -16 h-110z" fill="#e0a800"/><circle cx="-66" cy="-30" r="11" fill="#5a8ad0"/><path d="M-74 -40 l8 -10 l8 10z" fill="#e0a800"/>'
    return o
def tulasi(): return '<path d="M-26 0 h52 l-6 -34 h-40z" fill="#c9783a"/><path d="M-30 -34 h60 v-8 h-60z" fill="#a8553a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="4" fill="#3a8a3a" transform="rotate({r} {x} {y})"/>' for x,y,r in [(-10,-52,-30),(10,-52,30),(-14,-66,-40),(14,-66,40),(0,-60,0),(-6,-78,-20),(6,-78,20),(0,-88,0)])+'<path d="M0 -42 v-50" stroke="#3a6a2a" stroke-width="2"/>'
def crow(): return '<path d="M-14 0 q-4 -14 8 -18 h10 l12 -4 l-8 8 q4 10 -6 14z" fill="#222"/><circle cx="2" cy="-14" r="1.5" fill="#fff"/><path d="M10 -18 l8 -2 l-8 4" fill="#555"/>'
def river(w=560,y=150,c='#8fb8de'): return f'<path d="M0 {y} q{w/4} -16 {w/2} 0 t{w/2} 0 v{60} h{-w}z" fill="{c}" stroke="#111" stroke-width="2"/>'
def cow(): return beast('bull','#f4f1ea')
def hill_flame(): return '<path d="M-90 0 L0 -90 L90 0z" fill="#8a7a5a"/>'+'<g transform="translate(0 -90)">'+flames()+'</g>'
def pillar_fire(): return '<rect x="-14" y="-160" width="28" height="160" fill="#ff8c1a"/><path d="M-14 -160 q14 -20 28 0" fill="#ffd60a"/>'+''.join(f'<path d="M{-14+(k%2)*28} {-20-k*18} q{-10 if k%2==0 else 10} -6 0 -12" fill="none" stroke="#ffd60a" stroke-width="3"/>' for k in range(8))
def boat_lamp(): return '<path d="M-14 0 q14 8 28 0 l-4 -6 h-20z" fill="#5a8a3a"/><g transform="translate(0 -4) scale(.6)">'+lamp('#e0a800')+'</g>'
def sacred_thread(): return '<path d="M-20 -40 q20 30 40 60" fill="none" stroke="#f4f1ea" stroke-width="5"/><path d="M-20 -40 q20 30 40 60" fill="none" stroke="#e0a800" stroke-width="1.5"/>'
def rakhi(): return '<path d="M-40 0 h80" stroke="#c0392b" stroke-width="4"/><circle r="12" fill="#e0a800"/><circle r="5" fill="#c0392b"/>'+''.join(f'<path d="M0 0 L{14*math.cos(a)} {14*math.sin(a)}" stroke="#ff8c1a" stroke-width="2"/>' for a in [0,.8,1.6,2.4,3.2,4,4.8,5.6])
def gooseberry(): return tree('#4a7a3a')+''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#c9e27a" stroke="#111" stroke-width="1"/>' for x,y in [(-10,-40),(8,-50),(14,-34),(-16,-30)])
def pot_rice(): return pot('#a8553a')+'<path d="M-12 -12 q12 -10 24 0" fill="#fff"/>'
def kolam(): return ''.join(f'<circle cx="{x}" cy="{y}" r="2" fill="#fff" stroke="none"/>' for x in range(-40,44,16) for y in range(-24,28,16))+'<path d="M-40 0 q20 -30 40 0 t40 0 M-40 0 q20 30 40 0 t40 0" fill="none" stroke="#fff" stroke-width="2.5"/>'
def piNDa(): return ''.join(f'<circle cx="{x}" cy="-8" r="8" fill="#f3e3c3" stroke="#111" stroke-width="1.5"/>' for x in (-20,0,20))+'<path d="M-34 0 h68" stroke="#3a8a3a" stroke-width="5"/>'
def fig_row(label,items,labels=(),w=560,h=180,bg='#fffaf0',gy=None):
    # items: list of (svg, scale) drawn evenly across
    n=len(items); o=''
    if gy: o+=ground(w,h,gy)
    for k,(inner,s) in enumerate(items):
        x=w*(k+.5)/n; o+=g(x,(gy or h-22),s,inner)
    for k,t in enumerate(labels):
        if t: o+=lab(w*(k+.5)/n,h-6,t)
    return svg(w,h,label,o,bg=bg)
def panel(items,bg='#fff3cf',gy=None):
    n=len(items); o=''
    if gy: o+=f'<rect y="{gy}" width="144" height="{170-gy}" fill="#e9d6c0"/>'
    for k,(inner,s) in enumerate(items):
        x=144*(k+.5)/n; o+=g(x,(gy or 160),s,inner)
    return (o,bg)
# ITRANS -> IAST
def itrans(t):
    rep=[('R^i','ṛ'),('R^I','ṝ'),('L^i','ḷ'),('~N','ṅ'),('~n','ñ'),('chh','ch'),('Ch','ch'),('sh','ś'),('Sh','ṣ'),('aa','ā'),('ii','ī'),('uu','ū'),('A','ā'),('I','ī'),('U','ū'),('T','ṭ'),('D','ḍ'),('N','ṇ'),('M','ṃ'),('H','ḥ'),('.a',"’"),('|','.')]
    t=t.replace('ch','c').replace('cc','cc')
    # 'ch' in ITRANS = c ; 'Ch' = ch (aspirate)
    out=t
    for a,b in rep:
        if a=='chh' or a=='Ch': continue
        out=out.replace(a,b)
    out=out.replace('Ch','ch').replace('’’','’').replace('  ',' ')
    return out
