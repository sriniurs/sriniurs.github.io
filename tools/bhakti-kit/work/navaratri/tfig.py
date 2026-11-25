"""Shared figures for Tulu Nadu festivals and Temples of Karnataka (Nov 2026)."""
import math
from fig import g, lab, txt, svg, lamp, lotus, devi, sage, god, demon, mountain, tree, kalasha, bell, conch, sword, trident, elephant, sun, moon, flag, person
from fig2 import river
from fig3 import namaste, arati, plate, coconut, banana, incense, shrine, ganesha, lion
from tfig_base import LINGA, SHIVA, GOP, RATHA
NS='Noto Sans,sans-serif'
def T(x,y,t,size=11,anchor='middle',fill='#111'): return txt(x,y,t,size,anchor,fill=fill,font=NS,weight='700')
def S(label,inner,bg='#fff3cf',h=200,w=560): return svg(w,h,label,f'<rect width="{w}" height="{h}" fill="{bg}"/>'+inner)
def flame(s=1,c='#ffb703'):
    return f'<path d="M0 {-26*s} q{-8*s} {10*s} 0 {17*s} q{8*s} {-7*s} 0 {-17*s}z" fill="{c}" stroke="#e0501a" stroke-width="1.5"/><path d="M0 {-18*s} q{-3*s} {5*s} 0 {8*s} q{3*s} {-3*s} 0 {-8*s}z" fill="#fff3b0" stroke="none"/>'
def lamps_row(x0,y,n,dx=18,s=.45): return ''.join(g(x0+k*dx,y,s,lamp()) for k in range(n))
def tulu_temple(c='#a0522d',roof='#7a3b1f',w=120):
    """Coastal temple: low laterite walls under steep sloping tiled roofs (two tiers) and a kalaśa finial."""
    h=w*.42
    o=f'<rect x="{-w/2}" y="{-h}" width="{w}" height="{h}" fill="#d9a066"/><rect x="-12" y="{-h*.8}" width="24" height="{h*.8}" fill="#5a3a1a"/>'
    o+=f'<path d="M{-w/2-14} {-h} L{-w/4} {-h-28} H{w/4} L{w/2+14} {-h}z" fill="{roof}"/>'
    o+=f'<path d="M{-w/3} {-h-28} L{-w/8} {-h-50} H{w/8} L{w/3} {-h-28}z" fill="{c}"/>'
    o+=f'<path d="M0 {-h-50} v-8" stroke-width="2"/><circle cy="{-h-62}" r="5" fill="#e0a800"/>'
    for k in range(-2,3): o+=f'<path d="M{k*w/6} {-h-2} v-6" stroke="#5a2a10" stroke-width="1.2"/>'
    return o
def vimana(c='#e2cfa8',tiers=4,w=70):
    """Southern (Drāviḍa) shrine tower over a sanctum."""
    o=f'<rect x="{-w/2}" y="-46" width="{w}" height="46" fill="{c}"/><rect x="-9" y="-30" width="18" height="30" fill="#5a3a1a"/>'
    y=-46
    for k in range(tiers):
        ww=w*(1-.18*(k+1)); o+=f'<path d="M{-ww/2-4} {y} h{ww+8} l-4 -14 h{-ww}z" fill="{c if k%2 else "#f2e6c8"}"/>'; y-=14
    o+=f'<path d="M-12 {y} q12 -22 24 0z" fill="#e0a800"/><circle cy="{y-24}" r="4" fill="#e0a800"/>'
    return o
def hoysala_star(r=60):
    """Star-shaped Hoysaḷa plinth seen from above (jagati), with a tower."""
    pts=[]
    for k in range(32):
        rr=r if k%2==0 else r*.82; a=math.radians(k*360/32); pts.append(f'{rr*math.cos(a):.1f},{rr*math.sin(a)*.42:.1f}')
    o=f'<polygon points="{" ".join(pts)}" fill="#8f8a7a"/>'
    o+=f'<rect x="{-r*.55}" y="-52" width="{r*1.1}" height="52" fill="#a7a08c"/>'
    for k in range(6): o+=f'<path d="M{-r*.55} {-8-k*8} h{r*1.1}" stroke="#6f6a5a" stroke-width="1.2"/>'
    o+=f'<path d="M{-r*.4} -52 L0 -96 L{r*.4} -52z" fill="#8f8a7a"/>'
    return o
def bracket_figure(s=1):
    """A madanikā (bracket dancer) silhouette."""
    return g(0,0,s,'<path d="M0 -60 q-6 20 -2 40 q-10 10 -6 20 h16 q4 -10 -6 -20 q4 -20 -2 -40z" fill="#8f8a7a"/><circle cy="-66" r="7" fill="#8f8a7a"/><path d="M-2 -52 q-16 -6 -18 -20 M2 -52 q14 -4 18 -18" fill="none" stroke-width="3"/>')
def boulders(w=200,seed=1):
    o=''
    for k in range(9):
        x=((k*53+seed*17)%w)-w/2; r=10+(k*7+seed)%14
        o+=f'<ellipse cx="{x}" cy="{-r*.7}" rx="{r*1.2}" ry="{r}" fill="{"#c8a27a" if k%2 else "#b08a62"}"/>'
    return o
def drum(c='#c0392b'): return f'<ellipse rx="16" ry="8" fill="#e9d6c0"/><path d="M-16 0 v24 q16 10 32 0 v-24" fill="{c}"/><path d="M-16 4 l32 16 M16 4 l-32 16" stroke="#ffd60a" stroke-width="1.5"/><path d="M8 -22 l10 14 M-8 -22 l-10 14" stroke-width="2.5"/>'
def ball(c='#c0392b'): return f'<circle r="10" fill="{c}"/><path d="M-10 0 h20 M0 -10 q6 10 0 20" fill="none" stroke="#ffd60a" stroke-width="1.5"/>'
def tiger_dancer(pose=1):
    """Pilivēṣa dancer: a man painted in tiger stripes, mask and tail."""
    o='<path d="M-10 -40 h20 l4 30 h-28z" fill="#f4a020"/>'
    o+='<path d="M-6 -36 l4 6 M4 -32 l-4 6 M-8 -24 l6 4 M6 -20 l-6 4" stroke-width="2.2"/>'
    o+='<path d="M-12 -10 l-6 30 M10 -10 l8 30" stroke="#f4a020" stroke-width="8"/><path d="M-14 4 l6 2 M14 4 l-6 2" stroke-width="2"/>'
    o+=f'<path d="M-10 -38 l-16 {-14*pose} M10 -38 l18 {-12*pose}" stroke="#f4a020" stroke-width="7"/>'
    o+='<circle cy="-50" r="11" fill="#f4a020"/><path d="M-7 -55 l4 3 M7 -55 l-4 3 M-4 -46 q4 3 8 0" fill="none" stroke-width="1.8"/><path d="M-9 -60 l-3 -6 M9 -60 l3 -6" stroke-width="2.5"/>'
    o+='<path d="M10 -14 q24 4 22 -20" fill="none" stroke="#f4a020" stroke-width="5"/>'
    return o
def crowd(n=10,w=300,y=0,s=.55):
    cols=['#8e1f17','#1d4f8a','#e0a800','#2a9d6f','#6a3d9a','#c0392b']
    return ''.join(g(-w/2+k*w/(n-1),y,s,person(cols[k%6])) for k in range(n))
def float_cart(inner,c='#c0392b'):
    return f'<rect x="-40" y="-14" width="80" height="14" fill="{c}"/><circle cx="-26" cy="2" r="6" fill="#5a3a1a"/><circle cx="26" cy="2" r="6" fill="#5a3a1a"/><path d="M-40 -14 q40 -8 80 0" fill="none" stroke="#ffd60a" stroke-width="3"/>'+g(0,-14,1,inner)
def sugarcane(h=60): return f'<path d="M0 0 v{-h}" stroke="#4a8a3a" stroke-width="5"/>'+''.join(f'<path d="M-4 {-k*12} h8" stroke-width="1.5"/>' for k in range(1,int(h/12)))+f'<path d="M0 {-h} q-14 -10 -18 -2 M0 {-h} q14 -12 18 -2 M0 {-h} q2 -14 -4 -20" fill="none" stroke="#3a9a4a" stroke-width="3"/>'
def flagpole(h=90,c='#c0392b'): return f'<path d="M0 0 v{-h}" stroke-width="4"/>'+''.join(f'<path d="M-6 {-k*14} h12" stroke-width="2"/>' for k in range(1,int(h/14)))+f'<path d="M0 {-h} l26 8 l-26 8z" fill="{c}"/>'
def fireworks(): return ''.join(f'<path d="M0 0 l{18*math.cos(math.radians(a)):.1f} {18*math.sin(math.radians(a)):.1f}" stroke="#ffd60a" stroke-width="2"/>' for a in range(0,360,30))
def tank(w=160): return f'<rect x="{-w/2}" y="-16" width="{w}" height="16" fill="#4aa3df"/>'+''.join(f'<path d="M{-w/2+k*14} -16 v-4 h14" fill="none" stroke="#8a7a5a" stroke-width="2"/>' for k in range(int(w/14)))
def raft(): return '<path d="M-34 0 h68 l-6 8 h-56z" fill="#c98a5a"/><path d="M-24 0 v-26 h48 v26" fill="none" stroke="#e0a800" stroke-width="3"/><path d="M-28 -26 h56 l-28 -16z" fill="#c0392b"/>'
def map_frame(w=560,h=230,sea=True):
    o=f'<rect width="{w}" height="{h}" fill="#e9f2e1"/>'
    if sea: o+=f'<path d="M0 0 h90 q-20 70 10 130 q-30 60 -10 {h-130} h-90z" fill="#8fb8de" stroke="none"/>'+T(44,h/2,'Arabian Sea',10,fill='#1d4f8a')
    return o+T(w-80,h-8,'simplified, not to scale',9)
def pin(x,y,name,s=.4,anchor='start',dx=20,icon=None):
    return g(x,y,s,icon or shrine())+txt(x+(dx if anchor=='start' else -dx),y-4,name,11,anchor,font=NS,weight='700')
def pot_hanging(c='#c98a5a'): return f'<path d="M0 -30 v14" stroke-width="2"/><ellipse cy="-6" rx="11" ry="10" fill="{c}"/><path d="M-6 -16 h12" stroke-width="2"/>'
def tl_strip(items,w=560,h=120):
    """Simple horizontal timeline."""
    o=f'<path d="M30 {h/2} H{w-30}" stroke-width="3"/>'
    n=len(items)
    for k,(y,t) in enumerate(items):
        x=30+k*(w-60)/(n-1)
        o+=f'<circle cx="{x:.0f}" cy="{h/2}" r="7" fill="#e0a800"/>'+T(x,h/2-16,y,11)+txt(x,h/2+24,t,10,font=NS)
    return o
