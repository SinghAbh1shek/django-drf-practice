from rest_framework import serializers
from .models import *
from datetime import datetime
from rest_framework.validators import UniqueValidator
from .validators import no_number

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length = 100,
        validators = [
            UniqueValidator(queryset=Book.objects.all())
        ])
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

class AddressValidator(serializers.Serializer):
    city = serializers.CharField(max_length = 100)
    postal_code = serializers.CharField(max_length = 10)

    def validate_postal_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('postal code must contains digit only')
        return value
    
class UserSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length = 100,
        validators = [no_number]
        )
    email = serializers.EmailField()
    age = serializers.IntegerField()
    phone = serializers.RegexField(
        regex=r'^[789]\d{9}$', error_messages = {
            'invalid': 'phone number must be entered correctly'
        }
    )
    address = AddressValidator()
    user_type = serializers.ChoiceField(choices=['admin', 'regular'])
    admin_code = serializers.CharField(required = False)

    # def validate_age(self, value):
    #     if value < 18 or value > 30:
    #         raise serializers.ValidationError('Age must be above 18 and below 30')
    #     return value
    
    # def validate_email(self, value):
    #     if value.split('@')[1] == 'gmail.com':
    #         raise serializers.ValidationError('email must be bussiness email')
    #     return value
    
    # We can also write all the validatation in single place like this
    def validate(self, data):
        if 'age' in data and data['age'] < 18 or data['age'] > 30:
            raise serializers.ValidationError('Age must be above 18 and below 30')

        if 'email' in data and data['email'].split('@')[1] == 'gmail.com':
            raise serializers.ValidationError('email must be bussiness email')
        
        if data['user_type'] == 'admin' and not data.get('admin_code'):
            raise serializers.ValidationError('admin code is required')

        return super().validate(data)
    
