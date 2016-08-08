import html
import json
from urllib.parse import urlparse
from typing import List

from lib.db import (
    AsyncSQLite
)


class Link(object):

    def __init__(self, url: str, tags: List[str]):
        self.raw_url = url
        self.url = urlparse(url)
        self.tags = [t.strip() for t in  tags]

    @classmethod
    def from_request(cls, req):
        p = req.POST
        return cls(
            url=p['url'],
            tags=p['tags'].split(',')
        )

    @classmethod
    def from_row(cls, row):
        r = json.loads(row)
        return cls(
            url=r['url'],
            tags=r['tags']
        )

    async def persist(self):
        status = await self.db.set(self.key, json.dumps(self.public()))
        return status

    @classmethod
    async def all(cls):
        _all = await cls.db.get_all()

        return [cls.from_row(a) for a in _all]

    @classmethod
    async def find_with_tags(cls, tag):
        _all = await cls.all()

        return [
            a for a in _all
            if tag in a.tags
        ]

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


class SQLLink(Link):
    db = AsyncSQLite('test.db')
