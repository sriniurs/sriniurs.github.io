"""Unpack site-update*.zip files uploaded to the repo root into their real paths.

Used when a scheduled task can't push: it sends Srini one zip, he uploads it at
https://github.com/sriniurs/sriniurs.github.io/upload/main, and this script puts
every file where it belongs. archive/index.html is MERGED (new entries go below
the marker), never overwritten, so two updates on the same day can't clash.
"""
import glob, os, re, sys, zipfile

MARK = "<!-- NEWEST ENTRY GOES DIRECTLY BELOW THIS LINE -->"
ALLOWED = re.compile(r"^(index\.html|og\.png|(archive|markets|funds|nifty|ortho-pulse)/[A-Za-z0-9._-]+\.(html|png|jpg|json))$")

def merge_archive(new_html):
    path = "archive/index.html"
    cur = open(path, encoding="utf-8").read()
    have = set(re.findall(r'<li><a href="([^"]+)"', cur))
    add = [l.strip() for l in new_html.splitlines()
           if l.strip().startswith("<li><a href=")
           and re.search(r'href="([^"]+)"', l).group(1) not in have]
    if add and MARK in cur:
        cur = cur.replace(MARK, MARK + "\n" + "\n".join(add), 1)
        open(path, "w", encoding="utf-8").write(cur)
    print(f"archive: added {len(add)} entr{'y' if len(add)==1 else 'ies'}")

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
            if not ALLOWED.match(name):
                print("  skipped (not an allowed site path):", name); continue
            data = zf.read(info)
            if name == "archive/index.html":
                merge_archive(data.decode("utf-8")); continue
            os.makedirs(os.path.dirname(name) or ".", exist_ok=True)
            open(name, "wb").write(data)
            print("  wrote", name)
    os.remove(z)
