from contextlib import contextmanager
import sqlite3

from .base import (
    async_wrap,
    BaseAsyncDB
)


class AsyncSQLite(BaseAsyncDB):

    def __init__(self, name):
        self.name = name
        super().__init__()

    @contextmanager
    def open(self):
        conn = sqlite3.connect(self.name)
        yield conn

        conn.close()

    def _create_table(self, conn):
        conn.execute(
            '''create table if not exists
            links (
            id integer primary key autoincrement,
            link text unique,
            json text
            );'''
        )

    def _insert(self, conn, url, json):
        conn.execute(
            '''insert into links
            values (?, ?);
            ''', (url, json)
        )
        conn.commit()

    @async_wrap
    def set(self, key, val):
        with self.open() as conn:
            self._create_table(conn)
            try:
                self._insert(conn, key, val)
            except sqlite3.IntegrityError:
                return False

            return True

    @async_wrap
    def get_all(self):
        with self.open() as conn:
            self._create_table(conn)
            _all = conn.execute('select id, json from links;').fetchall()
            conn.commit()

            return [{'id': a[0], 'json': a[1]} for a in _all]
