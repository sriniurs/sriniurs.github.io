import re,importlib,sys
k=open('/home/claude/srini-bhakti/temples-of-india/kerala/index.html').read()
def hub(base,out,T,D,parts,labels,bg):
    s=k
    s=re.sub(r'<title>.*?</title>',f'<title>{T} · Srini Presents</title>',s)
    s=s.replace('An illustrated overview of Kerala temple architecture and ten guides to Kerala’s shrines, pilgrimages and living traditions.',D)
    s=s.replace('https://bhakti.srinipresents.com/temples-of-india/kerala/','https://bhakti.srinipresents.com'+base)
    s=s.replace('content="Temples of Kerala"',f'content="{T}"').replace('<h1>Temples of Kerala</h1>',f'<h1>{T}</h1>')
    s=s.replace('/temples-of-india/kerala/banner.svg',base+'banner.svg').replace('alt="Kerala-style temple roofs, palms and a ceremonial boat"',f'alt="{T}"')
    s=s.replace('<a class="sr-reader-back" href="/temples-of-india/">','<a class="sr-reader-back" href="/festivals/">')
    s=s.replace('<p class="bhakti-breadcrumb"><a href="/temples-of-india/">Temples and Tīrthas</a></p>','<p class="bhakti-breadcrumb"><a href="/festivals/">Festivals</a></p>')
    s=s.replace('aria-label="Temples of Kerala articles"',f'aria-label="{T} articles"')
    tiles=''.join(f'<li><a href="{base}{slug}/"><div class="tile-art"><img src="{base}{slug}/cover.svg" width="380" height="268" alt="" loading="lazy"></div><div class="tile-copy"><strong class="label">{labels[n]}</strong><h2>{title}</h2><p>{tag}</p></div></a></li>\n' for n,(slug,title,tag) in enumerate(parts))
    s=re.sub(r'(<ol class="tiles"[^>]*>).*?(</ol>)',lambda m:m.group(1)+tiles+m.group(2),s,flags=re.S)
    open(out+'index.html','w').write(s)
    inner=re.search(r'<svg[^>]*>(.*)</svg>',open(out+parts[0][0]+'/cover.svg').read(),re.S).group(1)
    open(out+'banner.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800"><rect width="1200" height="800" fill="{bg}"/><g transform="translate(90 40) scale(2.7)">{inner}</g></svg>')
import ek_data
from ek_more import M as _M
_ORD=[x for _,_,ks,_ in ek_data.MONTHS for x in ks]; _MON={x:m for _,m,ks,_ in ek_data.MONTHS for x in ks}
EKP=[('overview','What Ekādaśī Is','The Eleventh Day and the Goddess Who Slew Mura'),('keeping-the-vow','Keeping the Vow','Fasting, the Night, and Breaking the Fast')]+[(x,ek_data.EK[x]['name'].split(' (')[0]+' Ekādaśī',f"{_MON[x]}, {ek_data.EK[x]['pak']} fortnight: {ek_data.EK[x]['mean']}") for x in _ORD]
hub('/festivals/ekadashi/','outx/ekadashi/','Ekādaśī','An illustrated 28-part guide to Ekādaśī: what the eleventh day is, how the vow is kept, and each of the 26 named Ekādaśīs of the year in its own article, with its story, meaning and customs.',EKP,['Part 1 · Overview','Part 2 · Practice']+[f'Part {n+3} · {_MON[x]}' for n,x in enumerate(_ORD)],'#e3eaf3')
KP=[('overview','Kārtika Māsa','The Month of Lamps'),('damodarashtakam','The Dāmodarāṣṭakam','Kṛṣṇa Bound with a Rope'),('somavara-lakshadipotsava','Kārtika Somavāras','Śiva’s Mondays and the Lakṣa Dīpotsava'),('karthigai-deepam','Kārttikai Dīpam','The Flame on Aruṇācala'),('tulasi','Tulasī','The Sacred Plant in the Courtyard'),('prabodhini-tulasi-vivaha','Prabodhinī and Tulasī Vivāha','Viṣṇu Wakes, Tulasī Weds'),('kartika-purnima','Kārtika Pūrṇimā','Tripurāri and the River of Lamps')]
hub('/festivals/kartika/','outx/kartika/','Kārtika Māsa','An illustrated 7-part guide to Kārtika, the month of lamps: the Dāmodarāṣṭakam, Śiva’s Mondays and the Lakṣa Dīpotsava, Kārttikai Dīpam, Tulasī and her wedding, and Kārtika Pūrṇimā.',KP,[f'Part {n+1}' for n in range(7)],'#e3eaf3')
PP=[('overview','Pitṛ Pakṣa','The Fortnight of the Ancestors'),('shraddha-tarpana','Śrāddha and Tarpaṇa','What the Rites Mean'),('mahalaya-amavasya','Mahālaya Amāvāsyā','The New Moon for All Ancestors'),('places','The Places of Śrāddha','Gayā, Kāśī, Prayāga and Śrīraṅgapaṭṇa'),('after-death','What Happens After Death','The Tradition’s Map, and the Garuḍa Purāṇa')]
hub('/festivals/pitru-paksha/','outx/pitru-paksha/','Pitṛ Pakṣa and Mahālaya','An illustrated 5-part guide to Pitṛ Pakṣa, the fortnight of the ancestors: śrāddha and tarpaṇa, Mahālaya Amāvāsyā, the places of śrāddha, and what the tradition says happens after death.',PP,[f'Part {n+1}' for n in range(5)],'#e3eaf3')
GP=[('vyasa-purnima','Vyāsa Pūrṇimā','The Sage Who Arranged the Veda'),('the-guru','The Guru','“Gurur Brahmā” and the Silent Teacher'),('chaturmasya','Cāturmāsya Begins','The Ascetics’ Rainy-Season Retreat')]
hub('/festivals/guru-purnima/','outx/guru-purnima/','Guru Pūrṇimā','An illustrated 3-part guide to Guru Pūrṇimā: Vyāsa, the guru and the Guru Gītā verses, Dakṣiṇāmūrti, and the start of Cāturmāsya.',GP,[f'Part {n+1}' for n in range(3)],'#e3eaf3')
SP=[('upakarma','Upākarma','Renewing the Thread and the Veda'),('raksha-bandhan','Rakṣā Bandhan','The Thread of Protection')]
hub('/festivals/shravana-purnima/','outx/shravana-purnima/','Śrāvaṇa Pūrṇimā','An illustrated 2-part guide to Śrāvaṇa Pūrṇimā: Upākarma and Hayagrīva Jayantī, and Rakṣā Bandhan with its stories.',SP,[f'Part {n+1}' for n in range(2)],'#e3eaf3')
DP=[('overview','Dhanurmāsa','The Month of Dawn Worship'),('andal-tiruppavai','Āṇḍāḷ and the Tiruppāvai','A Girl’s Vow for the Lord'),('in-temples','Dhanurmāsa in Temples','Tirumala, Śrīraṅgam and the Triraṅga'),('at-home','Dhanurmāsa at Home','Rangoli, Huggi and the Road to Saṅkrānti')]
hub('/festivals/dhanurmasa/','outx/dhanurmasa/','Dhanurmāsa','An illustrated 4-part guide to Dhanurmāsa, the month of dawn worship: Āṇḍāḷ and the Tiruppāvai, the month in Tirumala, Śrīraṅgam and the Triraṅga temples, and rangoli, huggi and Saṅkrānti at home.',DP,[f'Part {n+1}' for n in range(4)],'#e3eaf3')
print('hubs ok')
PRP=[('overview','Pradoṣa','Śiva’s Twilight, Twice a Month'),('nilakantha','Nīlakaṇṭha','The Poison, the Blue Throat and the Dance on Nandi'),('vrata-katha','The Pradoṣa Vrata Kathā','Śāṇḍilya, the Widow and the Two Boys'),('pradosha-stotram','The Pradoṣa Stotrāṣṭakam','The Hymn of the Twilight Hour'),('keeping-the-vow','Keeping the Pradoṣa Vow','The Fast, the Hour and the Worship'),('weekday-pradoshas','The Seven Pradoṣas','Soma, Bhauma, Śani and the Rest'),('in-temples','Pradoṣa in Temples','Nandi, the Crescent Path and the Procession'),('masa-shivaratri','Māsa Śivarātri','The Night After Pradoṣa')]
hub('/festivals/pradosha/','outx/pradosha/','Pradoṣa','An illustrated 8-part guide to Pradoṣa, Śiva’s twilight on Trayodaśī: the Nīlakaṇṭha story, the vrata kathā, the Pradoṣa hymn verse by verse, keeping the vow, the seven weekday Pradoṣas, Pradoṣa in temples and Māsa Śivarātri.',PRP,[f'Part {n+1}' for n in range(8)],'#e3eaf3')
