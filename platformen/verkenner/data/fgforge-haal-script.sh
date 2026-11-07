#!/bin/sh
# Haalt alle items van de Fantasy Grounds Forge op (openbare tabel van de winkel, met CSRF-token uit de pagina).
# Velden: price in centen, subcount = aantal abonnees (eigenaars), created_at.
set -e
d=$(mktemp -d)
curl -s -c "$d/jar" https://forge.fantasygrounds.com/shop -o "$d/shop.html"
tok=$(grep -oE 'csrf-token" content="[^"]+' "$d/shop.html" | cut -d'"' -f3)
curl -s -b "$d/jar" -H "X-CSRF-TOKEN: $tok" -H "X-Requested-With: XMLHttpRequest" -X POST \
  "https://forge.fantasygrounds.com/api/visitor/items/datatable" --data "draw=1&start=0&length=10000" \
  -o "fgforge-items-$(date -u +%F).json"
