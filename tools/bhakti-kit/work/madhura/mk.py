b=open('/home/claude/work/suprabhatam/build1.py').read()
b=b.replace("sys.path.insert(0,'.')","sys.path.insert(0,'.'); sys.path.insert(0,'/home/claude/work/suprabhatam')")
b=b.replace('from sdata1 import V,talk,person,F,SUN,HILL,TEMPLE','from sdata1 import talk,person,F,SUN,HILL,TEMPLE\nfrom mdata import V')
b=b.replace('Śrī Veṅkaṭeśa Suprabhātam · Part 1 · srini.presents','Madhurāṣṭakam · srini.presents')
b=b.replace('Kausalyā suprajā rāma: the Śrī Veṅkaṭeśa Suprabhātam, Part 1 (verses 1–15), explained verse by verse in plain English with illustrations: the dawn hymn of Tirumala.','Adharaṃ madhuram: Vallabhācārya’s Madhurāṣṭakam, the hymn to Kṛṣṇa’s sweetness, explained verse by verse in plain English with illustrations.')
b=b.replace('<div class="burst yel">PART 1 OF 5</div>','<div class="burst yel">8 VERSES</div>')
b=b.replace('<h1 style="font-size:clamp(26px,7.6vw,72px)">ŚRĪ VEṄKAṬEŚA<br>SUPRABHĀTAM</h1>','<h1 style="font-size:clamp(24px,7vw,80px)">MADHURĀṢṬAKAM</h1>')
b=b.replace('PART 1 · VERSES 1–15 · THE WORLD WAKES UP','ŚRĪ VALLABHĀCĀRYA · THE SWEETNESS OF KṚṢṆA')
b=b.replace('The dawn hymn of Tirumala · explained and illustrated','“Adharaṃ madhuram” · explained and illustrated')
b=b.replace('First Part 1 for chanting in one go.','First the whole hymn for chanting in one go.')
i=b.index("cover=("); j=b.index("story_svg=(")
b=b[:i]+open('cover.txt').read()+b[j:]
i=b.index('<section class="page" id="foreword">'); j=b.index('<section class="page" id="contents">')
b=b[:i]+open('front.txt').read()+b[j:]
b=b.replace('<a href="#full">Part 1 in One Go</a>','<a href="#full">The Madhurāṣṭakam in One Go</a>').replace('<a href="#story">The Story: A Morning Call, 600 Years Old</a>','<a href="#story">The Story: A Midnight Vision</a>').replace('<a href="#about">About the Suprabhātam</a>','<a href="#about">About the Madhurāṣṭakam</a>').replace('<a href="#end">Part 1 on One Page</a>','<a href="#end">The Madhurāṣṭakam on One Page</a>').replace('VERSES 1–15</li>','THE 8 VERSES</li>')
i=b.index('<section class="page" id="end">'); j=b.index('<div class="follow">',i)
b=b[:i]+open('end.txt').read()+b[j:]
i=b.index('<footer'); j=b.index('</footer>')
b=b[:i]+'<footer style="text-align:center;font-size:13px;opacity:.75">Study notes on the Madhurāṣṭakam of Śrī Vallabhācārya. Text checked word by word against shlokam.org and the Wikipedia article “Madhurāṣṭakam”; variant readings (smaraṇam, bhuktam) are noted. Background: Wikipedia (author, legend of composition, Puṣṭimārga); shlokam.org. Vallabha’s dates differ slightly between sources (1478 or 1479–1531). Meanings of vamitam and śamitam vary between commentators. Meanings are our own plain-English renderings. Zappy and Prof. Bolt are fictional.'+b[j:]
b=b.replace("open('Venkatesa_Suprabhatam_Part1.html','w')","open('Madhurashtakam.html','w')")
open('build.py','w').write(b)
