import json,re,sys
I=json.load(open('/home/claude/ill/all.json'))
CSS=open('/home/claude/ill/ill.css').read().strip()
def apply(path,mp):
    h=open(path).read()
    h=re.sub(r'<style id="comic-ills">.*?</style>\n?','',h,flags=re.S)
    h=re.sub(r'<svg class="ill[^"]*"[^>]*>.*?</svg>\n?','',h,flags=re.S)
    if '</style>' in h: h=h.replace('</style>','</style>\n'+CSS,1)
    n=0
    for i,(ep,k) in enumerate(mp.items()):
        pat=f'<div class="ep-head"><span class="no">{ep}</span>'
        j=h.find(pat); assert j>=0,(path,ep)
        e=h.find('</div>',j)+6
        svg=f'\n<svg class="ill{" r" if i%2 else ""}" viewBox="0 0 100 100" role="img" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">{I[k]}</svg>'
        h=h[:e]+svg+h[e:]; n+=1
    open(path,'w').write(h); print(path,n)
M={
'silk':{'EP 1':'crown','EP 3':'queue','EP 4':'soldout','EP 6':'stadium','EP 7':'silkworm','EP 8':'spool','EP 9':'loom','EP 10':'money'},
'gold-vs-silver':{'EP 2':'goldbars','EP 3':'silvercoins','EP 4':'gloves','EP 5':'rocket','EP 6':'cliff','EP 8':'scale','EP 10':'ship','EP 11':'diya'},
'scan-pay-repeat':{'EP 1':'cashnotes','EP 2':'phoneqr','EP 5':'bus','EP 7':'shield','EP 8':'globe','EP 9':'card','EP 11':'money','EP 13':'puzzle'},
'smog-machine':{'EP 1':'alarm','EP 2':'dust','EP 3':'potlid','EP 5':'farmfire','EP 6':'cracker','EP 7':'ladder','EP 8':'mask','EP 10':'raincloud'},
'trin-trin':{'EP 1':'bicycle','EP 3':'coaster','EP 5':'leakbucket','EP 7':'brokenbike','EP 8':'money','EP 10':'pothole','EP 11':'globe'},
'mysore-to-karnataka':{'EP 1':'scissormap','EP 2':'palace','EP 3':'mappin','EP 4':'crown','EP 6':'signboard','EP 7':'trophy','EP 12':'scroll','EP 14':'puzzle'},
}
import glob
for k,mp in M.items():
    if k=='silk':
        for p in ['/home/claude/silk_comic.html','/home/claude/silk_body.html']:
            if p.endswith('body.html'):
                # body has no style; only svgs
                h=open(p).read(); open(p,'w').write(h)
            apply(p,mp)
    else:
        apply(glob.glob(f'/home/claude/sriniurs.github.io/archive/*-{k}.html')[0],mp)
