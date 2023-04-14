"""Tickets urls"""

# Django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Views
from frida_ayala.tickets.views.tickets import TicketsViewSet

router = DefaultRouter()
router.register(r'tickets', TicketsViewSet, basename='tickets')
urlpatterns = [
    path('', include(router.urls))
]

