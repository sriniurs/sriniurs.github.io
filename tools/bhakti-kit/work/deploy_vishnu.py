import os,re,shutil
R='/home/claude/sriniurs.github.io/bhakti/vishnu'
W='/home/claude/work'
def put(src,dst,nav=None):
    h=open(src).read()
    if nav:
        i=h.index('<div class="follow">'); h=h[:i]+nav+'\n  '+h[i:]
    os.makedirs(os.path.dirname(dst),exist_ok=True); open(dst,'w').write(h)
def navpanel(slug,title,parts,cur):
    links=' · '.join((f'<b><a href="/bhakti/vishnu/{slug}/part-{k}/">Part {k}: {t}</a></b>' if k==cur else f'<a href="/bhakti/vishnu/{slug}/part-{k}/">Part {k}: {t}</a>') for k,t in parts)
    return f'<div class="panel"><span class="caption">{title}</span><p style="margin:0">{links}</p></div>'
VSN=[(1,'The Opening'),(2,'Names 1–132'),(3,'Names 133–255'),(4,'Names 256–372'),(5,'Names 373–512'),(6,'Names 513–632'),(7,'Names 633–764'),(8,'Names 765–885'),(9,'Names 886–1000'),(10,'The Closing')]
SUP=[(1,'The World Wakes Up'),(2,'The Court at the Door'),(3,'The Stotram'),(4,'The Prapatti'),(5,'The Maṅgalāśāsanam')]
for k,_ in VSN: put(f'{W}/vsn/Vishnu_Sahasranama_Part{k}.html',f'{R}/vishnu-sahasranama/part-{k}/index.html',navpanel('vishnu-sahasranama','The ten parts',VSN,k))
for k,_ in SUP: put(f'{W}/suprabhatam/Venkatesa_Suprabhatam_Part{k}.html',f'{R}/venkatesa-suprabhatam/part-{k}/index.html',navpanel('venkatesa-suprabhatam','The five parts',SUP,k))
put(f'{W}/shanta/Shantakaram.html',f'{R}/shantakaram/index.html')
put(f'{W}/acyuta/Acyutashtakam.html',f'{R}/acyutashtakam/index.html')
put(f'{W}/madhura/Madhurashtakam.html',f'{R}/madhurashtakam/index.html')
# series index pages from Bhaja Govindam index template
tpl=open(f'{R}/bhaja-govindam/index.html').read()
def art(svgbody,bg,num=None):
    t=f'<text x="82" y="92" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="bold" fill="#962039">{num}</text>' if num else ''
    return f'<div class="tile-art" style="background:{bg}"><svg class="ill" viewBox="0 0 100 100" aria-hidden="true"><g stroke="#151515" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{svgbody}</g>{t}</svg></div>'
ART_V='<path d="M30 58 q-8 -6 -10 -18" fill="none" stroke="#3b6fd0" stroke-width="5"/><path d="M70 58 q8 -6 10 -18" fill="none" stroke="#3b6fd0" stroke-width="5"/><circle cx="20" cy="36" r="6" fill="#fff"/><circle cx="80" cy="36" r="6" fill="#ffd60a"/><circle cx="50" cy="36" r="12" fill="#3b6fd0"/><path d="M40 26 h20 l-3 -12 h-14z" fill="#ffd60a"/><path d="M32 92 q-4 -40 18 -50 q22 10 18 50z" fill="#ffd60a"/>'
ART_S='<circle cx="50" cy="52" r="24" fill="#ffd60a" stroke="#ff8c1a"/><path d="M6 92 l18 -22 l14 10 l14 -22 l14 22 l14 -12 l14 24z" fill="#2a7a4a"/><path d="M40 52 h20 v-10 l-10 -14 l-10 14z" fill="#ffd60a"/>'
ART_R='<path d="M8 74 h84" stroke="#4aa3df" stroke-width="6"/><ellipse cx="50" cy="66" rx="40" ry="8" fill="#e0e0e0"/><path d="M18 60 q30 -14 58 -6" fill="none" stroke="#3b6fd0" stroke-width="9"/><circle cx="78" cy="52" r="7" fill="#3b6fd0"/><path d="M84 60 q6 -20 2 -30" fill="none" stroke="#2a7a4a" stroke-width="6"/><path d="M48 54 q2 -18 0 -30" fill="none" stroke="#2a9d6f" stroke-width="2"/><path d="M48 24 q-8 -8 0 -14 q8 6 0 14z" fill="#f08aa6"/>'
ART_A='<path d="M24 92 q-4 -40 14 -50 q18 10 14 50z" fill="#ffd60a"/><circle cx="38" cy="34" r="10" fill="#2a9d6f"/><path d="M14 30 q-10 30 0 60" fill="none" stroke="#7a5a3a"/><path d="M58 92 q-4 -40 14 -50 q18 10 14 50z" fill="#ffd60a"/><circle cx="72" cy="34" r="10" fill="#3b6fd0"/><path d="M78 44 l16 -6" stroke="#7a5a3a"/>'
ART_M='<circle cx="50" cy="32" r="13" fill="#3b6fd0"/><path d="M54 18 q6 -12 2 -16" fill="none" stroke="#2a9d6f"/><path d="M30 92 q-4 -40 20 -50 q24 10 20 50z" fill="#ffd60a"/><path d="M52 40 L84 32" stroke="#7a5a3a" stroke-width="4"/><path d="M14 20 q4 -6 8 0 q4 -6 8 0 q-8 8 -8 8 q0 0 -8 -8z" fill="#e05a8a" stroke-width="1.5"/>'
ART_B='<circle cx="50" cy="34" r="14" fill="#4a7fd0"/><path d="M30 92 q-4 -40 20 -50 q24 10 20 50z" fill="#ffd60a"/><path d="M28 50 L74 40" stroke="#7a5a3a" stroke-width="4"/><path d="M46 22 q6 -14 14 -10 q-4 6 -8 12z" fill="#2a9d6f" stroke-width="2"/>'
BG=['#e3f2fd','#fff3c4','#ddf5ea','#fde4ec','#efe6ff']
def tile(href,a,label,h2,p,read='Read ↗'):
    return f'<li><a href="{href}">{a}<div class="tile-copy"><strong class="label">{label}</strong><h2>{h2}</h2><p>{p}</p><span class="read">{read}</span></div></a></li>'
def seriesindex(slug,title,desc,heroP,tiles):
    h=tpl
    h=re.sub(r'<title>.*?</title>',f'<title>{title} · srini.presents</title>',h)
    h=re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*"',lambda m:m.group(1)+desc+'"',h)
    h=re.sub(r'(<meta (?:property|name)="(?:og:title|twitter:title)" content=")[^"]*"',lambda m:m.group(1)+title+'"',h)
    h=h.replace('https://srinipresents.com/bhakti/vishnu/bhaja-govindam/',f'https://srinipresents.com/bhakti/vishnu/{slug}/')
    h=re.sub(r'<div class="hero-copy"><h1>.*?</h1><p>.*?</p></div>',f'<div class="hero-copy"><h1>{title}</h1><p>{heroP}</p></div>',h,flags=re.S)
    h=re.sub(r'<ol class="tiles">.*?</ol>','<ol class="tiles">\n    '+'\n    '.join(tiles)+'\n    </ol>',h,flags=re.S)
    # remove og:image lines pointing to bhaja (workflow regenerates)
    h=re.sub(r'<meta (?:property|name)="(?:og:image[^"]*|twitter:image[^"]*)" content="[^"]*">\n?','',h)
    os.makedirs(f'{R}/{slug}',exist_ok=True); open(f'{R}/{slug}/index.html','w').write(h)
VD=['The opening: the opening prayers, Yudhiṣṭhira\'s six questions, Bhīṣma\'s answer and the meditation verses.',
 'Viśvam, the universe; the Witness within; Kṛṣṇa; the grateful Lord; Acyuta, name 100.',
 'The fourfold Lord; Vāmana; the healer; Śrīnivāsa and Govinda; the lion, name 200; Nārāyaṇa.',
 'Dharma as His body; medicine and bridge; the peacock feather; Vāsudeva; Dāmodara.',
 'The hidden cause; Rāma; Oṃ; the good friend; a mother\'s love; name 500.',
 'Mukunda; avatāras hidden in the names; twelve names of Śrī; the destroyer of sorrow.',
 'Keśava and Hari; the hymn that praises itself; one and many; without pride, giving honour.',
 'Hard and easy to reach; the thread of the worlds; the rain cloud; the bearer of our burden.',
 'The Wonderful; well-being; beyond words; the best of the forgiving; name 1000.',
 'The fruits of chanting; "one verse is enough"; Śrī Rāma Rāma Rāma; the final offering.']
seriesindex('vishnu-sahasranama','Śrī Viṣṇu Sahasranāma',
 'The thousand names of Viṣṇu from the Mahābhārata, every name explained in plain English with illustrations, in ten parts.',
 'The thousand names of Viṣṇu, given by Bhīṣma on his bed of arrows: every verse and every name explained in plain English, in ten illustrated parts. Start with Part 1.',
 [tile(f'/bhakti/vishnu/vishnu-sahasranama/part-{k}/',art(ART_V,BG[(k-1)%5],k),f'Part {k} · {t}',['The Opening','The Universe and the Witness','Vāmana to Nārāyaṇa','Dharma and Dāmodara','Past the Halfway Mark','Avatāras and Śrī','One and Many','The Lord in Nature','The Last of the Thousand','The Closing'][k-1],VD[k-1]) for k,t in VSN])
SD=['Kausalyā suprajā rāma: Lakṣmī greeted first; sages, birds, bees and cowherds wake the Lord.',
 'The court gathers at His door: guardians, planets, avatāras; the sun rises; the blessing.',
 'Eleven verses of praise and plea: Veṅkaṭeśa, Kṛṣṇa and Rāma; "forgive my faults".',
 'Sixteen verses of surrender at His feet: "śrī veṅkaṭeśa caraṇau śaraṇaṃ prapadye".',
 'Fourteen blessings for the Lord, and the whole Suprabhātam on one page.']
seriesindex('venkatesa-suprabhatam','Śrī Veṅkaṭeśa Suprabhātam',
 'The dawn hymn of Tirumala, all four sections (Suprabhātam, Stotram, Prapatti, Maṅgalāśāsanam), explained verse by verse in plain English with illustrations.',
 '"Kausalyā suprajā rāma…": the dawn hymn sung at Tirumala, all 70 verses of its four sections explained in five illustrated parts. Start with Part 1.',
 [tile(f'/bhakti/vishnu/venkatesa-suprabhatam/part-{k}/',art(ART_S,BG[(k-1)%5],k),f'Part {k} · '+['Verses 1–15','Verses 16–29','Stotram · 11 verses','Prapatti · 16 verses','Maṅgalāśāsanam · 14 verses'][k-1],t,SD[k-1]) for k,t in SUP])
# Vishnu page
vp=f'{R}/index.html'; h=open(vp).read()
tiles=[tile('/bhakti/vishnu/vishnu-sahasranama/',art(ART_V,'#e3f2fd'),'Viṣṇu Sahasranāma · 10 parts','The Thousand Names','Bhīṣma\'s answer from the bed of arrows: all 1,000 names of Viṣṇu, every one explained.','Open series ↗'),
 tile('/bhakti/vishnu/venkatesa-suprabhatam/',art(ART_S,'#fff3c4'),'Veṅkaṭeśa Suprabhātam · 5 parts','The Dawn Hymn of Tirumala','"Kausalyā suprajā rāma": Suprabhātam, Stotram, Prapatti and Maṅgalāśāsanam, all 70 verses.','Open series ↗'),
 tile('/bhakti/vishnu/shantakaram/',art(ART_R,'#ddf5ea'),'Dhyāna ślokam · 1 verse','Śāntākāraṃ Bhujagaśayanam','The best-loved meditation verse: peace that holds up the universe, word by word.'),
 h[h.index('<li><a href="/bhakti/vishnu/bhaja-govindam/">'):h.index('</li>',h.index('<li><a href="/bhakti/vishnu/bhaja-govindam/">'))+5],
 tile('/bhakti/vishnu/acyutashtakam/',art(ART_A,'#fde4ec'),'Acyutāṣṭakam · 9 verses','Acyutaṃ Keśavam','A garland of the Lord\'s names: Rāma of the forest, little Gopāla, and a meditation on His form.'),
 tile('/bhakti/vishnu/madhurashtakam/',art(ART_M,'#efe6ff'),'Madhurāṣṭakam · 8 verses','Adharaṃ Madhuram','Vallabhācārya\'s song of Kṛṣṇa\'s sweetness: everything about Him is sweet.')]
h=re.sub(r'<ol class="tiles">.*?</ol>','<ol class="tiles">\n    '+'\n    '.join(tiles)+'\n    </ol>',h,flags=re.S)
h=h.replace('The series opens with Bhaja Govindam.','From the thousand names to the dawn hymn of Tirumala.')
nd='Hymns to Viṣṇu explained verse by verse in plain English with illustrations: the Viṣṇu Sahasranāma, the Veṅkaṭeśa Suprabhātam, Śāntākāram, Bhaja Govindam, the Acyutāṣṭakam and the Madhurāṣṭakam.'
h=re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*"',lambda m:m.group(1)+nd+'"',h)
open(vp,'w').write(h)
# Bhakti hub
bp='/home/claude/sriniurs.github.io/bhakti/index.html'; h=open(bp).read()
h=h.replace('<strong class="label">1 hymn · 3 articles</strong><h2>Viṣṇu</h2><p>Bhaja Govindam, Ādi Śaṅkara\'s "hammer for delusion", in three parts.</p>','<strong class="label">6 hymns · 21 articles</strong><h2>Viṣṇu</h2><p>The Viṣṇu Sahasranāma, the Veṅkaṭeśa Suprabhātam, Śāntākāram, Bhaja Govindam and more.</p>')
open(bp,'w').write(h)
print('done')
