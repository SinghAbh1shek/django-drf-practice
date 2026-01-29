from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import *

@api_view(['POST'])
def create_book(request):
    data = request.data
    serializer = BookSerializer(data = data)
    if not serializer.is_valid():
        return Response(
            {
                'status': False,
                'message': 'record not created',
                'error': serializer.errors
            }
        )
    serializer.save()
    # print(serializer.validated_data)
    return Response(
        {
            'status': True,
            'message': 'record created',
            'data': serializer.data,
        }
    )

@api_view(['GET'])
def get_book(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many = True)
    return Response({
        'status': True,
        'message': 'book fetched',
        'books': serializer.data,
    })