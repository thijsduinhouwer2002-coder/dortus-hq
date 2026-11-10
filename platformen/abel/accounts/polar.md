# Polar: kant-en-klaar plan (Abel)

Versie 2, 10 nov 2026 02:55 NL. Status: klaar. Avatar van Mila, akkoord Daan (keuring 2), proef op de echte afrekenpagina bekeken.

## Wat er nu staat (GEZIEN 10 nov 00:45)
- De afrekenpagina van Rollwright Skins (buy.polar.sh/polar_cl_...) heet "Dortus | Rollwright Skins". Organisatie: naam **Dortus**, slug **dortus**.
- Avatar: geen eigen upload. Polar probeert automatisch een logo op te halen bij een logodienst (logo.dev) voor dortus.com. Dat lukt niet: op de afrekenpagina staat nu een **grijs rondje met een letter D** (GEZIEN 10 nov 02:50, `merk/proef/polar-afrekenen-desktop.png` vóór mijn vervanging toonde dat). Dat is het eerste wat een koper naast de prijs ziet.
- polar.sh/dortus (de openbare winkelpagina van Polar) geeft 404: die staat uit. Dat is prima, zie onder.

## Waarom het telt
De afrekenpagina is het moment waarop iemand zijn betaalgegevens invult. Een eigen, scherp logo naast "Dortus" voelt als een echte winkel; een vaag of ontbrekend logo daar kost verkopen.

## Stap 1. Logo (Thijs, ±2 min)
Nagezocht in de openbare broncode van Polar (GEZIEN, github.com/polarsource/polar, `OrganizationProfileSettings.tsx`, 10 nov): bij de organisatie-instellingen staat links bovenaan een veld **Logo**, een klein rondje. Klikken op dat rondje opent het kiezen van een bestand. Toegestaan: jpg, png, gif, webp, svg, tot 1 MB.
1. Inloggen op https://polar.sh en de organisatie **Dortus** kiezen.
2. Links **Settings** (de eerste tab, General). Bovenaan staat "Logo" met het rondje en daarnaast "Organization Name".
3. Klik op het rondje en kies `platformen/abel/merk/avatar-512-v2.png` (37 kB).
4. Naam `Dortus` laten staan. Website `https://dortus.com` laten staan of invullen. Niets anders veranderen.
5. Onderaan op **Save** klikken (zonder opslaan blijft het oude rondje).
6. Controle: open de afrekenlink van Rollwright Skins (staat in de README van rollwright). Linksboven naast "Dortus" moet de lila D staan in plaats van de grijze letter.

Zo ziet het eruit: `merk/proef/polar-afrekenen-uitsnede.png` (de echte afrekenpagina, alleen in mijn browser het rondje vervangen). Op 24 px rond leest het als een lila D op donker; de gouden scharnieren worden daar spikkels, zoals Daan al zag (kan-punt 7), maar het blijft herkenbaar en veel sterker dan de grijze letter.

## Stap 2. Openbare winkelpagina: uit laten
De Polar-winkelpagina (polar.sh/dortus) toont alleen wat we via Polar verkopen (nu alleen Rollwright Skins). Kopers komen via de plugin, niet via die pagina. Een halflege winkel met één product wekt minder vertrouwen dan geen winkel. Aanzetten pas als er drie of meer producten via Polar lopen.

## Klaar als
Op de afrekenpagina staat de lila D naast "Dortus".
