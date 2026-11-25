#!/bin/bash
# usage: tchk.sh outdir root slug...
OUTD=$1; ROOT=$2; shift 2
(curl -s -o /dev/null localhost:8765/ || (cd /home/claude/srv && nohup python3 -m http.server 8765 >/dev/null 2>&1 &)); sleep 1
for s in "$@"; do mkdir -p /home/claude/srv/$ROOT; rm -rf /home/claude/srv/$ROOT/$s; cp -r $OUTD/$ROOT/$s /home/claude/srv/$ROOT/; done
python3 chk.py $ROOT "$@"
for s in "$@"; do python3 - "$s" <<'P'
import pypdf,sys,re
s=sys.argv[1]; r=pypdf.PdfReader(f'/tmp/{s}.pdf')
prev=None
for i,p in enumerate(r.pages):
    t=p.extract_text()[:40].replace('\n',' ')
    if not re.match(r'\s*[A-ZĀĪŪṚṆṢŚḌṬḶ0-9 ·&’\'\-:,]{4,}',t): print('  spill? page',i+1,repr(t))
P
done
