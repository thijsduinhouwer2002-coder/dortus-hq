#!/bin/sh
# Haalt de beelden uit spel-bronnen.txt op naar bron/<doelmap>/0001.png ... Gebruik: sh spel-bronnen.sh [lokale-map]
# Met een lokale map (zelfde mapnamen als op schermen) wordt gekopieerd in plaats van gedownload.
B=https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/453aac1e7576ed4c9c00e75c7798f90c7c774a47/steam-hol
grep -v '^#' spel-bronnen.txt | while read doel map van tot; do
  [ -z "$doel" ] && continue
  mkdir -p "bron/$doel"; n=1; i=$van
  while [ $i -le $tot ]; do
    f=$(printf 'f%08d.png' $((i*5))); u=$(printf '%04d.png' $n)
    if [ -n "$1" ]; then cp "$1/$map/$f" "bron/$doel/$u"; else curl -sSfL -o "bron/$doel/$u" "$B/$map/los/$f" || exit 1; fi
    n=$((n+1)); i=$((i+1))
  done
done
