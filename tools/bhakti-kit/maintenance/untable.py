"""Turn 'ct fact' tables outside At a Glance into reading text (bold label + value)."""
import re,glob,sys
R='/home/claude/srini-bhakti/'
done=[]
def cell(x): return re.sub(r'\s+',' ',x).strip()
for f in glob.glob(R+'**/index.html',recursive=True):
    h=open(f).read(); ch=[0]
    def fix(m):
        sid=m.group(1); s=m.group(0)
        if sid=='glance' or '<table class="ct fact"' not in s: return s
        while True:
            t=re.search(r'<table class="ct fact">(.*?)</table>',s,re.S)
            if not t: break
            ps='';hdr=None
            cap=re.search(r'<caption>(.*?)</caption>',t.group(1),re.S)
            if cap: ps+=f'<p><b>{cell(cap.group(1))}</b></p>'
            for r in re.findall(r'<tr[^>]*>(.*?)</tr>',t.group(1),re.S):
                cs=[cell(c) for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>',r,re.S)]
                if not cs: continue
                if '<td' not in r: hdr=cs; continue
                if len(cs)==1: ps+=f'<p>{cs[0]}</p>'; continue
                def dot(v): return v if re.sub(r'<[^>]+>','',v).rstrip().endswith(('.','?','!','”',')')) else v+'.'
                if len(cs)>2 and hdr and len(hdr)==len(cs):
                    ps+=f'<p><b>{cs[0]}.</b> '+' '.join(f'<i>{hdr[k]}:</i> {dot(cs[k])}' for k in range(1,len(cs)))+'</p>'
                elif len(cs)>2:
                    ps+=f'<p><b>{cs[0]}.</b> '+' '.join(dot(c) for c in cs[1:])+'</p>'
                else:
                    ps+=f'<p><b>{cs[0]}.</b> {dot(cs[1])}</p>'
            assert ps.count('<p>')>(1 if cap else 0), (f,sid)
            rt=s.rfind('<div class="reading-table">',0,t.start())
            if rt!=-1 and rt==t.start()-len('<div class="reading-table">'):
                ee=s.find('</div>',t.end())
                s=s[:rt]+'<div class="panel reading">'+ps+'</div>'+s[ee+6:]; ch[0]+=1; continue
            s=s[:t.start()]+s[t.end():]
            if '<div class="panel reading">' in s: s=s.replace('<div class="panel reading">','<div class="panel reading">'+ps,1)
            else: s=s[:t.start()]+'<div class="panel reading">'+ps+'</div>'+s[t.start():]
            ch[0]+=1
        return s
    h2=re.sub(r'<section class="page[^"]*"(?: id="([^"]*)")?[^>]*>.*?</section>',fix,h,flags=re.S)
    if ch[0]: open(f,'w').write(h2); done.append((f.replace(R,'').replace('/index.html',''),ch[0]))
print(len(done),sum(n for _,n in done))
open('/tmp/untabled.txt','w').write('\n'.join(d for d,_ in done))
