"""Tickets urls"""

# Django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Views
from frida_ayala.tickets.views.orders import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='tickets-orders')
urlpatterns = [
    path('', include(router.urls))
]
