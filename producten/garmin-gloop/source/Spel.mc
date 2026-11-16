import Toybox.Lang;

// Vaste getallen van het spel.
module Regel {
    const KLAAR = 0;
    const VALT = 1;
    const SLOK = 2;
    const WEG = 3;
    const WACHT = 4;
    const EINDE = 5;

    const RONDE_MS = 30000;
    const VANG_BOVEN = 700.0;
    const VANG_ONDER = 900.0;
    const RAAK_BOVEN = 780.0;
    const RAAK_ONDER = 850.0;
    const SNEL_START = 0.50;
    const SNEL_MIN = 0.40;
    const SNEL_MAX = 1.30;
    const SLOK_MS = 300;
    const WEG_MS = 600;
    const DICHT_MS = 250;
    const OPNIEUW_MS = 800;
}

// De spelregels, los van het scherm, zodat ze te toetsen zijn.
// Een held valt van 0 (boven) naar 1000 (de vloer). Druk je terwijl hij bij de bek
// van Gloop is, dan slokt Gloop hem op en vliegt zijn hoed op de toren.
// Missen kost niets: de held loopt weg en de volgende valt iets langzamer.
class Spel {

    var toestand as Number = Regel.KLAAR;
    var y as Float = 0.0;
    var snelheid as Float = Regel.SNEL_START;
    var hoeden as Number = 0;
    var reeks as Number = 0;
    var beste as Number = 0;
    var nieuwBeste as Boolean = false;
    var raak as Boolean = false;
    var tijdOver as Number = Regel.RONDE_MS;
    var fase as Number = 0;
    var wachtDuur as Number = 300;
    var hapDicht as Number = 0;
    var held as Number = 0;
    var zaad as Number = 1;

    function initialize(beginZaad as Number) {
        zaad = beginZaad;
    }

    // Eigen toevalsgetal, zodat een toets altijd hetzelfde potje krijgt.
    function toeval(grens as Number) as Number {
        zaad = (zaad * 1103515245 + 12345) & 0x7FFFFFFF;
        return (zaad / 65536) % grens;
    }

    function begin() as Void {
        hoeden = 0;
        reeks = 0;
        nieuwBeste = false;
        raak = false;
        tijdOver = Regel.RONDE_MS;
        snelheid = Regel.SNEL_START;
        hapDicht = 0;
        nieuweHeld();
    }

    function nieuweHeld() as Void {
        toestand = Regel.VALT;
        y = 0.0;
        fase = 0;
        held = toeval(6);
    }

    function inVangzone() as Boolean {
        return y >= Regel.VANG_BOVEN && y <= Regel.VANG_ONDER;
    }

    function druk() as Void {
        if (toestand == Regel.KLAAR) {
            begin();
        } else if (toestand == Regel.EINDE) {
            if (fase >= Regel.OPNIEUW_MS) {
                begin();
            }
        } else if (toestand == Regel.VALT) {
            if (hapDicht > 0) {
                return;
            }
            if (inVangzone()) {
                hoeden += 1;
                raak = (y >= Regel.RAAK_BOVEN && y <= Regel.RAAK_ONDER);
                reeks = raak ? reeks + 1 : 0;
                snelheid = snelheid * 1.06;
                if (snelheid > Regel.SNEL_MAX) {
                    snelheid = Regel.SNEL_MAX;
                }
                toestand = Regel.SLOK;
                fase = 0;
            } else {
                // Te vroeg: Gloop hapt in de lucht en heeft even zijn bek dicht.
                hapDicht = Regel.DICHT_MS;
            }
        }
    }

    function tik(dt as Number) as Void {
        if (toestand == Regel.KLAAR || toestand == Regel.EINDE) {
            fase += dt;
            return;
        }
        tijdOver -= dt;
        if (tijdOver <= 0) {
            tijdOver = 0;
            toestand = Regel.EINDE;
            fase = 0;
            if (hoeden > beste) {
                beste = hoeden;
                nieuwBeste = true;
            }
            return;
        }
        if (hapDicht > 0) {
            hapDicht -= dt;
            if (hapDicht < 0) {
                hapDicht = 0;
            }
        }
        if (toestand == Regel.VALT) {
            y += snelheid * dt;
            if (y > Regel.VANG_ONDER) {
                toestand = Regel.WEG;
                fase = 0;
                reeks = 0;
                snelheid = snelheid * 0.85;
                if (snelheid < Regel.SNEL_MIN) {
                    snelheid = Regel.SNEL_MIN;
                }
            }
        } else if (toestand == Regel.SLOK) {
            fase += dt;
            if (fase >= Regel.SLOK_MS) {
                wacht();
            }
        } else if (toestand == Regel.WEG) {
            fase += dt;
            if (fase >= Regel.WEG_MS) {
                wacht();
            }
        } else if (toestand == Regel.WACHT) {
            fase += dt;
            if (fase >= wachtDuur) {
                nieuweHeld();
            }
        }
    }

    function wacht() as Void {
        toestand = Regel.WACHT;
        fase = 0;
        wachtDuur = 100 + toeval(350);
    }
}
