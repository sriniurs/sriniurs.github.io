import json,math
exec(open('/home/claude/work/up_lib.py').read())
_s=open('/home/claude/work/shakti/al_common.py').read()
exec(_s[_s.index('def LOTUS'):_s.index('import re as _re')])
exec(_s[_s.index('ALS='):_s.index('def series_note_al')])
D='bhakti/devi/ashta-lakshmi'
cp('shakti/AL0_Overview.html',f'{D}/overview')
FN={'adi':'AL1_Adi','dhanya':'AL2_Dhanya','dhairya':'AL3_Dhairya','gaja':'AL4_Gaja','santana':'AL5_Santana','vijaya':'AL6_Vijaya','vidya':'AL7_Vidya','dhana':'AL8_Dhana'}
for k,f in FN.items(): cp('shakti/'+f+'.html',f'{D}/{k}')
bg={'adi':'#ffe3ec','dhanya':'#dff5ea','dhairya':'#fde0d8','gaja':'#e6eefc','santana':'#fff1d6','vijaya':'#fde4e4','vidya':'#f4f4f8','dhana':'#fff5c0'}
blurb={'adi':'The primordial Lakṣmī: Bhṛgu’s daughter, Viṣṇu’s eternal consort, the merciful mediator, Padmāvatī of Tirumala.',
 'dhanya':'Grain and harvest: the Śrī Sūkta’s fertile Śrī, Annapūrṇā, Saṅkrānti and Pongal, never wasting food.',
 'dhairya':'Courage, also Vīra Lakṣmī: the eight-armed warrior, close to Durgā; Sītā, Sāvitrī and Prahlāda.',
 'gaja':'Bathed by elephants: the oldest image of Lakṣmī, from Bharhut and Sāñcī to coins and Hoysaḷa door lintels.',
 'santana':'Children and family: Kardama in the Śrī Sūkta, Varalakṣmī Vratam and Cārumatī, Santāna Gopāla.',
 'vijaya':'Victory: Vijayadaśamī, Mysuru Dasara, Arjuna “Vijaya”, Rāja Lakṣmī and the city of Vijayanagara.',
 'vidya':'Knowledge: not Sarasvatī but learning as fortune; Lakṣmī Hayagrīva, vidyārambha and the wealth no thief can take.',
 'dhana':'Money and gold: artha, Kubera’s loan, Śaṅkara’s rain of gold, Dhanteras and Dīpāvalī; earn rightly, give freely.'}
def ICON(k,s=.62): return f'<g transform="translate(0 4)">{LAK(k,50,50,s if k!="gaja" else .55)}</g>'
RING=''.join(f'<circle cx="{50+32*math.cos(i*0.785-1.57):.1f}" cy="{50+32*math.sin(i*0.785-1.57):.1f}" r="8" fill="{c}"/>' for i,c in enumerate(['#e0115f','#2a9d6f','#c0392b','#d8d8e0','#ffd60a','#e05a3a','#ffffff','#e0a800']))+'<circle cx="50" cy="50" r="12" fill="#f2a6c0"/>'
tiles=[tile(f'/{D}/overview/','#3a1414',RING,'Start here · overview','The Eight Forms of Lakṣmī','Who Lakṣmī is, the Śrī Sūkta and the churning, why eight and how the lists differ, her days and the Aṣṭalakṣmī temples.')]
for i,(k,n,d) in enumerate(AL): tiles.append(tile(f'/{D}/{k}/',bg[k],ICON(k),f'Form {i+1} of 8',n,blurb[k]))
index(D,'Aṣṭa Lakṣmī','The eight forms of Lakṣmī: Ādi, Dhānya, Dhairya, Gaja, Santāna, Vijaya, Vidyā and Dhana Lakṣmī. An illustrated reference guide to each form, its roots, stories, worship and meaning.','/bhakti/devi/','Devi','#3a1414','#ffd27a','#fdf3f3','/bhakti/devi/devi-banner.jpg',
 'One Goddess of fortune, eight gifts: grain, courage, royal grace, family, victory, knowledge, money, and the first Lakṣmī behind them all. Start with the overview, then meet each form.',tiles)
C=f'{R}/bhakti/catalog.json'; c=json.load(open(C)); L=c['entries']; p=f'/{D}/'
t=tile(p,'#ffe3ec',RING,'Series · overview + 8 forms','Aṣṭa Lakṣmī','The eight forms of Lakṣmī, from Ādi to Dhana: grain, courage, elephants, family, victory, knowledge and wealth.','Open series ↗')
old=[e for e in L if e['path']==p]
if old: old[0]['tile']=t
else:
    i=[j for j,e in enumerate(L) if e['path']=='/bhakti/devi/dasha-mahavidya/'][0]
    L.insert(i+1,{'path':p,'door':'gods','deities':['devi'],'tile':t})
json.dump(c,open(C,'w'),ensure_ascii=False,indent=1)
print('ok')
