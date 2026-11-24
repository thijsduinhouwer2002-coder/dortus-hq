#!/usr/bin/env bash
# Pakt Click Cuts in als extensie-zip: /tmp/click_cuts.zip (daarna: blender --command extension validate).
set -euo pipefail
cd "$(dirname "$0")/.."
rm -f /tmp/click_cuts.zip
(cd split_joints && zip -qr /tmp/click_cuts.zip . -x '*__pycache__*')
echo /tmp/click_cuts.zip
