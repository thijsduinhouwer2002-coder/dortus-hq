#!/bin/sh
# Haalt TrustMRR-profielen (.md, robots.txt staat het toe) van startups met UI-woorden in de slug.
# Gebruik: sh trustmrr-uikits-haal.sh <map>; daarna python3 -I trustmrr-uikits-analyse.py (in die map, met submap tm/)
cd "$1" && mkdir -p tm
curl -s https://trustmrr.com/startup-sitemap.xml | grep -o '<loc>[^<]*</loc>' | sed 's/<[^>]*>//g;s#.*/startup/##' | grep -Ei 'ui|block|kit|component|templat|shadcn|tailwind|starter|boilerplat|landing|theme' > sel.txt
cat sel.txt | xargs -P4 -I{} sh -c 'curl -s --max-time 20 "https://trustmrr.com/startup/{}.md" -o tm/{}.md; sleep 0.3'
