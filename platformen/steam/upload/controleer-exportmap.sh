#!/usr/bin/env bash
# Controle van een exportmap van Het Hol voor die naar Steam gaat (Olaf, 21 nov 2026).
# Gebruik: controleer-exportmap.sh <map> [naam]
# Stopt met code 1 bij een fout. Gebruikt door .github/workflows/steam-uitbrengen.yml en door upload.sh.
set -u
map="${1:?geef de exportmap, bijvoorbeeld steam/vol}"
naam="${2:-$(basename "$map")}"
MAX_MB="${MAX_MB:-500}"
fout=0
f() { echo "FOUT ($naam): $1"; fout=$((fout+1)); }

if [ ! -d "$map" ]; then echo "FOUT ($naam): map $map bestaat niet"; exit 1; fi

# 1. de exe en het pakbestand van Godot moeten er zijn (export met embed_pck geeft alleen de exe)
[ -f "$map/HetHol.exe" ] || f "HetHol.exe ontbreekt"
if [ -f "$map/HetHol.exe" ]; then
  kb=$(( $(wc -c < "$map/HetHol.exe") / 1024 ))
  [ "$kb" -ge 1024 ] || f "HetHol.exe is maar $kb KB, waarschijnlijk geen echte export"
  # een Windows-exe begint met MZ
  [ "$(head -c 2 "$map/HetHol.exe")" = "MZ" ] || f "HetHol.exe is geen Windows-programma (geen MZ aan het begin)"
fi

# 2. verboden in een depot: logs, saves, debug, vdf (sleutels), tijdelijke bestanden, git
vreemd=$(find "$map" \( -name '*.log' -o -name '*.pdb' -o -name '*.vdf' -o -name '*.save' -o -name '*.sav' \
  -o -name '*.tmp' -o -name '*.tres' -o -name '*.import' -o -name '.git*' -o -name 'config.vdf' -o -name '*.env' \) -print)
if [ -n "$vreemd" ]; then f "verboden bestanden: $(echo $vreemd)"; fi

# 3. geen lege map en niet te groot
n=$(find "$map" -type f | wc -l)
[ "$n" -gt 0 ] || f "map is leeg"
mb=$(du -sm "$map" | cut -f1)
[ "$mb" -lt "$MAX_MB" ] || f "map is $mb MB (grens $MAX_MB MB)"

# 4. geen bestandsnamen met tekens die Steam of Windows lastig vinden
raar=$(find "$map" -type f -name '*[:*?"<>|]*' -print)
[ -z "$raar" ] || f "bestandsnamen met verboden tekens: $(echo $raar)"

echo "$naam: $n bestanden, $mb MB, $fout FOUT"
find "$map" -type f -printf '  %P  %s\n' | sort
[ "$fout" -eq 0 ]
