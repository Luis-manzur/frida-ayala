"""Profile serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    class Meta:
        """Meta class."""

        model = Profile
        exclude = ['created', 'modified', 'user']
