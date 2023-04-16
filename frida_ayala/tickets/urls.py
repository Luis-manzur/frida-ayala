"""Tickets urls"""

# Django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Views
from frida_ayala.tickets.views.orders import OrderViewSet

router = DefaultRouter()
router.register(r'tickets-orders', OrderViewSet, basename='tickets')
urlpatterns = [
    path('', include(router.urls))
]
