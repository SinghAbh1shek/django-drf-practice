from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer

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
                    'data': serialzer.data
                })
            return Response({
                'status': False,
                'message': 'key error',
                'data': serialzer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'somethng went wrong',
                'data': str(e)
            })

        
            