from rest_framework import serializers
from .models import Book

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