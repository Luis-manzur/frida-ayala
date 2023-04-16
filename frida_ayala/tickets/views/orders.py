"""Orders Views"""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Models
from frida_ayala.tickets.models.orders import Order
# Serializers
from frida_ayala.tickets.serializers.orders import OrderCreateSerializer, OrderModelSerializer
# Permissions
from frida_ayala.utils.permissions import IsObjectOwner


class OrderViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """Order View Set"""

    # serializer_class = OrderCreateSerializer

    def get_serializer_class(self):
        """Assign serializer based on action"""
        if self.action in ['create']:
            return OrderCreateSerializer
        else:
            return OrderModelSerializer

    def get_queryset(self):
        return Order.objects.all()

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['create']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated, IsObjectOwner]

        return [p() for p in permissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        data = OrderModelSerializer(order).data
        return Response(data)
