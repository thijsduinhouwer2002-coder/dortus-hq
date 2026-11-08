package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.driver.client.Remote
import com.intellij.driver.client.utility
import com.intellij.driver.model.LockSemantics
import com.intellij.driver.model.OnDispatcher
import com.intellij.driver.sdk.singleProject

/*
 * Alleen voor het log (kan-punt controleur 8 nov 08:10): welke regel van een kiesmenu (zoals "Find Usages Of"
 * met calc.y en calc.yy) Enter kiest, en wat het Find-paneel daarna toont. Alles hier mag mislukken zonder
 * dat de test faalt: dan staat in het log waarom het niet te lezen was.
 */

@Remote("java.awt.KeyboardFocusManager")
interface FocusBeheerOpAfstand {
    fun getCurrentKeyboardFocusManager(): FocusBeheerOpAfstand
    fun getFocusOwner(): FocusOnderdeelOpAfstand?
}

@Remote("java.awt.Component")
interface FocusOnderdeelOpAfstand

@Remote("javax.swing.JList")
interface LijstOpAfstand {
    fun getSelectedIndex(): Int
    fun getModel(): LijstModelOpAfstand
    fun getCellRenderer(): CelTekenaarOpAfstand
}

/** De tekst die de gebruiker ziet: de regel laten tekenen en de toegankelijke naam lezen (run 42473572181: geen PsiElement). */
@Remote("javax.swing.ListCellRenderer")
interface CelTekenaarOpAfstand {
    fun getListCellRendererComponent(list: LijstOpAfstand, value: IetsOpAfstand?, index: Int, isSelected: Boolean, cellHasFocus: Boolean): GetekendeCelOpAfstand?
}

@Remote("java.awt.Component")
interface GetekendeCelOpAfstand {
    fun getAccessibleContext(): ToegankelijkOpAfstand?
}

@Remote("javax.accessibility.AccessibleContext")
interface ToegankelijkOpAfstand {
    fun getAccessibleName(): String?
}

@Remote("javax.swing.ListModel")
interface LijstModelOpAfstand {
    fun getSize(): Int
    fun getElementAt(index: Int): IetsOpAfstand?
}

@Remote("java.lang.Object")
interface IetsOpAfstand

@Remote("com.intellij.navigation.NavigationItem")
interface NavigeerbaarOpAfstand {
    fun getPresentation(): PresentatieOpAfstand?
}

@Remote("com.intellij.psi.PsiElement")
interface PsiElementOpAfstand {
    fun getText(): String?
    fun getContainingFile(): PsiBestandOpAfstand?
}

@Remote("com.intellij.psi.PsiFile")
interface PsiBestandOpAfstand {
    fun getName(): String
}

@Remote("com.intellij.ui.content.ContentManager")
interface InhoudBeheerOpAfstand {
    fun getSelectedContent(): InhoudOpAfstand?
}

@Remote("com.intellij.ui.content.Content")
interface InhoudOpAfstand {
    fun getDisplayName(): String?
    fun getDescription(): String?
}

/** "regel 1 van 2 gekozen: [1] NUM in calc.y (presentatie 'NUM calc.y'); [2] ...", of waarom het niet lukte. */
internal fun Driver.kiesmenuKeuze(): String = try {
    withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
        val eigenaar = utility<FocusBeheerOpAfstand>().getCurrentKeyboardFocusManager().getFocusOwner()
            ?: return@withContext "geen onderdeel met focus"
        val lijst = try { cast(eigenaar, LijstOpAfstand::class) } catch (t: Throwable) {
            return@withContext "focus ligt niet op een lijst (${t.javaClass.simpleName})"
        }
        val model = lijst.getModel()
        val regels = (0 until minOf(model.getSize(), 10)).map { i ->
            val ding = model.getElementAt(i)
            val zichtbaar = try {
                lijst.getCellRenderer().getListCellRendererComponent(lijst, ding, i, false, false)?.getAccessibleContext()?.getAccessibleName()
            } catch (t: Throwable) {
                "niet te tekenen (${t.javaClass.simpleName})"
            }
            "[${i + 1}] '$zichtbaar' ${beschrijf(ding)}"
        }
        "regel ${lijst.getSelectedIndex() + 1} van ${model.getSize()} gekozen: ${regels.joinToString("; ")}"
    }
} catch (t: Throwable) {
    "kiesmenu niet te lezen: ${t.javaClass.simpleName}: ${t.message?.take(200)}"
}

private fun Driver.beschrijf(ding: IetsOpAfstand?): String {
    if (ding == null) return "leeg"
    val psi = try {
        val e = cast(ding, PsiElementOpAfstand::class)
        "${e.getText()?.take(40)} in ${e.getContainingFile()?.getName()}"
    } catch (t: Throwable) {
        "geen PsiElement"
    }
    val tekst = try { cast(ding, NavigeerbaarOpAfstand::class).getPresentation()?.getPresentableText() } catch (t: Throwable) { null }
    return "$psi (presentatie '$tekst')"
}

/** Naam en beschrijving van het open tabblad in het Find-paneel, of waarom het niet te lezen was. */
internal fun Driver.findTabblad(): String = try {
    val panelen = utility<PanelenOpAfstand>().getInstance(singleProject())
    withContext(OnDispatcher.EDT) {
        val paneel = panelen.getToolWindow("Find") ?: return@withContext "geen Find-paneel"
        val inhoud = paneel.getContentManager().getSelectedContent()
            ?: return@withContext "geen tabblad"
        "tabblad '${inhoud.getDisplayName()}', beschrijving '${inhoud.getDescription()}'"
    }
} catch (t: Throwable) {
    "Find-tabblad niet te lezen: ${t.javaClass.simpleName}: ${t.message?.take(200)}"
}
