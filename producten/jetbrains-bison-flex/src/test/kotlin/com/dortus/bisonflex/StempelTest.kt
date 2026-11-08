package com.dortus.bisonflex

import com.dortus.bisonflex.pro.StempelControle
import junit.framework.TestCase
import java.io.File
import java.security.KeyFactory
import java.security.PrivateKey
import java.security.Signature
import java.security.cert.CertificateFactory
import java.security.cert.X509Certificate
import java.security.spec.PKCS8EncodedKeySpec
import java.util.Base64

/**
 * Handtekening van de licentiestempel (Moet in 1.0 punt 6, ontwerp.md). Een echte sleutel van JetBrains hebben we niet,
 * dus de positieve gevallen gebruiken een eigen testketen uit `testdata/handtekening/` (test-root ondertekent test-blad;
 * vreemd-blad is ondertekend door een root die niet vertrouwd wordt).
 */
class StempelTest : TestCase() {

    private val map get() = File(System.getProperty("dortus.testdata")).resolve("handtekening")
    private val fabriek = CertificateFactory.getInstance("X.509")
    private val b64 = Base64.getEncoder()

    private fun cert(naam: String) =
        map.resolve(naam).inputStream().use { fabriek.generateCertificate(it) as X509Certificate }

    private fun sleutel(naam: String): PrivateKey {
        val pem = map.resolve(naam).readText().lines().filter { !it.startsWith("-----") }.joinToString("")
        return KeyFactory.getInstance("RSA").generatePrivate(PKCS8EncodedKeySpec(Base64.getDecoder().decode(pem)))
    }

    private fun onderteken(data: ByteArray, sleutel: PrivateKey, type: String = "SHA1withRSA"): ByteArray =
        Signature.getInstance(type).run { initSign(sleutel); update(data); sign() }

    private fun licentie(id: String = "ABC123", code: String = "PBISONFLEX") =
        """{"licenseId":"$id","licenseeName":"Test","products":[{"code":"$code","paidUpTo":"2099-01-01"}]}"""

    private fun keyStempel(
        id: String = "ABC123",
        tekst: String = licentie(),
        blad: String = "test",
        handtekening: ByteArray? = null,
    ): String {
        val bytes = tekst.toByteArray()
        val sig = handtekening ?: onderteken(bytes, sleutel("$blad-blad.key"))
        val c = cert("$blad-blad.pem").encoded
        return "key:$id-${b64.encodeToString(bytes)}-${b64.encodeToString(sig)}-${b64.encodeToString(c)}"
    }

    private fun stampStempel(tijd: Long, verwacht: String = "M1", machine: String = "M1"): String {
        val sig = onderteken("$tijd:$machine".toByteArray(), sleutel("test-blad.key"), "SHA256withRSA")
        val c = cert("test-blad.pem").encoded
        return "stamp:$verwacht:$tijd:$machine:SHA256withRSA:${b64.encodeToString(sig)}:${b64.encodeToString(c)}"
    }

    override fun setUp() {
        super.setUp()
        StempelControle.zetRootsVoorTest(listOf(cert("test-root.pem")))
    }

    override fun tearDown() {
        StempelControle.zetRootsVoorTest(null)
        super.tearDown()
    }

    fun testLeegEnRommelZijnGeen() {
        for (s in listOf(null, "", "   ", "rommel", "key:", "key:a-b-c", "key:a-b-c-d", "stamp:", "stamp:x:y", "eval:", "eval:morgen", "KEY:x")) {
            assertFalse("stempel '$s'", StempelControle.isGeldig(s))
        }
    }

    fun testGoedOndertekendeSleutelIsGeldig() {
        assertTrue(StempelControle.isGeldig(keyStempel()))
    }

    fun testVeranderdeLicentieOfHandtekeningIsGeen() {
        val goed = keyStempel()
        val delen = goed.removePrefix("key:").split("-")
        val anderTekst = b64.encodeToString(licentie().replace("2099", "2100").toByteArray())
        assertFalse(StempelControle.isGeldig("key:${delen[0]}-$anderTekst-${delen[2]}-${delen[3]}"))
        val sig = onderteken(licentie().toByteArray(), sleutel("test-blad.key")).also { it[10] = (it[10] + 1).toByte() }
        assertFalse(StempelControle.isGeldig(keyStempel(handtekening = sig)))
    }

    fun testProductcodeWordtNietApartGeeist() {
        // zoals het voorbeeld van JetBrains: de IDE geeft de stempel al alleen voor onze code (zie Licentie.kt)
        assertTrue(StempelControle.isGeldig(keyStempel(tekst = licentie(code = "PMAKECOFFEE"))))
    }

    fun testAndereLicentieIdIsGeen() {
        assertFalse(StempelControle.isGeldig(keyStempel(id = "XYZ999")))
    }

    fun testCertificaatVanVreemdeRootIsGeen() {
        assertFalse(StempelControle.isGeldig(keyStempel(blad = "vreemd")))
    }

    fun testMetDeRootsVanJetBrainsIsOnzeTestsleutelGeen() {
        StempelControle.zetRootsVoorTest(null)
        assertFalse(StempelControle.isGeldig(keyStempel()))
    }

    fun testServerStempel() {
        val nu = System.currentTimeMillis()
        assertTrue(StempelControle.isGeldig(stampStempel(nu - 60_000), nu))
        assertFalse("te oud", StempelControle.isGeldig(stampStempel(nu - 2 * 3_600_000), nu))
        assertFalse("andere machine", StempelControle.isGeldig(stampStempel(nu, verwacht = "M2"), nu))
        val goed = stampStempel(nu)
        assertFalse("verkeerde handtekening", StempelControle.isGeldig(goed.replace("stamp:M1:$nu:M1", "stamp:M1:${nu + 1}:M1"), nu))
    }

    fun testServerStempelVerlooptOokUitHetGeheugen() {
        val nu = System.currentTimeMillis()
        val s = stampStempel(nu)
        assertTrue(StempelControle.isGeldig(s, nu))
        assertFalse(StempelControle.isGeldig(s, nu + 2 * 3_600_000))
    }

    fun testProef() {
        val nu = System.currentTimeMillis()
        assertTrue(StempelControle.isGeldig("eval:${nu + 86_400_000}", nu))
        assertFalse(StempelControle.isGeldig("eval:${nu - 1}", nu))
    }

    fun testGeheugenDraaitDeControleEenKeer() {
        val s = keyStempel()
        val voor = StempelControle.aantalControles()
        repeat(100) { assertTrue(StempelControle.isGeldig(s)) }
        assertEquals(1, StempelControle.aantalControles() - voor)
        val fout = keyStempel(id = "XYZ999")
        repeat(100) { assertFalse(StempelControle.isGeldig(fout)) }
        assertEquals(2, StempelControle.aantalControles() - voor)
        assertTrue(StempelControle.isGeldig(s))
        assertEquals(3, StempelControle.aantalControles() - voor)
    }
}
