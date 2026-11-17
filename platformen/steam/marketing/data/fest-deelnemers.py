# Sem, run 20 (17 nov 2026): wie doet echt mee aan een thema-fest van Steam?
# WERKT NOG NIET BETROUWBAAR (GEZIEN 17 nov 07:00 UTC): match_count springt per verzoek en per pagina tussen 524, 773 en 1.634
# (start=0 gaf beide 524 en 1.634; start=50 gaf 773; start=100 gaf 1.634). Eerste lijst (565) was dus een mengsel. Niet gebruiken
# als bewijs tot het eerlijk werkt; op 14 jan opnieuw proberen of met de hand tellen in de pagina.
# De festpagina (store.steampowered.com/category/<naam>/) is een tagpagina; wie zich aanmeldde (opt-in) staat in het vak
# "sale_item_browser". Die lijst haalt de pagina zelf op via saleaction/ajaxgetsaledynamicappquery met optin_only=true
# (gevonden door de pagina te openen in Chromium en de verzoeken te bekijken). Openbaar, alleen lezen, 1 verzoek per seconde.
# Gebruik: python3 fest-deelnemers.py <clanAccountID> <clanAnnouncementGID> <categorie> <optin_naam> <optin_tagid> <uit.txt>
# Auto-Battler RPG Fest 2026: 41316928 719039819889509999 auto_battler_rpg sale_auto_battler_2026 1407724
# Voor ons fest (14 jan) staan de waarden in data-event en data-partnereventstore van de festpagina.
import json,sys,time,urllib.request
clan,gid,cat,naam,tag,uit=sys.argv[1:7]
B=('https://store.steampowered.com/saleaction/ajaxgetsaledynamicappquery?cc=US&l=english'
   f'&clanAccountID={clan}&clanAnnouncementGID={gid}&tabuniqueid=6&sectionuniqueid=94134&flavor=contenthub_all&return_capsules=true'
   f'&strContentHubType=category&strContentHubCategory={cat}&bContentHubDiscountedOnly=false&strTabFilter='
   f'&prune_list_optin_name={naam}&optin_tagid={tag}&optin_only=true&bUseCreatorHomeApps=false&bAllowDemos=true')
# Let op (GEZIEN 17 nov): dezelfde vraag geeft afwisselend twee antwoorden. De ene server past de aanmeldfilter toe
# (Auto-Battler: 524), de andere niet en geeft de hele tagpagina (1.634, met spellen die zich niet aanmeldden).
# Daarom: per pagina opnieuw vragen tot match_count het kleinste getal is dat we zagen.
def haal(s):
    d=json.load(urllib.request.urlopen(urllib.request.Request(B+f'&start={s}&count=50',headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
    time.sleep(1); return d
kleinste=min(haal(0)['match_count'] for _ in range(6))
ids=[]
for s in range(0,3000,50):
    for _ in range(12):
        d=haal(s)
        if d['match_count']==kleinste: break
    else: sys.exit('geen antwoord met de filter voor start=%d'%s)
    a=d.get('appids',[]); ids+=a
    if len(a)<50: break
ids=list(dict.fromkeys(ids)); open(uit,'w').write('\n'.join(map(str,ids))+'\n'); print(len(ids),'deelnemers, match_count',d.get('match_count'))
