package com.dortus.bisonflex

import com.dortus.bisonflex.parser.BisonElementen
import com.dortus.bisonflex.pro.GaNaarDefinitie
import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.dortus.bisonflex.pro.ProMelding
import com.intellij.lang.folding.LanguageFolding
import com.intellij.notification.Notification
import com.intellij.notification.Notifications
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiFile
import com.intellij.testFramework.PlatformTestUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/**
 * Eis 8 (licentie en Pro-melding) en eis 6 (ga naar definitie, eerste deel), met een nagebootste licentie.
 * De rekenmachine uit `e2e/project/` als testbestand.
 */
class ProTest : BasePlatformTestCase() {

    private val meldingen = ArrayList<Notification>()
    private val project get() = File(System.getProperty("dortus.testdata")).parentFile.resolve("e2e/project")

    override fun setUp() {
        super.setUp()
        ProMelding.getInstance().opnieuwVoorTest()
        meldingen.clear()
        getProject().messageBus.connect(testRootDisposable).subscribe(Notifications.TOPIC, object : Notifications {
            override fun notify(notification: Notification) {
                if (notification.groupId == ProMelding.GROEP) meldingen += notification
            }
        })
    }

    override fun tearDown() {
        try {
            Licentie.zetBronVoorTest(null)
            ProMelding.getInstance().opnieuwVoorTest()
        } finally {
            super.tearDown()
        }
    }

    private fun stand(s: LicentieStand) = Licentie.zetBronVoorTest { s }

    private fun open(naam: String): PsiFile = myFixture.configureByText(naam, File(project, naam).readText())

    /**
     * Ga naar definitie op het [n]-de voorkomen (vanaf 0) van [tekst], met de cursor in het midden van het woord,
     * zoals bij een echte ga-naar-actie (Ctrl+B). Zweven zonder actie staat in ProZwevenTest en GaNaarActieTest.
     */
    private fun gaNaar(tekst: String, n: Int = 0): List<PsiElement> {
        val inhoud = myFixture.editor.document.text
        var plek = -1
        repeat(n + 1) { plek = inhoud.indexOf(tekst, plek + 1) }
        assertTrue("'$tekst' (#$n) niet gevonden", plek >= 0)
        val offset = plek + tekst.length / 2
        val blad = myFixture.file.findElementAt(offset)
        return GaNaarDefinitie { true }.getGotoDeclarationTargets(blad, offset, myFixture.editor)?.toList() ?: emptyList()
    }

    /** Korte vorm van een doel: type, tekst en regel (vanaf 1). */
    private fun doel(e: PsiElement): String {
        val d = e.containingFile.viewProvider.document!!
        return "${e.containingFile.name}:${d.getLineNumber(e.textOffset) + 1} ${e.node.elementType} ${e.text}"
    }

    // ---- stand GEEN ----

    fun testGeenLicentieBinnenBestandSpringtZonderMelding() {
        stand(LicentieStand.GEEN)
        assertFalse(Licentie.proWerkt())
        val f = open("calc.y")
        // Gratis deel werkt gewoon: parser zonder fouten, regels in de boom, folding.
        assertNull(com.intellij.psi.util.PsiTreeUtil.findChildOfType(f, com.intellij.psi.PsiErrorElement::class.java))
        assertTrue(f.node.findChildByType(BisonElementen.RULES) != null)
        val bouwer = LanguageFolding.INSTANCE.forLanguage(f.language)
        assertTrue(LanguageFolding.buildFoldingDescriptors(bouwer, f, myFixture.editor.document, false).isNotEmpty())
        // Twee pogingen binnen hetzelfde bestand: dat is gratis, dus wel een sprong en geen melding.
        assertEquals(listOf("calc.y:25 RULE_NAME exp"), gaNaar("exp", 0).map(::doel))
        assertEquals(listOf("calc.y:9 TOKEN_NAME NUM"), gaNaar("NUM", 1).map(::doel))
        assertEquals(0, meldingen.size)
    }

    fun testGeenLicentieOokInFlexEenmaal() {
        stand(LicentieStand.GEEN)
        myFixture.addFileToProject("calc.y", File(project, "calc.y").readText())
        open("calc.l")
        assertEquals(emptyList<PsiElement>(), gaNaar("NUM"))
        myFixture.configureFromTempProjectFile("calc.y")
        assertEquals(listOf("calc.y:25 RULE_NAME exp"), gaNaar("exp", 2).map(::doel))
        assertEquals(1, meldingen.size)
    }

    // ---- stand GEEN: binnen hetzelfde bestand gratis ----

    fun testGeenSpringtBinnenBestandNaarRegel() {
        stand(LicentieStand.GEEN)
        open("calc.y")
        assertEquals(listOf("calc.y:20 RULE_NAME line"), gaNaar("line", 0).map(::doel))
        assertEquals(0, meldingen.size)
        assertFalse(ProMelding.getInstance().isGetoond())
    }

    fun testGeenSpringtBinnenBestandNaarToken() {
        stand(LicentieStand.GEEN)
        open("calc.y")
        assertEquals(listOf("calc.y:9 TOKEN_NAME NUM"), gaNaar("NUM", 1).map(::doel))
        assertEquals(0, meldingen.size)
    }

    fun testGeenSpringtBinnenBestandStartConditie() {
        stand(LicentieStand.GEEN)
        myFixture.configureByText("sc.l", START_CONDITIES)
        assertEquals(listOf("sc.l:1 START_CONDITION_NAME COMMENT"), gaNaar("COMMENT", 2).map(::doel))
        assertEquals(listOf("sc.l:1 START_CONDITION_NAME STR"), gaNaar("STR", 1).map(::doel))
        assertEquals(0, meldingen.size)
    }

    // ---- stand GEEN: tussen bestanden is Pro ----

    fun testGeenTussenBestandenMeldingEenmaalDaarnaHint() {
        stand(LicentieStand.GEEN)
        myFixture.addFileToProject("calc.y", File(project, "calc.y").readText())
        open("calc.l")
        // Eerste klik: geen sprong, de balloon, geen hint.
        assertEquals(emptyList<PsiElement>(), gaNaar("NUM"))
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertEquals(1, meldingen.size)
        val m = meldingen.single()
        assertEquals("Bison & Flex Pro", m.title)
        assertEquals(ProMelding.TEKST, m.content)
        assertEquals(listOf("Start free trial", "Not now"), m.actions.map { it.templateText })
        assertEquals(0, ProMelding.getInstance().aantalHints())
        // Tweede en derde klik: geen sprong, geen tweede balloon, wel elke keer de korte hint.
        assertEquals(emptyList<PsiElement>(), gaNaar("NUM"))
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertEquals(emptyList<PsiElement>(), gaNaar("NUM"))
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertEquals(1, meldingen.size)
        assertEquals(2, ProMelding.getInstance().aantalHints())
    }

    fun testGeenMeldingAlsErGeenDoelIs() {
        stand(LicentieStand.GEEN)
        open("calc.y")
        assertEquals(emptyList<PsiElement>(), gaNaar("printf"))
        assertEquals(0, meldingen.size)
    }

    // ---- stand GELDIG ----

    fun testGeldigSpringtNaarRegel() {
        stand(LicentieStand.GELDIG)
        open("calc.y")
        // `input line` (regel 17) naar `line:` (regel 20), `exp '\\n'` (regel 22) naar `exp:` (regel 25).
        assertEquals(listOf("calc.y:20 RULE_NAME line"), gaNaar("line", 0).map(::doel))
        assertEquals(listOf("calc.y:25 RULE_NAME exp"), gaNaar("exp", 0).map(::doel))
        assertEquals(0, meldingen.size)
    }

    fun testGeldigSpringtNaarToken() {
        stand(LicentieStand.GELDIG)
        open("calc.y")
        assertEquals(listOf("calc.y:9 TOKEN_NAME NUM"), gaNaar("NUM", 1).map(::doel))
        assertEquals(0, meldingen.size)
    }

    fun testGeldigVanScannerNaarGrammatica() {
        stand(LicentieStand.GELDIG)
        myFixture.addFileToProject("calc.y", File(project, "calc.y").readText())
        open("calc.l")
        assertEquals(listOf("calc.y:9 TOKEN_NAME NUM"), gaNaar("NUM").map(::doel))
        assertEquals(0, meldingen.size)
    }

    fun testGeldigStartConditie() {
        stand(LicentieStand.GELDIG)
        val f = myFixture.configureByText("sc.l", START_CONDITIES)
        assertNull(com.intellij.psi.util.PsiTreeUtil.findChildOfType(f, com.intellij.psi.PsiErrorElement::class.java))
        assertEquals(listOf("sc.l:1 START_CONDITION_NAME COMMENT"), gaNaar("COMMENT", 2).map(::doel))
        assertEquals(listOf("sc.l:1 START_CONDITION_NAME STR"), gaNaar("STR", 1).map(::doel))
        assertEquals(0, meldingen.size)
    }

    fun testGeenDoelOpDefinitieZelf() {
        stand(LicentieStand.GELDIG)
        open("calc.y")
        // De cursor op `exp:` zelf (een RULE_NAME, geen SYMBOL_REF): geen sprong van ons.
        assertEquals(emptyList<PsiElement>(), gaNaar("exp:"))
    }

    // ---- stand ONBEKEND ----

    fun testOnbekendSpringtZonderMelding() {
        stand(LicentieStand.ONBEKEND)
        assertTrue(Licentie.proWerkt())
        myFixture.addFileToProject("calc.y", File(project, "calc.y").readText())
        myFixture.configureFromTempProjectFile("calc.y")
        assertEquals(listOf("calc.y:25 RULE_NAME exp"), gaNaar("exp", 0).map(::doel))
        open("calc.l")
        assertEquals(listOf("calc.y:9 TOKEN_NAME NUM"), gaNaar("NUM").map(::doel))
        assertEquals(0, meldingen.size)
    }

    fun testEchteBronGeeftInTestGeenGeldig() {
        // Zonder nagebootste bron: in de testomgeving is er geen stempel; de stand is ONBEKEND of GEEN, nooit GELDIG.
        Licentie.zetBronVoorTest(null)
        assertTrue(Licentie.stand() != LicentieStand.GELDIG)
    }

    private companion object {
        const val START_CONDITIES =
            "%x COMMENT STR\n%%\n\"/*\"  BEGIN(COMMENT);\n<COMMENT>\"*/\"  BEGIN(INITIAL);\n<STR,COMMENT>.  ;\n%%\n"
    }
}
