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
def incense(): return '<path d="M-10 0 h20 l-3 -6 h-14z" fill="#7a4a1a"/><path d="M0 -6 V-40" stroke="#5a3a1a" stroke-width="2"/><circle cy="-41" r="2" fill="#e0501a" stroke="none"/><path d="M0 -44 q-8 -8 0 -16 q8 -8 0 -16" fill="none" stroke="#9a9aa8" stroke-width="2"/>'
def face(mark='vaishnava',skin='#c98a5a'):
    m={'vaishnava':'<path d="M-6 -42 v-12 M6 -42 v-12" stroke="#fff" stroke-width="3"/><path d="M0 -40 v-12" stroke="#c0392b" stroke-width="3"/>',
       'shaiva':'<path d="M-10 -50 h20 M-10 -46 h20 M-10 -42 h20" stroke="#fff" stroke-width="2.5"/><circle cy="-46" r="2.5" fill="#c0392b" stroke="none"/>',
       'bindi':'<circle cy="-46" r="4" fill="#c0392b"/>',
       'kumkum':'<path d="M0 -50 v10" stroke="#c0392b" stroke-width="4"/>'}[mark]
    return f'<path d="M-22 0 q0 -20 22 -22 q22 2 22 22z" fill="#1d6fb8"/><circle cy="-40" r="20" fill="{skin}"/><path d="M-20 -46 q20 -24 40 0 q-20 -12 -40 0z" fill="#2a1a10"/>'+m+'<circle cx="-7" cy="-36" r="2" fill="#111" stroke="none"/><circle cx="7" cy="-36" r="2" fill="#111" stroke="none"/><path d="M-5 -28 q5 4 10 0" fill="none"/>'
def arati(): return '<ellipse cy="-4" rx="24" ry="7" fill="#e0a800"/><path d="M-4 -8 h8 v-4 h-8z" fill="#fff"/><path d="M0 -12 q-8 -12 0 -26 q8 14 0 26z" fill="#ffb703" stroke="#e0501a" stroke-width="1.5"/><path d="M0 -4 V14" stroke="#7a4a1a" stroke-width="4"/>'
def coconut(): return '<ellipse cy="-14" rx="14" ry="13" fill="#7a4a1a"/><circle cx="-4" cy="-20" r="2" fill="#3a2a1a" stroke="none"/><circle cx="4" cy="-20" r="2" fill="#3a2a1a" stroke="none"/><circle cy="-14" r="2" fill="#3a2a1a" stroke="none"/>'
def banana(): return '<path d="M-16 -4 q16 12 32 -14 q-14 8 -32 6z" fill="#ffd60a"/>'
def namaste(c='#1d6fb8'): return f'<path d="M-14 0 l3 -34 h22 l3 34z" fill="{c}"/><circle cy="-44" r="10" fill="#c98a5a"/><path d="M0 -30 l-6 10 h12z" fill="#c98a5a"/>'
def shrine(): return '<path d="M-50 0 v-60 q50 -40 100 0 v60z" fill="#fff3cf"/><path d="M-50 -60 q50 -40 100 0" fill="none" stroke="#c0392b" stroke-width="4"/>'
def baby(): return '<ellipse cy="-10" rx="16" ry="10" fill="#fff8e7"/><circle cx="14" cy="-14" r="8" fill="#f2c79b"/><path d="M-12 -10 h18" stroke="#e0a800" stroke-width="2"/>'
def cradle(): return '<path d="M-36 -40 V0 M36 -40 V0" stroke="#7a4a1a" stroke-width="4"/><path d="M-36 -40 h72" stroke="#7a4a1a" stroke-width="3"/><path d="M-20 -40 v12 M20 -40 v12" stroke="#7a4a1a" stroke-width="2"/><path d="M-26 -28 q26 16 52 0z" fill="#e0a800"/>'+'<g transform="translate(0 -24) scale(.8)"><ellipse cy="-6" rx="14" ry="7" fill="#fff8e7"/><circle cx="12" cy="-8" r="6" fill="#f2c79b"/></g>'
def slate(t='a ā i'): return f'<rect x="-30" y="-40" width="60" height="40" rx="3" fill="#2a3a2a"/><text x="0" y="-15" font-size="13" text-anchor="middle" fill="#fff" stroke="none" font-family="serif">{t}</text>'
def agni(): return '<path d="M-26 0 h52 l-6 -12 h-40z" fill="#c0392b"/>'+'<g transform="translate(0 -12) scale(.6)"><path d="M-20 0 q-6 -30 10 -46 q-2 18 10 10 q4 -20 14 -30 q8 24 -2 66z" fill="#ff8c1a"/><path d="M-8 0 q-2 -16 8 -26 q6 14 4 26z" fill="#ffd60a"/></g>'
def steps7(): return ''.join(f'<ellipse cx="{-60+j*20}" cy="{-4-(j%2)*8}" rx="5" ry="8" fill="#c0392b" stroke-width="1"/>' for j in range(7))
def mother(c='#c0392b'): return f'<path d="M-14 0 l2 -30 q12 6 16 -2 l8 32z" fill="{c}"/><ellipse cx="6" cy="-16" rx="9" ry="10" fill="{c}"/><circle cy="-40" r="9" fill="#c98a5a"/><path d="M-8 -46 q8 -8 16 0" fill="#2a1a10"/>'
def ear(): return '<path d="M0 -30 q20 0 20 18 q0 14 -14 12 q-6 0 -6 6" fill="#c98a5a"/><circle cx="6" cy="-4" r="4" fill="#e0a800"/>'
def scissors(): return '<circle cx="-8" cy="-6" r="6" fill="none"/><circle cx="8" cy="-6" r="6" fill="none"/><path d="M-4 -10 L10 -36 M4 -10 L-10 -36" stroke-width="2.5"/>'
def thread(): return '<path d="M-14 -40 q20 22 26 40" fill="none" stroke="#fff8e7" stroke-width="5"/><path d="M-14 -40 q20 22 26 40" fill="none" stroke="#e0c060" stroke-width="2"/>'
