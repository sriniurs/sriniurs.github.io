import json, os, urllib.request, urllib.parse, urllib.error, datetime
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
d = (datetime.datetime.now(IST) - datetime.timedelta(days=1)).date()
tok = os.environ.get("GC_TOKEN", "").strip()
A = "https://sriniurs.goatcounter.com/api/v0"
def utc(day, end=False):
    t = datetime.datetime.combine(day, datetime.time(23, 59, 59) if end else datetime.time(0, 0), IST)
    return t.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def get(path, **q):
    url = A + path + ("?" + urllib.parse.urlencode(q) if q else "")
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:500]
        print(f"ERROR {e.code} on {path}: {body}")
        return {"error": e.code, "body": body}
    except Exception as e:
        print(f"ERROR on {path}: {e}")
        return {"error": str(e)}
print("token present:", bool(tok), "length:", len(tok))
s, e = utc(d), utc(d, True)
first = datetime.date(2026, 11, 2)
out = {"date": str(d),
       "total": get("/stats/total", start=s, end=e),
       "day_hits": get("/stats/hits", start=s, end=e, limit=50),
       "all_time_hits": get("/stats/hits", start=utc(first), end=e, limit=100),
       "referrers": get("/stats/toprefs", start=s, end=e)}
os.makedirs("stats", exist_ok=True)
for f in (f"stats/{d}.json", "stats/latest.json"):
    json.dump(out, open(f, "w"), indent=1)
print(json.dumps(out)[:1500])
