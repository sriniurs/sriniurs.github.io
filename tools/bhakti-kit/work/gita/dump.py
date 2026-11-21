import re,sys,io,contextlib
exec(open('gc.py').read())
C=int(sys.argv[1]); A=int(sys.argv[2]); Z=int(sys.argv[3])
def build2(P):
    for v in P['V']:
        n=int(v['n'])
        if A<=n<=Z:
            t=lambda x:re.sub('<[^>]+>','',x)
            print(f"## {n} {v['theme']} | {t(v['mean'])[:160]}\nC: {t(v['ctx'])}\nR: {t(v['read'])}\nL: {t(v['life'])}")
src=open(f'c{C:02d}.py').read().replace("exec(open('/home/claude/work/gita/gc.py').read())","")
with contextlib.redirect_stdout(sys.stdout): exec(src)
