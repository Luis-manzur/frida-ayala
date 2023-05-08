"""Products urls"""

# Django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Views
from frida_ayala.products.views import ProductsViewSet, ProductOrderViewSet, CartViewSet, BrandViewSet

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'products/cart', CartViewSet, basename='cart')
router.register(r'product-orders', ProductOrderViewSet, basename='product-orders')

urlpatterns = [
    path('', include(router.urls))
]
