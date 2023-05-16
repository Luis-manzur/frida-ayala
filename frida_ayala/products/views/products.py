"""Products views"""
from django_filters.rest_framework import DjangoFilterBackend
# Django
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
# DRF
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from frida_ayala.companies.models import Company
# Models
from frida_ayala.products.models import Product, Category
from frida_ayala.products.serializers.brands import BrandSerializer
from frida_ayala.products.serializers.categories import CategorySerializer
# Serializers
from frida_ayala.products.serializers.products import ProductSerializer, ProductDetailSerializer


class ProductsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ("name",)
    ordering_fields = ("-price", "price", "created", "-created")
    ordering = (
        "-created",
        "price",
    )
    filter_fields = ("supplier", "category")

    def get_serializer_class(self):
        """Based on Action"""
        if self.action in ['retrieve']:
            return ProductDetailSerializer
        else:
            return ProductSerializer

    queryset = Product.objects.all()

    @action(detail=False, methods=['get'], url_path='filters')
    def get_filters(self, request, *args, **kwargs):
        categories = Category.objects.filter(products__isnull=False).distinct()
        brands = Company.objects.filter(products__isnull=False).distinct()

        brands_serialized = BrandSerializer(brands, many=True).data
        categories_serialized = CategorySerializer(categories, many=True).data

        data = [
            {'id': 'suppliers',
             'name': 'Marcas',
             'options': brands_serialized,
             },
            {'id': 'categories',
             'name': 'Categorías',
             'options': categories_serialized,
             },
        ]

        return Response(data, status=status.HTTP_200_OK)
