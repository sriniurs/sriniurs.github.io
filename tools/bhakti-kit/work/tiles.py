R='/home/claude/sriniurs.github.io/'
def tile(href,bg,svg,label,h2,p,read='Read ↗'):
    return f'<li><a href="{href}"><div class="tile-art" style="background:{bg}"><svg class="ill" viewBox="0 0 100 100" aria-hidden="true"><g stroke="#151515" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{svg}</g></svg></div><div class="tile-copy"><strong class="label">{label}</strong><h2>{h2}</h2><p>{p}</p><span class="read">{read}</span></div></a></li>'
DEVI='<circle cx="50" cy="30" r="12" fill="#f2c79b"/><path d="M36 18 h28 l-4 -12 l-6 6 l-4 -8 l-4 8 l-6 -6z" fill="#ffd60a"/><path d="M28 92 q-4 -42 22 -50 q26 8 22 50z" fill="#c0392b"/><path d="M16 60 l18 -4 M84 60 l-18 -4" stroke="#f2c79b" stroke-width="5"/>'
ANDAL='<circle cx="50" cy="34" r="12" fill="#c98b5a"/><path d="M38 26 q12 -16 24 0" fill="#2b1a0e"/><path d="M60 22 q10 -6 12 6" fill="none" stroke="#2b1a0e" stroke-width="6"/><path d="M30 92 q-2 -40 20 -46 q22 6 20 46z" fill="#2e9a5a"/><path d="M34 60 q16 10 32 0" fill="none" stroke="#ffd60a" stroke-width="4"/>'
RANG='<path d="M10 70 q40 14 80 0 q-6 10 -40 12 q-34 -2 -40 -12z" fill="#7aa86a"/><circle cx="20" cy="54" r="5" fill="#7aa86a"/><circle cx="14" cy="60" r="5" fill="#7aa86a"/><circle cx="26" cy="60" r="5" fill="#7aa86a"/><path d="M26 66 q30 -14 56 -2" fill="none" stroke="#3b6fd0" stroke-width="10"/><circle cx="28" cy="60" r="8" fill="#3b6fd0"/><path d="M22 52 h12 l-2 -8 h-8z" fill="#ffd60a"/>'
GOP='<path d="M20 90 h60 l-4 -12 h-52z M26 78 h48 l-4 -12 h-40z M32 66 h36 l-4 -12 h-28z M38 54 h24 l-4 -12 h-16z" fill="#e2cfa8"/><path d="M44 42 l6 -14 l6 14z" fill="#e0a800"/><rect x="44" y="76" width="12" height="14" fill="#5a3a1a"/>'
def ins(path,anchor_href,newtile,after=True):
    s=open(R+path).read(); assert newtile.split('"')[1] not in s, path
    i=s.find(f'<li><a href="{anchor_href}"'); assert i>0,(path,anchor_href); j=s.find('</a></li>',i)+9
    s=s[:j]+newtile+s[j:] if after else s[:i]+newtile+s[i:]
    open(R+path,'w').write(s)
ins('bhakti/devi/index.html','/bhakti/devi/ya-devi-sarvabhuteshu/',tile('/bhakti/devi/devi-mahatmya/','#fde4e4',DEVI,'Series · 6 of 19 parts','Devī Māhātmya','The Durgā Saptaśatī in 19 illustrated parts: Kavacam, Argalā, Kīlakam and all 13 chapters, verse by verse.','Open series ↗'),after=False)
ins('bhakti/vishnu/index.html','/bhakti/vishnu/purusha-suktam/',tile('/bhakti/vishnu/tiruppavai/','#dfe9f6',ANDAL,'Dhanurmāsa · Day 1 of 30','Tiruppāvai','Āṇḍāḷ’s thirty Tamil songs for the dawns of Mārgaḻi, one illustrated article a day.','Open series ↗'),after=False)
ins('bhakti/temples-of-india/index.html','/bhakti/temples-of-india/12-jyotirlingas/',tile('/bhakti/temples-of-india/triranga/','#dcecff',RANG,'4 articles · overview + 3 guides','Triraṅga','Three island temples of Raṅganātha on the Kāverī: Ādi Raṅga, Madhya Raṅga and Antya Raṅga (Śrīraṅgam).','Open series ↗')+tile('/bhakti/temples-of-india/around-mysuru/','#f3e3c3',GOP,'Nañjanagūḍu + 2 Raṅgas','Temples around Mysuru','Reference guides to the great temples of the Kāverī country around Mysuru, starting with Nañjanagūḍu.','Open series ↗'))
h=open(R+'bhakti/index.html').read()
for a,b in [('<strong class="label">7 hymns</strong><h2>Devi</h2><p>','<strong class="label">8 hymns · 13 articles</strong><h2>Devi</h2><p>The Devī Māhātmya series, '),
 ('<strong class="label">8 hymns · 23 articles</strong><h2>Viṣṇu</h2><p>The Puruṣa Sūktam,','<strong class="label">9 hymns · 24 articles</strong><h2>Viṣṇu</h2><p>Āṇḍāḷ’s Tiruppāvai, the Puruṣa Sūktam,'),
 ('<strong class="label">12 Jyotirliṅgas · 13 articles</strong>','<strong class="label">3 series · 18 articles</strong>'),
 ("starting with Śiva's twelve jyotirliṅgas.","the twelve jyotirliṅgas, the Triraṅga and the temples around Mysuru.")]:
    assert a in h,a; h=h.replace(a,b)
open(R+'bhakti/index.html','w').write(h)
print('ok')
