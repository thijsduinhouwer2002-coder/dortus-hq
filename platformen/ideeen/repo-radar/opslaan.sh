#!/usr/bin/env bash
# Zet de uitkomst van de repo-radar op de tak ideeen-data, in de map repo-radar/ (niet op main).
#   repo-radar/<datum>/rapport.md en kandidaten.json   uitkomst van die dag (een tweede run die dag overschrijft)
#   repo-radar/rapport.md                               het nieuwste rapport (om snel te lezen)
#   repo-radar/gezien.json                              welke repo's al eens in de top stonden, en wanneer
# Nooit geforceerd: lukt de push niet (een ander was net eerder), dan opnieuw ophalen en opnieuw proberen.
# Naar het voorbeeld van platformen/ai-handel/scanner/opslaan.sh.
# Gebruik (in de workflow):  bash opslaan.sh <map met <datum>/ en gezien.json>   nodig: GH_TOKEN, GITHUB_REPOSITORY
set -u
BRON="$1"
TAK=ideeen-data
URL="https://x-access-token:${GH_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
[ -d "$BRON" ] || { echo "geen data in $BRON"; exit 0; }
DAG="$(ls -1 "$BRON" | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' | sort | tail -1)"
[ -n "$DAG" ] && [ -s "$BRON/$DAG/rapport.md" ] || { echo "geen rapport in $BRON"; exit 1; }
for poging in 1 2 3 4 5; do
  W="$(mktemp -d)"
  if git ls-remote --exit-code "$URL" "refs/heads/$TAK" >/dev/null 2>&1; then
    git clone -q --depth 1 --branch "$TAK" --single-branch "$URL" "$W" || { rm -rf "$W"; sleep 5; continue; }
  else
    git -C "$W" init -q -b "$TAK" && git -C "$W" remote add origin "$URL"
  fi
  mkdir -p "$W/repo-radar/$DAG"
  cp "$BRON/$DAG"/* "$W/repo-radar/$DAG/"
  cp "$BRON/$DAG/rapport.md" "$W/repo-radar/rapport.md"
  [ -s "$BRON/gezien.json" ] && cp "$BRON/gezien.json" "$W/repo-radar/gezien.json"
  git -C "$W" add repo-radar
  if git -C "$W" diff --cached --quiet; then echo "niets nieuw"; rm -rf "$W"; exit 0; fi
  git -C "$W" -c user.name="dortus-repo-radar" -c user.email="41898282+github-actions[bot]@users.noreply.github.com" \
    commit -q -m "Repo-radar: rapport $DAG ($(date -u +%H:%MZ))"
  if git -C "$W" push -q origin "HEAD:refs/heads/$TAK"; then
    echo "opgeslagen op $TAK (poging $poging)"; rm -rf "$W"; exit 0
  fi
  rm -rf "$W"
  sleep $((poging * 3 + RANDOM % 5))
done
echo "opslaan mislukt na 5 pogingen"
exit 1
