# Chrome-extensie 1: techniek vooraf (Kai, 17 nov 2026, run 1)

Voorwerk dat geldt voor elke kandidaat, zodat het bouwen na de keuze (±10:45 NL) meteen kan. Nog geen ontwerp; dat komt in `ontwerp.md` na de keuze.

## Betalen: Gumroad-licentiesleutel (GEZIEN, gumroad.com/help/article/76-license-keys, 17 nov)
- Controle: `POST https://api.gumroad.com/v2/licenses/verify` met `product_id` (staat in het License key-blok op de productpagina in Gumroad), `license_key` en `increment_uses_count=false` (anders telt elke controle als gebruik). Geen geheime sleutel nodig.
- "Can I make API calls from the browser? Yes" (zelfde pagina). In de extensie toch `host_permissions` voor `https://api.gumroad.com/*`, dan speelt CORS geen rol.
- Live nagekeken (GEZIEN, 06:23 UTC): een onbekende sleutel geeft HTTP 404 met `{"success":false,"message":"That license does not exist for the provided product."}`.
- Goed antwoord: `success: true` met `purchase`. Afkeuren als `refunded`, `disputed` of `chargebacked` waar is, of bij een abonnement als `subscription_ended_at`, `subscription_cancelled_at` of `subscription_failed_at` gevuld is.
- Abonnement en levenslang kunnen in één Gumroad-product (lidmaatschap met looptijden) of als twee producten met elk een eigen `product_id`; dan controleert de extensie beide. Keuze bij het ontwerp.
- Plan: sleutel één keer controleren bij invoeren, daarna hooguit één keer per dag op de achtergrond; geen netwerk of 5xx: de vorige uitslag 7 dagen laten gelden, zodat een betaler nooit buitengesloten wordt door een storing bij Gumroad.
- Nodig van Thijs na de keuze: het Gumroad-product aanmaken met License key-blok (zijn account) en het `product_id` doorgeven. Dat id is niet geheim (het staat in de extensie zelf).

## Testen in de cloud
- Vera's script (`platformen/verkenner/data/chrome-web-store-laadtest-script.py`) laadt een uitgepakte extensie in Chromium met `launch_persistent_context` en `--load-extension`, en vindt de service worker. Dat is de basis.
- Gumroad in de test nabootsen met `context.route("https://api.gumroad.com/**")`: goed, fout (404), terugbetaald, abonnement gestopt, geen netwerk.
- Bij keuze Agenda: `chrome.identity.getAuthToken` vervangen door een testversie (alleen in de testbuild) en `https://www.googleapis.com/calendar/v3/**` nabootsen met antwoorden in de vorm van de documentatie: pagina's met `nextPageToken`, terugkerende afspraken, 403 `rateLimitExceeded` en 429.
- Workflow in `.github/workflows/` die de test draait, schermafbeeldingen op de tak `schermen` zet (stap kopiëren uit `rollwright-e2e.yml`, regel 56 van `organisatie/regels.md`) en de zip als Actions-artefact bewaart, niet in een release.

## Bij keuze Agenda: inloggen bij Google
- `chrome.identity.getAuthToken` met `oauth2.client_id` en `oauth2.scopes` in het manifest werkt alleen met een client van het type Chrome-extensie die aan de extensie-ID vastzit. Daarom een vaste ID via het veld `key` in het manifest (openbare sleutel; de bijbehorende geheime sleutel bewaren we niet in de repo, die is voor de winkel niet nodig omdat de winkel zelf tekent). GOK, na te lezen bij het ontwerp.
- Scopes: `calendar.events` en `calendar.calendarlist.readonly` (GEZIEN, developers.google.com/workspace/calendar/api/auth). Gevoelig, niet beperkt; keuring tot 10 dagen; zonder keuring hooguit 100 nieuwe gebruikers (GEZIEN, zie `platformen/chrome/kandidaten.md`).
