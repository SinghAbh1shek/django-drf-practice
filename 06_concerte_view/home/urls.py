from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students/v2', StudentViewSet, basename='students')

urlpatterns = [
    path('students/', StudentListCreate.as_view()),
]

urlpatterns += router.urls