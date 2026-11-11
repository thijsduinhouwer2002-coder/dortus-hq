import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.WatchUi;

// Settings in Ebb-stijl (blad v7 scherm 9 en 9b, keuring bouw 1 punt 9, Daan D9): zwart, kop "settings", de gekozen
// regel als blauwe pil met de naam groot en de waarde eronder, één regel erboven en twee eronder, de zeestrook onderaan.
// Omhoog en omlaag (of vegen) kiest een regel, select (of tik) verandert hem. Geen "touch lock": dat is geen instelling,
// het aanraakscherm doet tijdens een sessie altijd niets.
class EbbInstellingenView extends WatchUi.View {
    var keuze as Number = 0;
    // Per regel [naam, soort, sleutel]: soort 0 waarde uit EbbInstellingen, 1 aan/uit, 2 actie.
    // Mila blad v12 punt 3: bij de laatste twee regels ben je op de bodem. De zee komt hoger (kamlijn 0,745 D), de
    // vaste zin staat wit in het water (geen knop) en je eigen dier zit eronder. Bij Safety info zakt de pil één plek.
    const GEEN_GELUID = "Ebb is silent. Buzz only.";
    const ZEE_BODEM = 0.745;
    var dier as Number = EbbTrouw.zwemmer();
    const REGELS = [
        ["Rounds", 0, 2], ["Breathing pace", 0, 1], ["Breaths", 0, 0], ["Recovery hold", 0, 3], ["Weekly goal", 0, 8],
        ["Buzz every 30 s", 1, :tik30], ["Buzz on last 3 breaths", 1, :laatste3], ["Vibration", 1, :trillen],
        ["My pattern: in", 0, 4], ["My pattern: hold", 0, 5], ["My pattern: out", 0, 6], ["My pattern: rest", 0, 7],
        ["Start my pattern", 2, :eigen], ["Safety info", 2, :veilig]
    ] as Array<Array>;
    var veiligGezet as Boolean = false;

    function initialize() {
        View.initialize();
    }

    function aantal() as Number {
        return REGELS.size();
    }

    function waarde(r as Number) as String or Null {
        var regel = REGELS[r];
        var soort = regel[1] as Number;
        if (soort == 0) {
            return EbbInstellingen.tekst(regel[2] as Number);
        }
        if (soort == 1) {
            return aan(regel[2] as Symbol) ? "on" : "off";
        }
        var id = regel[2] as Symbol;
        if (id == :eigen) {
            return EbbStart.eigenTekst();
        }
        if (id == :veilig) {
            return veiligGezet ? "next start" : "read again";
        }
        return null;
    }

    function aan(id as Symbol) as Boolean {
        if (id == :tik30) {
            return EbbInstellingen.tik30();
        }
        if (id == :laatste3) {
            return EbbInstellingen.laatste3();
        }
        return EbbInstellingen.trillen();
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var d = w < dc.getHeight() ? w : dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        var bodem = keuze >= aantal() - 2;
        var laag = keuze == aantal() - 1;
        if (bodem) {
            EbbZee.zeeBanden(dc, d, [ZEE_BODEM, 0.86, 0.93] as Array<Float>, [1, 2, 3] as Array<Number>, 0.008, 0.0);
        } else {
            EbbZee.strook(dc, d);
        }
        var midden = Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER;
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.21).toNumber(), EbbTeken.fS(), "settings", midden);
        // Keuring bouw 2 punt 6: regels gelijk verdeeld (0,325 boven, pil 0,40 tot 0,61, dan 0,685 en 0,765: telkens
        // 0,075 D lucht tot de pil en 0,08 D tussen de regels). De pil is 24 px breder dan de langste regel erin,
        // hoogstens 0,83 D; past de naam niet in de grote letter, dan een kleinere.
        // Keuring bouw 3 punt 6: pil 10 px hoger (0,022 D), regels buiten de pil in één lettermaat, gelijk verdeeld:
        // telkens dezelfde lucht (0,035 D) tussen pil en regel en tussen de regels.
        var bh = (d * 0.21).toNumber();
        var py = (d * (laag ? 0.564 : 0.483)).toNumber();
        var fx = dc.getFontHeight(EbbTeken.fX());
        var lucht = (d * 0.035).toNumber();
        var maxW = (d * 0.83).toNumber();
        var naam = REGELS[keuze][0] as String;
        var v = waarde(keuze);
        var fNaam = EbbTeken.fM();
        if (dc.getTextWidthInPixels(naam, fNaam) > maxW - 24) {
            fNaam = EbbTeken.fS();
        }
        if (dc.getTextWidthInPixels(naam, fNaam) > maxW - 24) {
            fNaam = EbbTeken.fX();
        }
        var langst = dc.getTextWidthInPixels(naam, fNaam);
        if (v != null) {
            var vw = dc.getTextWidthInPixels(v as String, EbbTeken.fS());
            langst = vw > langst ? vw : langst;
        }
        // Keuring bouw 7 punt 4 (k19 op 260): passen naam en waarde niet onder elkaar in de pil, dan wordt de pil
        // zo hoog als de twee regels samen plus 8 px, en staan de regels strak onder elkaar zonder te raken.
        var hN = dc.getFontHeight(fNaam);
        var hV = dc.getFontHeight(EbbTeken.fS());
        var krap = (v != null) && (hN + hV + 8 > bh);
        if (krap) {
            // Beeld run 43104540264 (FR255 scène 19): de hogere pil duwde de regel erboven in de kop "settings".
            // De bovenkant van de pil blijft nu waar hij was (de pil groeit naar beneden) en de lucht om de pil is
            // kleiner, zodat de onderste regel op zijn plek blijft.
            if (!laag) {
                py += (hN + hV + 8 - bh) / 2;
                lucht = lucht * 5 / 9;
                lucht = lucht < 4 ? 4 : lucht;
            }
            bh = hN + hV + 8;
        }
        if (laag) {
            // Twee regels boven de lage pil, op de vaste plekken van blad v12 (0,304 en 0,384 D).
            regelKort(dc, d, keuze - 2, 0.304);
            regelKort(dc, d, keuze - 1, 0.384);
        } else if (keuze > 0) {
            regelKort(dc, d, keuze - 1, (py - bh / 2 - lucht - fx / 2).toFloat() / d);
        }
        var bw = langst + 24;
        var minW = (d * 0.5).toNumber();
        bw = bw < minW ? minW : (bw > maxW ? maxW : bw);
        dc.setColor(EbbTeken.ZEE_KLEUR[1], EbbTeken.ZEE_KLEUR[1]);
        dc.fillRoundedRectangle(w / 2 - bw / 2, py - bh / 2, bw, bh, bh / 2);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        if (v == null) {
            dc.drawText(w / 2, py, fNaam, naam, midden);
        } else {
            dc.drawText(w / 2, krap ? py - (hN + hV) / 2 + hN / 2 : py - (d * 0.045).toNumber(), fNaam, naam, midden);
            dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, krap ? py + (hN + hV) / 2 - hV / 2 : py + (d * 0.055).toNumber(), EbbTeken.fS(), v as String, midden);
        }
        var y1 = py + bh / 2 + lucht + fx / 2;
        if (keuze + 1 < aantal()) {
            regelKort(dc, d, keuze + 1, y1.toFloat() / d);
        }
        if (keuze + 2 < aantal() && !bodem) {
            regelKort(dc, d, keuze + 2, (y1 + fx + lucht).toFloat() / d);
        }
        if (bodem) {
            dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, (d * 0.802).toNumber(), EbbTeken.fX(), GEEN_GELUID, midden);
            if (dier >= 0) {
                EbbDierVoorraad.teken(dc, dier, w / 2, (d * 0.890).toNumber(), EbbTeken.px(d, 12), EbbDierPlaatje.GEVONDEN);
            }
        }
    }

    // Regel buiten de pil: "Rounds  3" in lichtcyaan, kleiner als hij niet binnen de ronde rand past.
    function regelKort(dc as Graphics.Dc, d as Number, r as Number, y as Float) as Void {
        var v = waarde(r);
        var tekst = (REGELS[r][0] as String) + ((v != null && (REGELS[r][1] as Number) != 3) ? "  " + v : "");
        var f = EbbTeken.fX();
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), f, tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    function verschuif(stap as Number) as Void {
        keuze = (keuze + stap + aantal()) % aantal();
        WatchUi.requestUpdate();
    }

    // Select: waarde een stap verder, aan/uit wisselen, of de actie. Geeft true als er een nieuw scherm kwam.
    function kies() as Boolean {
        var regel = REGELS[keuze];
        var soort = regel[1] as Number;
        if (soort == 0) {
            EbbInstellingen.volgende(regel[2] as Number);
        } else if (soort == 1) {
            var id = regel[2] as Symbol;
            var nieuw = !aan(id);
            if (id == :tik30) {
                EbbInstellingen.zetTik30(nieuw);
            } else if (id == :laatste3) {
                EbbInstellingen.zetLaatste3(nieuw);
            } else {
                EbbInstellingen.zetTrillen(nieuw);
            }
        } else if ((regel[2] as Symbol) == :eigen) {
            // Keuring bouw 3 punt 3: ook My pattern eerst via "Sit or lie down".
            var sc = new StartCheckView();
            sc.zetEigen();
            // Keuring bouw 7 punt 3: wisselen in plaats van stapelen, zodat je na My pattern in het menu uitkomt.
            WatchUi.switchToView(sc, new StartCheckDelegate(sc), WatchUi.SLIDE_LEFT);
            return true;
        } else if ((regel[2] as Symbol) == :veilig) {
            EbbVeilig.opnieuwTonen();
            veiligGezet = true;
        }
        WatchUi.requestUpdate();
        return false;
    }
}

class EbbInstellingenDelegate extends WatchUi.BehaviorDelegate {
    private var _view as EbbInstellingenView;

    function initialize(view as EbbInstellingenView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function onNextPage() as Boolean {
        _view.verschuif(1);
        return true;
    }

    function onPreviousPage() as Boolean {
        _view.verschuif(-1);
        return true;
    }

    function onSelect() as Boolean {
        _view.kies();
        return true;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        _view.kies();
        return true;
    }

    function onBack() as Boolean {
        WatchUi.popView(WatchUi.SLIDE_RIGHT);
        return true;
    }
}
