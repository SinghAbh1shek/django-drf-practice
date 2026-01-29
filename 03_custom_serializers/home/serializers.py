from rest_framework import serializers
from .models import *
from datetime import datetime

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 100)
    author = serializers.CharField(max_length = 100)
    price = serializers.FloatField()
    tax = 12

    def calculate_tax_price(self, price):
        return self.tax + price

    def to_representation(self, instance):
        return {
            'title': instance.title,
            'author': instance.author,
            'price': self.calculate_tax_price(instance.price),
            # 'price': instance.price + self.tax
        }

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book
    
    def update(self, instance, validated_data):
        title = validated_data.get('title', instance.title)
        author = validated_data.get('author', instance.author)
        price = validated_data.get('price', instance.price)

        instance.title = title
        instance.author = author
        instance.price = price
        instance.save()

        return instance
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def calculate_age(self, dob):
        current_date = datetime.now()
        age = current_date.year - dob.year
        return age
    
    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['age'] = self.calculate_age(instance.dob)
        return data
    
    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data['name'] = data['name'].strip().title()
        # print(data['name'])
        return data
    
    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        student.student_id = f'STU-{str(student.id).zfill(5)}'
        student.save()
        return student
    
    def get_fields(self):
        fields = super().get_fields()
        authenticated = True
        if authenticated:
            fields.pop('email', None)
        print(fields)
        return fields