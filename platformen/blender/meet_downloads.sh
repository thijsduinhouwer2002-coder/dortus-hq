#!/bin/sh
# Meet de downloadteller van Click Joints en zet een regel onder downloads.csv. Gebruik: sh meet_downloads.sh
cd "$(dirname "$0")"
n=$(curl -sS -m 30 https://extensions.blender.org/add-ons/click-joints/ | tr -s ' \n' ' ' | sed -n 's/.*Downloads *<[^>]*> *\([0-9,]*\).*/\1/p; s/.*Downloads \([0-9,]*\).*/\1/p' | head -1 | tr -d ,)
[ -z "$n" ] && n=$(curl -sS -m 30 https://extensions.blender.org/add-ons/click-joints/ | python3 -c "import sys,re,html;t=html.unescape(re.sub(r'<[^>]+>',' ',sys.stdin.read()));m=re.search(r'Downloads\s+([0-9,]+)',t);print(m.group(1).replace(',','') if m else '')")
echo "$(date -u '+%Y-%m-%d %H:%M'),$n,?,0.1.0,https://extensions.blender.org/add-ons/click-joints/" >> downloads.csv
tail -1 downloads.csv
