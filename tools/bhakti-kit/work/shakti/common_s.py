import sys,re; sys.path.insert(0,'/home/claude/work/triranga')
from common_t import *
src=open('/home/claude/work/mysuru/uttanahalli.py').read()
exec(src.split("head=head_red(")[0].split("from common_t import *",1)[1])
exec(src[src.find('def tl('):src.find('cover=(')])
_h=('The 18 Śakti Pīṭhas · Aṣṭādaśa Śakti Pīṭha Stotram · srini.presents',
 'The 18 great Śakti Pīṭhas: the legend of Satī and Dakṣa, the Aṣṭādaśa Śakti Pīṭha Stotram verse by verse with meanings, a map and table of all 18, the disputed sites, and how the count grew from 4 to 51 to 108. An illustrated reference guide.')
SER='/bhakti/temples-of-india/18-shakti-peethas/'
# --- the 18 ---
P=[ # n, goddess, stotram place, today, state, lat, lon, part, short
 (1,'Śāṅkarī','Laṅkā','Trincomalee (claimed)','Sri Lanka',8.58,81.23,'groin','Laṅkā'),
 (2,'Kāmākṣī','Kāñcīpura','Kanchipuram','Tamil Nadu',12.83,79.70,'navel','Kāñcī'),
 (3,'Śṛṅkhalā','Pradyumna','Pandua, Hooghly (claimed)','West Bengal',23.08,88.28,'stomach','Pradyumna'),
 (4,'Cāmuṇḍā','Krauñcapaṭṭaṇa','Mysuru','Karnataka',12.27,76.67,'hair','Mysuru'),
 (5,'Jogulāmbā','Alampura','Alampur','Telangana',15.88,78.13,'teeth','Alampur'),
 (6,'Bhramarāmbikā','Śrīśaila','Srisailam','Andhra Pradesh',16.07,78.87,'neck','Śrīśailam'),
 (7,'Mahālakṣmī','Kolhāpura','Kolhapur','Maharashtra',16.70,74.24,'eyes','Kolhāpur'),
 (8,'Ekavīrikā','Māhura','Mahur','Maharashtra',19.83,77.92,'hand','Māhur'),
 (9,'Mahākālī','Ujjayinī','Ujjain','Madhya Pradesh',23.18,75.77,'upper lip','Ujjain'),
 (10,'Puruhūtikā','Pīṭhikā','Pithapuram','Andhra Pradesh',17.12,82.25,'back','Pīṭhāpuram'),
 (11,'Girijā','Oḍhyāṇa','Jajpur (Birajā)','Odisha',20.85,86.33,'navel','Jājpur'),
 (12,'Māṇikyā','Dakṣavāṭikā','Draksharamam','Andhra Pradesh',16.79,82.06,'left cheek','Drākṣārāmam'),
 (13,'Kāmarūpī','Harikṣetra','Kāmākhyā, Guwahati','Assam',26.17,91.70,'yoni','Kāmākhyā'),
 (14,'Mādhaveśvarī','Prayāga','Prayagraj','Uttar Pradesh',25.43,81.85,'fingers','Prayāga'),
 (15,'Vaiṣṇavī','Jvālā','Jwalamukhi, Kangra','Himachal Pradesh',31.88,76.32,'tongue','Jvālāmukhī'),
 (16,'Māṅgalyagaurī','Gayā','Gaya','Bihar',24.78,85.00,'breast','Gayā'),
 (17,'Viśālākṣī','Vārāṇasī','Varanasi','Uttar Pradesh',25.32,83.01,'earrings','Vārāṇasī'),
 (18,'Sarasvatī','Kāśmīra','Śāradā (ruins), Neelum valley','Pakistan-administered Kashmir',34.79,74.19,'right hand','Śāradā')]
POLY='21,163 40,174 26,177 46,195 66,190 68,214 75,246 87,281 107,318 120,333 128,325 140,309 146,290 151,274 149,252 173,240 193,221 219,204 224,186 243,185 246,175 242,155 238,136 256,134 280,127 312,109 332,111 324,128 308,153 295,167 286,182 275,165 271,152 258,145 244,132 238,121 208,119 180,121 150,104 139,82 123,65 132,44 121,33 92,34 79,45 88,62 96,68 88,80 80,91 70,97 51,116 40,130 43,141 33,154'
def xy(lat,lon): return 42+(lon-70.4)*11, 193+(20.89-lat)*11
LANKA=' '.join(f'{xy(a,b)[0]:.0f},{xy(a,b)[1]:.0f}' for a,b in ((9.8,80.0),(8.5,81.3),(7,81.8),(6,80.6),(6.4,79.9),(8,79.8)))
GANGA='<path d="M126 83 L136 104 L158 126 L180 143 L208 142 L236 153" fill="none" stroke="#4aa3df" stroke-width="2.5"/>'
def LAND(): return f'<polygon points="{POLY}" fill="#f4e6d0" stroke="#111" stroke-width="2"/><polygon points="{LANKA}" fill="#f4e6d0" stroke="#111" stroke-width="2"/>'+GANGA
def minimap(hi,label):
    g=''
    for n,_,_,_,_,la,lo,_,sh in P:
        x,y=xy(la,lo)
        if n in hi:
            right = x<215 and n not in (5,12,14)
            g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#c0392b" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(10 if right else -10):.0f}',f'{y+4:.0f}',f'{n} {sh}',13,'#111','start' if right else 'end')
        else: g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#bbb" stroke="#111" stroke-width="1.2"/>'
    return f'<svg width="230" height="190" viewBox="0 0 230 190" role="img" aria-label="{label}"><rect width="230" height="190" fill="#fdf1e8"/><g transform="translate(12 -4) scale(0.52)">'+LAND()+g+'</g></svg>'
# --- figures ---
def FLAME(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-34" y="0" width="68" height="18" fill="#c9a26b"/><path d="M-24 0 q-8 -34 10 -52 q2 22 10 24 q2 -30 18 -44 q-6 30 8 40 q8 -10 6 -22 q16 26 -4 54z" fill="#ff8c1a"/><path d="M-10 0 q-2 -16 8 -24 q2 12 8 12 q4 -8 2 -14 q10 14 -2 26z" fill="#ffd60a"/></g>'
def KING(x,y,s=1,c='#7a5a2a',head='#f2c79b'): return f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,c,head,1)+'<path d="M-12 -40 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800" stroke="#111" stroke-width="1.5"/></g>'
def SHIVA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-22 70 q-4 -60 22 -70 q26 10 22 70z" fill="#5b8fe0"/><circle cy="-14" r="13" fill="#5b8fe0"/>'
 '<path d="M-10 -26 q10 -24 20 0" fill="#3a2a1a"/><path d="M4 -34 a6 6 0 1 0 8 4" fill="none" stroke="#fff8c0" stroke-width="2.4"/><path d="M-6 -16 h3 M3 -16 h3"/><path d="M0 -22 v4" stroke="#c0392b"/>'
 '<path d="M-26 70 h52" stroke="#d9a066" stroke-width="5"/><path d="M-18 12 q-16 6 -12 22" fill="none" stroke="#5b8fe0" stroke-width="7"/></g>')
def SATI(x,y,s=1,rot=0): return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke="#111" stroke-width="2"><path d="M-40 0 q40 -14 80 0 q-40 12 -80 0z" fill="#c0392b"/><circle cx="-46" cy="-2" r="9" fill="#f2c79b"/><path d="M-55 -4 q-10 10 -4 24" fill="none" stroke="#2b1a0e" stroke-width="5"/><path d="M-30 4 h50" stroke="#e0a800" stroke-width="3"/></g>'
def CHAKRA(x,y,r=16): return f'<g transform="translate({x} {y})" stroke="#111" stroke-width="2"><circle r="{r}" fill="#ffd60a"/>'+''.join(f'<path d="M0 0 L{r*1.25*__import__("math").cos(k*0.785):.1f} {r*1.25*__import__("math").sin(k*0.785):.1f}" stroke="#e0a800" stroke-width="3"/>' for k in range(8))+f'<circle r="{r*0.35:.0f}" fill="#fff"/></g>'
STAR=''.join(f'<circle cx="{a}" cy="{b}" r="1.6" fill="#fff"/>' for a,b in ((40,20),(120,40),(500,30),(460,60),(300,14),(220,30),(380,22),(80,60)))