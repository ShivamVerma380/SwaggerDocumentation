from aiohttp import web
import requests,json


#welcome api
async def handle(request):
    response_obj = {"Message":"Welcome"}
    return web.Response(text=json.dumps(response_obj),status = 200);

#otp sending
async def sendOTP(request):
    try:
        email = request.query['email'];
        response_obj = {"message":"Your otp is:123456"}
        return web.Response(text=json.dumps(response_obj),status=200)
    except Exception as e:
        response_obj = {"message":str(e)}
        return web.Response(text=json.dumps(response_obj),status=500)


#otp verify
async def verifyOTP(request):
    try:
        input_otp = str(request.query['otp']);
        otp = "123456";
        if input_otp == otp:
            respponse_obj = {"message":"Email verified successfully"}
            return web.Response(text=json.dumps(response_obj),status=200)
        else:
            response_obj = {"message":"Incorrect otp"}
            return web.Response(text=json.dumps(response_obj),status=400)
        # return web.Response(text=json.dumps(response_obj),status=200)
    except Exception as e:
        response_obj = {"message":str(e)}
        return web.Response(text=json.dumps(response_obj),status=500)

app = web.Application();
app.router.add_get('/',handle);
app.router.add_post('/verify-email',sendOTP);
app.router.add_post('/verify-otp',verifyOTP);
web.run_app(app)