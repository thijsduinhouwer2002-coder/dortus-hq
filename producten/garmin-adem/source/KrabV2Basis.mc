import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// DE BASISWERELD (besluit Thijs 12 nov 11:50): één rustige zee voor elk dier zonder eigen wereld. Per dier verschilt
// alleen wat geen tekenwerk kost: de lucht en het water van zijn familie (Mila werelden v5, bron/werelden_v5_lucht.py)
// en één van vier bodems (zand, kiezels, rotsen, zeegras aan de randen). Geen grapvoorwerp, weinig versiering.
// De held staat midden onder de cijfers; zijn maat volgt uit zijn eigen kader (EbbDierMaat.grenzen). Maten in 1/260.
module KrabV2Basis {
    // Familie per dier (nummers uit TrouwDieren.mc): 0 krab, 1 strand, 2 vliegers, 3 huisjes, 4 koud, 5 licht.
    const FAM = [3, 1, 5, 0, 0, 5, 1, 0, 3, 3, 3, 2, 1, 2, 2, 1, 2, 5, 5, 4, 4, 4, 1, 4, 3] as Array<Number>;
    // Bodem per dier: 0 zand, 1 kiezels, 2 rotsen, 3 zeegras.
    const BODEM = [0, 1, 0, 3, 2, 3, 2, 2, 1, 2, 0, 0, 1, 0, 1, 3, 0, 2, 3, 1, 2, 2, 3, 0, 3] as Array<Number>;
    // Lucht overdag per familie: MIP boven, MIP band, AMOLED drie stappen, knik in procenten van de horizon.
    const LUCHT = [
        0x0055AA, 0x00AAFF, 0x001E5F, 0x004BA5, 0x00A5FA, 55,
        0x0055FF, 0x55AAFF, 0x002878, 0x0050D2, 0x5AB4FF, 66,
        0x0055AA, 0x55AAFF, 0x00235A, 0x0055AA, 0x6EB9FF, 55,
        0x5500AA, 0xFF5555, 0x28005A, 0x6414A0, 0xFF6E5A, 55,
        0x0055AA, 0xAAFFFF, 0x002864, 0x0055A0, 0xBEF5FF, 74,
        0x0000AA, 0xFFFFAA, 0x0A0050, 0x2814AA, 0xFFF0A0, 55] as Array<Number>;
    // Water onder water op AMOLED overdag per familie; nooit lichter dan 00698C van de krab (wit moet 4,5 halen).
    const WATER = [0x00698C, 0x006E82, 0x0064A0, 0x46508C, 0x14647D, 0x3C4696] as Array<Number>;

    function fam(dier as Number) as Number {
        return (dier >= 0 && dier < FAM.size()) ? FAM[dier] : 0;
    }

    // Kader van het dier in 1/260 bij maat 1: breedte en hoogte.
    function kader(dier as Number) as Array<Float> {
        var g = EbbDierMaat.grenzen(dier);
        var s = EbbDierData.SCHAAL * 1.0;
        return [(g[1] - g[0]) / s, (g[3] - g[2]) / s] as Array<Float>;
    }

    // Grootste maat waarbij het dier binnen breed x hoog (1/260) past, hoogstens max.
    function maat(dier as Number, breed as Number, hoog as Number, max as Number) as Number {
        var k = kader(dier);
        var mb = breed / k[0];
        var mh = hoog / k[1];
        var m = (mb < mh ? mb : mh).toNumber();
        return m > max ? max : (m < 8 ? 8 : m);
    }

    // Boven water (in, uit, Calm): midden onder de cijfers, 0,65 van zijn hoogte boven de kam (bovenkant nooit
    // hoger dan 118). Onder water: inhouden en menu midden onderin, eindscherm links naast het belletje.
    function held(dier as Number, s as Number) as Array<Number> {
        var k = kader(dier);
        if (s <= 2) {
            var m = maat(dier, 76, 36, 46);
            var h = k[1] * m;
            var top = kam(dier, s) - 0.65 * h;
            return [130, (top + h / 2).toNumber(), m] as Array<Number>;
        }
        if (s == 5) {
            var m5 = maat(dier, 60, 40, 36);
            return [76, 134, m5] as Array<Number>;
        }
        var m3 = maat(dier, 90, 42, 50);
        return [130, s == 3 ? 192 : 196, s == 3 ? m3 : m3 * 9 / 10] as Array<Number>;
    }

    // De kam ligt op 0,65 van de hoogte van het dier: het drijft in het water, niet erboven.
    function kam(dier as Number, s as Number) as Number {
        if (s == 1) {
            return KrabV2Tekst.KAM[1];
        }
        var h = kader(dier)[1] * maat(dier, 76, 36, 46);
        var y = (118 + 0.65 * h).toNumber();
        return y < 134 ? 134 : y;
    }

    // Onderkant (1/260) van de laagste tekstregel die boven de kam begint: daar mag de lichte lucht pas beginnen.
    function tekstOnder(v as KrabV2View, top as Number) as Number {
        var o = 0;
        var vak = KrabV2Tekst._vak;
        for (var i = 0; i + 3 < vak.size(); i += 4) {
            if (vak[i + 1] < v.q(top) && vak[i + 3] > o) {
                o = vak[i + 3];
            }
        }
        return o * 260 / v.q(260);
    }

    // Onder water, laag 1 tot 3: verre ruggen en zand voor elk dier; daarna de bodem van dit dier.
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number, dier as Number) as Void {
        var sp = (scherm == 4);
        var zak = sp ? 18 : (scherm == 5 ? 10 : 0);
        var bodem = (dier >= 0 && dier < BODEM.size()) ? BODEM[dier] : 0;
        if (stap == 1) {
            var zeeTop = nacht ? 0x000069 : WATER[fam(dier)];
            var verder = am ? EbbTeken.meng(nacht ? 0x00003C : 0x001E46, zeeTop, 0.5) : (nacht ? 0x0000AA : 0x0055AA);
            v.rondje(dc, 60, 196 + zak, 90, 18, verder, -1, -1);
            v.rondje(dc, 210, 192 + zak, 80, 22, verder, -1, -1);
            var dof = nacht && !am;
            v.rondje(dc, 130, 273 + zak / 2.0, 190, 67 - zak / 2.0, dof ? 0xFFFFAA : 0xAAAA55, -1, -1);
            v.rondje(dc, 130, 275 + zak / 2.0, 180, 65 - zak / 2.0, am ? 0xEBE196 : (dof ? 0xAAAA55 : 0xFFFFAA), -1, -1);
        } else if (stap == 2 && bodem == 2) {
            // twee rotsen tegen de randen, niet achter tekst
            if (!KrabV2Tekst.raakt(v, 30, 214 + zak, 30)) {
                v.rondje(dc, 30, 214 + zak, 32, 24, 0x5555AA, 0xAAAAFF, 0xAAAAFF);
            }
            if (!KrabV2Tekst.raakt(v, 232, 220 + zak, 26)) {
                v.rondje(dc, 232, 220 + zak, 28, 20, 0x5555AA, 0xAAAAFF, 0xAAAAFF);
            }
        } else if (stap == 2 && bodem == 3) {
            // zeegras aan de randen: twee sprieten links, twee rechts; een spriet die tekst raakt staat er niet
            var s = [18, 70, 8, 9, 0, 36, 50, 7, -7, 1, 226, 54, 7, 8, 1, 244, 74, 8, -9, 0] as Array<Number>;
            for (var i = 0; i < 4; i += 1) {
                var x = s[5 * i];
                var y0 = 224 + zak;
                var vrij = true;
                for (var hh = 0; hh <= s[5 * i + 1]; hh += 8) {
                    if (KrabV2Tekst.raakt(v, x + s[5 * i + 3] * hh / s[5 * i + 1], y0 - hh, 5)) {
                        vrij = false;
                    }
                }
                if (vrij) {
                    KrabV2Schild.spriet(v, dc, x, y0, s[5 * i + 1], s[5 * i + 3], s[5 * i + 2], s[5 * i + 4] == 1 ? KrabV2Schild.GRAS : KrabV2Schild.GRAS_D, false);
                }
            }
        } else if (stap == 3 && bodem == 1) {
            // kiezels op het zand, hoog genoeg om binnen de ronde rand te blijven
            var p = [70, 238, 6, 4, 0, 92, 246, 5, 3, 1, 118, 242, 4, 3, 2, 150, 247, 6, 4, 1, 172, 240, 5, 3, 0, 194, 236, 4, 3, 2, 56, 232, 4, 3, 1, 206, 230, 5, 3, 0] as Array<Number>;
            var kl = [0xAAAAAA, 0xFFAAAA, 0xAAAAFF] as Array<Number>;
            for (var i = 0; i < 8; i += 1) {
                v.rondje(dc, p[5 * i], p[5 * i + 1] + zak / 2, p[5 * i + 2], p[5 * i + 3], kl[p[5 * i + 4]], 0xFFFFFF, -1);
            }
        }
    }

    // Laag 4 (inhouden en menu): schaduw onder het dier op het zand.
    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>, dier as Number) as Void {
        if (scherm != 3 && scherm != 4) {
            return;
        }
        var k = kader(dier);
        var b = k[0] * h[2] * 0.42;
        if (am) {
            v.gloed(dc, h[0] + 4, 236 + (scherm == 4 ? 12 : 0), b, 4.5, 0x5A5028, 53, 0xEBE196);
        } else {
            v.rondje(dc, h[0] + 4, 236 + (scherm == 4 ? 12 : 0), b, 4, 0xAAAA55, -1, -1);
        }
    }

    // Na de held, boven water: het golfje voor zijn buik, zodat hij in het water drijft.
    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, dier as Number) as Void {
        if (scherm > 2) {
            return;
        }
        var k = kader(dier);
        var b = k[0] * h[2] * 0.62;
        var y0 = v.kam() + 2;
        for (var ronde = 0; ronde < 2; ronde += 1) {
            var pts = [] as Array<[Numeric, Numeric]>;
            for (var x = h[0] - b; x <= h[0] + b; x += 8) {
                pts.add([v.q(x), v.q(y0 + 1.8 * Math.sin((x - h[0]) / 7.0) - (ronde == 0 ? 1.6 : 0.0))]);
            }
            pts.add([v.q(h[0] + b * 0.9), v.q(y0 + 8)]);
            pts.add([v.q(h[0] - b * 0.9), v.q(y0 + 8)]);
            v.kleur(dc, ronde == 0 ? 0xFFFFFF : (am ? (nacht ? 0x004B96 : 0x0055AF) : (nacht ? 0x0000AA : 0x0055AA)));
            dc.fillPolygon(pts);
        }
    }
}

// Het aanmeldblok van de basiswereld: één klas voor elk dier zonder eigen wereld; het diernummer gaat mee.
class KrabV2WBasis extends KrabV2Wereld {
    private var _dier as Number;

    function initialize(nr as Number) {
        KrabV2Wereld.initialize();
        _dier = nr;
    }

    function dier() as Number {
        return _dier;
    }

    // De nieuwe vriend op het proefbeeld van het eindscherm: het volgende dier van de lijst.
    function vriend() as Number {
        return (_dier + 1) % 24;
    }

    function vriendNaam() as String {
        return EbbTrouw.DIEREN[(_dier + 1) % 24][0] as String;
    }

    function held(s as Number) as Array<Number> {
        return KrabV2Basis.held(_dier, s);
    }

    function kam(s as Number) as Number {
        return KrabV2Basis.kam(_dier, s);
    }

    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        KrabV2Basis.onder(v, dc, stap, am, nacht, scherm, _dier);
    }

    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        KrabV2Basis.onderHeld(v, dc, scherm, am, h, _dier);
    }

    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        KrabV2Basis.voor(v, dc, scherm, am, nacht, h, _dier);
    }

    function lucht() as Array<Number> or Null {
        var f = KrabV2Basis.fam(_dier) * 6;
        return KrabV2Basis.LUCHT.slice(f, f + 6);
    }

    function water() as Number {
        return KrabV2Basis.WATER[KrabV2Basis.fam(_dier)];
    }

    function bundel(scherm as Number) as Array<Number> {
        return [130, 130] as Array<Number>;
    }

    // Het kader van het dier staat recht onder de cijfers: te weinig lucht is NEE.
    function streng() as Boolean {
        return true;
    }
}
