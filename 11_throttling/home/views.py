from .models import Author
from .serializers import AuthorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class AuthorAPI(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({
            'status': True,
            'message': 'Data Fetched',
            'data': serializer.data
        })
