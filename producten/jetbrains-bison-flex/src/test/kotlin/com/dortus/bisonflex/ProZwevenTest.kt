package com.dortus.bisonflex

import com.dortus.bisonflex.pro.GaNaarDefinitie
import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.dortus.bisonflex.pro.ProMelding
import com.intellij.notification.Notification
import com.intellij.notification.Notifications
import com.intellij.testFramework.PlatformTestUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.awt.AWTEvent
import java.awt.event.InputEvent
import java.awt.event.KeyEvent
import java.awt.event.MouseEvent
import java.io.File
import javax.swing.JPanel

/** Pro-melding alleen bij een echte actie (Ctrl+B, klik, menu), niet bij Ctrl/Cmd+zweven. */
class ProZwevenTest : BasePlatformTestCase() {

    private val meldingen = ArrayList<Notification>()
    private val bron = JPanel()

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

    private fun muis(id: Int) = MouseEvent(bron, id, 0L, InputEvent.CTRL_DOWN_MASK, 10, 10, 1, false)
    private fun toets(code: Int) = KeyEvent(bron, KeyEvent.KEY_PRESSED, 0L, InputEvent.CTRL_DOWN_MASK, code, KeyEvent.CHAR_UNDEFINED)

    /** Ga naar definitie op `NUM` in `return NUM;` (een token in een ander bestand), met [e] als huidige gebeurtenis. */
    private fun probeer(e: AWTEvent?): Int {
        val offset = myFixture.editor.document.text.indexOf("return NUM") + 8
        val doelen = GaNaarDefinitie { e }.getGotoDeclarationTargets(myFixture.file.findElementAt(offset), offset, myFixture.editor)
        return doelen?.size ?: 0
    }

    fun testZwevenHerkend() {
        assertTrue(GaNaarDefinitie.isZweven(muis(MouseEvent.MOUSE_MOVED)))
        assertTrue(GaNaarDefinitie.isZweven(toets(KeyEvent.VK_CONTROL)))
        assertTrue(GaNaarDefinitie.isZweven(toets(KeyEvent.VK_META)))
        assertFalse(GaNaarDefinitie.isZweven(muis(MouseEvent.MOUSE_PRESSED)))
        assertFalse(GaNaarDefinitie.isZweven(muis(MouseEvent.MOUSE_CLICKED)))
        assertFalse(GaNaarDefinitie.isZweven(toets(KeyEvent.VK_B)))
        assertFalse(GaNaarDefinitie.isZweven(null))
    }

    fun testZwevenGeenSprongGeenMelding() {
        assertEquals(0, probeer(muis(MouseEvent.MOUSE_MOVED)))
        assertEquals(0, probeer(toets(KeyEvent.VK_CONTROL)))
        assertEquals(0, meldingen.size)
        assertFalse(ProMelding.getInstance().isGetoond())
    }

    fun testZwevenNaMeldingGeenHint() {
        assertEquals(0, probeer(toets(KeyEvent.VK_B)))
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertEquals(0, probeer(muis(MouseEvent.MOUSE_MOVED)))
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertEquals(1, meldingen.size)
        assertEquals(0, ProMelding.getInstance().aantalHints())
    }

    fun testNaZwevenGeeftEchteActieWelDeMelding() {
        assertEquals(0, probeer(muis(MouseEvent.MOUSE_MOVED)))
        assertEquals(0, probeer(toets(KeyEvent.VK_B)))
        assertEquals(0, probeer(muis(MouseEvent.MOUSE_CLICKED)))
        assertEquals(1, meldingen.size)
    }

    /** Binnen hetzelfde bestand is gratis: zweven op `exp` in `| exp '\n'` van calc.y geeft doelen, zonder melding of hint. */
    fun testGeenLicentieZwevenBinnenBestandGeeftDoelenZonderMelding() {
        myFixture.openFileInEditor(myFixture.findFileInTempDir("calc.y"))
        val offset = myFixture.editor.document.text.indexOf("| exp '") + 2
        val doelen = GaNaarDefinitie { muis(MouseEvent.MOUSE_MOVED) }
            .getGotoDeclarationTargets(myFixture.file.findElementAt(offset), offset, myFixture.editor)
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertTrue((doelen?.size ?: 0) >= 1)
        assertEquals(0, meldingen.size)
        assertFalse(ProMelding.getInstance().isGetoond())
        assertEquals(0, ProMelding.getInstance().aantalHints())
    }

    fun testMetLicentieSpringtZwevenWel() {
        Licentie.zetBronVoorTest { LicentieStand.GELDIG }
        assertEquals(1, probeer(muis(MouseEvent.MOUSE_MOVED)))
        assertEquals(0, meldingen.size)
    }
}
