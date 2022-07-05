from aiohttp import web
import requests,json
from aiohttp_swagger import *



#user api backend dictionary maintatin
#create login api return token by which other apis can be fired
#Now create apis for posting and getting user on basis of token . Maintain user list in dictionary.





#welcome api
async def handle(request):
    """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Welcome api
    produces:
    - text/json
    responses:
        "200":
            description: successful operation. Return "Welcome" text
        "500":
            description: invalid HTTP Method. Returns Internal Server error.
    """
    response_obj = {"Message":"Welcome"}
    return web.Response(text=json.dumps(response_obj),status = 200);

#Verify email
async def verifyEmail(request):
    """
    ---
    description: This end-point will allow you to verify your email.
    tags:
    - Verify Email api
    products:
    - text/json
    responses:
        "200":
            description: Successful operation. Return "Email verified successfully" text
        "500":
            description: invalid HTTP Method. Returns Internal server error.
    
    """

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
    """
    ---
    description: This end-point will allow you to register user. Remember, you need to verify the email before registering.
    tags:
    - Register api
    products:
    - text/json
    responses:
        "200":
            description: Successful operation. Return "User created with name  $request.query['name'] successfully" text
        "500":
            description: invalid HTTP Method. Returns Internal server error.
    
    """
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


setup_swagger(app, swagger_url="/api/v1/doc", ui_version=2)  # <-- NEW Doc URI

web.run_app(app, host="127.0.0.1")