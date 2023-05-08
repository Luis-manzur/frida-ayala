"""Brand Views"""

# Django REST Framework
from rest_framework import viewsets, mixins

# Models
from frida_ayala.companies.models import Company
# Serializers
from frida_ayala.products.serializers import BrandSerializer


class BrandViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Company.objects.filter(products__isnull=False).distinct()
    serializer_class = BrandSerializer

    
