exec(open('/home/claude/work/shakti/common_s.py').read())
psrc=open('/home/claude/work/shakti/pithapuram.py').read()
exec('def GAYASURA('+psrc.split('def GAYASURA(')[1].split('\ndef PUR(')[0])
head=head_red('Māṅgalyagaurī · Gayā · The 18 Śakti Pīṭhas · srini.presents',
 'Māṅgalyagaurī (Maṅgalā Gaurī) of Gayā, the sixteenth of the 18 Śakti Pīṭhas: Satī’s breast on the Bhasmakūṭa hill, the Goddess of nourishment, Gayāsura’s head and the three Gayās, the Viṣṇupada footprint, the Phalgu and Sītā’s curse, the Akṣayavaṭa, piṇḍa-dāna and Pitṛ Pakṣa, and the Maṅgalā Gaurī vrata. An illustrated reference guide.')
def gy(lat,lon): return 280+(lon-85.005)*3800, 150+(24.795-lat)*3800
def GYMAP(w=560,h=300):
    o=f'<rect width="{w}" height="{h}" fill="#e7f0d8"/>'
    o+=f'<path d="M{gy(24.85,85.035)[0]:.0f} 0 Q{gy(24.78,85.02)[0]:.0f} {gy(24.78,85.02)[1]:.0f} {gy(24.70,85.03)[0]:.0f} {h}" stroke="#f4e6c0" stroke-width="40" fill="none"/>'
    o+=f'<path d="M{gy(24.85,85.035)[0]:.0f} 0 Q{gy(24.78,85.02)[0]:.0f} {gy(24.78,85.02)[1]:.0f} {gy(24.70,85.03)[0]:.0f} {h}" stroke="#9fd0ea" stroke-width="5" stroke-dasharray="10 8" fill="none"/>'+T(f'{gy(24.82,85.04)[0]+30:.0f}',f'{gy(24.82,85.04)[1]:.0f}','PHALGU (mostly sand)',11,'#1d4f9a','start')
    for nm,la,lo,side in (('Bhasmakūṭa',24.775,85.002,'l'),('Brahmayoni',24.76,84.99,'l'),('Rāmaśilā',24.81,85.01,'l'),('Pretaśilā',24.83,84.98,'l')):
        x,y=gy(la,lo); o+=f'<path d="M{x-30:.0f} {y+12:.0f} l30 -32 l30 32z" fill="#8a9a6a" stroke="#111" stroke-width="1.5"/>'
    for nm,la,lo,col,side in (('MAṄGALĀ GAURĪ',24.775,85.002,'#c0392b','l'),('Viṣṇupada',24.77,85.022,'#3b6fd0','l'),('Akṣayavaṭa',24.765,85.01,'#bbb','r'),('Brahmayoni',24.758,84.99,'#bbb','l'),('Rāmaśilā',24.81,85.01,'#bbb','r'),('Pretaśilā',24.83,84.98,'#bbb','r')):
        x,y=gy(la,lo); r=8 if col=='#c0392b' else 6
        o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{col}" stroke="#111" stroke-width="1.5"/>'+T(f'{x+(12 if side=="r" else -12):.0f}',f'{y+4:.0f}',nm,12,'#111','start' if side=='r' else 'end')
    return o+T(w-10,h-8,'schematic, not to scale; Bodh Gayā lies further south',10,'#555','end')
def GAURI(x,y,s=1): return GENTLE(x,y,s).replace('#e05a8a','#e0a800')
def PINDA(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="1.5"><ellipse rx="40" ry="10" fill="#3a8a3a"/>'+''.join(f'<circle cx="{dx}" cy="-6" r="7" fill="#f4f4e8"/>' for dx in (-20,0,20))+'</g>'
def FOOT(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-50" y="-30" width="100" height="60" rx="6" fill="#555"/><path d="M-12 18 q-10 -20 -2 -36 q12 -8 20 4 q6 16 -4 32z" fill="#888"/>'+''.join(f'<circle cx="{-10+i*6}" cy="{-26+(i%2)}" r="2.6" fill="#888"/>' for i in range(5))+'<path d="M-30 -20 v40 M30 -20 v40" stroke="#c9a26b" stroke-width="3"/></g>'
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The golden Goddess Mangala Gauri on a rocky hill above a sandy river, with pinda offerings below">'
 '<rect width="380" height="268" fill="#4a0e0e" rx="8"/><path d="M60 200 Q190 60 320 200z" fill="#8a9a6a" stroke="#111"/><path d="M0 240 Q190 220 380 244 V268 H0z" fill="#f4e6c0"/><path d="M40 252 h300" stroke="#9fd0ea" stroke-width="3" stroke-dasharray="10 8"/>'
 +GAURI(190,150,1.2)+PINDA(110,236,.7)+PINDA(270,236,.7)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Goddess','<b>Māṅgalyagaurī</b> in the hymn; <b>Maṅgalā Gaurī</b> in Gayā: “Gaurī of good fortune”'),
 ('Hymn','<i>gayā māṅgalyagaurikā</i>'),
 ('Where','On the <b>Bhasmakūṭa</b> hill (Maṅgalā Gaurī hill), Gayā, Bihar, above the <b>Phalgu</b>'),
 ('Pīṭha','Satī’s <b>breast</b> fell here: so this is the <b>Pālana Pīṭha</b>, seat of nourishment'),
 ('Form','Two rounded stones, worshipped as the Goddess'),
 ('Texts','Named in the Padma, Vāyu, Agni, Devī Bhāgavata and Mārkaṇḍeya Purāṇas'),
 ('Gayā','City of <b>piṇḍa-dāna</b> for the dead, Gayāsura’s head, and Viṣṇu’s footprint')])
 +talk("A Goddess of good fortune in a city of funeral rites?","The living come to her for blessings; the dead are fed at Viṣṇupada below. Gayā holds both ends of life.")))
pages.append(page('where','WHERE IT IS','Hills around a sandy river',fig(560,300,'Schematic map of Gaya: the wide sandy Phalgu on the east, Mangala Gauri temple on Bhasmakuta hill, the Vishnupada temple on the river bank, the Akshayavata, and the hills Brahmayoni, Ramashila and Pretashila',GYMAP())
 +'<div class="g2"><div>'+minimap([16,17],'Map of India marking Gaya and Varanasi')+'</div><div class="panel reading small"><p><b>Ringed by hills.</b> Gayā sits among rocky hills on three sides, Maṅgalā Gaurī, Rāmaśilā, Pretaśilā and Brahmayoni among them, with the Phalgu on the fourth.</p><p><b>Bodh Gayā,</b> where the Buddha was enlightened, is a short way south.</p></div></div>'))
pages.append(page('names','THE NAMES','Gaurī of good fortune',facts([
 ('Māṅgalyagaurī','<i>māṅgalya</i> “auspiciousness, the married state” + Gaurī'),
 ('Maṅgalā Gaurī','Her name in Gayā; also <b>Sarvamaṅgalā</b>'),
 ('Pālana Pīṭha','“Seat of nurture”, because the breast fell here'),
 ('Bhasmakūṭa','“Hill of ashes”: the hill she stands on'),
 ('Gayā','Named after the demon-saint <b>Gayāsura</b>')])
 +talk("Why is she linked with marriage?","Māṅgalya is the auspicious state of a married woman. Women pray to her for long, happy marriages.")))
pages.append(page('pitha','THE PĪṬHA','Where the breast fell',fig(560,170,'Shiva carrying Sati’s body as Vishnu’s discus cuts it, a piece falling onto a rocky hill above a river of sand',
 '<rect width="560" height="170" fill="#1a0e1e"/>'+STAR+SHIVA(150,40,.7)+SATI(220,60,.9,-8)+CHAKRA(300,70,14)+'<path d="M330 170 Q410 90 490 170z" fill="#8a9a6a"/><circle cx="400" cy="112" r="7" fill="#ffd166" stroke="#111"/><circle cx="416" cy="112" r="7" fill="#ffd166" stroke="#111"/><path d="M0 164 h560" stroke="#f4e6c0" stroke-width="10"/>')+'''<div class="steps">
<div><b>The breast.</b> As Śiva carried Satī’s body home toward Kailāsa, her <b>breast</b> fell on the Bhasmakūṭa hill at Gayā.</div>
<div><b>Two stones.</b> The Kālikā Purāṇa, as quoted locally, says it took the shape of <b>two stones</b>, worshipped in the sanctum to this day.</div>
<div><b>Nourishment.</b> The breast feeds; so here the Goddess is worshipped as the giver of nourishment, kindness and plenty.</div>
<div><b>Lists differ.</b> Some lists count Gayā as a lesser (upa-) Pīṭha; the Aṣṭādaśa hymn counts it among the eighteen great ones.</div>
</div>'''))
pages.append(page('temple','THE TEMPLE','A small shrine on a rocky hill',fig(560,180,'A small east-facing temple on a rocky hilltop reached by a long flight of steps, with smaller shrines beside it',
 '<rect width="560" height="180" fill="#cfe3f5"/><path d="M60 180 Q280 40 500 180z" fill="#8a9a6a" stroke="#111" stroke-width="2"/>'+''.join(f'<rect x="{160+i*12}" y="{170-i*10}" width="14" height="6" fill="#ccc" stroke="#111" stroke-width=".8"/>' for i in range(8))+TEMPLE(280,92,1,'#ffe1a8')+TEMPLE(360,112,.6,'#f2c9a0')+TEMPLE(210,112,.6,'#f2c9a0'))+facts([
 ('Faces','East, on the top of the hill'),
 ('Reached by','A flight of steps, or a road'),
 ('Sanctum','Cave-like and dark; the two stones are draped and worshipped by lamplight'),
 ('Age','The present building is often dated to the 15th century'),
 ('Complex','Shrines of Kālī, Gaṇeśa, Śiva and Hanumān'),
 ('Lamp','An undying lamp is said to burn in the sanctum')])))
pages.append(page('gayasura','GAYĀSURA','The demon-saint’s head',fig(560,140,'A giant lying across India with his head at Gaya marked, his navel at Jajpur and feet at Pithapuram',
 '<rect width="560" height="140" fill="#fdf1e8"/>'+GAYASURA(70,80,420)+'<circle cx="56" cy="74" r="10" fill="#c0392b" stroke="#111"/>'+T(56,40,'HEAD · GAYĀ',12,'#7a1d12','start')+T(280,40,'NAVEL · JĀJPUR',12,'#7a1d12')+T(500,40,'FEET · PĪṬHĀPURAM',12,'#7a1d12','end'))+'''<div class="steps">
<div><b>Too holy.</b> The Vāyu Purāṇa’s Gayā Māhātmya tells of <b>Gayāsura</b>, a giant whose penance made him so pure that whoever touched him went straight to heaven, emptying hell.</div>
<div><b>The altar.</b> The gods asked for his body as a place for a sacrifice. He lay down; when he still stirred, Viṣṇu pressed him still with his foot.</div>
<div><b>His boon.</b> Gayāsura asked that the gods stay on his body for ever, and that rites done there for the dead free them. So Gayā became the place of piṇḍa-dāna.</div>
<div><b>Three Gayās.</b> His head is at Gayā, his navel at Jājpur (Śakti Pīṭha 11) and his feet at Pīṭhāpuram (Śakti Pīṭha 10).</div>
</div>'''+talk("Three Śakti Pīṭhas sit on one giant?","Gayā, Jājpur, Pīṭhāpuram: his head, navel and feet are three Pīṭhas too. The two stories run side by side.")))
pages.append(page('vishnupada','VIṢṆUPADA','The footprint in stone',fig(560,170,'An octagonal temple tower by a riverbank and, inside, a footprint carved in black rock within a silver-rimmed basin',
 '<rect width="560" height="170" fill="#efe4cc"/>'+FOOT(160,100,1.2)+'<g transform="translate(400 160)" stroke="#111" stroke-width="2"><rect x="-50" y="-30" width="100" height="30" fill="#bbb"/><path d="M-36 -30 l10 -90 h52 l10 90z" fill="#ccc"/>'+''.join(f'<path d="M{-30+i*12} -30 v-80" stroke="#999" stroke-width="1"/>' for i in range(6))+'<circle cy="-126" r="8" fill="#e0a800"/></g>')+facts([
 ('What','A footprint about 40 cm long, carved in basalt, ringed by a silver basin'),
 ('Belief','Where Viṣṇu set his foot to hold Gayāsura down'),
 ('Temple','The present temple, by the Phalgu, was rebuilt by <b>Ahilyābāī Holkar</b> of Indore in <b>1787</b>'),
 ('Priests','The hereditary <b>Gayāwāl</b> paṇḍās guide the rites'),
 ('Akṣayavaṭa','An undying banyan nearby, where the last piṇḍas are offered')])))
pages.append(page('phalgu','THE PHALGU AND SĪTĀ’S CURSE','The river that hides',fig(560,170,'A woman offering balls of sand on a riverbank; a cow, a flowering bush and a priest looking away; the river vanishing into sand',
 '<rect width="560" height="170" fill="#fdf1e8"/><rect y="110" width="560" height="60" fill="#f4e6c0"/><path d="M0 140 h200" stroke="#4aa3df" stroke-width="10"/><path d="M200 140 h360" stroke="#9fd0ea" stroke-width="4" stroke-dasharray="8 8"/>'
 +person(260,130,'#c0392b','#f2c79b',1)+''.join(f'<circle cx="{300+i*16}" cy="132" r="6" fill="#e8d8a8" stroke="#111"/>' for i in range(3))
 +'<g transform="translate(420 130)" stroke="#111" stroke-width="2"><rect x="-26" y="-26" width="46" height="20" rx="8" fill="#fff"/><circle cx="28" cy="-28" r="9" fill="#fff"/></g>'+TEMPLE(500,140,.4,'#ffe1a8'))+'''<div class="steps">
<div><b>Daśaratha’s piṇḍa.</b> Rāma, Lakṣmaṇa and Sītā came to Gayā to offer piṇḍas for King Daśaratha. While the brothers were away fetching things for the rite, the king’s spirit appeared and asked Sītā for his offering at once.</div>
<div><b>Balls of sand.</b> With nothing else at hand, Sītā offered piṇḍas of sand, with the river, a cow, a ketakī flower and a brāhmaṇa as her witnesses.</div>
<div><b>Lies and a curse.</b> When Rāma returned, all but the banyan denied it. Sītā cursed the <b>Phalgu</b> to flow hidden under the sand; she blessed the banyan, the <b>Akṣayavaṭa</b>, to live for ever.</div>
<div><b>To this day.</b> For much of the year the Phalgu is a wide bed of sand; pilgrims dig to reach its water.</div>
</div>'''))
pages.append(page('pinda','PIṆḌA-DĀNA','Feeding the ancestors',facts([
 ('What','Offering <b>piṇḍas</b>, balls of rice or barley, to the departed, so they may find peace'),
 ('Why Gayā','Gayāsura’s boon: rites done here free the ancestors'),
 ('Vedīs','Rites are performed at many altars (vedīs) around the city: Viṣṇupada, the Phalgu, the Akṣayavaṭa, Pretaśilā, Rāmaśilā and more'),
 ('Pitṛ Pakṣa','The fortnight of the ancestors, in Bhādrapada–Āśvina, brings the largest crowds'),
 ('Gayā Śrāddha','Many Hindus aim to perform it once in life for their parents')])
 +talk("And Maṅgalā Gaurī fits in how?","Pilgrims who come to free their dead also climb the hill to ask the Mother's blessing for the living.")))
pages.append(page('vrata','MAṄGALĀ GAURĪ VRATA','Tuesdays in Śrāvaṇa',facts([
 ('When','Every <b>Tuesday</b> (Maṅgalavāra) of the month of <b>Śrāvaṇa</b>'),
 ('Who','Chiefly newly married women, for the first years of marriage'),
 ('Why','For a long life for one’s husband and a happy home'),
 ('Name','Maṅgalā Gaurī: Gaurī of auspiciousness, honoured on Maṅgala’s day'),
 ('At Gayā','Tuesdays and Śrāvaṇa bring women in great numbers to the hill')])
 +talk("The same Gaurī they worship at home?","The vrata is done all over India. At Gayā they worship her at her own Pīṭha.")))
pages.append(page('bodhgaya','GAYĀ AND BODH GAYĀ','Two traditions, one land',facts([
 ('Bodh Gayā','A short way south: where the Buddha attained enlightenment under the Bodhi tree'),
 ('Shared','Gayā is holy to Hindus and Buddhists alike'),
 ('An old reading','A 19th-century scholar read Gayāsura’s story as an allegory of Buddhism’s eclipse at Gayā; others reject it'),
 ('Ancient Gayā','Maurya-era caves in the nearby Barābar and Nāgārjunī hills')])))
pages.append(page('history','HISTORY','A city of rites',tl([
 ('Purāṇas','The Vāyu Purāṇa’s Gayā Māhātmya; the Padma, Agni and Devī Bhāgavata name Maṅgalā Gaurī.'),
 ('6th–5th c. BCE','The Buddha’s enlightenment at Bodh Gayā.'),
 ('3rd c. BCE','Mauryan cave-shelters in the Barābar hills nearby.'),
 ('15th c.','The present Maṅgalā Gaurī shrine, by common dating.'),
 ('1787','<b>Ahilyābāī Holkar</b> rebuilds Viṣṇupada.'),
 ('Today','Millions come in Pitṛ Pakṣa; Navarātri and Śrāvaṇa crowd the hill.')])))
pages.append(page('festivals','THROUGH THE YEAR','Navarātri and Śrāvaṇa',facts([
 ('Navarātri','Both, in Caitra and Āśvina: the hill’s great festivals'),
 ('Śrāvaṇa Tuesdays','The Maṅgalā Gaurī vrata'),
 ('Pitṛ Pakṣa','The great fair of the ancestors in the city below'),
 ('Daily','Lamps, red cloth and sindūr offered at the stones')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Māṅgalya','Auspiciousness, the married state'),('Pālana','Nurture'),('Bhasma','Ash'),('Kūṭa','Peak'),('Piṇḍa','Rice-ball offering to ancestors'),
 ('Śrāddha','Rites for the dead'),('Pitṛ','Ancestor'),('Vedī','Altar'),('Pada','Foot'),('Vaṭa','Banyan'),('Vrata','Vow, observance')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>The Pīṭha.</b> Satī’s breast on the Bhasmakūṭa hill: Māṅgalyagaurī, Goddess of nourishment and good fortune.</div>
<div><b>The form.</b> Two stones in a small east-facing shrine.</div>
<div><b>Gayā.</b> Gayāsura’s head; Viṣṇu’s footprint; the hidden Phalgu; the undying banyan.</div>
<div><b>The rites.</b> Piṇḍa-dāna for the dead below, blessings for the living above.</div>
<div><b>The vow.</b> Maṅgalā Gaurī vrata on Śrāvaṇa Tuesdays.</div>
</div>'''+talk("One line to remember?","In the city where the dead are fed, the Mother who feeds sits on the hill.")+'<div class="key">The sixteenth seat of the Mother: <b>Māṅgalyagaurī of Gayā</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Mangla Gauri Temple” (Padma, Vāyu, Agni, Devī Bhāgavata, Mārkaṇḍeya Purāṇas; east-facing on the hill; breast; complex; upa-pīṭha in one version). Incredible India (breast; nourishment). Government of Bihar (eighteen Mahā Pīṭhas). devdhamyatra.com (Bhasmakūṭa; Kālikā Purāṇa: two stones; Pālana Pīṭha). templesinindiainfo.com (steps and road; carved sculptures). templepurohit.com and exploreourindia.com (15th c.). Law, <i>Geographical Dictionary</i> via jainqq.org (Bhasmakūṭa spur of Brahmayoni; Gayā Māhātmya in the Vāyu Purāṇa; Mitra’s allegory reading).</p>
<p><b>Gayā:</b> Wikipedia, “Vishnupad Temple” (Phalgu; Gayāsura pinned; Akṣayavaṭa; rebuilt by Ahilyābāī Holkar 1787). Government of Bihar (Rāma and Sītā; 1787). Tibetan Buddhist Encyclopedia (surrounding hills; basalt footprint; Gayāwāl paṇḍās).</p>
<p><b>Sources differ:</b> Mahā or upa-pīṭha; the temple’s age. <b>Not verified, tradition only:</b> the undying lamp; Sītā’s witnesses as listed (versions vary); the footprint’s size. Maps are schematic. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('where','Where It Is'),('names','The Names'),('pitha','The Pīṭha'),('temple','The Temple'),('gayasura','Gayāsura'),('vishnupada','Viṣṇupada'),('phalgu','The Phalgu and Sītā’s Curse'),
 ('pinda','Piṇḍa-dāna'),('vrata','Maṅgalā Gaurī Vrata'),('bodhgaya','Gayā and Bodh Gayā'),('history','History'),('festivals','Through the Year'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">ŚAKTI PĪṬHA 16 OF 18</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(20px,6.4vw,64px)">MĀṄGALYAGAURĪ</h1>
  <div class="series">GAYĀ · A REFERENCE GUIDE</div>
  <div class="tag">The Mother who nourishes, in the city of the ancestors</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Gayā is where Hindus come to feed their dead. At the footprint of Viṣṇu by the sandy Phalgu, families offer rice-balls so their ancestors may rest.</p>
    <p>Above the city, on a rocky hill, sits the Goddess who feeds the living: <b>Maṅgalā Gaurī</b>, the <b>Māṅgalyagaurī</b> of the Śakti Pīṭha hymn. Here, tradition says, Satī’s breast fell, and she is worshipped as two stones in a small dark shrine.</p>
    <p>This guide tells her story, and the stories of Gayā around her: a giant who gave his body, a river cursed to hide, and a banyan that cannot die.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Maṅgalā Gaurī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Why would a Goddess of good fortune live above a city of funerals?","Because grief and blessing go together. You free your parents below, and ask the Mother to look after your children above.")}
  <div class="panel reading small"><p>Part of <a href="{SER}">The 18 Śakti Pīṭhas</a>. Start with the <a href="{SER}ashtadasha-shakti-peetha-stotram/">overview and the hymn</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/Mangalyagauri_Gaya.html','w').write(head+b+tail())
print('ok',len(pages))
