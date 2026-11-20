import json
exec(open('/home/claude/work/up_lib.py').read())
src=open('/home/claude/work/shakti/dv_common.py').read()
exec(open('/home/claude/work/shakti/ps_common.py').read().split('def LINGA')[0].split("exec(open('/home/claude/work/shakti/common_s.py').read())")[1].replace('import common_t as _ct','import sys; sys.path.insert(0,"/home/claude/work/triranga"); import common_t as _ct'))
exec('DVS'+src.split('DVS',1)[1].split('def head_vis')[0]); exec('def AV'+src.split('def AV')[1].split('def VISHNU')[0])
D='bhakti/vishnu/dashavatara'
files=['DV0_Dashavatara','DV1_Matsya','DV2_Kurma','DV3_Varaha','DV4_Narasimha','DV5_Vamana','DV6_Parashurama','DV7_Rama','DV8_Balarama_Buddha','DV9_Krishna','DV10_Kalki']
cp(f'shakti/{files[0]}.html',f'{D}/overview')
for (n,nm,s,f,y,d),fn in zip(DV,files[1:]): cp(f'shakti/{fn}.html',f'{D}/{s}')
WHEEL=''.join(f'<g transform="translate({50+34*__import__("math").cos(i*0.6283-1.57):.1f} {50+34*__import__("math").sin(i*0.6283-1.57):.1f})"><circle r="9" fill="#fff8e7"/>{AV(i+1,0,0,.17)}</g>' for i in range(10))
tiles=[tile(f'/{D}/overview/','#0d3f73',WHEEL,'Start here · overview','The Ten Avatāras','What an avatāra is, the Gītā’s promise, why the lists differ, the Vedic roots, art and temples.')]
for n,nm,s,f,y,d in DV:
    tiles.append(tile(f'/{D}/{s}/','#dcecff',f'<g transform="translate(50 54)">{AV(n,0,0,.85)}</g>'.replace('stroke="#111" stroke-width="2"','stroke="#151515" stroke-width="2"'),f'Avatāra {n} of 10 · {y}',nm,d[0].upper()+d[1:]+'.'))
index(D,'Daśāvatāra','Daśāvatāra, the ten avatāras of Viṣṇu, from Matsya the fish to Kalki the rider still to come: an illustrated reference guide to each, with stories, texts, art and temples.','/bhakti/vishnu/','Viṣṇu','#0d3f73','#ffd23f','#eef3fa','/bhakti/gods-banner.jpg',
 'Fish, tortoise, boar, man-lion, dwarf, three Rāmas, Kṛṣṇa and the rider to come: whenever dharma falls, he comes. Start with the overview, then meet each avatāra.',tiles)
c=json.load(open(f'{R}/bhakti/catalog.json'))
if not any(e['path']==f'/{D}/' for e in c['entries']):
    t=tile(f'/{D}/','#0d3f73',WHEEL,'Series · overview + 10 avatāras','Daśāvatāra','The ten avatāras of Viṣṇu, Matsya to Kalki: who each one is, the stories, texts, art and temples.','Open series ↗')
    i=[n for n,e in enumerate(c['entries']) if e['door']=='gods'][-1]
    c['entries'].insert(i+1,{'path':f'/{D}/','door':'gods','deities':['vishnu'],'tile':t})
    json.dump(c,open(f'{R}/bhakti/catalog.json','w'),ensure_ascii=False,indent=1)
print('ok')
