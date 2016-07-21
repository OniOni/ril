import json

from aiohttp import web

from lib.link import Link

async def test(request):
    return web.Response(
        body='OK\n'.encode('utf-8')
    )

async def save(request):
    await request.post()
    doc = Link.from_request(request)

    await doc.persist()

    return web.json_response({
        'status': 'ok',
        'document': doc.public()
    })

async def get_all(request):
    _all = await Link.all()

    return web.json_response({
        'status': 'ok',
        'document': _all
    })

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
