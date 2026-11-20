#!/bin/bash
# Install the srini.presents Bhakti builder kit into a working folder.
# usage: bash tools/bhakti-kit/setup.sh [WORK_DIR]   (default /home/claude/work)
set -e
KIT="$(cd "$(dirname "$0")" && pwd)"
WORK="${1:-/home/claude/work}"
CHECK="$(dirname "$WORK")/check.py"
mkdir -p "$WORK"
cp -r "$KIT/work/." "$WORK/"
find "$WORK" -name '*.html.tmpl' | while read f; do mv "$f" "${f%.tmpl}"; done
cp "$KIT/check.py" "$CHECK"
if [ "$WORK" != "/home/claude/work" ]; then
  find "$WORK" -name '*.py' -o -name '*.sh' | xargs sed -i "s#/home/claude/work#$WORK#g; s#/home/claude/check.py#$CHECK#g"
  sed -i "s#/home/claude/work#$WORK#g" "$CHECK"
fi
REPO="$(cd "$KIT/../.." && pwd)"
if [ "$REPO" != "/home/claude/sriniurs.github.io" ]; then
  find "$WORK" -name '*.py' | xargs sed -i "s#/home/claude/sriniurs.github.io#$REPO#g"
fi
echo "Bhakti kit installed in $WORK (check script: $CHECK, repo: $REPO)"
