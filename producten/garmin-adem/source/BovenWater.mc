import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// Boven water is ademen (bericht hoofdchat 12 nov 01:45): de lucht van het dagdeel, de zee die groot stijgt en zakt,
// en je dier dat midden op de kam dobbert. Geen bodem, geen planten. Alleen het samenstellen: de lucht tekent
// EbbLucht, de zee EbbZee, het dier EbbDierVoorraad. Nu alleen in de proefscènes (EbbLucht.proef), tot Mila's blad
// boven water gekeurd is.
module EbbBovenWater {
    // water 0 (uit) tot 1 (in), golfFase de fase van de golf, dier het gekozen dier (of -1).
    function teken(dc as Graphics.Dc, d as Number, water as Float, golfFase as Float, dier as Number) as Void {
        var top = EbbZee.grootTop(water);
        var kam = (d * top).toNumber();
        EbbLucht.teken(dc, d, EbbLucht.deelNu(), EbbLucht.maanNu(), kam);
        EbbZee.ademZeeGroot(dc, d, water, golfFase);
        if (dier >= 0) {
            // Midden van het scherm: de golf staat daar op kam + amp * sin(fase) (EbbZee.golf), het dier gaat mee en
            // ligt een honderdste D in het water. Maat zoals op het inhoudscherm zonder wereld (±0,19 D breed).
            var maat = EbbDierMaat.inVak(dier, (d * 0.218).toNumber(), (d * 0.12).toNumber());
            var cy = kam + (d * EbbZee.ADEM_AMP * Math.sin(golfFase)).toNumber() + d / 100;
            EbbDierVoorraad.teken(dc, dier, dc.getWidth() / 2, cy, maat, EbbDierPlaatje.GEVONDEN);
        }
    }
}
