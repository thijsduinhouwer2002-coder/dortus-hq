package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.driver.client.Remote
import com.intellij.driver.client.service
import com.intellij.driver.sdk.openFile
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertTrue

/** Hulp in de plugin voor deze stap (`meldingen/MeldingenDiagnose.kt`), werkt alleen met de e2e-eigenschap. */
@Remote("com.dortus.bisonflex.meldingen.MeldingenDiagnose", plugin = "com.dortus.bisonflex")
interface MeldingenDiagnoseOpAfstand {
    fun zetStand(stand: String)
    fun vervang(oud: String, nieuw: String): Boolean
    fun meldingen(): String
    fun cursorOp(tekst: String, extra: Int): Boolean
}

private const val ANKER = "\n%%\n\nvoid yyerror"
private const val MET_FOUT = "\nunused:\n    UNDEFINED\n  ;\n\n%%\n\nvoid yyerror"
private const val ONGEBRUIKT = "Unused rule 'unused'"
private const val ONGEDEFINIEERD = "Undefined symbol 'UNDEFINED'"

/**
 * Eis 7 in de echte IDE (ontwerp.md, toetsbare eis f; Daan, beoordeling 10). Loopt na het hernoemen, dus in stand
 * GEEN: eerst kijken dat er geen meldingen zijn, dan de stand op GELDIG (de StandLuisteraar herstart de analyse),
 * in calc.y tijdelijk een ongebruikte regel met een onbekend symbool, de meldingen afwachten en tonen
 * (schermen `meldingen` en `meldingen-oplossing` met het Alt+Enter-menu), en calc.y terugzetten.
 */
internal fun IdeTest.meldingen(d: Driver, naam: String) = with(d) {
    val diagnose = service<MeldingenDiagnoseOpAfstand>()
    openFile("calc.y")
    pauze()
    assertTrue(diagnose.vervang(ANKER, MET_FOUT), "fout in calc.y gezet ($naam)")
    Thread.sleep(5_000)
    val inGeen = diagnose.meldingen()
    println("DORTUS-E2E [$naam] meldingen in stand GEEN: '$inGeen' (moet leeg zijn)")
    assertEquals("", inGeen, "geen meldingen in stand GEEN ($naam)")

    diagnose.zetStand("GELDIG")
    println("DORTUS-E2E [$naam] stand op GELDIG gezet")
    var gezien = ""
    val beide = wacht(40) {
        gezien = diagnose.meldingen()
        ONGEBRUIKT in gezien && ONGEDEFINIEERD in gezien
    }
    println("DORTUS-E2E [$naam] meldingen in stand GELDIG: '$gezien'")
    assertTrue(beide, "beide meldingen in calc.y na GELDIG ($naam), gezien: '$gezien'")
    assertTrue(diagnose.cursorOp("    UNDEFINED", 4), "cursor op UNDEFINED ($naam)")
    pauze()
    scherm("$naam-meldingen.png")

    // Alt+Enter op de ongebruikte regel: het menu met "Remove unused rule 'unused'".
    assertTrue(diagnose.cursorOp("\nunused:", 2), "cursor op unused ($naam)")
    Thread.sleep(2_000)
    toets("alt+Return")
    Thread.sleep(3_000)
    scherm("$naam-meldingen-oplossing.png")
    toets("Escape")
    Thread.sleep(1_000)

    assertTrue(diagnose.vervang(MET_FOUT, ANKER), "calc.y teruggezet ($naam)")
    val schoon = wacht(20) { diagnose.meldingen().isEmpty() }
    println("DORTUS-E2E [$naam] na terugzetten: meldingen '${diagnose.meldingen()}'")
    assertTrue(schoon, "geen meldingen meer na terugzetten ($naam)")
    diagnose.zetStand("GEEN")
}
