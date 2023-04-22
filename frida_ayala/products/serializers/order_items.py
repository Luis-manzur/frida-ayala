"""product order items Serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.products.models import OrderItem
# Serializers
from frida_ayala.products.serializers.products import ProductSerializer


class OrderItemCreateModelSerializer(serializers.ModelSerializer):
    """ Order Item Model Serializer"""

    class Meta:
        model = OrderItem
        exclude = ['created', 'modified', 'order', ]


class OrderItemModelSerializer(serializers.ModelSerializer):
    """ Order Item Model Serializer"""
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        exclude = ['created', 'modified', 'order', ]
