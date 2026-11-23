#!/usr/bin/env bash
# Systeempakketten voor de filmpjes-workflows, zonder onnodig wachten (Olaf, 23 nov).
# Gemeten (GEZIEN, stap "Systeempakketten" in 22 runs van regisseur-1 t/m 4 en studio op 23 nov): meestal 10 tot 60 s,
# maar soms 3 tot 8 min (regisseur-3 run 45227517215: 8 min 17 s), omdat `apt-get update` op een trage spiegel bleef
# hangen tot de grens van 300 s. De runner heeft al een pakketlijst. Daarom eerst installeren zonder update; alleen als
# dat mislukt (pakket weg uit de oude lijst) een update van hooguit 120 s en dan nog een keer.
# Proef 23 nov ±21:30 (run 45259595436, GEZIEN, 3 runners): installeren zonder update lukt op een schone runner
# (alles aanwezig), 25 en 32 s, maar één runner deed er 310 s over, ook zonder update. De uitschieters zitten dus
# (ook) in het downloaden van een trage spiegel; dit script haalt alleen de update-wachttijd weg. Volgende stap: de
# .deb-bestanden bewaren met actions/cache, dan hoeft er niets van de spiegel.
# Gebruik in een workflow:  bash commercie/filmpjes/apt-snel.sh xvfb ffmpeg fonts-inter ...
# Met bewaarde .deb-bestanden (Olaf, 23 nov ±22:30): zet APT_DEBS=$HOME/apt-debs en bewaar die map met actions/cache
# (voorbeeld in .github/workflows/apt-snel-proef.yml). apt haalt dan alleen wat nog niet in de map staat van de spiegel.
set -u
[ "$#" -gt 0 ] || { echo "gebruik: apt-snel.sh pakket..."; exit 2; }
OPT=(-y -q -o Acquire::http::Timeout=20 -o Acquire::Retries=3)
export DEBIAN_FRONTEND=noninteractive
if [ -n "${APT_DEBS:-}" ]; then
  mkdir -p "$APT_DEBS/partial"
  echo "apt-snel: $(ls "$APT_DEBS"/*.deb 2>/dev/null | wc -l) bewaarde .deb-bestanden in $APT_DEBS"
  OPT+=(-o "Dir::Cache::Archives=$APT_DEBS" -o APT::Sandbox::User=root -o APT::Keep-Downloaded-Packages=true)
  trap 'sudo chown -R "$(id -u):$(id -g)" "$APT_DEBS"; sudo rm -f "$APT_DEBS/lock"' EXIT
fi
if timeout 600 sudo apt-get install "${OPT[@]}" "$@" >/tmp/apt-snel.log 2>&1; then
  echo "apt-snel: geïnstalleerd zonder update"
  grep -c '^Get:' /tmp/apt-snel.log | sed 's/^/apt-snel: van de spiegel gehaald: /'
  exit 0
fi
echo "apt-snel: eerste poging mislukt, nu update en opnieuw"
tail -5 /tmp/apt-snel.log
timeout 120 sudo apt-get update -q -o Acquire::http::Timeout=20 -o Acquire::Retries=3 >/dev/null || echo "apt-snel: update traag, ga door"
timeout 600 sudo apt-get install "${OPT[@]}" "$@"
