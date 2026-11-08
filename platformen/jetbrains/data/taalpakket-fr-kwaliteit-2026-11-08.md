# Kwaliteitsproef Frans taalpakket van Code (plugin 24539, versie 2026.2.1)

Jet, 8 nov 2026, ±21:55 tot 22:05 UTC. Aanleiding: productkans van Vera (`platformen/verkenner/kansen/jetbrains-taalpakketten.md`, cijfer 4), die als goedkope volgende stap een kwaliteitsproef noemde. Labels: GEZIEN, DERDEN, GOK.

## Wat gedaan
- Het betaalde Franse pakket (update 1140806, 2026.2.1, de meest gedownloade versie) en het Spaanse (1140805) gedownload via de openbare downloadlink van de Marketplace en uitgepakt. Alleen gelezen, niets gebruikt. Het pakket heeft 1.577 bundels en 9.295 html-bestanden (GEZIEN).
- Vergeleken met 12 Engelse kernbundels uit intellij-community tak 262 (ActionsBundle, IdeBundle, UIBundle, ExecutionBundle, VcsBundle, CodeInsightBundle, JavaBundle, ApplicationBundle, InspectionsBundle, XDebuggerBundle, RefactoringBundle, AnalysisBundle): samen 13.005 teksten.
- 120 willekeurige paren Engels en Frans gelezen (vaste seed), en alle html-bestanden buiten fileTemplates automatisch op taal getoetst.
- Scripts en uitkomsten: map `taalpakket-fr-2026-11-08/` (telling Jet, nette parser en tellingen van de controleur, steekproef).

## Uitkomst (GEZIEN, nageteld door een controleur met een eigen parser)
- **Dekking 99,5%:** 68 van 13.005 teksten ontbreken, allemaal nieuwe teksten uit 262 (precies dezelfde 68 als in het Spaanse pakket). Die vallen terug op Engels.
- **Echt onvertaald:** 1 tekst in de kernbundels ("Pac&kage local"); de rest van wat gelijk is aan het Engels is code. Van 8.686 html-bestanden zijn er 8 Engels gebleven, 7.493 Frans, 1.185 te kort om te beoordelen.
- **Plaatshouders:** 8 echte fouten, verouderde vertalingen van teksten die in 262 veranderden (zo ziet de gebruiker bij `updates.from.to` letterlijk "{2}").
- **Sneltoetsen:** van 462 teksten met een sneltoets-& is er in het Frans geen enkele kwijt.
- **Steekproef 120 paren:** 113 goed bruikbaar, 7 matig, 0 fout. Matig: woordkeus niet overal gelijk ("scope" 52 keer naast "portée" 495 keer, "Tablette" naast "mettre en réserve"), een paar letterlijke vertalingen ("Réduire dans une boucle"), verbuiging bij plaatshouders. Franse typografie (spatie voor de dubbele punt) in 6.165 van de 6.661 gevallen.
- Kanttekening: geen moedertaalspreker gekeurd, en alleen de 12 kernbundels geteld, niet alle 1.577.

## Wat dit betekent
De klachten in de reviews ("missing texts", "machine translation") passen niet bij de huidige versie. Ze komen uit apr 2025 tot aug 2026 en horen bij oudere versies, of bij het terugkerende probleem dat nieuwe teksten pas later vertaald worden (GOK). Het slechte sterrencijfer (1,75 uit 4 stemmen) zegt weinig over het pakket van nu.

Een merkbaar beter Frans pakket is dus niet te maken op dekking of basiskwaliteit. Winnen kan alleen op snelheid (nieuwe teksten op de dag van de release), gelijke woordkeus en prijs. Dat is te weinig om klanten weg te halen bij een pakket dat 99,5% dekt en vloeiend leest.

## Besluit Jet
Taalpakketten: **nee** als tweede product. Het cijfer van Vera gaat voor mij van 4 naar 2 tot 3: de "zwakke nummer één" was het belangrijkste argument en dat blijkt niet te kloppen voor de huidige versie; betaalcijfers waren al onzichtbaar. Niet bij Hans voorgelegd (niets om te beslissen). Komt er een nieuw feit (bijvoorbeeld verkoopcijfers, of een groot pakket dat stopt), dan opnieuw kijken. Italiaans en Tsjechisch niet apart getoetst: zelfde maker en zelfde werkwijze, dus vermoedelijk zelfde kwaliteit (GOK).
