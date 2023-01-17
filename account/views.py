import json
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic.list import ListView
from account.serializer import UserSerializer, UserActivateSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializer import UserRegistrSerializer
from rest_framework.views import APIView
from .services.update import update_spectate, update_online
from django.utils import timezone
from datetime import timedelta
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .services.activate import activate_user, longpoll_get_new_admin, block_user, add_user_to_file

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class UsersView(ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
class OnlineUsersView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request: HttpRequest):
        server = request.user.server
        
        users = User.objects.filter(server=server, last_online__gte=timezone.now()-timedelta(seconds=360)).values('nickname', 'username', 'server', 'spectate')
        return Response(users, status=200)

class UserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'
    serializer_class = UserSerializer

class UserActivateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: HttpRequest):
        username = json.loads(request.body).get('username')
        if username:
            if activate_user(username):
                return Response({'status': True}, status=200)
        return Response({'error': 'Bad request'}, status=400)
    
class UserBlockView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: HttpRequest):
        username = json.loads(request.body).get('username')
        if username:
            if block_user(username):
                return Response({'status': True}, status=200)
        return Response({'error': 'Bad request'}, status=400)


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            add_user_to_file(request.data.get('username'))
            return Response(data, status=status.HTTP_200_OK)
        else: # Иначе
            data = serializer.errors
            return Response(data)
        
class LoginUserView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username
        })
        
class UpdateSpectate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: HttpRequest):
        print(request.body)
        spectate = json.loads(request.body).get('spectate')
        print(spectate)
        if update_spectate(request.user, spectate):
            return Response({'status': True}, status=200)
        return Response({'error': 'Bad request'}, status=400)

class UpdateOnline(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: HttpRequest):
        if update_online(request.user):
            return Response({'status': True}, status=200)
        return Response({'error': 'Bad request'}, status=400)
    
class LPView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request: HttpRequest):
        users = longpoll_get_new_admin(request.user)
        if users:
            return Response(users, status=200)
        else:
            return Response({'status': 'error', 'info': 'New unactivateds don`t exist.'})