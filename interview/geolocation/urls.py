from django.urls import path
from .viewsets import LocationViewSet

urlpatterns = [
    path('api/location/', LocationViewSet.as_view()),
]