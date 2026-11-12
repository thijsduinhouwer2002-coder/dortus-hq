# Contrast van de dieren van Ebb tegen de achtergronden van hun familie (Gijs, run 72).
# Rekent het kleurverschil dE (CIE76) uit de kleuren in de code. Gebruik:
#   python3 contrast_dieren.py                 de tabel van alle 25 dieren
#   python3 contrast_dieren.py 13 AAAAAA       dier 13 met een ander lijf
#   python3 contrast_dieren.py 13 55AAFF 3     dier 13 met de lucht van familie 3
import sys
NAMEN = "Fish Shrimp Jellyfish Turtle Crab Seahorse Starfish Clownfish Pufferfish Octopus Eel Ray Seal Dolphin Swordfish Sea-otter Manta Shark Sunfish Orca Narwhal Giant-squid Lobster Whale Sea-cucumber".split()
LIJF = [0xFFAA55,0xFFAAAA,0xFF55AA,0x00AA55,0xFF5500,0xFFAA00,0xFFAA55,0xFF5500,0xFFFF55,0xAA55FF,0xAAFF55,0xAAAA55,0xAAAAAA,0x55AAFF,0x5555FF,0xAA5500,0xAAAAAA,0x55AAAA,0xAAAAFF,0x555555,0x5555AA,0xAA55FF,0xFF5555,0x55AAFF,0x55FFAA]
FAM = [3,1,5,0,0,5,1,0,3,3,3,2,1,2,2,1,2,5,5,4,4,4,1,4,3]
# per familie: MIP boven, MIP band, AMOLED drie stappen (KrabV2Basis.LUCHT)
LUCHT = [[0x0055AA,0x00AAFF,0x001E5F,0x004BA5,0x00A5FA],[0x0055FF,0x55AAFF,0x002878,0x0050D2,0x5AB4FF],[0x0055AA,0x55AAFF,0x00235A,0x0055AA,0x6EB9FF],[0x5500AA,0xFF5555,0x28005A,0x6414A0,0xFF6E5A],[0x0055AA,0xAAFFFF,0x002864,0x0055A0,0xBEF5FF],[0x0000AA,0xFFFFAA,0x0A0050,0x2814AA,0xFFF0A0]]
WATER = [0x00698C,0x006E82,0x0064A0,0x46508C,0x14647D,0x3C4696]

def rgb(c): return ((c>>16)&255,(c>>8)&255,c&255)
def lab(c):
    v=[]
    for x in rgb(c):
        x/=255.0; v.append(x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4)
    r,g,b=v
    X=(0.4124*r+0.3576*g+0.1805*b)/0.95047; Y=0.2126*r+0.7152*g+0.0722*b; Z=(0.0193*r+0.1192*g+0.9505*b)/1.08883
    f=lambda t: t**(1/3.0) if t>0.008856 else 7.787*t+16/116.0
    return (116*f(Y)-16, 500*(f(X)-f(Y)), 200*(f(Y)-f(Z)))
def de(a,b):
    A,B=lab(a),lab(b); return sum((x-y)**2 for x,y in zip(A,B))**0.5
def nk(c,am):  # EbbNacht.k
    r,g,b=rgb(c)
    if am:
        r=(7*r*r+1274)//2550; g=(7*g*g+1274)//2550; b=(7*b*b+1274)//2550
        m=max(r,b,80); g=min(g,m); y=299*r+587*g+114*b
        r=(7000*r+3*y+5000)//10000; g=(7000*g+3*y+5000)//10000; b=(7000*b+3*y+5000)//10000
    else:
        t=lambda v: 0 if (v+42)//85<2 else ((v+42)//85-1)*85
        r,g,b=t(r),t(g),t(b); m=max(r,b,85); g=min(g,m)
    return (r<<16)|(g<<8)|b
def held(c,am):  # EbbNacht.held
    r,g,b=rgb(c)
    if (g>=r and g>b) or (r>=g and g>b and r<=0xAA):
        return ((r*4//5)<<16)|((g*4//5)<<8)|(b*4//5) if am else c
    return nk(c,am)
def rij(i,lijf=None,fam=None):
    c=LIJF[i] if lijf is None else lijf; f=FAM[i] if fam is None else fam; g=FAM[i]
    lu=list(LUCHT[f])
    if i==5: lu[1]=0xFFAAFF; lu[4]=0xFFAAE6
    w=[de(c,WATER[g]), min(de(c,0x005555),de(c,0x0055AA)), de(c,lu[4]), de(c,lu[1]), de(held(c,True),0x000069), de(held(c,False),0x000000)]
    return [round(x) for x in w]
if len(sys.argv)>2:
    i=int(sys.argv[1]); print(NAMEN[i], sys.argv[2], rij(i,int(sys.argv[2],16), int(sys.argv[3]) if len(sys.argv)>3 else None))
else:
    print("nr dier lijf | water dag AMOLED, water dag MIP, lucht dag AMOLED, lucht dag MIP, water nacht AMOLED, nacht MIP | laagste")
    for i in sorted(range(25), key=lambda i: min(rij(i))):
        print(i, NAMEN[i], "%06X"%LIJF[i], rij(i), min(rij(i)))
