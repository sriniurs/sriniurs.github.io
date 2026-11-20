import re,sys
sys.path.insert(0,'.')
from d10 import V
from d1 import talk,person,F,BHISMA,VIS,K
src=open('/home/claude/work/bhaja/Bhaja_Govindam_Part1.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śrī Viṣṇu Sahasranāma · Part 10 · The Closing · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Śrī Viṣṇu Sahasranāma, Part 10: the uttarabhāga, the fruits of chanting the thousand names and the closing verses of Arjuna, Kṛṣṇa, Vyāsa, Śiva, Brahmā and Sañjaya, explained in plain English with illustrations.">',head)
head=head.replace('</style>','  .iast .cl2{padding-left:2.2em}\n  .full .ln2{padding-left:2.2em}\n  .pt{font-size:14.5px;line-height:1.45;margin:8px 0}\n  .toc.tight{gap:5px;grid-template-columns:repeat(3,1fr)}.toc.tight li{padding:3px 8px;font-size:13px}.toc.tight .part{font-size:16px}\n  .long .vfig svg{max-height:150px;width:auto}\n  .long .ct td{padding-top:2px;padding-bottom:2px}\n  @media(max-width:720px){.iast .cl2{padding-left:1.4em}.full .ln2{padding-left:1.4em}}\n</style>',1)
tail=src[src.find('<script>\n  document.querySelectorAll'):]
def iast(v): return '<div class="iast">'+''.join(f'<span class="cl">{a}</span><span class="cl cl2">{b}</span>' for a,b in v['lines'])+'</div>'
def full(v):
    o=f'<p><span class="vn">{v["lab"]}</span>'
    for a,b in v['lines']:
        b=re.sub(r'\s*‖(\d+)‖$',r'<span class="end">‖ \1 ‖</span>',b)
        o+=f'<span class="ln">{a}</span><span class="ln ln2">{b}</span>'
    return o+'</p>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Bhishma lying on a bed of arrows at Kurukshetra at sunset, with Yudhishthira kneeling and Krishna standing, and the four-armed Vishnu shining in the sky">'
 '<circle cx="190" cy="80" r="70" fill="#ffd60a" opacity=".5"/>'+VIS(190,-6,.75)+
 '<path d="M0 230 H380 V268 H0Z" fill="#c9a26b"/>'+BHISMA(190,232,1.4)+person(70,250,'#e63946','#f2c79b',.7)+K(320,120,.6)+'</svg>')
story_svg=('<svg class="fig" style="border:3px solid var(--ink);background:#fff" width="460" height="210" viewBox="0 0 460 210" role="img" aria-label="Three panels: the war ends at Kurukshetra; Bhishma teaches Yudhishthira from the bed of arrows while Krishna listens; the thousand names are recited">'
 '<rect width="460" height="210" fill="#fff8ec"/>'+''.join(f'<rect x="{6+151*i}" y="6" width="145" height="198" fill="{bg}" stroke="#111" stroke-width="3"/><text x="{78+151*i}" y="196" text-anchor="middle" font-family="Bangers" font-size="12">{t}</text>' for i,(bg,t) in enumerate([('#ffe3c4','THE WAR ENDS'),('#e7f4ea','BHĪṢMA TEACHES'),('#dfe9f6','1000 NAMES')]))
 +''.join(f'<path d="M{20+16*k} 160 l10 -60" stroke="#7a5a3a" stroke-width="3"/>' for k in range(7))
 +'<g transform="translate(78 0)">'+'</g>'+BHISMA(230,150,.9)+person(186,170,'#e63946','#f2c79b',.45)+K(270,60,.35)
 +''.join(f'<text x="{330+22*(k%5)}" y="{50+24*(k//5)}" font-family="Bangers" font-size="11" fill="#1d6fb8">✿</text>' for k in range(25))+'</svg>')
b=[f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">PART 10 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(24px,7vw,72px)">ŚRĪ VIṢṆU<br>SAHASRANĀMA</h1>
  <div class="series">PART 10 · THE UTTARABHĀGA · THE FRUITS</div>
  <div class="tag">The thousand names of Viṣṇu · explained and illustrated</div>
  {cover}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First all of Part 10 for chanting in one go. Then the story and background, and <b>one page for each verse</b>: the chant, a picture, what it says, the key words, one insight and the one thing to remember.
  </div>
</section>

<section class="page" id="foreword">
  <h2 class="page-title">THE LAST WORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p><b>In Parts 1–9</b>, Yudhiṣṭhira asked his questions, Bhīṣma answered with a thousand names, and we went through every one, from "Viśvam", the universe, to "Sarvapraharaṇāyudha", whose weapons are all things.</p>
    <p><b>Part 10</b> is the <i>uttarabhāga</i>, the closing section: 33 verses. First Bhīṣma tells what chanting the names brings (verses 1–22). Then others speak: Arjuna prays, Kṛṣṇa promises that one verse is enough, Vyāsa bows, Pārvatī asks for a shortcut and Śiva gives "Śrī Rāma Rāma Rāma", Brahmā praises, Sañjaya speaks the Gītā's last verse, and it ends with prayers for all who suffer, and an offering of everything we do.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d6fb8">Hari Oṃ,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is there really a shortcut for all thousand names?","Śiva himself gives it in verse 27: 'Śrī Rāma Rāma Rāma'. And Kṛṣṇa says even one sincere verse is enough!")}
</section>
''']
def fullpage(id_,title,sub,vs,note=''):
    return f'''<section class="page" id="{id_}">
  <h2 class="page-title">{title}</h2>
  <div class="sub">{sub}</div>
  <div class="full">{''.join(full(v) for v in vs)}</div>{note}
</section>
'''
ph=[v for v in V if v['sec']=='PHALA']; cl=[v for v in V if v['sec']=='CLOSE']
b.append(fullpage('full','PART 10 IN ONE GO','Phalaśruti 1–12',ph[:12]))
b.append(fullpage('full2','PART 10 IN ONE GO · CONTINUED','Phalaśruti 13–22',ph[12:]))
b.append(fullpage('full3','PART 10 IN ONE GO · CLOSING VERSES','Verses 23–33',cl,'\n  <div class="note">Lines are split at natural pauses. Text checked word by word against shlokam.org; two small differences are noted on their pages.</div>'))
b.append(f'''<section class="page" id="story">
  <h2 class="page-title">WHO SPEAKS AT THE END</h2>
  <div class="sub">Seven voices close the hymn</div>
  <table class="ct">
    <tr><th>Verses</th><th>Speaker</th><th>What they say</th></tr>
    <tr><td><b>1–22</b></td><td>Bhīṣma</td><td>The fruits of hearing and chanting the names</td></tr>
    <tr><td><b>23</b></td><td>Arjuna</td><td>"Protect Your loving devotees"</td></tr>
    <tr><td><b>24</b></td><td>Kṛṣṇa</td><td>"One verse is enough"</td></tr>
    <tr><td><b>25</b></td><td>Vyāsa</td><td>"The three worlds are Your dwelling"</td></tr>
    <tr><td><b>26–27</b></td><td>Pārvatī and Śiva</td><td>The shortcut: "Śrī Rāma Rāma Rāma"</td></tr>
    <tr><td><b>28</b></td><td>Brahmā</td><td>"Of a thousand forms and names"</td></tr>
    <tr><td><b>29</b></td><td>Sañjaya</td><td>"Where Kṛṣṇa and Arjuna are…" (Gītā 18.78)</td></tr>
    <tr><td><b>30–31</b></td><td>Kṛṣṇa</td><td>Gītā 9.22 and 4.8: "I carry their needs"; "age after age"</td></tr>
    <tr><td><b>32–33</b></td><td>Closing prayers</td><td>For all who suffer; offering everything to Nārāyaṇa</td></tr>
  </table>
  <div class="panel reading" style="margin-top:10px"><p><b>Texts vary.</b> Different traditions add or omit a few closing verses; this series follows the 33 given on shlokam.org.</p></div>
  {talk("Śiva, Brahmā, Vyāsa, Arjuna: all together?","The hymn ends like a festival: gods, sages and devotees all join in praising the same Lord.")}
</section>

<section class="page" id="about">
  <h2 class="page-title">THE PROMISES, IN SHORT</h2>
  <div class="sub">What Bhīṣma says the names bring</div>
  <div class="steps">
    <div><b>For everyone.</b> Hearing alone is enough (2); every calling is blessed (3); whatever you seek, you find (4).</div>
    <div><b>How.</b> Rise early, be clean, keep your mind on Him, chant with devotion (5).</div>
    <div><b>Outer gifts.</b> Good name, steady fortune, health, freedom from illness, bondage, fear and danger (6–9).</div>
    <div><b>Inner gifts.</b> Joy, patience, steadiness, memory; no anger, envy or greed (12–13).</div>
    <div><b>The highest gift.</b> Purified, the devotee reaches the eternal, and is never defeated (10, 22).</div>
  </div>
  {talk("Is it just about getting things?","The list starts with worldly goods but rises to inner peace and liberation. Bhīṣma meets everyone where they are, and leads them higher.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc tight">
    <li class="part">START HERE</li>
    <li><span class="num">✍</span><a href="#foreword">The Last Word</a></li>
    <li><span class="num">🔤</span><a href="#full">Part 10 in One Go</a></li>
    <li><span class="num">★</span><a href="#story">Who Speaks at the End</a></li>
    <li><span class="num">ℹ</span><a href="#about">The Promises, in Short</a></li>
    <li><span class="num">∑</span><a href="#end">The Whole Sahasranāma on One Page</a></li>
    <li class="part">PHALAŚRUTI · BHĪṢMA</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title()}</a></li>' for v in ph)}
    <li class="part">CLOSING VERSES</li>
    {''.join(f'<li><span class="num">{v["n"]}</span><a href="#v{v["n"]}">{v["theme"].title()}</a></li>' for v in cl)}
  </ul>
</section>
''')
for v in V:
    lg=len(v['lines'])>=3
    ws=v['words'][:4] if lg else v['words']
    words=''.join(f'<tr><td class="w">{a}</td><td>{m}</td></tr>' for a,m in ws)
    plain='' if lg else f'<div class="plain">{v["plain"]}</div>'
    note=f'\n  <div class="note">{v["note"]}</div>' if v.get('note') else ''
    b.append(f'''<section class="page{' long' if lg else ''}" id="v{v['n']}">
  <h2 class="page-title">{v['lab']}</h2>
  <div class="sloka" style="margin-top:4px">
    <div class="sloka-head"><span class="theme" style="font-size:22px">{v['theme']}</span></div>
    {iast(v)}
    <div class="vfig">{v['svg']}<div class="mean">{v['mean']}</div></div>
    {plain}
    <table class="ct"><tr><th>Word</th><th>Means</th></tr>{words}</table>
  </div>
  <div class="panel reading pt">{v['point']}</div>
  <div class="key">{v['key']}</div>{note}
</section>
''')
b.append(f'''<section class="page" id="end">
  <h2 class="page-title">THE WHOLE SAHASRANĀMA ON ONE PAGE</h2>
  <div class="sub">Ten parts, a thousand names, one answer</div>
  <div class="steps">
    <div><b>Part 1 · The question.</b> On his bed of arrows, Bhīṣma is asked: who is the one God, and what frees us? His answer: the thousand names.</div>
    <div><b>Parts 2–5 · Names 1–512.</b> The universe and its Witness; the avatāras; the healer and the bridge; the friend and the mother's love; name 500.</div>
    <div><b>Parts 6–9 · Names 513–1000.</b> Śrī everywhere; one and many; hard and easy to reach; the bearer of our burden; the Wonderful; everything is His weapon to protect us.</div>
    <div><b>Part 10 · The fruits.</b> Health, courage and peace; one verse is enough; "Śrī Rāma Rāma Rāma".</div>
    <div><b>The last word.</b> Whatever I do, I offer to Nārāyaṇa.</div>
  </div>
  {talk("So what's the one thing to remember from all ten parts?","Bhīṣma's answer to 'what frees us?': remember the Lord, by any of His names, with love. One sincere name is enough.")}
  <div class="key">Śrī Viṣṇu Sahasranāma: <b>a thousand ways to remember one loving Lord</b>. Hari Oṃ 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>
</section>

<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Śrī Viṣṇu Sahasranāma, Part 10: the uttarabhāga (33 verses as given on shlokam.org). Text checked word by word against shlokam.org; we read jñātiprādhānyam (v6) and parikalpyate (v17) where that site differs. Gītā references: 18.78, 9.22, 4.8. The numerical reading of "Rāma" in verse 27 is a traditional explanation. Some recitations add or omit closing verses. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.</footer>
</div>
''')
open('Vishnu_Sahasranama_Part10.html','w').write(head+''.join(b)+tail)
