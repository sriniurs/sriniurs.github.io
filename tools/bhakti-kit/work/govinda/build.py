import re,sys
sys.path.insert(0,'.')
from gdata import S,P,NOTES,talk,person,F,VIS,K,svg,B,lab,HILL,crowd
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Govinda Nāmālu · Śrī Śrīnivāsa Govindā · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Śrīnivāsa Govindā, Śrī Veṅkaṭeśa Govindā: the Govinda Nāmālu, the pilgrims\' chant of Tirumala, all 38 stanzas with every name explained in plain English and illustrated.">',head)
head=head.replace('</style>','''  .gl{display:flex;flex-wrap:wrap;gap:0 1.2em}
  .gl span{white-space:nowrap}
  .full .st{margin:0 0 6px;break-inside:avoid}
  .full .st b{color:#1d6fb8;font-style:normal;margin-right:.4em}
  .refrain{border:3px solid var(--ink);background:#fff3c4;padding:8px 12px;text-align:center;font-style:italic;font-size:18px;margin:6px 0 10px}
  .stz{font-family:Bangers;letter-spacing:1px;color:#1d6fb8;font-size:15px;margin-top:6px}
  .gp .vfig svg{max-height:104px;width:auto}
  .gp .pt{font-size:14px;margin:6px 0}
  .gp .ct td{padding-top:2px;padding-bottom:2px}
  .toc.tight{gap:5px;grid-template-columns:repeat(2,1fr)}.toc.tight li{padding:3px 8px;font-size:13px}.toc.tight .part{font-size:16px}
  @media(max-width:720px){.toc.tight{grid-template-columns:1fr}}
</style>''',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
REF='govindā hari govindā · gokulanandana govindā'
def gl(n):
    e=[a for a,_ in S[n]]; rows=[e[i:i+2] for i in range(0,len(e),2)]
    return ''.join('<span class="cl">'+' · '.join(f'{x} govindā' for x in r)+'</span>' for r in rows)
def fullst(n):
    e=[a for a,_ in S[n]]
    return f'<p class="st"><b>{n}</b>'+' · '.join(f'{x} govindā' for x in e)+'</p>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Pilgrims climbing steps up the seven green hills toward a golden temple at sunrise, singing">'
 '<circle cx="190" cy="70" r="46" fill="#ffd60a" stroke="#ff8c1a" stroke-width="4"/>'
 +''.join(f'<path d="M{-10+56*k} 240 l38 -{70+(k%3)*24} l38 {70+(k%3)*24}z" fill="#2a7a4a" stroke="#111" stroke-width="2"/>' for k in range(7))
 +'<g transform="translate(190 96)" stroke="#111" stroke-width="3"><rect x="-26" y="-22" width="52" height="22" fill="#ffd60a"/><path d="M-18 -22 l18 -30 l18 30z" fill="#e0a800"/></g>'
 +'<path d="M40 260 q80 -60 150 -150" fill="none" stroke="#c9a26b" stroke-width="10" stroke-dasharray="8 5"/>'
 +''.join(person(60+26*k,250-36*k,['#ff8c1a','#e05a8a','#fff','#2a9d6f'][k%4],'#f2c79b',.38) for k in range(4))
 +'<text x="300" y="200" font-family="Bangers" font-size="26" fill="#fff" stroke="#111" stroke-width="1">GOVINDĀ!</text></svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">38 STANZAS</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,76px)">GOVINDA NĀMĀLU</h1>
  <div class="series">ŚRĪ ŚRĪNIVĀSA GOVINDĀ · ŚRĪ VEṄKAṬEŚA GOVINDĀ</div>
  <div class="tag">The pilgrims' chant of the Seven Hills · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First the whole chant to sing along. Then what it is and how to sing it, and <b>one page for every two stanzas</b>: the chant, a picture, every name with its meaning, the story behind it and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>"Śrī Śrīnivāsā Govindā, Śrī Veṅkaṭeśā Govindā…" Anyone who has climbed the Seven Hills to Tirumala has heard it: pilgrims of every age calling out the Lord's names, one after another, each ending in a joyful "Govindā!"</p>
    <p>The <b>Govinda Nāmālu</b>, "names of Govinda" (<i>nāmālu</i> is Telugu for "names"), is a simple chant of about 150 names of Śrīnivāsa, mostly in Sanskrit with a few Telugu ones, set to a refrain everyone can join: <i>Govindā Hari Govindā, Gokulanandana Govindā</i>.</p>
    <p>No learning is needed to sing it. That is its beauty.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Govindā Govindā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why does every line end with Govindā?","Because it's a call and an answer. One person sings the name, everyone shouts 'Govindā!'. It turns a crowd into a single voice.")}
</section>

<section class="page" id="full">
  <h2 class="page-title">THE CHANT IN ONE GO</h2>
  <div class="sub">Stanzas 1–19 · sing the refrain after every stanza</div>
  <div class="refrain">{REF} <span style="font-style:normal;font-size:14px">[veṅkaṭaramaṇa]</span></div>
  <div class="full">{''.join(fullst(n) for n in range(1,20))}</div>
</section>
<section class="page" id="full2">
  <h2 class="page-title">THE CHANT IN ONE GO · CONTINUED</h2>
  <div class="sub">Stanzas 20–38 · refrain after every stanza</div>
  <div class="refrain">{REF} <span style="font-style:normal;font-size:14px">[veṅkaṭaramaṇa]</span></div>
  <div class="full">{''.join(fullst(n) for n in range(20,39))}</div>
  <div class="note">Text checked name by name against shlokam.org ("Govinda Naamaavali", 38 stanzas). Spellings and versions vary between singers; variants are noted on the stanza pages.</div>
</section>

<section class="page" id="about">
  <h2 class="page-title">WHAT IS GOVINDA NĀMĀLU?</h2>
  <div class="sub">A chant of the people</div>
  <div class="g2">
    <div class="card bg-blue"><h4>🗣 The language</h4><p>Mostly Sanskrit names, sung in the Telugu style, with a few Telugu names like <b>Ēḍukoṇḍalavāḍā</b> (Lord of the Seven Hills) and <b>Vaḍḍikāsulavāḍā</b> (the interest collector).</p></div>
    <div class="card bg-yellow"><h4>✍️ The author</h4><p>Traditional: no known author or date. It grew among the pilgrims and devotees of Tirumala, and versions vary in length and order.</p></div>
  </div>
  <div class="panel reading">
    <p><b>Simple by design.</b> Each stanza has four names, each followed by "Govindā", then the refrain. No metre to learn, no grammar to follow: just names and love.</p>
    <p><b>What's in the names.</b> Śrīnivāsa and Veṅkaṭeśa; the avatāras, especially Rāma and Kṛṣṇa; the Lord's ornaments at Tirumala (diamond crown, musk tilaka, Vaijayantī garland); and devotees and teachers linked with the hill: Padmāvatī, Rāmānuja, Hātīrāma.</p>
    <p><b>Govinda.</b> "Finder of cows" or "known through the Vedas": a name of Kṛṣṇa, and the great name of Tirumala, shouted as "Govindā! Govindā!".</p>
  </div>
  {talk("Is it the same as Bhaja Govindam?","No! Bhaja Govindam is Śaṅkara's teaching poem. Govinda Nāmālu is a pilgrims' chant of names. Both love the name Govinda.")}
</section>

<section class="page" id="howto">
  <h2 class="page-title">HOW TO SING IT</h2>
  <div class="sub">Call, answer, refrain</div>
  <div class="steps">
    <div><b>The leader calls.</b> One person sings the name: "Śrī Śrīnivāsā…"</div>
    <div><b>Everyone answers.</b> All respond: "…Govindā!"</div>
    <div><b>Four names, then the refrain.</b> After every four names, everyone sings together: "Govindā Hari Govindā, Gokulanandana Govindā".</div>
    <div><b>Speed it up.</b> Many groups start slowly and get faster and louder as the chant goes on, ending in a joyful rush.</div>
    <div><b>Alone, too.</b> Sing both parts yourself, softly, while walking, cooking or before sleep. It needs no setting and no special time.</div>
  </div>
  <div class="refrain">{REF}</div>
  {talk("Can I sing it without knowing what the names mean?","Of course! But the next pages will make every 'Govindā' mean something.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">Foreword</a></li>
    <li><span class="num">🔤</span><a href="#full">The Chant in One Go</a></li>
    <li><span class="num">ℹ</span><a href="#about">What Is Govinda Nāmālu?</a></li>
    <li><span class="num">🎵</span><a href="#howto">How to Sing It</a></li>
    <li><span class="num">∑</span><a href="#end">Govinda Nāmālu on One Page</a></li>
    <li class="part">THE 38 STANZAS</li>
    {''.join(f'<li><span class="num">{a}</span><a href="#s{a}">{t.title()} <small>({a}–{c})</small></a></li>' for (a,c),t,*_ in P)}
  </ul>
</section>
''']
for (a,c),theme,sv,_,point,key in P:
    rows=''.join(f'<tr><td class="no">{n}</td><td class="w">{e}</td><td>{m}</td></tr>' for n in (a,c) for e,m in S[n])
    note=''
    if any(n in NOTES for n in (a,c)): rows+=''.join(f'<tr><td class="no">{n}</td><td colspan="2" style="font-size:13px"><i>{NOTES[n]}</i></td></tr>' for n in (a,c) if n in NOTES)
    b.append(f'''<section class="page gp" id="s{a}">
  <h2 class="page-title">STANZAS {a}–{c}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{theme}</span></div>
    <div class="iast"><div class="stz">STANZA {a}</div>{gl(a)}<div class="stz">STANZA {c}</div>{gl(c)}<span class="cl" style="color:#1d6fb8">· {REF} ·</span></div>
    {'' if len(S[a])+len(S[c])>8 else '<div class="vfig" style="justify-content:center">'+svg(theme.title(),sv(),B)+'</div>'}
    <table class="ct nt"><tr><th>St.</th><th>Name</th><th>Means</th></tr>{rows}</table>
  </div>
  <div class="panel reading pt">{point}</div>
  <div class="key">{key}</div>{note}
</section>
''')
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">GOVINDA NĀMĀLU ON ONE PAGE</h2>
  <div class="sub">38 stanzas in five lines</div>
  <div class="steps">
    <div><b>Stanzas 1–4.</b> Śrīnivāsa, Lord of Veṅkaṭa, loving to devotees; dark as a rain cloud; the butter thief who protects the good.</div>
    <div><b>Stanzas 5–8, 25–26.</b> All the avatāras, from the Fish to Kalki, with Rāma and Kṛṣṇa again and again.</div>
    <div><b>Stanzas 9–18.</b> Friend in trouble, ocean of compassion, the fear-not hand, rescuer of the elephant, God made visible.</div>
    <div><b>Stanzas 19–31.</b> The Lord of Tirumala: diamond crown, the interest collector, Lord of the Seven Hills, on the side of His own.</div>
    <div><b>Stanzas 32–38.</b> Śiva and Keśava in one; dear to Hātīrāma and Rāmānuja; and back to Śrī Śrīnivāsa.</div>
  </div>
  <div class="refrain">{REF}</div>
  {talk("What's the one thing to remember?","You don't need to know Sanskrit to call God. Say His name, and the whole crowd, the whole hill, answers 'Govindā!'")}
  <div class="key">Govinda Nāmālu: <b>call His name, and everyone answers "Govindā!"</b> 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Govinda Nāmālu (Govinda Nāmāvalī), a traditional chant of the Tirumala pilgrims; author unknown. Text checked name by name against shlokam.org (38 stanzas); where the page shows bracketed alternatives, they are noted as variants. Temple legends (the loan from Kubera, Hātīrāma, the Virajā waters) are told as tradition. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Govinda_Namalu.html','w').write(head+''.join(b)+tail)
