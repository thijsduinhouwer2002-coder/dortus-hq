# Maakt per schermmaat de lijst met maten voor het horloge uit het blad van Mila.
# Bron: maten-tij-tabel.md (kopie van ontwerp/garmin/reeks/maten-tij-tabel.md op main; daar is Mila de baas).
# Gebruik: python3 maak_maten.py          schrijft resources*/jsondata/maten.json en jsondata.xml
#          python3 maak_maten.py --toets  schrijft niets, faalt als de bestanden niet bij het blad passen
import json, os, re, sys
HIER = os.path.dirname(os.path.abspath(__file__))
# Volgorde in de lijst = volgorde van de getallen in het blad, rij voor rij. Maten.mc gebruikt dezelfde nummers.
NAMEN = ['DATUM_Y', 'DATUM_PX', 'TIJD_Y', 'TIJD_PX', 'VELD_XL', 'VELD_XM', 'VELD_XR', 'ICOON_Y', 'ICOON_H',
         'VELD_Y', 'VELD_PX', 'WATER_TOP', 'WATER_BODEM', 'NU_X', 'LIJN_X', 'BAND_0', 'BAND_1', 'BAND_2', 'BAND_3',
         'LIJN_DIK', 'BOOT_HALF', 'MAST', 'BB_Y', 'BB_PX', 'BB_RAND', 'GOLF_B', 'GOLF_DIK', 'GOLF_AFSTAND', 'VEILIG']
BASIS = 260  # de map "resources" zonder maat: voor schermen zonder eigen map (Instinct 2, Venu Sq 2)

def lees_blad(pad):
    regels = [r for r in open(pad, encoding='utf-8').read().split('\n\n')[0].split('\n') if r.startswith('|')]
    kop = [c.strip() for c in regels[0].strip('|').split('|')]
    maten = [int(c) for c in kop[1:]]
    uit = {S: [] for S in maten}
    for r in regels[2:]:
        cellen = [c.strip() for c in r.strip().strip('|').split('|')]
        if len(cellen) != len(maten) + 1:
            raise SystemExit('rij met een ander aantal kolommen: ' + cellen[0])
        for S, c in zip(maten, cellen[1:]):
            uit[S] += [int(g) for g in re.findall(r'\d+', c)]
    for S, l in uit.items():
        if len(l) != len(NAMEN):
            raise SystemExit(f'maat {S}: {len(l)} getallen, verwacht {len(NAMEN)}')
    return uit

def map_voor(S):
    return 'resources' if S == BASIS else f'resources-round-{S}x{S}'

def main():
    toets = '--toets' in sys.argv
    blad = lees_blad(os.path.join(HIER, 'maten-tij-tabel.md'))
    fout = 0
    doelen = [(map_voor(S), l) for S, l in sorted(blad.items())] + [(f'resources-round-{BASIS}x{BASIS}', blad[BASIS])]
    for m, l in doelen:
        d = os.path.join(HIER, m, 'jsondata')
        tekst = json.dumps(l, separators=(',', ':'))
        xml = '<resources>\n    <jsonData id="Maten" filename="maten.json"/>\n</resources>\n'
        if toets:
            try:
                ok = open(os.path.join(d, 'maten.json')).read() == tekst and open(os.path.join(d, 'jsondata.xml')).read() == xml
            except OSError:
                ok = False
            print(('goed ' if ok else 'FOUT ') + m)
            fout += 0 if ok else 1
        else:
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, 'maten.json'), 'w').write(tekst)
            open(os.path.join(d, 'jsondata.xml'), 'w').write(xml)
            print('geschreven', m, len(l), 'getallen')
    if not toets:
        # De nummers voor Maten.mc, om naast de bron te leggen.
        print('    ' + '\n    '.join(f'const {n} = {i};' for i, n in enumerate(NAMEN)))
    sys.exit(1 if fout else 0)

if __name__ == '__main__':
    main()
