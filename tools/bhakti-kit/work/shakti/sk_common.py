exec(open('/home/claude/work/shakti/ps_common.py').read())
# Subrahmaṇya Ṣaṣṭhī series (Śiva family, navy theme)
SKS='/bhakti/shiva/subrahmanya-shashthi/'
SKP=[('skanda','Who is Skanda?'),('shashthi','The Ṣaṣṭhī Story'),('kukke','Kukke Subrahmaṇya'),('ghati','Ghāṭi Subrahmaṇya')]
FAM='/bhakti/shiva/shiva-family-and-symbols/'
def VEL(x,y,s=1,h=90):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M0 0 V-{h}" stroke="#7a5a2a" stroke-width="4"/>'
            f'<path d="M0 -{h} q11 -14 0 -34 q-11 20 0 34z" fill="#e0a800"/><circle cy="-{h}" r="3" fill="#c0392b"/></g>')
def SKHEAD(x,y,r,skin):
    return (f'<g transform="translate({x} {y})"><circle r="{r}" fill="{skin}"/><path d="M-{r*.8:.1f} -{r*.7:.1f} h{r*1.6:.1f} l-{r*.25:.1f} -{r*.9:.1f} l-{r*.35:.1f} {r*.4:.1f} l-{r*.2:.1f} -{r*.6:.1f} l-{r*.2:.1f} {r*.6:.1f} l-{r*.35:.1f} -{r*.4:.1f}z" fill="#e0a800"/>'
            f'<circle cx="-{r*.35:.1f}" cy="-{r*.1:.1f}" r="{r*.15:.1f}" fill="#111" stroke="none"/><circle cx="{r*.35:.1f}" cy="-{r*.1:.1f}" r="{r*.15:.1f}" fill="#111" stroke="none"/>'
            f'<path d="M-{r*.3:.1f} {r*.4:.1f} q{r*.3:.1f} {r*.25:.1f} {r*.6:.1f} 0" fill="none"/><path d="M0 -{r*.55:.1f} v{r*.3:.1f}" stroke="#c0392b" stroke-width="2"/></g>')
def SKANDA(x,y,s=1,six=True,skin='#e8a860',dress='#e0701a',vel=True):
    heads=(SKHEAD(-34,-20,8,skin)+SKHEAD(34,-20,8,skin)+SKHEAD(-19,-26,10,skin)+SKHEAD(19,-26,10,skin)+SKHEAD(0,-30,13,skin)) if six else SKHEAD(0,-30,13,skin)
    v=VEL(44,40,1,110) if vel else ''
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">{v}<path d="M-24 60 q-2 -64 24 -72 q26 8 24 72z" fill="{dress}"/>'
            f'<path d="M-24 22 h48" stroke="#e0a800" stroke-width="4"/><path d="M-20 0 l-20 -16 M20 0 l24 6" stroke="{skin}" stroke-width="6"/>'
            '<path d="M-44 -22 v-8 M-40 -22 v-9 M-36 -22 v-8" stroke="#e8a860" stroke-width="2.5"/>'
            f'<path d="M-10 -14 q10 8 20 0" fill="none" stroke="#e0a800" stroke-width="3"/>{heads}</g>')
def PEACOCK(x,y,s=1,flip=False):
    f=' scale(-1 1)' if flip else ''
    eyes=''.join(f'<circle cx="{-70*__import__("math").cos(a/10*3.1416):.0f}" cy="{-70*__import__("math").sin(a/10*3.1416)+0:.0f}" r="6" fill="#2a9d6f"/><circle cx="{-70*__import__("math").cos(a/10*3.1416):.0f}" cy="{-70*__import__("math").sin(a/10*3.1416):.0f}" r="2.6" fill="#1d3f9a" stroke="none"/>' for a in range(1,10))
    return (f'<g transform="translate({x} {y}) scale({s}){f}" stroke="#111" stroke-width="2"><path d="M-80 0 A80 80 0 0 1 80 0z" fill="#3a8a3a"/>{eyes}'
            '<path d="M-26 6 q0 -26 26 -26 q30 0 30 22 q-26 14 -56 4z" fill="#1d6fb8"/><path d="M22 -10 q10 -26 6 -44" fill="none" stroke="#1d6fb8" stroke-width="9"/>'
            '<circle cx="28" cy="-56" r="8" fill="#1d6fb8"/><path d="M34 -56 l10 3 l-10 3z" fill="#e0a800"/><circle cx="29" cy="-58" r="1.8" fill="#fff" stroke="none"/>'
            '<path d="M24 -64 l-4 -10 M28 -64 l0 -11 M32 -64 l4 -10" stroke-width="1.5"/><path d="M-6 6 v14 M8 6 v14" stroke="#e0a800" stroke-width="3"/></g>')
def ROOSTER(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-16 0 q-6 -20 10 -24 q4 -14 14 -10 q10 4 4 16 q10 6 4 18z" fill="#fff4e0"/>'
            '<path d="M-16 -2 q-14 -14 -8 -30 q6 12 12 14" fill="#2a9d6f"/><path d="M4 -36 q4 -8 8 -2 q4 -6 6 2z" fill="#c0392b"/><path d="M18 -26 l6 2 l-6 2z" fill="#e0a800"/>'
            '<circle cx="12" cy="-28" r="1.6" fill="#111"/><path d="M-2 0 v8 M6 0 v8" stroke="#e0a800" stroke-width="2.5"/></g>')
def FLAG(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M0 0 V-90" stroke="#7a5a2a" stroke-width="4"/><path d="M0 -90 h46 l-10 14 l10 14 h-46z" fill="#e0701a"/></g>'
            +ROOSTER(x+22*s,y-68*s,.55*s))
def NAGA(x,y,s=1,hoods=7,c='#4a7a3a',coil=True):
    import math
    hd=''
    for k in range(hoods):
        a=math.pi*(0.15+0.7*k/(max(hoods-1,1))); hx=-34*math.cos(a); hy=-60-26*math.sin(a)
        hd+=f'<path d="M0 -40 Q{hx*0.6:.0f} {hy+30:.0f} {hx:.0f} {hy:.0f}" fill="none" stroke="{c}" stroke-width="7"/>'
    for k in range(hoods):
        a=math.pi*(0.15+0.7*k/(max(hoods-1,1))); hx=-34*math.cos(a); hy=-60-26*math.sin(a)
        hd+=f'<ellipse cx="{hx:.0f}" cy="{hy:.0f}" rx="9" ry="11" fill="{c}"/><circle cx="{hx-3:.0f}" cy="{hy-2:.0f}" r="1.5" fill="#ffd60a" stroke="none"/><circle cx="{hx+3:.0f}" cy="{hy-2:.0f}" r="1.5" fill="#ffd60a" stroke="none"/>'
    cl=('<ellipse cx="0" cy="0" rx="44" ry="12" fill="'+c+'"/><ellipse cx="0" cy="-12" rx="34" ry="10" fill="'+c+'"/><ellipse cx="0" cy="-24" rx="24" ry="8" fill="'+c+'"/>') if coil else ''
    return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">{cl}<path d="M0 -28 q-6 -10 0 -16" fill="none" stroke="{c}" stroke-width="10"/>{hd}<path d="M-6 -46 q6 -6 12 0" fill="none" stroke="#e8e0b0" stroke-width="3"/></g>'
def ANTHILL(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-44 0 q4 -30 18 -40 q4 -20 14 -18 q8 -16 16 0 q12 4 12 20 q20 14 28 38z" fill="#b07a4a"/>'
            '<ellipse cx="2" cy="-30" rx="5" ry="4" fill="#3a2a1a"/><ellipse cx="-18" cy="-14" rx="4" ry="3" fill="#3a2a1a"/><ellipse cx="22" cy="-12" rx="4" ry="3" fill="#3a2a1a"/></g>')
def MANGOTREE(x,y,s=1,split=False):
    if split:
        return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-14 0 v-50 l-20 -40 l10 -4 l16 34z" fill="#7a4a1a"/><path d="M14 0 v-50 l20 -40 l-10 -4 l-16 34z" fill="#7a4a1a"/>'
                '<circle cx="-40" cy="-96" r="22" fill="#3a8a3a"/><circle cx="40" cy="-96" r="22" fill="#3a8a3a"/></g>')
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-10 0 v-60 h20 v60z" fill="#7a4a1a"/><circle cy="-90" r="40" fill="#3a8a3a"/>'
            '<path d="M-14 -96 q6 -2 8 6 q-6 6 -8 -6z M10 -80 q6 -2 8 6 q-6 6 -8 -6z" fill="#ffb03a"/></g>')
def KTEMPLE(x,y,s=1,wall='#f2e6c8',roof='#a0482a'):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-60" y="-40" width="120" height="40" fill="{wall}"/>'
            f'<path d="M-76 -40 L-40 -70 H40 L76 -40z" fill="{roof}"/><path d="M-50 -70 L-24 -94 H24 L50 -70z" fill="{roof}"/><path d="M0 -94 v-14" stroke="#e0a800" stroke-width="4"/><circle cy="-110" r="4" fill="#e0a800"/>'
            '<rect x="-12" y="-28" width="24" height="28" fill="#5a3a1a"/>'+''.join(f'<path d="M{a} -40 v40" stroke="#c9b48a"/>' for a in (-44,-28,28,44))+'</g>')
def RATHA(x,y,s=1,c='#c0392b'):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><circle cx="-26" cy="-8" r="12" fill="#7a4a1a"/><circle cx="26" cy="-8" r="12" fill="#7a4a1a"/><rect x="-40" y="-36" width="80" height="22" fill="#8a5a2a"/>'
            f'<path d="M-34 -36 L-24 -100 H24 L34 -36z" fill="{c}"/>'+''.join(f'<path d="M-26 {-46-k*14} h52" stroke="#ffd60a" stroke-width="3"/>' for k in range(4))+
            '<path d="M-24 -100 L0 -126 L24 -100z" fill="#e0a800"/><circle cy="-130" r="4" fill="#e0a800"/></g>')
def CROWD(x,y,n=8,dx=16):
    cs=['#c0392b','#1d6fb8','#2a9d6f','#e0a800','#7a3a8a','#e0701a']
    return ''.join(f'<g transform="translate({x+i*dx} {y})" stroke="#111" stroke-width="1.5"><path d="M-6 0 q0 -16 6 -18 q6 2 6 18z" fill="{cs[i%6]}"/><circle cy="-22" r="5" fill="#f2c79b"/></g>' for i in range(n))
def series_note(prev=None,nxt=None):
    p=f' Previous: <a href="{SKS}{prev[0]}/">{prev[1]}</a>.' if prev else ''
    n=f' Next: <a href="{SKS}{nxt[0]}/">{nxt[1]}</a>.' if nxt else ''
    return f'<div class="panel reading small"><p>Part of <a href="{SKS}">Subrahmaṇya Ṣaṣṭhī</a>, a four-part guide to Śiva’s son and his serpent shrines of Karnataka.{p}{n}</p></div>'
def cover(burst,h1,size,tag,art,series='SUBRAHMAṆYA ṢAṢṬHĪ · A REFERENCE GUIDE'):
    return f'''<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">{burst}</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp({size}px,{size*0.3:.1f}vw,{size*3}px)">{h1}</h1>
  <div class="series">{series}</div>
  <div class="tag">{tag}</div>
  {art}
  {CAST}
</section>'''
def foreword(title_say,paras,q,a,note):
    ps=''.join(f'<p>{x}</p>' for x in paras)
    return f'''<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">{ps}
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#0b2a4a">{title_say}</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk(q,a)}
  {note}
</section>'''
def story(id_,title,sub,w,h,label,inner,steps,after=''):
    st='<div class="steps">'+''.join(f'<div><b>{a}</b> {b}</div>' for a,b in steps)+'</div>'
    return page(id_,title,sub,fig(w,h,label,inner)+st+after)
