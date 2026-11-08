package com.dortus.bisonflex.pro

import com.dortus.bisonflex.BisonLanguage
import com.dortus.bisonflex.psi.Koppeling
import com.dortus.bisonflex.psi.Koppeling.ScannerGebruik
import com.dortus.bisonflex.psi.NaamElement
import com.intellij.openapi.editor.Editor
import com.intellij.openapi.project.Project
import com.intellij.psi.PsiElement
import com.intellij.refactoring.rename.RenamePsiElementProcessor
import com.intellij.util.containers.MultiMap
import java.awt.Component

/**
 * Hernoemen (Shift+F6) met de Pro-regel (eis 6, besluit van Jet). Binnen één bestand is hernoemen gratis.
 * Wordt een token uit de grammatica ook in een scanner gebruikt en is er geen licentie (stand GEEN), dan
 * gebeurt er niets: half hernoemen breekt stil de build. In plaats daarvan eenmaal per sessie de balloon over
 * hernoemen ([ProMelding.tekstHernoemen]), daarna de hint die zegt waarom er niets gebeurde
 * ([ProMelding.hintHernoemen]); zonder editor (structuurweergave, projectvenster) als kleine balloon bij de gekozen
 * knoop: we geven het onderdeel met de focus mee (de boom), want deze processor krijgt geen DataContext.
 * Bij ONBEKEND en GELDIG werkt alles, zonder melding.
 *
 * Tijdens het indexeren is niet te weten of een scanner het token gebruikt (Daan, beoordeling 8 punt 4). Dan
 * hernoemen we een token niet (ook niet met licentie: de verwijzingen uit de scanner zijn dan niet te vinden,
 * dus het zou half gaan) en tonen we de neutrale hint [ProMelding.HINT_INDEXEREN], zonder Pro.
 *
 * `substituteElementToRename` die null geeft, breekt het hernoemen af voor het iets verandert; zowel de dialoog
 * als het hernoemen in de editor vragen dit eerst. Shift+F6 in de scanner zelf: zie [ProHernoemenScanner].
 */
class ProHernoemen : RenamePsiElementProcessor() {

    override fun canProcessElement(element: PsiElement): Boolean = element is NaamElement

    /** Een naam die al bestaat zou regels of tokens stil samenvoegen: dat wordt een conflict in het venster. */
    override fun findExistingNameConflicts(element: PsiElement, newName: String, conflicts: MultiMap<PsiElement, String>) {
        val f = element.containingFile ?: return
        if (element !is NaamElement || newName == element.name) return
        val bestaat = if (f.language == BisonLanguage) Koppeling.bisonDoel(f, newName) else Koppeling.startConditie(f, newName)
        if (bestaat != null) conflicts.putValue(element, "'$newName' already exists in ${f.name}")
    }

    override fun substituteElementToRename(element: PsiElement, editor: Editor?): PsiElement? =
        when (val gebruik = Koppeling.scannerGebruik(element)) {
            ScannerGebruik.Nee -> element
            ScannerGebruik.Indexeren -> {
                ProMelding.getInstance().toonHint(editor, ProMelding.HINT_INDEXEREN, element.project, bron(element.project, editor))
                null
            }
            is ScannerGebruik.Ja -> if (Licentie.proWerkt()) element else {
                meldGeblokkeerd(element.project, editor, element.text, opsomming(gebruik.scanners.map { it.name }))
                null
            }
        }

    companion object {
        /** Bestandsnamen als "calc.l" of "calc.l and calc.ll" of "a.l, b.l and c.l" (Engels, zoals de melding). */
        fun opsomming(namen: List<String>): String =
            if (namen.size <= 1) namen.joinToString() else namen.dropLast(1).joinToString() + " and " + namen.last()

        /**
         * Hernoemen van [naam] is tegengehouden omdat het ook [ander] raakt: de eerste keer per sessie de balloon
         * over hernoemen, daarna de korte hint (in [editor], of zonder editor als kleine balloon bij [bron]).
         */
        fun meldGeblokkeerd(project: Project, editor: Editor?, naam: String, ander: String, bron: Component? = bron(project, editor)) {
            val m = ProMelding.getInstance()
            if (!m.toonEenmaal(project, ProMelding.tekstHernoemen(naam, ander), ProMelding.HERNOEMEN)) {
                m.toonHint(editor, ProMelding.hintHernoemen(naam, ander), project, bron)
            }
        }

        /** Zonder editor: het onderdeel met de focus ([ProMelding.focusOnderdeel]), met editor null. */
        fun bron(project: Project, editor: Editor?): Component? =
            if (editor != null) null else ProMelding.focusOnderdeel(project)
    }
}
