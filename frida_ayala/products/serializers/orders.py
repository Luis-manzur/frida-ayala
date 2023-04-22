"""Product orders"""

# Django REST Framework
from rest_framework import serializers

from frida_ayala.payments.serializers.payments import PaymentCreateSerializer
# Models
from frida_ayala.products.models import OrderItem, ProductOrder
# Serializers
from frida_ayala.products.serializers.order_items import OrderItemModelSerializer, OrderItemCreateModelSerializer
# Tasks
from frida_ayala.tickets.tasks import send_ticket_purchase_email_user


class ProductOrderCreateSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    products = serializers.ListField(child=OrderItemCreateModelSerializer())
    payment = PaymentCreateSerializer()

    def create(self, data):
        products_data = data.pop('products')
        payment = data.pop('payment')
        order = ProductOrder(**data)
        order.save()
        for product_data in products_data:
            product_data['order'] = order
            product = OrderItem.objects.create(**product_data)
            product.save()

        send_ticket_purchase_email_user.delay(order.code)
        return order


class ProductOrderModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    products = OrderItemModelSerializer(many=True, read_only=True, source='order_set')

    class Meta:
        model = ProductOrder
        exclude = ['created', 'modified']
