from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer, UserDataSerializer, PasswordSerializer
from .models import UserData

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def userLogin(request):

    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            login(request,user)
            return Response('Logged in successfully')
        else:
            return Response('account not active')
    else:
        return Response('Wrong cretentials')

@login_required
@api_view(['GET'])
def userLogout(request):
    logout(request)
    return Response('Logged out successfully')

@api_view(['GET'])
def userList(request):
    user = User.objects.all()
    userSerializer = UserSerializer(user, many=True)
    for user in userSerializer.data:
        id = user['id']
        userData = UserData.objects.get(user=id)
        userDataSerializer = UserDataSerializer(userData, many=False)
        user['group'] = userDataSerializer.data['group']
        user['age_class'] = userDataSerializer.data['age_class']
      
    return Response(userSerializer.data)


@api_view(['GET'])
def userDetail(request, username):
    user = User.objects.get(username=username)
    userSerializer = UserSerializer(user, many=False)
    id = userSerializer.data['id']
    userData = UserData.objects.get(user=id)
    userDataSerializer = UserDataSerializer(userData, many=False)
    userSerializer_data = userSerializer.data
    userSerializer_data['group'] = userDataSerializer.data['group']
    userSerializer_data['age_class'] = userDataSerializer.data['age_class']
    return Response(userSerializer_data)

@login_required
@api_view(['POST'])
def userChangePassword(request, username):
    user = User.objects.get(username=username)
    
    password = request.data['password']
    securePassword = make_password(password)
    request.data['password'] = securePassword
    serializer = PasswordSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        if request.session['_auth_user_id'] == str(serializer.data['id']):
            serializer.save() 
        else:
            return Response("can't change others users password")
    else:
        return Response("Invalid data")