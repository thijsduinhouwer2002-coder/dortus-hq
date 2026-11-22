# Herweging: Garmin Connect IQ, betaalde apps en datavelden

Kees, 9 nov 2026, run 16:23 UTC. Oud cijfer 5 (Vera, 6 nov, `platformen/verkenner/voorstellen/garmin-connect-iq.md`). Nagekeken door een controleur (eigen volledige ophaal van 45.052 apps): getallen kloppen, één correctie op de gratis-eerst-telling, verwerkt.

## De doorslaggevende meting
Vera liet Garmin op 5 staan om één vraag: **is een download van een betaalde app een verkoop?** Als ja, dan laat de winkel zelf zien hoeveel nieuwe betaalde apps verkopen. Ik heb dat op drie manieren getest.

1. **Regels (DERDEN, makers en Garmin op het forum):** de koper betaalt vóór het downloaden, er is geen proefversie of kopen binnen de app in Garmin Pay, één aankoop geldt per account voor alle horloges (officieel antwoord ConnectIQAppAdmin, forumdraad 403756). Van gratis naar betaald mag, met nieuwe keuring; oude gratis downloads blijven dan waarschijnlijk in de teller (GOK).
2. **Overstap gratis naar betaald, gemeten (GEZIEN):** 3.814 niet-wijzerplaten uit beide eigen metingen (6 en 9 nov) naast elkaar: 720 betaald op beide dagen, **0** gingen van gratis naar betaald of terug. Dat is maar 3 dagen, dus alleen een aanwijzing.
3. **Reviews van alle 204 betaalde niet-wijzerplaten uit 2026 met 100+ (GEZIEN):** in 5 zie je dat ze eerst gratis waren (allemaal spelletjes: Crossy Road 3D, Stack van MangoIQ, Google Dinosaur Game, Voidrunner Arcade, Ball Sort). De controleur vond er een zesde: Stack - Blocks Game van garminland (10.000+), ook een spel. Bij de sport-, meet- en hulpapps geen enkele aanwijzing. Ruwe uitkomst: `data/garmin-reviews-gratis-eerst-2026-11-09.json`.
4. **Eén maker met eigen cijfers:** Ski Pin, 68 verkopen in januari, winkel nu 100+ (DERDEN plus GEZIEN). Klopt.

**Uitkomst:** bij een hulp- of sportapp die vanaf het begin betaald is, is de emmer ongeveer het aantal kopende accounts (een ondergrens van de emmer, min een paar terugbetalingen binnen 48 uur). Bij spelletjes niet: daar begint een flink deel gratis. Ook let op: veel makers zetten een gratis en een betaalde versie naast elkaar (Flight Scanner, Rampo, FikirLtd), en Run Cue (FikirLtd, 1.000+ in een maand met 1 review) is verdacht.

## Wat dat zegt over geld (GEZIEN, data 9 nov, zonder de 6 gratis-eerst-spellen en zonder externe abonnementen)

| Betaalde niet-wijzerplaten, eerste goedkeuring | n | 10+ | 100+ | 1.000+ | prijs mediaan |
|---|---|---|---|---|---|
| jan t/m 8 mei 2026 (6 tot 10 maanden) | 95 | 84% | 57% | 15% | $2,49 |
| idem, kleine makers (max 5 apps in 2026) | 45 | 82% | 51% | 7% | $2,99 |
| 9 mei t/m 9 aug 2026 (3 tot 6 maanden) | 132 | 71% | 36% | 5% | $2,25 |
| idem, kleine makers | 48 | 73% | 38% | 2% | $2,25 |

Controleur (eigen ophaal): 252 apps jan t/m 9 aug, 43% 100+, 10% 1.000+.

In geld, met 85% voor de maker en de emmer als ondergrens (GOK op GEZIEN):
- **100+** (36 tot 57%): minstens ±$190 tot 250 in totaal. Merkbaar, maar klein.
- **Boven ±$300 per maand**, hulp- en sportapps die betaald begonnen: Flight Scanner Pro ($2,99, aug, 1.000+: ±$850 per maand), Ping Pong, Hybrid en Pickleball Smash van Multipassionate ($8,49, elk ±$700 per maand of meer), Peak Finder Compass ($3,49, mei, ±$500), RuckTrack ($2,99, apr, ±$350). Dus een paar, vooral makers met meerdere apps.

## Nieuw cijfer: 7 (was 5)
- Punt 1 (nieuwe kleine makers verdienen nu): **ja, krap.** Downloads van betaalde hulpapps zijn kopers; 36 tot 57% haalt 100+, een paar zitten boven $300 per maand. Maar de bedragen zijn klein (mediaan $2,25) en bij kleine makers haalt maar 2 tot 7% de 1.000+.
- Punt 2 (bereik voor nieuwkomers): **ja.** Zoeken op sport en functie werkt, lijsten nieuw en hot & fresh (Vera).
- Punt 3 (bouwen en testen): **ja, met moeite.** Monkey C en de SDK draaien op Linux, bouwen kan in GitHub Actions; testen op veel horlogemodellen alleen via de simulator (GOK).
- Punt 4 (Thijs kan binnen een week verkopen): **ja.** Particulier in Nederland mag zonder bedrijf (Garmin-medewerker op het forum, draad 428218), $100 per jaar, ID, BSN-bewijs en adres via Adyen, uitbetaling maandelijks vanaf €10 (GEZIEN in de onboarding-pagina van Garmin). Dit zijn invulstappen van Thijs zelf.

Waarom geen 8: punt 1 is er, maar dun. Voor €350 per maand zijn ±140 verkopen per maand van $3 nodig, dat is een app op 1.000+ per kwartaal blijven halen; dat lukt 2 tot 7% van de nieuwe apps van kleine makers. Steam (8 krap) geeft per geslaagde app meer geld. Waarom wel een 7: de grootste twijfel van Vera is weg, en de rest (bereik, kosten, papieren) is goed.

## Wat nog schuurt
- Bedragen per verkoop klein; succes hangt aan één nichefunctie (Hyrox, padel, vluchten, rucking).
- Spelletjes vallen af als meetgroep en als product (gratis eerst is daar gewoon).
- Betalen werkt alleen op nieuwere horloges, Nederlandse debitkaarten passen vaak niet in Garmin Pay (DERDEN).
- Herhaalmeting rond 9 dec: dezelfde apps opnieuw ophalen; een betaalde hulpapp die van 100+ naar 1.000+ gaat zonder gratis-klachten is het sterkste bewijs. Script: Vera's `platformen/verkenner/data/garmin-kans-haal.py`.
- Als Hans Garmin opent: het product uit `platformen/verkenner/kansen/garmin-zwakke-nummer-een.md` (loopband-app) is een hulp- en sportapp, dus precies de groep waar downloads verkopen zijn.
