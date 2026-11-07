package com.dortus.bisonflex

import com.dortus.bisonflex.pro.Proef
import com.intellij.openapi.actionSystem.ActionManager
import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.testFramework.PlatformTestUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase

/** "Start free trial": de registratie-actie van de IDE met onze code, anders de browser (Daan, beoordeling 6 punt 2). */
class ProefTest : BasePlatformTestCase() {

    private class Nep : AnAction() {
        var code: String? = null
        var uitleg: String? = null
        var keer = 0
        override fun actionPerformed(e: AnActionEvent) {
            keer++
            code = e.dataContext.getData(Proef.CODE_SLEUTEL)
            uitleg = e.dataContext.getData(Proef.UITLEG_SLEUTEL)
        }
    }

    private val geopend = ArrayList<String>()

    private fun start(acties: Map<String, AnAction>) {
        Proef.start(zoek = { acties[it] }, browser = { geopend += it })
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
    }

    fun testRegisterPluginsKrijgtCodeEnUitleg() {
        val nep = Nep()
        val register = Nep()
        start(mapOf("RegisterPlugins" to nep, "Register" to register))
        assertEquals(1, nep.keer)
        assertEquals(0, register.keer)
        assertEquals("PBISONFLEX", nep.code)
        assertEquals(Proef.UITLEG, nep.uitleg)
        assertEquals(emptyList<String>(), geopend)
    }

    fun testZonderRegisterPluginsDanRegister() {
        val register = Nep()
        start(mapOf("Register" to register))
        assertEquals(1, register.keer)
        assertEquals("PBISONFLEX", register.code)
        assertEquals(emptyList<String>(), geopend)
    }

    fun testZonderRegistratieDeMarketplace() {
        start(emptyMap())
        assertEquals(listOf(Proef.KOOPPAGINA), geopend)
    }

    /** Niet meteen: pas op de EDT na invokeLater (niet-modaal), zoals het voorbeeld van JetBrains. */
    fun testLooptLater() {
        val nep = Nep()
        Proef.start(zoek = { if (it == "RegisterPlugins") nep else null }, browser = { geopend += it })
        assertEquals(0, nep.keer)
        PlatformTestUtil.dispatchAllInvocationEventsInIdeEventQueue()
        assertEquals(1, nep.keer)
    }

    fun testCodeKlopt() {
        val xml = javaClass.classLoader.getResource("META-INF/plugin.xml")!!.readText()
        assertTrue(xml.contains("code=\"${Proef.CODE}\""))
        val am = ActionManager.getInstance()
        println("DORTUS-TEST RegisterPlugins ${am.getAction("RegisterPlugins") != null}, Register ${am.getAction("Register") != null}")
    }
}
