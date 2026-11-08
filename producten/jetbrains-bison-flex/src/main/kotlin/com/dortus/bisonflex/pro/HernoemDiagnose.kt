package com.dortus.bisonflex.pro

import com.intellij.ide.DataManager
import com.intellij.openapi.actionSystem.ActionManager
import com.intellij.openapi.actionSystem.ActionUiKind
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.actionSystem.CommonDataKeys
import com.intellij.openapi.actionSystem.DataContext
import com.intellij.openapi.actionSystem.IdeActions
import com.intellij.openapi.actionSystem.LangDataKeys
import com.intellij.openapi.actionSystem.PlatformCoreDataKeys
import com.intellij.openapi.actionSystem.ex.ActionUtil
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.components.Service
import com.intellij.openapi.keymap.KeymapManager
import com.intellij.refactoring.rename.PsiElementRenameHandler
import com.intellij.refactoring.rename.RenameHandler
import com.intellij.refactoring.rename.RenameHandlerRegistry
import com.intellij.refactoring.rename.RenamePsiElementProcessor
import java.awt.Component
import java.awt.KeyboardFocusManager

/**
 * Alleen voor de IDE-test (Driver, `e2e/.../Hernoemen.kt`): laat zien wat de IDE bij Shift+F6 ziet in het
 * onderdeel met de focus (de structuurweergave), en kan de Rename-actie met precies die DataContext starten.
 * Verandert zelf niets aan de plugin; een gebruiker komt hier nooit.
 */
@Service(Service.Level.APP)
class HernoemDiagnose {

    private fun focus(): Component? = KeyboardFocusManager.getCurrentKeyboardFocusManager().let { it.focusOwner ?: it.permanentFocusOwner }

    private fun context(): DataContext = DataManager.getInstance().getDataContext(focus())

    private fun probeer(wat: String, f: () -> Any?): String = try { "$wat ${f()}" } catch (e: Throwable) { "$wat fout ${e.javaClass.simpleName}: ${e.message?.take(120)}" }

    /** Op de EDT aanroepen. Een regel tekst voor het log: focus, PSI-element, editor, handlers, of de actie aan staat, sneltoetsen. */
    fun focusInfo(): String {
        val ctx = context()
        val psi = try { CommonDataKeys.PSI_ELEMENT.getData(ctx) } catch (e: Throwable) { null }
        val actie = ActionManager.getInstance().getAction(IdeActions.ACTION_RENAME)
        val delen = listOf(
            "focus ${focus()?.javaClass?.name}",
            probeer("psi") { psi?.let { "${it.javaClass.simpleName} '$it' in ${it.containingFile?.name}" } },
            probeer("psi-rij") { LangDataKeys.PSI_ELEMENT_ARRAY.getData(ctx)?.size },
            probeer("psi-bestand") { CommonDataKeys.PSI_FILE.getData(ctx)?.name },
            probeer("context-onderdeel") { PlatformCoreDataKeys.CONTEXT_COMPONENT.getData(ctx)?.javaClass?.simpleName },
            probeer("editor") { CommonDataKeys.EDITOR.getData(ctx) != null },
            probeer("veto") { psi?.let { PsiElementRenameHandler.isVetoed(it) } },
            probeer("processor") { psi?.let { RenamePsiElementProcessor.forElement(it).javaClass.simpleName } },
            probeer("handlers aan") { RenameHandler.EP_NAME.extensionList.filter { it.isAvailableOnDataContext(ctx) }.map { it.javaClass.simpleName } },
            probeer("gekozen handler") { RenameHandlerRegistry.getInstance().getRenameHandler(ctx)?.javaClass?.simpleName },
            probeer("actie") {
                val e = AnActionEvent.createEvent(ctx, actie.templatePresentation.clone(), "e2e", ActionUiKind.NONE, null)
                ActionUtil.updateAction(actie, e)
                "${actie.javaClass.simpleName} aan ${e.presentation.isEnabled} zichtbaar ${e.presentation.isVisible}"
            },
            probeer("sneltoetsen") { KeymapManager.getInstance().activeKeymap.let { k -> "${k.name}: ${k.getShortcuts(IdeActions.ACTION_RENAME).joinToString()}" } },
        )
        return delen.joinToString(", ")
    }

    /** Start de Rename-actie later op de EDT met de DataContext van de focus (het venster kan modaal zijn). */
    fun hernoemMetFocus(): String {
        val ctx = context()
        val actie = ActionManager.getInstance().getAction(IdeActions.ACTION_RENAME)
        ApplicationManager.getApplication().invokeLater { ActionUtil.invokeAction(actie, ctx, "e2e", null, null) }
        return "gestart met focus ${focus()?.javaClass?.simpleName}"
    }
}
