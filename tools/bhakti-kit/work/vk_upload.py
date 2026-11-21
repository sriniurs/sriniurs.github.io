import json
exec(open('/home/claude/work/up_lib.py').read())
cp('shakti/VK_Vaikuntha.html','bhakti/vishnu/vaikuntha-ekadashi')
p='/bhakti/vishnu/vaikuntha-ekadashi/'
IC='<path d="M22 90 v-44 q28 -34 56 0 v44z" fill="#e0a800"/><path d="M32 90 v-38 q18 -22 36 0 v38z" fill="#fff8d0"/><circle cx="50" cy="62" r="9" fill="#4a7fd0"/><path d="M42 54 h16 l-3 -10 h-10z" fill="#e0a800"/>'
t=tile(p,'#1b2f5a',IC,'Festival · Sun 20 Dec 2026','Vaikuṇṭha Ekādaśī','The day the northern gate opens, also Gītā Jayantī: Srirangam, Tirumala, the fast, the vigil, pāraṇa and Ambarīṣa.')
C=f'{R}/bhakti/catalog.json'; c=json.load(open(C)); L=c['entries']
old=[e for e in L if e['path']==p]
if old: old[0]['tile']=t
else:
    i=[j for j,e in enumerate(L) if e['path']=='/bhakti/vishnu/hanuman/'][0]
    L.insert(i+1,{'path':p,'door':'gods','deities':['vishnu'],'tile':t})
json.dump(c,open(C,'w'),ensure_ascii=False,indent=1); print('ok')
