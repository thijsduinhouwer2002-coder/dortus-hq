package com.dortus.bisonflex

import com.dortus.bisonflex.pro.GaNaarActie
import com.dortus.bisonflex.pro.GaNaarDefinitie
import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.dortus.bisonflex.pro.ProMelding
import com.intellij.notification.Notification
import com.intellij.notification.Notifications
import com.intellij.openapi.actionSystem.ActionManager
import com.intellij.openapi.actionSystem.ActionUiKind
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.actionSystem.AnActionResult
import com.intellij.openapi.actionSystem.DataContext
import com.intellij.openapi.actionSystem.IdeActions
import com.intellij.openapi.actionSystem.MouseShortcut
import com.intellij.openapi.actionSystem.Presentation
import com.intellij.openapi.actionSystem.ex.AnActionListener
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.keymap.KeymapManager
import com.intellij.testFramework.PlatformTestUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.awt.event.InputEvent
import java.awt.event.MouseEvent
import java.io.File

/**
 * De echte handler (zonder vervanging) met de echte luisteraar uit plugin.xml: melding en hint alleen als er een
 * ga-naar-actie bezig is. De acties gaan via de berichtenbus van de IDE, zoals ActionUtil dat doet.
 */
class GaNaarActieTest : BasePlatformTestCase() {

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

    private val bus get() = ApplicationManager.getApplication().messageBus.syncPublisher(AnActionListener.TOPIC)
    private fun gebeurtenis() = AnActionEvent.createEvent(DataContext.EMPTY_CONTEXT, Presentation(), "test", ActionUiKind.NONE, null)

    /** Doet [werk] binnen de actie [id], met before/afterActionPerformed zoals de IDE. */
    private fun <T> inActie(id: String, werk: () -> T): T {
        val actie = ActionManager.getInstance().getAction(id)
        assertNotNull("actie $id bestaat", actie)
        val e = gebeurtenis()
        bus.beforeActionPerformed(actie, e)
        try {
            return werk()
        } finally {
            bus.afterActionPerformed(actie, e, AnActionResult.PERFORMED)
        }
    }

    /** De echte handler op `NUM` in `return NUM;` (doel in calc.y, dus Pro). Geeft het aantal doelen. */
    private fun probeer(): Int {
        val offset = myFixture.editor.document.text.indexOf("return NUM") + 8
        val doelen = GaNaarDefinitie().getGotoDeclarationTargets(myFixture.file.findElementAt(offset), offset, myFixture.editor)
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        return doelen?.size ?: 0
    }

    fun testGeenActieBezigGeeftGeenMelding() {
        assertFalse(GaNaarActie.isBezig())
        assertEquals(0, probeer())
        assertEquals(0, probeer())
        assertEquals(0, meldingen.size)
        assertFalse(ProMelding.getInstance().isGetoond())
        assertEquals(0, ProMelding.getInstance().aantalHints())
    }

    fun testActieBezigGeeftWelMelding() {
        assertEquals(0, inActie(IdeActions.ACTION_GOTO_DECLARATION) { assertTrue(GaNaarActie.isBezig()); probeer() })
        assertFalse("na afterActionPerformed geen actie meer", GaNaarActie.isBezig())
        assertEquals(1, meldingen.size)
        // Zweven na de balloon: geen hint erbij. Een tweede Ctrl+B wel.
        assertEquals(0, probeer())
        assertEquals(0, ProMelding.getInstance().aantalHints())
        assertEquals(0, inActie("GotoDeclarationOnly") { probeer() })
        assertEquals(1, meldingen.size)
        assertEquals(1, ProMelding.getInstance().aantalHints())
    }

    fun testAndereActieTeltNiet() {
        inActie(IdeActions.ACTION_EDITOR_COPY) { assertFalse(GaNaarActie.isBezig()); probeer() }
        assertEquals(0, meldingen.size)
    }

    fun testActieBinnenActieWistDeVlagNietTeVroeg() {
        inActie(IdeActions.ACTION_GOTO_DECLARATION) {
            inActie(IdeActions.ACTION_GOTO_TYPE_DECLARATION) { }
            assertTrue(GaNaarActie.isBezig())
        }
        assertFalse(GaNaarActie.isBezig())
    }

    /** De id's in GaNaarActie bestaan in de IDE (anders zou de vlag nooit staan). */
    fun testActieIdsBestaan() {
        for (id in GaNaarActie.ACTIES) assertNotNull("actie $id", ActionManager.getInstance().getAction(id))
    }

    /** Ctrl+klik loopt via de muissnelkoppeling van dezelfde actie (zo vindt CtrlMouseHandler2 ook de actie). */
    fun testCtrlKlikIsGotoDeclarationInDeKeymap() {
        val keymap = KeymapManager.getInstance().activeKeymap
        val muis = keymap.getShortcuts(IdeActions.ACTION_GOTO_DECLARATION).filterIsInstance<MouseShortcut>()
        println("DORTUS-TEST keymap ${keymap.name}: muissnelkoppelingen GotoDeclaration $muis")
        assertTrue(muis.any { it.button == MouseEvent.BUTTON1 && it.modifiers and (InputEvent.CTRL_DOWN_MASK or InputEvent.META_DOWN_MASK) != 0 })
    }
}
