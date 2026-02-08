from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView

class StudentModelListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(name__startswith = 'a')
    
    def perform_create(self, serializer):
        print('perform create called')
        return super().perform_create(serializer)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Students(APIView):
    def get(self, request):
        queryset = Student.objects.all()
        student = StudentSerializer(queryset, many = True)
        return Response(
            {
                'status': True,
                'message': 'record fetched',
                'students': student.data
            }
        )
    
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data = data)
        if not serializer.is_valid():
            return Response(
                {
                    'status': True,
                    'message': 'record not created',
                    'error': serializer.errors
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