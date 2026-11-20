#!/usr/bin/env python3
"""Tell Bing, Yandex and other IndexNow engines about changed public pages.

Usage: indexnow.py <git-revision-range or --since=ISO-time> | --all
Maps changed */index.html files to their srinipresents.com URLs and POSTs them.
"""
import json, re, subprocess, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = 'srinipresents.com'
KEY = 'fcbb8aadcc140fcc6786d7f515d592f4'
SKIP = ('queue/', 'preview/', 'stats/', 'assets/', 's/', 'pagefind/')

def sitemap_urls():
    return re.findall(r'<loc>([^<]+)</loc>', (ROOT / 'sitemap.xml').read_text())

def changed_files(arg):
    if arg.startswith('--since='):
        cmd = ['git', 'log', f'--since={arg[8:]}', '--name-only', '--pretty=format:']
    else:
        cmd = ['git', 'diff', '--name-only', arg]
    out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return {l.strip() for l in out.splitlines() if l.strip()}

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else '--since=26 hours ago'
    known = set(sitemap_urls())
    if arg == '--all':
        urls = sorted(known)
    else:
        urls = set()
        for f in changed_files(arg):
            if not f.endswith('index.html') or f.startswith(SKIP):
                continue
            path = f[:-len('index.html')]
            url = f'https://{HOST}/{path}'
            if url in known and (ROOT / f).exists():
                urls.add(url)
        urls = sorted(urls)
    if not urls:
        print('IndexNow: nothing to submit'); return
    body = json.dumps({'host': HOST, 'key': KEY,
                       'keyLocation': f'https://{HOST}/{KEY}.txt',
                       'urlList': urls[:10000]}).encode()
    req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body,
                                 headers={'Content-Type': 'application/json; charset=utf-8'})
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f'IndexNow: HTTP {r.status} for {len(urls)} URL(s)')
    for u in urls: print('  ', u)

if __name__ == '__main__':
    main()
