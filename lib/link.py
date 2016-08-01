import html
import json
from typing import List

from lib.db import AsyncKyoto


class Link(object):
    db = AsyncKyoto('test.kch')

    def __init__(self, url: str, tags: List[str]):
        self.url = url
        self.tags = tags

    @classmethod
    def from_request(cls, req):
        p = req.POST
        return cls(
            url=p['url'],
            tags=p['tags'].split(',')
        )

    async def persist(self):
        await self.db.set(self.url, json.dumps(self.public()))

    @classmethod
    async def all(cls):
        _all = await cls.db.get_all()

        return [json.loads(a.decode('utf-8')) for a in _all]

    def public(self) -> str:
        return {
            'url': self.url,
            'tags': [
                html.escape(t)
                for t in self.tags
            ]
        }
