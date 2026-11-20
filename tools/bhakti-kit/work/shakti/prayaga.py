exec(open('/home/claude/work/shakti/common_s.py').read())
head=head_red('Mādhaveśvarī · Prayāga · The 18 Śakti Pīṭhas · srini.presents',
 'Mādhaveśvarī of Prayāga, the fourteenth of the 18 Śakti Pīṭhas: the Goddess beside Veṇī Mādhava at the Triveṇī Saṅgam, Satī’s fingers, the empty doli of Alopī Devī and the vanished bride, the rival claim of Lalitā Devī, Tīrtharāja Prayāga, the Akṣayavaṭa and the Kumbha. An illustrated reference guide.')
def SANGAM(w=560,h=300):
    o=f'<rect width="{w}" height="{h}" fill="#e7f0d8"/>'
    o+=f'<path d="M300 0 Q300 120 360 190 T560 250" stroke="#bfe3f0" stroke-width="40" fill="none"/>'
    o+=f'<path d="M0 230 Q200 230 360 196" stroke="#3b4fa0" stroke-width="34" fill="none"/>'
    o+=f'<path d="M360 196 Q460 230 560 250" stroke="#7aa8d8" stroke-width="56" fill="none"/>'
    o+=T(330,40,'GAṄGĀ',13,'#1d4f9a','start')+T(60,214,'YAMUNĀ',13,'#fff','start')+T(470,270,'GAṄGĀ (onward)',11,'#1d4f9a')
    o+=f'<circle cx="360" cy="196" r="14" fill="none" stroke="#c0392b" stroke-width="3" stroke-dasharray="4 3"/>'+T(380,182,'TRIVEṆĪ SAṄGAM',12,'#7a1d12','start')+T(380,198,'(+ hidden Sarasvatī)',10,'#7a1d12','start')
    for nm,x,y,col,side in (('Alopī Devī (Alopī Bāgh)',270,150,'#c0392b','l'),('Lalitā Devī (Mīrāpur)',180,250,'#c0392b','l'),('Akṣayavaṭa (in the fort)',330,215,'#bbb','l'),('Veṇī Mādhava (Dārāgañj)',300,110,'#bbb','r')):
        o+=f'<circle cx="{x}" cy="{y}" r="7" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(x+(12 if side=='r' else -12),y+4,nm,11,'#111','start' if side=='r' else 'end')
    return o+T(w-10,16,'schematic, not to scale',10,'#555','end')
def DOLI(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-80 -110 h160" stroke="#7a5a2a" stroke-width="6"/><path d="M-50 -110 v40 M50 -110 v40" stroke="#c9a26b" stroke-width="3"/>'
 '<rect x="-56" y="-72" width="112" height="56" rx="8" fill="#c0392b"/><path d="M-56 -72 q56 -24 112 0" fill="#e0a800"/>'+''.join(f'<circle cx="{-44+i*22}" cy="-14" r="5" fill="#ffd166"/>' for i in range(5))+'<path d="M-40 -60 q40 20 80 0" stroke="#ffd166" stroke-width="2" fill="none"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="An empty red palanquin hanging over a pool, above the meeting of a pale river and a dark river">'
 '<rect width="380" height="268" fill="#4a0e0e" rx="8"/><path d="M190 268 Q190 210 240 190 T380 170" stroke="#bfe3f0" stroke-width="30" fill="none"/><path d="M0 220 Q120 220 200 206" stroke="#3b4fa0" stroke-width="26" fill="none"/>'
 +'<ellipse cx="190" cy="170" rx="80" ry="14" fill="#4aa3df" stroke="#111"/>'+DOLI(190,150,1.1)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Mādhaveśvarī</b> in the hymn: “the Goddess of Mādhava”'),
 ('Hymn','<i>prayāge mādhaveśvarī</i>'),
 ('Where','<b>Prayāga</b> (Prayagraj), Uttar Pradesh, at the meeting of the Gaṅgā, Yamunā and hidden Sarasvatī'),
 ('Pīṭha','Satī’s <b>fingers</b> fell here, by most lists'),
 ('Identified with','<b>Alopī Devī</b> at Alopī Bāgh, where an empty <b>doli</b> is worshipped; <b>Lalitā Devī</b> at Mīrāpur also claims the Pīṭha'),
 ('Bhairava','<b>Bhava</b>, by the Pīṭha-nirṇaya'),
 ('Place','<b>Tīrtharāja</b>, “king of pilgrimage places”, home of the Kumbha Melā')])
 +talk("Two temples for one Pīṭha?","Prayāga is that kind of place: everything here is a meeting. Even the claims meet.")))
pages.append(page('where','WHERE IT IS','Where three rivers meet',fig(560,300,'Schematic map of Prayag: the pale Ganga from the north and the dark Yamuna from the west meeting at the Triveni Sangam; Alopi Devi, Lalita Devi, the Akshayavata and Veni Madhava marked',SANGAM())
 +'<div class="g2"><div>'+minimap([14],'Map of India with Prayag marked')+'</div><div class="panel reading small"><p><b>Two colours.</b> At the Saṅgam the pale, muddy Gaṅgā and the dark, clear Yamunā flow side by side before mixing. The <b>Sarasvatī</b> is said to join unseen, from below.</p><p><b>Both temples</b> are a short way inland from the confluence.</p></div></div>'))
pages.append(page('names','THE NAMES','Mādhava’s Goddess',facts([
 ('Mādhaveśvarī','<i>Mādhava</i> (Viṣṇu) + <i>īśvarī</i>: the Goddess beside Prayāga’s Viṣṇu, <b>Veṇī Mādhava</b>'),
 ('Alopī · Alopśaṅkarī','“The one who disappeared”'),
 ('Lalitā','The Pīṭha-nirṇaya’s name for the Goddess here'),
 ('Prayāga','“Place of sacrifice”: Brahmā’s first yajña was held here, it is said'),
 ('Tīrtharāja','“King of tīrthas”'),
 ('Triveṇī','“Three braids”: the three rivers')])
 +talk("Why name her after Viṣṇu?","Prayāga's guardian is Veṇī Mādhava. Śiva's wife here is called 'Mādhava's Goddess' by the hymn: everyone belongs to the Saṅgam.")))
pages.append(page('pitha','THE PĪṬHA','The last to fall',fig(560,170,'Shiva carrying Sati’s body as Vishnu’s discus cuts it, a small glowing piece falling and vanishing over a river confluence',
 '<rect width="560" height="170" fill="#1a0e1e"/>'+STAR+SHIVA(150,40,.7)+SATI(220,60,.9,-8)+CHAKRA(300,70,14)+'<circle cx="400" cy="110" r="8" fill="#ffd166" opacity=".5" stroke="#ffd166"/><circle cx="400" cy="110" r="16" fill="none" stroke="#ffd166" stroke-dasharray="3 3"/><path d="M330 168 Q420 120 560 150" stroke="#bfe3f0" stroke-width="8" fill="none"/><path d="M200 168 Q300 160 420 140" stroke="#3b4fa0" stroke-width="7" fill="none"/>')+'''<div class="steps">
<div><b>The fingers.</b> The Pīṭha-nirṇaya Tantra says the <b>group of fingers</b> (aṅguli-vṛnda) of the Goddess fell at Prayāga; she is <b>Lalitā</b> and her Bhairava is <b>Bhava</b>.</div>
<div><b>The last piece.</b> Alopī Devī’s tradition adds that this was the <b>last</b> part to fall, and that it vanished at once: so she is <b>Alopī</b>, “the one who disappeared”, and the holiest of all.</div>
<div><b>Other tellings.</b> One account names the ringlets of her hair instead. Sources differ.</div>
</div>'''))
pages.append(page('alopi','ALOPĪ DEVĪ','Worshipping an empty doli',fig(560,200,'Inside the temple: a red wooden palanquin hanging over a small square pool on a silver platform, garlands around it, devotees tying threads',
 '<rect width="560" height="200" fill="#efe4cc"/><rect x="200" y="170" width="160" height="20" fill="#bbb" stroke="#111" stroke-width="2"/><rect x="220" y="160" width="120" height="12" fill="#4aa3df" stroke="#111"/>'+DOLI(280,150,1.1)
 +person(120,180,'#ffd60a','#c98b5a',1)+person(440,180,'#2a9d6f','#c98b5a',1)+'<path d="M134 140 l30 -10" stroke="#c0392b" stroke-width="2"/>')+facts([
 ('No image','There is no statue and no stone: a wooden <b>doli</b> (palanquin), wrapped in red, is the Goddess'),
 ('Where','It hangs over a small pool, on a platform in the sanctum'),
 ('Touch','Devotees may touch it and make offerings directly'),
 ('Rakṣā-sūtra','Pilgrims tie a red protective thread, believed to keep the Mother’s care with them while it stays tied'),
 ('Rites','Families bring children here for the <b>muṇḍana</b>, the first head-shaving'),
 ('Belief','Some say the doli sways by itself when the temple is locked')])
 +talk("They worship an empty carriage?","An empty seat says 'she was here, she is here, but you can't see her'. That's what Alopī means.")))
pages.append(page('bride','LEGEND · THE VANISHED BRIDE','A local story',fig(560,170,'A wedding procession in a forest attacked by robbers; the robbers lifting the curtain of the bride’s palanquin and finding it empty',
 '<rect width="560" height="170" fill="#e7f0d8"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="26" fill="#3a8a3a"/>' for x,y in ((40,40),(110,30),(470,30),(530,50)))+DOLI(280,160,.8)
 +person(160,160,'#1a1a1a','#8a5a3a',1)+'<path d="M180 120 l40 -10" stroke="#bbb" stroke-width="3"/>'+person(400,160,'#1a1a1a','#8a5a3a',1)+T(280,40,'?!',22,'#c0392b'))+'''<div class="steps">
<div><b>The procession.</b> A bridal party was carrying a new bride in her doli through the forest.</div>
<div><b>Robbers.</b> Bandits attacked, killed the men and seized the wealth, then turned to the doli.</div>
<div><b>Empty.</b> When they pulled back the curtain, the doli was empty. The bride had vanished.</div>
<div><b>A temple.</b> The story spread; a shrine rose where it happened, and people worshipped the bride as <b>Alopī Devī</b>, the maiden Goddess who disappeared.</div>
</div>'''+talk("Is that the 'real' origin?","It's the local one. The Pīṭha story and the bride story both end the same way: she's gone, and the doli stays.")))
pages.append(page('lalita','LALITĀ DEVĪ OF MĪRĀPUR','The rival claim',facts([
 ('Where','<b>Mīrāpur</b>, near the Yamunā bank in Prayāga'),
 ('Claim','Many hold that this is <b>the</b> Prayāga Śakti Pīṭha, where Satī’s fingers fell, with the Goddess named Lalitā as in the Pīṭha-nirṇaya'),
 ('Image','Here the Goddess has a form, unlike at Alopī Bāgh'),
 ('Three places','One tradition counts three Prayāga Pīṭha spots: Alopī, Mīrāpur and the <b>Akṣayavaṭa</b>')])
 +'''<div class="g2">
<div class="card bg-red"><h4>🔴 For Alopī</h4><p>Long local devotion; the name Alopśaṅkarī; the story of the last, vanished part; most Aṣṭādaśa pilgrims go here.</p></div>
<div class="card bg-blue"><h4>🔵 For Lalitā</h4><p>The Tantric list names <b>Lalitā</b> with the fingers; some writers say Prayāga has only one Pīṭha, and it is this.</p></div>
</div>'''+talk("Which should a pilgrim visit?","Most visit both. They're in the same city, and the Goddess isn't counting.")))
pages.append(page('venimadhava','VEṆĪ MĀDHAVA','The Viṣṇu of Prayāga',facts([
 ('Who','Viṣṇu as <b>Veṇī Mādhava</b>, presiding deity of Prayāga; his temple is at Dārāgañj'),
 ('Veṇī','“Braid”: the three rivers braided together'),
 ('Twelve Mādhavas','Prayāga tradition has twelve Mādhava shrines guarding the sacred zone'),
 ('Pilgrims','A visit to the Saṅgam is said to be complete only after darśana of Veṇī Mādhava'),
 ('Caitanya','The Bengali saint is said to have danced in ecstasy at his temple')])
 +talk("So the hymn's 'Mādhaveśvarī' points here?","To his consort-Goddess at the Saṅgam. Prayāga is Mādhava's city; she is its queen.")))
pages.append(page('triveni','THE TRIVEṆĪ SAṄGAM','King of tīrthas',fig(560,160,'Pilgrims in boats at the confluence, a line where the pale and dark waters meet',
 '<rect width="560" height="160" fill="#cfe3f5"/><path d="M0 70 h560 v90 h-560z" fill="#bfe3f0"/><path d="M0 70 L560 70 L560 160 L260 160z" fill="#3b4fa0"/><path d="M260 160 L560 70" stroke="#fff" stroke-width="2" stroke-dasharray="6 4"/>'
 +''.join(f'<g transform="translate({x} {y})"><path d="M-30 0 h60 l-10 10 h-40z" fill="#c9a26b" stroke="#111"/>'+person(0,-4,'#ff8c1a','#c98b5a',.5)+'</g>' for x,y in ((120,110),(300,120),(450,96))))+facts([
 ('Three rivers','The <b>Gaṅgā</b>, the <b>Yamunā</b>, and the unseen <b>Sarasvatī</b>'),
 ('Tīrtharāja','The Purāṇas call Prayāga the king of all sacred places'),
 ('Snāna','A dip at the Saṅgam is held to wash away sins; ancestors’ rites and the shaving of heads are done here'),
 ('Brahmā’s yajña','Prayāga is said to be where Brahmā performed the first sacrifice after creating the world'),
 ('Māgha','Every year in the month of Māgha, pilgrims camp by the river: the <b>Māgh Melā</b>')])))
pages.append(page('kumbha','THE KUMBHA','The pot of nectar',facts([
 ('Legend','When gods and demons churned the ocean, a pot (<b>kumbha</b>) of nectar emerged; in the struggle, drops fell at four places'),
 ('Four places','<b>Prayāga</b>, <b>Haridvāra</b>, <b>Ujjayinī</b> and <b>Nāsika</b>'),
 ('The Melā','A great gathering is held at each by turns, timed by the positions of Jupiter and the Sun'),
 ('Prayāga’s','The largest of all: the Kumbha, the Ardh Kumbha, and the Mahā Kumbha'),
 ('Akhāṛās','Orders of ascetics lead the royal bathing processions')])
 +'<div class="key">See also: <a href="/bhakti/temples-of-india/18-shakti-peethas/mahakali-ujjain/">Ujjain</a> · <a href="/bhakti/temples-of-india/sapta-puri/">Haridvāra (Māyā)</a></div>'))
pages.append(page('akshaya','THE AKṢAYAVAṬA','The banyan that never dies',facts([
 ('What','“The undying banyan”: a sacred tree, now inside the fort by the Saṅgam'),
 ('Legend','At the end of an age, when the world floods, the infant Viṣṇu floats on a leaf of this banyan'),
 ('Rāma','By tradition, Rāma, Sītā and Lakṣmaṇa rested under it on their way to exile'),
 ('Pīṭha link','One tradition counts it among Prayāga’s three Pīṭha spots'),
 ('Pātālapurī','An underground temple near it is part of the pilgrimage')])
 +talk("A tree that survives the end of the world?","So the legend says. It's Prayāga's way of saying: this place was here before, and will be after.")))
pages.append(page('history','HISTORY','From Prayāga to Prayagraj',tl([
 ('Vedic','Hymns praise the meeting of the white and dark rivers.'),
 ('3rd c. BCE','An Aśokan pillar, later inscribed by Samudragupta, now stands in the fort.'),
 ('7th c.','The Chinese pilgrim Xuanzang describes a great gathering at the confluence under King Harṣa.'),
 ('1575','Akbar founds a fort at the Saṅgam; the city becomes Illāhābād.'),
 ('1800s','Mahārānī Baizābāī Scindia restores the Saṅgam ghāṭs and temples.'),
 ('2018','The city is officially renamed Prayagraj.')])
 +'<div class="panel reading small"><p><b>The temples’ age.</b> The founding date of the Alopī Devī temple is not known; its roots are in tradition rather than records.</p></div>'))
pages.append(page('festivals','THROUGH THE YEAR','Navarātri and the river',facts([
 ('Navarātri','The great festival of Alopī Devī, especially in Āśvina'),
 ('Māgh Melā','Pilgrims camping at the Saṅgam visit the Goddess'),
 ('Kumbha years','Crowds on a vast scale'),
 ('Daily','Doli worship, threads, flowers; muṇḍana for children')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Alopa','Disappearance'),('Doli','Palanquin, bridal carriage'),('Aṅguli','Finger'),('Saṅgam','Confluence'),('Triveṇī','Three braids, three rivers'),
 ('Tīrtharāja','King of sacred places'),('Mādhava','Viṣṇu'),('Akṣaya','Undying'),('Vaṭa','Banyan'),('Muṇḍana','First head-shaving'),('Rakṣā-sūtra','Protective thread')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Pīṭha.</b> Satī’s fingers at Prayāga: Mādhaveśvarī in the hymn, Lalitā in the Tantra.</div>
<div><b>Alopī Devī.</b> No image, an empty red doli: the Goddess who vanished.</div>
<div><b>The rival.</b> Lalitā Devī at Mīrāpur; pilgrims visit both.</div>
<div><b>The city.</b> The Triveṇī Saṅgam, Veṇī Mādhava, the Akṣayavaṭa, the Kumbha.</div>
<div><b>The meaning.</b> She is present exactly where she can’t be seen.</div>
</div>'''+talk("One line to remember?","Where three rivers become one, the Mother left an empty seat.")+'<div class="key">The fourteenth seat of the Mother: <b>Mādhaveśvarī of Prayāga</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Alopi Devi Mandir” (no image, wooden doli; Alopī = disappeared; last part to fall; claim debated in favour of Lalitā Devī with the fingers; the vanished-bride legend). optimatravels.com (Alop Śaṅkarī; doli in the centre under the śikhara, wrapped in red; Brahmā’s yajña). bhaktibharat.com (doli over a pool on a silver platform). pilgrimaide.com (doli on a stand; touching and offerings). bhaktikalpa.com (Mādhaveśvarī as main deity; muṇḍana). t.tripadvisor (rakṣā-sūtra). hindupad.com (doli swaying when locked). greenmesg.org (Pīṭha-nirṇaya: aṅguli-vṛnda, Lalitā, Bhava; Alopī and Lalitā both identified). templepurohit.com (three spots: Akṣayavaṭa, Mīrāpur, Alopī; Tīrtharāja). memoriesandsuch.com (ringlets of hair; Baizābāī Scindia; unknown founding date).</p>
<p><b>General:</b> standard Purāṇic accounts of Prayāga, the Kumbha and the Akṣayavaṭa; Prayagraj renaming 2018; Akbar’s fort (1575).</p>
<p><b>Sources differ:</b> Alopī or Lalitā as the Pīṭha; fingers or hair. <b>Not verified:</b> the twelve Mādhavas; Caitanya at Veṇī Mādhava; Rāma at the Akṣayavaṭa; the doli swaying. Maps are schematic. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('pitha','The Pīṭha'),('alopi','Alopī Devī'),('bride','Legend · The Vanished Bride'),('lalita','Lalitā Devī of Mīrāpur'),('venimadhava','Veṇī Mādhava'),
 ('triveni','The Triveṇī Saṅgam'),('kumbha','The Kumbha'),('akshaya','The Akṣayavaṭa'),('history','History'),('festivals','Through the Year'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 14 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(22px,7vw,70px)">MĀDHAVEŚVARĪ</h1>
  <div class="series">PRAYĀGA · A REFERENCE GUIDE</div>
  <div class="tag">The Goddess who vanished at the Saṅgam</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>At Prayāga, where the pale Gaṅgā meets the dark Yamunā and the hidden Sarasvatī rises to join them, the Śakti Pīṭha hymn places <b>Mādhaveśvarī</b>, the Goddess beside Prayāga’s Viṣṇu, Veṇī Mādhava.</p>
    <p>In her best-known shrine there is no image at all. Pilgrims touch and garland an empty red palanquin, because the Goddess here is <b>Alopī</b>: the one who disappeared. A second temple across town says the Pīṭha is really there.</p>
    <p>This guide tells both stories, and the story of the confluence that makes Prayāga the king of pilgrim places.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Alopī Mātā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("If nothing is there, what do people see?","Whatever their faith shows them. An empty seat is the easiest place to imagine the Mother.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Madhaveshwari_Prayaga.html','w').write(head+b+tail())
print('ok',len(pages))
