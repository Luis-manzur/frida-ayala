"""Tickets views"""
# Django
from django_filters.rest_framework import DjangoFilterBackend
# DRF
from rest_framework import viewsets, mixins

# Models
from frida_ayala.tickets.models import Ticket
# Serializers
from frida_ayala.tickets.serializers.tickets import TicketSerializer


class TicketsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Ticket.objects.all()

    # Filter The Tickets By event
    filter_backends = [DjangoFilterBackend]
    search_fields = ['event']

    serializer_class = TicketSerializer
