exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Tārā · Daśa Mahāvidyā 2 · srini.presents',
 'Tārā, the second of the Daśa Mahāvidyā: the blue Goddess who carries across, her forms Ugratārā, Ekajaṭā and Nīlasarasvatī, Akṣobhya and the poison, Tārā nursing Śiva, Vasiṣṭha, the Buddha and Cīnācāra, Tārāpīṭh on the Dvārakā river, the cremation ground, Bāmākhepā, and Hindu and Buddhist Tārā. An illustrated reference guide.')
def TARA(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-24 64 q-4 -60 24 -74 q28 14 24 74z" fill="#3b4fa0"/><path d="M-24 30 h48 v24 h-48z" fill="#e0a800"/>'+''.join(f'<path d="M{-22+i*9} 34 l4 16" stroke="#111" stroke-width="2"/>' for i in range(5))
 +'<path d="M-22 -4 q22 30 44 0" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="4 5"/>'
 '<path d="M-22 -2 l-28 -24 M22 -2 l28 -24 M-22 12 l-30 6 M22 12 l30 6" stroke="#3b4fa0" stroke-width="7"/>'
 '<path d="M48 -28 l8 -12 l6 4 l-8 12z" fill="#bbb"/><ellipse cx="-52" cy="-28" rx="9" ry="6" fill="#ddd"/><path d="M-56 22 h-8 l4 -10z" fill="#e0a800"/><path d="M52 22 q8 -14 4 -24" stroke="#2a9d6f" stroke-width="3" fill="none"/>'
 '<path d="M0 -50 q-6 -20 0 -34 q6 14 0 34z" fill="#111"/><circle cy="-36" r="15" fill="#3b4fa0"/><path d="M-12 -46 h24 l-4 -12 l-6 6 l-2 -8 l-2 8 l-6 -6z" fill="#e0a800"/>'
 '<circle cx="-5" cy="-38" r="2.6" fill="#fff"/><circle cx="5" cy="-38" r="2.6" fill="#fff"/><circle cy="-45" r="2" fill="#ff8c1a"/><path d="M-3 -28 q3 14 6 0z" fill="#e04040"/></g>')
def NURSE(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2"><path d="M-30 60 q-4 -60 30 -74 q34 14 30 74z" fill="#3b4fa0"/><circle cy="-34" r="15" fill="#3b4fa0"/>'
 '<path d="M-12 -44 h24 l-4 -12 l-6 6 l-2 -8 l-2 8 l-6 -6z" fill="#e0a800"/><circle cx="-5" cy="-36" r="2.4" fill="#fff"/><circle cx="5" cy="-36" r="2.4" fill="#fff"/>'
 '<path d="M-26 10 q26 24 52 0" stroke="#3b4fa0" stroke-width="8" fill="none"/><g transform="translate(6 14) rotate(-20)"><ellipse rx="22" ry="9" fill="#9ac0e8"/><circle cx="-22" r="8" fill="#9ac0e8"/><path d="M-26 -8 q4 -6 8 0" stroke="#5a3a1a" stroke-width="3" fill="none"/><path d="M-20 4 h4" stroke="#3b4fa0"/></g></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The blue goddess Tara standing on a cremation ground under a starry sky, a river and a funeral fire behind her">'
 '<rect width="380" height="268" fill="#0b1a3a" rx="8"/>'+''.join(f'<circle cx="{(i*53)%380}" cy="{(i*29)%120}" r="1.8" fill="#fff"/>' for i in range(34))+'<path d="M300 50 l4 10 l10 2 l-8 6 l2 10 l-8 -6 l-8 6 l2 -10 l-8 -6 l10 -2z" fill="#ffd166"/>'
 +'<path d="M0 240 Q190 224 380 242 V268 H0z" fill="#3a5a8a"/>'+FLAME(70,230,.7)+TARA(190,170,1.15)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Tārā</b>: “star”, and “she who carries across” (from <i>tṝ</i>, to cross)'),
 ('Place','<b>Second</b> of the ten Mahāvidyās, closest in look to Kālī'),
 ('Look','Blue; short and big-bellied; tiger skin; knife and skull-cup, sword and lotus; one matted braid; on a cremation ground'),
 ('Forms','<b>Ugratārā</b>, <b>Ekajaṭā</b>, <b>Nīlasarasvatī</b>'),
 ('Bhairava','<b>Akṣobhya</b>: Śiva who drank the poison unshaken'),
 ('Great seat','<b>Tārāpīṭh</b>, Birbhum, West Bengal, on the Dvārakā river'),
 ('Saint','<b>Bāmākhepā</b> (1837–1911), the “mad saint” of Tārāpīṭh'),
 ('Shared name','Tārā is also a great saviour goddess of Buddhism; the two traditions overlap')])
 +talk("A star and a ferry-woman?","Both guide you across the dark. Sailors steered by stars; Tārā steers souls across the ocean of life.")))
pages.append(page('names','HER NAMES','Star, saviour, blue speech',facts([
 ('Tārā','“Star”; and <i>tāriṇī</i>, “she who carries across”'),
 ('Ugratārā','“Fierce Tārā”: she saves from terrible (ugra) dangers'),
 ('Ekajaṭā','“One braid”: her hair in a single matted lock'),
 ('Nīlasarasvatī','“Blue Sarasvatī”: giver of speech and learning'),
 ('Tāriṇī','“Saviour”: the name in Bengali devotion'),
 ('Atharvaveda','One text calls her the form of the Atharva Veda')])
 +talk("Blue Sarasvatī? Isn't Sarasvatī white?","Tārā gives speech too, but the speech that comes out of the dark, out of a crisis. Hence blue.")))
pages.append(page('form','HER FORM','Like Kālī, but not Kālī',fig(560,200,'The blue goddess Tara, short and heavy-bellied, in a tiger skin, holding a knife and skull-cup, with a single tall braid',
 '<rect width="560" height="200" fill="#0b1a3a"/>'+TARA(280,130,1.2))+facts([
 ('Colour','Blue, like the night sky or deep water'),
 ('Build','Short, with a full belly: she holds the whole world'),
 ('Hands','Scissors or knife (kartṛ), skull-cup, sword, blue lotus'),
 ('Dress','Tiger skin, a garland of heads, snakes as ornaments'),
 ('Hair','One tall matted braid; a small image of Akṣobhya in it'),
 ('Ground','Standing on Śiva on a cremation ground, often with a funeral pyre')])
 +talk("How do I tell her from Kālī?","Blue not black, tiger skin not bare, scissors not sword, short not tall, and that single braid.")))
pages.append(page('poison','AKṢOBHYA AND THE POISON','The mother of Śiva',fig(560,180,'The blue goddess holding the pale-blue infant Shiva to her breast',
 '<rect width="560" height="180" fill="#fdf1e8"/>'+NURSE(280,110,1.2)+'<path d="M80 150 q20 -60 60 -40" stroke="#2a9d6f" stroke-width="6" fill="none"/>'+T(90,40,'HĀLĀHALA',12,'#2a9d6f'))+'''<div class="steps">
<div><b>The poison.</b> When the gods and demons churned the ocean, the deadly <b>hālāhala</b> poison rose first. Śiva drank it to save the worlds, and his throat turned blue.</div>
<div><b>Unshaken.</b> He swallowed it without being disturbed: so in Tārā’s worship he is <b>Akṣobhya</b>, “the unshaken”, her Bhairava.</div>
<div><b>The Mother’s milk.</b> Bengal tradition adds that the poison still burned in him, until Tārā took him on her lap like a baby and nursed him, and the burning stopped.</div>
<div><b>At Tārāpīṭh.</b> The ancient stone image there shows exactly this: Tārā suckling Śiva.</div>
</div>'''+talk("The Goddess is Śiva's mother here?","At Tārāpīṭh, yes. The fiercest Mahāvidyā turns out to be the gentlest mother.")))
pages.append(page('vasishtha','VASIṢṬHA AND THE BUDDHA','A sage learns from China',fig(560,170,'A sage in meditation failing; then the same sage bowing before a calm seated Buddha; then a blue goddess appearing in light',
 '<rect width="560" height="170" fill="#fdf1e8"/>'+person(100,150,'#ff8c1a','#d8b090',1)+'<path d="M160 100 h40" stroke="#111" stroke-width="3"/><path d="M200 100 l-10 -6 v12z" fill="#111"/>'
 +'<g transform="translate(280 150)" stroke="#111" stroke-width="2"><path d="M-30 0 q30 -20 60 0z" fill="#e0a800"/><path d="M-20 -6 q-4 -40 20 -48 q24 8 20 48z" fill="#e0a800"/><circle cy="-62" r="12" fill="#f2c79b"/><circle cy="-76" r="5" fill="#3a2a1a"/></g>'
 +'<path d="M340 100 h40" stroke="#111" stroke-width="3"/><path d="M380 100 l-10 -6 v12z" fill="#111"/><circle cx="460" cy="90" r="50" fill="#ffd166" opacity=".4"/>'+NURSE(460,100,.6))+'''<div class="steps">
<div><b>No success.</b> The Rudrayāmala tells that the sage <b>Vasiṣṭha</b> worshipped Tārā for ages without result, and grew angry.</div>
<div><b>Go to Mahācīna.</b> A voice told him to learn the right way from the <b>Buddha</b> (taken in some Hindu schools as an avatāra of Viṣṇu) in “Mahācīna”, a land north of the Himalaya.</div>
<div><b>Cīnācāra.</b> The Buddha taught him <b>cīnācāra</b>, the “Chinese way” of left-hand (vāmācāra) worship, and pointed him to Tārāpīṭh.</div>
<div><b>The vision.</b> There Vasiṣṭha worshipped on the cremation ground; Tārā appeared to him nursing Śiva, then became the stone image still worshipped.</div>
</div>'''+talk("A Hindu sage taught by the Buddha?","That's the legend, and it shows how close the Hindu and Buddhist Tārās once were.")))
pages.append(page('buddhist','HINDU AND BUDDHIST TĀRĀ','Two rivers, one source?',facts([
 ('Buddhist Tārā','A compassionate saviour, the “mother of all Buddhas”, beloved in Tibet and Nepal: Green Tārā, White Tārā and twenty-one forms'),
 ('Hindu Tārā','The second Mahāvidyā: fiercer, closer to Kālī, a Tantric Goddess of Bengal and Assam'),
 ('Overlap','Shared name, shared idea of rescue; Ekajaṭā and Ugratārā appear in both systems'),
 ('Borrowing','Scholars think the two grew together in the Buddhist-Śaiva world of eastern India, Oḍḍiyāna and the Himalaya'),
 ('Mahācīna','The Tantras locate her worship partly in a northern land beyond the mountains')])
 +talk("Same Goddess or different?","Two traditions shaped her side by side. Each sees her its own way; both call her the one who saves.")))
pages.append(page('where','TĀRĀPĪṬH','A village on the Dvārakā',facts([
 ('Where','Tārāpīṭh village, near Rampurhat, Birbhum district, West Bengal, on the north-flowing <b>Dvārakā</b> river'),
 ('Name','Bengali <i>tārā</i> also means the pupil of the eye: tradition says Satī’s <b>third eye</b> fell here, and the village, once Candīpur, was renamed'),
 ('Pīṭha status','Temple tradition counts it among the 51; many standard lists of the 51 do not, and call it a <b>Siddha Pīṭha</b>'),
 ('Holy trio','With Kālīghāṭ and Navadvīp, one of the great tīrthas of Bengali Hindus'),
 ('Administration','Today managed under the Tarapith Rampurhat Development Authority')])
 +'<div class="key">See also: <a href="/bhakti/temples-of-india/18-shakti-peethas/51-shakti-peethas/">The 51 Śakti Pīṭhas</a></div>'))
pages.append(page('temple','THE TEMPLE','Two images in one sanctum',fig(560,200,'A red Bengal temple with a curved roof; inside, a large metal mask-image of the goddess with a silver crown and flowing hair, and behind it a smaller stone image of the goddess nursing Shiva',
 '<rect width="560" height="200" fill="#fdf1e8"/><g transform="translate(150 190)" stroke="#111" stroke-width="2"><rect x="-80" y="-80" width="160" height="80" fill="#c0392b"/><path d="M-90 -80 q90 -50 180 0z" fill="#a01a1a"/><path d="M-30 -110 q30 -24 60 0 v-6 h-60z" fill="#a01a1a"/><rect x="-16" y="-50" width="32" height="50" fill="#5a1a1a"/></g>'
 +'<g transform="translate(400 110)" stroke="#111" stroke-width="2"><circle r="60" fill="#c0c0c0"/><path d="M-50 -40 q50 -50 100 0" fill="#ddd"/><circle cx="-18" cy="-6" r="9" fill="#fff"/><circle cx="18" cy="-6" r="9" fill="#fff"/><circle cx="-18" cy="-6" r="4" fill="#111"/><circle cx="18" cy="-6" r="4" fill="#111"/><path d="M-10 24 q10 10 20 0" fill="#c0392b"/><path d="M-60 0 q-20 40 0 70 M60 0 q20 40 0 70" stroke="#111" stroke-width="6" fill="none"/></g>')+facts([
 ('Outer image','A large metal image: the fierce face, silver crown, flowing hair, smeared with red sindūr; this is what most devotees see'),
 ('Inner image','Behind it, the ancient stone image of Tārā nursing Śiva, said to be the one Vasiṣṭha saw'),
 ('Building','Bengal style with curved roofs; local accounts credit Jagannāth Rāy of Mallārpur; the often-quoted year “1225” is most likely in the Bengali era, not 1225 CE'),
 ('Gate','A carving of Durgā and her family over the main gate')])))
pages.append(page('smashana','THE CREMATION GROUND','Where Tārā lives',facts([
 ('Mahāśmaśāna','The great cremation ground by the Dvārakā, beside the temple, is part of the shrine'),
 ('Sādhanā','For centuries tāntrikas have meditated here among the pyres'),
 ('Why there','Where bodies burn, the illusion that we are only bodies burns too'),
 ('Pañcamuṇḍī','Seats of five skulls on which Tantric adepts are said to sit in practice'),
 ('Visitors','Pilgrims see the pyres and the ascetics; most worship at the temple only')])
 +talk("Is it frightening?","For a visitor, maybe. For the tāntrika, it's the most honest place on earth.")))
pages.append(page('bamakhepa','BĀMĀKHEPĀ','The mad saint of Tārāpīṭh',fig(560,160,'A wild-haired ascetic sitting by a fire on a riverbank with dogs around him, speaking to a blue goddess in the sky',
 '<rect width="560" height="160" fill="#2a1a1a"/>'+FLAME(200,150,.8)+person(280,150,'#ff8c1a','#c98b5a',1.1)+'<path d="M266 108 q-16 -20 -6 -40 M294 108 q16 -20 6 -40" stroke="#ddd" stroke-width="5" fill="none"/>'
 +''.join(f'<g transform="translate({x} 150)" stroke="#111"><ellipse rx="14" ry="6" fill="#8a6a4a"/><circle cx="-14" cy="-6" r="5" fill="#8a6a4a"/></g>' for x in (120,380))+'<circle cx="460" cy="50" r="30" fill="#3b4fa0" opacity=".6"/>')+facts([
 ('Born','<b>Bāmācaraṇ Caṭṭopādhyāy</b>, 22 February 1837, in a village near Tārāpīṭh'),
 ('Life','Lived on the cremation ground, worshipping Tārā as his mother; ate with dogs, cared nothing for rules'),
 ('Khepā','“Mad”: he would speak to the Goddess aloud, scold her, eat her offerings before she did, and the temple came to accept it'),
 ('Died','18 July 1911; his shrine and āśrama stand by the Dvārakā, near the temple'),
 ('Legacy','He brought the secret Tārā worship into open, loving devotion')])
 +talk("He ate the Goddess's food first?","The legend says she told the priests: 'he's my son; let him eat'. That's Tārāpīṭh.")))
pages.append(page('festivals','THROUGH THE YEAR','Dark nights',facts([
 ('Kauśikī Amāvasyā','The new moon of Bhādrapada: the great night of Tārāpīṭh, when Tārā is said to have appeared; tāntrikas gather'),
 ('Kālī Pūjā','Dīpāvalī night, worship through the night'),
 ('Phalahāriṇī Amāvasyā','In Jyeṣṭha'),
 ('Ambubācī','Observed here as at Kāmākhyā'),
 ('Tārā Mā’s birth','A special day in Caitra, by local tradition'),
 ('Daily','Ritual bath of the image at dawn; bhog offered; animal sacrifice is still part of some rites')])))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of Tārā',facts([
 ('Crossing over','In every crisis, a guiding star: call her and she carries you across'),
 ('Sound','As Nīlasarasvatī, she is the first word that breaks the silence'),
 ('Fierce mother','She is terrible to danger and tender to her child, even to Śiva'),
 ('Beyond sects','Hindu and Buddhist alike reach for her in trouble'),
 ('Second wisdom','After Kālī’s dissolution, Tārā’s rescue: the first light in the dark')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Tārā · Tāriṇī','Star · she who carries across'),('Ugra','Fierce'),('Ekajaṭā','One braid'),('Akṣobhya','Unshaken'),('Hālāhala','The world-poison'),
 ('Cīnācāra','“Chinese way” of Tantric worship'),('Mahāśmaśāna','Great cremation ground'),('Khepā','Mad (Bengali)'),('Siddha Pīṭha','A seat made holy by saints’ practice')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Tārā, the blue saviour, second of the ten: Ugratārā, Ekajaṭā, Nīlasarasvatī.</div>
<div><b>Akṣobhya.</b> Śiva unshaken by the poison, nursed at her breast.</div>
<div><b>Vasiṣṭha.</b> Taught Cīnācāra by the Buddha; saw her at Tārāpīṭh.</div>
<div><b>Tārāpīṭh.</b> The third eye, two images, the cremation ground on the Dvārakā.</div>
<div><b>Bāmākhepā.</b> The mad saint who made her everyone’s mother.</div>
</div>'''+talk("One line to remember?","When it's darkest, look for the blue star. She's already rowing toward you.")+'<div class="key">The second Great Wisdom: <b>Tārā</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Goddess:</b> Wikipedia, “Tara (Mahavidya)” (second Mahāvidyā; Tārāpīṭh; Ekajaṭā, Ugratārā, Nīlasarasvatī; form of the Atharva Veda; Akṣobhya in the Toḍala Tantra, who drank the poison without agitation; Svatantra Tantra on Ugratārā; Oḍḍiyāna and Buddhist links; Rudrayāmala and Vasiṣṭha; Bṛhat-tantrasāra; Bāmākhepā). worldhistory.org (Buddhist Tārā as saviour).</p>
<p><b>Tārāpīṭh:</b> Wikipedia, “Tarapith” and “Tarapith temple” (third eye; Vasiṣṭha and the Buddha; image of Tārā suckling Śiva; Bāmākhepā 1837–1911; administration). shubhpanchang.com (Dvārakā river; Rampurhat; tārā = eyeball). templepurohit.com (Candīpur renamed; Jagannāth Rāy of Mallārpur; “1225”; Durgā over the gate). storeboard.com and bharatpedia (metal and stone images). Wikipedia, “Bamakhepa” (22 February 1837 – 18 July 1911).</p>
<p><b>Sources differ:</b> whether Tārāpīṭh is one of the 51; the temple’s date (we read “1225” as the Bengali era, an inference); Bāmākhepā stories. <b>Not verified, tradition only:</b> the nursing legend’s source; Pañcamuṇḍī seats; festival list. Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('form','Her Form'),('poison','Akṣobhya and the Poison'),('vasishtha','Vasiṣṭha and the Buddha'),('buddhist','Hindu and Buddhist Tārā'),('where','Tārāpīṭh'),('temple','The Temple'),
 ('smashana','The Cremation Ground'),('bamakhepa','Bāmākhepā'),('festivals','Through the Year'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 2 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(28px,9vw,90px)">TĀRĀ</h1>
  <div class="series">DAŚA MAHĀVIDYĀ · A REFERENCE GUIDE</div>
  <div class="tag">The blue star who carries you across</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>She looks like Kālī’s younger sister: blue instead of black, short and full-bellied, in a tiger skin, a knife in one hand and a skull-cup in the other, standing on a cremation ground. Her name means “star”, and “she who carries across”.</p>
    <p>This is <b>Tārā</b>, the second Great Wisdom. When Śiva drank the world’s poison, she nursed him like a baby. A sage learned her worship from the Buddha. And in a Bengal village by a cremation ground, a “mad saint” called her mother and ate from her plate.</p>
    <p>This guide tells her stories and visits her great seat, Tārāpīṭh.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Tārā Mā,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("Is she the same as the Buddhist Tārā?","Related, not identical. This guide is about the Hindu Mahāvidyā, with a page on how the two meet.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms. Previous: <a href="{MVS}kali/">Kālī</a>.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV02_Tara.html','w').write(head+b+tail())
print('ok',len(pages))
