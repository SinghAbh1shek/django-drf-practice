from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class Test(APIView):
    def get(self, request):
        return Response({
            'status': True,
            'message': 'server is running',
        })

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serialzer = RegisterSerializer(data=data)
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'status': True,
                    'message': 'user created',
                    'data': {}
                })
            return Response({
                'status': False,
                'message': 'key error',
                'data': serialzer.errors
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'somethng went wrong',
                'data': {}
            })


class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serialzer = LoginSerializer(data=data)
            if serialzer.is_valid():
                user = authenticate(request, email=serialzer.validated_data['email'], password=serialzer.validated_data['password'])
                if user:
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({
                        'status': True,
                        'message': 'logged in successfully',
                        'data': {
                            'token': str(token)
                        }
                    })

                return Response({
                    'status': False,
                    'message': 'invalid credential',
                    'data': {}
                })
            return Response({
                'status': False,
                'message': 'key error',
                'data': serialzer.errors
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'somethng went wrong',
                'data': {}
            })

        
            