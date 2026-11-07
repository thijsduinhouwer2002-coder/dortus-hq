package com.dortus.bisonflex

import com.intellij.openapi.fileTypes.LanguageFileType
import com.intellij.openapi.util.IconLoader
import javax.swing.Icon

object BisonIconen {
    @JvmField val BISON: Icon = IconLoader.getIcon("/icons/bison.svg", BisonIconen::class.java)
    @JvmField val FLEX: Icon = IconLoader.getIcon("/icons/flex.svg", BisonIconen::class.java)
}

object BisonFileType : LanguageFileType(BisonLanguage) {
    override fun getName(): String = "Bison"
    override fun getDescription(): String = "Bison/Yacc grammar"
    override fun getDefaultExtension(): String = "y"
    override fun getIcon(): Icon = BisonIconen.BISON
}

object FlexFileType : LanguageFileType(FlexLanguage) {
    override fun getName(): String = "Flex"
    override fun getDescription(): String = "Flex/Lex scanner"
    override fun getDefaultExtension(): String = "l"
    override fun getIcon(): Icon = BisonIconen.FLEX
}
