from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    STATUS_CHOICES = (
        ('upcoming', 'Upcoming'),
        ('cancelled', 'Cancelled'),
        ('happening', 'Happening'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    data = models.DateField()
    capacity = models.IntegerField()
    ticket_price = models.FloatField(default=100)
    status = models.TextField(max_length=100, choices=STATUS_CHOICES, default='upcoming')
    image = models.ImageField(upload_to='event_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ticket(models.Model):
    TICKET_TYPE_CHOICES = (
        ('vip', 'VIP'),
        ('regular', 'Regular'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=100, choices=TICKET_TYPE_CHOICES)
    price = models.FloatField()

class Booking(models.Model):
    TICKET_TYPE_CHOICES = (
        ('vip', 'VIP'),
        ('regular', 'Regular'),
    )
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending')
    ticket_type = models.CharField(max_length=100, choices=TICKET_TYPE_CHOICES)
    total_price = models.FloatField()

    

