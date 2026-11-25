#!/bin/bash
# sheet.sh slug cols -> /tmp/sheet_<slug>.png
s=$1; c=${2:-6}; rm -f /tmp/cs_$s-*; pdftoppm -r 30 -png /tmp/$s.pdf /tmp/cs_$s
python3 -c "
from PIL import Image;import glob
fs=sorted(glob.glob('/tmp/cs_$s-*.png'));ims=[Image.open(f) for f in fs];w,h=ims[0].size;c=$c
S=Image.new('RGB',(w*c,h*((len(ims)+c-1)//c)),'white')
for k,im in enumerate(ims): S.paste(im,((k%c)*w,(k//c)*h))
S.save('/tmp/sheet_$s.png')"
