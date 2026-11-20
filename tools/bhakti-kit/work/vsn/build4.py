import re,sys
sys.path.insert(0,'.')
from d4 import V
from d1 import talk,person,F,BHISMA,VIS,K
src=open('Vishnu_Sahasranama_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=head.replace('Part 1 · The Opening · srini.presents','Part 4 · Names 256–372 · srini.presents')
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 4: verses 28–40, names 256–372 (vṛṣāhī vṛṣabho viṣṇuḥ…), each name explained in plain English with illustrations.">',head)
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
  <div class="burst yel">PART 4 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 4 · VERSES 28–40 · NAMES {first}–{last}</div>
  <div class="tag">"Vṛṣāhī vṛṣabho viṣṇuḥ" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First verses 28–40 for chanting in one go. Then <b>one page for each verse</b>: the chant, a picture, every name with its number and meaning, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">PREVIOUSLY · AND NOW</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Part 3</b>, names 133–255: the fourfold Lord, Vāmana, the healer, the mountain-lifter, Śrīnivāsa and Govinda, the lion (200), the Cosmic Person and Nārāyaṇa.</p>
    <p><b>Part 4</b> covers verses 28–40, names {first} to {last}. Themes here: dharma as His body, the Lord as medicine and bridge, desire ended and fulfilled, the peacock-feathered Kṛṣṇa, Vāsudeva, the ferryman across saṃsāra, and Dāmodara, bound by a mother's love.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Some names come back again?","Yes: Viṣṇu, Acyuta, Padmanābha and Mahīdhara all return here. The commentators always find a new sense the second time.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 28–40 IN ONE GO</h2>
  <div class="sub">For chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Text checked word by word against shlokam.org. Name numbers follow its list.</div>
</section>

<section class="page" id="howto">
  <h2 class="page-title">THREE THREADS IN THIS PART</h2>
  <div class="sub">What to listen for in verses 28–40</div>
  <div class="steps">
    <div><b>Dharma (vṛṣa).</b> Verse 28 uses "vṛṣa", the bull of dharma, five times: dharma is not a rule outside the Lord but His very body and steps.</div>
    <div><b>Healing.</b> After Vaidya the physician (164), He is now Auṣadham, the medicine (287), and Setu, the bridge (288): cure and crossing for the disease of saṃsāra.</div>
    <div><b>Desire (kāma).</b> Verse 32 holds five names on desire: He ends it, fulfils it, gives it, and is Himself the beloved we most desire.</div>
    <div><b>Kṛṣṇa of Vṛndāvana.</b> Śikhaṇḍī, the peacock feather (311); Śauri (340); and Dāmodara (367), tied to a mortar by Yaśodā.</div>
    <div><b>Repeats.</b> Viṣṇu (258), Acyuta (318), Padmanābha (346), Mahīdhara (317, 369), Vāsudeva (332, again at 695 and 709): each time with a fresh meaning.</div>
  </div>
  {talk("Why repeat names at all?","Because one meaning is never enough for the Lord. Each repeat opens another door.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Previously, and Now</a></li>
    <li><span class="num">🔤</span><a href="#full">Verses 28–40 in One Go</a></li>
    <li><span class="num">ℹ</span><a href="#howto">Three Threads in This Part</a></li>
    <li><span class="num">∑</span><a href="#end">Part 4 on One Page</a></li>
    <li class="part">VERSES 28–40 · NAMES {first}–{last}</li>
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
  <h2 class="page-title">PART 4 ON ONE PAGE</h2>
  <div class="sub">Names {first}–{last} in five lines</div>
  <div class="steps">
    <div><b>Verses 28–30.</b> Dharma is His body; He gives wealth and is wealth; moonbeam, sunlight and the sacred syllable.</div>
    <div><b>Verses 31–32.</b> The medicine and the bridge of the world; the Lord who ends, fulfils and is our deepest desire.</div>
    <div><b>Verses 33–35.</b> Maker of the ages, unseen yet seen; the peacock-feathered One who takes away anger; never careless with His own.</div>
    <div><b>Verses 36–38.</b> Vāsudeva, dwelling in all; the ferryman, ever favourable; the Lord in the lotus of the heart.</div>
    <div><b>Verses 39–40.</b> Beyond compare, always on time; Dāmodara, bound by love; the path itself.</div>
  </div>
  {talk("Which name stays with you?","Anukūla, name 342: ever favourable. The Lord is never against anyone.")}
  <div class="key">Names {first}–{last}: <b>from "dharma is His body" to "bound by love"</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, verses 28–40, names {first}–{last}. Text checked word by word against shlokam.org; name numbers follow its list. Meanings are our own plain-English renderings of the commonly given explanations, mostly Śaṅkara's; where Śaṅkara and Parāśara Bhaṭṭar differ, this is noted. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part4.html','w').write(head+''.join(b)+tail)
