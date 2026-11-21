exec(open('/home/claude/work/shakti/ps_common.py').read())
import re as _re
PKS='/bhakti/temples-of-india/pancha-kedar/'
JYK='/bhakti/temples-of-india/12-jyotirlingas/kedarnath/'
PK=[('kedarnath','Kedārnāth','the hump'),('tungnath','Tuṅganāth','the arms'),('rudranath','Rudranāth','the face'),('madhyamaheshwar','Madhyamaheśvar','the navel'),('kalpeshwar','Kalpeśvar','the matted hair')]
def PEAKS(W=560,H=160,snow=True):
    return (f'<rect width="{W}" height="{H}" fill="#cfe3f6"/>'+''.join(f'<path d="M{x-w} {H} L{x} {H-h} L{x+w} {H}z" fill="#8aa0b8" stroke="#111" stroke-width="2"/>'+(f'<path d="M{x-w*0.25} {H-h*0.75} L{x} {H-h} L{x+w*0.25} {H-h*0.75} l-{w*0.12} 8 l-{w*0.13} -6 l-{w*0.13} 6z" fill="#fff" stroke="#111" stroke-width="1.5"/>' if snow else '') for x,w,h in ((W*0.15,W*0.2,H*0.8),(W*0.45,W*0.25,H*0.95),(W*0.8,W*0.22,H*0.75))))
def STONE(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-30" y="-40" width="60" height="40" fill="#9a9a90"/><path d="M-30 -40 L0 -80 L30 -40z" fill="#8a8a80"/>'
     '<path d="M-6 0 v-22 h12 v22" fill="#3a3a3a"/><path d="M0 -80 v-12" /><path d="M0 -92 l10 4 -10 4" fill="#ff8c1a"/>'+''.join(f'<path d="M-30 {-40+i*10} h60" stroke="#7a7a70" stroke-width="1"/>' for i in range(1,4))+'</g>')
def BULL(x,y,s=1,part=None):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><ellipse rx="40" ry="18" fill="#eee"/><path d="M-6 -16 q8 -16 18 0" fill="#ddd"/><circle cx="-44" cy="-8" r="12" fill="#eee"/><path d="M-50 -18 l-6 -10 M-40 -20 l2 -10" /><path d="M-30 16 v16 M30 16 v16 M-14 16 v16 M14 16 v16" stroke-width="5"/>'
    if part=='hump': g+='<path d="M-6 -16 q8 -16 18 0" fill="#ffd60a"/>'
    return g+'</g>'
def series_note_pk(i):
    prev=f' Previous: <a href="{PKS}{PK[i-1][0]}/">{PK[i-1][1]}</a>.' if i>0 else f' Previous: <a href="{PKS}overview/">Overview</a>.'
    nxt=f' Next: <a href="{PKS}{PK[i+1][0]}/">{PK[i+1][1]}</a>.' if i<len(PK)-1 else ''
    return f'<div class="panel reading small"><p>Part of <a href="{PKS}">Pañca Kedār</a>, Śiva’s five Himalayan shrines.{prev}{nxt}</p></div>'
def P(pid,title,sub,rows,t=None,extra='',figure=''):
    return page(pid,title,sub,figure+facts(rows)+(talk(*t) if t else '')+extra)
def addx(pages,EX):
    out=[]
    for p in pages:
        m=_re.search(r'id="([^"]+)"',p); k=m.group(1) if m else ''
        if k in EX:
            i=p.rfind('</section>'); p=p[:i]+'<div class="panel reading">'+''.join(f'<p>{x}</p>' for x in EX[k])+'</div>'+p[i:]
        out.append(p)
    return out
def endpage(i,lines,q,a):
    nx=(f'<div class="key">Next: <a href="{PKS}{PK[i+1][0]}/">{PK[i+1][1]}</a></div>' if i is not None and i<4 else ('<div class="key">The fifth Kedār: <b>Kalpeśvar</b>. The series is complete. 🙏</div>' if i==4 else f'<div class="key">Begin: <a href="{PKS}kedarnath/">Kedārnāth</a></div>'))
    return page('end','ON ONE PAGE','In a few lines','<div class="steps">'+''.join(f'<div><b>{k}.</b> {v}</div>' for k,v in lines)+'</div>'+talk(q,a)+nx+FOLLOW)
def srcpage(txt,unv): return page('sources','SOURCES &amp; NOTES','Where the facts come from',f'<div class="panel reading small"><p><b>Sources:</b> {txt}</p><p><b>Sources differ / unverified:</b> {unv} Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p></div>')
def pkbuild(fname,title,desc,burst,h1,size,tag,art,fw,fwq,note,pages,EX):
    head=head_navy(title,desc)
    cov=cover(burst,h1,size,tag,art).replace('PAÑCABHŪTA STHALAS · A REFERENCE GUIDE','PAÑCA KEDĀR · A REFERENCE GUIDE')
    fwd=foreword('Har Har Mahādev,',fw,*fwq,note)
    pages=addx(pages,EX)
    toc=[(_re.search(r'id="([^"]+)"',p).group(1),_re.search(r'class="page-title">(.*?)<',p).group(1).title().replace('’S','’s')) for p in pages]
    build(f'/home/claude/work/shakti/{fname}.html',head,cov,fwd,pages,toc)
def ART(label,extra=''): return f'<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="{label}"><rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+STAR+f'<g transform="translate(0 108)">{PEAKS(380,160)}</g>'+extra+'</svg>'
