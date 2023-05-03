"""Cart serializer"""

# Django REST Framework
from rest_framework import serializers

# Model
from frida_ayala.products.models import Cart, CartItem
# Serializers
from frida_ayala.products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity')


class CartModelSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    products = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        exclude = ['created', 'modified']
