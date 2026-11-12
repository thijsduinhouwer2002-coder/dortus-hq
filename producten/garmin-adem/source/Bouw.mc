import Toybox.Lang;
import Toybox.WatchUi;

// Testbouw voor eis 10 (demo.jungle zet DEMO aan): een korte sessie met bekende inhoudtijden 3 s en 5 s,
// daarna opslaan, en een tweede opname die wordt weggegooid. De echte bouw sluit (:demo) uit.
(:demo)
module EbbBouw {
    const DEMO = true;
    const PLAATJE = false;
    const SCENES = 85;
    // Eerste scène van de plaatjesbouw; de workflow zet dit op een proeftak op 51 (alleen de proefscènes).
    const EERSTE = 0;
    const INHOUD_MS = [3000, 5000] as Array<Number>;
    // De workflow zet dit voor één aparte bouw op true (bin/pauze-<horloge>.prg): bewijs dat het pauzemenu vanzelf opslaat.
    const PAUZEPROEF = false;
    // Scenes.mc hoort alleen bij de plaatjesbouw ((:plaatje)); in deze bouw bestaat EbbScenes niet (herkeuring 12 nov punt 6).
    function scene(app as EbbApp, view as EbbView) as [WatchUi.Views, WatchUi.InputDelegates] or Null {
        return null;
    }
}

(:echt)
module EbbBouw {
    const DEMO = false;
    const PLAATJE = false;
    const SCENES = 85;
    // Eerste scène van de plaatjesbouw; de workflow zet dit op een proeftak op 51 (alleen de proefscènes).
    const EERSTE = 0;
    const INHOUD_MS = [] as Array<Number>;
    const PAUZEPROEF = false;
    // Scenes.mc hoort alleen bij de plaatjesbouw ((:plaatje)); in deze bouw bestaat EbbScenes niet (herkeuring 12 nov punt 6).
    function scene(app as EbbApp, view as EbbView) as [WatchUi.Views, WatchUi.InputDelegates] or Null {
        return null;
    }
}

// Bouw voor de winkelplaatjes (plaatjes.jungle): elke start toont één vaste scène, stilgezet zodat de
// schermafbeelding niet van de timing afhangt. Neemt niets op.
(:plaatje)
module EbbBouw {
    const DEMO = false;
    const PLAATJE = true;
    const SCENES = 85;
    // Eerste scène van de plaatjesbouw; de workflow zet dit op een proeftak op 51 (alleen de proefscènes).
    const EERSTE = 0;
    const INHOUD_MS = [] as Array<Number>;
    const PAUZEPROEF = false;
    function scene(app as EbbApp, view as EbbView) as [WatchUi.Views, WatchUi.InputDelegates] or Null {
        return EbbScenes.start(app, view);
    }
}
