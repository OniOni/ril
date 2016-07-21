import html
import json
from typing import List

from lib.db import AsyncKyoto


class Link(object):

    def __init__(self, url: str, tags: List[str]):
        self.url = url
        self.tags = tags

        self.db = AsyncKyoto('test.kch')

    @classmethod
    def from_request(cls, req):
        p = req.POST
        return cls(
            url=p['url'],
            tags=p['tags'].split(',')
        )

    async def persist(self):
        await self.db.open()
        await self.db.set(self.url, json.dumps(self.public()))
        await self.db.close()

    @classmethod
    async def all(self):
        db = AsyncKyoto('test.kch')
        await db.open()
        _all = await db.get_all()
        await db.close()
        print(_all)
        return [json.loads(a.decode('utf-8')) for a in _all]

    def public(self) -> str:
        return {
            'url': self.url,
            'tags': [
                html.escape(t)
                for t in self.tags
            ]
    }
