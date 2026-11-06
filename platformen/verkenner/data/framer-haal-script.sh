#!/bin/bash
S=/tmp/claude-0/-home-claude/010270e6-4dcd-589c-b69f-55c8f74143ea/scratchpad/framer
s=$1; [ -s $S/pages/$s.html ] && exit 0
code=$(curl -s -m 20 -o $S/pages/$s.html -w "%{http_code}" https://www.framer.com/marketplace/plugins/$s/)
echo "$s $code" >> $S/log2.txt
[ "$code" = "200" ] || { rm -f $S/pages/$s.html; sleep 10; }
sleep 0.5
