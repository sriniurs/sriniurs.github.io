import re,sys,math
sys.path.insert(0,'/home/claude/work/purusha')
from pdata import talk,svg,person,F,SUN,lab,crowd,MOON,STARS,FIRE
SRC='/home/claude/work/Rameswaram_Jyotirlinga.html'
def make_head(title,desc,extra=''):
    h=open(SRC).read(); head=h[:h.find('<div class="book">')]
    css,rest=head[:head.find('</style>')],head[head.find('</style>'):]
    for a,b in [('#0b2a4a','#0d3f73'),('#1d4f9a','#1d6fb8'),('#09283f','#0d3f73'),('#04101f','#06203b'),('#2c5f9e','#3b82c4')]: css=css.replace(a,b)
    head=css+rest
    head=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',head,flags=re.S)
    head=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',head)
    return head.replace('</style>',extra+'</style>',1)
def tail():
    h=open(SRC).read(); return h[h.find('</div>\n<script data-goatcounter')+7:]
FOLLOW='<div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>'
CAST='''<div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>'''
def RANGA(x,y,s=1,hoods=7,skin='#3b6fd0',youth=False):
    hd=''.join(f'<circle cx="{-62+ (k-(hoods-1)/2)*7:.0f}" cy="{-30+abs(k-(hoods-1)/2)*4:.0f}" r="7" fill="#7aa86a"/>' for k in range(hoods))
    face='<circle cx="-46" cy="-6" r="1.6" fill="#111"/>' if youth else '<path d="M-50 -6 q3 2 6 0" stroke="#111" fill="none"/>'
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
      '<path d="M-74 14 q74 24 148 0 q-10 14 -74 16 q-64 -2 -74 -16z" fill="#7aa86a"/><path d="M-70 4 q70 18 140 0" fill="none" stroke="#5a8a4a" stroke-width="3"/>'
      +hd+f'<path d="M-50 2 q50 -20 104 -4" fill="none" stroke="{skin}" stroke-width="15"/><circle cx="-48" cy="-6" r="11" fill="{skin}"/>'+face+
      '<path d="M-58 -16 h20 l-3 -12 h-14z" fill="#ffd60a"/><path d="M-30 -10 h22" stroke="#ffd60a" stroke-width="4"/>'
      '<circle cx="58" cy="2" r="5" fill="#f2c79b"/></g>')
T=lambda x,y,t,s=12,c='#111',a='middle': f'<text x="{x}" y="{y}" text-anchor="{a}" {F} font-size="{s}" fill="{c}">{t}</text>'
def page(id_,title,sub,body):
    return f'<section class="page" id="{id_}"><h2 class="page-title">{title}</h2><div class="sub">{sub}</div>\n{body}\n</section>\n'
def fig(w,h,label,inner,bg='#fff'):
    return f'<svg class="pg-fig" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}"><rect width="{w}" height="{h}" fill="{bg}"/>{inner}</svg>'
def facts(rows): return '<table class="ct fact">'+''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in rows)+'</table>'
