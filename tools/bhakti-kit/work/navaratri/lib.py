# Navarātri series library: head/CSS from the published Guruvāyūr page, recoloured to the Devī red theme.
import re
SRC='/home/claude/srini-bhakti/temples-of-india/kerala/guruvayur/index.html'
def head(title,desc,canon,red=True,theme=None):
    s=open(SRC).read()
    h=s[:s.find('<div class="book">')]
    for a,b in [(r'<!-- seo:auto -->.*?<!-- /seo:auto -->',''),(r'<!-- sitenav:auto -->.*?<!-- /sitenav:auto -->','')]:
        h=re.sub(a,b,h,flags=re.S)
    h=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',h,flags=re.S)
    h=re.sub(r'<link rel="canonical" href="[^"]*">',f'<link rel="canonical" href="{canon}">',h)
    h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',h)
    if theme=='blue':
        h=h.replace('data-bhakti-article="navy"','data-bhakti-article="light-blue"').replace('#15365a','#1d4f8a')
        return h
    if not red: return h
    h=h.replace('data-bhakti-article="navy"','data-bhakti-article="maroon"')
    h=h.replace('/* Śiva theme: navy */','/* Devī theme: red */')
    for a,b in [('#0b2a4a','#8e1f17'),('#1d4f9a','#c0392b'),('#dfe9f6','#fde4e4'),('#2c5f9e','#c0392b'),
                ('#04101f','#3a0a06'),('#5b6f8a','#8a5a4a'),('#15365a','#8e1f17')]:
        h=h.replace(a,b)
    h=h.replace('</head>','<style>.panel.bg-red-soft{background-color:#fde4e4}.cover2 .coverart{background:#f6e3e1}</style>\n</head>')
    return h
LOGO='<img class="pglogo" src="/assets/brand/logo-clear.png" alt="srini.presents" width="420" height="192">'
def say(who,text):
    if who=='z': return f'<div class="say z"><svg class="av" viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg><p class="bubble"><span class="who">ZAPPY:</span> {text}</p></div>'
    return f'<div class="say b"><svg class="av" viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg><p class="bubble"><span class="who">PROF. BOLT:</span> {text}</p></div>'
def talk(*pairs): return '<div class="talk">'+''.join(say(w,t) for w,t in pairs)+'</div>'
def cover(kicker,title,tag,svg,cap,how):
    return f'''<section class="page cover cover2">
  <div class="mast">
    <img class="brandtile" src="/assets/brand/logo-clear.png" alt="srini.presents" width="420" height="192">
    <p class="byline">Srini presents</p>
    <div class="kicker">{kicker}</div>
    <h1 style="font-size:clamp(44px,9vw,84px)">{title}</h1>
    <p class="tag">{tag}</p>
  </div>
  <div class="coverbody">
    {svg}
    <p class="cvcap">{cap}</p>
    <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
    </div>
    <div class="bubble"><b class="lead">HOW THIS WORKS:</b> {how}</div>
  </div>
</section>'''
def page(id,title,sub,body): return f'<section class="page" id="{id}">{LOGO}<h2 class="page-title">{title}</h2><div class="sub">{sub}</div>\n{body}\n</section>'
def doc(h,pages): return h+'<div class="book">\n'+'\n\n'.join(pages)+'\n</div>\n</body>\n</html>\n'
