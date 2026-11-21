import re,sys,glob
exec(open('gc.py').read())
C=int(sys.argv[1]); TH=int(sys.argv[2]) if len(sys.argv)>2 else 230
def build2(P):
    D={}
    for f in sorted(glob.glob(f'd{C:02d}*.py')): exec(open(f).read(),{'DEEP':D})
    out=[]
    for v in P['V']:
        n=int(v['n']); d=D.get(n,('','',''))
        t=' '.join([v['ctx'],v['read'],v['life'],d[0],d[1],d[2]]+(list(v['talk']) if v.get('talk') else []))
        w=len(re.sub('<[^>]+>','',t).split())
        if w<TH: out.append(f'{n}:{w}')
    print(C,len(out),' '.join(out))
src=open(f'c{C:02d}.py').read().replace("exec(open('/home/claude/work/gita/gc.py').read())","")
exec(src)
