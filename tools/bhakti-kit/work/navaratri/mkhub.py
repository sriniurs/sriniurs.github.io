import re,os,sys
R='/home/claude/srini-bhakti'
src=open(R+'/tulunadu/festivals/index.html').read()
head=src[:src.find('<header class="hero">')]
head=re.sub(r'<!-- (seo|sitenav|bhaktitrail):auto -->.*?<!-- /\1:auto -->','',head,flags=re.S)
def page(path,title,desc,h1,sub,nav,tiles,og='/tulunadu/og-share.jpg'):
    h=head.replace('/tulunadu/festivals/og-share.jpg',og)
    h=re.sub(r'<title>.*?</title>',f'<title>{title} · Bhakti | Srini Presents</title>',h,flags=re.S)
    h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',h)
    h=re.sub(r'<link rel="canonical" href="[^"]*">',f'<link rel="canonical" href="https://bhakti.srinipresents.com{path}">',h)
    h=re.sub(r'<meta property="og:(title|description|url)" content="[^"]*">','',h)
    body=f'<header class="hero">\n  <div class="hero-copy"><h1>{h1}</h1><p>{sub}</p></div>\n</header>\n{nav}\n<ul class="tiles tulu-cards" aria-label="{h1}">\n'+'\n'.join(tiles)+'\n</ul>\n</main>\n<footer>srini.presents</footer>\n<script data-goatcounter="https://sriniurs.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>\n</body>\n</html>\n'
    os.makedirs(R+path,exist_ok=True); open(R+path+'index.html','w').write(h+body)
def tile(href,img,h2,p,bg='#e3eaf3',label=''):
    return f'<li><a href="{href}"><div class="tile-art" style="background:{bg}"><img src="{img}" alt="" width="380" height="268" loading="lazy"></div><div class="tile-copy">'+(f'<strong class="label">{label}</strong>' if label else '')+f'<h2>{h2}</h2><p>{p}</p></div></a></li>'
sys.path.insert(0,'/home/claude/work/navaratri')
os.chdir('/home/claude/work/navaratri')
from kd_common import KD_PARTS
built=[(k,s,t,tag) for k,(s,t,tag) in enumerate(KD_PARTS) if os.path.exists(R+f'/kodagu/{s}/index.html')]
page('/karnataka-cultures/','Karnataka Cultures','The regional cultures of Karnataka: Tulu Nadu on the coast and Kodagu in the hills, their temples, festivals and traditions.','Karnataka Cultures','Regional traditions of Karnataka: the Tuḷu coast and the Kodagu hills.',
 '<nav class="tulu-nav" aria-label="Karnataka Cultures navigation"><a href="/">← Home</a> <a href="/tulunadu/">Tulu Nadu</a> <a href="/kodagu/">Kodagu</a></nav>',
 [tile('/tulunadu/','/tulunadu/art/tulunadu-intro.svg','Tulu Nadu','Temples, daiva and nāga traditions, Yakṣagāna, Kambaḷa and the festivals of coastal Karnataka.','#f3e3c3'),
  tile('/kodagu/','/kodagu/kodavas/cover.svg','Kodagu','The Kodavas of the hills: Puttari, Kailpoḷd, Kāverī Saṅkramaṇa, Igguthappa, the ainmane and more.')])
page('/kodagu/','Kodagu: Culture and Festivals','Kodagu (Coorg): the Kodavas, their festivals Puttari, Kailpoḷd and Kāverī Saṅkramaṇa, Igguthappa, the ainmane, dances, rites and temples. An illustrated series.','Kodagu','The Kodavas and Kodagu: festivals, gods, houses and traditions of the hills.',
 '<nav class="tulu-nav" aria-label="Kodagu navigation"><a href="/karnataka-cultures/">← Karnataka Cultures</a> <a href="/tulunadu/">Tulu Nadu</a></nav>',
 [tile(f'/kodagu/{s}/',f'/kodagu/{s}/cover.svg',t,tag,label=f'Part {k+1} of 12') for k,s,t,tag in built],og='/kodagu/og-share.jpg')
print('kodagu tiles',len(built))
