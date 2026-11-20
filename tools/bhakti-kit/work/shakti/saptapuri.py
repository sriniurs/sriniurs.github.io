exec(open('/home/claude/work/shakti/common_s.py').read())
import common_t
def head_navy(title,desc):
    h=open(common_t.SRC).read(); hd=h[:h.find('<div class="book">')]
    hd=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',hd,flags=re.S)
    return re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',hd)
head=head_navy('The Saptapurī · Seven Cities of Liberation · srini.presents',
 'The Saptapurī, the seven mokṣapurīs of Hindu tradition: Ayodhyā, Mathurā, Māyā (Haridvār), Kāśī, Kāñcī, Avantikā (Ujjain) and Dvārakā. The Purāṇic verse word by word, a map, each city on its own page, the “Purī” question, and how the seven connect to the Jyotirliṅgas and Śakti Pīṭhas. An illustrated reference guide.')
C=[ # key, verse name, modern, state, lat, lon, deity, river, colour
 ('ayodhya','Ayodhyā','Ayodhyā','Uttar Pradesh',26.80,82.20,'Rāma','Sarayū'),
 ('mathura','Mathurā','Mathurā','Uttar Pradesh',27.49,77.67,'Kṛṣṇa','Yamunā'),
 ('maya','Māyā','Haridvār','Uttarakhand',29.95,78.16,'Gaṅgā; Śiva and Viṣṇu','Gaṅgā'),
 ('kashi','Kāśī','Vārāṇasī','Uttar Pradesh',25.32,83.01,'Śiva as Viśvanātha','Gaṅgā'),
 ('kanchi','Kāñcī','Kāñcīpuram','Tamil Nadu',12.83,79.70,'Śiva, Viṣṇu and Kāmākṣī','Vegavatī and Pālār'),
 ('avantika','Avantikā','Ujjain','Madhya Pradesh',23.18,75.77,'Śiva as Mahākāla','Kṣiprā'),
 ('dvaraka','Dvārāvatī','Dvārakā','Gujarat',22.24,68.97,'Kṛṣṇa as Dvārakādhīśa','Gomatī and the sea')]
def sevmap(hi=None,w=230,h=190,scale=.52,tx=12,ty=-4,big=False):
    g=''
    for i,(k,vn,mn,st,la,lo,*_) in enumerate(C):
        x,y=xy(la,lo); on = hi is None or k==hi
        if on:
            g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{10 if big else 7}" fill="#1d4f9a" stroke="#111" stroke-width="1.5"/>'
            g+=T(f'{x:.0f}',f'{y+4:.0f}',str(i+1),11,'#fff') if big else T(f'{x+(10 if x<215 else -10):.0f}',f'{y+4:.0f}',mn,13,'#111','start' if x<215 else 'end')
        else: g+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#bbb" stroke="#111" stroke-width="1.2"/>'
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Map of India marking the seven sacred cities"><rect width="{w}" height="{h}" fill="#eef3fa"/><g transform="translate({tx} {ty}) scale({scale})">'+LAND().replace('#f4e6d0','#e8eedf')+g+'</g></svg>'
def GHAT(y,w=560): return ''.join(f'<rect x="{k*40}" y="{y-k%3*4}" width="40" height="{14+k%3*4}" fill="#e2cfa8" stroke="#111" stroke-width="1"/>' for k in range(w//40))
def RIVER(y,w=560,h=30): return f'<rect y="{y}" width="{w}" height="{h}" fill="#4aa3df"/>'+''.join(f'<path d="M{k*46} {y+10+(k%2)*10} q10 -6 20 0" stroke="#fff" stroke-width="2" fill="none"/>' for k in range(w//46))
def SHIKH(x,y,s=1,c='#f2e6c8',flag='#ff8c1a'): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.6"><rect x="-30" y="-24" width="60" height="24" fill="{c}"/><path d="M-22 -24 Q-20 -70 0 -90 Q20 -70 22 -24z" fill="{c}"/>'+''.join(f'<path d="M{-18+j*6} -30 Q{-14+j*4} -60 0 -86" fill="none" stroke-width="1"/>' for j in range(7))+f'<path d="M0 -90 v-22" /><path d="M0 -112 l18 6 l-18 6z" fill="{flag}"/></g>'
def LAMP(x,y): return f'<g transform="translate({x} {y})" stroke="#111" stroke-width="1.5"><path d="M-8 0 q8 6 16 0 l-2 -4 h-12z" fill="#c98b2a"/><path d="M0 -4 q-4 -8 0 -14 q4 6 0 14z" fill="#ffd60a"/></g>'
RAMA=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,'#ffd60a','#3fa36b',1)+'<path d="M-12 -40 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800" stroke="#111" stroke-width="1.5"/><path d="M24 -40 q12 30 0 60" stroke="#7a5a2a" stroke-width="3" fill="none"/><path d="M24 -40 v60" stroke="#ccc"/></g>'
KRSNA=lambda x,y,s=1: f'<g transform="translate({x} {y}) scale({s})">'+person(0,0,'#ffd60a','#3b6fd0',1)+'<path d="M-12 -40 h24 l-3 -12 l-5 5 l-4 -9 l-4 9 l-5 -5z" fill="#e0a800" stroke="#111" stroke-width="1.5"/><path d="M4 -48 q10 -16 14 -6" stroke="#2a9d6f" stroke-width="3" fill="none"/><path d="M-26 -10 l52 -8" stroke="#7a5a2a" stroke-width="4"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Seven temple towers in a row on a river bank at sunrise, each a different style, with lamps floating on the water">'
 '<rect width="380" height="268" fill="#0b2a4a" rx="8"/><circle cx="190" cy="80" r="44" fill="#ffd166" opacity=".55"/>'+RIVER(210,380,58)
 +''.join(SHIKH(30+k*53,206,.55+(.12 if k==3 else 0),'#f2e6c8' if k%2 else '#e2cfa8') for k in range(7))+''.join(LAMP(40+k*60,236+(k%2)*12) for k in range(6))+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Saptapurī','The “seven cities”, also called the <b>mokṣapurīs</b>: cities said to grant liberation'),
 ('The seven','<b>Ayodhyā</b>, <b>Mathurā</b>, <b>Māyā</b> (Haridvār), <b>Kāśī</b>, <b>Kāñcī</b>, <b>Avantikā</b> (Ujjain), <b>Dvārakā</b>'),
 ('The verse','One śloka, found in the <b>Garuḍa</b>, <b>Nārada</b> and <b>Skanda</b> Purāṇas'),
 ('Mokṣa','Liberation from the cycle of birth and death'),
 ('Who','Two of Viṣṇu’s avatāras (Ayodhyā, Mathurā, Dvārakā), Śiva (Kāśī, Ujjain), the Gaṅgā (Haridvār), and Śiva, Viṣṇu and the Goddess together (Kāñcī)'),
 ('South','Only <b>Kāñcī</b> lies in the South; the other six are in the North and West'),
 ('Question','Is “Purī” in the verse a word, or an eighth city, Jagannātha Purī?')])
 +talk("Seven cities that can free you from rebirth?","That's the promise. Live, worship or die in one of them, the texts say, and the wheel stops turning.")))
pages.append('''<section class="page" id="verse"><h2 class="page-title">THE VERSE</h2>
<div class="sloka" style="margin-top:4px">
<div class="sloka-head"><span class="theme" style="font-size:22px">SEVEN CITIES THAT GIVE LIBERATION</span></div>
<div class="iast"><span class="cl">ayodhyā mathurā māyā</span><span class="cl">kāśī kāñcī avantikā |</span><span class="cl">purī dvārāvatī caiva</span><span class="cl">saptaitā mokṣadāyikāḥ ‖</span></div>
<div class="vfig">'''+sevmap()+'''<div class="mean">Ayodhyā, Mathurā, Māyā, Kāśī, Kāñcī, Avantikā, and the city of Dvārāvatī too: these seven are the givers of liberation.</div></div>
<div class="plain">Seven cities, named in one breath: from Rāma’s city to Kṛṣṇa’s, by way of the Gaṅgā, Śiva’s Kāśī, the southern Kāñcī and Ujjain.</div>
<table class="ct"><tr><th>Word</th><th>Means</th></tr>
<tr><td class="w">māyā</td><td><b>Māyāpurī</b>: Haridvār</td></tr><tr><td class="w">avantikā</td><td><b>Avanti</b>: Ujjain</td></tr>
<tr><td class="w">purī dvārāvatī</td><td>“the <b>city</b> Dvārāvatī”: Dvārakā (but see next page)</td></tr><tr><td class="w">caiva</td><td>“and also”</td></tr>
<tr><td class="w">sapta etāḥ</td><td><b>these seven</b></td></tr><tr><td class="w">mokṣadāyikāḥ</td><td><b>givers of liberation</b></td></tr></table>
</div>
<div class="panel reading small"><p><b>Where it comes from.</b> The verse appears in the <b>Garuḍa Purāṇa</b> (in its section on the dead), the <b>Nārada Purāṇa</b>, and in a slightly different order in the <b>Kāśī Khaṇḍa</b> of the Skanda Purāṇa. Some versions read <i>jñeyāḥ</i>, “should be known”, for <i>caiva</i>.</p></div>
</section>
''')
pages.append(page('puri','SEVEN OR EIGHT?','The little word “purī”',fig(560,130,'Two readings side by side: seven city pins, and eight pins with Puri added on the east coast',
 '<rect width="560" height="130" fill="#eef3fa"/>'+''.join(f'<circle cx="{40+k*28}" cy="60" r="10" fill="#1d4f9a" stroke="#111"/>' for k in range(7))+T(124,100,'SEVEN CITIES',13,'#0b2a4a')
 +''.join(f'<circle cx="{330+k*28}" cy="60" r="10" fill="{"#c0392b" if k==6 else "#1d4f9a"}" stroke="#111"/>' for k in range(8))+T(428,100,'EIGHT, WITH PURĪ?',13,'#7a1d12'))+'''<div class="g2">
<div class="card bg-blue"><h4>📖 Reading 1: seven</h4><p><i>Purī</i> simply means “city”: “the <b>city</b> Dvārāvatī”. The verse itself says <i>sapta</i>, seven, so this is the usual reading.</p></div>
<div class="card bg-red"><h4>📖 Reading 2: Purī the city</h4><p>Some take <i>Purī</i> as <b>Jagannātha Purī</b> in Odisha. Then there are eight names for seven places, so one list drops Māyā and keeps Purī.</p></div>
</div>'''+talk("So is Jagannātha Purī one of the seven or not?","Most lists say no: it's one of the four Dhāms instead. But you'll find books that slip it in.")))
bm=''
for i,(k,vn,mn,st,la,lo,*_) in enumerate(C):
    x,y=xy(la,lo); bm+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="10" fill="#1d4f9a" stroke="#111" stroke-width="1.5"/>'+T(f'{x:.0f}',f'{y+4:.0f}',str(i+1),11,'#fff')
key=''.join(T(452,50+i*26,f'{i+1} {c[2]}',14,'#111','start') for i,c in enumerate(C))
pages.append(page('map','THE SEVEN ON ONE MAP','Six in the North and West, one in the South',fig(560,470,'Simplified map of India with the seven sacred cities numbered in the order of the verse',
 '<rect width="560" height="470" fill="#eef3fa"/><g transform="translate(-14 4) scale(1.3)">'+LAND().replace('#f4e6d0','#e8eedf')+bm+'</g><rect x="440" y="24" width="114" height="200" fill="#fff" stroke="#111" stroke-width="2"/>'+key+T(436,462,'Outline simplified; not an official boundary.',11,'#555','end'))
 +'<div class="key">Three rivers hold four of them: <b>Gaṅgā, Yamunā, Sarayū</b>. Kāñcī stands alone in the South.</div>'))
def city(k,title,sub,art,rows,talkq,talka,extra=''):
    c=[x for x in C if x[0]==k][0]
    return page(k,title,sub,'<div class="g2" style="align-items:center"><div>'+fig(270,200,art[0],art[1])+'</div><div>'+sevmap(k)+'</div></div>'+facts(rows)+extra+talk(talkq,talka))
pages.append(city('ayodhya','1 · AYODHYĀ','Rāma’s city on the Sarayū',('Rama with his bow before a temple tower by the Sarayu river, lamps on the ghats',
 '<rect width="270" height="200" fill="#fff4cd"/>'+RIVER(170,270,30)+GHAT(160,270)+SHIKH(170,156,1.0)+RAMA(70,130,1.1)+''.join(LAMP(30+k*40,178) for k in range(6))),
 [('Name','Ayodhyā, “the unconquerable”; also Sāketa'),('River','The <b>Sarayū</b> (Ghaghara)'),('Story','Birthplace and capital of <b>Rāma</b>; where the Rāmāyaṇa begins and ends'),
  ('Temples','Hanumān Gaṛhī, Kanak Bhavan, and more than a hundred others'),('Today','The <b>Rāma Janmabhūmi</b> temple, consecrated in <b>January 2024</b> after the Supreme Court’s 2019 judgment in the long dispute over the site'),
  ('Festival','Dīpāvalī, Rāma’s homecoming, with lamps along the Sarayū')],
 "Is this the Ayodhyā of the Rāmāyaṇa?","Tradition says yes, and has for many centuries. Archaeologists debate the early layers; devotees don't."))
pages.append(city('mathura','2 · MATHURĀ','Kṛṣṇa’s birthplace on the Yamunā',('Baby Krishna in a basket carried across the Yamuna in rain by his father, a temple on the bank',
 '<rect width="270" height="200" fill="#dfe8f5"/>'+RIVER(150,270,50)+''.join(f'<path d="M{a} {b} l-4 10" stroke="#1d4f9a" stroke-width="2"/>' for a,b in ((20,20),(60,40),(100,14),(180,30),(230,50),(250,16)))+person(110,150,'#ffd60a','#c98b5a',1.1)+'<ellipse cx="110" cy="100" rx="22" ry="8" fill="#c98b2a" stroke="#111" stroke-width="1.5"/><circle cx="110" cy="96" r="6" fill="#3b6fd0" stroke="#111"/>'+SHIKH(220,150,.8)),
 [('Name','Mathurā, “churned”; also Madhupurī'),('River','On the right bank of the <b>Yamunā</b>'),('Story','Birthplace of <b>Kṛṣṇa</b> in Kaṃsa’s prison; heart of <b>Braj</b>, with Vṛndāvana nearby'),
  ('Sites','The Kṛṣṇa Janmasthān complex, Viśrām Ghāṭ and its evening ārati'),('History','A great centre of art under the Kuṣāṇas; the Janmasthān stands beside the Shāhī Īdgāh mosque, and the site’s history is before the courts'),
  ('Festival','Janmāṣṭamī and Holī')],
 "Why do people walk around the whole region?","Braj parikramā: the land itself is Kṛṣṇa's playground. Mathurā is the gate."))
pages.append(city('maya','3 · MĀYĀ · HARIDVĀR','Where the Gaṅgā leaves the hills',('The Ganga flowing out of green hills past a clock-tower ghat, crowds bathing, evening lamps',
 '<rect width="270" height="200" fill="#e7f0d8"/>'+HILL(70,120,160,80,'#3a7a3a')+HILL(200,120,160,90,'#4a8a4a')+RIVER(120,270,80)+GHAT(196,270)+'<rect x="180" y="150" width="20" height="46" fill="#c98b6a" stroke="#111"/><circle cx="190" cy="148" r="8" fill="#fff" stroke="#111"/>'+''.join(LAMP(20+k*36,140+(k%3)*14) for k in range(7))),
 [('Name','<b>Māyāpurī</b>, after the Goddess <b>Māyā Devī</b>; Haridvār (“gate of Hari”) or Haradvār (“gate of Hara”)'),('River','The <b>Gaṅgā</b>, just as she reaches the plains'),
  ('Sites','<b>Har kī Pauṛī</b> and the Brahmakuṇḍ; the Māyā Devī temple, counted among the Śakti Pīṭhas'),('Story','One of the four places where drops of <b>amṛta</b> fell from the pot of nectar'),
  ('Festivals','The <b>Kumbha Melā</b> every twelve years; the evening Gaṅgā ārati every day')],
 "Gate of Hari or gate of Hara?","Both! Vaiṣṇavas say Hari, Śaivas say Hara. The Gaṅgā doesn't mind."))
pages.append(city('kashi','4 · KĀŚĪ','Śiva’s city that he never leaves',('Steps of ghats down to the Ganga, a cremation fire burning, a golden-spired temple above',
 '<rect width="270" height="200" fill="#fde9c4"/>'+RIVER(160,270,40)+''.join(f'<rect x="0" y="{150-k*12}" width="270" height="12" fill="{"#e2cfa8" if k%2 else "#d6c09a"}" stroke="#111" stroke-width="1"/>' for k in range(4))+SHIKH(180,100,.85,'#ffd60a')+'<path d="M50 150 q-8 -20 6 -34 q2 14 8 14 q4 -10 2 -18 q12 16 -2 38z" fill="#ff8c1a" stroke="#111"/>'+T(56,170,'MAṆIKARṆIKĀ',9,'#fff')),
 [('Name','Kāśī, “the shining”; Vārāṇasī (between the Varuṇā and Asi); <b>Avimukta</b>, “never released”'),('River','The <b>Gaṅgā</b>, flowing north here'),
  ('Lord','Śiva as <b>Viśvanātha</b>, a <a href="/bhakti/temples-of-india/12-jyotirlingas/kashi-vishwanath/">jyotirliṅga</a>; the Goddess as <b>Viśālākṣī</b>, a Śakti Pīṭha'),
  ('Belief','Whoever dies in Kāśī is freed: Śiva himself whispers the saving mantra in the dying ear'),('Sites','Some 80 ghāṭs, with <b>Maṇikarṇikā</b> where the cremation fires never go out')],
 "Why is Kāśī the most famous of the seven?","Because of that promise about dying. People still come to Kāśī to spend their last days."))
pages.append(city('kanchi','5 · KĀÑCĪ','The one in the South',('Several temple gopuras of a southern city skyline, the Goddess seated in the centre',
 '<rect width="270" height="200" fill="#fdf1e8"/>'+''.join(f'<g transform="translate({x} 190) scale({s})" stroke="#111" stroke-width="1.6">'+''.join(f'<path d="M{-30+j*3} {-j*12} h{60-j*6} l-1 -12 h{-(58-j*6)}z" fill="{"#f2e6c8" if j%2 else "#e2cfa8"}"/>' for j in range(6))+'</g>' for x,s in ((40,.8),(135,1.1),(230,.8)))+GENTLE(135,40,.4).replace('#e05a8a','#c0392b')),
 [('Name','Kāñcī, “the girdle”: the city as the earth’s waistband'),('Rivers','The <b>Vegavatī</b> and <b>Pālār</b>'),
  ('All three','<b>Śiva</b> (Ekāmbareśvara, the earth liṅga), <b>Viṣṇu</b> (Varadarāja and many Divya Deśams) and the Goddess <b>Kāmākṣī</b>, a Śakti Pīṭha'),
  ('Halves','Old writers speak of <b>Śiva Kāñcī</b> and <b>Viṣṇu Kāñcī</b>; Jain temples stand across the river'),('History','Capital of the <b>Pallavas</b>; a great centre of Sanskrit, Tamil and Buddhist learning')],
 "Why only one southern city in the list?","Nobody knows. But Kāñcī carries three traditions at once, so perhaps it counts double.",
 '<div class="panel reading small"><p>Read more: <a href="/bhakti/temples-of-india/18-shakti-peethas/kamakshi/">Kāmākṣī of Kāñcīpuram</a>.</p></div>'))
pages.append(city('avantika','6 · AVANTIKĀ · UJJAIN','The city of Mahākāla on the Kṣiprā',('A temple with a tall spire on the Kshipra river, an old astronomical instrument, and a crescent moon',
 '<rect width="270" height="200" fill="#e6eef8"/>'+RIVER(170,270,30)+SHIKH(90,166,1.1,'#f2e6c8','#c0392b')+'<path d="M190 166 h60 v-10 h-60z M200 156 l20 -60 l20 60" fill="#e2cfa8" stroke="#111" stroke-width="1.6"/>'+'<path d="M230 30 a14 14 0 1 0 10 22 a10 10 0 1 1 -10 -22z" fill="#fff8c0" stroke="#111"/>'),
 [('Name','Avanti or Avantikā, Ujjayinī (“the victorious”); Ujjain today'),('River','The <b>Kṣiprā</b>'),
  ('Lord','Śiva as <b>Mahākāla</b>, “Great Time”, a <a href="/bhakti/temples-of-india/12-jyotirlingas/mahakaleshwar/">jyotirliṅga</a>; the Goddess as <b>Mahākālī</b>, a Śakti Pīṭha'),
  ('Learning','The old prime meridian of Indian astronomy ran through Ujjain; an 18th-century Jantar Mantar stands here'),('Festival','The <b>Siṃhastha Kumbha</b>, when Jupiter is in Leo')],
 "Indian astronomers measured from Ujjain?","Like Greenwich, centuries earlier. Fitting for the city of the Lord of Time."))
pages.append(city('dvaraka','7 · DVĀRAKĀ','Kṛṣṇa’s city on the western sea',('A tall multi-storeyed temple with a great flag on the seashore, waves, and outlines of an older city under the water',
 '<rect width="270" height="200" fill="#dff0fa"/>'+'<rect y="140" width="270" height="60" fill="#2a7ac0"/>'+''.join(f'<rect x="{30+k*40}" y="{168+(k%2)*6}" width="22" height="12" fill="none" stroke="#bfe6ff" stroke-width="2" stroke-dasharray="3 3"/>' for k in range(6))+SHIKH(140,138,1.2,'#e2cfa8','#ff8c1a')+KRSNA(60,120,.9)),
 [('Name','Dvārakā or Dvārāvatī, “the city of gates”'),('Water','Where the <b>Gomatī</b> meets the <b>Arabian Sea</b>'),
  ('Story','The city <b>Kṛṣṇa</b> built after leaving Mathurā; the Mahābhārata says the sea swallowed it after he left the world'),
  ('Temple','<b>Dvārakādhīśa</b> (Jagat Mandir), with its great flag changed several times a day; Bet Dvārakā on an island nearby'),
  ('Also','One of the four <b>Dhāms</b>; the <a href="/bhakti/temples-of-india/12-jyotirlingas/nageshwar/">Nāgeśvara</a> jyotirliṅga is close by'),('Under the sea','Marine archaeologists have studied submerged stone structures off the coast; what they are is debated')],
 "A city under the sea? Like Atlantis?","Divers have found stone structures off the coast. Whether they're Kṛṣṇa's city is another question."))
pages.append(page('moksha','WHY CITIES?','What “mokṣadāyikā” means',fig(560,140,'A wheel of rebirth with a figure stepping off it towards a light, a city skyline beneath',
 '<rect width="560" height="140" fill="#0b2a4a"/><circle cx="160" cy="70" r="50" fill="none" stroke="#ffd166" stroke-width="5"/>'+''.join(f'<path d="M160 70 L{160+50*__import__("math").cos(k*0.785):.0f} {70+50*__import__("math").sin(k*0.785):.0f}" stroke="#ffd166" stroke-width="2"/>' for k in range(8))
 +person(290,96,'#fff','#f2c79b',.8)+'<path d="M330 70 h120" stroke="#ffd166" stroke-width="3" stroke-dasharray="6 5"/><circle cx="480" cy="70" r="26" fill="#ffd166" opacity=".9"/>'+T(480,124,'MOKṢA',13,'#ffd166'))+'''<div class="panel reading">
<p><b>The idea.</b> Hindu traditions teach that the self is reborn again and again until it is freed: <b>mokṣa</b>. Most paths to it are inner, through knowledge, devotion or right action.</p>
<p><b>A place that helps.</b> The Purāṇas add something simpler: certain places are so holy that living, worshipping, or dying there carries one towards liberation. The Garuḍa Purāṇa gives this verse in its teaching about death.</p>
<p><b>Kāśī’s promise</b> is the strongest: Śiva, the texts say, gives the dying in Kāśī the knowledge that frees them.</p>
<p><b>A modern reading.</b> Some present-day teachers map the seven cities onto the seven <b>cakras</b> of yoga. This is a new interpretation, not found in the Purāṇas.</p>
</div>'''))
ov=[('Ayodhyā','—','—','—'),('Mathurā','—','—','—'),('Haridvār','—','Māyā Devī (51-list)','—'),('Kāśī','Viśvanātha','Viśālākṣī (18)','—'),('Kāñcī','—','Kāmākṣī (18)','—'),('Ujjain','Mahākāla','Mahākālī (18)','—'),('Dvārakā','Nāgeśvara (nearby)','—','Dvārakā')]
pages.append(page('overlaps','HOW THE LISTS OVERLAP','Saptapurī, Jyotirliṅgas, Śakti Pīṭhas, Dhāms','<table class="ct"><tr><th>City</th><th>Jyotirliṅga</th><th>Śakti Pīṭha</th><th>Cār Dhām</th></tr>'+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in ov)+'</table>'
 +'''<div class="g2"><div class="card bg-yellow"><h4>🏆 Three lists</h4><p><b>Kāśī</b> and <b>Ujjain</b> are in all three of the Saptapurī, the Jyotirliṅgas and the 18 Śakti Pīṭhas.</p></div>
<div class="card bg-blue"><h4>🧭 The four Dhāms</h4><p><b>Badrīnāth</b>, <b>Dvārakā</b>, <b>Purī</b> and <b>Rāmeśvaram</b>, at the four corners. Only Dvārakā is also a mokṣapurī.</p></div></div>'''
 +talk("Which city wins the most lists?","Kāśī and Ujjain, tie! Mokṣapurī, jyotirliṅga and Śakti Pīṭha, all at once.")))
pages.append(page('rivers','THE RIVERS','Every city has its water',facts([
 ('Sarayū','Ayodhyā: where Rāma, the Rāmāyaṇa says, left the world'),('Yamunā','Mathurā: Kṛṣṇa’s river'),('Gaṅgā','Haridvār and Kāśī: the same river, at the hills and on the plains'),
 ('Vegavatī &amp; Pālār','Kāñcī: the Vegavatī of the mango-tree flood'),('Kṣiprā','Ujjain: the Kumbha river of Mālwā'),('Gomatī &amp; the sea','Dvārakā: river meets ocean')])
 +talk("Is it a coincidence they're all on water?","Never. A holy city needs a holy bath. The tīrtha is the crossing place.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Saptapurī','The seven cities'),('Mokṣa','Liberation from rebirth'),('Mokṣadāyikā','Giver of liberation'),('Purī','City; also Jagannātha Purī'),('Tīrtha','A crossing place; a holy site'),
 ('Avimukta','“Never released”: Kāśī'),('Dhām','Abode; one of the four corner shrines'),('Kumbha Melā','The great bathing festival of Haridvār, Prayāga, Ujjain and Nāsik'),('Parikramā','Walking around a holy place'),('Ghāṭ','Steps down to a river')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The list.</b> Ayodhyā, Mathurā, Māyā, Kāśī, Kāñcī, Avantikā, Dvārakā: seven cities that give liberation.</div>
<div><b>The verse.</b> In the Garuḍa, Nārada and Skanda Purāṇas; “purī” usually means “city”, not Jagannātha Purī.</div>
<div><b>The gods.</b> Rāma, Kṛṣṇa twice, the Gaṅgā, Śiva twice, and Kāñcī with Śiva, Viṣṇu and Kāmākṣī.</div>
<div><b>The map.</b> Six in the North and West, Kāñcī alone in the South; every one on a river or the sea.</div>
<div><b>The links.</b> Kāśī and Ujjain are also jyotirliṅgas and Śakti Pīṭhas; Dvārakā is also a Dhām.</div>
</div>'''+talk("One line to remember?","Seven cities, one promise: come here, and the road home is shorter.")+'<div class="key">Ayodhyā · Mathurā · Māyā · Kāśī · Kāñcī · Avantikā · <b>Dvārakā</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>The verse and list:</b> Wikipedia, “Sapta Puri”: the śloka from the Garuḍa Purāṇa; mokṣa; modern names; Choudhury’s list with Purī in place of Māyā; city details (Sarayū; Yamunā and Viśrām Ghāṭ; Har kī Pauṛī and Kumbha; Maṇikarṇikā; Kāmākṣī and the Pālār; Mahākāla and Jantar Mantar; Gomatī and Bet Dvārakā); Cār Dhām. vedapath.app: Garuḍa Purāṇa Preta Kalpa 49.114 (the <i>jñeyāḥ</i> reading); Nārada Purāṇa Pūrva Bhāga 27.35; Skanda Purāṇa Kāśī Khaṇḍa 6.68. Art of Living (the seven cakras reading).</p>
<p><b>Other facts</b> are standard reference knowledge and appear in our other guides: Kāśī Viśvanātha, Mahākāleśvara, Nāgeśvara, Kāmākṣī.</p>
<p><b>Sources differ:</b> whether “purī” is a city name; the identity of Dvārakā’s submerged structures; the early archaeology of Ayodhyā. Maps are simplified. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('verse','The Verse'),('puri','Seven or Eight?'),('map','The Seven on One Map'),('ayodhya','1 · Ayodhyā'),('mathura','2 · Mathurā'),('maya','3 · Māyā · Haridvār'),('kashi','4 · Kāśī'),('kanchi','5 · Kāñcī'),('avantika','6 · Avantikā · Ujjain'),('dvaraka','7 · Dvārakā'),
 ('moksha','Why Cities?'),('overlaps','How the Lists Overlap'),('rivers','The Rivers'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">THE SEVEN MOKṢAPURĪS</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,80px)">SAPTAPURĪ</h1>
  <div class="series">SEVEN CITIES OF LIBERATION · A REFERENCE GUIDE</div>
  <div class="tag">Ayodhyā · Mathurā · Māyā · Kāśī · Kāñcī · Avantikā · Dvārakā</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>One line of Sanskrit names seven cities and makes them a promise: <i>saptaitā mokṣadāyikāḥ</i>, “these seven give liberation”.</p>
    <p>Rāma’s Ayodhyā, Kṛṣṇa’s Mathurā and Dvārakā, the Gaṅgā’s Haridvār, Śiva’s Kāśī and Ujjain, and in the South, Kāñcī, where Śiva, Viṣṇu and the Goddess share one city.</p>
    <p>This guide takes the verse word by word, visits each city, and shows how the seven tie in with the Jyotirliṅgas and Śakti Pīṭhas.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Om,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is this a pilgrimage route?","It's a list, not a route. But people have walked it for centuries anyway.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Saptapuri.html','w').write(head+b+tail())
print('ok',len(pages))
