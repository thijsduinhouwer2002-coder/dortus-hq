package com.dortus.bisonflex.pro

import com.intellij.ui.LicensingFacade
import org.jetbrains.annotations.TestOnly
import java.io.ByteArrayInputStream
import java.security.Signature
import java.security.cert.CertPathBuilder
import java.security.cert.CertPathValidator
import java.security.cert.CertStore
import java.security.cert.Certificate
import java.security.cert.CertificateFactory
import java.security.cert.CollectionCertStoreParameters
import java.security.cert.PKIXBuilderParameters
import java.security.cert.TrustAnchor
import java.security.cert.X509CertSelector
import java.security.cert.X509Certificate
import java.util.Base64
import java.util.concurrent.atomic.AtomicInteger

/**
 * De licentiestand van Bison & Flex Pro (eis 8, ontwerp.md).
 * - ONBEKEND: de IDE heeft de licenties nog niet geladen (`LicensingFacade` is null). Pro werkt, geen melding.
 * - GELDIG: er is een stempel voor [Licentie.PRODUCTCODE] (proef of licentie) met een kloppende handtekening. Pro werkt.
 * - GEEN: de facade is er, maar zonder geldige stempel. Pro werkt niet, wel eenmaal per sessie de Pro-melding.
 */
enum class LicentieStand { ONBEKEND, GELDIG, GEEN }

/** Waar de stand vandaan komt. In de IDE de facade, in unittests een nagebootste bron. */
fun interface LicentieBron {
    fun stand(): LicentieStand
}

/**
 * De echte bron: `LicensingFacade.getConfirmationStamp`, met de stempel gecontroleerd door [StempelControle].
 *
 * Alleen voor de IDE-test: `-Dbisonflex.internal.e2e.forceNoLicense=true` zet de stand op GEEN, omdat de facade
 * in de test-IDE null is en de Pro-melding dan nooit komt.
 */
object FacadeBron : LicentieBron {
    const val E2E_EIGENSCHAP = "bisonflex.internal.e2e.forceNoLicense"

    @Volatile
    private var e2eStand: LicentieStand? = null

    /**
     * Alleen voor de IDE-test (via de Driver): zet halverwege de test een andere stand, bijvoorbeeld GELDIG voor de
     * meldingen van eis 7. Werkt alleen als [E2E_EIGENSCHAP] gezet is, dus nooit bij een gebruiker.
     */
    @JvmStatic
    fun zetE2eStand(stand: String) {
        if (System.getProperty(E2E_EIGENSCHAP) == "true") e2eStand = LicentieStand.valueOf(stand)
    }

    /** Alleen voor unittests: doet alsof de facade er wel of niet is, met deze stempel. `null` gebruikt de echte facade. */
    @Volatile
    private var testFacade: Pair<Boolean, String?>? = null

    @TestOnly
    fun zetFacadeVoorTest(aanwezig: Boolean, stempel: String?) {
        testFacade = aanwezig to stempel
    }

    @TestOnly
    fun wisFacadeVoorTest() {
        testFacade = null
    }

    override fun stand(): LicentieStand {
        if (System.getProperty(E2E_EIGENSCHAP) == "true") return e2eStand ?: LicentieStand.GEEN
        val (aanwezig, stempel) = testFacade ?: LicensingFacade.getInstance().let { facade ->
            (facade != null) to facade?.getConfirmationStamp(Licentie.PRODUCTCODE)
        }
        // nog geen facade (licentiedeel van de IDE nog niet geladen): ONBEKEND, Pro blijft werken (ontwerp.md)
        if (!aanwezig) return LicentieStand.ONBEKEND
        return if (StempelControle.isGeldig(stempel)) LicentieStand.GELDIG else LicentieStand.GEEN
    }
}

/**
 * Controle van de handtekening van een licentiestempel, overgenomen uit het voorbeeld `CheckLicense` van JetBrains
 * (marketplace-makemecoffee-plugin, versie 2024.3+; `eval:` uit de versie voor 2024.2). Zie ontwerp.md,
 * "Ontwerp handtekening licentiestempel".
 *
 * De uitkomst van de laatste stempeltekst wordt onthouden, zodat de cryptografie niet bij elke vraag draait.
 */
object StempelControle {
    private const val KEY_VOORVOEGSEL = "key:"
    private const val STAMP_VOORVOEGSEL = "stamp:"
    private const val EVAL_VOORVOEGSEL = "eval:"

    /** Hoe lang een stempel van de licentieserver geldt, zoals in het voorbeeld. */
    const val TIJDSTEMPEL_GELDIG_MS = 60L * 60 * 1000

    /**
     * Hoe lang een afgekeurde stempel afgekeurd blijft voor we hem opnieuw controleren. Niet voor altijd: een eenmalige
     * fout (klok van de licentieserver net verkeerd, een storing in de cryptografie) mag een betalende klant niet tot de
     * volgende herstart blokkeren. Eén controle per minuut kost niets merkbaars.
     */
    const val AFGEKEURD_OPNIEUW_MS = 60L * 1000

    /** Publieke root-certificaten van JetBrains, letterlijk uit het voorbeeld CheckLicense. */
    private val ROOT_CERTIFICATEN = arrayOf(
        """
        -----BEGIN CERTIFICATE-----
        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
        -----END CERTIFICATE-----
        """.trimIndent(),
        """
        -----BEGIN CERTIFICATE-----
        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
        7tlDFnvaRnQukqSG+VqNWg==
        -----END CERTIFICATE-----
        """.trimIndent(),
    )

    private val echteRoots: List<X509Certificate> by lazy {
        val fabriek = CertificateFactory.getInstance("X.509")
        ROOT_CERTIFICATEN.map {
            fabriek.generateCertificate(ByteArrayInputStream(it.toByteArray(Charsets.UTF_8))) as X509Certificate
        }
    }

    @Volatile
    private var testRoots: List<X509Certificate>? = null

    private val roots: List<X509Certificate> get() = testRoots ?: echteRoots

    /** De onthouden uitkomst voor één stempeltekst, geldig tot [geldigTot] (milliseconden). */
    private class Onthouden(val stempel: String, val geldig: Boolean, val geldigTot: Long)

    @Volatile
    private var onthouden: Onthouden? = null

    private val controles = AtomicInteger()

    /** Is deze stempel geldig voor ons product? Null, leeg of onleesbaar is niet geldig. */
    fun isGeldig(stempel: String?, nu: Long = System.currentTimeMillis()): Boolean {
        if (stempel.isNullOrBlank()) return false
        onthouden?.let { if (it.stempel == stempel && nu < it.geldigTot) return it.geldig }
        controles.incrementAndGet()
        val (geldig, geldigTot) = controleer(stempel, nu)
        onthouden = Onthouden(stempel, geldig, geldigTot)
        return geldig
    }

    /** Uitkomst en tot wanneer die uitkomst mag blijven staan. Afgekeurd blijft hoogstens [AFGEKEURD_OPNIEUW_MS] staan. */
    private fun controleer(stempel: String, nu: Long): Pair<Boolean, Long> {
        val afgekeurd = false to nu + AFGEKEURD_OPNIEUW_MS
        return when {
            // licentie via JetBrains Account of ingevoerd als activeringscode
            stempel.startsWith(KEY_VOORVOEGSEL) ->
                if (isSleutelGeldig(stempel.substring(KEY_VOORVOEGSEL.length))) true to Long.MAX_VALUE else afgekeurd
            // licentie via een ticket van de JetBrains Floating License Server
            stempel.startsWith(STAMP_VOORVOEGSEL) -> {
                val tijd = isServerStempelGeldig(stempel.substring(STAMP_VOORVOEGSEL.length), nu)
                if (tijd != null) true to tijd + TIJDSTEMPEL_GELDIG_MS else afgekeurd
            }
            // proef, zoals het voorbeeld voor 2024.2
            stempel.startsWith(EVAL_VOORVOEGSEL) -> {
                val verval = stempel.substring(EVAL_VOORVOEGSEL.length).toLongOrNull()
                if (verval != null && nu < verval) true to verval else afgekeurd
            }
            else -> afgekeurd
        }
    }

    private fun isSleutelGeldig(sleutel: String): Boolean {
        val delen = sleutel.split("-")
        if (delen.size != 4) return false // verkeerde vorm

        val licentieId = delen[0]
        val licentieBase64 = delen[1]
        val handtekeningBase64 = delen[2]
        val certificaatBase64 = delen[3]

        return try {
            val base64 = Base64.getMimeDecoder()
            val sig = Signature.getInstance("SHA1withRSA")
            // false: geen controle op het verlopen van het certificaat (een sleutel kan ook een blijvende licentie
            // voor oudere versies zijn); het gaat erom dat de sleutel met een echt certificaat van JetBrains is ondertekend
            sig.initVerify(maakCertificaat(base64.decode(certificaatBase64.toByteArray(Charsets.UTF_8)), emptyList(), false))
            val licentieBytes = base64.decode(licentieBase64.toByteArray(Charsets.UTF_8))
            sig.update(licentieBytes)
            if (!sig.verify(base64.decode(handtekeningBase64.toByteArray(Charsets.UTF_8)))) return false
            // zoals het voorbeeld: de licentie-id moet in de ondertekende licentie staan ('least-effort', geen JSON-lezer)
            val licentie = String(licentieBytes, Charsets.UTF_8)
            // geen eigen eis op de productcode: de IDE geeft de stempel al alleen voor PBISONFLEX, en een extra eis die we niet
            // met een echte sleutel kunnen toetsen zou een betalende klant kunnen blokkeren (controleur 8 nov)
            licentie.contains("\"licenseId\":\"$licentieId\"")
        } catch (e: Throwable) {
            false
        }
    }

    /** Geeft het tijdstempel terug als de stempel geldig is, anders null. */
    private fun isServerStempelGeldig(serverStempel: String, nu: Long): Long? {
        try {
            val delen = serverStempel.split(":")
            val base64 = Base64.getMimeDecoder()

            val verwachteMachineId = delen[0]
            val tijdstempel = delen[1].toLong()
            val machineId = delen[2]
            val handtekeningType = delen[3]
            val handtekening = base64.decode(delen[4].toByteArray(Charsets.UTF_8))
            val certificaat = base64.decode(delen[5].toByteArray(Charsets.UTF_8))
            val tussen = (6 until delen.size).map { base64.decode(delen[it].toByteArray(Charsets.UTF_8)) }

            val sig = Signature.getInstance(handtekeningType)
            // true: het certificaat moet nu geldig zijn, een verlopen certificaat van een licentieserver vertrouwen we niet
            sig.initVerify(maakCertificaat(certificaat, tussen, true))
            sig.update("$tijdstempel:$machineId".toByteArray(Charsets.UTF_8))
            if (sig.verify(handtekening)) {
                // de machine-id moet kloppen met het antwoord van de server, en dat antwoord moet vers zijn
                if (verwachteMachineId == machineId && Math.abs(nu - tijdstempel) < TIJDSTEMPEL_GELDIG_MS) return tijdstempel
            }
        } catch (e: Throwable) {
            // stempel ongeldig
        }
        return null
    }

    private fun maakCertificaat(certBytes: ByteArray, tussenBytes: Collection<ByteArray>, nuGeldig: Boolean): X509Certificate {
        val fabriek = CertificateFactory.getInstance("X.509")
        val cert = fabriek.generateCertificate(ByteArrayInputStream(certBytes)) as X509Certificate

        val alle = HashSet<Certificate>()
        alle.add(cert)
        for (bytes in tussenBytes) alle.add(fabriek.generateCertificate(ByteArrayInputStream(bytes)))

        try {
            // het startcertificaat van de keten
            val kiezer = X509CertSelector()
            kiezer.certificate = cert
            val ankers = roots.map { TrustAnchor(it, null) }.toSet()

            val pkix = PKIXBuilderParameters(ankers, kiezer)
            pkix.isRevocationEnabled = false
            if (!nuGeldig) {
                // bewust op de begindatum van het certificaat, zodat het niet afhangt van het moment van controleren
                pkix.date = cert.notBefore
            }
            pkix.addCertStore(CertStore.getInstance("Collection", CollectionCertStoreParameters(alle)))
            // keten bouwen en controleren
            val pad = CertPathBuilder.getInstance("PKIX").build(pkix).certPath
            if (pad != null) {
                CertPathValidator.getInstance("PKIX").validate(pad, pkix)
                return cert
            }
        } catch (e: Exception) {
            // keten klopt niet
        }
        throw Exception("Certificate used to sign the license is not signed by JetBrains root certificate")
    }

    /** Alleen voor tests: andere roots (een eigen testketen); `null` zet de roots van JetBrains terug. Wist ook het geheugen. */
    @TestOnly
    fun zetRootsVoorTest(nieuw: List<X509Certificate>?) {
        testRoots = nieuw
        onthouden = null
    }

    /** Alleen voor tests: hoe vaak de echte controle (cryptografie) gedraaid heeft. */
    @TestOnly
    fun aantalControles(): Int = controles.get()
}

object Licentie {
    /** Zelfde code als `product-descriptor` in plugin.xml. */
    const val PRODUCTCODE = "PBISONFLEX"

    @Volatile
    private var bron: LicentieBron = FacadeBron

    /** Elke keer opnieuw gevraagd: de facade kan later komen, of de proef kan net gestart zijn. */
    fun stand(): LicentieStand = bron.stand()

    /** Pro werkt bij GELDIG en ONBEKEND, alleen niet bij GEEN. */
    fun proWerkt(): Boolean = stand() != LicentieStand.GEEN

    /** Alleen voor tests: een nagebootste licentie zetten; `null` zet de echte bron terug. */
    @TestOnly
    fun zetBronVoorTest(nieuw: LicentieBron?) {
        bron = nieuw ?: FacadeBron
    }
}
