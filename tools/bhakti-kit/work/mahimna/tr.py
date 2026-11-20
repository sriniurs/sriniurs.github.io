V={'अ':'a','आ':'ā','इ':'i','ई':'ī','उ':'u','ऊ':'ū','ऋ':'ṛ','ॠ':'ṝ','ए':'e','ऐ':'ai','ओ':'o','औ':'au'}
M={'ा':'ā','ि':'i','ी':'ī','ु':'u','ू':'ū','ृ':'ṛ','ॄ':'ṝ','े':'e','ै':'ai','ो':'o','ौ':'au'}
C={'क':'k','ख':'kh','ग':'g','घ':'gh','ङ':'ṅ','च':'c','छ':'ch','ज':'j','झ':'jh','ञ':'ñ','ट':'ṭ','ठ':'ṭh','ड':'ḍ','ढ':'ḍh','ण':'ṇ','त':'t','थ':'th','द':'d','ध':'dh','न':'n','प':'p','फ':'ph','ब':'b','भ':'bh','म':'m','य':'y','र':'r','ल':'l','व':'v','श':'ś','ष':'ṣ','स':'s','ह':'h','ळ':'ḷ'}
D='०१२३४५६७८९'
def tr(s):
    o=[];i=0
    while i<len(s):
        ch=s[i]; nx=s[i+1] if i+1<len(s) else ''
        if ch in C:
            o.append(C[ch])
            if nx=='्': i+=2; continue
            if nx in M: o.append(M[nx]); i+=2; continue
            o.append('a'); i+=1; continue
        if ch in V: o.append(V[ch])
        elif ch=='ं': o.append('ṃ')
        elif ch=='ः': o.append('ḥ')
        elif ch=='ँ': o.append('m̐')
        elif ch=='ऽ': o.append("'")
        elif ch=='।': o.append('|')
        elif ch=='॥': o.append('‖')
        elif ch in D: o.append(str(D.index(ch)))
        else: o.append(ch)
        i+=1
    return ''.join(o)
import re,json
lines=open('dev.txt').read().strip().split('\n')
verses=[];cur=[]
for l in lines:
    t=tr(l).strip()
    t=re.sub(r'\s*\|$',' |',t)
    m=re.search(r'‖\s*(\d+)‖$',t)
    if m: t=t[:m.start()].rstrip()+f' ‖{m.group(1)}‖'; cur.append(t); verses.append(cur); cur=[]
    else: cur.append(t)
json.dump(verses,open('v.json','w'),ensure_ascii=False,indent=0)
for v in verses: print('\n'.join(v)); print()
