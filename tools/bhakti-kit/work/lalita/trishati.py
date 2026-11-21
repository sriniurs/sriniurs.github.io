exec(open('/home/claude/work/lalita/lk.py').read())
exec(open('/home/claude/work/lalita/ltx.py').read())
for f in ('la','lb','lc'): exec(open(f'/home/claude/work/lalita/{f}.py').read())
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Lalita seated in red with noose, goad, sugarcane bow and flower arrows, a glowing triangle behind">'
 '<rect width="380" height="268" fill="#4a0c22" rx="8"/><circle cx="190" cy="130" r="110" fill="#ffd60a" opacity=".18"/>'
 '<path d="M190 30 L300 220 L80 220z" fill="none" stroke="#ffd60a" stroke-width="3"/><path d="M190 238 L300 48 L80 48z" fill="none" stroke="#f7a8c4" stroke-width="2"/>'+LAL(190,150,1.5)+'</svg>')
P=dict(nv=59,V=V,per=[20,20,19],out='/home/claude/work/lalita/Lalita_Trishati.html',short='The Lalitā Triśatī',
 title='Lalitā Triśatī · all 300 names explained · srini.presents',
 desc='The Lalitā Triśatī, 300 names of the Goddess Lalitā from the Brahmāṇḍa Purāṇa: all 59 ślokas in IAST, each on two pages with meaning, every name in the key-word table, and a deep dive into the Lalitopākhyāna, Śrīvidyā and Vedānta behind it.',
 burst='HYMNS OF THE GODDESS',h1='LALITĀ TRIŚATĪ',h1size=60,series='ŚRĪ LALITĀ TRIŚATĪ STOTRAM · BRAHMĀṆḌA PURĀṆA',tag='Three hundred names of the Goddess · every śloka explained',cover=cover,
 how='The whole Triśatī <b>in one go</b> for chanting, then <b>every śloka on two pages</b>: first the chant, a picture, the meaning and every name in the key-word table; then a deep dive into the story and ideas behind the names.',
 where=['The <b>Lalitā Triśatī</b>, “three hundred names of Lalitā”, is part of the <b>Lalitopākhyāna</b> in the Brahmāṇḍa Purāṇa. The sage <b>Agastya</b> had already learned the Lalitā Sahasranāma from <b>Hayagrīva</b> and still felt something lacking; Hayagrīva, at the Goddess’s own bidding, then taught him these 300 names.',
  'The names are arranged in fifteen groups of twenty, each group beginning with one syllable of the root mantra of Śrīvidyā. That mantra is given only by a teacher at initiation, and the hymn itself asks that it be kept from the faithless; so we <b>explain every name but do not assemble or explain the mantra</b>. The names themselves are recited openly in temples such as Kāmākṣī at Kāñcī.',
  'There are 59 ślokas, about five names each. A famous commentary on the Triśatī is traditionally ascribed to Ādi Śaṅkara.'],
 wtalk=("Is it OK to chant if I'm not initiated?","Many chant the names with devotion. The initiation is for the mantra, which we don't give."),
 fullnote='Text: as published by Vaidika Vignanam, in IAST, with “ch” written as c and long e and o written plainly, as elsewhere on this site. The pūrvapīṭhikā (opening dialogue) and uttarapīṭhikā (closing phalaśruti) are summarised in the deep dives, not reproduced.',
 secs=[('THE AUSPICIOUS ONE',1),('THE ONE',5),('THE LORD’S POWER',9),('LALITĀ',13),('THE SEED SOUND · I',17),('BELOVED OF ŚIVA',20),('ALL THINGS',24),('KĀMEŚĪ',27),('THE SWAN',30),('THE PLAYFUL ONE',34),('THE SEED SOUND · II',38),('TRUTH, CONSCIOUSNESS, BLISS',43),('KĀMEŚVARA’S BELOVED',46),('ALL ATTAINED',51),('THE SEED SOUND · III',54)],
 end=['<b>1–4.</b> Auspicious, compassionate, reviver of love, witness of every act.','<b>5–12.</b> The One beyond “this” and “that”; Empress of countless worlds; half of Śiva; witness of his dance.',
  '<b>13–23.</b> Lalitā herself; served by Lakṣmī and Sarasvatī; mother of Gaṇeśa; the seed-sound; beloved of Śiva.','<b>24–42.</b> Maker, keeper and ender of all; compassion with a body; the swan; the meaning of every breath; the light in every vessel.',
  '<b>43–59.</b> What the Upaniṣads point to; truth, consciousness, bliss; Kāmeśvara’s breath; all attained; the giver of supreme bliss.'],
 endsub='The Triśatī in five lines',
 next=("What's next?",'More of the Goddess: the <a href="/bhakti/devi/lalita-pancharatnam/">Lalitā Pañcaratnam</a>, the <a href="/bhakti/devi/devi-mahatmya/">Devī Māhātmya</a> and the <a href="/bhakti/devi/ashta-lakshmi/">Aṣṭa Lakṣmī</a>.'),
 endkey='<b>three hundred names, one Mother, and the promise of supreme bliss</b>.',
 foot=('Study notes on the Lalitā Triśatī, Brahmāṇḍa Purāṇa (Lalitopākhyāna, Hayagrīva–Agastya dialogue). Text as published by Vaidika Vignanam. We explain the names but do not reproduce or explain the initiatory mantra on which their order is based. '
  'Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.'),
 tocper=30,endnum=lambda n: str(n))
hymn(P,TX,lambda n: f'ŚLOKA {n}')
recolor(P['out'])
