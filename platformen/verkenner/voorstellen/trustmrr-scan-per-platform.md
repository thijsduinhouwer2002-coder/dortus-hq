# TrustMRR-scan: waar verdienen nieuwe kleine makers sinds 2025 geverifieerd geld?

Vera, 8 nov 2026, runs 20:31 (ophalen) en 21:31 (analyse). Nagekeken door een controleur (klopt met correcties, verwerkt).

## Wat is gemeten
- Alle 12.304 profielen van TrustMRR opgehaald (GEZIEN). TrustMRR toont omzet die rechtstreeks uit Stripe, RevenueCat, Polar, Paddle enzovoort komt, dus geen opgegeven bedragen.
- Makers met startdatum 1 jan 2025 tot vandaag: 8.469 (Pastel uitgesloten: $4,58 miljoen winkelomzet via Shopify, geen product).
- Indeling per platform op websitedomein en vaste zinnen in naam en beschrijving. Script: `data/trustmrr-platform-analyse.py`, data: `data/trustmrr-alle-2026-11-08.jsonl`.
- Maatstaf: omzet laatste 30 dagen (d30), aandeel met $300+ en $1.000+.

Let op (beperkingen): TrustMRR is een etalage van makers die willen laten zien wat ze verdienen, dus de bedragen zijn hoger dan bij een gemiddelde maker. Vergelijk platformen daarom met elkaar en met het gemiddelde, niet als absolute verwachting. De startdatum is vaak de aanmelddatum, niet de echte start (controleur: 11 makers met start september 2026 of later halen $10.000+).

## Uitkomst (GEZIEN, na controle)

| Groep | Makers sinds 2025 | $300+ in 30 dagen | Echt op het platform? |
|---|---|---|---|
| Alle makers | 8.469 | 1.358 (16%) | |
| iPhone-apps | 515 | 115 (22%) | ja, maar al bekeken (druk, App Store) |
| Mac-apps buiten de App Store | 208 | 41 (20%) | ja; van de eerste 23 met $300+ zijn 20 unieke makers buiten de App Store |
| Tools rond Claude Code, MCP, agent skills | 97 | 21, waarvan 11 echt in dat ecosysteem | half |
| Chrome-extensies | 120 | 10 (8%) | ja |
| Android-apps | 70 | 8 (11%) | ja |
| Discord-bots | 6 | 4 | alle 4 echte bots (Cosmo $14.608, SalesGenie $1.867, ShotCaller $794, OneBump $600) |
| Blender | 3 | 2 echt | 3D-Agent ($6.733, AI-plugin via MCP, abonnement), Dola AI ($847, Unreal) |
| Shopify, Telegram, Slack, Notion, Obsidian, Raycast, Google Workspace, Figma, WordPress, Roblox | 2 tot 16 per platform | 0 tot 2 per platform | vaak tools óver het platform |

Wat de controleur rechtzette: de Mac-groep is groter dan mijn eerste telling (zinnen als "for macOS" vielen weg), Claude/MCP telt 11 echte producten met $300+ in plaats van 21, en bij Discord, Figma en Blender zijn de treffers wél echte plugins of bots.

## Wat het betekent
1. **Geen nieuw winkelplatform springt eruit.** De platformen met een eigen winkel (Shopify, Slack, Telegram, Figma, Notion, Obsidian, Raycast, Workspace) hebben op TrustMRR elk maar een handvol nieuwe makers met geld. Dat past bij wat we eerder zelf maten.
2. **Het geld van nieuwe kleine makers zit vooral in apps die ze zelf verkopen**: iPhone-apps (via de App Store, al bekeken en druk) en Mac-apps buiten de App Store (eigen site, Stripe, Polar of Paddle). Bij Mac-apps buiten de App Store haalt 1 op 5 nieuwe makers $300+ per maand.
3. **Mac-apps buiten de App Store zijn geen winkel.** Er is geen lijst die nieuwe apps laat zien; je vindt klanten zelf (Product Hunt, X, Reddit, zoekmachine). Dat is precies wat Dortus nu het minst heeft: een eigen publiek. Daarom geen ja.
4. **Tools rond AI-codeagenten groeien snel**: menubalk-apps die het verbruik van Claude Code en Codex tonen of verlagen (Headroom $3.091, SessionWatcher $1.563, UsageBar $1.484), skill-bibliotheken (Skillry $11.804, ClaudeKit $1.952). Kleine, goed af te bakenen producten die wij in 1 tot 2 weken kunnen bouwen.
5. **Discord-bots verdienen meer dan ik bij Discord dacht** (4 van 6 met $300+, allemaal rond betaalde communities en verkopen in een server). Kleine groep, maar een reden om Discord bij de volgende herhaalmeting opnieuw te wegen (stond op 5, nee voor nu).
6. **Hint voor Blender (productkans):** 3D-Agent, een AI-plugin voor Blender met abonnement, haalt $31.565 in 12 maanden en $6.733 in de laatste 30 dagen (DERDEN, TrustMRR geverifieerd via Stripe). Er bestaat een sterke gratis opensource-tegenhanger (blender-mcp), dus eerst de harde regel toepassen: hoe sterk is de top? Te onderzoeken in een volgende productkans-run.

## Cijfer en advies
- **Mac-apps buiten de App Store: cijfer 5, nog niet klaar.** Geld aangetoond (DERDEN, geverifieerd), bouwbaar voor ons (Swift of Electron, 1 tot 2 weken), maar bereik hangt helemaal af van eigen verspreiding en dat is niet te meten zonder een eigen test. Wat er nog gemeten moet worden: hoe de 20 makers met $300+ hun eerste klanten vonden (Product Hunt-lanceringen, X-volgers), en of een maker zonder publiek het ook haalt.
- **Tools rond AI-codeagenten: cijfer 5, nog niet klaar.** Snelle groei, kleine producten, betalende ontwikkelaars, maar ook geen winkel en veel gratis concurrentie op GitHub. Zelfde vraag: hoe vinden ze klanten?
- **De scan zelf:** nuttig als bron. Geen nieuw platform met cijfer 6 of hoger. Het script kan elke maand opnieuw draaien om groepen te volgen.
