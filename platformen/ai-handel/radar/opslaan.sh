#!/usr/bin/env bash
# Zet de meetdata van de kansenradar op de tak ai-handel-data, in de map radar/ (de scanner en de schaduwbot
# gebruiken dezelfde tak, maar een andere map). Maakt daar ook radar/rapport.md opnieuw en zet de nieuwste lijst
# met munten per beurs in radar/paren-laatst.json (de volgende run vergelijkt daarmee, zodat een notering tussen
# twee runs niet verloren gaat).
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
  mkdir -p "$W/radar"
  cp -r "$BRON"/. "$W/radar/"
  # nieuwste lijst met munten (van een vaste run, niet van een proef) naar radar/paren-laatst.json
  LAATST="$(ls -t "$BRON"/*/run-*/paren-laatst.json 2>/dev/null | grep -v -- '-proef/' | head -1)"
  [ -n "$LAATST" ] && cp "$LAATST" "$W/radar/paren-laatst.json"
  if python3 -I "$HIER/radar_rapport.py" "$W/radar" > "$W/rapport.tmp" && [ -s "$W/rapport.tmp" ]; then
    mv "$W/rapport.tmp" "$W/radar/rapport.md"
  else
    echo "rapport mislukt (data wel bewaard, vorig rapport blijft staan)"; rm -f "$W/rapport.tmp"
  fi
  git -C "$W" add radar
  if git -C "$W" diff --cached --quiet; then echo "niets nieuw"; rm -rf "$W"; exit 0; fi
  git -C "$W" -c user.name="dortus-radar" -c user.email="41898282+github-actions[bot]@users.noreply.github.com" \
    commit -q -m "Radar: meetdata $(date -u +%Y-%m-%dT%H:%MZ)"
  if git -C "$W" push -q origin "HEAD:refs/heads/$TAK"; then
    echo "opgeslagen op $TAK (poging $poging)"; rm -rf "$W"; exit 0
  fi
  rm -rf "$W"
  sleep $((poging * 3 + RANDOM % 5))
done
echo "opslaan mislukt na 5 pogingen"
exit 1
