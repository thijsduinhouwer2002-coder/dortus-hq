# Voorstel: HighLevel App Marketplace (pionier)

Noor, 8 nov 2026, run 18:38 UTC. Korte toets, gekozen omdat betalen er al werkt (bericht Thijs 19:16).

**Cijfer: 3. Advies: nee voor de pionier.** Betalen werkt uitstekend, maar de winkel is niet jong meer en wordt gevuld door app-fabrieken; nieuwkomers krijgen bijna niets. Vera kwam op 6 nov met haar eigen meting op hetzelfde uit (mediaan 6 subaccounts, nee).

## Wat HighLevel is
Marketingsoftware voor bureaus (CRM, afspraken, sms, funnels) die de bureaus onder eigen merk doorverkopen aan hun klanten (subaccounts). Apps in de Marketplace werken voor een bureau of voor een subaccount.

## De vijf vragen

1. **Groeit het platform hard?** Waarschijnlijk wel, maar het is niet jong (opgericht 2018). Niet zelf gemeten deze run; de vraag doet er weinig toe omdat vraag 2 en 5 al afvallen.
2. **Is de winkel jong?** Nee. 2.844 openbare apps in de open API (GEZIEN, https://backend.leadconnectorhq.com/marketplace/public/all, script `data/highlevel-apps-meet.py`). Nieuw per jaar (datum uit de app-id): 84 in 2023, 464 in 2024, 1.207 in 2025, 1.066 in 2026 tot nu; de laatste maanden 100 tot 150 per maand (GEZIEN). Vijf makers hebben samen 1.116 apps (All The Apps 443, Plugins 275, CRM Pros 243, HighLevel zelf als LeadConnector 91, Rozi Academy 62) (GEZIEN).
3. **Kan er betaald worden?** Ja, het beste van alles wat ik zag: HighLevel rekent af, houdt 0% en keert maandelijks uit via Tipalti; abonnement, eenmalig, freemium, per gebruik, proef van 1 tot 90 dagen; bureaus mogen doorverkopen met opslag (GEZIEN, https://gohighlevelassist.freshdesk.com/support/solutions/articles/155000001217-set-up-your-app-pricing). 1.349 van de 2.844 apps zijn betaald (GEZIEN).
4. **Is er vraag?** Ja, bureaus betalen voor apps (bulk-installaties over al hun subaccounts). Niet verder gemeten.
5. **Is de eerste plek te pakken?** Nauwelijks. Nieuwe apps van maart tot augustus 2026, zonder de grote fabrieken: 450 apps, mediaan 5 installaties, 39 met 100+, 6 met 1.000+ (GEZIEN). De betaalde daarvan: 193 apps, mediaan 2, 8 met 100+; de beste nieuwkomer haalde 575 (TaraPayments) (GEZIEN). De installatietellers zijn ook nog opgeblazen door bulk-installaties: een bundel van All The Apps van juli 2026 staat al op 30.000+ per app (GEZIEN). Bovenaan staan grote merken (Make 376.683, Pabbly, Pipedream) en HighLevel zelf, dat de grote koppelingen (Canva, Slack, LinkedIn, TikTok, YouTube) in 2026 zelf maakte (GEZIEN).

## Risico en wat het zou veranderen
Een eigen kanaal naar bureaus (zelf al HighLevel-bureau zijn of een partner) zou de vindbaarheid oplossen; zonder dat verdwijnt een nieuwe app tussen de fabrieken. Een nieuwe pluginlaag van HighLevel met een datum (bijvoorbeeld een nieuw soort app die alles moet vervangen) is een reden om opnieuw te kijken.

## Herhaalmeting
Niet nodig voor de pionier. Wie wil: `python3 -I data/highlevel-apps-meet.py` en `python3 -I data/highlevel-apps-analyse.py <bestand>`.
