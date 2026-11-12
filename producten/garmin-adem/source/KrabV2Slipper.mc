import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// PROEF krabwereld (zie KrabV2.mc): de slipper waarop de krab drijft en het V-bandje over de krab heen. Uit KrabV2.mc
// gehaald in run 55 (regel van 300), niets aan de tekening veranderd. v.sl is hak x, y, schaal en hoek van de slipper.
module KrabV2Slipper {
    // Punt op de slipper (hak op 0, neus op 62) naar 1/260 van het scherm.
    function rs(v as KrabV2View, x as Float, y as Float) as Array<Float> {
        var a = Math.toRadians(v.sl[3]);
        var c = Math.cos(a);
        var s = Math.sin(a);
        return [(v.sl[0] + (x * c - y * s) * v.sl[2]).toFloat(), (v.sl[1] + (x * s + y * c) * v.sl[2]).toFloat()] as Array<Float>;
    }

    function halveBreedte(x as Float) as Float {
        if (x < 0.0) {
            return Math.sqrt(169.0 - x * x).toFloat();
        } else if (x < 26.0) {
            return 13.0 - 4.2 * x / 26.0;
        } else if (x <= 50.0) {
            return 8.8 + 6.2 * (x - 26.0) / 24.0;
        }
        var r = 225.0 - (x - 50.0) * (x - 50.0);
        return r > 0.0 ? Math.sqrt(r).toFloat() : 0.0;
    }

    function slipper(v as KrabV2View, dc as Graphics.Dc) as Void {
        var p = [] as Array<Float>;
        for (var i = 0; i <= 14; i += 1) {
            var x = -13.0 + i * 78.0 / 14.0;
            p.addAll(rs(v, x, -halveBreedte(x) * 0.8));
        }
        for (var i = 14; i >= 0; i -= 1) {
            var x = -13.0 + i * 78.0 / 14.0;
            p.addAll(rs(v, x, halveBreedte(x) * 0.8));
        }
        var zool = [] as Array<Float>;
        for (var i = 0; i < p.size(); i += 2) {
            zool.add(p[i] + 0.8 * v.sl[2]);
            zool.add(p[i + 1] + 3.2 * v.sl[2]);
        }
        v.blob(dc, zool, 0xAA0055, 0xFFFFFF, 2.2);
        v.blob(dc, p, 0xFF55AA, -1, 0.0);
        var g = [] as Array<Float>;
        g.addAll(rs(v, 30.0, -4.5)); g.addAll(rs(v, 46.0, -6.0)); g.addAll(rs(v, 58.0, -4.0)); g.addAll(rs(v, 46.0, -3.0));
        v.blob(dc, g, 0xFFAAFF, -1, 0.0);
        var t = [] as Array<Float>;
        t.addAll(rs(v, 52.0, -1.0)); t.addAll(rs(v, 57.0, -3.5)); t.addAll(rs(v, 61.0, -1.0)); t.addAll(rs(v, 57.0, 1.5));
        v.blob(dc, t, 0xAA0055, -1, 0.0);
    }

    // V-bandje over de krab heen: van het teenpaaltje naar beide kanten van de taille, wit en dik.
    function bandje(v as KrabV2View, dc as Graphics.Dc) as Void {
        var sch = v.sl[2];
        var paal = rs(v, 55.0, 0.0);
        var py = paal[1] - 2.0 * sch;
        var kant = [rs(v, 31.0, -10.5), rs(v, 31.0, 10.5)] as Array<Array<Float> >;
        v.kleur(dc, 0xFFFFFF);
        var w = v.q(5.0 * sch);
        dc.setPenWidth(w < 2 ? 2 : w);
        for (var i = 0; i < 2; i += 1) {
            dc.drawLine(v.q(kant[i][0]), v.q(kant[i][1]), v.q(paal[0]), v.q(py));
            dc.fillCircle(v.q(kant[i][0]), v.q(kant[i][1]), v.q(2.1 * sch));
        }
        dc.fillCircle(v.q(paal[0]), v.q(py), v.q(3.2 * sch));
        dc.setPenWidth(1);
    }
}
