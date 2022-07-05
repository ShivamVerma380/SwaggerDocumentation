from aiohttp import web
import requests,json


#welcome api
async def handle(request):
    response_obj = {"Message":"Welcome"}
    return web.Response(text=json.dumps(response_obj),status = 200);

async def new_user(request):
    try:
        user = request.query['name'];
        print("Creating a new user with name",user);
        response_obj={"message":"User "+user+" created successfully"}
        return web.Response(text=json.dumps(response_obj),status=200)
    except Exception as e:
        response_obj = {"message":str(e)}
        return web.Response(text=json.dumps(response_obj),status=500);
    
# async def login(request):
#     try:
#         user password
#     except Exception as e:
#         response_obj = {"message":str(e)}
#         return web.Response(text=json.dumps(response_obj),status=500);

app = web.Application();
app.router.add_get('/',handle);
app.router.add_post('/register',new_user);
# app.router.add_post('/verify-otp',verifyOTP);
web.run_app(app)