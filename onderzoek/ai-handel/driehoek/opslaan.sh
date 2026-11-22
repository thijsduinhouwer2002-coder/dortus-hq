#!/usr/bin/env bash
# Zet de meetdata van de driehoek-meter op de tak ai-handel-data, in de map driehoek/ (scanner en schaduwbot
# gebruiken dezelfde tak, maar een andere map). Maakt daar ook driehoek/rapport.md opnieuw. Naar ../scanner/opslaan.sh.
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
  mkdir -p "$W/driehoek"
  cp -r "$BRON"/. "$W/driehoek/"
  # eerst naar een tijdelijk bestand: een mislukt rapport laat het vorige rapport.md staan (geen leeg bestand)
  if python3 -I "$HIER/rapport.py" "$W/driehoek" > "$W/rapport.tmp" && [ -s "$W/rapport.tmp" ]; then
    mv "$W/rapport.tmp" "$W/driehoek/rapport.md"
  else
    echo "rapport mislukt (data wel bewaard, vorig rapport blijft staan)"; rm -f "$W/rapport.tmp"
  fi
  git -C "$W" add driehoek
  if git -C "$W" diff --cached --quiet; then echo "niets nieuw"; rm -rf "$W"; exit 0; fi
  git -C "$W" -c user.name="dortus-driehoek" -c user.email="41898282+github-actions[bot]@users.noreply.github.com" \
    commit -q -m "Driehoek-meter: meetdata $(date -u +%Y-%m-%dT%H:%MZ)"
  if git -C "$W" push -q origin "HEAD:refs/heads/$TAK"; then
    echo "opgeslagen op $TAK (poging $poging)"; rm -rf "$W"; exit 0
  fi
  rm -rf "$W"
  sleep $((poging * 3 + RANDOM % 5))
done
echo "opslaan mislukt na 5 pogingen"
exit 1
