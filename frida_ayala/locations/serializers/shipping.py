"""Shipping Serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.locations.models import Shipping, Delivery


class ShippingModelSerializer(serializers.ModelSerializer):
    """Shipping model serializer."""

    class Meta:
        model = Shipping
        exclude = ['created', 'modified']


class DeliveryModelSerializer(serializers.ModelSerializer):
    """Delivery model serializer."""

    class Meta:
        model = Delivery
        exclude = ['created', 'modified']
