exec(open('/home/claude/work/shakti/dv_common.py').read())
head=head_vis('Paraśurāma · Daśāvatāra 6 · srini.presents','Paraśurāma, Rāma with the axe, sixth avatāra of Viṣṇu: son of Jamadagni and Reṇukā, the axe from Śiva, the hard command and Reṇukā restored, Kārtavīrya Arjuna and the wish-cow, twenty-one campaigns against cruel kings, the gift of the earth to Kaśyapa, the meeting with Rāma, the teacher of Bhīṣma, Droṇa and Karṇa, the land raised from the sea from Gokarṇa to Kerala, Udupi’s Paraśurāma Kṣetra, Saundatti and Māhūr, and the immortal sage on Mahendra. An illustrated reference guide.')
def AXEMAN(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 50 q-4 -60 30 -70 q34 10 30 70z" fill="#e05a3a"/>'
 '<path d="M-22 -6 l-24 20 M22 -6 l26 -30" stroke="#c98b5a" stroke-width="8"/><path d="M48 -40 v100" stroke="#7a4a1a" stroke-width="6"/><path d="M48 -40 q34 6 30 34 q-16 -6 -30 -6z" fill="#ccc"/>'
 '<circle cy="-36" r="15" fill="#c98b5a"/><path d="M-12 -46 q12 -16 24 0 q-4 -14 -12 -16 q-8 2 -12 16z" fill="#3a2a1a"/><circle cx="-5" cy="-38" r="2.4" fill="#111"/><circle cx="5" cy="-38" r="2.4" fill="#111"/><path d="M-6 -28 h12" /><path d="M-10 -6 l20 0" stroke="#fff" stroke-width="1.5"/></g>')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="A matted-haired warrior sage holding a great axe, standing on a coast with the sea pulling back">'
 '<rect width="380" height="268" fill="#0d3f73" rx="8"/>'+STAR+'<path d="M0 268 L0 190 Q120 170 200 200 L380 160 V268Z" fill="#5a9a4a"/><path d="M200 200 L380 160 V268 H260Z" fill="#1d5f9a"/>'+''.join(f'<path d="M{50+i*40} {160-i*4} l-10 30" stroke="#2a7a3a" stroke-width="3"/><circle cx="{50+i*40}" cy="{156-i*4}" r="9" fill="#2a9d6f"/>' for i in range(3))+AXEMAN(190,200,1.3)+'</svg>')
cov=cover_dv('DAŚĀVATĀRA 6 OF 10','PARAŚURĀMA',13,'The Brahmin warrior',art)
fw=foreword_dv('Keśava dhṛta-bhṛgupati-rūpa,',[
 'The sixth avatāra carries an axe. <b>Paraśurāma</b>, “Rāma with the axe”, was born a Brahmin, son of the sage <b>Jamadagni</b> and <b>Reṇukā</b>, but lived as a warrior. He won his axe from Śiva himself.',
 'When the thousand-armed king <b>Kārtavīrya Arjuna</b> stole his father’s wish-granting cow, and the king’s sons later killed his father, Paraśurāma swore to rid the earth of arrogant rulers, and did so twenty-one times. Then he gave the whole earth away and went to the mountains to meditate. On the west coast he is the hero who threw his axe into the sea and raised new land: the coast from Gokarṇa to Kerala, including Udupi’s Tuḷunāḍu.',
 'He is also the great teacher of the Mahābhārata, and the only avatāra said to be still alive.'],
 'An avatāra who is still alive?','He is one of the seven Cirañjīvins, the long-lived ones. Tradition says he will teach Kalki.',
 series_note_dv(6))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Avatāra','<b>Sixth</b> of the ten; Tretā Yuga (at its start)'),('Form','A Brahmin sage-warrior with matted hair and an <b>axe</b> (paraśu)'),
 ('Parents','The sage Jamadagni of the Bhṛgu line, and Reṇukā'),('Deeds','Slays Kārtavīrya Arjuna; humbles proud kings 21 times; gives the earth to Kaśyapa'),
 ('Teacher','Of Bhīṣma, Droṇa and Karṇa in the Mahābhārata'),('West coast','Raises the land from Gokarṇa to Kerala from the sea'),
 ('Cirañjīvin','Still alive, on Mount Mahendra'),('Day','Paraśurāma Jayantī, Akṣaya Tṛtīyā')])
 +talk("A Brahmin who fights?","That's the surprise. He's the priest's son who became the greatest warrior of his age.")))
pages.append(page('names','NAMES','Rāma of the Bhṛgus',facts([
 ('Paraśurāma','<i>paraśu</i> axe + Rāma'),('Bhārgava Rāma','Rāma of the Bhṛgu family'),('Jāmadagnya','Son of Jamadagni'),('Bhṛgupati','“Lord of the Bhṛgus”: Jayadeva’s word'),('Rāma','His birth name; the axe was added later'),('Three Rāmas','Paraśurāma, Rāma of Ayodhyā and Balarāma')])))
pages.append(page('axe','THE AXE FROM ŚIVA','How Rāma got his paraśu',facts([
 ('The student','The young Rāma went to the Himālaya and did penance to Śiva'),
 ('The gift','Pleased, Śiva taught him the arts of war and gave him the axe and divine weapons'),
 ('The name','From then on he was Paraśurāma'),
 ('Gaṇeśa','A later story says he struck Gaṇeśa with the axe when he blocked his way to Śiva, breaking one of Gaṇeśa’s tusks'),
 ('Meaning','Even Viṣṇu’s avatāra learns from Śiva: the gods help each other')])))
pages.append(page('renuka','THE HARD COMMAND','Reṇukā and the sons',fig(560,160,'A sage pointing, a young man with an axe, and a woman restored to life with light around her',
 '<rect width="560" height="160" fill="#fdf1e8"/>'+person(110,140,'#f4f4f4','#c98b5a',1)+AXEMAN(280,110,.8)+GENTLE(440,110,.75)+'<circle cx="440" cy="80" r="40" fill="none" stroke="#ffd60a" stroke-width="3"/>')+facts([
 ('The lapse','Reṇukā, fetching water, was lost for a moment in admiring a passing celestial king; Jamadagni saw it and was enraged'),
 ('The order','He told his sons to kill her. The elder four refused; Paraśurāma obeyed'),
 ('The boon','Pleased, Jamadagni offered a boon. Paraśurāma asked that his mother and brothers be restored, with no memory of it. All came back to life'),
 ('Reṇukā','She is worshipped as a goddess, as Yellammā at Saundatti in Karnataka and at Māhūr in Mahārāṣṭra'),
 ('Our note','A hard story, told in the Mahābhārata and Purāṇas, about obedience and its limits')])
 +'<div class="key">See: <a href="/bhakti/temples-of-india/18-shakti-peethas/ekavirika-mahur/">Ekavīrikā, Māhūr</a></div>'))
pages.append(page('kartavirya','THE THOUSAND-ARMED KING','Kārtavīrya Arjuna and the cow',fig(560,170,'A many-armed king leading away a white cow while a sage protests',
 '<rect width="560" height="170" fill="#eef3fa"/>'+KING(200,150,1.1)+''.join(f'<path d="M200 100 l{50*__import__("math").cos(a/3):.0f} {-50*__import__("math").sin(a/3):.0f}" stroke="#c98b5a" stroke-width="4"/>' for a in range(1,9))+'<g transform="translate(380 130)" stroke="#111" stroke-width="2"><path d="M-40 0 q-4 -30 30 -30 h30 q14 0 16 14 l8 4 v10 h-14z" fill="#fff"/><path d="M-30 0 v20 M20 0 v20" stroke-width="5"/></g>'+person(500,150,'#f4f4f4','#c98b5a',.8))+facts([
 ('Who','Kārtavīrya Arjuna (Sahasrārjuna), king of the Haihayas, who had a thousand arms by the boon of Dattātreya'),
 ('The visit','Jamadagni fed the king and his whole army with the help of his wish-granting cow, Kāmadhenu'),
 ('The theft','The king wanted the cow and took her by force'),
 ('The answer','Paraśurāma pursued him, cut off his thousand arms and killed him, and brought the cow home')])))
pages.append(page('vow','TWENTY-ONE TIMES','The great vow',facts([
 ('Revenge','The king’s sons came while Paraśurāma was away and killed Jamadagni'),
 ('The grief','Reṇukā beat her breast twenty-one times'),
 ('The vow','Paraśurāma swore to clear the earth of arrogant kṣatriya rulers twenty-one times'),
 ('Samantapañcaka','He filled five lakes with their blood at Kurukṣetra and offered the waters to his ancestors'),
 ('The end','His ancestors asked him to stop; he gave the whole earth to the sage Kaśyapa and left for Mount Mahendra')])
 +talk("Twenty-one times! Isn't that terrible?","The texts don't hide it. He stands for justice that has gone too far, and he himself stops.")))
pages.append(page('rama','THE TWO RĀMAS MEET','After the broken bow',fig(560,160,'A warrior with an axe facing a young prince who holds a bow',
 '<rect width="560" height="160" fill="#fff4dc"/>'+AXEMAN(180,110,.9)+AV(7,380,110,1.3))+facts([
 ('The bow','At Sītā’s svayaṃvara, Rāma of Ayodhyā broke Śiva’s great bow'),
 ('The challenge','Paraśurāma arrived in fury and challenged him to string Viṣṇu’s bow'),
 ('The answer','Rāma strung it easily'),
 ('The handover','Paraśurāma recognised Viṣṇu in Rāma, yielded his power and went back to his penance'),
 ('Meaning','One avatāra steps aside for the next')])
 +'<div class="key">Next avatāra: <a href="'+DVS+'rama/">Rāma</a></div>'))
pages.append(page('guru','TEACHER OF THE MAHĀBHĀRATA','Bhīṣma, Droṇa and Karṇa',facts([
 ('Bhīṣma','Learned arms from him; later they fought to a standstill over Ambā'),
 ('Droṇa','Received weapons and knowledge from him'),
 ('Karṇa','Came to him pretending to be a Brahmin. When a stinging insect bit Karṇa’s thigh and he bore it without moving, his guru knew he was a kṣatriya and cursed him to forget his weapons at his hour of need'),
 ('Meaning','The teacher who shaped the greatest warriors of the epic')])
 +talk("He cursed his own student?","For the lie. Karṇa's curse came true on the field of Kurukṣetra.")))
pages.append(page('coast','LAND FROM THE SEA','Gokarṇa to Kerala',fig(560,180,'A warrior throwing an axe far out to sea, the sea pulling back to reveal green land',
 '<rect width="560" height="180" fill="#cfe8f6"/><path d="M0 180 V60 Q60 70 120 60 V180Z" fill="#5a9a4a"/><path d="M120 60 Q260 90 420 70 V180 H120Z" fill="#8ac07a"/>'+AXEMAN(80,110,.7)+'<path d="M120 60 q140 -60 300 0" stroke="#111" stroke-dasharray="6 6" fill="none"/><path d="M420 60 l20 -10 v20z" fill="#ccc" stroke="#111"/>')+facts([
 ('The story','Having given away the earth, Paraśurāma had no land of his own; he asked Varuṇa, god of the sea, for some'),
 ('The throw','He threw his axe from the Sahyādri hills, and the sea drew back as far as it flew'),
 ('The land','The coast from Gokarṇa to Kanyākumārī rose: Paraśurāma Kṣetra'),
 ('Tuḷunāḍu','Coastal Karnataka, with Udupi, is part of this land; seven Paraśurāma kṣetras are listed there'),
 ('Kerala','The Kēraḷōlpatti tradition says he founded Kerala and its 64 villages'),
 ('Geology','Scientists point out that this coast did rise from the sea over long ages')])
 +talk("A myth that matches geology?","The coast really was under the sea once. The legend remembers it as an axe throw.")))
pages.append(page('places','PARAŚURĀMA PLACES','Temples and tīrthas',facts([
 ('Udupi and Tuḷunāḍu','Paraśurāma Kṣetra; a Paraśurāma theme park and shrines along the coast'),
 ('Saundatti','Yellammā (Reṇukā) temple, Beḷagāvi district, Karnataka, linked to Jamadagni’s hermitage'),
 ('Chiplūṇ','A Paraśurāma temple in the Konkan, Mahārāṣṭra'),
 ('Paraśurām Kuṇḍ','Lohit district, Arunachal Pradesh: tradition says he washed away his sin here; a fair at Makara Saṅkrānti'),
 ('Mahendragiri','The mountain in Odisha where he is said to live on'),
 ('Tṛkkākara','Tradition says he founded the Vāmana temple there')])))
pages.append(page('cirajivi','THE LONG-LIVED ONE','Cirañjīvin',facts([
 ('The seven','Aśvatthāmā, Bali, Vyāsa, Hanumān, Vibhīṣaṇa, Kṛpa and Paraśurāma are traditionally named as cirañjīvins'),
 ('Where','On Mahendra mountain, in meditation'),
 ('Future','The Kalki Purāṇa says he will teach Kalki the arts of war'),
 ('Two at once','He is an avatāra who lives alongside the next one, Rāma')])
 +'<div class="key">See: <a href="'+DVS+'kalki/">Kalki</a></div>'))
pages.append(page('festivals','THROUGH THE YEAR','His days',facts([
 ('Paraśurāma Jayantī','Vaiśākha Śukla Tṛtīyā, Akṣaya Tṛtīyā (Apr–May)'),('Saundatti','Yellammā’s fairs in Māgha and on full moons'),('Paraśurām Kuṇḍ','Makara Saṅkrānti (Jan)')])))
pages.append(page('meaning','WHAT PARAŚURĀMA TEACHES','The wisdom of the axe',facts([
 ('Power checks power','Rulers who abuse their power will be brought down'),
 ('Anger has limits','Even he stopped and gave everything away'),
 ('Step aside','He yielded to Rāma when his time was done'),
 ('Truth with teachers','Karṇa’s lie cost him dearly')])
 +talk("What should I take from Paraśurāma?","Stand against bullies. Then know when to put the axe down.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Paraśu','Axe'),('Bhārgava','Of the Bhṛgu clan'),('Kṣatriya','Warrior-ruler class'),('Kāmadhenu','Wish-granting cow'),('Svayaṃvara','Bride’s choice of groom'),('Cirañjīvin','Long-lived immortal'),('Kṣetra','Sacred land'),('Kēraḷōlpatti','Origin legend of Kerala')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Paraśurāma, Rāma with the axe, sixth avatāra; son of Jamadagni and Reṇukā.</div>
<div><b>Deeds.</b> The axe from Śiva; Kārtavīrya’s death; 21 campaigns; the earth given to Kaśyapa.</div>
<div><b>Links.</b> Yields to Rāma; teaches Bhīṣma, Droṇa and Karṇa.</div>
<div><b>West coast.</b> The axe throw that raised Gokarṇa to Kerala; Udupi; Saundatti.</div>
<div><b>Lesson.</b> Fight injustice, then lay down the axe.</div>
</div>'''+talk("One line to remember?","A priest with an axe, who knew when to stop.")+'<div class="key">Next: <a href="'+DVS+'rama/">Rāma, the prince of Ayodhyā</a></div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Texts:</b> Mahābhārata, Vana Parva 116–117 and Śānti Parva 49 (Reṇukā, Kārtavīrya, 21 campaigns, Samantapañcaka, gift to Kaśyapa); Bhāgavata Purāṇa 9.15–16; Vālmīki Rāmāyaṇa, Bāla Kāṇḍa 74–76 (meeting with Rāma); Mahābhārata, Śānti Parva 3 (Karṇa’s curse); Brahmāṇḍa Purāṇa (Gaṇeśa’s tusk); Kēraḷōlpatti; Kalki Purāṇa.</p>
<p><b>Places:</b> Saundatti Yellammā, Udupi and Tuḷunāḍu traditions; Paraśurām Kuṇḍ (Arunachal Pradesh); Chiplūṇ; Thrikkakara temple tradition (Wikipedia).</p>
<p><b>Sources differ / unverified:</b> the identity of Reṇukā with Yellammā is a regional tradition; the number and list of the seven Paraśurāma kṣetras; the Gaṇeśa tusk story is late; geological links are general. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('axe','The Axe from Śiva'),('renuka','The Hard Command'),('kartavirya','The Thousand-Armed King'),('vow','Twenty-One Times'),('rama','The Two Rāmas Meet'),('guru','Teacher of the Mahābhārata'),
 ('coast','Land from the Sea'),('places','Paraśurāma Places'),('cirajivi','The Long-Lived One'),('festivals','Through the Year'),('meaning','What Paraśurāma Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/DV6_Parashurama.html',head,cov,fw,pages,toc)
