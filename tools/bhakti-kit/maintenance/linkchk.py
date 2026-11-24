import re,os,sys
root='/home/claude/srini-bhakti'; bad=0
for f in sys.argv[1:]:
    h=open(f).read()
    for u in set(re.findall(r'href="(/[^"#?]*)',h)):
        p=root+u
        if not (os.path.isfile(p) or os.path.isfile(p.rstrip('/')+'/index.html')): print('BROKEN',f,u); bad+=1
print('broken',bad)
