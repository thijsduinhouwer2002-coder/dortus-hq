// Opslag in het geheugen, voor de lokale versie en de toetsen. Gedraagt zich als het stukje Redis in Opslag.
import type {Opslag} from './logica.ts'

export class GeheugenOpslag implements Opslag {
  #waarden = new Map<string, string>()
  #rijen = new Map<string, Map<string, number>>()

  async get(key: string): Promise<string | undefined> {
    return this.#waarden.get(key)
  }
  async set(key: string, value: string): Promise<void> {
    this.#waarden.set(key, value)
  }
  async setNX(key: string, value: string): Promise<boolean> {
    if (this.#waarden.has(key)) return false
    this.#waarden.set(key, value)
    return true
  }
  async incrBy(key: string, value: number): Promise<number> {
    const n = Number(this.#waarden.get(key) ?? 0) + value
    this.#waarden.set(key, String(n))
    return n
  }
  async zAdd(key: string, member: string, score: number): Promise<void> {
    let rij = this.#rijen.get(key)
    if (!rij) {
      rij = new Map()
      this.#rijen.set(key, rij)
    }
    rij.set(member, score)
  }
  async zScore(key: string, member: string): Promise<number | undefined> {
    return this.#rijen.get(key)?.get(member)
  }
  #gesorteerd(key: string): {member: string; score: number}[] {
    const rij = this.#rijen.get(key) ?? new Map<string, number>()
    return [...rij.entries()]
      .map(([member, score]) => ({member, score}))
      .sort((a, b) => b.score - a.score || (a.member < b.member ? 1 : -1))
  }
  async zTop(
    key: string,
    aantal: number,
  ): Promise<{member: string; score: number}[]> {
    return this.#gesorteerd(key).slice(0, aantal)
  }
  async zPlekHoog(key: string, member: string): Promise<number | undefined> {
    const i = this.#gesorteerd(key).findIndex(r => r.member === member)
    return i < 0 ? undefined : i
  }
  async expire(_key: string, _seconden: number): Promise<void> {}
}
