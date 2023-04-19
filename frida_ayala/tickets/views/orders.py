"""Orders Views"""

# Django
from django.views.generic import TemplateView
# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Models
from frida_ayala.tickets.models.orders import Order
# Serializers
from frida_ayala.tickets.serializers.orders import OrderCreateSerializer, OrderModelSerializer, VerifyTicketSerializer
from frida_ayala.tickets.serializers.ticket_orders import TicketOrderModelSerializer
# Permissions
from frida_ayala.utils.permissions import IsObjectOwner, IsStaff


class OrderViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """Order View Set"""

    # serializer_class = OrderCreateSerializer

    def get_serializer_class(self):
        """Assign serializer based on action"""
        if self.action in ['create']:
            return OrderCreateSerializer
        elif self.action in ['verify_ticket']:
            return VerifyTicketSerializer
        else:
            return OrderModelSerializer

    def get_queryset(self):
        return Order.objects.all()

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['create']:
            permissions = [IsAuthenticated]

        elif self.action in ['verify_ticket']:
            permissions = [IsAuthenticated, IsStaff]
        else:
            permissions = [IsAuthenticated, IsObjectOwner]

        return [p() for p in permissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        data = OrderModelSerializer(order).data
        return Response(data)

    @action(detail=False, methods=['post'], url_path='verify-ticket')
    def verify_ticket(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save()
        data = TicketOrderModelSerializer(ticket).data
        return Response(data)


class QReadeTemplateView(TemplateView):
    template_name = 'tickets/qr_reader.html'
