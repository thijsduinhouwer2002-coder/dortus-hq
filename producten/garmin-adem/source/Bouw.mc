import Toybox.Lang;

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
}
