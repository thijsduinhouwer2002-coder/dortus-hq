package com.dortus.bisonflex.meldingen

import com.intellij.codeInsight.daemon.DaemonCodeAnalyzer
import com.intellij.openapi.project.Project
import java.lang.reflect.Method

/**
 * Herstart de analyse van alle open bestanden, zonder verouderde API.
 *
 * `DaemonCodeAnalyzer.restart()` is verouderd sinds 2025.3 (Plugin Verifier, keuring Marketplace 8 nov 2026);
 * de opvolger `restart(Object reason)` bestaat pas vanaf 2025.3 (253). Wij steunen nog 2025.2 (since-build 252),
 * dus zoeken we de opvolger op de openbare klasse [DaemonCodeAnalyzer] op. Alleen in 2025.2 valt hij terug op
 * `restart()`, die daar nog niet verouderd is. Beide via reflectie, zodat geen van beide in de bytecode staat.
 * Weg zodra since-build 253 of hoger is: dan gewoon `restart(REDEN)`.
 */
object HerstartAnalyse {
    const val REDEN = "Bison & Flex: licentiestand veranderd"

    /** De opvolger als die bestaat (2025.3 en nieuwer), anders null. Openbaar voor de unittest. */
    val metReden: Method? = runCatching { DaemonCodeAnalyzer::class.java.getMethod("restart", Any::class.java) }.getOrNull()

    /** Alleen nog nodig in 2025.2. Openbaar voor de unittest. */
    val zonderReden: Method? = runCatching { DaemonCodeAnalyzer::class.java.getMethod("restart") }.getOrNull()

    fun voor(project: Project) {
        if (project.isDisposed) return
        val analyse = DaemonCodeAnalyzer.getInstance(project)
        when {
            metReden != null -> metReden.invoke(analyse, REDEN)
            zonderReden != null -> zonderReden.invoke(analyse)
        }
    }
}
