"""Products urls"""

# Django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Views
from frida_ayala.products.views import ProductsViewSet, OrderViewSet, CartViewSet

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'products/orders', OrderViewSet, basename='orders')
router.register(r'products/cart', CartViewSet, basename='cart')
urlpatterns = [
    path('', include(router.urls))
]
