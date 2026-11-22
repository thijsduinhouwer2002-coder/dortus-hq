# Marktbewijs: sync en samenwerken in Obsidian (Chris, 9 nov 2026, ±00:45 tot 01:05 UTC)

Waarom: open punt 3 uit ronde 5 van Olaf (`platformen/obsidian/volgend-product.md`): "Sync en samenwerken alleen als er een smalle plek is (Remotely Save PRO staat stil, nagaan of er een opvolger is)". Ik kies het product niet; dit is alleen het bewijs. Gemeten door een onderzoeker (agent), nagekeken door een controleur (agent): akkoord mits, alle moet-punten verwerkt.

## Hoe gemeten
Downloads uit `community-plugin-stats.json` van obsidianmd/obsidian-releases: commit 6a3f2be8 (3 nov 00:13:47 UTC) tegen b65f4503 (9 nov 00:16:08 UTC), 6,00 dag. Vanaf 3 nov omdat downloads tot ±1 nov veel nep bevatten (zie ronde 5). "Beste versie" is de grootste toename van één versie. Prijzen met curl op de prijspagina's. Alles GEZIEN door onderzoeker en controleur, tenzij anders vermeld.

| Plugin | Prijs en vorm | Totaal 9 nov | Per dag totaal / beste versie | Laatste update |
|---|---|---|---|---|
| obsidian-git | gratis, eigen git-remote | 3.427.654 | 5.694 / 3.204 | 5 nov 2026 |
| obsidian-livesync | gratis, eigen CouchDB, S3 of P2P | 1.096.723 | 3.605 / 1.387 | 7 nov 2026 |
| remotely-save | basis gratis; PRO "FREE while beta before Jan 1, 2027. The price will be determined later." (remotelysave.com/pricing) | 2.366.518 | 2.281 / 2.158 | 20 okt 2024 |
| nutstore-sync | gratis, vast aan de dienst Nutstore | 248.944 | 1.070 / 993 | 27 okt 2026 |
| fast-note-sync | gratis, eigen server | 181.624 | 500 / 411 | 20 jul 2026 |
| google-drive-sync | gratis | 201.341 | 415 / 414 | 26 aug 2026 |
| easy-sync | gratis (MIT) | 26.197 | 359 / 130 | 8 nov 2026 |
| system3-relay (Relay) | Free $0, Hobby $5 per maand (tot 3 gebruikers), Starter $6 per gebruiker per maand, Premium $18 (relay.md/pricing) | 228.268 | 276 / 176 | 9 sep 2026 |
| sync-engine | gratis (MIT): WebDAV, S3, Google Drive, Dropbox, slim samenvoegen bij conflicten | 53.991 | 248 / 210 | 8 nov 2026 |
| onedrive-sync | gratis (MIT) | 26.951 | 187 / 187 | 10 okt 2026 |
| nextcloud-sync | gratis (MIT) | 24.214 | 173 / 170 | 27 okt 2026 |
| sync-vault-ce | freemium: ¥11,9 per maand, ¥72 per jaar, ¥199 eenmalig (kqiu.top/product/sync-vault/) | 16.825 | 60 / 50 | 3 nov 2026 |
| synch | eigen dienst: Free, $1 per maand of $10 per jaar, Plus $9 per maand (synch.run/pricing) | 10.720 | 60 / 35 | 5 nov 2026 |

Prijsanker: Obsidian Sync $4 per gebruiker per maand bij jaarbetaling, $5 per maand los (obsidian.md/pricing, GEZIEN).

## Remotely Save PRO
- Staat stil: laatste release 0.5.25 op 20 okt 2024, laatste commit 10 nov 2024 (GEZIEN, kloon). Toch nog ±2.158 installs per dag op die versie.
- PRO bestaat uit "PRO connect" (OneDrive Full, Google Drive, Box, pCloud, Yandex Disk, Koofr, Azure Blob) en "PRO merge" (slim samenvoegen of dupliceren bij een conflict), met een account op remotelysave.com (GEZIEN).
- Er wordt niets verkocht: gratis tot 1 jan 2027, prijs "later". Wat er na 1 jan gebeurt is onbekend (GOK).
- Open issues en meest gemelde problemen: niet gemeten (GitHub gaf 403 in deze run).

## Opvolgers die het gat al vullen (controleur)
- **sync-engine** (MIT, bijgewerkt 8 nov 2026, 248 per dag) doet Google Drive, Dropbox, WebDAV en S3 met slim samenvoegen, gratis, en zet zich in zijn README af tegen Remotely Save ("development paused for years"). Alleen OneDrive ontbreekt.
- google-drive-sync (415 per dag) en onedrive-sync (187 per dag) vullen de losse diensten gratis. Daarnaast ±20 kleine Google Drive-plugins en powerconnect, rclone-bisync, mdsync (GEZIEN in community-plugins.json, niet gemeten).
- Nieuwe groei bij "eigen opslag" gaat bijna helemaal naar gratis MIT-plugins: easy-sync, sync-engine, onedrive-sync en nextcloud-sync samen ±970 per dag.

## Wat mensen vragen (forum, likes van het hele topic, GEZIEN)
1. Sync op de achtergrond op mobiel (t/25906): 396 likes, 17.641 views. Kan niet in een plugin (README Remotely Save: "technically impossible", DERDEN).
2. Obsidian Sync met eigen server (t/20975): 215 likes, 141.410 views; live samen bewerken (t/6058): 104 likes, 44.254 views. Wordt al gedaan door LiveSync (gratis) en Relay (betaald).
3. iOS met eigen opslag (WebDAV, Dropbox): veel views (1.000 tot 4.200 per draad in 2026), weinig likes: mensen zoeken uitleg, geen product.

## Oordeel (voor Olaf en Hans)
**Geen smalle plek met betaalbewijs.** Betalen gebeurt bij Relay, Synch en Sync Vault, maar van geen van drieën is een klant- of omzetcijfer te zien; Remotely Save verkoopt zelfs nog niets. Het gat dat Remotely Save achterlaat wordt al gratis gevuld door sync-engine en losse plugins per dienst, en Obsidian Sync zet het plafond op $4 per maand. Wie betaalt: onbekend. Hoeveel: hooguit ±$1 tot $2 per maand (GOK). Bewijs: geen.
**Wat dit zou veranderen:** na 1 jan 2027 een prijs voor Remotely Save PRO, of een golf klachten van Remotely Save-gebruikers die PRO kwijt zijn (forum en issues meten rond 5 jan 2027), of een omzetcijfer van Relay of Synch.
