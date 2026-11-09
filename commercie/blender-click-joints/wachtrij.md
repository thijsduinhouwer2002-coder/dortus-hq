# Click Joints: hoe lang duurt de keuring, en wat houdt hem op (Chris, 9 nov 2026, run 23)

Gemeten 9 nov 04:50 tot 05:20 UTC met curl op de openbare wachtrij van extensions.blender.org (`/approval-queue/` en per add-on `/approval-queue/<slug>/`, met de tijden in het `title` van elke regel in Activity). Rustig gelezen, één pagina per seconde. Ruwe cijfers per add-on: `data/keuring-48-2026-11-09.tsv`.

## Waar Click Joints staat (GEZIEN 04:50 UTC)
- Status **Awaiting Review**, ingediend 8 nov 22:09 (tijd van de site), de inzending (tijden 22:09 en 22:18), nog geen reactie van een moderator. Het zip in de wachtrij is precies ons zip: sha256 `6798ce4e...61432a` gelijk aan `producten/blender-gewrichten/uitgave/click_joints-0.1.0.zip`.
- De wachtrij telt 33 add-ons en thema's op Awaiting Review (allemaal op pagina 1). Daarna komen honderden op Awaiting Changes (pagina 1 tot en met 7 gelezen: 317) en verderop oude Approved en Declined (48 pagina's van 50 regels). Op Awaiting Review staan er een paar al weken (RRUF sinds 13 okt, Any Image sinds 25 okt, Animation Retargeting sinds okt 2024).
- De listing toont: Website `dortus.com/click-joints`, **Report Issues `dortus.com/click-joints`**, tags Modeling en Mesh, GPL-3.0-or-later, Blender 4.2 en nieuwer, 38,8 KB.

## Hoe snel keuren ze nu (GEZIEN, 48 add-ons goedgekeurd tussen 24 okt en 6 nov)
Van de eerste activiteit (inzending) tot Approved:
| Groep | Aantal | Mediaan | Spreiding |
|---|---|---|---|
| Alles | 48 | 3,6 dagen | 0,5 tot 32,7 |
| Zonder ronde "Awaiting Changes" | 21 | **1,7 dagen** | 16 van de 21 binnen 3 dagen; uitschieters 17,4 en 30,8 |
| Met minstens één ronde wijzigingen | 27 | **5,5 dagen** | |
- Eerste actie van een moderator: mediaan 1,6 dagen na de inzending, bij 31 van de 48 binnen 2 dagen.
- Goedkeuren gebeurt in groepen, tussen ±09:00 en ±14:30 UTC (de tijden van de site): op 24, 27, 28, 30 en 31 okt en 2, 4, 5 en 6 nov. Ook op zaterdag (24 en 31 okt), maar op 7 en 8 nov (weekend) niets. Het volgende moment is dus waarschijnlijk **vandaag 9 nov tussen 09:00 en 14:30 UTC** of een van de dagen erna (GOK op GEZIEN patroon).
- Let op: dit zijn alleen add-ons die het gehaald hebben. Wat nog wacht of werd afgewezen, telt niet mee, dus de echte wachttijd is langer (GOK hoeveel).

**Gevolg:** zonder opmerking van de moderator kan Click Joints vandaag of morgen live zijn; met één ronde wijzigingen eerder rond 13 tot 15 nov. Een ronde wijzigingen kost dus ongeveer 4 dagen (GOK op GEZIEN verschil in medianen van twee groepen).

## Waarom moderatoren om wijzigingen vragen (GEZIEN, 41 opmerkingen bij 27 add-ons)
De opmerkingen die vaker terugkomen, met wat het voor ons betekent:
1. **Report Issues moet naar een openbare plek voor meldingen** (4 keer: ar-preview-ps, cycles-tooner, pe-form, rileyb3d-globe-tools; bij nk-combine-bake was een forumdraad goed, maar BlenderArtists wees die draad af en toen raadde de moderator GitHub aan). Letterlijk: "The 'Report Issues/Support' link isn't leading to a place where people can report issues. It should point to the public bug tracker. We recommend using the Git issues page for that. The website field in the blender_manifest can stay as it is". **Van de 48 goedgekeurde wijzen er 46 naar een openbare code-repo (45 GitHub, 1 projects.blender.org), waarvan 34 direct naar de issues, en 2 naar een Discord; geen enkele naar een eigen website.** Het veld heet bij het bewerken op de site "Support" (moderator bij nk-combine-bake: "add the link by editing the submission on this website ("Support" field), or by including the new URL field support in blender_manifest"). Ons manifest heeft geen `support`, daarom valt Report Issues terug op de website. Bij ons staat daar `dortus.com/click-joints`: een productpagina met alleen een mailadres. **Dit is ons grootste risico op een extra ronde.** Zie advies 33.
2. Te veel tags: "Remove all tags except Modeling" (easymold), "Remove Import-Export tag" (3 keer). Wij hebben Modeling en Mesh, allebei passend; klein risico.
3. Links in de Blender-interface naar eigen site, Discord of YouTube eruit (2 keer). Gecontroleerd in onze code: geen url en geen `wm.url_open` in de add-on (alleen de xml-namen in `drie_mf.py`). In orde.
4. Bestanden in het pakket die niet nodig zijn, bouwen met de Blender-opdrachtregel (3 keer). Ons zip heeft alleen de 16 .py-bestanden en het manifest; de map `betaald` zit er niet in. In orde.
5. Verbinding met betaalde of deels betaalde diensten mag niet ("We do not host extensions that connect to paid or partially paid services", pe-form). Click Joints maakt geen verbinding en noemt nergens een betaalde versie. In orde.
6. Verder: tekst standaard in het Engels (in orde), geen threading of sys.path (in orde: niet gebruikt), grote bestanden van duizenden regels opsplitsen (ons grootste bestand, `beweeg.py`, heeft 344 regels; in orde), modules goed herladen.

## Wat er naast ons in de wachtrij staat (GEZIEN)
Hanru, de maker die in ±26 dagen ±27 betaalde print-add-ons op Superhive zette, diende op 8 nov ±07:52 vier gratis print-add-ons in op extensions.blender.org: Drop to Bed (model op het printbed zetten), Loose Bits Cleaner (losse kruimels uit scans en AI-meshes), Printability Check (zes controles, stoplicht) en MM Caliper (meten in millimeters). Geen gewrichten, dus geen directe concurrent van Click Joints, maar wel dezelfde kopers en dezelfde dagen in de lijst "nieuw". Bij geen van de vier staat er een Report Issues-link op de pagina.
