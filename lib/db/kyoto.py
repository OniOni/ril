import kyotocabinet as kc

from .base import BaseAsyncDB

class AsyncKyoto(BaseAsyncDB):

    def __init__(self, name):
        self.name = name
        self.db = kc.DB()
        super().__init__()

    async def open(self):
        res = await self._async_run(
            self.db.open,
            self.name,
            kc.DB.OWRITER | kc.DB.OCREATE
        )

        return res

    async def close(self):
        res = await self._async_run(
            self.db.close
        )

        return res

    async def set(self, key, val):
        res = await self._async_run(
            self.db.set, key, val
        )

        return res

    async def get(self, key):
        res = await self._async_run(
            self.db.get, key
        )

        return res

    def _get_all(self):
        cur = self.db.cursor()
        cur.jump()
        res = [self.db.get(k) for k in cur]
        cur.disable()

        return res

    async def get_all(self):
        res = await self._async_run(
            self._get_all
        )

        return res
