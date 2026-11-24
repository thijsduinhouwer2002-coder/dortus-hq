package com.dortus.bisonflex.e2e

import org.junit.jupiter.api.Assertions.assertFalse
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test

/**
 * Kan-punt keuring Chris 24 nov (platformen/jetbrains/keuring/2026-11-24-e2e-bekendePlatformfout-chris.md):
 * de filter in Gedeeld.kt vastleggen met drie gevallen. Start geen IDE, duurt een fractie van een seconde.
 */
class PlatformfoutTest {
    private val stackIntelliJ = """
        java.lang.IllegalArgumentException: node is not a child
            at javax.swing.tree.DefaultMutableTreeNode.getIndex(DefaultMutableTreeNode.java:0)
            at com.intellij.ide.OccurenceNavigatorSupport.findNode(OccurenceNavigatorSupport.java:0)
    """.trimIndent()

    @Test
    fun bekendeFoutZonderPluginWordtOvergeslagen() {
        assertTrue(bekendePlatformfout("node is not a child", stackIntelliJ))
    }

    @Test
    fun zelfdeFoutBijPreviousConflictWordtOvergeslagen() {
        // Run 45305066655: knop "Previous Conflict", tekst van Swing is dan "argument is not a child".
        val stackVorige = """
            java.lang.IllegalArgumentException: argument is not a child
                at javax.swing.tree.DefaultMutableTreeNode.getChildBefore(DefaultMutableTreeNode.java:973)
                at com.intellij.ide.OccurenceNavigatorSupport.findNextNodeAfter(OccurenceNavigatorSupport.java:119)
        """.trimIndent()
        assertTrue(bekendePlatformfout("PreviousOccurenceToolbarAction", stackVorige))
    }

    @Test
    fun bekendeFoutMetPluginInDeStackFaaltNog() {
        val metPlugin = stackIntelliJ + "\n    at com.dortus.bisonflex.pro.HernoemDiagnose.run(HernoemDiagnose.kt:0)"
        assertFalse(bekendePlatformfout("node is not a child", metPlugin))
    }

    @Test
    fun andereFoutFaaltNog() {
        assertFalse(bekendePlatformfout("java.lang.NullPointerException", "at com.intellij.openapi.editor.impl.EditorImpl.paint"))
        // Alleen een van de twee delen is niet genoeg.
        assertFalse(bekendePlatformfout("node is not a child", "at javax.swing.tree.DefaultMutableTreeNode.getIndex"))
    }
}
