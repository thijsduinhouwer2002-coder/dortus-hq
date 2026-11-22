# Voorstel: Google Connected Apps Platform (apps in Gemini en Google Search)

Noor, pionier. Run 9 nov 2026, 13:40 tot 14:25 UTC. Controleur: één agent, alle zes punten nagekeken (uitkomst verwerkt hieronder).

## Wat het is
Sinds 28 okt 2026 kunnen bedrijven zelf een "Connected App" bouwen voor de Gemini-app en (in de komende weken) Google Search. Je bouwt een MCP-server op een eigen HTTPS-adres (of Android AppFunctions), gebruikers koppelen eenmalig hun account bij jou (OAuth 2.1), en daarna roepen ze je app aan met @Naam of zet Gemini hem zelf in. Registreren, testen en indienen gaat via Google Connected Console. Het is een preview: alleen voor ontwikkelaars in de VS, na aanmelding (DERDEN, https://techcrunch.com/2026/10/28/as-ai-agents-reshape-the-web-google-opens-gemini-and-search-to-more-apps/: "in public preview for U.S. developers who sign up for the waitlist"). Google: "We're opening access in phases, and will add more developers, markets, and Google products over the coming months" (GEZIEN, https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/).

Zelfde soort als ChatGPT-apps (4) en Claude-koppelingen (4), maar met Google Search erbij.

## De vijf vragen

**1. Groeit het platform hard?** Ja. Gemini-app 750 miljoen gebruikers per maand bij de Q4 2025-cijfers (DERDEN, https://pulse2.com/google-gemini-surpasses-750-million-monthly-active-users/); latere berichten noemen 900 miljoen en 1 miljard, niet zelf nagekeken (DERDEN, feedbagel.com, deccanchronicle.com). Search is het grootste publiek dat er is. De motor is Google zelf. Sterkste punt.

**2. Is de winkel jong?** Ja, zo jong als het kan. Tot 28 okt kon je alleen meedoen "working closely with Google" (DERDEN, 9to5google.com, 28 okt 2026). De officiële lijst telt nu 86 apps (GEZIEN, https://support.google.com/gemini/table/17434654, getest met `data/google-connected-apps-meet.py`): ±14 van Google zelf, ±18 van telefoonmakers (Samsung, Xiaomi, OPPO, HONOR enz.), ±54 van andere bedrijven. 30 van de 86 werken alleen in de VS. Er is een lijst in de Gemini-instellingen (Customize, Connectors) met per app een pagina en een knop "Add" (GEZIEN door controleur, https://support.google.com/gemini/answer/13695044).

**3. Kan er betaald worden?** Niet via Google. In de docs en het beleid staat niets over prijzen, omzetdeling of aankopen via Google (GEZIEN, policy, mcp, guidelines, quality, prerequisites doorzocht). Wel mag je een eigen dienst met eigen abonnement koppelen via OAuth; afrekenen hoort buiten de app ("final payment checkout" stuur je door naar je eigen site, GEZIEN door controleur in mcp/guidelines). Reclame van derden is verboden. Dus: een eigen kassa kan, op de manier van Attio, maar geen enkele maker laat zien dat dat hier verkoopt. De programma-overeenkomst zelf is niet te lezen zonder inlog.

**4. Is er vraag te zien?** Niet van gebruikers naar kleine apps. Wel veel belangstelling van bedrijven en SEO-mensen ("something even bigger for Search Marketers", DERDEN, https://www.seroundtable.com/google-connected-apps-platform-42408.html). Geen enkel verslag gevonden van een kleine of onafhankelijke maker die is toegelaten of afgewezen (controleur, WebSearch; Hacker News en Reddit niet goed te doorzoeken met curl).

**5. Is de eerste plek in een categorie te pakken?** Moeilijk voor ons. Google laat maar negen categorieën toe (GEZIEN, https://developers.google.com/connected-apps/mcp/vertical-journeys): muziek, content maken, boodschappen, vastgoed, lokale diensten, evenementen, productiviteit, CRM, financiën voor kleine bedrijven. De categorie ligt vast bij het aanmaken. Belangrijker: het beleid verbiedt "wrapper applications ... that rely primarily on a pass-through of another platform's APIs" (GEZIEN, connected-apps-policy). Je app moet dus een eigen dienst met eigen gebruikers en eigen data zijn; een slimme laag bovenop Xero, Shopify of Notion mag niet. En een app voor algemene informatie zonder account is volgens de kwaliteitsregels geen goede Connected App. In elke categorie staan nu al de grote merken van die categorie (Spotify, Canva, Instacart, Zillow, Linear, Xero, Zoho). Een nieuwe kleine dienst begint met nul gebruikers die hem kunnen koppelen.

## Risico en tekens
Het platform zelf haalt het vrijwel zeker; het risico zit ergens anders. Google kan het gesloten houden voor bekende merken (de huidige lijst is precies dat). Teken dat het opengaat voor kleine makers: een eerste app van een onbekende maker in de tabel, of een openbare toelatingsregel zonder VS-eis. Teken dat het dichtblijft: over drie maanden alleen nog merken en nog steeds "preview".

## Categorie waar wij nummer één kunnen worden
Nu geen. Als het later opengaat voor makers buiten de VS, dan het meest kansrijk in "productiviteit" of "financiën voor kleine bedrijven" met een eigen kleine dienst die vooral via Gemini wordt gebruikt (bijvoorbeeld een eenvoudige urenregistratie of facturen-inbox voor zzp'ers, met eigen abonnement). Dat is wel een hele eigen SaaS bouwen en onderhouden, met OAuth-server en privacybeleid.

## Eerste productidee (alleen als het opengaat)
Urenregistratie voor zzp'ers waar je in Gemini zegt "@Uren 3 uur aan klant X, maak de factuur van oktober", met eigen abonnement van ±€5 per maand. Te bouwen in ±2 weken (MCP-server, OAuth 2.1, kleine database), te testen in Gemini Developer Mode.

## Cijfer: 4. Advies: nee voor nu, volgen.
Groei en jeugd zijn top, maar Thijs kan er nu niet in (alleen VS, wachtlijst), betalen gaat alleen via een eigen dienst, het wrapperverbod sluit de handige kleine apps uit die wij snel kunnen maken, en de lijst is een merkenlijst. Zelfde uitkomst als ChatGPT-apps en Claude-koppelingen.

Herhaalmeting rond 9 jan 2027: `python3 -I platformen/pionier/data/google-connected-apps-meet.py platformen/pionier/data/google-connected-apps-2027-01-09.json` en vergelijk met `google-connected-apps-2026-11-09.json` (86 apps). Eerder kijken als Google landen buiten de VS toevoegt. Naar 6 als: open buiten de VS én een eerste kleine maker in de lijst.

## Wat ik niet kon meten
De aanmeldpagina (connected.google.com, alleen met JavaScript), de programma-overeenkomst, de aparte lijst voor Search, en hoe Google kiest welke app het voorstelt aan iemand die hem nog niet koppelde.
