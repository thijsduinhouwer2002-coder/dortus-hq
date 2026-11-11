import Toybox.Application;
import Toybox.Lang;

// Eis 9: 56 dagen als één ByteArray van 56 x 11 = 616 B. Per dag: dagnummer 4 B, 2 B vrij (was "beste", weg sinds
// keuring v5 G1: Ebb houdt geen record bij), som 4 B (s), aantal 1 B. De maat bleef gelijk, zodat oude opslag blijft werken.
// Plek in de rij is dagnummer % 56, dus een dag van 56 dagen geleden wordt vanzelf overschreven.
class EbbOpslag {
    static const DAGEN = 56;
    static const MAAT = 11;
    static const SLEUTEL = "dagen";
    var bytes as ByteArray;

    function initialize() {
        var oud = Application.Storage.getValue(SLEUTEL);
        if (oud instanceof ByteArray && (oud as ByteArray).size() == DAGEN * MAAT) {
            bytes = oud as ByteArray;
        } else {
            bytes = new [DAGEN * MAAT]b;
        }
    }

    private function lees(o as Number, f as Lang.NumberFormat) as Number {
        return bytes.decodeNumber(f, {:offset => o, :endianness => Lang.ENDIAN_BIG}) as Number;
    }

    private function schrijf(v as Number, o as Number, f as Lang.NumberFormat) as Void {
        bytes.encodeNumber(v, f, {:offset => o, :endianness => Lang.ENDIAN_BIG});
    }

    // Leg een inhoudtijd (s) vast op dagnummer dag (dagen sinds 1970, lokale datum).
    function voegToe(dag as Number, inhoudS as Number) as Void {
        var o = (dag % DAGEN) * MAAT;
        if (lees(o, Lang.NUMBER_FORMAT_UINT32) != dag) {
            schrijf(dag, o, Lang.NUMBER_FORMAT_UINT32);
            schrijf(0, o + 4, Lang.NUMBER_FORMAT_UINT16);
            schrijf(0, o + 6, Lang.NUMBER_FORMAT_UINT32);
            bytes[o + 10] = 0;
        }
        var s = (inhoudS > 65535) ? 65535 : inhoudS;
        schrijf(lees(o + 6, Lang.NUMBER_FORMAT_UINT32) + s, o + 6, Lang.NUMBER_FORMAT_UINT32);
        if (bytes[o + 10] < 255) {
            bytes[o + 10] = bytes[o + 10] + 1;
        }
    }

    // [gemiddelde, aantal] voor dag, of null als er die dag geen sessie was (een gat in de getijdenlijn).
    function dag(dag as Number) as Array<Number> or Null {
        var o = (dag % DAGEN) * MAAT;
        var n = bytes[o + 10];
        if (dag <= 0 || lees(o, Lang.NUMBER_FORMAT_UINT32) != dag || n == 0) {
            return null;
        }
        return [lees(o + 6, Lang.NUMBER_FORMAT_UINT32) / n, n] as Array<Number>;
    }

    function bewaar() as Void {
        Application.Storage.setValue(SLEUTEL, bytes);
    }

    static function wis() as Void {
        Application.Storage.deleteValue(SLEUTEL);
    }
}
