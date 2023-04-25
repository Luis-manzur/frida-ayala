"""Sponsors Views"""
# Django filters
from django_filters.rest_framework import DjangoFilterBackend
# DRF
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter

# Models
from frida_ayala.events.models import Sponsor
# Serializer
from frida_ayala.events.serializers import SponsorModelSerializer


class SponsorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """EventDay view set.
        Handle EventDays list and retrieve.
        """
    serializer_class = SponsorModelSerializer

    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    ordering_fields = ('capacity', '-created', 'created')
    ordering = ('-created',)

    def get_queryset(self):
        return Sponsor.objects.filter(event__slug_name=self.kwargs['event_slug_name'])
