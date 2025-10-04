from django.urls import path
from . import views

urlpatterns = [
    #users
    path('users/', views.UserList.as_view(), name='users-list'),
    path('user-detail/<int:pk>/', views.UserDetail.as_view(), name='user-details'),

    #tasks
    path('tasks/', views.TaskList.as_view(), name='tasks-list'),
    path('task-detail/<int:pk>/', views.TaskDetail.as_view(), name ='task-details'),

    #lists
    path('lists/', views.ListList.as_view(), name = 'lists-list'),
    path('list-detail/<int:pk>/', views.ListDetail.as_view(), name = 'list-details')
]
