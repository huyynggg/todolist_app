from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User, Task, List 
from .serializers import UserSerializer, TaskSerializer, ListSerializer

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

#Users
class UserList (generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Lists
class ListList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

#Tasks
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


