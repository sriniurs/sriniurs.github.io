import json
exec(open('/home/claude/work/up_lib.py').read())
exec(open('/home/claude/work/shakti/ps_common.py').read().split('def LINGA')[0].split("exec(open('/home/claude/work/shakti/common_s.py').read())")[1].replace('import common_t as _ct','import sys; sys.path.insert(0,"/home/claude/work/triranga"); import common_t as _ct'))
D='bhakti/temples-of-india/pancha-bhuta-sthalas'
files=[('overview','PS0_Pancha_Bhuta'),('ekambareshvara','PS1_Ekambareshvara'),('jambukeshvara','PS2_Jambukeshvara'),('arunachaleshvara','PS3_Arunachaleshvara'),('kalahastishvara','PS4_Kalahastishvara'),('chidambaram','PS5_Chidambaram')]
for slug,f in files: cp(f'shakti/{f}.html',f'{D}/{slug}')
ART={'earth':'<path d="M20 80 q30 -60 60 0z" fill="#c9a26b"/>','water':'<path d="M50 14 q30 38 0 64 q-30 -26 0 -64z" fill="#5ab0f0"/>','fire':'<path d="M30 86 q-14 -34 8 -58 q4 22 12 24 q2 -24 18 -34 q-6 30 8 40 q6 18 -14 28z" fill="#ff8c1a"/>',
 'air':'<path d="M14 40 q30 -16 54 0 q20 12 0 22 M14 60 q36 -12 64 6 M22 80 q24 -8 44 4" fill="none" stroke="#3a8a70" stroke-width="5"/>','space':'<circle cx="50" cy="50" r="34" fill="#1d1040"/><circle cx="38" cy="40" r="3" fill="#fff"/><circle cx="62" cy="34" r="3" fill="#fff"/><circle cx="58" cy="62" r="3" fill="#fff"/>'}
FIVE=''.join(f'<circle cx="{x}" cy="{y}" r="11" fill="{c}"/>' for x,y,c in ((50,18,'#e0501a'),(82,42,'#7ab8a0'),(70,80,'#6a4aa0'),(30,80,'#3b8fd0'),(18,42,'#a0703a')))+'<path d="M38 70 v-24 a12 12 0 0 1 24 0 v24z" fill="#2b2f36"/>'
BLURB={'earth':'The sand liṅga under the mango tree, Kāmākṣī’s embrace and Kṛṣṇadevarāya’s tower.','water':'The spring in the sanctum, the spider and the elephant, and the priest dressed as the Goddess.','fire':'The endless column, the hill that is Śiva, Kārttikai Dīpam, Girivalam and Ramaṇa.',
 'air':'The lamp that flickers without wind, Kaṇṇappa’s eyes and the tower that fell.','space':'Naṭarāja’s dance, the Secret of Cidambaram and the golden roof.'}
tiles=[tile(f'/{D}/overview/','#0b2a4a',FIVE,'Start here · overview','The Five Element Temples','Earth, water, fire, air and space: the idea, the map, the Goddesses and the saints.')]
for k in S5:
    tiles.append(tile(f'/{D}/{k[10]}/','#eef3fa',ART[k[0]],f'{k[2]} · {k[6]}',k[3],BLURB[k[0]]))
index(D,'Pañcabhūta Sthalas','The Pañcabhūta Sthalas, Śiva’s five temples of the five elements: Kāñcīpuram (earth), Tiruvānaikkāval (water), Tiruvaṇṇāmalai (fire), Śrīkāḷahasti (air) and Cidambaram (space), in illustrated reference guides.','/bhakti/temples-of-india/','Temples of India','#0b2a4a','#ffd23f','#eef3fa','/bhakti/temples-of-india/temples-banner.jpg',
 'Five temples, five elements, one Śiva: as the earth at Kāñcī, water at Tiruvānaikkāval, fire at Aruṇācala, air at Kāḷahasti and space at Cidambaram.',tiles)
c=json.load(open(f'{R}/bhakti/catalog.json'))
if not any(e['path']==f'/{D}/' for e in c['entries']):
    t=tile(f'/{D}/','#0b2a4a',FIVE,'6 articles · overview + 5 guides','Pañcabhūta Sthalas','Śiva’s five element temples: earth, water, fire, air and space, from Kāñcī to Cidambaram.','Open series ↗')
    i=[n for n,e in enumerate(c['entries']) if e['path'].endswith('/12-jyotirlingas/')][0]
    c['entries'].insert(i+1,{'path':f'/{D}/','door':'temples','deities':['shiva'],'group':'circuits','tile':t})
    json.dump(c,open(f'{R}/bhakti/catalog.json','w'),ensure_ascii=False,indent=1)
print('ok')
