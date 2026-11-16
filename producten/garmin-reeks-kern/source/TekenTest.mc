import Toybox.Lang;
import Toybox.Test;

(:test)
function testProfielDriePunten(logger as Test.Logger) as Boolean {
    var p = Teken.profiel([10, 50, 90] as Array<Number>, 0, 100, 100, 0, 3);
    return p.size() == 5 && p[1][1] == 90 && p[2][1] == 50 && p[3][1] == 10 && p[3][0] == 100;
}

(:test)
function testProfielTeWeinigWaarden(logger as Test.Logger) as Boolean {
    return Teken.profiel([40] as Array<Number>, 0, 100, 100, 0, 40).size() == 0
        && Teken.profiel([] as Array<Number>, 0, 100, 100, 0, 40).size() == 0;
}

(:test)
function testGolfAantalPunten(logger as Test.Logger) as Boolean {
    return Teken.golf(0, 100, 50, 60, 3, 24).size() == 26;
}
