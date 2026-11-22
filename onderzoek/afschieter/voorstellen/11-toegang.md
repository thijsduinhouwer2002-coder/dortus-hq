# Voorstel 11: toegang met officiële sleutels

Nieuw (opdracht Thijs 9 nov 23:50). Eén lijst die Thijs in één keer afwerkt, plus de regels hoe de ploeg sleutels veilig gebruikt. Bronnen met links per punt: `../bronnen/toegang-ruw.md` (uit officiële documentatie, met curl gelezen op 10 nov).
Nieuw bestand voor de repo: `organisatie/toegang.md` (de tekst hieronder vanaf "# Toegang").

---

# Toegang

Doel: de ploeg doet zelf wat met een officiële sleutel kan. Wachtwoorden staan nooit in GitHub. Thijs logt nooit in namens een robot, en een robot logt nooit in als Thijs.

## Wat er nu al is (GEZIEN in `.github/workflows`, 10 nov)
- `JETBRAINS_MARKETPLACE_TOKEN`: nieuwe versies van Bison & Flex uploaden (wordt al gebruikt).
- `MONEYBIRD_SANDBOX_TOKEN`: alleen de proefadministratie voor Klopt.
- `GITHUB_TOKEN`: komt vanzelf, werkt alleen binnen dortus-hq en vervalt na de run.

## De lijst voor Thijs (in deze volgorde: ±5 minuten nu, later nog ±40)

| # | Sleutel | Wanneer | Min | Wat de ploeg er dan zelf mee kan | Wat hij níet kan |
|---|---|---|---|---|---|
| 1 | **Polar: Organization Access Token**, scopes alleen lezen: `orders:read`, `subscriptions:read`, `metrics:read`, `products:read`, `checkouts:read`. Verloopdatum 90 dagen. Secret `POLAR_READ_TOKEN`. | nu | 5 | Elk uur echte verkopen en omzet zien, op het dashboard en in status.md. Dit is de euro-meter. | Prijzen, producten, uitbetalingen of klanten wijzigen. Let op: orders bevatten waarschijnlijk het e-mailadres van de koper (niet bevestigd); de workflow schrijft alleen bedragen en aantallen weg, nooit namen of adressen (dortus-hq is openbaar). Scopes nagekeken in de broncode van Polar (`server/polar/auth/scope.py`). |
| 2b | **GitHub: fine-grained token** voor alleen `rollwright` en `click-joints`, recht Contents: read and write, 366 dagen. Secret `RELEASE_REPOS_TOKEN`. | pas als een manager zelf moet kunnen uitbrengen | 5 | Vanuit een workflow in dortus-hq de openbare bestanden naar die repo zetten en een **concept-release** (draft) maken. De hoofdchat of Thijs drukt op publiceren; dat houdt het besluit van Hans (20:44, advies 6: hooguit één versie per week via Thijs) intact. Nu doet de hoofdchat dit met `publiceer.sh` vanuit een eigen sessie; dat werkt, dus dit is gemak, niet dringend. | Iets buiten die twee repo's, instellingen, leden, verwijderen van de repo. |
| 3 | **Blender: API-token** (profielpagina extensions.blender.org, "API Tokens"). Secret `BLENDER_EXTENSIONS_TOKEN`. | zodra Click Joints 0.1.0 is goedgekeurd | 3 | Nieuwe versies van Click Joints zelf uploaden. | De eerste upload van een nieuwe extensie (gaat met de hand en wordt gekeurd). Scopes niet bevestigd in de docs. |
| 4 | **Polar: tweede token met schrijfrecht** alleen `products:write`, `benefits:write`, `files:write`, `license_keys:write`, `checkout_links:write`, 30 dagen. Secret `POLAR_WRITE_TOKEN`, alleen in environment `polar-schrijven`. | zodra er een tweede betaald product is (bijvoorbeeld Click Joints Pro) | 5 | Een nieuw product met licentiesleutel of downloadbestand klaarzetten (of Polar een conceptstand kent: niet bevestigd, dus het product pas aanmaken als de hoofdchat de prijs heeft gekozen). | Uitbetalingen, bank, KYC. Prijzen gaan wel via deze sleutel: daarom regel 3 hieronder. |
| 5 | **Steam: build-account.** Thijs maakt een tweede Steam-account (alleen voor builds), geeft het in Steamworks alleen "Edit App Metadata" en "Publish App Changes To Steam", logt één keer in met `steamcmd` op zijn eigen computer en zet het bestand `config.vdf` als secret `STEAM_CONFIG_VDF`. Stappenlijst maakt Olaf wanneer het zover is. | pas als er een build is die naar Steam moet (december) | 20 | Builds naar een testtak op Steam uploaden. | Een build live zetten op de hoofdtak, de winkelpagina of prijzen (blijft in Steamworks bij Thijs). Hoe lang die login geldig blijft is niet bevestigd: soms opnieuw. |
| 6 | **dortus.com: Cloudflare Pages-token** (Account API token, alleen "Cloudflare Pages: Edit", verloopdatum). | pas als Klopt echt verkoopt | 10 | De site bijwerken. | DNS, domein, betalen. |

Niet nodig of niet mogelijk:
- **Obsidian**: geen sleutel. Updates komen vanzelf uit GitHub-releases (dus sleutel 2).
- **Garmin Connect IQ**: er is geen upload-API. Elke upload en elke update gaat met de hand door Thijs (verzoek bij Garmin staat op "Acknowledged", CIQQA-4193). Gevolg: plan Garmin-versies zuinig, hooguit één per week, en bundel.
- **Steam Web API-sleutel en financiële sleutel**: alleen te beperken met een vast IP-adres, en GitHub-runners hebben dat niet. Niet aanmaken. Verkoopcijfers leest de hoofdchat voorlopig met Thijs.
- **Moneybird echte administratie**: de persoonlijke sleutel opent volgens Moneybird zelf de hele administratie ("lijkt op een wachtwoord"). Niet aanmaken voor Dortus zelf. Voor Klopt-klanten werkt het via hun eigen OAuth-toestemming.
- **TikTok Shop**: pas na de KvK. App Key en Secret als secret, de winkeltoken ververst de Worker zelf (elke 7 dagen).
- **dortus.com nu**: draait op GitHub Pages (GEZIEN: `server: GitHub.com`). Geen sleutel nodig. Let op: volgens de voorwaarden van GitHub is Pages niet bedoeld voor een commerciële dienst. Een productpagina mag; afrekenen gebeurt toch bij Polar. Bij echte verkoop van Klopt verhuizen (sleutel 6).

## Regels voor de ploeg
1. Een sleutel staat alleen als **repository secret of environment secret** in GitHub. Nooit in een bestand, bericht, logboek, issue of commit. Ook niet een stukje ervan.
2. Een sleutel wordt alleen gebruikt **in GitHub Actions**, in een workflow die draait bij push naar main of met de hand (`workflow_dispatch`), nooit bij `pull_request`. Per platform een eigen environment (`polar`, `blender`, `steam`, ...), zodat een workflow alleen zijn eigen sleutel ziet.
3. **Prijzen, live zetten op Steam, een eerste inzending en alles wat naar klanten gaat** beslist de hoofdchat (of Thijs). Een sleutel die het kan, betekent niet dat het mag.
4. Een workflow print nooit de omgeving of de antwoorden van een API in zijn geheel. Alleen de getallen die nodig zijn. dortus-hq is **openbaar** (GEZIEN via de GitHub API, 10 nov): elke log van Actions en elk bestand is voor iedereen te lezen.
5. Verloopt een sleutel binnen 14 dagen, dan zet de manager van dat platform één regel op de lijst van Thijs: "sleutel X vernieuwen, 3 min".
6. Lekt er toch iets: meteen melden aan de hoofdchat, Thijs trekt de sleutel in (1 minuut), daarna pas uitzoeken hoe.

## Wat altijd bij Thijs of de hoofdchat blijft, ook met sleutels
Accounts aanmaken, inloggen, voorwaarden en overeenkomsten accepteren, betalen, bank, belasting, ID, profielen en winkelpagina's (tekst en uiterlijk op Steam, JetBrains-verkoperspagina), prijzen, de eerste inzending van elk nieuw product, een Steam-build live zetten, elke Garmin-upload, en alles posten (Reddit, forums, sociale media).
