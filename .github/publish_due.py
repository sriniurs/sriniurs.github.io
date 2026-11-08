"""Publish queued stories on their day (Srini, 6 Nov 2026).

Each story waits in queue/<slug>.json:
  {"slug": "green-crackers", "date": "2026-11-09", "href": "/green-crackers/",
   "line": "<li><a href=\"/green-crackers/\">Title</a><span>9 Nov 2026 · Theme · shape</span></li>"}
The story page itself (/<slug>/index.html, og.png, s/<slug>/) is uploaded whenever it is ready,
so its own link works at once. The scheduled queue check runs at 4:30 am IST on its date. Then:
  1. its line is added to Past stories (archive/index.html), newest on top;
  2. the front page (index.html + og.png) becomes a copy of the newest story that is due.
Safe to run any number of times. Run by .github/workflows/publish.yml at 4:30 am IST,
and again after every zip upload (so a story uploaded on its own day goes live straight away).
Usage: python3 .github/publish_due.py [--today YYYY-MM-DD]   (--today is only for testing)
"""
import datetime, glob, json, os, re, sys

MARK = "<!-- NEWEST ENTRY GOES DIRECTLY BELOW THIS LINE -->"
SITE = "https://sriniurs.github.io"

if "--today" in sys.argv:
    today = datetime.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1])
else:
    # Publish the current Indian calendar date, including the 04:30 and 04:45 IST runs.
    today = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)).date()

items = []
for p in sorted(glob.glob("queue/*.json")):
    try:
        it = json.load(open(p, encoding="utf-8"))
        it["_date"] = datetime.date.fromisoformat(it["date"])
        items.append(it)
    except Exception as e:
        print("bad queue file", p, e)

due = [i for i in items if i["_date"] <= today and os.path.exists(f'{i["slug"]}/index.html')]
waiting = [i for i in items if i["_date"] > today]
due.sort(key=lambda i: (i["_date"], i["slug"]))
print(f"today (IST) {today}: {len(due)} due, {len(waiting)} waiting",
      [f'{i["date"]} {i["slug"]}' for i in sorted(waiting, key=lambda i: i["_date"])])
if not due:
    sys.exit(0)

# 1. Past stories
path = "archive/index.html"
arch = open(path, encoding="utf-8").read()
have = set(re.findall(r'<li><a href="([^"]+)"', arch))
new = [i for i in due if i["href"] not in have]
if new and MARK in arch:
    new.sort(key=lambda i: (i["_date"], i["slug"]), reverse=True)
    arch = arch.replace(MARK, MARK + "\n" + "\n".join(i["line"] for i in new), 1)
    open(path, "w", encoding="utf-8").write(arch)
    print("Past stories: added", [i["slug"] for i in new])

# 2. Front page = newest due story
top = due[-1]
slug, ymd = top["slug"], top["date"].replace("-", "")
s = open(f"{slug}/index.html", encoding="utf-8").read()
s = re.sub(r'<meta property="og:image" content="[^"]*">',
           f'<meta property="og:image" content="{SITE}/og.png?v={ymd}">', s, count=1)
s = re.sub(r'<meta property="og:url" content="[^"]*">',
           f'<meta property="og:url" content="{SITE}/">', s, count=1)
s = re.sub(r'<meta name="latest-story"[^>]*>', '', s)
s = s.replace("</title>", f'</title><meta name="latest-story" content="/{slug}/">', 1)
old = open("index.html", encoding="utf-8").read() if os.path.exists("index.html") else ""
if s != old:
    open("index.html", "w", encoding="utf-8").write(s)
    print("front page ->", slug)
if os.path.exists(f"{slug}/og.png"):
    b = open(f"{slug}/og.png", "rb").read()
    if not os.path.exists("og.png") or open("og.png", "rb").read() != b:
        open("og.png", "wb").write(b)
        print("og.png ->", slug)
