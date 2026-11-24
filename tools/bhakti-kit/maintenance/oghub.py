import re,os,glob,json,io,sys,html as H
sys.argv=['og.py','/home/claude/srini-bhakti','--x']
exec(open('/home/claude/work/og.py').read().split("files = [")[0])
REPO='/home/claude/srini-bhakti'
from playwright.sync_api import sync_playwright
from PIL import Image
todo=[]
for f in glob.glob(REPO+'/**/index.html',recursive=True):
    rel=os.path.relpath(os.path.dirname(f),REPO); 
    if rel.startswith(('tools','assets','search')): continue
    h=open(f).read()
    if 'class="book' in h or 'http-equiv="refresh"' in h: continue
    key='/' if rel=='.' else '/'+rel+'/'
    img=PAINT.get(key)
    if not img:  # first child article's painted image
        kids=[k for k in PAINT if k.startswith(key) and k!=key]
        links=re.findall(r'href="('+re.escape(key)+r'[^"#?]+/)"',h)
        for l in links:
            if l in PAINT: img=PAINT[l]; break
    m=re.search(r'property="og:image" content="([^"]*)"',h)
    cur=m.group(1) if m else ''
    good=cur and re.search(r'\.(jpg|jpeg|png|webp)$',cur) and os.path.exists(REPO+'/'+re.sub(r'^https://bhakti\.srinipresents\.com/','',cur))
    if img and not (good and key=='/'): todo.append((f,rel,key,img))
print(len(todo))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1200,'height':630})
    for f,rel,key,img in todo:
        h=open(f).read()
        t=re.search(r'<h1[^>]*>(.*?)</h1>',h,re.S); t=re.sub('<[^>]+>','',t.group(1)).strip() if t else re.sub(r'\s*\|.*','',re.search(r'<title>(.*?)</title>',h,re.S).group(1))
        open('/tmp/ogcard.html','w').write(pcard(REPO+img,'#15365a','Collection',t))
        pg.goto('file:///tmp/ogcard.html'); pg.wait_for_timeout(60)
        Image.open(io.BytesIO(pg.screenshot())).convert('RGB').save(os.path.dirname(f)+'/og-share.jpg',quality=86,optimize=True)
        open(f,'w').write(meta(h,rel if rel!='.' else '').replace('https://bhakti.srinipresents.com//','https://bhakti.srinipresents.com/'))
    b.close()
print('done')
