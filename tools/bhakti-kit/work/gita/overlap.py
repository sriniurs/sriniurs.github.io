import re,sys,io,contextlib,glob,unicodedata
exec(open('gc.py').read())
C=int(sys.argv[1])
def norm(s): return re.sub(r'[^a-zāīūṛṝḷṃḥṅñṭḍṇśṣ]','',s.lower())
def build2(P):
    D={}
    for f in sorted(glob.glob(f'd{C:02d}*.py')): exec(open(f).read(),{'DEEP':D})
    for v in P['V']:
        n=int(v['n']); d=D.get(n)
        if not d: continue
        ws=[norm(re.sub('<[^>]+>','',a)) for a,b in v['words']]
        for t in re.findall(r'<i>([^<]+)</i>',' '.join(d)):
            t2=norm(t)
            if len(t2)>4 and any(t2 in w or w in t2 for w in ws): print(n,t)
src=open(f'c{C:02d}.py').read().replace("exec(open('/home/claude/work/gita/gc.py').read())","")
exec(src)
