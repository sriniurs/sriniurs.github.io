import re, os, json
from lib import head as _head, LOGO, talk, cover
import fig as F
CFG=dict(theme='red',series='Navarātri and Dasarā',sign='Devī',art='#f6e3e1',fwbg='bg-red',signc='#8e1f17',short='Navarātri')
BASE='/festivals/navaratri/'
SITE='https://bhakti.srinipresents.com'
OUT='out/'
EXTRA={}
PARTS=[('overview','Navarātri: An Overview','Nine Nights and the Victorious Tenth'),
 ('the-story','The Story Behind It','The Devī and Mahiṣāsura'),
 ('starting-the-nine-nights','Starting the Nine Nights','Ghaṭasthāpana, the Kalaśa and the Lamp'),
 ('shailaputri','Śailaputrī','Night 1 · Daughter of the Mountain'),
 ('brahmacharini','Brahmacāriṇī','Night 2 · The Goddess of Penance'),
 ('chandraghanta','Candraghaṇṭā','Night 3 · The Moon-Bell'),
 ('kushmanda','Kūṣmāṇḍā','Night 4 · The Smile That Made the World'),
 ('skandamata','Skandamātā','Night 5 · Mother of Skanda'),
 ('katyayani','Kātyāyanī','Night 6 · The Sage’s Daughter Who Slew Mahiṣa'),
 ('kalaratri','Kālarātri','Night 7 · The Dark Night That Ends Fear'),
 ('mahagauri','Mahāgaurī','Night 8 · The Radiant White One'),
 ('siddhidatri','Siddhidātrī','Night 9 · Giver of Perfection'),
 ('gombe-habba','Gombe Habba','The Doll Steps of Karnataka'),
 ('sarasvati-puja-durgashtami','Sarasvatī Pūjā and Durgāṣṭamī','Books, Little Girls and the Junction Hour'),
 ('mahanavami-vijayadashami','Mahānavamī and Vijayadaśamī','Āyudha Pūjā, the Śamī Tree and the Day of Victory'),
 ('mysuru-dasara','The Mysuru Dasarā','Four Centuries of the Nāḍa Habba')]
N=len(PARTS)
def url(i): return BASE+(PARTS[i][0]+'/' if PARTS[i][0] else '')
def link(i,txt=None): return f'<a href="{url(i)}">{txt or "Part "+str(i+1)+", "+PARTS[i][1]}</a>'
SHARE='''<!-- reader-feedback:start -->
<div class="bhakti-reader-feedback" style="box-sizing:border-box;max-width:820px;margin:26px auto 32px;padding:22px 24px;border:1px solid #dec8aa;border-radius:12px;background:#fff8ed;color:#321f2a;font:16px/1.65 system-ui,-apple-system,'Segoe UI',sans-serif">
  <strong style="display:block;font:700 25px/1.25 Georgia,serif;margin-bottom:8px">Share your thoughts</strong>
  <p style="margin:0 0 13px">If an article touched your heart, or you have a suggestion, reflection or correction, I would love to hear from you.</p>
  <a href="mailto:srini.presents@gmail.com?subject=Bhakti%20reader%20feedback" style="display:inline-block;max-width:100%;overflow-wrap:anywhere;padding:10px 14px;border-radius:6px;background:#973f2c;color:white;text-decoration:none;font-weight:700">Write to me · srini.presents@gmail.com</a>
</div>
<!-- reader-feedback:end -->'''
def P(id,title,sub,body): return f'<section class="page" id="{id}">{LOGO}<h2 class="page-title">{title}</h2>'+(f'<div class="sub">{sub}</div>' if sub else '')+f'\n{body}\n</section>'
def paras(ps,cls='panel reading'): return f'<div class="{cls}">'+''.join(f'<p>{p}</p>' for p in ps)+'</div>'
def key(t): return f'<div class="key">{t}</div>'
def T(*pairs): return talk(*pairs)
def reading(id,title,sub,figsvg,ps,tk=None,k=None,extra=''):
    return P(id,title,sub,figsvg+paras(ps)+extra+(T(*tk) if tk else '')+(key(k) if k else ''))
def story(id,title,sub,stripsvg,lead,steps,tk=None,k=None):
    body=stripsvg+f'<div class="panel"><h3>The story</h3><p>{lead}</p><div class="steps">'+''.join(f'<div>{s}</div>' for s in steps)+'</div></div>'
    return P(id,title,sub,body+(T(*tk) if tk else '')+(key(k) if k else ''))
def cards(id,title,sub,figsvg,cs,tk=None,k=None,intro=''):
    body=figsvg+(f'<div class="panel reading"><p>{intro}</p></div>' if intro else '')+'<div class="g2">'+''.join(f'<div class="card"><h4>{e} {h}</h4><p>{t}</p></div>' for e,h,t in cs)+'</div>'
    return P(id,title,sub,body+(T(*tk) if tk else '')+(key(k) if k else ''))
def glance(rows,figsvg,tk=None,k=None):
    tb='<table class="ct fact">'+''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in rows)+'</table>'
    return P('glance','AT A GLANCE','The whole subject in one table',figsvg+tb+(T(*tk) if tk else '')+(key(k) if k else ''))
def verse(id,title,theme,lines,figsvg,meaning,words,insight,tk=None,k=None,note=''):
    iast='<div class="iast">'+''.join(f'<span class="cl">{l}</span>' for l in lines)+'</div>'
    wt='<table class="ct">'+'<tr><th>Word</th><th>Meaning</th></tr>'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in words)+'</table>'
    body=(f'<div class="sloka"><div class="sloka-head"><h3>{title}</h3><span class="theme">{theme}</span></div>{iast}'
          f'<div class="vfig">{figsvg}<div class="mean">{meaning}</div></div>{wt}<p>{insight}</p>'+(f'<div class="note">{note}</div>' if note else '')+'</div>')
    return P(id,'IN THE VERSE','',body+(T(*tk) if tk else '')+(key(k) if k else ''))
def end(i,lines,nexta,k):
    nq='What’s next?'
    body='<div class="steps">'+''.join(f'<div>{l}</div>' for l in lines)+'</div>'+T(('z',nq),('b',nexta))
    nxt=(' Next: '+link(i+1,'Part '+str(i+2)+': '+PARTS[i+1][1])) if i+1<N else ' Back to '+f'<a href="{BASE}">the series</a>'
    body+=key(f'Part {i+1}: {k}.{nxt}' if N>1 else f'{k}. Back to <a href="/festivals/">all festivals</a>.')
    return P('end','ON ONE PAGE','The whole article in five lines',body)
def sources(ps,unver,study):
    body=paras([f'<b>{a}</b> {b}' for a,b in ps]+[f'<b>Sources differ / unverified:</b> {unver}'],'panel reading small')
    body+=f'<p class="studynotes"><b>Study notes:</b> {study} Interpretations are marked as such. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</p>'
    return P('sources','SOURCES &amp; NOTES','Where the facts come from',body)
def foreword(i,ps,tk):
    prev=(f'Previous: {link(i-1)}. ' if i>0 else '')
    nxt=(f'Next: {link(i+1)}.' if i+1<N else f'This is the last part.')
    body=f'<div class="panel {CFG["fwbg"]} halftone" style="font-size:17px;line-height:1.6">'+''.join(f'<p>{p}</p>' for p in ps)
    body+='<p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:'+CFG['signc']+'">With the blessings of the '+CFG['sign']+',</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p></div>'
    body+=T(*tk)+(f'<div class="panel reading small"><p>Part {i+1} of <a href="{BASE}">{CFG["series"]}</a>, a {N}-part illustrated series. {prev}{nxt}</p></div>' if N>1 else '<div class="panel reading small"><p>One of our illustrated <a href="/festivals/">festival guides</a>.</p></div>')
    return P('foreword','WHERE WE ARE','',body)
def contents(items):
    li=''.join(f'<li><span class="num">{n+1}</span><a href="#{a}">{b}</a></li>' for n,(a,b) in enumerate(items))
    return P('contents','CONTENTS','',f'<ul class="toc">{li}</ul>')
def build(i,kicker,cov_svg,cap,how,desc,pages):
    slug,title,tag=PARTS[i]
    # contents from pages after contents
    items=[]
    for p in pages:
        m=re.search(r'<section class="page" id="([^"]+)">.*?<h2 class="page-title">(.*?)</h2>(?:<div class="sub">(.*?)</div>)?',p,re.S)
        if m:
            t=m.group(2)
            if t in ('IN THE VERSE',): t='The Verse: '+re.search(r'<h3>(.*?)</h3>',p).group(1)
            items.append((m.group(1),t.title().replace('’S','’s').replace("'S","'s").replace('&Amp;','&amp;')))
    hd=_head(f'{title}: {tag} · {CFG["short"]}, Part {i+1} · srini.presents' if N>1 else f'{title}: {tag} · srini.presents',desc,SITE+url(i),red=CFG['theme']=='red',theme=CFG['theme'])
    hd=hd.replace('<link rel="stylesheet" href="/assets/editorial/article-cover.css?v=2">','')
    cv=cover(kicker,title,f'{tag} · explained and illustrated',cov_svg,cap,how)
    ex=EXTRA.get(url(i),[])
    if ex: pages=pages[:-2]+ex+pages[-2:]
    fw,rest=pages[0],pages[1:]
    html=hd+'<div class="book">\n'+'\n\n'.join([cv,fw,contents(items)]+rest)+'\n</div>\n'+SHARE+'\n</body>\n</html>\n'
    d=OUT+slug if slug else OUT.rstrip('/')
    os.makedirs(d,exist_ok=True)
    open(d+'/index.html','w').write(html)
    # tile cover.svg
    inner=re.search(r'<svg class="coverart"[^>]*>(.*)</svg>',cov_svg,re.S).group(1)
    open(d+'/cover.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="380" height="268" viewBox="0 0 380 268"><rect width="380" height="268" fill="{CFG["art"]}"/><g transform="translate(0 24) scale(.8636)">{inner}</g></svg>')
    return html
def covart(label,inner): return f'<svg class="coverart" width="440" height="220" viewBox="0 0 440 220" role="img" aria-label="{label}"><rect width="440" height="220" rx="10" fill="{CFG["art"]}"/><rect y="196" width="440" height="24" fill="{"#e9c9c3" if CFG["theme"]=="red" else "#c9d6e6"}"/>{inner}</svg>'

def configure(base,parts,theme,series,sign,short):
    global BASE,PARTS,N
    BASE=base; PARTS[:]=parts; N=len(parts)
    CFG.update(theme=theme,series=series,sign=sign,short=short,
      art={'red':'#f6e3e1','navy':'#e3eaf3','blue':'#e3eaf3'}[theme],
      fwbg={'red':'bg-red','navy':'bg-blue','blue':'bg-blue'}[theme],
      signc={'red':'#8e1f17','navy':'#0b2a4a','blue':'#1d4f8a'}[theme])
