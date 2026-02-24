from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsProductOwnerPermission

@api_view()
def home(request):
    return Response({
        'status': True,
        'message': 'server is running'
    })


class registerAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'user created',
                'data': serializer.data
            })
        
        return Response({
            'status': False,
            'message': 'user not created',
            'error': serializer.errors
        })
    
class loginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = authenticate(username = data['username'], password=data['password'])
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
            'error': serializer.errors
        })
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsProductOwnerPermission, IsAuthenticated]
    authentication_classes = [TokenAuthentication]