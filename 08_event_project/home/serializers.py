from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100)
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['event'] = EventSerializer(instance.ticket.event).data
        response['ticket'] = TicketSerializer(instance.ticket).data
        return response


class TicketBookingSerializer(serializers.Serializer):
    event = serializers.IntegerField()
    ticket_type = serializers.CharField()
    total_person = serializers.IntegerField()
    user = serializers.IntegerField()

    def validate_event(self, value):
        if not Event.objects.filter(id = value, status = 'happening').exists():
            raise serializers.ValidationError('Event does not exist')
        return value

    def validate_user(self, value):
        if not User.objects.filter(id = value).exists():
            raise serializers.ValidationError('user does not exist')
        return value
    
    def create(self, validated_data):
        event = Event.objects.get(id = validated_data['event'])
        user = User.objects.get(id = validated_data['user'])
        ticket_type = validated_data['ticket_type']
        total_person = validated_data['total_person']


        ticket = Ticket.objects.create(event = event, ticket_type = ticket_type, total_person = int(total_person))

        total_price = event.ticket_price * total_person

        booking = Booking.objects.create(
            ticket = ticket,
            user = user,
            status = 'paid',
            total_price = total_price
        )

        return {
            "event": event.id,
            "ticket_type": ticket_type,
            "total_person": total_person,
            "user": user.id
        }