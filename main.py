from aiohttp import web

routes = web.RouteTableDef()


def html_response(document):
    s = open(document, "r")
    return web.Response(text=s.read(), content_type='text/html')


@routes.get('/')
async def hello(request):
    return html_response('StreamDemo.html')

app = web.Application()
app.router.add_static('/static/', path='', name='static')

app.add_routes(routes)
web.run_app(app)
