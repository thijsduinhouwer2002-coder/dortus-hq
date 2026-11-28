# Plakkaart gratis Click Joints 0.1.3 (Bram, 28 nov 2026, issue #306)

**Plakken op ma 30 nov, door de hoofdchat, na de plak van Pro 1.2.9.** Vervangt de plakkaart van 0.1.2 (`platformen/blender/indienen.md`, kop "Update 0.1.2"): 0.1.2 staat in geen winkel behalve Printables (direct-zip, 27 nov), 0.1.3 heeft alles van 0.1.2 plus de tenenfix. Niet allebei uploaden.

**Waarom (geld):** de gratis versie is de weg naar Pro. Overal staat nu nog **0.1.1** (GEZIEN, curl 28 nov 02:15 NL: extensions.blender.org noemt alleen 0.1.1, `dortus.com/click-joints/click-joints-free.zip` heeft `version = "0.1.1"`). Op Printables staat de direct-zip 0.1.2 (`commercie/geplaatst.md`, 27 nov). In 0.1.1 en 0.1.2 houdt een knie op een figuur met losse tenen (zoals Blender's Human Base Meshes) kleine teenstukjes in het lijf; wie zo'n STL print, krijgt losse tenen en denkt dat de add-on stuk is. 0.1.3 lost dat op en brengt de meldknop en de reviewregel van 0.1.2 voor het eerst naar de gebruikers. Effect op verkoop: GOK, klein; vooral minder afhakers en slechte eerste indruk.

**Gekeurd:** code en toets Daan ja (8, #326). Automatische keurder ja op f893c68 (`platformen/blender/keuring/2026-11-28-auto-blender-gewrichten-f893c68.md`). E2e **46081457885** op f893c68 (tak `claude/blender-306`) groen in Blender 4.2.23, 5.2.3 en 5.3.0, met de stap "Extensie-zip valideren (zoals extensions.blender.org)" en de tenen-toets (GEZIEN via de API, 28 nov 02:12 NL). De releasenotes hieronder zijn de gekeurde zinnen uit `CHANGELOG.md` (0.1.2, Daan #127; 0.1.3, Daan #326), samengevoegd omdat de gebruikers van 0.1.1 komen.

## Volgorde (stopt bij de eerste fout)
1. Zips ophalen (deel 1) en de sha256 narekenen.
2. extensions.blender.org: deel 2 (extensions-zip, zonder Pro-knoppen).
3. Superhive Lite: deel 3, eerste blok (ook de extensions-zip, als nieuwe versie 0.1.3).
4. dortus.com, Gumroad gratis en Printables: deel 3, de andere blokken (direct-zip, met de Pro-knoppen).
5. Controle: `bash producten/blender-gewrichten/winkel/controle-gratis-0.1.3.sh` moet eindigen op `ALLES GOED`. De regel voor extensions.blender.org blijft `WACHT` tot een moderator 0.1.3 goedkeurt (dagen); dat is geen fout.
6. Regel in `commercie/geplaatst.md` en een regel onderaan `berichten/bram.md` (of een reactie in #306).

## 1. De zips (allebei op main, raw-link werkt zonder inloggen)

| | Extensions-zip | Direct-zip |
|---|---|---|
| Bestand | `producten/blender-gewrichten/uitgave/click_joints-0.1.3.zip` | `producten/blender-gewrichten/uitgave/click_joints_direct-0.1.3.zip` |
| Raw | https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/producten/blender-gewrichten/uitgave/click_joints-0.1.3.zip | https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/producten/blender-gewrichten/uitgave/click_joints_direct-0.1.3.zip |
| Grootte | 49.850 bytes (GEZIEN) | 51.270 bytes (GEZIEN) |
| sha256 | `144664a2f9cd5a3c1b0357fd3c34ba69eff1e2bf23ae74815ebe567eae51104f` (GEZIEN) | `7a943b6946932a9c6c279481c7d5ed9aa0861fc34625ff363f761449653680df` (GEZIEN) |
| Waar naartoe | extensions.blender.org en Superhive Lite | dortus.com, Gumroad gratis, Printables |
| Pro-knoppen | geen (regels 6.1 en 6.3 van Blender) | drie op slot plus "Upgrade to Pro" |

Gebouwd met `e2e/maak_zip.sh` (gratis en direct) uit commit f893c68, dezelfde bron als de groene e2e. Nagekeken (GEZIEN): `version = "0.1.3"` in beide; `toets_zips.py` 0 FOUT (gratis zip gelijk aan de gekeurde sha-lijst, noemt Pro nergens); `toets_direct_zip.py` 0 FOUT (direct-zip is de gratis zip plus `direct.py`). Niet uitpakken, niet hernoemen.

## 2. extensions.blender.org (extensions-zip)
1. https://extensions.blender.org/add-ons/click-joints/manage/ , tabblad versies, **Upload new version**, kies `click_joints-0.1.3.zip`. Inloggen doet Thijs.
2. Releasenotes plakken (Engels, 711 tekens, onder de grens van 1024):
```
Fixed
- A knee joint on a figure with separate toes (for example Blender's Human Base Meshes) no longer leaves small loose pieces of the toes in the body part. The whole foot stays with the lower leg.
- On some figures, a knee joint could leave the sole of the foot as a loose piece. The foot now stays with the leg.

Added
- "Report a problem" at the bottom of the Click Joints tab opens a bug report on GitHub with your Click Joints, Blender and system versions already filled in. Nothing is sent until you submit it yourself.
- After a Good fit and an export, one small line at the bottom of the panel links to the reviews on Blender Extensions. Click the link or the X and it does not ask again. No popups.
```
3. Versturen. Een update gaat opnieuw langs de moderatoren; 0.1.1 blijft tot dan live.
4. Vraagt het formulier om iets anders dan zip en notes (voorwaarden, nieuwe toestemmingen): stoppen en melden in #306. Het manifest vraagt dezelfde toestemming als 0.1.1 ("Export the joint parts as STL or 3MF files"); tagline en tag Sculpt zijn nieuw sinds 0.1.1 (uit 0.1.2, Daan #127).

## 3. De andere plekken
- **Superhive, licentie Lite van Click Joints Pro** (https://superhivemarket.com/products/click-joints-pro): krijgt de **extensions-zip** `click_joints-0.1.3.zip`, niet de direct-zip. De Lite-zin belooft dezelfde code als extensions.blender.org; de direct-zip heeft drie knoppen op slot en "Upgrade to Pro", en wie $3 betaalde hoort dat niet te zien (Daan M1, #340). Nu staat Lite ook op de extensions-zip 0.1.1 (`commercie/geplaatst.md`, 24 nov). Superhive werkt met versies, zoals bij Pro: bij Lite een **nieuwe versie 0.1.3** aanmaken met deze zip en de releasenotes uit deel 2 als changelog, niet alleen het bestand wisselen. In de Lite-tekst alleen het versienummer aanpassen: "Lite is the same code as the free Click Joints 0.1.1 on extensions.blender.org" wordt "Lite is the same code as the free Click Joints 0.1.3 on extensions.blender.org" (GEZIEN, curl 28 nov 02:25 NL: zo staat de zin er nu). De Pro-zip 1.2.9 en de andere teksten niet aanraken.

De direct-zip `click_joints_direct-0.1.3.zip` gaat naar:
- **dortus.com:** in repo `dortus` het bestand `click-joints/click-joints-free.zip` vervangen door `click_joints_direct-0.1.3.zip` (zelfde naam houden: `click-joints-free.zip`).
- **Gumroad gratis** (https://duinhouwer8.gumroad.com/l/click-joints-free): Content-tab, oude zip vervangen. Kopers niet mailen ("Skip for now"; een mail is een bericht onder de naam van Thijs).
- **Printables** (https://www.printables.com/model/1931596-click-joints-free-blender-add-on-for-ball-joints-i): bij Other files `click_joints_direct-0.1.2.zip` vervangen door `click_joints_direct-0.1.3.zip`.

## Na het plakken (Bram)
Tak `claude/blender-306` naar main (hoofdmanager 28 nov: na de plak van 1.2.9), kop in `CHANGELOG.md` naar "## 0.1.3 (2026-11-30)", `click-joints-uitgave.yml` naar VERSIE 0.1.3 met deze zip en sha256. De tenenfix in Pro komt in 1.2.10.
