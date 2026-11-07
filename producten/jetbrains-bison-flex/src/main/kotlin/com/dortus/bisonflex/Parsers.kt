package com.dortus.bisonflex

import com.dortus.bisonflex.lexer.BisonTokens
import com.dortus.bisonflex.lexer.FlexTokens
import com.dortus.bisonflex.lexer.TokenTypes
import com.dortus.bisonflex.lexer.bisonLexer
import com.dortus.bisonflex.lexer.flexLexer

import com.intellij.extapi.psi.ASTWrapperPsiElement
import com.intellij.extapi.psi.PsiFileBase
import com.intellij.lang.ASTNode
import com.intellij.lang.Language
import com.intellij.lang.ParserDefinition
import com.intellij.lang.PsiBuilder
import com.intellij.lang.PsiParser
import com.intellij.lexer.Lexer
import com.intellij.openapi.fileTypes.FileType
import com.intellij.openapi.project.Project
import com.intellij.psi.FileViewProvider
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiFile
import com.intellij.psi.tree.IFileElementType
import com.intellij.psi.tree.TokenSet

/**
 * Versie 0.1: echte lexer (zie `lexer/`), nog een platte parser: alle tokens direct onder
 * het bestand. De echte parser met regels, tokens en meldingen komt hierna, zie ontwerp.md.
 * Hieronder de vaste elementtypes per taal (globaal register, dus één keer maken).
 */
object BisonTypes {
    @JvmField val BESTAND = IFileElementType(BisonLanguage)
}

object FlexTypes {
    @JvmField val BESTAND = IFileElementType(FlexLanguage)
}

abstract class SkeletParserDefinition(
    private val taal: Language,
    private val soort: () -> FileType,
    private val maakLexer: () -> Lexer,
    private val types: TokenTypes,
    private val bestand: IFileElementType,
) : ParserDefinition {

    override fun createLexer(project: Project?): Lexer = maakLexer()
    override fun createParser(project: Project?): PsiParser = PsiParser { root, builder: PsiBuilder ->
        val m = builder.mark()
        while (!builder.eof()) builder.advanceLexer()
        m.done(root)
        builder.treeBuilt
    }
    override fun getFileNodeType(): IFileElementType = bestand
    override fun getCommentTokens(): TokenSet = types.commentaar
    override fun getStringLiteralElements(): TokenSet = types.strings
    override fun createElement(node: ASTNode): PsiElement = ASTWrapperPsiElement(node)
    override fun createFile(viewProvider: FileViewProvider): PsiFile = object : PsiFileBase(viewProvider, taal) {
        override fun getFileType(): FileType = soort()
        override fun toString(): String = "${taal.id}-bestand"
    }
}

class BisonParserDefinition : SkeletParserDefinition(BisonLanguage, { BisonFileType }, ::bisonLexer, BisonTokens.TYPES, BisonTypes.BESTAND)
class FlexParserDefinition : SkeletParserDefinition(FlexLanguage, { FlexFileType }, ::flexLexer, FlexTokens.TYPES, FlexTypes.BESTAND)
