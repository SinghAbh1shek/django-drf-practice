from django.urls import path
from .views import Test, RegisterAPI

urlpatterns = [
    path('test/', Test.as_view()),
    path('register/', RegisterAPI.as_view()),
]
