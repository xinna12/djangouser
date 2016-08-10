#coding=utf-8

import pdb

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework import status
from rest_framework.renderers import JSONRenderer

from djangouser.serializers import UserSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        res = {}
        res["meta"] = {"status": 200}
        res["data"] = data
        content = JSONRenderer().render(res)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def auth_login(request):
    """
    user login
    """
    try:
        params = request.POST
        username = params['username']
        password = params["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                csrf_token = request.META["CSRF_COOKIE"]
                serializer = UserSerializer(user)
                data = serializer.data
                data.update({
                    "csrf_token":csrf_token,
                })
            else:
                return JSONResponse({"error":"The password is valid, but the account has been disabled!"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return JSONResponse({"error":"The username and password were incorrect."},
                            status=status.HTTP_400_BAD_REQUEST)

    except Exception,e:
        return JSONResponse({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return JSONResponse(data)

@csrf_exempt
def auth_logout(request):
    """
    user logout
    """
    try:
        logout(request)
    except Exception,e:
        return JSONResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return JSONResponse({})