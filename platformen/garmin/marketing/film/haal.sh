#!/bin/sh
# Haalt de echte simulatorbeelden van Ebb op voor de Roep-filmpjes en toetst ze (filmmaker-hoofdchat, 20 nov 2026).
# Bron: simulatorrun 43327097299 op e40269e1 (de ingediende app, fenix 8 47 mm), tak schermen, map garmin-adem/plaatjes/namen.
# Plus commercie/ebb/ebb-film.mp4 (dezelfde schermen met overvloeiers, ook gebruikt voor filmpje 4).
set -e
mkdir -p bron
S=https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/schermen/garmin-adem/plaatjes/namen
for n in krab2-hold-nacht basisoctopus-hold-nacht basiszeepaard-hold-nacht schild2-hold-nacht sessie-otter-hold-nacht \
         sessie-kreeft-hold-nacht sessie-komkommer-hold-nacht basisoctopus-hold-dag basiszeepaard-hold-dag schild2-hold-dag \
         einde-6b sealog-3-alle25 veilig-1 menu-krab; do
  curl -sSfL --retry 3 -o "bron/$n.png" "$S/$n-fenix847mm.png"
done
cp "${GITHUB_WORKSPACE:-../../../..}/commercie/ebb/ebb-film.mp4" bron/ebb-film.mp4
sha256sum -c bronnen.sha256
