b=open('build4.py').read()
b=b.replace('from sdata4 import V','from sdata5 import V')
b=b.replace('Part 4 · Prapatti · srini','Part 5 · Maṅgalāśāsanam · srini').replace('Part 4, the Śrī Veṅkaṭeśa Prapatti (16 verses of surrender)','Part 5, the Śrī Veṅkaṭeśa Maṅgalāśāsanam (14 verses of blessing)')
b=b.replace("Part4.html'","Part5.html'")
b=b.replace('PART 4 OF 5','PART 5 OF 5').replace('PART 4 · THE PRAPATTI · 16 VERSES OF SURRENDER','PART 5 · THE MAṄGALĀŚĀSANAM · 14 BLESSINGS')
i=b.index('<section class="page" id="foreword">'); j=b.index('<section class="page" id="contents">')
new=open('front5.txt').read()
b=b[:i]+new+b[j:]
b=b.replace('<a href="#foreword">From Praise to Surrender</a>','<a href="#foreword">The Last Word: Maṅgalam</a>').replace('<a href="#full">The Prapatti in One Go</a>','<a href="#full">The Maṅgalāśāsanam in One Go</a>').replace('<a href="#story">The Shape of the Prapatti</a>','<a href="#story">The Shape of the Maṅgalāśāsanam</a>').replace('<a href="#end">Part 4 on One Page</a>','<a href="#end">The Whole Suprabhātam on One Page</a>').replace('THE 16 VERSES</li>','THE 14 VERSES</li>')
i=b.index('<section class="page" id="end">'); j=b.index('<div class="follow">',i)
b=b[:i]+open('end5.txt').read()+b[j:]
b=b.replace('Study notes on the Śrī Veṅkaṭeśa Prapatti (section 3 of the Suprabhātam). Key words checked against shlokam.org; Vedic and Gītā references: Ṛg Veda 1.154.5, Bhagavad Gītā 18.66','Study notes on the Śrī Veṅkaṭeśa Maṅgalāśāsanam (section 4 of the Suprabhātam). Key words checked against shlokam.org')
b=b.replace('<li><span class="num">🔤</span><a href="#full">','<li><span class="num">🔤</span><a href="#full">')
open('build5.py','w').write(b)
