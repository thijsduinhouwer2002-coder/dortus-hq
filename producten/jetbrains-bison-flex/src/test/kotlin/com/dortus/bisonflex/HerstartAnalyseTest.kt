package com.dortus.bisonflex

import com.dortus.bisonflex.meldingen.HerstartAnalyse
import com.intellij.openapi.application.ApplicationInfo
import com.intellij.testFramework.fixtures.BasePlatformTestCase

/** Herstart van de analyse zonder verouderde API (keuring Marketplace 8 nov 2026), zie [HerstartAnalyse]. */
class HerstartAnalyseTest : BasePlatformTestCase() {

    /** Op elk platform vanaf 2025.2 vindt hij een weg, en vanaf 2025.3 de opvolger met reden. */
    fun testVindtDeJuisteWegVoorDitPlatform() {
        val build = ApplicationInfo.getInstance().build.baselineVersion
        println("HERSTART: platform $build, met reden ${HerstartAnalyse.metReden != null}, zonder reden ${HerstartAnalyse.zonderReden != null}")
        if (build >= 253) assertNotNull("restart(Object) hoort te bestaan vanaf 253", HerstartAnalyse.metReden)
        else assertNull("restart(Object) bestaat in $build nog niet openbaar", HerstartAnalyse.metReden)
        assertTrue(HerstartAnalyse.metReden != null || HerstartAnalyse.zonderReden != null)
    }

    /** De herstart zelf geeft geen fout en de analyse loopt daarna gewoon door. */
    fun testHerstartGeeftGeenFout() {
        myFixture.configureByText("calc.y", "%token NUM\n%%\nexp: NUM ;\n")
        HerstartAnalyse.voor(project)
        myFixture.checkHighlighting(false, false, false)
    }
}
