exec(open('/home/claude/work/gita/gc.py').read())
_h=open('/home/claude/work/shakti/hn_common.py').read()
exec(_h[_h.index('def HANUMAN'):_h.index('def series_note_hn')])
exec(_h[_h.index('def RAMA'):_h.index('def MONKEY')])
HB='/bhakti/vishnu/hanuman/'
def HS(label,cap=None,right=None,extra='',rama=False,mace=True,fold=False,bg=B):
    fig=HANUMAN(58,112,.72,mace=mace,fold=fold)
    if rama: fig=RAMA(150,120,.62)+HANUMAN(58,118,.62,mace=False,fold=True)
    r=ICON(right) if right else ''
    c=BUBBLE(110,22,cap,max(80,len(cap)*7.2),10) if cap else ''
    return sc(label,extra+fig+r+c,bg)
def hymn(P,TXTH,num_label):
    """P like gita build2; TXTH dict n->list of lines; ch fixed 99"""
    for n,lines in TXTH.items(): TXT[f'99.{n}']={'body':lines,'sp':[]}
    P=dict(P,ch=99)
    build2(P)
    s=open(P['out']).read()
    for n in range(len(TXTH),0,-1):
        s=s.replace(f'ŚLOKA 99.{n} ·',f'{num_label(n)} ·').replace(f'ŚLOKA 99.{n}<',f'{num_label(n)}<').replace(f'↑ 99.{n}<',f'↑ {num_label(n)}<')
        s=s.replace(f'<span class="vn">99.{n}</span>',f'<span class="vn">{num_label(n)}</span>')
    s=s.replace('THE CHAPTER IN ONE GO','THE HYMN IN ONE GO').replace('CHAPTER 99 ON ONE PAGE','THE HYMN ON ONE PAGE').replace('Chapter 99:',P['short']+':')
    s=re.sub(r'Chapter 99, ślokas [^<]*',f'All {len(TXTH)} verses',s)
    if P.get('endnum'): s=re.sub(r'‖( ?)(\d+)( ?)‖',lambda m:'‖'+m.group(1)+P['endnum'](int(m.group(2)))+m.group(3)+'‖',s)
    open(P['out'],'w').write(s)
