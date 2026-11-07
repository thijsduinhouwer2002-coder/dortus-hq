package com.dortus.bisonflex.pro

import com.intellij.codeInsight.hint.HintManager
import com.intellij.notification.NotificationAction
import com.intellij.notification.NotificationGroupManager
import com.intellij.notification.NotificationType
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.components.Service
import com.intellij.openapi.editor.Editor
import com.intellij.openapi.project.Project
import com.intellij.openapi.wm.StatusBar
import org.jetbrains.annotations.TestOnly
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.atomic.AtomicInteger

/**
 * De Pro-melding (Daan punt 3): een gewone balloon, nooit een dialoog, hoogstens één keer per IDE-sessie per actie.
 * Een vlag per actie ([GA_NAAR], [HERNOEMEN]; Daan, beoordeling 8 punt 5): wie eerst de ga-naar-balloon zag,
 * hoort bij Shift+F6 toch één keer dat hernoemen Pro is. De vlaggen zitten in deze application service, dus gelden
 * voor alle projecten samen. Bij latere keren een korte hint zonder knop: in de editor, of zonder editor in de
 * statusbalk ([toonHint]).
 */
@Service(Service.Level.APP)
class ProMelding {
    private val getoond = ConcurrentHashMap.newKeySet<String>()
    private val hints = AtomicInteger(0)
    private val hintsZonderEditor = AtomicInteger(0)
    @Volatile private var laatsteHint: String? = null
    @Volatile private var laatsteMelding: String? = null

    /**
     * Toont de balloon met [tekst] als dat deze sessie voor [actie] nog niet gebeurd is.
     * Geeft true als hij nu getoond is.
     */
    fun toonEenmaal(project: Project?, tekst: String = TEKST, actie: String = GA_NAAR): Boolean {
        if (!getoond.add(actie)) return false
        laatsteMelding = tekst
        NotificationGroupManager.getInstance().getNotificationGroup(GROEP)
            .createNotification(TITEL, tekst, NotificationType.INFORMATION)
            .addAction(NotificationAction.createSimpleExpiring("Start free trial") { Proef.start() })
            .addAction(NotificationAction.createSimpleExpiring("Not now") {})
            .notify(project)
        return true
    }

    /**
     * De korte hint [tekst] (standaard [HINT]) zonder knop (op de EDT aanroepen). Met [editor] als informatiehint
     * in die editor. Zonder editor (hernoemen vanuit de structuurweergave of het projectvenster) in de statusbalk
     * van [project]: daar staat geen editor om een hint aan te hangen, en een tweede balloon zou de verkooptekst
     * herhalen (hoogstens één balloon per sessie per actie).
     */
    fun toonHint(editor: Editor?, tekst: String = HINT, project: Project? = editor?.project) {
        hints.incrementAndGet()
        laatsteHint = tekst
        if (editor != null) {
            HintManager.getInstance().showInformationHint(editor, tekst)
        } else {
            hintsZonderEditor.incrementAndGet()
            StatusBar.Info.set(tekst, project)
        }
    }

    /** Of er deze sessie al een Pro-balloon getoond is, voor welke actie ook (ook gelezen door de IDE-test). */
    fun isGetoond(): Boolean = getoond.isNotEmpty()

    /** Of de balloon voor [actie] deze sessie al getoond is (ook gelezen door de IDE-test). */
    fun isGetoondVoor(actie: String): Boolean = actie in getoond

    /** Hoe vaak de korte hint deze sessie getoond is, in de editor en in de statusbalk samen (ook voor de IDE-test). */
    fun aantalHints(): Int = hints.get()

    /** Hoe vaak de korte hint in de statusbalk kwam, omdat er geen editor was. */
    fun aantalHintsZonderEditor(): Int = hintsZonderEditor.get()

    /** Tekst van de laatste hint en van de laatste balloon, of null (voor het log van de IDE-test). */
    fun laatsteHint(): String? = laatsteHint
    fun laatsteMelding(): String? = laatsteMelding

    @TestOnly
    fun opnieuwVoorTest() {
        getoond.clear()
        hints.set(0)
        hintsZonderEditor.set(0)
        laatsteHint = null
        laatsteMelding = null
    }

    companion object {
        /** Zelfde id als `notificationGroup` in plugin.xml. */
        const val GROEP = "Bison & Flex Pro"
        const val TITEL = "Bison & Flex Pro"

        /** Namen van de acties, elk met een eigen "al getoond"-vlag. */
        const val GA_NAAR = "ga-naar"
        const val HERNOEMEN = "hernoemen"

        const val TEKST = "Go to declaration across grammar and scanner is a Pro feature. Try it free for 30 days."
        /** Korte hint bij latere klikken, zonder knop. */
        const val HINT = "Go to declaration across grammar and scanner is a Pro feature"
        /** Neutrale hint tijdens het indexeren: de IDE weet nog niet welke bestanden een naam gebruiken. Geen Pro. */
        const val HINT_INDEXEREN = "Indexing, try again in a moment"

        /** Balloon bij de eerste geblokkeerde hernoeming van [naam], die ook [ander] zou veranderen. */
        fun tekstHernoemen(naam: String, ander: String) =
            "Renaming $naam also changes $ander. Rename across grammar and scanner is a Pro feature. Try it free for 30 days."

        /** Korte hint bij een latere geblokkeerde hernoeming: zegt waarom er niets veranderd is. */
        fun hintHernoemen(naam: String, ander: String) =
            "$naam is also used in $ander. Rename across grammar and scanner is a Pro feature."

        fun getInstance(): ProMelding = ApplicationManager.getApplication().getService(ProMelding::class.java)
    }
}
