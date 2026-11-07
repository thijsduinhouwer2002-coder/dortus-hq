package com.dortus.bisonflex.psi

import com.dortus.bisonflex.BisonFileType
import com.dortus.bisonflex.FlexFileType
import com.dortus.bisonflex.parser.BisonElementen as B
import com.dortus.bisonflex.parser.FlexElementen as F
import com.intellij.lang.ASTNode
import com.intellij.openapi.project.DumbService
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiFile
import com.intellij.psi.PsiManager
import com.intellij.psi.impl.source.tree.LeafElement
import com.intellij.psi.search.FileTypeIndex
import com.intellij.psi.search.GlobalSearchScope
import com.intellij.psi.tree.IElementType
import com.intellij.psi.util.CachedValueProvider
import com.intellij.psi.util.CachedValuesManager
import com.intellij.psi.util.PsiModificationTracker

/**
 * Wat waar gedefinieerd staat, per bestand bewaard tot de volgende wijziging (eis 6). Kijkt NIET naar de licentie:
 * dat doen de verwijzingen ([CodeVerwijzing]) en het hernoemen (`pro/ProHernoemen.kt`).
 */
object Koppeling {
    /** Knopen met C-code. Een naam erin kan een token of start-conditie zijn (`BEGIN(C)` in de user code). */
    val BISON_CODE: Set<IElementType> = setOf(B.ACTION, B.CODE_BLOCK, B.PROLOGUE, B.EPILOGUE)
    val FLEX_CODE: Set<IElementType> = setOf(F.ACTION, F.PROLOGUE, F.TOP_BLOCK, F.CODE, F.USER_CODE)

    private val NAAM = Regex("[A-Za-z_][A-Za-z0-9_]*")
    fun isNaam(t: CharSequence) = NAAM.matches(t)

    /** Bison: regels en tokens op naam, in volgorde van het bestand; tokens uit `%token` eerst. */
    class BisonNamen(val regels: Map<String, List<PsiElement>>, val tokens: Map<String, List<PsiElement>>)

    /** Flex: start-condities op naam, en alle namen die in acties voorkomen. */
    class FlexNamen(val condities: Map<String, List<PsiElement>>, val inActies: Set<String>)

    fun bison(f: PsiFile): BisonNamen = CachedValuesManager.getCachedValue(f) {
        val regels = LinkedHashMap<String, MutableList<PsiElement>>()
        val inToken = LinkedHashMap<String, MutableList<PsiElement>>()
        val anders = LinkedHashMap<String, MutableList<PsiElement>>()
        for (k in zoek(f.node, setOf(B.RULE_NAME, B.TOKEN_NAME))) {
            val doel = when {
                k.elementType == B.RULE_NAME -> regels
                k.treeParent?.elementType == B.TOKEN_DECL -> inToken
                else -> anders
            }
            doel.getOrPut(k.text) { ArrayList() } += k.psi
        }
        for ((n, l) in anders) inToken.getOrPut(n) { ArrayList() } += l
        CachedValueProvider.Result.create(BisonNamen(regels, inToken), PsiModificationTracker.MODIFICATION_COUNT)
    }

    fun flex(f: PsiFile): FlexNamen = CachedValuesManager.getCachedValue(f) {
        val condities = LinkedHashMap<String, MutableList<PsiElement>>()
        for (k in zoek(f.node, setOf(F.START_CONDITION_NAME))) condities.getOrPut(k.text) { ArrayList() } += k.psi
        val inActies = HashSet<String>()
        for (a in zoek(f.node, FLEX_CODE)) bladeren(a).filter { isNaam(it.text) }.forEach { inActies += it.text }
        CachedValueProvider.Result.create(FlexNamen(condities, inActies), PsiModificationTracker.MODIFICATION_COUNT)
    }

    /** Waar een `SYMBOL_REF` heen gaat: de eerste regel met die naam, anders het eerste token. */
    fun bisonDoel(f: PsiFile, naam: String): PsiElement? {
        val n = bison(f)
        return n.regels[naam]?.firstOrNull() ?: n.tokens[naam]?.firstOrNull()
    }

    fun bisonToken(f: PsiFile, naam: String): PsiElement? = bison(f).tokens[naam]?.firstOrNull()

    fun startConditie(f: PsiFile, naam: String): PsiElement? = flex(f).condities[naam]?.firstOrNull()

    /**
     * De grammatica's (`.y`/`.yy`) waarvoor [heeft] klopt, gesorteerd op pad. Staat er een in dezelfde map als
     * [scanner], dan alleen die uit die map (koppeling `.l` naar `.y`). Leeg tijdens het indexeren.
     */
    fun grammaticas(scanner: PsiFile, heeft: (PsiFile) -> Boolean): List<PsiFile> {
        val project = scanner.project
        if (DumbService.isDumb(project)) return emptyList()
        val psi = PsiManager.getInstance(project)
        val alle = FileTypeIndex.getFiles(BisonFileType, GlobalSearchScope.projectScope(project))
            .sortedBy { it.path }
            .mapNotNull { psi.findFile(it) }
            .filter(heeft)
        val map = scanner.originalFile.virtualFile?.parent
        return alle.filter { it.virtualFile?.parent == map }.ifEmpty { alle }
    }

    /** De tokens met [naam] waar een actie in [scanner] heen gaat (een per grammatica). */
    fun tokensVoorScanner(scanner: PsiFile, naam: String): List<PsiElement> =
        grammaticas(scanner) { bisonToken(it, naam) != null }.mapNotNull { bisonToken(it, naam) }

    /**
     * Of een token uit een grammatica ook in een scanner gebruikt wordt (ongeacht de licentie). Dan raakt
     * hernoemen ook dat andere bestand.
     */
    fun gebruiktInScanner(token: PsiElement): Boolean {
        if (token.node.elementType != B.TOKEN_NAME) return false
        val naam = token.text
        val project = token.project
        if (DumbService.isDumb(project)) return true
        val psi = PsiManager.getInstance(project)
        val grammatica = token.containingFile ?: return false
        val eerste = bisonToken(grammatica, naam)
        return FileTypeIndex.getFiles(FlexFileType, GlobalSearchScope.projectScope(project)).any { vf ->
            val f = psi.findFile(vf) ?: return@any false
            naam in flex(f).inActies && startConditie(f, naam) == null && eerste in tokensVoorScanner(f, naam)
        }
    }

    /** Vervangt de tekst van een blad, met hetzelfde tokentype (voor hernoemen). */
    fun vervang(blad: ASTNode?, tekst: String) {
        (blad as? LeafElement)?.replaceWithText(tekst)
    }

    /** Alle bladeren onder [n], in volgorde. */
    fun bladeren(n: ASTNode): List<ASTNode> {
        val uit = ArrayList<ASTNode>()
        fun loop(k: ASTNode) {
            if (k.firstChildNode == null) { if (k.textLength > 0) uit += k; return }
            var c = k.firstChildNode
            while (c != null) { loop(c); c = c.treeNext }
        }
        loop(n)
        return uit
    }

    /** Alle knopen van een van [types] onder [n], in volgorde van het bestand. */
    fun zoek(n: ASTNode, types: Set<IElementType>): List<ASTNode> {
        val uit = ArrayList<ASTNode>()
        fun loop(k: ASTNode) {
            if (k.elementType in types) uit += k
            var c = k.firstChildNode
            while (c != null) { loop(c); c = c.treeNext }
        }
        loop(n)
        return uit
    }
}
