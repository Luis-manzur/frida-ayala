"""Movies serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.events.models.movies import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    """Movie model serializer."""

    class Meta:
        model = Movie
        exclude = ['created', 'modified', 'show']
