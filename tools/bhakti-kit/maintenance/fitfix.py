import sys,asyncio,re,shutil,os
from playwright.async_api import async_playwright
R='/home/claude/srini-bhakti/'; LIM=965
def shrink(f,sid,mh):
    h=open(f).read(); s=h.find(f'id="{sid}"'); s=h.rfind('<section',0,s); e=h.find('</section>',s); sec=h[s:e]
    m=re.search(r'<svg(?![^>]*class="av")[^>]*>',sec)
    if not m: return False
    tag=m.group(0); tag2=re.sub(r' data-fit="1" style="[^"]*"','',tag)
    tag2=tag2.replace('<svg',f'<svg data-fit="1" style="max-height:{mh}px;width:auto;max-width:100%;display:block;margin:0 auto"',1)
    sec=sec.replace(tag,tag2,1); open(f,'w').write(h[:s]+sec+h[e:]); return True
async def main(ds):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        for d in ds:
            n='fit-'+d.replace('/','-'); dst=f'/home/claude/srv/test/{n}'
            mh={}
            for it in range(6):
                shutil.rmtree(dst,ignore_errors=True); shutil.copytree(R+d,dst)
                pg=await b.new_page(viewport={'width':794,'height':1123}); await pg.emulate_media(media='print')
                await pg.goto(f'http://localhost:8765/test/{n}/'); await pg.wait_for_timeout(400)
                r=await pg.evaluate("[...document.querySelectorAll('section.page')].map(s=>[s.id,s.scrollHeight])"); await pg.close()
                over=[(i,hh) for i,hh in r if hh>LIM and i]
                if not over: break
                for i,hh in over:
                    mh[i]=mh.get(i,230)-max(30,hh-LIM+10)
                    if mh[i]<80 or not shrink(R+d+'/index.html',i,mh[i]): print('CANNOT',d,i,hh)
            print(d,'over:',over)
        await b.close()
asyncio.run(main(sys.argv[1:]))
