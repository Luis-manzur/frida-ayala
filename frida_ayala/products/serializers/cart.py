"""Cart serializer"""

# Django REST Framework
from rest_framework import serializers

# Model
from frida_ayala.products.models import Cart, CartItem
# Serializers
from frida_ayala.products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    size = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity', 'size')

    def get_size(self, obj: CartItem):
        return obj.size.name


class CartModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    products = CartItemSerializer(many=True, read_only=True, source='cartitem_set')
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        exclude = ['created', 'modified']

    def get_total(self, obj: Cart):
        total = 0
        cart_items = CartItem.objects.filter(cart=obj)
        for cart_item in cart_items:
            total += cart_item.quantity * cart_item.product.price
        return total


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['size', 'quantity', 'product']

    def validate_size(self, data):
        user = self.context['user']
        cart, response = Cart.objects.get_or_create(user=user)
        self.context['cart'] = cart
        if cart.cartitem_set.filter(size=data).exists():
            raise serializers.ValidationError('The product with this size has been already added to the cart.')
        return data

    def validate(self, data):
        if data['size'].stock < data['quantity']:
            raise serializers.ValidationError('The quantity is greater than the product stock.')
        return data

    def create(self, data):
        cart = self.context['cart']
        data['cart'] = cart
        cart_item = CartItem.objects.create(**data)

        return cart_item
