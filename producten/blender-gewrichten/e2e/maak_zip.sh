#!/usr/bin/env bash
# Pakt Click Joints in als extensie-zip (zoals extensions.blender.org hem wil).
#   bash e2e/maak_zip.sh          -> gratis build /tmp/click_joints.zip (zonder click_joints/betaald/)
#   bash e2e/maak_zip.sh betaald  -> betaalde build /tmp/click_joints_betaald.zip (met betaald/ en de
#                                    registratie uit e2e/betaald/init_betaald.py achter __init__.py)
#   bash e2e/maak_zip.sh direct   -> gratis build voor directe download /tmp/click_joints_direct.zip: de gratis zip plus
#                                    e2e/direct/direct.py als direct.py en e2e/direct/init_direct.py achter __init__.py
#                                    (Pro-knoppen op slot). NIET voor extensions.blender.org, die krijgt de gratis zip.
# Twee builds uit één bron (ontwerp betaald v1.1): de gratis code noemt de betaalde versie nergens.
set -euo pipefail
cd "$(dirname "$0")/.."
soort="${1:-gratis}"
case "$soort" in
  gratis)
    rm -f /tmp/click_joints.zip
    (cd click_joints && zip -qr /tmp/click_joints.zip . -x '*__pycache__*' -x 'betaald/*')
    echo /tmp/click_joints.zip
    ;;
  betaald)
    werk="$(mktemp -d)"
    cp -r click_joints "$werk/click_joints"
    find "$werk" -name '__pycache__' -prune -exec rm -rf {} +
    cat e2e/betaald/init_betaald.py >> "$werk/click_joints/__init__.py"
    # Eigen naam en versie voor Superhive (id blijft click_joints, zodat de weigering naast de gratis werkt).
    m="$werk/click_joints/blender_manifest.toml"
    sed -i 's/^name = .*/name = "Click Joints Pro"/; s/^version = .*/version = "'"${PRO_VERSIE:-1.0.0}"'"/; s/^tagline = .*/tagline = "Poseable 3D print figures from your rig, with bend range"/' "$m"
    rm -f /tmp/click_joints_betaald.zip
    (cd "$werk/click_joints" && zip -qr /tmp/click_joints_betaald.zip .)
    rm -rf "$werk"
    echo /tmp/click_joints_betaald.zip
    ;;
  direct)
    werk="$(mktemp -d)"
    cp -r click_joints "$werk/click_joints"
    rm -rf "$werk/click_joints/betaald"
    find "$werk" -name '__pycache__' -prune -exec rm -rf {} +
    cp e2e/direct/direct.py "$werk/click_joints/direct.py"
    cat e2e/direct/init_direct.py >> "$werk/click_joints/__init__.py"
    rm -f /tmp/click_joints_direct.zip
    (cd "$werk/click_joints" && zip -qr /tmp/click_joints_direct.zip .)
    rm -rf "$werk"
    echo /tmp/click_joints_direct.zip
    ;;
  *) echo "onbekend: $soort (gratis, betaald of direct)" >&2; exit 2 ;;
esac
