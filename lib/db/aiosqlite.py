import sqlite3

from .base import BaseAsyncDB


class AsyncSQLite(BaseAsyncDB):

    def __init__(self, name):
        self.name = name
        super().__init__()

    async def open(self):
        self.db = await self._async_run(
            sqlite3.connect, self.name
        )

    async def close(self):
        await self._async_run(
            self.db.close()
        )
