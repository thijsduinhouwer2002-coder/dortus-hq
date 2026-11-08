import json
from PIL import Image
d=json.load(open('frames.json'));meta=open('fr/meta.json').read()
IW,IH=Image.open('fr/held-top.png').size
s=open('b.html').read().replace('__DATA__',json.dumps(d)).replace('__META__',meta).replace('__IW__',str(IW)).replace('__IH__',str(IH))
s=s.replace('__WOLF__',open('wolf-head.svg').read().strip()).replace('__TRAP__',open('jaw-trap.svg').read().strip())
open('b-r.html','w').write(s)
