from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .permissions import IsAdmin
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from django.db.models import Q

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'account created',
                'data': {},
            })
        return Response({
            'status': False,
            'message': 'invalid input',
            'error': serializer.errors,
        })

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            user = authenticate(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
                )
            if user:
                token, _ = Token.objects.get_or_create(user = user)
                return Response({
                    'status': True,
                    'message': 'user logged in',
                    'data': {'token': token.key},
                })
            else:
                return Response({
                    'status': False,
                    'message': 'invalid credential',
                    'data': {},
                })
            
        return Response({
            'status': False,
            'message': 'invalid input',
            'error': serializer.errors,
        })


class PublicEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    # def create(self, request):
    #     raise MethodNotAllowed('POST')
    
    # def partial_update(self, request, *args, **kwargs):
    #     raise MethodNotAllowed('PATCH')

    http_method_names = ['get'] # This only allow get method

    @action(detail=False, methods=['get'])
    def search_event(self, request):
        search = request.GET.get('search')
        events = Event.objects.all()
        if search:
            events = events.filter(
                Q(title__icontains=search) | Q(description__icontains = search)
            )
        serializer = EventSerializer(events, many=True)
        return Response({
            'status': True,
            'message': 'record fetched',
            'data': serializer.data
        })
        

class PrivateEventViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def create_booking(self, request):
        data = request.data
        serializer = TicketBookingSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'event booked',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'event not booked',
            'error': serializer.errors
        })


