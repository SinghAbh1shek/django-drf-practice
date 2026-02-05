from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from.serializers import *
from rest_framework.views import APIView

class TestAPI(APIView):
    def get(self, request):
        return Response({
            'status': True,
            'message': 'This is get method'
        })
    
    def post(self, request):
        return Response({
            'status': True,
            'message': 'This is post method'
        })


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

@api_view(['POST'])
def create_book(request):
    data = request.data
    serializer = BookSerializer(data = data)
    if not serializer.is_valid():
        return Response(
            {
                'status': False,
                'message': 'record not created',
                'errors': serializer.errors
            }
        )
    serializer.save()

    return Response(
        {
            'status': True,
            'message': 'record fetched',
            'books': serializer.data
        }
    )