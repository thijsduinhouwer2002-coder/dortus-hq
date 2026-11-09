#!/bin/bash
ep=$1; curl -sS -m 20 -A "Mozilla/5.0" "https://frontend.cfx-services.net/api/servers/single/$ep" | python3 -c "
import json,sys
try:
 d=json.load(sys.stdin)['Data']; print(json.dumps({'ep':'$ep','clients':d.get('clients'),'host':d.get('hostname','')[:120],'res':d.get('resources',[]),'fw':[k for k in d.get('vars',{}) if 0],'tags':d.get('vars',{}).get('tags','')}))
except Exception as e: print(json.dumps({'ep':'$ep','err':str(e)}))
" > single/$ep.json
