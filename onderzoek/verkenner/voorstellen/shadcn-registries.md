# Voorstel: shadcn-registry's en betaalde shadcn-kits (Vera, 8 nov 2026, run 18:33)

**Cijfer: 4. Advies: nee voor nu.** Geld is er, maar het zit bij wie vroeg begon en eerst een groot gratis bereik had. Shadcnblocks (sinds 2023) heeft 5.420 betalende klanten. Van de 10 nieuwe React/Tailwind-kits uit 2025 en 2026 met geverifieerde omzet haalt de helft niet meer dan ±$500 in totaal, en alle 10 samen verdienden de laatste 30 dagen ±$2.600. Een nieuwkomer zonder eigen publiek verdwijnt hier.

Doorgegeven door Noor (pionier, cijfer 4, zie `platformen/pionier/voorstellen/shadcn-registries.md`). Haar vraag aan mij: verkopen kleine premium-registry's nu?

## Wat ik mat en hoe
- **Eigen meting (GEZIEN):** TrustMRR is een openbare lijst van startups waarvan de omzet rechtstreeks uit Stripe of Polar komt (geen schermafdrukken). robots.txt staat lezen toe. Uit de sitemap (12.305 startups) nam ik alle 374 met UI-woorden in de naam, plus 127 uit categoriepagina's en losse namen: 502 profielen. Daarvan gaan er 30 over UI-kits of componenten. Script en data: `data/trustmrr-uikits-haal.sh`, `data/trustmrr-uikits-analyse.py`, `data/trustmrr-uikits-2026-11-08.json`.
- **Eigen controle op sites (GEZIEN):** tellers op de sites van de grote spelers.
- **Onderzoeker (agent):** openbare omzetverhalen, 21st.dev, Gumroad.
- **Niet te meten:** installaties per registry (shadcn toont ze niet), verkopen bij makers die niet op TrustMRR staan. TrustMRR is een zelfgekozen groep: wie weinig verdient meldt zich minder vaak aan, maar wie een website wil verkopen juist wel. Zie het als steekproef, niet als hele markt.

## Cijfers

**Nieuwkomers, React/shadcn/Tailwind-kits gestart jan 2025 t/m okt 2026, totale geverifieerde omzet (GEZIEN, TrustMRR 8 nov):**

| Kit | Start | Totaal | Laatste 30 dagen |
|---|---|---:|---:|
| Efferd (solo, shadcn-blocks) | sep 2025 | $17.973 | $548 (laatste 6 mnd $11.487) |
| RetroUI (solo) | jan 2025 | $7.013 | $0 |
| RareUI (gratis met betaalde laag) | eerste omzet sep 2026 (geen startdatum) | $1.358 | $681 |
| HextaUI Pro (solo) | okt 2026 | $1.058 | $960 (lancering) |
| VantaUI | jun 2026 | $522 | $198 |
| Motoko UI (solo) | aug 2026 | $448 | $129 |
| OpenTailwind | sep 2026 | $228 | $38 |
| LandingGo | aug 2025 | $207 | $0 |
| Charcoal UI | okt 2026 | $69 | $69 |
| UIforSaaS | mrt 2025 | $2,42 | $0 |

Niet in de tabel: QuasarUI (Vue, sep 2025, $1.505), shadcn-ui-blocks-pro ($949, geen startdatum, omzet al voor nov 2025), GetUrUI en Spectrum UI ($0).

- Mediaan totaal: ±$485. 2 van 10 boven $5.000, 4 van 10 boven $1.000 (GEZIEN).
- Alle 10 samen de laatste 30 dagen: ±$2.620 (GEZIEN). Verkoop piekt bij de lancering en zakt dan weg (Efferd -79% in 30 dagen volgens TrustMRR).
- Ter vergelijking, oudere kits op TrustMRR: Frameblox (Framer, 2024) $136.874, Nocodable Components (Webflow, 2023) $112.246, Web3Templates (2021) $75.701, GrabUI (2024) $31.045 (GEZIEN). Boilerplates met shadcn doen het beter dan losse blocks: TurboStarter (feb 2026) $85.385, laatste 30 dagen $6.442 (GEZIEN).

**Grote spelers (GEZIEN op hun site, 8 nov):**
- Shadcnblocks: 22.162 gratis gebruikers, 5.420 Pro-klanten, ±10.000 installs per dag. Prijs $149 / $299 / $399 eenmalig. Bij die prijzen grofweg $0,8 tot 1,5 miljoen totaal (GOK).
- Kokonut UI Pro: "Bought by 1k+", $119 tot $159 levenslang. Cult UI Pro: "416+ buyers".
- Aceternity UI Pro: $80.000 in 2 maanden na lancering (DERDEN, starterstory.com/stories/aceternity-ui, ±2024).
- Obra shadcn/ui Pro (Figma-kit, klein Belgisch bureau): ±€10.000 uit ±100 orders in 40 dagen, maar met al 45.000 kopieën van de gratis kit (DERDEN, blog Obra 24 apr 2026).

**Andere kanalen:**
- 21st.dev: losse componenten zijn daar altijd gratis; alleen templates mogen geld kosten, maker krijgt 70%, na beoordeling (GEZIEN door onderzoeker, help.21st.dev/publishing/monetization.md).
- Gumroad: zoeken op "shadcn" geeft 45 producten, betaalde met 0 of 1 rating. Geen belangrijk kanaal (GEZIEN door onderzoeker).

## De maatstaf
- **Bereik:** niet te meten per registry. Het platform zelf groeit extreem (npm shadcn ×28 in een jaar, DERDEN via Noor). Maar de winnaars hadden eerst duizenden gratis gebruikers of veel volgers op X.
- **Geld:** ja, aangetoond, maar vooral voor wie vroeg was. Voor nieuwkomers mediaan ±$485 totaal (GEZIEN, steekproef).
- **Wie betaalt, hoeveel, hoe vaak:** ontwikkelaars en kleine startups, $49 tot $399, bijna altijd **eenmalig** (levenslang). Geen abonnement. Dat past slecht bij de koers van 8 nov (terugkerend geld).
- **Drukte:** 548 registry's in de officiële lijst, ±117 nieuw per maand (DERDEN via Noor). Plus honderden kits buiten de lijst.
- **Vindbaarheid:** X, Reddit, de officiële lijst, en steeds meer AI-agents die `shadcn add` draaien ("blocks that agents already trust", tekst van Efferd). Geen winkel met ranglijst.
- **Past het bij ons:** bouwen kan zeker in 1 tot 2 weken. Maar Thijs heeft geen publiek onder ontwikkelaars op X, en dat is hier de motor.

## Voor en tegen
Voor:
- Mensen betalen aantoonbaar, en voor flinke bedragen ($149 tot $399).
- Het platform groeit nog steeds hard, en AI-bouwers halen componenten automatisch op.
- Eén solo-nieuwkomer (Efferd) haalde $18.000 in 13 maanden.

Tegen:
- Voor 8 van de 10 nieuwkomers bleef het onder $1.400 totaal.
- Eenmalige verkoop, piek bij lancering, dan stil.
- Geen winkel die nieuwe makers zichtbaar maakt; succes hangt aan eigen volgers.
- Grote spelers met duizenden blocks, en shadcn of Vercel nemen populaire onderdelen zelf op.

## Eerste idee, als we het toch zouden doen
Een registry in een dunne hoek (Noor: kalender en planning 6, e-commerce 6, auth 8): complete planningsblokken (dag, week, resource-planning, boekingen) met een gratis basis en een Pro-pakket van $99 tot $149. Liever als onderdeel van een boilerplate, want die verdienen meer dan losse blocks. Verwachting voor een nieuwkomer zonder publiek: $0 tot $2.000 in het eerste jaar (GOK op basis van de tabel).

## Wat het zou veranderen
- shadcn of 21st.dev opent een betaalde laag met kassa en ranglijst, zodat nieuwe makers gevonden worden zonder eigen volgers.
- Dortus krijgt zelf een publiek onder ontwikkelaars (bijvoorbeeld via de JetBrains-plugin).
- Herhaalmeting rond 8 jan 2027, samen met die van Noor: draai `data/trustmrr-uikits-haal.sh` opnieuw en kijk of de nieuwkomers van sep tot nov 2026 doorverkopen na hun lancering.

## Nagekeken
Controleur (agent, 8 nov): tabel, mediaan en tellers op de sites kloppen, 3 profielen opnieuw opgehaald met dezelfde cijfers. Correcties verwerkt: QuasarUI (Vue) uit de tabel, RareUI erin, som laatste 30 dagen ±$2.620. Oordeel controleur: 4 is redelijk, eerder 3 dan 5.

## Cijfer
Bereik niet te meten, geld wel maar scheef verdeeld, eenmalig, druk, en de motor (eigen publiek) hebben we niet. **4, nee voor nu.**
