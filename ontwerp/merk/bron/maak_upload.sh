#!/bin/sh
# Abel: zet de definitieve beelden per account in upload/, met namen die zeggen waar ze heen gaan, plus een zip.
# Draai vanuit platformen/abel/:  sh merk/bron/maak_upload.sh   (standaard v2b, akkoord Daan keuring 5; v2 alleen als terugval)
set -e
V=${1:-v2b}
rm -rf upload && mkdir -p upload/1-steam upload/2-polar upload/3-github upload/4-blender upload/5-obsidian upload/6-dortus-com upload/7-superhive
cp merk/avatar-184-v2.png                upload/1-steam/profiel-en-groep-avatar-184.png
cp merk/steam-kop-1500x220-v2.png        upload/1-steam/ontwikkelaarspagina-kop-1500x220.png
cp merk/steam-logo-1200x460-$V.png       upload/1-steam/ontwikkelaarspagina-logo-1200x460.png
cp merk/steam-achtergrond-1920-v3.png    upload/1-steam/ontwikkelaarspagina-achtergrond-1920x1200.png
cp merk/avatar-512-v2.png                upload/2-polar/logo-512.png
cp merk/avatar-512-v2.png                upload/3-github/profielfoto-512.png
cp merk/social-1280x640-$V-nu.png        upload/3-github/social-preview-rollwright-en-click-joints-1280x640.png
cp merk/avatar-512-v2.png                upload/4-blender/blender-id-avatar-512.png
cp merk/avatar-512-v2.png                upload/5-obsidian/forum-profielfoto-512.png
cp merk/og-1200x630-$V-nu.png            upload/6-dortus-com/og-home-1200x630.png
cp merk/superhive-avatar-400.jpg          upload/7-superhive/account-avatar-400.jpg
cp merk/superhive-banner-2400x660.png     upload/7-superhive/winkel-banner-2400x660.png
cp merk/superhive-banner-1200x330.png     upload/7-superhive/winkel-banner-1200x330-reserve.png
cp merk/LEESMIJ-upload.md                upload/LEESMIJ.md
rm -f dortus-beelden.zip && (cd upload && zip -qr ../dortus-beelden.zip .)
echo "upload/ en dortus-beelden.zip gemaakt met versie $V"
