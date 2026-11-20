exec(open('/home/claude/work/shakti/mv_common.py').read())
head=head_red('Kālī · Daśa Mahāvidyā 1 · srini.presents',
 'Kālī, the first of the Daśa Mahāvidyā: the dark Goddess of time, her birth from Durgā’s brow in the Devī Māhātmya, Cāmuṇḍā and Raktabīja, why she stands on Śiva, what her garland, sword and tongue mean, Dakṣiṇa Kālī and Bhadrakālī, Kālīghāṭ and Dakṣiṇeśvar, Rāmprasād and Rāmakṛṣṇa, and Kālī Pūjā. An illustrated reference guide.')
def KALI(x,y,s=1): return (f'<g transform="translate({x} {y}) scale({s})" stroke="#111" stroke-width="2">'
 '<path d="M-60 70 h120" stroke="#fff" stroke-width="8"/><ellipse cx="0" cy="66" rx="60" ry="8" fill="#e8eef2"/>'
 '<path d="M-26 64 q-6 -70 26 -84 q32 14 26 84z" fill="#1a1a2a"/>'+''.join(f'<path d="M{-24+i*8} 30 v14" stroke="#1a1a2a" stroke-width="5"/>' for i in range(7))
 +'<path d="M-24 -8 q24 40 48 0" fill="none" stroke="#fff" stroke-width="6" stroke-dasharray="4 5"/>'
 '<path d="M-22 -4 l-30 -26 M22 -4 l30 -26 M-22 10 l-34 4 M22 10 l34 4" stroke="#1a1a2a" stroke-width="7"/>'
 '<path d="M52 -30 l14 -40" stroke="#bbb" stroke-width="5"/><circle cx="-54" cy="-32" r="8" fill="#2a2a3a"/><path d="M-56 18 q-4 8 0 14" stroke="#c0392b" stroke-width="3" fill="none"/>'
 '<path d="M-18 -40 q-14 30 -10 70 M18 -40 q14 30 10 70" stroke="#111" stroke-width="7" fill="none"/>'
 '<circle cy="-38" r="16" fill="#1a1a2a"/><path d="M-14 -50 h28 l-4 -16 l-6 6 l-4 -10 l-4 10 l-6 -6z" fill="#e0a800"/>'
 '<circle cx="-6" cy="-40" r="3" fill="#fff"/><circle cx="6" cy="-40" r="3" fill="#fff"/><circle cy="-48" r="2.6" fill="#ff8c1a"/><path d="M-4 -30 q4 20 8 0z" fill="#e04040"/></g>')
cover=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="The dark goddess Kali with flowing hair, a garland of heads and a sword, standing on the reclining white form of Shiva">'
 '<rect width="380" height="268" fill="#1a0e1e" rx="8"/>'+''.join(f'<circle cx="{(i*53)%380}" cy="{(i*31)%120}" r="1.6" fill="#fff"/>' for i in range(30))+'<circle cx="190" cy="110" r="90" fill="#c0392b" opacity=".35"/>'+KALI(190,170,1.15)+'</svg>')
pages=[]
pages.append(page('glance','AT A GLANCE','The essential facts on one page',facts([
 ('Name','<b>Kālī</b>: “the dark one”, and “she who is Time” (kāla)'),
 ('Place','<b>First</b> of the ten Mahāvidyās; head of the Kālīkula'),
 ('Look','Black or dark blue; wild hair; tongue out; garland of heads; skirt of arms; sword and severed head; standing on Śiva'),
 ('First great story','The <b>Devī Māhātmya</b> (c. 6th c.): born from Durgā’s brow; kills Caṇḍa and Muṇḍa, drinks Raktabīja’s blood'),
 ('Names','Kālikā, Śyāmā, Dakṣiṇa Kālī, Bhadrakālī, Cāmuṇḍā, Bhavatāriṇī'),
 ('Temples','<b>Kālīghāṭ</b> (a Śakti Pīṭha) and <b>Dakṣiṇeśvar</b>, Kolkata; Bhadrakālī shrines in Kerala'),
 ('Festival','<b>Kālī Pūjā</b>, on the new moon of Kārtika, the night of Dīpāvalī in Bengal'),
 ('Poets and saints','Rāmprasād Sen; Śrī Rāmakṛṣṇa')])
 +talk("Why is the first Mahāvidyā the scariest?","She's first because she's the ground: Time eats everything, and the Mother of Time is the start of all ten.")))
pages.append(page('names','HER NAMES','Time, darkness, mercy',facts([
 ('Kālī','Feminine of <i>kāla</i>: “time”, “death”, and “black”'),
 ('Mahākālī','“Great Kālī”, Goddess of the first chapter of the Devī Māhātmya; consort of Mahākāla'),
 ('Cāmuṇḍā','Slayer of Caṇḍa and Muṇḍa'),
 ('Dakṣiṇa Kālī','The Bengal form: “the gracious” or “right-footed” Kālī'),
 ('Śyāmā','“The dark one”: the name in Bengali songs'),
 ('Bhadrakālī','“Auspicious Kālī”: the Kerala form'),
 ('Bhavatāriṇī','“She who carries across the ocean of existence”: Dakṣiṇeśvar’s Kālī')])
 +talk("A goddess called 'auspicious' and 'death' at once?","That's Kālī. What ends one thing makes room for the next.")))
pages.append(page('roots','EARLY ROOTS','Before the Purāṇas',facts([
 ('Agni’s tongue','The Muṇḍaka Upaniṣad names Kālī as the first of the seven flickering tongues of fire'),
 ('Village goddess','Many scholars think she began as a local goddess of the hills and forests, later joined to Pārvatī'),
 ('Battle goddess','By the 6th century she is the wrath of the Goddess in war'),
 ('Tantra','Later Tantras make her the supreme Goddess, beyond even Śiva')])))
pages.append(page('chanda','DEVĪ MĀHĀTMYA · CAṆḌA AND MUṆḌA','Born from a frown',fig(560,170,'A golden goddess on a lion frowning; from her brow a dark goddess leaps out with a sword toward two demons',
 '<rect width="560" height="170" fill="#2a1a1a"/>'+GENTLE(120,110,.9).replace('#e05a8a','#e0a800')+'<path d="M128 70 L220 90" stroke="#ff8c1a" stroke-width="4" stroke-dasharray="6 4"/>'+KALI(280,110,.6)+DEMON(430,140,.9)+DEMON(500,140,.9,'#5a2a2a'))+'''<div class="steps">
<div><b>The frown.</b> When the demons <b>Caṇḍa</b> and <b>Muṇḍa</b> came to seize the Goddess Ambikā, her face darkened with anger.</div>
<div><b>Kālī leaps out.</b> From her furrowed brow sprang <b>Kālī</b>: gaunt, dark, with a garland of skulls and a tiger skin, mouth gaping, tongue lolling.</div>
<div><b>Cāmuṇḍā.</b> She destroyed the armies, cut off both demon heads and brought them to Ambikā, who named her <b>Cāmuṇḍā</b>.</div>
</div>'''+'<div class="key">Read the text: <a href="/bhakti/devi/devi-mahatmya/">The Devī Māhātmya series</a></div>'))
pages.append(page('raktabija','DEVĪ MĀHĀTMYA · RAKTABĪJA','The demon who multiplied',fig(560,170,'A battlefield full of identical demons rising from drops of blood; the dark goddess with her tongue spread wide catching the blood',
 '<rect width="560" height="170" fill="#2a1a1a"/>'+''.join(DEMON(260+i*50,150-(i%2)*10,.55,'#5a2a2a') for i in range(6))+KALI(140,110,.75)+''.join(f'<circle cx="{210+i*14}" cy="{120+(i%3)*6}" r="3" fill="#c0392b"/>' for i in range(5)))+'''<div class="steps">
<div><b>The boon.</b> <b>Raktabīja</b>, “blood-seed”, had a boon: every drop of his blood that touched the ground became a new Raktabīja.</div>
<div><b>An army of copies.</b> The more the Goddesses wounded him, the more demons filled the field.</div>
<div><b>Kālī’s answer.</b> Kālī spread her tongue across the battlefield and drank every drop before it fell, swallowing the copies. Bloodless, Raktabīja fell.</div>
</div>'''+talk("Why does she drink blood?","To stop evil from multiplying. Some troubles grow every time you strike at them; Kālī swallows them whole.")))
pages.append(page('shiva','WHY SHE STANDS ON ŚIVA','The tongue between her teeth',fig(560,200,'The dark goddess with one foot on the chest of the reclining white Shiva, her tongue out',
 '<rect width="560" height="200" fill="#1a0e1e"/>'+'<g transform="translate(280 190)" stroke="#111" stroke-width="2"><rect x="-120" y="-16" width="240" height="16" fill="#8a7a6a"/><path d="M-110 -16 q110 -26 220 0" fill="#e8eef2"/><circle cx="-112" cy="-24" r="12" fill="#e8eef2"/></g>'+KALI(280,110,.95))+'''<div class="steps">
<div><b>The popular story.</b> After the battle, Kālī danced on, drunk with victory, and the earth began to shake. Śiva lay down in her path. When her foot touched him she stopped, and put out her tongue in shame.</div>
<div><b>The Tantric reading.</b> Śiva below is <b>śava</b>, still consciousness; Kālī above is <b>śakti</b>, the power that moves it. Without her, Śiva is a corpse.</div>
<div><b>Both are taught.</b> Bengal tells the first; Tantra the second. The image holds both.</div>
</div>'''))
pages.append(page('icon','READING THE IMAGE','What each sign means',facts([
 ('Black','All colours vanish into black: everything dissolves into her'),
 ('Garland of heads','Often fifty: the fifty letters of Sanskrit, the sound from which the world is made'),
 ('Skirt of arms','The deeds (karma) she cuts away from her devotee'),
 ('Sword','The knowledge that cuts the ego'),
 ('Severed head','The ego, already cut'),
 ('Fear-not and boon hands','In Dakṣiṇa Kālī her right hands bless and say “do not fear”'),
 ('Nakedness','Digambarī, “clothed in the sky”: nothing covers or limits her'),
 ('Cremation ground','Where all pretence ends; her home')])
 +talk("So the scary parts are actually blessings?","For the devotee, yes. She cuts off exactly what was holding you down.")))
pages.append(page('forms','HER FORMS','Many Kālīs',facts([
 ('Dakṣiṇa Kālī','Four-armed; right foot forward on Śiva; the gracious form of Bengal homes and temples'),
 ('Śmaśāna Kālī','The cremation-ground Kālī of Tantric practice, left foot forward'),
 ('Bhadrakālī','In Kerala the fierce, protective Goddess of the Kāvu groves, slayer of Dārika'),
 ('Mahākālī','In the Devī Māhātmya’s first chapter, Yoganidrā who wakes Viṣṇu; ten-faced, ten-armed in some images'),
 ('Ādyā Kālī','“Primordial Kālī”, source of all'),
 ('Rakṣā Kālī','Worshipped to ward off epidemic and disaster')])
 +'<div class="key">See also: <a href="/bhakti/temples-of-india/18-shakti-peethas/mahakali-ujjain/">Mahākālī of Ujjain</a> (Śakti Pīṭha 9)</div>'))
pages.append(page('kalighat','KĀLĪGHĀṬ','Kolkata’s oldest Kālī',fig(560,180,'A Bengal-style temple with a curved roof and small top, and inside a black goddess with three large eyes and a long golden tongue',
 '<rect width="560" height="180" fill="#fdf1e8"/><g transform="translate(160 170)" stroke="#111" stroke-width="2"><rect x="-70" y="-60" width="140" height="60" fill="#f2e6c8"/><path d="M-80 -60 q80 -40 160 0z" fill="#e8d8b8"/><path d="M-30 -84 q30 -20 60 0 v-6 h-60z" fill="#e8d8b8"/><rect x="-16" y="-40" width="32" height="40" fill="#7a3a2a"/></g>'
 +'<g transform="translate(400 100)" stroke="#111" stroke-width="2"><rect x="-50" y="-50" width="100" height="110" rx="20" fill="#1a1a1a"/>'+''.join(f'<ellipse cx="{dx}" cy="-20" rx="12" ry="9" fill="#fff"/><circle cx="{dx}" cy="-20" r="4" fill="#c0392b"/>' for dx in (-22,22))+'<ellipse cy="-40" rx="8" ry="6" fill="#fff"/><path d="M-8 4 q8 40 16 0z" fill="#e0a800"/></g>')+facts([
 ('Pīṭha','One of the 51 Śakti Pīṭhas: the toes of Satī’s right foot; among the four Ādi Pīṭhas in another list (as the face)'),
 ('Image','Black touchstone; three huge eyes; a long golden tongue; four hands of gold'),
 ('Temple','Present building completed in <b>1809</b> under the <b>Sābarṇa Rāy Caudhurī</b> family; older shrines on the site since at least the 15th century'),
 ('River','It stood on the Ādi Gaṅgā, an old channel of the Hooghly, now almost dry'),
 ('Art','Its bazaar gave birth to <b>Kalighat paintings</b>, bold 19th-century pictures'),
 ('City','One theory derives “Kolkata” from Kālīkṣetra, Kālī’s field')])))
pages.append(page('dakshineswar','DAKṢIṆEŚVAR','Bhavatāriṇī and Rāmakṛṣṇa',fig(560,180,'A white and red temple with nine spires on a riverbank, smaller shrines in a row beside it',
 '<rect width="560" height="180" fill="#cfe3f5"/><rect y="150" width="560" height="30" fill="#4aa3df"/><g transform="translate(200 150)" stroke="#111" stroke-width="2"><rect x="-80" y="-60" width="160" height="60" fill="#fff"/><rect x="-50" y="-100" width="100" height="40" fill="#fff"/><rect x="-20" y="-130" width="40" height="30" fill="#fff"/>'
 +''.join(f'<path d="M{dx} {dy} q10 -24 20 0z" fill="#c0392b"/>' for dx,dy in ((-80,-60),(-10,-60),(60,-60),(-80+0,-60),(-50,-100),(30,-100),(-10,-130),(-50,-100),(30,-100)))+'</g>'
 +''.join(f'<g transform="translate({330+i*36} 150)" stroke="#111"><rect x="-14" y="-30" width="28" height="30" fill="#f2e6c8"/><path d="M-16 -30 q16 -18 32 0z" fill="#e0a800"/></g>' for i in range(6)))+facts([
 ('Founder','<b>Rāṇī Rāsmaṇi</b>, a wealthy widow of Kolkata, after a dream of the Goddess on the eve of a pilgrimage to Kāśī'),
 ('Consecrated','<b>31 May 1855</b>, on the east bank of the Hooghly'),
 ('Goddess','<b>Bhavatāriṇī</b>, Kālī who carries devotees across saṃsāra'),
 ('Style','Bengal <b>navaratna</b>, “nine jewels”: three storeys and nine spires; twelve Śiva shrines along the river'),
 ('Rāmakṛṣṇa','<b>Śrī Rāmakṛṣṇa</b> served here as priest; his visions of the Mother made Dakṣiṇeśvar world-famous, with Śāradā Devī and Vivekānanda')])))
pages.append(page('ramprasad','RĀMPRASĀD AND ŚYĀMĀ SAṄGĪT','Songs to a dark mother',facts([
 ('Rāmprasād Sen','18th-century poet of Bengal, who sang to Kālī as a child sings to his mother, sometimes scolding her'),
 ('Śyāmā saṅgīt','“Songs to Śyāmā”: the Bengali devotional song tradition he shaped'),
 ('Kamalākānta','Another great Śākta poet in the same tradition'),
 ('The tone','Intimate, playful, defiant: the devotee demands the Mother’s attention'),
 ('Rāmakṛṣṇa','Loved and sang Rāmprasād’s songs')])
 +talk("People scold Kālī in their songs?","Like a child tugging at his mother's sari. The fiercer the Goddess, the closer her children get.")))
pages.append(page('puja','KĀLĪ PŪJĀ','The darkest night',facts([
 ('When','The new moon (<b>amāvāsyā</b>) of Kārtika: the night of Dīpāvalī in Bengal, Assam and Odisha'),
 ('Worship','Through the night: clay images in homes and paṇḍāls, hibiscus, lamps, sweets'),
 ('Lamps','Rows of lamps in the darkest night of the year'),
 ('Other days','Phalahāriṇī Kālī Pūjā in Jyeṣṭha; Raṭanti Kālī Pūjā in Māgha'),
 ('Hibiscus','Red jabā flowers are her favourite offering')])
 +talk("Lakṣmī on Dīpāvalī elsewhere, Kālī in Bengal?","Same night, two Goddesses: plenty and freedom. Bengal chose freedom.")))
pages.append(page('meaning','WHAT SHE TEACHES','The wisdom of Kālī',facts([
 ('Time','Everything that is born is eaten by time; she is that time, and beyond it'),
 ('Fearlessness','Face death and loss, and fear loses its grip'),
 ('Love','Behind the terror, a mother: devotees call her “Mā” first'),
 ('Freedom','Bhavatāriṇī: she frees from the cycle of birth and death'),
 ('First wisdom','The first Mahāvidyā: dissolve, and only then begin')])))
pages.append(page('glossary','GLOSSARY','Words used in this guide',facts([
 ('Kāla','Time, death; also black'),('Śava','Corpse'),('Digambarī','Clothed in the sky'),('Śmaśāna','Cremation ground'),('Muṇḍa-mālā','Garland of heads'),
 ('Amāvāsyā','New moon'),('Jabā','Hibiscus'),('Navaratna','Nine-spired temple style'),('Śyāmā','The dark one')])))
pages.append(page('end','ON ONE PAGE','The whole guide in five lines','''<div class="steps">
<div><b>Who.</b> Kālī: the dark Mother of Time, first of the ten Mahāvidyās.</div>
<div><b>Stories.</b> Born from Durgā’s frown; Caṇḍa, Muṇḍa and Raktabīja; her foot on Śiva.</div>
<div><b>The image.</b> Heads for letters, arms for karma, sword for wisdom, black for all that dissolves.</div>
<div><b>Where.</b> Kālīghāṭ (1809, a Śakti Pīṭha) and Dakṣiṇeśvar (1855, Rāmakṛṣṇa).</div>
<div><b>When.</b> Kālī Pūjā on the new moon of Dīpāvalī.</div>
</div>'''+talk("One line to remember?","She is the end of everything, which is why she is the safest place to begin.")+'<div class="key">The first Great Wisdom: <b>Kālī</b>. 🙏</div>'+FOLLOW))
pages.append(page('sources','SOURCES &amp; NOTES','Where the facts come from','''<div class="panel reading small">
<p><b>Goddess:</b> Wikipedia, “Kali” (Devī Māhātmya, 6th c., first major appearance; kāla, time, black; Cāmuṇḍā; Raktabīja; Liṅga Purāṇa and Dāruka; Agni’s black tongue; Devī Bhāgavata). encyclopedia.com (village-goddess origins; ugra and saumya; Kālīghāṭ image dressed). Kinsley, <i>Hindu Goddesses</i> and <i>Tantric Visions</i> (Kālī as Durgā’s wrath; Śiva-śava reading).</p>
<p><b>Temples:</b> Wikipedia, “Kalighat Kali Temple” (1809 under the Sābarṇa Rāy Caudhurī family, begun 1798 by Santoṣ Rāy Caudhurī, completed by Rājīvlocan; image of 1570; Ādi Gaṅgā; Halder priests). theculturetrip.com (black stone, three eyes, gold tongue; navaratna). Britannica, “Dakshineswar Kali Temple” (Rāsmaṇi’s dream; consecration 31 May 1855). myoksha.com (Bhavatāriṇī meaning). llmpedia (Rāmprasād; Kālī Pūjā with Dīpāvalī).</p>
<p><b>Sources differ:</b> the meaning of “Dakṣiṇa”; the Kālīghāṭ body part (toes or face); the origin of “Kolkata”. <b>Not verified:</b> fifty heads as fifty letters (a common teaching, not universal). Zappy and Prof. Bolt are fictional.</p>
</div>'''))
toc=[('glance','At a Glance'),('names','Her Names'),('roots','Early Roots'),('chanda','Caṇḍa and Muṇḍa'),('raktabija','Raktabīja'),('shiva','Why She Stands on Śiva'),('icon','Reading the Image'),('forms','Her Forms'),
 ('kalighat','Kālīghāṭ'),('dakshineswar','Dakṣiṇeśvar'),('ramprasad','Rāmprasād and Śyāmā Saṅgīt'),('puja','Kālī Pūjā'),('meaning','What She Teaches'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
b=f'''<div class="book">

<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">MAHĀVIDYĀ 1 OF 10</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(28px,9vw,90px)">KĀLĪ</h1>
  <div class="series">DAŚA MAHĀVIDYĀ · A REFERENCE GUIDE</div>
  <div class="tag">The dark Mother of Time</div>
  {cover}
  {CAST}
</section>

<section class="page" id="foreword">
  <h2 class="page-title">FOREWORD</h2>
  <div class="panel bg-red halftone" style="font-size:17px;line-height:1.6">
    <p>She is black as the night sky, her hair loose, her tongue out, a garland of heads round her neck, a sword in her hand, and her foot on Śiva. And millions of people call her, simply, <b>Mā</b>.</p>
    <p><b>Kālī</b> is the first of the ten Great Wisdoms: the Goddess of Time, who ends all things and frees her devotees from fear. She leapt from Durgā’s frown to destroy demons no one else could stop; in Bengal she is worshipped on the darkest night of the year.</p>
    <p>This guide tells her stories, reads her image piece by piece, and visits her two great temples in Kolkata.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#c0392b">Jai Mā Kālī,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>
  {talk("How can something so frightening be loved?","Ask any child who's been scolded and then hugged. Her fierceness is for what harms you, never for you.")}
  <div class="panel reading small"><p>Part of <a href="{MVS}">Daśa Mahāvidyā</a>, the ten Great Wisdoms.</p></div>
</section>

<section class="page" id="contents">
  <h2 class="page-title">CONTENTS</h2>
  <ul class="toc">
    {''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc))}
  </ul>
</section>
'''+''.join(pages)+'</div>\n'
open('/home/claude/work/shakti/MV01_Kali.html','w').write(head+b+tail())
print('ok',len(pages))
