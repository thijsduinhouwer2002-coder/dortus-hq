package com.dortus.bisonflex.pro

import com.intellij.openapi.actionSystem.ActionManager
import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.actionSystem.AnActionResult
import com.intellij.openapi.actionSystem.IdeActions
import com.intellij.openapi.actionSystem.ex.AnActionListener
import java.util.concurrent.atomic.AtomicInteger

/**
 * Weet of er nu een echte ga-naar-actie bezig is (Ctrl+B, Ctrl+klik, het menu Navigate). Alleen dan mag
 * [GaNaarDefinitie] de Pro-melding of de hint tonen; Ctrl+zweven vraagt ook om doelen, maar zonder actie.
 *
 * Waarom zo (broncode IntelliJ Community, tak 252):
 * - Ctrl+zweven: `CtrlMouseHandler2` (CtrlMouseHandler.kt) roept bij een muisbeweging met Ctrl
 *   `GotoDeclarationAction.getCtrlMouseData` aan op `Dispatchers.Default` in een read-action, dus op een
 *   achtergronddraad buiten elke actie. Daar is `IdeEventQueue.trueCurrentEvent` niet de muisbeweging; daarom werkte
 *   de oude herkenning (`isZweven`) in de echte IDE niet (IDE-run 42389630766).
 * - Ctrl+B en het menu: `GotoDeclarationAction.actionPerformed` gaat naar `GotoDeclarationOrUsageHandler2.invoke`,
 *   dat de doelen in `underModalProgress` berekent en daarop wacht. Dat gebeurt dus tussen `beforeActionPerformed` en
 *   `afterActionPerformed`, mogelijk op een andere draad. Daarom een gewone teller voor de hele IDE, geen ThreadLocal.
 * - Ctrl+klik: `CtrlMouseHandler2` doet bij loslaten alleen opruimen; de klik zelf loopt via de muissnelkoppeling
 *   (Ctrl+knop 1) van de keymap naar dezelfde actie `GotoDeclaration`, met dezelfde luisteraars.
 * Een teller in plaats van een vlag, zodat een actie binnen een actie de vlag niet te vroeg wist.
 */
class GaNaarActie : AnActionListener {

    override fun beforeActionPerformed(action: AnAction, event: AnActionEvent) {
        if (isGaNaar(action)) bezig.incrementAndGet()
    }

    override fun afterActionPerformed(action: AnAction, event: AnActionEvent, result: AnActionResult) {
        if (isGaNaar(action)) bezig.updateAndGet { if (it > 0) it - 1 else 0 }
    }

    companion object {
        /** De acties die een [GaNaarDefinitie] aanroepen (id's uit de IDE, gecontroleerd in GaNaarActieTest). */
        val ACTIES = setOf(IdeActions.ACTION_GOTO_DECLARATION, "GotoDeclarationOnly", IdeActions.ACTION_GOTO_TYPE_DECLARATION)

        private val bezig = AtomicInteger(0)

        /** Of er nu een ga-naar-actie bezig is. */
        fun isBezig(): Boolean = bezig.get() > 0

        private fun isGaNaar(action: AnAction): Boolean = ActionManager.getInstance().getId(action) in ACTIES
    }
}
