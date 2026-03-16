from django.urls import path
from .views import AuthorAPI

urlpatterns = [
    path('author/', AuthorAPI.as_view())
]
