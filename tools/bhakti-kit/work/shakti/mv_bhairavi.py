exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Bhairavī · Daśa Mahāvidyā 5 · srini.presents',
 'Bhairavī or Tripurabhairavī, the fifth of the Daśa Mahāvidyā: the awe-inspiring Goddess of fire and tapas, her fierce and gentle forms, Bhairava and the sixty-four yoginīs, the three cities, the Bhairavī Brāhmaṇī who taught Śrī Rāmakṛṣṇa, the rāga Bhairavī, and her temples at Kāśī and in Odisha. An illustrated reference guide.')
def FIRE(x,y,s=1): return f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 0 q-10 -40 14 -70 q0 26 16 30 q4 -30 20 -50 q16 40 10 90z" fill="#ff7a1a"/><path d="M-14 0 q-4 -24 10 -38 q4 18 14 18 q6 -10 10 -16 q6 20 0 36z" fill="#ffd60a"/></g>'
def BHAI(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-60 54 q60 -30 120 0" fill="#e0115f"/><path d="M-30 50 q-4 -54 30 -66 q34 12 30 66z" fill="#a01a1a"/>'
 '<path d="M-20 -6 q20 26 40 0" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="3 4"/>'
 '<path d="M-22 -8 l-26 -20 M22 -8 l26 -20 M-22 6 l-26 10 M22 6 l26 10" stroke="#e05a3a" stroke-width="7"/>'
 '<circle cx="-52" cy="-30" r="8" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="2 2"/><rect x="44" y="-40" width="16" height="12" fill="#e8d8a8"/>'
 '<path d="M-14 -40 q-14 30 -10 56 M14 -40 q14 30 10 56" stroke="#111" stroke-width="5" fill="none"/>'
 '<circle cy="-36" r="15" fill="#e05a3a"/><path d="M-14 -48 h28 l-4 -16 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/><path d="M-5 -68 a8 8 0 1 0 11 3" fill="none" stroke="#fff8c0" stroke-width="2.5"/>'
 '<circle cx="-5" cy="-38" r="2.4" fill="#fff"/><circle cx="5" cy="-38" r="2.4" fill="#fff"/><path d="M-3 -46 h6" stroke="#ffd60a" stroke-width="2"/><path d="M-6 -29 q6 5 12 0" fill="none"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The red goddess Bhairavi seated on a red lotus with a rosary and a book, flames rising behind her">'
 '<rect width="380" height="268" fill="#2a0a0a" rx="8"/>'+FIRE(110,250,1.6)+FIRE(270,250,1.6)+FIRE(190,240,2.2)+BHAI(190,170,1.25)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Bhairavī</b>: “the terrifying”, “the awe-inspiring”; also <b>Tripurabhairavī</b>'),
 ('Place','<b>Fifth</b> of the ten Mahāvidyās'),
 ('She is','The Goddess as <b>fire</b>: the heat that destroys, purifies and transforms'),
 ('Look','Red as a thousand rising suns; three eyes; crescent moon; garland of heads; rosary, book and blessing hands'),
 ('Consort','<b>Bhairava</b>, the fierce Śiva'),
 ('Court','Queen of the <b>sixty-four yoginīs</b>'),
 ('Title','A woman adept in Tantra is also called a <i>bhairavī</i>'),
 ('Temples','Tripurabhairavī at Kāśī; Bhairabī shrines across Odisha')])
 +talk("Terrifying, but she holds a book and a rosary?","Both. The fire that burns the house down also cooks the food. She is that fire.")))
pages.append(page('names','HER NAMES','Fear, awe and the three cities',facts([
 ('Bhairavī','Feminine of <i>bhairava</i>, “terrible, awe-inspiring”'),
 ('Tripurabhairavī','<i>tri-pura</i>, “three cities”: the Bhairavī of the three worlds'),
 ('Śubhaṅkarī','“She who does good”: the kind face behind the fierce one'),
 ('Kālarātri','“Night of time”: a name she shares with Kālī'),
 ('Ṣaṭkūṭā, Kauleśī, Rudrabhairavī','Some of her forms named in the Tantras'),
 ('Bhairavī (title)','A woman who has mastered Tantric practice')])
 +talk("Is Tripurabhairavī the same as Tripurasundarī?","Close relatives, not twins. Teachers say they are linked, but distinct.")))
pages.append(page('form','HER FORM','Two faces of one Goddess',fig(560,200,'The goddess Bhairavi in red, with a garland of heads, rosary and book, seated on a red lotus before flames',
 '<rect width="560" height="200" fill="#fde8e0"/>'+FIRE(200,196,1.2)+FIRE(360,196,1.2)+BHAI(280,130,1.2))+facts([
 ('Colour','Red, “like the light of a thousand rising suns”'),
 ('Face','Three eyes, crescent moon, smiling or fierce'),
 ('Gentle form','Rosary and book, with the gestures of boon-giving and “fear not”; seated on a red lotus'),
 ('Fierce form','Red garments, a garland of severed heads, blood on her breast, sometimes in the cremation ground'),
 ('Meaning','The same power that creates also destroys: both forms are true')])))
pages.append(page('fire','THE GODDESS OF FIRE','Tapas, the heat of practice',facts([
 ('Tapas','Literally “heat”: the inner fire of discipline, fasting and meditation'),
 ('She is that heat','The burning that clears away ignorance and old habits'),
 ('Destroyer','Kinsley notes her strong link with destruction: she is the end of every created thing'),
 ('Kuṇḍalinī','Teachers place her at the root of the body, the fire that rises upward'),
 ('Fifth wisdom','After Bhuvaneśvarī makes room for the world, Bhairavī burns away what does not belong')])
 +talk("Why would anyone pray to a destroyer?","Because some things should end: anger, fear, pride. You ask her to burn those.")))
pages.append(page('tripura','THE THREE CITIES','Why “Tripura”?',fig(560,170,'Three flaming citadels in the sky, and a red goddess facing them',
 '<rect width="560" height="170" fill="#1d0e2a"/>'+''.join(f'<g transform="translate({x} {y})" stroke="#111" stroke-width="2"><rect x="-34" y="-20" width="68" height="34" fill="#c9a26b"/><path d="M-34 -20 l10 -16 l10 16 l10 -16 l10 16 l10 -16 l10 16" fill="#e8d8b8"/></g>'+FIRE(x,y-24,.5) for x,y in ((330,60),(420,100),(500,60)))+BHAI(130,100,.8))+facts([
 ('The legend','Tripura was three flying cities of demons; Śiva burnt them with a single arrow'),
 ('In Kāśī','Local tradition says Bhairavī took her fierce form to destroy the three cities'),
 ('Inner meaning','Teachers read the three cities as waking, dream and deep sleep, or body, mind and causal self'),
 ('Beyond','Burn all three and what is left is pure awareness')])
 +talk("A goddess who burns cities?","The cities are inside us. She burns the walls we build around the self.")))
pages.append(page('yoginis','BHAIRAVA AND THE YOGINĪS','Her court',facts([
 ('Bhairava','Śiva in his fierce form, guardian of Kāśī and of every temple: Bhairavī is his power'),
 ('Sixty-four yoginīs','Female deities of Tantra; Bhairavī is called their leader'),
 ('Yoginī temples','Circular, open-air shrines such as Hirāpur (Odisha) and Mitāolī (Madhya Pradesh) honour the yoginīs'),
 ('Charnel ground','A 17th-century Mughal-period painting in the Metropolitan Museum shows Bhairavī and Śiva as skull-bearing ascetics'),
 ('Other consort','Some texts pair her with Dakṣiṇāmūrti, Śiva as teacher')])
 +'<div class="key">See also: <a href="/bhakti/devi/devi-mahatmya/">The Devī Māhātmya series</a></div>'))
pages.append(page('brahmani','THE BHAIRAVĪ BRĀHMAṆĪ','A living bhairavī',fig(560,170,'A woman ascetic in ochre with loose hair stepping off a boat at a riverside temple ghat',
 '<rect width="560" height="170" fill="#bfe3f0"/><rect y="120" width="560" height="50" fill="#5a9ad0"/><path d="M60 120 h120 l-14 18 h-92z" fill="#8a5a2a" stroke="#111"/>'
 +'<g transform="translate(420 120)" stroke="#111" stroke-width="2"><rect x="-80" y="-60" width="160" height="60" fill="#f2e6c8"/><path d="M-30 -60 q0 -40 30 -50 q30 10 30 50z" fill="#c9a26b"/></g>'+person(120,96,'#e07a1a','#c98b5a',.9)+person(330,96,'#fff','#c98b5a',.8))+facts([
 ('Who','Yogeśvarī, known as the <b>Bhairavī Brāhmaṇī</b>, a woman ascetic from Jessore, Bengal'),
 ('1861','She arrived by boat at the Dakṣiṇeśvar Kālī temple and met Śrī Rāmakṛṣṇa'),
 ('Teacher','She became his first formal guru and led him through the sixty-four Tantric practices'),
 ('Witness','She argued before pandits that his states were spiritual, not madness'),
 ('After','Her later life and death are not recorded')])
 +talk("So a bhairavī is also a person?","A title earned by mastery. This one taught the saint of Dakṣiṇeśvar.")))
pages.append(page('raga','THE RĀGA BHAIRAVĪ','The Goddess in music',facts([
 ('Hindustani','<b>Bhairavī</b> is the morning rāga, and by custom the last piece of a concert'),
 ('Mood','Devotion, tenderness, longing: the gentle face of the Goddess'),
 ('Carnatic','Bhairavi is also a major Carnatic rāga, with a different scale'),
 ('Family','The rāga Bhairav is named for Bhairava; Bhairavī is its feminine partner'),
 ('Name only','The rāgas carry her name; they are not hymns to her')])
 +talk("Concerts end with a fierce Goddess?","With her sweetest side. Even the terrible one sings softly at dawn.")))
pages.append(page('kashi','TRIPURABHAIRAVĪ AT KĀŚĪ','Her temple in Varanasi',fig(560,170,'A small riverside temple above stone ghat steps on the Ganga',
 '<rect width="560" height="170" fill="#ffe8c8"/><rect y="130" width="560" height="40" fill="#7ab0d8"/>'+''.join(f'<rect x="{80+k*10}" y="{130-k*10}" width="{400-k*20}" height="10" fill="#d8c8a8" stroke="#111"/>' for k in range(5))
 +'<g transform="translate(280 80)" stroke="#111" stroke-width="2"><rect x="-40" y="-30" width="80" height="30" fill="#e05a3a"/><path d="M-26 -30 l26 -40 l26 40z" fill="#c0392b"/><path d="M0 -70 v-10 l12 4 l-12 4" fill="#ffd60a"/></g>')+facts([
 ('Where','Near Mīr Ghāṭ, in the lanes by the Viśvanātha temple; the steps below are <b>Tripurabhairavī Ghāṭ</b>'),
 ('Deity','A self-manifested (svayambhū) image; the Tripureśvara liṅga, her partner, is in the same shrine'),
 ('Kāśī Khaṇḍa','Skanda Purāṇa, Kāśī Khaṇḍa ch. 72: she is one of the powers the Goddess released in her battle with Durgāsura'),
 ('The ghāṭ','Once Vṛddhāditya Ghāṭ; renamed after an 18th-century temple to her')])
 +'<div class="key">More Kāśī: <a href="/bhakti/temples-of-india/18-shakti-peethas/vishalakshi-varanasi/">Viśālākṣī</a></div>'))
pages.append(page('odisha','BHAIRABĪ IN ODISHA','Shrines of the east',facts([
 ('Puruṇākaṭak','Boudh district: Bhairabī is the presiding deity of the town'),
 ('Boudh','A second Bhairabī temple in the district town'),
 ('Mantridi','Near Berhampur, Ganjam: Ek-pāda Bhairavī, a one-legged image in a temple said to date to the 8th century'),
 ('Malkangiri','A Bhairabī temple on the edge of the town, tied to the old royal house'),
 ('Kāmākhyā','Bhairavī has her own shrine on the Nīlācala hill with the other Mahāvidyās')])
 +talk("Why so many in Odisha?","Odisha kept its village goddesses and its Tantric temples. Bhairabī belongs to both.")))
pages.append(page('festivals','THROUGH THE YEAR','Her days',facts([
 ('Bhairavī Jayantī','The full moon of Mārgaśīrṣa (November–December)'),
 ('Navarātri','Both seasons; she is honoured among the ten Mahāvidyās'),
 ('Kālabhairava Aṣṭamī','The day of her consort, Kālabhairava, in the same month'),
 ('Gupta Navarātri','The “hidden” Navarātris of Māgha and Āṣāḍha, kept by Tantric worshippers')])))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of fire',facts([
 ('Burn what binds','Discipline is heat; it hurts, and it frees'),
 ('Fear and awe','What terrifies the ego is liberating to the self'),
 ('Speech and knowledge','Her book and rosary: learning and practice go together'),
 ('Women as teachers','The title bhairavī honours women who master the path')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Bhairava','Fierce Śiva'),('Tapas','Heat; ascetic discipline'),('Tripura','Three cities'),('Yoginī','Female Tantric deity or adept'),('Svayambhū','Self-manifested'),('Ghāṭ','River steps'),('Rāga','Melodic mode'),('Mārgaśīrṣa','November–December month')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Bhairavī, Tripurabhairavī, fifth Mahāvidyā: the Goddess as fire and tapas.</div>
<div><b>Form.</b> Red as sunrise; fierce with heads and blood, or gentle with book and rosary.</div>
<div><b>Court.</b> Bride of Bhairava, queen of the sixty-four yoginīs.</div>
<div><b>In the world.</b> The Bhairavī Brāhmaṇī; the rāga Bhairavī; Kāśī and Odisha.</div>
<div><b>Lesson.</b> Let the fire burn what binds you.</div>
</div>'''+talk("One line to remember?","Bhuvaneśvarī gives you room; Bhairavī clears it.")+'<div class="key">The fifth Great Wisdom: <b>Bhairavī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Goddess:</b> Wikipedia, “Bhairavi” (meaning; fifth Mahāvidyā; Tripurabhairavī and the three states; dhyāna with red garments, garland of heads, three eyes, crescent; rosary, book, abhaya, varada; red lotus; consort Bhairava or Dakṣiṇāmūrti; 64 yoginīs; Tripurasundarī and Tripurabhairavī linked but distinct; bhairavī as title). D. Kinsley, <i>Tantric Visions of the Divine Feminine</i> (1997). Metropolitan Museum, painting by Payāg, c. 1630–35.</p>
<p><b>Bhairavī Brāhmaṇī:</b> Wikipedia (fl. 1861–1873; first formal guru; whereabouts after unknown); Swāmī Sāradānanda, <i>Śrī Rāmakṛṣṇa the Great Master</i>, Part 2, ch. 10–11.</p>
<p><b>Temples:</b> varanasitemples.in and sahasa.in (Tripurabhairavī, Mīr Ghāṭ, svayambhū, Tripureśvara; Kāśī Khaṇḍa ch. 72); ghāṭ history from Varanasi ghāṭ guides. Boudh district official site (Puruṇākaṭak); Malkangiri district official site; <i>Organiser</i> (Mantridi).</p>
<p><b>Sources differ / unverified:</b> the 8th-century date and “Ādi Śakti Pīṭha” claim for Mantridi; the Tripura-burning legend at Kāśī is local tradition; Gupta Navarātri customs vary. Avatāra pairings differ between Tantras. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('form','Her Form'),('fire','The Goddess of Fire'),('tripura','The Three Cities'),('yoginis','Bhairava and the Yoginīs'),('brahmani','The Bhairavī Brāhmaṇī'),
 ('raga','The Rāga Bhairavī'),('kashi','Tripurabhairavī at Kāśī'),('odisha','Bhairabī in Odisha'),('festivals','Through the Year'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 5 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,8vw,76px)">BHAIRAVĪ</h1>
  <div class="series">DAŚA MAHĀVIDYĀ · A REFERENCE GUIDE</div>
  <div class="tag">The fire that burns and purifies</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>Bhuvaneśvarī makes room for the world. The fifth Great Wisdom, <b>Bhairavī</b>, is the fire that clears it: red as a thousand suns, bride of the fierce Bhairava, queen of the sixty-four yoginīs. She holds a garland of heads in one telling and a book and rosary in another.</p>
    <p>Her name is also a title. In 1861 a woman ascetic called the Bhairavī Brāhmaṇī stepped off a boat at Dakṣiṇeśvar and became Śrī Rāmakṛṣṇa’s first guru. And every Hindustani concert traditionally ends with a rāga that bears her name.</p>
    <p>This guide tells her stories, her meaning and her temples.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Bhairavī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is she scary or kind?","Yes. Fire is both, and she is fire.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms. Previous: <a href="{MVS}bhuvaneshvari/">Bhuvaneśvarī</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV05_Bhairavi.html','w').write(head+b+tail())
print('ok',len(pages))
