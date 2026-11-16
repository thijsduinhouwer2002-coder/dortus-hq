#!/bin/bash
f="mk/$1.json"; [ -s "$f" ] || curl -s -m 60 "https://api.apify.com/v2/store?username=$1&limit=1000&sortBy=newest" -o "$f"
last=$(python3 -c "import json;d=json.load(open('$f'))['data']['items'];print(d[-1]['username']+'~'+d[-1]['name'] if d else '')")
[ -n "$last" ] && { g="mk/$1.first.json"; [ -s "$g" ] || curl -s -m 30 "https://api.apify.com/v2/acts/$last" -o "$g"; }
