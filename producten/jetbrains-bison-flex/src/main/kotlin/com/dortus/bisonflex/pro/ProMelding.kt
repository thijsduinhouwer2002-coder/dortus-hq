package com.dortus.bisonflex.pro

import com.intellij.codeInsight.hint.HintManager
import com.intellij.notification.NotificationAction
import com.intellij.notification.NotificationGroupManager
import com.intellij.notification.NotificationType
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.components.Service
import com.intellij.openapi.editor.Editor
import com.intellij.openapi.project.Project
import org.jetbrains.annotations.TestOnly
import java.util.concurrent.atomic.AtomicBoolean
import java.util.concurrent.atomic.AtomicInteger

/**
 * De Pro-melding (Daan punt 3): een gewone balloon, nooit een dialoog, hoogstens één keer per IDE-sessie.
 * De vlag zit in deze application service, dus geldt voor alle projecten samen.
 * Bij latere klikken (balloon al getoond) een korte informatiehint in de editor, zonder knop.
 */
@Service(Service.Level.APP)
class ProMelding {
    private val getoond = AtomicBoolean(false)
    private val hints = AtomicInteger(0)

    /** Toont de melding als dat deze sessie nog niet gebeurd is. Geeft true als hij nu getoond is. */
    fun toonEenmaal(project: Project?): Boolean {
        if (!getoond.compareAndSet(false, true)) return false
        NotificationGroupManager.getInstance().getNotificationGroup(GROEP)
            .createNotification(TITEL, TEKST, NotificationType.INFORMATION)
            .addAction(NotificationAction.createSimpleExpiring("Start free trial") { Proef.start() })
            .addAction(NotificationAction.createSimpleExpiring("Not now") {})
            .notify(project)
        return true
    }

    /** De korte hint [tekst] (standaard [HINT]) in [editor] (op de EDT aanroepen). */
    fun toonHint(editor: Editor, tekst: String = HINT) {
        hints.incrementAndGet()
        HintManager.getInstance().showInformationHint(editor, tekst)
    }

    /** Of de melding deze sessie al getoond is (ook gelezen door de IDE-test). */
    fun isGetoond(): Boolean = getoond.get()

    /** Hoe vaak de korte hint deze sessie getoond is (ook gelezen door de IDE-test). */
    fun aantalHints(): Int = hints.get()

    @TestOnly
    fun opnieuwVoorTest() {
        getoond.set(false)
        hints.set(0)
    }

    companion object {
        /** Zelfde id als `notificationGroup` in plugin.xml. */
        const val GROEP = "Bison & Flex Pro"
        const val TITEL = "Bison & Flex Pro"
        const val TEKST = "Go to declaration across grammar and scanner is a Pro feature. Try it free for 30 days."
        /** Korte hint bij latere klikken, zonder knop. */
        const val HINT = "Go to declaration across grammar and scanner is a Pro feature"
        /** Korte hint bij hernoemen dat ook het andere bestand raakt. */
        const val HINT_HERNOEMEN = "Rename across grammar and scanner is a Pro feature"

        fun getInstance(): ProMelding = ApplicationManager.getApplication().getService(ProMelding::class.java)
    }
}
