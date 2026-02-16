from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .permissions import IsAdmin

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'account created',
                'data': {},
            })
        return Response({
            'status': False,
            'message': 'invalid input',
            'error': serializer.errors,
        })

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            user = authenticate(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
                )
            if user:
                token, _ = Token.objects.get_or_create(user = user)
                return Response({
                    'status': True,
                    'message': 'user logged in',
                    'data': {'token': token.key},
                })
            else:
                return Response({
                    'status': False,
                    'message': 'invalid credential',
                    'data': {},
                })
            
        return Response({
            'status': False,
            'message': 'invalid input',
            'error': serializer.errors,
        })


class PublicEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class PrivateEventViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

