"""Products serializer"""

# Drf
from rest_framework import serializers

# Models
from frida_ayala.products.models import Product
# Serializers
from frida_ayala.products.serializers.sizes import SizeSerializer


class ProductSerializer(serializers.ModelSerializer):
    """Product model serializer"""

    class Meta:
        model = Product
        exclude = ['modified', 'created', 'supplier']


class ProductDetailSerializer(serializers.ModelSerializer):
    """Product detail Model serializer"""
    sizes = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        exclude = ['modified', 'created', 'supplier']
