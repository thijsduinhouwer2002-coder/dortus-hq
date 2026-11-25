# Keuring blender-gewrichten, statusregel live zetten, 25-11-2026, automatische keurder
Wat ik keurde: commit 479bf7b9e (44b1131..479bf7b), alleen `producten/blender-gewrichten/KAART.md` (één regel erbij)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is alleen een statusregel: "live op Gumroad en Superhive: 1.2.8, titel met zoekwoorden, kop en alinea B3, Try it free, galerij". Er verandert geen code, add-on of winkeltekst. | Feit | Hoog | Het diff bevat alleen die regel. |
| 2 | Of het echt live staat kan ik niet zien. De regel noemt als bron de hoofdchat en `commercie/geplaatst.md`, geen van beide zit in deze wijziging. | Vermoeden | Midden | `curl` van de twee productpagina's, met versie 1.2.8, de titel en de galerij zichtbaar. |
| 3 | Het commitbericht noemt ook "Click Cuts 1.0.0 vastgezet", maar dat staat niet in het diff. | Feit | Hoog | Een ander bestand in deze commit, of een correctie van het bericht. |
| 4 | De ontwerpkeuring van Daan (25 nov ±07:00) dekt het uitbrengen van Pro 1.2.8 en vraagt dat moet 1 en 2 uit #37 gedaan zijn. Of dat gebeurd is, blijkt hier niet. | Vermoeden | Midden | Het keuringsbestand `2026-11-25-pro-1.2.8-uitbrengen-daan.md`, met moet 1 en 2 afgevinkt. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het bestand blijft ver onder de 400 regels en er staan geen persoonsgegevens, sleutels of tests in het diff. | Feit | Hoog | Bestandsgrootte, geen persoonsgegevens |
| 2 | "Live" staat er zonder label (GEZIEN, DERDEN of GOK). Andere regels in dit bestand zeggen wel "GEZIEN" bij een controle. | Feit | Hoog | Cijfers en beweringen met herkomst |
| 3 | `architectuur.md` hoeft niet mee, want de wijziging raakt geen code. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | De nieuwe regel is een los lijstpunt na een lege regel, terwijl de rest van het bestand vette labels gebruikt. Dat is een kleine stijlafwijking. | Feit | Hoog | Smaak |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Er is niets te spelen of zien. De wijziging is een interne kaart. | Niet van toepassing. | Klein |
| 2 | De galerij (klik, strip, bereik) en de tekst B3 staan nu voor kopers. Ik kan ze niet beoordelen, want ze zitten niet in de wijziging. | Zet in de kaart een verwijzing naar de keuring of blinde test van deze plaatjes en teksten. | Klein |

## Deel C: is het goed genoeg?
Niet beoordeeld. Deze wijziging bevat geen beeld en geen winkeltekst, dus ik geef geen cijfers. Dit oordeel zegt niets over de kwaliteit van de galerij of de tekst die nu live staat. Daarvoor is nog een uitslag nodig: GESLAAGD van de blinde test voor de hoofdbeelden, plus een keuring door Daan.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Zet bij "live" erbij hoe je het zag (bijvoorbeeld "GEZIEN, curl 25 nov 20:25") en wat de pagina's tonen.
2. Verwijs naar het keuringsbestand van de gelijktijdig geplaatste galerij en teksten (B3, titel, Try it free). In deze wijziging is geen keuring of blinde test van die beelden te vinden. Is die er niet, dan is dat een open punt voor Daan.
3. Leg uit of "Click Cuts 1.0.0 vastgezet" uit het commitbericht in een ander bestand staat, of haal het uit het bericht.
4. Controleer dat moet 1 en 2 uit #37 echt gedaan zijn voor 1.2.8, en noteer dat in de kaart.
5. Pas de opmaak van de nieuwe regel aan op de rest van het bestand (vet label).

---
Automatische keurder, model `claude-sonnet-5-5`, 18378 tokens in, 3199 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
