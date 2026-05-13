from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookApiView(APIView):
    def get(self, request):
        try:
            queryset = Book.objects.all()
            serializer = BookSerializer(queryset, many=True)
            return Response({
                'status': True,
                'message': 'record fetched', 
                'data': serializer.data
            })
            
        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrong', 
                'data': str(e)
            }, status=500)
