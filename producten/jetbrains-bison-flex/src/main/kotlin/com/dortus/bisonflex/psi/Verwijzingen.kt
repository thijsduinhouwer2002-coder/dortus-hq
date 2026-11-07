package com.dortus.bisonflex.psi

import com.dortus.bisonflex.BisonLanguage
import com.dortus.bisonflex.pro.Licentie
import com.intellij.openapi.util.TextRange
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiElementResolveResult
import com.intellij.psi.PsiPolyVariantReferenceBase
import com.intellij.psi.PsiReferenceBase
import com.intellij.psi.ResolveResult

/**
 * De verwijzingen voor alle plekken vinden en hernoemen (eis 6). Gratis en Pro (Jet, zelfde regel als ga naar
 * definitie): binnen één bestand altijd. Alleen [CodeVerwijzing] kan naar een ander bestand gaan (Flex-actie naar
 * `%token` in een `.y`); die werkt alleen als [Licentie.proWerkt]. Zonder licentie vindt alle plekken dus alleen
 * plekken in het eigen bestand; hernoemen dat het andere bestand raakt houdt `pro/ProHernoemen.kt` tegen.
 */

/** Hernoemt het blad op [plek] (binnen [el]) en geeft [el] terug. */
private fun hernoemBlad(el: PsiElement, plek: TextRange, nieuw: String): PsiElement {
    Koppeling.vervang(el.node.findLeafElementAt(plek.startOffset), nieuw)
    return el
}

/** `SYMBOL_REF` naar de regel of het token, `START_CONDITION_REF` naar `%x`/`%s`; altijd in hetzelfde bestand. */
class SymboolVerwijzing(el: SymboolElement) :
    PsiReferenceBase<SymboolElement>(el, TextRange(0, el.node.firstChildNode?.textLength ?: el.textLength)) {

    override fun resolve(): PsiElement? {
        val f = element.containingFile ?: return null
        val naam = value
        return if (element.language == BisonLanguage) Koppeling.bisonDoel(f, naam) else Koppeling.startConditie(f, naam)
    }

    override fun handleElementRename(nieuw: String): PsiElement = hernoemBlad(element, rangeInElement, nieuw)
}

/** Een tweede definitie met dezelfde naam (`%left NUM` na `%token NUM`, een regel in twee stukken) naar de eerste. */
class NaarEerste(el: NaamElement, private val doel: PsiElement) :
    PsiReferenceBase<NaamElement>(el, TextRange(0, el.textLength)) {
    override fun resolve(): PsiElement = doel
    override fun handleElementRename(nieuw: String): PsiElement = element.setName(nieuw)
}

/** Een naam in C-code. Zacht: een naam die nergens heen gaat (`yytext`, `atof`) is geen fout. */
class CodeVerwijzing(el: CodeElement, begin: Int, private val naam: String) :
    PsiPolyVariantReferenceBase<CodeElement>(el, TextRange(begin, begin + naam.length), true) {

    override fun multiResolve(incompleteCode: Boolean): Array<ResolveResult> {
        val f = element.containingFile ?: return ResolveResult.EMPTY_ARRAY
        val doelen: List<PsiElement> = if (element.language == BisonLanguage) {
            listOfNotNull(Koppeling.bisonToken(f, naam))
        } else {
            Koppeling.startConditie(f, naam)?.let { listOf(it) }
                // Naar een ander bestand: Pro.
                ?: if (Licentie.proWerkt()) Koppeling.tokensVoorScanner(f, naam) else emptyList()
        }
        return doelen.map { PsiElementResolveResult(it) }.toTypedArray()
    }

    override fun handleElementRename(nieuw: String): PsiElement = hernoemBlad(element, rangeInElement, nieuw)
}
