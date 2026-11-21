import re,sys
REP=[
(r' Some modern linguists have suggested a Dravidian root, ān-manti, “male monkey”, Sanskritised into Hanumān; this remains a scholarly guess, not tradition\.',''),
('Jain authors rejected the idea of a talking vānara army','Jain authors rejected the idea of an army of animals'),
('a vidyādhara prince, not a monkey','a vidyādhara prince of a royal clan whose banner bore a vānara'),
('Kapi, monkey;','Kapi, another word for the vānaras;'),
('she-monkey','vānarī'),
('Is he a monkey or a god?','Is he a vānara or a god?'),
('the prince embracing the monkey','the prince embracing his vānara servant'),
('O Monkey','O Kapi'),
('lord of the monkeys','lord of the vānaras'),('lord of monkeys','lord of the vānaras'),
('leader of monkey troops','leader of the vānara hosts'),
('hero (śūra) among monkeys','hero (śūra) among the vānaras'),('among monkeys','among the vānaras'),
('monkeys besieged the jail','an army of vānaras besieged the jail'),
('ring of small monkeys','ring of small vānaras'),
('Hanumān banner','Hanumān banner'),('Arjuna’s monkey','Arjuna’s Hanumān'),
("And monkeys watching every one of them.","And pilgrims chanting on every one of them."),
('Monkey people','The vānaras, the forest people of the Rāmāyaṇa'),
('monkey people','vānara people'),
]
GEN=[(r'\b([Mm])onkeys\b',lambda m:('V' if m.group(1)=='M' else 'v')+'ānaras'),(r'\b([Mm])onkey\b',lambda m:('V' if m.group(1)=='M' else 'v')+'ānara')]
KEEP=['Monkeys on Jakhu','famous for its bold monkeys','def MONKEY','MONKEY(']
for f in sys.argv[1:]:
    s=open(f).read(); o=s
    for a,b in REP: s=re.sub(a,b,s) if a.startswith(' Some') else s.replace(a,b)
    out=[]
    for line in s.split('\n'):
        if any(k in line for k in KEEP) and not ('monkey' in line.lower().replace('monkeys on jakhu','').replace('bold monkeys','').replace('monkey(','')): out.append(line); continue
        segs=re.split(r'(Monkeys on Jakhu|bold monkeys|def MONKEY|MONKEY\()',line)
        segs=[x if x in ('Monkeys on Jakhu','bold monkeys','def MONKEY','MONKEY(') else re.sub(GEN[0][0],GEN[0][1],re.sub(GEN[1][0],GEN[1][1],re.sub(GEN[0][0],GEN[0][1],x))) for x in segs]
        out.append(''.join(segs))
    s='\n'.join(out)
    if s!=o: open(f,'w').write(s); print('fixed',f)
