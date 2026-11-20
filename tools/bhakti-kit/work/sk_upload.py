import json
exec(open('/home/claude/work/shakti/sk_common.py').read())
exec(open('/home/claude/work/up_lib.py').read())
D='bhakti/shiva/subrahmanya-shashthi'
files={'skanda':'SK1_Skanda','shashthi':'SK2_Shashthi','kukke':'SK3_Kukke','ghati':'SK4_Ghati'}
for k,f in files.items(): cp('shakti/'+f+'.html',f'{D}/{k}')
art={'skanda':SKANDA(50,58,.55,vel=False),'shashthi':MANGOTREE(50,92,.55,split=True)+ROOSTER(50,40,.7),'kukke':NAGA(50,88,.75),'ghati':NAGA(36,88,.55)+'<rect x="60" y="40" width="26" height="36" rx="4" fill="#d8ecf8"/>'}
bg={'skanda':'#fde8d0','shashthi':'#dfe9f6','kukke':'#e6f2df','ghati':'#f6efd8'}
blurb={'skanda':'His names, his birth in the reeds and six faces, the vel, peacock and rooster, Valli and Devasenā, and why Karnataka worships him as a serpent.',
 'shashthi':'The war with Tāraka and Śūrapadma, the mango tree split into peacock and rooster, Skanda Ṣaṣṭhī and Subrahmaṇya Ṣaṣṭhī, and how the day is kept.',
 'kukke':'Vāsuki hiding from Garuḍa, the three-tier sanctum, Ādi Subrahmaṇya’s anthill, the nāga rites and the Campā Ṣaṣṭhī chariot.',
 'ghati':'Subrahmaṇya as a seven-hooded cobra and Lakṣmī Narasiṃha in one image, seen in a mirror; nāga stones, the chariot and the cattle fair.'}
tiles=[tile(f'/{D}/{k}/',bg[k],art[k],f'Part {i+1} of 4',t,blurb[k]) for i,(k,t) in enumerate(SKP)]
index(D,'Subrahmaṇya Ṣaṣṭhī','Subrahmaṇya Ṣaṣṭhī: who Skanda (Kārttikeya, Murugan) is, the Ṣaṣṭhī story of his war and wedding, and his two great serpent shrines in Karnataka, Kukke and Ghāṭi. An illustrated four-part guide.','/bhakti/shiva/','Śiva','#0b2a4a','#ffd23f','#eef3fa','/bhakti/shiva/shiva-banner.jpg',
 'Śiva’s son, the six-faced god of the spear, and the day Karnataka keeps for him. Meet Skanda, hear the Ṣaṣṭhī story, then visit Kukke and Ghāṭi.',tiles)
C=f'{R}/bhakti/catalog.json'; c=json.load(open(C)); L=c['entries']
p=f'/{D}/'
if not any(e['path']==p for e in L):
    i=[j for j,e in enumerate(L) if e['path']=='/bhakti/shiva/shiva-family-and-symbols/'][0]
    t=tile(p,'#dfe9f6',SKANDA(50,58,.55,vel=False),'Series · 4 parts','Subrahmaṇya Ṣaṣṭhī','Who Skanda is, the Ṣaṣṭhī story of his war and wedding, and his serpent shrines at Kukke and Ghāṭi.','Open series ↗')
    L.insert(i+1,{'path':p,'door':'gods','deities':['shiva'],'tile':t})
    json.dump(c,open(C,'w'),ensure_ascii=False,indent=1)
print('ok')
