# Voorstel: Zendesk Marketplace (apps voor de helpdesk Zendesk)

Vera, 16 nov 2026, run 11:31 (Amsterdam). Eigen meting van de hele winkel via de open API, nagekeken door een controleur (agent): alle zes getallen klopten, correcties op de uitleg verwerkt.

**Cijfer: 2. Advies: nee.**

## Wat het is
Zendesk is helpdesksoftware voor bedrijven. In de Marketplace staan apps van Zendesk zelf en van derden. Betaalde apps kunnen via Zendesk afrekenen (Stripe, per account of per agent per maand). www.zendesk.com geeft vanaf hier een Cloudflare-blokkade (403), maar de open API `marketplace.zendesk.com/api/v2/apps.json` geeft alle apps met aanmaakdatum, aantal installaties, prijsplannen en reviews. robots.txt verbiedt alleen twee statistiekpaden van de helpcentra (GEZIEN, 16 nov).

## Cijfers
- **Omvang:** 1.898 apps, waarvan 565 betaald en 207 alleen een verwijzing (marketing_only) (GEZIEN, API 16 nov). Zendesk zegt zelf "1,800+ apps" (DERDEN, menu op zendesk.com, gezien door de controleur).
- **Drukte (aangemaakt per maand):** 2025: 9 tot 26 per maand. Mrt t/m aug 2026: ±30 per maand. Sep 2026: 55. Okt 2026: 107, waarvan 55 van één maker (Great Work LLC, apps met namen als Clientwell, Ferrywell, Staffwell) (GEZIEN). Dat is een vloed die net begint.
- **Bereik, lichting aangemaakt mei t/m aug 2026** (zonder marketing_only, n=103, mediaan ±96 dagen live): mediaan 1 installatie, 0% met 100+, 2% met 10+. Betaald (n=36): mediaan 0, geen enkele met 10+ (GEZIEN).
- **Bereik, oudere lichtingen:** jan t/m jun 2025 (n=88, ±17 maanden live): mediaan 5, 2% met 100+, 38% met 10+. Jul t/m dec 2025 (n=96): mediaan 5,5, 5% met 100+ (GEZIEN). Per maand live is het tempo bij jong en oud ongeveer gelijk, ±0,3 installaties per maand. Dus: het bereik is niet slechter geworden, het is al jaren laag.
- **Grootste nieuwkomers sinds 2025:** Klaviyo 743 (van Klaviyo zelf), VOC Patterns 550 (Zendesk Labs). Grootste kleine maker: PDF Export & Download for Tickets (Ino Studio Lab, 143, gratis), daarna Kanban (SweetHawk, 136, betaald, $2 tot $5 per agent) (GEZIEN).
- **Geld:** betalen werkt en de oude toppers zijn echte bedrijfjes: Advanced Search Plus (Swifteq, 543 installaties, vanaf $99 per account), Recurring Tickets (SweetHawk, 388, $120), Exporter (Sparkly, 1.139, $30) (GEZIEN, prijzen en installaties; omzet niet openbaar). Van de 223 betaalde apps die sinds 2025 zijn aangemaakt halen er hooguit 9 een geschatte bovengrens van $300 per maand (installaties maal laagste prijs, per agent maal 5 agents), bijna allemaal van gevestigde seriemakers (SweetHawk, Swifteq, Adelante, OAPPS); één buitenstaander (Optimate.me, ±$1.350 als bovengrens) (GEZIEN, de bovengrens zelf is GOK: installaties zijn geen betalers en een plan als "Free Auto Merge" voor $249 wekt twijfel).
- **Openbaar bedrag van een kleine nieuwe maker:** niet gevonden (geen TrustMRR-profielen, niets op Hacker News; gezocht door de controleur).
- **Niet bevestigd:** of installation_count actieve installaties zijn of een totaal, en of proefaccounts meetellen. Verwijderde apps ontbreken in de lijst, dus het echte beeld is eerder slechter.

## Voor en nadelen
- Voor: open API met installaties per app (zeldzaam), betalen via Zendesk, klanten betalen per agent (hoge prijzen, $30 tot $250 per maand per account is gewoon).
- Tegen: nieuwe apps halen bijna niets (mediaan 1 na drie maanden, 5 na anderhalf jaar), kopers zijn bedrijven (de les van Atlassian), de bekende gaten (export, splitsen, samenvoegen, zoeken) zijn al jaren bezet door seriemakers, en er begint een vloed van AI-gemaakte apps (55 van één maker in oktober).

## Wat we er zouden bouwen
Niets. Als het toch moest: een nauwe hulp voor kleine teams (bijvoorbeeld ticket-export naar pdf, waar Ino Studio Lab met een gratis app in een jaar 143 installaties haalde). Dat laat zelf al zien hoe klein het bereik is.

## Wat het cijfer kan veranderen
Een lijst voor nieuwe apps in de winkel die zichtbaar installaties geeft (een lichting met 20%+ op 10+ binnen drie maanden), of een openbaar bedrag van een kleine nieuwe maker boven $300 per maand. Herhalen kan met `python3 -I data/zendesk-marketplace-haal-script.py uit.jsonl`; de meting van vandaag staat in `data/zendesk-marketplace-2026-11-16.jsonl`. Let op: indelen op `created_at`, niet op `date_published` (wordt bij oude apps opnieuw gezet).

## Les voor volgende runs
Helpdesk- en CRM-winkels met afrekenen via het platform hebben soms een open API met installaties (zoals Zendesk en Clover). Freshworks (Freshdesk) is de logische volgende met dezelfde aanpak.
