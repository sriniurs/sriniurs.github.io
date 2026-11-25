def LINGA(x,y,s=1,blood=False):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-46 0 h92 l-8 -14 h-76z" fill="#8a8a8a"/><path d="M34 -7 h26 l-4 6 h-22z" fill="#8a8a8a"/>'
     '<path d="M-18 -14 v-38 a18 18 0 0 1 36 0 v38z" fill="#3a3a3a"/><path d="M-12 -46 h24 M-12 -40 h24 M-12 -34 h24" stroke="#fff" stroke-width="2.4"/>'
     '<circle cx="0" cy="-30" r="3" fill="#c0392b" stroke="none"/>'+('<path d="M6 -22 q4 6 2 12" stroke="#c0392b" stroke-width="4" fill="none"/>' if blood else '')+'</g>')

def SHIVA(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
     '<path d="M-30 60 q30 -70 60 0z" fill="#ffb3c7"/><circle r="22" cy="-6" fill="#8fd0f5"/>'
     '<path d="M-14 -28 q14 -22 28 0 q-6 -6 -14 -4 q-8 -2 -14 4z" fill="#5a3a1a"/><path d="M-6 -36 q6 -6 12 0" fill="none" stroke="#fff" stroke-width="3"/>'
     '<path d="M-10 -4 q4 3 8 0 M2 -4 q4 3 8 0" fill="none"/><path d="M-6 8 q6 4 12 0" fill="none"/>'
     '<path d="M-12 18 q12 8 24 0" stroke="#1d4f9a" stroke-width="7" fill="none"/></g>')

GOP=lambda x,y,s=1,t=7: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-34+k*3} {-k*12} h{68-k*6} l-1 -12 h{-(66-k*6)}z" fill="{"#f2e6c8" if k%2 else "#e2cfa8"}"/>' for k in range(t))+''.join(f'<path d="M{-14+j*7} {-t*12} l2 -10 l2 10z" fill="#e0a800"/>' for j in range(5))+'<rect x="-9" y="-20" width="18" height="20" fill="#5a3a1a"/></g>'

def RATHA(x,y,s=1,c='#c0392b'):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cx="-18" cy="-6" r="8" fill="#7a5a2a"/><circle cx="18" cy="-6" r="8" fill="#7a5a2a"/>'
     '<rect x="-26" y="-30" width="52" height="18" fill="#a0522d"/><path d="M-22 -30 v-24 M22 -30 v-24" stroke-width="3"/>'
     f'<path d="M-30 -54 h60 l-30 -46z" fill="{c}"/><path d="M-26 -54 q26 10 52 0" fill="none" stroke="#ffd60a" stroke-width="3"/><circle cy="-102" r="4" fill="#e0a800"/></g>')
