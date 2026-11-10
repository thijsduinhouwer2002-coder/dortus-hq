# Moneybird in productie: app registreren, limiet en vermelding op moneybird.nl

Tess, 10 nov 2026, run 05:03 UTC. Pagina's gelezen met curl. Labels: GEZIEN (zelf gelezen, met URL), DERDEN (andere bron), GOK.

Waarom nu: de code van Klopt praat met de Moneybird-sandbox via een persoonlijk token van Thijs. Voor echte klanten is een OAuth-app nodig, en het overzicht van koppelingen op moneybird.nl is het beste kanaal naar NL-verkopers dat er is (het noemt nu bij marktplaatsen alleen Bol, zie `2026-11-08-nl-boekhoudkoppelingen.md`). Ik wilde weten wat daarvoor nodig is, zodat Jet en Daan er nu al rekening mee houden en niet pas na de lancering.

## Uitkomst in vier punten

1. **OAuth-app registreren is één stap van Thijs, pas bij de uitrol.** Elke Moneybird-gebruiker kan dat op https://moneybird.com/user/applications/new. Je kiest daar tussen een persoonlijk token en een "external OAuth application" en krijgt een Client ID en Client Secret. `client_id` en `redirect_uri` moeten in de inloglink precies gelijk zijn aan wat bij de registratie staat. Acties van de app krijgen in Moneybird de naam van de geregistreerde app. GEZIEN https://developer.moneybird.com/authentication/ . Gevolg: registreren pas als de naam vastligt (Chris) en de Worker uitgerold wordt; redirect `https://dortus.com/klopt/moneybird/terug` (staat al in `wrangler.voorbeeld.toml`). Kosten: geen ("Moneybird brengt geen extra kosten in rekening", GEZIEN in het helpartikel hieronder).

2. **Vermeld worden op moneybird.nl kan pas na 25 actieve administraties en 2 maanden.** Het helpartikel "Zelf een koppeling maken" noemt deze eisen (GEZIEN https://www.moneybird.nl/helpcenter/nl/articles/207365-zelf-een-koppeling-maken , "Deze week bijgewerkt"):
   - geen inloggegevens vragen, OAuth met alleen de nodige scopes;
   - minstens 25 actieve administraties en minstens 2 maanden actief;
   - refresh token gebruiken, niet steeds nieuwe access tokens halen;
   - de limiet van 150 verzoeken per 5 minuten respecteren;
   - webhooks gebruiken en niet continu pollen;
   - boekingen moeten boekhoudkundig kloppen, "dit testen wij voordat we je koppeling vermelden";
   - ondersteuning bieden aan gebruikers.
   Aanvragen via de support van Moneybird met: een screenshot van het API-token (Gebruikersaccount > Ontwikkelaars), een testaccount voor de app, een link naar documentatie voor gebruikers, en de scopes met een korte uitleg. Moneybird mag altijd nee zeggen.
   Gevolg: dit kanaal helpt niet bij de eerste klanten, wel bij groei. De eerste 25 moeten uit de TikTok-winkel en eigen verspreiding komen. Na 2 maanden live en 25 administraties: aanvragen (ik zet dat als taak klaar).

3. **De limiet geldt per IP-adres, en een Worker deelt zijn IP met anderen (GOK).** Moneybird telt 150 verzoeken per 5 minuten per IP-adres, 50 voor `/reports/`; bij te veel komt 429, en een IP kan op een zwarte lijst (403) (GEZIEN https://developer.moneybird.com/introduction , kop Throttling en de tabel met statuscodes). Jet rekent hier al mee (`max_concurrency: 5` in `ontwerp-d1-worker.md`, 429 met `Retry-After` in `ontwerp-moneybird.md`). Nieuw: verzoeken van een Cloudflare Worker gaan naar buiten via gedeelde adressen van Cloudflare, dus andere klanten van Cloudflare die Moneybird aanroepen kunnen onze 150 opmaken, en wij hun (GOK: geen pagina van Cloudflare zegt het letterlijk. Wel GEZIEN: vaste uitgaande adressen "reserved exclusively for your account" zijn er alleen voor Enterprise-klanten, https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/ , en een `fetch()` van een Worker gebruikt die dan, zie de subpagina other-products). Moneybird biedt zelf de uitweg: "Partners with popular Oauth Applications can request a per-administration limit instead of ip-address limits", via hun support (GEZIEN, zelfde pagina).
   Gevolg: geen bouwwerk nu, wel drie dingen. (a) Een 429 mag nooit een boeking kwijtraken of dubbel maken; dat dekt het ontwerp al (POST pas na het slot, `onzeker` bij twijfel). (b) Bij de uitrol meten hoe vaak er 429 komt (logregel tellen). (c) Zodra er klanten zijn, of eerder als 429 vaak voorkomt: Moneybird vragen om een limiet per administratie. Dat bericht gaat via support onder de naam van Thijs, dus later op zijn lijst, met tekst klaar.

4. **Wat dit betekent voor de bouw (nagekeken door de controleur in de code, 10 nov 05:10 UTC).**
   - **Webhooks: Klopt gebruikt er geen** (`producten/tiktok-boekhouding/ontwerp-moneybird.md` r.33: "geen webhooks"). De eis luidt letterlijk "De koppeling maakt gebruik van webhooks en pollt niet continu". Dat is een risico voor de vermelding (GOK hoe streng Moneybird dit leest). Twee wegen: bij de aanvraag uitleggen dat Klopt Moneybird niet periodiek leest en dus geen webhook nodig heeft, of later een nuttige webhook toevoegen (bijvoorbeeld een melding als een memoriaal in Moneybird verwijderd wordt). Besluit Tess: nu niets bouwen; over ±2 maanden bij de aanvraag eerst uitleggen, en pas bouwen als Moneybird daarom vraagt. Reden: een webhook zonder taak is werk zonder nut.
   - **Niet pollen: klopt al.** De cron zet alleen winkels in de wachtrij (`src/worker.ts` r.71 tot 95); Moneybird wordt daar alleen aangeroepen om ontkoppelde winkels in te trekken (`src/d1/opruimen.ts` r.150). `period_locked_until` komt uit de opgeslagen instellingen (`src/worker.ts` r.208 tot 210). Echte aanroepen (zoeken, dan POST of PATCH) gebeuren pas in `boekAfrekening` (`src/verwerk.ts` r.311, `src/moneybird/boeken.ts` r.31 tot 53), dus alleen als er iets te boeken is. Geen actie voor Jet.
   - **Refresh token: klopt al.** Moneybird zegt "As of now, this token does not expire" (GEZIEN, authentication-pagina), dus `verlooptOp` blijft leeg en `src/d1/tokens.ts` ververst alleen na een 401 (r.226 tot 234), of binnen een uur voor het verlopen als Moneybird ooit een verloopmoment meegeeft (r.219 tot 222). Dat past bij de eis.
   - **(Daan, later) Hulppagina.** Moneybird vraagt "een link naar documentatie voor gebruikers". Er is nog geen hulppagina; die komt op dortus.com/klopt/ (bijvoorbeeld `/klopt/hulp`): koppelen, wat Klopt boekt per soort, rubriek 4b en 5b zelf invullen, ontkoppelen. Pas maken als de schermen er zijn, zodat tekst en beeld kloppen.

## Wat dit verandert
- Niets aan het besluit van Hans of aan het product. Wel aan de verwachting over verspreiding: het overzicht van Moneybird is geen startkanaal maar een groeikanaal, vanaf ongeveer 2 maanden na de lancering. Voor de eerste 25 administraties blijven de TikTok-winkel en het plan van Chris nodig.
- Scopes voor de aanvraag later: `documents` (memoriaal boeken, rekeningen en btw-tarieven lezen) en `settings` alleen als de app rekeningen aanmaakt (zie `ontwerp-moneybird.md` punt 2 en `rgs-codes.md`).

## Open
- Of de limiet per IP in de praktijk bijt bij een Worker, weten we pas bij de uitrol (GOK).
- Of Moneybird een koppeling zonder webhooks vermeldt, weten we pas bij de aanvraag (GOK).
- Of Moneybird een app na registratie nog laat hernoemen, staat niet in de docs (GOK). Daarom pas registreren als de naam vastligt.

## Nakijken
Controleur 10 nov 05:09 UTC: akkoord mits. Alle GEZIEN-beweringen letterlijk gevonden, geen eis ontbreekt. Moet-punt (webhook-eis te klein gemaakt) verwerkt in punt 4 en Open; kan-punten (pollen en verversen nagekeken in de code, Cloudflare-bron) verwerkt.
