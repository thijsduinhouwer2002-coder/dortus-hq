#!/usr/bin/env bash
# Hulp voor de beeldvergelijking en de week-test (roestronde R4). Draait in GitHub Actions.
# Nodig: TOKEN (github.token met contents: write) en GITHUB_REPOSITORY.
#
#   beelden.sh haal <pad op tak schermen> <doelmap> [terugvalpad]
#       Haalt de referentiebeelden (laatste geslaagde run) op. Is er nog geen referentie, dan de beelden van
#       het terugvalpad (de laatste run, geslaagd of niet). Niets gevonden: lege doelmap, geen fout.
#   beelden.sh bewaar <bronmap> <pad op tak schermen> <omschrijving>
#       Zet de beelden van deze (geslaagde) run als nieuwe referentie op de tak schermen.
#   beelden.sh vergelijk <nu-map> <pad op tak schermen> <uitmap> <grens-procent> <naam> [terugvalpad] [maskers]
#       haal plus organisatie/controle/beeldvergelijk.py (Pillow en numpy in een eigen venv).
#   beelden.sh meld <product> <eigenaar> <map met beeldverschil-artefacten> <tak>
#       Eén kort bericht per run voor alle jobs samen (beeldbericht.py), alleen als dat verschil nog niet gemeld
#       is: de sleutel staat in referentie/<product>/<tak>/GEMELD.md op de tak schermen en wordt eerst daar
#       geclaimd (een push die botst = een andere run was eerder), pas daarna komt het bericht.
#   beelden.sh datum
#       Datum en tijd in Nederland voor de kop van een bericht, bijvoorbeeld "19 nov 2026 04:20".
#   beelden.sh bericht <naam> <tekstbestand>
#       Zet de tekst onderaan berichten/<naam>.md op de nieuwste main, controle, push, tot vijf pogingen.
set -u
HIER="$(cd "$(dirname "$0")" && pwd)"
URL="${BEELDEN_URL:-https://x-access-token:${TOKEN}@github.com/${GITHUB_REPOSITORY}.git}"
wie() {
  git config --global user.name "dortus-week-test"
  git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
}

haal() {
  local pad="$1" doel="$2" terug="${3:-}" w
  w=$(mktemp -d)
  mkdir -p "$doel"
  if git clone -q --depth 1 --filter=blob:none --sparse --branch schermen "$URL" "$w/s" 2>/dev/null; then
    git -C "$w/s" sparse-checkout set "$pad" ${terug:+"$terug"} 2>/dev/null
    if [ -d "$w/s/$pad" ]; then
      cp -r "$w/s/$pad"/. "$doel"/
      echo "referentie $pad"
    elif [ -n "$terug" ] && [ -d "$w/s/$terug" ]; then
      cp -r "$w/s/$terug"/. "$doel"/
      echo "TERUGVAL: nog geen referentie, vergeleken met de laatste run in $terug (geslaagd of niet)"
    fi
  fi
  rm -rf "$w"
  echo "referentie: $(find "$doel" -name '*.png' | wc -l) plaatjes"
}

bewaar() {
  local bron="$1" pad="$2" wat="$3" w poging
  [ -d "$bron" ] && [ -n "$(find "$bron" -name '*.png' | head -1)" ] || { echo "geen plaatjes in $bron"; return 0; }
  wie
  for poging in 1 2 3 4 5; do
    w=$(mktemp -d)
    if git clone -q --depth 1 --filter=blob:none --sparse --branch schermen "$URL" "$w/s" 2>/dev/null; then
      git -C "$w/s" sparse-checkout set "$pad"
    else
      git init -q -b schermen "$w/s" && git -C "$w/s" remote add origin "$URL"
    fi
    rm -rf "${w:?}/s/$pad" && mkdir -p "$w/s/$pad"
    (cd "$bron" && find . -name '*.png' -print0 | xargs -0 -I{} cp --parents {} "$w/s/$pad"/)
    echo "referentie uit run ${GITHUB_RUN_ID:-?}, commit ${GITHUB_SHA:-?}, $(date -u +%FT%TZ)" > "$w/s/$pad/RUN.txt"
    git -C "$w/s" add -A
    if git -C "$w/s" diff --cached --quiet; then echo "referentie ongewijzigd"; rm -rf "$w"; return 0; fi
    git -C "$w/s" commit -q -m "Referentiebeelden $wat run ${GITHUB_RUN_ID:-?}"
    if git -C "$w/s" push -q origin HEAD:schermen; then echo "referentie bewaard: $pad"; rm -rf "$w"; return 0; fi
    rm -rf "$w"; sleep $((poging * 4))
  done
  echo "referentie bewaren lukte niet (geen fout: de volgende geslaagde run probeert het weer)"
}

vergelijk() {
  local nu="$1" pad="$2" uit="$3" grens="$4" naam="$5" terug="${6:-}" maskers="${7:-}"
  rm -rf /tmp/bv-ref
  haal "$pad" /tmp/bv-ref "$terug" | tee /tmp/bv-haal.txt
  if grep -q TERUGVAL /tmp/bv-haal.txt; then
    naam="$naam (terugval: laatste run, geslaagd of niet)"
    # Geen bericht aan de eigenaar bij een terugval: die run kan rood of van een oudere test zijn.
    [ -n "${GITHUB_OUTPUT:-}" ] && echo "terugval=1" >> "$GITHUB_OUTPUT"
  fi
  local py=/tmp/bv-venv/bin/python
  if ! "$py" -c "import PIL, numpy" 2>/dev/null; then
    { python3 -m venv /tmp/bv-venv && "$py" -m pip install -q pillow numpy; } >/dev/null 2>&1 || py=python3
  fi
  if [ "$py" = python3 ] && ! python3 -c "import PIL, numpy" 2>/dev/null; then
    python3 -m pip install -q --user --break-system-packages pillow numpy >/dev/null 2>&1 || { echo "Pillow niet te installeren, geen vergelijking"; return 0; }
  fi
  BV_REF="$(head -1 /tmp/bv-ref/RUN.txt 2>/dev/null || echo geen)" "$py" -I "$HIER/beeldvergelijk.py" "$nu" /tmp/bv-ref "$uit" "$grens" "$naam" "$maskers"
  # Verslag ook naast de schermen, zodat het op de tak schermen staat (zonder sleutel te lezen).
  [ -f "$uit/verslag.md" ] && [ -d "$nu" ] && cp "$uit/verslag.md" "$nu/BEELDVERSCHIL.md"
  rm -rf /tmp/bv-ref
}

bericht() {
  local naam="$1" tekst="$2" w poging
  [ -s "$tekst" ] || { echo "geen tekst"; return 0; }
  wie
  for poging in 1 2 3 4 5; do
    w=$(mktemp -d)
    git clone -q --depth 1 --filter=blob:none --sparse --branch main "$URL" "$w/m" || { sleep $((poging * 5)); continue; }
    git -C "$w/m" sparse-checkout set berichten organisatie/controle
    { echo; cat "$tekst"; } >> "$w/m/berichten/$naam.md"
    git -C "$w/m" add "berichten/$naam.md"
    git -C "$w/m" commit -q -m "Week-test en beeldvergelijking: bericht aan $naam (run ${GITHUB_RUN_ID:-?})"
    (cd "$w/m" && python3 organisatie/controle/check.py HEAD~1 HEAD) || { echo "controle NIET OK, bericht niet geplaatst"; rm -rf "$w"; return 1; }
    if git -C "$w/m" push -q origin HEAD:main; then echo "bericht aan $naam staat op main"; rm -rf "$w"; return 0; fi
    rm -rf "$w"; sleep $((poging * 5))
  done
  echo "bericht aan $naam lukte niet na 5 pogingen"; return 1
}

meld() {
  local product="$1" eigenaar="$2" art="$3" tak="$4" w poging sleutel pad
  rm -rf /tmp/bb
  python3 -I "$HIER/beeldbericht.py" "$art" "$product" "$tak" /tmp/bb
  [ -s /tmp/bb/sleutel.txt ] || return 0
  sleutel=$(head -1 /tmp/bb/sleutel.txt)
  pad="referentie/$product/$tak"
  wie
  for poging in 1 2 3 4 5; do
    w=$(mktemp -d)
    git clone -q --depth 1 --filter=blob:none --sparse --branch schermen "$URL" "$w/s" 2>/dev/null || { rm -rf "$w"; sleep $((poging * 4)); continue; }
    git -C "$w/s" sparse-checkout set "$pad"
    if [ "$(head -1 "$w/s/$pad/GEMELD.md" 2>/dev/null)" = "$sleutel" ]; then
      echo "al gemeld: $sleutel"; rm -rf "$w"; return 0
    fi
    mkdir -p "$w/s/$pad" && cp /tmp/bb/gemeld.md "$w/s/$pad/GEMELD.md"
    git -C "$w/s" add "$pad/GEMELD.md" && git -C "$w/s" commit -q -m "Beeldverschil gemeld: $sleutel (run ${GITHUB_RUN_ID:-?})"
    if git -C "$w/s" push -q origin HEAD:schermen; then
      rm -rf "$w"
      {
        echo "## $(datum) NL, van de beeldvergelijking (automatisch): $product"
        cat /tmp/bb/bericht.md
        echo "Welke plaatjes: https://github.com/${GITHUB_REPOSITORY}/blob/schermen/$pad/GEMELD.md"
      } > /tmp/bb/volledig.md
      bericht "$eigenaar" /tmp/bb/volledig.md
      return $?
    fi
    rm -rf "$w"; sleep $((poging * 4))
  done
  echo "claim op schermen lukte niet, geen bericht (de volgende run probeert het weer)"
}

datum() {
  python3 -c "import datetime,zoneinfo; n=datetime.datetime.now(zoneinfo.ZoneInfo('Europe/Amsterdam')); m='jan feb mrt apr mei jun jul aug sep okt nov dec'.split()[n.month-1]; print(f'{n.day} {m} {n.year} {n:%H:%M}')"
}

opdracht="${1:-}"; shift || true
case "$opdracht" in
  haal) haal "$@" ;;
  bewaar) bewaar "$@" ;;
  vergelijk) vergelijk "$@" ;;
  bericht) bericht "$@" ;;
  meld) meld "$@" ;;
  datum) datum ;;
  *) sed -n '2,21p' "$0"; exit 2 ;;
esac
