"""Cart Views"""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Models
from frida_ayala.products.models import Cart
# Serializers
from frida_ayala.products.serializers.cart import CartModelSerializer, AddToCartSerializer, CartItemSerializer
# Permissions
from frida_ayala.utils.permissions import IsObjectOwner


class CartViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """Cart View Set"""

    lookup_field = 'user__username'

    def get_serializer_class(self):
        if self.action == 'add_to_cart':
            return AddToCartSerializer
        else:
            return CartModelSerializer

    def get_queryset(self):
        return Cart.objects.all()

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['add_to_cart']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated, IsObjectOwner]

        return [p() for p in permissions]

    @action(detail=False, methods=['post'], url_path='add-to-cart')
    def add_to_cart(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.context['user'] = request.user
        serializer.is_valid(raise_exception=True)
        cart_item = serializer.save()
        data = CartItemSerializer(cart_item).data
        return Response(data)
