#!/bin/bash
# Leest per TrustMRR-profiel (.md, toegestaan in robots.txt) de X-volgers en oprichter. Invoer: tsv met d30<TAB>slug
A="Mozilla/5.0 DortusVerkenner"
while IFS=$'\t' read d s; do p=$(curl -sL -A "$A" --max-time 20 "https://trustmrr.com/startup/$s.md"); xf=$(echo "$p" | grep -o -E "X followers: [0-9,]+" | grep -o -E "[0-9,]+$" | tr -d ,); fo=$(echo "$p" | grep -o -E "trustmrr.com/founder/[^)]*" | head -1 | sed 's#.*/##'); echo -e "$d\t$s\t${xf:-geen}\t${fo:-?}"; sleep 1; done < "$1"
