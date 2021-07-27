from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

app_name = 'authorization'

urlpatterns = [
    path('', views.authorizationOverview, name='authorization-overview'),
    path('login/', auth_views.obtain_auth_token, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('user-detail/<str:username>', views.userDetail, name='user-detail'),
    path('user-list/', views.userList, name='user-list'),
    path('change-password/<str:username>', views.userChangePassword, name='change-password'),
]