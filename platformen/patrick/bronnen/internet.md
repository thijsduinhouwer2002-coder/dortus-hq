# Wat anderen doen: bronnen (verzameld 9 nov 2026, 22:20, door een agent met curl; links zijn door die agent geopend)

1. CLAUDE.md onder 200 regels; langer kost context en "reduce adherence". https://code.claude.com/docs/en/memory , https://code.claude.com/docs/en/costs
2. Importeren of verplicht laten lezen bespaart niets: "imported files load together with the CLAUDE.md". Alleen laden als het nodig is bespaart. https://code.claude.com/docs/en/memory
3. Modellen volgen ongeveer 150 tot 200 instructies redelijk; daarboven negeren ze alles gelijkmatig meer (HumanLayer, eigen analyse, niet streng onderzocht). Hun eigen CLAUDE.md is minder dan 60 regels. https://www.humanlayer.dev/blog/writing-a-good-claude-md
4. Progressive disclosure: altijd alleen een korte index, details pas laden als nodig (skills). https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
5. Context rot: meer tekens, slechter onthouden. Doel: "the smallest possible set of high-signal tokens", "just in time" laden. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
6. Harde regels in een hook of instelling, niet in hoofdletters of IMPORTANT; nadruk stapelen laat Claude de regel te vaak toepassen. https://code.claude.com/docs/en/best-practices
7. Tegenstrijdige en verouderde regels actief opruimen; bij tegenspraak kiest Claude willekeurig. https://code.claude.com/docs/en/memory
8. Lange klussen: kort voortgangsbestand plus git log als overdracht, elke sessie één taak afmaken, niet "klaar" roepen als het niet zo is. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
9. Takenlijst in JSON met vast statusveld; model overschrijft JSON minder snel dan markdown. (zelfde bron)
10. Agents ~4x tokens van chat, multi-agent ~15x; slecht geschikt voor werk met veel afhankelijkheden. https://www.anthropic.com/engineering/multi-agent-research-system ; agent teams ~7x: https://code.claude.com/docs/en/costs
11. Begin met 3 tot 5 agents; meer = meer overleg, minder winst; lang onbewaakt laten draaien vergroot verspild werk. https://code.claude.com/docs/en/agent-teams
12. Eén eigenaar per bestand, scharpe taakgrenzen; vage opdrachten gaven dubbel zoekwerk. (agent-teams, multi-agent-research-system), https://lucumr.pocoo.org/2025/6/12/agentic-coding/ , https://simonwillison.net/2025/Oct/5/parallel-coding-agents/
13. Wachten op elkaar is een bekend knelpunt; resultaat in bestanden, alleen een verwijzing doorgeven. (multi-agent-research-system)
14. Leg vast hoeveel moeite een taak waard is; veel gemaakte fout: te veel werk in simpele vragen; stopvoorwaarde nodig. (multi-agent-research-system), https://www.anthropic.com/engineering/building-effective-agents
15. Eenvoudigste opzet die werkt. Gas Town (20 tot 30 agents) heeft een aparte bewaker die vastgelopen agents opspoort; "4-10 agents become chaotic" zonder structuur. https://raw.githubusercontent.com/steveyegge/gastown/main/README.md . Willison: de echte grens is hoe snel de mens het resultaat kan nakijken.
16. Headless runs: `--max-budget-usd` als kostengrens, `--bare` slaat CLAUDE.md over. https://code.claude.com/docs/en/headless

Niet kunnen openen: Medium-stuk "Welcome to Gas Town" (403).
