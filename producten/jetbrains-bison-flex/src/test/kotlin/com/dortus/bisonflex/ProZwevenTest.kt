package com.dortus.bisonflex

import com.dortus.bisonflex.pro.GaNaarDefinitie
import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.dortus.bisonflex.pro.ProMelding
import com.intellij.notification.Notification
import com.intellij.notification.Notifications
import com.intellij.testFramework.PlatformTestUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/**
 * Pro-melding alleen bij een echte actie (Ctrl+B, klik, menu), niet bij Ctrl/Cmd+zweven.
 * Zweven is hier: geen ga-naar-actie bezig ([GaNaarDefinitie] met `{ false }`); een echte actie: `{ true }`.
 * De koppeling met de echte actie-luisteraar staat in GaNaarActieTest.
 */
class ProZwevenTest : BasePlatformTestCase() {

    private val meldingen = ArrayList<Notification>()

    override fun setUp() {
        super.setUp()
        ProMelding.getInstance().opnieuwVoorTest()
        project.messageBus.connect(testRootDisposable).subscribe(Notifications.TOPIC, object : Notifications {
            override fun notify(notification: Notification) {
                if (notification.groupId == ProMelding.GROEP) meldingen += notification
            }
        })
        Licentie.zetBronVoorTest { LicentieStand.GEEN }
        val map = File(System.getProperty("dortus.testdata")).parentFile.resolve("e2e/project")
        // Een doel in een ander bestand (Pro): `return NUM;` in calc.l naar `%token NUM` in calc.y.
        myFixture.addFileToProject("calc.y", File(map, "calc.y").readText())
        myFixture.configureByText("calc.l", File(map, "calc.l").readText())
    }

    override fun tearDown() {
        try {
            Licentie.zetBronVoorTest(null)
            ProMelding.getInstance().opnieuwVoorTest()
        } finally {
            super.tearDown()
        }
    }

    /** Ga naar definitie op `NUM` in `return NUM;` (een token in een ander bestand); [actie] is of er een ga-naar-actie bezig is. */
    private fun probeer(actie: Boolean): Int {
        val offset = myFixture.editor.document.text.indexOf("return NUM") + 8
        val doelen = GaNaarDefinitie { actie }.getGotoDeclarationTargets(myFixture.file.findElementAt(offset), offset, myFixture.editor)
        return doelen?.size ?: 0
    }

    private val ZWEVEN = false
    private val ACTIE = true

    fun testZwevenGeenSprongGeenMelding() {
        assertEquals(0, probeer(ZWEVEN))
        assertEquals(0, probeer(ZWEVEN))
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertEquals(0, meldingen.size)
        assertEquals(0, ProMelding.getInstance().aantalHints())
        assertFalse(ProMelding.getInstance().isGetoond())
    }

    fun testZwevenNaMeldingGeenHint() {
        assertEquals(0, probeer(ACTIE))
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertEquals(0, probeer(ZWEVEN))
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertEquals(1, meldingen.size)
        assertEquals(0, ProMelding.getInstance().aantalHints())
    }

    fun testNaZwevenGeeftEchteActieWelDeMelding() {
        assertEquals(0, probeer(ZWEVEN))
        assertEquals(0, probeer(ACTIE))
        assertEquals(0, probeer(ACTIE))
        assertEquals(1, meldingen.size)
    }

    /** Binnen hetzelfde bestand is gratis: zweven op `exp` in `| exp '\n'` van calc.y geeft doelen, zonder melding of hint. */
    fun testGeenLicentieZwevenBinnenBestandGeeftDoelenZonderMelding() {
        myFixture.openFileInEditor(myFixture.findFileInTempDir("calc.y"))
        val offset = myFixture.editor.document.text.indexOf("| exp '") + 2
        val doelen = GaNaarDefinitie { ZWEVEN }
            .getGotoDeclarationTargets(myFixture.file.findElementAt(offset), offset, myFixture.editor)
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertTrue((doelen?.size ?: 0) >= 1)
        assertEquals(0, meldingen.size)
        assertFalse(ProMelding.getInstance().isGetoond())
        assertEquals(0, ProMelding.getInstance().aantalHints())
    }

    fun testMetLicentieSpringtZwevenWel() {
        Licentie.zetBronVoorTest { LicentieStand.GELDIG }
        assertEquals(1, probeer(ZWEVEN))
        assertEquals(0, meldingen.size)
    }
}
