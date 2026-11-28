# Plakbestand: sleeplink "drag into Blender" en README zonder "not print tested" (Bram, 28 nov 2026, issue #380)

**Plakken door de hoofdchat, na een ja van Daan.** Mag nu al, los van 0.1.3: de link van 0.1.1 werkt vandaag. Bij de plak van gratis 0.1.3 wisselt de link (plakkaart `winkel/plak-gratis-0.1.3.md`, deel 4).

**Waarom (geld):** de gratis Click Joints is de etalage van Pro. JewelCraft haalt 156k downloads met één sleeplink bovenaan zijn README (DERDEN, `organisatie/lat/broncode/jewelcraft.md`). Bij ons staat op GitHub en dortus.com alleen een link naar de pagina, dus wie de README leest moet eerst naar het platform en daar nog eens klikken. Effect op installs: GOK, klein maar gratis. Daarbij zegt de live README nog "not print tested by us yet" (GEZIEN, curl 28 nov 14:00 NL); de verbeterde versie uit #160 is nooit gepusht. Die gaat mee.

## Wat er bewezen is (GEZIEN, 28 nov 2026, Blender 4.2.23 LTS en 5.3.0)
`e2e/toets_sleeplink.py` doet na wat Blender bij het slepen doet (code `bl_pkg`, `_invoke_for_drop` en `_draw_override_after_sync`), zonder het dialoogvenster, met de link zoals hij letterlijk in de README staat:
- link van 0.1.1: bron "extensions.blender.org" gevonden uit `?repository=`, pakket `click_joints 0.1.1` gevonden, geïnstalleerd en aangezet; de bron blijft aan en zoekt updates bij het starten. In beide versies.
- link van 0.1.0 (oudere versie): "NIET GEVONDEN". Blender vergelijkt de link met de nieuwste versie op het platform. Daarom moet de link bij elke gratis versie wisselen; controle regel 5 in `winkel/controle-gratis-0.1.3.sh` vangt een vergeten wissel (FOUT-pad nagedaan).
- Blender neemt elke gesleepte https-link naar een .zip aan; de knop op extensions.blender.org is zelf ook een gewone sleepbare link met dezelfde href. Een link op GitHub of dortus.com werkt dus hetzelfde. Het echte slepen met de muis kon ik hier niet doen (geen scherm met browser en Blender naast elkaar).

Eerlijk over updates: Blender installeert een update niet vanzelf, het meldt dat er een is. Daarom staat er "Blender tells you when there is an update", niet "keeps itself up to date".

## 1. README van `thijsduinhouwer2002-coder/click-joints`
Het hele bestand vervangen door `producten/blender-gewrichten/repo-click-joints/README.md` (main). Verschil met de live README (GEZIEN, diff 28 nov):
- nieuw, onder "Free on the Blender Extensions platform ...":
  `Or drag [this link](https://extensions.blender.org/download/sha256:d1643ba56f09540986a3a951d78fbc5046ad5744fd30c324730ae5b9f980fe3d/add-on-click-joints-v0.1.1.zip?repository=%2Fapi%2Fv1%2Fextensions%2F&blender_version_min=4.2.0) into Blender 4.2 or newer: it installs Click Joints in one step, and Blender tells you when there is an update.`
- Install: "Drag the link at the top into Blender, or open Edit > Preferences > Get Extensions and search "Click Joints". Or download ..."
- uit #160 (al gekeurd, nooit gepusht): "Measured in Blender, not print tested by us yet: print a test joint first." wordt "Measured in Blender. Print the Fit test strip first: every printer is different." met de regel over 4.2; en de reviewregel onder Install.

## 2. dortus.com/click-joints
Tak `claude/cj-sleeplink` in repo `dortus` (commit a1888ce), één zin in de installeeralinea van `click-joints/index.html`: na "search for **joints** and press Install." komt "Quicker: drag this link into the Blender window; it installs in one step, and Blender tells you when there is an update." De link telt mee in Umami als `gratis-sleeplink`. Plakken = de tak in main zetten (geen conflict met main op 28 nov, één regel). Bekeken op 390 en 1280 px: leest als de andere links in de zin.

## Na het plakken
`bash producten/blender-gewrichten/winkel/controle-gratis-0.1.3.sh`: regel 5 moet voor README en dortus.com `GOED ... v0.1.1.zip` geven (tot 0.1.3 live is), en de README mag geen "print tested" meer bevatten (`curl -s https://raw.githubusercontent.com/thijsduinhouwer2002-coder/click-joints/main/README.md | grep -c "print tested"` geeft 0).
