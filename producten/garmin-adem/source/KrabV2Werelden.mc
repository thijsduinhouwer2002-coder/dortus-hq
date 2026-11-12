import Toybox.Graphics;
import Toybox.Lang;

// HET INPLUGPUNT VAN DE WERELDEN (WERELD-BOUWEN.md). Dit is de enige plek waar een wereldnummer naar een wereld
// wijst. Een wereld toevoegen is: je eigen bestand source/KrabV2<Naam>.mc (module met de zes functies plus onderaan
// het aanmeldblok "class KrabV2W<Naam> extends KrabV2Wereld") en EEN regel in de lijst in KrabV2Werelden.maak.
// Geen ander bestand hoeft te wijzigen: de scènes en de namen van de beelden volgen uit de lijst.

// Wat elke wereld kan leveren. Wat je niet overschrijft doet niets of geeft de gewone waarde.
class KrabV2Wereld {
    function initialize() {
    }

    // Nummer van de held in DierenData.mc.
    function dier() as Number {
        return 4;
    }

    // Nummer en naam van de nieuwe vriend op het eindscherm (naam uit DierenData.mc, in het Engels).
    function vriend() as Number {
        return 1;
    }

    function vriendNaam() as String {
        return "Shrimp";
    }

    // Per scherm 0 tot 5: midden van het dier x, y en zijn maat, in 1/260.
    function held(s as Number) as Array<Number> {
        return [130, 196, 30] as Array<Number>;
    }

    // Per scherm de hoek in graden (min is neus omhoog, het dier kijkt naar links).
    function kantel(s as Number) as Float {
        return 0.0;
    }

    // Onder water, laag 1 tot 3: ver, midden, dichtbij.
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
    }

    // Onder water en boven water, laag 4: wat direct onder of achter de held staat.
    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
    }

    // Boven water, laag 3: één drijvend ding onder het oppervlak.
    function boven(v as KrabV2View, dc as Graphics.Dc, top as Number) as Void {
    }

    // Elke beurt na de held: de grap en wat voor het dier langs loopt.
    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
    }

    // ---- Zelden nodig. Overschrijf alleen met een reden uit een keuring en zet die reden erbij. ----

    // Eén keer bij het begin van een scherm (de krab zet hier de plek van zijn zwemband).
    function start(v as KrabV2View, s as Number) as Void {
    }

    // Hoogte van de kam boven water per scherm 0 tot 2.
    function kam(s as Number) as Number {
        return KrabV2Tekst.KAM[s];
    }

    // Lichtbundel onder water (alleen AMOLED, inhouden en menu): x bovenaan en x op de bodem, zodat hij op de held valt.
    function bundel(scherm as Number) as Array<Number> {
        return [(scherm == 3) ? 126 : 120, (scherm == 3) ? 128 : 124] as Array<Number>;
    }

    // Belletjes in laag 3 onder water: x, y, straal om en om. Ze wijken vanzelf voor tekst.
    function bellen(scherm as Number) as Array<Number> {
        return [] as Array<Number>;
    }

    // De lichtere band 0055FF in de lucht op MIP bij dag.
    function luchtband() as Boolean {
        return true;
    }

    // Lucht in 1/260 tussen de cijfers en de bovenkant van de held boven water.
    function ruimte() as Number {
        return 7;
    }

    // Bovenkant van de held in 1/260 voor de veilige zone: gewoon het kader van het dier.
    function heldBoven(v as KrabV2View, scherm as Number) as Number {
        var g = EbbDierMaat.grenzen(v.dier);
        var h = v.held();
        return h[1] - (g[3] - g[2]) * h[2] / (2 * EbbDierData.SCHAAL);
    }

    // Waar: te weinig lucht tussen tekst en held is NEE (run rood). Onwaar: het kader is te grof, de meting meldt "krap".
    function streng() as Boolean {
        return false;
    }

    // Eigen meting van de grap tegen de cijfers boven water (de meeuw van de schildpad).
    function veiligExtra(v as KrabV2View, scherm as Number, tekstRechts as Number, tekstOnder as Number) as Void {
    }
}

module KrabV2Werelden {
    // Het thuiswater (startscherm) is geen wereld en heeft een eigen nummer buiten de lijst.
    const THUIS = -1;

    // DE LIJST. Eén regel per wereld, in volgorde, nummers zonder gaten. Het woord achter "naam:" wordt de naam van
    // de beelden (<naam>-in-dag-<horloge>.png) en de workflow telt deze regels om te weten hoeveel scènes er zijn.
    function maak(w as Number) as KrabV2Wereld {
        if (w == 0) { return new KrabV2WKrab(); } // naam: krab2
        if (w == 1) { return new KrabV2WSchild(); } // naam: schild2
        if (w == 2) { return new KrabV2WGarnaal(); } // naam: garnaal
        if (w == 3) { return new KrabV2WZeester(); } // naam: zeester
        return new KrabV2Wereld();
    }
}
