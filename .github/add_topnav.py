"""Add the approved top + bottom navigation (Srini, 4 Nov 2026) to a site page.

Usage:
  python3 .github/add_topnav.py slug/index.html            # a story page
  python3 .github/add_topnav.py index.html --latest /slug/

- Slim strip above the cover: "📚 Past stories" + a red-dot pill.
- Same two buttons (bigger) at the end of the page, replacing the old
  '<p class="foot"><a href="/archive/">…' line if present.
- A tiny script reads <meta name="latest-story"> from the live front page:
  on the latest story the pill says "🔴 Latest story" (muted, not a link);
  on any older page it turns red: "🔴 New story today →" linking to "/".
  So old pages never need editing again.
Safe to run twice (it replaces its own earlier blocks).
"""
import re, sys

CSS = '''<style id="topnav">
.topnav{display:flex;justify-content:space-between;align-items:center;gap:10px;max-width:1000px;margin:0 auto -12px;font-family:var(--body);font-weight:800;font-size:14.5px;line-height:1}
.topnav a,.topnav span,.botnav a,.botnav span{display:inline-flex;align-items:center;gap:6px;padding:7px 13px;border:2.5px solid var(--line);border-radius:999px;background:var(--panel);color:var(--ink);text-decoration:none;box-shadow:2px 2px 0 var(--line);white-space:nowrap}
.botnav{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin:22px auto 6px;font-family:var(--body);font-weight:800;font-size:16px;line-height:1}
.botnav a,.botnav span{padding:10px 16px;box-shadow:3px 3px 0 var(--line)}
.topnav .new,.botnav .new{background:#d62828;color:#fff;border-color:#151515;box-shadow:2px 2px 0 #151515}
.topnav .here,.botnav .here{box-shadow:none;opacity:.75}
</style>'''

JS = '''<script id="topnav-js">(function(){var n=function(x){return x.replace(/index\.html$/,'').replace(/\/$/,'')||'/';};var p=n(location.pathname);
function set(latest){document.querySelectorAll('.js-latest').forEach(function(a){if(latest){a.className='js-latest here';a.textContent='\\u{1F534} Latest story';a.removeAttribute('href');}else{a.className='js-latest new';a.textContent='\\u{1F534} New story today \\u2192';a.setAttribute('href','/');}});}
if(p==='/'){set(true);return;}
fetch('/',{cache:'no-store'}).then(function(r){return r.text();}).then(function(t){var m=t.match(/<meta name="latest-story" content="([^"]+)"/);if(m)set(n(m[1])===p);}).catch(function(){});})();</script>'''

TOP = '<nav class="topnav"><a href="/archive/">\U0001F4DA Past stories</a><a class="js-latest" href="/">\U0001F534 Latest story \u2192</a></nav>\n'
BOT = '<nav class="botnav"><a href="/archive/">\U0001F4DA Past stories</a><a class="js-latest" href="/">\U0001F534 Latest story \u2192</a></nav>\n'

path = sys.argv[1]
latest = sys.argv[sys.argv.index('--latest') + 1] if '--latest' in sys.argv else None
s = open(path, encoding='utf-8').read()

# remove earlier copies
s = re.sub(r'<style id="topnav">.*?</style>', '', s, flags=re.S)
s = re.sub(r'<script id="topnav-js">.*?</script>', '', s, flags=re.S)
s = re.sub(r'<nav class="(?:topnav|botnav)">.*?</nav>\n?', '', s, flags=re.S)
s = re.sub(r'<p class="foot"><a href="/archive/">.*?</p>\n?', '', s, flags=re.S)
s = re.sub(r'<meta name="latest-story"[^>]*>', '', s)

s = s.replace('</head>', CSS + '</head>', 1)
m = re.search(r'<header class="cover', s)
if not m:
    sys.exit('no <header class="cover"> found in ' + path)
s = s[:m.start()] + TOP + s[m.start():]
i = s.rindex('</main>')
s = s[:i] + BOT + s[i:]
j = s.rindex('</body>')
s = s[:j] + JS + s[j:]
if latest:
    s = s.replace('</title>', '</title><meta name="latest-story" content="%s">' % latest, 1)
open(path, 'w', encoding='utf-8').write(s)
print('topnav added to', path, '(latest=%s)' % latest if latest else '')
