
from rest_framework_simplejwt.tokens import RefreshToken
import json
 
from wsgiref.handlers import read_environ
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout


def error_on_request(error_msg):
    return JsonResponse({"error": error_msg}, status=400)


def bad_request():
    return error_on_request("bad request")

def generate_new_token(user):
    refresh = RefreshToken.for_user(user)

    return str(refresh.access_token)
     
@csrf_exempt
def handle_login(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)

            username = data.get("username")
            password = data.get("password")

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                token = generate_new_token(user)
                print("printed request user!!!!", request.user, "user ID HERE!!!", user.id)
                return JsonResponse(data={"username": user.username, "userID":user.id, "token":token}, status=200)
    except Exception as e:
        return error_on_request(str(e))

    return bad_request()

@csrf_exempt
def handle_logout(request):
    try:
        if request.method == "POST":
            logout(request)
            return JsonResponse(data={"status": "logged out successfully"}, status=200)
  
    except Exception as e:
        return error_on_request(str(e))

    return bad_request()
