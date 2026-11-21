import json,re
V={'अ':'a','आ':'ā','इ':'i','ई':'ī','उ':'u','ऊ':'ū','ऋ':'ṛ','ॠ':'ṝ','ऌ':'ḷ','ए':'e','ऐ':'ai','ओ':'o','औ':'au'}
M={'ा':'ā','ि':'i','ी':'ī','ु':'u','ू':'ū','ृ':'ṛ','ॄ':'ṝ','ॢ':'ḷ','े':'e','ै':'ai','ो':'o','ौ':'au'}
C={'क':'k','ख':'kh','ग':'g','घ':'gh','ङ':'ṅ','च':'c','छ':'ch','ज':'j','झ':'jh','ञ':'ñ','ट':'ṭ','ठ':'ṭh','ड':'ḍ','ढ':'ḍh','ण':'ṇ','त':'t','थ':'th','द':'d','ध':'dh','न':'n','प':'p','फ':'ph','ब':'b','भ':'bh','म':'m','य':'y','र':'r','ल':'l','ळ':'ḻ','व':'v','श':'ś','ष':'ṣ','स':'s','ह':'h'}
O={'ॐ':'oṃ','ं':'ṃ','ः':'ḥ','ँ':'m̐','ऽ':'’','्':'','़':''}
D={c:str(i) for i,c in enumerate('०१२३४५६७८९')}
def tr(s):
    o=[];i=0
    while i<len(s):
        ch=s[i]
        if ch in C:
            o.append(C[ch]); nx=s[i+1] if i+1<len(s) else ''
            if nx=='्': i+=2; continue
            if nx in M: o.append(M[nx]); i+=2; continue
            o.append('a'); i+=1; continue
        if ch in V: o.append(V[ch])
        elif ch in O: o.append(O[ch])
        elif ch in D: o.append(D[ch])
        else: o.append(ch)
        i+=1
    return ''.join(o)
R=lambda a,b:(lambda z:z.replace(a,b))
FIX={(1,34):R('श्चशुराः','श्वशुराः'),(2,31):R('युद्धाछ्रेयो','युद्धाच्छ्रेयो'),(2,33):R('चैत्त्वम','चेत्त्वम'),
 (11,54):lambda z:z.replace('शक्यमहमेवं','शक्य अहमेवं').replace('दृष्टुं','द्रष्टुं'),(16,20):R('असुरीं','आसुरीं'),(17,23):R('तत्सदिति','ॐ तत्सदिति'),
 (17,25):R('मोक्षकाङ्क्षि।','मोक्षकाङ्क्षिभिः।'),(6,32):R('सः योगी','स योगी'),(4,29):R('प्राण प्राणे','प्राणं प्राणे'),
 (9,21):R('एव त्रयी','एवं त्रयी'),(11,21):R('सङ्घाः विशन्ति','सङ्घा विशन्ति'),(11,28):R('मुखाः द्रवन्ति','मुखा द्रवन्ति'),
 (14,23):R('इत्येव यो','इत्येवं यो'),(15,4):R('परिमार्गितव्य ','परिमार्गितव्यं '),(5,8):R('शृणवन्','शृण्वन्'),(11,54.5):0,(11,46):R('चक्रहस्त\n\nमिच्छामि','चक्रहस्तम्\n\nइच्छामि')}
raw=json.load(open('/home/claude/gita_src/data/verse.json'))
out={}
for x in raw:
    c,n=x['chapter_number'],x['verse_number']
    t=x['text'].replace('‍','').replace('‌','')
    t=re.sub(r'्ि([क-ह])',r'्\1ि',t).replace('श्रृ','शृ').replace('ृ़','ॄ').replace('़','')
    t=FIX.get((c,n),lambda z:z)(t)
    t=re.sub(r'[।॥|]+\s*[\d०-९]+\.[\d०-९]+\s*[।॥|]*','‖',t)
    t=re.sub(r'^(\s*(?:धृतराष्ट्र|सञ्जय|अर्जुन|श्री\s*भगवान्?|श्रीभगवान्?)\s*[उु]?वाच)',r'\1\n',t.strip())
    t=re.sub(r'\s{3,}','\n',t)
    t=tr(t)
    if c==13: n=n-1
    segs=[s.strip() for s in re.split(r'[\n।॥‖]+',t) if s.strip()]
    sp=[s.replace('bhagavānuvāca','bhagavān uvāca').replace('śrī bhagavān','śrībhagavān').replace('saṃjaya','sañjaya') for s in segs if s.endswith('uvāca') and len(s)<22]
    body=[s for s in segs if not (s.endswith('uvāca') and len(s)<22)]
    body=[b.replace('’’','’') for b in body]
    for k in range(len(body)-1):
        m=re.match(r'^([kgcjṭḍtdnpbmyrlvśṣsh])\1',body[k+1])
        if m and not body[k].endswith(' '): body[k]+=m.group(1); body[k+1]=body[k+1][1:]
        if re.match(r'^r[kgcjṭḍtdnpbmyvśṣsh]',body[k+1]): body[k]+='r'; body[k+1]=body[k+1][1:]
    out[f'{c}.{n}']=dict(sp=sp,body=body)
out['1.20']['body'].append('hṛṣīkeśaṃ tadā vākyamidamāha mahīpate')
out['1.21']['body']=[b for b in out['1.21']['body'] if not b.startswith('hṛṣīkeśaṃ')]
out['1.28']['sp']=[]; out['1.28']['mid']=[1,'arjuna uvāca']
import glob
for f in glob.glob('/home/claude/vs_src/slok/*.json'):
    y=json.load(open(f))
    if 'ध्यायः' in y['slok']:
        out[f"col{y['chapter']}"]=tr(re.sub(r'\|\|.*','',y['slok']).replace('\n',' ')).strip()
json.dump(out,open('gita_iast.json','w'),ensure_ascii=False,indent=0)
print(len(out))
for k in ['1.1','2.47','4.7','11.32','13.0','13.1','18.66','2.20','11.36']: print(k,out[k])
