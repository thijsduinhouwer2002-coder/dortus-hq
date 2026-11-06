# Voorstel: Roblox Creator Store (betaalde plugins voor Roblox Studio)

**Advies: nog niet klaar. Cijfer: 4 van 10.** Geen manager en geen bouwwerk. Geschreven op 6 nov 2026, run 17:31 UTC.

Waarom: de betaalregeling is de beste die we tot nu toe zagen (100% van de netto opbrengst naar de maker, in dollars, via Stripe). Maar nieuwe betaalde plugins halen bijna niets aan zichtbare gebruikers, het aanbod is in een jaar ±10 keer zo groot geworden, en we vonden geen kleine nieuwe maker met aantoonbaar geld.

## Eigen meting (GEZIEN, 6 nov 2026)
Werkwijze: de openbare zoek-API van de Creator Store (`apis.roblox.com/toolbox-service/v2/assets:search`, categorie Plugin) met curl/python gelezen. Twee lijsten van elk het maximum van 1.000: alle betaalde plugins (filter prijs vanaf 1 cent) en alle plugins (standaardvolgorde). Data en scripts: `data/roblox-betaald-2026-11-06.json`, `data/roblox-betaald-feb-aug-2026-met-favorieten.json`, `data/roblox-haal-script.py`, `data/roblox-favorieten-script.py`.

Let op: de API geeft maximaal 1.000 resultaten in een volgorde die we niet kennen. Er zijn dus waarschijnlijk meer betaalde plugins dan 1.000.

**Bereik**
- De winkel toont geen installs of verkopen. Het veld "Sales" in de oude economy-API staat op 0, ook bij de bekendste betaalde plugin (GEZIEN).
- Wat wel zichtbaar is: stemmen (duim omhoog of omlaag), afgerond op één cijfer (10, 20, 100, 600, 1.000, 30.000), en favorieten. Onder ±10 stemmen toont de API 0. "Mediaan 0 stemmen" betekent dus: mediaan minder dan ±10 stemmen.
- Betaalde plugins gemaakt van feb tot aug 2026 (3 tot 9 maanden oud): **365 stuks, mediaan 0 stemmen. 8 hebben 10 of meer stemmen (2%), 1 heeft 100.** (GEZIEN)
- Favorieten bij dezelfde groep: 264 opgehaald, allemaal 0. Ook plugins met 100 stemmen hebben 0 favorieten, dus favorieten werken niet voor nieuwe plugins (GEZIEN). Bij de oude Moon Animator 2 staan er 41.233.
- Ook betaalde plugins van 2024 en eerder (198 stuks) hebben mediaan 0 stemmen. Stemmen zijn dus een grove maat. Hoeveel installs bij één stem horen weten we niet (GOK: tientallen).
- Mediaan en percentage 100+ installs: **niet te meten.** Sorteren op verkoop of installs geeft een fout in de API (controleur, GEZIEN). Alleen de maker ziet verkoop in zijn eigen dashboard ([aankondiging](https://devforum.roblox.com/t/analytics-top-selling-and-grossing-plugins-and-models-for-creator-store/3187401)).

**Drukte**
- Nieuwe betaalde plugins per maand in onze lijst (GEZIEN): jun 2025 9, dec 2025 14, mrt 2026 36, jun 2026 55, jul 91, sep 116, okt 156. Dat is ±10 keer zo veel als een jaar geleden, in onze lijst van maximaal 1.000. Omdat we de volgorde van de API niet kennen, kunnen recente plugins oververtegenwoordigd zijn (GOK).
- 211 makers voor 365 plugins (feb tot aug 2026). Eén maker heeft er 22, een andere 11 (GEZIEN). Wijst op makers die in serie bouwen, mogelijk met AI (GOK). Sommige makers zeggen er zelf bij dat AI hielp ([voorbeeld](https://devforum.roblox.com/search?q=Eclipse%20Animator)).

**Geld**
- Plugins worden verkocht in dollars, Roblox geeft **100% van de netto opbrengst** aan de maker, buiten de Robux-afdracht van 30% om. Betaling via Stripe, die btw en sales tax voor de koper berekent en valuta omrekent. Wat de verkoper zelf aan btw moet doen staat er niet in. Nederland werkt. [Aankondiging, apr 2024](https://devforum.roblox.com/t/creator-store-buy-and-sell-plug-ins-with-real-world-currency/2923445) (DERDEN). 100% netto opnieuw bevestigd in dec 2025, toen ook modellen betaald werden (https://devforum.roblox.com/t/4142112). Verkopen kan alleen vanaf een persoonlijk account met ID-verificatie.
- Prijzen (GEZIEN): mediaan $4,99, de middelste helft $4,99 tot $7,99. Laag: voor € 350 per maand zijn ±80 verkopen per maand nodig (GOK).
- Wie verdient: de best beoordeelde betaalde plugins zijn oud of van bekende makers. Moon Animator 2 (2020, $19,99, ±30.000 stemmen) is de duidelijkste. Eclipse Animator (okt 2026, $19,99, ±10.000 stemmen) lijkt nieuw, maar was bij de start een paar dagen gratis ([DevForum](https://devforum.roblox.com/search?q=Eclipse%20Animator)), dus de stemmen zeggen weinig over verkoop.
- Geen enkele kleine nieuwe maker gevonden met een bedrag. Op DevForum zochten we op "plugin sales", "paid plugin earnings", "my plugin sold" en "plugin revenue month" (sinds juni 2025): geen omzetcijfers, wel klachten over alleen dollars als betaalmiddel en een maker die over uitbetaling vraagt ([voorbeeld](https://devforum.roblox.com/t/i-cannot-cash-out-plugin-earnings/4605334)).

**Vindbaarheid**
- Plugins worden gevonden via de Toolbox in Roblox Studio en de Creator Store op de site. Volgorde onbekend. Grote spelers met een groep of YouTube-kanaal lijken te winnen (GOK).

**Past het bij ons**
- Plugins zijn Luau-code in Roblox Studio. Bouwen in 1 tot 2 weken kan (GOK), maar testen vraagt Roblox Studio (Windows of Mac) en een Roblox-account met Stripe van Thijs.
- Het publiek is jong, dat beperkt mogelijk de koopkracht (GOK).
- Sinds aug 2026 moet een account een leeftijdscheck hebben, minstens 2 dagen oud zijn en in orde zijn om te publiceren (https://devforum.roblox.com/t/4820095). Een topic uit 2025 noemt 2 plugins per maand zonder ID-verificatie, 10 met (https://devforum.roblox.com/t/3986362) (DERDEN).

## Voor
- Beste betaalregeling tot nu toe: 100% netto, dollars, Stripe regelt btw.
- Groot platform met veel makers die gereedschap nodig hebben.
- Animatie- en bouwgereedschap verkoopt bewezen, bij de grote namen.

## Tegen
- Nieuwe betaalde plugins: mediaan 0 stemmen, 2% haalt 10 of meer.
- Aanbod ±10 keer zo groot als een jaar geleden.
- Lage prijzen ($4,99), dus veel verkopen nodig.
- Geen bedrag van een kleine nieuwe maker te vinden.
- Jong publiek, en Roblox Studio hebben wij niet in de cloud.
- Sinds dec 2025 mogen ook modellen betaald verkocht worden: nog meer aanbod.
- Uitbetalingen gaan soms mis (DERDEN, DevForum 2026): openstaande omzet naar €0 (https://devforum.roblox.com/t/4709909, 30 jun), ±2,5 maand niet uitbetaald, laatste op 1 juli (https://devforum.roblox.com/t/4887569, 22 sep), laatste uitbetaling in juli (https://devforum.roblox.com/t/4965114, 29 okt).
- Gemelde truc waarbij kopers via terugbetaling gratis bij betaalde plugins komen (https://devforum.roblox.com/t/4695361).

## Eerste idee (als het later ja wordt)
Een betaald gereedschap voor makers van spellen dat in de Studio ontbreekt, in een categorie waar bekend geld zit (animatie, bouwen), maar dan voor een smalle taak waar de grote plugins niet op letten.

## Wat er nog gemeten moet worden (grens vooraf vastgelegd, GOK)
Het wordt pas ja als:
1. **Geld:** minstens 2 kleine makers die sinds 2025 begonnen zijn en $300+ per maand met plugins melden (DevForum, X, YouTube), liefst met een schermafdruk van het dashboard.
2. **Bereik:** een maat voor installs. Kan via een maker die zijn cijfers deelt, of als wij een gratis plugin uitbrengen en zelf meten.
3. **Past het bij ons:** Thijs kan Roblox Studio en een Stripe-account voor een Roblox-account regelen.

## Nakijken
Controleur akkoord (6 nov, run 17:31). Hij rekende de data na, testte de API en las de aankondiging. Hij zocht met 9 zoekopdrachten op DevForum en 3 op het web naar een kleine maker met $300+ per maand: niets gevonden. Wel: een maker die "a few copies" verkocht (https://devforum.roblox.com/t/4085004) en "200 Creator Store downloads" bij RoExpress (https://devforum.roblox.com/t/4646082). Acht correcties verwerkt. Beste route voor bereik blijft een eigen gratis plugin, als het ooit zover komt.
