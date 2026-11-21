exec(open('/home/claude/work/shakti/mv_common.py').read())
def LOTUS(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.5">'+''.join(f'<path d="M0 0 q{dx} -26 {dx*2} 0z" fill="#f2a6c0" transform="rotate({r})"/>' for dx,r in ((-10,0),(10,0),(-8,-30),(8,30)))+'<path d="M-10 0 q10 -34 20 0z" fill="#e0115f"/></g>'
def ELE(x,y,s=1,flip=1): return (f'<g transform="translate({x} {y}) scale({s*flip} {s})" stroke="#111" stroke-width="2"><path d="M-30 20 q-4 -40 30 -44 q34 4 30 44z" fill="#d8d8e0"/><path d="M20 -10 q24 -10 30 -40 q2 -10 -4 -12" fill="none" stroke="#d8d8e0" stroke-width="9"/><path d="M20 -10 q24 -10 30 -40 q2 -10 -4 -12" fill="none" stroke="#111" stroke-width="1"/>'
 '<path d="M-20 20 v14 M20 20 v14" stroke="#d8d8e0" stroke-width="10"/><circle cx="10" cy="-12" r="2.4" fill="#111"/><path d="M-6 -20 q-14 0 -14 16 q10 4 16 -4z" fill="#c8c8d0"/>'
 '<path d="M44 -54 l-6 -10 h16z" fill="#e0a800"/></g>')
def KAM(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 +''.join(f'<path d="M0 54 q{dx} -30 {dx*2} 0z" fill="#f2a6c0"/>' for dx in (-34,-20,20,34))+'<ellipse cy="54" rx="56" ry="8" fill="#2a9d6f"/>'
 '<path d="M-30 50 q-4 -54 30 -66 q34 12 30 66z" fill="#e0115f"/><path d="M-26 20 q26 10 52 0" stroke="#e0a800" stroke-width="4" fill="none"/>'
 '<path d="M-22 -8 l-26 -20 M22 -8 l26 -20 M-22 6 l-24 6 M22 6 l24 6" stroke="#f2c070" stroke-width="7"/>'
 +LOTUS(-50,-28,.7)+LOTUS(50,-28,.7)+'<circle cx="46" cy="14" r="4" fill="#e0a800"/><circle cx="52" cy="18" r="4" fill="#e0a800"/>'
 '<circle cy="-36" r="15" fill="#f2c070"/><path d="M-14 -48 h28 l-4 -16 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/>'
 '<circle cx="-5" cy="-38" r="2.4" fill="#111"/><circle cx="5" cy="-38" r="2.4" fill="#111"/><path d="M-3 -46 h6" stroke="#c0392b" stroke-width="2"/><path d="M-6 -29 q6 5 12 0" fill="none"/></g>')
def GAJA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})">'+ELE(-96,-10,.9,1)+ELE(96,-10,.9,-1)+'<path d="M-50 -62 q20 10 34 34 M50 -62 q-20 10 -34 34" stroke="#5ab0f0" stroke-width="4" fill="none" stroke-dasharray="5 4"/>'+KAM(0,0,1)+'</g>'

import re as _re
ALS='/bhakti/devi/ashta-lakshmi/'
AL=[('adi','Ādi Lakṣmī','the primordial Lakṣmī'),('dhanya','Dhānya Lakṣmī','Lakṣmī of grain and harvest'),('dhairya','Dhairya Lakṣmī','Lakṣmī of courage'),('gaja','Gaja Lakṣmī','Lakṣmī with the elephants'),
    ('santana','Santāna Lakṣmī','Lakṣmī of children and family'),('vijaya','Vijaya Lakṣmī','Lakṣmī of victory'),('vidya','Vidyā Lakṣmī','Lakṣmī of knowledge'),('dhana','Dhana Lakṣmī','Lakṣmī of wealth')]
COL={'adi':'#e0115f','dhanya':'#2a9d6f','dhairya':'#c0392b','gaja':'#e0115f','santana':'#e0115f','vijaya':'#c0392b','vidya':'#f4f4f4','dhana':'#c0392b'}
def ATTR(k):
    return {'adi':'<path d="M44 -40 v40" stroke="#7a4a1a" stroke-width="3"/><path d="M44 -40 l14 5 -14 5" fill="#fff"/>',
     'dhanya':''.join(f'<path d="M{40+d} 10 q{d} -30 {d*2} -46" stroke="#c9a26b" stroke-width="3" fill="none"/>' for d in (-4,0,4))+'<path d="M-50 10 v-50" stroke="#2a9d6f" stroke-width="4"/>',
     'dhairya':'<path d="M40 -10 l20 -40" stroke="#bbb" stroke-width="4"/><circle cx="-50" cy="-30" r="9" fill="none" stroke="#e0a800" stroke-width="4"/>',
     'gaja':'',
     'santana':'<circle cx="0" cy="22" r="8" fill="#f2c79b"/><path d="M-8 34 q8 -8 16 0z" fill="#ffd60a"/>',
     'vijaya':'<circle cx="-50" cy="-30" r="9" fill="none" stroke="#e0a800" stroke-width="4"/><path d="M48 -38 q-6 10 4 14" fill="#fff8e7"/><path d="M40 0 l18 -40" stroke="#bbb" stroke-width="4"/>',
     'vidya':'<rect x="34" y="-30" width="26" height="18" fill="#fff3b0"/><path d="M47 -30 v18"/>',
     'dhana':'<path d="M38 0 q0 -20 14 -20 q14 0 14 20z" fill="#e0a800"/>'+''.join(f'<circle cx="{44+i*6}" cy="{8+i%2*4}" r="3.5" fill="#ffd60a"/>' for i in range(4))}[k]
def LAK(k,x,y,s=1):
    base=KAM(0,0,1)
    base=base.replace('fill="#e0115f"/><path d="M-26 20',f'fill="{COL[k]}"/><path d="M-26 20',1)
    if k=='gaja': return f'<g transform="translate({x} {y}) scale({s})">'+GAJA(0,0,.8)+'</g>'
    return f'<g transform="translate({x} {y}) scale({s})">'+base+f'<g stroke="#111" stroke-width="2">{ATTR(k)}</g></g>'
def series_note_al(i):
    prev=f' Previous: <a href="{ALS}{AL[i-1][0]}/">{AL[i-1][1]}</a>.' if i>0 else f' Previous: <a href="{ALS}overview/">Overview</a>.'
    nxt=f' Next: <a href="{ALS}{AL[i+1][0]}/">{AL[i+1][1]}</a>.' if i<len(AL)-1 else ''
    return f'<div class="panel reading small"><p>Part of <a href="{ALS}">Aṣṭa Lakṣmī</a>, the eight forms of Lakṣmī.{prev}{nxt}</p></div>'
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
def albuild(fname,title,desc,burst,h1,tag,cover,fw,say,tq,note,pages,EX,size=76):
    head=head_red(title,desc)
    pages=addx(pages,EX)
    toc=[(_re.search(r'id="([^"]+)"',p).group(1),_re.search(r'class="page-title">(.*?)<',p).group(1).title().replace('’S','’s')) for p in pages]
    ps=''.join(f'<p>{x}</p>' for x in fw)
    b=f"""<div class="book">
<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">{burst}</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,{size}px)">{h1}</h1>
  <div class="series">AṢṬA LAKṢMĪ · A REFERENCE GUIDE</div>
  <div class="tag">{tag}</div>
  {cover}
  {CAST}
</section>
<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">{ps}
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">{say}</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk(*tq)}
  {note}
</section>
<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">{''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}</ul>
</section>
"""+''.join(pages)+'</div>\n'
    open(f'/home/claude/work/shakti/{fname}.html','w').write(head+b+tail()); print('ok',len(pages))
def COVER(k,bg='#0e3a4a'):
    return (f'<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="{dict((a,b) for a,b,c in AL)[k]} seated on a lotus">'
     f'<rect width="380" height="268" fill="{bg}" rx="8"/><rect y="220" width="380" height="48" fill="#1d6f8a"/>'+''.join(LOTUS(30+i*64,236,.6) for i in range(6))+LAK(k,190,140,1.25)+'</svg>')
def endpage(i,lines,q,a):
    nx=f'<div class="key">Next: <a href="{ALS}{AL[i+1][0]}/">{AL[i+1][1]}</a></div>' if i is not None and i<len(AL)-1 else ('<div class="key">The eighth form: <b>Dhana Lakṣmī</b>. The series is complete. 🙏</div>' if i==7 else f'<div class="key">Begin: <a href="{ALS}adi/">Ādi Lakṣmī</a></div>')
    return page('end','ON ONE PAGE','In a few lines','<div class="steps">'+''.join(f'<div><b>{k}.</b> {v}</div>' for k,v in lines)+'</div>'+talk(q,a)+nx+FOLLOW)
def srcpage(txt,unv): return page('sources','SOURCES &amp; NOTES','Where the facts come from',f'<div class="panel reading small"><p><b>Sources:</b> {txt}</p><p><b>Sources differ / unverified:</b> {unv} The Aṣṭalakṣmī Stotram is a modern composition; we describe it but do not reproduce it. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p></div>')

def FORM(i,d):
    k,name,short=AL[i]
    pages=[P(*x) if isinstance(x,tuple) else x for x in d['pages']]
    pages.append(endpage(i,d['end'],*d['endq']))
    pages.append(srcpage(d['src'],d['unv']))
    albuild(f'AL{i+1}_{k.capitalize()}',f'{name} · Aṣṭa Lakṣmī {i+1} · srini.presents',d['desc'],f'AṢṬA LAKṢMĪ {i+1} OF 8',name.upper(),d['tag'],COVER(k),d['fw'],f'Jai {name},',d['fwq'],series_note_al(i),pages,d['EX'],size=d.get('size',70))
