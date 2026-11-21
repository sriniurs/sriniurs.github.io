import re,sys,glob
exec(open('gc.py').read())
C=int(sys.argv[1])
def toks(s):
    s=re.sub('<[^>]+>','',s)
    return set(w.lower() for w in re.findall(r"[A-ZĀĪŪṚŚṢṆḌṬ][\wāīūṛṝḷṃḥṅñṭḍṇśṣ’-]{3,}|\d+\.\d+|\d+\.\d+\.\d+",s))-{'commentators','the','many','this','some','śaṅkara','rāmānuja','madhva','kṛṣṇa','arjuna','gītā','lord','vedic','hindu'}
def build2(P):
    D={}
    for f in sorted(glob.glob(f'd{C:02d}*.py')):
        if f.endswith('z.py'): continue
        exec(open(f).read(),{'DEEP':D})
    Z={}; exec(open(f'd{C:02d}z.py').read().split('for _k')[0],{},Z) if False else None
    g={}; exec(open(f'd{C:02d}z.py').read().split('\nfor _k')[0],g); Z=g['Z']
    for v in P['V']:
        n=int(v['n']); d=D.get(n,('','',''))
        old=' '.join([v['mean'],v['ctx'],v['read'],v['life'],*d]+(list(v['talk']) if v.get('talk') else []))
        common=toks(Z.get(n,''))&toks(old)
        if common: print(n,sorted(common))
src=open(f'c{C:02d}.py').read().replace("exec(open('/home/claude/work/gita/gc.py').read())","")
exec(src)
