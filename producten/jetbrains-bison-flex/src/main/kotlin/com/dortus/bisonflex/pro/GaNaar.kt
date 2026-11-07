package com.dortus.bisonflex.pro

import com.dortus.bisonflex.BisonFileType
import com.dortus.bisonflex.BisonLanguage
import com.dortus.bisonflex.FlexLanguage
import com.dortus.bisonflex.parser.BisonElementen as B
import com.dortus.bisonflex.parser.FlexElementen as F
import com.intellij.codeInsight.hint.HintManager
import com.intellij.codeInsight.navigation.actions.GotoDeclarationHandler
import com.intellij.ide.IdeEventQueue
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.application.ModalityState
import com.intellij.lang.ASTNode
import com.intellij.openapi.editor.Editor
import com.intellij.openapi.project.DumbService
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiFile
import com.intellij.psi.PsiManager
import com.intellij.psi.search.FileTypeIndex
import com.intellij.psi.search.GlobalSearchScope
import com.intellij.psi.tree.IElementType
import java.awt.AWTEvent
import java.awt.event.KeyEvent
import java.awt.event.MouseEvent

/**
 * Ga naar definitie (eis 6, eerste deel; Pro). Geen eigen PSI-klassen: we zoeken in de boom van de parser.
 * - Bison: `SYMBOL_REF` naar de `RULE_NAME` van die regel, anders naar de `TOKEN_NAME` (eerst in `%token`).
 * - Flex: `START_CONDITION_REF` naar de `START_CONDITION_NAME` in `%x`/`%s`.
 * - Flex: een naam in een actie (`return NUM;`) naar `%token NUM` in een `.y`/`.yy` van het project.
 * Bij stand GEEN: geen sprong, wel eenmaal per sessie de Pro-melding (alleen als er een doel was).
 */
class GaNaarDefinitie(
    /** De gebeurtenis die de vraag veroorzaakt; in tests te vervangen. */
    private val gebeurtenis: () -> AWTEvent? = { IdeEventQueue.getInstance().trueCurrentEvent },
) : GotoDeclarationHandler {

    override fun getGotoDeclarationTargets(bron: PsiElement?, offset: Int, editor: Editor?): Array<PsiElement>? {
        val blad = bron?.node ?: return null
        val doelen = doelen(blad, bron.containingFile ?: return null)
        if (doelen.isEmpty()) return null
        if (!Licentie.proWerkt()) {
            // Ctrl/Cmd+zweven vraagt ook om doelen: dan geen sprong en geen melding, alleen bij een echte actie.
            if (!isZweven(gebeurtenis()) && ProMelding.getInstance().toonEenmaal(bron.project)) verbergNietGevonden()
            return null
        }
        return doelen.toTypedArray()
    }

    /**
     * Zonder doel toont de IDE na deze handler de hint "Cannot find declaration to go to". Die hoort niet naast
     * de Pro-melding. De hint komt op de EDT nadat de actie klaar is; twee keer `invokeLater` (niet-modaal) loopt
     * daarna en haalt hem weg. De balloon is geen editor-hint en blijft staan.
     */
    private fun verbergNietGevonden() {
        val app = ApplicationManager.getApplication()
        app.invokeLater({ app.invokeLater({ HintManager.getInstance().hideAllHints() }, ModalityState.nonModal()) },
            ModalityState.nonModal())
    }

    /** De doelen zonder te letten op de licentie (los te testen). */
    fun doelen(blad: ASTNode, bestand: PsiFile): List<PsiElement> {
        val ouder = blad.treeParent ?: return emptyList()
        val naam = blad.text
        return when (bestand.language) {
            BisonLanguage -> if (ouder.elementType == B.SYMBOL_REF) bisonDoelen(bestand.node, naam) else emptyList()
            FlexLanguage -> when {
                ouder.elementType == F.START_CONDITION_REF ->
                    zoek(bestand.node, F.START_CONDITION_NAME).filter { it.text == naam }.map { it.psi }
                ouder.elementType == F.ACTION && NAAM.matches(naam) -> tokenInGrammatica(bestand, naam)
                else -> emptyList()
            }
            else -> emptyList()
        }
    }

    private fun bisonDoelen(bestand: ASTNode, naam: String): List<PsiElement> {
        val regels = zoek(bestand, B.RULE_NAME).filter { it.text == naam }
        if (regels.isNotEmpty()) return regels.map { it.psi }
        return tokenNamen(bestand, naam)
    }

    /** `TOKEN_NAME`s met deze naam: eerst die in `%token`, anders die in `%left` enz. */
    private fun tokenNamen(bestand: ASTNode, naam: String): List<PsiElement> {
        val alle = zoek(bestand, B.TOKEN_NAME).filter { it.text == naam }
        val inToken = alle.filter { it.treeParent?.elementType == B.TOKEN_DECL }
        return inToken.ifEmpty { alle }.map { it.psi }
    }

    private fun tokenInGrammatica(flex: PsiFile, naam: String): List<PsiElement> {
        val project = flex.project
        if (DumbService.isDumb(project)) return emptyList()
        val psi = PsiManager.getInstance(project)
        return FileTypeIndex.getFiles(BisonFileType, GlobalSearchScope.projectScope(project))
            .sortedBy { it.path }
            .mapNotNull { psi.findFile(it) }
            .flatMap { tokenNamen(it.node, naam) }
    }

    companion object {
        /** Muisbeweging of alleen een losse Ctrl/Cmd/Shift/Alt: dat is zweven (navigatie-hint), geen echte actie. */
        fun isZweven(e: AWTEvent?): Boolean = when (e) {
            is MouseEvent -> e.id == MouseEvent.MOUSE_MOVED || e.id == MouseEvent.MOUSE_DRAGGED ||
                e.id == MouseEvent.MOUSE_ENTERED || e.id == MouseEvent.MOUSE_EXITED || e.id == MouseEvent.MOUSE_WHEEL
            is KeyEvent -> e.keyCode in LOSSE_TOETSEN
            else -> false
        }

        private val LOSSE_TOETSEN = setOf(KeyEvent.VK_CONTROL, KeyEvent.VK_META, KeyEvent.VK_SHIFT, KeyEvent.VK_ALT)
        private val NAAM = Regex("[A-Za-z_][A-Za-z0-9_]*")

        /** Alle knopen van [type] onder [n], in volgorde van het bestand. */
        private fun zoek(n: ASTNode, type: IElementType): List<ASTNode> {
            val uit = ArrayList<ASTNode>()
            fun loop(k: ASTNode) {
                if (k.elementType == type) uit += k
                var c = k.firstChildNode
                while (c != null) { loop(c); c = c.treeNext }
            }
            loop(n)
            return uit
        }
    }
}
