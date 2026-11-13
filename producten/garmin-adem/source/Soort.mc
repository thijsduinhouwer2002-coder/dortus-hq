import Toybox.Lang;

// Welke app wordt er gebouwd? De volle Ebb (monkey.jungle, demo.jungle, plaatjes.jungle sluiten (:calm) uit) of de
// gratis Ebb Calm (calm.jungle en calm-plaatjes.jungle sluiten (:vol) uit; eigen manifest-calm.xml met eigen app-id).
// Ebb Calm (besluit Thijs 13 nov 2026): alleen Calm 4-7-8 met de zee, één dier (de vis), geen verzameling, geen sea
// log, geen reeksen, geen rondes en geen My pattern. Alles wat anders is hangt aan deze ene vlag.
(:vol)
module EbbSoort {
    const CALM = false;
    const NAAM = "Ebb";
}

(:calm)
module EbbSoort {
    const CALM = true;
    const NAAM = "Ebb Calm";
}
