# Voorstel: Open VSX (extensies voor Cursor, Windsurf, Antigravity, Kiro, VSCodium)

**Advies: nee voor nu. Cijfer: 4 van 10.** Open VSX is groot en groeit hard, maar de downloadtellers zeggen weinig: elke nieuwe extensie krijgt vanzelf ±500 tot 700 downloads van automatisch verkeer, ook als niemand hem gebruikt. Echte gebruikers zijn niet te meten. Verkopen kan alleen buiten de winkel om, en de beste nagekeken kleine maker zit op $131 per maand. Het is ook erg druk. Geschreven op 7 nov 2026, run 12:31 (tweede platform).

## Wat ik zelf mat
- Met `data/openvsx-haal-script.py` de open API gelezen: 20.765 extensies in totaal. De zoek-API geeft er hooguit 10.000 (de laatst bijgewerkte, tot 3 juni 2026 terug). Daaruit een toevallige steekproef van 2.500, met per extensie de datum van de eerste versie en het aantal versies. Uitkomst in `data/openvsx-steekproef-2026-11-07.jsonl`. GEZIEN
- Groep: eerste versie tussen 4 juni en 31 aug 2026 (2 tot 5 maanden oud). Die zit volledig in de 10.000, want haar laatste update is na 3 juni. n=807. GEZIEN
- Grens: downloads tellen ook updates en automatisch verkeer (mirrors, CI, agents), DERDEN: [Eclipse, 21 apr 2026](https://newsroom.eclipse.org/node/43804). Het aantal echte gebruikers staat nergens.

## Cijfers

**Bereik**
- Groep juni tot aug 2026: mediaan 1.492 downloads, 68% 1.000+, 18% 5.000+, 7% 10.000+. Kleine makers (namespace met hooguit 3 extensies, niet verified, n=280): mediaan 999, 50% 1.000+. GEZIEN
- **De vloer:** de laagste extensie per maand van eerste versie: juni 628, juli 558, aug 474, sept 356, okt 132 downloads. Geen enkele extensie met eerste versie op of voor 7 sept zit onder de 400. Extensies met maar 1 versie (geen updates, n=240) hebben mediaan 729, vlak boven die vloer, en maar 16% komt boven de 1.000. GEZIEN
- Voorbeelden met 1 versie, 0 reviews en een heel smal publiek: pic/classroom 474, 1046prt/envlint 500, Zells-Zone/type-practice 508 downloads (controleur, via de API). GEZIEN
- Dus: voor een gewone nieuwe extensie is het grootste deel van de downloads automatisch. Echte gebruikers waarschijnlijk tientallen tot enkele honderden. GOK
- Eclipse zegt zelf dat steeds meer verkeer van machine naar machine gaat (agents, CI) en zette er in maart 2026 limieten op. DERDEN: [Eclipse, 3 mrt 2026](https://newsroom.eclipse.org/node/43620), [21 apr 2026](https://newsroom.eclipse.org/node/43804)
- Ter vergelijking (GEZIEN eerder, zie `onderzocht.md`): VS Code Marketplace mediaan 19 installs, JetBrains 111 downloads.

**Geld**
- Geen betaling in de winkel. Makers verkopen een licentiesleutel via Polar, LemonSqueezy of Stripe. DERDEN: [Dodo Payments](https://dodopayments.com/blogs/sell-vscode-extensions)
- Nagekeken kleine makers (TrustMRR, gelezen 7 nov 2026), DERDEN:
  - [Claude Code and Codex Assist](https://trustmrr.com/startup/claude-code-and-codex-assist-history-diff-viewer-chat-manager), start juni 2025: $131 per maand, $433 in de laatste 30 dagen (waarschijnlijk ook eenmalige licenties van $49,99), $7.672 totaal, 30 abonnees, ±33.664 gebruikers, via Polar.
  - [Vinsly](https://trustmrr.com/startup/vinsly), start nov 2025: $219 totaal, nu 0 abonnees.
- Een post met $6.800 per maand uit drie extensies noemt geen namen en lijkt niet betrouwbaar. DERDEN, zwak: [dev.to, mrt 2026](https://dev.to/hopkins_jesse_cdb68cfa22c/how-i-make-6800month-selling-niche-vs-code-extensions-eji)
- Geen kleine maker boven de $300 per maand gevonden bij het doorzoeken van TrustMRR, Indie Hackers-verhalen en blogs over verkochte VS Code-extensies (hulpagent). DERDEN / GEZIEN

**Drukte**
- In de steekproef kwamen 442 van de 2.500 in oktober uit; de steekproef is een kwart van de 10.000, dus ±1.700 nieuwe extensies in oktober. GEZIEN (afgeleid). Eclipse noemde in april ±12.000 extensies, de API telt nu 20.765. DERDEN / GEZIEN. Die twee zijn waarschijnlijk niet op dezelfde manier geteld, dus lees het verschil niet als groei.
- Veel nieuwe extensies zijn hulpjes rond AI-agents (Claude Code, Codex). GEZIEN bij het bekijken van de nieuwste.

**Vindbaarheid**
- In Cursor zoek je in het extensiepaneel via de proxy van Cursor. Er is geen sortering op relevantie, populaire extensies drukken de rest weg; Cursor noemt dat een bekend probleem (9 juli 2026). DERDEN: [forum Cursor](https://forum.cursor.com/t/add-sorting-by-relevance-to-extension-browser/165150)
- Cursor scant elke extensie opnieuw, teams kunnen een wachttijd voor nieuwe versies instellen. Open VSX heeft sinds begin 2026 een scan vóór publicatie met quarantaine. DERDEN: [Cursor docs](https://cursor.com/docs/configuration/extensions), [The Hacker News, feb 2026](https://thehackernews.com/2026/02/eclipse-foundation-mandates-pre-publish.html)

**Past het bij ons**
- Technisch ja: een VS Code-extensie is in 1 tot 2 weken te bouwen (GOK). Thijs moet een namespace claimen (GitHub-login, Eclipse-akkoord). DERDEN: [Open VSX wiki](https://github.com/eclipse/openvsx/wiki/Namespace-Access)
- Het gat van Microsoft-extensies die niet in Cursor mogen (C/C++, Pylance, C#) wordt gevuld door Cursor zelf, Meta (Pyrefly) en Red Hat. DERDEN: [The Register, apr 2025](https://www.theregister.com/2025/04/24/microsoft_vs_code_subtracts_cc_extension/). Daar kan Dortus niet tegenop. GOK

## Voor
- Heel groot publiek (Cursor, Antigravity, Kiro, Windsurf) en hard groeiend: meer dan 300 miljoen downloads per maand. DERDEN: [Eclipse, 3 mrt 2026](https://newsroom.eclipse.org/node/43620)
- Een extensie die we toch bouwen (bijvoorbeeld voor JetBrains-achtige ideeën in VS Code-vorm) kan hier gratis mee.

## Tegen
- Bereik is niet eerlijk te meten: de tellers geven een vloer van honderden automatische downloads.
- Erg druk: ±1.700 nieuwe extensies per maand, slecht zoeken in Cursor.
- Geld: geen betaling in de winkel, geen kleine maker boven $300 per maand aangetoond.

## Eerste idee (als het later ja wordt)
Alleen als bijvangst: een extensie die we al voor een ander platform bouwen ook hier zetten, met een licentiesleutel via Polar (dat zet Obsidian al op).

## Wat er nog gemeten kan worden
- Echte gebruikers: een extensie van onszelf publiceren en het verschil zien tussen downloads en echte activaties (alleen met eigen telling, privacy eerst). Of makers vragen naar hun verhouding.
- Herhaalmeting over 4 weken met hetzelfde script laat zien hoe snel de vloer stijgt.

## Nakijken
Controleur akkoord (7 nov run 12:31), alle cijfers nagerekend, 9 correcties verwerkt: links en labels erbij, vloer scherper (400) met drie voorbeelden, $433 in 30 dagen erbij, telling april en nu niet als groei lezen.
