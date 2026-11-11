import Toybox.Lang;

// Testbouw voor eis 10 (demo.jungle zet DEMO aan): een korte sessie met bekende inhoudtijden 3 s en 5 s,
// daarna opslaan, en een tweede opname die wordt weggegooid. De echte bouw sluit (:demo) uit.
(:demo)
module EbbBouw {
    const DEMO = true;
    const PLAATJE = false;
    const SCENES = 35;
    const INHOUD_MS = [3000, 5000] as Array<Number>;
}

(:echt)
module EbbBouw {
    const DEMO = false;
    const PLAATJE = false;
    const SCENES = 35;
    const INHOUD_MS = [] as Array<Number>;
}

// Bouw voor de winkelplaatjes (plaatjes.jungle): elke start toont één vaste scène, stilgezet zodat de
// schermafbeelding niet van de timing afhangt. Neemt niets op.
(:plaatje)
module EbbBouw {
    const DEMO = false;
    const PLAATJE = true;
    const SCENES = 35;
    const INHOUD_MS = [] as Array<Number>;
}
