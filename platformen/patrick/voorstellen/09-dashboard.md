Wat verandert: het dashboard voor Thijs toont bovenaan uitkomst (gebruikers en geld tegen het tussendoel) in plaats van drukte (commits), en per product de lanceerdatum en waar het op wacht. Kleine aanpassing in `dashboard/bouw.py` en `dashboard/sjabloon.html`; geen Claude nodig om het te bouwen (dat blijft zo, en dat is goed).
Waarom: het kopcijfer is nu "commits vandaag" (511 op 9 nov, `data.json`). Dat beloont drukte. Thijs wil in één blik zien of we geld gaan verdienen. Anthropic: geef iets wat geslaagd of mislukt teruggeeft (bron 20); LangChain: één inbox voor de mens (bron 26). Wat al goed is: "Wacht op jou" staat bovenaan, de cijfers van Obsidian en JetBrains komen rechtstreeks uit hun openbare API's, en het wordt elk half uur door GitHub Actions gebouwd zonder verbruik.

---

## 1. Nieuwe bovenste rij: "Op weg naar 20 december"
Drie getallen naast elkaar, met het doel eronder:
- **Gebruikers (alle producten samen):** som van de downloads/installs die bouw.py al ophaalt (Obsidian, JetBrains, later Blender, Steam, Garmin). Doel: 1.000 in één product.
- **Betalende klanten:** uit de `Cijfers:`-regel in elke `status.md` (sjabloon voorstel 03). Doel: eerste.
- **Euro per maand:** idem. Doel: € 100.
Plus één woord: **op koers / achter / ver achter**, uit de eerste regel van het laatste rapport van Hans.

## 2. Per product: lanceerdatum en "wacht op"
Lees uit `status.md` (sjabloon 03) de regels `- Lanceerdatum (richt):` en `- Wacht op:`. Toon per product: fase, lanceerdatum met "nog N dagen" (rood als voorbij), en "wacht op Thijs / keuring / niets". Zo ziet Thijs meteen dat Click Joints en Bison & Flex al sinds 8 nov op een keuring wachten.

Code (in bouw.py, naast `eerste_stand`):
```python
def regel(pad, sleutel):
    for r in lees(pad).splitlines():
        if r.startswith(f"- {sleutel}:"):
            return schoon(r.split(":", 1)[1], 120)
    return ""
# in de lus over config["producten"]:
#   "lancering": regel(p["status"], "Lanceerdatum (richt)"),
#   "wacht_op":  regel(p["status"], "Wacht op"),
#   "cijfers":   regel(p["status"], "Cijfers"),
```

## 3. Ploeg: laatste uitkomst in plaats van aantal commits
Vervang "vandaag: 66 commits" door de regel `- Laatste uitkomst:` uit de `status.md` van die persoon (veld `status` toevoegen aan elke persoon in `ploeg.json`). Wie 3 uur actief is zonder dat die regel verandert, krijgt een oranje stip "geen uitkomst sinds ...". Dat is wat Hans nu met de hand zoekt ("draait iemand rondjes").

## 4. Kopcijfer "commits vandaag" weg
Uit `samenvatting` en de kop van de pagina. Mag onderaan blijven voor wie het wil zien.

**Werk:** ±1 uur voor de hoofdchat (of een bouwer). **Gewoon goed.** Hangt af van voorstel 03 (status.md-sjabloon); zonder dat sjabloon blijven de nieuwe velden leeg en toont de pagina "nog niet ingevuld".
