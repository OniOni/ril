import html
import json
from urllib.parse import urlparse
from typing import List

from lib.db import (
    AsyncKyoto,
    AsyncSQLite
)


class Link(object):

    def __init__(self, url: str, tags: List[str]):
        self.raw_url = url
        self.url = urlparse(url)
        self.tags = tags

    @classmethod
    def from_request(cls, req):
        p = req.POST
        return cls(
            url=p['url'],
            tags=p['tags'].split(',')
        )

    async def persist(self):
        await self.db.set(self.key, json.dumps(self.public()))

    @classmethod
    async def all(cls):
        _all = await cls.db.get_all()

        return [json.loads(a) for a in _all]

    def public(self) -> str:
        return {
            'url': self.raw_url,
            'tags': [
                html.escape(t)
                for t in self.tags
            ]
        }

    @property
    def key(self):
        return "{}{}".format(self.url.netloc, self.url.path)


class KyotoLink(Link):
    db = AsyncKyoto('test.kch')

class SQLLink(Link):
    db = AsyncSQLite('test.db')
