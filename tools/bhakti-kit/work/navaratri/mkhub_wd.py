import re,os,sys
sys.path.insert(0,'/home/claude/work/navaratri'); os.chdir('/home/claude/work/navaratri')
from wd_common import WD_PARTS
R='/home/claude/srini-bhakti'
src=open(R+'/tulunadu/festivals/index.html').read()
head=src[:src.find('<header class="hero">')]
head=re.sub(r'<!-- (seo|sitenav|bhaktitrail|library:[a-z-]+):auto -->.*?<!-- /\1:auto -->','',head,flags=re.S)
head=head.replace('/tulunadu/festivals/og-share.jpg','/why-do-we/og-share.jpg')
head=re.sub(r'<title>.*?</title>','<title>Why Do We… · Bhakti | Srini Presents</title>',head,flags=re.S)
d='Why do we do ārati, wear tilaka, take prasāda, break a coconut, ring the bell, do pradakṣiṇā and namaskāra, worship tulasī, count 108 and fast? Ten illustrated explainers.'
head=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{d}">',head)
head=re.sub(r'<link rel="canonical" href="[^"]*">','<link rel="canonical" href="https://bhakti.srinipresents.com/why-do-we/">',head)
head=re.sub(r'<meta property="og:(title|description|url)" content="[^"]*">','',head)
tiles=''.join(f'<li><a href="/why-do-we/{s}/"><div class="tile-art" style="background:#e3eaf3"><img src="/why-do-we/{s}/cover.svg" alt="" width="380" height="268" loading="lazy"></div><div class="tile-copy"><strong class="label">Part {k+1} of 10</strong><h2>{t}</h2><p>{tag}</p></div></a></li>\n' for k,(s,t,tag) in enumerate(WD_PARTS))
body='<header class="hero">\n  <div class="hero-copy"><h1>Why Do We…</h1><p>The meaning behind everyday Hindu practices: ārati, tilaka, prasāda, the coconut, the bell, pradakṣiṇā, namaskāra, tulasī, 108 and fasting.</p></div>\n</header>\n<nav class="tulu-nav" aria-label="Why Do We navigation"><a href="/">← Home</a> <a href="/home-puja/">Home Pūjā</a> <a href="/festivals/">Festivals</a></nav>\n<ul class="tiles tulu-cards" aria-label="Why Do We">\n'+tiles+'</ul>\n</main>\n<footer>srini.presents</footer>\n<script data-goatcounter="https://sriniurs.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>\n</body>\n</html>\n'
os.makedirs(R+'/why-do-we',exist_ok=True); open(R+'/why-do-we/index.html','w').write(head+body)
