import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;

// De werelden in de echte ademsessie, stap 1 (plan in platformen/garmin/status.md, run 60): ademen en inhouden van
// Rounds tekenen de wereld van je dier (KrabV2View) met de echte tekst van dit moment. Per scherm (in, uit,
// inhouden) één stilstaand plaatje; bij een wissel bouwt het nieuwe zich in vijf beurten op.
// Veiligheid: de wereld bij inhouden is op elk moment hetzelfde plaatje, hij beloont langer inhouden niet.
// Staat nog UIT in de gewone app (aan = false): alleen de proefscènes "sessie-..." zetten hem aan, tot de beelden
// gekeurd zijn. Herstel, eindscherm, menu en Calm volgen in stap 2.
module EbbWereldSessie {
    var aan as Boolean = false;
    // Plaatjesbouw: 0 dag, 1 nacht; -1 is de klok van het horloge (nacht van 21 tot 6 uur, EbbLucht).
    var proefNacht as Number = -1;
    var _kv as KrabV2View or Null = null;
    var _sleutel as Number = -1;
    var _dier as Number = -2;
    var _wereld as Number = -1;

    // Nummer van de wereld van dit dier in de lijst van KrabV2Werelden, of -1 als het dier nog geen wereld heeft.
    // De lijst eindigt bij de eerste lege wereld: die geeft het dier van de krab terug en staat niet op plek 0.
    function wereldVan(dier as Number) as Number {
        if (dier != _dier) {
            _dier = dier;
            _wereld = -1;
            for (var w = 0; w < 40; w += 1) {
                var d = KrabV2Werelden.maak(w).dier();
                if (w > 0 && d == 4) {
                    break;
                }
                if (d == dier) {
                    _wereld = w;
                    break;
                }
            }
        }
        return _wereld;
    }

    function los() as Void {
        _kv = null;
        _sleutel = -1;
    }

    // Tekent ademen of inhouden in de wereld van het dier. Geeft false als dat niet kan (uit, geen dier, geen
    // wereld, andere fase): dan tekent het gewone sessiescherm.
    function teken(v as EbbView, dc as Graphics.Dc, nu as Number) as Boolean {
        var fase = v.sessie.fase;
        if (!aan || v.gezelschap < 0 || (fase != Ebb.FASE_ADEMEN && fase != Ebb.FASE_INHOUDEN)) {
            los();
            return false;
        }
        var w = wereldVan(v.gezelschap);
        if (w < 0) {
            return false;
        }
        var nacht = proefNacht >= 0 ? proefNacht == 1 : EbbLucht.deelNu() == 3;
        var ronde = "round " + (v.sessie.ronde + 1);
        var scherm = 3;
        var tekst = [] as Array<String>;
        if (fase == Ebb.FASE_ADEMEN) {
            var isIn = v.sessie.isIn(nu);
            scherm = isIn ? 0 : 1;
            var n = v.sessie.ademhaling(nu);
            var rest = v.sessie.ademhalingen - n;
            var over = rest <= 0 ? "last breath" : (rest == 1 ? "1 breath left" : rest + " breaths left");
            tekst = [isIn ? "breathe in" : "breathe out", n.toString(), ronde + " · " + over, over] as Array<String>;
        } else {
            var s = v.sessie.verstreken(nu) / 1000;
            var bpm = EbbBouw.PLAATJE ? 61 : EbbOpname.hartslag();
            // Na 3:00 zegt de kop "breathe" in plaats van "hold" (het gewone scherm zegt daar "time to breathe";
            // dat past bovenaan het ronde scherm niet in de grote letter). De stopregel eronder blijft staan.
            tekst = [s < 180 ? "hold" : "breathe", v.stopTekst(), (s / 60).toString() + ":" + (s % 60).format("%02d"),
                (bpm > 0 ? bpm + " bpm · " : "") + ronde] as Array<String>;
        }
        var sleutel = scherm + 10 * w + (nacht ? 1000 : 0);
        if (sleutel != _sleutel || _kv == null) {
            _kv = null; // eerst het oude plaatje los, dan pas het nieuwe (geheugen op de FR255)
            _kv = new KrabV2View(scherm, nacht, w);
            _sleutel = sleutel;
        }
        KrabV2Tekst.echt = tekst;
        (_kv as KrabV2View).onUpdate(dc);
        KrabV2Tekst.echt = null;
        return true;
    }
}
