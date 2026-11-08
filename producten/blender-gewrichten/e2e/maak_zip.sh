#!/usr/bin/env bash
# Pakt Click Joints in als extensie-zip (zoals extensions.blender.org hem wil).
set -euo pipefail
cd "$(dirname "$0")/.."
rm -f /tmp/click_joints.zip
(cd click_joints && zip -qr /tmp/click_joints.zip . -x '*__pycache__*')
echo /tmp/click_joints.zip
