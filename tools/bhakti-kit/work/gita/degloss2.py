import re,glob,sys
ITEM=re.compile(r'<i>[^<]+</i>,? “[^”]*”')
def clean(t):
    sents=re.split(r'(?<=[.?!”])\s+(?=<i>|[A-ZĀĪŪṚŚṢṆḌṬ“])',t)
    keep=[]
    for s in sents:
        rest=ITEM.sub('',s)
        rest=re.sub(r'\b(and|or|the|a|an|then)\b','',rest)
        if ITEM.search(s) and len(re.findall(r'[A-Za-zĀ-ž]{2,}',re.sub('<[^>]+>','',rest)))<3: continue
        keep.append(s)
    return ' '.join(keep).strip()
removed=0
for f in sorted(glob.glob('d[0-9][0-9]*.py')):
    D={};exec(open(f).read(),{'DEEP':D})
    for k in D:
        new=tuple(clean(x) for x in D[k])
        for a,b in zip(D[k],new):
            if a!=b: removed+=1; 
            if a!=b and '-v' in sys.argv: print(f,k,'|',a[:160],'\n   =>',b[:160])
        D[k]=new
    if '--write' in sys.argv:
        open(f,'w').write(''.join(f'DEEP[{k}]=({D[k][0]!r},\n {D[k][1]!r},\n {D[k][2]!r})\n' for k in sorted(D)))
print('changed fields',removed)
