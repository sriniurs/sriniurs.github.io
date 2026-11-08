# Daily article queue

GitHub Actions owns daily publishing. The workflow is `.github/workflows/publish.yml`,
and `.github/publish_due.py` reads `publishing-queue.json`. The former local Codex
publisher is paused. No computer, open app, API key or local files are required.

The primary scheduled check is 05:00 Asia/Kolkata (23:30 UTC on the preceding date).
Hourly recovery checks run at minute 15. GitHub scheduling and Pages deployment can
be delayed; 05:00 is the target, not a guaranteed exact public-live time.

## Adding articles

Upload the finished article to `/<slug>/index.html`, inspect it, and add a pending
entry to `publishing-queue.json`. Numbers must be unique positive integers, ordered
by intended release. Each entry needs its URL, path, title, timezone-aware
`not_before`, status, `published_at` and complete matching `card_html`.
Preserve completed publication records. Insertions can renumber pending entries
when needed to preserve scheduled order. Update their data-queue-number values too.

Every new article must include exactly one GoatCounter script using
`data-goatcounter="https://sriniurs.goatcounter.com/count"` and
`src="https://gc.zgo.at/count.js"`, before its closing body tag. This ensures
visits through direct article links are counted as well as homepage visits.

Do not add pending cards to the homepage or archive early. Public repository files
and direct article URLs are public immediately: this queue schedules homepage
discovery, not private access. Private-until-release material must not be committed
to this public repository before its release time.

## Publishing behaviour

The script validates the queue, source lists and article files before editing.
Before 05:00 IST it does nothing. It also does nothing when today's release is
already recorded or the queue is empty. A future last_published_on is an error.
It considers only the smallest-number pending entry and respects not_before;
it never skips a future entry or publishes several stories to catch up.

It prepends the selected card to the direct `.page > ul` source list in both
`index.html` and `archive/index.html`, before `theme-groups-js`. Existing cards
with the same canonical link are replaced by one updated card at the front.
It preserves the hero, all other articles, scripts, styles and analytics.
Delayed runs use the actual release date, rather than backdating the card.

The queue's selected entry, published_at and last_published_on are updated with
both collection pages in one commit. The workflow never force-pushes or rebases
stale generated pages. A conflicting push fails safely, and the next check
recomputes from the latest main. It explicitly requests a Pages build because
GITHUB_TOKEN commits do not automatically trigger branch-based Pages builds.

The old `queue/*.json` files are historical and are no longer read by the
publisher. Zip-upload processing calls the same new publisher, so it observes
the same one-story-per-day and 05:00 IST rules.

## Checking and manual recovery

Open Actions → Publish today's story → Run workflow. Select dry_run for a
read-only preview; leave it unchecked to publish if a story is due. Repeated runs
cannot release a second queued story on the same IST calendar day. The run log
and summary report the selected story or why no change was needed.

Local preview: `python3 .github/publish_due.py --dry-run`.
Simulated dates are allowed only in dry-run mode. Unit tests cover early runs,
repeat runs, delays, queue order, duplicate links, missing files and preservation.
