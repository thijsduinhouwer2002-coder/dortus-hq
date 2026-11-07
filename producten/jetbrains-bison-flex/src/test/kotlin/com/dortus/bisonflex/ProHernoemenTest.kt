package com.dortus.bisonflex

import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.dortus.bisonflex.pro.ProHernoemen
import com.dortus.bisonflex.pro.ProHernoemenScanner
import com.dortus.bisonflex.pro.ProMelding
import com.dortus.bisonflex.psi.Koppeling
import com.dortus.bisonflex.psi.NaamElement
import com.intellij.notification.Notification
import com.intellij.notification.Notifications
import com.intellij.openapi.actionSystem.CommonDataKeys
import com.intellij.openapi.actionSystem.impl.SimpleDataContext
import com.intellij.psi.PsiDocumentManager
import com.intellij.psi.PsiFile
import com.intellij.psi.PsiManager
import com.intellij.psi.util.PsiTreeUtil
import com.intellij.testFramework.DumbModeTestUtils
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/**
 * Daan, beoordeling 8: de meldingen bij geblokkeerd hernoemen (zonder licentie, token ook in de scanner).
 * 1. de balloon gaat over hernoemen en noemt naam en ander bestand; 2. de hint zegt waarom er niets gebeurde;
 * 3. zonder editor (structuurweergave) komt de hint in de statusbalk; 4. tijdens indexeren nooit de Pro-melding en
 * nooit half hernoemen; 5. een eigen vlag per actie; 6. Shift+F6 in de scanner geeft de melding, geen IDE-fout.
 */
class ProHernoemenTest : BasePlatformTestCase() {

    private val meldingen = ArrayList<Notification>()
    private val map get() = File(System.getProperty("dortus.testdata")).parentFile.resolve("e2e/project")
    private fun tekst(naam: String) = File(map, naam).readText()
    private val melding get() = ProMelding.getInstance()

    override fun setUp() {
        super.setUp()
        melding.opnieuwVoorTest()
        project.messageBus.connect(testRootDisposable).subscribe(Notifications.TOPIC, object : Notifications {
            override fun notify(notification: Notification) {
                if (notification.groupId == ProMelding.GROEP) meldingen += notification
            }
        })
    }

    override fun tearDown() {
        try {
            Licentie.zetBronVoorTest(null)
            melding.opnieuwVoorTest()
        } finally {
            super.tearDown()
        }
    }

    private fun stand(s: LicentieStand) = Licentie.zetBronVoorTest { s }

    private fun definitie(f: PsiFile, naam: String): NaamElement =
        PsiTreeUtil.findChildrenOfType(f, NaamElement::class.java).first { it.name == naam }

    private fun cursorOp(woord: String) = myFixture.editor.caretModel.moveToOffset(myFixture.editor.document.text.indexOf(woord) + 1)

    private fun inhoud(pad: String): String {
        PsiDocumentManager.getInstance(project).commitAllDocuments()
        return PsiManager.getInstance(project).findFile(myFixture.findFileInTempDir(pad))!!.text
    }

    /** calc.l in het project, calc.y open in de editor; geeft calc.y. */
    private fun grammaticaOpen(): PsiFile {
        stand(LicentieStand.GEEN)
        myFixture.addFileToProject("calc.l", tekst("calc.l"))
        return myFixture.configureByText("calc.y", tekst("calc.y"))
    }

    fun testBalloonGaatOverHernoemen() {
        grammaticaOpen()
        cursorOp("NUM")
        myFixture.renameElementAtCaret("GETAL")
        assertEquals(1, meldingen.size)
        assertEquals(
            "Renaming NUM also changes calc.l. Rename across grammar and scanner is a Pro feature. Try it free for 30 days.",
            meldingen[0].content,
        )
        assertEquals(0, melding.aantalHints())
    }

    fun testHintZegtWaaromErNietsGebeurde() {
        grammaticaOpen()
        cursorOp("NUM")
        myFixture.renameElementAtCaret("GETAL")
        myFixture.renameElementAtCaret("GETAL")
        assertEquals(1, meldingen.size)
        assertEquals(1, melding.aantalHints())
        assertEquals(0, melding.aantalHintsZonderEditor())
        assertEquals("NUM is also used in calc.l. Rename across grammar and scanner is a Pro feature.", melding.laatsteHint())
        assertEquals(tekst("calc.y"), inhoud("calc.y"))
        assertEquals(tekst("calc.l"), inhoud("calc.l"))
    }

    fun testZonderEditorHintInDeStatusbalk() {
        val f = grammaticaOpen()
        val num = definitie(f, "NUM")
        // Zoals de structuurweergave: hernoemen zonder editor.
        assertNull(ProHernoemen().substituteElementToRename(num, null))
        assertEquals(1, meldingen.size)
        assertNull(ProHernoemen().substituteElementToRename(num, null))
        assertEquals(1, meldingen.size)
        assertEquals(1, melding.aantalHints())
        assertEquals(1, melding.aantalHintsZonderEditor())
        assertEquals("NUM is also used in calc.l. Rename across grammar and scanner is a Pro feature.", melding.laatsteHint())
    }

    fun testTijdensIndexerenGeenProMeldingEnNietHalf() {
        val f = grammaticaOpen()
        val num = definitie(f, "NUM")
        val exp = definitie(f, "exp")
        DumbModeTestUtils.runInDumbModeSynchronously(project) {
            assertEquals(Koppeling.ScannerGebruik.Indexeren, Koppeling.scannerGebruik(num))
            assertNull(ProHernoemen().substituteElementToRename(num, myFixture.editor))
            // Ook met licentie niet: de verwijzingen uit de scanner zijn nu niet te vinden.
            stand(LicentieStand.GELDIG)
            assertNull(ProHernoemen().substituteElementToRename(num, myFixture.editor))
            // Een regel staat nooit in een scanner: die mag gewoon.
            assertSame(exp, ProHernoemen().substituteElementToRename(exp, myFixture.editor))
        }
        assertEquals(0, meldingen.size)
        assertFalse(melding.isGetoond())
        assertEquals(2, melding.aantalHints())
        assertEquals(ProMelding.HINT_INDEXEREN, melding.laatsteHint())
        // Na het indexeren weer de gewone Pro-regel.
        stand(LicentieStand.GEEN)
        assertEquals(listOf("calc.l"), (Koppeling.scannerGebruik(num) as Koppeling.ScannerGebruik.Ja).scanners.map { it.name })
    }

    fun testEigenVlagPerActie() {
        grammaticaOpen()
        // Eerst de ga-naar-balloon (zoals na Ctrl+B in calc.l).
        assertTrue(melding.toonEenmaal(project))
        assertTrue(melding.isGetoondVoor(ProMelding.GA_NAAR))
        assertFalse(melding.isGetoondVoor(ProMelding.HERNOEMEN))
        cursorOp("NUM")
        myFixture.renameElementAtCaret("GETAL")
        assertEquals(2, meldingen.size)
        assertEquals(ProMelding.TEKST, meldingen[0].content)
        assertTrue(meldingen[1].content.startsWith("Renaming NUM also changes calc.l."))
        assertTrue(melding.isGetoondVoor(ProMelding.HERNOEMEN))
        assertEquals(0, melding.aantalHints())
        // En de ga-naar-vlag blijft: geen tweede ga-naar-balloon.
        assertFalse(melding.toonEenmaal(project))
    }

    private fun scannerOpen(): ProHernoemenScanner {
        stand(LicentieStand.GEEN)
        myFixture.addFileToProject("calc.y", tekst("calc.y"))
        myFixture.configureByText("calc.l", tekst("calc.l"))
        cursorOp("NUM")
        return ProHernoemenScanner()
    }

    private fun context() = SimpleDataContext.builder()
        .add(CommonDataKeys.PROJECT, project)
        .add(CommonDataKeys.EDITOR, myFixture.editor)
        .add(CommonDataKeys.PSI_FILE, myFixture.file)
        .build()

    fun testShiftF6InScannerGeeftMeldingGeenFout() {
        scannerOpen()
        // De echte actie: een IDE-fout ("Cannot perform refactoring") gooit in tests een RefactoringErrorHintException.
        myFixture.performEditorAction("RenameElement")
        assertEquals(1, meldingen.size)
        assertEquals(
            "Renaming NUM also changes calc.y. Rename across grammar and scanner is a Pro feature. Try it free for 30 days.",
            meldingen[0].content,
        )
        myFixture.performEditorAction("RenameElement")
        assertEquals(1, meldingen.size)
        assertEquals("NUM is also used in calc.y. Rename across grammar and scanner is a Pro feature.", melding.laatsteHint())
        assertEquals(tekst("calc.l"), myFixture.editor.document.text)
        assertEquals(tekst("calc.y"), inhoud("calc.y"))
    }

    fun testScannerHandlerAlleenZonderLicentieEnBijEenToken() {
        val h = scannerOpen()
        assertTrue(h.isAvailableOnDataContext(context()))
        // yytext is geen token van de grammatica: dan beslist de IDE zelf.
        cursorOp("yytext")
        assertFalse(h.isAvailableOnDataContext(context()))
        cursorOp("NUM")
        stand(LicentieStand.GELDIG)
        assertFalse(h.isAvailableOnDataContext(context()))
        DumbModeTestUtils.runInDumbModeSynchronously(project) {
            assertTrue(h.isAvailableOnDataContext(context()))
            h.invoke(project, myFixture.editor, myFixture.file, context())
        }
        assertEquals(0, meldingen.size)
        assertEquals(ProMelding.HINT_INDEXEREN, melding.laatsteHint())
    }
}
