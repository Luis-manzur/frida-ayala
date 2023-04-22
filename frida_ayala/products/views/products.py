"""Products views"""
# Django
from django_filters.rest_framework import DjangoFilterBackend
# DRF
from rest_framework import viewsets, mixins

# Models
from frida_ayala.products.models import Product
# Serializers
from frida_ayala.products.serializers.products import ProductSerializer


class ProductsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    # Filter The Tickets By event
    filter_backends = [DjangoFilterBackend]
    search_fields = ['supplier']

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
