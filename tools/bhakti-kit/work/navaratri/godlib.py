"""Deity guides for the Gods door: one detailed article per deity."""
import pages as PG
from pages import *
from pages import foreword,glance,reading,story,cards,end,sources,build,covart
from fx import *
from fig import devi
L=lambda u,t: f'<a href="{u}">{t}</a>'
def S(label,inner,bg='#fff3cf',h=190): return svg(560,h,label,f'<rect width="560" height="{h}" fill="{bg}"/>'+inner)
def row(label,figs,bg='#fff3cf',h=190,labels=None):
    n=len(figs); o=''
    for k,(f,s) in enumerate(figs):
        x=560*(k+.5)/n; o+=g(x,h-16,s,f)
        if labels: o+=lab(x,h-3,labels[k],11)
    return S(label,o,bg,h)
def kail(): return g(0,0,1,mountain('#9fb3c8',True))
def deity(base,slug,title,tag,theme,sign,d):
    PG.configure(base,[(slug,title,tag)],theme,'The Gods',sign,'The Gods')
    PG.CFG['backurl']='/gods/'; PG.CFG['backname']='guides to the gods'
    PG.OUT='outd/gods/'
    pp=[foreword(0,d['fw'],d['fwtk']),glance(d['glance'],d['gfig'],d.get('gtk'),d.get('gk'))]
    for p in d['pages']:
        k=p[0]
        if k=='r': pp.append(reading(*p[1:]))
        elif k=='s': pp.append(story(*p[1:]))
        elif k=='c': pp.append(cards(*p[1:]))
    pp.append(cards('glossary','WORDS TO KNOW','The vocabulary of this guide',d['wfig'],d['words'],d['wtk'],'Words <b>to keep</b>.'))
    pp.append(end(0,d['end'],d['endnext'],d['endk']))
    pp.append(sources(d['src'],d['unver'],d['study']))
    build(0,d['kicker'],d['cov'],d['cap'],d['how'],d['desc'],pp)
    print(slug,len(pp)+2)
