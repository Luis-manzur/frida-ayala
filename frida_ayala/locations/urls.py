"""Locations URLs."""

# Django
from django.urls import include, path
# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import venues as venues_views

router = DefaultRouter()
router.register(r'venues', venues_views.VenueViewSet, basename='venues')

urlpatterns = [
    path('', include(router.urls)),
]
