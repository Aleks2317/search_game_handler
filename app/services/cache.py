from redis import asyncio as aioredis

from app.settings import (
    REDIS_HOST,
    REDIS_PORT,
)


class RedisCache:
    def __init__(self):
        self.redis = None

    async def init(self):
        self.redis = await aioredis.from_url(
            f"redis://{REDIS_HOST}:{REDIS_PORT}",
            decode_responses=True,
            max_connections=10,
        )

    async def get(self, key):
        return await self.redis.get(key)

    async def set(self, key, value):
        await self.redis.set(key, value)


redis_cache = RedisCache()
