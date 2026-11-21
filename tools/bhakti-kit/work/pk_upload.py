import json
exec(open('/home/claude/work/up_lib.py').read())
D='bhakti/temples-of-india/pancha-kedar'
FN=[('overview','PK0_Overview'),('kedarnath','PK1_Kedarnath'),('tungnath','PK2_Tungnath'),('rudranath','PK3_Rudranath'),('madhyamaheshwar','PK4_Madhyamaheshwar'),('kalpeshwar','PK5_Kalpeshwar')]
for k,f in FN: cp('shakti/'+f+'.html',f'{D}/{k}')
SNOW='<path d="M6 86 L32 40 L46 60 L62 30 L94 86z" fill="#9fb3c8"/><path d="M54 44 L62 30 L70 44 l-4 4 l-4 -3 l-4 3z" fill="#fff"/>'
def TEM(extra=''): return SNOW+'<rect x="36" y="62" width="28" height="22" fill="#9a9a90"/><path d="M36 62 L50 44 L64 62z" fill="#8a8a80"/><path d="M50 44 v-8 l7 3 -7 3" fill="#ff8c1a"/>'+extra
IC={'overview':SNOW+''.join(f'<rect x="{10+i*17}" y="74" width="12" height="10" fill="#9a9a90"/><path d="M{10+i*17} 74 l6 -8 l6 8z" fill="#8a8a80"/>' for i in range(5)),
 'kedarnath':TEM('<path d="M44 84 q6 -10 12 0z" fill="#3a3a3a"/>'),
 'tungnath':TEM('<circle cx="82" cy="20" r="7" fill="#fff8e7"/>'),
 'rudranath':SNOW+'<path d="M26 86 q24 -46 48 0z" fill="#6a6a60"/><circle cx="50" cy="74" r="7" fill="#5b8fe0"/>',
 'madhyamaheshwar':TEM('<circle cx="50" cy="76" r="3" fill="#ffd60a"/>'),
 'kalpeshwar':'<path d="M6 86 h88" stroke="#6a9a4a" stroke-width="6"/><path d="M20 84 q30 -54 60 0z" fill="#6a6a60"/><path d="M40 84 q10 -16 20 0z" fill="#2a2a2a"/><path d="M42 50 q8 -10 16 0 q-8 -4 -16 0" fill="none" stroke="#3a2a1a" stroke-width="3"/>'}
bl={'overview':('Start here · overview','Śiva’s Five Himalayan Shrines','The Pāṇḍavas and the bull, the five parts, winter seats, Karnataka’s priests at Kedār and Ādi Śaṅkara.'),
 'kedarnath':('Kedār 1 of 5 · the hump','Kedārnāth','The hump-shaped rock liṅga, Jyotirliṅga and Char Dhām, the 2013 flood and Bhīm Śilā, the Karnataka Rāval.'),
 'tungnath':('Kedār 2 of 5 · the arms','Tuṅganāth','The highest Śiva temple, below Candraśilā where Rāma meditated; local Makkumath priests.'),
 'rudranath':('Kedār 3 of 5 · the face','Rudranāth','Nīlakaṇṭha’s face in a rock cave among high meadows; the Vaitaraṇī and offerings for ancestors.'),
 'madhyamaheshwar':('Kedār 4 of 5 · the navel','Madhyamaheśvar','The navel-shaped liṅga below Chaukhamba, Būḍhā Madhyamaheśvar and its holy water.'),
 'kalpeshwar':('Kedār 5 of 5 · the hair','Kalpeśvar','Śiva’s jaṭā in a cave in the Urgam valley, the wish-tree, and the only Kedār open all year.')}
bg={'overview':'#0b2a4a','kedarnath':'#dceefa','tungnath':'#e6eefc','rudranath':'#e8eef2','madhyamaheshwar':'#e6f2df','kalpeshwar':'#eef6e2'}
tiles=[tile(f'/{D}/{k}/',bg[k],IC[k],*bl[k]) for k,f in FN]
index(D,'Pañca Kedār','Pañca Kedār, Śiva’s five Himalayan shrines in Garhwal: Kedārnāth, Tuṅganāth, Rudranāth, Madhyamaheśvar and Kalpeśvar, with the legend of the Pāṇḍavas and the bull. An illustrated reference guide.','/bhakti/temples-of-india/','Temples of India','#0b2a4a','#ffd23f','#eef3fa','/bhakti/shiva/shiva-banner.jpg',
 'The Pāṇḍavas chased Śiva; he dived into the Himalaya as a bull. His hump, arms, face, navel and hair rose in five valleys. Start with the overview, then visit each Kedār.',tiles)
C=f'{R}/bhakti/catalog.json'; c=json.load(open(C)); L=c['entries']; p=f'/{D}/'
t=tile(p,'#dceefa',IC['overview'],'Series · overview + 5 shrines','Pañca Kedār','Śiva’s five Himalayan shrines: Kedārnāth, Tuṅganāth, Rudranāth, Madhyamaheśvar and Kalpeśvar, and the bull legend.','Open series ↗')
old=[e for e in L if e['path']==p]
if old: old[0]['tile']=t
else:
    i=[j for j,e in enumerate(L) if e['path']=='/bhakti/temples-of-india/12-jyotirlingas/'][0]
    L.insert(i+1,{'path':p,'door':'temples','deities':['shiva'],'tile':t})
json.dump(c,open(C,'w'),ensure_ascii=False,indent=1)
print('ok')
