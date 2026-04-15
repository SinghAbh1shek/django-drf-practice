from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class HomeAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            'status': True,
            'message': 'home page fetched',
            'data': {
                'user': request.user.first_name,
                'message': "Hey There!"
            }
        })
