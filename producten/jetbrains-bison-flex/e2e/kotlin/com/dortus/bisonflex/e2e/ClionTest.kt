package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.driver.client.Remote
import com.intellij.driver.client.service
import com.intellij.driver.client.utility
import com.intellij.driver.model.LockSemantics
import com.intellij.driver.model.OnDispatcher
import com.intellij.driver.sdk.Editor
import com.intellij.driver.sdk.FileEditorManager
import com.intellij.driver.sdk.getEnabledPlugins
import com.intellij.driver.sdk.getHighlights
import com.intellij.driver.sdk.getToolWindow
import com.intellij.driver.sdk.getPlugin
import com.intellij.driver.sdk.openFile
import com.intellij.driver.sdk.openToolWindow
import com.intellij.driver.sdk.PsiFile
import com.intellij.driver.sdk.PsiManager
import com.intellij.driver.sdk.Project
import com.intellij.driver.sdk.singleProject
import com.intellij.driver.sdk.VirtualFile
import com.intellij.driver.sdk.waitForCodeAnalysis
import com.intellij.driver.sdk.waitForIndicators
import com.intellij.ide.starter.driver.engine.runIdeWithDriver
import com.intellij.ide.starter.ide.IdeProductProvider
import com.intellij.ide.starter.models.TestCase
import com.intellij.ide.starter.project.LocalProjectInfo
import com.intellij.ide.starter.runner.Starter
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.fail
import kotlin.time.Duration.Companion.minutes

/*
 * De structuurweergave via het model van de plugin (BisonStructuur, zoals de IDE hem vraagt). De weg via
 * StructureViewWrapperImpl uit StructuurEnZweven.kt bestaat in 263 niet meer (run 42442619271).
 */
@Remote("com.dortus.bisonflex.BisonStructuur", plugin = "com.dortus.bisonflex")
interface BisonStructuurOpAfstand {
    fun getStructureViewBuilder(psiFile: PsiFile): StructuurBouwerOpAfstand
}

@Remote("com.intellij.ide.structureView.TreeBasedStructureViewBuilder")
interface StructuurBouwerOpAfstand {
    fun createStructureViewModel(editor: Editor?): StructuurModelOpAfstand
}

@Remote("com.intellij.ide.structureView.StructureViewModel")
interface StructuurModelOpAfstand {
    fun getRoot(): StructuurElementOpAfstand
}

@Remote("com.intellij.ide.util.treeView.smartTree.TreeElement")
interface StructuurElementOpAfstand {
    fun getChildren(): Array<StructuurElementOpAfstand>
    fun getPresentation(): PresentatieOpAfstand
}

@Remote("com.intellij.navigation.ItemPresentation")
interface PresentatieOpAfstand {
    fun getPresentableText(): String?
}

/** Thema van de IDE, om in het log te zetten welk thema echt actief is (en zo nodig te wisselen). */
@Remote("com.intellij.ide.ui.LafManager")
interface LafManagerOpAfstand {
    fun getCurrentUIThemeLookAndFeel(): ThemaOpAfstand?
    fun findLaf(themeId: String): ThemaOpAfstand?
    fun setCurrentLookAndFeel(info: ThemaOpAfstand, lockEditorScheme: Boolean)
    fun updateUI()
    fun getAutodetect(): Boolean
}

@Remote("com.intellij.ide.ui.laf.UIThemeLookAndFeelInfo")
interface ThemaOpAfstand {
    fun getId(): String
    fun getName(): String
    fun isDark(): Boolean
}

@Remote("com.intellij.openapi.editor.colors.EditorColorsManager")
interface KleurenOpAfstand {
    fun getGlobalScheme(): KleurenschemaOpAfstand
    fun getScheme(name: String): KleurenschemaOpAfstand?
    fun setGlobalScheme(scheme: KleurenschemaOpAfstand?)
}

@Remote("com.intellij.openapi.editor.colors.EditorColorsScheme")
interface KleurenschemaOpAfstand {
    fun getName(): String
}

@Remote("com.intellij.openapi.wm.WindowManager")
interface WindowManagerOpAfstand {
    fun getStatusBar(project: Project): StatusBalkOpAfstand?
}

@Remote("com.intellij.openapi.wm.StatusBar")
interface StatusBalkOpAfstand {
    fun getWidget(id: String): StatusBalkOnderdeelOpAfstand?
}

@Remote("com.intellij.openapi.wm.StatusBarWidget")
interface StatusBalkOnderdeelOpAfstand {
    fun ID(): String
}

@Remote("com.intellij.openapi.util.registry.Registry")
interface RegistryOpAfstand {
    fun `is`(key: String): Boolean
}

/**
 * Eis 1 in de echte CLion (de doelgroep van de plugin), los van IdeTest: een eigen Gradle-taak `clionTest`.
 * Gebruikt een RC- of EAP-build van CLion, want die heeft een ingebouwde tijdelijke licentie (±30 dagen na de
 * builddatum). De release (2026.3, 263.7307.209, 5 nov) vraagt een licentie of inlog en kan hier dus niet.
 * Starter weigert alleen een verlopen EAP zelf; bij een verlopen RC verschijnt het licentievenster en faalt de test
 * met die reden. Verlopen: kies de nieuwste RC of EAP (data.services.jetbrains.com/products/releases?code=CL&type=rc,eap)
 * en pas [CLION_BUILD] en [CLION_SOORT] aan.
 * Verschijnt er toch een licentie- of voorwaardenvenster, dan klikt de test niets weg: schermafbeelding, titel in
 * het log, en de test faalt met die reden.
 */
class ClionTest {
    companion object {
        /** CLion 2026.3 RC van 30 okt 2026, geldig tot ongeveer 29 nov 2026 (was EAP 263.7307.35, tot ±22 nov). */
        const val CLION_BUILD = "263.7307.108"
        /** "rc" of "eap", zoals het veld `type` in de releases-API van JetBrains. */
        const val CLION_SOORT = "rc"
        private const val PLUGIN_ID = "com.dortus.bisonflex"
        private val VERDACHT = Regex("licen|activat|agreement|terms|eula|register|subscription|trial|log ?in|sign ?in|evaluat|privacy|data sharing|expired", RegexOption.IGNORE_CASE)
    }

    /** Hulpfuncties (schermafbeelding, pauze, wachten) en de CIServer-instelling staan in Gedeeld.kt. */
    init { zetCiServer() }

    /*
     * Thema-ids van 263: "Islands Light" en "Islands Dark" (intellij-community, intellij.platform.ide.impl.xml:
     * themeProvider id="Islands Dark" path="/themes/islands/ManyIslandsDark.theme.json"). Het editorschema van
     * Islands Dark heet ook "Islands Dark" (themes/islands/IslandSchemeDark.xml). Met ExperimentalDark bleven beide
     * CLion-schermen licht (run 42443828755).
     */
    @Test
    fun lichtThema() = draai("licht", "Islands Light", "Light", donker = false)

    @Test
    fun donkerThema() = draai("donker", "Islands Dark", "Islands Dark", donker = true)

    /** useEAP(build) zoekt alleen in type "eap"; voor een RC zet useRC() de soort en vullen we het buildnummer zelf in. */
    private fun clionTestCase(project: java.nio.file.Path) = TestCase(IdeProductProvider.CL, LocalProjectInfo(project)).let { tc ->
        if (CLION_SOORT == "eap") tc.useEAP(CLION_BUILD)
        else tc.useRC().let { it.copy(ideInfo = it.ideInfo.copy(buildNumber = CLION_BUILD)) }
    }

    private fun draai(naam: String, themaId: String, kleurenschema: String, donker: Boolean) {
        val project = winkelproject("clion-$naam")
        val wachter = Vensterwachter(naam).also { it.start() }
        try {
            Starter.newContext("clion-$naam", clionTestCase(project))
                .apply {
                    richIn(themaId, kleurenschema) {
                        // "Cannot update plugin: Unable to identify where ... was installed from" komt van
                        // PluginsMissingUpdateSourceNotifier (PluginUpdateSourceInitializationActivity.kt): elke plugin zonder
                        // vastgelegde bron (Marketplace of eigen repository) krijgt die melding. Starter pakt de zip zelf uit in
                        // de plugins-map, dus er is geen bron. Alleen in deze test-IDE: die functie uit (registry-sleutel).
                        addSystemProperty("platform.enable.plugin.update.source.feature", false)
                    }
                }
                .runIdeWithDriver()
                .useDriverAndCloseIde {
                    try {
                        controleer(naam, wachter, themaId, kleurenschema, donker)
                    } catch (e: Throwable) {
                        wachter.reden?.let { fail("CLion [$naam] toont een licentie- of voorwaardenvenster: $it", e) }
                        throw e
                    }
                }
        } catch (e: Throwable) {
            wachter.reden?.let { if (e !is AssertionError) fail("CLion [$naam] toont een licentie- of voorwaardenvenster: $it", e) }
            throw e
        } finally {
            wachter.klaar()
        }
    }

    private fun Driver.controleer(naam: String, wachter: Vensterwachter, themaId: String, kleurenschema: String, donker: Boolean) {
        waitForIndicators(5.minutes)
        wachter.reden?.let { fail("CLion [$naam] toont een licentie- of voorwaardenvenster: $it") }

        sluitWizard(naam)
        thema(naam, themaId, kleurenschema, donker)
        val bronFunctie = utility<RegistryOpAfstand>().`is`("platform.enable.plugin.update.source.feature")
        println("DORTUS-E2E [clion-$naam] registry platform.enable.plugin.update.source.feature: $bronFunctie (false = geen melding over de updatebron)")
        assertTrue(!bronFunctie, "functie updatebron van plugins uit in de test-IDE ($naam)")
        // getEnabledPluginsIds() van de Driver telt alleen ingebouwde plugins (run 42441271116), dus zelf zoeken.
        val aan = getEnabledPlugins()
        val geladen = aan.any { it.getPluginId().getIdString() == PLUGIN_ID }
        val plugin = getPlugin(PLUGIN_ID)
        println("DORTUS-E2E [clion-$naam] plugin $PLUGIN_ID in geladen plugins: $geladen, naam '${plugin?.getName()}', aan ${plugin?.isEnabled()}, plugins aan ${aan.size}")
        assertTrue(geladen && plugin?.isEnabled() == true, "plugin staat in de geladen plugins van CLion ($naam)")

        val ftm = service<FileTypeManagerOpAfstand>()
        for ((bestand, soort) in listOf("calc.y" to "Bison", "calc.l" to "Flex")) {
            val gevonden = ftm.getFileTypeByFileName(bestand).getName()
            println("DORTUS-E2E [clion-$naam] $bestand -> soort $gevonden")
            assertEquals(soort, gevonden, "soort van $bestand in CLion ($naam)")
        }

        openFile("calc.l")
        pauze()
        openFile("calc.y")
        pauze()
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor() ?: fail("geen editor voor calc.y ($naam)")
        val bestand = editor.getVirtualFile()
        println("DORTUS-E2E [clion-$naam] open editor: ${bestand.getName()}")
        waitForCodeAnalysis(singleProject(), bestand, 2.minutes)
        val fouten = getHighlights(editor.getDocument()).filter { it.getSeverity().getName() == "ERROR" }
        println("DORTUS-E2E [clion-$naam] rode fouten in calc.y: ${fouten.size} ${fouten.take(5).map { "'${it.getText()}': ${it.getDescription()}" }}")
        assertEquals(0, fouten.size, "geen rode syntaxfouten in calc.y ($naam)")

        openToolWindow("Structure")
        pauze()
        val zichtbaar = getToolWindow("Structure").isVisible()
        val regels = structuurRegels(bestand, editor)
        println("DORTUS-E2E [clion-$naam] Structure-venster zichtbaar: $zichtbaar, structuur calc.y: ${regels.size} regels ${regels.take(10)}")
        assertTrue(zichtbaar, "Structure-venster zichtbaar ($naam)")
        assertTrue(regels.size > 1, "structuurweergave toont regels van calc.y ($naam)")
        pauze()
        wachter.reden?.let { fail("CLion [$naam] toont een licentie- of voorwaardenvenster: $it") }
        val meter = service<WindowManagerOpAfstand>().getStatusBar(singleProject())?.getWidget("Memory")
        println("DORTUS-E2E [clion-$naam] geheugenmeter in de statusbalk: ${meter != null}")
        assertTrue(meter == null, "geen geheugenmeter in de statusbalk ($naam)")
        scherm("clion-$naam-calc-y.png")
    }

    /**
     * Zet in het log welk thema en editorschema CLion uit de config heeft geladen. Klopt dat niet met [themaId], dan
     * wisselt de test via LafManager (zoals Settings dat doet) en zegt dat in het log. Daarna moet het thema bij
     * [donker] passen, anders faalt de test.
     */
    private fun Driver.thema(naam: String, themaId: String, kleurenschema: String, donker: Boolean) {
        val laf = service<LafManagerOpAfstand>()
        val kleuren = service<KleurenOpAfstand>()
        val geladen = laf.getCurrentUIThemeLookAndFeel()
        println("DORTUS-E2E [clion-$naam] thema uit de config: id '${geladen?.getId()}', naam '${geladen?.getName()}', donker ${geladen?.isDark()}, autodetect ${laf.getAutodetect()}, editorschema '${kleuren.getGlobalScheme().getName()}' (gevraagd '$themaId', '$kleurenschema')")
        if (geladen?.getId() != themaId) {
            withContext(OnDispatcher.EDT) {
                val gewenst = laf.findLaf(themaId) ?: fail("thema '$themaId' bestaat niet in CLion ($naam)")
                laf.setCurrentLookAndFeel(gewenst, true)
                laf.updateUI()
            }
            println("DORTUS-E2E [clion-$naam] thema uit de config klopte niet, gewisseld via LafManager naar '$themaId'")
        }
        if (!zelfdeSchema(kleuren.getGlobalScheme().getName(), kleurenschema)) {
            withContext(OnDispatcher.EDT) { kleuren.setGlobalScheme(kleuren.getScheme(kleurenschema) ?: fail("editorschema '$kleurenschema' bestaat niet ($naam)")) }
            println("DORTUS-E2E [clion-$naam] editorschema gewisseld naar '$kleurenschema'")
        }
        pauze()
        val nu = laf.getCurrentUIThemeLookAndFeel()
        val schema = kleuren.getGlobalScheme().getName()
        println("DORTUS-E2E [clion-$naam] actief thema: id '${nu?.getId()}', naam '${nu?.getName()}', donker ${nu?.isDark()}, editorschema '$schema'")
        assertEquals(donker, nu?.isDark(), "thema van CLion is ${if (donker) "donker" else "licht"} ($naam)")
        assertTrue(zelfdeSchema(schema, kleurenschema), "editorschema van CLion is '$kleurenschema' (of de eigen kopie ervan), niet '$schema' ($naam)")
    }

    /** De IDE werkt met een eigen kopie van het schema, met het voorvoegsel `_@user_` (run 42449362463: '_@user_Islands Dark'). */
    private fun zelfdeSchema(schema: String, gevraagd: String) = schema == gevraagd || schema == "_@user_$gevraagd"

    /**
     * CLion opent een map zonder CMakeLists.txt met de "Open Project Wizard" (CMake-profielen, run 42441271116).
     * Dat is geen licentie of voorwaarden: Escape sluit hem zonder CMake-model, zoals een gebruiker met Cancel.
     */
    private fun sluitWizard(naam: String) {
        val wizard = vensters().firstOrNull { it.second == "Open Project Wizard" } ?: return
        ProcessBuilder("xdotool", "windowactivate", "--sync", wizard.first).inheritIO().start().waitFor()
        Thread.sleep(1_000)
        toets("Escape")
        val weg = wacht(15) { vensters().none { it.second == "Open Project Wizard" } }
        println("DORTUS-E2E [clion-$naam] Open Project Wizard met Escape gesloten: $weg")
        assertTrue(weg, "Open Project Wizard dicht ($naam)")
    }

    /** Knopen van de structuur van calc.y (twee niveaus diep), via het model van de plugin, in een read-action. */
    private fun Driver.structuurRegels(bestand: VirtualFile, editor: Editor): List<String> =
        withContext(OnDispatcher.DEFAULT, LockSemantics.READ_ACTION) {
            val psi = service<PsiManager>(singleProject()).findFile(bestand) ?: return@withContext emptyList<String>()
            val wortel = new(BisonStructuurOpAfstand::class).getStructureViewBuilder(psi).createStructureViewModel(editor).getRoot()
            wortel.getChildren().flatMap { kop ->
                listOf(kop.getPresentation().getPresentableText() ?: "?") +
                    kop.getChildren().map { "  " + (it.getPresentation().getPresentableText() ?: "?") }
            }
        }

    /**
     * Kijkt elke 3 seconden welke vensters er zichtbaar zijn (xdotool) en zet nieuwe titels in het log. Heeft een
     * venster een titel die op een licentie, inlog of voorwaarden lijkt: schermafbeelding van dat venster en de reden
     * bewaren. Er wordt niets aangeklikt.
     */
    private inner class Vensterwachter(private val naam: String) : Thread("vensterwachter-$naam") {
        @Volatile var reden: String? = null
        @Volatile private var door = true
        private val gezien = mutableSetOf<String>()

        init { isDaemon = true }

        override fun run() {
            while (door) {
                for ((id, titel) in vensters()) {
                    if (gezien.add("$id $titel")) println("DORTUS-E2E [clion-$naam] venster $id: '$titel'")
                    if (reden == null && VERDACHT.containsMatchIn(titel)) {
                        val doel = schermen.resolve("clion-$naam-licentievenster.png")
                        val code = ProcessBuilder("import", "-window", id, doel.toString()).inheritIO().start().waitFor()
                        reden = "venster '$titel' (schermafbeelding ${doel.fileName}, code $code)"
                        println("DORTUS-E2E [clion-$naam] LICENTIE/VOORWAARDEN: $reden")
                    }
                }
                try { sleep(3_000) } catch (e: InterruptedException) { return }
            }
        }

        fun klaar() { door = false; interrupt() }
    }
}
