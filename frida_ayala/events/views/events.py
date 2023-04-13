"""Events Views"""
# Django filters
from django_filters.rest_framework import DjangoFilterBackend
# DRF
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter

# Models
from frida_ayala.events.models import Event
# Serializer
from frida_ayala.events.serializers import EventModelSerializer


class EventViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """Event view set.
        Handle Events list and retrieve.
        """
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer
    lookup_field = 'slug_name'

    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    ordering_fields = ('capacity', '-created', 'created')
    ordering = ('-created',)
