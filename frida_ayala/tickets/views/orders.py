"""Orders Views"""
# Utils
from io import BytesIO

# Django
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views.generic import TemplateView
# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
# xhtml2pdf
from xhtml2pdf import pisa

# Models
from frida_ayala.tickets.models import Order, OrderTicket
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
        elif self.action in ['download_pdf']:
            return None
        else:
            return OrderModelSerializer

    def get_queryset(self):
        return Order.objects.all()

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['create']:
            permissions = [IsAuthenticated]

        elif self.action in ['download_pdf']:
            permissions = [AllowAny]

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

    @action(detail=False, methods=['get'], url_path='download-ticket/(?P<code>[^/.]+)')
    def download_pdf(self, request, *args, **kwargs):
        ticket = get_object_or_404(OrderTicket, code=self.kwargs['code'])
        template = get_template('pdfs/qr.html')
        html = template.render({'ticket': ticket})
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None


class QReadeTemplateView(TemplateView):
    template_name = 'tickets/qr_reader.html'
