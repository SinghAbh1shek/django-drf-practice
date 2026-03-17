from .models import Author
from .serializers import AuthorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .throttle import CustomThrottle

class AuthorAPI(APIView):
    throttle_classes = [CustomThrottle]
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({
            'status': True,
            'message': 'Data Fetched',
            'data': serializer.data
        })
