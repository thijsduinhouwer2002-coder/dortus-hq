#!/usr/bin/env bash
# Zet de openbare bestanden van Rollwright in de eigen repo thijsduinhouwer2002-coder/rollwright.
# Gebruik: bash producten/obsidian-rollwright/publiceer.sh <pad naar kloon van rollwright> [release]
# Met "release" maakt de workflow daar een release van de versie in manifest.json.
# Alleen doen als de e2e-test groen is en Daan akkoord gaf (organisatie/regels.md).
set -euo pipefail
BRON="$(cd "$(dirname "$0")" && pwd)"
DOEL="${1:?pad naar de kloon van rollwright}"
MODUS="${2:-}"
cd "$DOEL" && git pull -q --rebase origin main 2>/dev/null || true
# Alleen wat openbaar hoort: geen interne notities, geen e2e, geen ontwerpstukken.
find "$DOEL" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
tar -C "$BRON" -cf - \
  --exclude='./node_modules' --exclude='./main.js' --exclude='*.map' \
  --exclude='./e2e' --exclude='./OPEN.md' --exclude='./architectuur.md' --exclude='./ontwerp*.md' --exclude='./bouwplan*.md' \
  --exclude='./publiceer.sh' --exclude='./.github' . | tar -C "$DOEL" -xf -
mkdir -p "$DOEL/.github/workflows"
cp "$BRON/../../organisatie/sjablonen/obsidian-release.yml" "$DOEL/.github/workflows/release.yml"
printf 'node_modules/\nmain.js\n*.map\n' > "$DOEL/.gitignore"
V=$(node -p "require('$DOEL/manifest.json').version")
cd "$DOEL"
git add -A
BERICHT="Rollwright $V"; [ "$MODUS" = "release" ] && BERICHT="$BERICHT [release]"
git commit -q -m "$BERICHT" || { echo "niets veranderd"; exit 0; }
git push -q origin HEAD:main
git ls-remote origin main
echo "Gepusht: $BERICHT. Uitslag: https://github.com/thijsduinhouwer2002-coder/rollwright/actions"
