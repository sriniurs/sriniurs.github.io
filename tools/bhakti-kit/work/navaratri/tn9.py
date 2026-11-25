from tn_common import *
i=8
def areca(): return '<path d="M0 0 v-40" stroke="#b8a060" stroke-width="3"/>'+''.join(f'<path d="M0 {-10-k*8} q{(-1)**k*14} -6 {(-1)**k*20} 4" fill="none" stroke="#f2e6a8" stroke-width="3"/>' for k in range(4))
def woman(c='#c0392b',flowers=True): return g(0,0,1,person(c))+(g(14,-56,.8,areca()) if flowers else '')
def smap():
    o=map_frame()
    for t,x,y in [('Hiriyaḍka',220,60),('Paṅgāla',190,110),('Nandaḷike (Kārkaḷa)',300,90),('Kavatār',280,160),('Nidgal (Beḷtaṅgaḍi)',400,190)]: o+=pin(x,y,t)
    return o+T(120,30,'Uḍupi ↑',10)
fw=foreword(i,['On a full-moon night at a shrine near Uḍupi, hundreds of women stand holding sprays of areca flowers. As the old song of Siri rises, one after another they begin to sway, then to dance, and the shrine fills with women who speak as Siri, as her daughter Sonne, as her granddaughters Abbaga and Dāraga. A man in the part of Siri’s son Kumāra goes among them, asking each: who are you?',
 'This is the <b>Siri Jātre</b>, the festival of a Tuḷu princess who refused an insult, walked out of a bribed judgement, and became a power the coast still calls on. This guide tells her story in four parts, then the shrines, the night of <b>darśana</b>, Kumāra, the 15,683-line <b>Siri pāḍdana</b>, and what scholars and the women themselves say it means.',
 'Siri’s full guide is in '+L('/tulunadu/daiva/siri/','Siri')+'; the daiva world in '+L('/tulunadu/daiva/','Daiva and Nāga traditions')+'. Previous: '+L('/tulunadu/festivals/bappanadu-jatre/','Bappanāḍu Jātre')+'.'],
 [('z','A festival where women become goddesses?'),('b','For one night, many women of the coast speak with Siri’s voice. It is one of the most remarkable festivals in India.')])
gl=glance([('Who','Siri Āḷvedi, a Baṇṭ princess worshipped as a daiva, with her family'),('Her line','Son Kumāra; daughter Sonne; granddaughters Abbaga and Dāraga'),('Patron god','Bermer, Tuḷunāḍu’s Brahmā'),('Shrines','The Ādi Āḷade; five great centres: Hiriyaḍka, Paṅgāla, Nandaḷike, Kavatār, Nidgal'),('Festival','Siri Jātre (also Siri Āḷade): a night-long festival on a full moon, held yearly at each centre'),('The rite','Darśana: women possessed by Siri and her family (dayyol)'),('The mediator','A man as Kumāra, Siri’s son'),('Held in hand','Sprays of areca flowers'),('The song','The Siri pāḍdana: 15,683 lines, about 25 hours'),('Who takes part','Women of many castes and communities')],
 S('Women holding areca flowers under a full moon at a shrine','<rect width="560" height="200" fill="#20243a"/>'+g(480,40,1.2,moon())+g(100,190,.9,tulu_temple())+''.join(g(220+k*50,190,1,woman(['#c0392b','#e0a800','#2a9d6f','#6a3d9a','#1d4f8a','#ff8c1a'][k])) for k in range(6)),'#20243a',200),
 [('z','Is Siri a goddess or a daiva?'),('b','A daiva: a woman who lived, suffered and became a power. On the coast that makes her closer to people than any distant god.')],'A princess who became <b>a power</b>.')
country=reading('country','SIRI’S COUNTRY','The Ādi Āḷade',svg(560,230,'Simplified map of the five great Siri centres in Uḍupi and Dakṣiṇa Kannaḍa',smap()),
 ['<b>Āḷade.</b> Siri’s shrines are called <b>Āḷade</b>; the original seats of her worship are the <b>Ādi Āḷade</b>, “the first Āḷade”. Many smaller shrines across the coast derive from them.',
  '<b>Five great centres.</b> <b>Hiriyaḍka</b> and <b>Paṅgāla</b> near Uḍupi, <b>Nandaḷike</b> near Kārkaḷa, <b>Kavatār</b>, and <b>Nidgal</b> in Beḷtaṅgaḍi taluk. Some lists add others, such as Dalyottu.',
  '<b>Hiriyaḍka.</b> Its Siri Jātre is among the most famous; thousands of women return to it year after year.',
  '<b>Nidgal first.</b> Nidgal is where the story begins, at the ancestral temple Siri’s father restored.',
  '<b>Kavatār.</b> A centre with old carved images of the Siri family.'],
 [('z','Why so many shrines?'),('b','Because Siri walked. The places of her life and her family’s became the places of her worship.')],'Shrines along <b>the road she walked</b>.')
born=story('born','SIRI · BORN OF FLOWERS','A gift from Bermer',
 strip('Three panels: an old lord grieving; a disguised god speaking to him at a ruined temple; areca flowers turning into a baby girl',
  [('<rect width="144" height="190" fill="#e9e2d6"/>'+g(72,170,1,person('#f4f1ea',seat=True)),'#e9e2d6'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(40,170,.9,sage())+g(104,170,.8,person('#f4f1ea'))+g(72,80,.5,tulu_temple()),'#fff3cf'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(50,160,1.4,areca())+g(100,150,1,'<circle r="12" fill="#c98a5a"/><path d="M-12 12 q12 24 24 0" fill="#f4f1ea"/>'),'#fff3cf')],
  ['grief','Bermer’s word','a daughter of flowers']),'Siri’s story, part 1, from the Siri pāḍdana.',
 ['<b>Bermaṇṇa Āḷva</b>, an ageing Baṇṭ lord of Satyanāpura, had lost his wife and his only daughter. With no heir, he prayed to <b>Bermer</b>.',
  'Bermer came to him disguised as a Brahmin and said his sorrow came from neglecting his family god’s temple, lying in ruins at <b>Nidgal</b>.',
  'Bermaṇṇa restored the temple and brought home its prasāda: <b>areca flowers</b> and sandal paste.',
  'Overnight the flowers turned into a baby girl.',
  'He named her <b>Siri</b>, “prosperity”.'],
 [('z','Is that why the women hold areca flowers?'),('b','Exactly. Siri came from areca flowers; at her jātre the women hold them as they dance.')],'A daughter <b>born of areca flowers</b>.')
insult=story('insult','SIRI · THE REFUSAL','A sari worn first by another',
 strip('Three panels: a husband giving a sari to a courtesan; Siri refusing the sari at a ceremony; Siri with her baby son at her father’s house',
  [('<rect width="144" height="190" fill="#e9e2d6"/>'+g(40,170,.9,person('#1d4f8a'))+g(104,170,.9,person('#e05050'))+g(72,100,.6,'<rect x="-14" y="-6" width="28" height="12" fill="#e0a800"/>'),'#e9e2d6'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(56,170,1,person('#c0392b'))+'<path d="M80 110 l30 -10" stroke-width="3"/>'+g(116,96,.6,'<rect x="-14" y="-6" width="28" height="12" fill="#e0a800"/>'),'#fff3cf'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(60,170,1,person('#c0392b',seat=True))+g(92,140,.7,'<circle r="10" fill="#c98a5a"/><path d="M-10 10 q10 20 20 0" fill="#f4f1ea"/>'),'#fff3cf')],
  ['the gift soiled','she refuses','Kumāra']),'Siri’s story, part 2.',
 ['Siri grew up beautiful. <b>Kānta Pūñja</b>, a minor lord of Basrūr, married her.',
  'On his way home with a sari for his pregnant wife, he visited a courtesan, Siddu, who wore the sari first.',
  'At the ceremony for her pregnancy Siri recognised it and <b>refused</b> to wear a sari another woman had worn first.',
  'Kānta Pūñja never forgave her.',
  'She gave birth to a son, <b>Kumāra</b>, at her father’s house. Her husband and his family sent no word.'],
 [('z','She turned down a gift from her husband?'),('b','She turned down an insult dressed as a gift. That one refusal is the turning point of the whole epic.')],'She refused <b>an insult dressed as a gift</b>.')
fire_=story('curse','SIRI · FIRE AND THE ROAD','Cheated, she walks away',
 strip('Three panels: bribed elders ruling; a manor house in flames; Siri walking toward a forest with her baby and her maid',
  [('<rect width="144" height="190" fill="#e9e2d6"/>'+''.join(g(26+k*30,170,.7,person('#f4f1ea',seat=True)) for k in range(4))+g(72,100,.6,'<circle r="10" fill="#e0a800"/>'),'#e9e2d6'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(72,170,.8,tulu_temple('#a0522d','#5a2a10'))+g(50,110,1.2,flame(1,'#ff8c1a'))+g(96,100,1.4,flame(1,'#ff8c1a')),'#20243a'),
   ('<rect width="144" height="190" fill="#e9f2e1"/>'+g(110,170,.8,tree('#2f6a3a'))+g(40,170,.85,person('#c0392b'))+g(70,170,.8,person('#8a6a3a')),'#e9f2e1')],
  ['the bribed elders','the curse','to Bola']),'Siri’s story, part 3.',
 ['When Bermaṇṇa died, the question of his succession went before the elders. Kānta Pūñja joined with Aṇṇu Śeṭṭi, and the <b>bribed</b> elders ruled against Siri.',
  'Siri cursed her husband’s lands and clan. By her power she set fire to the manor, now in her rival’s hands.',
  'She walked away from Satyanāpura with her baby Kumāra and her maid Dāru, toward the forest of <b>Bola</b>, working wonders on the way.',
  'On that journey she lost Kumāra and Dāru. (In some tellings Kumāra dies; in others he vanishes, foretelling that she will marry again and have a daughter.)',
  'At Bola she was taken in as a sister and married Kōḍsar Āḷva of Kotrāḍi; she bore a daughter, <b>Sonne</b>. Before she died she promised blessing and healing to all who would worship her.'],
 [('z','So Siri dies too?'),('b','She leaves human life, as every daiva of the coast does, and comes back as a power. Her last promise is why people still call on her.')],'Wronged, she walked out, <b>and promised healing</b>.')
twins=story('twins','SONNE AND THE TWINS','A broken vow',
 strip('Three panels: a couple vowing before a shrine; twin girls playing a pit board game; the twins honoured together as a carved pair',
  [('<rect width="144" height="190" fill="#fff3cf"/>'+g(50,170,.9,person('#2a9d6f'))+g(80,170,.9,person('#1d4f8a'))+g(118,170,.5,tulu_temple()),'#fff3cf'),
   ('<rect width="144" height="190" fill="#fff3cf"/>'+g(40,170,.8,person('#e0a800',seat=True))+g(104,170,.8,person('#e05050',seat=True))+'<rect x="56" y="140" width="32" height="12" fill="#8a6a3a"/>'+''.join(f'<circle cx="{60+k*6}" cy="146" r="2" fill="#fff"/>' for k in range(5)),'#fff3cf'),
   ('<rect width="144" height="190" fill="#e3eaf3"/>'+g(56,170,.9,person('#e0a800'))+g(88,170,.9,person('#e05050'))+'<rect x="36" y="80" width="72" height="96" fill="none" stroke="#8a6a3a" stroke-width="4"/>','#e3eaf3')],
  ['the vow','the board game','Abbaga–Dāraga']),'Siri’s story, part 4.',
 ['Sonne married Guru Marla, but they had no children. They vowed that if children came, they would be dedicated to Bermer.',
  'Twin daughters were born: <b>Abbaga</b> and <b>Dāraga</b>. The family forgot their vow, and ignored Bermer’s warning.',
  'While the parents were away, Bermer opened for the girls a game of <b>cenne</b>, the coast’s pit-and-seed board game.',
  'The sisters quarrelled over it; one struck the other dead with the board, and then threw herself into a well.',
  'Bermer declared the gift taken back for the broken vow. The sisters are honoured together as daivas; the carved pair Abbaga–Dāraga is among the best-known images of the cult.'],
 [('z','A tragedy over a board game?'),('b','Over a forgotten vow. The game is only how the god collected what was promised.')],'A forgotten vow, <b>two sisters lost</b>.')
night=story('night','THE SIRI JĀTRE','The night of darśana',
 strip('Three panels: women gathering at the shrine with areca flowers at dusk; women in trance dancing as the song rises; a man as Kumāra speaking with a possessed woman',
  [('<rect width="144" height="190" fill="#e9b07a"/>'+g(36,170,.8,woman('#c0392b'))+g(72,170,.8,woman('#2a9d6f'))+g(108,170,.8,woman('#6a3d9a')),'#e9b07a'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(40,170,.85,woman('#c0392b'))+g(100,160,.85,woman('#e0a800'))+g(120,40,.8,moon()),'#20243a'),
   ('<rect width="144" height="190" fill="#20243a"/>'+g(46,170,.9,woman('#2a9d6f'))+g(104,170,.9,person('#f4f1ea'))+'<path d="M80 100 q10 -10 20 0" fill="none" stroke="#fff" stroke-width="2"/>','#20243a')],
  ['gathering','the song and the trance','“Who are you?”']),'The festival night at an Ādi Āḷade, as described in our guide and by scholars who have attended.',
 ['Each Ādi Āḷade holds its yearly <b>Siri Jātre</b> through one full-moon night. (Sources differ on the month at each centre.)',
  'Women gather, often hundreds at a time; many hold sprays of <b>areca flowers</b>.',
  'Parts of the <b>Siri pāḍdana</b> are sung in a solemn ritual style. Women enter trance and are possessed by Siri, Sonne, Abbaga and Dāraga: this is <b>darśana</b> (the festival is also called <b>dayyol</b>).',
  'A man in the part of <b>Kumāra</b> goes among them, asking each who she is, and acts as mediator between the possessed women and the people, and as a healer.',
  'Through the night the women dance, speak and are heard; at dawn they come out of trance and go home.'],
 [('z','Is it frightening?'),('b','People who have been there describe it as intense, not frightening: grief let out, and answered.')],'One night when <b>the women are heard</b>.')
kumara=reading('kumara','KUMĀRA','The only man in the rite',
 S('A man in white speaking gently with women in trance holding areca flowers','<rect width="560" height="200" fill="#20243a"/>'+g(280,190,1.3,person('#f4f1ea'))+''.join(g(120+k*80,190,1.1,woman(['#c0392b','#e0a800','#2a9d6f','#6a3d9a','#1d4f8a'][k])) for k in [0,1,3,4]),'#20243a',200),
 ['<b>Siri’s son.</b> In the story Kumāra is the son Siri lost on the road to Bola. In the rite, a man takes his part.',
  '<b>The question.</b> He goes from woman to woman asking, again and again, <i>“Tell me who you are?”</i> Each names which of Siri’s family has come to her.',
  '<b>Mediator.</b> He speaks for the people to the possessed women and for them to the people; he is also a healer.',
  '<b>The only man.</b> He is the only male character from the legend in the rite; everything else belongs to women.',
  '<b>A son returned.</b> Each year the lost son comes back to his mother’s festival. (Interpretation.)'],
 [('z','Why ask “who are you?”'),('b','Because naming is the heart of it. A woman who arrived as someone’s troubled wife or daughter answers as Siri.')],'The lost son <b>who asks the question</b>.')
song=reading('paddana','THE SIRI PĀḌDANA','The longest poem in Tuḷu',
 S('Women transplanting paddy in a flooded field, singing',''.join(g(60+k*80,180,1,person(['#c0392b','#e0a800','#2a9d6f','#6a3d9a','#1d4f8a','#ff8c1a'][k])) for k in range(6))+'<rect y="170" width="560" height="30" fill="#4aa3df" opacity=".7"/>'+''.join(g(40+k*36,176,.6,'<path d="M0 0 q-4 -16 2 -24 M0 0 q6 -14 2 -22" fill="none" stroke="#2f7a3a" stroke-width="3"/>') for k in range(15)),'#d8efc8',200),
 ['<b>Its size.</b> The Siri pāḍdana, also called Siri Sandhi, runs to <b>15,683 lines</b>, the longest poem in Tuḷu; a full recitation takes about 25 hours.',
  '<b>Sung in the fields.</b> Women traditionally sang it while transplanting paddy, verse by verse, through the long days of the monsoon planting.',
  '<b>The great recording.</b> The best-known version was sung by <b>Gōpāla Nāyka</b> and published with an English translation by the folklorist Lauri Honko and colleagues in 1998.',
  '<b>Kargi.</b> The pāḍdana singer Kargi, who received Siri’s darśana all her life, died on the full-moon night of the Hiriyaḍka Siri Jātre in 1994. Newspapers called her “the queen of pāḍdana singers”.',
  '<b>At the jātre.</b> Parts of the song are sung through the festival night; the whole epic lives spread across a community.'],
 [('z','Twenty-five hours of singing?'),('b','Nobody sings it all at once. Women sing parts in the fields; singers recite parts at the jātre.')],'An epic <b>kept by women in the fields</b>.')
why=reading('meaning','WHAT IT MEANS','Readings of the Siri Jātre',
 S('A woman standing tall with areca flowers, others behind her',g(280,190,1.6,woman('#c0392b'))+''.join(g(120+k*80,190,1,woman(['#e0a800','#2a9d6f','#6a3d9a','#1d4f8a','#ff8c1a'][k],False)) for k in [0,1,3,4]),'#f6e3e1',200),
 ['<b>A heroine.</b> Siri refused a soiled gift, refused a bribed judgement, and walked away. Many women of the coast see in her a model of dignity.',
  '<b>What women say.</b> Women interviewed at Hiriyaḍka describe the jātre as the most cherished experience of their lives; many come every year without fail.',
  '<b>What scholars say.</b> Researchers describe the rite as a space where women in hard circumstances, such as late or failed marriages or childlessness, find release, recognition and healing, and some read it as a challenge to male-dominated norms. Others ask how far the rite changes women’s lives outside the night.',
  '<b>Across lines.</b> Women of many castes and communities take part; for a night, a woman of any background may speak as a revered daiva. (Scholars note this reversal.)',
  '<b>Her promise.</b> For believers it is simply Siri keeping the promise she made before she died: blessing and healing for all who call on her.'],
 [('z','So is it healing or protest?'),('b','Ask ten scholars and you get ten answers. Ask the women and most say: she comes, and we are lighter.')],'Dignity, release <b>and a promise kept</b>.')
endp=end(i,['<b>Siri.</b> Born of areca flowers, she refused an insult and a bribed ruling, and walked away.','<b>Family.</b> Kumāra, Sonne, and the twins Abbaga and Dāraga, all honoured as daivas.','<b>Shrines.</b> The Ādi Āḷade: Hiriyaḍka, Paṅgāla, Nandaḷike, Kavatār, Nidgal.','<b>Night.</b> Women in darśana, areca flowers, Kumāra’s question.','<b>Song.</b> The 15,683-line pāḍdana, kept in the paddy fields.'],
 'This is the last part. Back to the '+L('/tulunadu/festivals/','Festivals of Tulu Nadu')+', or read Siri’s full guide in '+L('/tulunadu/daiva/siri/','Siri')+'.','The night the women speak as Siri')
src=sources([('Siri:','Our '+L('/tulunadu/daiva/siri/','Siri')+' guide (story, shrines, jātre, pāḍdana, Kargi); Deccan Herald, “Seeking empowerment through Siri” (centres including Kavatār, Hiriyaḍka, Dalyottu, Paṅgāla, Nidgal; areca flowers; women’s accounts); Yogitha Shetty, Rupkatha Journal (Siri pāḍdana and the ritual, reversal of hierarchy); TalkingMyths (Kumāra’s question; full-moon timing); an article in a SAGE journal on the Siri ritual and healing.')],
 'the month of the jātre at each centre (one source gives Paggu, glossed as February, which does not match the Tuḷu calendar); the list of great centres varies between sources; Kumāra’s survival or death varies between tellings.','Story as in the Siri pāḍdana as summarised in our guide.')
finish(i,'PART 9 OF 9 · SIRI · DARŚANA · THE SONG',covart('Women with areca flowers dancing under a full moon before a shrine','<rect width="440" height="196" fill="#20243a"/>'+g(380,40,1,moon())+g(70,186,.8,tulu_temple())+''.join(g(160+k*56,190,1.1,woman(['#c0392b','#e0a800','#2a9d6f','#6a3d9a','#1d4f8a'][k])) for k in range(5))),'The night the women speak as Siri',
 'The <b>Siri Jātre</b>: Siri’s story in four parts, her shrines, the full-moon night of <b>darśana</b>, Kumāra’s question, the <b>Siri pāḍdana</b>, and what it means.',
 'Siri Jātre explained and illustrated: Siri born of areca flowers, the refused sari, the bribed elders and the road to Bola, Sonne and the twins Abbaga and Dāraga, the Ādi Āḷade shrines, the night of darśana, Kumāra, the Siri pāḍdana and its meaning.',
 [fw,gl,country,born,insult,fire_,twins,night,kumara,song,why,endp,src])
