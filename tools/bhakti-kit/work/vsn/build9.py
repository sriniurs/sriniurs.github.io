import re,sys
sys.path.insert(0,'.')
from d9 import V
from d1 import talk,person,F,BHISMA,VIS,K
src=open('Vishnu_Sahasranama_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=head.replace('Part 1 · The Opening · srini.presents','Part 9 · Names 886–1000 · srini.presents')
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 9: verses 95–108, names 886–1000, the last of the thousand names, ending with sarvapraharaṇāyudhaḥ, each name explained in plain English with illustrations.">',head)
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
first=V[0]['names'][0][0]; last='1000'
def rng(v): return 'THE CLOSING PRAYER' if v['names'][0][0]=='—' else f"NAMES {v['names'][0][0]}–{v['names'][-1][0]}"
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 9 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 9 · VERSES 95–108 · NAMES {first}–{last}</div>
  <div class="tag">"Ananto hutabhug bhoktā" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First verses 95–108 for chanting in one go. Then <b>one page for each verse</b>: the chant, a picture, every name with its number and meaning, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">PREVIOUSLY · AND NOW</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Part 8</b>, names 765–885: hard to reach and easy to reach, the thread of the worlds, Sundara, name 800, the rain cloud, the bearer of our burden, and the sun.</p>
    <p><b>Part 9</b> completes the thousand: verses 95–107, names {first} to 1000, and the closing prayer, verse 108. Here are the Wonderful, name 900 and the names of well-being, the One beyond words, the best of the forgiving, the destroyer of bad dreams, Lakṣmī among the names, fourteen names of sacrifice, Devakī's joy, and finally His weapons, ending with name 1000.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("We actually reach 1000?","Name 1000 is in verse 107: Sarvapraharaṇāyudha, 'whose weapons are all things'. Then verse 108 gathers it all into one prayer.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 95–108 IN ONE GO</h2>
  <div class="sub">For chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Text checked word by word against shlokam.org. Name numbers follow its list.</div>
</section>

<section class="page" id="howto">
  <h2 class="page-title">THE LORD'S FIVE WEAPONS</h2>
  <div class="sub">How the thousand names end</div>
  <table class="ct">
    <tr><th>Weapon</th><th>Name</th><th>What it stands for</th></tr>
    <tr><td><b>Pāñcajanya</b>, the conch</td><td>Śaṅkhabhṛt (993)</td><td>The call of dharma; the sacred sound</td></tr>
    <tr><td><b>Nandaka</b>, the sword</td><td>Nandakī (994)</td><td>Knowledge that cuts ignorance</td></tr>
    <tr><td><b>Sudarśana</b>, the discus</td><td>Cakrī (995)</td><td>The wheel of time; the mind</td></tr>
    <tr><td><b>Śārṅga</b>, the bow</td><td>Śārṅgadhanvā (996)</td><td>The senses, held in control</td></tr>
    <tr><td><b>Kaumodakī</b>, the mace</td><td>Gadādhara (997)</td><td>Strength; the intellect</td></tr>
  </table>
  <div class="panel reading" style="margin-top:10px"><p><b>Symbols.</b> The meanings in the last column are traditional readings that link each weapon to a power of the mind and cosmos; texts differ in the details. Then name 1000 says the rest: <i>everything</i> is His weapon to protect us.</p></div>
  {talk("Why end a thousand names with weapons?","Because the hymn began with 'what frees us from fear?'. It ends: nothing can stop Him from protecting you.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Previously, and Now</a></li>
    <li><span class="num">🔤</span><a href="#full">Verses 95–108 in One Go</a></li>
    <li><span class="num">ℹ</span><a href="#howto">The Lord’s Five Weapons</a></li>
    <li><span class="num">∑</span><a href="#end">Part 9 on One Page</a></li>
    <li class="part">VERSES 95–108 · NAMES {first}–{last}</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title()} <small>({rng(v).replace("NAMES ","").title()})</small></a></li>' for v in V)}
  </ul>
</section>
''']
for v in V:
    rows=''.join(f'<tr><td class="no">{n}</td><td class="w">{a}</td><td>{m}</td></tr>' for n,a,m in v['names'])
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    b.append(f'''<section class="page nm" id="v{v['n']}">
  <h2 class="page-title">VERSE {v['n']} · {rng(v)}</h2>
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
  <h2 class="page-title">PART 9 ON ONE PAGE</h2>
  <div class="sub">Names {first}–{last} in five lines</div>
  <div class="steps">
    <div><b>Verses 95–97.</b> The Wonderful; name 900 and five names of well-being; beyond words, yet praised by every word.</div>
    <div><b>Verses 98–100.</b> Best of the forgiving; destroyer of bad dreams; without anger, remover of fear.</div>
    <div><b>Verses 101–103.</b> Lakṣmī among His names; the flower's smile, ever awake; beyond birth, age and death.</div>
    <div><b>Verses 104–106.</b> Tree of the three worlds; the sacrifice, the food and its eater; Devakī's joy.</div>
    <div><b>Verses 107–108.</b> His five weapons and name 1000; "may He protect us".</div>
  </div>
  {talk("We made it to a thousand!","And the last word is protection. Part 10, the uttarabhāga, tells what chanting them brings.")}
  <div class="key">Names {first}–1000: <b>the wonderful Lord, who protects us with everything</b>. 🙏</div>
  
<div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, verses 95–108, names {first}–{last}. Text checked word by word against shlokam.org; name numbers follow its list. Meanings are our own plain-English renderings of the commonly given explanations, mostly Śaṅkara's; where Śaṅkara and Parāśara Bhaṭṭar differ, this is noted. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part9.html','w').write(head+''.join(b)+tail)
