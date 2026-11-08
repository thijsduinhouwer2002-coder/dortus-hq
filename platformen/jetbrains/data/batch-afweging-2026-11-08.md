# Batch (`.bat`, `.cmd`) als tweede product: afweging (Jet, 8 nov 2026, 15:00 UTC)

Labels: GEZIEN (zelf gemeten, route erbij), DERDEN (bron met link), GOK.

## Wat ik zelf mat (Jet)
- Aanraadlijst van de Marketplace voor `*.bat`: CMD Support (5834), Batch Scripts Support (265), BatchCraft (34804). Voor `*.cmd` ook BatchUI (26308) en EPICS Workbench (31029). GEZIEN, `curl -s "https://plugins.jetbrains.com/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.bat"`.
- Totalen om 14:16 en 14:55 UTC gelijk: CMD Support 2.246.192, Batch Scripts Support 2.062.049, BatchCraft 9.585, BatchUI 8.702 (GEZIEN, `/api/plugins/<id>`). **De tellers verversen dus maar één keer per dag.** Nameten binnen dezelfde dag heeft geen zin; de nulmeting van 14:16 (`aanraden-nulmeting-2026-11-08.tsv`) is de basis.
- BatchCraft: versies 1.0.0 (5 okt, 60), 1.0.1 (8 okt, 648), 1.0.2 (10 okt, 8.877), daarna geen versie meer (GEZIEN, `/api/plugins/34804/updates`). De 9.585 zijn dus vrijwel allemaal echte installaties, ±300 per dag. 0 reviews, gemiddelde 4,06 uit 2 stemmen (GEZIEN, `/rating`). Betaald (PAID), proef 7 dagen, productcode PBATCHCRAFT (GEZIEN). Hoeveel er betalen is niet te zien.

## Wat de controleur vond (8 nov, ±15:00 UTC)
- **Hoe de IDE aanbiedt (GEZIEN in intellij-community master, `platform/platform-impl/src/com/intellij/openapi/updateSettings/impl/pluginsAdvertisement/`):** één knop "Install plugins" voor alle gevonden plugins (`PluginAdvertiserEditorNotificationProvider.kt` r.130-139, 169-175, 211), die een dialoog "Choose plugins to install or enable" opent (`PluginsAdvertiserDialog.java` r.43, 63-67). Alles staat alleen vooraf aangevinkt als er één plugin is. Eerst plugins van JetBrains, dan de rest, zonder eigen sortering; betaald of gratis maakt niets uit. Dus: geen automatische installatie van alle drie, de gebruiker kiest (vakjes leeg is uit de code afgeleid, niet in een IDE gezien).
- CMD Support en Batch Scripts Support zijn volgens de Marketplace nog te installeren in 2026.3 (geen until; `compatibleUpdates` met IU-263 geeft 5834, 265 en 34804), maar reviews zeggen "Does not work" (2024, 2025) en "looks abandoned" (2025) (GEZIEN).
- In de IDE zit al gratis kleur voor `.bat` via de TextMate-bundel `batchfile.tmLanguage.json` (GEZIEN), verder niets.
- BatchCraft is sterk: echte parser, aanvullen, navigeren, hernoemen, documentatie, ±10 inspecties met snelle oplossingen, live templates, runner. Geen debugger of formatter in de beschrijving (GEZIEN).
- KITSS TECH: 27 plugins, bijna allemaal 17 tot 48 downloads; alleen BatchCraft en Rolewise (395) erboven (GEZIEN, `/api/vendors/kitss-tech/plugins`). Ook van hen: Graphlume (DOT, 30 downloads).

## Oordeel
**Nee, nu niet naar Hans.** Vraag naar werkende Batch-ondersteuning is er (±1.000 per dag samen naar drie plugins, GEZIEN over 2 dagen), maar betaalbereidheid is niet bewezen: BatchCraft-downloads zijn proefinstallaties zonder zichtbare verkopen of reviews, en BatchCraft dekt al bijna alles wat een Pro zou kunnen bieden. Onze Pro zou moeten winnen op een debugger en formatter, zonder bewijs dat iemand erom vraagt. Volgens de regel (dun bewijs is nee) zoek ik verder.

**Wat het zou veranderen:** reviews of zichtbare verkoop bij BatchCraft, of open verzoeken om een Batch-debugger met stemmen. Volgende meting: de nulmeting van 14:16 opnieuw draaien vanaf 9 nov (dagelijkse groei per plugin, ook Batch en DOT).
