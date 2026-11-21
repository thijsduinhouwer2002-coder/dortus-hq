#!/usr/bin/env bash
# Schrijft het app-build-bestand (met depot erin) dat steamcmd krijgt (Olaf, 21 nov 2026).
# Vorm volgens Valve, sdk/tools/ContentBuilder/scripts/app_build_1000.vdf: één depot, alles uit ContentRoot.
# Gebruik: maak-appbuild.sh <appid> <contentroot> <steamtak> <omschrijving> <uitbestand> [depotid]
#   depotid: standaard appid+1 (het eerste depot dat Steamworks bij een nieuwe app maakt)
#   steamtak: nooit default of public; live zetten doet Thijs in Steamworks.
set -eu
appid="${1:?appid}"; root="${2:?contentroot}"; tak="${3:?steamtak}"; desc="${4:?omschrijving}"; uit="${5:?uitbestand}"
depot="${6:-}"

[[ "$appid" =~ ^[0-9]+$ ]] || { echo "FOUT: appid '$appid' is geen getal"; exit 1; }
[ -n "$depot" ] || depot=$((appid+1))
[[ "$depot" =~ ^[0-9]+$ ]] || { echo "FOUT: depotid '$depot' is geen getal"; exit 1; }
t=$(echo "$tak" | tr 'A-Z' 'a-z' | xargs)
if [ -z "$t" ] || [ "$t" = "default" ] || [ "$t" = "public" ]; then
  echo "FOUT: Steam-tak '$tak' mag niet. Een build gaat alleen naar een niet-openbare tak."; exit 1
fi
echo "$t" | grep -Eq '^[a-z0-9_-]{1,32}$' || { echo "FOUT: Steam-tak '$tak': alleen kleine letters, cijfers, - en _"; exit 1; }
# aanhalingstekens en backslashes breken het vdf-formaat
desc=$(echo "$desc" | tr -d '"\\' | cut -c1-120)
root_abs=$(cd "$root" && pwd)

cat > "$uit" <<EOF
"AppBuild"
{
	"AppID" "$appid"
	"Desc" "$desc"
	"ContentRoot" "$root_abs"
	"BuildOutput" "$(dirname "$root_abs")/steam-output"
	"SetLive" "$t"
	"Preview" "0"
	"Depots"
	{
		"$depot"
		{
			"FileMapping"
			{
				"LocalPath" "*"
				"DepotPath" "."
				"recursive" "1"
			}
			"FileExclusion" "*.pdb"
			"FileExclusion" "*.log"
			"FileExclusion" "*.vdf"
		}
	}
}
EOF
echo "app-build geschreven: $uit (app $appid, depot $depot, tak $t)"
