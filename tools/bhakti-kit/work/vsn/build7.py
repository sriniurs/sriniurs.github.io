import re,sys
sys.path.insert(0,'.')
from d7 import V
from d1 import talk,person,F,BHISMA,VIS,K
src=open('Vishnu_Sahasranama_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=head.replace('Part 1 · The Opening · srini.presents','Part 7 · Names 633–764 · srini.presents')
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 7: verses 68–81, names 633–764 (arciṣmān arcitaḥ kumbhaḥ…), each name explained in plain English with illustrations.">',head)
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
  <div class="burst yel">PART 7 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 7 · VERSES 68–81 · NAMES {first}–{last}</div>
  <div class="tag">"Arciṣmān arcitaḥ kumbhaḥ" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First verses 68–81 for chanting in one go. Then <b>one page for each verse</b>: the chant, a picture, every name with its number and meaning, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">PREVIOUSLY · AND NOW</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Part 6</b>, names 513–632: Mukunda, the hidden avatāras, the Lord as medicine and doctor, twelve Śrī names, name 600, and the destroyer of sorrow.</p>
    <p><b>Part 7</b> covers verses 68–81, names {first} to {last}. Here are Keśava and Hari, Dhanañjaya, the verse of ten "Brahma" names, the hymn that praises itself, name 700, the one-syllable names "who, what, which, that", and the Lord who is without pride yet gives honour to all.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Can 'what' really be a name of God?","In verse 78, yes: 'kaḥ, kim, yat, tat'. The Upaniṣads point to God with the smallest words: That.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 68–81 IN ONE GO</h2>
  <div class="sub">For chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Text checked word by word against shlokam.org. Name numbers follow its list.</div>
</section>

<section class="page" id="howto">
  <h2 class="page-title">PAIRS OF OPPOSITES</h2>
  <div class="sub">The Lord holds both sides</div>
  <table class="ct">
    <tr><th>Pair</th><th>Nos.</th><th>Meaning</th></tr>
    <tr><td><b>Eka · Naika</b></td><td>725–726</td><td>The One · the many</td></tr>
    <tr><td><b>Mūrti · Amūrtimān</b></td><td>717–720</td><td>Of every form · formless</td></tr>
    <tr><td><b>Acala · Cala</b></td><td>745–746</td><td>Unmoving · moving</td></tr>
    <tr><td><b>Darpahā · Darpada</b></td><td>712–713</td><td>Humbles pride · gives dignity</td></tr>
    <tr><td><b>Amānī · Mānada</b></td><td>747–748</td><td>Without pride · gives honour</td></tr>
    <tr><td><b>Pragraha · Nigraha</b></td><td>760–761</td><td>Holds the reins · restrains</td></tr>
    <tr><td><b>Stavya · Stotā</b></td><td>679–683</td><td>The praised · the one who praises</td></tr>
  </table>
  <div class="panel reading" style="margin-top:10px"><p><b>Not a contradiction.</b> The Upaniṣads describe Brahman in pairs like these: "It moves, and It moves not; It is far, and It is near" (Īśa Upaniṣad 5). The names hold both sides at once.</p></div>
  {talk("How can He be one and many at once?","Like the sun reflected in a hundred bowls of water: one sun, many reflections.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Previously, and Now</a></li>
    <li><span class="num">🔤</span><a href="#full">Verses 68–81 in One Go</a></li>
    <li><span class="num">ℹ</span><a href="#howto">Pairs of Opposites</a></li>
    <li><span class="num">∑</span><a href="#end">Part 7 on One Page</a></li>
    <li class="part">VERSES 68–81 · NAMES {first}–{last}</li>
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
  <h2 class="page-title">PART 7 ON ONE PAGE</h2>
  <div class="sub">Names {first}–{last} in five lines</div>
  <div class="steps">
    <div><b>Verses 68–70.</b> Pure and purifying; Keśava and Hari; Dhanañjaya, the devotee counted as Himself.</div>
    <div><b>Verses 71–73.</b> Ten Brahma names; eight times "great"; the hymn that praises itself.</div>
    <div><b>Verses 74–76.</b> Swift as the mind; name 700 by the Yamunā; the humbler of pride.</div>
    <div><b>Verses 77–79.</b> Every form and formless; one and many, "That", the lover of devotees; moving and unmoving.</div>
    <div><b>Verses 80–81.</b> Without pride, giving honour; the One who holds the reins.</div>
  </div>
  {talk("Which name stays with you?","Bhaktavatsala, name 736: the Lord who loves His devotees.")}
  <div class="key">Names {first}–{last}: <b>one and many, form and formless, always loving</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, verses 68–81, names {first}–{last}. Text checked word by word against shlokam.org; name numbers follow its list. Meanings are our own plain-English renderings of the commonly given explanations, mostly Śaṅkara's; where Śaṅkara and Parāśara Bhaṭṭar differ, this is noted. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part7.html','w').write(head+''.join(b)+tail)
