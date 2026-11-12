import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;

// De werelden in de echte ademsessie, stap 1 (plan in platformen/garmin/status.md, run 60): ademen en inhouden van
// Rounds tekenen de wereld van je dier (KrabV2View) met de echte tekst van dit moment. Per scherm (in, uit,
// inhouden) één stilstaand plaatje; bij een wissel bouwt het nieuwe zich in vijf beurten op.
// Veiligheid: de wereld bij inhouden is op elk moment hetzelfde plaatje, hij beloont langer inhouden niet.
// Staat sinds run 63 AAN in de gewone app (besluit Thijs 12 nov 11:50: de werelden in de echte ademsessie). Een dier
// zonder eigen wereld krijgt de basiswereld (KrabV2Basis.mc). Herstel, eindscherm en menu tekenen hun eigen scherm; Calm sinds run 71 ook de wereld (tekenCalm).
module EbbWereldSessie {
    var aan as Boolean = true;
    // Plaatjesbouw: 0 dag, 1 nacht; -1 is de klok van het horloge (nacht van 21 tot 6 uur, EbbLucht).
    var proefNacht as Number = -1;
    // Plaatjesbouw, scène sessie-terugval-*: dwingt de terugval zonder plaatje af (KrabV2View.onUpdate).
    var proefDirect as Boolean = false;
    var _kv as KrabV2View or Null = null;
    var _sleutel as Number = -1;

    // Nummer van de wereld van dit dier: krab 0, schildpad 1, elk ander dier zijn basiswereld (KrabV2Basis.mc,
    // besluit Thijs 12 nov 11:50); -1 als het nummer geen dier is.
    function wereldVan(dier as Number) as Number {
        if (dier == 4) {
            return 0;
        }
        if (dier == 3) {
            return 1;
        }
        return (dier >= 0 && dier < 25) ? KrabV2Werelden.BASIS + dier : -1;
    }

    // Tekent de wereld dit moment? Ja bij ademen en inhouden, voor elk dier en ook zonder dier (keuring code en
    // veiligheid 12 nov, punt 3: het oude scherm met de zee die donkerder wordt mag in geen enkel pad meer komen).
    // Eigen functie zodat de toets alle dieren en de lege opslag kan nalopen.
    function kan(gezelschap as Number, fase as Number) as Boolean {
        return aan && (fase == Ebb.FASE_ADEMEN || fase == Ebb.FASE_INHOUDEN) && wereldVan(gezelschap < 0 ? 13 : gezelschap) >= 0;
    }

    function los() as Void {
        _kv = null;
        _sleutel = -1;
    }

    // Tekent ademen of inhouden in de wereld van het dier. Geeft false als dat niet kan (uit, geen
    // wereld, andere fase): dan tekent het gewone sessiescherm.
    function teken(v as EbbView, dc as Graphics.Dc, nu as Number) as Boolean {
        if (aan) {
            v.sessie.bijwerken(nu);
        }
        var fase = v.sessie.fase;
        if (!kan(v.gezelschap, fase as Number)) {
            los();
            return false;
        }
        // Run 64: wie nog geen dier heeft (de allereerste sessie) kreeg het oude scherm, met een zee die per 30 s
        // donkerder werd en "time to breathe". Nu dezelfde gedeelde zee als de andere dieren (blauwe lucht, zand,
        // de basiswereld van dier 13), alleen zonder held. Zo ziet de eerste sessie eruit zoals de winkel belooft.
        var zonder = v.gezelschap < 0;
        var w = wereldVan(zonder ? 13 : v.gezelschap);
        if (w < 0) {
            return false;
        }
        // In de plaatjesbouw altijd dag tenzij de scène nacht vraagt: anders hangt het beeld af van het uur van de run.
        var nacht = proefNacht >= 0 ? proefNacht == 1 : (!EbbBouw.PLAATJE && EbbLucht.deelNu() == 3);
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
        return toon(dc, scherm, w, nacht, zonder, tekst);
    }

    // Calm (hoofdchat 12 nov 20:15 punt 1): geen zwart scherm meer. Dezelfde zee boven water als het ademen, met je
    // dier (scherm 2 van de wereld, dat er al was). tekst: fasewoord, seconden, naam van het patroon (lang en kort).
    function tekenCalm(dc as Graphics.Dc, gezelschap as Number, tekst as Array<String>) as Boolean {
        var zonder = gezelschap < 0;
        var w = wereldVan(zonder ? 13 : gezelschap);
        if (!aan || w < 0) {
            return false;
        }
        var nacht = proefNacht >= 0 ? proefNacht == 1 : (!EbbBouw.PLAATJE && EbbLucht.deelNu() == 3);
        return toon(dc, 2, w, nacht, zonder, tekst);
    }

    // Het plaatje van dit scherm (nieuw bij een wissel, eerst het oude los) met de echte tekst van dit moment.
    function toon(dc as Graphics.Dc, scherm as Number, w as Number, nacht as Boolean, zonder as Boolean, tekst as Array<String>) as Boolean {
        var sleutel = scherm + 10 * w + (nacht ? 100000 : 0) + (zonder ? 200000 : 0);
        if (sleutel != _sleutel || _kv == null) {
            _kv = null; // eerst het oude plaatje los, dan pas het nieuwe (geheugen op de FR255)
            var kv = new KrabV2View(scherm, nacht, w);
            kv.zonderHeld = zonder;
            _kv = kv;
            _sleutel = sleutel;
        }
        KrabV2Tekst.echt = tekst;
        (_kv as KrabV2View).onUpdate(dc);
        KrabV2Tekst.echt = null;
        return true;
    }
}
