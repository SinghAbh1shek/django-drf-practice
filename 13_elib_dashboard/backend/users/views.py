from rest_framework.views import APIView
from rest_framework.response import Response

class Test(APIView):
    def get(self, request):
        return Response({
            'status': True,
            'message': 'server is running',
        })

class RegisterAPI(APIView):
    pass