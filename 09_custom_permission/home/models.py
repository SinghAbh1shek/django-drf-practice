from django.db import models
from django.contrib.auth.models import User

class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title
