from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Index(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        print(request.user)
        return Response({
            'status': 'True',
            'message': 'user is authenticated'
        })
    
    
    

class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'user registered successfully',
                'data': serializer.data,
            })
        
        return Response({
            'status': False,
            'message': 'key missing',
            'data': serializer.errors,
        })

class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = authenticate(username = serializer.data['username'], password = serializer.data['password'])
            if user is None:
                return Response({
                    'status': False,
                    'message': 'invalid credentials',
                    'data': {}
                })
            
            token, _ = Token.objects.get_or_create(user = user)

            return Response({
                'status': True,
                'message': 'user token',
                'data': {
                    'token': token.key
                }
            })
        
        return Response({
            'status': False,
            'message': 'key missing',
            'data': serializer.errors
        })