#!/usr/bin/env bash
# Zet de meetdata van de scanner op de tak ai-handel-data, in de map scanner/ (de schaduwbot gebruikt dezelfde
# tak, maar een andere map). Maakt daar ook scanner/rapport.md opnieuw.
# Nooit geforceerd: lukt de push niet (een ander was net eerder), dan opnieuw ophalen en opnieuw proberen.
# Gebruik (in de workflow):  bash opslaan.sh <map met <datum>/<run>/...>     nodig: GH_TOKEN, GITHUB_REPOSITORY
set -u
BRON="$1"
TAK=ai-handel-data
URL="https://x-access-token:${GH_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
HIER="$(cd "$(dirname "$0")" && pwd)"
[ -d "$BRON" ] || { echo "geen data in $BRON"; exit 0; }
for poging in 1 2 3 4 5; do
  W="$(mktemp -d)"
  if git ls-remote --exit-code "$URL" "refs/heads/$TAK" >/dev/null 2>&1; then
    git clone -q --depth 1 --branch "$TAK" --single-branch "$URL" "$W" || { rm -rf "$W"; sleep 5; continue; }
  else
    git -C "$W" init -q -b "$TAK" && git -C "$W" remote add origin "$URL"
  fi
  mkdir -p "$W/scanner"
  cp -r "$BRON"/. "$W/scanner/"
  python3 -I "$HIER/rapport.py" "$W/scanner" > "$W/scanner/rapport.md" || echo "rapport mislukt (data wel bewaard)"
  git -C "$W" add scanner
  if git -C "$W" diff --cached --quiet; then echo "niets nieuw"; rm -rf "$W"; exit 0; fi
  git -C "$W" -c user.name="dortus-scanner" -c user.email="41898282+github-actions[bot]@users.noreply.github.com" \
    commit -q -m "Scanner: meetdata $(date -u +%Y-%m-%dT%H:%MZ)"
  if git -C "$W" push -q origin "HEAD:refs/heads/$TAK"; then
    echo "opgeslagen op $TAK (poging $poging)"; rm -rf "$W"; exit 0
  fi
  rm -rf "$W"
  sleep $((poging * 3 + RANDOM % 5))
done
echo "opslaan mislukt na 5 pogingen"
exit 1
