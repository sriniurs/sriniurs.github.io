exec(open('/home/claude/work/up_lib.py').read())
src=open('/home/claude/work/upload_all.py').read()
import re
RANG=re.search(r"\nRANG=(.*)\n",src).group(1); RANG=eval(RANG)
T='bhakti/temples-of-india/triranga'
RIVER='<path d="M0 60 q25 -14 50 0 q25 14 50 0 v40 h-100z" fill="#5ab0f0"/>'+''.join(f'<ellipse cx="{x}" cy="58" rx="9" ry="5" fill="#8ab070"/><path d="M{x-5} 54 l5 -10 l5 10z" fill="#d9782f"/>' for x in (20,50,80))
tiles=[tile(f'/{T}/overview/','#0b2a4a',RIVER,'Start here · overview','Triraṅga Darśanam','The three Raṅganātha temples on the Kāverī islands, and the tradition of seeing all three in one day.'),
 tile(f'/{T}/adi-ranga/','#dcecff',RANG,'1 · Ādi Raṅga · Karnataka','Śrīraṅgapaṭṭaṇa','The first Raṅga: Gautama and the Kāverī, the Gaṅgas, Hoysaḷas, Vijayanagara and the Mysore kings.'),
 tile(f'/{T}/madhya-ranga/','#dcecff',RANG,'2 · Madhya Raṅga · Karnataka','Śivanasamudra','The middle Raṅga, the youthful Jaganmohana Raṅga between the great falls of the Kāverī.'),
 tile(f'/{T}/antya-ranga/','#dcecff',RANG,'3 · Antya Raṅga · Tamil Nadu','Śrīraṅgam','The last Raṅga and first of the 108 Divya Deśams: Vibhīṣaṇa’s vimāna, the Āḻvārs and Rāmānuja.')]
index(T,'Triraṅga','Triraṅga Darśanam: the three Raṅganātha temples on the islands of the Kāverī, Ādi Raṅga at Śrīraṅgapaṭṭaṇa, Madhya Raṅga at Śivanasamudra and Antya Raṅga at Śrīraṅgam, in illustrated reference guides.','/bhakti/temples-of-india/','Temples of India','#0b2a4a','#ffd23f','#eef3fa','/bhakti/temples-of-india/temples-banner.jpg',
 'Three Raṅganāthas on three islands of the Kāverī, from Karnataka to Tamil Nadu. Start with the overview, then visit each Raṅga.',tiles)
print('ok')
