import json
exec(open('/home/claude/work/up_lib.py').read())
exec(open('/home/claude/work/gita_icons.py').read())
G={}; exec(open('/home/claude/work/gita/gc.py').read(),G); CH=G['CH']
D='bhakti/vishnu/bhagavad-gita'
cp('gita/Gita_Overview.html',f'{D}/overview')
for n,*_ in CH: cp(f'gita/Gita_Chapter{n:02d}.html',f'{D}/chapter-{n}')
def num(n,fill='#ffd60a'): return f'<circle cx="50" cy="50" r="34" fill="{fill}"/><text x="50" y="62" text-anchor="middle" font-size="{34 if n<10 else 30}" font-weight="bold" fill="#151515" stroke="none" font-family="Georgia,serif">{n}</text>'
tiles=[tile(f'/{D}/overview/','#0d3f73',BOOK,'Start here · overview','The Song of the Lord','What the Gītā is, the story before it, who is who, a map of all 18 chapters, famous verses and how the great teachers read it.')]
for n,nm,en,nv in CH:
    tiles.append(tile(f'/{D}/chapter-{n}/','#dcecff',icon(n),f'Chapter {n} of 18 · {nv} ślokas',en[0].upper()+en[1:],f'{nm}. All {nv} ślokas in IAST, each with meaning, key words and a deep dive.'))
index(D,'Bhagavad Gītā','The Bhagavad Gītā, all 18 chapters and 700 ślokas explained and illustrated: every śloka in IAST with plain-English meaning, key words and a deep dive, plus a series overview.','/bhakti/vishnu/','Viṣṇu','#0d3f73','#ffd23f','#eef3fa','/bhakti/vishnu/vishnu-banner.jpg',
 'On a battlefield, Arjuna drops his bow and Kṛṣṇa answers him. All 700 ślokas, chapter by chapter, each on two pages: the chant, a picture, the meaning, the key words and a deep dive. Start with the overview.',tiles)
c=json.load(open(f'{R}/bhakti/catalog.json'))
old=[e for e in c['entries'] if e['path']==f'/{D}/']
if old:
    old[0]['tile']=tile(f'/{D}/','#0d3f73',BOOK,'Series · overview + 18 chapters','Bhagavad Gītā','All 700 ślokas of the Song of the Lord, chapter by chapter, each explained on two pages with a deep dive.','Open series ↗')
    json.dump(c,open(f'{R}/bhakti/catalog.json','w'),ensure_ascii=False,indent=1)
else:
    t=tile(f'/{D}/','#0d3f73',BOOK,'Series · overview + 18 chapters','Bhagavad Gītā','All 700 ślokas of the Song of the Lord, chapter by chapter, each explained on two pages with a deep dive.','Open series ↗')
    i=[n for n,e in enumerate(c['entries']) if e['door']=='scriptures'][-1]
    c['entries'].insert(i+1,{'path':f'/{D}/','door':'scriptures','deities':['vishnu'],'tile':t})
    json.dump(c,open(f'{R}/bhakti/catalog.json','w'),ensure_ascii=False,indent=1)
print('ok')
