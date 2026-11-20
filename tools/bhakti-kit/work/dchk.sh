#!/bin/bash
# usage: dchk.sh builder.py out.html  (run in devim)
cd /home/claude/work/devim && python3 $1 && python3 /home/claude/check.py $PWD/$2 | tail -1 && python3 -c "
import pypdf;print('pdf',len(pypdf.PdfReader('/home/claude/work/out.pdf').pages))" && grep -c '<section class="page' $2 && cd .. && rm -f c-*.png && pdftoppm -r 40 -png out.pdf c && python3 -c "
from PIL import Image;import glob
f=sorted(glob.glob('c-*.png'));ims=[Image.open(x) for x in f];w,h=ims[0].size;n=7
s=Image.new('RGB',(w*n,h*((len(ims)+n-1)//n)),'white')
for i,im in enumerate(ims):s.paste(im,((i%n)*w,(i//n)*h))
s.save('sheet.png')"
python3 -c "
import pypdf;r=pypdf.PdfReader('/home/claude/work/out.pdf')
for i,p in enumerate(r.pages):
  t=(p.extract_text() or '').strip()
  if t.startswith('⚡') or len(t)<60: print('OVERFLOW? page',i+1,t[:60])"
