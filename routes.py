from lib.frk import app

from lib.link import SQLLink as Link


@app.route('GET', '/test')
async def test(request):
    return {
        'status': 'OK'
    }

@app.route('POST', '/save')
async def save(request):
    await request.post()
    doc = Link.from_request(request)

    status = await doc.persist()

    return {
        'status': 'ok' if status else 'error',
        'document': doc.public()
    }

@app.route('GET', '/all')
async def get_all(request):
    _all = await Link.all()

    return {
        'status': 'ok',
        'tags': list(set([
            t for d in _all
            for t in d.tags
        ])),
        'document': [
            a.public() for a in _all
        ]
    }

@app.route('GET', '/find/{tag}')
async def find_with_tag(request):
    tag = request.match_info.get('tag')
    matches = await Link.find_with_tags(tag)

    return {
        'status': 'ok',
        'document': [
            m.public() for m in matches
        ]
    }

@app.route('DELETE', '/{id}')
async def delete(request):
    id = request.match_info.get('id')
    await Link.delete(id)

    return {
        'status': 'ok'
    }
