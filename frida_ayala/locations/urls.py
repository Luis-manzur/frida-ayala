"""Locations URLs."""

# Django
from django.urls import include, path
# Django REST Framework
from rest_framework.routers import DefaultRouter

from .views import states as states_views
# Views
from .views import venues as venues_views

router = DefaultRouter()
router.register(r'venues', venues_views.VenueViewSet, basename='venues')
router.register(r'states', states_views.StateViewSet, basename='states')

urlpatterns = [
    path('', include(router.urls)),
]
