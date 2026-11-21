import json
exec(open('/home/claude/work/up_lib.py').read())
_s=open('/home/claude/work/lalita/lk.py').read()
exec(_s[_s.index('def LAL'):_s.index('def LS')])
cp('lalita/Lalita_Trishati.html','bhakti/devi/lalita-trishati')
p='/bhakti/devi/lalita-trishati/'
IC='<path d="M50 6 L94 84 L6 84z" fill="none" stroke="#e0a800" stroke-width="3"/>'+LAL(50,60,.6)
t=tile(p,'#fde8ee',IC,'Hymn · 59 ślokas, 300 names','Lalitā Triśatī','All 300 names of Lalitā from the Brahmāṇḍa Purāṇa, every śloka on two pages with meanings and a deep dive.')
C=f'{R}/bhakti/catalog.json'; c=json.load(open(C)); L=c['entries']
old=[e for e in L if e['path']==p]
if old: old[0]['tile']=t
else:
    i=[j for j,e in enumerate(L) if e['path']=='/bhakti/devi/lalita-pancharatnam/'][0]
    L.insert(i+1,{'path':p,'door':'hymns','deities':['devi'],'tile':t})
json.dump(c,open(C,'w'),ensure_ascii=False,indent=1); print('ok')
