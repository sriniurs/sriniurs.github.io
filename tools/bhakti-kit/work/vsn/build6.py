import re,sys
sys.path.insert(0,'.')
from d6 import V
from d1 import talk,person,F,BHISMA,VIS,K
src=open('Vishnu_Sahasranama_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=head.replace('Part 1 · The Opening · srini.presents','Part 6 · Names 513–632 · srini.presents')
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 6: verses 55–67, names 513–632 (jīvo vinayitā sākṣī…), each name explained in plain English with illustrations.">',head)
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
  <div class="burst yel">PART 6 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 6 · VERSES 55–67 · NAMES {first}–{last}</div>
  <div class="tag">"Jīvo vinayitā sākṣī" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First verses 55–67 for chanting in one go. Then <b>one page for each verse</b>: the chant, a picture, every name with its number and meaning, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">PREVIOUSLY · AND NOW</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Part 5</b>, names 373–512: the hidden cause, Rāma, Oṃ, time and rest, the good friend, a mother's love, name 500, and the Lord who keeps His word.</p>
    <p><b>Part 6</b> covers verses 55–67, names {first} to {last}. Here come many avatāras (Kapila, Matsya, Varāha, Paraśurāma, Balarāma), the Lord as medicine and doctor, a dozen <b>Śrī</b> names in a row, name 600, and the One who cuts our doubts and destroys our grief.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("So many avatāras in one part?","Yes! Look for the fish with a horn, the great boar, the axe, the plough. They're hidden in single words.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 55–67 IN ONE GO</h2>
  <div class="sub">For chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Text checked word by word against shlokam.org. Name numbers follow its list.</div>
</section>

<section class="page" id="howto">
  <h2 class="page-title">AVATĀRAS HIDDEN IN THE NAMES</h2>
  <div class="sub">Spot them in verses 55–67</div>
  <table class="ct">
    <tr><th>Name</th><th>No.</th><th>Avatāra</th></tr>
    <tr><td><b>Trivikrama</b></td><td>530</td><td>Vāmana, of the three strides</td></tr>
    <tr><td><b>Maharṣiḥ Kapilācāryaḥ</b></td><td>531</td><td>Kapila, the sage of Sāṅkhya</td></tr>
    <tr><td><b>Mahāśṛṅga</b></td><td>536</td><td>Matsya, the great horned fish</td></tr>
    <tr><td><b>Mahāvarāha</b></td><td>538</td><td>Varāha, the boar who lifted the earth</td></tr>
    <tr><td><b>Saṅkarṣaṇa · Halāyudha</b></td><td>552 · 562</td><td>Balarāma, with the plough</td></tr>
    <tr><td><b>Khaṇḍaparaśu</b></td><td>568</td><td>Paraśurāma, with the axe</td></tr>
    <tr><td><b>Sarvadṛg-vyāsa</b></td><td>572</td><td>Vyāsa, who divided the Veda</td></tr>
    <tr><td><b>Bhūśaya</b></td><td>628</td><td>Rāma, lying on the shore</td></tr>
  </table>
  <div class="panel reading" style="margin-top:10px"><p><b>Many readings.</b> These identifications follow the traditional commentaries; some names carry other meanings too (Govinda at 539 is read as "finder of the earth", linking it to Varāha).</p></div>
  {talk("Why hide avatāras inside single words?","So that chanting the names is also re-telling the stories. One word, one whole story.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Previously, and Now</a></li>
    <li><span class="num">🔤</span><a href="#full">Verses 55–67 in One Go</a></li>
    <li><span class="num">ℹ</span><a href="#howto">Avatāras Hidden in the Names</a></li>
    <li><span class="num">∑</span><a href="#end">Part 6 on One Page</a></li>
    <li class="part">VERSES 55–67 · NAMES {first}–{last}</li>
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
  <h2 class="page-title">PART 6 ON ONE PAGE</h2>
  <div class="sub">Names {first}–{last} in five lines</div>
  <div class="steps">
    <div><b>Verses 55–57.</b> Mukunda, giver of freedom; bliss and the three strides; Kapila and the great horned fish.</div>
    <div><b>Verses 58–60.</b> The great Boar; the tree of refuge; Bhagavān, with Kṛṣṇa's garland and Balarāma's plough.</div>
    <div><b>Verses 61–62.</b> Vyāsa among the names; the medicine and the doctor; five names of peace.</div>
    <div><b>Verses 63–65.</b> Friend of the cows; name 600; twelve names of Śrī.</div>
    <div><b>Verses 66–67.</b> The remover of doubts; the destroyer of sorrow.</div>
  </div>
  {talk("Which name stays with you?","Śokanāśana, name 632: the One who destroys our grief.")}
  <div class="key">Names {first}–{last}: <b>avatāras, healing, Śrī, and comfort</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, verses 55–67, names {first}–{last}. Text checked word by word against shlokam.org; name numbers follow its list. Meanings are our own plain-English renderings of the commonly given explanations, mostly Śaṅkara's; where Śaṅkara and Parāśara Bhaṭṭar differ, this is noted. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part6.html','w').write(head+''.join(b)+tail)
