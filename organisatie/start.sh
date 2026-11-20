#!/usr/bin/env bash
# Start van elke run: nieuwste stand ophalen en de automatische controle aanzetten.
# Gebruik: bash organisatie/start.sh
cd "$(git rev-parse --show-toplevel 2>/dev/null || dirname "$0"/..)" || exit 1
export GIT_TERMINAL_PROMPT=0
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
