# Flat comic figure helpers for the Navarātri series
import math
K='stroke="#111"'
def g(x,y,s,inner,rot=0,flip=False):
    t=f'translate({x} {y}) scale({-s if flip else s} {s})'+(f' rotate({rot})' if rot else '')
    return f'<g transform="{t}" stroke="#111" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">{inner}</g>'
def txt(x,y,t,size=13,anchor='middle',fill='#111',font='Bangers,Impact,sans-serif',weight='400',ls='1'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" font-size="{size}" font-weight="{weight}" letter-spacing="{ls}" fill="{fill}">{t}</text>'
def lab(x,y,t,size=11): return txt(x,y,t,size,font='Noto Sans,sans-serif',weight='700',ls='.3')
# ---------- objects (drawn around 0,0, ~40px) ----------
def lamp(rim='#c0392b'): return f'<path d="M0 -26 q-7 9 0 15 q7 -6 0 -15z" fill="#ffb703" stroke="#e0501a" stroke-width="1.5"/><path d="M-15 -8 q15 16 30 0z" fill="{rim}"/><path d="M-6 -8 h12"/>'
def trident(): return '<path d="M0 30 v-62" stroke-width="3.5"/><path d="M-12 -22 q0 -14 -3 -18 M12 -22 q0 -14 3 -18 M-12 -22 q12 10 24 0 M0 -32 l-4 -8 l4 -6 l4 6z" fill="#e0a800"/>'
def lotus(c='#f4a6b8',c2='#f07a98'): return f'<path d="M0 0 q-18 -5 -21 -18 q13 0 21 11z" fill="{c}"/><path d="M0 0 q18 -5 21 -18 q-13 0 -21 11z" fill="{c}"/><path d="M0 0 q-10 -12 0 -28 q10 16 0 28z" fill="{c2}"/>'
def sword(): return '<path d="M0 26 v-10 M-8 16 h16" stroke-width="3"/><path d="M-3 16 l0 -42 l3 -6 l3 6 l0 42z" fill="#dfe6ee"/>'
def bell(): return '<path d="M0 -20 v-6"/><path d="M-12 8 q0 -26 12 -28 q12 2 12 28z" fill="#e0a800"/><path d="M-15 8 h30"/><circle cy="13" r="3" fill="#a8553a"/>'
def rosary(): return ''.join(f'<circle cx="{14*math.cos(a/12*6.283):.1f}" cy="{14*math.sin(a/12*6.283)-4:.1f}" r="3" fill="#a8553a" stroke-width="1"/>' for a in range(12))+'<circle cy="14" r="4" fill="#e0a800" stroke-width="1"/>'
def kamandalu(): return '<path d="M-11 -6 q-4 18 11 20 q15 -2 11 -20z" fill="#c9783a"/><path d="M-7 -6 q7 -10 14 0" fill="none"/><path d="M11 0 q10 -2 12 -10" fill="none" stroke-width="3"/>'
def pot(c='#e0a800'): return f'<path d="M-12 -6 q-6 16 12 18 q18 -2 12 -18z" fill="{c}"/><rect x="-8" y="-12" width="16" height="6" fill="{c}"/>'
def discus(): return '<circle r="13" fill="#e0a800"/><circle r="5" fill="#fff"/>'+''.join(f'<path d="M0 0 L{13*math.cos(a/8*6.283):.1f} {13*math.sin(a/8*6.283):.1f}"/>' for a in range(8))
def conch(): return '<path d="M-10 10 q-6 -16 6 -24 q14 -4 14 10 q0 12 -20 14z" fill="#fff"/><path d="M-2 -6 q6 2 4 8" fill="none"/>'
def mace(): return '<path d="M0 26 v-34" stroke-width="3.5"/><circle cy="-16" r="10" fill="#e0a800"/>'
def damaru(): return '<path d="M-10 -12 h20 l-10 12 l10 12 h-20 l10 -12z" fill="#c9783a"/>'
def hook(): return '<path d="M0 24 v-40 q12 -2 10 10" fill="none" stroke-width="3"/>'
def vajra(): return '<path d="M0 -20 l-6 8 h12z M0 20 l-6 -8 h12z" fill="#e0a800"/><rect x="-3" y="-12" width="6" height="24" fill="#e0a800"/>'
def book(): return '<path d="M-18 -10 q9 -5 18 0 q9 -5 18 0 v20 q-9 -5 -18 0 q-9 -5 -18 0z" fill="#fff8d0"/><path d="M0 -10 v20"/>'
def abhaya(): return '<path d="M-6 10 v-14 q0 -4 3 -4 v-6 q3 -3 4 0 v-2 q3 -3 4 0 v2 q3 -2 4 1 v13 q0 10 -8 10z" fill="#f2c79b"/>'
def bow(): return '<path d="M-6 -30 q22 30 0 60" fill="none" stroke="#7a4a1a" stroke-width="4"/><path d="M-6 -30 v60" stroke-width="1"/>'
def arrow(): return '<path d="M-26 0 h44" stroke-width="2.5"/><path d="M18 0 l-8 -5 v10z" fill="#111"/><path d="M-26 0 l-5 -5 M-26 0 l-5 5"/>'
def vina():
    fr=''.join(f'<path d="M{-40+i*9} -5 v-5" stroke-width="1.5"/>' for i in range(8))
    return f'<g transform="rotate(-32)"><rect x="-46" y="-10" width="92" height="10" rx="3" fill="#a8553a"/>{fr}<ellipse cx="52" cy="-4" rx="20" ry="18" fill="#c9783a"/><circle cx="-24" cy="12" r="11" fill="#e0a800"/></g>'
def kalasha():
    lv=''.join(f'<path d="M0 -58 q{dx} -14 {dx*1.8} -4 q{-dx} 6 {-dx*1.8} 4z" fill="#2f7a3a"/>' for dx in (-14,-8,8,14))
    return f'<path d="M-26 0 q-14 -30 6 -50 h40 q20 20 6 50z" fill="#c9783a"/><path d="M-20 -50 h40 v-8 h-40z" fill="#a8553a"/><path d="M-24 -26 h48" stroke="#e0a800" stroke-width="4"/>{lv}<ellipse cy="-70" rx="13" ry="15" fill="#8a5a2a"/>'
def moon(): return '<path d="M-14 -6 q14 16 28 0 q-14 8 -28 0z" fill="#fff8d0"/>'
def sun(r=22): return ''.join(f'<path d="M{(r+4)*math.cos(a/12*6.283):.1f} {(r+4)*math.sin(a/12*6.283):.1f} L{(r+12)*math.cos(a/12*6.283):.1f} {(r+12)*math.sin(a/12*6.283):.1f}" stroke="#e0a800" stroke-width="3"/>' for a in range(12))+f'<circle r="{r}" fill="#ffd60a"/>'
def flag(c='#ff8c1a'): return f'<path d="M0 0 v-80" stroke-width="3.5"/><path d="M2 -78 l34 10 l-34 14z" fill="{c}"/>'
def gourd(): return '<ellipse rx="18" ry="14" fill="#a7c957"/><path d="M-12 -6 q12 -6 24 0 M-14 2 q14 -4 28 0" fill="none" stroke-width="1"/><path d="M0 -14 q2 -6 6 -6" fill="none" stroke="#2f7a3a" stroke-width="3"/>'
def egg(): return '<ellipse rx="22" ry="28" fill="#fff3b0"/><path d="M-22 0 q22 10 44 0" fill="none" stroke="#e0a800" stroke-width="2"/>'
def mountain(c='#8a9a8a',snow=True): return f'<path d="M-60 0 L-18 -60 L0 -40 L22 -72 L66 0z" fill="{c}"/>'+('<path d="M-18 -60 l-8 12 l8 -4 l6 6 l6 -8 z M22 -72 l-10 14 l10 -4 l8 6 l4 -6z" fill="#fff"/>' if snow else '')
def tree(c='#2f7a3a'): return f'<path d="M-4 0 v-34 h8 v34z" fill="#8a5a2a"/><circle cy="-46" r="22" fill="{c}"/><circle cx="-16" cy="-36" r="14" fill="{c}"/><circle cx="16" cy="-36" r="14" fill="{c}"/>'
def shami(): return '<path d="M-5 0 q-4 -30 2 -50 h8 q4 20 -1 50z" fill="#8a5a2a"/><path d="M0 -40 q-12 -10 -24 -12 M0 -46 q12 -12 26 -12" fill="none" stroke-width="3"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="11" fill="#5a8a3a"/>' for x,y in [(-26,-56),(-10,-70),(8,-72),(26,-60),(0,-54),(-18,-46),(18,-48)])+'<path d="M-6 -24 q6 -6 12 0 v12 h-12z" fill="#3a2a1a"/>'
def doll(c='#c0392b',c2='#e0a800',crown=True):
    return (f'<path d="M-9 0 l3 -26 h12 l3 26z" fill="{c}"/><circle cy="-32" r="7" fill="#c98a5a"/>'+
            (f'<path d="M-6 -38 l2 -6 l4 4 l4 -4 l2 6z" fill="{c2}"/>' if crown else ''))
def steps(n=5,w=200,h=110,cloth='#fff8ec'):
    o=''
    for i in range(n):
        ww=w-i*(w/(n+1)); o+=f'<rect x="{-ww/2:.0f}" y="{-(i+1)*h/n:.0f}" width="{ww:.0f}" height="{h/n:.0f}" fill="{cloth}"/>'
    return o
def books_stack(): return ''.join(f'<rect x="-22" y="{-12-i*10}" width="44" height="10" fill="{c}"/>' for i,c in enumerate(['#c0392b','#1d6fb8','#2a9d6f','#e0a800']))
def tools(): return '<path d="M-30 10 l20 -20" stroke-width="5" stroke="#8a5a2a"/><path d="M-16 -16 l10 -6 l6 6 l-10 8z" fill="#9aa"/><circle cx="18" cy="0" r="14" fill="none" stroke-width="4"/><circle cx="18" cy="0" r="3" fill="#111"/>'+''.join(f'<path d="M18 0 L{18+14*math.cos(a/6*6.283):.1f} {14*math.sin(a/6*6.283):.1f}"/>' for a in range(6))
def elephant(howdah=True):
    o=('<path d="M-46 0 v-22 q-6 -32 26 -40 q40 -6 52 18 q8 16 2 44 h-12 v-18 h-14 v18 h-14 v-18 h-14 v18z" fill="#8a8f9a"/>'
       '<path d="M30 -26 q18 -2 18 14 q0 22 -8 30 q-4 2 -4 -4 q6 -10 2 -24" fill="#8a8f9a"/><circle cx="26" cy="-30" r="2.5" fill="#111"/>'
       '<path d="M18 -36 q-14 2 -12 18 q8 6 16 0z" fill="#9aa0aa"/><path d="M-40 -34 q30 -8 60 0 v14 q-30 6 -60 0z" fill="#c0392b"/>')
    if howdah: o+='<path d="M-30 -40 h44 l-4 -24 q-18 -14 -36 0z" fill="#e0a800"/><path d="M-8 -68 v-8 M-8 -78 l0 0" /><circle cx="-8" cy="-80" r="4" fill="#e0a800"/><path d="M-24 -48 h32" stroke="#a8553a"/>'
    return o
def palace():
    o='<rect x="-110" y="-60" width="220" height="60" fill="#f3e3c3"/>'
    for x in (-110,-60,0,60,110): o+=f'<path d="M{x-14} -60 q14 -30 28 0z" fill="#e8c06a"/><circle cx="{x}" cy="-86" r="3" fill="#e0a800"/>'
    o+='<path d="M-24 -60 q24 -60 48 0z" fill="#d99a3a"/>'
    for x in range(-96,100,24): o+=f'<path d="M{x} 0 v-26 q6 -8 12 0 v26" fill="#fff"/>'
    for x in range(-108,112,12): o+=f'<circle cx="{x}" cy="-62" r="2" fill="#ffd60a" stroke-width="1"/>'
    return o
def effigy(): 
    heads=''.join(f'<circle cx="{-36+i*8}" cy="-78" r="5" fill="#2a9d6f" stroke-width="1.5"/>' for i in range(10))
    return f'<path d="M-14 0 l4 -50 h20 l4 50z" fill="#c0392b"/><path d="M-14 -46 l-14 24 M14 -46 l14 24" stroke-width="4"/><circle cy="-62" r="12" fill="#2a9d6f"/>{heads}<path d="M-12 -72 h24 l-4 -10 h-16z" fill="#e0a800"/>'
def flames(): return '<path d="M-20 0 q-6 -30 10 -46 q-2 18 10 10 q4 -20 14 -30 q8 24 -2 66z" fill="#ff8c1a"/><path d="M-8 0 q-2 -16 8 -26 q6 14 4 26z" fill="#ffd60a"/>'
def child(): return '<path d="M-8 0 l2 -16 h12 l2 16z" fill="#ff8c1a"/><circle cy="-22" r="7" fill="#f2c79b"/><path d="M-5 -28 l2 -5 l3 3 l3 -3 l2 5z" fill="#e0a800"/>'
def person(c='#1d6fb8',skin='#c98a5a',seat=False):
    return (f'<path d="M-12 0 l4 -34 h16 l4 34z" fill="{c}"/>' if not seat else f'<path d="M-18 0 q0 -12 6 -14 l4 -20 h16 l4 20 q6 2 6 14z" fill="{c}"/>')+f'<circle cy="-42" r="9" fill="{skin}"/>'
def buffalo(): return beast('buffalo')
def beast(kind,c=None):
    col={'lion':'#e0a23a','tiger':'#f08a24','bull':'#f4f1ea','donkey':'#9a9a9a','buffalo':'#3a3a40','owl':'#b08a5a'}[kind] if c is None else c
    o=f'<path d="M-34 -8 q0 -26 30 -26 h24 q16 0 16 20 v6z" fill="{col}"/>'
    o+=''.join(f'<path d="M{x} -10 v22" stroke="{col}" stroke-width="7"/><path d="M{x} -10 v22" fill="none" stroke-width="0"/>' for x in (-28,-16,14,26))
    o+=''.join(f'<rect x="{x-4}" y="-12" width="8" height="24" fill="{col}"/>' for x in (-28,-16,14,26))
    o+=f'<path d="M-34 -24 q-14 -4 -16 -18" fill="none" stroke-width="3"/>'
    if kind=='lion': o+=f'<circle cx="38" cy="-36" r="18" fill="#a8553a"/><circle cx="40" cy="-34" r="11" fill="{col}"/><circle cx="44" cy="-37" r="2" fill="#111"/><path d="M46 -30 q3 2 6 0" fill="none"/>'
    elif kind=='tiger': o+=''.join(f'<path d="M{x} -34 q3 10 0 18" fill="none" stroke-width="3"/>' for x in (-20,-8,4,16))+f'<circle cx="40" cy="-34" r="13" fill="{col}"/><path d="M32 -46 l2 -6 l5 5 M44 -47 l3 -6 l3 6" fill="{col}"/><circle cx="44" cy="-36" r="2" fill="#111"/><path d="M40 -28 h8" />'
    elif kind=='bull': o+=f'<path d="M-2 -34 q6 -12 14 0z" fill="{col}"/><path d="M28 -28 q4 -16 18 -14 q8 6 4 18 q-10 6 -22 -4z" fill="{col}"/><path d="M36 -40 q-4 -10 -10 -10 M44 -40 q4 -10 10 -10" fill="none" stroke-width="3"/><circle cx="44" cy="-34" r="2" fill="#111"/>'
    elif kind=='donkey': o+=f'<path d="M28 -30 q6 -14 18 -10 q6 6 4 18 q-10 6 -22 -8z" fill="{col}"/><path d="M34 -40 l-4 -16 l6 2z M40 -40 l2 -16 l5 4z" fill="{col}"/><circle cx="44" cy="-32" r="2" fill="#111"/>'
    elif kind=='buffalo': o+=f'<path d="M28 -28 q4 -16 18 -14 q8 6 4 18 q-10 6 -22 -4z" fill="{col}"/><path d="M30 -38 q-14 -14 -26 -6 q10 0 18 10 M48 -38 q14 -14 26 -6 q-10 0 -18 10" fill="#d9d2c0"/><circle cx="44" cy="-32" r="2.5" fill="#ff5a4a" stroke="none"/>'
    return o
def devi(skin='#f2c79b',sari='#c0392b',items=('trident','lotus'),crown='#e0a800',halo='#ffd60a',seat=False,hair_open=False,fierce=False,third_eye=True,moon_c=False,child_lap=False):
    o=f'<circle cy="-62" r="30" fill="{halo}" stroke-width="1.5" opacity=".9"/>'
    o+=(f'<path d="M-22 0 q-2 -30 8 -44 h28 q10 14 8 44z" fill="{sari}"/>' if not seat else f'<path d="M-34 0 q0 -14 14 -18 l6 -26 h28 l6 26 q14 4 14 18z" fill="{sari}"/>')
    o+=f'<path d="M-14 -44 q14 8 28 0" fill="none" stroke="#e0a800" stroke-width="3"/>'
    n=len(items)
    for k,it in enumerate(items):
        ang=math.radians(-172+ (164*(k+.5)/n))
        r=44 if n>2 else 36
        hx,hy=r*math.cos(ang), -36+r*math.sin(ang)*0.9
        sx=-10 if hx<0 else 10
        o+=f'<path d="M{sx} -40 L{hx:.0f} {hy:.0f}" stroke="#111" stroke-width="7.5"/><path d="M{sx} -40 L{hx:.0f} {hy:.0f}" stroke="{skin}" stroke-width="4.5"/>'
        o+=f'<g transform="translate({hx:.0f} {hy:.0f}) scale(.6)">{ITEMS[it]()}</g>'
    o+=f'<circle cy="-56" r="13" fill="{skin}"/>'
    if hair_open: o+=f'<path d="M-13 -60 q-12 20 -8 40 M13 -60 q12 20 8 40 M-6 -68 q-14 -4 -16 -14 M6 -68 q14 -4 16 -14" fill="none" stroke="#111" stroke-width="3"/>'
    else: o+=f'<path d="M-13 -58 q0 -14 13 -14 q13 0 13 14 q-6 -8 -13 -8 q-7 0 -13 8z" fill="#151515"/>'
    o+=f'<path d="M-11 -70 l3 -12 l5 6 l3 -9 l3 9 l5 -6 l3 12z" fill="{crown}"/>'
    if moon_c: o+='<path d="M-6 -86 q6 6 12 0 q-6 3 -12 0z" fill="#fff8d0"/>'
    o+=f'<circle cx="-4.5" cy="-56" r="1.6" fill="#111"/><circle cx="4.5" cy="-56" r="1.6" fill="#111"/>'
    if third_eye: o+='<path d="M0 -63 v-3" stroke="#c0392b" stroke-width="2"/>'
    o+=('<path d="M-5 -50 q5 4 10 0" fill="#c0392b"/>' if fierce else '<path d="M-4 -50 q4 3 8 0" fill="none"/>')
    if child_lap: o+=f'<g transform="translate(0 -14) scale(.9)">{child()}</g>'
    return o
ITEMS={'trident':trident,'lotus':lotus,'sword':sword,'bell':bell,'rosary':rosary,'kamandalu':kamandalu,'pot':pot,'discus':discus,
       'conch':conch,'mace':mace,'damaru':damaru,'hook':hook,'vajra':vajra,'book':book,'abhaya':abhaya,'bow':bow,'arrow':arrow,
       'redpot':lambda:pot('#9a2a1a')}
def shiva(skin='#9fb7d6'):
    return (f'<circle cy="-62" r="28" fill="#dfe9f6" stroke-width="1.5"/><path d="M-20 0 q-2 -30 8 -44 h24 q10 14 8 44z" fill="#f3e3c3"/>'
            f'<path d="M-12 -40 q12 10 24 0" fill="none" stroke="#3a3a40" stroke-width="3"/><circle cy="-56" r="12" fill="{skin}"/>'
            f'<path d="M-9 -66 q9 -16 18 0 q-2 -10 -9 -12 q-7 2 -9 12z" fill="#5a3a1a"/><path d="M-6 -78 q6 6 12 0" fill="none" stroke="#fff8d0" stroke-width="2"/>'
            f'<circle cx="-4" cy="-56" r="1.5" fill="#111"/><circle cx="4" cy="-56" r="1.5" fill="#111"/><path d="M-6 -62 h12" stroke="#fff" stroke-width="1.5"/>'
            f'<g transform="translate(26 -10) scale(.5)">{trident()}</g>')
def sage(c='#ff8c1a'): return f'<path d="M-16 0 q0 -14 6 -16 l2 -18 h16 l2 18 q6 2 6 16z" fill="{c}"/><circle cy="-42" r="9" fill="#c98a5a"/><path d="M-7 -38 q7 14 14 0 q-2 10 -7 12 q-5 -2 -7 -12z" fill="#eee"/><path d="M-6 -50 q6 -8 12 0 l-2 -6 h-8z" fill="#5a3a1a"/>'
def god(c='#1d6fb8'): return f'<path d="M-12 0 l3 -32 h18 l3 32z" fill="{c}"/><circle cy="-40" r="9" fill="#f2c79b"/><path d="M-7 -48 l7 -10 l7 10z" fill="#e0a800"/>'
def demon(c='#2a6a3a'): return f'<path d="M-16 0 l4 -34 h24 l4 34z" fill="{c}"/><circle cy="-42" r="11" fill="{c}"/><path d="M-8 -52 l-6 -8 M8 -52 l6 -8" stroke-width="3"/><circle cx="-4" cy="-43" r="2" fill="#ff5a4a" stroke="none"/><circle cx="4" cy="-43" r="2" fill="#ff5a4a" stroke="none"/><path d="M-5 -36 h10"/>'
# ---------- composers ----------
def svg(w,h,label,inner,bg='#fffaf0',cls='pg-fig'):
    return f'<svg class="{cls}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}"><rect width="{w}" height="{h}" fill="{bg}"/>{inner}</svg>'
def ground(w,h,y,c='#e9d6c0'): return f'<rect y="{y}" width="{w}" height="{h-y}" fill="{c}"/>'
def strip(label,panels,caps):
    # three panels in 460x210
    o=''
    for i,(inner,bg) in enumerate(panels):
        x=8+i*150
        o+=f'<g transform="translate({x} 8)"><clipPath id="cp{abs(hash(label))%9999}{i}"><rect width="144" height="170" rx="6"/></clipPath><g clip-path="url(#cp{abs(hash(label))%9999}{i})"><rect width="144" height="170" fill="{bg}"/>{inner}</g><rect width="144" height="170" rx="6" fill="none" stroke="#111" stroke-width="3"/></g>'
        o+=lab(x+72,198,caps[i],10.5)
    return f'<svg class="fig" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="{label}"><rect width="460" height="210" fill="#fffaf0"/>{o}</svg>'
