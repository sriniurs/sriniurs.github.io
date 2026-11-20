import re,shutil,os
R='/home/claude/sriniurs.github.io'; W='/home/claude/work'
def cp(src,dst):
    os.makedirs(f'{R}/{dst}',exist_ok=True); shutil.copy(f'{W}/{src}',f'{R}/{dst}/index.html')
for n in range(1,7): cp(f'devim/Devi_Mahatmya_Part0{n}.html',f'bhakti/devi/devi-mahatmya/part-{n}')
cp('tiruppavai/Tiruppavai_Day01.html','bhakti/vishnu/tiruppavai/day-1')
cp('triranga/Triranga_Darshanam.html','bhakti/temples-of-india/triranga')
for s,f in [('adi-ranga','Adi_Ranga'),('madhya-ranga','Madhya_Ranga'),('antya-ranga','Antya_Ranga')]: cp(f'triranga/{f}.html',f'bhakti/temples-of-india/triranga/{s}')
cp('mysuru/Nanjangud.html','bhakti/temples-of-india/around-mysuru/nanjangud')

T=open(f'{R}/bhakti/temples-of-india/12-jyotirlingas/index.html').read()
T=re.sub(r'<!-- seo:auto -->.*?<!-- /seo:auto -->\n?','',T,flags=re.S)
T=re.sub(r'<!-- sitenav:auto -->.*?<!-- /sitenav:auto -->\n?','',T,flags=re.S)
HEAD=T[:T.find('<main>')]
def tile(href,bg,svg,label,h2,p,read='Read ↗'):
    return f'<li><a href="{href}"><div class="tile-art" style="background:{bg}"><svg class="ill" viewBox="0 0 100 100" aria-hidden="true"><g stroke="#151515" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{svg}</g></svg></div><div class="tile-copy"><strong class="label">{label}</strong><h2>{h2}</h2><p>{p}</p><span class="read">{read}</span></div></a></li>'
def index(path,title,desc,backurl,backname,heroc,h1c,bodyc,banner,intro,tiles,extra=''):
    h=HEAD
    h=re.sub(r'<title>.*?</title>',f'<title>{title} · srini.presents</title>',h)
    h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',h)
    h=re.sub(r'<link rel="canonical" href="[^"]*">',f'<link rel="canonical" href="https://srinipresents.com/{path}/">',h)
    h=h.replace('.hero{background:#0b2a4a}.hero h1{color:#ffd23f}.hero p{color:#fff}body{background:#eef3fa}',f'.hero{{background:{heroc}}}.hero h1{{color:{h1c}}}.hero p{{color:#fff}}body{{background:{bodyc}}}')
    h=re.sub(r'<a href="/bhakti/temples-of-india/">← Temples of India</a>',f'<a href="{backurl}">← {backname}</a>',h)
    html=h+f'''<main>
  <header class="hero">
    <div class="hero-copy"><h1>{title}</h1><p>{intro}</p></div>
    <img src="{banner}" alt="" width="1200" height="800" fetchpriority="high">
  </header>
  <ol class="tiles">
    {"".join(tiles)}
  </ol>{extra}
</main>
<footer>srini.presents</footer>
<script data-goatcounter="https://sriniurs.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body></html>
'''
    os.makedirs(f'{R}/{path}',exist_ok=True); open(f'{R}/{path}/index.html','w').write(html)
# --- Devi Mahatmya
DEVI='<circle cx="50" cy="30" r="12" fill="#f2c79b"/><path d="M36 18 h28 l-4 -12 l-6 6 l-4 -8 l-4 8 l-6 -6z" fill="#ffd60a"/><path d="M28 92 q-4 -42 22 -50 q26 8 22 50z" fill="#c0392b"/>'
dm=[('Devī Kavacam · verses 1–17','The armour of the Goddess, part one: Brahmā tells Mārkaṇḍeya the secret of the Kavacam and the nine Durgās.'),
 ('Devī Kavacam · verses 18–56','The armour, part two: the Goddess guarding every part of the body, head to foot, and the fruits of the hymn.'),
 ('Argalā Stotram','The bolt that opens the door: the hymn of requests, “give form, give victory, give glory, destroy foes”.'),
 ('Kīlakam','The pin: the short hymn that unlocks the Devī Māhātmya, and why it is recited before the text.'),
 ('Chapter 1 · the frame story','King Suratha and the merchant Samādhi meet the sage Medhas: why the mind clings to what has left it.'),
 ('Chapter 1 · Brahmā’s hymn','Madhu and Kaiṭabha, Viṣṇu asleep on Śeṣa, and Brahmā’s hymn to Yoganidrā that wakes him.')]
tiles=[tile(f'/bhakti/devi/devi-mahatmya/part-{i+1}/','#fde4e4',DEVI+f'<text x="50" y="74" text-anchor="middle" font-size="22" font-family="Georgia" fill="#fff" stroke="none">{i+1}</text>',f'Part {i+1} of 19',t,d) for i,(t,d) in enumerate(dm)]
index('bhakti/devi/devi-mahatmya','Devī Māhātmya','The Devī Māhātmya (Durgā Saptaśatī) in 19 illustrated parts: Kavacam, Argalā, Kīlakam and all 13 chapters, verse by verse in plain English.','/bhakti/devi/','Devi','#3a1414','#ffd27a','#fdf3f3','/bhakti/devi/devi-banner.jpg',
 'The Glory of the Goddess, also called the Durgā Saptaśatī, the 700 verses: the three limbs recited before it (Kavacam, Argalā, Kīlakam), then all thirteen chapters, verse by verse, in 19 illustrated parts. Parts 1–6 are here; the rest follow.',tiles,
 '\n  <p style="margin:18px 0 0">Coming next: Chapter 2, the birth of the Goddess from the light of all the gods. Also read <a href="/bhakti/devi/ya-devi-sarvabhuteshu/">Yā Devī Sarvabhūteṣu</a> (from chapter 5) and <a href="/bhakti/devi/mahishasura-mardini/">Mahiṣāsura Mardinī</a>.</p>')
# --- Tiruppavai
ANDAL='<circle cx="50" cy="34" r="12" fill="#c98b5a"/><path d="M38 26 q12 -16 24 0" fill="#2b1a0e"/><path d="M60 22 q10 -6 12 6" fill="none" stroke="#2b1a0e" stroke-width="6"/><path d="M30 92 q-2 -40 20 -46 q22 6 20 46z" fill="#2e9a5a"/><path d="M34 60 q16 10 32 0" fill="none" stroke="#ffd60a" stroke-width="4"/>'
index('bhakti/vishnu/tiruppavai','Tiruppāvai','Āṇḍāḷ’s Tiruppāvai, 30 Tamil songs for the dawns of Mārgaḻi (Dhanurmāsa): one illustrated page per day, in IAST with meaning in plain English.','/bhakti/vishnu/','Viṣṇu','#0d3f73','#ffd23f','#eef3fa','/bhakti/vishnu/vishnu-banner.jpg',
 'Thirty songs by the girl-saint Āṇḍāḷ, sung one a day at dawn through the month of Mārgaḻi (Dhanurmāsa, mid-December to mid-January). One illustrated article for each day.',
 [tile('/bhakti/vishnu/tiruppavai/day-1/','#dfe9f6',ANDAL+'<text x="50" y="80" text-anchor="middle" font-size="18" font-family="Georgia" fill="#fff" stroke="none">1</text>','Day 1 of 30','Mārgaḻit Tiṅgaḷ','The first dawn: Āṇḍāḷ calls the girls of Gokula to bathe and to go to Nārāyaṇa for the drum.')])
# --- Triranga tile art + around mysuru
RANG='<path d="M10 70 q40 14 80 0 q-6 10 -40 12 q-34 -2 -40 -12z" fill="#7aa86a"/><circle cx="20" cy="54" r="5" fill="#7aa86a"/><circle cx="14" cy="60" r="5" fill="#7aa86a"/><circle cx="26" cy="60" r="5" fill="#7aa86a"/><path d="M26 66 q30 -14 56 -2" fill="none" stroke="#3b6fd0" stroke-width="10"/><circle cx="28" cy="60" r="8" fill="#3b6fd0"/><path d="M22 52 h12 l-2 -8 h-8z" fill="#ffd60a"/>'
LINGA='<path d="M16 86 h68 l-6 -10 h-56z" fill="#8a8a8a"/><path d="M36 76 v-34 a14 14 0 0 1 28 0 v34z" fill="#3a3a3a"/><path d="M40 46 h20 M40 52 h20 M40 58 h20" stroke="#fff" stroke-width="2.4"/><circle cx="50" cy="66" r="3" fill="#c0392b" stroke="none"/>'
index('bhakti/temples-of-india/around-mysuru','Temples around Mysuru','Illustrated reference guides to the great temples around Mysuru: Nañjanagūḍu, Śrīraṅgapaṭṭaṇa, Śivanasamudra and more.','/bhakti/temples-of-india/','Temples of India','#0b2a4a','#ffd23f','#eef3fa','/bhakti/temples-of-india/temples-banner.jpg',
 'The temples of the Kāverī country around Mysuru: their legends, history, architecture and festivals. Full reference guides, one temple at a time.',
 [tile('/bhakti/temples-of-india/around-mysuru/nanjangud/','#0b2a4a',LINGA,'Śiva · on the Kapilā','Nañjanagūḍu','Śrīkaṇṭheśvara, the Lord who drank the poison: Dakṣiṇa Kāśī, Hakīm Nañjuṇḍa and the five-chariot festival.'),
  tile('/bhakti/temples-of-india/triranga/adi-ranga/','#dcecff',RANG,'Viṣṇu · also in Triraṅga','Ādi Raṅga · Śrīraṅgapaṭṭaṇa','The first Raṅga, on the Kāverī island of Śrīraṅgapaṭṭaṇa: Gautama, the Gaṅgas and Hoysaḷas, and Rāmānuja.'),
  tile('/bhakti/temples-of-india/triranga/madhya-ranga/','#dcecff',RANG,'Viṣṇu · also in Triraṅga','Madhya Raṅga · Śivanasamudra','The middle Raṅga, the youthful Lord on the island of Śivanasamudra, above the great falls of the Kāverī.')])
print('done')
