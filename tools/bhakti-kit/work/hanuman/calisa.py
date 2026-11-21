exec(open('/home/claude/work/hanuman/hk.py').read())
exec(open('/home/claude/work/hanuman/ca.py').read())
exec(open('/home/claude/work/hanuman/cb.py').read())
def lab(n):
    if n<=2: return f'DOHĀ {n}'
    if n==43: return 'CLOSING DOHĀ'
    return f'CAUPĀĪ {n-2}'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Hanuman kneeling with folded hands, Rama, Lakshmana and Sita shown in a glowing heart above">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/>'+GLOW(190,90,90,'#ffd60a',.25)+'<path d="M190 150 q-90 -50 -54 -96 q32 -26 54 10 q22 -36 54 -10 q36 46 -54 96z" fill="#e05a8a" stroke="#111" stroke-width="2"/>'+RAMA(190,120,.42)+HANUMAN(190,230,1.0,mace=False,fold=True)+'</svg>')
CH_OK='/bhakti/vishnu/hanuman/'
P=dict(nv=43,V=V,per=[22,21],out='/home/claude/work/hanuman/Hanuman_Chalisa.html',short='The Hanumān Cālīsā',
 title='Hanumān Cālīsā · every verse explained · srini.presents',
 desc='The Hanumān Cālīsā of Tulasīdāsa, every verse explained: the two opening dohās, all forty caupāīs and the closing dohā in IAST, each on two pages with a plain-English meaning, the key words and a deep dive into the story behind it, how it is read and what it means today.',
 burst='HYMNS OF HANUMĀN',h1='HANUMĀN CĀLĪSĀ',h1size=60,series='HANUMĀN CĀLĪSĀ · TULASĪDĀSA · AWADHĪ',tag='Forty verses to the son of the Wind · every verse explained',cover=cover,
 how='The whole Cālīsā <b>in one go</b> for chanting, then <b>every verse on two pages</b>: first the chant, a picture, what it says and the key words; then a deep dive into the story behind it, how it is read and what it means for us today.',
 where=['The <b>Hanumān Cālīsā</b> is the most recited hymn in North India and, today, across the world. Its name means simply “the forty”: forty four-line verses (caupāīs) in Awadhī, framed by two dohās at the start and one at the end, in all 43 verses. Tradition gives it to <b>Tulasīdāsa</b> (c. 1532–1623), the poet of the Rāmacaritamānas, whose name is in its last caupāī.',
  'It moves in a clear arc: an invocation; a portrait of Hanumān; his deeds in the Rāmāyaṇa, from the leap at the sun to the herb that saved Lakṣmaṇa; what he does for those who call on him; and a closing blessing. It takes about ten minutes to chant.',
  f'For his life story, see our <a href="{HB}">Hanumān</a> series. Here we take the hymn verse by verse.'],
 wtalk=("Why is it so popular?","Short, simple, in the people's language, and it promises courage. Everyone needs that."),
 fullnote='Text: the common Gītā Press reading in IAST transliteration of Awadhī. Spellings vary between editions (for example sumirauṃ / sumiro, saṅkara suvana / saṅkara svayaṃ); we note important variants in the deep dives.',
 secs=[('THE INVOCATION',1),('WHO HE IS',3),('WHAT HE DID',11),('WHAT HE GIVES',22),('THE BLESSING',39)],
 end=['<b>Invocation (dohās 1–2).</b> Clean the mirror of the mind; ask for strength, wisdom and learning.',
  '<b>Who he is (1–8).</b> Ocean of wisdom, Rāma’s messenger, thunder-limbed hero, golden, Śiva’s own, eager to serve, lover of Rāma’s story.',
  '<b>What he did (9–19).</b> Small for Sītā, huge for Laṅkā; the herb for Lakṣmaṇa; Rāma’s embrace; Sugrīva and Vibhīṣaṇa made kings; the sun; the ring and the sea.',
  '<b>What he gives (20–36).</b> Hard things made easy; guard of Rāma’s door; no fear, no ghosts, less pain; freedom from trouble; siddhis by Sītā’s boon; the way to Rāma.',
  '<b>Blessing (37–40, closing dohā).</b> Be my guru; recite and be free; Śiva is witness; live in my heart with Rāma, Lakṣmaṇa and Sītā.'],
 endsub='The Cālīsā in five lines',
 next=("What's next?",f'More hymns to Hanumān: the <a href="/bhakti/vishnu/sankatmochan-ashtak/">Saṅkaṭmocan Aṣṭak</a> and the <a href="/bhakti/vishnu/hanuman-slokas/">Sanskrit ślokas</a>. And his story, in the <a href="{HB}">Hanumān</a> series.'),
 endkey='<b>strength, wisdom and a fearless heart, all in Rāma’s service</b>.',
 foot=('Study notes on the Hanumān Cālīsā, attributed to Tulasīdāsa (16th–17th century), in Awadhī. Text follows the common Gītā Press reading, in IAST. Stories are from Vālmīki’s Rāmāyaṇa and Tulasīdāsa’s Rāmacaritamānas; where readings or attributions are disputed, we say so. '
  'Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.'),
 tocper=60,endnum=lambda n: 'dohā' if n in (1,2,43) else str(n-2))
hymn(P,TX,lab)
