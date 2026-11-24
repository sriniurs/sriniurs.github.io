from fig import *
from fig2 import *
from fig3 import *
NIGHT='#20243a'
def nightsky(w=560,h=190): return f'<rect width="{w}" height="{h}" fill="{NIGHT}"/>'+''.join(f'<circle cx="{(37*k)%w}" cy="{(23*k*k)%(h-60)+8}" r="1.5" fill="#fff8d0" stroke="none"/>' for k in range(1,22))
def lamps_row(n,x0,dx,y,s=1.2): return ''.join(g(x0+k*dx,y,s,lamp()) for k in range(n))
def umbrella(): return '<path d="M0 0 v-40" stroke-width="2.5"/><path d="M-22 -36 q22 -24 44 0z" fill="#e0a800"/>'
def vamana(): return g(0,0,.75,person('#e0a800'))+g(14,-30,.8,umbrella())
def bali(c='#7a3fa0'): return god(c)+'<path d="M-10 -47 l2 -12 l4 6 l4 -9 l4 9 l4 -6 l2 12z" fill="#e0a800"/>'
def yama(): return god('#2a3a5a')
def lakshmi(): return devi(sari='#c0392b',items=('lotus','lotus'))
def krishna(): return god('#2a5aa8')
def garuda(): return g(0,0,1.6,bird('#c0582a'))
def big_step(): return '<path d="M0 0 q-4 -60 30 -120" fill="none" stroke="#2a5aa8" stroke-width="14"/><ellipse cx="34" cy="-124" rx="18" ry="9" fill="#2a5aa8"/>'
def lantern(c='#e0a800'): return f'<path d="M0 -40 v8"/><path d="M0 -32 l16 16 l-16 30 l-16 -30z" fill="{c}"/><path d="M-6 14 l-2 14 M0 14 v16 M6 14 l2 14" stroke="#c0392b"/>'
def rangoli(): return ''.join(f'<circle r="{r}" fill="none" stroke="{c}" stroke-width="4"/>' for r,c in [(36,'#c0392b'),(26,'#e0a800'),(16,'#2a9d6f'),(6,'#7a3fa0')])+''.join(f'<circle cx="{40*__import__("math").cos(k*0.785):.1f}" cy="{40*__import__("math").sin(k*0.785):.1f}" r="5" fill="#fff" stroke="#c0392b"/>' for k in range(8))
def pot_deco(): return pot('#c98a5a')+'<path d="M-14 -14 h28" stroke="#fff" stroke-width="3" stroke-dasharray="3 3"/><circle cy="-6" r="3" fill="#c0392b"/>'
def apamarga(): return '<path d="M0 0 v-46" stroke="#2f7a3a" stroke-width="2.5"/>'+''.join(f'<path d="M0 -{8+k*9} l{(-1)**k*12} -6" stroke="#2f7a3a" stroke-width="2"/>' for k in range(5))
def coins(): return ''.join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="4" fill="#e0a800"/>' for x,y in [(-12,0),(8,0),(-2,-6),(14,-8),(-8,-12)])
def ledger(): return '<rect x="-20" y="-26" width="40" height="30" rx="3" fill="#c0392b"/><path d="M-12 -18 h24 M-12 -10 h24" stroke="#e0a800" stroke-width="2"/><text x="0" y="-2" font-size="9" text-anchor="middle" fill="#fff" stroke="none" font-family="Noto Sans">śubha</text>'
def balifig(): return '<path d="M-26 0 l26 -52 l26 52z" fill="#6a5a3a"/><circle cy="-30" r="5" fill="#ffd60a"/>'+''.join(g(x,-6,.4,lotus('#ff8c1a','#e0a800')) for x in (-14,0,14))
L=lambda u,t: f'<a href="{u}">{t}</a>'

def fire(): return '<path d="M-30 0 l10 -10 l-6 -20 l14 8 l4 -26 l10 20 l8 -14 l2 22 l10 -6 l-6 26z" fill="#ff8c1a"/><path d="M-14 0 l4 -14 l6 6 l4 -16 l6 14 l6 -6 l2 16z" fill="#ffd60a"/><path d="M-36 4 h72" stroke="#6a4a2a" stroke-width="6"/>'
def pyre(): return '<path d="M-40 0 l40 -50 l40 50z" fill="#8a6a3a"/>'+''.join(f'<path d="M{x} 0 l{-x/3:.0f} -46" stroke="#6a4a2a" stroke-width="3"/>' for x in (-30,-15,0,15,30))
def splash(c): return f'<circle r="16" fill="{c}" stroke="none" opacity=".85"/><circle cx="14" cy="-10" r="7" fill="{c}" stroke="none" opacity=".8"/><circle cx="-14" cy="9" r="6" fill="{c}" stroke="none" opacity=".8"/>'
def swing(): return '<path d="M-40 -90 h80 M-30 -90 v60 M30 -90 v60" stroke="#6a4a2a" stroke-width="4"/><rect x="-36" y="-32" width="72" height="8" fill="#e0a800"/>'
def pillar(): return '<rect x="-14" y="-110" width="28" height="110" fill="#c9b8a0"/><path d="M-20 -110 h40 M-20 0 h40" stroke-width="4"/>'
def narasimha(): return '<path d="M-18 0 l4 -40 h28 l4 40z" fill="#e0a800"/><circle cy="-50" r="15" fill="#e0a800"/>'+''.join(f'<path d="M0 -50 l{14*__import__("math").cos(k*0.52):.1f} {14*__import__("math").sin(k*0.52):.1f}" stroke="#c0582a" stroke-width="5"/>' for k in range(12))+'<circle cy="-50" r="9" fill="#f2c79b"/><circle cx="-3" cy="-52" r="1.6" fill="#111"/><circle cx="3" cy="-52" r="1.6" fill="#111"/>'
def bowarrow_flower(): return '<path d="M-20 -30 q-10 30 0 60" fill="none" stroke="#c0392b" stroke-width="3"/><path d="M-20 -30 v60" stroke-width="1"/><path d="M-20 0 h40" stroke-width="2"/>'+g(24,0,.5,lotus())
def eye3(): return '<ellipse rx="14" ry="6" fill="#fff"/><circle r="4" fill="#c0392b"/>'
def jaggery(): return '<path d="M-12 0 l4 -16 h16 l4 16z" fill="#b5651d"/>'
def mango(): return '<path d="M0 0 q-14 -6 -10 -24 q8 -10 16 -2 q6 12 -6 26z" fill="#9ccc3c"/>'
def neem(): return '<path d="M0 0 v-40" stroke="#2f7a3a" stroke-width="2"/>'+''.join(f'<ellipse cx="{(-1)**k*9}" cy="-{6+k*5}" rx="7" ry="3" fill="#3a9a4a" transform="rotate({(-1)**k*30} {(-1)**k*9} -{6+k*5})"/>' for k in range(7))+'<circle cy="-44" r="3" fill="#fff"/><circle cx="4" cy="-42" r="2.5" fill="#fff"/>'
def sugarcane(): return '<path d="M0 0 v-80" stroke="#7a9a3a" stroke-width="7"/>'+''.join(f'<path d="M-4 -{k*16} h8" stroke="#4a6a2a" stroke-width="2"/>' for k in range(1,5))+'<path d="M0 -80 q-20 -10 -26 -30 M0 -80 q18 -14 22 -32" stroke="#3a9a4a" stroke-width="3" fill="none"/>'
def scroll(): return '<rect x="-30" y="-36" width="60" height="40" rx="3" fill="#fff8e7"/><path d="M-22 -26 h44 M-22 -18 h44 M-22 -10 h30" stroke="#888" stroke-width="2"/>'
def linga(): return '<path d="M-34 0 h68 l-8 -12 h-52z" fill="#8a8f9a"/><path d="M-30 -12 h60 q10 0 14 6 l-8 4" fill="#8a8f9a"/><path d="M-14 -12 v-38 q14 -16 28 0 v38z" fill="#3a3a40"/>'
def nandi(): return beast('bull','#f4f1ea')
