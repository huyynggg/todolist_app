from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-lilst'),
    path('user-detail/<int:pk>/', views.UserDetail.as_view(), name='user-details'),
]
