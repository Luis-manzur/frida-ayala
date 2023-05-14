"""Orders Views"""

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Models
from frida_ayala.products.models import ProductOrder
# Serializers
from frida_ayala.products.serializers.orders import ProductOrderCreateSerializer, ProductOrderModelSerializer
# Permissions
from frida_ayala.utils.permissions import IsObjectOwner


class ProductOrderViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin):
    """Order View Set"""

    def get_serializer_class(self):
        """Assign serializer based on action"""
        if self.action in ['create']:
            return ProductOrderCreateSerializer
        else:
            return ProductOrderModelSerializer

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user)

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
        data = ProductOrderModelSerializer(order).data
        return Response(data, status=status.HTTP_201_CREATED)
