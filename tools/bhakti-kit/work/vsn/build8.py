import re,sys
sys.path.insert(0,'.')
from d8 import V
from d1 import talk,person,F,BHISMA,VIS,K
src=open('Vishnu_Sahasranama_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=head.replace('Part 1 · The Opening · srini.presents','Part 8 · Names 765–885 · srini.presents')
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 8: verses 82–94, names 765–885 (caturmūrtiś caturbāhuḥ…), each name explained in plain English with illustrations.">',head)
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
  <div class="burst yel">PART 8 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 8 · VERSES 82–94 · NAMES {first}–{last}</div>
  <div class="tag">"Caturmūrtiś caturbāhuḥ" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First verses 82–94 for chanting in one go. Then <b>one page for each verse</b>: the chant, a picture, every name with its number and meaning, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">PREVIOUSLY · AND NOW</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Part 7</b>, names 633–764: Keśava and Hari, the hymn that praises itself, name 700, one and many, form and formless, and the Lord without pride who gives honour.</p>
    <p><b>Part 8</b> covers verses 82–94, names {first} to {last}. Here are the "four" names, "hard to reach" and "easy to reach", the thread on which the worlds are strung, Sundara the beautiful, name 800, the rain cloud, the sacred trees, smaller than an atom and greater than the universe, the bearer of our burden, and the sun.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Hard to reach AND easy to reach?","Name 777 and name 817! The difference, say the commentators, is love.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 82–94 IN ONE GO</h2>
  <div class="sub">For chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Text checked word by word against shlokam.org. Name numbers follow its list.</div>
</section>

<section class="page" id="howto">
  <h2 class="page-title">THE LORD IN NATURE</h2>
  <div class="sub">Look around: He is in what you see</div>
  <table class="ct">
    <tr><th>In nature</th><th>Name</th><th>No.</th></tr>
    <tr><td>The thread of a garland</td><td><b>Sutantu</b></td><td>784</td></tr>
    <tr><td>A deep, calm lake</td><td><b>Mahāhrada</b></td><td>803</td></tr>
    <tr><td>The jasmine flower</td><td><b>Kunda</b></td><td>809</td></tr>
    <tr><td>The monsoon rain cloud</td><td><b>Parjanya</b></td><td>810</td></tr>
    <tr><td>The wind</td><td><b>Anila</b></td><td>812</td></tr>
    <tr><td>Banyan, fig and peepal trees</td><td><b>Nyagrodha · Udumbara · Aśvattha</b></td><td>822–824</td></tr>
    <tr><td>Fire with seven tongues</td><td><b>Saptajihva</b></td><td>827</td></tr>
    <tr><td>The atom and the cosmos</td><td><b>Aṇu · Bṛhat</b></td><td>835–836</td></tr>
    <tr><td>The sun</td><td><b>Ravi · Sūrya · Savitā</b></td><td>881–884</td></tr>
  </table>
  {talk("So I can chant these names just by looking around?","Exactly! The rain, the trees, the sun: each is a reminder of one of His names.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Previously, and Now</a></li>
    <li><span class="num">🔤</span><a href="#full">Verses 82–94 in One Go</a></li>
    <li><span class="num">ℹ</span><a href="#howto">The Lord in Nature</a></li>
    <li><span class="num">∑</span><a href="#end">Part 8 on One Page</a></li>
    <li class="part">VERSES 82–94 · NAMES {first}–{last}</li>
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
  <h2 class="page-title">PART 8 ON ONE PAGE</h2>
  <div class="sub">Names {first}–{last} in five lines</div>
  <div class="steps">
    <div><b>Verses 82–84.</b> Four, four, four, and the world only one quarter of Him; hard to reach without love; the thread of the worlds.</div>
    <div><b>Verses 85–87.</b> Sundara, the beautiful; name 800, the golden drop and the great lake; the rain cloud.</div>
    <div><b>Verses 88–89.</b> Easy to reach for the loving; the sacred trees; fire, sun and the remover of fear.</div>
    <div><b>Verses 90–92.</b> Smaller than an atom, greater than all; bearer of our burden; the archer who disciplines with patience.</div>
    <div><b>Verses 93–94.</b> He makes love grow; the sun, Savitā of the Gāyatrī.</div>
  </div>
  {talk("Which name stays with you?","Bhārabhṛt, name 847: He carries our burden.")}
  <div class="key">Names {first}–{last}: <b>hard to reach, easy to reach, carrying our burden</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, verses 82–94, names {first}–{last}. Text checked word by word against shlokam.org; name numbers follow its list. Meanings are our own plain-English renderings of the commonly given explanations, mostly Śaṅkara's; where Śaṅkara and Parāśara Bhaṭṭar differ, this is noted. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part8.html','w').write(head+''.join(b)+tail)
