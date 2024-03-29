"""Product orders"""

import logging

from django.forms.models import model_to_dict
# Django REST Framework
from rest_framework import serializers

from frida_ayala.locations.models import Delivery, Shipping
from frida_ayala.locations.serializers import ShippingModelSerializer, DeliveryModelSerializer
from frida_ayala.payments.models import Payment
from frida_ayala.payments.serializers.payments import PaymentCreateSerializer, make_payment, PaymentModelSerializer
# Models
from frida_ayala.products.models import ProductOrder, Cart, CartItem, OrderItem, Product, Size
# Serializers
from frida_ayala.products.serializers.order_items import OrderItemModelSerializer

logger = logging.getLogger('console')


class ProductOrderCreateSerializer(serializers.Serializer):
    PAYMENT_CHOICES = (
        ('CARD', 'Debit/Credit card'),
        ('CASH', 'Cash'),
    )
    SHIPPING_CHOICES = (
        ('DELIVERY', 'Delivery'),
        ('MRW', 'MRW'),
    )

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    payment_method = serializers.ChoiceField(choices=PAYMENT_CHOICES, default='CARD')
    shipping_method = serializers.ChoiceField(choices=SHIPPING_CHOICES, default='DELIVERY')
    payment = PaymentCreateSerializer(required=False)
    shipping = ShippingModelSerializer(required=False)
    delivery = DeliveryModelSerializer(required=False)

    def validate_cart(self, data):
        cart_items = CartItem.objects.filter(cart=data)
        if len(cart_items) == 0:
            raise serializers.ValidationError('Cart is empty')
        self.context['cart_items'] = cart_items
        return data

    def validate_delivery(self, obj):
        shipping_method = self.initial_data['shipping_method']
        if shipping_method == 'DELIVERY' and obj == None:
            raise serializers.ValidationError('Delivery data must be completed')
        return obj

    def validate_shipping(self, data):
        shipping_method = self.initial_data['shipping_method']
        if shipping_method == 'MRW' and data == None:
            raise serializers.ValidationError('shipping data must be completed')

    def validate_payment(self, obj):
        payment_method = self.initial_data['payment_method']
        if payment_method == 'CARD':
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
        return obj

    def create(self, data):
        cart_items = self.context['cart_items']
        cart = data.pop('cart')
        cart.delete()
        if data.get('payment'):
            payment = data.pop('payment')
        if data.get('delivery'):
            delivery_data = data.pop('delivery')
            delivery = Delivery.objects.create(**delivery_data)
            delivery.save()
            data['delivery'] = delivery

        if data.get('shipping'):
            shipping_data = data.pop('shipping')
            shipping = Shipping.objects.create(**shipping_data)
            shipping.save()
            data['shipping'] = shipping

        order = ProductOrder(**data)
        order.save()
        for cart_item in cart_items:
            cart_item = model_to_dict(cart_item)
            cart_item.pop('id')
            cart_item.pop('cart')
            cart_item['product'] = Product.objects.get(pk=cart_item['product'])
            cart_item['size'] = Size.objects.get(pk=cart_item['size'])
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
