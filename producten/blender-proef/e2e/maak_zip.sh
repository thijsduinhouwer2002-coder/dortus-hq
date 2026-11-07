#!/usr/bin/env bash
# Pakt de add-on in als extensie-zip (zoals extensions.blender.org hem wil).
set -euo pipefail
cd "$(dirname "$0")/.."
rm -f /tmp/dortus_proef.zip
(cd dortus_proef && zip -qr /tmp/dortus_proef.zip . -x '__pycache__/*')
echo /tmp/dortus_proef.zip
