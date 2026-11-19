// Opslag op Reddit: Redis van Devvit. Eén Redis per installatie (per subreddit).
import {redis} from '@devvit/web/server'
import type {Opslag} from './logica.ts'

export const redisOpslag: Opslag = {
  get: key => redis.get(key),
  set: async (key, value) => {
    await redis.set(key, value)
  },
  incrBy: (key, value) => redis.incrBy(key, value),
  zAdd: async (key, member, score) => {
    await redis.zAdd(key, {member, score})
  },
  zScore: (key, member) => redis.zScore(key, member),
  zTop: async (key, aantal) =>
    (await redis.zRange(key, 0, aantal - 1, {by: 'rank', reverse: true})).map(
      r => ({
        member: r.member,
        score: r.score,
      }),
    ),
  zPlekHoog: async (key, member) => {
    // Redis zRank telt vanaf de laagste score; wij willen de plek vanaf de hoogste.
    const laag = await redis.zRank(key, member)
    if (laag === undefined) return undefined
    const totaal = await redis.zCard(key)
    return totaal - 1 - laag
  },
  expire: (key, seconden) => redis.expire(key, seconden),
}
