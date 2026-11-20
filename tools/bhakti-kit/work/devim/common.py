import re,sys,math
sys.path.insert(0,'/home/claude/work/purusha')
from pdata import talk,svg,person,F,SUN,lab,crowd,MOON,STARS,FIRE
R='#fde4e4'
def make_head(title,desc,extra=''):
    src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
    head=src[:src.find('<div class="book">')]
    css,rest=head[:head.find('</style>')],head[head.find('</style>'):]
    for a,b in [('#1d6fb8','#c0392b'),('#1d4f9a','#a02a1f'),('#0b2a4a','#3a1414'),('#2c5f9e','#d9822b'),('#dfe9f6','#fde4e4'),('#e3f2fd','#fdecea'),('#8fd0f5','#ffd27a'),('#0b3d6e','#6e1a0b'),('#5b6f8a','#8a5b5b'),('#04101f','#1f0604')]: css=css.replace(a,b)
    head=css+rest
    head=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',head)
    head=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',head)
    head=head.replace('</style>','''  .iast .cl2{padding-left:2.2em}
  .full .ln2{padding-left:2.2em}
  .full p{margin:0 0 6px}
  .pt{font-size:14.5px;line-height:1.45;margin:8px 0}
  .toc.tight{gap:5px;grid-template-columns:repeat(3,1fr)}.toc.tight li{padding:3px 8px;font-size:13px}.toc.tight .part{font-size:16px}
  .vfig svg{max-height:150px;width:auto}
  .g3{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:8px 0}
  .g3 .tile{border:3px solid var(--ink);background:#fff;padding:6px;box-shadow:3px 3px 0 var(--ink);text-align:center}
  .g3 .tile svg{width:100%;max-width:150px;height:auto;display:block;margin:0 auto}
  .g3 .tile h4{margin:4px 0 0;font-family:Bangers,Impact,sans-serif;letter-spacing:1px;font-size:17px;color:var(--red)}
  .g3 .tile .nt2{font-size:11px;font-weight:bold;margin:0}
  .g3 .tile p{margin:2px 0 0;font-size:12.5px;line-height:1.35}
  @media(max-width:720px){.iast .cl2{padding-left:1.4em}.full .ln2{padding-left:1.4em}.g3{grid-template-columns:repeat(2,1fr)}}
'''+extra+'</style>',1)
    return head
def tail():
    src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
    return src[src.find('<script>\n  document.querySelectorAll'):]
FOLLOW='<div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>'
CAST='''<div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>'''
def DEVI(x=110,y=0,s=1,arms=True,sari='#c0392b',skin='#f2c79b',hair='#151515'):
    a=(f'<path d="M-24 76 q-30 -6 -42 -30" fill="none" stroke="{skin}" stroke-width="7"/><path d="M24 76 q30 -6 42 -30" fill="none" stroke="{skin}" stroke-width="7"/>'
       f'<path d="M-24 92 q-34 4 -46 22" fill="none" stroke="{skin}" stroke-width="7"/><path d="M24 92 q34 4 46 22" fill="none" stroke="{skin}" stroke-width="7"/>'
       '<path d="M-66 46 v-26" stroke="#7a5a3a" stroke-width="3"/><path d="M-72 22 l6 -12 l6 12 M-66 10 v-6" stroke="#ccc" stroke-width="3" fill="none"/>'
       '<circle cx="70" cy="114" r="8" fill="#fff" stroke="#111" stroke-width="2"/>'
       '<path d="M60 40 h14" stroke="#111" stroke-width="2"/><circle cx="66" cy="40" r="9" fill="none" stroke="#e0a800" stroke-width="4"/>') if arms else ''
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2.2">'+a+
     '<path d="M-14 26 h28 l-4 -18 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#ffd60a"/>'
     f'<path d="M-17 36 q-6 30 4 40 M17 36 q6 30 -4 40" fill="{hair}"/>'
     f'<circle cy="42" r="15" fill="{skin}"/><circle cy="36" r="2" fill="#c0392b" stroke="none"/>'
     f'<path d="M-30 150 q-6 -70 30 -88 q36 18 30 88z" fill="{sari}"/><path d="M-26 110 q26 -16 52 0" fill="none" stroke="#ffd60a" stroke-width="4"/></g>')
LION=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-30" y="-14" width="56" height="26" rx="12" fill="#e0a800"/><circle cx="32" cy="-14" r="15" fill="#c46a1a"/><circle cx="34" cy="-14" r="9" fill="#e0a800"/><path d="M-30 -6 q-14 -6 -12 -20" fill="none"/></g>'
HILLS='<path d="M0 120 L40 70 L70 96 L110 50 L150 92 L180 64 L220 104 V160 H0Z" fill="#dfe9f6" stroke="#111" stroke-width="2"/><path d="M100 62 l10 -12 l10 12 M170 74 l10 -10 l8 10" stroke="#fff" stroke-width="4" fill="none"/>'
T=lambda x,y,t,s=12,c='#111': f'<text x="{x}" y="{y}" text-anchor="middle" {F} font-size="{s}" fill="{c}">{t}</text>'
def MOUNT(kind,x,y,s=1,c=None):
    g=f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
    body=lambda col,head='': f'<rect x="-26" y="-12" width="50" height="22" rx="10" fill="{col}"/>'+head+'<path d="M-18 10 v10 M14 10 v10" stroke="#111" stroke-width="3"/>'
    if kind=='bull': g+=body(c or '#fff','<circle cx="28" cy="-12" r="10" fill="'+(c or '#fff')+'"/><path d="M24 -20 l-4 -8 M32 -20 l4 -8" stroke="#111" stroke-width="2"/>')
    elif kind=='lion': g+=body('#e0a800','<circle cx="28" cy="-12" r="12" fill="#c46a1a"/><circle cx="30" cy="-12" r="7" fill="#e0a800"/>')
    elif kind=='tiger': g+=body('#ff8c1a','<circle cx="28" cy="-12" r="10" fill="#ff8c1a"/>')+''.join(f'<path d="M{-18+k*10} -12 v10" stroke="#111" stroke-width="2"/>' for k in range(4))
    elif kind=='donkey': g+=body('#888','<circle cx="28" cy="-10" r="9" fill="#888"/><path d="M24 -18 l-2 -12 M30 -18 l2 -12" stroke="#111" stroke-width="3"/>')
    elif kind=='elephant': g+='<rect x="-28" y="-20" width="54" height="30" rx="12" fill="#bbb"/><circle cx="26" cy="-14" r="14" fill="#bbb"/><path d="M36 -8 q8 12 0 22" fill="none" stroke="#111" stroke-width="5"/><path d="M-18 10 v10 M14 10 v10" stroke="#111" stroke-width="4"/>'
    elif kind=='buffalo': g+=body('#333','<circle cx="28" cy="-10" r="10" fill="#333"/><path d="M20 -16 q-6 -10 2 -12 M36 -16 q6 -10 -2 -12" stroke="#ccc" stroke-width="3" fill="none"/>')
    elif kind=='garuda': g+='<path d="M-30 -6 q30 -26 60 0 q-30 -6 -60 0z" fill="#e0a800"/><circle cy="-16" r="8" fill="#c0392b"/><path d="M6 -16 l8 2 l-8 3z" fill="#ffd60a"/>'
    elif kind=='peacock': g+='<path d="M-30 0 q0 -30 24 -30 q-4 14 6 30z" fill="#2a9d6f"/>'+''.join(f'<circle cx="{-22+k*6}" cy="{-20+(k%2)*6}" r="2.5" fill="#3b6fd0"/>' for k in range(4))+'<ellipse cx="8" cy="-4" rx="10" ry="7" fill="#1d6fb8"/><path d="M14 -10 q4 -12 0 -18" stroke="#1d6fb8" stroke-width="4" fill="none"/>'
    elif kind=='swan': g+='<ellipse cx="0" cy="0" rx="24" ry="10" fill="#fff"/><path d="M18 -2 q8 -26 -2 -26" fill="none" stroke="#111" stroke-width="5"/><path d="M18 -2 q8 -26 -2 -26" fill="none" stroke="#fff" stroke-width="3"/><path d="M-4 -28 l-6 2 l6 2z" fill="#ff8c1a"/>'
    elif kind=='lotus': g+='<path d="M0 10 q-30 -6 -26 -20 q14 0 26 20 q12 -20 26 -20 q4 14 -26 20z" fill="#f08aa6"/><path d="M0 10 q-8 -16 0 -30 q8 14 0 30z" fill="#ffc2dc"/>'
    elif kind=='corpse': g+='<rect x="-30" y="-6" width="60" height="12" rx="6" fill="#d9d9d9"/><circle cx="-34" cy="0" r="7" fill="#d9d9d9"/>'
    return g+'</g>'
def MINI(sari='#c0392b',skin='#f2c79b',mount=None,mc=None,sym=''):
    m=MOUNT(mount,60,92,.8,mc) if mount else ''
    return f'<svg viewBox="0 0 120 110" role="img" aria-hidden="true"><rect width="120" height="110" fill="#fff8ec"/>{m}{DEVI(60,-2,.5,False,sari,skin)}{sym}</svg>'
def iast(lines): return '<div class="iast">'+''.join(f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>' for a,b in lines)+'</div>'
def fp(lab,lines):
    o=f'<p><span class="vn">{lab}</span>'
    for a,b in lines:
        b=re.sub(r'\s*‖([\w–]+)‖$',r'<span class="end">‖ \1 ‖</span>',b)
        o+=f'<span class="ln">{a}</span><span class="ln ln2">{b}</span>'
    return o+'</p>'
def vpage(v):
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in v['words'])
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    plain=f'\n    <div class="plain">{v["plain"]}</div>' if v.get('plain') else ''
    tk=f"\n  {talk(*v['talk'])}" if v.get('talk') else ''
    return f'''<section class="page" id="v{v['n']}">
  <h2 class="page-title">{v.get('lab','VERSE '+v['n'])}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(v['lines'])}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>{plain}
    {'<table class="ct"><tr><th>Word</th><th>Means</th></tr>'+words+'</table>' if words else ''}
  </div>
  <div class="panel reading pt">{v['point']}</div>{tk}
  <div class="key">{v['key']}</div>{note}
</section>
'''
SERIES=[('1','Devī Kavacam I','The Nine Durgās and the Mothers'),('2','Devī Kavacam II','Armour for every limb'),('3','Argalā Stotram','“Rūpaṃ dehi, jayaṃ dehi”'),('4','Kīlakam','The pin that unlocks the text'),('5','The Frame','Suratha, Samādhi and the sage'),
 ('6','Chapter 1','Madhu and Kaiṭabha'),('7','Chapter 2','The Goddess is born'),('8','Chapter 3','Mahiṣāsura slain'),('9','Chapter 4','The Śakrādi stuti'),('10','Chapter 5','“Yā devī sarvabhūteṣu”'),
 ('11','Chapter 6','Dhūmralocana'),('12','Chapter 7','Caṇḍa, Muṇḍa and Cāmuṇḍā'),('13','Chapter 8','Raktabīja'),('14','Chapter 9','Niśumbha'),('15','Chapter 10','Śumbha'),
 ('16','Chapter 11','The Nārāyaṇī stuti'),('17','Chapter 12','The fruits of reciting'),('18','Chapter 13','The boons'),('19','The Closing','The three rahasyas')]
