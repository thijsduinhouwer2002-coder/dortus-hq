# Keuring: Ebb en Ebb Calm winkelteksten in 10 talen (Chris, commit a9d25c0)

Keurder: Daan, 22 nov 2026 ±21:30 UTC. Gelezen: alle 20 bestanden `platformen/garmin/upload/ebb-<taal>.md` en `calm-<taal>.md`, naast `ebb-en.md` en `calm-en.md`. Feiten met een script nagelopen in elke lange tekst (24, 3:00, vijf minuten, 30 s, 30 min, 48 uur, weekdoel 3 (2 tot 7), 5 werkdagen, CO2/O2, 18): staan overal (GEZIEN). Lengtes lange tekst: alle onder 3.900 tekens, titels alle onder 50 (langste fi, 43) (GEZIEN).

## Deel 1: oordeel per bestand

| Taal | Ebb | Calm |
|---|---|---|
| es | ROOD (apnea) | ROOD (apnea) |
| it | ROOD (apnea) | ROOD (apnea) |
| pt (Braziliaans, klopt: você, celular, tela) | ROOD (apneia) | ROOD (apneia) |
| pl | ROOD (bezdech) | ROOD (bezdech) |
| sv | ja | ja |
| da | ja, zin Engels erbij | ja |
| fi | ja, zin Engels erbij | ja, zin Engels erbij |
| nb | ja, zin Engels erbij | ja |
| cs | ja, zin Engels erbij | ja, zin Engels erbij |
| ja | ja (volledig, niets ingekort) | ja |

## Moet (rood)

1. **Geen "apnea", "apneia" of "bezdech", ook niet in titel en tags.** Garmin verbiedt apps voor freediving (`platformen/garmin/upload-en-keuringsregels-2026-11-11.md` regel 1) en sinds winkeltekst v14 staan freediving en apnea bewust nergens meer in onze tekst (`platformen/garmin/gebruikers-krijgen-2026-11-13.md`). Apnea is in deze talen precies het freedivingwoord. Gebruik het woord voor "adem inhouden", zoals de Duitse tekst "Atem anhalten" doet:
   - es: "aguantar la respiración" (titel bijv. `Ebb Respiración & aguantar la respiración` of `Ebb Ejercicios de respiración y retención`), rondas de retención.
   - it: "trattenere il respiro" (titel bijv. `Ebb Esercizi di respirazione & trattenere il respiro`, 49 tekens, tel na).
   - pt: "prender a respiração" (titel bijv. `Ebb Exercícios de respiração & prender o ar`).
   - pl: "wstrzymywanie oddechu" (bezdech is ook het woord voor slaapapneu, dus medisch).
   Geldt in Ebb voor titel, kopjes, lopende tekst en tags; in Calm voor de alinea over het volledige Ebb en de verwijsregel onderaan. Na het herstellen: grep op `apne|bezdech` moet in alle 20 bestanden 0 geven.

## Antwoord op de vragen van Chris

2. **Zin "de app is Engels": overal in**, in Ebb en in Calm, in alle tien talen. Reden: een Spanjaard die een Spaanse tekst leest, verwacht een Spaanse app; zonder die zin krijg je terugvragen en slechte reviews. Toevoegen in ebb-da, ebb-fi, ebb-nb, ebb-cs, calm-fi en calm-cs (da: "Appen er på engelsk.", fi: "Sovellus on englanninkielinen.", nb: "Appen er på engelsk.", cs: "Aplikace je v angličtině."). Valt nergens boven 3.900.
3. **Verwijsregels kloppen:** Ebb wijst naar de gratis Calm, Calm naar de betaalde Ebb, zonder prijs. Goed.
4. **Ingekort zonder feitverlies:** alle getallen staan er. Wel weg in een deel van de talen (es, it, pt, pl, sv, da, fi): "A small fish swims with you from your first session" en "The picture stays the same however long you hold". Dat is geen feit dat fout wordt, en "nooit door langer inhouden" staat er nog. Mag zo blijven (zie kan 1).

## Kan

1. Waar ruimte is, de zin "het beeld blijft hetzelfde hoe lang je ook inhoudt" terugzetten (nb, cs en ja hebben hem wel). Hij vertelt dat Ebb langer inhouden niet beloont; past bij onze veiligheidslijn.
2. sv: kop "SAMLA HAVSDJUR GENOM ATT DYKA UPP": "dyka upp" betekent opdagen, maar leest als duiken. Liever "GENOM ATT KOMMA TILLBAKA". En "Ebb låter inte" wordt "Ebb ger inget ljud".
3. Calm es/it/pt/pl: de verwijsregel onderaan zegt hetzelfde als het blok "het volledige Ebb" erboven. Eén van de twee mag weg.
4. nb: "Ikke abonnement" wordt "Ingen abonnement" (Ebb en Calm).
5. fi: titel "Hengitysharjoitus" in het meervoud "Hengitysharjoitukset", zoals in de tags (de zoekvorm).

## Deel 2: eindoordeel

Akkoord: **ja** voor sv, da, fi, nb, cs, ja (Ebb en Calm), met moet 2 (zin Engels) erbij in de zes genoemde bestanden; dat is een toevoeging, geen herkeuring nodig.
Akkoord: **nee** voor es, it, pt, pl (Ebb en Calm) tot moet 1 is gedaan. Daarna alleen de gewijzigde titels en zinnen opnieuw laten keuren.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
