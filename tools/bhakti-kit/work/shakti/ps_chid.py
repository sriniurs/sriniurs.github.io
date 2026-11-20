exec(open('/home/claude/work/shakti/ps_common.py').read())
head=head_navy('Naṭarāja, Cidambaram · Pañcabhūta Sthala of Space · srini.presents',
 'The Naṭarāja temple of Cidambaram (Tillai): Śiva as space (Ākāśa), the dance of bliss seen by Patañjali and Vyāghrapāda, the Naṭarāja image explained, the Secret of Cidambaram, the golden roof, the five halls, the dance contest with Kāḷī, Govindarāja inside, the Dīkṣitars and the 2014 ruling, Nandanār, Māṇikkavācakar and the rediscovered Tēvāram, Ārudrā and Āṉi Tirumañjaṉam. An illustrated reference guide.')
def NATA(x,y,s=1):
    ring=''.join(f'<path d="M{70*__import__("math").cos(a/10):.1f} {-60+70*__import__("math").sin(a/10):.1f} l{6*__import__("math").cos(a/10):.1f} {6*__import__("math").sin(a/10):.1f}" stroke="#ff8c1a" stroke-width="4"/>' for a in range(-31,1,3))
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-70 0 A70 70 0 1 1 70 0" fill="none" stroke="#e0a800" stroke-width="5" transform="translate(0 -60)"/>{ring}'
     '<ellipse cx="0" cy="10" rx="80" ry="8" fill="#c9a26b"/><path d="M-30 6 q30 -14 60 0 q-30 10 -60 0z" fill="#3a5a2a"/>'
     '<path d="M0 -60 l-6 40 l-14 22" stroke="#c8a060" stroke-width="7" fill="none"/><path d="M0 -60 l10 26 l30 -14" stroke="#c8a060" stroke-width="7" fill="none"/>'
     '<path d="M0 -94 v34" stroke="#c8a060" stroke-width="12"/><path d="M-6 -86 l-32 -10 M6 -86 l30 -14 M-6 -76 l-28 6 M6 -76 l26 8" stroke="#c8a060" stroke-width="6"/>'
     '<path d="M-44 -100 l-4 -8 l8 0z" fill="#e0e0e0"/><path d="M36 -104 q4 -12 -2 -16 q-6 8 2 16z" fill="#ff8c1a"/>'
     '<circle cy="-108" r="12" fill="#c8a060"/><path d="M-10 -116 q-26 -10 -40 2 M10 -116 q26 -10 40 2 M-10 -112 q-26 2 -36 14 M10 -112 q26 2 36 14" stroke="#c8a060" stroke-width="3" fill="none"/>'
     '<path d="M-8 -122 h16 l-3 -10 h-10z" fill="#e0a800"/></g>')
def CURTAIN(x,y,s=1,open_=True):
    c='<path d="M-60 -120 h50 v120 h-50z" fill="#1d1d2a"/><path d="M10 -120 h50 v120 h-50z" fill="#c0392b"/>' if open_ else '<path d="M-60 -120 h120 v120 h-120z" fill="#1d1d2a"/>'
    bil=''.join(f'<path d="M{-30+i*10} {-90+(i%2)*6} q4 -8 8 0 q-4 6 -8 0z" fill="#e0a800" stroke="#111" stroke-width="1"/>' for i in range(7))
    return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-70" y="-130" width="140" height="130" fill="#0b0b18"/>{bil}{c}</g>'
def ROOF(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><rect x="-90" y="-50" width="180" height="50" fill="#c9a26b"/>'
 '<path d="M-110 -50 q110 -70 220 0z" fill="#e0a800"/>'+''.join(f'<path d="M{-90+i*20} -50 q{110-(-90+i*20)} -60 0 -64" stroke="#b08000" stroke-width="1" fill="none"/>' for i in range(0))+''.join(f'<path d="M{-80+i*20} -54 q0 -20 0 -24" stroke="#b08000" fill="none"/>' for i in range(9))
 +''.join(f'<path d="M{-40+i*10} -96 v-10" stroke="#e0a800" stroke-width="4"/><circle cx="{-40+i*10}" cy="-108" r="3" fill="#e0a800"/>' for i in range(9))+'</g>')
art=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Nataraja dancing in a ring of fire under a golden roof, with a curtain and empty space beside him">'
 '<rect width="380" height="268" fill="#1d1040" rx="8"/>'+STAR+NATA(150,236,1.25)+CURTAIN(310,246,.7)+'</svg>')
cov=cover('PAÑCABHŪTA 5 · SPACE','CIDAMBARAM',15,'Naṭarāja: Śiva as space',art)
fw=foreword('Om Naṭarājāya namaḥ,',[
 'The last element is the one that holds all the others: <b>space</b>. At <b>Cidambaram</b>, the old forest of Tillai, Śiva is worshipped as space itself. In the sanctum he dances as <b>Naṭarāja</b>, the Lord of Dance, under a roof of gold. Beside him, behind a curtain, is the <b>Secret of Cidambaram</b>: an empty space hung with a garland of golden bilva leaves.',
 'The sages Patañjali and Vyāghrapāda waited here to see his dance of bliss. The Tamil saints sang it, a Chola king gilded its roof, the lost Tēvāram was found in its locked room, and the poet Cēkkiḻār first recited the lives of the 63 saints in its hall. Viṣṇu reclines in the same courtyard.',
 'This guide explains the dance, the secret and the temple, and the people of Tillai.'],
 'Worship an empty space?','Space has no shape, so the highest form here is no form. The dance and the emptiness are the same God.',
 series_note(prev=('kalahastishvara','Kāḷahastīśvara, Śrīkāḷahasti (air)')))
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Element','<b>Space</b> (Ākāśa): the fifth Pañcabhūta Sthala'),
 ('Śiva as','<b>Naṭarāja</b>, Lord of Dance; also Sabhānāyaka, Lord of the Hall'),
 ('Liṅga','The <b>Ākāśa liṅga</b>: the empty space of the Cidambara Rahasyam'),
 ('Goddess','<b>Śivakāmasundarī</b>'),
 ('Where','Cidambaram, Cuddalore district, Tamil Nadu, near the coast and the Picāvaram mangroves'),
 ('Roof','The golden roof of the Cit Sabhā, gilded by Chola kings in the 10th century'),
 ('Priests','The Poṭu Dīkṣitars, hereditary priests and managers of the temple'),
 ('Also','Govindarāja Perumāḷ, a Divya Deśam of Viṣṇu, inside the temple')])
 +talk("Is Cidambaram the most important Śiva temple?","For Tamil Śaivas, simply “the Temple” (Kōyil) means Cidambaram.")))
pages.append(page('names','NAMES','Hall of consciousness',facts([
 ('Cidambaram','<i>cit</i> consciousness + <i>ambara</i> sky, space: “the space of awareness”'),
 ('Ciṟṟambalam','Tamil: “the little hall”, the sanctum'),
 ('Tillai','The old name, from the tillai mangrove trees that grew here'),
 ('Poṉṉambalam','“The golden hall”'),
 ('Kōyil','“The Temple”, as Tamil Śaivas call it'),
 ('Abhrasadas','“Hall in the sky”: its Sanskrit name in the verse on liberation')])
 +talk("Consciousness and sky in one word?","That's the whole idea. Inner space and outer space are the same space.")))
pages.append(page('dance','THE DANCE OF BLISS','Patañjali and Vyāghrapāda',fig(560,200,'Two sages, one with a serpent body and one with tiger feet, watching Shiva dance',
 '<rect width="560" height="200" fill="#1d1040"/>'+NATA(280,190,1.0)+'<g transform="translate(110 180)" stroke="#111" stroke-width="2"><path d="M-30 0 q10 -20 20 0 q10 20 20 0 q10 -20 20 0" stroke="#3a6a3a" stroke-width="10" fill="none"/></g>'+person(110,150,'#e08a2a','#c98b5a',.7)+person(450,170,'#e08a2a','#c98b5a',.8)+'<path d="M440 172 l-8 6 M460 172 l8 6" stroke="#e0a800" stroke-width="4"/>')+'''<div class="steps">
<div><b>Two sages.</b> Patañjali, said to be Ādiśeṣa, the cosmic serpent, in human form, and Vyāghrapāda, “tiger-foot”, who asked for tiger’s claws to climb trees and pick unspoilt flowers for Śiva, longed to see Śiva’s dance.</div>
<div><b>The wait.</b> They worshipped in the Tillai forest for ages.</div>
<div><b>The dance.</b> On Tai Pūsam, in the month of Tai, Śiva danced the Ānanda Tāṇḍava, the dance of bliss, for them in the golden hall, and promised to dance there forever.</div>
</div>'''+talk("Patañjali of the Yoga Sūtras?","Tradition identifies the two. His Naṭarāja hymn without long vowels is still sung here.")))
pages.append(page('icon','THE NAṬARĀJA IMAGE','Every detail means something',fig(560,240,'Nataraja image labelled: drum, fire, fear-not hand, pointing hand, raised foot, dwarf under foot, ring of flames',
 '<rect width="560" height="240" fill="#fff8e7"/>'+NATA(280,220,1.35)+T(120,60,'drum: creation',12)+T(450,50,'fire: dissolution',12)+T(110,140,'fear not',12)+T(460,130,'raised foot: release',12)+T(280,236,'Apasmāra: ignorance',12))+facts([
 ('Ḍamaru (drum)','The first sound: creation'),
 ('Agni (fire)','Dissolution'),
 ('Abhaya hand','“Do not fear”: protection'),
 ('Pointing hand','To the raised foot: refuge and release'),
 ('Apasmāra','The dwarf of forgetfulness crushed underfoot'),
 ('Ring of fire','The cosmos, endlessly made and unmade'),
 ('Five acts','Creation, sustenance, dissolution, concealment and grace: the whole cosmos in one dance')])))
pages.append(page('three','THREE FORMS OF ŚIVA','Form, form-and-formless, formless',facts([
 ('Rūpa · form','Naṭarāja, the dancing image'),
 ('Rūpārūpa · form and formless','The crystal liṅga, Candramauḷīśvara, bathed several times a day'),
 ('Arūpa · formless','The empty space of the Rahasyam'),
 ('Ratnasabhāpati','A small emerald Naṭarāja, bathed once a day'),
 ('One sanctum','All three in the Cit Sabhā')])
 +talk("Three Śivas in one room?","One Śiva, shown three ways: shape, half-shape, no shape. You choose where your mind can rest.")))
pages.append(page('rahasyam','THE SECRET OF CIDAMBARAM','Cidambara Rahasyam',fig(560,200,'A dark niche with a garland of golden leaves, a curtain black outside and red inside, drawn back',
 '<rect width="560" height="200" fill="#fdf1e8"/>'+CURTAIN(280,180,1.2)+person(120,180,'#e08a2a','#c98b5a',.9)+'<path d="M140 140 h40 l-6 6 h-28z" fill="#c9a26b" stroke="#111"/><path d="M160 140 q-6 -12 0 -20 q6 8 0 20z" fill="#ff8c1a" stroke="#111"/>')+facts([
 ('Where','To the right of Naṭarāja in the Cit Sabhā'),
 ('What you see','A curtain is drawn aside during the pūjā: behind it, empty space and a hanging garland of golden bilva leaves'),
 ('The curtain','Black outside for ignorance, red inside for knowledge'),
 ('Meaning','Śiva as pure space, without form: when ignorance is drawn aside, there is only the infinite'),
 ('“Rahasyam”','The saying “that’s the secret of Cidambaram” now means a hidden truth, in Tamil and beyond')])
 +talk("Nothing there?","Nothing that is a thing. That's the secret.")))
pages.append(page('roof','THE GOLDEN ROOF','Poṉṉambalam',fig(560,180,'A hall with a curved golden roof and nine golden finials',
 '<rect width="560" height="180" fill="#eef3fa"/>'+ROOF(280,170,1.3))+facts([
 ('Gilded','By the Chola king Parāntaka I (907–955), who took the title “the king who roofed the hall of Tillai with gold”; Āditya I is also credited'),
 ('21,600 tiles','Said to equal the breaths a person takes in a day'),
 ('72,000 nails','Said to equal the nāḍīs, channels of the subtle body'),
 ('Nine finials','The nine kalaśas, for nine forms of energy'),
 ('Our note','The counts are the temple’s symbolic tradition; sources also give 26,000 or 22,600 tiles')])
 +talk("Did they really count breaths?","15 breaths a minute × 60 × 24 = 21,600. The roof is a lesson in arithmetic and yoga.")))
pages.append(page('sabhas','THE FIVE HALLS','Pañca Sabhā',facts([
 ('Cit Sabhā','The sanctum hall where Naṭarāja dances, the Ciṟṟambalam'),
 ('Kanaka Sabhā','The golden hall in front of it, where daily rites are performed'),
 ('Nṛtta Sabhā','The hall of the dance contest, carved like a chariot'),
 ('Deva Sabhā','Where the processional images are kept'),
 ('Rāja Sabhā','The thousand-pillared hall, where great festivals and gatherings are held')])
 +talk("Five halls for five elements?","A neat parallel some teachers draw. The halls are also the dance stages of Śiva's life here.")))
pages.append(page('kali','THE DANCE CONTEST','Śiva and Kāḷī',fig(560,170,'Shiva dancing with one leg raised straight up, and Kali watching',
 '<rect width="560" height="170" fill="#1d1d2a"/><g transform="translate(200 160)" stroke="#111" stroke-width="2"><path d="M0 -60 v40" stroke="#c8a060" stroke-width="10"/><path d="M0 -20 l-6 20" stroke="#c8a060" stroke-width="7"/><path d="M0 -24 l4 -70" stroke="#c8a060" stroke-width="7"/><circle cy="-72" r="11" fill="#c8a060"/></g>'+FIERCE(380,110,.8))+facts([
 ('The challenge','Kāḷī, the guardian of Tillai, challenged Śiva to a dance contest'),
 ('The move','Śiva raised one leg straight up to his ear: the Ūrdhva Tāṇḍava'),
 ('The end','Kāḷī would not do that pose and accepted defeat'),
 ('Tillai Kāḷī','She went to the edge of town, where her temple still stands; worshippers visit her too'),
 ('Where','The Nṛtta Sabhā carvings show the contest')])))
pages.append(page('vishnu','GOVINDARĀJA PERUMĀḶ','Viṣṇu in the same courtyard',fig(560,150,'Nataraja dancing and Vishnu reclining side by side',
 '<rect width="560" height="150" fill="#eef3fa"/>'+NATA(180,140,.75)+'<g transform="translate(400 120)" stroke="#111" stroke-width="2"><path d="M-80 10 q80 20 160 0 q-10 14 -80 16 q-70 -2 -80 -16z" fill="#7aa86a"/><path d="M-60 0 q60 -18 120 -4" fill="none" stroke="#3b6fd0" stroke-width="15"/><circle cx="-58" cy="-8" r="11" fill="#3b6fd0"/></g>')+facts([
 ('What','A shrine of Viṣṇu reclining (Govindarāja), the Tillai Tiruccitrakūṭam, one of the 108 Divya Deśams'),
 ('Unique','From one spot, devotees can see both Naṭarāja and Govindarāja'),
 ('History','The shrine had a troubled past: sources say a Chola king removed the image in the 12th century, and it was reinstated under Vijayanagara rule in the 16th'),
 ('Story','Viṣṇu is said to have watched the dance contest as witness, playing the drum for Śiva in some tellings')])
 +talk("Śiva and Viṣṇu side by side?","Here more than anywhere. The past had quarrels; the present has both.")))
pages.append(page('gopurams','FOUR TOWERS AND 108 POSES','Dance in stone',fig(560,190,'A temple tower with small dancing figures carved on its gateway',
 '<rect width="560" height="190" fill="#fff4dc"/>'+GOPURAM(280,186,.9,'#e8d8b0',7)+''.join(f'<g transform="translate({140+(i%6)*56} {150-(i//6)*30}) scale(.25)"><path d="M0 -60 v40 l-14 22 M0 -40 l20 -10" stroke="#7a5a2a" stroke-width="8" fill="none"/><circle cy="-70" r="9" fill="#7a5a2a"/></g>' for i in range(0)))+facts([
 ('Four towers','Seven-tiered gopurams on four sides, built between the 12th and 16th centuries'),
 ('108 karaṇas','The eastern and western towers carry carvings of the 108 dance poses of Bharata’s <i>Nāṭyaśāstra</i>, with their verses'),
 ('Dancers','Bharatanāṭyam dancers study these panels'),
 ('Śivagaṅgā','The temple tank'),
 ('Size','The temple covers about 16 hectares (40 acres) at the heart of the town')])
 +talk("A dance textbook carved on a tower?","Exactly that. 108 poses, each labelled. Dancers still come to read it.")))
pages.append(page('dikshitar','THE DĪKṢITARS','Priests of Tillai',facts([
 ('Who','The Poṭu Dīkṣitars, a hereditary community of priests; tradition says 3,000 came with Śiva from Kailāsa, the “Tillai Mūvāyiravar”'),
 ('Marks','They wear the hair-knot at the front of the head; only married men serve in the rites'),
 ('Management','They manage the temple as a community, not under the usual state endowments system'),
 ('2014 ruling','On 6 January 2014 India’s Supreme Court recognised them as a religious denomination and set aside the Tamil Nadu government’s 2009 takeover of administration'),
 ('Since','Disputes over rites and access have continued in the courts and in public debate; this guide reports them, it does not judge them')])))
pages.append(page('saints','SAINTS OF TILLAI','Songs, a lost book and a fire',facts([
 ('Tēvāram','All three Tēvāram poets sang Tillai'),
 ('The lost hymns','Tradition says Rājarāja Chola and Nampi Āṇḍār Nampi found the forgotten Tēvāram palm leaves in a locked room of this temple, half eaten by ants, and arranged them as the Tirumuṟai'),
 ('Māṇikkavācakar','Sang the <i>Tiruvācakam</i> and is said to have merged into Naṭarāja here'),
 ('Nandanār','A saint from an outcaste community who longed to see Naṭarāja; the <i>Periya Purāṇam</i> says he passed through fire and entered the temple'),
 ('Cēkkiḻār','First recited his <i>Periya Purāṇam</i>, the lives of the 63 Nāyaṉmārs, in the thousand-pillared hall')])))
pages.append(page('cern','NAṬARĀJA IN THE WORLD','From Tillai to Geneva',facts([
 ('Chola bronzes','The classic Naṭarāja bronze took its form in the Chola workshops around the 10th century'),
 ('Museums','Chola Naṭarājas are treasured in museums around the world'),
 ('CERN','In 2004 India gave a 2 m Naṭarāja statue to CERN, the particle physics laboratory in Geneva, as a symbol of the cosmic dance of matter'),
 ('Dance','Bharatanāṭyam dancers bow to Naṭarāja before they begin'),
 ('Nāṭyāñjali','A dance festival held at the temple around Mahāśivarātri')])
 +talk("A Hindu god at a physics lab?","A gift from India. Physicists liked the image of the dance of creation and destruction.")))
pages.append(page('festivals','THROUGH THE YEAR','Its great days',facts([
 ('Ārudrā Darśanam','Mārkaḻi (Dec–Jan): Naṭarāja’s great abhiṣeka, the chariot festival and his dance out of the hall'),
 ('Āṉi Tirumañjaṉam','Āṉi (Jun–Jul): the other great festival, with chariots'),
 ('Six abhiṣekams','Naṭarāja is bathed only six times a year, on fixed days'),
 ('Daily','The crystal liṅga is bathed several times a day; the Rahasyam is shown at the pūjās'),
 ('Nāṭyāñjali','Around Mahāśivarātri (Feb–Mar)')])))
pages.append(page('meaning','WHAT SPACE TEACHES','The wisdom of emptiness',facts([
 ('Room for all','Space holds every element; nothing exists without it'),
 ('Beyond form','The highest form of God has no form'),
 ('Joy','The universe is a dance, not a machine'),
 ('Draw the curtain','Remove ignorance and the infinite is already there')])
 +talk("What should I take from space?","Make room. And remember that the whole universe is dancing.")))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Cit · Ambara','Consciousness · sky, space'),('Ākāśa','Space'),('Tāṇḍava','Śiva’s dance'),('Apasmāra','Dwarf of forgetfulness'),('Sabhā · Ambalam','Hall'),('Rahasyam','Secret'),('Karaṇa','Dance pose'),('Dīkṣitar','The temple’s priests')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Element.</b> Space: the Ākāśa liṅga, the empty Secret of Cidambaram.</div>
<div><b>Dance.</b> Naṭarāja’s dance of bliss for Patañjali and Vyāghrapāda.</div>
<div><b>Temple.</b> The golden roof, five halls, 108 poses in stone, Govindarāja inside.</div>
<div><b>People.</b> The Dīkṣitars; Nandanār; the rediscovered Tēvāram; Cēkkiḻār.</div>
<div><b>Lesson.</b> Draw aside the curtain: the infinite is already here.</div>
</div>'''+talk("One line to end the five?","Earth, water, fire, air: all of them dance in space. That's Cidambaram.")+'<div class="key">The Pañcabhūta Sthalas are complete: <a href="'+PSS+'">back to the series</a> 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Temple:</b> Wikipedia, “Thillai Nataraja Temple”; Wikimedia note on the Chola gilding by Āditya I and Parāntaka I; behindeverytemple.org and esamskriti.com (three forms; Rahasyam; roof symbolism); Hinduism Today and The Daily Pioneer (Supreme Court, 6 Jan 2014; denomination status; 2009 takeover); CERN (Naṭarāja statue, 2004).</p>
<p><b>Literature:</b> Patañjali, Caraṇaśṛṅgarahita Naṭarāja Stotram; Māṇikkavācakar, <i>Tiruvācakam</i>; Cēkkiḻār, <i>Periya Purāṇam</i> (Nandanār); Tirumuṟai tradition (Nampi Āṇḍār Nampi); Bharata, <i>Nāṭyaśāstra</i> (108 karaṇas).</p>
<p><b>Sources differ / unverified:</b> tile and nail counts; tower dates and builders; the Govindarāja history (inscriptions and tradition differ); Patañjali’s identity with the Yoga Sūtra author; the number of Dīkṣitar families today. Court cases on the temple continue; we describe them neutrally. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Names'),('dance','The Dance of Bliss'),('icon','The Naṭarāja Image'),('three','Three Forms of Śiva'),('rahasyam','The Secret of Cidambaram'),('roof','The Golden Roof'),('sabhas','The Five Halls'),('kali','The Dance Contest'),
 ('vishnu','Govindarāja Perumāḷ'),('gopurams','Four Towers, 108 Poses'),('dikshitar','The Dīkṣitars'),('saints','Saints of Tillai'),('cern','Naṭarāja in the World'),('festivals','Through the Year'),('meaning','What Space Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
build('/home/claude/work/shakti/PS5_Chidambaram.html',head,cov,fw,pages,toc)
