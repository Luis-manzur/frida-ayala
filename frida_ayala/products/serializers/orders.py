"""Product orders"""

import logging

from django.forms.models import model_to_dict
# Django REST Framework
from rest_framework import serializers

from frida_ayala.locations.serializers import ShippingModelSerializer
from frida_ayala.payments.models import Payment
from frida_ayala.payments.serializers.payments import PaymentCreateSerializer, make_payment, PaymentModelSerializer
# Models
from frida_ayala.products.models import ProductOrder, Cart, CartItem, OrderItem, Product
# Serializers
from frida_ayala.products.serializers.order_items import OrderItemModelSerializer

logger = logging.getLogger('console')


class ProductOrderCreateSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    payment = PaymentCreateSerializer()
    shipping = ShippingModelSerializer()

    def validate_cart(self, data):
        cart_items = CartItem.objects.filter(cart=data)
        if len(cart_items) == 0:
            raise serializers.ValidationError('Cart is empty')
        self.context['cart_items'] = cart_items
        return data

    def validate_payment(self, obj):
        cart_valid = False
        try:
            self.validate_cart(self.initial_data['cart'])
            cart_valid = True
        except:
            return obj
        if cart_valid:
            transaction_response = make_payment(obj)
            if not transaction_response:
                logger.error('Transaction error. Communication error')
                raise serializers.ValidationError("Transaction error, try again later.")
            data = {
                'card': obj['card'][-4:],
                'reference': transaction_response.get('referencia'),
                'amount': obj['amount'],
                'status': 'A' if transaction_response['ok'] else 'F',
                'code': transaction_response['codigo']
            }

            payment = Payment.objects.create(**data)
            payment.save()
            if transaction_response['ok']:
                logger.info(f'Transaction success {transaction_response["referencia"]}')
                return obj
            else:
                logger.info(
                    f'Transaction error {transaction_response["referencia"]}: {transaction_response["respuesta_data"]}')
                raise serializers.ValidationError(transaction_response['respuesta_data'])

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
        return order


class ProductOrderModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    products = OrderItemModelSerializer(many=True, read_only=True, source='orderitem_set')
    payments = PaymentModelSerializer(read_only=True)
    shipping = ShippingModelSerializer(read_only=True)

    class Meta:
        model = ProductOrder
        exclude = ['created', 'modified']
