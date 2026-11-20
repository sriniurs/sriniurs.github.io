import re,sys
sys.path.insert(0,'.')
from d5 import V
from d1 import talk,person,F,BHISMA,VIS,K
src=open('Vishnu_Sahasranama_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=head.replace('Part 1 · The Opening · srini.presents','Part 5 · Names 373–512 · srini.presents')
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 5: verses 41–54, names 373–512 (udbhavaḥ kṣobhaṇo devaḥ…), each name explained in plain English with illustrations.">',head)
head=head.replace('</style>','  .nt td.no{width:3em;text-align:center;font-weight:700;color:#1d6fb8}\n  .nt td{padding-top:3px;padding-bottom:3px}\n  .nm .vfig svg{max-height:140px;width:auto}\n</style>',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
def iast(v): return '<div class="iast">'+''.join(f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>' for a,b in v['lines'])+'</div>'
def full(v):
    o=f'<p><span class="vn">VERSE {v["n"]}</span>'
    for a,b in v['lines']:
        b=re.sub(r'\s*‖(\d+)‖$',r'<span class="end">‖ \1 ‖</span>',b)
        o+=f'<span class="ln">{a}</span><span class="ln ln2">{b}</span>'
    return o+'</p>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The four-armed Vishnu against a starry universe, with a garland of a thousand small flowers circling him">'
 '<rect x="20" y="10" width="340" height="250" rx="20" fill="#0b3d6e"/>'+''.join(f'<circle cx="{30+(k*67)%320}" cy="{20+(k*41)%230}" r="1.8" fill="#fff"/>' for k in range(40))
 +''.join(f'<circle cx="{190+120*__import__("math").cos(k*0.157)}" cy="{135+105*__import__("math").sin(k*0.157)}" r="5" fill="{["#f08aa6","#ffd60a","#fff"][k%3]}" stroke="#111" stroke-width=".8"/>' for k in range(40))
 +VIS(190,26,1.05)+'</svg>')
first=V[0]['names'][0][0]; last=V[-1]['names'][-1][0]
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 5 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 5 · VERSES 41–54 · NAMES {first}–{last}</div>
  <div class="tag">"Udbhavaḥ kṣobhaṇo devaḥ" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First verses 41–54 for chanting in one go. Then <b>one page for each verse</b>: the chant, a picture, every name with its number and meaning, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">PREVIOUSLY · AND NOW</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Part 4</b>, names 256–372: dharma as His body, the medicine and the bridge, the Lord who ends and fulfils desire, the peacock feather, Vāsudeva, the ferryman, and Dāmodara bound by love.</p>
    <p><b>Part 5</b> covers verses 41–54, names {first} to {last}, and passes the <b>halfway mark: name 500</b>. Here we meet Rāma (394), Oṃ (409), the Sudarśana discus and time itself, the good friend (460), Vatsala, the Lord with a mother's love (471), and Satyasandha, the One who always keeps His word (510).</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Halfway already?","Name 500 is in verse 53! And it's a lovely one: Bhoktā, the Lord who accepts every offering.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 41–54 IN ONE GO</h2>
  <div class="sub">For chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Text checked word by word against shlokam.org. Name numbers follow its list.</div>
</section>

<section class="page" id="howto">
  <h2 class="page-title">THE LORD AS A FRIEND</h2>
  <div class="sub">The tender names in verses 41–54</div>
  <div class="steps">
    <div><b>Neya (398).</b> No one leads Him (400), yet He lets Himself be led by His devotees' love: Kṛṣṇa as Arjuna's charioteer.</div>
    <div><b>Viśrāma (424).</b> After all the turning of time, He is the place where the tired soul rests.</div>
    <div><b>Anirviṇṇa (435).</b> He never tires of us, never gives up on us, however often we fall.</div>
    <div><b>Suhṛt (460) and Vatsala (471).</b> The good friend of all beings, with a mother cow's love that does not mind the dirt.</div>
    <div><b>Satyasandha (510).</b> True to His word: "My devotee never perishes" (Gītā 9.31).</div>
  </div>
  {talk("I thought the names would all be grand cosmic titles!","Many are. But tucked between them are names like these, which show a God who is close, patient and kind.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Previously, and Now</a></li>
    <li><span class="num">🔤</span><a href="#full">Verses 41–54 in One Go</a></li>
    <li><span class="num">ℹ</span><a href="#howto">The Lord as a Friend</a></li>
    <li><span class="num">∑</span><a href="#end">Part 5 on One Page</a></li>
    <li class="part">VERSES 41–54 · NAMES {first}–{last}</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title()} <small>({v["names"][0][0]}–{v["names"][-1][0]})</small></a></li>' for v in V)}
  </ul>
</section>
''']
for v in V:
    rows=''.join(f'<tr><td class="no">{n}</td><td class="w">{a}</td><td>{m}</td></tr>' for n,a,m in v['names'])
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    b.append(f'''<section class="page nm" id="v{v['n']}">
  <h2 class="page-title">VERSE {v['n']} · NAMES {v['names'][0][0]}–{v['names'][-1][0]}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(v)}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>
    <table class="ct nt"><tr><th>No.</th><th>Name</th><th>Means</th></tr>{rows}</table>
  </div>
  <div class="panel reading pt">{v['point']}</div>
  <div class="key">{v['key']}</div>{note}
</section>
''')
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">PART 5 ON ONE PAGE</h2>
  <div class="sub">Names {first}–{last} in five lines</div>
  <div class="steps">
    <div><b>Verses 41–43.</b> The hidden cause in the cave of the heart; Dhruva's fixed place; Rāma, whom love can lead.</div>
    <div><b>Verses 44–46.</b> Oṃ itself; Sudarśana, time, and rest at its end; the imperishable seed that seeks nothing.</div>
    <div><b>Verses 47–48.</b> The tireless hub of the stars; the worship and the knowledge it leads to.</div>
    <div><b>Verses 49–51.</b> The good friend; a mother's love; being and becoming, all He.</div>
    <div><b>Verses 52–54.</b> The great God of gods; name 500, who accepts every offering; the Lord who keeps His word.</div>
  </div>
  {talk("Which name stays with you?","Anirviṇṇa, name 435: He never tires of us.")}
  <div class="key">Names {first}–{last}: <b>past the halfway mark, a God who is our friend</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, verses 41–54, names {first}–{last}. Text checked word by word against shlokam.org; name numbers follow its list. Meanings are our own plain-English renderings of the commonly given explanations, mostly Śaṅkara's; where Śaṅkara and Parāśara Bhaṭṭar differ, this is noted. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part5.html','w').write(head+''.join(b)+tail)
