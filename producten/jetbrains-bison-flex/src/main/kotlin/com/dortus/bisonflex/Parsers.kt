package com.dortus.bisonflex

import com.dortus.bisonflex.lexer.BisonTokens
import com.dortus.bisonflex.lexer.FlexTokens
import com.dortus.bisonflex.lexer.TokenTypes
import com.dortus.bisonflex.lexer.bisonLexer
import com.dortus.bisonflex.lexer.flexLexer
import com.dortus.bisonflex.parser.BisonElementen
import com.dortus.bisonflex.parser.BisonParser
import com.dortus.bisonflex.parser.FlexElementen
import com.dortus.bisonflex.parser.FlexParser

import com.intellij.extapi.psi.ASTWrapperPsiElement
import com.intellij.extapi.psi.PsiFileBase
import com.intellij.lang.ASTNode
import com.intellij.lang.Language
import com.intellij.lang.ParserDefinition
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
 * De parserdefinitie per taal: de handgeschreven lexer (`lexer/`) en parser (`parser/`).
 * De elementtypes staan in `parser/Elementen.kt`.
 */
abstract class TaalParserDefinition(
    private val taal: Language,
    private val soort: () -> FileType,
    private val maakLexer: () -> Lexer,
    private val types: TokenTypes,
    private val bestand: IFileElementType,
    private val maakParser: () -> PsiParser,
) : ParserDefinition {

    override fun createLexer(project: Project?): Lexer = maakLexer()
    override fun createParser(project: Project?): PsiParser = maakParser()
    override fun getFileNodeType(): IFileElementType = bestand
    override fun getCommentTokens(): TokenSet = types.commentaar
    override fun getStringLiteralElements(): TokenSet = types.strings
    override fun createElement(node: ASTNode): PsiElement = ASTWrapperPsiElement(node)
    override fun createFile(viewProvider: FileViewProvider): PsiFile = object : PsiFileBase(viewProvider, taal) {
        override fun getFileType(): FileType = soort()
        override fun toString(): String = "${taal.id}-bestand"
    }
}

class BisonParserDefinition : TaalParserDefinition(
    BisonLanguage, { BisonFileType }, ::bisonLexer, BisonTokens.TYPES, BisonElementen.BESTAND, ::BisonParser)
class FlexParserDefinition : TaalParserDefinition(
    FlexLanguage, { FlexFileType }, ::flexLexer, FlexTokens.TYPES, FlexElementen.BESTAND, ::FlexParser)
