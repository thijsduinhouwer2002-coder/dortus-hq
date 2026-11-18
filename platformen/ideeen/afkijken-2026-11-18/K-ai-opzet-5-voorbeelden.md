# K. Hoe vijf winnaars hun AI-opzet hebben ingericht (hoofdchat, 18 nov 2026)

Alles GEZIEN: zelf gelezen in de repo's (blobless clone, `git show`), 18 nov ±22:10. Aanvulling op `F-ai-werkwijze.md`.

## 1. OpenStatus (statuspagina's, klein team, $30 tot $500 per maand)
- **Instructies:** `CLAUDE.md` is één verwijzing naar `AGENTS.md`; daarnaast een `AGENTS.md` per app (9 stuks).
- **Instellingen:** `.claude/settings.json` met alleen een SessionStart-hook: `.claude/hooks/session-start.sh` zet in cloudsessies alles klaar (pnpm install, lokale database, skills koppelen, dashboard voorbouwen), zodat de eerste schermafbeelding binnen seconden kan.
- **Skills** in `.agents/skills/` (gedeeld door elke AI-tool): `screenshot` (verplicht na elke zichtbare wijziging, desktop en mobiel), `grill-me` (plan laten doorzagen), `codebase-design`.
- **Commando:** `.claude/commands/ship.md`: alleen git en gh toegestaan; tak maken, opmaak, commit, PR; stopt als er een .env meekomt.
- **Claude in GitHub:** `claude.yml` (Claude reageert op `@claude` in issues en PR's, alleen van eigenaar of teamleden) en `claude-code-review.yml` (bij elke PR een automatische review via `anthropics/claude-code-action@v1`).

## 2. Twenty (CRM, $9 en $39 per gebruiker per maand)
- **Instructies:** `CLAUDE.md` en `AGENTS.md` in de root, plus een eigen `CLAUDE.md` per app-voorbeeld.
- **Instellingen:** attributie uitgezet (geen "Generated with Claude", geen co-author) en een SessionStart-hook die elke sessie de stijlregels inprent: kort, menselijk, **geen gedachtestreepjes**, geen emoji, geen overbodige commentaarregels.
- **Koppelingen (`.mcp.json`):** Postgres (de AI kan de database lezen), Playwright (echte browser, headless), Context7 (actuele documentatie van bibliotheken).
- **Skills:** `qa-scout` (na de e2e-tests in een echte browser 2 tot 4 scenario's testen en de logs lezen), `ui-design`, en zes skills voor hun eigen kernonderdeel.
- **Claude in GitHub:** `claude.yml`, PR-review via een eigen GitHub-app, en **`ci-agent-skills-drift`**: als code verandert waar een skill over gaat, kijkt een agent of de skill verouderd is en zet één opmerking in de PR. Skills verouderen dus niet stilletjes.

## 3. tldraw (tekencanvas, commerciële licentie)
- **Instructies:** `CLAUDE.md` is `@AGENTS.md`; skills staan in `skills/` en zijn gedeeld met Cursor (`.cursor/skills`).
- **Instellingen:** een lijst met **toegestane commando's** (tests, lint, typecheck, `gh pr`, `git add`), zodat de AI niet steeds toestemming hoeft te vragen; een Stop-hook die alle gewijzigde bestanden opmaakt met prettier; een PreToolUse-hook die een verboden commando (yarn) tegenhoudt met uitleg.
- **Skills (±20):** `dotcom-release-marketing` (elke week de wijzigingen omzetten in een concepttekst voor marketing), `pr-walkthrough` (maakt een **video met stem** die een PR uitlegt), `review-translations`, `issue`, `pr`, `commit-changes`, `skill-creator`.
- **Grappig detail:** eigen woorden voor de wachtanimatie ("panning", "zooming").

## 4. GitLens (Git in VS Code, GitKraken, betaald Pro)
- **Instellingen:** de officiële plugin `claude-code-setup` aan; hooks die na elke bewerking de code opmaken (`oxfmt`), een **commentaarbewaker** en een CSS-controle draaien; een PreToolUse-hook die bewerken van gegenereerde stukken in `package.json` blokkeert met de juiste weg; hooks voor aparte werkmappen (worktrees) per taak.
- **Skills (±30):** plannen (`deep-planning`, `challenge-plan`), keuren (`review`, `deep-review`, `ux-review`, `a11y-audit`), uitbrengen (`commit`, `changelog-story`, `audit-commits`), werk beheren (`triage`, `prioritize`, `create-issue`, `update-issues`), en "live" skills waarmee de AI de extensie echt bedient (`live-exercise`, `live-inspect`, `live-perf`).
- **Agents en evals:** een eigen subagent `inspector-driver` met een **eval** (taken plus scorekaart) die meet hoe goed die agent het doet.

## 5. zsviczian (Excalidraw voor Obsidian, solo, 9 mln downloads)
- **Instructies:** één grote `AGENTS.md` (460 regels) plus `docs/agent-workflows/issue-assessment.md` en `issue-resolution.md`, en een overdrachtsdocument voor een tweede agent.
- **Werkwijze:** agent 1 beoordeelt een melding met een vast formulier (feit of vermoeden, zekerheid, wat het bevestigt), de maker kiest, agent 2 bouwt op dezelfde tak. Geen eigen Claude-instellingen of hooks: de kwaliteit zit in de formulieren.
- **CI:** gewone tests, native tests, CodeQL (beveiliging) en een release-workflow.

## Gemene deler
1. Korte hoofdinstructie, kennis dicht bij de code (AGENTS.md per map), skills gedeeld door alle AI-tools.
2. **Hooks doen het saaie werk vanzelf:** sessie klaarzetten, opmaken, verboden dingen tegenhouden met uitleg.
3. **Een lijst met toegestane veilige commando's**, zodat de AI doorwerkt zonder te vragen.
4. **Echte browser of echte app** als controle (Playwright, screenshot-skill, live-skills).
5. **Claude in GitHub zelf:** reageert op `@claude` en keurt elke PR.
6. Skills voor herhaalwerk, ook marketing (release-tekst, PR-video).
7. Bij de groten: meten hoe goed hun agents werken (evals, drift-controle).

## Stand bij Dortus (18 nov) en wat er nog kan
| | Dortus nu | Kan erbij |
|---|---|---|
| Hoofdinstructie | korte CLAUDE.md met wegwijzer | AGENTS.md per product (nu `architectuur.md`) |
| SessionStart | `organisatie/start.sh` via hook | ook klaarzetten van tools (Godot, Blender) voor snellere runs |
| Controles | pre-push privacycontrole, WebFetch geblokkeerd | PostToolUse-hook die check.py op het bewerkte bestand draait (meteen feedback) |
| Toegestane commando's | niet ingesteld | lijst voor git, python3, curl, godot, blender |
| Skills | 5 (bouwen-in-stappen, frontend-design, keuren, uitbrengen, update-tekst) | `screenshot`, `ship`, `triage`, marketing-skills; drift-controle |
| Koppelingen (MCP) | geen in de repo | Playwright (echte browser), Context7 (actuele docs) |
| Claude in GitHub | niet | `claude-code-action`: review per PR en `@claude` in issues; vraagt een Anthropic-sleutel of het abonnementstoken (kosten of verbruik: besluit Thijs) |
| Evals | niet | later |
