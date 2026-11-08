import json,sys,subprocess
from PIL import Image
var=sys.argv[1]
d=json.load(open('frames.json'));meta=open('fr/meta.json').read()
IW,IH=Image.open('fr/held-top.png').size
T=json.load(open(f'times-{var}.json'))
s=open(f'{var}.html').read().replace('__DATA__',json.dumps(d)).replace('__META__',meta).replace('__IW__',str(IW)).replace('__IH__',str(IH)).replace('__TIMES__',json.dumps(T))
open(f'{var}-r.html','w').write(s)
