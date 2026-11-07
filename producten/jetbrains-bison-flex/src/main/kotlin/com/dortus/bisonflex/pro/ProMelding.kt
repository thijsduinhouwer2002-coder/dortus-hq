package com.dortus.bisonflex.pro

import com.intellij.ide.BrowserUtil
import com.intellij.notification.NotificationAction
import com.intellij.notification.NotificationGroupManager
import com.intellij.notification.NotificationType
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.components.Service
import com.intellij.openapi.project.Project
import org.jetbrains.annotations.TestOnly
import java.util.concurrent.atomic.AtomicBoolean

/**
 * De Pro-melding (Daan punt 3): een gewone balloon, nooit een dialoog, hoogstens één keer per IDE-sessie.
 * De vlag zit in deze application service, dus geldt voor alle projecten samen.
 */
@Service(Service.Level.APP)
class ProMelding {
    private val getoond = AtomicBoolean(false)

    /** Toont de melding als dat deze sessie nog niet gebeurd is. Geeft true als hij nu getoond is. */
    fun toonEenmaal(project: Project?): Boolean {
        if (!getoond.compareAndSet(false, true)) return false
        NotificationGroupManager.getInstance().getNotificationGroup(GROEP)
            .createNotification(TITEL, TEKST, NotificationType.INFORMATION)
            .addAction(NotificationAction.createSimpleExpiring("Start free trial") { BrowserUtil.browse(KOOPPAGINA) })
            .addAction(NotificationAction.createSimpleExpiring("Not now") {})
            .notify(project)
        return true
    }

    /** Of de melding deze sessie al getoond is (ook gelezen door de IDE-test). */
    fun isGetoond(): Boolean = getoond.get()

    @TestOnly
    fun opnieuwVoorTest() = getoond.set(false)

    companion object {
        /** Zelfde id als `notificationGroup` in plugin.xml. */
        const val GROEP = "Bison & Flex Pro"
        const val TITEL = "Bison & Flex Pro"
        const val TEKST = "Go to declaration across grammar and scanner is a Pro feature. Try it free for 30 days."
        /** Nog de algemene Marketplace: de id van de pluginpagina is er pas na het indienen (architectuur.md, Open). */
        const val KOOPPAGINA = "https://plugins.jetbrains.com/"

        fun getInstance(): ProMelding = ApplicationManager.getApplication().getService(ProMelding::class.java)
    }
}
