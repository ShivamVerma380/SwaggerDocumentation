from aiohttp import web

import requests,json,secrets
from aiohttp_tokenauth import token_auth_middleware

from aiohttp_swagger import *
async def example_resource(request):
    return web.json_response(request['user'])


async def login(request):
    try:
        name = request.query["name"];
        password = request.query["password"];
        if name=="Shivam" and password=="1234":
            print("User logged in successfully");
            global token;
            token = secrets.token_hex(16)
            response_obj = {"message":"Login Successfull",
                            "Token":token}
            return web.Response(text=json.dumps(response_obj),status=200);
        else:
            print("Bad credentials");
            response_obj = {"Message":"Enter correct name/password"}
            return web.Response(text=json.dumps(response_obj),status=404);
    except Exception as e:
        print(str(e))
        response_obj={"message":str(e)}
        return web.Response(text=json.dumps(response_obj),status=500)

async def init():

    async def user_loader(headerToken: str):
        """Checks that token is valid

        It's the callback that will get the token from "Authorization" header.
        It can check that token is exist in a database or some another place.

        Args:
            token (str): A token from "Authorization" http header.

        Returns:
            Dict or something else. If the callback returns None then
            the aiohttp.web.HTTPForbidden will be raised.
        """
        user = None
        global token
        if token == headerToken:
            user = {'uuid': 'fake-uuid'}
        return user

    app = web.Application(middlewares=[
    token_auth_middleware(
        user_loader=user_loader,
        # You can use regular expressions here
        exclude_routes=('/login', r'/login/\w+/info'),
        exclude_methods=('POST',),
    ),
])
    app.router.add_get('/', example_resource)
    app.router.add_post('/login',login)
    setup_swagger(app, swagger_url="/api/v1/doc", ui_version=2)  # <-- NEW Doc URI

    return app



if __name__ == '__main__':
    web.run_app(init(),host="127.0.0.1")