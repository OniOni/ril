from contextlib import contextmanager
import kyotocabinet as kc

from .base import (
    async_wrap,
    BaseAsyncDB
)

class AsyncKyoto(BaseAsyncDB):

    def __init__(self, name):
        self.name = name
        self.db = kc.DB()
        super().__init__()

    @contextmanager
    def open(self):
        conn = self.db.open(
            self.name,
            kc.DB.OWRITER | kc.DB.OCREATE
        )
        yield conn

        self.db.close()

    async def set(self, key, val):
        with self.open():
            return self.db.set(key, val)

    @async_wrap
    def get(self, key):
        with self.open():
            return self.db.get(key)

    @async_wrap
    def get_all(self):
        with self.open():
            cur = self.db.cursor()
            cur.jump()
            res = [
                self.db.get(k) for k in cur
            ]
            cur.disable()

            return res
