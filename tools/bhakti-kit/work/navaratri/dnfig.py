"""Figures for the Durgā Namaskāra Pūjā article."""
import math
from fig import g, lab, txt, svg, lamp, lotus, devi, sage, god, demon, strip, mountain, tree, kalasha, bell, conch, sword, trident
from fig3 import namaste, arati, plate, coconut, banana, incense, leaf, shrine
def S(label,inner,bg='#fff3cf',h=200): return svg(560,h,label,f'<rect width="560" height="{h}" fill="{bg}"/>'+inner)
def flame(s=1,c='#ffb703'):
    return f'<path d="M0 {-26*s} q{-8*s} {10*s} 0 {17*s} q{8*s} {-7*s} 0 {-17*s}z" fill="{c}" stroke="#e0501a" stroke-width="1.5"/><path d="M0 {-18*s} q{-3*s} {5*s} 0 {8*s} q{3*s} {-3*s} 0 {-8*s}z" fill="#fff3b0" stroke="none"/>'
def kaludipa(h=120,heads=5):
    """Tall standing brass lamp (kālu-dīpa / kāl-dīpa): base, stem, bowl, flames."""
    b='#d8a520'
    o=f'<path d="M-30 0 q30 -14 60 0 z" fill="{b}"/><ellipse cy="0" rx="30" ry="5" fill="#b8860b"/>'
    o+=f'<rect x="-4" y="{-h+16}" width="8" height="{h-18}" fill="{b}"/>'
    for y in (-h*0.35,-h*0.65): o+=f'<ellipse cy="{y:.0f}" rx="9" ry="4" fill="#b8860b"/>'
    o+=f'<path d="M-30 {-h+16} q30 18 60 0 z" fill="{b}"/><path d="M-30 {-h+16} h60" stroke-width="2.5"/>'
    xs=[-24,-12,0,12,24][:heads] if heads==5 else [0]
    for x in xs: o+=f'<g transform="translate({x} {-h+15})">{flame(.8 if x else 1.05)}</g>'
    o+=f'<path d="M-6 {-h+16} l6 -6 l6 6" fill="none"/>'
    return o
def petal(r1,r2,a,c,ry=1):
    a=math.radians(a); x1,y1=r1*math.cos(a),r1*math.sin(a)*ry; x2,y2=r2*math.cos(a),r2*math.sin(a)*ry
    pa=a+math.pi/2; w=(r2-r1)*.38
    cx,cy=(x1+x2)/2,(y1+y2)/2
    return f'<path d="M{x1:.1f} {y1:.1f} Q{cx+w*math.cos(pa):.1f} {cy+w*math.sin(pa)*ry:.1f} {x2:.1f} {y2:.1f} Q{cx-w*math.cos(pa):.1f} {cy-w*math.sin(pa)*ry:.1f} {x1:.1f} {y1:.1f}z" fill="{c}"/>'
def mandala_floor(R=150,ry=.36,lamp_h=120,small=8):
    """Mandala on the floor in perspective, a tall lamp standing at its centre, small lamps on the rim."""
    o=f'<path d="M{-R} 0 L0 {-R*ry} L{R} 0 L0 {R*ry}z" fill="#c0392b"/>'
    o+=f'<path d="M{-R*.86} 0 L0 {-R*ry*.86} L{R*.86} 0 L0 {R*ry*.86}z" fill="#fff8ec"/>'
    o+=f'<ellipse rx="{R*.72}" ry="{R*.72*ry}" fill="#e0a800"/>'
    for k in range(8): o+=petal(R*.22,R*.68,k*45+22.5,'#f07a98' if k%2 else '#ff8c1a',ry)
    o+=f'<ellipse rx="{R*.24}" ry="{R*.24*ry}" fill="#2a9d6f"/>'
    for k in range(small):
        a=math.radians(k*360/small); o+=g(R*.8*math.cos(a),R*.8*ry*math.sin(a)+2,.55,lamp())
    o+=g(0,4,1,kaludipa(lamp_h))
    return o
def mandala_top(R=82,labels=True):
    """Top-down plan of a Durgā maṇḍala: square with four gates, eight-petal lotus, six-point star, lamp at the bindu."""
    o=f'<rect x="{-R}" y="{-R}" width="{2*R}" height="{2*R}" fill="#c0392b"/>'
    gw=R*.32
    for ang in (0,90,180,270):
        o+=f'<g transform="rotate({ang})"><rect x="{-gw/2}" y="{-R-10}" width="{gw}" height="14" fill="#c0392b"/><rect x="{-gw/2+5}" y="{-R-5}" width="{gw-10}" height="9" fill="#fff8ec" stroke="none"/></g>'
    o+=f'<rect x="{-R+8}" y="{-R+8}" width="{2*R-16}" height="{2*R-16}" fill="#fff8ec"/>'
    o+=f'<circle r="{R*.84}" fill="#e0a800"/>'
    for k in range(8): o+=petal(R*.36,R*.82,k*45+22.5,'#f07a98' if k%2 else '#ff8c1a')
    o+=f'<circle r="{R*.38}" fill="#fff8ec"/>'
    t=R*.36
    tri=lambda rot:' '.join(f'{t*math.cos(math.radians(rot+a)):.1f},{t*math.sin(math.radians(rot+a)):.1f}' for a in (-90,30,150))
    o+=f'<polygon points="{tri(0)}" fill="none" stroke="#c0392b" stroke-width="2.5"/><polygon points="{tri(180)}" fill="none" stroke="#1d4f8a" stroke-width="2.5"/>'
    o+=f'<circle r="7" fill="#c0392b"/>'+g(0,3,.55,flame(1))
    return o
def bee(): return '<ellipse rx="9" ry="6" fill="#ffd60a"/><path d="M-3 -6 v12 M3 -6 v12" stroke-width="2.5"/><ellipse cx="-3" cy="-9" rx="5" ry="4" fill="#fff" opacity=".9"/><ellipse cx="4" cy="-9" rx="5" ry="4" fill="#fff" opacity=".9"/><circle cx="10" cy="0" r="3" fill="#111"/>'
def bees(n=12,w=120,h=60,seed=3):
    o=''
    for k in range(n):
        x=((k*37+seed*11)%w)-w/2; y=-((k*23+seed*7)%h)
        o+=g(x,y,.6+.2*(k%3),bee())
    return o
def vedas_scroll(c='#fff8e7'): return f'<rect x="-14" y="-30" width="28" height="30" rx="3" fill="{c}"/><path d="M-9 -22 h18 M-9 -15 h18 M-9 -8 h12" stroke="#888" stroke-width="1.5"/>'
def cracked(w=144,y=150): return f'<rect y="{y}" width="{w}" height="40" fill="#c9a36b"/>'+''.join(f'<path d="M{x} {y+4} l8 10 l-6 10 l10 8" fill="none" stroke="#7a5a2a" stroke-width="1.5"/>' for x in range(10,w,34))
def greens(): return ''.join(f'<g transform="translate({x} 0)"><path d="M0 0 q-10 -14 -4 -26 q10 10 4 26z" fill="#3a9a4a"/><path d="M0 0 q12 -12 8 -24 q-12 6 -8 24z" fill="#2f7a3a"/></g>' for x in (-20,-6,8,22))
def letters(): 
    ls=['a','ā','i','ī','u','ū','ṛ','e','ai','o','au','ka','ca','ṭa','ta','pa','ya','śa','ha','kṣa']
    return ls
def fort(): return '<path d="M-50 0 v-50 h12 v8 h10 v-8 h12 v8 h10 v-8 h12 v8 h10 v-8 h12 v50z" fill="#c9a36b"/><path d="M-12 0 v-24 q12 -14 24 0 v24z" fill="#5a3a1a"/>'
def prostrate(c='#8e1f17'): return f'<rect x="-40" y="-12" width="70" height="12" rx="6" fill="{c}"/><circle cx="38" cy="-7" r="8" fill="#c98a5a"/><path d="M44 -4 l14 0" stroke-width="3"/>'
def priest(): return sage('#f4f1ea')
def wave(w=560,y=150,c='#2a5a8a'): return f'<path d="M0 {y} q{w/8} -10 {w/4} 0 t{w/4} 0 t{w/4} 0 t{w/4} 0 v80 h{-w}z" fill="{c}" stroke="none"/>'
def boat(): return '<path d="M-40 0 h80 l-12 14 h-56z" fill="#c98a5a"/><path d="M0 0 v-46 l26 34z" fill="#fff8ec"/>'
def rock(): return '<path d="M-40 0 q-6 -30 14 -44 q20 -14 40 -2 q22 10 26 46z" fill="#8a8f9a"/>'
def heart(): return '<path d="M0 30 q-60 -40 -40 -70 q20 -24 40 0 q20 -24 40 0 q20 30 -40 70z" fill="#f6c3c3"/>'
