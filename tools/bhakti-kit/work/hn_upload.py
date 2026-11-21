import json
exec(open('/home/claude/work/up_lib.py').read())
CY='#ffd60a';CO='#ff9f1c';CB='#4dabf7';CG='#69db7c';CW='#fff8e7';CR='#e03131'
def HN(x=50,y=56,s=1,extra=''):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M14 22 q22 -2 18 -26" fill="none" stroke="#e08a2a" stroke-width="5"/><path d="M-14 30 q-2 -30 14 -34 q16 4 14 34z" fill="#e0701a"/>'
     f'<circle cy="-14" r="10" fill="#e08a2a"/><ellipse cy="-9" rx="6.5" ry="5" fill="#f2c79b"/><path d="M-7 -24 h14 l-2 -7 l-3 3 l-2 -5 l-2 5 l-3 -3z" fill="{CY}"/>{extra}</g>')
ICONS={
'who':HN(50,56,1.15,'<path d="M20 22 l8 -30" stroke="#7a4a1a" stroke-width="3"/><circle cx="29" cy="-12" r="7" fill="#e0a800"/>'),
'birth':f'<circle cx="72" cy="28" r="16" fill="{CY}"/>'+HN(36,62,.8),
'kishkindha':''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.7}" fill="#c9a26b"/>' for x,y,r in ((20,84,14),(80,82,16),(64,70,10)))+HN(50,56,.9),
'sundara':f'<rect x="0" y="70" width="100" height="30" fill="{CB}"/><path d="M6 80 q10 -6 20 0 t20 0 t20 0 t20 0" fill="none" stroke="#fff"/>'+HN(46,44,.8)+''.join(f'<rect x="{78+i*6}" y="{52-i*4}" width="5" height="{20+i*4}" fill="{CY}"/>' for i in range(3)),
'yuddha':HN(40,60,.85)+f'<path d="M58 40 l10 -22 l8 10 l8 -16 l12 28z" fill="#6a9a4a"/><circle cx="70" cy="34" r="2.5" fill="{CY}"/><circle cx="80" cy="36" r="2.5" fill="{CY}"/>',
'temples':f'<path d="M30 86 v-30 l20 -26 l20 26 v30z" fill="{CW}"/><path d="M42 86 v-16 h16 v16" fill="{CO}"/><path d="M50 30 v-18 l14 5 -14 5" fill="{CO}"/>',
'chalisa':f'<path d="M18 30 q16 -8 32 0 v50 q-16 -8 -32 0z" fill="{CW}"/><path d="M82 30 q-16 -8 -32 0 v50 q16 -8 32 0z" fill="{CW}"/><text x="34" y="62" text-anchor="middle" font-size="16" font-weight="bold" fill="#151515" stroke="none" font-family="Georgia,serif">40</text><path d="M58 46 h16 M58 56 h16 M58 66 h12"/>',
'ashtak':f'<circle cx="50" cy="50" r="30" fill="{CR}"/><text x="50" y="62" text-anchor="middle" font-size="34" font-weight="bold" fill="#fff" stroke="none" font-family="Georgia,serif">8</text>',
'slokas':f'<circle cx="50" cy="50" r="32" fill="{CY}"/><text x="49" y="66" text-anchor="middle" font-size="44" fill="#151515" stroke="none" font-family="serif">ॐ</text>',
}
D='bhakti/vishnu/hanuman'
PARTS=[('who','HN1_Who','Who Hanumān Is','His names, whose son he is, his forms and the five-faced Pañcamukha, the cirañjīvī belief, the Mahābhārata, Jain and Thai tellings, worship and Jayantī dates.','#dcecff'),
 ('birth','HN2_Birth','Birth and Boyhood','Añjanā and the Wind, the leap at the sun, Indra’s thunderbolt and the broken jaw, the gods’ boons, the curse of forgetting, and four birthplace claims.','#fff3c4'),
 ('kishkindha','HN3_Kishkindha','Kiṣkindhā','Meeting Rāma in disguise, “not one wrong word”, the fire-vow with Sugrīva, Vālī’s death, the rains, the ring, Sampāti and Jāmbavān’s reminder.','#f2e6c8'),
 ('sundara','HN4_Sundara','The Leap to Laṅkā','The Sundara Kāṇḍa scene by scene: Surasā, Laṅkinī, the night search, Sītā found, the ring and crest-jewel, Laṅkā on fire, “Seen Sītā”.','#dceefa'),
 ('yuddha','HN5_Yuddha','The War and After','Vibhīṣaṇa’s refuge, the bridge, two mountains of herbs, Ahirāvaṇa, news to Sītā, the pearl necklace, Rāma in his heart, Rāma’s farewell.','#e6f2df'),
 ('temples','HN6_Temples','Hanumān’s Temples','Saṅkaṭ Mocan, Hanumāngaṛhī, Sālāsar, Jakhu, Añjanādri and Yantroddhāraka at Hampi, Gāli Āñjaneya, Nāmakkal, Suchindram and more.','#fde8d0')]
for k,f,*_ in PARTS: cp('shakti/'+f+'.html',f'{D}/{k}')
HY=[('hanuman-chalisa','hanuman/Hanuman_Chalisa','chalisa','Hanumān Cālīsā','All 43 verses of Tulasīdāsa’s hymn, each on two pages with meaning, key words and a deep dive.','#fff3c4'),
 ('sankatmochan-ashtak','hanuman/Sankatmochan_Ashtak','ashtak','Saṅkaṭmocan Aṣṭak','Eight rescues and one refrain, “who does not know your name is Saṅkaṭmocan?”, every verse explained.','#fde4e4'),
 ('hanuman-slokas','hanuman/Hanuman_Slokas','slokas','Hanumān Ślokas','Manojavam, buddhir balam, atulitabaladhāmam and more, with the Hanumān Gāyatrī, each explained.','#fff8d6')]
for slug,f,*_ in HY: cp(f+'.html',f'bhakti/vishnu/{slug}')
tiles=[tile(f'/{D}/{k}/',bg,ICONS[k],f'Part {i+1} of 6',t,b) for i,(k,f,t,b,bg) in enumerate(PARTS)]
tiles+=[tile(f'/bhakti/vishnu/{slug}/',bg,ICONS[ic],'Hymn · verse by verse',t,b) for slug,f,ic,t,b,bg in HY]
index(D,'Hanumān','Hanumān, Rāma’s messenger and greatest devotee: an illustrated six-part guide to who he is, his birth, Kiṣkindhā, the leap to Laṅkā, the war and his temples, with the Hanumān Cālīsā, Saṅkaṭmocan Aṣṭak and Sanskrit ślokas verse by verse.','/bhakti/vishnu/','Viṣṇu','#0d3f73','#ffd23f','#eef3fa','/bhakti/vishnu/vishnu-banner.jpg',
 'Son of the Wind, servant of Rāma, guard at every village gate. Six parts tell his story, from the leap at the sun to Rāma’s farewell, then visit his temples; three hymns follow, verse by verse.',tiles)
C=f'{R}/bhakti/catalog.json'; c=json.load(open(C)); L=c['entries']
def add(path,door,deities,t,after):
    if any(e['path']==path for e in L):
        [e for e in L if e['path']==path][0]['tile']=t; return
    idx=[j for j,e in enumerate(L) if e['door']==door and after(e)]
    L.insert((idx[-1]+1) if idx else len(L),{'path':path,'door':door,'deities':deities,'tile':t})
add(f'/{D}/','gods',['vishnu','shiva'],tile(f'/{D}/','#dcecff',ICONS['who'],'Series · 6 parts + 3 hymns','Hanumān','Rāma’s messenger: who he is, his story from the sun leap to Rāma’s farewell, and his great temples.','Open series ↗'),lambda e:'vishnu' in e['deities'])
for slug,f,ic,t,b,bg in HY:
    add(f'/bhakti/vishnu/{slug}/','hymns',['vishnu'],tile(f'/bhakti/vishnu/{slug}/',bg,ICONS[ic],'Hymn · Hanumān',t,b),lambda e:e['deities'][0]=='vishnu')
json.dump(c,open(C,'w'),ensure_ascii=False,indent=1)
print('ok')
