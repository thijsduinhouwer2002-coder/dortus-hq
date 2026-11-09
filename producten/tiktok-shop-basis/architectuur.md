# Architectuur: TikTok Shop-basis

Kleine bibliotheek in TypeScript zonder afhankelijkheden. Draait in Node 22.18+ (TypeScript zonder bouwstap) en is bedoeld voor Cloudflare Workers: alleen Web Crypto, `fetch` en `URLSearchParams`. Ontwerp: `ontwerp.md`.

| Bestand | Wat | Gebruikt |
| --- | --- | --- |
| `src/sign.ts` | HMAC-SHA256-handtekening volgens TikTok | Web Crypto |
| `src/fouten.ts` | `TikTokApiError` met soort (te veel verzoeken, token verlopen, geen toegang, handtekening, auth_code, server, overig) | |
| `src/auth.ts` | inloglink, `state`, auth_code inwisselen, verversen, verloopcheck; gaat buiten de client om (secret in de query, nooit loggen) | fouten |
| `src/client.ts` | `TikTokClient.roep`: app_key, timestamp, sign, kop `x-tts-access-token`, shop_cipher, 3 pogingen bij 429/5xx met `Retry-After` | sign, fouten |
| `src/paginate.ts` | `allePaginas` met bovengrens 500, `verzamel` | |
| `src/endpoints.ts` | winkels, afrekeningen (statements), transacties per afrekening | client, paginate |
| `src/bedrag.ts` | tekstbedrag naar kleinste munteenheid, zonder afronden | |
| `src/index.ts` | alles naar buiten | |

Tests: `npm test` (`node --test`). Nagebootste antwoorden in `test/voorbeelden/` zijn letterlijk de voorbeelden uit de docs van TikTok (bestandsnaam is de pagina op partner.tiktokshop.com/docv2/page/). `test/hulp.ts` heeft een nep-fetch die elk verzoek onthoudt.

Nog niet: echte aanroepen (geen app key zonder registratie), test in een echte ontwikkelwinkel (na de KvK), opslag van tokens, webhooks, boekingen naar een pakket. Dat komt in het product dat Tess kiest, dat deze map importeert.
