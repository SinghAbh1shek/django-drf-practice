from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer

class RegisterAPI(APIView):
    
    def get(self, requset):
        return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {}
            })

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