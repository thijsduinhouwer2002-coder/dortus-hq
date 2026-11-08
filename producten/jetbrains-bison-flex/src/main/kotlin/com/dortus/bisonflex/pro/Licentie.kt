package com.dortus.bisonflex.pro

import com.intellij.ui.LicensingFacade
import org.jetbrains.annotations.TestOnly

/**
 * De licentiestand van Bison & Flex Pro (eis 8, ontwerp.md).
 * - ONBEKEND: de IDE heeft de licenties nog niet geladen (`LicensingFacade` is null). Pro werkt, geen melding.
 * - GELDIG: er is een stempel voor [Licentie.PRODUCTCODE] (proef of licentie). Pro werkt.
 * - GEEN: de facade is er, maar zonder stempel. Pro werkt niet, wel eenmaal per sessie de Pro-melding.
 */
enum class LicentieStand { ONBEKEND, GELDIG, GEEN }

/** Waar de stand vandaan komt. In de IDE de facade, in unittests een nagebootste bron. */
fun interface LicentieBron {
    fun stand(): LicentieStand
}

/**
 * De echte bron: `LicensingFacade.getConfirmationStamp`. We kijken alleen of er een stempel is,
 * de handtekening van de stempel controleren we (nog) niet (zie architectuur.md, Open).
 *
 * Alleen voor de IDE-test: `-Dbisonflex.internal.e2e.forceNoLicense=true` zet de stand op GEEN, omdat de facade
 * in de test-IDE null is en de Pro-melding dan nooit komt.
 */
object FacadeBron : LicentieBron {
    const val E2E_EIGENSCHAP = "bisonflex.internal.e2e.forceNoLicense"

    @Volatile
    private var e2eStand: LicentieStand? = null

    /**
     * Alleen voor de IDE-test (via de Driver): zet halverwege de test een andere stand, bijvoorbeeld GELDIG voor de
     * meldingen van eis 7. Werkt alleen als [E2E_EIGENSCHAP] gezet is, dus nooit bij een gebruiker.
     */
    @JvmStatic
    fun zetE2eStand(stand: String) {
        if (System.getProperty(E2E_EIGENSCHAP) == "true") e2eStand = LicentieStand.valueOf(stand)
    }

    override fun stand(): LicentieStand {
        if (System.getProperty(E2E_EIGENSCHAP) == "true") return e2eStand ?: LicentieStand.GEEN
        val facade = LicensingFacade.getInstance() ?: return LicentieStand.ONBEKEND
        val stempel = facade.getConfirmationStamp(Licentie.PRODUCTCODE)
        return if (stempel.isNullOrBlank()) LicentieStand.GEEN else LicentieStand.GELDIG
    }
}

object Licentie {
    /** Zelfde code als `product-descriptor` in plugin.xml. */
    const val PRODUCTCODE = "PBISONFLEX"

    @Volatile
    private var bron: LicentieBron = FacadeBron

    /** Elke keer opnieuw gevraagd: de facade kan later komen, of de proef kan net gestart zijn. */
    fun stand(): LicentieStand = bron.stand()

    /** Pro werkt bij GELDIG en ONBEKEND, alleen niet bij GEEN. */
    fun proWerkt(): Boolean = stand() != LicentieStand.GEEN

    /** Alleen voor tests: een nagebootste licentie zetten; `null` zet de echte bron terug. */
    @TestOnly
    fun zetBronVoorTest(nieuw: LicentieBron?) {
        bron = nieuw ?: FacadeBron
    }
}
