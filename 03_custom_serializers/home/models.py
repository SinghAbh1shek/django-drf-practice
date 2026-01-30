from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    price = models.FloatField()

class Student(models.Model):
    student_id = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
