import Toybox.Lang;
using Toybox.Application;
using Toybox.Application.Storage;
using Toybox.Audio;
using Toybox.Audio.Capture;
using Toybox.Audio.Output;
using Toybox.Graphics;
using Toybox.System;
using Toybox.Timer;
using Toybox.WatchUi;

// Proef voor de spraakmemo (Gijs, 17 nov 2026): neemt de simulator op, hoeveel bytes per seconde,
// kan het terug worden afgespeeld en hoeveel past er in de opslag. Alles gaat met println naar het log.

class Vanger {
    var bytes = 0;
    var blokken = 0;
    var stukken = [];
    function initialize() {}
    function onData(audioData) {
        blokken += 1;
        bytes += audioData.size();
        if (stukken.size() < 60) { stukken.add(audioData); }
        System.println("MEMO onData blok " + blokken + " grootte " + audioData.size() + " totaal " + bytes);
    }
    function onError(error) { System.println("MEMO onError " + error); }
    function onComplete() { System.println("MEMO onComplete totaal " + bytes + " bytes in " + blokken + " blokken"); }
}

class MemoProefView extends WatchUi.View {
    var regel = "start";
    function initialize() { View.initialize(); }
    function onUpdate(dc) {
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_BLACK);
        dc.clear();
        dc.drawText(dc.getWidth() / 2, dc.getHeight() / 2, Graphics.FONT_SMALL, regel, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}

class MemoProefApp extends Application.AppBase {
    var vanger;
    var view;
    var t1;
    var t2;
    var t3;
    var formaat;

    function initialize() { AppBase.initialize(); }

    function getInitialView() {
        view = new MemoProefView();
        return [view];
    }

    function onStart(state) {
        System.println("MEMO start, geheugen vrij " + System.getSystemStats().freeMemory + " van " + System.getSystemStats().totalMemory);
        t1 = new Timer.Timer();
        t1.start(method(:stap1), 2000, false);
    }

    function probeer(naam, f) {
        try {
            if (!(Capture has :isFormatSupported)) { System.println("MEMO formaat " + naam + ": isFormatSupported bestaat niet op dit horloge"); return; }
            System.println("MEMO formaat " + naam + " ondersteund: " + Capture.isFormatSupported(f));
        } catch (e) {
            System.println("MEMO formaat " + naam + " fout: " + e.getErrorMessage());
        }
    }

    function stap1() as Void {
        var opus16 = { :containerFormat => Audio.CONTAINER_OGG, :codec => Audio.CODEC_OPUS, :frequency => Audio.FREQ_16_KHZ, :channels => Audio.CHANNEL_MONO };
        var opus8 = { :containerFormat => Audio.CONTAINER_OGG, :codec => Audio.CODEC_OPUS, :frequency => Audio.FREQ_8_KHZ, :channels => Audio.CHANNEL_MONO };
        var wav8 = { :containerFormat => Audio.CONTAINER_WAV, :codec => Audio.CODEC_LPCM, :frequency => Audio.FREQ_8_KHZ, :channels => Audio.CHANNEL_MONO };
        var wav16 = { :containerFormat => Audio.CONTAINER_WAV, :codec => Audio.CODEC_LPCM, :frequency => Audio.FREQ_16_KHZ, :channels => Audio.CHANNEL_MONO };
        System.println("MEMO heeft Toybox Audio: " + (Toybox has :Audio));
        System.println("MEMO Audio heeft CONTAINER_OGG: " + (Audio has :CONTAINER_OGG) + ", Capture: " + (Audio has :Capture) + ", Output: " + (Audio has :Output) + ", AudioResource: " + (Audio has :AudioResource));
        var kanOpnemen = (Audio has :Capture) && (Capture has :initializeAudioCapture) && (Capture has :start);
        System.println("MEMO kan opnemen volgens has: " + kanOpnemen);
        if (!kanOpnemen) {
            System.println("MEMO geen Audio in deze simulator met deze horlogebestanden, alleen de opslag wordt gemeten");
            vanger = new Vanger();
            formaat = null;
            t3 = new Timer.Timer();
            t3.start(method(:stap3), 1000, false);
            return;
        }
        System.println("MEMO heeft Audio Capture: " + (Audio has :Capture) + ", Output: " + (Audio has :Output));
        System.println("MEMO Capture heeft init: " + (Capture has :initializeAudioCapture) + ", start: " + (Capture has :start) + ", filters: " + (Capture has :getSupportedFilters) + ", staat: " + (Capture has :getState));
        System.println("MEMO Output heeft play: " + (Output has :play) + ", bouwer: " + (Output has :DynamicAudioSourceBuilder));
        System.println("MEMO heeft DynamicResource: " + (Application has :DynamicResource));
        probeer("ogg-opus-16k", opus16);
        probeer("ogg-opus-8k", opus8);
        probeer("wav-lpcm-8k", wav8);
        probeer("wav-lpcm-16k", wav16);
        try {
            if (Capture has :getSupportedFilters) { System.println("MEMO filters: " + Capture.getSupportedFilters()); }
        } catch (e) {
            System.println("MEMO filters fout: " + e.getErrorMessage());
        }
        formaat = opus16;
        vanger = new Vanger();
        try {
            var terug = Capture.initializeAudioCapture(vanger, { :format => formaat, :windowSize => 4096, :windowFilledBehavior => Capture.WINDOW_FILLED_CONTINUE, :filters => [] });
            System.println("MEMO instellingen terug: " + terug);
            System.println("MEMO staat na init: " + Capture.getState());
            Capture.start();
            System.println("MEMO staat na start: " + Capture.getState());
            view.regel = "opname";
            WatchUi.requestUpdate();
        } catch (e) {
            System.println("MEMO opname fout: " + e.getErrorMessage());
        }
        t2 = new Timer.Timer();
        t2.start(method(:stap2), 10000, false);
    }

    function stap2() as Void {
        try {
            Capture.stop();
            System.println("MEMO gestopt na 10 s, staat: " + Capture.getState() + ", totaal " + vanger.bytes + " bytes, " + vanger.blokken + " blokken");
        } catch (e) {
            System.println("MEMO stop fout: " + e.getErrorMessage());
        }
        t3 = new Timer.Timer();
        t3.start(method(:stap3), 2000, false);
    }

    function stap3() as Void {
        System.println("MEMO na stop: totaal " + vanger.bytes + " bytes, per seconde ongeveer " + (vanger.bytes / 10));
        // terug afspelen uit de bewaarde stukken
        if (formaat != null) { try {
            var bouwer = new Output.DynamicAudioSourceBuilder({ :format => formaat });
            for (var i = 0; i < vanger.stukken.size(); i++) { bouwer.append(vanger.stukken[i]); }
            var bron = bouwer.complete();
            Output.play(bron, null);
            System.println("MEMO afspelen gestart, staat: " + Output.getState() + ", fout: " + Output.getError());
        } catch (e) {
            System.println("MEMO afspelen fout: " + e.getErrorMessage());
        } }
        // opslag: hoeveel blokken van 30.000 bytes passen erin
        var blok = new [30000]b;
        var n = 0;
        try {
            Storage.clearValues();
            while (n < 400) {
                Storage.setValue("b" + n, blok);
                n += 1;
            }
            System.println("MEMO opslag: 400 blokken van 30000 bytes pasten, niet verder geprobeerd");
        } catch (e) {
            System.println("MEMO opslag vol na " + n + " blokken van 30000 bytes: " + e.getErrorMessage());
        }
        try {
            var terug = Storage.getValue("b0");
            System.println("MEMO opslag teruglezen b0: " + (terug == null ? "null" : terug.size()));
            Storage.clearValues();
        } catch (e) {
            System.println("MEMO teruglezen fout: " + e.getErrorMessage());
        }
        if (formaat != null) { System.println("MEMO afspeelstaat aan het eind: " + Output.getState() + ", fout: " + Output.getError()); }
        System.println("MEMO geheugen vrij aan het eind " + System.getSystemStats().freeMemory);
        System.println("MEMO klaar");
        view.regel = "klaar";
        WatchUi.requestUpdate();
    }
}
