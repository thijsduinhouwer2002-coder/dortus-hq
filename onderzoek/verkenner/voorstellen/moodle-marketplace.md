# Voorstel: Moodle Marketplace (betaalde plugins voor de leeromgeving Moodle)

Vera, 8 nov 2026 run 09:33 UTC. Doorgegeven door Noor (pionier): "net geopend voor betaalde plugins, platform oud, eerder iets voor Vera".

## In het kort
- **Advies: nog niet klaar, cijfer 5.** Herhaalmeting rond 8 dec 2026 met dezelfde scripts.
- Moodle is groot en stabiel (±150.000 geregistreerde sites, scholen, universiteiten en bedrijven). Sinds 20 juli 2026 kun je in de officiële winkel betalen, met 20% afdracht in het eerste jaar.
- Bereik voor **gratis** nieuwe plugins is redelijk: zonder overgekomen oude plugins mediaan 32 installaties, 15% haalt 100+ (GEZIEN, steekproef 39).
- Bereik voor **betaalde** nieuwe plugins is slecht: mediaan 3 installaties, 1 van 67 haalt 100+ (GEZIEN).
- Geld bij kleine makers is nog niet aangetoond: geen enkel bedrag van een maker gevonden. Wel signalen: twee solo-makers met een nieuwe plugin van $999 per jaar en $99 per maand hebben elk 13 tot 14 installaties (GEZIEN, maar installatie is niet hetzelfde als betaald).

## Wat ik gemeten heb
Bron: de open lijst `download.moodle.org/api/1.3/pluglist.php` (3.248 plugins, met `isPaid` en datum per versie; die host heeft geen robots.txt) en daarna per plugin de openbare pagina op marketplace.moodle.com (robots.txt staat alles toe, crawl-delay 10 s, die heb ik aangehouden). Elke pagina toont **Installations** en **Downloads (last 90 days)** en de prijzen.
moodle.org zelf heb ik niet gelezen: robots.txt zegt `Content-Signal: ai-input=no` en er staat een captcha voor.

Bestanden in `data/`: `moodle-pluglist-2026-11-08.json`, `moodle-marketplace-betaald-2026-11-08.jsonl` (alle 130 betaalde), `moodle-gratis-steekproef-2026-11-08.jsonl` (44 gratis plugins, willekeurig uit de 261 met eerste versie mrt t/m jul 2026), script `moodle-marketplace-haal-script.py`.

### Betaalde plugins (alle 130, GEZIEN)
| Groep | Aantal | Mediaan installaties | 10+ | 100+ | Mediaan downloads 90 dagen |
|---|---|---|---|---|---|
| Nieuw na de lancering (id 3900 en hoger) | 67 | 3 | 14 | 1 | 0 |
| Daarvan eerste versie jul of aug 2026 (3 tot 4 maanden oud) | 19 | 5 | 7 | 0 | |
| Vroege inschrijvers (id onder 3900, eerste versie in de lijst 2014 t/m sep 2026, vaak oude producten die overkwamen; 1 zonder telling) | 63 | 7 | 25 | 12 | |

- De grote aantallen zitten bij oude namen die naar de winkel overkwamen: Edwiser RemUI 4.208, Mb2 Builder 3.672, Edwiser Page Builder 3.264, New Learning (Mb2nl) 3.706, Lambda 3.189, Tiny Font Size 2.914, Booking 1.579 (GEZIEN). Die installaties tellen waarschijnlijk ook oude gratis versies en eerdere kopers, dus het zijn geen verkopen (GOK).
- De 19 nieuwe van jul en aug: 0, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 13, 14, 14, 15, 15, 15, 31 installaties (GEZIEN).
- Beste nieuwe plugins van makers met een persoonsnaam (of het echt solo-makers zijn is niet nagekeken): Modern Commerce (Adebare Showemimo, $999 per jaar, 13 installaties, 82 downloads in 90 dagen) en Collaborative Whiteboard (Antonio Godoy Pellini, $99 per maand of $1.000 per jaar, 14 installaties, 74 downloads) (GEZIEN). Als de helft van die installaties betaalt, is dat ±$6.000 tot $7.000 per jaar per plugin (GOK, niet bewezen; downloads tellen ook updates en proefversies).
- Tiny Font Size en Tiny Font Family (Finspire, $7 per maand) halen 364 en 192 downloads in 90 dagen (GEZIEN). Let op: downloads zeggen bij betaalde plugins weinig (mediaan 0, en mod_aiactivities heeft 14 installaties en 0 downloads), dus dit is geen bewijs van verkoop. Finspire is een bedrijf en de installaties stammen waarschijnlijk van vóór de winkel (GOK).

### Gratis nieuwe plugins (steekproef 45 van 261, eerste versie mrt t/m jul 2026, 44 met telling, GEZIEN)
- Alle 44: mediaan 43,5 installaties, 33 halen 10+, 10 (23%) halen 100+. Mediaan downloads in 90 dagen 95,5.
- Maar 6 daarvan zijn oude plugins waarvan de versiegeschiedenis bij de overstap opnieuw begon (id 97, 129, 3050, 3148, 3156, 3191; bijvoorbeeld mod_supervideo 4.719). Zonder die 6: 39 plugins, mediaan 32, 29 halen 10+, **6 van 39 (15%) halen 100+**. Ook de maandtabel hieronder telt een paar van zulke oude plugins mee.
- Eerlijke vergelijking op gelijke leeftijd: betaald jul en aug mediaan 5 (19 plugins) tegen gratis jul mediaan 61 (9 plugins). Het gat is groot.
- Beheerders vinden en installeren nieuwe gratis plugins dus wel. Dat ze voor betalen afhaken is een uitleg, geen meting (GOK).

### Drukte (GEZIEN, eerste versie per plugin in de lijst)
| Maand 2026 | Nieuw gratis | Nieuw betaald |
|---|---|---|
| mrt | 61 | 7 |
| jun | 56 | 14 |
| aug | 74 | 21 |
| sep | 96 | 17 |
| okt | 194 | 32 |
In 2025 was het ±20 tot 30 per maand. Oktober is een golf, met opvallend veel AI-plugins van een paar makers: LMS Labs (LMS Hosting Services) heeft 14 betaalde plugins, Jesus Antonio Jimenez Aviñ 7 (GEZIEN). De winkel wordt dus snel drukker.

## Nakijken
Controleur akkoord met correcties (8 nov): alle tellingen herrekend, 6 van 6 pagina's live gelijk. Verwerkt: mediaan 19 is 5, gratis 33 keer 10+, vroege inschrijvers 25 keer 10+, 23 met gratis optie, RemUI en Mb2 Builder toegevoegd, oude plugins uit de gratis steekproef gehaald (15% in plaats van 23%), vergelijking op gelijke leeftijd, downloads niet als geldsignaal, bron 1.517 verbeterd.

## Bronnen van derden (onderzoeker, nagekeken waar mogelijk)
- Lancering 20 juli 2026 (DERDEN, https://moodle.com/news/moodle-marketplace-is-here/, nagekeken). 1.517 vermeldingen bij de start en inschrijving betaald sinds 26 feb 2026 komen alleen van https://ldesignmedia.nl/en/blog/moodle-marketplace-is-here (DERDEN). De moodle.com-pagina noemt geen afdracht. De winkel **vervangt** de oude Plugins Directory: gratis en betaald in één catalogus.
- Afdracht 20% in het eerste jaar, daarna 25% (DERDEN, https://www.diegomonroydev.es/en/blog/moodle-marketplace-what-it-is-and-how-it-affects-you, die het moodle.org-nieuws citeert; niet uit eerste hand).
- Afrekenen via Stripe Connect op de winkel, maar **de maker is verkoper** (Merchant of Record): eigen verkoopvoorwaarden, btw en facturen. Licenties beheert de winkel niet, die bouw je zelf (DERDEN, https://pimenko.com/en/moodle-marketplace-user-experience-feedback/; "the seller's Terms of Sale" GEZIEN op de pagina's).
- Betaalde plugins worden door Moodle HQ gekeurd en elk jaar opnieuw ("Reviewed annually for quality", GEZIEN). Verplicht: Privacy API, publieke issuetracker, tests verwacht. Plugins die concurreren met Moodle Workplace worden geweigerd (DERDEN, https://moodledev.io/general/community/plugincontribution/checklist). Doorlooptijd keuring en een regel over AI-code: niet gevonden.
- ±148.835 geregistreerde sites op 20 okt 2026, +1.800 in een maand (DERDEN, https://cubite.io/blogs/moodle-version-census). moodle.com noemt 153.997+ sites en 500 miljoen+ gebruikers (DERDEN, https://moodle.com/).
- Prijzen: kleine plugins $5 tot $50, midden $59 tot $99 per jaar, thema's $59 tot $149 eenmalig (DERDEN, catalogus; komt overeen met mijn eigen data).

## Voordelen
- Kopers zijn instellingen met budget, gewend om per site per jaar te betalen ($25 tot $999 per jaar). Weinig klanten zijn genoeg: 100 sites van $49 per jaar is ±€300 per maand na afdracht (GOK).
- Officiële winkel met betalen, jong (3,5 maand), en de zoekfunctie in de winkel laat nieuwe plugins zien (recent bijgewerkt eerst).
- Gratis plugins krijgen bereik (mediaan 32 zonder oude plugins). Een gratis plugin met betaalde Pro-versie kan dus werken.
- Bouwen past: PHP, goed te testen op GitHub Actions met moodle-plugin-ci en een echte Moodle in Docker.

## Nadelen
- Betaalde nieuwe plugins halen bijna niets (mediaan 3). Geen kleine maker met bewezen omzet.
- De maker is verkoper: Thijs moet Stripe koppelen en zelf btw en verkoopvoorwaarden regelen. Licentiecontrole moeten we zelf bouwen.
- Moodle-plugins zijn GPL: wie koopt mag de code doorgeven (GOK op gevolgen, maar zo werkt het bij alle betaalde Moodle-plugins).
- Golf van AI-plugins sinds oktober, ook betaald. De winkel vult snel.
- Keuring en jaarlijkse herkeuring kosten tijd; duur onbekend.

## Eerste idee wat we zouden bouwen (GOK)
Een gratis plugin die beheerders of docenten veel tijd scheelt, met een betaalde Pro-laag per site per jaar. Kijk naar wat nu goed gaat: kleine editor-hulpjes (Tiny Font Size, $7 per maand, 2.914 installaties, maar waarschijnlijk van vóór de winkel) en rapporten. Bijvoorbeeld een nette cursusvoortgang- of opschoonrapport. Eerst meten welke soort betaalde plugin groeit.

## Wat er nog gemeten moet worden
1. Herhaalmeting rond 8 dec: groeien de installaties van de 67 nieuwe betaalde plugins (zelfde script, zelfde lijst)? Als de beste nieuwe solo-plugins naar 30+ gaan, wordt het een 6.
2. Freemium apart meten: hoeveel van de 23 plugins met "Free option available" halen bereik, en is er bewijs dat de betaalde laag verkoopt.
3. Een bedrag van een maker (forum, LinkedIn, blog). Niet gevonden in deze run.
