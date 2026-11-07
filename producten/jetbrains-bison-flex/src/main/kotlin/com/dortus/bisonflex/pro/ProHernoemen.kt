package com.dortus.bisonflex.pro

import com.dortus.bisonflex.psi.Koppeling
import com.dortus.bisonflex.psi.NaamElement
import com.intellij.openapi.editor.Editor
import com.intellij.psi.PsiElement
import com.intellij.refactoring.rename.RenamePsiElementProcessor

/**
 * Hernoemen (Shift+F6) met de Pro-regel (eis 6, besluit van Jet). Binnen één bestand is hernoemen gratis.
 * Wordt een token uit de grammatica ook in een scanner gebruikt en is er geen licentie (stand GEEN), dan
 * gebeurt er niets: half hernoemen breekt stil de build. In plaats daarvan eenmaal per sessie de Pro-melding,
 * daarna de korte hint [ProMelding.HINT_HERNOEMEN]. Bij ONBEKEND en GELDIG werkt alles, zonder melding.
 *
 * `substituteElementToRename` die null geeft, breekt het hernoemen af voor het iets verandert; zowel de dialoog
 * als het hernoemen in de editor vragen dit eerst.
 */
class ProHernoemen : RenamePsiElementProcessor() {

    override fun canProcessElement(element: PsiElement): Boolean = element is NaamElement

    override fun substituteElementToRename(element: PsiElement, editor: Editor?): PsiElement? {
        if (Licentie.proWerkt() || !Koppeling.gebruiktInScanner(element)) return element
        val melding = ProMelding.getInstance()
        if (!melding.toonEenmaal(element.project) && editor != null) melding.toonHint(editor, ProMelding.HINT_HERNOEMEN)
        return null
    }
}
