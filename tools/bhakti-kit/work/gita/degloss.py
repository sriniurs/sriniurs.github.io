import re,glob,sys
G=re.compile(r'(?:(?<=^)|(?<=\. )|(?<=” )|(?<=\? )|(?<=\.” ))<i>[^<]+</i>, “[^”]*”(?:\.|(?<=[?!.]”))\s*')
tot=0;empty=[]
for f in sorted(glob.glob('d[0-9][0-9]*.py')):
    s=open(f).read()
    D={};exec(s,{'DEEP':D})
    out=[]
    for k in sorted(D):
        parts=[]
        for t in D[k]:
            n=G.sub('',t).strip()
            parts.append(n)
        if not parts[0]: empty.append(f'{f}:{k}')
        D[k]=tuple(parts)
    if '--write' in sys.argv:
        open(f,'w').write(''.join(f'DEEP[{k}]=({D[k][0]!r},\n {D[k][1]!r},\n {D[k][2]!r})\n' for k in sorted(D)))
    w=[len(re.sub('<[^>]+>','',' '.join(v)).split()) for v in D.values()]
    print(f, 'avg added words after', sum(w)//len(w))
print('ctx now empty:',len(empty))
