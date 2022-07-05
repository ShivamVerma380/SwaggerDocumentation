from aiohttp import web
import requests,json


async def handle(request):
    response_obj = {"Message":"Welcome"}
    return web.Response(text=json.dumps(response_obj),status = 200);

app = web.Application();
app.router.add_get('/',handle);

web.run_app(app)