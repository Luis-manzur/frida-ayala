"""Venues Views"""
# Django filters
from django_filters.rest_framework import DjangoFilterBackend
# DRF
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter

# Models
from frida_ayala.locations.models import Venue
# Serializer
from frida_ayala.locations.serializers import VenueModelSerializer


class VenueViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """Venue view set.
        Handle Venues list and retrieve.
        """
    queryset = Venue.objects.all()
    serializer_class = VenueModelSerializer

    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'municipality')
    ordering_fields = ('capacity', '-created', 'created')
    ordering = ('-created',)
