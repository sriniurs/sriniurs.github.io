import re,os
exec(open('/home/claude/work/up_lib.py').read())
exec(open('/home/claude/work/shakti/mv_common.py').read().split('def BODY')[0].replace("exec(open('/home/claude/work/shakti/common_s.py').read())",''))
src=open('/home/claude/work/shakti/mv_common.py').read()
exec('def BODY'+src.split('def BODY')[1].split('MVN=')[0])
import ast
_t=src.split('MVN=')[1]; _d=0
for _i,_c in enumerate(_t):
    _d+=(_c=='[')-(_c==']')
    if _d==0: break
MVN=ast.literal_eval(_t[:_i+1])
S='shakti/'; D='bhakti/devi/dasha-mahavidya'
files={'kali':'MV01_Kali','tara':'MV02_Tara','tripurasundari':'MV03_Tripurasundari','bhuvaneshvari':'MV04_Bhuvaneshvari','bhairavi':'MV05_Bhairavi','chinnamasta':'MV06_Chinnamasta','dhumavati':'MV07_Dhumavati','bagalamukhi':'MV08_Bagalamukhi','matangi':'MV09_Matangi','kamala':'MV10_Kamala'}
cp(S+'Dasha_Mahavidya.html',D+'/overview')
for k,f in files.items(): cp(S+f+'.html',f'{D}/{k}')
WHEEL=''.join(f'<circle cx="{50+32*__import__("math").cos(i*0.6283)}" cy="{50+32*__import__("math").sin(i*0.6283)}" r="7" fill="{c}"/>' for i,c in enumerate(['#1a1a2a','#3b4fa0','#c0392b','#e0115f','#a01a1a','#e05a3a','#9a9a9a','#ffd60a','#2a9d6f','#f2c070']))+'<circle cx="50" cy="50" r="14" fill="#ffd60a"/>'
bg={1:'#2a2a3a',2:'#dfe6ff',3:'#fde4e4',4:'#fff1d6',5:'#fde0d8',6:'#fde0d8',7:'#e8e8ec',8:'#fff5c0',9:'#dff5ea',10:'#ffe3ec'}
blurb={1:'Time, death and the Mother of the cremation ground; Dakṣiṇeśvar and Kālīghāṭ.',2:'The saviour who carries across; Tārāpīṭh, Vasiṣṭha and the Buddhist Tārā.',3:'Lalitā, the Śrī Cakra and the beauty of the three worlds.',
4:'Queen of the worlds, Goddess of space, and Kannada Tāyi of Karnataka.',5:'The fire of tapas, the Bhairavī Brāhmaṇī and the rāga.',6:'The self-beheaded Goddess, Chinnamuṇḍā and Rajrappa.',
7:'The smoky widow on the crow-bannered chariot; Kāśī and Datiā.',8:'The yellow Goddess who stills the storm and seizes the tongue.',9:'The green Goddess of speech and music, born from leftovers.',10:'The lotus Goddess bathed by elephants: the Tantric Lakṣmī.'}
tiles=[tile(f'/{D}/overview/','#3a1414',WHEEL,'Start here · overview','The Ten Great Wisdoms','Who the Mahāvidyās are, Satī and the ten directions, their order, pairings and temples.')]
for n,nm,slug,m in MVN:
    tiles.append(tile(f'/{D}/{slug}/',bg[n],f'<g transform="translate(0 6)">{MV(n,50,48,.75)}</g>',f'Mahāvidyā {n} of 10',nm,blurb[n]))
index(D,'Daśa Mahāvidyā','The ten Great Wisdoms of the Goddess, Kālī to Kamalā: an illustrated reference guide to each Mahāvidyā, her stories, meaning and temples.','/bhakti/devi/','Devi','#3a1414','#ffd27a','#fdf3f3','/bhakti/devi/devi-banner.jpg',
 'Ten faces of one Mother, from Kālī in the cremation ground to Kamalā on her lotus. Start with the overview, then meet each Goddess.',tiles)
print('ok')
