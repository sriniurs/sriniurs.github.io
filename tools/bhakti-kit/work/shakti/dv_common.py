exec(open('/home/claude/work/shakti/ps_common.py').read())
DVS='/bhakti/vishnu/dashavatara/'
TI='/bhakti/temples-of-india/'
# n, name, slug, form, yuga, one-line
DV=[(1,'Matsya','matsya','the fish','Satya','saves Manu, the seeds of life and the Vedas from the flood'),
    (2,'Kūrma','kurma','the tortoise','Satya','bears Mount Mandara as the ocean of milk is churned'),
    (3,'Varāha','varaha','the boar','Satya','lifts the Earth from the cosmic ocean and slays Hiraṇyākṣa'),
    (4,'Narasiṃha','narasimha','the man-lion','Satya','bursts from a pillar to save Prahlāda from Hiraṇyakaśipu'),
    (5,'Vāmana','vamana','the dwarf','Tretā','asks Bali for three steps and spans the worlds'),
    (6,'Paraśurāma','parashurama','Rāma with the axe','Tretā','the Brahmin warrior who humbles proud kings'),
    (7,'Rāma','rama','the prince of Ayodhyā','Tretā','the ideal king who defeats Rāvaṇa'),
    (8,'Balarāma · Buddha','balarama-buddha','the plough-bearer / the awakened one','Dvāpara · Kali','the disputed eighth place: Kṛṣṇa’s elder brother, or the Buddha'),
    (9,'Kṛṣṇa','krishna','the dark one','Dvāpara','the cowherd, the charioteer, the teacher of the Gītā'),
    (10,'Kalki','kalki','the rider on the white horse','Kali (future)','will end the dark age and begin a new one')]
def head_vis(title,desc): return _ct.make_head(title,desc)
def AV(n,x,y,s=1):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
    if n==1: return g+'<path d="M-40 0 q30 -26 60 0 q-30 26 -60 0z" fill="#3b8fd0"/><path d="M20 0 l18 -14 v28z" fill="#3b8fd0"/><circle cx="-26" cy="-4" r="3" fill="#fff"/><path d="M-10 -14 q4 14 0 28 M2 -14 q4 14 0 28" fill="none" stroke="#9fd0ea"/></g>'
    if n==2: return g+'<ellipse cy="0" rx="38" ry="22" fill="#5a8a3a"/><path d="M-20 -14 l12 10 l14 -10 l12 10" fill="none" stroke="#3a5a2a"/><circle cx="44" cy="2" r="9" fill="#8ab070"/><path d="M-30 18 l-6 8 M30 18 l6 8 M-20 20 v8 M20 20 v8" stroke="#8ab070" stroke-width="5"/></g>'
    if n==3: return g+'<path d="M-34 14 q-4 -34 26 -36 q30 0 34 22 l12 4 l-12 6 q-6 6 -30 6z" fill="#5a4a4a"/><path d="M28 -6 q8 -8 2 -16" fill="none" stroke="#fff" stroke-width="3"/><path d="M-26 14 v10 M14 14 v10" stroke-width="5"/><circle cx="16" cy="-10" r="2.4" fill="#fff"/><circle cx="-6" cy="-36" r="12" fill="#5ab0f0"/></g>'
    if n==4: return g+'<path d="M-24 34 q-4 -40 24 -48 q28 8 24 48z" fill="#e0a800"/><circle cy="-24" r="20" fill="#e0a800"/><path d="M-20 -30 q-10 -16 6 -24 q14 -6 28 4 q14 10 6 26" fill="#c06a1a"/><circle cx="-7" cy="-26" r="2.6" fill="#111"/><circle cx="7" cy="-26" r="2.6" fill="#111"/><path d="M-8 -14 q8 6 16 0" fill="none"/></g>'
    if n==5: return g+'<path d="M-14 30 q-2 -26 14 -30 q16 4 14 30z" fill="#ffd60a"/><circle cy="-14" r="11" fill="#f2c79b"/><path d="M-26 -30 q26 -20 52 0z" fill="#e8d8b0"/><path d="M0 -30 v26" stroke-width="2"/><path d="M14 10 h10 v14 h-10z" fill="#c9a26b"/></g>'
    if n==6: return g+'<path d="M-16 34 q-2 -36 16 -40 q18 4 16 40z" fill="#e05a3a"/><circle cy="-16" r="11" fill="#c98b5a"/><path d="M-8 -26 q8 -10 16 0" fill="#3a2a1a"/><path d="M20 -36 v60" stroke="#7a4a1a" stroke-width="5"/><path d="M20 -36 q22 4 20 22 q-12 -4 -20 -4z" fill="#ccc"/></g>'
    if n==7: return g+'<path d="M-16 34 q-2 -36 16 -40 q18 4 16 40z" fill="#3b8fd0"/><circle cy="-16" r="11" fill="#5b8fe0"/><path d="M-10 -26 h20 l-3 -10 h-14z" fill="#e0a800"/><path d="M-30 -30 q-14 30 0 60" fill="none" stroke="#7a4a1a" stroke-width="4"/><path d="M-30 -30 v60" stroke="#bbb" stroke-width="1"/></g>'
    if n==8: return g+'<path d="M-16 34 q-2 -36 16 -40 q18 4 16 40z" fill="#f4f4f4"/><circle cy="-16" r="11" fill="#f2e6d0"/><path d="M20 -30 v52 M14 22 h14 l-4 8z" stroke="#7a4a1a" stroke-width="4"/><path d="M-36 30 q-4 -20 -24 -26 M-60 6 q10 -14 22 -10" fill="none" stroke="#e08a2a" stroke-width="2"/></g>'
    if n==9: return g+'<path d="M-16 34 q-2 -36 16 -40 q18 4 16 40z" fill="#ffd60a"/><circle cy="-16" r="11" fill="#3b6fd0"/><path d="M2 -30 q10 -16 18 -6 q-8 2 -18 6z" fill="#2a9d6f"/><circle cx="16" cy="-30" r="3" fill="#3b8fd0"/><path d="M-30 -6 l44 -10" stroke="#7a4a1a" stroke-width="4"/></g>'
    return g+'<path d="M-34 10 q-2 -24 26 -26 q22 0 30 -14 l6 8 l-4 6 q2 18 -16 26z" fill="#f4f4f4"/><path d="M-28 10 v18 M-8 12 v16 M10 10 v18" stroke="#f4f4f4" stroke-width="6"/><circle cx="-4" cy="-30" r="9" fill="#c98b5a"/><path d="M4 -34 l30 -26" stroke="#ccc" stroke-width="4"/></g>'
def VISHNU(x,y,s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 50 q-4 -54 30 -66 q34 12 30 66z" fill="#ffd60a"/>'
     '<path d="M-22 -8 l-26 -20 M22 -8 l26 -20 M-22 6 l-24 10 M22 6 l24 10" stroke="#3b6fd0" stroke-width="7"/>'
     '<circle cx="-52" cy="-30" r="9" fill="#fff8e7"/><circle cx="52" cy="-30" r="9" fill="none" stroke="#e0a800" stroke-width="4"/><path d="M-48 16 v18" stroke="#7a4a1a" stroke-width="5"/><circle cx="48" cy="18" r="6" fill="#f08aa6"/>'
     '<circle cy="-36" r="15" fill="#3b6fd0"/><path d="M-14 -48 h28 l-4 -18 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/><path d="M-3 -46 v-6 M3 -46 v-6" stroke="#fff" stroke-width="2"/>'
     '<circle cx="-5" cy="-38" r="2.4" fill="#fff"/><circle cx="5" cy="-38" r="2.4" fill="#fff"/><path d="M-6 -29 q6 5 12 0" fill="none"/></g>')
def OCEAN(W=560,H=60,y=0,c='#3b8fd0'): return f'<rect y="{y}" width="{W}" height="{H}" fill="{c}"/>'+''.join(f'<path d="M{i*40} {y+10} q20 -10 40 0" stroke="#9fd0ea" stroke-width="2" fill="none"/>' for i in range(W//40+1))
def series_note_dv(n):
    prev = (f' Previous: <a href="{DVS}{DV[n-2][2]}/">{DV[n-2][1]}</a>.' if n>1 else f' Previous: <a href="{DVS}overview/">Overview</a>.') if n else ''
    nxt = f' Next: <a href="{DVS}{DV[n][2]}/">{DV[n][1]}</a>.' if n<10 else ''
    return f'<div class="panel reading small"><p>Part of <a href="{DVS}">Daśāvatāra</a>, the ten avatāras of Viṣṇu.{prev}{nxt}</p></div>'
def cover_dv(burst,h1,size,tag,art):
    return cover(burst,h1,size,tag,art).replace('PAÑCABHŪTA STHALAS · A REFERENCE GUIDE','DAŚĀVATĀRA · A REFERENCE GUIDE')
def foreword_dv(say,paras,q,a,note):
    return foreword(say,paras,q,a,note).replace('color:#0b2a4a','color:#0d3f73')
