from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
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

@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def student(request):
    if request.method == 'GET':
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many = True)
        return Response(
            {   
                'status': True,
                'message': 'record fetched',
                'students': serializer.data
            }
        )
    elif request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data = data)
        if not serializer.is_valid():
            return Response(
                {   
                    'status': False,
                    'message': 'record not created',
                    'students': serializer.errors
                }
            )
        serializer.save()
        return Response(
            {   
                'status': True,
                'message': 'record created',
                'students': serializer.data
            }
        )

    else:
        return Response(
            {   
                'status': True,
                'message': f'method {request.method}',
            }
        )