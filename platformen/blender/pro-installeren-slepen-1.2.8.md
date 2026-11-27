# Click Joints Pro 1.2.8: installeren met slepen en de Mac-valkuil (Bram, 27 nov 2026, issue #258)

**Waarom (geld, saledag):** de Docs-tab van Pro op Superhive en "After you buy" op Gumroad noemen alleen Install from Disk (curl 27 nov ±10:15 NL, GEZIEN). Een koper op een Mac wiens zip door Safari een map werd, loopt vast: Blender installeert geen map. Dat kost een terugbetaling of een slechte beoordeling (GOK, klein maar juist vandaag). Click Cuts heeft sinds vanochtend dezelfde zinnen (#250, Daan ja #254, commit 527385c9); dit is dezelfde familie, dus dezelfde woorden.

Plakken door de hoofdchat, vóór de laatste meter van 20:00. Drie blokken, elk met waar het hoort. Alles wat niet in een blok staat, blijft zoals het nu live staat.

## Plakken 1: Superhive, Click Joints Pro, tab Documentation
https://superhivemarket.com/products/click-joints-pro/docs

Vervang alleen de alinea die begint met **Install:** (eerste alinea onder "Getting started"). "Install:" blijft vet, net als nu.

```
Install: open Blender 4.2 or newer. Drag click_joints_pro-1.2.8.zip from your Superhive download into the Blender window and confirm. Do not unzip it. Or go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right, choose Install from Disk and pick the zip. Got a folder instead of a zip? See the FAQ. Updating from an older Pro? Install the new zip the same way.
```

De alinea "Coming from the free version: turn the free one off first..." blijft staan tot 1.2.9 live is (1.2.9 zet de gratis zelf uit, #114).

## Plakken 2: Gumroad, Click Joints Pro, beschrijving, kopje "After you buy"
https://duinhouwer8.gumroad.com/l/click-joints-pro (bewerken in Gumroad)

Vervang alleen de eerste opsommingsregel "Install: ..." onder "After you buy" door deze twee regels (de regels "Coming from the free version" en "Open the panel" blijven). Gumroad heeft geen FAQ, dus de Mac-zin staat hier zelf.

```
- Install: open Blender 4.2 or newer. Drag click_joints_pro-1.2.8.zip from your Gumroad library into the Blender window and confirm. Do not unzip it. Or go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right, choose Install from Disk and pick the zip.
- Got a folder instead of a zip? Safari on a Mac can unzip downloads by itself, and Blender cannot install a folder. Download it again with another browser, such as Chrome or Firefox, and drag the zip into Blender without opening it.
```

Zelfde wijziging voor de inhoudspagina (Content-tab, boven de zip) als die geplaatst wordt: in Plakken B van `platformen/blender/pro-gumroad-na-kopen-1.2.8.md` wordt de regel "1. Install: ..." dan:

```
1. Install: drag the zip below into the Blender window (Blender 4.2 or newer) and confirm. Do not unzip it. Or use Edit > Preferences > Get Extensions, drop-down menu at the top right, Install from Disk.
   Got a folder instead of a zip? Safari on a Mac can unzip downloads by itself. Download it again with another browser and drag the zip into Blender.
```

## Plakken 3: Superhive, Click Joints Pro, tab FAQ
https://superhivemarket.com/products/click-joints-pro/faq

Nu staan er twee vragen (curl 27 nov ±10:15 NL, GEZIEN). Zet deze twee vragen bovenaan, vóór "Can I use the free Click Joints and Pro at the same time?". Vraag vet, antwoord eronder, zoals de bestaande.

```
How do I install it?
Drag click_joints_pro-1.2.8.zip into the Blender window and confirm. Do not unzip it. Or go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right, choose Install from Disk and pick the zip. Then press N in the 3D viewport and open the Click Joints tab.

The install failed or I got a folder instead of a zip. What now?
Safari on a Mac can unzip downloads by itself, and Blender cannot install a folder. Download it again with another browser, such as Chrome or Firefox, and drag the zip into Blender without opening it. Also check your Blender version: click the Blender logo at the top left, then About Blender. Click Joints Pro needs Blender 4.2 or newer and does not install in older versions. Still stuck? Send a message through Superhive with your Blender version and a screenshot of the error.
```

Vervang in dezelfde tab ook het antwoord bij "Will the joints fit on my printer?" (het zegt nog "Print one small joint first", terwijl de gekeurde Docs-tab de Fit test strip noemt):

```
The default clearance of 0.2 mm works on most well tuned printers, but every printer is different. Print the Fit test strip first: in the Pro part under Print this first, click Fit test: ball or Fit test: hinge. You get five joints from 0.10 to 0.30 mm. Pick the one that turns smoothly without wobble and set Clearance (mm) to that number.
```

## Waar elke bewering vandaan komt
| In de tekst | Bron |
|---|---|
| Slepen naar het Blender-venster, vanaf 4.2 | Blender 4.2 handboek: "drag-and-drop an extension .zip package into Blender" (DERDEN, https://docs.blender.org/manual/en/4.2/editors/preferences/extensions.html, zelfde bron als Click Cuts #250) |
| Safari kan een zip vanzelf uitpakken | Apple: "Safari decompresses files such as .zip files after it downloads them" (DERDEN, https://support.apple.com/en-gb/guide/safari/sfri40598/mac). "can", want het hangt af van een instelling; de naam ervan noemen we niet (niet nagelezen) |
| Blender installeert geen map | Install from Disk vraagt om een .zip (handboek, zelfde pagina) |
| 4.2 of nieuwer, oudere versies niet | `click_joints/blender_manifest.toml` `blender_version_min = "4.2.0"`; geen `bl_info` in de code (grep 0, GEZIEN), dus het oude add-on-menu laadt hem niet |
| Blender-logo linksboven > About Blender | DERDEN, https://docs.blender.org/manual/en/4.2/interface/window_system/topbar.html |
| `click_joints_pro-1.2.8.zip` | live op Superhive Docs en Gumroad (curl 27 nov, GEZIEN); e2e `click_joints_pro-${PRO_VERSIE}.zip` (`.github/workflows/blender-gewrichten-e2e.yml` r. 123) |
| N, tab Click Joints; Fit test: ball/hinge, 0.10 tot 0.30 mm, Clearance (mm) | gekeurde Docs-tab `platformen/blender/superhive/docs-tab-1.2.8.md` (Daan #130) |
| "Send a message through Superhive" | Superhive heeft een berichtknop ("Login to message", curl FAQ-pagina, GEZIEN) |

**Bewust weggelaten:** "FDM and resin" uit het fit-antwoord (geen bron voor resin, zelfde reden als bij de Docs-tab). "not print tested" of "we printed": nergens.

**Na 1.2.9 (niet vóór ma 30 nov):** zipnaam wordt `click_joints_pro-1.2.9.zip` in alle drie de blokken; "Coming from the free version" wordt "Pro turns it off for you."

## Stand
- 27 nov ±10:20 NL: concept klaar, keuring gevraagd aan Daan (#262). Apple-pagina gaf om 10:20 een 429 bij curl; de zin is vanochtend voor Click Cuts nagelezen (#250, DERDEN). Blender-zin opnieuw nagelezen 10:20 (GEZIEN).
