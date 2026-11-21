exec(open('/home/claude/work/hanuman/hk.py').read())
def LAL(x,y,s=1):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
    g+='<path d="M-24 50 q-6 -56 24 -64 q30 8 24 64z" fill="#d1144a"/><path d="M-24 50 q24 -14 48 0" fill="none" stroke="#e0a800" stroke-width="3"/>'
    g+='<path d="M-20 -2 l-22 -20 M20 -2 l22 -20 M-18 10 l-26 4 M18 10 l26 4" stroke="#f2c79b" stroke-width="6"/>'
    g+='<path d="M-48 -28 q-10 -10 0 -18 q10 8 0 18" fill="none" stroke="#e0a800" stroke-width="3"/>'  # noose
    g+='<path d="M48 -24 v-20 l6 6" fill="none" stroke="#bbb" stroke-width="3"/>'  # goad
    g+='<path d="M-50 16 q-6 -16 0 -30" fill="none" stroke="#2a9d6f" stroke-width="4"/>'  # cane bow
    g+=''.join(f'<path d="M46 18 l{8+i*2} {-10-i*3}" stroke="#7a4a1a"/><circle cx="{54+i*2}" cy="{8-i*3}" r="3" fill="#f08aa6"/>' for i in range(3))
    g+='<circle cy="-24" r="14" fill="#f2c79b"/><path d="M-14 -30 q14 -14 28 0" fill="#111"/><path d="M-12 -38 h24 l-3 -14 l-5 6 l-4 -10 l-4 10 l-5 -6z" fill="#e0a800"/>'
    g+='<circle cx="-5" cy="-24" r="2" fill="#111"/><circle cx="5" cy="-24" r="2" fill="#111"/><circle cy="-31" r="2" fill="#c0392b"/><path d="M-4 -17 q4 3 8 0" fill="none" stroke="#c0392b"/>'
    g+='<path d="M8 -48 q6 -6 12 0" fill="none" stroke="#fff8e7" stroke-width="3"/>'  # crescent
    return g+'</g>'
def LS(label,cap=None,right=None,extra='',bg='#fde8ee'):
    fig=LAL(62,112,.78)
    r=ICON(right) if right else ''
    c=BUBBLE(112,22,cap,max(80,len(cap)*7.2),10) if cap else ''
    return sc(label,extra+fig+r+c,bg)
RECOL={'#e3f2fd':'#fde8ee','#3b8fd0':'#c0306a','#3b6fd0':'#a8285a','#8fd3ff':'#f7a8c4','#5b8fe0':'#d0507a','#0d3f73':'#5a0f2a','#1565c0':'#a8285a','#0b3d91':'#6a1030','#bbdefb':'#f9c9da','#90caf9':'#f3a3bf','#e8f1fb':'#fdf0f4','#dcecff':'#fde0ea','#2b6cb0':'#a8285a','#1d6fb8':'#b3215a','#1d4f9a':'#8a1a44','#2c5f9e':'#9a2050','#0b2a4a':'#4a0c22'}
def recolor(path):
    s=open(path).read()
    for a,b in RECOL.items(): s=s.replace(a,b).replace(a.upper(),b)
    open(path,'w').write(s)
