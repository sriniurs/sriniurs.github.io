exec(open('/home/claude/work/shakti/dv_common.py').read())
HNS='/bhakti/vishnu/hanuman/'
HN=[('who','Who Hanumān Is','his names, forms and why he is loved'),
    ('birth','Birth and Boyhood','Añjanā, the Wind and the leap at the sun'),
    ('kishkindha','Kiṣkindhā','Sugrīva, the meeting with Rāma and the search'),
    ('sundara','The Leap to Laṅkā','the Sundara Kāṇḍa: Sītā found, Laṅkā burned'),
    ('yuddha','The War and After','the mountain of herbs, the return and the deathless servant'),
    ('temples','Hanumān’s Temples','great shrines across India')]
def HANUMAN(x,y,s=1,mace=True,fold=False):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
    g+='<path d="M24 40 q40 -6 34 -50 q-2 -14 8 -20" fill="none" stroke="#e08a2a" stroke-width="7"/><path d="M24 40 q40 -6 34 -50 q-2 -14 8 -20" fill="none" stroke="#111" stroke-width="1"/>'
    g+='<path d="M-26 52 q-4 -56 26 -64 q30 8 26 64z" fill="#e0701a"/><path d="M-14 52 v-20 h28 v20" fill="#c0392b"/>'
    g+='<circle cy="-28" r="17" fill="#e08a2a"/><ellipse cy="-20" rx="11" ry="9" fill="#f2c79b"/><path d="M-6 -14 q6 4 12 0" fill="none"/>'
    g+='<circle cx="-5" cy="-30" r="2.4" fill="#111"/><circle cx="5" cy="-30" r="2.4" fill="#111"/><path d="M-12 -46 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800"/><path d="M0 -42 v6" stroke="#c0392b" stroke-width="3"/>'
    if fold: g+='<path d="M-8 4 l8 -16 l8 16z" fill="#f2c79b"/>'
    if mace: g+='<path d="M34 34 l14 -54" stroke="#7a4a1a" stroke-width="5"/><circle cx="50" cy="-28" r="12" fill="#e0a800"/><path d="M40 -28 h20 M50 -38 v20" stroke="#b07a00"/>'
    return g+'</g>'
def MOUNTAIN(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 10 l14 -30 l10 12 l12 -24 l24 42z" fill="#6a9a4a"/><circle cx="-6" cy="-6" r="3" fill="#ffd60a"/><circle cx="8" cy="0" r="3" fill="#ffd60a"/><circle cx="-16" cy="4" r="3" fill="#ffd60a"/></g>'
def SUN(x,y,r=26): return f'<g transform="translate({x} {y})" stroke="#111" stroke-width="2">'+''.join(f'<path d="M0 0 L{r*1.6*__import__("math").cos(k*0.523):.1f} {r*1.6*__import__("math").sin(k*0.523):.1f}" stroke="#ff9f1c" stroke-width="4"/>' for k in range(12))+f'<circle r="{r}" fill="#ffd60a"/></g>'
def series_note_hn(i):
    prev=f' Previous: <a href="{HNS}{HN[i-1][0]}/">{HN[i-1][1]}</a>.' if i>0 else ''
    nxt=f' Next: <a href="{HNS}{HN[i+1][0]}/">{HN[i+1][1]}</a>.' if i<len(HN)-1 else ''
    return f'<div class="panel reading small"><p>Part {i+1} of {len(HN)} in <a href="{HNS}">Hanumān</a>, the illustrated guide to Rāma’s great devotee.{prev}{nxt}</p></div>'
def cover_hn(burst,h1,size,tag,art):
    return cover(burst,h1,size,tag,art).replace('PAÑCABHŪTA STHALAS · A REFERENCE GUIDE','HANUMĀN · A REFERENCE GUIDE')
import re as _re
def P(pid,title,sub,rows,t=None,extra='',figure=''):
    body=figure+facts(rows)+(talk(*t) if t else '')+extra
    return page(pid,title,sub,body)
def addx(pages,EX):
    out=[]
    for p in pages:
        m=_re.search(r'id="([^"]+)"',p); k=m.group(1) if m else ''
        if k in EX:
            i=p.rfind('</section>'); p=p[:i]+'<div class="panel reading">'+''.join(f'<p>{x}</p>' for x in EX[k])+'</div>'+p[i:]
        out.append(p)
    return out
def nxt(i): return f'<div class="key">Next: <a href="{HNS}{HN[i+1][0]}/">{HN[i+1][1]}</a></div>' if i<len(HN)-1 else ''
def endpage(i,lines,q,a): return page('end','ON ONE PAGE','The part in a few lines','<div class="steps">'+''.join(f'<div><b>{k}.</b> {v}</div>' for k,v in lines)+'</div>'+talk(q,a)+nxt(i)+FOLLOW)
def srcpage(txt,unv): return page('sources','SOURCES &amp; NOTES','Where the facts come from',f'<div class="panel reading small"><p><b>Texts:</b> {txt}</p><p><b>Sources differ / unverified:</b> {unv} Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p></div>')
def hbuild(i,fname,desc,burst,h1,size,tag,art,fw_paras,fwq,fwa,pages,EX):
    head=head_vis(f'{HN[i][1]} · Hanumān {i+1} · srini.presents',desc)
    cov=cover_hn(burst,h1,size,tag,art)
    fw=foreword_dv('Jai Hanumān,',fw_paras,fwq,fwa,series_note_hn(i))
    pages=addx(pages,EX)
    toc=[(_re.search(r'id="([^"]+)"',p).group(1),_re.search(r'class="page-title">(.*?)<',p).group(1).title()) for p in pages]
    build(f'/home/claude/work/shakti/{fname}.html',head,cov,fw,pages,toc)

def RAMA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 50 q-4 -60 30 -70 q34 10 30 70z" fill="#ffd60a"/>'
 '<path d="M-22 -6 l-22 26 M22 -6 l26 -8" stroke="#3b6fd0" stroke-width="8"/><path d="M-50 -60 q-26 60 0 120" fill="none" stroke="#7a4a1a" stroke-width="5"/><path d="M-50 -60 v120" stroke="#ccc" stroke-width="1.5"/><path d="M40 -20 l20 -40" stroke="#7a4a1a" stroke-width="3"/>'
 '<circle cy="-36" r="15" fill="#3b6fd0"/><path d="M-12 -48 h24 l-4 -16 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/><circle cx="-5" cy="-38" r="2.4" fill="#fff"/><circle cx="5" cy="-38" r="2.4" fill="#fff"/><path d="M-6 -29 q6 4 12 0" fill="none"/><path d="M-3 -46 v-5 M3 -46 v-5" stroke="#fff" stroke-width="1.5"/></g>')

def MONKEY(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-20 40 q-2 -44 20 -50 q22 6 20 50z" fill="#e08a2a"/><path d="M20 30 q30 -10 26 -50" fill="none" stroke="#e08a2a" stroke-width="6"/>'
 '<circle cy="-20" r="14" fill="#e08a2a"/><ellipse cy="-14" rx="9" ry="7" fill="#f2c79b"/><circle cx="-4" cy="-22" r="2" fill="#111"/><circle cx="4" cy="-22" r="2" fill="#111"/><path d="M-30 0 v-30" stroke="#7a4a1a" stroke-width="5"/><circle cx="-30" cy="-36" r="9" fill="#e0a800"/></g>')
