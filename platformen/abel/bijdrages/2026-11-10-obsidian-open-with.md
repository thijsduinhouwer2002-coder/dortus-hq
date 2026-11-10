# Bijdrage 1: forum.obsidian.md, "Disable Operating System Integration"

Status: klaar voor Daan en Thijs. Abel, 10 nov 2026 03:33 NL.

## Waar
https://forum.obsidian.md/t/120796 (Get help, gesteld 2 nov door Royi, nog geen enkel antwoord, GEZIEN 10 nov 03:35 NL).

## De vraag (kort)
Royi draait Obsidian draagbaar (portable, uitgepakt zonder installatie). Sinds 1.14.2 staat Obsidian in het contextmenu van het besturingssysteem. Hij vraagt of dat uit kan, bijvoorbeeld met een vlag bij het opstarten.

## Wat vaststaat (bron)
De officiële changelog van 1.14.2 (GEZIEN, https://obsidian.md/changelog/2026-09-15-desktop-v1.14.2/): "Obsidian now appears in your operating system's Open with menu, and you can set it as the default app for Markdown files (requires downloading the latest installer)." Het komt dus uit de installer, niet uit de app zelf. In de changelogs van 1.14.0 tot en met 1.15.1 staat geen vlag of instelling om het uit te zetten (GEZIEN, gezocht op "context menu", "operating system", "integration").

## Tekst om te plakken (Engels)
```
Not a full answer, but this might help narrow it down. The 1.14.2 changelog says the "Open with" entry comes from the installer, not from the app itself:

> Obsidian now appears in your operating system's Open with menu, and you can set it as the default app for Markdown files (requires downloading the latest installer).

https://obsidian.md/changelog/2026-09-15-desktop-v1.14.2/

So a copy that never went through the 1.14.2+ installer shouldn't add it on launch, and a CLI flag probably won't change it. If you see it with a purely portable copy, that would be worth a bug report. I couldn't find a setting or flag for it in the changelogs from 1.14.0 to 1.15.1. I haven't tested this on a portable setup myself.
```

## Waarom dit helpt
De vraag staat al acht dagen zonder antwoord. Het antwoord geeft de ene harde feit dat hij nodig heeft (het zit in de installer) met de bron, zegt eerlijk wat we niet weten, en wijst hem de weg (bugrapport als het toch gebeurt). Geen link naar onze producten, geen ervaring die Thijs niet had.

## Regels van de plek
forum.obsidian.md heeft geen AI-regel (zie `communities.md`); de gedragscode vraagt "participate more than you promote". Dit is meedoen zonder promotie. Thijs leest het en plaatst alleen als hij het voor zijn rekening neemt.

## Voor de hoofdchat
Eerst kijken of er intussen iemand antwoordde (dan niet plaatsen, of alleen als het iets toevoegt). Plaatsen als Thijs.Dortus, na een ja van Thijs voor dit bericht. ±2 min.
