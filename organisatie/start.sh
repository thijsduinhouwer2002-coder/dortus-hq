#!/usr/bin/env bash
# Start van elke run: nieuwste stand ophalen en de automatische controle aanzetten.
# Gebruik: bash organisatie/start.sh                  (in een bestaande kloon: doet alleen ophalen en de controle)
# Nog geen kloon? Draai dit in een lege map (maakt een snelle kloon in ./dortus-hq):
#   curl -sL https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/organisatie/start.sh | bash
#   ... | bash -s -- producten/blender-gewrichten platformen/blender     (eigen mappen er meteen bij)
# Snelle kloon = --filter=blob:none (hele geschiedenis, oude bestanden komen pas binnen als je ze opent) plus sparse
# checkout van wat een agent normaal nodig heeft (zie BASIS). De rest erbij halen:
#   git sparse-checkout add <map>        bijvoorbeeld: git sparse-checkout add producten/steam-hol
#   git sparse-checkout disable          alles uitpakken (±1 GB)
DORTUS_REPO="https://github.com/thijsduinhouwer2002-coder/dortus-hq"
BASIS="organisatie berichten marketing commercie dashboard .claude .githooks .github"
export GIT_TERMINAL_PROMPT=0
is_dortus() { [ -n "$1" ] && [ -f "$1/organisatie/start.sh" ] && [ -f "$1/CLAUDE.md" ]; }
hier=$(git -C "$(dirname "$0")" rev-parse --show-toplevel 2>/dev/null)
is_dortus "$hier" || hier=$(git rev-parse --show-toplevel 2>/dev/null)
if is_dortus "$hier"; then
  cd "$hier" || exit 1
else
  map="${DORTUS_MAP:-dortus-hq}"
  if [ -e "$map" ]; then echo "STOP: $(pwd)/$map bestaat al maar is geen kloon van dortus-hq. Kies een lege map (of zet DORTUS_MAP)."; exit 1; fi
  echo "Geen kloon gevonden: snelle kloon naar $(pwd)/$map (blob:none, sparse)."
  timeout 300 git clone -q --filter=blob:none --no-checkout "$DORTUS_REPO" "$map" || { echo "STOP: klonen lukte niet."; exit 1; }
  cd "$map" || exit 1
  # shellcheck disable=SC2086
  git sparse-checkout set --cone $BASIS "$@" && timeout 300 git checkout -q main || { echo "STOP: uitpakken lukte niet."; exit 1; }
  echo "Uitgepakt: de hoofdmap plus $BASIS${*:+ $*}. Meer nodig: git sparse-checkout add <map>."
  # Let op: wegwijzer.py geeft in deze sparse kloon valse meldingen (mappen die niet zijn uitgepakt lijken weg).
  # Draai hem in Actions (wegwijzer.yml) of na git sparse-checkout disable; niets "repareren" op zijn melding hier.
  echo "Let op: in deze kloon geeft wegwijzer.py valse meldingen (niet uitgepakte mappen); draai hem in Actions of na git sparse-checkout disable."
fi
# Losse HEAD of een tak zonder upstream: haal main op en werk daarop verder (hing anders tot de time-out, Bram 20 nov).
if ! git symbolic-ref -q HEAD >/dev/null || ! git rev-parse -q --verify '@{u}' >/dev/null 2>&1; then
  timeout 60 git fetch -q origin main && { git merge -q --ff-only FETCH_HEAD 2>/dev/null || echo "LET OP: kon niet vooruitspoelen naar origin/main (eigen commits? eerst samenvoegen)."; }
else
  timeout 60 git pull -q --rebase 2>/dev/null || echo "LET OP: git pull --rebase lukte niet (eigen wijzigingen? eerst committen)."
fi
git config core.hooksPath .githooks
chmod +x .githooks/* 2>/dev/null
echo "Dortus: stand opgehaald ($(git log -1 --format='%h %cr')). Controle voor elke push staat aan."
echo "Harde regels: geld alleen na ja van Thijs; geen persoonsgegevens (repo is openbaar); webpagina's met curl, nooit WebFetch; niets naar buiten onder de naam van Thijs; GEZIEN/GOK bij elk cijfer; alleen in je eigen plekken schrijven; alleen de koppelingen Gmail (lezen), Metricool (alleen de Maker van Roep plaatst), Claude Code Remote en context7, de rest nooit (ook AnythingMCP); Nederlands zonder gedachtestreepjes."
