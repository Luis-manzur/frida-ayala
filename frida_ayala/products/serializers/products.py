"""Products serializer"""

# Drf
from rest_framework import serializers

# Models
from frida_ayala.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Ticket model serializer"""

    class Meta:
        model = Product
        exclude = ['modified', 'created', 'stock', 'supplier']
