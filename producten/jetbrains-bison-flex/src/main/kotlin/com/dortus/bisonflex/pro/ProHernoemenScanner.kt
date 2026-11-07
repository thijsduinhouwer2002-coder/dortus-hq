package com.dortus.bisonflex.pro

import com.dortus.bisonflex.FlexLanguage
import com.dortus.bisonflex.psi.Koppeling
import com.intellij.openapi.actionSystem.CommonDataKeys
import com.intellij.openapi.actionSystem.DataContext
import com.intellij.openapi.editor.Editor
import com.intellij.openapi.project.DumbService
import com.intellij.openapi.project.Project
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiFile
import com.intellij.refactoring.rename.RenameHandler

/**
 * Shift+F6 op een token in de C-code van een scanner (`return NUM;` in calc.l) zonder licentie (Daan, beoordeling 8
 * punt 6). De verwijzing naar `%token NUM` in de grammatica is Pro en gaat dan nergens heen, dus de IDE vond niets
 * om te hernoemen en gaf haar eigen fout ("Cannot perform refactoring"). Deze handler neemt het dan over en geeft
 * dezelfde melding als hernoemen vanuit de grammatica ([ProHernoemen.meldGeblokkeerd]); er verandert niets.
 * Tijdens het indexeren is niet te weten waar de naam heen gaat: dan de neutrale hint, zonder Pro.
 * Met licentie (of als de naam geen token van een grammatica is) is deze handler er niet en hernoemt de IDE zelf.
 */
class ProHernoemenScanner : RenameHandler {

    /** Wat er bij de cursor gebeurt: de naam, en de grammatica's (leeg tijdens indexeren). */
    private class Geval(val naam: String, val grammaticas: List<PsiFile>, val indexeren: Boolean)

    private fun geval(editor: Editor?, file: PsiFile?): Geval? {
        if (editor == null || file == null || file.language != FlexLanguage) return null
        val blad = naamBijCursor(file, editor.caretModel.offset) ?: return null
        val naam = blad.text
        if (Koppeling.startConditie(file, naam) != null) return null
        if (DumbService.isDumb(file.project)) return Geval(naam, emptyList(), true)
        if (Licentie.proWerkt()) return null
        val grammaticas = Koppeling.grammaticas(file) { Koppeling.bisonToken(it, naam) != null }
        return if (grammaticas.isEmpty()) null else Geval(naam, grammaticas, false)
    }

    override fun isAvailableOnDataContext(dataContext: DataContext): Boolean =
        geval(CommonDataKeys.EDITOR.getData(dataContext), CommonDataKeys.PSI_FILE.getData(dataContext)) != null

    override fun isRenaming(dataContext: DataContext): Boolean = isAvailableOnDataContext(dataContext)

    override fun invoke(project: Project, editor: Editor?, file: PsiFile?, dataContext: DataContext?) {
        val g = geval(editor, file) ?: return
        if (g.indexeren) ProMelding.getInstance().toonHint(editor, ProMelding.HINT_INDEXEREN, project)
        else ProHernoemen.meldGeblokkeerd(project, editor, g.naam, ProHernoemen.opsomming(g.grammaticas.map { it.name }))
    }

    /** Zonder editor (structuurweergave) komt deze handler niet in beeld: daar staan geen namen uit C-code. */
    override fun invoke(project: Project, elements: Array<out PsiElement>, dataContext: DataContext?) {}

    companion object {
        /** Het blad met een naam in Flex-code op [offset] (of net ervoor, cursor achter het woord), of null. */
        fun naamBijCursor(file: PsiFile, offset: Int): PsiElement? {
            for (o in listOf(offset, offset - 1)) {
                if (o < 0) continue
                val blad = file.findElementAt(o) ?: continue
                if (!Koppeling.isNaam(blad.text)) continue
                var k = blad.node.treeParent
                while (k != null) {
                    if (k.elementType in Koppeling.FLEX_CODE) return blad
                    k = k.treeParent
                }
            }
            return null
        }
    }
}
