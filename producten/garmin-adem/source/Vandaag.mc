import Toybox.Application;
import Toybox.Lang;

// Blad v6 scherm 6 (today) en keuring 01:55 punt 2 en 5: de hele dag, niet alleen de laatste sessie.
// Per opgeslagen sessie van vandaag [klok in minuten na middernacht, inhoudtijden in s]. Hoogstens MAX sessies
// (de laatste), elk hoogstens 6 rondes (de instelling gaat tot 6). Een nieuwe dag begint leeg.
module EbbVandaag {
    const SLEUTEL = "vandaag";
    const MAX = 3;

    // Bewaart een sessie: [dag, klok1, [tijden1], klok2, [tijden2], ...].
    function bewaar(dag as Number, klok as Number, tijden as Array<Number>) as Void {
        var oud = lees(dag);
        oud.add([klok, tijden] as Array);
        while (oud.size() > MAX) {
            oud = oud.slice(1, null);
        }
        var uit = [dag] as Array<Application.Storage.ValueType>;
        for (var i = 0; i < oud.size(); i += 1) {
            uit.add(oud[i][0] as Number);
            uit.add(oud[i][1] as Array<Application.Storage.ValueType>);
        }
        Application.Storage.setValue(SLEUTEL, uit);
    }

    // De sessies van dag, oudste eerst, elk [klok, tijden]. Andere dag of kapotte opslag: leeg.
    function lees(dag as Number) as Array<Array> {
        var v = Application.Storage.getValue(SLEUTEL);
        var uit = [] as Array<Array>;
        if (!(v instanceof Array)) {
            return uit;
        }
        var a = v as Array;
        if (a.size() < 1 || !(a[0] instanceof Number) || (a[0] as Number) != dag) {
            return uit;
        }
        for (var i = 1; i + 1 < a.size(); i += 2) {
            if (a[i] instanceof Number && a[i + 1] instanceof Array) {
                uit.add([a[i], a[i + 1]] as Array);
            }
        }
        return uit;
    }

    function wis() as Void {
        Application.Storage.deleteValue(SLEUTEL);
    }

    // "7:40" uit minuten na middernacht.
    function klokTekst(min as Number) as String {
        return (min / 60).toString() + ":" + (min % 60).format("%02d");
    }

    // [aantal holds, gemiddelde in s] over alle sessies.
    function samen(sessies as Array<Array>) as Array<Number> {
        var n = 0;
        var som = 0;
        for (var i = 0; i < sessies.size(); i += 1) {
            var t = sessies[i][1] as Array<Number>;
            for (var j = 0; j < t.size(); j += 1) {
                som += t[j];
                n += 1;
            }
        }
        return [n, n > 0 ? (som + n / 2) / n : 0] as Array<Number>;
    }
}
