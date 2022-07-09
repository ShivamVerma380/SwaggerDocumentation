from aiohttp import web

import requests,json,secrets
from aiohttp_tokenauth import token_auth_middleware

from aiohttp_swagger import *


users={}
userId = 0
token=""



#1. Add users
#2. Get users

@swagger_path("swagger.yaml")
async def addUser(request):
    try:
        data = await request.json()
        # print(await request.read())
        print(data.get("name"))
        name = data.get("name")
        email = data.get("email")
        # name = request.query["name"]
        global users
        global userId
        users[userId] = {"email":email,"name":name}
        userId=userId+1
        response_obj={"Message":"User "+name+" created successfully"}
        return web.Response(text=json.dumps(response_obj),status=200)
    except Exception as e:
        print(str(e))
        response_obj = {"Message":str(e)}
        return web.Response(text=json.dumps(response_obj),status=500)

@swagger_path("swagger.yaml")
async def getUser(request):
    try:
        global users;
        return web.Response(text=str(users),status=200)
    except Exception as e:
        print(str(e))
        response_obj={"Message":str(e)}
        return web.Response(text=json.dumps(response_obj),status=500)
    

@swagger_path("swagger.yaml")
async def deleteUser(request):
    try:
        global users;
        data = await request.json()
        email = data.get("email")
        flag = True
        for i in users:
            print(users[i].get("email"))
            if users[i].get("email") == email:
                del users[i]
                flag = False
                response_obj={"Message":"User with email " + email + " deleted successfully"}
                return web.Response(text=json.dumps(response_obj),status=200)
        if flag==True:
            response_obj={"Message":"User with email "+email + " not found"}
            return web.Response(text=json.dumps(response_obj),status=404)
        
    except Exception as e:
        print(str(e))
        response_obj={"Message":str(e)}
        return web.Response(text=json.dumps(response_obj),status=500)



app = web.Application()
app.router.add_post("/user",addUser)
app.router.add_get("/user",getUser)
app.router.add_delete("/user",deleteUser)
setup_swagger(app, swagger_url="/api/v1/doc", ui_version=2)  # <-- NEW Doc URI

web.run_app(app, host="127.0.0.1")