from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

app_name = 'authorization'

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('user-detail/<str:username>', views.userDetail, name='user-detail'),
    path('user-list/', views.userList, name='user-list'),
    path('change-password/<str:username>', views.userChangePassword, name='change-password'),
    path('api-token-auth/', auth_views.obtain_auth_token)
]