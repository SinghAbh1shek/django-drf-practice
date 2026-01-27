from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student

@api_view()
def index(request):
    students = ['Aman', 'Abhishek', 'Arjun']
    data = {
        'status': True,
        'message': 'This is from django rest framework',
        'students': students
    }
    return Response(data)

@api_view(['POST'])
def create_record(request):
    data = request.data
    Student.objects.create(**data)

    return Response({
        'status': True,
        'message': 'Record Created'
    })

@api_view(['GET'])
def get_record(request):
    students = [
        {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'dob': student.dob,
        }
        for student in Student.objects.all().order_by('-dob')
    ]

    
    return Response({
        'status': True,
        'message': 'record fetched',
        'students': students
    })


@api_view(['DELETE'])
def delete_record(request):
    try:
        data = request.data
        Student.objects.get(id = data.get('id')).delete()
        return Response({
            'status': True,
            'message': 'record deleted',
            'data': {}
        })
    except Exception as e:
        return Response({
            'status': False,
            'message': 'invalid id',
            'data': {}
        })
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student(request):
    if request.method == 'GET':
        students = [
            {
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'dob': student.dob,
            }
            for student in Student.objects.all().order_by('-dob')
        ]
        return Response({
            'status': True,
            'message': 'record fetched',
            'students': students
        })
    elif request.method == 'POST':
        data = request.data
        Student.objects.create(**data)

        return Response({
            'status': True,
            'message': 'Record Created'
        })
    elif request.method == 'DELETE':
        try:
            data = request.data
            Student.objects.get(id = data.get('id')).delete()
            return Response({
                'status': True,
                'message': 'record deleted',
                'data': {}
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'invalid id',
                'data': {}
            })