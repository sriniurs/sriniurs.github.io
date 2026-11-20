b=open('build9.py').read()
b=b.replace("first=V[0]['names'][0][0]; last=V[-1]['names'][-1][0]","first=V[0]['names'][0][0]; last='1000'\ndef rng(v): return 'THE CLOSING PRAYER' if v['names'][0][0]=='—' else f\"NAMES {v['names'][0][0]}–{v['names'][-1][0]}\"")
b=b.replace("""<h2 class="page-title">VERSE {v['n']} · NAMES {v['names'][0][0]}–{v['names'][-1][0]}</h2>""","""<h2 class="page-title">VERSE {v['n']} · {rng(v)}</h2>""")
b=b.replace("""<small>({v["names"][0][0]}–{v["names"][-1][0]})</small>""","""<small>({rng(v).replace("NAMES ","").title()})</small>""")
def rep(start,endmark,new):
    global b
    i=b.index(start); j=b.index(endmark,i); b=b[:i]+new+b[j:]
rep('<section class="page" id="foreword">','<section class="page" id="full">',open('f9.txt').read())
rep('<section class="page" id="howto">','<section class="page" id="contents">',open('h9.txt').read())
b=b.replace('<a href="#howto">The Lord in Nature</a>','<a href="#howto">The Lord’s Five Weapons</a>')
rep('  <div class="steps">\n    <div><b>Verses 82–84.','<div class="follow">',open('e9.txt').read())
open('build9.py','w').write(b)
