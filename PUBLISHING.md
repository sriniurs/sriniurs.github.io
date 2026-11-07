# Daily article queue

The homepage features one queued article per day, in ascending number order, at 05:00 Asia/Kolkata, starting 8 November 2026.

The Codex chat automation “Publish Srini’s next article” owns this task. Do not create a second publisher. The scheduler starts at 05:00; committing and GitHub Pages deployment take additional time. Local scheduled tasks need the computer awake and Codex running.

## Adding articles

Upload the finished article to its own URL, then tell this chat its URL and queue number. Add a corresponding pending entry to publishing-queue.json after inspecting the actual article. Numbers must be unique positive integers. card_html is the complete matching story-card HTML, including its publication date. not_before prevents early release. Preserve existing numbers and completed publication records. Do not add pending cards to either collection page early.

## Each morning

Read the live main branch and publishing-queue.json. Use Asia/Kolkata for the current date and time. Before 05:00 do nothing. If last_published_on is today, do nothing. If it is a later date, report a clock inconsistency and do nothing. Pick only the smallest-number pending entry: if its not_before is in the future, wait rather than skipping it. An empty queue leaves the current homepage unchanged.

Confirm its article exists, then read index.html and archive/index.html. Identify the direct article-source ul under .page, before the theme-groups-js script. Prepend its card_html to that source list in both pages. Never add it to the runtime generated lists. If the same canonical href already exists, move the existing card to the front instead of duplicating it, and update its date. Use the actual release date in the card when a run is delayed; do not backdate it. Preserve every other article, the hero, style, recent-seven behaviour, monthly archive and analytics.

Update the selected queue entry to published, record its published_at timestamp, and set last_published_on to today's IST date. Commit both collection pages and publishing-queue.json in one atomic commit to main using the GitHub connector create_tree/create_commit/update_ref operations, with the freshly read main commit as base and expected_sha. Never force-push. If main changes, reread before retrying. Verify the saved pages and queue after publishing. Only one card per local calendar day, including retries and delayed runs; never bulk catch up. Do not rewrite article content, or generate another article. Existing direct article links are public; this queue schedules homepage discovery, not access control.
