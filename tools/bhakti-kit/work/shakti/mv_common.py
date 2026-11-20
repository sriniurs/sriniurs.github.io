exec(open('/home/claude/work/shakti/common_s.py').read())
MVS='/bhakti/devi/dasha-mahavidya/'
def BODY(x,y,s,skin,dress,fierce=False,extra=''):
    tongue='<path d="M-3 -24 q3 16 6 0z" fill="#e04040"/>' if fierce else '<path d="M-4 -22 q4 3 8 0" fill="none"/>'
    hair='<path d="M-16 -36 q-10 30 -6 50 M16 -36 q10 30 6 50" stroke="#111" stroke-width="5" fill="none"/>' if fierce else ''
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-24 60 q-2 -64 24 -72 q26 8 24 72z" fill="{dress}"/>{hair}'
     f'<path d="M-20 0 l-20 -18 M20 0 l20 -18" stroke="{skin}" stroke-width="6"/><circle cy="-30" r="13" fill="{skin}"/>'
     '<path d="M-12 -40 h24 l-4 -14 l-6 6 l-2 -10 l-2 10 l-6 -6z" fill="#e0a800"/><circle cx="-5" cy="-32" r="2.2" fill="#fff"/><circle cx="5" cy="-32" r="2.2" fill="#fff"/><circle cy="-39" r="1.8" fill="#c0392b"/>'
     +tongue+extra+'</g>')
SKULLS='<path d="M-20 -10 q20 30 40 0" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="3 4"/>'
SWORD='<path d="M40 -18 l14 -30" stroke="#bbb" stroke-width="4"/>'
def MV(n,x,y,s=1):
    if n==1: return BODY(x,y,s,'#1a1a2a','#1a1a2a',True,SKULLS+SWORD+'<circle cx="-42" cy="-20" r="6" fill="#2a2a3a"/>')
    if n==2: return BODY(x,y,s,'#3b4fa0','#c9a26b',True,SKULLS+'<path d="M40 -18 l10 -10 l4 6 z" fill="#bbb"/><path d="M-20 30 h40" stroke="#e0a800" stroke-width="4" stroke-dasharray="4 4"/>')
    if n==3: return BODY(x,y,s,'#f2a07a','#c0392b',False,'<path d="M-42 -40 q-10 22 0 44" stroke="#2a9d6f" stroke-width="4" fill="none"/><path d="M40 -18 l4 -20 l6 4" stroke="#e0a800" stroke-width="3" fill="none"/>')
    if n==4: return BODY(x,y,s,'#f2c070','#e0115f',False,'<path d="M-4 -56 a8 8 0 1 0 10 4" fill="none" stroke="#fff8c0" stroke-width="2.5"/><circle cx="-40" cy="-18" r="7" fill="none" stroke="#e0a800" stroke-width="3"/>')
    if n==5: return BODY(x,y,s,'#e05a3a','#a01a1a',True,'<circle cx="-40" cy="-18" r="7" fill="none" stroke="#fff" stroke-dasharray="2 2"/><rect x="34" y="-28" width="14" height="10" fill="#e8d8a8"/>')
    if n==6: return BODY(x,y,s,'#e05a3a','#c0392b',True,'<circle cx="40" cy="-30" r="9" fill="#e05a3a"/><path d="M0 -44 q-10 -30 -14 -40 M0 -44 q0 -30 0 -40 M0 -44 q10 -30 14 -40" stroke="#c0392b" stroke-width="3" fill="none"/>')
    if n==7: return BODY(x,y,s,'#9a9a9a','#f2f2f2',False,'<path d="M-46 -14 q6 -10 14 -2 q-6 10 -14 2z" fill="#c9a26b"/><path d="M40 -20 l8 -6 l6 4 l-6 4z" fill="#111"/>')
    if n==8: return BODY(x,y,s,'#f2d040','#ffd60a',False,'<path d="M40 -18 l12 -28" stroke="#7a5a2a" stroke-width="6"/><path d="M-40 -18 q-10 4 -14 14" stroke="#c0392b" stroke-width="3" fill="none"/>')
    if n==9: return BODY(x,y,s,'#2a9d6f','#c0392b',False,'<path d="M-30 10 l60 -40" stroke="#7a5a2a" stroke-width="4"/><circle cx="-28" cy="12" r="7" fill="#c9a26b"/><path d="M44 -22 q8 -8 12 2 l-6 4z" fill="#2ac06f"/>')
    if n==10: return BODY(x,y,s,'#f2c070','#e0115f',False,'<path d="M-46 -26 q6 -14 12 0 q-6 6 -12 0z" fill="#f2a6c0"/><path d="M34 -26 q6 -14 12 0 q-6 6 -12 0z" fill="#f2a6c0"/>')
MVN=[(1,'Kālī','kali','time, death and transformation'),(2,'Tārā','tara','the saviour who carries across'),(3,'Tripurasundarī (Ṣoḍaśī)','tripurasundari','beauty of the three worlds'),
 (4,'Bhuvaneśvarī','bhuvaneshvari','queen of the worlds, space'),(5,'Bhairavī','bhairavi','fierce heat of tapas'),(6,'Chinnamastā','chinnamasta','the self-beheaded, life feeding life'),
 (7,'Dhūmāvatī','dhumavati','the smoky widow, emptiness'),(8,'Bagalāmukhī','bagalamukhi','the stopper of speech and foes'),(9,'Mātaṅgī','matangi','the outcaste Sarasvatī, speech and art'),(10,'Kamalā','kamala','the lotus Lakṣmī, abundance')]
