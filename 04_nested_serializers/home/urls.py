from django.urls import path
from .views import *

urlpatterns = [
    path("", index ),
    path("get-book/", get_book ),
    path("create-book/", create_book ),
    path("v2/test/", TestAPI.as_view() ),
]
