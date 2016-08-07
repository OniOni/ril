from aiohttp import web

from lib.link import SQLLink as Link


async def test(request):
    return web.Response(
        body='OK\n'.encode('utf-8')
    )

async def save(request):
    await request.post()
    doc = Link.from_request(request)

    status = await doc.persist()

    return web.json_response({
        'status': 'ok' if status else 'error',
        'document': doc.public()
    })

async def get_all(request):
    _all = await Link.all()

    return web.json_response({
        'status': 'ok',
        'document': _all
    })
