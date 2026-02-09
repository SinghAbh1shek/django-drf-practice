from .serializers import StudentSerializer
from .models import Student
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=False, methods=['POST'])
    def export_student(self, request):
        return Response({
            'status': True,
            'message': 'file exported',
            'data': {}
        })
    
    @action(detail=True, methods=['POST'])
    def send_email_student(self, request, pk):
        print(f'email sent - {pk}')
        return Response({
            'status': True,
            'message': f'email sent {pk}',
            'data': {}
        })