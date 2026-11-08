package com.dortus.bisonflex.meldingen

import com.dortus.bisonflex.pro.FacadeBron
import com.intellij.codeInsight.daemon.impl.DaemonCodeAnalyzerImpl
import com.intellij.lang.annotation.HighlightSeverity
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.application.ReadAction
import com.intellij.openapi.command.WriteCommandAction
import com.intellij.openapi.components.Service
import com.intellij.openapi.fileEditor.FileEditorManager
import com.intellij.openapi.project.ProjectManager

/**
 * Alleen voor de IDE-test (Driver, `e2e/.../Meldingen.kt`): zet de licentiestand om, past de tekst van de open
 * editor aan en leest welke meldingen van eis 7 er staan. Doet niets als `bisonflex.internal.e2e.forceNoLicense`
 * niet gezet is, dus nooit bij een gebruiker.
 */
@Service(Service.Level.APP)
class MeldingenDiagnose {
    private fun aan() = System.getProperty(FacadeBron.E2E_EIGENSCHAP) == "true"

    fun zetStand(stand: String) = FacadeBron.zetE2eStand(stand)

    private fun editor() = ProjectManager.getInstance().openProjects.firstOrNull()
        ?.let { FileEditorManager.getInstance(it).selectedTextEditor }

    /** Vervangt de eerste [oud] door [nieuw] in de open editor (één ongedaan-te-maken stap). Geeft of het lukte. */
    fun vervang(oud: String, nieuw: String): Boolean {
        if (!aan()) return false
        var gelukt = false
        ApplicationManager.getApplication().invokeAndWait {
            val e = editor() ?: return@invokeAndWait
            val i = e.document.text.indexOf(oud)
            if (i < 0) return@invokeAndWait
            WriteCommandAction.runWriteCommandAction(e.project, "Dortus e2e", null, {
                e.document.replaceString(i, i + oud.length, nieuw)
            })
            gelukt = true
        }
        return gelukt
    }

    /** De meldingen van eis 7 in de open editor, als "tekst @ regel" gescheiden door " | ", of leeg. */
    fun meldingen(): String {
        if (!aan()) return ""
        var uit = ""
        ApplicationManager.getApplication().invokeAndWait {
            val e = editor() ?: return@invokeAndWait
            val p = e.project ?: return@invokeAndWait
            uit = ReadAction.compute<String, RuntimeException> {
                DaemonCodeAnalyzerImpl.getHighlights(e.document, HighlightSeverity.INFORMATION, p)
                    .filter { it.description?.matches(Regex("(Undefined|Unused) .*")) == true }
                    .joinToString(" | ") { "${it.description} @ ${e.document.getLineNumber(it.startOffset) + 1}" }
            }
        }
        return uit
    }

    /** Zet de cursor op [tekst] plus [extra] tekens, voor Alt+Enter. */
    fun cursorOp(tekst: String, extra: Int): Boolean {
        if (!aan()) return false
        var gelukt = false
        ApplicationManager.getApplication().invokeAndWait {
            val e = editor() ?: return@invokeAndWait
            val i = e.document.text.indexOf(tekst)
            if (i >= 0) { e.caretModel.moveToOffset(i + extra); gelukt = true }
        }
        return gelukt
    }
}
