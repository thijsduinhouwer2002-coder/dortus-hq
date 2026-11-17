# Zet per horloge het startpictogram van Mila in de maat die dat horloge wil, zodat Garmin niet schaalt.
# Bron: iconen/icoon-<px>.png (kopie van ontwerp/garmin/tij/icoon/ op main; daar is Mila de baas) en
# iconen/maat-per-horloge.json (uit de regels LIMIET van de bouwstraat: "launcherIcon" in compiler.json van de SDK).
# Gebruik: python3 maak_iconen.py          schrijft resources-<horloge>/drawables/icoon.png en startpictogram.xml
#          python3 maak_iconen.py --toets  schrijft niets, faalt als een horloge uit het manifest geen passend pictogram heeft
import json, os, re, shutil, sys
from PIL import Image
HIER = os.path.dirname(os.path.abspath(__file__))
XML = '<drawables>\n    <bitmap id="LauncherIcon" filename="icoon.png"/>\n</drawables>\n'
BASIS = 40  # de map "resources": de maat van de meeste horloges, voor een horloge dat nog niet in de lijst staat


def main():
    toets = '--toets' in sys.argv
    maten = json.load(open(os.path.join(HIER, 'iconen', 'maat-per-horloge.json')))
    manifest = open(os.path.join(HIER, 'manifest.xml'), encoding='utf-8').read()
    horloges = re.findall(r'<iq:product id="([^"]+)"', manifest)
    fout = 0
    for h in horloges:
        if h not in maten:
            print('FOUT geen maat voor', h, '(zet hem in iconen/maat-per-horloge.json, uit de regel LIMIET van de bouwstraat)')
            fout += 1
    doelen = [('resources', BASIS)] + [('resources-' + h, maten[h]) for h in horloges if h in maten]
    for m, px in doelen:
        bron = os.path.join(HIER, 'iconen', 'icoon-%d.png' % px)
        if not os.path.exists(bron):
            print('FOUT geen pictogram van %d px voor %s' % (px, m))
            fout += 1
            continue
        if Image.open(bron).size != (px, px):
            print('FOUT', bron, 'is niet %d px' % px)
            fout += 1
            continue
        d = os.path.join(HIER, m, 'drawables')
        doel = os.path.join(d, 'icoon.png')
        xml = os.path.join(d, 'startpictogram.xml')
        if toets:
            try:
                ok = open(doel, 'rb').read() == open(bron, 'rb').read() and (m == 'resources' or open(xml).read() == XML)
            except OSError:
                ok = False
            if not ok:
                print('FOUT', m, 'heeft niet het pictogram van %d px' % px)
                fout += 1
        else:
            os.makedirs(d, exist_ok=True)
            shutil.copyfile(bron, doel)
            if m != 'resources':
                open(xml, 'w').write(XML)
    print(('toets: ' if toets else 'geschreven: ') + '%d mappen, %d fout' % (len(doelen), fout))
    sys.exit(1 if fout else 0)


if __name__ == '__main__':
    main()
