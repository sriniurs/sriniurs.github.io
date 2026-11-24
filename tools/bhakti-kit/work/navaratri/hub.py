import re,json
from pages import PARTS,BASE
from fig import *
k=open('/home/claude/srini-bhakti/temples-of-india/kerala/index.html').read()
T='Navarātri and Dasarā'; D='An illustrated 16-part guide to Navarātri: the story of the Devī and Mahiṣa, how the nine nights begin, the nine Durgās night by night, the Gombe Habba, Sarasvatī Pūjā, Āyudha Pūjā, Vijayadaśamī and the Mysuru Dasarā.'
s=k
s=re.sub(r'<title>.*?</title>',f'<title>{T} · Srini Presents</title>',s)
s=s.replace('An illustrated overview of Kerala temple architecture and ten guides to Kerala’s shrines, pilgrimages and living traditions.',D)
s=s.replace('https://bhakti.srinipresents.com/temples-of-india/kerala/','https://bhakti.srinipresents.com'+BASE)
s=s.replace('content="Temples of Kerala"',f'content="{T}"').replace('<h1>Temples of Kerala</h1>',f'<h1>{T}</h1>')
s=s.replace('/temples-of-india/kerala/banner.svg',BASE+'banner.svg').replace('alt="Kerala-style temple roofs, palms and a ceremonial boat"','alt="Nine lamps, the Devī on her lion and the golden howdah of Mysuru"')
s=s.replace('<a class="sr-reader-back" href="/temples-of-india/">','<a class="sr-reader-back" href="/festivals/">')
s=s.replace('<p class="bhakti-breadcrumb"><a href="/temples-of-india/">Temples and Tīrthas</a></p>','<p class="bhakti-breadcrumb"><a href="/festivals/">Festivals</a></p>')
s=s.replace('aria-label="Temples of Kerala articles"',f'aria-label="{T} articles"')
lab_={0:'Part 1 · Overview',1:'Part 2 · The story',2:'Part 3 · At home'}
tiles=''
for n,(slug,title,tag) in enumerate(PARTS):
    l=lab_.get(n) or (f'Part {n+1} · Night {n-2}' if 3<=n<=11 else f'Part {n+1} · {"Mysuru" if n==15 else "The great days"}')
    tiles+=f'<li><a href="{BASE}{slug}/"><div class="tile-art"><img src="{BASE}{slug}/cover.svg" width="380" height="268" alt="" loading="lazy"></div><div class="tile-copy"><strong class="label">{l}</strong><h2>{title}</h2><p>{tag}</p></div></a></li>\n'
s=re.sub(r'(<ol class="tiles"[^>]*>).*?(</ol>)',lambda m:m.group(1)+tiles+m.group(2),s,flags=re.S)
open('out/index.html','w').write(s)
# banner 1200x800
import math
rims=['#c0392b']*3+['#e0a800']*3+['#ffffff']*3
b='<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800"><rect width="1200" height="800" fill="#8e1f17"/><rect y="600" width="1200" height="200" fill="#5a120c"/>'
b+=''.join(g(240+k*90,220-int(80*math.sin(math.pi*k/8)),2.2,lamp(rims[k])) for k in range(9))
b+=g(430,600,3.2,beast('lion'))+g(430,500,2.6,devi(items=('trident','discus','sword','conch','lotus','abhaya')))+g(880,600,3,elephant())+g(860,385,1,devi(items=('trident','lotus')))
b+='</svg>'
open('out/banner.svg','w').write(b)
print('hub ok')
