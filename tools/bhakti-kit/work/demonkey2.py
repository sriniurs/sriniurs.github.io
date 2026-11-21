import sys
R=[('an army of vānaras and bears','an army of vānaras and bears'),('a vānara warrior bowing','a vānara warrior bowing'),('exiled vānara prince','exiled vānara prince'),
('The vānaras built','The vānaras built'),('Vānaras, a boatman','Vānaras, a boatman'),("('Vānara','The forest people who served Rāma')","('Vānara','The forest people who served Rāma')"),('<td>The forest people who served Rāma</td>','<td>The forest people who served Rāma</td>'),
('with vānaras serving them','with vānaras serving them'),('served by the vānaras','served by the vānaras'),('served by the vānaras','served by the vānaras'),('the vānara army of Hanumān','the vānara army of Hanumān'),
('the vānaras. The next','the vānaras. The next'),('a vulture, the vānaras.','a vulture, the vānaras.'),('a vānara army','a vānara army'),('Hanumān flying','Hanumān flying'),('Hanumān, sages','Hanumān, sages'),
('The Hanumān Banner','The Hanumān Banner'),('THE HANUMĀN BANNER','THE HANUMĀN BANNER'),('Hanumān banner','Hanumān banner'),('whose banner bears Hanumān','whose banner bears Hanumān'),('Hanumān-bannered','Hanumān-bannered'),
('Lord Of The Vānaras','Lord Of The Vānaras'),('LORD OF THE VĀNARAS','LORD OF THE VĀNARAS'),('Lord of the vānaras','Lord of the vānaras'),('the vānara army','the vānara army'),('vānara army','vānara army')]
for f in sys.argv[1:]:
    try: s=open(f).read()
    except Exception: continue
    o=s
    for a,b in R: s=s.replace(a,b)
    if s!=o: open(f,'w').write(s); print('fixed',f)
