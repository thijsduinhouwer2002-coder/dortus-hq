#!/bin/sh
# Meet de downloadteller van Click Joints en zet een regel onder downloads.csv. Gebruik: sh meet_downloads.sh
cd "$(dirname "$0")"
n=$(curl -sS -m 30 https://extensions.blender.org/add-ons/click-joints/ | tr -s ' \n' ' ' | sed -n 's/.*Downloads *<[^>]*> *\([0-9,]*\).*/\1/p; s/.*Downloads \([0-9,]*\).*/\1/p' | head -1 | tr -d ,)
[ -z "$n" ] && n=$(curl -sS -m 30 https://extensions.blender.org/add-ons/click-joints/ | python3 -c "import sys,re,html;t=html.unescape(re.sub(r'<[^>]+>',' ',sys.stdin.read()));m=re.search(r'Downloads\s+([0-9,]+)',t);print(m.group(1).replace(',','') if m else '')")
v=$(curl -sS -m 30 https://extensions.blender.org/api/v1/extensions/ | python3 -c "import sys,json;print(next((e.get('version','') for e in json.load(sys.stdin).get('data',[]) if e.get('id')=='click_joints'),''))" 2>/dev/null)
[ -z "$v" ] && v="?"
echo "$(date -u '+%Y-%m-%d %H:%M'),$n,?,$v,https://extensions.blender.org/add-ons/click-joints/" >> downloads.csv
tail -1 downloads.csv
