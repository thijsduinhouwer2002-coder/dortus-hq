package com.dortus.bisonflex.meldingen

import com.dortus.bisonflex.pro.Licentie
import com.intellij.openapi.project.Project
import com.intellij.openapi.startup.ProjectActivity
import com.intellij.openapi.util.Disposer
import com.intellij.util.concurrency.AppExecutorUtil
import java.util.concurrent.TimeUnit

/**
 * Onthoudt de laatste licentiestand en herstart de analyse bij een andere stand, zodat de meldingen van eis 7 na
 * het starten van de proef meteen komen. De facade geeft geen bericht bij een wijziging, dus elke 2 seconden kijken
 * (op een achtergronddraad, los van het opstarten; stopt als het project dicht gaat).
 */
class StandLuisteraar : ProjectActivity {
    override suspend fun execute(project: Project) {
        val wacht = StandWacht { HerstartAnalyse.voor(project) }
        val taak = AppExecutorUtil.getAppScheduledExecutorService().scheduleWithFixedDelay({ wacht.kijk() }, 2, 2, TimeUnit.SECONDS)
        Disposer.register(project) { taak.cancel(false) }
    }
}

/** Het denkwerk van [StandLuisteraar], los te toetsen: [herstart] alleen als Pro aan of uit gaat. */
class StandWacht(private val herstart: () -> Unit) {
    @Volatile private var laatste = Licentie.proWerkt()

    fun kijk() {
        val nu = Licentie.proWerkt()
        if (nu != laatste) {
            laatste = nu
            herstart()
        }
    }
}
