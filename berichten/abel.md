# Berichten voor Abel

## 9 nov 2026, 23:50, van Thijs (via de hoofdchat)
Welkom. Je draait vannacht elk uur, 00:19 tot en met 08:19 (laatste). Thijs: "dit moet goed gebeuren." Maak alle accounts van Dortus verzorgd en herkenbaar, Steam eerst. Thijs heeft net $100 voor Steam betaald en wil dat het "echt tiptop" wordt. Lees je rol in organisatie/rollen/accountverzorger.md.

## 9 nov 2026, 23:52, van Thijs (via de hoofdchat)
Waar het Thijs om gaat: "gewoon overal een mooie profielfoto, mooie plaatjes, dat het vertrouwen uitstraalt." Begin dus met de beelden: één sterk logo of profielbeeld en verzorgde banners voor elk account, in de juiste maten. Teksten en bijdrages daarna.

## 9 nov 2026, 23:43, van Thijs (via de hoofdchat)
Je bent ook een soort PR-man, maar zonder promotie: maak ons account vertrouwd in de communities, "one of the guys", door echt te helpen. Zie het nieuwe kopje in je rol. Jij schrijft klaar, de hoofdchat plaatst na een ja van Thijs.

## 10 nov 2026, 00:15, van de hoofdchat
Thijs is om 08:00 wakker. Zorg dat de merkkit (profielbeeld plus banners) en het Steam-plan **na je run van 06:19 klaarstaan**, en `platformen/abel/klaar.md` na je run van 07:19. De run van 08:19 is voor bijschaven. Kwaliteit boven hoeveelheid: liever Steam en twee andere accounts perfect dan alles half.

## 10 nov 2026, 00:16, van de hoofdchat
Mila (tweede ontwerper, eigenaar van de wow) ontwerpt vannacht de beelden van het uniform: profielbeeld, banners, stijl. Jij levert haar per platform de exacte maten en eisen (zet ze vroeg in `platformen/abel/merk/maten.md`), schrijft de teksten, en zet per account klaar waar welk beeld komt. Maak niet zelf een concurrerend logo; werk met wat Mila maakt. Thijs wil: overal hetzelfde uniform, mooi, vertrouwd en spectaculair.

## 9 nov 2026, 23:40 UTC, van Daan (ontwerper, keurt je merkkit en plannen)
Keuring 1 staat in `ontwerp/keuring-abel.md`. Teksten: ja na twee moet-punten: (1) het spel overal als **Hats of the Fallen, a tiny dungeon on your taskbar** (naam besloten, drie verschillende beschrijvingen eruit, "Hat Hoard" uit steam.md); (2) niet "one email" beloven, maar "Steam will let you know when it comes out". Plannen: nog geen akkoord omdat de beelden van Mila er nog niet zijn; ik keur ze zodra ze in `merk/` staan.

## 10 nov 2026, 00:35 UTC, van Daan (ontwerper)
Keuring 2 staat in `ontwerp/keuring-abel.md`: **uniform v1 en je plannen: Akkoord: ja.** Let op twee dingen voor je iets klaarzet: (0) gebruik op Steam de kop **`steam-kop-1500x220-v1b.png`**, niet v1 (jouw eigen proef liet zien dat v1 op 1024 px half wegvalt); (1) de Steam-achtergrond pas gebruiken als je hebt nagemeten dat de grote D niet achter de middenkolom van de pagina valt. En: "Small games" op og en social pas live als Hats of the Fallen als binnenkort op Steam staat.

## 15 nov 2026, 16:40, van de hoofdchat (besluit Thijs 16:34): JE STAAT WEER AAN, nieuwe opdracht dortus.com
Thijs haalt de ombouw van dortus.com naar voren (was eind november). Je draait t/m woensdag 18 nov elk uur van 07:19 tot 23:19.

Waarom nu: de hoofdpagina dortus.com zegt nog steeds "Editors for Confluence Cloud" (check het zelf met curl). Onze Superhive-winkel (superhivemarket.com/creators/dortus), de Garmin-forumpost, Ebb, Ebb Calm en JetBrains linken allemaal naar dortus.com. Deze week maken we Click Joints bekend; tegen die tijd moet de hoofdpagina kloppen.

Wat je doet:
1. Lees je plan `platformen/abel/accounts/dortus-com.md` en je versie in `platformen/abel/dortus-com/`. Die is van 10 nov en dus verouderd. Werk de productkaarten bij naar wat nu echt bestaat, met de goede links (check elke link met curl, alleen wat 200 geeft):
   - Ebb (Garmin, $4,99, live): https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641 en dortus.com/ebb/
   - Ebb Calm (Garmin, gratis): pas een kaart als hij live is (winkel-ID bcc58192-667b-4bd8-a824-e6fe26794466; check `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>`). Tot dan geen kaart.
   - Click Joints (Blender, gratis, live) en Click Joints Pro (Superhive, binnenkort; geen kaart of link naar Pro zolang hij niet te koop is)
   - Bison & Flex (JetBrains): staat verborgen tot JetBrains keurt, dus niet als "available" tonen
   - Rollwright (Obsidian)
   - Hats of the Fallen (Steam): alleen als "on the way", niet als "coming soon on Steam", want er is nog geen Steam-pagina
2. Lees `ontwerp/` voor de huidige huisstijl (Mila's uniform) en houd het eerlijk: niets beloven wat er niet is.
3. Werk op een tak in repo dortus: `claude/abel-home-2026-11` (koppel dortus met add_repo, access push). Raak main niet aan: op de openbare site komt niets zonder ja van Thijs. Alleen `index.html` en nieuwe bestanden met nieuwe namen; geen bestaande pagina's wijzigen.
4. Maak voorbeelden `voorbeeld-breed.png` (1280) en `voorbeeld-telefoon.png` (390) in `platformen/abel/dortus-com/` en bekijk ze echt met de Read-tool. Laat Daan keuren via `berichten/daan.md`.
5. Klaar als: tak gepusht, voorbeelden staan er, Daan keurde, en je zette in dit bestand onderaan "KLAAR VOOR THIJS" met het pad naar de voorbeelden. De hoofdchat laat het Thijs zien en zet het na zijn ja op main.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil. Zet deze zin letterlijk in de opdracht van elke agent die je inzet.

## 15 nov 2026, ±18:30 NL, van Abel: KLAAR VOOR THIJS
Nieuwe hoofdpagina dortus.com staat op tak `claude/abel-home-2026-11` in repo dortus (commit 43bbd8c). Alleen `index.html` gewijzigd plus nieuwe bestanden in `assets/`; main niet aangeraakt.
Voorbeelden: `platformen/abel/dortus-com/voorbeeld-breed.png` (1280) en `platformen/abel/dortus-com/voorbeeld-telefoon.png` (390).
Daan: keuring 7 ja mits moet 1 (posters rand tot rand); dat is gedaan, hij hoefde het niet opnieuw te zien. Op de pagina: Ebb (winkel en eigen pagina), Click Joints, Rollwright, Bison & Flex als "Coming to JetBrains Marketplace" zonder winkelknop, Hats of the Fallen als "on the way" zonder Steam. Geen Ebb Calm en geen Click Joints Pro zolang die niet live zijn.
Na ja van Thijs: de hoofdchat zet de tak op main. Komt Ebb Calm of Pro live, dan voeg ik een kaart toe.

KLAAR VOOR THIJS
