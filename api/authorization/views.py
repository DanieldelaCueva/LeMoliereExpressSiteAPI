from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from .serializers import UserSerializer, UserDataSerializer, PasswordSerializer
from .models import UserData

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['POST'])
def userLogin(request):

    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            # userInstance = User.objects.get(username=username)
            # token = Token.objects.get_or_create(user=userInstance)
            # serializer = TokenSerializer(token[0], many=False)
            login(request,user)
            return Response('Logged in successfully')
        else:
            return Response('account not active')
    else:
        return Response('Wrong cretentials')

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def userLogout(request):
    logout(request)
    response = Response('Logged out successfully')
    response.delete_cookie(key='csrftoken', domain='127.0.0.1')
    return response

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

# @login_required
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def userChangePassword(request, username):
    user = User.objects.get(username=username)
    idSerializer = UserSerializer(user, many=False)
    id = idSerializer.data['id']
    
    password = request.data['password']
    securePassword = make_password(password)
    serializer = PasswordSerializer(instance=user, data=request.data)

    token_key = Token.objects.get(user=id)

    if serializer.is_valid():
        serializer.validated_data['password'] = securePassword
        
        if str(token_key) == request.META.get('HTTP_AUTHORIZATION').split()[1]:
            serializer.save()
            return Response("Password reset successfully for user " + str(serializer.data['username']))
        else:
            return Response("Can't change others users password")

    else:
        return Response("Invalid data")