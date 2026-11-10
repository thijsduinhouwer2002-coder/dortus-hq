import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Timer;
import Toybox.WatchUi;

class AdemView extends WatchUi.View {
    private var _timer as Timer.Timer = new Timer.Timer();
    private var _start as Number = 0;
    private var _opname as Opname = new Opname();

    function initialize() {
        View.initialize();
    }

    function onShow() as Void {
        _start = System.getTimer();
        _timer.start(method(:tik), 50, true);
        _opname.start();
    }

    function onHide() as Void {
        _timer.stop();
    }

    function tik() as Void {
        WatchUi.requestUpdate();
    }

    function onUpdate(dc as Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var t = System.getTimer() - _start;
        var f = Adem.fractie(t, 4000, 4000, 4000, 4000);
        dc.setColor(0x0B1E2D, 0x0B1E2D);
        dc.clear();
        var rMin = w * 0.18;
        var rMax = w * 0.40;
        var r = rMin + (rMax - rMin) * f;
        dc.setColor(0x1F4E6B, Graphics.COLOR_TRANSPARENT);
        dc.fillCircle(w / 2, h / 2, r + 8);
        dc.setColor(0x7FD1C7, Graphics.COLOR_TRANSPARENT);
        dc.fillCircle(w / 2, h / 2, r);
        dc.setColor(0x0B1E2D, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, h / 2, Graphics.FONT_SMALL, Adem.fase(t, 4000, 4000, 4000, 4000), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}
