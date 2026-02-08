from django.urls import path
from .views import *
urlpatterns = [
    path('students/', Students.as_view()),
    path('v2/students/', StudentModelListView.as_view()),
]
