from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token

class RegisterAPI(APIView):
    
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'account created successfully',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': 'key error',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            })
        
class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                token, _ = Token.objects.get_or_create(user=serializer.validated_data['user'])
                return Response({
                    'status': True,
                    'message': 'login token generated',
                    'data': {
                        'token': str(token)
                    }
                })
            return Response({
                'status': False,
                'message': 'key error',
                'data': serializer.errors
            }, status=400)

        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            }, status=500)