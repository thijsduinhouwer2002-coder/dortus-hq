package com.dortus.bisonflex

import com.intellij.extapi.psi.PsiFileBase
import com.intellij.lang.ASTNode
import com.intellij.lang.Language
import com.intellij.lang.ParserDefinition
import com.intellij.lang.PsiBuilder
import com.intellij.lang.PsiParser
import com.intellij.lexer.Lexer
import com.intellij.lexer.LexerBase
import com.intellij.openapi.fileTypes.FileType
import com.intellij.openapi.project.Project
import com.intellij.psi.FileViewProvider
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiFile
import com.intellij.psi.impl.source.tree.LeafPsiElement
import com.intellij.psi.tree.IElementType
import com.intellij.psi.tree.IFileElementType
import com.intellij.psi.tree.TokenSet

/**
 * Skelet (versie 0): de hele tekst is één token. Zo herkent de IDE de soort en
 * is er een geldige PSI-boom. De echte lexer (JFlex) en parser (Grammar-Kit)
 * komen hierna, zie ontwerp.md.
 */
class HeleTekstLexer(private val token: IElementType) : LexerBase() {
    private var buffer: CharSequence = ""
    private var start = 0
    private var end = 0
    private var pos = 0

    override fun start(buffer: CharSequence, startOffset: Int, endOffset: Int, initialState: Int) {
        this.buffer = buffer; start = startOffset; end = endOffset; pos = startOffset
    }
    override fun getState(): Int = 0
    override fun getTokenType(): IElementType? = if (pos < end) token else null
    override fun getTokenStart(): Int = pos
    override fun getTokenEnd(): Int = end
    override fun advance() { pos = end }
    override fun getBufferSequence(): CharSequence = buffer
    override fun getBufferEnd(): Int = end
}

abstract class SkeletParserDefinition(
    private val taal: Language,
    private val soort: () -> FileType,
) : ParserDefinition {
    private val tekst = IElementType("TEKST", taal)
    private val bestand = IFileElementType(taal)

    override fun createLexer(project: Project?): Lexer = HeleTekstLexer(tekst)
    override fun createParser(project: Project?): PsiParser = PsiParser { root, builder: PsiBuilder ->
        val m = builder.mark()
        while (!builder.eof()) builder.advanceLexer()
        m.done(root)
        builder.treeBuilt
    }
    override fun getFileNodeType(): IFileElementType = bestand
    override fun getCommentTokens(): TokenSet = TokenSet.EMPTY
    override fun getStringLiteralElements(): TokenSet = TokenSet.EMPTY
    override fun createElement(node: ASTNode): PsiElement = LeafPsiElement(node.elementType, node.text)
    override fun createFile(viewProvider: FileViewProvider): PsiFile = object : PsiFileBase(viewProvider, taal) {
        override fun getFileType(): FileType = soort()
        override fun toString(): String = "${taal.id}-bestand"
    }
}

class BisonParserDefinition : SkeletParserDefinition(BisonLanguage, { BisonFileType })
class FlexParserDefinition : SkeletParserDefinition(FlexLanguage, { FlexFileType })
