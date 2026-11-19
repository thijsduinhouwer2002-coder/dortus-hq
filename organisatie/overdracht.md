# Overdracht: begin hier (bijgewerkt 18 nov 2026, 19:30 NL)

**Stand 19 nov 2026: dit bestand is historie. Wat geldt staat in `CLAUDE.md`, `organisatie/bord.md` en bovenaan `organisatie/besluiten.md`; die gaan voor alles hieronder.** Hoofdzaak is snel veel geld verdienen (niet meer nieuwe platformen vinden), hoofdproduct Click Joints Pro. Het account is van Thijs zelf (geen gedeeld account meer); welke koppelingen mogen staat in CLAUDE.md regel 7. De herinneringen en taak-id's hieronder zijn oud: kijk met list_triggers wat er echt draait.

**Sinds 18 nov 19:30 is de werkwijze omgebouwd** (besluit onderaan `organisatie/besluiten.md`): `CLAUDE.md` is een korte wegwijzer, de geldende besluiten staan bovenaan `organisatie/besluiten.md` (oude in `organisatie/archief/`), de regels per onderwerp in `organisatie/regels/`, en opdrachten voor geplande agents volgen `organisatie/sjablonen/agent-opdracht.md`. Zet je een agent weer aan, herschrijf zijn opdracht dan eerst naar dat sjabloon.

**Nieuwe hoofdchat? Lees eerst `CLAUDE.md` en daarna `organisatie/bord.md`.** Het bord is de stand op één plek: producten, agents, herinneringen, beloftes. Daarna `organisatie/lijst-thijs.md` (max 5) en de geldende besluiten bovenaan `organisatie/besluiten.md`.

**Koers sinds 17 nov 16:47: `organisatie/koers-kingmaker.md`.** Lees die direct na dit bestand. Hij gaat voor oudere regels waar die botsen.

**Wie de hoofdchat is (Thijs, 17 nov 16:35):** zijn compagnon. Kritisch, commercieel en gedurfd. Houdt alles bij (bord) en denkt uit zichzelf mee: komt zelf met wat er beter moet en waar het geld zit, wacht niet tot Thijs vraagt. Het doel is iets opbouwen waar veel geld mee te verdienen is. Tijd voor geld (maatwerk, freelance, opdrachten) doen we niet.

Eerste taak van een nieuwe hoofdchat:
1. Maak de losse herinneringen uit deel 3 van het bord opnieuw aan met send_later. De oude hangen aan de vorige chat (sessie van 17 nov) en komen daar binnen, niet in de nieuwe: avondcheck vandaag 20:00, Superhive-check wo 18 nov 10:30, Steam-app met Thijs wo 18 nov 12:00. Daarna de oude uitzetten (Avondcheck trig_01WhKTqEqGrpKWEdM28S7oXe, Superhive trig_012JkpmK4SCAySWA2FXWBmmX, Steam trig_01K545VbuHDjt5EYqtWgcypH, Abel trig_01C8MjM8mdFitn3ABamFi5Ve mag weg).
2. Antwoord Thijs nooit uit je hoofd: lees eerst het bord of het bestand in de repo. Zeg nooit "in dit gesprek niet gevonden": zoek in de repo.
3. Lessen van 17 nov: elk idee eerst door `organisatie/ideeentest.md`; wat het apparaat of platform zelf al kan is vraag 1. Ebb, Ebb Calm en de spraakmemo zitten ingebouwd in Garmin; Rollwright, Bison & Flex en Click Joints hadden bestaande concurrenten.

Wat hieronder staat is de oude overdracht van 6 nov, alleen als achtergrond.

---

# Overdracht (6 nov 2026, 15:00)

Voor elke Claude die in een nieuwe chat aan Dortus gaat werken. Lees daarna `CLAUDE.md`.

## Wat er staat
- **De ploeg draait.** Strateeg 07:44, Obsidian-, JetBrains-manager en verkenner elk uur van 08:00 tot 20:00, hoofdmanager met dagrapport om 20:44. Allemaal geplande taken in Claude, op Opus 5.5, Auto, in de cloud. De opdrachten staan in `organisatie/geplande-taken.md`.
- **Doelen:** zie `organisatie/doelen.md` (€ 300 tot 400 per maand in maart 2027, € 1.000 in nov 2027, € 2.000 tot 3.000 in nov 2028).
- **Nieuwe platformen vinden is de hoofdzaak.** Atlassian is gestopt. Geen oude apps overzetten.
- **Website:** dortus.com (repo `thijsduinhouwer2002-coder/dortus`), alleen in eigen productmappen werken. Support: support@dortus.com.
- **Middelen en inlogs:** `organisatie/middelen.md`.

## Wat we vandaag leerden
- Een geplande taak krijgt de repo-toegang die de chat had bij het aanmaken. Daarom: taken altijd aanmaken vanuit een chat die beide repo's met push heeft.
- `add_repo` bestaat niet altijd in een geplande run. De eerste stap is daarom: "Staat dortus-hq er al, gebruik die. Zo niet, koppel met add_repo."
- De status "geslaagd" van een taak zegt niets over opslaan. Elke run sluit af met `git ls-remote`.
- Claude in Chrome werkte vanuit de projectchat op Thijs' HP (Browser 2, deviceId 869e8714-0c9c-4923-be63-c9ffa1fecfc0), ingelogd op GitHub. Of geplande runs Chrome ook kunnen gebruiken, werd om 14:50 getest (taak "Dortus test: browser vanaf de HP"). Uitkomst: nog niet verwerkt.

## Thijs
- Ondernemer, dit is zijn fulltime werk. Durft ergens voor te gaan.
- Wil eerlijkheid en onderbouwing, maar niet te snel afschieten. Een 7 op 10 is top.
- Kies, onderbouw, en vraag alleen in nood.

## Nog open
- **Gedeeld account:** het Claude-account is nu van de vader van Thijs mee. Dat verandert. Krijgt Dortus een eigen account, dan moeten alle geplande taken daar opnieuw gemaakt worden vanuit een chat met beide repo's op push (zie `organisatie/geplande-taken.md`), en moet de cloudomgeving daar ook op Network access Full.
- Uitkomst van de Chrome-test verwerken. Werkt het: managers mogen zelf indienen en publiceren via de officiële weg.
- Repo dortus-hq op privé zetten (Thijs), na het eerste dagrapport.
- Koppelingen Gmail, Shopify, Trello en Kondo weghalen bij de geplande taken (Thijs, in de app).
- Thijs vult aan in `middelen.md`: waar het domein staat, welke mailaanbieder, of hosting GitHub Pages is.
