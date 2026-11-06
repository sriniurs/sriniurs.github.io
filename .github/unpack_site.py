"""Unpack site-update*.zip files uploaded to the repo root into their real paths.

Used when a scheduled task can't push: it sends Srini one zip, he uploads it at
https://github.com/sriniurs/sriniurs.github.io/upload/main, and this script puts
every file where it belongs. archive/index.html is MERGED (new entries go below
the marker), never overwritten, so two updates on the same day can't clash.

QUEUE (Srini, 6 Nov 2026): zips can be uploaded days early. A story's line in the zip's
archive/index.html is NOT added straight away; it goes into queue/<slug>.json with its date,
and .github/publish_due.py adds it to Past stories and makes it the front page on that date
(India time). A root index.html / og.png inside a zip is ignored: the front page is always
built by publish_due.py from the newest due story. Lines for non-story pages (e.g. /markets/)
or without a date are still merged at once, as before.
"""
import datetime, glob, json, os, re, sys, zipfile

MARK = "<!-- NEWEST ENTRY GOES DIRECTLY BELOW THIS LINE -->"
ALLOWED = re.compile(r"^(index\.html|og\.png|(archive|markets|funds|nifty|ortho-pulse)/[A-Za-z0-9._-]+\.(html|png|jpg|json))$")
# short story links (from 5 Nov 2026): /<slug>/index.html + /<slug>/og.png
STORY = re.compile(r"^(?!archive/|assets/|preview/|stats/|comics/|queue/)[a-z0-9][a-z0-9-]{1,40}/(index\.html|og\.png|card\.jpg|story\.jpg)$")
QUEUE = re.compile(r"^queue/[a-z0-9][a-z0-9-]{1,40}\.json$")
RESERVED = {"archive","assets","preview","stats","comics","markets","funds","nifty","ortho-pulse","s","queue"}
MONTHS = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}
STATUS = re.compile(r"^s/[a-z0-9][a-z0-9-]{1,40}/index\.html$")

def merge_archive(new_html):
    path = "archive/index.html"
    cur = open(path, encoding="utf-8").read()
    have = set(re.findall(r'<li><a href="([^"]+)"', cur))
    add, queued = [], []
    for l in new_html.splitlines():
        l = l.strip()
        if not l.startswith("<li><a href="):
            continue
        href = re.search(r'href="([^"]+)"', l).group(1)
        if href in have:
            continue
        m = re.match(r"^/([a-z0-9][a-z0-9-]{1,40})/$", href)
        d = re.search(r"<span>(\d{1,2}) ([A-Z][a-z]{2}) (\d{4})", l)
        if m and m.group(1) not in RESERVED and d and d.group(2) in MONTHS:
            slug = m.group(1)
            date = datetime.date(int(d.group(3)), MONTHS[d.group(2)], int(d.group(1))).isoformat()
            os.makedirs("queue", exist_ok=True)
            json.dump({"slug": slug, "date": date, "href": href, "line": l},
                      open(f"queue/{slug}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            queued.append(f"{date} {slug}")
        else:
            add.append(l)
    if add and MARK in cur:
        cur = cur.replace(MARK, MARK + "\n" + "\n".join(add), 1)
        open(path, "w", encoding="utf-8").write(cur)
    print(f"archive: added {len(add)} now, queued {queued}")

zips = sorted(glob.glob("site-update*.zip"))
if not zips:
    print("no site-update zip found"); sys.exit(0)
for z in zips:
    print("unpacking", z)
    with zipfile.ZipFile(z) as zf:
        for info in zf.infolist():
            name = info.filename.lstrip("./")
            if info.is_dir():
                continue
            if name in ("index.html", "og.png"):
                print("  skipped", name, "(front page is set by publish_due.py on the story's date)"); continue
            if not (ALLOWED.match(name) or STORY.match(name) or STATUS.match(name) or QUEUE.match(name)):
                print("  skipped (not an allowed site path):", name); continue
            data = zf.read(info)
            if name == "archive/index.html":
                merge_archive(data.decode("utf-8")); continue
            os.makedirs(os.path.dirname(name) or ".", exist_ok=True)
            open(name, "wb").write(data)
            print("  wrote", name)
    os.remove(z)
