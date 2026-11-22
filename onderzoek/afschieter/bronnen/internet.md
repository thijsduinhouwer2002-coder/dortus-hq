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

## Deel 2 (9 nov, ±22:30, tweede agent, links met curl geopend)
17. Harde grens per geplande run: `--max-turns`, timeouts, concurrency; "Keep your CLAUDE.md concise, since Claude reads it on every run." https://code.claude.com/docs/en/github-actions ; `--max-budget-usd`: https://code.claude.com/docs/en/headless
18. Geplande taak: prompt "self-contained and explicit about what to do and what success looks like"; per taak een lijst met eerdere runs; 100 geplande runs per uur per account; runs tellen mee in het gewone abonnementsgebruik. https://code.claude.com/docs/en/routines.md
19. Laat een verse beoordelaar bepalen of iets af is, niet de doener; voorwaarde = één meetbare eindstand plus een check plus "stop after N turns". https://code.claude.com/docs/en/goal.md
20. Geef iets dat geslaagd/mislukt teruggeeft; reviewer zonder voorkennis; "A reviewer that's asked to find problems will always find *something*", dus kleine punten laten liggen. https://code.claude.com/docs/en/best-practices.md
21. Hooks geven "deterministic control"; exit-code 2 blokkeert of stuurt terug. https://code.claude.com/docs/en/hooks-guide.md
22. Beste feedback: duidelijke regels en welke regel faalde; LLM-als-rechter "generally not a very robust method". https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
23. Eén ding per lus ("Only one thing"). https://ghuntley.com/ralph/
24. 16 parallelle Claudes (C-compiler): de controle moet bijna perfect zijn; "Claude can't tell time and, left alone, will happily spend hours running tests instead of making progress"; taken claimen met een bestand in `current_tasks/`. https://www.anthropic.com/engineering/building-c-compiler
25. Project Vend 2: een CEO-agent van hetzelfde model "wasn't much help, and might even have been a hindrance", deelde dezelfde blinde vlekken, keurde coulance ±8x vaker goed dan af; 's nachts raakten twee agents in een lus. Vaste procedures ("bureaucracy matters") en een agent met een eigen afgebakende rol werkten beter. https://www.anthropic.com/research/project-vend-2
26. Mens aanspreken in drie vormen: melden, vragen, nakijken; één "Agent Inbox" in plaats van een groeiende stroom meldingen. https://blog.langchain.com/introducing-ambient-agents/
27. Echte voorbeelden: anthropics/claude-code CLAUDE.md 40 regels; claude-agent-sdk-python 84; apache/airflow AGENTS.md 254 met een blok "Boundaries" (Ask first / Never); next.js 538 (vooral commando's).
Niet gelukt: openai/codex AGENTS.md (404); geen primair voorbeeld gevonden van een dagsamenvatting plus statuspagina voor één eigenaar.

## Deel 3 (9 nov, ±22:40, derde agent, links met curl geopend)
28. Besluiten op een vast moment ("betting table"), daarna niet meer ingrijpen: "nobody else can jump in afterward to interfere", "bets are commitments". https://basecamp.com/shapeup/2.2-chapter-08
29. Kanban: werk zichtbaar maken en "limit work in progress (WIP)", "make policies explicit". https://en.wikipedia.org/wiki/Kanban_(development)
30. "Three focused teammates often outperform five scattered ones." https://code.claude.com/docs/en/agent-teams
31. Notities: "structured note-taking ... with minimal overhead" (één NOTES-bestand); voortgangsbestand plus duidelijke commitberichten. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
32. C-compiler: 16 agents op hetzelfde probleem "didn't help", ze overschreven elkaars werk; multi-agent research leed aan "distracting each other with excessive updates". https://www.anthropic.com/engineering/building-c-compiler , https://www.anthropic.com/engineering/multi-agent-research-system
33. Ontwikkelaarsblog: "the fourth agent helps, the ninth is theatre"; "Unreviewed work isn't shipped work. It's inventory." https://crystl.dev/blog/how-many-agents-can-you-run/ (één persoon, geen onderzoek)
Niet gevonden: een bron over een besluitenlog met geldigheidsduur voor AI-agents.
