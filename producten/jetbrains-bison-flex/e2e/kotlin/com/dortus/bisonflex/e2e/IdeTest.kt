package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.driver.client.Remote
import com.intellij.driver.client.service
import com.intellij.driver.sdk.openFile
import com.intellij.driver.sdk.waitForIndicators
import com.intellij.ide.starter.ci.CIServer
import com.intellij.ide.starter.ci.NoCIServer
import com.intellij.ide.starter.di.di
import com.intellij.ide.starter.driver.engine.runIdeWithDriver
import com.intellij.ide.starter.ide.IdeProductProvider
import com.intellij.ide.starter.models.TestCase
import com.intellij.ide.starter.plugins.PluginConfigurator
import com.intellij.ide.starter.project.LocalProjectInfo
import com.intellij.ide.starter.runner.Starter
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.fail
import org.kodein.di.DI
import org.kodein.di.bindSingleton
import java.nio.file.Files
import java.nio.file.Path
import kotlin.io.path.createDirectories
import kotlin.io.path.writeText
import kotlin.time.Duration.Companion.minutes

@Remote("com.intellij.openapi.fileTypes.FileTypeManager")
interface FileTypeManagerOpAfstand {
    fun getFileTypeByFileName(fileName: String): FileTypeOpAfstand
}

@Remote("com.intellij.openapi.fileTypes.FileType")
interface FileTypeOpAfstand {
    fun getName(): String
    fun getIcon(): IcoonOpAfstand?
}

@Remote("javax.swing.Icon")
interface IcoonOpAfstand {
    fun getIconWidth(): Int
}

/**
 * Test in de echte IDE (IDEA Community 2025.2) op GitHub Actions.
 * Eis 1 en eis 10 (eerste deel) uit ontwerp.md: bestandssoorten herkend, schermen licht en donker.
 */
class IdeTest {
    companion object {
        /** Vast, zodat de test niet stilletjes naar een nieuwere IDE schuift (build 252.28539.149). */
        const val IDE_VERSIE = "2025.2.6.4"
    }

    init {
        di = DI {
            extend(di)
            bindSingleton<CIServer>(overrides = true) {
                object : CIServer by NoCIServer {
                    override fun reportTestFailure(testName: String, message: String, details: String, linkToLogs: String?) {
                        fail { "$testName faalt: $message\n$details" }
                    }
                }
            }
        }
    }

    private val schermen: Path = Path.of(System.getProperty("dortus.e2e.screenshots")).also { it.createDirectories() }

    @Test
    fun lichtThema() = draai("licht", "ExperimentalLight", "Light")

    @Test
    fun donkerThema() = draai("donker", "ExperimentalDark", "Dark")

    private fun draai(naam: String, themaId: String, kleurenschema: String) {
        val project = Files.createTempDirectory("bisonflex-$naam")
        Path.of(System.getProperty("dortus.e2e.project")).toFile().copyRecursively(project.toFile())

        Starter.newContext("bisonflex-$naam", TestCase(IdeProductProvider.IC, LocalProjectInfo(project)).useRelease(IDE_VERSIE))
            .apply {
                PluginConfigurator(this).installPluginFromPath(Path.of(System.getProperty("path.to.build.plugin")))
                // Thema vooraf vastzetten (GOK: zo werkt het in een verse config, de schermen laten het zien).
                val opties = paths.configDir.resolve("options").createDirectories()
                opties.resolve("laf.xml").writeText(
                    """<application><component name="LafManager" autodetect="false"><laf themeId="$themaId"/></component></application>"""
                )
                opties.resolve("colors.scheme.xml").writeText(
                    """<application><component name="EditorColorsManagerImpl"><global_color_scheme name="$kleurenschema"/></component></application>"""
                )
                applyVMOptionsPatch {
                    addSystemProperty("idea.trust.all.projects", true)
                    addSystemProperty("ide.show.tips.on.startup.default.value", false)
                }
            }
            .runIdeWithDriver()
            .useDriverAndCloseIde {
                waitForIndicators(5.minutes)
                val ftm = service<FileTypeManagerOpAfstand>()
                for ((bestand, soort) in listOf("calc.y" to "Bison", "calc.yy" to "Bison", "calc.l" to "Flex", "calc.ll" to "Flex")) {
                    val ft = ftm.getFileTypeByFileName(bestand)
                    val gevonden = ft.getName()
                    val breedte = ft.getIcon()?.getIconWidth() ?: 0
                    val icoon = breedte == 16
                    println("DORTUS-E2E [$naam] $bestand -> soort $gevonden, icoon $breedte px")
                    assertEquals(soort, gevonden, "soort van $bestand")
                    assertTrue(icoon, "icoon van $bestand")
                }
                openFile("calc.y")
                pauze()
                scherm("$naam-calc-y.png")
                openFile("calc.l")
                pauze()
                scherm("$naam-calc-l.png")
            }
    }

    private fun Driver.pauze() = Thread.sleep(3_000)

    /** Schermafbeelding van het hele (virtuele) scherm met ImageMagick. */
    private fun scherm(bestand: String) {
        val doel = schermen.resolve(bestand)
        val p = ProcessBuilder("import", "-window", "root", doel.toString()).inheritIO().start()
        val code = p.waitFor()
        val grootte = if (Files.exists(doel)) Files.size(doel) else 0
        println("DORTUS-E2E schermafbeelding $bestand: code $code, $grootte bytes")
        assertEquals(0, code, "import voor $bestand")
        assertTrue(grootte > 10_000, "schermafbeelding $bestand is te klein ($grootte bytes)")
    }
}
