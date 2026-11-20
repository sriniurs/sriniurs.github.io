exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Daśa Mahāvidyā · The Ten Great Wisdoms · srini.presents',
 'The Daśa Mahāvidyā, the ten Great Wisdoms of the Goddess: Kālī, Tārā, Tripurasundarī, Bhuvaneśvarī, Bhairavī, Chinnamastā, Dhūmāvatī, Bagalāmukhī, Mātaṅgī and Kamalā. How Satī became ten to stop Śiva, the ten directions, fierce and gentle forms, Kālīkula and Śrīkula, the avatāra links and the great temples. An illustrated overview.')
def RING(w=560,h=360):
    cx,cy,r=280,180,140
    g=f'<rect width="{w}" height="{h}" fill="#1a0e1e"/>'+STAR+f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#ffd166" stroke-dasharray="4 6"/>'
    import math
    for i in range(10):
        a=-math.pi/2+i*2*math.pi/10; x=cx+r*math.cos(a); y=cy+r*math.sin(a)
        g+=MV(i+1,x,y+10,.45)+T(f'{x:.0f}',f'{y+46:.0f}',MVN[i][1].split(' (')[0],10,'#ffd166')
    return g+SHIVA(cx,cy-30,.8)
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Ten goddesses in a ring, from dark fierce Kali to golden lotus Kamala">'
 '<rect width="380" height="268" fill="#2a0e1e" rx="8"/>'+''.join(MV(i+1,40+(i%5)*75,90+(i//5)*120,.6) for i in range(10))+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Mahāvidyā','“Great Wisdom”, “Great Knowledge”: a form of the Goddess who is herself a path to liberation'),
 ('Daśa','<b>Ten</b> of them, in the usual order:'),
 ('The ten','<b>Kālī, Tārā, Tripurasundarī, Bhuvaneśvarī, Bhairavī, Chinnamastā, Dhūmāvatī, Bagalāmukhī, Mātaṅgī, Kamalā</b>'),
 ('One Goddess','Ten faces of the one Mahādevī, from terrifying to beautiful'),
 ('Origin story','Satī becomes ten to stop Śiva from blocking her way to Dakṣa’s sacrifice'),
 ('Texts','Mahābhāgavata and Bṛhaddharma Purāṇas (c. 10th c. onward); many Tantras'),
 ('Tradition','Śākta Tantra; strongest in Bengal, Assam, Odisha, Nepal'),
 ('Temples','All ten together on Kāmākhyā’s Nīlācala hill; famous single shrines across India')])
 +talk("Ten goddesses or one?","One Mother, ten windows. Each shows a different truth about her: time, sound, beauty, space, fire, sacrifice, emptiness, stillness, speech, plenty.")))
pages.append(page('ten','THE TEN','In the usual order',fig(560,360,'Ten goddesses arranged in a ring around Shiva, each labelled',RING())
 +'<table class="ct"><tr><th>#</th><th>Mahāvidyā</th><th>Stands for</th></tr>'+''.join(f'<tr><td>{n}</td><td><b>{nm}</b></td><td>{d}</td></tr>' for n,nm,_,d in MVN)+'</table>'))
pages.append(page('myth','HOW SATĪ BECAME TEN','The best-known story',fig(560,180,'Shiva turning away while a furious goddess multiplies into many forms that surround him on all sides',
 '<rect width="560" height="180" fill="#2a0e1e"/>'+STAR+SHIVA(280,90,.8)+''.join(MV(i+1,60+i*49 if i<5 else 60+(i-5)*49+250,150 if i<5 else 150,.35) for i in range(10)))+'''<div class="steps">
<div><b>No invitation.</b> Dakṣa held a great sacrifice and did not invite Śiva. Satī wanted to go anyway; Śiva forbade it.</div>
<div><b>Her fury.</b> Satī grew terrible: she became <b>Kālī</b>, dark and wild. Śiva, alarmed, tried to flee.</div>
<div><b>Ten directions.</b> Wherever he turned, a different Goddess blocked his way: she had become ten, one in each of the ten directions (the eight points of the compass, above and below).</div>
<div><b>He yields.</b> Śiva let her go. She went to the sacrifice, and what followed is the story of the Śakti Pīṭhas.</div>
</div>'''+talk("The same Satī whose body became the Pīṭhas?","The very same. Before she died she showed Śiva all ten of her faces.")))
pages.append(page('other','OTHER BEGINNINGS','More than one story',facts([
 ('Pārvatī','In another telling, Pārvatī, after a quarrel with Śiva, takes ten forms to stop him leaving'),
 ('Durgā','Elsewhere they arise in the Goddess’s battles with demons, as her helpers'),
 ('Śatākṣī','One account links them to the hundred-eyed Goddess who ended a famine'),
 ('Texts','The Mahābhāgavata (c. 10th c.) and Bṛhaddharma Purāṇas tell the Satī version; Tantras such as the Toḍala and Śākta-pramoda describe each Goddess'),
 ('Lists vary','Some Purāṇic lists name Ṣoḍaśī for Tripurasundarī and order them differently')])
 +talk("Which story is true?","All of them point the same way: the Goddess is never just one thing.")))
pages.append(page('spectrum','FIERCE TO GENTLE','A spectrum of the Goddess',fig(560,170,'The ten goddesses in a row from dark to golden, fierce on the left and gentle on the right',
 '<rect width="560" height="170" fill="#fdf1e8"/><defs><linearGradient id="gg" x1="0" x2="1"><stop offset="0" stop-color="#1a1a2a"/><stop offset="1" stop-color="#ffd166"/></linearGradient></defs><rect x="20" y="150" width="520" height="10" fill="url(#gg)"/>'
 +''.join(MV(n,40+i*53,110,.42) for i,n in enumerate((1,6,2,5,7,8,9,4,3,10))))+facts([
 ('Fierce (ugra)','Kālī, Tārā, Chinnamastā, Bhairavī, Dhūmāvatī, Bagalāmukhī: they face death, fear and the ego head on'),
 ('Gentle (saumya)','Tripurasundarī, Bhuvaneśvarī, Mātaṅgī, Kamalā: beauty, space, art and plenty'),
 ('One cycle','Some teachers read them as stages: from Kālī’s dissolution to Kamalā’s full bloom'),
 ('Why fierce?','The fierce forms are mothers too: they destroy what binds the devotee')])))
pages.append(page('kula','KĀLĪKULA AND ŚRĪKULA','Two families of worship',facts([
 ('Kālīkula','The “family of Kālī”: Kālī, Tārā, Chinnamastā and the fierce forms; strong in Bengal and the east'),
 ('Śrīkula','The “family of Śrī”: Tripurasundarī (Lalitā), with the Śrī Cakra and Śrīvidyā; strong in the south'),
 ('Mātaṅgī','In Śrīvidyā she is Lalitā’s minister, Śyāmalā'),
 ('Bagalāmukhī','Lalitā’s general in some lists; Vārāhī also holds that role'),
 ('Meeting point','The Mahāvidyās bring both families into one set of ten')])
 +talk("So Śrīvidyā in Kāñcī and Kālī worship in Kolkata are cousins?","Same family tree, two branches. Tripurasundarī is the third Mahāvidyā.")))
pages.append(page('avatara','THE TEN AND THE TEN AVATĀRAS','A Tantric pairing',
 '<table class="ct"><tr><th>Mahāvidyā</th><th>Avatāra (Toḍala Tantra, as commonly cited)</th></tr>'+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in (('Kālī','Kṛṣṇa'),('Tārā','Matsya'),('Tripurasundarī','Paraśurāma'),('Bhuvaneśvarī','Vāmana'),('Bhairavī','Balarāma'),('Chinnamastā','Narasiṃha'),('Dhūmāvatī','Varāha'),('Bagalāmukhī','Kūrma'),('Mātaṅgī','Rāma'),('Kamalā','Buddha')))+'</table>'
 +'<div class="panel reading small"><p><b>Lists disagree.</b> Other Tantras pair them differently, and some say the Mahāvidyās are the source from which Viṣṇu’s avatāras arose. Read the table as one tradition’s view.</p></div>'
 +talk("Viṣṇu's avatāras come from the Goddess?","That's the Śākta view: every form of God is her power at work.")))
for a,b_ in ((0,5),(5,10)):
    cards=''
    for n,nm,slug,d in MVN[a:b_]:
        cards+=f'<div class="card bg-red" style="text-align:center"><svg width="150" height="120" viewBox="0 0 150 120" role="img" aria-label="{nm}"><rect width="150" height="120" fill="#fdf1e8"/>{MV(n,75,80,.6)}</svg><h4>{n}. {nm}</h4><p class="small">{d}</p></div>'
    pages.append(page(f'cards{a}',f'THE TEN · {a+1}–{b_}','How to recognise them','<div class="g2">'+cards+'</div>'))
pages.append(page('icon','HOW TO RECOGNISE THEM','Colours and objects',facts([
 ('Kālī','Black; tongue out; garland of heads; sword; standing on Śiva'),
 ('Tārā','Blue; short; tiger skin; scissors and skull-cup; on a cremation ground'),
 ('Tripurasundarī','Red-gold; sugarcane bow and flower arrows; noose and goad'),
 ('Bhuvaneśvarī','Golden; crescent moon; noose and goad; gestures of blessing'),
 ('Bhairavī','Red; red garments; rosary and book, or noose and goad'),
 ('Chinnamastā','Holds her own cut head; three streams of blood feed her and two attendants'),
 ('Dhūmāvatī','Grey widow in white; crow banner; winnowing basket; horseless chariot'),
 ('Bagalāmukhī','Yellow; pulls a demon’s tongue; raises a club'),
 ('Mātaṅgī','Green; vīṇā; parrot'),
 ('Kamalā','Golden; seated on a lotus; elephants pour water over her')])))
pages.append(page('temples','WHERE TO FIND THEM','Temples of the Mahāvidyās',facts([
 ('All ten','<a href="/bhakti/temples-of-india/18-shakti-peethas/kamakhya/">Kāmākhyā</a>, Guwahati: a temple for each on the Nīlācala hill'),
 ('Kālī','Kālīghāṭ and Dakṣiṇeśvar, Kolkata'),
 ('Tārā','Tārāpīṭh, Birbhum, West Bengal'),
 ('Tripurasundarī','Udaipur, Tripurā; and as Lalitā and Kāmākṣī in the south'),
 ('Chinnamastā','Rajrappa, Jharkhand'),
 ('Dhūmāvatī','Datia, Madhya Pradesh, beside Pītāmbarā Pīṭha'),
 ('Bagalāmukhī','Pītāmbarā Pīṭha, Datia; Nalkheda, Madhya Pradesh; Kangra'),
 ('Bhuvaneśvarī','Nīlācala hilltop; Pudukkottai, Tamil Nadu'),
 ('Kamalā','Worshipped widely as Lakṣmī; Kamalā shrine inside Kāmākhyā')])))
pages.append(page('worship','A WORD ON WORSHIP','Tantra and initiation',facts([
 ('Tantric','The Mahāvidyās belong to Tantric worship; their mantras and yantras are traditionally given by a guru, with initiation (dīkṣā)'),
 ('For everyone','Stories, images, names and temple darśana are open to all'),
 ('Fierce, not evil','Their fearsome looks stand for truths (death, desire, the ego) faced without flinching'),
 ('Navarātri','Gupta Navarātris in Māgha and Āṣāḍha are often kept for the Mahāvidyās'),
 ('This series','Ten guides, one per Goddess: myth, form, meaning, temples. No secret mantras')])
 +talk("Can I chant their mantras from a book?","Tradition says take them from a teacher. This series sticks to what is meant for everyone.")))
pages.append(page('series','THE SERIES','Ten guides',facts([(f'{n}. {nm}',f'<a href="{MVS}{slug}/">{d}</a>') for n,nm,slug,d in MVN])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Mahāvidyā','Great wisdom'),('Daśa','Ten'),('Ugra · Saumya','Fierce · gentle'),('Kula','Family, lineage'),('Śrīvidyā','Worship of Tripurasundarī'),('Yantra','Sacred diagram'),('Dīkṣā','Initiation'),('Gupta Navarātri','The “hidden” Navarātris')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Ten.</b> Kālī, Tārā, Tripurasundarī, Bhuvaneśvarī, Bhairavī, Chinnamastā, Dhūmāvatī, Bagalāmukhī, Mātaṅgī, Kamalā.</div>
<div><b>Origin.</b> Satī becomes ten to block Śiva in all ten directions.</div>
<div><b>Range.</b> From fierce to gentle; Kālīkula to Śrīkula.</div>
<div><b>Pairing.</b> One Tantra matches them to Viṣṇu’s ten avatāras.</div>
<div><b>Where.</b> All ten at Kāmākhyā; Kālī at Kālīghāṭ, Tārā at Tārāpīṭh, and more.</div>
</div>'''+talk("One line to remember?","Wherever you turn, the Mother is already there: ten ways.")+'<div class="key">The ten Great Wisdoms. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p>Wikipedia, “Mahavidya” (ten Tantric goddesses, usual order; Satī surrounding Śiva from ten directions; Mahābhāgavata and Bṛhaddharma lists with Ṣoḍaśī; Toḍala Tantra avatāra table; Guhyātiguhya Tantra: source of the avatāras; citing Kinsley 1997). Kinsley, <i>Tantric Visions of the Divine Feminine</i> (1997), via mahavidya.ca (Mahābhāgavata c. 10th c.; alternative origins: Pārvatī, Kālī, Śatākṣī; Śiva frightened). sahapedia.org (the Satī story). Shankarnarayanan, <i>The Ten Great Cosmic Powers</i> (avatāra variants).</p>
<p><b>Sources differ:</b> order of the ten; avatāra pairings; directions of each. <b>Iconography</b> follows common dhyāna descriptions; details vary. Temple list is a starting point, not complete. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('ten','The Ten'),('myth','How Satī Became Ten'),('other','Other Beginnings'),('spectrum','Fierce to Gentle'),('kula','Kālīkula and Śrīkula'),('avatara','The Ten and the Avatāras'),('cards0','The Ten · 1–5'),('cards5','The Ten · 6–10'),
 ('icon','How to Recognise Them'),('temples','Where to Find Them'),('worship','A Word on Worship'),('series','The Series'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">THE TEN GREAT WISDOMS</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,7vw,70px)">DAŚA MAHĀVIDYĀ</h1>
  <div class="series">DEVĪ · AN ILLUSTRATED OVERVIEW</div>
  <div class="tag">One Mother, ten faces</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>When Śiva forbade Satī to go to her father’s sacrifice, she did not argue. She grew dark and terrible, and when he turned to leave, he found her in front of him, and behind him, and on every side: ten Goddesses, one in each direction.</p>
    <p>These are the <b>Daśa Mahāvidyā</b>, the ten Great Wisdoms: Kālī of time, Tārā who carries across, Tripurasundarī of beauty, and seven more, down to golden Kamalā on her lotus.</p>
    <p>This overview introduces all ten. A full guide to each follows in the series.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why are some of them so scary?","Because some truths are. The fierce ones cut away fear; the gentle ones give what's left room to bloom.")}
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Dasha_Mahavidya.html','w').write(head+b+tail())
print('ok',len(pages))
