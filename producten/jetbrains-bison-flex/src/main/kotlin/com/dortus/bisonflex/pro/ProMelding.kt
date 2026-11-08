package com.dortus.bisonflex.pro

import com.dortus.bisonflex.BisonIconen
import com.intellij.codeInsight.hint.HintManager
import com.intellij.notification.NotificationAction
import com.intellij.notification.NotificationGroupManager
import com.intellij.notification.NotificationType
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.components.Service
import com.intellij.openapi.editor.Editor
import com.intellij.openapi.project.Project
import com.intellij.openapi.ui.MessageType
import com.intellij.openapi.ui.popup.Balloon
import com.intellij.openapi.ui.popup.JBPopupFactory
import com.intellij.openapi.wm.IdeFocusManager
import com.intellij.openapi.wm.WindowManager
import com.intellij.ui.BalloonImpl
import com.intellij.ui.awt.RelativePoint
import org.jetbrains.annotations.TestOnly
import java.awt.Component
import java.awt.KeyboardFocusManager
import java.awt.Point
import javax.swing.JComponent
import javax.swing.JTree
import javax.swing.SwingUtilities
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.atomic.AtomicInteger

/**
 * De Pro-melding (Daan punt 3): een gewone balloon, nooit een dialoog, hoogstens één keer per IDE-sessie per actie.
 * Een vlag per actie ([GA_NAAR], [HERNOEMEN]; Daan, beoordeling 8 punt 5): wie eerst de ga-naar-balloon zag,
 * hoort bij Shift+F6 toch één keer dat hernoemen Pro is. De vlaggen zitten in deze application service, dus gelden
 * voor alle projecten samen. Bij latere keren een korte hint zonder knop: in de editor, of zonder editor als
 * kleine balloon bij de gekozen knoop ([toonHint]).
 */
@Service(Service.Level.APP)
class ProMelding {
    private val getoond = ConcurrentHashMap.newKeySet<String>()
    private val hints = AtomicInteger(0)
    private val hintsZonderEditor = AtomicInteger(0)
    @Volatile private var laatsteHint: String? = null
    @Volatile private var laatsteMelding: String? = null
    @Volatile private var laatsteBalloon: Balloon? = null
    @Volatile private var laatstePlek: String? = null

    /**
     * Toont de balloon met [tekst] als dat deze sessie voor [actie] nog niet gebeurd is.
     * Geeft true als hij nu getoond is.
     */
    fun toonEenmaal(project: Project?, tekst: String = TEKST, actie: String = GA_NAAR): Boolean {
        if (!getoond.add(actie)) return false
        laatsteMelding = tekst
        NotificationGroupManager.getInstance().getNotificationGroup(GROEP)
            .createNotification(TITEL, tekst, NotificationType.INFORMATION)
            .setIcon(BisonIconen.PRO)
            .addAction(NotificationAction.createSimpleExpiring("Start free trial") { Proef.start() })
            .addAction(NotificationAction.createSimpleExpiring("Not now") {})
            .notify(project)
        return true
    }

    /**
     * De korte hint [tekst] (standaard [HINT]) zonder knop (op de EDT aanroepen). Met [editor] als informatiehint
     * in die editor. Zonder editor (hernoemen vanuit de structuurweergave of het projectvenster) een kleine balloon
     * zonder knoppen ([toonBalloonZonderEditor]) bij [component] (het onderdeel waar Shift+F6 vandaan kwam, meestal
     * de boom met de focus). Eerst stond die tekst in de statusbalk (`StatusBar.Info.set`), maar de nieuwe UI toont
     * die tekst niet (IDE-run 42423551917): de gebruiker zag niets. Geen notificatie: een tweede balloon met knoppen
     * zou de verkooptekst herhalen (hoogstens één per sessie per actie).
     */
    fun toonHint(editor: Editor?, tekst: String = HINT, project: Project? = editor?.project, component: Component? = null) {
        hints.incrementAndGet()
        laatsteHint = tekst
        if (editor != null) {
            HintManager.getInstance().showInformationHint(editor, tekst)
        } else {
            hintsZonderEditor.incrementAndGet()
            val bron = component ?: focusOnderdeel(project)
            val app = ApplicationManager.getApplication()
            if (app.isDispatchThread) toonBalloonZonderEditor(tekst, project, bron)
            else app.invokeLater { toonBalloonZonderEditor(tekst, project, bron) }
        }
    }

    /**
     * Zet de kleine balloon (`createHtmlTextBalloonBuilder`, soort INFO, geen knoppen, weg na 8 s, bij een klik of
     * toets ernaast). Plek: is [bron] een JTree met een gekozen knoop (de structuurweergave, het projectvenster), dan
     * onder die knoop met de punt omhoog (Daan, beoordeling 9: boven bedekte hij de kop "Declarations" en de tabbalk);
     * anders boven het midden van [bron]; zonder bron onderaan in het midden van het IDE-frame.
     * [laatsteBalloon] wordt pas gezet als `show` gelukt is. In een test zonder scherm (headless) wordt er niets
     * getoond, alleen geteld.
     */
    private fun toonBalloonZonderEditor(tekst: String, project: Project?, bron: Component?) {
        if (ApplicationManager.getApplication().isHeadlessEnvironment) { laatstePlek = "headless"; return }
        var b: Balloon? = null
        try {
            val (plek, richting) = plekVoor(project, bron) ?: run { laatstePlek = "geen plek"; return }
            laatsteBalloon?.let { if (!it.isDisposed) it.hide() }
            laatsteBalloon = null
            b = JBPopupFactory.getInstance().createHtmlTextBalloonBuilder(tekst, MessageType.INFO, null)
                .setFadeoutTime(8_000)
                .setHideOnClickOutside(true)
                .setHideOnKeyOutside(true)
                .createBalloon()
            b.show(plek, richting)
            laatsteBalloon = b
        } catch (e: Throwable) {
            b?.let { runCatching { if (!it.isDisposed) it.dispose() } }
            laatstePlek = "fout ${e.javaClass.simpleName}: ${e.message?.take(120)}"
        }
    }

    /** Waar de balloon komt en aan welke kant van dat punt (bij een boomknoop eronder, punt omhoog). */
    private fun plekVoor(project: Project?, bron: Component?): Pair<RelativePoint, Balloon.Position>? {
        if (bron is JTree && bron.isShowing) {
            val pad = bron.selectionPath
            val vak = pad?.let { bron.getPathBounds(it) }
            if (vak != null) {
                val zicht = bron.visibleRect
                val x = (vak.x + minOf(vak.width, 200) / 2).coerceIn(zicht.x, zicht.x + zicht.width)
                val y = (vak.y + vak.height).coerceIn(zicht.y, zicht.y + zicht.height)
                laatstePlek = "boom ${bron.javaClass.simpleName}, onder knoop '${pad.lastPathComponent}'"
                return RelativePoint(bron, Point(x, y)) to Balloon.Position.below
            }
        }
        if (bron is JComponent && bron.isShowing && bron.width > 0) {
            laatstePlek = "onderdeel ${bron.javaClass.simpleName}"
            return RelativePoint(bron, Point(bron.width / 2, minOf(bron.height / 2, 40))) to Balloon.Position.above
        }
        val frame = project?.let { WindowManager.getInstance().getIdeFrame(it) }?.component
            ?: bron?.let { SwingUtilities.getRootPane(it) }
            ?: return null
        laatstePlek = "frame"
        return RelativePoint(frame, Point(frame.width / 2, frame.height - 60)) to Balloon.Position.above
    }

    /**
     * Of de laatste balloon zonder editor nu echt op het scherm staat (ook gelezen door de IDE-test). Is het geen
     * [BalloonImpl], dan weten we het niet en zeggen we nee: de IDE-test mag niet slagen op een gok.
     */
    fun balloonZonderEditorInBeeld(): Boolean {
        val b = laatsteBalloon ?: return false
        if (b.isDisposed) return false
        return (b as? BalloonImpl)?.isVisible ?: false
    }

    /** Waar de laatste balloon zonder editor kwam ("boom ...", "onderdeel ...", "frame", "headless" of een fout), voor het log. */
    fun laatstePlekZonderEditor(): String? = laatstePlek

    /** Of er deze sessie al een Pro-balloon getoond is, voor welke actie ook (ook gelezen door de IDE-test). */
    fun isGetoond(): Boolean = getoond.isNotEmpty()

    /** Of de balloon voor [actie] deze sessie al getoond is (ook gelezen door de IDE-test). */
    fun isGetoondVoor(actie: String): Boolean = actie in getoond

    /** Hoe vaak de korte hint deze sessie getoond is, met en zonder editor samen (ook voor de IDE-test). */
    fun aantalHints(): Int = hints.get()

    /** Hoe vaak de korte hint zonder editor kwam (als kleine balloon, zie [toonHint]). */
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
        laatsteBalloon?.let { if (!it.isDisposed) it.hide() }
        laatsteBalloon = null
        laatstePlek = null
    }

    companion object {
        /** Zelfde id als `notificationGroup` in plugin.xml. */
        const val GROEP = "Bison & Flex Pro"
        const val TITEL = "Bison & Flex Pro"

        /** Namen van de acties, elk met een eigen "al getoond"-vlag. */
        const val GA_NAAR = "ga-naar"
        const val HERNOEMEN = "hernoemen"

        /**
         * Balloon bij de eerste geblokkeerde sprong van [van] naar [naar]. Kort, zodat hij op twee regels past
         * (Daan, beoordeling 9 punt 5: de oude tekst werd afgekapt bij "Try it free...").
         */
        fun tekstGaNaar(van: String, naar: String) = "Jumping from $van to $naar is a Pro feature, free to try for 30 days."
        /** Zelfde balloon zonder bestandsnamen (standaard van [toonEenmaal]). */
        const val TEKST = "Jumping between scanner and grammar is a Pro feature, free to try for 30 days."
        /** Korte hint bij latere klikken, zonder knop. */
        const val HINT = "Go to declaration across grammar and scanner is a Pro feature"
        /** Neutrale hint tijdens het indexeren: de IDE weet nog niet welke bestanden een naam gebruiken. Geen Pro. */
        const val HINT_INDEXEREN = "Indexing, try again in a moment"

        /** Balloon bij de eerste geblokkeerde hernoeming van [naam], die ook [ander] zou veranderen. */
        fun tekstHernoemen(naam: String, ander: String) =
            "Renaming $naam also changes $ander. That is a Pro feature, free to try for 30 days."

        /** Korte hint bij een latere geblokkeerde hernoeming: zegt waarom er niets veranderd is. */
        fun hintHernoemen(naam: String, ander: String) =
            "$naam is also used in $ander. Rename across grammar and scanner is a Pro feature."

        /**
         * Het onderdeel met de focus (bij Shift+F6 in de structuurweergave de boom), of null. De enige plek waar dat
         * bepaald wordt; ook [ProHernoemen.bron] gebruikt dit.
         */
        fun focusOnderdeel(project: Project?): Component? =
            project?.let { IdeFocusManager.getInstance(it).focusOwner }
                ?: KeyboardFocusManager.getCurrentKeyboardFocusManager().let { it.focusOwner ?: it.permanentFocusOwner }

        fun getInstance(): ProMelding = ApplicationManager.getApplication().getService(ProMelding::class.java)
    }
}
