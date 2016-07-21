import asyncio
import functools


class BaseAsyncDB(object):

    def __init__(self):
        self.loop = asyncio.get_event_loop()

    async def _async_run(self, func, *a, **k):
        res = await self.loop.run_in_executor(
            None, functools.partial(
                func, *a, **k
            )
        )

        return res
