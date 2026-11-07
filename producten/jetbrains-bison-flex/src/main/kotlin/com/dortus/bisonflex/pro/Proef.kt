package com.dortus.bisonflex.pro

import com.intellij.ide.BrowserUtil
import com.intellij.openapi.actionSystem.ActionManager
import com.intellij.openapi.actionSystem.ActionPlaces
import com.intellij.openapi.actionSystem.ActionUiKind
import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.actionSystem.DataContext
import com.intellij.openapi.actionSystem.DataKey
import com.intellij.openapi.actionSystem.Presentation
import com.intellij.openapi.actionSystem.ex.ActionUtil
import com.intellij.openapi.actionSystem.impl.SimpleDataContext
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.application.ModalityState

/**
 * "Start free trial" in de Pro-melding (Daan, beoordeling 6 punt 2): de registratie in de IDE (Help, Register) met
 * onze plugin al gekozen, zodat de proef met één klik start. Zoals het officiële JetBrains-voorbeeld voor betaalde
 * plugins (marketplace-makemecoffee-plugin, CheckLicense.requestLicense): eerst de actie `RegisterPlugins` (open
 * IDE's zoals IDEA Community), anders `Register` (betaalde IDE's), aangeroepen met een DataContext met de code uit de
 * `product-descriptor` en een korte uitleg. Op de EDT en niet-modaal. Is geen van beide acties er, dan de Marketplace
 * in de browser.
 */
object Proef {
    /** Zelfde code als `product-descriptor` in plugin.xml. */
    const val CODE = "PBISONFLEX"
    const val UITLEG = "Go to declaration across grammar and scanner is part of Bison & Flex Pro."
    /** Terugval zonder registratie-actie (de id van onze pluginpagina is er pas na het indienen, architectuur.md). */
    const val KOOPPAGINA = "https://plugins.jetbrains.com/"
    val ACTIES = listOf("RegisterPlugins", "Register")

    /** De sleutels die de registratie-acties lezen (namen uit de documentatie van JetBrains Marketplace). */
    val CODE_SLEUTEL: DataKey<String> = DataKey.create("register.product-descriptor.code")
    val UITLEG_SLEUTEL: DataKey<String> = DataKey.create("register.message")

    /** Start de proef. [zoek] en [browser] zijn in tests te vervangen. */
    fun start(
        zoek: (String) -> AnAction? = { ActionManager.getInstance().getAction(it) },
        browser: (String) -> Unit = { BrowserUtil.browse(it) },
    ) {
        ApplicationManager.getApplication().invokeLater({
            val actie = ACTIES.firstNotNullOfOrNull(zoek)
            if (actie == null) {
                browser(KOOPPAGINA)
            } else {
                ActionUtil.performAction(
                    actie,
                    AnActionEvent.createEvent(context(), Presentation(), ActionPlaces.NOTIFICATION, ActionUiKind.NONE, null),
                )
            }
        }, ModalityState.nonModal())
    }

    fun context(): DataContext = SimpleDataContext.builder()
        .add(CODE_SLEUTEL, CODE)
        .add(UITLEG_SLEUTEL, UITLEG)
        .build()
}
