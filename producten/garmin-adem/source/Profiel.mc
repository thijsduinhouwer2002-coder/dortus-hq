import Toybox.Application;
import Toybox.Lang;

// Rekenwerk voor 8 weeks, de zee tijdens het inhouden en de dieren, los van het tekenen zodat het te toetsen is.
module EbbProfiel {

    // 8 weeks (besluit 22:53, punt 6, blad v4.1 scherm 7): per week, oudste eerst, eindigend met de week tot en met
    // vandaag, [gemiddelde inhoudtijd in s over alle inhoudingen, aantal opgeslagen sessies, aantal inhoudingen].
    // sessieDagen is de lijst dagnummers met één regel per opgeslagen sessie (EbbTrouw.sessieDagen()).
    // Een lege week is [0, 0, 0].
    function weken(opslag as EbbOpslag, sessieDagen as Array<Number>, vandaag as Number) as Array<Array<Number> > {
        var uit = [] as Array<Array<Number> >;
        // Keuring bouw 3 punt 11: weken van maandag tot zondag (dag 0 was een donderdag), de laatste is deze week.
        var zondag = vandaag - (vandaag + 3) % 7 + 6;
        for (var w = 7; w >= 0; w -= 1) {
            var tot = zondag - w * 7;
            var van = tot - 6;
            tot = tot > vandaag ? vandaag : tot;
            var som = 0;
            var n = 0;
            for (var d = van; d <= tot; d += 1) {
                var g = opslag.dag(d);
                if (g != null) {
                    som += g[0] * g[1];
                    n += g[1];
                }
            }
            var sessies = 0;
            for (var i = 0; i < sessieDagen.size(); i += 1) {
                if (sessieDagen[i] >= van && sessieDagen[i] <= tot) {
                    sessies += 1;
                }
            }
            uit.add([(n > 0) ? (som + n / 2) / n : 0, sessies, n] as Array<Number>);
        }
        return uit;
    }

    // Blad v5 (Mila T2) met het besluit van de hoofdchat (keuring v5, 11 nov 00:55): de zee wordt elke 30 s inhouden
    // een stand donkerder tot 2:30 (stand 5) en blijft daarna gelijk. Niet lichter na 3:00: dan zou de kleur een
    // verborgen doel zijn. Het seintje na 3:00 is tekst, trilteken en buzz, niet de kleur.
    function zeeStand(sec as Number) as Number {
        var s = sec / 30;
        return s > 5 ? 5 : (s < 0 ? 0 : s);
    }

    // Banden per stand (ZEE_STAND in Mila's ebb_blad_v5.py): paren [bovenkant in honderdsten van D, watertint 0 tot 3].
    const ZEE = [
        [12, 0, 19, 1, 62, 2, 90, 3],
        [12, 0, 16, 1, 50, 2, 78, 3],
        [12, 1, 40, 2, 68, 3],
        [12, 1, 26, 2, 52, 3],
        [12, 2, 40, 3],
        [12, 2, 22, 3]
    ] as Array<Array<Number> >;

    // AMOLED: bovenop de banden het hele water 10 procent donkerder per stand (in procenten helderheid).
    function amoledHelderheid(stand as Number) as Number {
        return 100 - 10 * stand;
    }

}

// Eis 2: het veiligheidsscherm komt alleen tot het bevestigd is, en weer na "opnieuw tonen" in de instellingen.
module EbbVeilig {
    const SLEUTEL = "veilig";
    const DAGEN = 30;   // productkeuring: waarschuwing bij de eerste start en daarna elke 30 dagen

    // Bewaard is het dagnummer van de laatste bevestiging. Niets (of de oude waarde true) betekent: tonen.
    function moetTonenOp(vandaag as Number) as Boolean {
        var v = Application.Storage.getValue(SLEUTEL);
        if (!(v instanceof Number)) {
            return true;
        }
        return vandaag - (v as Number) >= DAGEN || vandaag < (v as Number);
    }

    function moetTonen() as Boolean {
        return moetTonenOp(EbbView.vandaag());
    }

    function bevestigOp(vandaag as Number) as Void {
        Application.Storage.setValue(SLEUTEL, vandaag);
    }

    function bevestig() as Void {
        bevestigOp(EbbView.vandaag());
    }

    function opnieuwTonen() as Void {
        Application.Storage.deleteValue(SLEUTEL);
    }
}

// Trouw (besluit 22:53): dieren verdien je met sessies en dagen op rij, niet met inhoudtijd.
// Hier alleen de tellers; welke dieren bij welke stand horen komt uit blad v4 van Mila.
// Een opgeslagen sessie telt (rondes en rustig ademen); weggooien telt niet.
