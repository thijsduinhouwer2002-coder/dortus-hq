import re,sys
for f in sys.argv[1:]:
    L=open(f).read().splitlines()
    kopen=[float(re.search(r"koop ([\d.]+):",l).group(1)) for l in L if l.startswith("HOL koop ") ]
    vang=[float(m.group(1)) for l in L for m in [re.match(r"HOL kroniek ([\d.]+) .*\+(\d+)$",l)] if m]
    gel=sum(1 for l in L if "koopgeluk vangst" in l); pech=sum(1 for l in L if "HOL droogte" in l)
    def gat(p,a=240,b=900):
        q=[a]+[x for x in p if a<x<b]+[b]; return max(y-x for x,y in zip(q,q[1:]))
    na=[min([v for v in vang if v>k] or [999])-k for k in kopen]
    print(f, "kopen", [round(k) for k in kopen], "| vangsten", len(vang), "| gat zonder vangst min4-15 %.0f s"%gat(vang), "| gat zonder koop %.0f s"%gat(kopen), "| koop->vangst", [round(x) for x in na], "| koopgeluk-vangsten",gel,"droogte",pech)
