# Vera 17 nov 2026: haal de lijst spellen van een thema-fest van Steam (de inhoudspagina van het fest).
# Werkt voor het Auto-Battler RPG Fest (16 tot 23 nov 2026), pagina store.steampowered.com/category/auto_battler_rpg/.
# Gevonden in de pagina zelf: data-community CLANACCOUNTID 41316928 en data-event ANNOUNCEMENT_GID 719039819889509999.
# De festinstellingen zeggen optin_only true (prune_list_optin_name sale_auto_battler_2026), dus GOK: dit zijn de deelnemers.
# Eén sortering mist apps (de volgorde schuift tijdens het bladeren), daarom drie sorteringen samen.
# Gebruik: python3 -I steam-fest-lijst-script.py uit.json   (rustig: 2 s tussen verzoeken)
import json, subprocess, sys, time

CLAN, GID, HUB = '41316928', '719039819889509999', 'auto_battler_rpg'

def haal(flavor):
    start, ids, mc = 0, [], None
    while True:
        u = ('https://store.steampowered.com/saleaction/ajaxgetsaledynamicappquery?cc=US&l=english'
             f'&clanAccountID={CLAN}&clanAnnouncementGID={GID}&flavor={flavor}&start={start}&count=100'
             f'&return_capsules=true&bForceUseSaleTag=true&strContentHubType=category&strContentHubCategory={HUB}')
        d = json.loads(subprocess.run(['curl', '-s', '--compressed', '-A', 'Mozilla/5.0', u],
                                      capture_output=True, text=True).stdout)
        a = d.get('appids', [])
        ids += a
        mc = d.get('match_count', mc)
        if not a or not d.get('possible_has_more'):
            return set(ids), mc
        start += 100
        time.sleep(2)

alle, mc = set(), None
for fl in ['popularpurchased', 'popularcomingsoon', 'price']:
    s, m = haal(fl)
    alle |= s
    mc = mc or m
korting, _ = haal('discounted')
binnenkort, _ = haal('popularcomingsoon')
uit = {'gehaald_utc': time.strftime('%Y-%m-%d %H:%M', time.gmtime()), 'match_count': mc,
       'alle': sorted(alle), 'met_korting': sorted(korting), 'binnenkort': sorted(binnenkort)}
json.dump(uit, open(sys.argv[1], 'w'))
print(f"match_count {mc}, gevonden {len(alle)}, met korting {len(korting)}, binnenkort {len(binnenkort)}")
