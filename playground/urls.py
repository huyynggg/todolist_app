from django.urls import path
from . import views 
from .views import PasswordResetConfirmView, PasswordResetRequestView, ActivateUserView

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
    path('lists/<int:pk>/', views.ListDetail.as_view(), name='list-detail'), 
    #passwordpath
    path('reset-password/', PasswordResetRequestView.as_view(), name = 'password_reset'),
    path('reset-password-confirm/<uibd64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #token_activation
    path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name = 'activate-user')
]     


