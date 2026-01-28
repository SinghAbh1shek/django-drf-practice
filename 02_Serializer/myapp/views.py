from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def index(request):
    data = {
        'status': True,
        'message': 'Hey from django rest framework'
    }
    return Response(data)

@api_view(['POST'])
def create_records(request):
    data = request.data
    serializer = StudentSerializer(data = data)
    if not serializer.is_valid():
        return Response(
            {
                'status': False,
                'message': 'record not created',
                'error': serializer.errors,
            }
        )
    serializer.save()
    return Response(
        {
            'status': True,
            'message': 'Record Created',
            'data': serializer.data,
        }
    )


@api_view(['PATCH'])
def update_records(request):
    data = request.data
    if data.get('id') is None:
        return Response(
            {
                'status': False,
                'message': 'record not updated',
                'error': 'id required',
            }
        )
    student_obj = Student.objects.get(id = data.get('id'))
    serializer = StudentSerializer(student_obj, data = data, partial = True)
    if not serializer.is_valid():
        return Response(
            {
                'status': False,
                'message': 'record not updated',
                'error': serializer.errors,
            }
        )
    serializer.save()
    return Response(
        {
            'status': True,
            'message': 'Record Updated',
            'data': serializer.data,
        }
    )

@api_view(['GET'])
def Get_records(request):

    if request.GET.get('id'):
        student = Student.objects.get(id = request.GET.get('id'))
        serializer = StudentSerializer(student)
        return Response(
            {
                'status': True,
                'message': 'Record Fetched',
                'students': serializer.data,
            }
        )


    queryset = Student.objects.all()
    serializer = StudentSerializer(queryset, many = True)
    
    return Response(
        {
            'status': True,
            'message': 'Record Fetched',
            'students': serializer.data,
        }
    )
