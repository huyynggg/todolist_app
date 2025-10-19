from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .models import User, Task, List 
from .serializers import UserSerializer, TaskSerializer, ListSerializer, PasswordResetRequestSerializer
from rest_framework.response import Response 
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes 
from rest_framework.views import APIView
from django.utils import timezone 
from django.contrib.auth import authenticate 

uid = urlsafe_base64_decode(force_bytes(User.pk))
token = default_token_generator.make_token(User)
activation_link = f"http://localhost:8000/activate/{uid}/{token}/"
 

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

class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.get(email=email)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_link = f"http://localhost:8000/reset-password-confirm/{uid}/{token}/"

        send_mail(
            "Password Reset Request",
            f"Click the link to reset your password: {reset_link}",
            "huyn301003@gmail.com",
            [email],
        )

        return Response({"detail": "Password reset link sent."}, status = status.HTTP_200_OK) 

class PasswordResetConfirmView(generics.GenericAPIView):
    def post(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error": "Invalid link."}, status = status.HTTP_400_BAD_REQUEST)
        
        new_password = request.data.get("new_password")
        if not new_password:
            return Response({"error": "Password required."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({"detail": "Password reset successful."}, status=status.HTTP_200_OK)
    
class ActivateUserView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error": "Invalid link."}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)

        user.activation_date = timezone.now()
        user.save()
        return Response({"detail": "Account activated successfully!"}, status=status.HTTP_200_OK)
        
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        if user.activation_date is None:
            return Response({"error": "Account not activated. Check your email."}, status=status.HTTP_403_FORBIDDEN)

        # proceed with issuing token or session
        return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)

        

