"""Sizes serializer"""

# Drf
from rest_framework import serializers

# Models
from frida_ayala.products.models import Size


class SizeSerializer(serializers.ModelSerializer):
    """Size model serializer"""

    class Meta:
        model = Size
        fields = ['name', 'stock', 'id']
