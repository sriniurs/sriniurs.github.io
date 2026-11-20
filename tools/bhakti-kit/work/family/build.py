import re,sys
sys.path.insert(0,'/home/claude/work/mahimna')
from data import talk,svg,LINGA
src=open('/home/claude/work/stotram.html').read()
head=src[:src.find('<div class="book">')]
head=re.sub(r'<title>.*?</title>','<title>Śiva\'s Family and Symbols · srini.presents</title>',head)
head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Why Śiva wears the moon, the Gaṅgā, a snake and ash; what the third eye, trident, ḍamaru, rudrākṣa, liṅga and Nandi mean; and Pārvatī, Gaṇeśa, Kārttikeya and the wider family, explained and illustrated.">',head)
F='font-family="Bangers"'
def page(id,title,sub,body): return f'<section class="page" id="{id}">\n  <h2 class="page-title">{title}</h2>\n  <div class="sub">{sub}</div>\n  {body}\n</section>\n'
def sym(id,title,sub,fig,what,reading,c,tk,key,note=''):
    cards=f'<div class="g2"><div class="card bg-yellow"><h4>{c[0]}</h4><p>{c[1]}</p></div><div class="card bg-blue"><h4>{c[2]}</h4><p>{c[3]}</p></div></div>'
    return page(id,title,sub,f'<div class="vfig">{fig}<div class="mean">{what}</div></div>\n  <div class="panel reading">{reading}</div>\n  {cards}\n  {talk(*tk)}\n  <div class="key">{key}</div>'+(f'\n  <div class="note">{note}</div>' if note else ''))
HEAD=lambda extra='',throat='#bcd4f0': f'<g stroke="#111" stroke-width="2.5"><circle cx="110" cy="70" r="30" fill="#bcd4f0"/><rect x="100" y="98" width="20" height="16" fill="{throat}"/><path d="M80 60 q30 -50 60 0" fill="#3a2a1a"/></g>{extra}'
P=[]
cover_svg=('<svg width="380" height="268" viewBox="0 0 380 268" role="img" aria-label="Shiva seated on Kailasa with crescent moon, Ganga, snake and trident, with Parvati beside him, Ganesha and Kartikeya below, and Nandi, the lion, the mouse and the peacock around">'
 '<path d="M40 150 L140 30 L190 70 L250 20 L340 150Z" fill="#e8f0f8" stroke="#111" stroke-width="2"/><path d="M140 30 l14 18 h-28z M250 20 l14 18 h-28z" fill="#fff" stroke="#111" stroke-width="1.5"/>'
 '<g stroke="#111" stroke-width="2.5"><circle cx="160" cy="100" r="16" fill="#bcd4f0"/><path d="M136 170 q24 -60 48 0z" fill="#bcd4f0"/><path d="M146 88 q14 -24 28 0" fill="#3a2a1a"/><circle cx="220" cy="104" r="14" fill="#f2c79b"/><path d="M198 170 q22 -56 44 0z" fill="#e05a8a"/></g>'
 '<path d="M150 82 a7 7 0 1 0 6 -8 a5 5 0 1 1 -6 8z" fill="#fff6b0"/><path d="M166 80 q10 -10 4 -22" fill="none" stroke="#4aa3df" stroke-width="3"/><path d="M118 70 v110" stroke="#111" stroke-width="4"/><path d="M108 82 q10 -20 20 0 M118 70 v-6" fill="none" stroke="#111" stroke-width="4"/>'
 '<g stroke="#111" stroke-width="2"><circle cx="150" cy="206" r="14" fill="#f6b26b"/><path d="M146 214 q-6 12 2 18" fill="none" stroke-width="4"/><circle cx="230" cy="204" r="12" fill="#f2c79b"/><path d="M226 192 l4 -10 l4 10" fill="#ffd60a"/></g>'
 '<g stroke="#111" stroke-width="2"><ellipse cx="80" cy="220" rx="26" ry="14" fill="#fff"/><circle cx="102" cy="210" r="8" fill="#fff"/><ellipse cx="300" cy="220" rx="22" ry="12" fill="#e0a800"/><circle cx="318" cy="210" r="8" fill="#e0a800"/><ellipse cx="190" cy="246" rx="8" ry="5" fill="#999"/><path d="M262 250 q10 -30 20 0" fill="#1d6fb8"/></g>'
 '</svg>')
P.append(f'''<section class="page cover">
  <div class="rays"></div>
  <div class="burst yel">WHO'S WHO ON KAILĀSA</div>
  <p class="byline">Srini presents</p>
  <h1 style="font-size:clamp(26px,7.6vw,76px)">ŚIVA'S FAMILY<br>AND SYMBOLS</h1>
  <div class="series">THE MOON, THE SNAKE, THE ASH · AND THE HOUSEHOLD OF KAILĀSA</div>
  <div class="tag">Why Śiva looks the way He does, and who lives with Him · explained and illustrated</div>
  {cover_svg}
  <div class="cast">
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#kiran"/></svg>Zappy<br><small>asks the questions</small></figure>
    <figure><svg viewBox="0 0 64 64" aria-hidden="true"><use href="#guru"/></svg>Prof. Bolt<br><small>has the answers</small></figure>
  </div>
  <div class="bubble" style="max-width:620px;margin:10px auto 4px;text-align:left">
    <span class="who">HOW THIS WORKS:</span> First a labelled picture of Śiva, then <b>one page for each symbol</b>: what it is, the story behind it, and what it teaches. Then the family: Pārvatī, Gaṇeśa, Kārttikeya and the wider family, and the four animals who should be enemies but live in peace.
  </div>
</section>
''')
P.append(page('foreword','FOREWORD','','''<div class="panel bg-blue halftone" style="font-size:17px;line-height:1.6">
    <p>Look at any picture of Śiva and questions crowd in. Why a moon in His hair? Why a river? Why a snake around the neck, ash on the body, a blue throat, a third eye? Why does He sit on a bull, and why is His wife's mount a lion that could eat it?</p>
    <p>Every detail has a story, and every story a meaning. The crescent moon is a curse that Śiva softened; the blue throat is the poison He held to save the world; the ash is what remains when everything else is burnt.</p>
    <p>And Śiva, the great ascetic, is also a family man: husband of Pārvatī, father of Gaṇeśa and Kārttikeya, at the centre of a household of the most unlikely companions. This guide explains them all, one page at a time.</p>
    <p style="text-align:right;margin-top:14px"><span class="bang" style="font-size:22px;color:#1d4f9a">Har Har Mahādev,</span><br><span class="bang" style="font-size:26px">srini.presents</span> 🙏</p>
  </div>''').replace('<div class="sub"></div>\n  ',''))
toc=[('glance','Śiva at a Glance'),('eye','The Third Eye'),('moon','The Crescent Moon'),('ganga','The Gaṅgā in His Hair'),('snake','The Serpent'),('throat','The Blue Throat'),('trident','The Trident and the Ḍamaru'),('ash','Ash and the Three Lines'),('rudraksha','Rudrākṣa and the Tiger Skin'),('linga','The Liṅga'),('kailasa','Kailāsa'),('nandi','Nandi'),('parvati','Pārvatī'),('ganesha','Gaṇeśa'),('kartikeya','Kārttikeya'),('wider','The Wider Family'),('opposites','A Family of Opposites'),('glossary','Glossary'),('end','On One Page'),('sources','Sources')]
P.append(page('contents','CONTENTS','','<ul class="toc">\n    <li class="part">THE SYMBOLS</li>'+''.join(f'<li><span class="num">{i+1}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc[:12]))+'<li class="part">THE FAMILY</li>'+''.join(f'<li><span class="num">{i+13}</span><a href="#{a}">{t}</a></li>' for i,(a,t) in enumerate(toc[12:]))+'\n  </ul>').replace('<div class="sub"></div>\n  ',''))
# glance
g=('<svg class="fig" style="border:3px solid var(--ink);background:#eef3fa" width="560" height="420" viewBox="0 0 560 420" role="img" aria-label="Labelled drawing of Shiva: crescent moon, Ganga in the hair, third eye, blue throat, serpent, rudraksha beads, ash lines, trident, damaru, tiger skin, and Nandi">'
 '<g stroke="#111" stroke-width="3"><path d="M200 400 q80 -220 160 0z" fill="#bcd4f0"/><path d="M230 400 l20 -90 h60 l20 90z" fill="#e0a800"/>'+''.join(f'<circle cx="{250+12*k}" cy="{340+((k*7)%3)*12}" r="3" fill="#111"/>' for k in range(6))+
 '<circle cx="280" cy="140" r="54" fill="#bcd4f0"/><path d="M226 120 q54 -110 108 0 q-10 -30 -54 -36 q-44 6 -54 36z" fill="#3a2a1a"/><rect x="266" y="190" width="28" height="22" fill="#1d4f9a"/></g>'
 '<path d="M240 70 a14 14 0 1 0 10 -16 a10 10 0 1 1 -10 16z" fill="#fff6b0" stroke="#111" stroke-width="2"/><path d="M314 76 q24 -20 10 -50" fill="none" stroke="#4aa3df" stroke-width="5"/>'
 '<path d="M272 118 l8 -14 l8 14 l-8 6z" fill="#e63946" stroke="#111" stroke-width="2"/><path d="M262 106 h36 M262 112 h36" stroke="#fff" stroke-width="3"/>'
 '<path d="M240 220 q40 30 80 0 q10 20 -10 30" fill="none" stroke="#2a9d6f" stroke-width="6"/><circle cx="310" cy="250" r="6" fill="#2a9d6f" stroke="#111"/>'
 '<path d="M150 120 v280" stroke="#111" stroke-width="6"/><path d="M130 140 q20 -40 40 0 M150 120 v-16" fill="none" stroke="#111" stroke-width="6"/><path d="M130 140 v-24 M170 140 v-24" stroke="#111" stroke-width="6"/>'
 '<path d="M152 200 l-14 -10 v20z M152 200 l14 -10 v20z" fill="#c9a26b" stroke="#111" stroke-width="2"/>'
 '<g stroke="#111" stroke-width="2.5"><ellipse cx="470" cy="370" rx="44" ry="24" fill="#fff"/><circle cx="508" cy="350" r="14" fill="#fff"/><path d="M500 340 l-4 -12 M514 338 l4 -12"/></g>'
 +''.join(f'<text x="{x}" y="{y}" {F} font-size="15" fill="#c0392b">{t}</text><path d="M{lx1} {ly1} L{lx2} {ly2}" stroke="#555" stroke-width="1.2"/>' for x,y,t,lx1,ly1,lx2,ly2 in [
  (40,60,'CRESCENT MOON',150,56,236,66),(380,30,'GAṄGĀ',380,36,326,44),(380,110,'THIRD EYE',378,106,290,112),(380,200,'BLUE THROAT',378,196,296,200),(380,250,'SERPENT',378,246,318,248),(380,320,'RUDRĀKṢA',378,316,322,342),(40,240,'ḌAMARU',96,236,140,204),(30,110,'TRIŚŪLA',94,106,130,124),(380,400,'NANDI',420,396,440,384),(40,300,'TIGER SKIN',120,300,240,360),(380,150,'ASH LINES',378,146,298,110)])
 +'</svg>')
P.append(page('glance','ŚIVA AT A GLANCE','Every detail has a story',g+'''
  <div class="note">A simplified drawing: images differ by region and tradition, and not every image shows every symbol.</div>
  '''+talk('That\'s a lot of things on one god!','And each one is a story. Turn the page and we\'ll take them one by one, from the head down.')))
def fig(label,body,bg='#eef3fa'): return svg(label,body,bg)
P.append(sym('eye','THE THIRD EYE','Tri-netra, Tryambaka',
 fig('Shiva\'s face with a vertical third eye on the forehead sending out a beam of fire toward a small figure of Kama turning to ash',HEAD('<path d="M104 52 l6 -12 l6 12 l-6 6z" fill="#e63946" stroke="#111" stroke-width="2"/><path d="M110 40 L180 14" stroke="#ff8c1a" stroke-width="5"/><ellipse cx="190" cy="24" rx="16" ry="5" fill="#999"/>')),
 'A third eye in the middle of Śiva\'s forehead. His two eyes see the world; the third sees beyond it. When it opens, it burns.',
 '<p><b>The story.</b> When Kāma, the god of desire, shot his flower arrow to break Śiva\'s meditation, Śiva opened His third eye and Kāma was burnt to ash. (See Part 2 of our Śiva Mahimna series.)</p><p><b>What it means.</b> The third eye is the eye of wisdom (<i>jñāna</i>). It doesn\'t look at things; it sees through them. What it burns is not the world but illusion and desire.</p><p><b>Three eyes.</b> Śiva is <b>Tryambaka</b> and <b>Trinetra</b>, "three-eyed". His eyes are often said to be the sun, the moon and fire.</p>',
 ('💡 Tryambaka','The "three-eyed": the first word of the Mahāmṛtyuñjaya mantra.','💡 The dot','Many people wear a dot or mark between the brows: the place of the inner eye.'),
 ('Can the third eye really burn things?','In the story it burnt Kāma. Its lesson is about us: when we see clearly, our desires lose their power.'),
 'Two eyes for the world, <b>a third for the truth</b>.'))
P.append(sym('moon','THE CRESCENT MOON','Candraśekhara, the moon-crowned',
 fig('Shiva\'s head with a thin crescent moon resting in the matted hair, and a night sky with the moon waxing and waning',HEAD('<path d="M86 34 a14 14 0 1 0 10 -16 a10 10 0 1 1 -10 16z" fill="#fff6b0" stroke="#111" stroke-width="2"/>')+''.join(f'<circle cx="{150+16*k}" cy="140" r="6" fill="#fff6b0" stroke="#111"/>' for k in range(4)),'#16264a'),
 'A thin crescent moon rests in Śiva\'s matted hair. He is called <b>Candraśekhara</b>, "moon-crested", and <b>Somanātha</b>, "Lord of the moon".',
 '<p><b>The story.</b> The Moon, Candra, married the twenty-seven daughters of Dakṣa but loved only Rohiṇī. Dakṣa cursed him to waste away. The dying Moon worshipped Śiva at Prabhāsa, and Śiva softened the curse: the Moon would wane and wax for ever. Śiva placed the crescent on His head. (Our Somanātha guide tells it in full.)</p><p><b>What it means.</b> The moon marks time, waxing and waning; Śiva wears it as an ornament because He is beyond time, <b>Mahākāla</b>. It also stands for the mind, which grows calm in His presence.</p>',
 ('💡 Somanātha','The first jyotirliṅga, named for this story.','💡 Phases','The waxing and waning moon, ruled by Śiva\'s blessing, sets the Hindu calendar.'),
 ('Why only a thin crescent?','The Moon came to Him at his weakest. Śiva wears the moon in its smallest phase: He holds what is fading.'),
 'Śiva wears time itself <b>as a small ornament</b>.'))
P.append(sym('ganga','THE GAṄGĀ IN HIS HAIR','Gaṅgādhara, bearer of the Gaṅgā',
 fig('The river Ganga falling from the sky into Shiva\'s matted hair and flowing out gently onto the earth below',HEAD('<path d="M150 0 q-20 20 -30 46" fill="none" stroke="#4aa3df" stroke-width="7"/><path d="M90 60 q-30 40 -40 100" fill="none" stroke="#4aa3df" stroke-width="5"/>')+f'<text x="170" y="20" {F} font-size="10">FROM HEAVEN</text><text x="40" y="150" {F} font-size="10">TO EARTH</text>'),
 'The river Gaṅgā flows from the knot of Śiva\'s matted hair (<i>jaṭā</i>). He is <b>Gaṅgādhara</b>, "the bearer of the Gaṅgā".',
 '<p><b>The story.</b> King <b>Bhagīratha</b> did long penance to bring the heavenly river down to earth, to purify the ashes of his ancestors. But her fall would have shattered the world. Śiva caught her in His hair and let her flow out gently, as the Gaṅgā.</p><p><b>What it means.</b> Śiva takes the force that would destroy and makes it a blessing. Raw power becomes a river that feeds a land.</p><p><b>Other rivers.</b> The Godāvarī, "the Gaṅgā of the South", is brought down by the sage Gautama in the Tryambakeśvara story.</p>',
 ('💡 Bhagīratha','His effort gave us the phrase "bhagīratha prayatna", a superhuman effort.','💡 Jaṭā','The matted locks of the ascetic; Śiva\'s are said to fill the sky.'),
 ('Why not let her fall straight down?','The force would have broken the earth. Śiva softened it. Great power needs someone to hold it gently.'),
 'He holds the force of heaven <b>so it can bless the earth</b>.'))
P.append(sym('snake','THE SERPENT','Nāgabhūṣaṇa, adorned with serpents',
 fig('A serpent coiled around Shiva\'s neck with its hood raised, and a small scene of the churning of the ocean with a snake as the rope',HEAD('<path d="M80 110 q30 26 60 0 q8 16 -6 24" fill="none" stroke="#2a9d6f" stroke-width="7"/><circle cx="134" cy="134" r="7" fill="#2a9d6f" stroke="#111" stroke-width="2"/>')),
 'A serpent, often named <b>Vāsuki</b>, coils around Śiva\'s neck. Snakes also form His armlets, sacred thread and earrings.',
 '<p><b>The story.</b> Vāsuki, king of serpents, served as the churning rope when gods and demons churned the ocean. Tradition says Śiva honoured him by wearing him as a garland.</p><p><b>What it means.</b> The snake is death, fear and danger. Śiva wears it as jewellery: what terrifies us is an ornament to Him. The coiled snake also stands for <b>kuṇḍalinī</b>, the sleeping inner energy, mastered by the yogī.</p><p><b>Shedding skin.</b> The snake sheds its old skin and lives on, a sign of renewal and of time\'s cycles.</p>',
 ('💡 Vāsuki','King of serpents and the churning rope of the Samudra Manthana.','💡 Nāga Pañcamī','The festival when snakes are honoured, in Śrāvaṇa.'),
 ('Isn\'t He afraid of the snake?','He\'s the Lord of death, Mṛtyuñjaya. What we fear, He wears. That\'s the point.'),
 'What we fear, <b>He wears as an ornament</b>.'))
P.append(sym('throat','THE BLUE THROAT','Nīlakaṇṭha',
 fig('Shiva drinking the dark poison from the ocean and his throat turning blue, with Parvati holding his throat',HEAD(throat='#1d4f9a')+'<path d="M110 160 q-30 -40 0 -44" fill="none" stroke="#2b2b2b" stroke-width="7" opacity=".7"/><path d="M150 100 q-14 4 -30 10" stroke="#f2c79b" stroke-width="6"/>'),
 'Śiva\'s throat is blue. He is <b>Nīlakaṇṭha</b>, "the blue-throated one".',
 '<p><b>The story.</b> When the ocean was churned, the first thing to rise was <b>Hālāhala</b>, a poison that could destroy the world. Gods and demons ran to Śiva. He drank it. Pārvatī pressed His throat so it would not go down, and it stayed there, turning the throat blue.</p><p><b>What it means.</b> Śiva takes in the world\'s poison so others don\'t have to. He neither swallows it (letting it harm Him) nor spits it out (letting it harm others): He holds it. The mark is a scar of compassion.</p>',
 ('💡 Hālāhala','The world-ending poison from the churned ocean.','💡 In the Mahimna','Verse 14 calls this mark Śiva\'s greatest ornament.'),
 ('Why didn\'t He just spit it out?','It would have poisoned the world. So He held it. Sometimes love means carrying what would hurt others.'),
 'He holds the world\'s poison, <b>and wears the mark as an ornament</b>.'))
P.append(sym('trident','THE TRIDENT AND THE ḌAMARU','Triśūla and ḍamaru',
 fig('A trident with a small hourglass drum tied to it, the drum sounding letters into the air',
  '<path d="M90 150 V30" stroke="#111" stroke-width="6"/><path d="M70 50 q20 -40 40 0 M90 30 v-14" fill="none" stroke="#111" stroke-width="6"/><path d="M70 50 v-26 M110 50 v-26" stroke="#111" stroke-width="6"/>'
  '<path d="M92 80 l-16 -12 v24z M92 80 l16 -12 v24z" fill="#c9a26b" stroke="#111" stroke-width="2"/>'+''.join(f'<text x="{x}" y="{y}" font-family="Noto Sans" font-style="italic" font-size="12">{t}</text>' for x,y,t in [(130,50,'a i u ṇ'),(140,74,'ṛ ḷ k'),(130,98,'e o ṅ'),(146,122,'ai au c')])),
 'The <b>triśūla</b>, a three-pronged trident, and the <b>ḍamaru</b>, a small hourglass-shaped drum, often tied to it.',
 '<p><b>The trident.</b> Its three prongs are read as many triads: creation, protection and dissolution; past, present and future; the three guṇas; will, knowledge and action. Śiva holds all three, and is beyond them.</p><p><b>The drum.</b> The ḍamaru beats the rhythm of creation as Śiva dances. Tradition says that at the end of His dance it sounded fourteen times, and the grammarian Pāṇini heard in them the <b>Maheśvara Sūtras</b>, the sound-lists on which Sanskrit grammar is built.</p><p><b>Sound and form.</b> Together they say: creation begins with sound and ends with the cutting away of illusion.</p>',
 ('💡 Maheśvara Sūtras','Fourteen sound-lists that open Pāṇini\'s grammar, traditionally from Śiva\'s drum.','💡 Triśūla','Also carried by the Goddess as Durgā: the shared weapon of Śiva and Śakti.'),
 ('A drum invented grammar?','That\'s the tradition! The fourteen beats of Śiva\'s drum became the sounds of Sanskrit. Sound comes before everything.'),
 'The drum <b>begins creation</b>; the trident <b>cuts illusion</b>.',
 'The Maheśvara Sūtras story is tradition; Pāṇini\'s own text does not tell it.'))
P.append(sym('ash','ASH AND THE THREE LINES','Bhasma, vibhūti and the tripuṇḍra',
 fig('A forehead marked with three horizontal lines of white ash and a red dot, beside a small fire burning down to ash',
  '<circle cx="80" cy="80" r="50" fill="#f2c79b" stroke="#111" stroke-width="2.5"/><path d="M48 66 h64 M46 78 h68 M48 90 h64" stroke="#fff" stroke-width="6"/><circle cx="80" cy="78" r="4" fill="#e63946"/>'
  '<path d="M150 140 h50 l-6 10 h-38z" fill="#7a5a3a" stroke="#111" stroke-width="2"/><path d="M160 140 q8 -24 16 0 q6 -18 12 0" fill="#ff8c1a" stroke="#111" stroke-width="1.5"/><ellipse cx="176" cy="114" rx="20" ry="5" fill="#ccc"/>'),
 'Śiva smears His body with ash. Śaivas wear it too, as <b>tripuṇḍra</b>: three horizontal lines across the forehead.',
 '<p><b>The meaning of ash.</b> Ash is what remains when everything else is burnt. It cannot burn again. Śiva wears it as a reminder that bodies and possessions end, and that only the Self remains.</p><p><b>The three lines.</b> The tripuṇḍra is a Śaiva mark of three horizontal lines; the Kālāgni Rudra Upaniṣad explains them as triads such as the three sacred fires, the three syllables of Oṃ, the three guṇas and the three worlds. Another reading sees in them Śiva\'s three powers of will, knowledge and action.</p><p><b>Vaiṣṇava contrast.</b> The Vaiṣṇava mark, the ūrdhva-puṇḍra, runs vertically.</p>',
 ('💡 Vibhūti','"Glory, power": the name for sacred ash.','💡 Bhasma ārati','Mahākāla in Ujjain is famous for the dawn worship with ash.'),
 ('Ash sounds sad.','It\'s actually freeing: once you know everything ends as ash, you hold it lightly. That\'s why Śiva wears it happily.'),
 'What remains when all is burnt: <b>Śiva wears it as His robe</b>.'))
P.append(sym('rudraksha','RUDRĀKṢA AND THE TIGER SKIN','Beads of tears, and a hide won in battle',
 fig('A string of rough rudraksha beads beside a tiger skin with stripes',
  ''.join(f'<circle cx="{60+38*__import__("math").cos(k/18*6.283):.0f}" cy="{80+38*__import__("math").sin(k/18*6.283):.0f}" r="6" fill="#8a4a2a" stroke="#111" stroke-width="1.5"/>' for k in range(18))
  +'<path d="M130 40 h70 l-6 30 l8 30 l-8 30 h-64 l6 -30 l-6 -30z" fill="#e0a800" stroke="#111" stroke-width="2.5"/>'+''.join(f'<path d="M{140+12*k} 50 q4 30 0 80" stroke="#111" stroke-width="3" fill="none"/>' for k in range(5))),
 '<b>Rudrākṣa</b> beads, the dried seeds of a tree, worn and used for japa; and the <b>tiger skin</b> Śiva sits on or wears.',
 '<p><b>Rudra\'s eye.</b> <i>Rudrākṣa</i> means "eye of Rudra". A common tradition says Śiva sat in meditation for a very long time, and when He opened His eyes, His tears fell to earth and became rudrākṣa trees. The beads are counted for japa, often in strings of 108 beads plus one.</p><p><b>The tiger.</b> In one story the proud sages of the Dāruka forest sent a tiger to kill Śiva. He killed it and wore its skin. The tiger is fierce desire and ego, tamed and sat upon.</p><p><b>The elephant hide.</b> Śiva also wears the hide of the elephant demon Gajāsura, whom He defeated, as <b>Gajāsura-saṃhāra</b>.</p>',
 ('💡 Mukhī','Rudrākṣa beads are classed by their "faces", the natural lines on them.','💡 Japa','Repeating a mantra, often Oṃ Namaḥ Śivāya, counted on beads.'),
 ('Tears became beads?','In the story, yes: tears of compassion. Devotees wear them to keep that compassion close.'),
 'Tears turned to beads, a tiger turned to a seat: <b>emotion and ego, mastered</b>.',
 'Legends of the rudrākṣa\'s origin differ between texts.'))
P.append(sym('linga','THE LIṄGA','The sign of the formless',
 fig('A linga on its base with water flowing over it, and behind it a faint endless pillar of light',
  '<rect x="94" y="0" width="32" height="160" fill="#ffd60a" opacity=".35"/>'+f'<g transform="translate(110 136) scale(1.6)">{LINGA}</g><path d="M110 20 q-4 30 0 50" stroke="#4aa3df" stroke-width="3" fill="none"/>'),
 'The <b>liṅga</b> is Śiva\'s most common form of worship: a smooth upright stone on a base, the <b>pīṭha</b> or yoni.',
 '<p><b>A sign.</b> <i>Liṅga</i> means "mark" or "sign": a sign of what has no form. It has no face or limbs because Śiva is beyond form.</p><p><b>The pillar of light.</b> Its origin story is the endless column of fire that Brahmā and Viṣṇu could not measure: the <b>Liṅgodbhava</b>. The twelve <b>jyotirliṅgas</b> are the places where that light is said to have appeared (see our series).</p><p><b>Śiva and Śakti.</b> The liṅga rising from the pīṭha is read as Śiva and Śakti, consciousness and energy, together. Water poured over it (<i>abhiṣeka</i>) flows out through the spout.</p>',
 ('💡 Svayambhū','Self-manifested liṅgas, found rather than carved, are especially revered.','💡 Abhiṣeka','Bathing the liṅga with water, milk and other offerings while chanting, as in the Rudram.'),
 ('Why a stone with no face?','Because Śiva is beyond any face. The liṅga points to the formless, like an arrow pointing to the sky.'),
 'A sign without a face <b>for the One beyond all form</b>.'))
P.append(sym('kailasa','KAILĀSA','Śiva\'s mountain home',
 fig('A snow mountain shaped like a pyramid with a lake in front, under a night sky',
  '<rect width="220" height="160" fill="#16264a"/><path d="M40 130 L110 30 L180 130Z" fill="#e8f0f8" stroke="#111" stroke-width="2.5"/><path d="M110 30 v100" stroke="#bcd" stroke-width="2"/><ellipse cx="110" cy="146" rx="80" ry="10" fill="#4aa3df"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="1.5" fill="#fff"/>' for x,y in [(20,20),(60,40),(170,20),(200,60),(30,80)])),
 '<b>Mount Kailāsa</b>, in the Himālaya in Tibet, is Śiva\'s home in tradition, where He sits in meditation with Pārvatī.',
 '<p><b>The axis of the world.</b> Hindus, Buddhists, Jains and followers of Bon all hold Kailāsa sacred. Four great rivers rise near it, and Lake Mānasarovar lies at its foot.</p><p><b>Never climbed.</b> Out of reverence, there is no recorded ascent of its summit. Pilgrims walk around it instead, the <b>parikramā</b>, about a day\'s hard walk or more.</p><p><b>Inner Kailāsa.</b> Yogīs speak of Kailāsa within: the crown of the head, where Śiva and Śakti unite.</p>',
 ('💡 Mānasarovar','The sacred lake at Kailāsa\'s foot, "made from Brahmā\'s mind".','💡 Rāvaṇa','The demon king tried to lift Kailāsa and was pinned by Śiva\'s toe.'),
 ('Nobody has climbed it?','There\'s no recorded ascent; climbers have left it alone out of respect for all the faiths that hold it holy.'),
 'The mountain at the centre of the world, <b>left unclimbed out of reverence</b>.'))
P.append(sym('nandi','NANDI','The bull who waits',
 fig('A white bull seated patiently facing a temple doorway with a linga inside',
  f'<rect x="130" y="40" width="70" height="100" fill="#e8c27a" stroke="#111" stroke-width="2.5"/><g transform="translate(165 132) scale(.8)">{LINGA}</g>'
  '<g stroke="#111" stroke-width="2.5"><ellipse cx="60" cy="120" rx="40" ry="20" fill="#fff"/><circle cx="100" cy="100" r="14" fill="#fff"/><path d="M94 88 l-4 -12 M106 88 l4 -12"/></g>'),
 '<b>Nandi</b>, the white bull, is Śiva\'s mount (<i>vāhana</i>), His gatekeeper and His greatest devotee. In temples he sits facing the sanctum.',
 '<p><b>Always facing Śiva.</b> In every Śiva temple Nandi sits outside the sanctum, gazing at the liṅga. He doesn\'t ask for anything; he waits. Devotees often whisper their prayers into his ear, to be passed on to Śiva.</p><p><b>Dharma.</b> The bull stands for dharma, strength and steadiness. Riding the bull, Śiva is master of strength, not ruled by it.</p><p><b>Chief of the gaṇas.</b> In many stories Nandi is the leader of Śiva\'s attendants and the guardian of Kailāsa.</p>',
 ('💡 Vāhana','A god\'s "vehicle": an animal that carries and also symbolises the deity.','💡 Nandi Hills','The hills near Bengaluru are named after a Nandi shrine on top.'),
 ('Why does Nandi always face the door?','He\'s the perfect devotee: patient, steady, eyes only on the Lord. That\'s why people whisper to him.'),
 'Patient, steady, eyes on the Lord: <b>the model devotee</b>.'))
P.append(sym('parvati','PĀRVATĪ','Satī, Pārvatī, and the half that completes Him',
 fig('Shiva and Parvati as Ardhanarishvara, half blue and half pink, in one body',
  '<g stroke="#111" stroke-width="2.5"><path d="M110 30 a24 24 0 0 0 0 48z" fill="#bcd4f0"/><path d="M110 30 a24 24 0 0 1 0 48z" fill="#f2c79b"/><path d="M110 78 l-34 80 h34z" fill="#1d4f9a"/><path d="M110 78 l34 80 h-34z" fill="#e05a8a"/></g><path d="M110 26 v134" stroke="#111" stroke-dasharray="3 3"/>'),
 '<b>Pārvatī</b>, "daughter of the mountain", is Śiva\'s wife: Śakti, the power without which Śiva cannot act. Her other forms include Durgā, Kālī, Umā and Gaurī.',
 '<p><b>Satī first.</b> Śiva\'s first wife was <b>Satī</b>, daughter of Dakṣa. Insulted at her father\'s sacrifice, she gave up her life; Śiva\'s grief and anger shook the worlds.</p><p><b>Pārvatī.</b> Satī was reborn as Pārvatī, daughter of Himavān, king of the mountains. She won the withdrawn Śiva not by charm (Kāma\'s arrow failed) but by her own fierce penance.</p><p><b>Ardhanārīśvara.</b> In the end Śiva made her half of His own body: the "Lord who is half woman". Śiva is consciousness, Śakti is energy; neither is complete alone.</p>',
 ('💡 Śakti Pīṭhas','The places where parts of Satī\'s body fell, sacred to the Goddess.','💡 Śiva–Śakti','"Śiva without Śakti is śava (a corpse)", a famous saying.'),
 ('She won Him by penance, not beauty?','Exactly. Kāma\'s arrow failed; her tapas succeeded. She was His equal in strength of will.'),
 'Śiva is consciousness, Pārvatī its power: <b>two halves of one</b>.'))
P.append(sym('ganesha','GAṆEŚA','The elder son, Lord of the gaṇas',
 fig('Ganesha with an elephant head and a broken tusk, seated, with a mouse beside him',
  '<g stroke="#111" stroke-width="2.5"><circle cx="110" cy="60" r="28" fill="#f6b26b"/><path d="M84 52 q-20 0 -20 24 q14 4 20 -10 M136 52 q20 0 20 24 q-14 4 -20 -10" fill="#f6b26b"/><path d="M106 80 q-10 30 8 40" fill="none" stroke-width="8" stroke="#f6b26b"/><path d="M106 80 q-10 30 8 40" fill="none" stroke-width="2"/><path d="M76 150 q34 -60 68 0z" fill="#e63946"/><path d="M98 78 l-6 8" stroke="#fff" stroke-width="4"/></g>'
  '<g stroke="#111" stroke-width="2"><ellipse cx="170" cy="146" rx="12" ry="7" fill="#999"/><circle cx="182" cy="142" r="4" fill="#999"/></g>'),
 '<b>Gaṇeśa</b>, son of Pārvatī and Śiva, with an elephant\'s head: remover of obstacles, lord of beginnings, worshipped first in every rite.',
 '<p><b>The story.</b> Pārvatī shaped a boy from turmeric paste and set him to guard her door. When Śiva came home, the boy, not knowing Him, blocked the way. In the fight Śiva cut off his head. Seeing Pārvatī\'s grief, Śiva gave the boy the head of an elephant and made him chief of the gaṇas: <b>Gaṇapati</b>.</p><p><b>The mouse.</b> His vehicle is a mouse, <b>Mūṣaka</b>: the small, restless mind or desire, mastered by wisdom.</p><p><b>The scribe.</b> Tradition says Gaṇeśa wrote down the Mahābhārata as Vyāsa dictated it, breaking off a tusk to use as a pen.</p>',
 ('💡 First worship','Rites begin with Gaṇeśa: "vakratuṇḍa mahākāya…".','💡 Gaṇeśa Caturthī','His birthday festival in Bhādrapada, huge in Maharashtra and Karnataka.'),
 ('Śiva cut off His own son\'s head?','He didn\'t know who the boy was. The story ends with a new life and a new honour: Gaṇeśa is worshipped first, before every god.'),
 'Guardian at the door, <b>remover of obstacles, first to be worshipped</b>.'))
P.append(sym('kartikeya','KĀRTTIKEYA','The younger son: Skanda, Murugan, Subrahmaṇya',
 fig('Karttikeya with six faces holding a spear, riding a peacock',
  '<g stroke="#111" stroke-width="2"><ellipse cx="110" cy="130" rx="44" ry="18" fill="#1d6fb8"/><path d="M150 124 q20 -30 10 -50" fill="none" stroke="#1d6fb8" stroke-width="6"/></g>'
  +''.join(f'<circle cx="{86+16*k}" cy="{56-6*abs(k-1.5)}" r="9" fill="#f2c79b" stroke="#111" stroke-width="1.5"/>' for k in range(4))
  +'<path d="M150 20 v100" stroke="#111" stroke-width="4"/><path d="M144 26 l6 -14 l6 14z" fill="#c9a26b" stroke="#111"/><path d="M96 70 q14 40 28 0z" fill="#ff8c1a" stroke="#111" stroke-width="2"/>'),
 '<b>Kārttikeya</b>, also called Skanda, Kumāra, Ṣaṇmukha ("six-faced"), and in the south <b>Murugan</b> and Subrahmaṇya: the warrior son, riding a peacock and holding the spear (<i>vel</i>).',
 '<p><b>Born to win.</b> The demon <b>Tāraka</b> could be killed only by a son of Śiva. Kāma\'s arrow, Pārvatī\'s penance and their marriage all led to this birth. Raised by the six <b>Kṛttikā</b> stars (the Pleiades), the child grew six faces to be fed by all six. He led the gods\' army and defeated Tāraka.</p><p><b>The mango.</b> A famous story: a single fruit would go to whichever son circled the world first. Kārttikeya flew off on his peacock; Gaṇeśa walked around his parents, saying "they are my world", and won. Hurt, Kārttikeya went south, to Palani.</p><p><b>Murugan.</b> In Tamil Nadu he is one of the most loved gods, with six great shrines, the <b>Ārupaḍai Vīḍu</b>.</p>',
 ('💡 Vel','The spear given to him by Pārvatī; in Tamil, "vel vel" is a cry of devotion.','💡 Mallikārjuna','In one legend Śiva and Pārvatī followed the hurt Kārttikeya to Śrīśaila (see our guide).'),
 ('Gaṇeśa won by walking around his parents?','He said his parents were his whole world. It\'s the best-known lesson about honouring one\'s parents in the tradition.'),
 'Six faces, a spear, a peacock: <b>the warrior who defeated Tāraka</b>.',
 'Whether Gaṇeśa or Kārttikeya is the elder differs between north and south India.'))
P.append(page('wider','THE WIDER FAMILY','Daughters, sons and forms in regional traditions','''<div class="panel reading"><p>The best-known family is Śiva, Pārvatī, Gaṇeśa and Kārttikeya, the <b>Śiva Parivār</b> of temple walls and family shrines. But many regions and texts add others.</p></div>
  <div class="g2">
    <div class="card bg-yellow"><h4>🌸 Aśokasundarī</h4><p>A daughter of Śiva and Pārvatī in the <b>Padma Purāṇa</b>, created from the wish-fulfilling tree to ease Pārvatī's loneliness; her name means "the beautiful one who ends sorrow". She married King Nahuṣa; she is largely absent from other major texts.</p></div>
    <div class="card bg-blue"><h4>🐍 Manasā</h4><p>The snake goddess of Bengal and eastern India, called Śiva's daughter in the medieval <b>Manasā-maṅgal</b> poems.</p></div>
    <div class="card bg-green"><h4>🌿 Ayyappa</h4><p>In Kerala, <b>Hariharaputra</b>, "son of Hari and Hara": born of Śiva and Viṣṇu as Mohinī; worshipped at Sabarimala.</p></div>
    <div class="card bg-red"><h4>🔥 Vīrabhadra and Bhairava</h4><p>Not children but fierce <b>forms</b> born from Śiva: Vīrabhadra destroyed Dakṣa's sacrifice; Kāla Bhairava guards Kāśī.</p></div>
  </div>
  <div class="panel"><span class="caption">The gaṇas</span><p style="margin:0">Śiva's household also includes his <b>gaṇas</b>, a host of attendants of every shape, led by Nandi and later by Gaṇeśa, and devotees like the sage <b>Bhṛṅgi</b>.</p></div>
  '''+talk('Śiva has a daughter?','In the Padma Purāṇa, yes: Aśokasundarī. Many people learnt of her from television. Regional traditions add more family; the core four are the ones in every shrine.')+'''
  <div class="note">These figures belong to particular texts and regions; accounts differ.</div>'''))
opp=('<svg class="fig" style="border:3px solid var(--ink);background:#fff8ec" width="560" height="240" viewBox="0 0 560 240" role="img" aria-label="Diagram of the family vehicles: the snake would eat the mouse, the peacock would eat the snake, the lion would eat the bull, yet all live together in peace">'
 +''.join(f'<g transform="translate({x} {y})"><circle r="38" fill="{c}" stroke="#111" stroke-width="3"/><text y="5" text-anchor="middle" {F} font-size="15">{t}</text><text y="56" text-anchor="middle" {F} font-size="12">{s}</text></g>' for x,y,c,t,s in [(90,70,'#fff','BULL','ŚIVA'),(470,70,'#e0a800','LION','PĀRVATĪ'),(90,180,'#ccc','MOUSE','GAṆEŚA'),(470,180,'#4aa3df','PEACOCK','KĀRTTIKEYA'),(280,124,'#2a9d6f','SNAKE','ŚIVA\'S NECK')])
 +f'<path d="M430 70 L130 70" stroke="#c0392b" stroke-width="3" stroke-dasharray="8 5"/><text x="280" y="60" text-anchor="middle" {F} font-size="12" fill="#c0392b">LION EATS BULL</text>'
 f'<path d="M244 140 L130 172" stroke="#c0392b" stroke-width="3" stroke-dasharray="8 5"/><text x="180" y="146" text-anchor="middle" {F} font-size="12" fill="#c0392b">SNAKE EATS MOUSE</text>'
 f'<path d="M432 172 L318 140" stroke="#c0392b" stroke-width="3" stroke-dasharray="8 5"/><text x="390" y="146" text-anchor="middle" {F} font-size="12" fill="#c0392b">PEACOCK EATS SNAKE</text>'
 f'<text x="280" y="226" text-anchor="middle" {F} font-size="16" fill="#2a9d6f">…YET ON KAILĀSA, ALL LIVE IN PEACE</text></svg>')
P.append(page('opposites','A FAMILY OF OPPOSITES','Why the animals of Kailāsa don\'t eat each other',opp+'''
  <div class="panel reading"><p><b>The puzzle.</b> Look at the family's animals: the snake around Śiva's neck would eat Gaṇeśa's mouse; Kārttikeya's peacock would eat the snake; Pārvatī's lion would eat Śiva's bull. In nature they are predator and prey. On Kailāsa they live side by side.</p><p><b>The teaching.</b> A home, a society, a mind can hold opposites without violence when something higher holds them together. In Śiva's presence, natural enmity falls away.</p><p><b>Opposites in the family itself.</b> The ascetic and the householder; the destroyer and the gracious one; the wise elder son and the warrior younger son; Śiva and Śakti as one body. The whole family is a lesson in harmony.</p></div>
  '''+talk('Do the animals really get along?','In the pictures, yes, and that\'s the point. If they can live together on Kailāsa, so can people with different natures.')+'''
  <div class="key">Natural enemies, one household: <b>harmony where something higher holds us together</b>.</div>'''))
gl=[('tri-netra','three-eyed'),('candraśekhara','moon-crested'),('gaṅgādhara','bearer of the Gaṅgā'),('nīlakaṇṭha','blue-throated'),('triśūla','trident'),('ḍamaru','hourglass drum'),('bhasma · vibhūti','sacred ash'),('tripuṇḍra','three lines of ash'),('rudrākṣa','"eye of Rudra" beads'),('liṅga','sign, mark'),('vāhana','vehicle, mount'),('gaṇa','attendant of Śiva'),('ardhanārīśvara','the Lord who is half woman'),('parivār','family')]
P.append(page('glossary','GLOSSARY','Words for Śiva\'s world','<table class="ct"><tr><th>Word</th><th>Means</th></tr>'+''.join(f'<tr><td class="w">{a}</td><td>{b}</td></tr>' for a,b in gl)+'</table>'))
P.append(page('end','ON ONE PAGE','Śiva\'s family and symbols in five lines','''<div class="steps">
    <div><b>The head.</b> The third eye of wisdom; the crescent moon of time, worn lightly; the Gaṅgā held so she can bless.</div>
    <div><b>The neck.</b> The serpent: fear worn as an ornament; the blue throat: the world's poison held out of compassion.</div>
    <div><b>The hands and body.</b> Trident and drum; ash that cannot burn again; rudrākṣa tears; the tamed tiger.</div>
    <div><b>Signs and home.</b> The liṅga, sign of the formless; Kailāsa, the unclimbed centre; Nandi, the patient devotee.</div>
    <div><b>The family.</b> Pārvatī as half of Him; Gaṇeśa, first to be worshipped; Kārttikeya, the warrior; four animals who should be enemies, at peace.</div>
  </div>
  '''+talk('What should I look for next time I see a picture of Śiva?','Start at the top: moon, river, third eye. Then the blue throat and the snake. Every detail is telling you a story.')+'''
  <div class="key">Śiva\'s family and symbols: <b>every detail is a teaching</b>. 🙏</div>
  <div class="follow"><b>Follow @srini.presents</b><a href="https://www.youtube.com/@srini.presents">YouTube</a> · <a href="https://www.instagram.com/srini.presents/">Instagram</a> · <a href="https://www.facebook.com/srini.presents">Facebook</a><br><b style="font-size:22px;margin-top:8px">Read more: <a href="https://srinipresents.com/">srinipresents.com</a></b></div>'''))
P.append(page('sources','SOURCES & NOTES','Where the facts come from','''<div class="panel reading small">
    <p><b>Tripuṇḍra:</b> Wikipedia's "Tripundra" and "Kalagni Rudra Upanishad" (the three lines as triads, after Deussen; Śiva's powers of will, knowledge and action, after Rigopoulos; the vertical Vaiṣṇava ūrdhva-puṇḍra).</p>
    <p><b>Aśokasundarī:</b> Wikipedia's "Ashokasundari" (daughter of Śiva and Pārvatī in the Padma Purāṇa; created from the Kalpavṛkṣa; consort of Nahuṣa; absent from most other major texts).</p>
    <p><b>The family's animals:</b> common iconographic tradition, as summarised in many devotional sources (snake and mouse, peacock and snake, lion and bull).</p>
    <p><b>Stories:</b> Śiva Purāṇa, Skanda Purāṇa, the epics and regional traditions, retold briefly; versions differ. Cross-references: our Śiva Mahimna series, 12 Jyotirliṅgas guides (Somanātha, Mallikārjuna, Tryambakeśvara) and Rudram articles.</p>
    <p><b>Not independently verified:</b> the Maheśvara Sūtras origin story; the rudrākṣa tears legend (versions differ); north–south differences on which son is elder.</p>
    <p>Pictures are simplified illustrations. Zappy and Prof. Bolt are fictional.</p>
  </div>'''))
tail=src[src.find('<script>\n  document.querySelectorAll'):]
tail=tail.replace("section.page[id$=\"b\"], section.page#about","section.page.none")
html=head+'<div class="book">\n'+''.join(P)+'</div>\n'+tail
open('Shiva_Family_and_Symbols.html','w').write(html)
print(len(html))
