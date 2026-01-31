from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from.serializers import BookSerializer


@api_view(['GET'])
def index(request):
    return Response({
        'status': True,
        'message': 'Server is running'
    })

@api_view(['GET'])
def get_book(request):
    queryset = Book.objects.all()
    books = BookSerializer(queryset, many=True)

    return Response(
        {
            'status': True,
            'message': 'record fetched',
            'books': books.data
        }
    )