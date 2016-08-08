import json

import aiohttp_cors

from routes import *


def cors_setup(app):
    cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    for route in list(app.router.routes()):
        cors.add(route)

    return app

def setup():
    app = web.Application()
    app.router.add_route('GET', '/test', test)
    app.router.add_route('POST', '/save', save)
    app.router.add_route('GET', '/all', get_all)
    app.router.add_route('GET', '/find/{tag}', find_with_tag)

    app = cors_setup(app)

    return app


def run(app):
    web.run_app(app)


if __name__ == '__main__':
    app = setup()
    run(app)
