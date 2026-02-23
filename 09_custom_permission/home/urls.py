from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('home', home),
    path('register/', registerAPI.as_view()),
    path('login/', loginAPI.as_view()),
    path('', include(router.urls)),

]
