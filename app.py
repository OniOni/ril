import aiohttp_cors

from lib import frk
import routes

def setup():
    app = frk.app
    app.cors_setup({
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    return app


def run(app):
    app.run()


if __name__ == '__main__':
    app = setup()
    run(app)
