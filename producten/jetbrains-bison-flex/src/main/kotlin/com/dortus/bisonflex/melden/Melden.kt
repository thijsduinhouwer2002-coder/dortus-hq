package com.dortus.bisonflex.melden

import com.intellij.ide.BrowserUtil
import com.intellij.ide.plugins.PluginManagerCore
import com.intellij.openapi.actionSystem.ActionUpdateThread
import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.application.ApplicationInfo
import com.intellij.openapi.extensions.PluginId
import com.intellij.openapi.project.DumbAware
import java.net.URLEncoder
import java.nio.charset.StandardCharsets

/**
 * Roestronde R5: klachten bij ons in plaats van in de reviews. Help, "Report a Problem with Bison & Flex..." opent een
 * nieuwe melding in de loketrepo op GitHub, met de versie van de plugin, de IDE en het besturingssysteem al ingevuld.
 *
 * Alleen een link die de gebruiker zelf opent: er gaat niets vanzelf het netwerk op, geen telemetrie.
 * De URL vult twee dingen: de velden `version`, `ide` en `os` van het meldformulier (`bug.yml` in de loketrepo, ids
 * gelijk aan `producten/jetbrains-bison-flex/loket/.github/ISSUE_TEMPLATE/bug.yml`) en een `body` met dezelfde gegevens.
 * Bewust zonder `template=`: zolang het formulier nog niet in de loketrepo staat, werkt de link dan ook (gewone melding
 * met de body ingevuld).
 */
object Melden {
    const val LOKET = "https://github.com/thijsduinhouwer2002-coder/bison-flex"
    const val PLUGIN_ID = "com.dortus.bisonflex"

    /** De link voor deze IDE. */
    fun urlHier(): String {
        val versie = PluginManagerCore.getPlugin(PluginId.getId(PLUGIN_ID))?.version ?: "unknown"
        val info = ApplicationInfo.getInstance()
        val ide = "${info.fullApplicationName} (${info.build.asString()})"
        return url(versie, ide, systeem())
    }

    /** Besturingssysteem zonder gebruikersnaam of paden, bijvoorbeeld "Linux 6.8.0 (amd64)". */
    fun systeem(): String =
        "${System.getProperty("os.name")} ${System.getProperty("os.version")} (${System.getProperty("os.arch")})"

    fun body(versie: String, ide: String, os: String): String = """
        |**What happened?**
        |
        |
        |**What did you expect?**
        |
        |
        |**Steps to reproduce** (a few lines of the .y or .l file help a lot)
        |
        |
        |---
        |Bison & Flex: $versie
        |IDE: $ide
        |OS: $os
    """.trimMargin()

    fun url(versie: String, ide: String, os: String): String {
        val velden = listOf(
            "version" to versie,
            "ide" to ide,
            "os" to os,
            "body" to body(versie, ide, os),
        )
        return "$LOKET/issues/new?" + velden.joinToString("&") { (k, v) -> "$k=${codeer(v)}" }
    }

    /** Procentcodering met %20 voor een spatie (niet +), zodat elke lezer het hetzelfde leest. */
    fun codeer(tekst: String): String = URLEncoder.encode(tekst, StandardCharsets.UTF_8).replace("+", "%20")
}

/** De menuregel onder Help (plugin.xml, `BisonFlex.ReportProblem`). */
class MeldProbleemActie : AnAction(), DumbAware {
    override fun actionPerformed(e: AnActionEvent) {
        BrowserUtil.browse(Melden.urlHier())
    }

    override fun getActionUpdateThread(): ActionUpdateThread = ActionUpdateThread.BGT
}
