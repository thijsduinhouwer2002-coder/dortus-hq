package com.dortus.bisonflex.meldingen

import com.dortus.bisonflex.pro.Licentie
import com.intellij.codeInsight.daemon.DaemonCodeAnalyzer
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
        var laatste = Licentie.proWerkt()
        val taak = AppExecutorUtil.getAppScheduledExecutorService().scheduleWithFixedDelay({
            val nu = Licentie.proWerkt()
            if (nu != laatste && !project.isDisposed) {
                laatste = nu
                DaemonCodeAnalyzer.getInstance(project).restart()
            }
        }, 2, 2, TimeUnit.SECONDS)
        Disposer.register(project) { taak.cancel(false) }
    }
}
