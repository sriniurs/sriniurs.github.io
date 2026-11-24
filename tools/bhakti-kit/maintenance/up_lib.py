import re,shutil,os
R='/home/claude/sriniurs.github.io'; W='/home/claude/work'
def cp(src,dst):
    os.makedirs(f'{R}/{dst}',exist_ok=True); shutil.copy(f'{W}/{src}',f'{R}/{dst}/index.html')

T=open(f'{R}/bhakti/temples-of-india/12-jyotirlingas/index.html').read()
T=re.sub(r'<!-- seo:auto -->.*?<!-- /seo:auto -->\n?','',T,flags=re.S)
T=re.sub(r'<!-- sitenav:auto -->.*?<!-- /sitenav:auto -->\n?','',T,flags=re.S)
HEAD=T[:T.find('<main>')]
def tile(href,bg,svg,label,h2,p,read='Read ↗'):
    return f'<li><a href="{href}"><div class="tile-art" style="background:{bg}"><svg class="ill" viewBox="0 0 100 100" aria-hidden="true"><g stroke="#151515" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{svg}</g></svg></div><div class="tile-copy"><strong class="label">{label}</strong><h2>{h2}</h2><p>{p}</p><span class="read">{read}</span></div></a></li>'
def index(path,title,desc,backurl,backname,heroc,h1c,bodyc,banner,intro,tiles,extra=''):
    h=HEAD
    h=re.sub(r'<title>.*?</title>',f'<title>{title} · srini.presents</title>',h)
    h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',h)
    h=re.sub(r'<link rel="canonical" href="[^"]*">',f'<link rel="canonical" href="https://srinipresents.com/{path}/">',h)
    h=h.replace('.hero{background:#0b2a4a}.hero h1{color:#ffd23f}.hero p{color:#fff}body{background:#eef3fa}',f'.hero{{background:{heroc}}}.hero h1{{color:{h1c}}}.hero p{{color:#fff}}body{{background:{bodyc}}}')
    h=re.sub(r'<a href="/bhakti/temples-of-india/">← Temples of India</a>',f'<a href="{backurl}">← {backname}</a>',h)
    html=h+f'''<main>
  <header class="hero">
    <div class="hero-copy"><h1>{title}</h1><p>{intro}</p></div>
    <img src="{banner}" alt="" width="1200" height="800" fetchpriority="high">
  </header>
  <ol class="tiles">
    {"".join(tiles)}
  </ol>{extra}
</main>
<footer>srini.presents</footer>
<script data-goatcounter="https://sriniurs.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body></html>
'''
    os.makedirs(f'{R}/{path}',exist_ok=True); open(f'{R}/{path}/index.html','w').write(html)
