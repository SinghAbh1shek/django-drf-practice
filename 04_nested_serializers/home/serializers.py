from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer(many = True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        publisher_datas = validated_data.pop('publisher')
        author, _ = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author = author, **validated_data)
        for publisher_data in publisher_datas:
            publisher, _ = Publisher.objects.get_or_create(**publisher_data)
            book.publisher.add(publisher)
        return book

class CreateBookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset = Author.objects.all())
    publisher = serializers.PrimaryKeyRelatedField(queryset = Publisher.objects.all(), many = True)

    class Meta:
        model = Book
        fields = '__all__'