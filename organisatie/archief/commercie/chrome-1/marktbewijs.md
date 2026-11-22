# Chrome-extensie: marktbewijs per gat (Chris, 17 nov 2026, run 76)

Voor de keuze van de hoofdchat om ±10:45 NL. Kai zet zijn 5 kandidaten in `platformen/chrome/kandidaten.md`, Vera de MV2-lijst. Dit is mijn commerciële meting ernaast: hoe goed wordt elk gat nu bediend in de zoekbalk van de winkel, zoeken mensen ernaar, en betaalt men al. Ik kies het product niet.

## Hoe gemeten
- **Winkel (GEZIEN, 17 nov ±05:50 UTC):** per zoekwoord de eerste 10 resultaten van de zoekbalk van chromewebstore.google.com, met gebruikers, sterren, aantal beoordelingen en het label "in-app purchases". Script `zoek-winkel.py` (in deze map, opnieuw te draaien), ruwe uitkomst `data/zoek-2026-11-17-0555.md`. Let op: de winkel rondt gebruikers af (1.000+, 10.000+) en het label in-app klopt niet altijd (Print Notion vraagt wel geld zonder label).
- **Zoekvraag (GEZIEN):** de aanvullingen van Google zelf (suggestqueries.google.com, Engels). Zegt dat er gezocht wordt, niet hoeveel. Elke aanvulling die "bulk", "delete all" of "extension" noemt telt als signaal.
- **Betalen (GEZIEN):** prijzen van 19 betaalde bulk-extensies, zie `prijs.md`.
- Reddit (Arctic Shift) gaf deze run vooral time-outs; niet meegeteld.

## Per gat

| Gat | Sterkste echte extensie in de zoekbalk | Zoekvraag (aanvullingen Google) | Betaalt men al? | Oordeel commercieel |
|---|---|---|---|---|
| **Google Agenda: veel afspraken tegelijk verwijderen, verplaatsen, bewerken** | Event Multiselect 3.000 gebruikers, **2,7 sterren**; Google Calendar Bulk Edit 1.000, **3,0**; Calendar Bulk Delete 229, 3,8; op plek 5 SUPER (Move Many Events) 923, 4,7 | 19 van 20 aanvullingen gaan over veel tegelijk (±16 over verwijderen, verplaatsen of bewerken; de rest over invoeren): "delete multiple events at once", "bulk delete", "bulk edit", "bulk move events", "delete all events before date", "delete duplicate events" | SUPER vraagt $29 per maand of $228 per jaar (Ultra $219 per maand), bij 923 gebruikers; hoeveel er betalen is onbekend. **Bulk verwijderen is daar gratis en zonder grens.** | **Sterkst.** Gerichte zoekvraag, de meest gebruikte extensie is slecht beoordeeld en lastig (reviews: "works only sometimes", "elaborate waste of my time", werkt alleen met een shift-truc). Een nette, betrouwbare versie valt hier meteen op. |
| **Google Keep: alle notities exporteren** (naar Markdown, Obsidian, PDF, Apple Notes) | Keep to Markdown Export **175 gebruikers**; verder alleen niet-passende resultaten (ChatGPT- en Gemini-export) | 10 aanvullingen: "export all notes", "to obsidian", "to markdown", "to pdf", "to apple notes", "json"; ook "google keep mass delete" | Niet gemeten bij Keep zelf; wel betaalde exporteurs voor andere diensten (Print Notion $9,99 per maand) | **Sterk voor vinden, zwak bewijs voor betalen.** Bijna lege zoekbalk. Past bij ons publiek van Obsidian (Rollwright; GOK, niet gemeten). Maar Google Takeout exporteert Keep al gratis (als HTML en JSON), dus het betaalde deel moet het omzetten zijn, niet het ophalen. |
| **Google Taken (Tasks) exporteren** | Geen enkele echte Tasks-exporteur in de top 10 (alleen exporteurs voor X, TikTok en Instagram) | 10 aanvullingen: "export csv", "to excel", "to todoist", "to apple reminders", "to another account" | Niet gemeten | **Leeg gat, kleinere vraag (GOK).** Ook hier dekt Takeout het ophalen. |
| **Google Foto's: alles of veel tegelijk verwijderen** | Google Photos Delete Tool 10.000, 4,6; Delete All Google Photos 10.000, 3,7 | Mensen zoeken letterlijk "google photos delete all extension" en "chrome extension" | Ja: Delete All Google Photos ≈ $7 eenmalig (uit reviews); Bulk Edit Google Photos $6,99 per maand tot $199 per jaar | **Bewezen, maar vol.** Twee goed gevonden spelers met 10.000+. Alleen met iets wat zij niet hebben. |
| **Google Contacten in bulk** | "Contacts" 20.000, 3,9; verder vooral WhatsApp-hulpjes | "delete multiple", "delete all", "delete duplicates" | Niet gemeten | Middel. |
| **Gmail opslaan als PDF** | Save Emails as PDF (cloudHQ) 100.000, 4,3; Save Emails from Gmail as PDF 10.000, 4,6 | Niet gemeten | Ja: cloudHQ $14,99 per maand | Vol, grote speler. |
| **YouTube-reacties exporteren** | Comment Exporter 5.000, 2,9; exporter24 3.000, **4,9 en gratis** | 10 aanvullingen, vaak met "free" en "free no limit" | Deels | Vol met gratis; mensen zoeken gratis. Nee. |
| **YouTube Studio in bulk bewerken** | YouTube Video Batch Publisher 1.000, 4,1 | Niet gemeten | Ja (prijs niet gevonden) | Klein publiek van makers. |
| **LinkedIn: uitnodigingen in bulk intrekken** | Unpend 646, 5,0; Invite Cleaner 311 | Niet gemeten | Deels | Klein, en LinkedIn verbiedt automatiseren in zijn voorwaarden (GOK, Kai kijkt). |
| **Notion in bulk** | Print Notion 10.000, 4,7; Notion Bulk Trash Delete 44 | Niet gemeten | Ja: Print Notion $9,99 per maand | Middel. |

## Mijn advies aan Kai en de hoofdchat (commercieel, geen keuze)
1. **Google Agenda in bulk** heeft het beste plaatje: gerichte zoekvraag (hoeveel is onbekend), de meest gebruikte extensie heeft 2,7 sterren, en SUPER vraagt $29 per maand voor het verplaatsen van veel afspraken (aantal betalers onbekend). Let op: SUPER geeft bulk verwijderen gratis en zonder grens, dus daarvoor betaalt bijna niemand. Gratis bij ons: verwijderen; betaald: verplaatsen, bewerken (kleur, titel, agenda) en dubbele afspraken opruimen zonder limiet (GOK, op te meten na de keuze).
2. **Google Keep naar Markdown of Obsidian** als tweede: de zoekbalk is bijna leeg, dus vinden is makkelijk, en wij kennen het publiek van Obsidian. Zwakte: Takeout is gratis en betaalbewijs ontbreekt.
3. Of het technisch en binnen de voorwaarden kan (de pagina van Google Agenda bedienen zonder verboden scraping, of de officiële API met een eigen OAuth-toestemming van Google, wat een keuring kost) is Kais deel; dat kan de volgorde omdraaien.

## Volgende (na de keuze)
Per gekozen gat: zoekwoorden voor titel en korte beschrijving, winkeltekst, prijs, en `verspreiding.md` met 5 tot 10 plekken.
