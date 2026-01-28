from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('create-record/', create_records),
    path('get-record/', Get_records),
    path('update-record/', update_records),
]
