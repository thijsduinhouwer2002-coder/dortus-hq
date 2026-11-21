#!/usr/bin/env bash
# Het Hol met steamcmd naar Steam, vanaf een eigen pc (Olaf, 21 nov 2026).
# Reservepad naast de knop .github/workflows/steam-uitbrengen.yml, voor als die niet kan
# (bijvoorbeeld als het geheim STEAM_CONFIG_VDF verlopen is). Alleen Thijs draait dit echt:
# steamcmd vraagt zelf om wachtwoord en Steam Guard-code, dit script slaat niets op.
#
# Gebruik:
#   upload.sh --droog <map-met-vol-en-demo>                 alle controles en de app-build-bestanden, geen upload
#   STEAM_USERNAME=... STEAM_APPID=... STEAM_DEMO_APPID=... \
#     upload.sh <map-met-vol-en-demo> [vol|demo|beide] [steamtak]   echte upload (standaard beide, tak intern)
# De map is de uitgepakte artifact "steam-depots" van een run van steam-uitbrengen.yml (met vol/ en demo/),
# zodat er precies de gekeurde build naar Steam gaat en niet iets van de eigen pc.
set -u
hier="$(cd "$(dirname "$0")" && pwd)"
droog=false
if [ "${1:-}" = "--droog" ]; then droog=true; shift; fi
map="${1:?geef de map met vol/ en demo/ (artifact steam-depots)}"
welke="${2:-beide}"
tak="${3:-intern}"
case "$welke" in vol|demo|beide) ;; *) echo "FOUT: welke is vol, demo of beide"; exit 1;; esac

# Alleen een echte uitgave van de knop mag naar Steam: geen proefdraai en geen map zonder VERSIE.txt.
if ! $droog; then
  [ -f "$map/VERSIE.txt" ] || { echo "FOUT: geen VERSIE.txt in $map; gebruik de artifact steam-depots van een echte run"; exit 1; }
  if grep -q "PROEFDRAAI" "$map/VERSIE.txt"; then echo "FOUT: dit is een proefdraai (VERSIE.txt), niet uploaden; neem een echte run met akkoord van Daan"; exit 1; fi
fi
werk="$(mktemp -d)"
fout=0
for d in vol demo; do
  [ "$welke" = "beide" ] || [ "$welke" = "$d" ] || continue
  bash "$hier/controleer-exportmap.sh" "$map/$d" "$d" || fout=$((fout+1))
  if [ "$d" = "vol" ]; then id="${STEAM_APPID:-}"; else id="${STEAM_DEMO_APPID:-}"; fi
  if [ -z "$id" ]; then
    if $droog; then id=1000; echo "let op: geen appid voor $d, droogloop gebruikt 1000"; else echo "FOUT: zet STEAM_APPID en STEAM_DEMO_APPID"; fout=$((fout+1)); continue; fi
  fi
  versie=$(head -1 "$map/VERSIE.txt" 2>/dev/null | tr -d '\r')
  [ -n "$versie" ] || versie="zonder VERSIE.txt"
  bash "$hier/maak-appbuild.sh" "$id" "$map/$d" "$tak" "Het Hol $d, $versie" "$werk/app_build_$d.vdf" || fout=$((fout+1))
done
[ "$fout" -eq 0 ] || { echo "Gestopt: $fout FOUT, niets geüpload."; exit 1; }

for v in "$werk"/app_build_*.vdf; do echo "===== $v"; cat "$v"; done
if $droog; then echo "Droogloop klaar: alles in orde, niets geüpload."; exit 0; fi

command -v steamcmd >/dev/null || { echo "FOUT: steamcmd niet gevonden (Valve: developer.valvesoftware.com/wiki/SteamCMD)"; exit 1; }
[ -n "${STEAM_USERNAME:-}" ] || { echo "FOUT: zet STEAM_USERNAME (het bouwaccount, niet het hoofdaccount)"; exit 1; }
args=(+login "$STEAM_USERNAME")
for v in "$werk"/app_build_*.vdf; do args+=(+run_app_build "$v"); done
args+=(+quit)
echo "steamcmd ${args[*]}"
steamcmd "${args[@]}"
echo "Klaar. De build staat op tak '$tak' in Steamworks; live zetten doet Thijs daar zelf."
