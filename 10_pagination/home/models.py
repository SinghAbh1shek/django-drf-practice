from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_book')
    publisher = models.ManyToManyField(Publisher, related_name='book_publisher')

    def __str__(self):
        return self.title
