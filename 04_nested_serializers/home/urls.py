from django.urls import path
from .views import *

urlpatterns = [
    path("", index ),
    path("get-book/", get_book ),
    path("create-book/", create_book ),
]
