# Superhive: wat verkoopt er echt aan add-ons (opdracht hoofdchat 15 nov 20:20)

Vera, verkenner. Uiterlijk wo 18 nov 18:00. **Stand: tussenstand van run 15 nov 20:31.** De volledige meting loopt in GitHub Actions en is pas na deze run klaar; de volgende run vult de cijfers in, laat het nakijken en schrijft het advies definitief.

## Hoe gemeten
- Workflow `.github/workflows/verkenner-superhive.yml` draait `data/superhive-6mnd-script.py`: de lijst van alle add-ons op datum (nieuwste eerst), daarna elke productpagina. Rustig: 1 pagina per 2 seconden, alleen openbare pagina's, niet ingelogd. Per add-on: naam, maker, prijs, verkoopblok, ratings, categorie, "Published ... ago", Blender-versie, korte beschrijving. Stopt na 40 add-ons op rij die 7 maanden of ouder zijn.
- De CSV komt op de tak `verkenner-data` (`superhive/addons-6mnd.csv`), tussentijds elke 15 minuten. De volgende run zet hem ook hier als `data/superhive-addons-6mnd-2026-11-15.csv`.
- Analyse: `data/superhive-6mnd-analyse.py` (verdeling 0 tot 10, 10 tot 100, 100+ en 1000+, per leeftijd, mediane prijs, per soort en per Superhive-categorie, prijsklassen, makers, 3D-printen).
- Let op bij het lezen: Superhive toont het verkoopblok pas vanaf 10 verkopen ("10+", "100+", "2600+"). Geen blok betekent 0 tot 9. Het blok is een ondergrens, dus omzet die we eruit rekenen is ook een ondergrens. "Published" is grof (in maanden), dus leeftijd is ±een halve maand.

## Voorproef uit de meting van 9 nov (GEZIEN, `data/superhive-nieuwe-addons-2026-11-09.jsonl`, wordt vervangen)
Dezelfde analyse op de 2.955 add-ons van de meting van 9 nov, alles van 0 tot 6 maanden oud (2.154 betaald, 829 makers):
- Betaald: **79,5% onder 10 verkopen**, 17,5% 10 tot 99, 2,9% 100 tot 999, 0,2% 1000+ (4 add-ons).
- Na 2 tot 6 maanden is het iets beter: 57 tot 77% onder 10, 3 tot 6% 100+.
- Mediane prijs $12 (kwartielen $8 en $20). Duurder verkoopt niet slechter: $15 tot $30 haalt 37 tot 41% 10+ en 9 tot 10% 100+, onder $10 maar 20 tot 23% en 0,5%.
- Scheef: de top 10 makers hebben ±56% van alle verkopen (ondergrens in dollars). Milad Kambari alleen al 12%.
- 3D-printen is klein maar loopt het best per add-on: van 31 betaalde add-ons van 2 tot 6 maanden haalt 16% 100+ (gemiddeld 4 tot 5%).

## 3D-printen: Cleave naast Click Joints Pro (GEZIEN, productpagina 15 nov)
- **Cleave** (V4SS3UR, enige product van deze maker): $23, of $28 als steunversie. Sales 100+, 3 ratings, ±2 maanden oud. Het is vooral een **splitser**: grote STL's in printbare delen knippen langs natuurlijke naden, met per naad een pen (4 profielen, ook zwaluwstaart), deuvel, staafkanaal, magneetgaten of, sinds versie 1.6, een **kogelgewricht** (één kant of dubbel, passing Resin, FDM of eigen, met een "ghost" die laat zien waar het deel heen zwaait). Verder: 120+ printers ingebouwd met "past of past niet" per deel, platen inpakken, 3MF per plaat, Exploded View en Reassemble, reparatie van AI-modellen (Meshy, Tripo). Sterk en breed product.
- **Wat Cleave niet heeft (gelezen op de pagina):** geen bereik in graden, geen scharnier met eindstop, geen testkaartje voor de speling per printer. Precies de punten van Click Joints Pro.
- Andere print-add-ons van de laatste 6 maanden (meting 9 nov): Dovetail Key $18 800+ (Milad Kambari), CatPin $27 400+ (nu met korting $21,60; ook Business-licentie $90), Split-3DPrint $28 400+, JointLab $65 20+, Cut Flex $34,99 10+, SPLIT IT! $12 10+, Oryx CAD $14,99 10+, en een golf van één maker (Hanru Croucamp, 6 nieuwe add-ons van $3 tot $17 in twee dagen). Splitsen met verbinders is de print-klus die verkoopt; gewrichten alleen (JointLab $65) verkoopt veel minder.

## Nog te doen (volgende run)
1. Volledige CSV binnenhalen en in de repo zetten, analyse draaien, cijfers hierboven vervangen.
2. 3D-printen: lijst compleet maken met de nieuwe data (wie, prijs, verkopen per maand, wat ontbreekt).
3. Top 5 ideeën met bewijs, en het prijsadvies voor Click Joints Pro naast Cleave.
4. Controleur (agent) laat 10 rijen live nakijken en de analyse herrekenen.
