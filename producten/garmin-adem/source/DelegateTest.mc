import Toybox.Lang;
import Toybox.Test;

// Eis 4: de stoptijd van het inhouden komt uit de knophandler, met nagebootste klok.
(:test)
function testInhoudenStopOpKnoptijd(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    var d = new EbbDelegate(view);
    view.sessie.bijwerken(96050);
    var inhoudStart = view.sessie.segmentStart;
    var knop = inhoudStart + 83417;
    var gestopt = d.stopOp(knop);
    var tijd = view.sessie.inhoudtijden[0];
    var afwijking = (tijd - 83417).abs();
    logger.debug("inhoudtijd " + tijd + " ms, afwijking " + afwijking + " ms");
    return gestopt && afwijking <= 100 && view.sessie.fase == Ebb.FASE_HERSTEL;
}

(:test)
function testTerugBuitenInhoudenIsPauze(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    var d = new EbbDelegate(view);
    var tijdensAdemen = d.terugActie();
    view.sessie.bijwerken(96000);
    var tijdensInhouden = d.terugActie();
    d.stopOp(120000);
    var tijdensHerstel = d.terugActie();
    return tijdensAdemen == :pauze && tijdensInhouden == :stop && tijdensHerstel == :pauze
        && !d.stopOp(121000);
}

// Eis 10 (deel in de unittest): zonder lopende opname geeft stoppen gewoon de inhoudtijd door, opslaan zonder opname geeft false.
(:test)
function testOpnameZonderSessieVeilig(logger as Test.Logger) as Boolean {
    var o = new EbbOpname();
    o.inhouden(42, 30);
    o.rondeKlaar();
    var ok = o.opslaan();
    o.weggooien();
    return !ok && !o.loopt() && o.laps == 0;
}

// Productkeuring 10 nov: aanraakscherm uit tijdens een sessie, na de sessie weer aan (wisselen vandaag en 8 weken).
(:test)
function testAanraakUitTijdensSessie(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 1, 15000, 0);
    var d = new EbbDelegate(view);
    var ademen = !d.aanraakAan();
    view.sessie.bijwerken(96000);
    var inhouden = !d.aanraakAan();
    d.stopOp(120000);
    view.sessie.bijwerken(140000);
    var klaar = d.aanraakAan();
    // Tikken tijdens het inhouden stopt niet meer: alleen de knop.
    return ademen && inhouden && klaar && view.sessie.fase == Ebb.FASE_KLAAR;
}

// Blad v5.4: Connect toont "Hold times 1:20 · 1:45 · 3:04" in plaats van "Longest hold"; de tekst past altijd in het veld.
(:test)
function testTijdenTekst(logger as Test.Logger) as Boolean {
    var t = EbbOpname.tijdenTekst("", 80);
    t = EbbOpname.tijdenTekst(t, 105);
    t = EbbOpname.tijdenTekst(t, 184);
    var lang = "";
    for (var i = 0; i < 20; i += 1) {
        lang = EbbOpname.tijdenTekst(lang, 125);
    }
    logger.debug("tijden " + t + " lang " + lang);
    return t.equals("1:20 · 1:45 · 3:04") && lang.toUtf8Array().size() <= 47 && lang.length() > 0;
}

// Keuring bouw 1 punt 1: na de sessie geeft terug het menu (geen pauzemenu) en opslaan telt maar één keer.
(:test)
function testNaSessieTerugNaarMenuEnNietDubbel(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 1, 15000, 0);
    var d = new EbbDelegate(view);
    view.sessie.bijwerken(96000);
    d.stopOp(120000);
    view.sessie.bijwerken(140000);
    var klaar = view.sessie.fase == Ebb.FASE_KLAAR;
    var actie = d.terugActie();
    var eerste = view.opgeslagen;
    view.opslaan();
    var tweedeKeer = view.opslaan();
    logger.debug("klaar " + klaar + " actie " + actie + " tweede " + tweedeKeer);
    return klaar && actie == :menu && !eerste && view.opgeslagen && !tweedeKeer;
}

// Keuring bouw 7 punt 7: een tik in het pauzemenu kiest de regel waarop je tikt, daarbuiten niets; omlaag en omhoog
// lopen rond over Resume, Save, Discard.
(:test)
function testPauzeTikEnSchuif(logger as Test.Logger) as Boolean {
    var goed = true;
    var maten = [260, 390, 454] as Array<Number>;
    for (var m = 0; m < maten.size(); m += 1) {
        var d = maten[m];
        for (var i = 0; i < 3; i += 1) {
            goed = goed && PauzeDelegate.regelBij(d, EbbTeken.px(d, PauzeView.Y[i])) == i;
        }
        goed = goed && PauzeDelegate.regelBij(d, EbbTeken.px(d, 40)) == -1 && PauzeDelegate.regelBij(d, EbbTeken.px(d, 240)) == -1;
    }
    var pv = new PauzeView("round 1 · 0:10", -1);
    var view = new EbbView();
    var pd = new PauzeDelegate(pv, view.method(:hervatNu), view.method(:opslaanEnTonen), view.method(:weggooien));
    pd.schuif(1);
    pd.schuif(1);
    var discard = pv.keuze == 2;
    pd.schuif(1);
    logger.debug("tik goed " + goed + " discard " + discard + " rond " + pv.keuze);
    return goed && discard && pv.keuze == 0;
}

// Telt wat het pauzemenu aanroept (voor de toets hieronder).
class PauzeTeller {
    var hervat as Number = 0;
    var bewaar as Number = 0;
    var weg as Number = 0;

    function initialize() {
    }

    function opHervat() as Void {
        hervat += 1;
    }

    function opBewaar() as Void {
        bewaar += 1;
    }

    function opWeg() as Void {
        weg += 1;
    }
}

// Codekeuring bouw 9 punt 9: Discard gooit echt weg. `kies` haalt eerst het pauzemenu van het scherm (popView) en dat
// kan niet in een toets, daarom roept de toets `doe` aan, de functie die `kies` zelf gebruikt. Discard (2) roept
// alleen weggooien aan, nooit opslaan, en vraagt om het startmenu; Save (1) en Resume (0) gooien niets weg.
// Daarna met een echte EbbView zonder lopende opname: weggooien mag niet crashen.
(:test)
function testPauzeDiscardGooitWeg(logger as Test.Logger) as Boolean {
    var t = new PauzeTeller();
    var pv = new PauzeView("round 1 · 0:10", -1);
    var pd = new PauzeDelegate(pv, t.method(:opHervat), t.method(:opBewaar), t.method(:opWeg));
    var naarMenu = pd.doe(2);
    var naDiscard = t.weg == 1 && t.bewaar == 0 && t.hervat == 0;
    var m1 = pd.doe(1);
    var m0 = pd.doe(0);
    logger.debug("discard weg " + t.weg + " bewaar " + t.bewaar + " hervat " + t.hervat + " menu " + naarMenu + " " + m1 + " " + m0);
    var view = new EbbView();
    var echt = new PauzeDelegate(pv, view.method(:hervatNu), view.method(:opslaanEnTonen), view.method(:weggooien));
    var m2 = echt.doe(2);
    return naarMenu && naDiscard && !m1 && !m0 && t.weg == 1 && t.bewaar == 1 && t.hervat == 1 && m2 && !view.opgeslagen;
}

// Productkeuring 12 nov punt 1: op een aanraakscherm gooit één tik op Discard niets weg. De eerste tik kiest alleen
// de regel, de tweede voert uit; voor Save hetzelfde. Een tik op een andere regel begint opnieuw. Resume mag in één tik.
(:test)
function testPauzeTikDiscardTweeKeer(logger as Test.Logger) as Boolean {
    var t = new PauzeTeller();
    var pv = new PauzeView("round 1 · 0:10", -1);
    var pd = new PauzeDelegate(pv, t.method(:opHervat), t.method(:opBewaar), t.method(:opWeg));
    var eerste = pd.tik(2);
    var gekozen = pv.keuze == 2 && t.weg == 0;
    var wissel = pd.tik(1);
    var naWissel = pv.keuze == 1 && t.bewaar == 0;
    var terug = pd.tik(2);
    var tweede = pd.tik(2);
    var save1 = pd.tik(1);
    var save2 = pd.tik(1);
    var resume = pd.tik(0);
    logger.debug("TIK discard " + eerste + " " + gekozen + " wissel " + wissel + " " + naWissel + " terug " + terug + " tweede " + tweede + " save " + save1 + " " + save2 + " resume " + resume + " weg " + t.weg);
    return !eerste && gekozen && !wissel && naWissel && !terug && tweede && !save1 && save2 && resume && t.weg == 0 && t.bewaar == 0;
}

// Keuring code en veiligheid 12 nov, punt 1: het inhouden stopt vanzelf op 5:00 en gaat door naar herstel.
(:test)
function testInhoudenStoptVanzelfOpVijfMinuten(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    view.sessie.bijwerken(96050);
    var start = view.sessie.segmentStart;
    var teVroeg = view.bewaak(start + 299999);
    var nogInhouden = view.sessie.fase == Ebb.FASE_INHOUDEN;
    // de timer komt soms later: 137 ms na de grens moet de tijd toch precies 5:00 zijn
    var gestopt = view.bewaak(start + 300137);
    var tijd = view.sessie.inhoudtijden.size() == 1 ? view.sessie.inhoudtijden[0] : -1;
    var nogEens = view.bewaak(start + 300500);
    logger.debug("te vroeg " + teVroeg + ", gestopt " + gestopt + ", tijd " + tijd + " ms, fase " + view.sessie.fase + ", nog eens " + nogEens);
    return !teVroeg && nogInhouden && gestopt && tijd == 300000 && view.sessie.fase == Ebb.FASE_HERSTEL
        && view.vanzelfGestopt && !nogEens && view.sessie.inhoudtijden.size() == 1;
}

// Herkeuring 12 nov, veiligheid 1 (besluit hoofdchat 17:40): na een inhouding die vanzelf stopt op 5:00 begint er
// GEEN nieuwe ronde. Na het herstel is de sessie klaar, ook al waren er drie rondes gekozen. Een inhouding die je zelf
// stopt gaat wel gewoon door naar de volgende ronde.
(:test)
function testNaVanzelfStoppenGeenNieuweRonde(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    view.sessie.bijwerken(96050);
    var start = view.sessie.segmentStart;
    view.bewaak(start + 300050);
    view.sessie.bijwerken(start + 300000 + 14999);
    var inHerstel = view.sessie.fase == Ebb.FASE_HERSTEL;
    view.sessie.bijwerken(start + 300000 + 15000);
    var klaar = view.sessie.fase == Ebb.FASE_KLAAR;
    view.sessie.bijwerken(start + 300000 + 900000);
    var blijftKlaar = view.sessie.fase == Ebb.FASE_KLAAR && view.sessie.inhoudtijden.size() == 1;
    // zelf gestopt: wel door naar ronde 2
    var zelf = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    zelf.bijwerken(96050);
    zelf.stopInhouden(96000 + 80000);
    zelf.bijwerken(96000 + 80000 + 15000);
    var door = zelf.fase == Ebb.FASE_ADEMEN && zelf.ronde == 1 && !zelf.vanzelf;
    logger.debug("VANZELF herstel " + inHerstel + " klaar " + klaar + " blijft " + blijftKlaar + " zelf door " + door);
    return inHerstel && klaar && blijftKlaar && door;
}

// Herkeuring 12 nov, veiligheid 2: een vanzelf gestopte inhouding telt niet mee in Today, 8 weeks en het gemiddelde.
// Ronde 1 zelf gestopt op 1:20, ronde 2 vanzelf op 5:00: er telt precies één tijd mee, 80 s.
(:test)
function testVanzelfGestoptTeltNietMee(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    view.sessie.bijwerken(96050);
    view.stopInhouden(96000 + 80000);
    var zonder = view.sessie.telbaar().size();
    view.sessie.bijwerken(96000 + 80000 + 15000 + 96050);
    var start = view.sessie.segmentStart;
    var gestopt = view.bewaak(start + 300010);
    var tel = view.sessie.telbaar();
    var alle = view.sessie.inhoudtijden;
    logger.debug("TELBAAR voor " + zonder + " gestopt " + gestopt + " alle " + alle + " telt " + tel);
    return zonder == 1 && gestopt && alle.size() == 2 && alle[1] == 300000 && tel.size() == 1 && tel[0] == 80000;
}

// Herkeuring 12 nov, veiligheid 4: een melding over het pauzemenu zet de 30 minuten niet terug op nul. Na 10 minuten
// in het menu loopt de timer nog 20 minuten, en nooit korter dan 50 ms.
(:test)
function testPauzeRestNaMelding(logger as Test.Logger) as Boolean {
    var vers = PauzeView.rest(1800000, 5000, 5000);
    var naTien = PauzeView.rest(1800000, 5000, 5000 + 600000);
    var voorbij = PauzeView.rest(1800000, 5000, 5000 + 1900000);
    logger.debug("PAUZEREST " + vers + " " + naTien + " " + voorbij);
    return vers == 1800000 && naTien == 1200000 && voorbij == 50;
}
