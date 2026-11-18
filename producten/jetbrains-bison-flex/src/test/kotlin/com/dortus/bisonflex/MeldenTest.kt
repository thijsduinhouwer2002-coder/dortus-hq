package com.dortus.bisonflex

import com.dortus.bisonflex.melden.Melden
import com.dortus.bisonflex.melden.MeldProbleemActie
import com.intellij.openapi.actionSystem.ActionManager
import com.intellij.openapi.actionSystem.DefaultActionGroup
import com.intellij.openapi.actionSystem.IdeActions
import com.intellij.openapi.diagnostic.ErrorReportSubmitter
import com.intellij.openapi.extensions.ExtensionPointName
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.net.URI
import java.net.URLDecoder
import java.nio.charset.StandardCharsets

/** Roestronde R5: meldregel onder Help en de error handler van JetBrains Marketplace. */
class MeldenTest : BasePlatformTestCase() {

    private fun velden(url: String): Map<String, String> =
        URI(url).rawQuery.split("&").associate {
            val (k, v) = it.split("=", limit = 2)
            k to URLDecoder.decode(v, StandardCharsets.UTF_8)
        }

    fun testUrlVultVersieIdeEnSysteem() {
        val url = Melden.url("2026.1.3", "CLion 2025.2.3 (CL-252.1)", "Linux 6.8.0 (amd64)")
        assertTrue(url, url.startsWith("https://github.com/thijsduinhouwer2002-coder/bison-flex/issues/new?"))
        assertFalse("geen template: werkt ook zonder formulier in de loketrepo", url.contains("template="))
        assertFalse("spatie als %20, niet +", url.contains("+"))
        val v = velden(url)
        assertEquals("2026.1.3", v["version"])
        assertEquals("CLion 2025.2.3 (CL-252.1)", v["ide"])
        assertEquals("Linux 6.8.0 (amd64)", v["os"])
        val body = v["body"]!!
        assertTrue(body, body.contains("Bison & Flex: 2026.1.3"))
        assertTrue(body, body.contains("IDE: CLion 2025.2.3 (CL-252.1)"))
        assertTrue(body, body.contains("OS: Linux 6.8.0 (amd64)"))
        assertTrue("ver onder de grens van GitHub (8 KB)", url.length < 2000)
    }

    fun testUrlHierHeeftEchteGegevens() {
        val v = velden(Melden.urlHier())
        assertFalse(v["ide"].isNullOrBlank())
        assertEquals(Melden.systeem(), v["os"])
        assertTrue("versie uit versie.txt: ${v["version"]}", Regex("""\d{4}\.\d+\.\d+""").matches(v["version"]!!))
        val naam = System.getProperty("user.name") ?: ""
        if (naam.length >= 4) assertFalse("geen gebruikersnaam in het systeem", v["os"]!!.contains(naam))
    }

    fun testActieStaatOnderHelp() {
        val actie = ActionManager.getInstance().getAction("BisonFlex.ReportProblem")
        assertTrue(actie is MeldProbleemActie)
        assertEquals("Report a Problem with Bison & Flex...", actie!!.templatePresentation.text)
        val am = ActionManager.getInstance()
        val help = am.getAction(IdeActions.GROUP_HELP_MENU) as DefaultActionGroup
        val ids = help.getChildActionsOrStubs().map { am.getId(it) }
        assertTrue("$ids", "BisonFlex.ReportProblem" in ids)
    }

    fun testErrorHandlerVanMarketplace() {
        val ep = ExtensionPointName<ErrorReportSubmitter>("com.intellij.errorHandler")
        val van = ep.extensionList
            .filter { it.javaClass.name == "com.intellij.diagnostic.JetBrainsMarketplaceErrorReportSubmitter" }
            .map { it.pluginDescriptor?.pluginId?.idString }
        assertTrue("$van", Melden.PLUGIN_ID in van)
    }
}
