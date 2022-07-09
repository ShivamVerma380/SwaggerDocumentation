# from aiohttp import web
# import requests,json
# from aiohttp_swagger import *



# #user api backend dictionary maintatin
# #create login api return token by which other apis can be fired
# #Now create apis for posting and getting user on basis of token . Maintain user list in dictionary.





# #welcome api
# @swagger_path("swagger.json")
# async def handle(request):
    
#     response_obj = {"Message":"Welcome"}
#     return web.Response(text=json.dumps(response_obj),status = 200);

# #Verify email
# @swagger_path("swagger.json")
# async def verifyEmail(request):
    
#     try:
#         updateVar()
#         # flag = True;
#         email = request.query['email'];
#         response_obj = {"message":"Email verified successfully"}
#         return web.Response(text=json.dumps(response_obj),status=200)
#     except Exception as e:
#         response_obj = {"message":str(e)}
#         return web.Response(text=json.dumps(response_obj),status=500);
    


# #Register
# @swagger_path("swagger.json")    
# async def new_user(request):
    
#     try:
#         print(flag)
#         if flag==False:
#             response_obj = {"message":"Please verify email first"}
#             return web.Response(text=json.dumps(response_obj),status=404)
#         else:
#             user = request.query['name'];
#             print("Creating a new user with name",user);
#             response_obj={"message":"User "+user+" created successfully"}
#             return web.Response(text=json.dumps(response_obj),status=200)
#     except Exception as e:
#         response_obj = {"message":str(e)}
#         return web.Response(text=json.dumps(response_obj),status=500);
    
# def updateVar():
#     print("In verify email")
#     global flag
#     flag = True
#     print(flag)
# # async def login(request):
# #     try:
# #         user password
# #     except Exception as e:
# #         response_obj = {"message":str(e)}
# #         return web.Response(text=json.dumps(response_obj),status=500);

# app = web.Application();
# app.router.add_get('/',handle);
# app.router.add_post('/register',new_user);
# flag = False

# app.router.add_post('/verify',verifyEmail);


# setup_swagger(app, swagger_url="/api/v1/doc", ui_version=2)  # <-- NEW Doc URI

# web.run_app(app, host="127.0.0.1")

import flask 
from flask import  Flask,request
from flask_swagger_ui import get_swaggerui_blueprint
# import requests
app = flask.Flask(__name__)
app.config["DEBUG"] = True

user="Shivam"
password="123456"

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static',path)

SWAGGER_URL='/swagger'
API_URL='/static/swagger.json'
swaggerui_blueprint=get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name':"test"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET'])
def home():
    return "hello"

@app.route('/register', methods=['POST'])
def register():
    username = request.form["name"];
    userpassword = request.form["password"];
    userconfirmpassword = request.form["confirm_password"];
    response_obj = {"Message":"User added successfully"}
    
    # return web.Response(text=json.dumps(response_obj),status=200)
    return "Succesfully registered"

@app.route('/login', methods=['POST'])
def login():
    
    login_data={
        
    'username' : request.form["name"],
    'userpassword' : request.form["password"]
    }
    if login_data.username==user and login_data.userpassword==password:
        return "logged in succesfully"
    else:
        return "check credentials"
    
# app.router.add_post('/register',register)
# app.router.add_post('/user',addUser)
app.run()