#!/usr/bin/env bash
# Controle na het plakken van gratis Click Joints 0.1.3 (Bram, 28 nov 2026, issue #306).
# Draai na het plakken: bash producten/blender-gewrichten/winkel/controle-gratis-0.1.3.sh
# Leest alleen openbare pagina's en bestanden met curl. Geen inloggen, geen sleutel.
# Code 0 = ALLES GOED. extensions.blender.org mag WACHT geven zolang de moderator 0.1.3 nog niet goedkeurde.
# Gumroad gratis en Printables geven hun zip alleen na een klik of inloggen; die kijkt de hoofdchat met het oog na.
set -u
UA="Mozilla/5.0"
T=$(mktemp -d)
fout=0
direct_sha="7a943b6946932a9c6c279481c7d5ed9aa0861fc34625ff363f761449653680df"

# 1. dortus.com: de gratis download is de direct-zip 0.1.3
curl -sL -A "$UA" -o "$T/free.zip" https://dortus.com/click-joints/click-joints-free.zip
s=$(sha256sum "$T/free.zip" | cut -d' ' -f1)
v=$(unzip -p "$T/free.zip" blender_manifest.toml 2>/dev/null | grep '^version' | head -1)
if [ "$s" = "$direct_sha" ]; then echo "GOED  dortus.com zip is direct-0.1.3 ($v)"
else echo "FOUT  dortus.com zip: $v, sha256 $s (verwacht $direct_sha)"; fout=1; fi

# 2. Superhive: Lite-zin noemt 0.1.3, niet meer 0.1.1
curl -sL -A "$UA" -o "$T/sh.html" https://superhivemarket.com/products/click-joints-pro
if grep -q "free Click Joints 0.1.3" "$T/sh.html" && ! grep -q "free Click Joints 0.1.1" "$T/sh.html"; then
  echo "GOED  Superhive Lite-zin noemt 0.1.3"
elif [ ! -s "$T/sh.html" ]; then echo "FOUT  Superhive gaf een lege pagina (na 5 minuten opnieuw)"; fout=1
else echo "FOUT  Superhive Lite-zin noemt nog geen 0.1.3"; fout=1; fi

# 3. Gumroad gratis: pagina noemt geen oude versie als nieuwste
curl -sL -A "$UA" -o "$T/gf.html" https://duinhouwer8.gumroad.com/l/click-joints-free
if grep -q "print tested" "$T/gf.html"; then echo "FOUT  Gumroad gratis zegt 'print tested'"; fout=1
else echo "GOED  Gumroad gratis bereikbaar, zonder 'print tested' (zip zelf: met het oog)"; fi

# 4. extensions.blender.org: 0.1.3 zichtbaar na goedkeuring van de moderator
curl -sL -A "$UA" -o "$T/ext.html" https://extensions.blender.org/add-ons/click-joints/
if grep -q "0\.1\.3" "$T/ext.html"; then echo "GOED  extensions.blender.org toont 0.1.3"
else echo "WACHT extensions.blender.org toont nog geen 0.1.3 (moderator; geen fout)"; fi

# 5. Sleeplink (#380): Blender vindt een gesleepte link alleen als hij gelijk is aan de archive_url
#    van de NIEUWSTE versie op het platform. Oude link = "not found" bij de gebruiker.
api=$(curl -sL -A "$UA" "https://extensions.blender.org/api/v1/extensions/?blender_version=4.2.0" | python3 -c "
import json, sys
print(next((x['archive_url'] for x in json.load(sys.stdin)['data'] if x['id'] == 'click_joints'), ''))")
curl -sL -A "$UA" -o "$T/readme.md" https://raw.githubusercontent.com/thijsduinhouwer2002-coder/click-joints/main/README.md
curl -sL -A "$UA" -o "$T/site.html" https://dortus.com/click-joints/
for plek in "README click-joints:$T/readme.md" "dortus.com/click-joints:$T/site.html"; do
  naam="${plek%%:*}"; bestand="${plek#*:}"
  link=$(grep -o 'https://extensions.blender.org/download/sha256:[0-9a-f]*/[^?"]*\.zip' "$bestand" | head -1)
  if [ -z "$api" ]; then echo "FOUT  API van extensions.blender.org gaf geen click_joints"; fout=1
  elif [ -z "$link" ]; then echo "WACHT $naam heeft nog geen sleeplink (#380, nog niet geplakt)"
  elif [ "$link" = "$api" ]; then echo "GOED  $naam sleeplink is de nieuwste (${api##*/})"
  else echo "FOUT  $naam sleeplink is ${link##*/}, platform heeft ${api##*/}: link wisselen (plakkaart deel 4)"; fout=1; fi
done

rm -rf "$T"
if [ $fout -eq 0 ]; then echo "ALLES GOED"; else echo "NIET GOED: plak het blok met FOUT opnieuw en draai opnieuw"; fi
exit $fout
