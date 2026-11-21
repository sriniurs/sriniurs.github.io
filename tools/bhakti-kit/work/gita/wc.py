import re,sys,io,contextlib
exec(open('gc.py').read())
_b=build2
R={}
def build2(P):
    ws=[len(re.sub('<[^>]+>','',v['ctx']+' '+v['read']+' '+v['life']+' '+(' '.join(v['talk']) if v.get('talk') else '')).split()) for v in P['V']]
    R[P['ch']]=ws
for c in range(1,19):
    src=open(f'c{c:02d}.py').read().replace("exec(open('/home/claude/work/gita/gc.py').read())","")
    try:
        with contextlib.redirect_stdout(io.StringIO()): exec(src)
    except Exception as e: print(c,'ERR',e)
for c,ws in sorted(R.items()): print(c,len(ws),'avg',sum(ws)//len(ws),'min',min(ws),'max',max(ws))
