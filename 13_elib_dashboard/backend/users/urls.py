from django.urls import path
from .views import Test, RegisterAPI, LoginAPI

urlpatterns = [
    path('test/', Test.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]
