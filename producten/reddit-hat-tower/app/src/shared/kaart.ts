// De uitslagkaart: platte tekst die iemand als reactie onder de dagpost zet.
// Elke held is een vakje, zodat je in de reacties ziet wie waar misging zonder de score te verklappen.
import {dagRegel} from './spel.ts'

const VAKJE: Record<string, string> = {
  perfect: '🟩',
  gulp: '🟨',
  gold: '🌟',
  miss: '⬛',
}

export function kaartTekst(
  dag: number,
  hoeden: number,
  besteReeks: number,
  uitslagen: readonly string[],
  dagenOpRij: number,
  opmaak: 'plat' | 'reactie' = 'plat',
): string {
  const regel = dagRegel(dag)
  const vakjes = uitslagen.map(u => VAKJE[u] ?? '⬛')
  const rijen: string[] = []
  for (let i = 0; i < vakjes.length; i += 10)
    rijen.push(vakjes.slice(i, i + 10).join(''))
  const regels = [
    `Gloop's Hat Tower #${dag} (${regel.naam})`,
    `🎩 ${hoeden} hats, best perfect streak ${besteReeks}`,
    ...rijen,
  ]
  if (dagenOpRij > 1) regels.push(`🔥 ${dagenOpRij} days in a row`)
  // In een Reddit-reactie wordt één regelovergang geen nieuwe regel; daar een witregel ertussen.
  return regels.join(opmaak === 'reactie' ? '\n\n' : '\n')
}
