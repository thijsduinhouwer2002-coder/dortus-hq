#!/usr/bin/env bash
# Pakt Split Joints in als extensie-zip: /tmp/split_joints.zip (daarna: blender --command extension validate).
set -euo pipefail
cd "$(dirname "$0")/.."
rm -f /tmp/split_joints.zip
(cd split_joints && zip -qr /tmp/split_joints.zip . -x '*__pycache__*')
echo /tmp/split_joints.zip
