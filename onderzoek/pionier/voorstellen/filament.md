# Voorstel: Filament (plugins voor Laravel-adminpanelen)

Noor, pionier, 8 nov 2026. Nagekeken door een controleur (agent, zelf opnieuw gemeten met curl, alle 7 beweringen klopten; zie onder).

## In het kort
Filament is een open framework om adminpanelen en bedrijfssoftware te bouwen in Laravel (PHP). Er is een officiële pluginlijst op filamentphp.com/plugins met een open API. Makers verkopen betaalde plugins met hun eigen kassa (Anystack, Privato, Lemon Squeezy) en houden bijna alles. Het platform groeit in een jaar het hardst van alles wat ik tot nu toe mat, en nieuwe makers worden binnen een paar maanden nummer één in een hoek. De winkel zelf is niet jong (sinds 2021), maar het betaalde deel wel: 77 van de 130 betaalde plugins kwamen er in 2026 bij.

**Cijfer: 6. Advies: ja, met kleine inzet.** Eerste product: goedkeuringen (approvals) voor Filament v5, gratis basis plus betaald Pro.

## De vijf vragen

### 1. Groeit het platform hard en zichtbaar? Ja, heel hard.
- Packagist, daggemiddelde downloads van filament/filament: 35.039 per dag in december 2025, 142.838 in september 2026, 244.327 in november 2026 (maand pas 8 dagen oud) (GEZIEN, https://packagist.org/packages/filament/filament/stats/all.json?average=monthly). Bijna 7 keer zo veel in 11 maanden.
- Ter vergelijking laravel/framework: 269.434 per dag in oktober 2025, 907.907 in november 2026 (GEZIEN, zelfde URL). Ook Laravel zelf groeit dus ruim 3 keer; dat komt deels door CI en AI-agents die projecten opzetten. Maar het aandeel van Filament ten opzichte van Laravel ging van ±13% naar ±27%: Filament groeit dubbel zo hard als zijn eigen platform.
- 3.734 pakketten hangen van filament/filament af (GEZIEN, packagist.org/packages/filament/filament.json).
- Motor: Laravel (financiering en Laravel Cloud), AI-gereedschap dat Laravel plus Filament kiest voor bedrijfsapps, en een vast team dat elke paar maanden een grote versie uitbrengt (v4 op 11 aug 2025, v5 op 16 jan 2026, GEZIEN in de versietijden op Packagist).

### 2. Is de app-winkel jong of gaat hij net open? Half.
- De pluginlijst bestaat sinds 2021. In februari 2026 verhuisde hij van een GitHub-repo (687 plugins) naar een database met open API: nu 1.237 plugins (GEZIEN, https://filamentphp.com/api/plugins, meta.total).
- Instroom (publish_date): ±25 per maand in 2025, 85 in september 2026, 120 in oktober 2026 (GEZIEN). De winkel vult zich dus snel.
- Versies: 878 plugins ondersteunen v5, 617 nog v3 (GEZIEN). Bij elke grote versie vallen plugins af die niet meer bijgewerkt worden; dat geeft steeds nieuwe gaten.
- Het betaalde deel is jong: 130 betaalde plugins, waarvan 77 met een publish_date in 2026, 24 in 2025, 16 in 2024 (GEZIEN, nagekeken: precies 77).

### 3. Kan er betaald worden? Ja.
- Betaalde plugins staan gewoon in de lijst met prijs en kassa-link (velden price, checkout_url, anystack_id, privato_id). 72 gebruiken Anystack, 16 Privato (GEZIEN). Filament zelf noemt Privato zijn "premium plugin distribution partner" (DERDEN, https://filamentphp.com/insights/alexandersix-welcoming-privato-as-a-premium-plugin-distribution-partner).
- Prijzen: meestal $29 tot $99 per plugin, ook €149 tot €299 voor grote pakketten (GEZIEN).
- Het Filament-team verkoopt zelf ook: Custom Dashboards $89, Blueprint $49, vier thema's van $29 tot $39 (GEZIEN). Dat bewijst dat er gekocht wordt, maar is ook concurrentie (zie risico).
- Wat ik niet kan zien: verkopen per plugin. Anystack en Privato tonen geen tellers. Dat de oudste verkopers (ralphjsmit sinds 2023 met 10 betaalde plugins, Kenneth Sese met Advanced Tables) blijven uitbreiden, wijst op verkoop (GOK).

### 4. Is er al vraag te zien? Ja.
- Nieuwe gratis plugins halen veel bereik. Mediaan Packagist-downloads totaal: gepubliceerd nov 2025 tot feb 2026: 7.567; feb tot mei 2026: 4.463 (controleur met eigen steekproef van 20: 5.731); mei tot aug 2026: 2.178 (GEZIEN, `data/filament-plugins-analyse.py`). Ter vergelijking: een nieuwe JetBrains-plugin haalt mediaan 111. Let op: Packagist telt installs, ook CI-builds; het aantal echte gebruikers is veel lager (GOK: een tiende tot een vijftigste).
- Nieuwkomers winnen: Notification Center (juli 2026) 22.837 per maand, Guardian (april) 21.948, Passkeys (mei) 21.648, Onboarding (juli) 18.684 (GEZIEN).
- Gebruikers vragen bij oude plugins om de nieuwe versie: 194 issues "Filament v4/v5 support" op GitHub, waarvan 39 nog open (GEZIEN, GitHub-zoekopdracht). Open met de meeste stemmen: filament-kanban (13 reacties sinds juni 2025, ondertussen opgevolgd door Flowforge), Excel Import van eightynine (nog geen v5, 13.317 downloads per maand) en Approvals van eightynine (alleen v3).

### 5. Is de eerste plek in een categorie nog te pakken? In smalle hoeken wel.
De grote basisstukken (rechten, mediabibliotheek, kalender, back-ups) zijn bezet door sterke gratis plugins met honderdduizenden downloads per maand. Maar in 2026 werden in minstens vier hoeken nieuwkomers binnen een paar maanden de grootste. Hoeken met een zwakke of verlaten nummer één (GEZIEN, downloads per maand):
- **Goedkeuringen (approvals):** oude leider eightynine Approvals alleen v3, 18.588 totaal, nu 300 per maand. Nieuwe: Flow van packstub (sept 2026) 1.839, Approval Engine van mkdev 705. Geen betaalde. Nog geen duidelijke nummer één voor v5.
- **Excel-import:** eightynine Excel Import 13.317 per maand maar geen v5; Import Wizard (april 2026) 2.138; Filament heeft zelf een eenvoudige CSV-import.
- **Gantt en planning:** maar één plugin (packstub, eind oktober 2026, 340).
- **Rapporten:** eightynine Reports v3/v4, 2.477 per maand.

## Categorie en eerste productidee
**Goedkeuringen voor Filament v5.** Bedrijfsapps (inkoop, verlof, facturen, documenten) hebben bijna altijd een goedkeuringsstap nodig. De oude leider is blijven hangen op v3 en de nieuwe zijn nog klein. Gratis basis: een goedkeuringsstap op elk model met knoppen in tabel en formulier, geschiedenis en meldingen. Betaald Pro ($49 tot $79, via Privato): meerdere stappen en rollen, regels op bedrag, vervanging bij afwezigheid, herinneringen en een overzicht "wacht op mij". Het moet er opvallend goed uitzien in een Filament-paneel, met Daan vanaf het begin.

Reserve: Excel-import Pro voor v5, als de herhaalmeting laat zien dat eightynine niet bijwerkt.

## Risico's en waaraan je ze ziet
- **Opgeblazen tellers.** Laravel zelf groeit ruim 3 keer in een jaar; dat is meer dan echt gebruik. Teken van gevaar: als de maandcijfers van nieuwe plugins wegzakken terwijl de lijst blijft groeien. Herhaalmeting in 4 weken met maandcijfers in plaats van totalen.
- **De winkel loopt vol.** 120 nieuwe plugins in oktober. Over een jaar kan dit een oceaan zijn; daarom nu beginnen of niet.
- **Het Filament-team bouwt het zelf.** Het team verkoopt dashboards en thema's. Teken: een officiële goedkeuringsplugin of goedkeuringen in de kern. Dan stoppen of omschakelen naar import.
- **Verkopen niet te zien.** We weten niet of betaalde plugins van nieuwkomers verkopen. Dat lossen we alleen op door het zelf te doen, met een kleine inzet en de stopregel.
- **Uitbrengen vraagt Thijs.** Een Packagist-account, een GitHub-repo en een Privato- of Anystack-account (betaalgegevens) zijn stappen voor Thijs.

## Wat er gemeten is en hoe opnieuw
- `data/filament-plugins-meet.py` haalt de hele lijst via de open API en per plugin de Packagist-tellers (±10 minuten). Uitkomst: `data/filament-plugins-2026-11-08.json` (1.237 plugins, 1.088 met tellers).
- `data/filament-plugins-analyse.py` geeft medianen per periode en de nieuwkomers met 2.000+ per maand.
- Herhaalmeting rond 8 dec: opnieuw meten en vergelijken. Ja blijft ja als de instroom van nieuwe plugins blijft en nieuwkomers boven 1.000 per maand komen; anders 5.

## Controle
Een controleur (agent) mat alle zeven kernbeweringen opnieuw met curl: totaal 1.237, de Packagist-cijfers, de releasedata, 130 betaald waarvan 77 in 2026, Approvals alleen v3 met 18.588, Excel Import v3/v4 met 13.317 per maand, mediaan van nieuwe gratis plugins (zijn steekproef: 5.731). Alles klopte. Zijn waarschuwing staat bij de risico's: downloads zijn installs, geen mensen; vergelijk met de groei van Filament zelf en kijk naar maandcijfers.
