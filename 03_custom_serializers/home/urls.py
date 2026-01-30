from django.urls import path
from .views import *

urlpatterns = [
    path('create-book/', create_book),
    path('get-book/', get_book),
    path('students/', student),
    path('create-user/', create_user),
]
