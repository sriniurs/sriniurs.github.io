#!/usr/bin/env python3
"""Embed the srini.presents logo into a page as a data URI, for a sample or preview sent as a file.

usage: python3 tools/article-kit/embed_logo.py <in.html> [out.html]

Site pages keep the https://srinipresents.com/assets/brand/logo.png link (new_article.py puts it on
every cover). A file opened outside the site, or in an offline preview, may not load that link, so
run this on the copy you send. Writes to out.html (default: overwrites in.html).
"""
import base64, os, sys
KIT = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(KIT, '..', '..'))
src, out = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else sys.argv[1])
uri = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(REPO, 'assets/brand/logo.png'), 'rb').read()).decode()
s = open(src, encoding='utf-8').read()
n = 0
for url in ('https://srinipresents.com/assets/brand/logo.png', '/assets/brand/logo.png'):
    n += s.count(f'src="{url}"'); s = s.replace(f'src="{url}"', f'src="{uri}"')
open(out, 'w', encoding='utf-8').write(s)
print(f'embedded logo in {n} place(s) -> {out}')
