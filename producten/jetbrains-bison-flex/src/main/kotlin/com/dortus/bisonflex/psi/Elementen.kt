package com.dortus.bisonflex.psi

import com.dortus.bisonflex.BisonLanguage
import com.dortus.bisonflex.parser.BisonElementen as B
import com.dortus.bisonflex.parser.FlexElementen as F
import com.intellij.extapi.psi.ASTWrapperPsiElement
import com.intellij.lang.ASTNode
import com.intellij.navigation.ItemPresentation
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiNameIdentifierOwner
import com.intellij.psi.PsiReference

/**
 * Eigen PSI-klassen voor alle plekken vinden en hernoemen (eis 6). De boom zelf blijft zoals de parser hem maakt;
 * alleen deze knopen krijgen een klasse, de rest blijft `ASTWrapperPsiElement`.
 */
object BisonFlexPsi {
    fun maak(node: ASTNode): PsiElement = when (node.elementType) {
        B.RULE_NAME, B.TOKEN_NAME, F.START_CONDITION_NAME -> NaamElement(node)
        B.SYMBOL_REF, F.START_CONDITION_REF -> SymboolElement(node)
        in Koppeling.BISON_CODE, in Koppeling.FLEX_CODE -> CodeElement(node)
        else -> ASTWrapperPsiElement(node)
    }
}

/**
 * Een definitie: `exp:` (`RULE_NAME`), `%token NUM` (`TOKEN_NAME`, ook in `%left` enz.) of `%x COMMENT`
 * (`START_CONDITION_NAME`). Staat dezelfde naam er vaker (een regel in twee stukken, `%token NUM` en `%left NUM`),
 * dan is de eerste de echte definitie en verwijzen de andere ernaar, zodat hernoemen ze allemaal meeneemt.
 */
class NaamElement(node: ASTNode) : ASTWrapperPsiElement(node), PsiNameIdentifierOwner {
    override fun getName(): String = node.text
    override fun getNameIdentifier(): PsiElement? = node.firstChildNode?.psi

    override fun setName(name: String): PsiElement {
        Koppeling.vervang(node.firstChildNode, name)
        return this
    }

    /** De eerste definitie met deze naam in dit bestand (kan dit element zelf zijn). */
    fun eerste(): PsiElement? {
        val f = containingFile ?: return null
        return when (node.elementType) {
            B.RULE_NAME -> Koppeling.bison(f).regels[name]?.firstOrNull()
            B.TOKEN_NAME -> Koppeling.bisonToken(f, name)
            else -> Koppeling.startConditie(f, name)
        }
    }

    override fun getReference(): PsiReference? {
        val doel = eerste() ?: return null
        return if (doel == this) null else NaarEerste(this, doel)
    }

    /**
     * Wat het kiesmenu toont (Choose declaration bij Ctrl+B, Find Usages Of bij Alt+F7, Shift+F6). Staat een token
     * in calc.y en calc.yy, dan stonden er twee gelijke regels "NUM  calculator" (Daan, beoordeling 13). Het platform
     * (`targetPresentation` in `codeInsight/navigation/util.kt`) zet `locationString` grijs achter de naam: daar
     * komt de bestandsnaam, dus "NUM calc.y" en "NUM calc.yy". De modulenaam rechts zet het platform er zelf bij.
     */
    override fun getPresentation(): ItemPresentation = object : ItemPresentation {
        override fun getPresentableText(): String = name
        override fun getLocationString(): String? = containingFile?.name
        override fun getIcon(unused: Boolean) = containingFile?.getIcon(0)
    }

    override fun toString(): String = "${node.elementType}($name)"
}

/** Een gebruik: `exp` of `NUM` in een regel, `%type`, `%start`, `%prec` (`SYMBOL_REF`), of `<COMMENT>`. */
class SymboolElement(node: ASTNode) : ASTWrapperPsiElement(node) {
    override fun getReference(): PsiReference = SymboolVerwijzing(this)
}

/**
 * C-code: een actie, `%code {}`, proloog of epiloog; in Flex ook `%top{}`, ingesprongen code en de user code. Elke naam erin kan een verwijzing zijn. In Bison naar een token
 * van hetzelfde bestand (`return NUM;` in de epiloog). In Flex naar een start-conditie (`BEGIN(COMMENT)`) of naar
 * een token in de grammatica (`return NUM;`, Pro).
 */
class CodeElement(node: ASTNode) : ASTWrapperPsiElement(node) {
    override fun getReferences(): Array<PsiReference> {
        val f = containingFile ?: return PsiReference.EMPTY_ARRAY
        val bison = language == BisonLanguage
        val begin = node.startOffset
        return Koppeling.bladeren(node)
            .filter { Koppeling.isNaam(it.text) && (!bison || Koppeling.bisonToken(f, it.text) != null) }
            .map { CodeVerwijzing(this, it.startOffset - begin, it.text) }
            .toTypedArray()
    }

    override fun getReference(): PsiReference? = references.firstOrNull()
}
