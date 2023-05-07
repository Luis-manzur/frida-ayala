"""Product orders"""

from django.forms.models import model_to_dict
# Django REST Framework
from rest_framework import serializers

from frida_ayala.payments.serializers.payments import PaymentCreateSerializer
# Models
from frida_ayala.products.models import ProductOrder, Cart, CartItem, OrderItem, Product
# Serializers
from frida_ayala.products.serializers.order_items import OrderItemModelSerializer


# Tasks


class ProductOrderCreateSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    payment = PaymentCreateSerializer()

    def validate_cart(self, data):
        cart_items = CartItem.objects.filter(cart=data)
        if len(cart_items) == 0:
            raise serializers.ValidationError('Cart is empty')
        self.context['cart_items'] = cart_items
        return data

    def create(self, data):
        cart_items = self.context['cart_items']
        cart = data.pop('cart')
        cart.delete()
        payment = data.pop('payment')
        order = ProductOrder(**data)
        order.save()
        for cart_item in cart_items:
            cart_item = model_to_dict(cart_item)
            cart_item.pop('id')
            cart_item.pop('cart')
            cart_item['product'] = Product.objects.get(pk=cart_item['product'])
            cart_item['order'] = order
            order_item = OrderItem(**cart_item)
            order_item.save()

        return data


class ProductOrderModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    products = OrderItemModelSerializer(many=True, read_only=True, source='order_set')

    class Meta:
        model = ProductOrder
        exclude = ['created', 'modified']
