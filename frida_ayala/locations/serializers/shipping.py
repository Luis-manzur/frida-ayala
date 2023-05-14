"""Shipping Serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.locations.models import Shipping


class ShippingModelSerializer(serializers.ModelSerializer):
    """Shipping model serializer."""

    class Meta:
        model = Shipping
        exclude = ['created', 'modified']
