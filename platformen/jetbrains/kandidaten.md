# JetBrains: kandidaten (6 nov 2026)

**Uitkomst: voorlopige keuze, nog geen bouwbesluit.** De downloadcijfers van de Marketplace waren in deze run niet te lezen. De verplichte vergelijking met cijfers is dus niet gemaakt. Elke kandidaat mist downloads en omzet.

## Wat niet te lezen was (GEZIEN, 6 nov)
- `plugins.jetbrains.com` via curl: de proxy weigert (403). Via de leestool: toestemming niet op tijd beantwoord.
- Ook geweigerd via curl: `repo1.maven.org`, `plugins.gradle.org`, `services.gradle.org`, `cache-redirector.jetbrains.com`. Zonder deze kan een plugin hier waarschijnlijk niet gebouwd of getest worden (GOK, nog niet met een echte build geprobeerd).

## Kandidaten

| | A. Agent-wijzigingen nakijken | B. Betaalde MCP-koppeling met de IDE-index | C. Betaalde visuele editor in de IDE (JCEF) |
|---|---|---|---|
| Wat | Wijzigingen van Claude Code en dergelijke per stuk accepteren, afwijzen, terugdraaien | Agents zoeken en refactoren via de IDE-index | Grafische editor voor een bestandssoort die in de IDE ontbreekt. Soort nog niet gekozen, geen oude Dortus-app |
| Bewijs van vraag | Eén verzoek: [#13120](https://github.com/anthropics/claude-code/issues/13120). [#35814](https://github.com/anthropics/claude-code/issues/35814) vraagt bredere IDE-integratie en raakt dit alleen via de diff-viewer (DERDEN, omvang onbekend) | [Open source plugin](https://github.com/hechtcarmel/jetbrains-index-mcp-plugin) (MIT), geen prijs genoemd, 367 sterren (DERDEN) | Mermaid Studio: 15.441 downloads (GEZIEN, zie `status.md`) |
| Bewijs van betalen | Geen gevonden, Marketplace onleesbaar | Geen gevonden, Marketplace onleesbaar | Geen bewijs van betalen, wel een gevraagde prijs: Mermaid Studio, $49 per jaar (GEZIEN, zie `status.md`). Aantal betalers onbekend |
| Grootste bezwaar | JetBrains biedt zelf [diff en terugdraaien voor agentwijzigingen](https://www.jetbrains.com/help/idea/agents-in-ide.html) (DERDEN, 4 nov 2026). Claude Code werkt in dezelfde omgeving, maar de pagina zegt niet letterlijk dat deze functies daarvoor gelden, en per stuk accepteren of afwijzen staat er niet. Ook [AgentBridge](https://github.com/catatafishen/agentbridge) is open source (87 sterren, DERDEN). Prijs niet genoemd. Air is een aparte plugin en vraagt volgens de pagina geen JetBrains AI-abonnement (DERDEN) | De bestaande plugin heeft MIT-licentie en is open source, dus betalen is moeilijk te verkopen | Eén voorbeeld is geen markt, en er zijn al 88 Mermaid-plugins (GEZIEN, zie `status.md`). Het bewijs komt uit een soort die we niet mogen kopiëren |

## Voorlopige keuze: C
Doelen zeggen dat geld voor bereik gaat. C is de enige waarvoor nu een gevraagde prijs bekend is. Of mensen betalen is ook daar onbekend. Voor A en B kon niet op de Marketplace gezocht worden, dus "geen gevonden" zegt daar weinig. A en B botsen op open source aanbod, A ook op JetBrains zelf.

Dit bewijs is dun. Niet bouwen voordat onderstaande controle is gedaan.

## Controle zodra de Marketplace leesbaar is
1. Haal alle betaalde en freemium plugins op, met downloads, cijfer, prijs en leeftijd.
2. Zoek welke bestandssoorten nog geen goede visuele editor hebben, en kies er één.
3. Doorgaan alleen als minstens 3 betaalde plugins van dit type aantoonbaar bestaan met elk meer dan 5.000 downloads (grens is een GOK). Anders opnieuw kiezen uit wat de lijst laat zien.
