package com.dortus.bisonflex

import com.dortus.bisonflex.parser.BisonElementen as B
import com.dortus.bisonflex.parser.FlexElementen as F
import com.intellij.icons.AllIcons
import com.intellij.ide.structureView.StructureViewBuilder
import com.intellij.ide.structureView.StructureViewModel
import com.intellij.ide.structureView.StructureViewModelBase
import com.intellij.ide.structureView.StructureViewTreeElement
import com.intellij.ide.structureView.TreeBasedStructureViewBuilder
import com.intellij.ide.structureView.impl.common.PsiTreeElementBase
import com.intellij.lang.ASTNode
import com.intellij.lang.PsiStructureViewFactory
import com.intellij.openapi.editor.Editor
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiFile
import com.intellij.psi.tree.IElementType
import javax.swing.Icon

/**
 * Structuurweergave per taal, gebouwd op de knopen van de parser (`parser/Elementen.kt`).
 * Alleen ingebouwde iconen van de IDE, en de volgorde zoals in het bestand (geen sorteerders).
 * Klikken springt naar de knoop (de PSI-knoop is een `ASTWrapperPsiElement`, dus navigeerbaar).
 */
class Knoop(
    element: PsiElement,
    private val naam: String,
    private val plek: String?,
    private val icoon: Icon,
    private val kinderen: () -> List<StructureViewTreeElement> = { emptyList() },
) : PsiTreeElementBase<PsiElement>(element) {
    override fun getPresentableText(): String = naam
    override fun getLocationString(): String? = plek
    override fun getIcon(open: Boolean): Icon = icoon
    override fun getChildrenBase(): Collection<StructureViewTreeElement> = kinderen()
}

/** Het bestand zelf: de bovenste knoop (niet zichtbaar). */
private class BestandKnoop(file: PsiFile, private val kinderen: (PsiFile) -> List<StructureViewTreeElement>) :
    PsiTreeElementBase<PsiFile>(file) {
    override fun getPresentableText(): String? = element?.name
    override fun getChildrenBase(): Collection<StructureViewTreeElement> = element?.let(kinderen) ?: emptyList()
}

private fun ASTNode.kinderen(): Sequence<ASTNode> = generateSequence(firstChildNode) { it.treeNext }

/** Alle knopen van [types] onder [n], in volgorde van het bestand (niet dieper dan een gevonden knoop). */
private fun zoek(n: ASTNode, types: Set<IElementType>): List<ASTNode> {
    val uit = ArrayList<ASTNode>()
    fun loop(k: ASTNode) {
        if (k.elementType in types) { uit += k; return }
        k.kinderen().forEach(::loop)
    }
    n.kinderen().forEach(::loop)
    return uit
}

private fun groep(node: ASTNode?, naam: String, kinderen: List<StructureViewTreeElement>): StructureViewTreeElement? =
    if (node == null || kinderen.isEmpty()) null
    else Knoop(node.psi, naam, null, AllIcons.Nodes.Folder) { kinderen }

/** Eén regel tekst, ingekort tot ongeveer [max] tekens. */
fun kort(tekst: String, max: Int = 40): String {
    val een = tekst.replace(Regex("\\s+"), " ").trim()
    return if (een.length <= max) een else een.take(max - 1) + "…"
}

private class Model(file: PsiFile, editor: Editor?, root: StructureViewTreeElement, private val soorten: Set<IElementType>) :
    StructureViewModelBase(file, editor, root), StructureViewModel.ElementInfoProvider {
    override fun isAlwaysShowsPlus(element: StructureViewTreeElement): Boolean = false
    override fun isAlwaysLeaf(element: StructureViewTreeElement): Boolean = false
    override fun isSuitable(element: PsiElement?): Boolean = element?.node?.elementType in soorten
}

abstract class TaalStructuur : PsiStructureViewFactory {
    abstract fun bovenste(file: PsiFile): List<StructureViewTreeElement>
    abstract val soorten: Set<IElementType>

    fun model(file: PsiFile, editor: Editor?): StructureViewModel =
        Model(file, editor, BestandKnoop(file, ::bovenste), soorten)

    override fun getStructureViewBuilder(psiFile: PsiFile): StructureViewBuilder = object : TreeBasedStructureViewBuilder() {
        override fun createStructureViewModel(editor: Editor?): StructureViewModel = model(psiFile, editor)
        override fun isRootNodeShown(): Boolean = false
    }
}

/** Bison: "Declarations" (tokens, `%type`/`%nterm`-namen, `%start`) en "Rules". */
class BisonStructuur : TaalStructuur() {
    override val soorten = setOf(B.TOKEN_NAME, B.SYMBOL_REF, B.RULE)

    override fun bovenste(file: PsiFile): List<StructureViewTreeElement> {
        val bestand = file.node
        val decl = bestand.findChildByType(B.DECLARATIONS)
        val regels = bestand.findChildByType(B.RULES)
        return listOfNotNull(
            groep(decl, "Declarations", decl?.let(::declaraties) ?: emptyList()),
            groep(regels, "Rules", regels?.let(::regels) ?: emptyList()),
        )
    }

    /**
     * Namen uit `%token`, `%type`/`%nterm` en `%start`, plus tokennamen die alleen in
     * `%left`/`%right`/`%nonassoc`/`%precedence` staan (tekenliteralen zoals `'+'` zijn geen
     * TOKEN_NAME en vallen dus weg). Een naam die al in een `%token` staat komt één keer, op die plek.
     */
    private fun declaraties(decl: ASTNode): List<StructureViewTreeElement> {
        val alle = zoek(decl, setOf(B.TOKEN_DECL, B.TYPE_DECL, B.NTERM_DECL, B.START) + VOORRANG)
        val gezien = alle.filter { it.elementType == B.TOKEN_DECL }
            .flatMap { zoek(it, setOf(B.TOKEN_NAME)) }.mapTo(HashSet()) { it.text }
        return alle.flatMap { d ->
            val opdracht = d.firstChildNode?.text
            when (d.elementType) {
                B.TOKEN_DECL -> zoek(d, setOf(B.TOKEN_NAME)).map { Knoop(it.psi, it.text, opdracht, AllIcons.Nodes.Constant) }
                in VOORRANG -> zoek(d, setOf(B.TOKEN_NAME)).filter { gezien.add(it.text) }
                    .map { Knoop(it.psi, it.text, opdracht, AllIcons.Nodes.Constant) }
                B.START -> zoek(d, setOf(B.SYMBOL_REF)).map { Knoop(it.psi, it.text, opdracht, AllIcons.Nodes.EntryPoints) }
                else -> zoek(d, setOf(B.SYMBOL_REF)).map { Knoop(it.psi, it.text, opdracht, AllIcons.Nodes.Type) }
            }
        }
    }

    private companion object {
        val VOORRANG = setOf(B.LEFT, B.RIGHT, B.NONASSOC, B.PRECEDENCE)
    }

    private fun regels(regels: ASTNode): List<StructureViewTreeElement> =
        zoek(regels, setOf(B.RULE)).map { r ->
            Knoop(r.psi, r.findChildByType(B.RULE_NAME)?.text ?: kort(r.text), null, AllIcons.Nodes.Method)
        }
}

/** Flex: "Definitions" (naamdefinities en start-condities) en "Rules" (patronen en `<SC>`-blokken). */
class FlexStructuur : TaalStructuur() {
    override val soorten = setOf(F.DEFINITION_NAME, F.START_CONDITION_NAME, F.FLEX_RULE, F.SC_BLOCK)

    override fun bovenste(file: PsiFile): List<StructureViewTreeElement> {
        val bestand = file.node
        val defs = bestand.findChildByType(F.DEFINITIONS)
        val regels = bestand.findChildByType(F.RULES)
        return listOfNotNull(
            groep(defs, "Definitions", defs?.let(::definities) ?: emptyList()),
            groep(regels, "Rules", regels?.let(::regels) ?: emptyList()),
        )
    }

    private fun definities(defs: ASTNode): List<StructureViewTreeElement> =
        zoek(defs, setOf(F.NAME_DEF, F.START_CONDITION_DECL)).flatMap { d ->
            if (d.elementType == F.NAME_DEF) {
                val naam = d.findChildByType(F.DEFINITION_NAME) ?: return@flatMap emptyList()
                listOf(Knoop(naam.psi, naam.text, d.findChildByType(F.PATTERN)?.text?.let { kort(it) }, AllIcons.Nodes.Variable))
            } else {
                val opdracht = d.firstChildNode?.text
                zoek(d, setOf(F.START_CONDITION_NAME)).map { Knoop(it.psi, it.text, opdracht, AllIcons.Nodes.Tag) }
            }
        }

    private fun regels(n: ASTNode): List<StructureViewTreeElement> =
        zoek(n, setOf(F.FLEX_RULE, F.SC_BLOCK)).map { r ->
            if (r.elementType == F.SC_BLOCK) {
                val condities = r.kinderen().takeWhile { it.elementType == F.SC_LIST }.joinToString("") { it.text }
                Knoop(r.psi, condities, null, AllIcons.Nodes.Tag) { regels(r) }
            } else {
                // Condities plus patroon, zoals in het bestand (zonder de actie).
                val kop = r.kinderen().filter { it.elementType == F.SC_LIST || it.elementType == F.PATTERN }
                    .joinToString("") { it.text }
                Knoop(r.psi, kort(kop.ifEmpty { r.text }), null, AllIcons.Nodes.Method)
            }
        }
}
