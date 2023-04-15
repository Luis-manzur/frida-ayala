"""Movies Views"""
# Django filters
from django_filters.rest_framework import DjangoFilterBackend
# DRF
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter

# Models
from frida_ayala.events.models.movies import Movie
# Serializer
from frida_ayala.events.serializers import MovieModelSerializer


class MovieViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """Movie view set.
        Handle Movies list and retrieve.
        """
    serializer_class = MovieModelSerializer
    lookup_field = 'slug_name'

    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    ordering_fields = ('-created', 'created')
    ordering = ('-created',)

    def get_queryset(self):
        return Movie.objects.filter(show=self.kwargs['show_pk'])
