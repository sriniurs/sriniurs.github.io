import re,sys
sys.path.insert(0,'.')
from d2 import V
from d1 import talk,person,F,BHISMA,VIS,K
src=open('Vishnu_Sahasranama_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=head.replace('Part 1 · The Opening · srini.presents','Part 2 · Names 1–132 · srini.presents')
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 2: verses 1–14, names 1–132 (viśvaṃ viṣṇur vaṣaṭkāraḥ…), each name explained in plain English with illustrations.">',head)
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
  <div class="burst yel">PART 2 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 2 · VERSES 1–14 · NAMES {first}–{last}</div>
  <div class="tag">"Viśvaṃ viṣṇur vaṣaṭkāraḥ" · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First verses 1–14 for chanting in one go. Then <b>one page for each verse</b>: the chant, a picture, every name with its number and meaning, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">THE NAMES BEGIN</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Part 1</b>, Yudhiṣṭhira asked his six questions and Bhīṣma answered: praise the Lord with His thousand names. We prepared with the opening prayers, the nyāsa and the meditation verses.</p>
    <p><b>Part 2</b> begins the names themselves: verses 1–14, names {first} to {last}. They start with the widest view possible, "Viśvam", the universe, and move through the Self within, the creator, the refuge, time itself, and the Veda.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("How do you count names inside a verse?","Each verse packs eight to twelve names. Most are single words; a few, like 'muktānāṃ paramā gatiḥ', are phrases counted as one name.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">VERSES 1–14 IN ONE GO</h2>
  <div class="sub">For chanting</div>
  <div class="full">{''.join(full(v) for v in V)}</div>
  <div class="note">Text checked word by word against shlokam.org. Name numbers follow its list.</div>
</section>

<section class="page" id="howto">
  <h2 class="page-title">HOW TO READ A NAME</h2>
  <div class="sub">Every name is a teaching</div>
  <div class="steps">
    <div><b>Names from qualities.</b> Bhīṣma called them <i>gauṇa</i>: each name describes a quality or deed of the Lord (Part 1, pūrvabhāga 13).</div>
    <div><b>More than one meaning.</b> Sanskrit packs meanings: Āditya is "the sun" and "Aditi's son, Vāmana". The pages give the main sense and note others.</div>
    <div><b>Two great guides.</b> Ādi Śaṅkara (Advaita) and Parāśara Bhaṭṭar (Viśiṣṭādvaita) explained every name. Meanings here follow the commonly given ones, mostly Śaṅkara's, and say where the two differ.</div>
    <div><b>Counting.</b> Some names are phrases, and lists differ slightly in where they split them. Numbers here follow shlokam.org.</div>
    <div><b>Repeats.</b> A few names appear twice, like Veda-vit in verse 14. Each time, the commentators find a different sense.</div>
  </div>
  {talk("So I don't have to memorise a thousand meanings?","No! Chant the names; read one page at a time. Even one name understood changes how you chant all the others.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">The Names Begin</a></li>
    <li><span class="num">🔤</span><a href="#full">Verses 1–14 in One Go</a></li>
    <li><span class="num">ℹ</span><a href="#howto">How to Read a Name</a></li>
    <li><span class="num">∑</span><a href="#end">Part 2 on One Page</a></li>
    <li class="part">VERSES 1–14 · NAMES {first}–{last}</li>
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
  <h2 class="page-title">PART 2 ON ONE PAGE</h2>
  <div class="sub">Names {first}–{last} in five lines</div>
  <div class="steps">
    <div><b>Verses 1–2.</b> The universe, the all-pervading, Lord of all time; the Supreme Self, the silent Witness within.</div>
    <div><b>Verses 3–5.</b> Yoga’s goal, the man-lion, the Supreme Person; Śiva the auspicious; self-born, without beginning or end.</div>
    <div><b>Verses 6–8.</b> Hṛṣīkeśa, master of the senses; Kṛṣṇa, existence-bliss; life itself, the golden seed, Mādhava.</div>
    <div><b>Verses 9–11.</b> The grateful Lord who remembers every offering; our refuge; Acyuta, name 100, who never lets us fall.</div>
    <div><b>Verses 12–14.</b> The Truth, equal to all; the many-headed Puruṣa; the Veda and its seer.</div>
  </div>
  {talk("Which name stays with you?","Kṛtajña, name 82: the grateful Lord. The God of the universe remembers a single flower offered with love.")}
  <div class="key">Names {first}–{last}: <b>from "the universe" to "the seer"</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, verses 1–14, names {first}–{last}. Text checked word by word against shlokam.org; name numbers follow its list. Meanings are our own plain-English renderings of the commonly given explanations, mostly Śaṅkara's; where Śaṅkara and Parāśara Bhaṭṭar differ, this is noted. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part2.html','w').write(head+''.join(b)+tail)
