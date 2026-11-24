# usage: sheet.sh slug
rm -f /tmp/c-*.png; pdftoppm -r 32 -png /tmp/$1.pdf /tmp/c; python3 -c "
from PIL import Image;import glob
f=sorted(glob.glob('/tmp/c-*.png'));ims=[Image.open(x) for x in f];w,h=ims[0].size;n=6
s=Image.new('RGB',(w*n,h*((len(ims)+n-1)//n)),'white')
for i,im in enumerate(ims):s.paste(im,((i%n)*w,(i//n)*h))
s.save('/home/claude/work/navaratri/sheet_$1.png')"
