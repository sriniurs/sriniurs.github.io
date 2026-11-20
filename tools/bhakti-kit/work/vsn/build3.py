import re,sys
sys.path.insert(0,'.')
from d3 import V
from d1 import talk,person,F,BHISMA,VIS,K
src=open('Vishnu_Sahasranama_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=head.replace('Part 1 · The Opening · srini.presents','Part 3 · Names 133–255 · srini.presents')
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 3: verses 15–27, names 133–255 (lokādhyakṣaḥ surādhyakṣaḥ…), each name explained in plain English with illustrations.">',head)
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
  <div class="burst yel">PART 3 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 3 · VERSES 15–27 · NAMES {first}–{last}</div>
  <div class="tag">"Lokādhyakṣaḥ surādhyakṣaḥ" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First verses 15–27 for chanting in one go. Then <b>one page for each verse</b>: the chant, a picture, every name with its number and meaning, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">PREVIOUSLY · AND NOW</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Part 2</b>, the names began with "Viśvam", the universe, and moved through the Witness within, the man-lion, Kṛṣṇa, the grateful Lord, Acyuta (name 100) and the Veda: names 1–132.</p>
    <p><b>Part 3</b> continues with verses 15–27, names {first} to {last}. Here the avatāras and the great Tirumala names appear: Vāmana the dwarf who became a giant, the mountain-lifter, Śrīnivāsa and Govinda, the lion (name 200), the Cosmic Person with a thousand heads, and Nārāyaṇa.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Are there stories behind these names?","Lots! The dwarf who asked for three steps, the boy who held up a mountain, the twin sages Nara and Nārāyaṇa. See the next pages.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 15–27 IN ONE GO</h2>
  <div class="sub">For chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Text checked word by word against shlokam.org. Name numbers follow its list.</div>
</section>

<section class="page" id="howto">
  <h2 class="page-title">STORIES BEHIND THE NAMES</h2>
  <div class="sub">Four stories hidden in verses 15–27</div>
  <div class="steps">
    <div><b>The four vyūhas (v15, v20).</b> In the Pāñcarātra tradition the Lord appears as Vāsudeva, Saṅkarṣaṇa, Pradyumna and Aniruddha: hence "of four emanations" (138) and Aniruddha (185).</div>
    <div><b>Vāmana (v17).</b> The demon-king Bali ruled the three worlds. Viṣṇu came as a dwarf boy (152) and asked for three steps of land; then grew into a giant (153) and measured earth and sky.</div>
    <div><b>The mountain (v19).</b> Mahādridhṛk (180): as Kūrma He bore Mount Mandara at the churning of the ocean; as Kṛṣṇa He lifted Govardhana to shelter Vraja from Indra's storm.</div>
    <div><b>Nara and Nārāyaṇa (v26).</b> Twin sages who meditated at Badarī in the Himalayas; the Mahābhārata says they were reborn as Arjuna and Kṛṣṇa.</div>
    <div><b>The Puruṣa (v24).</b> The Ṛg Veda's Cosmic Person, "thousand-headed, thousand-eyed, thousand-footed": names 224–227.</div>
  </div>
  {talk("Why tell stories in a list of names?","Because each name is a doorway into a story, and stories are how the names stay in the heart.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Previously, and Now</a></li>
    <li><span class="num">🔤</span><a href="#full">Verses 15–27 in One Go</a></li>
    <li><span class="num">ℹ</span><a href="#howto">Stories Behind the Names</a></li>
    <li><span class="num">∑</span><a href="#end">Part 3 on One Page</a></li>
    <li class="part">VERSES 15–27 · NAMES {first}–{last}</li>
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
  <h2 class="page-title">PART 3 ON ONE PAGE</h2>
  <div class="sub">Names {first}–{last} in five lines</div>
  <div class="steps">
    <div><b>Verses 15–17.</b> The fourfold Lord; the food and the eater, the patient one; Vāmana, the dwarf who became a giant.</div>
    <div><b>Verses 18–20.</b> Vaidya, the healer; the mountain-lifter; Śrīnivāsa and Govinda, the names of the Seven Hills.</div>
    <div><b>Verses 21–22.</b> Swan, eagle and serpent; name 200, the lion who guards His devotees.</div>
    <div><b>Verses 23–24.</b> The greatest teacher, eyes closed yet ever watchful; the thousand-headed Cosmic Person.</div>
    <div><b>Verses 25–27.</b> The still hub of the turning wheel; Nārāyaṇa, refuge of all; the Lord whose will is always done.</div>
  </div>
  {talk("Which name stays with you?","Vaidya, name 164: the physician. The Lord as the healer of the soul.")}
  <div class="key">Names {first}–{last}: <b>from the fourfold Lord to the giver of success</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, verses 15–27, names {first}–{last}. Text checked word by word against shlokam.org; name numbers follow its list. Meanings are our own plain-English renderings of the commonly given explanations, mostly Śaṅkara's; where Śaṅkara and Parāśara Bhaṭṭar differ, this is noted. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part3.html','w').write(head+''.join(b)+tail)
