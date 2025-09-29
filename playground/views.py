from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User
from .serializers import UserSerializer 

def whatsup(request):
    return HttpResponse('Hello World!!!')

def home(request):
    html_content= """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Welcome</title>
        </head>
        <body>
            <h1>Welcome to the ToDo List App</h1>
            <h2>This is a ToDo List App created by Huy Nguyen</h2>
        </body>
        </html>
        """
    return HttpResponse(html_content)

class UserList (generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

