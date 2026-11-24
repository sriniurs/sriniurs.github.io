from fig2 import *
# Gaṇeśa and his things; base at y=0, ~100 tall, stroke inherited (#111 via g())
def ganesha(c='#e8703a',dhoti='#ffd60a',crown='#e0a800',seat=True,arms=4,lion=False):
    s=''
    if seat: s+='<path d="M-40 0 q40 -14 80 0 v6 h-80z" fill="#c0392b"/>'
    s+=f'<path d="M-30 -4 q30 16 60 0 l-4 -18 q-26 10 -52 0z" fill="{dhoti}"/>'  # legs
    s+=f'<ellipse cy="-34" rx="25" ry="24" fill="{c}"/>'                          # belly
    s+='<path d="M-14 -50 q14 6 28 0" fill="none" stroke="#e0a800" stroke-width="3"/>'  # sacred thread hint
    if arms>=4:
        s+=f'<path d="M-22 -48 q-18 -8 -22 -26" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/><path d="M22 -48 q18 -8 22 -26" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
        s+='<g transform="translate(-45 -78)"><path d="M0 12 V-10" stroke="#7a4a1a" stroke-width="3"/><path d="M0 -10 q10 -2 11 6 q-6 0 -11 3z" fill="#ccc"/></g>'   # axe
        s+='<path transform="translate(45 -80)" d="M0 8 q-9 -9 0 -16 q9 7 0 16" fill="none" stroke="#e0a800" stroke-width="3"/>'  # noose
    s+=f'<path d="M-22 -40 q-14 8 -10 22" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/><path d="M22 -40 q14 8 12 22" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
    s+='<path transform="translate(36 -16)" d="M-6 4 q-2 -10 6 -14 q8 4 6 14z" fill="#fff8e7"/>'  # modaka in hand
    s+=f'<ellipse cx="-22" cy="-74" rx="12" ry="15" fill="{c}"/><ellipse cx="22" cy="-74" rx="12" ry="15" fill="{c}"/>'  # ears
    s+=f'<circle cy="-74" r="16" fill="{c}"/>'
    s+='<path d="M-7 -62 q-3 5 -1 10" fill="none" stroke="#111" stroke-width="5" stroke-linecap="round"/><path d="M-7 -62 q-3 5 -1 10" fill="none" stroke="#fff8e7" stroke-width="2.5" stroke-linecap="round"/>'
    s+='<path d="M0 -66 q-2 14 6 20 q6 4 8 -3" fill="none" stroke="#111" stroke-width="11" stroke-linecap="round"/>'
    s+=f'<path d="M0 -66 q-2 14 6 20 q6 4 8 -3" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'  # trunk
    s+='<circle cx="-6" cy="-77" r="2" fill="#111" stroke="none"/><circle cx="6" cy="-77" r="2" fill="#111" stroke="none"/>'
    s+=f'<path d="M-11 -88 l3 -12 l5 6 l3 -8 l3 8 l5 -6 l3 12z" fill="{crown}"/>'
    s+='<path d="M-5 -84 q5 -5 10 0" fill="none" stroke="#fff8d0" stroke-width="2"/>'  # tilaka-moon hint
    return s
def mouse(c='#9a8a80'): return f'<ellipse cy="-8" rx="14" ry="8" fill="{c}"/><circle cx="12" cy="-12" r="6" fill="{c}"/><circle cx="12" cy="-18" r="3" fill="#f4a6b8"/><circle cx="15" cy="-13" r="1.2" fill="#111" stroke="none"/><path d="M-14 -8 q-12 -2 -16 8" fill="none"/>'
def modaka(c='#fff8e7'): return f'<path d="M-10 0 q-4 -14 10 -24 q14 10 10 24z" fill="{c}"/><path d="M-5 0 q-1 -10 5 -20 M5 0 q1 -10 -5 -20" fill="none"/>'
def laddu(c='#e0a800'): return f'<circle cy="-9" r="9" fill="{c}"/><circle cx="-3" cy="-11" r="1.2" fill="#7a4a1a" stroke="none"/><circle cx="3" cy="-6" r="1.2" fill="#7a4a1a" stroke="none"/>'
def durva(): return ''.join(f'<path d="M0 0 q{dx} -16 {dx*2} -30" fill="none" stroke="#2f8a3a" stroke-width="2.4"/>' for dx in (-6,-3,0,3,6))
def plate(): return '<ellipse cy="-2" rx="26" ry="7" fill="#c9a26b"/>'
def offerings(): return g(-30,0,1,modaka())+g(0,0,1,laddu())+g(28,0,1,durva())
def moonrise(x=0,y=0,r=22,c='#fff8d0'): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/><circle cx="{x+r*0.35}" cy="{y-r*0.1}" r="{r*0.9}" fill="#2a2a3a" opacity=".35" stroke="none"/>'
def sky(w=560,h=180,c='#20243a'): return f'<rect width="{w}" height="{h}" fill="{c}" stroke="none"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#fff" stroke="none"/>' for x,y in [(40,20),(120,44),(200,18),(330,30),(420,52),(500,22),(260,60),(80,80)])
def lion(c='#e0a800'): return f'<ellipse cy="-14" rx="24" ry="12" fill="{c}"/><circle cx="24" cy="-24" r="12" fill="#b8741a"/><circle cx="26" cy="-24" r="7" fill="{c}"/><path d="M-22 -14 q-12 -6 -14 -18" fill="none"/>'
def bird(c='#7a5a3a'): return f'<path d="M-24 -10 q24 -22 48 0 q-24 -8 -48 0z" fill="{c}"/><ellipse cy="-10" rx="10" ry="7" fill="{c}"/><circle cx="10" cy="-16" r="5" fill="#c9a26b"/><path d="M14 -16 l6 2 l-6 2z" fill="#e0a800"/>'
def hanuman(c='#c0582a'):  # Hanumān: vānara hero with mace, respectful figure
    return (f'<path d="M14 -6 q22 -8 16 -40 q-2 -6 -6 0 q4 26 -14 32" fill="{c}"/>'
            f'<path d="M-12 0 l3 -32 h18 l3 32z" fill="#ff8c1a"/><circle cy="-42" r="10" fill="{c}"/><ellipse cy="-38" rx="6" ry="4" fill="#f2c79b"/>'
            '<path d="M-7 -51 l7 -9 l7 9z" fill="#e0a800"/><g transform="translate(-20 -8)"><path d="M0 0 V-26" stroke="#7a4a1a" stroke-width="3"/><circle cy="-30" r="7" fill="#e0a800"/></g>')
def leaf(c='#2f7a3a'): return ''.join(f'<path transform="rotate({r})" d="M0 0 q-8 -12 0 -24 q8 12 0 24z" fill="{c}"/>' for r in (-40,0,40))
