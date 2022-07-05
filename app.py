from aiohttp import web
import requests,json


#welcome api
async def handle(request):
    response_obj = {"Message":"Welcome"}
    return web.Response(text=json.dumps(response_obj),status = 200);

#Verify email
async def verifyEmail(request):
    try:
        updateVar()
        # flag = True;
        email = request.query['email'];
        response_obj = {"message":"Email verified successfully"}
        return web.Response(text=json.dumps(response_obj),status=200)
    except Exception as e:
        response_obj = {"message":str(e)}
        return web.Response(text=json.dumps(response_obj),status=500);
    


#Register
async def new_user(request):
    try:
        print(flag)
        if flag==False:
            response_obj = {"message":"Please verify email first"}
            return web.Response(text=json.dumps(response_obj),status=404)
        else:
            user = request.query['name'];
            print("Creating a new user with name",user);
            response_obj={"message":"User "+user+" created successfully"}
            return web.Response(text=json.dumps(response_obj),status=200)
    except Exception as e:
        response_obj = {"message":str(e)}
        return web.Response(text=json.dumps(response_obj),status=500);
    
def updateVar():
    print("In verify email")
    global flag
    flag = True
    print(flag)
# async def login(request):
#     try:
#         user password
#     except Exception as e:
#         response_obj = {"message":str(e)}
#         return web.Response(text=json.dumps(response_obj),status=500);

app = web.Application();
app.router.add_get('/',handle);
app.router.add_post('/register',new_user);
flag = False

app.router.add_post('/verify',verifyEmail);
web.run_app(app)