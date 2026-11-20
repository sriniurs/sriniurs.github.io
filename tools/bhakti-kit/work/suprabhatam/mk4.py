b=open('build3.py').read()
b=b.replace('from sdata3 import V','from sdata4 import V')
b=b.replace('Part 3 · Stotram · srini','Part 4 · Prapatti · srini').replace('Part 3, the Śrī Veṅkaṭeśa Stotram (11 verses)','Part 4, the Śrī Veṅkaṭeśa Prapatti (16 verses of surrender)')
b=b.replace("Part3.html'","Part4.html'")
b=b.replace('PART 3 OF 5','PART 4 OF 5').replace('PART 3 · THE STOTRAM · 11 VERSES OF PRAISE','PART 4 · THE PRAPATTI · 16 VERSES OF SURRENDER')
i=b.index('<section class="page" id="foreword">'); j=b.index('<section class="page" id="contents">')
new=open('front4.txt').read()
b=b[:i]+new+b[j:]
b=b.replace('<a href="#foreword">Now That He Is Awake</a>','<a href="#foreword">From Praise to Surrender</a>').replace('<a href="#full">The Stotram in One Go</a>','<a href="#full">The Prapatti in One Go</a>').replace('<a href="#story">The Shape of the Stotram</a>','<a href="#story">The Shape of the Prapatti</a>').replace('<a href="#end">Part 3 on One Page</a>','<a href="#end">Part 4 on One Page</a>').replace('THE 11 VERSES</li>','THE 16 VERSES</li>')
i=b.index('<section class="page" id="end">'); j=b.index('<div class="follow">',i)
b=b[:i]+open('end4.txt').read()+b[j:]
b=b.replace('Study notes on the Śrī Veṅkaṭeśa Stotram (section 2 of the Suprabhātam). Text checked word by word against shlokam.org and sanskritdocuments.org','Study notes on the Śrī Veṅkaṭeśa Prapatti (section 3 of the Suprabhātam). Key words checked against shlokam.org; Vedic and Gītā references: Ṛg Veda 1.154.5, Bhagavad Gītā 18.66')
b=b.replace('Metre names are from standard prosody.','Metre names are from standard prosody; readings of the Lord’s hand gestures are traditional interpretations.')
open('build4.py','w').write(b)
