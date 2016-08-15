from functools import wraps

from aiohttp import web
import aiohttp_cors


class Application(web.Application):

    def route(self, method, path):
        def outer(f):
            @wraps(f)
            async def wrapper(*a, **k):
                print("{} {}".format(method, path))
                res = await f(*a, **k)
                return web.json_response(res)

            print("Adding {} with {}, {}".format(f, method, path))
            self.router.add_route(
                method, path, wrapper
            )

            return wrapper

        return outer

    def cors_setup(self, rules):
        cors = aiohttp_cors.setup(self, defaults=rules)

        for route in list(self.router.routes()):
            cors.add(route)

        return app

    def run(self):
        web.run_app(self)


app = Application()
