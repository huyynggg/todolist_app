from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    #userspath
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    #taskpath
    path('tasks/', views.TaskList.as_view(), name='tasks-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    #listpath
    path('lists/', views.ListList.as_view(), name='lists-list'),
    path('lists/<int:pk>/', views.ListDetail.as_view(), name='list-detail')
]     

 