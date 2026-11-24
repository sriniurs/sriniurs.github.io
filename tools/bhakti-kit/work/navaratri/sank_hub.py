import re
k=open('/home/claude/srini-bhakti/temples-of-india/kerala/index.html').read()
def hub(base,out,T,D,parts,labels,bg,back='/festivals/',backname='Festivals'):
    s=k
    s=re.sub(r'<title>.*?</title>',f'<title>{T} · Srini Presents</title>',s)
    s=s.replace('An illustrated overview of Kerala temple architecture and ten guides to Kerala’s shrines, pilgrimages and living traditions.',D)
    s=s.replace('https://bhakti.srinipresents.com/temples-of-india/kerala/','https://bhakti.srinipresents.com'+base)
    s=s.replace('content="Temples of Kerala"',f'content="{T}"').replace('<h1>Temples of Kerala</h1>',f'<h1>{T}</h1>')
    s=s.replace('/temples-of-india/kerala/banner.svg',base+'banner.svg').replace('alt="Kerala-style temple roofs, palms and a ceremonial boat"',f'alt="{T}"')
    s=s.replace('<a class="sr-reader-back" href="/temples-of-india/">',f'<a class="sr-reader-back" href="{back}">')
    s=re.sub(r'<p class="bhakti-breadcrumb">.*?</p>',lambda m:f'<p class="bhakti-breadcrumb"><a href="{back}">{backname}</a></p>',s,count=1,flags=re.S)
    s=s.replace('aria-label="Temples of Kerala articles"',f'aria-label="{T} articles"')
    tiles=''.join(f'<li><a href="{base}{slug}/"><div class="tile-art"><img src="{base}{slug}/cover.svg" width="380" height="268" alt="" loading="lazy"></div><div class="tile-copy"><strong class="label">{labels[n]}</strong><h2>{title}</h2><p>{tag}</p></div></a></li>\n' for n,(slug,title,tag) in enumerate(parts))
    s=re.sub(r'(<ol class="tiles"[^>]*>).*?(</ol>)',lambda m:m.group(1)+tiles+m.group(2),s,flags=re.S)
    open(out+'index.html','w').write(s)
    inner=re.search(r'<svg[^>]*>(.*)</svg>',open(out+parts[0][0]+'/cover.svg').read(),re.S).group(1)
    open(out+'banner.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800"><rect width="1200" height="800" fill="{bg}"/><g transform="translate(90 40) scale(2.7)">{inner}</g></svg>')

import sank
P=sank.PARTS_
labels=['Part 1 · Overview','Part 2 · Practice','Part 3 · The moon','Part 4 · Tuesday']+[f'Part {n+5} · {d["mon"]}' for n,d in enumerate(sank.SK)]
hub(sank.BASE,'outs/sankashti-chaturthi/','Saṅkaṣṭī Caturthī','An illustrated 17-part guide to Saṅkaṣṭī Caturthī, Gaṇeśa’s monthly fast to moonrise: what it is, how it is kept, the moon and Aṅgārakī, and each of the thirteen monthly Saṅkaṣṭīs with its form, seat and story.',P,labels,'#f6e3e1',back='/ganesha/festivals/',backname='Gaṇeśa festivals')
print('hub ok')
