import json

from routes import *

def setup():
    app = web.Application()
    app.router.add_route('GET', '/test', test)
    app.router.add_route('POST', '/save', save)
    app.router.add_route('GET', '/all', get_all)

    return app

def run(app):
    web.run_app(app)

if __name__ == '__main__':
    app = config()
    run(app)
